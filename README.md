Helping Hands are interactive public sculptures that invite people to listen to local stories about climate-adapted futures.


<img width="800" height="200" alt="helping hands wordmark" src="https://github.com/user-attachments/assets/ca242abb-a82e-46ed-b473-48588106e7b9" />


<img width="338" height="600.0" alt="DSC00719" src="https://github.com/user-attachments/assets/b928054b-a593-4d7c-a91b-3269a63d4c65" />


Each hand senses when it is touched, glows with light, and plays an audio story. The project began as part of *Waters of Leith*, a design project exploring how local knowledge, everyday experience, and public imagination can shape climate adaptation in Leith, Edinburgh.

This repository contains the files needed to make your own Helping Hand: 3D-printable parts, casting tools, wiring notes, firmware, and installation guidance.

---

## What are Helping Hands?

Helping Hands are small, touch-sensitive audio sculptures designed to be installed in public or semi-public places.

<img width="600" height="400" alt="DSC00763" src="https://github.com/user-attachments/assets/1e37ef9f-a0d7-499f-9ddc-ab6969c5dafd" />


They act as **waymarkers**: physical points where community stories, memories, concerns, and hopes can be held, heard, and shared.

When someone holds a hand, it responds with light and sound. Each hand can contain a different voice, story, or message from the future.

---

## Why make them?

Helping Hands are about making local imagination tangible.

They can be used for:

- community engagement
- speculative design workshops
- climate adaptation conversations
- public art installations
- local storytelling projects
- education and participatory research
- playful civic experiments

The project is intentionally open-ended. You can build one as a sculpture, a workshop output, a public installation, or a starting point for your own version.

---

## Features

<img width="240" height="320" alt="Tommy chat - 2026-05-01 06 41 29" src="https://github.com/user-attachments/assets/9ce7360f-4b9e-4195-b154-7d6c2b7e1a0d" />


Current and planned firmware features:

- [x] MicroPython firmware
- [x] Touch sensing
- [x] Audio playback using the JQ6500 MP3 module
- [x] Blue LED pulse when touched
- [x] Direct touch trigger
- [x] Near-sense trigger mode
- [x] Access Point monitor dashboard
- [x] Touch logging
- [x] Touch duration logging
- [x] Day/night behaviour
- [x] Quiet hours
- [x] Optional RTC support for reliable timekeeping
- [ ] Mesh mode for linking multiple hands together
- [ ] Windows/Linux install wizard
- [ ] Improved dashboarding
- [ ] Remote access
- [ ] USB-C battery-management routing
- [ ] Lower-cost electronics version
- [ ] More confirmed print profiles

Confirmed print testing:

- [x] Bambu Lab A1 Mini
- [x] Bambu Lab P1S
- [x] Creality Ender 3
- [ ] More printers wanted!

---

## Overall instructions

<img width="240" height="320" alt="Tommy chat - 2026-05-01 06 41 34" src="https://github.com/user-attachments/assets/07fab208-61d1-4871-bddb-5fe0dfcf63c0" />


The basic build process is:

1. Buy the electronic components.
2. Print the enclosure and internal parts.
3. Cast the hands.
4. Wire the electronics.
5. Flash the ESP32 with MicroPython.
6. Upload the Helping Hands firmware.
7. Add your audio files to the JQ6500 module.
8. Configure the hand.
9. Test touch, audio, lights, and power.
10. Install the hand.

For the full build guide, see:

[`docs/instructions.md`](docs/instructions.md)

For print settings and tuning, see:

[`docs/3d-printing.md`](docs/3d-printing.md)

For enclosure customisation, see:

[`docs/enclosure-customisation.md`](docs/enclosure-customisation.md)

---

## Tools

You will likely need:

- 3D printer
- Soldering iron
- laptop or desktop computer

---

# Parts list

## 3D prints

The printable files are split into a few sets:

| Print set | Description | Link |
|---|---|---|
| Enclosure | Main body, lid, mounts, internal structure | MakerWorld link coming soon |
| PCB / wiring carrier | Printable wiring support or internal carrier | MakerWorld link coming soon |
| Hand casting tool | Tools for aligning threaded rod and casting hands | MakerWorld link coming soon |

More detail:

[`docs/3d-printing.md`](docs/3d-printing.md)

---

## Components
For full list see: 

[`docs/shopping-list.md`](docs/shopping-list.md)

### Electronics

| Part | Notes | Link |
|---|---|---|
| ESP32 WROOM dev board | Main controller | Link coming soon |
| JQ6500 MP3 player | Audio playback module | Link coming soon |
| Adafruit BQ25185 solar charger | For solar installs | Adafruit link coming soon |
| DS3231 RTC module | Optional, improves day/night and quiet-hour reliability | Link coming soon |
| 18650 Li-ion cell | Use a reputable protected cell where possible | Link coming soon |
| 3W 8Ω 67mm speaker driver | Main audio output | Link coming soon |
| 24 LED COB WS2812B Light Ring | Light feedback | Adafruit / cheap link coming soon |

---

# Firmware

The firmware is written in MicroPython.

Current files include:

| File | Description |
|---|---|
| `main.py` | Main Helping Hands firmware |
| `jq6500.py` | JQ6500 MP3 player library |
| `rtc_flash.py` | RTC setup / flashing helper |
| `config.py.example` | Example configuration file |

---

# Customisation

This project is meant to be messed with. You can customise:

- enclosure form
- textures and surface details
- light behaviour
- timing
- audio content
- installation context
- overall theme

See:

[`docs/enclosure-customisation.md`](docs/enclosure-customisation.md)

---

# Wiring

See:

[`docs/wiring.md`](docs/wiring.md)

---

# Installation

Helping Hands can be installed indoors, outdoors, or as part of temporary public engagement events.

Before installing in public, consider:

- permission from the site owner
- weather protection
- safe mounting
- battery access
- charging method
- audio volume
- trip hazards
- sharp edges
- vandal resistance
- how people will know what to do
- whether the hand needs a plaque, label, or prompt

Suggested prompt:

> Hold my hand. Hear my story.

---

# Documentation

Planned documentation:

| Document | Status |
|---|---|
| `docs/instructions.md` | In progress |
| `docs/3d-printing.md` | In progress |
| `docs/wiring.md` | In progress |
| `docs/firmware.md` | In progress |
| `docs/enclosure-customisation.md` | In progress |
| `docs/casting.md` | In progress |
| `docs/installing.md` | In progress |
| `docs/troubleshooting.md` | In progress |

---

# Troubleshooting

Common issues currently include:

| Problem | Likely cause |
|---|---|
| Touch works on USB but not battery | Weak ground reference or touch threshold needs tuning |
| LEDs do not turn on | Power issue, wrong data pin, or insufficient current |
| Audio does not play | JQ6500 file indexing or wiring issue |
| Time-based features are wrong | RTC not set or missing |
| Dashboard does not appear | ESP32 AP mode not active |
| Touch is too sensitive | Threshold too low |
| Touch is not sensitive enough | Threshold too high or poor touch connection |

See:

[`docs/troubleshooting.md`](docs/troubleshooting.md)

---

# Roadmap

Things I would like to improve next:

- [ ] Better installation wizard
- [ ] Cleaner dashboard UI
- [ ] Mesh behaviour between multiple hands
- [ ] Easier audio upload process
- [ ] Better battery monitoring
- [ ] More reliable solar version
- [ ] Cheaper electronics version
- [ ] More enclosure variants
- [ ] More mounting options
- [ ] More print profiles from different printers
- [ ] Better documentation for public installs

---

# Contributing

Please contribute!

This project is still developing, and there are lots of ways to help:

- build your own version
- share photos of your installation
- test the print files on different printers
- suggest better components
- improve the firmware
- report bugs
- improve the documentation
- make new enclosure variants
- adapt the project for another place or community

If something does not work, open an issue and describe:

1. what you were trying to do
2. what happened
3. what hardware you used
4. what firmware version you used
5. photos or screenshots if useful

Pull requests are welcome, especially for small fixes, documentation improvements, and tested hardware changes.

Forks, remixes, and strange versions are encouraged.

---

# Credits

Created by **Tommy Newbold / Studio Tommy** as part of the *Waters of Leith* project.

This project uses the `jq6500.py` library for controlling the JQ6500 MP3 module.

Credit and source link to be added.

---

# Licensing

This project uses separate licences for code and physical/documentation files.

1. **Code:** Licensed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).
2. **3D Models and Documentation:** Licensed under [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

This means you can use, adapt, remix, and share the project, but improvements should remain open and credited.

---

# A note on AI-assisted code

Some of the firmware and documentation for this project has been developed with the help of AI coding tools.

That means the code should be treated like any other experimental open-source hardware project: useful, hackable, and worth checking carefully before relying on it.

If you spot something odd, inefficient, unsafe, or just badly explained, please open an issue or suggest an improvement.
