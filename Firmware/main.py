from time import ticks_ms, ticks_diff, sleep_ms
from machine import Pin, TouchPad, SoftI2C, UART
from jq6500 import Player
import neopixel
import network
import socket
import ujson
import gc

# =========================================================
# CONFIG
# =========================================================

# --- audio player
p = Player(port=2)
p.set_volume(30)

# --- touch input
TOUCH_PIN = 4
tp = TouchPad(Pin(TOUCH_PIN))

# --- RTC / I2C
I2C_SDA = 21
I2C_SCL = 22
RTC_ADDR = 0x68
RTC_ENABLED = True

# --- NeoPixel
NEO_PIN = 27
NUM_PIXELS = 24
LED_BRIGHTNESS = 0.4
PULSE_PERIOD_MS = 2200
LED_UPDATE_MS = 15

# --- touch tunables
A = 0.2
ON = 0.93
OFF = 0.96
DB_ON = 100
DB_OFF = 100
DRIFT = 0.01
RESTART = 5_000
PRINT_EVERY = 1000

# --- loop timing
LOOP_MS = 10

# --- logging
ENABLE_LOGGING = True
LOG_PATH = "touch_log.csv"
FLUSH_EVERY = 20
SAFETY_FLUSH_MS = 5_000

# --- dashboard / Wi-Fi AP
AP_SSID = "HelpingHand01"
AP_PASSWORD = "handtouch"
HTTP_PORT = 80
RECENT_EVENTS_MAX = 20
PLACEHOLDER_BATTERY_V = 3.92

# --- rolling stats
ROLLING_TOUCH_COUNT = 20

# --- housekeeping
GC_EVERY_MS = 10_000
HTTP_RECV_SIZE = 1024
HTTP_CLIENT_TIMEOUT = 0.15
HTTP_BACKLOG = 4
MAX_HTTP_PER_LOOP = 3

# =========================================================
# RTC HELPERS
# =========================================================

i2c = None
if RTC_ENABLED:
    i2c = SoftI2C(scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=100000)

def bcd_to_dec(b):
    return ((b >> 4) * 10) + (b & 0x0F)

def dec_to_bcd(d):
    return ((d // 10) << 4) | (d % 10)

def rtc_read_datetime():
    if not RTC_ENABLED or i2c is None:
        raise OSError("RTC disabled")
    data = i2c.readfrom_mem(RTC_ADDR, 0x00, 7)
    second = bcd_to_dec(data[0] & 0x7F)
    minute = bcd_to_dec(data[1] & 0x7F)
    hour = bcd_to_dec(data[2] & 0x3F)
    weekday = bcd_to_dec(data[3] & 0x07)
    day = bcd_to_dec(data[4] & 0x3F)
    month = bcd_to_dec(data[5] & 0x1F)
    year = 2000 + bcd_to_dec(data[6])
    return (year, month, day, hour, minute, second, weekday)

def rtc_set_datetime(year, month, day, hour, minute, second, weekday=1):
    if not RTC_ENABLED or i2c is None:
        raise OSError("RTC disabled")
    data = bytes([
        dec_to_bcd(second), dec_to_bcd(minute), dec_to_bcd(hour),
        dec_to_bcd(weekday), dec_to_bcd(day), dec_to_bcd(month),
        dec_to_bcd(year - 2000),
    ])
    i2c.writeto_mem(RTC_ADDR, 0x00, data)

def rtc_iso_string():
    if not RTC_ENABLED:
        return "RTC_DISABLED"
    try:
        y, mo, d, h, mi, s, wd = rtc_read_datetime()
        return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(y, mo, d, h, mi, s)
    except Exception as e:
        print("RTC read error:", e)
        return "RTC_ERROR"

def rtc_epoch_seconds():
    if not RTC_ENABLED:
        return None
    try:
        y, mo, d, h, mi, s, wd = rtc_read_datetime()
    except Exception as e:
        print("RTC read error:", e)
        return None
    mdays = [31,28,31,30,31,30,31,31,30,31,30,31]
    mdays_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
    def is_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days = 0
    for yr in range(2000, y):
        days += 366 if is_leap(yr) else 365
    month_days = mdays_leap if is_leap(y) else mdays
    for m in range(1, mo):
        days += month_days[m - 1]
    days += (d - 1)
    return days * 86400 + h * 3600 + mi * 60 + s

# =========================================================
# GENERAL HELPERS
# =========================================================

def format_uptime(ms):
    total_s = ms // 1000
    days = total_s // 86400
    total_s %= 86400
    hours = total_s // 3600
    total_s %= 3600
    mins = total_s // 60
    secs = total_s % 60
    return "{}d {}h {}m {}s".format(days, hours, mins, secs)

def format_duration_ms(ms):
    return "{:.2f} s".format(ms / 1000)

def get_state_string(playing, touch_active, armed):
    if playing: return "playing"
    if touch_active: return "touched"
    if armed: return "armed"
    return "idle"

# =========================================================
# NEOPIXEL HELPERS
# =========================================================

np = neopixel.NeoPixel(Pin(NEO_PIN, Pin.OUT), NUM_PIXELS)
_last_led = None
last_led_update = 0

def scale8(x, brightness):
    v = int(x * brightness)
    if v < 0: return 0
    if v > 255: return 255
    return v

def set_all(r, g, b):
    global _last_led
    rr = scale8(r, LED_BRIGHTNESS)
    gg = scale8(g, LED_BRIGHTNESS)
    bb = scale8(b, LED_BRIGHTNESS)
    rgb = (rr, gg, bb)
    if _last_led == rgb:
        return
    for i in range(NUM_PIXELS):
        np[i] = rgb
    np.write()
    _last_led = rgb

def leds_off():
    set_all(0, 0, 0)

def pulse_blue(now_ms):
    phase = now_ms % PULSE_PERIOD_MS
    half = PULSE_PERIOD_MS // 2
    x = (phase / half) if phase < half else ((PULSE_PERIOD_MS - phase) / half)
    eased = x * x * (3.0 - 2.0 * x)
    level = 16 + int(239 * eased)
    set_all(0, level // 6, level)

def update_leds(now_ms, active, client_connected):
    global last_led_update
    if ticks_diff(now_ms, last_led_update) < LED_UPDATE_MS:
        return
    last_led_update = now_ms
    if active:
        # Playing or touch active - blue pulse takes priority
        pulse_blue(now_ms)
    elif client_connected:
        # Steady dim warm white to indicate a device is connected
        set_all(40, 30, 10)
    else:
        leds_off()

def _hsv_to_rgb(h, s, v):
    """Convert HSV (0-255 each) to RGB tuple."""
    if s == 0:
        return (v, v, v)
    h6 = (h * 6) >> 8
    f  = (h * 6) & 0xFF
    p  = (v * (255 - s)) >> 8
    q  = (v * (255 - (s * f >> 8))) >> 8
    t  = (v * (255 - (s * (255 - f) >> 8))) >> 8
    if h6 == 0: return (v, t, p)
    if h6 == 1: return (q, v, p)
    if h6 == 2: return (p, v, t)
    if h6 == 3: return (p, q, v)
    if h6 == 4: return (t, p, v)
    return (v, p, q)

def play_connect_effect():
    """
    Blocking rainbow chase for ~2 s when a client connects.
    Rotates the full hue wheel around the ring twice.
    Ends by settling into steady warm white (client connected indicator).
    """
    DURATION_MS = 2000
    STEP_MS     = 20
    steps       = DURATION_MS // STEP_MS
    for i in range(steps):
        offset = (i * 256 // steps) & 0xFF
        for j in range(NUM_PIXELS):
            hue = (offset + j * 256 // NUM_PIXELS) & 0xFF
            r, g, b = _hsv_to_rgb(hue, 220, 180)
            np[j] = (scale8(r, LED_BRIGHTNESS),
                     scale8(g, LED_BRIGHTNESS),
                     scale8(b, LED_BRIGHTNESS))
        np.write()
        sleep_ms(STEP_MS)
    # Settle into steady warm white — client is still connected
    set_all(40, 30, 10)

def play_armed_effect():
    """
    Blocking pink slow-pulse effect for entering armed state (~1.8 s).
    Pink = high red, medium blue, no green.
    One full breathe-in / breathe-out cycle using smoothstep easing.
    LEDs go dark at the end (armed idle = off).
    """
    STEPS = 60
    STEP_MS = 15
    for i in range(STEPS):
        x = i / (STEPS - 1)
        # smoothstep up then down
        if x < 0.5:
            t = x * 2
        else:
            t = (1.0 - x) * 2
        eased = t * t * (3.0 - 2.0 * t)
        level = int(255 * eased)
        r = level
        g = level // 8          # slight warmth
        b = level // 2          # pink-purple tint
        for j in range(NUM_PIXELS):
            np[j] = (scale8(r, LED_BRIGHTNESS),
                     scale8(g, LED_BRIGHTNESS),
                     scale8(b, LED_BRIGHTNESS))
        np.write()
        sleep_ms(STEP_MS)
    leds_off()

# =========================================================
# LOGGING
# =========================================================

BOOT = ticks_ms()
_log_buf = []
_buf_count = 0
next_flush = BOOT + SAFETY_FLUSH_MS

def ensure_log_header():
    if not ENABLE_LOGGING:
        return
    try:
        with open(LOG_PATH, "r") as f:
            header = f.readline().strip()
            expected = "touch_id,rtc_start,uptime_start_ms,duration_ms,min_ema,armed"
            if header != expected:
                print("WARNING: existing log header differs from expected.")
    except OSError:
        with open(LOG_PATH, "w") as f:
            f.write("touch_id,rtc_start,uptime_start_ms,duration_ms,min_ema,armed\n")

def flush_log():
    global _buf_count
    if (not ENABLE_LOGGING) or (not _log_buf):
        return
    try:
        with open(LOG_PATH, "a") as f:
            f.write("".join(_log_buf))
        _log_buf.clear()
        _buf_count = 0
    except OSError as e:
        print("LOG WRITE ERROR:", e)

def log_touch_event(touch_id, rtc_start, uptime_start_ms, dur_ms, min_ema, armed_flag):
    global _buf_count
    if not ENABLE_LOGGING:
        return
    _log_buf.append("{},{},{},{},{},{}\n".format(
        touch_id, rtc_start, uptime_start_ms, dur_ms, int(min_ema),
        1 if armed_flag else 0
    ))
    _buf_count += 1
    if _buf_count >= FLUSH_EVERY:
        flush_log()

# =========================================================
# AUDIO HELPERS
#
# Key facts about the JQ6500 flash (16P) module:
#   - Flash module never truly "stops" - it goes to PAUSED after a track ends.
#   - p.play() (cmd 0x0D) resumes from paused, which means it restarts
#     from the beginning when the track has finished (position resets).
#   - play_by_index is unreliable from paused/stopped state on flash.
#   - The uart.read() flush inside write_bytes in jq6500.py can leave
#     the UART dirty if called too quickly after a previous command.
#     We flush the UART ourselves before issuing play to stay clean.
# =========================================================

# Raw JQ6500 command frames (bypasses library's uart.read() flush
# which can misalign timing when the module has sent back unsolicited
# status bytes after a track finishes).
_CMD_PLAY      = bytes([0x7E, 0x02, 0x0D, 0xEF])  # resume/play
_CMD_RESET     = bytes([0x7E, 0x02, 0x0C, 0xEF])  # soft reset
_CMD_VOL_30    = bytes([0x7E, 0x03, 0x06, 0x1E, 0xEF])  # volume 30
_CMD_SRC_FLASH = bytes([0x7E, 0x03, 0x09, 0x04, 0xEF])  # source = builtin flash
_CMD_PLAY_IDX2 = bytes([0x7E, 0x04, 0x03, 0x00, 0x02, 0xEF])  # play index 2
_CMD_PLAY_IDX3 = bytes([0x7E, 0x04, 0x03, 0x00, 0x03, 0xEF])  # play index 3

def _uart_drain():
    """
    Properly drain the JQ6500 RX buffer.
    Wait long enough for any in-flight bytes to arrive, then read them all.
    Unlike the library's uart.read() with no args (returns immediately),
    this actually waits for the bus to go quiet.
    """
    sleep_ms(120)
    while p.uart.any():
        p.uart.read()
        sleep_ms(20)

def _raw_write(cmd):
    """Send a raw command frame, bypassing the library's flush-then-write."""
    p.uart.write(cmd)

def reset_track():
    """
    Restart track 1 on the JQ6500 flash module from a clean state.

    Problem: after a track ends naturally the module sends unsolicited
    status bytes. The library's write_bytes() does uart.read() before
    every command, but with no length/timeout this only drains what's
    already arrived — if bytes are still in flight it grabs a partial
    frame and the next command gets dropped silently.

    Solution:
      1. Drain properly (wait + read loop)
      2. Soft-reset the module to guarantee a known state
      3. Wait for reset to complete (500 ms per datasheet)
      4. Re-set source to builtin flash and volume
      5. Send play
    """
    print("DBG reset_track: draining UART")
    _uart_drain()

    print("DBG reset_track: sending soft reset")
    _raw_write(_CMD_RESET)
    sleep_ms(600)          # datasheet says wait ~500 ms after reset

    print("DBG reset_track: setting source + volume")
    _raw_write(_CMD_SRC_FLASH)
    sleep_ms(200)
    _raw_write(_CMD_VOL_30)
    sleep_ms(100)

    print("DBG reset_track: sending play")
    _raw_write(_CMD_PLAY)
    print("DBG reset_track: done")

def play_track_once(cmd):
    """
    Play a specific track by raw index command, bypassing the library.
    Used for effect tracks (armed = track 2, connect = track 3) that
    should play once and leave the module in a known paused state.
    Drains UART first, sends cmd, no wait — caller decides timing.
    """
    _uart_drain()
    _raw_write(_CMD_SRC_FLASH)
    sleep_ms(100)
    _raw_write(_CMD_VOL_30)
    sleep_ms(50)
    _raw_write(cmd)

# =========================================================
# RECENT EVENTS
# =========================================================

recent_events = []

def add_event(msg):
    stamp = rtc_iso_string()
    line = "{} | {}".format(stamp, msg)
    recent_events.append(line)
    if len(recent_events) > RECENT_EVENTS_MAX:
        recent_events.pop(0)
    print("EVENT:", line)

# =========================================================
# DASHBOARD / STATS HELPERS
# =========================================================

recent_touch_durations = []
touch_timestamps_24h = []
audio_play_count = 0
last_touch_time = "Never"

def add_touch_duration(dur_ms):
    recent_touch_durations.append(dur_ms)
    if len(recent_touch_durations) > ROLLING_TOUCH_COUNT:
        recent_touch_durations.pop(0)

def get_avg_touch_duration_ms():
    if not recent_touch_durations:
        return None
    return sum(recent_touch_durations) / len(recent_touch_durations)

def update_24h_touch_window():
    if not RTC_ENABLED:
        return None
    now_s = rtc_epoch_seconds()
    if now_s is None:
        return None
    cutoff = now_s - 86400
    while touch_timestamps_24h and touch_timestamps_24h[0] < cutoff:
        touch_timestamps_24h.pop(0)
    return len(touch_timestamps_24h)

def add_touch_timestamp_24h():
    if not RTC_ENABLED:
        return
    now_s = rtc_epoch_seconds()
    if now_s is None:
        return
    touch_timestamps_24h.append(now_s)
    update_24h_touch_window()

def get_touches_24h_display():
    count = update_24h_touch_window()
    if count is None:
        return "N/A"
    return count

def get_clients_connected():
    try:
        stations = ap.status("stations")
        if not stations:
            return 0
        return len(stations)
    except Exception as e:
        print("stations error:", e)
        return 0

# =========================================================
# DASHBOARD HTML
# =========================================================

def dashboard_html():
    return """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Helping Hand</title>
<style>
body{{font-family:Arial,sans-serif;margin:0;padding:16px;background:#f4f4f4;color:#111}}
h1{{margin-top:0;font-size:1.4rem}}
.card{{background:#fff;border:1px solid #ddd;border-radius:10px;padding:14px;margin-bottom:12px}}
.row{{display:flex;justify-content:space-between;gap:12px;padding:6px 0;border-bottom:1px solid #eee}}
.row:last-child{{border-bottom:none}}
.label{{color:#555}}.value{{font-weight:bold;text-align:right}}
pre{{white-space:pre-wrap;word-wrap:break-word;font-size:0.9rem;margin:0}}
.btn{{display:inline-block;padding:10px 14px;border-radius:8px;border:1px solid #111;text-decoration:none;color:#111;margin-right:8px}}
.small{{color:#666;font-size:0.9rem}}.section-title{{font-weight:bold;margin-bottom:8px}}
.err{{color:#a00;font-size:0.9rem;margin-top:6px}}
</style>
</head>
<body>
<h1>Helping Hand 01</h1>
<div class="small">AP: <b>{ssid}</b> &nbsp;|&nbsp; IP: <b>{ip}</b></div>
<div class="card">
  <div class="section-title">Status</div>
  <div class="row"><div class="label">RTC</div><div class="value" id="rtc">-</div></div>
  <div class="row"><div class="label">State</div><div class="value" id="state">-</div></div>
  <div class="row"><div class="label">Battery</div><div class="value" id="battery_v">-</div></div>
  <div class="row"><div class="label">Uptime</div><div class="value" id="uptime">-</div></div>
  <div class="row"><div class="label">Clients</div><div class="value" id="clients_connected">-</div></div>
</div>
<div class="card">
  <div class="section-title">Activity</div>
  <div class="row"><div class="label">Touches logged</div><div class="value" id="touch_count">-</div></div>
  <div class="row"><div class="label">Touches 24h</div><div class="value" id="touches_24h">-</div></div>
  <div class="row"><div class="label">Avg duration</div><div class="value" id="avg_touch_duration">-</div></div>
  <div class="row"><div class="label">Audio plays</div><div class="value" id="audio_play_count">-</div></div>
  <div class="row"><div class="label">Last touch</div><div class="value" id="last_touch_time">-</div></div>
</div>
<div class="card">
  <div class="section-title">Diagnostics</div>
  <div class="row"><div class="label">Ratio</div><div class="value" id="ratio">-</div></div>
  <div class="row"><div class="label">Buf rows</div><div class="value" id="buf">-</div></div>
  <div class="err" id="err"></div>
</div>
<div class="card">
  <a class="btn" href="/log.csv">Download CSV</a>
  <a class="btn" href="/" onclick="location.reload();return false;">Refresh</a>
</div>
<div class="card">
  <div class="section-title">Recent events</div>
  <pre id="recent">Connecting...</pre>
</div>
<script>
async function tick(){{
  try{{
    const r=await fetch('/api',{{cache:'no-store'}});
    if(!r.ok)throw new Error('HTTP '+r.status);
    const d=await r.json();
    document.getElementById('rtc').textContent=d.rtc;
    document.getElementById('state').textContent=d.state;
    document.getElementById('battery_v').textContent=d.battery_v+' V';
    document.getElementById('uptime').textContent=d.uptime;
    document.getElementById('clients_connected').textContent=d.clients_connected;
    document.getElementById('touch_count').textContent=d.touch_count;
    document.getElementById('touches_24h').textContent=d.touches_24h;
    document.getElementById('avg_touch_duration').textContent=d.avg_touch_duration;
    document.getElementById('audio_play_count').textContent=d.audio_play_count;
    document.getElementById('last_touch_time').textContent=d.last_touch_time;
    document.getElementById('ratio').textContent=d.ratio;
    document.getElementById('buf').textContent=d.buf_count;
    document.getElementById('recent').textContent=d.events.join('\\n')||'No events yet';
    document.getElementById('err').textContent='';
  }}catch(e){{document.getElementById('err').textContent='API error: '+e;}}
}}
tick();setInterval(tick,4000);
</script>
</body>
</html>
""".format(ssid=AP_SSID, ip=AP_IP)

# =========================================================
# HTTP HELPERS
# =========================================================

def socket_send_all(client, data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    try:
        client.sendall(data)
        return
    except AttributeError:
        pass
    sent = 0
    total = len(data)
    while sent < total:
        n = client.send(data[sent:])
        if n is None or n <= 0:
            raise OSError("socket send failed")
        sent += n

def send_response(client, status="200 OK", content_type="text/plain", body="", extra_headers=None):
    if isinstance(body, str):
        body = body.encode("utf-8")
    headers = [
        "HTTP/1.1 {}".format(status),
        "Content-Type: {}".format(content_type),
        "Content-Length: {}".format(len(body)),
        "Connection: close",
        "Cache-Control: no-store",
    ]
    if extra_headers:
        headers.extend(extra_headers)
    socket_send_all(client, "\r\n".join(headers) + "\r\n\r\n")
    if body:
        socket_send_all(client, body)

def send_json(client, obj):
    send_response(client, "200 OK", "application/json", ujson.dumps(obj))

def send_csv_file(client, path):
    try:
        with open(path, "r") as f:
            body = f.read()
        send_response(client, "200 OK", "text/csv", body,
            extra_headers=['Content-Disposition: attachment; filename="touch_log.csv"'])
    except OSError:
        send_response(client, "500 Internal Server Error", "text/plain", "CSV read error")

def parse_path(req_text):
    try:
        first_line = req_text.split("\r\n", 1)[0]
        parts = first_line.split(" ")
        if len(parts) >= 2:
            path = parts[1]
            if path.startswith("http://") or path.startswith("https://"):
                slash = path.find("/", path.find("://") + 3)
                return path[slash:] if slash != -1 else "/"
            return path
    except Exception:
        pass
    return "/"

def build_api_payload(now_ms):
    ratio = (ema / base) if base else 0
    avg_touch_ms = get_avg_touch_duration_ms()
    return {
        "rtc": rtc_iso_string(),
        "state": get_state_string(playing, touch_active, armed),
        "battery_v": PLACEHOLDER_BATTERY_V,
        "uptime": format_uptime(ticks_diff(now_ms, BOOT)),
        "clients_connected": get_clients_connected(),
        "touch_count": touch_count,
        "touches_24h": get_touches_24h_display(),
        "avg_touch_duration": format_duration_ms(avg_touch_ms) if avg_touch_ms is not None else "N/A",
        "audio_play_count": audio_play_count,
        "last_touch_time": last_touch_time,
        "ratio": round(ratio, 3),
        "buf_count": _buf_count,
        "events": recent_events[-RECENT_EVENTS_MAX:],
    }

# =========================================================
# WIFI / AP SETUP
# =========================================================

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=AP_SSID, password=AP_PASSWORD)
AP_IP = ap.ifconfig()[0]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", HTTP_PORT))
server.listen(HTTP_BACKLOG)
server.settimeout(0.0)

# =========================================================
# STARTUP
# =========================================================

ensure_log_header()

if RTC_ENABLED and i2c is not None:
    try:
        print("I2C devices:", [hex(x) for x in i2c.scan()])
    except Exception as e:
        print("I2C scan error:", e)
else:
    print("RTC disabled")

# Allow the touch peripheral to settle after I2C activity on boot.
# Especially important if Set_rtc.py was run just before this — the
# SoftI2C bus needs time to fully release the GPIO pins before the
# capacitive touch peripheral can get a clean reading.
sleep_ms(500)

def _tp_read_safe():
    """Read touchpad with retries - ESP32 occasionally throws ValueError
    after I2C bus activity due to GPIO noise on capacitive pins."""
    for _ in range(5):
        try:
            return tp.read()
        except ValueError:
            sleep_ms(20)
    raise RuntimeError("Touchpad unresponsive after retries")

samples = []
for _ in range(40):
    samples.append(_tp_read_safe())
base = sum(samples) / len(samples)
ema = base
raw = int(base)
print("Baseline:", base)

add_event("boot")
add_event("AP started: ssid={} ip={}".format(AP_SSID, AP_IP))

# =========================================================
# STATE
# =========================================================

playing = False
want = None
t0 = ticks_ms()
last_touch = ticks_ms()
armed = False
next_print = ticks_ms()
next_gc = ticks_ms() + GC_EVERY_MS

touch_active = False
touch_start = 0
touch_rtc_start = ""
touch_count = 0
touch_min_ema = 1e9
touch_armed = False

# Prevents audio firing more than once per touch gesture
audio_triggered = False

# Client connect effect tracking
_prev_clients = 0

leds_off()
gc.collect()

# =========================================================
# HTTP REQUEST HANDLER
# =========================================================

def handle_one_http(now_ms):
    try:
        client, addr = server.accept()
    except OSError:
        return False
    try:
        client.settimeout(HTTP_CLIENT_TIMEOUT)
        req = client.recv(HTTP_RECV_SIZE)
        if not req:
            try: client.close()
            except Exception: pass
            return True
        try:
            req_text = req.decode("utf-8")
        except Exception:
            req_text = ""
        path = parse_path(req_text)
        if path == "/api":
            send_json(client, build_api_payload(now_ms))
        elif path == "/log.csv":
            flush_log()
            send_csv_file(client, LOG_PATH)
        else:
            send_response(client, "200 OK", "text/html; charset=utf-8", dashboard_html())
    except Exception as e:
        print("HTTP error:", e)
        try:
            send_response(client, "500 Internal Server Error", "text/plain", "Server error")
        except Exception:
            pass
    try:
        client.close()
    except Exception:
        pass
    return True

def handle_http_budget(now_ms):
    # Cap at 1 request while armed to keep loop timing tight
    limit = 1 if armed else MAX_HTTP_PER_LOOP
    handled = 0
    while handled < limit:
        if not handle_one_http(now_ms):
            break
        handled += 1
    return handled

# =========================================================
# MAIN LOOP
# =========================================================

while True:
    now = ticks_ms()

    # -----------------------------------------
    # Touch sampling
    # -----------------------------------------
    try:
        raw = tp.read()
    except ValueError:
        pass  # occasional ESP32 touchpad glitch - skip this sample
    ema = A * raw + (1 - A) * ema

    touched = ema < base * ON
    released = ema > base * OFF

    if (not playing) and (not touched):
        base = DRIFT * ema + (1 - DRIFT) * base

    # -----------------------------------------
    # Arming logic
    # -----------------------------------------
    if (not playing) and (ticks_diff(now, last_touch) > RESTART):
        if not armed:
            add_event("armed after idle")
            # Play track 2 + pink pulse (blocking ~1.8 s)
            play_track_once(_CMD_PLAY_IDX2)
            play_armed_effect()
            # After effect, module is left playing track 2 in background;
            # drain so it doesn't interfere with track 1 on next touch.
            _uart_drain()
        armed = True

    # -----------------------------------------
    # Touch session logging
    # -----------------------------------------
    if touched and (not touch_active):
        touch_active = True
        touch_start = now
        touch_rtc_start = rtc_iso_string()
        touch_min_ema = ema
        touch_armed = armed
        add_event("touch start")

    if touch_active and (ema < touch_min_ema):
        touch_min_ema = ema

    if released and touch_active:
        touch_active = False
        dur = ticks_diff(now, touch_start)
        touch_count += 1
        last_touch_time = rtc_iso_string()
        log_touch_event(
            touch_id=touch_count,
            rtc_start=touch_rtc_start,
            uptime_start_ms=ticks_diff(touch_start, BOOT),
            dur_ms=dur,
            min_ema=touch_min_ema,
            armed_flag=touch_armed
        )
        add_touch_duration(dur)
        add_touch_timestamp_24h()
        add_event("touch end | dur={}ms | min_ema={}".format(dur, int(touch_min_ema)))

    # -----------------------------------------
    # Client connect effect
    # -----------------------------------------
    cur_clients = get_clients_connected()
    if cur_clients > 0 and _prev_clients == 0:
        add_event("client connected")
        play_track_once(_CMD_PLAY_IDX3)
        play_connect_effect()
        _uart_drain()
    elif cur_clients == 0 and _prev_clients > 0:
        add_event("client disconnected")
    _prev_clients = cur_clients

    # -----------------------------------------
    # HTTP (before state machine; refresh now after)
    # -----------------------------------------
    handle_http_budget(now)
    now = ticks_ms()

    # -----------------------------------------
    # Touch/audio state machine
    # -----------------------------------------
    if not playing:
        if touched:
            if not audio_triggered:
                if want is not True:
                    want = True
                    t0 = now
                elif ticks_diff(now, t0) > DB_ON:
                    audio_triggered = True
                    try:
                        if armed:
                            # Flash module is always PAUSED after track ends.
                            # Flush stale UART bytes first, then play resumes
                            # from the paused position (start, since it finished).
                            reset_track()
                            add_event("audio replay")
                        else:
                            p.play()
                            add_event("audio play")
                        audio_play_count += 1
                        armed = False
                        playing = True
                        want = None
                        last_touch = now
                    except Exception as e:
                        print("audio error:", e)
                        add_event("audio error: " + str(e))
                        want = None
                        audio_triggered = False
        else:
            want = None
            audio_triggered = False
    else:
        if not released:
            last_touch = now

        if released:
            if want is not False:
                want = False
                t0 = now
            elif ticks_diff(now, t0) > DB_OFF:
                try:
                    p.pause()
                    add_event("audio pause")
                except Exception as e:
                    print("pause error:", e)
                    add_event("audio pause error: " + str(e))
                playing = False
                want = None
                # Start RESTART countdown from this moment
                last_touch = now
        else:
            want = None

    # -----------------------------------------
    # LEDs
    # -----------------------------------------
    update_leds(now, playing or touch_active, cur_clients > 0)

    # -----------------------------------------
    # Periodic safety flush
    # -----------------------------------------
    if ENABLE_LOGGING and _buf_count > 0 and ticks_diff(now, next_flush) >= 0:
        flush_log()
        next_flush = now + SAFETY_FLUSH_MS

    # -----------------------------------------
    # Debug print
    # -----------------------------------------
    if ticks_diff(now, next_print) >= 0:
        ratio = (ema / base) if base else 0
        avg_touch_ms = get_avg_touch_duration_ms()
        print(
            "raw:{} ema:{:.1f} base:{:.1f} ratio:{:.3f} state:{} touches:{} plays:{} clients:{} buf:{} mem:{}"
            .format(
                raw, ema, base, ratio,
                get_state_string(playing, touch_active, armed),
                touch_count, audio_play_count,
                get_clients_connected(),
                _buf_count,
                gc.mem_free()
            )
        )
        next_print = now + PRINT_EVERY

    # -----------------------------------------
    # Housekeeping
    # -----------------------------------------
    if ticks_diff(now, next_gc) >= 0:
        gc.collect()
        next_gc = now + GC_EVERY_MS

    sleep_ms(LOOP_MS)