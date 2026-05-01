from machine import Pin, SoftI2C

I2C_SDA = 21
I2C_SCL = 22
RTC_ADDR = 0x68

i2c = SoftI2C(scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=100000)

def dec_to_bcd(d):
    return ((d // 10) << 4) | (d % 10)

def rtc_set_datetime(year, month, day, hour, minute, second, weekday=1):
    data = bytes([
        dec_to_bcd(second),
        dec_to_bcd(minute),
        dec_to_bcd(hour),
        dec_to_bcd(weekday),
        dec_to_bcd(day),
        dec_to_bcd(month),
        dec_to_bcd(year - 2000),
    ])
    i2c.writeto_mem(RTC_ADDR, 0x00, data)

# Set to: 2026-04-20 12:30:00
# weekday: 1-7 (DS3231 convention, not super important for your current code)
rtc_set_datetime(2026, 4, 30, 14, 53, 0, 4)

print("RTC set")