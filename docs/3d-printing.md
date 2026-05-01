# 3D Printing Guide

This guide covers the recommended printing approach for the Helping Hands enclosure, internal parts, LED/speaker assembly, and 3D printed PCB-style carrier board.

For the best lighting effect and strength, print the visible enclosure parts in **translucent PET-G**.

> [!IMPORTANT]  
> Translucent PET-G must be thoroughly dried before printing. Wet PET-G will print weaker, cloudier, stringier, and less cleanly.

---

## Quick print summary

[![Static Badge](https://img.shields.io/badge/Main_Body-MakerWorld-%2308bf08?style=flat&logo=bambulab)](https://makerworld.com/en/models/2741945-helping-hands) 
[![Static Badge](https://img.shields.io/badge/PCB-MakerWorld-%2308bf08?style=flat&logo=bambulab)](https://makerworld.com/en/models/2741945-helping-hands) 
[![Static Badge](https://img.shields.io/badge/Alignment_Tool-MakerWorld-%2308bf08?style=flat&logo=bambulab)](https://makerworld.com/en/models/2741945-helping-hands)


| Setting / requirement | Recommendation |
| --- | --- |
| Material | Translucent PET-G |
| Nozzle size | 0.4mm |
| Minimum bed size | 150mm × 150mm |
| Filament drying | At least 8 hours before printing |
| Main goal | Strength, translucency, and clean light diffusion |
| Recommended profile | [Print Glass by Dennis Lenz on MakerWorld](https://makerworld.com/en/models/560963-print-glass#profileId-480277) |

The print settings used across the build are based on the MakerWorld **Print Glass** profile by **Dennis Lenz**.

Credit:  
[Print Glass — Dennis Lenz, MakerWorld](https://makerworld.com/en/models/560963-print-glass#profileId-480277)

---

<details open>
<summary><strong>1. Before printing</strong></summary>

## 1. Before printing

### 1.1 Print bed size

All parts have been designed to fit on a **150mm × 150mm** print bed.

This means the parts should fit on smaller printers such as:

- Bambu Lab A1 mini
- Bambu Lab P1S
- Creality Ender 3
- Similar printers with at least a 150mm × 150mm usable print area

### 1.2 Dry the filament

Dry translucent PET-G for at least **8 hours** before printing.

Wet PET-G will reduce:

- Strength
- Clarity
- Surface quality
- Layer bonding
- Light transmission

### 1.3 How to tell if PET-G is wet

Wet PET-G often makes a **popping, snapping, or crackling sound** while extruding.

Good, dry PET-G should extrude smoothly and quietly.

If the print is poor, check these three things first:

1. Dry the filament again
2. Wash the build plate
3. Slow the print down

> [!TIP]  
> When in doubt: dry the filament, clean the plate, and print slower.

</details>

---

<details open>
<summary><strong>2. Recommended slicer profile</strong></summary>

## 2. Recommended slicer profile

The recommended starting point is the MakerWorld profile:

[Print Glass by Dennis Lenz](https://makerworld.com/en/models/560963-print-glass#profileId-480277)

Use that profile directly where possible.

### 2.1 Why use a “glass” PET-G profile?

The Helping Hand enclosure benefits from translucent PET-G because it:

- Diffuses the internal light
- Allows the blue glow to show through the body
- Gives the enclosure a softer, more object-like quality
- Provides better toughness than PLA
- Is more suitable for repeated handling and semi-public installation

### 2.2 Manual slicing fallback

If you cannot use the MakerWorld profile directly, use the settings below as a manual starting point.

> [!NOTE]  
> These are fallback settings, not a replacement for the linked MakerWorld profile. Always test with your own filament and printer.

| Setting | Suggested starting point |
| --- | --- |
| Nozzle | 0.4mm |
| Layer height | 0.1mm–0.2mm |
| Line Width | 0.5-0.6mm|
| Nozzle temperature | 260c-270c |
| Bed temperature | 65-70c |
| Print speed | 20-30mm/s on all walls |
| Cooling | 0 - 20%  |
| Top layers | 0, where the profile requires glass-like infill exposure |
| Bottom layers | 0, where the profile requires glass-like infill exposure |
| Infill | 100% Aligned Rectalinear |
| Flow rate | 1.01 (slightly higer than you normally would)|
| **Always Print with 5mm Brim** |
### 2.3 What matters most

For this project, the important goals are:

1. Strong layer bonding
2. Clean translucent walls
3. Smooth light diffusion
4. Minimal stringing
5. Reliable fit of mechanical parts

If clarity is poor, print slower and dry the filament again before changing lots of slicer settings.

</details>

---

<details open>
<summary><strong>3. Design-for-printing notes</strong></summary>

## 3. Design-for-printing notes

The parts have been designed with FDM 3D printing in mind.

### 3.1 Bevelled edges

Bevelled edges are used to reduce visible hull lines and make the printed parts feel more finished.

### 3.2 Surface texture

Some surfaces include texture to help hide layer lines and reduce the appearance of print artefacts.

### 3.3 Cut overhangs

Overhangs have been reduced or cut away where possible, especially around bolt heads and fixing points.

### 3.4 Press fits

Press fits are used where possible to reduce extra hardware and make assembly easier.

### 3.5 Brass inserts

Brass heat-set inserts are used where parts need to be assembled and disassembled repeatedly.

This is especially useful for:

- The enclosure
- The inner lid
- The LED/speaker assembly
- Parts that may need servicing later

</details>

---

<details open>
<summary><strong>4. Brass inserts</strong></summary>

## 4. Brass inserts

The enclosure uses both **M3** and **M2** brass heat-set inserts.

Useful reference:

[Instructables: Add Metal Threads to Your 3D Prints](https://www.instructables.com/Add-Metal-Threads-to-Your-3D-Prints-Make-Them-Func/)

---

### 4.1 Insert count

The current build uses:

| Insert size | Quantity | Location |
| --- | ---: | --- |
| M3 | 5 | Main enclosure fixing points |
| M2 | 6 | Inner lid |
| M2 | 5 | LED/speaker assembly |

Total:

- **5 × M3 inserts**
- **11 × M2 inserts**

---

### 4.2 Installing brass inserts

1. Use a soldering iron with a clean tip
2. Set the insert squarely into the printed hole
3. Heat the insert gently with the soldering iron
4. Press it down slowly as the plastic softens
5. Stop when the insert sits flush with the surface
6. Let the plastic cool before adding screws

> [!CAUTION]  
> Do not force the insert in cold. This can split the print or deform the hole.

### 4.3 Tips for clean inserts

- Use gentle pressure
- Keep the insert straight
- Do not overheat the plastic
- Test with one insert on a failed print if possible
- Let inserts cool fully before assembling

</details>

---

<details open>
<summary><strong>5. Print quality checks</strong></summary>

## 5. Print quality checks

Before assembly, check each printed part carefully.

### 5.1 Enclosure

Check that:

- The main enclosure is not warped
- The lid fits cleanly
- Screw holes are open
- Brass insert holes are clean
- The hand mounting area is flat and strong
- The key switch hole is clean
- Cable holes are clear

### 5.2 Internal parts

Check that:

- The board carrier fits inside the enclosure
- The battery holder fits
- The LED/speaker assembly fits
- The LED ring sits correctly
- The speaker is not blocked
- The internal lid closes without crushing wires

### 5.3 3D printed PCB-style board

Check that:

- Trace channels are clean
- Copper tape can sit flat in the traces
- Header pin holes are clear
- There are no blobs or strings between traces
- The board is flat enough to solder onto

### 5.4 Alignment tool

Check that:

- The M5 threaded rods fit cleanly
- The rods sit square
- The spacing matches the enclosure
- The tool is strong enough to hold the rods while casting

</details>

---

<details open>
<summary><strong>6. Optional finishing</strong></summary>

## 6. Optional finishing

The printed parts can be used straight from the printer, but there are optional finishing steps.

### 6.1 Light flame polishing

You can very lightly pass a blowtorch over the outside of the translucent PET-G parts to improve clarity.

This can slightly smooth the outer surface and make the print appear clearer.

> [!WARNING]  
> Flame polishing is risky. It is easy to deform the model, burn the surface, or release unpleasant fumes. Only do this in a well-ventilated area, away from flammable materials, and do not breathe the fumes.

### 6.2 Go very lightly

If you try flame polishing:

1. Use a small flame
2. Keep the flame moving
3. Do not hold heat in one place
4. Test on a failed print first
5. Stop before the part visibly softens

This step is optional. A clean, slow, dry PET-G print is more important than finishing.

</details>

---

## Troubleshooting

### The print is cloudy

Likely causes:

- Wet filament
- Printing too fast
- Too much cooling
- Too low nozzle temperature
- Poor flow calibration

Try:

1. Dry the filament again
2. Increase temperature within the filament manufacturer’s range
3. Slow the print down
4. Reduce cooling
5. Check flow calibration

### The print is weak

Likely causes:

- Wet filament
- Low nozzle temperature
- Poor layer bonding
- Too much cooling
- Under-extrusion

Try:

1. Dry the filament again
2. Increase nozzle temperature within the safe PET-G range
3. Reduce fan speed
4. Check extrusion and flow
5. Print slower

### The print will not stick

Likely causes:

- Dirty build plate
- Incorrect bed temperature
- Poor first layer height
- Damp filament

Try:

1. Wash the build plate
2. Re-level or recalibrate the printer
3. Check first layer squish
4. Dry the filament
5. Use the correct plate settings for PET-G

### The print is stringy

Likely causes:

- Wet filament
- Too high temperature
- Retraction not tuned
- Travel moves too slow

Try:

1. Dry the filament
2. Tune temperature
3. Tune retraction
4. Increase travel speed if appropriate

---

## Final print checklist

Before moving on to assembly, check:

### Printing

- [ ] Translucent PET-G used
- [ ] Filament dried for at least 8 hours
- [ ] 0.4mm nozzle used
- [ ] Parts printed cleanly
- [ ] No major warping
- [ ] No major cracking or delamination
- [ ] All parts fit on the intended 150mm × 150mm bed

### Fit and finish

- [ ] Enclosure closes properly
- [ ] Lid fits
- [ ] Board carrier fits
- [ ] Battery holder fits
- [ ] LED/speaker assembly fits
- [ ] Cable holes are clear
- [ ] Mounting slots are clear

### Inserts and hardware

- [ ] 5 × M3 inserts installed
- [ ] 11 × M2 inserts installed
- [ ] Screws thread cleanly
- [ ] Inserts are flush
- [ ] No melted or distorted fixing points

### Ready for assembly

- [ ] 3D printed PCB traces are clean
- [ ] Alignment tool works with M5 threaded rods
- [ ] Enclosure is ready for electronics
- [ ] Hand mounting area is ready
