# Helping Hands Build Instructions

This guide walks through the full process of building a Helping Hand: buying parts, printing the enclosure, casting the hand, wiring the electronics, flashing the firmware, adding audio, testing the system, and installing it.

> [!IMPORTANT]  
> Read the whole guide before starting. Some steps, especially casting and wiring, are much easier if you plan ahead.

---

## Build overview

The basic build process is:

1. Buy the electronic components  
   See [`docs/shopping_list.md`](./shopping_list.md)

2. Print the enclosure and internal parts  
   See the MakerWorld model page and [`docs/3d_printing.md`](./3d_printing.md)

3. Cast the hand  
   Choose either a plaster hand or a polyurethane cold cast hand.

4. Wire the electronics

5. Flash the ESP32 with MicroPython  
   See the official [MicroPython ESP32 getting started guide](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)

6. Upload the Helping Hands firmware

7. Add your audio files to the JQ6500 module

8. Test touch, audio, lights, and power

9. Install the hand

---

## Before you begin

### What kind of hand should I make?

There are two final hand types:

| Hand type | Best for | Notes |
| --- | --- | --- |
| Plaster hand | Indoor use, exhibitions, protected installations, low-cost prototypes | Cheaper and easier to make |
| Polyurethane cold cast hand | Outdoor use, public installation, more durable builds | Stronger and more weather-resistant |

> [!NOTE]  
> To make a cold cast hand, you must first make a plaster hand. The plaster hand becomes the master used to make the silicone mould.

### Useful links

- [MicroPython ESP32 getting started guide](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
- [`mpremote` on PyPI](https://pypi.org/project/mpremote/)
- [Thonny Python IDE](https://thonny.org/)
- [Instructables: Lifecasting Hands](https://www.instructables.com/Lifecasting---hands/)
- [Smooth-On: Moulding a 3D object with Rebound 25](https://www.smooth-on.com/tutorials/molding-3-object-rebound-25-brush-silicone-rubber/)

---

<details>
<summary><strong>1. Buy the electronic components</strong></summary>

## 1. Buy the electronic components

Buy the required electronic components before printing and casting so you can test-fit parts as you go.

See:

[`docs/shopping_list.md`](./shopping_list.md)

### Core components

The exact list may change between versions, but the core system includes:

- ESP32 development board
- JQ6500 audio module
- Audio driver / amplifier
- Speaker
- RTC module
- BQ25185 battery / charging board
- Li-ion battery
- NeoPixel / addressable RGB LED ring
- Key switch
- JST connectors
- Copper tape
- Header pins
- Wire
- M3 and M5 hardware

</details>

---

<details>
<summary><strong>2. Print the enclosure and internal parts</strong></summary>

## 2. Print the enclosure and internal parts

Print the enclosure, internal mounts, alignment tools, and 3D printed PCB-style carrier board.

See:

[`docs/3d_printing.md`](./3d_printing.md)

Also check the MakerWorld model page when available.

### Recommended print checks

Before moving on, check that:

- The enclosure closes properly
- The board fits inside the enclosure
- The battery holder fits
- The LED ring fits
- The mounting slots are clear
- The threaded rod alignment tool prints cleanly
- The 3D printed PCB trace channels are clean and usable

### Notes

Printing profiles have been tested on:

- Bambu Lab A1 mini
- Bambu Lab P1S
- Creality Ender 3

More printer profiles are welcome.

</details>

---

<details open>
<summary><strong>3. Cast the hand</strong></summary>

## 3. Cast the hand

You can make either:

- A plaster hand
- A polyurethane and atomised metal powder cold cast hand

The plaster hand is the simpler version. The cold cast hand is stronger and more suitable for outdoor/public use.

---

### 3.1 Casting a plaster hand

You can either:

- Buy a life casting hand kit and follow the kit instructions
- Or buy around **500g of alginate per hand** and a strong casting plaster such as **Herculite 2**

For the basic hand casting process, follow:

[Instructables: Lifecasting Hands](https://www.instructables.com/Lifecasting---hands/)

Or follow the instructions provided with your casting kit.

#### While the plaster is setting

Before the plaster cures, insert both the touch sensing wires and the mounting rods.

##### Add touch sensing wires

Insert **4 wires** into the hand, reaching into the fingers.

These wires improve touch sensing reliability by increasing the conductive area inside the hand.

Prepare each wire like this:

1. Strip around **80%** of the wire that will sit inside the plaster
2. Leave a small amount of sheathing inside the plaster so the wire is mechanically held
3. Leave around **100mm** of wire hanging out from the base of the hand

These wires will later connect to the capacitive touch sensing lead.

##### Add mounting rods

Insert **two 150mm lengths of M5 threaded rod** into the alignment tool, then set them into the plaster.

These rods align the hand with the enclosure and provide the mechanical fixing points.

#### Cure and finish the plaster hand

Once the plaster has cured enough to remove:

1. Carefully remove the hand from the alginate mould
2. Leave the plaster hand to fully dry and cure for at least **48 hours**
3. Sand, paint, or finish the hand if desired

Your plaster hand is now finished.

> [!TIP]  
> Have fun with different hand poses. The best Helping Hands have character: an inviting grip, a soft hold, or a slightly strange little personality.

---

### 3.2 Making a cold cast hand

To make a cold cast hand, start with a fully dried plaster hand.

You can skip setting wires and threaded rods into this plaster hand, because it will be used as the master for the silicone mould. The wires and rods will be added to the final polyurethane hand later.

#### Make the silicone mould

1. Take your dried plaster hand
2. Hot glue it to a board you do not care about
3. Use a brush-on silicone such as **Smooth-On Rebound 25**
4. Build up the mould in layers, following Smooth-On’s instructions
5. Allow the mould to fully cure

Useful reference:

[Smooth-On: Moulding a 3D object with Rebound 25](https://www.smooth-on.com/tutorials/molding-3-object-rebound-25-brush-silicone-rubber/)

#### Mix the cold cast resin

Use:

- 10-minute polyurethane resin
- Atomised aluminium powder, or another atomised metal powder of your choice

Mix at a ratio of roughly:

```txt
1 part resin : 3 parts metal powder
```

The mixture will be thick.

Start with a small batch. Around **60g** is usually enough for the first coat on a large male hand.

#### Cast the hollow shell

1. Pour the first resin/metal mix into the mould
2. Rotate the mould constantly so the resin coats every surface
3. Keep rotating for around **5 minutes**, or until the resin starts to set and no longer drips
4. Repeat immediately with another batch
5. Build up **3–4 coats** until you have a strong hollow hand

#### Add wires and mounting rods

Once the hollow hand has been formed:

1. Insert the touch sensing wires into the fingers
2. Insert the M5 threaded rods using the alignment tool
3. Fix everything in place with a final batch of resin

You do not need to add metal powder to this final internal fixing pour.

#### Finish the cold cast hand

Once cured:

1. Demould carefully
2. Trim or sand any rough edges
3. Polish the surface with a metal polish such as Autosol, if desired

The cold cast hand should now have a metallic surface, a strong shell, embedded sensing wires, and mounting rods ready for installation.

</details>

---

<details open>
<summary><strong>4. Wire the electronics</strong></summary>

## 4. Wire the electronics

The Helping Hand uses a 3D printed PCB-style carrier board with copper tape traces.

Work slowly. The board is simple, but it is easy to lift copper tape or accidentally create shorts.

> [!WARNING]  
> Always solder with ventilation or extraction. Avoid breathing solder fumes or melted plastic fumes.

---

### 4.1 Prepare the 3D printed PCB

1. Lay copper tape over all the printed traces
2. Gently press the tape into the trace channels  
   A cotton bud tip works well
3. Sand away the extra copper tape using 400 grit sandpaper or an orbital sander
4. Keep sanding until only the intended copper traces remain
5. Check carefully for shorts between traces

Go gently. If you sand too far and rip off a trace, either:

- Replace it with a precisely cut piece of copper tape
- Or jump the broken trace with a wire

---

### 4.2 Add header pins

1. Place PTH header pins into the board from the non-tape side
2. Solder each joint onto the copper tape
3. Heat the pin, not the tape
4. Let the solder flow onto the copper

> [!CAUTION]  
> Do not overheat the copper tape. The plastic board can melt.

---

### 4.3 Add the components

Place the components in their marked positions and solder them to the board.

The exact layout depends on your board version, but the core modules are:

- ESP32
- JQ6500 audio module
- BQ25185 battery / charging board
- RTC module
- Audio driver / amplifier
- LED ring connections
- Touch sensing lead
- Key switch connections
- Battery connector

---

### 4.4 Wire through the enclosure

Through the holes in the bottom of the enclosure:

| Connection | Wire to |
| --- | --- |
| Key switch | GND and EN on the BQ25185 |
| Sensing lead | D4 |
| LED ring GND | GND |
| LED ring power | 5V |
| LED ring data | D27 |
| Audio driver power | JQ6500 / audio power pads |
| Battery enclosure | BQ25185 via JST connector |

Install the board and battery into the enclosure.

For easy disassembly, use a small terminal block or WAGO connector between the hand’s sensing wires and the main sensing lead.

</details>

---

<details open>
<summary><strong>5. Flash and upload the firmware</strong></summary>

## 5. Flash and upload the firmware

The Helping Hand firmware runs on MicroPython.

---

### 5.1 Flash MicroPython to the ESP32

Flash the ESP32 with MicroPython using the official guide:

[MicroPython ESP32 tutorial](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)

You can use whichever flashing method you prefer, but `esptool.py` is the common route.

Once MicroPython is installed, confirm that you can connect to the board before uploading the Helping Hands files.

---

### 5.2 Choose an upload tool

You can upload files using either:

- [`mpremote`](https://pypi.org/project/mpremote/)
- [Thonny](https://thonny.org/)

Use whichever tool you are most comfortable with.

---

### 5.3 Set the RTC

First upload and run:

```txt
firmware/set_rtc.py
```

This script grabs the current time and date from your computer and writes it to the onboard RTC.

---

### 5.4 Upload the main files

Next upload:

```txt
jq6500.py
main.py
```

Optional settings you may want to tweak in `main.py` include:

- LED brightness
- Touch-on sensitivity
- Touch-off sensitivity
- Pulse speed
- Quiet hours
- Day/night behaviour
- Wi-Fi dashboard name
- Audio behaviour

</details>

---

<details open>
<summary><strong>6. Add audio to the JQ6500 module</strong></summary>

## 6. Add audio to the JQ6500 module

Upload your audio tracks to the JQ6500 module using the JQ6500 upload tool.

### File naming

Format the files like this:

```txt
001 Main story audio, played when touched, up to 60 seconds.mp3
002 Arming sound effect.mp3
003 Wi-Fi connected sound effect.mp3
```

### Audio behaviour

The exact behaviour depends on the firmware version, but the general structure is:

| Track | Use |
| --- | --- |
| `001` | Main voice / story audio |
| `002` | Arming sound effect |
| `003` | Wi-Fi connected sound effect |

Keep the main story track short. Around **30–60 seconds** works well for public interaction.

</details>

---

<details open>
<summary><strong>7. Test the hand</strong></summary>

## 7. Test the hand

Before installation, test the full system.

---

### 7.1 Power on

1. Turn the key switch to power on the hand
2. Wait around **10 seconds** for the touch sensor to calibrate
3. Do not touch the hand during calibration

---

### 7.2 Test the touch interaction

When you hold the hand:

- The hand should light up
- The main audio should start playing

When you let go:

- The audio should stop or pause
- The lights should return to the idle state

If you grab the hand again within around **10 seconds**, the audio should resume from where it left off.

If the hand is left untouched for longer, it should:

- Flash pink
- Play the arming sound
- Restart the main story track the next time it is touched

---

### 7.3 Check the dashboard

To check the dashboard:

1. Connect to the hand’s Wi-Fi network  
   Usually named something like:

```txt
HelpingHand1
```

2. Open a browser and go to:

```txt
http://192.168.4.1
```

From the dashboard you can check:

- Uptime
- System time
- Current state
- Number of touches
- Touch duration
- Recent activity
- Other system metrics

</details>

---

<details open>
<summary><strong>8. Install the hand</strong></summary>

## 8. Install the hand

The enclosure can be mounted in two main ways.

---

### 8.1 Wall mounting

Use **4 M3 screws** through the mounting slots to attach the hand to a wall or flat surface.

---

### 8.2 Pole mounting

Use **2 jubilee clips** to mount the hand to a pole, railing, or similar street furniture.

---

### 8.3 Outdoor notes

For outdoor use:

- Use the cold cast hand
- Check the enclosure is closed properly
- Protect cables from strain
- Consider extra sealing depending on the installation environment
- Avoid placing the speaker or openings where water can pool

</details>

---

## Final checklist

Before calling the build finished, check:

### Printed parts

- [ ] Enclosure printed
- [ ] Internal printed parts complete
- [ ] Board carrier printed
- [ ] Alignment tool printed

### Cast hand

- [ ] Hand cast
- [ ] Touch wires embedded
- [ ] Mounting rods embedded
- [ ] Hand fully cured
- [ ] Hand finished / sealed if needed

### Electronics

- [ ] Copper tape PCB prepared
- [ ] No shorts between traces
- [ ] Components soldered
- [ ] Battery connected
- [ ] Key switch working
- [ ] LED ring connected
- [ ] Speaker connected
- [ ] Touch sensing lead connected

### Firmware and audio

- [ ] ESP32 flashed with MicroPython
- [ ] RTC set
- [ ] Firmware uploaded
- [ ] Audio uploaded to JQ6500
- [ ] Touch sensing tested
- [ ] LED ring tested
- [ ] Audio tested
- [ ] Dashboard tested

### Installation

- [ ] Enclosure closed securely
- [ ] Hand mounted securely
- [ ] Cables protected
- [ ] Outdoor sealing checked, if relevant

Once all of that works, you have a Helping Hand.
