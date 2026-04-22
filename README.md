# Helping Hands

**Helping Hands** is an open-source interactive sculpture project built around cast hands, touch, sound, light, and modular electronics.

Hold a hand, and it speaks back.

Build one as a standalone object, or connect multiple hands together to create installations that wake up across a space.

![Helping Hands hero image](assets/images/hero.jpg)

Helping Hands brings together:

- cast hand sculptures
- ESP32-based electronics
- audio playback
- timed behaviours
- modular 3D-printed parts
- a printed PCB-style internal system
- a guided setup and flashing workflow
- tools for casting and alignment
- support for connected multi-hand installations

This repo is the main home for the full project: code, files, build notes, documentation, and all the odd little details that make it work.

If you want to build one, remix one, or make your own strange version, you’re in the right place.
---

## What is it?

Helping Hands combines:

- cast hand sculptures
- ESP32-based electronics
- audio playback
- timed behaviours
- modular 3D-printed parts
- a printed PCB-style internal system
- a guided flashing / setup workflow
- tools for casting and alignment
- support for connected multi-hand installations

This repo is the main home for the full project: code, files, docs, build notes, and all the weird little bits that make it work.

---

## Why it exists

This project started as a way to make stories of the future feel physical, social, and hard to ignore.

Instead of reading a panel or staring at a screen, you hold something human. It speaks back. It lights up. In a larger installation, other hands can wake up too.

The goal is not just to preserve one finished object. It is to make the system open enough that other people can build with it, adapt it, and carry it somewhere new.

---

## Features

- touch-based interaction
- cast + printed hybrid build
- ESP32 control
- JQ6500 audio playback
- RTC-supported timed behaviour
- modular enclosure system
- printed PCB-style internal layout
- configurable firmware
- guided setup and flashing workflow
- support for connected installations
- open files for remixing and reuse

---

## How it works

A typical Helping Hands build has a few main layers:

### The hand
The public-facing part. Cast, tactile, and made to be held.

### The enclosure
A printable body that holds the electronics and can be adapted for different installs.

### The internal hardware system
Off-the-shelf components organised through a repeatable internal layout, including a printed PCB-style carrier system.

### The firmware
Handles touch interaction, timing, lighting, audio playback, and configuration.

### The wider platform
One hand works on its own. Multiple hands can be configured as a larger connected installation.

---

## Build your own?

Yes — that is the point.

Helping Hands is designed to be replicated, modified, and reinterpreted. If you want to build one, this repo is intended to give you everything you need to understand the system and make your own version.

### Start here

- [`docs/overview.md`](docs/overview.md)
- [`docs/quick-start.md`](docs/quick-start.md)
- [`docs/build-guide.md`](docs/build-guide.md)
- [`docs/bill-of-materials.md`](docs/bill-of-materials.md)
- [`docs/wiring.md`](docs/wiring.md)
- [`docs/3d-prints.md`](docs/3d-prints.md)
- [`docs/casting-hands.md`](docs/casting-hands.md)
- [`docs/flashing.md`](docs/flashing.md)

---

## 3D prints

This project includes more than just an outer shell.

The printable parts include:

- enclosure/body parts
- hand-casting tools
- printed PCB-style carrier parts
- editable models where available

See [`docs/3d-prints.md`](docs/3d-prints.md).

---

## Casting hands

Casting is a core part of the build.

The casting guide covers:

- moulding and casting workflow
- materials and process notes
- alignment tools
- bolt placement
- repeatable assembly tricks
- lessons learned from testing

See [`docs/casting-hands.md`](docs/casting-hands.md).

---

## Firmware

Current firmware parts include:

- `firmware/main.py`
- `firmware/rtc.py`
- `firmware/jq6500.py`
- `firmware/config.py.example`

See [`docs/firmware.md`](docs/firmware.md).

---

## Customisation

This project is meant to be messed with.

You can customise:

- enclosure form
- textures and surface details
- embedded text and graphics
- light behaviour
- timing
- audio content
- installation context
- overall theme

The enclosure customisation guide includes notes on using **BumpMesh** and related tools to add patterns, text, and site-specific identity.

See [`docs/enclosure-customisation.md`](docs/enclosure-customisation.md).

---

## Repository structure

```text
helping-hands/
├─ README.md
├─ LICENSE-CODE
├─ LICENSE-DESIGN
├─ CONTRIBUTING.md
├─ docs/
│  ├─ overview.md
│  ├─ quick-start.md
│  ├─ build-guide.md
│  ├─ bill-of-materials.md
│  ├─ wiring.md
│  ├─ firmware.md
│  ├─ flashing.md
│  ├─ networking.md
│  ├─ 3d-prints.md
│  ├─ printed-pcb-system.md
│  ├─ casting-hands.md
│  ├─ enclosure-customisation.md
│  ├─ ai-transparency.md
│  ├─ credits.md
│  └─ faq.md
├─ firmware/
├─ hardware/
├─ 3d-files/
├─ assets/
├─ examples/
└─ community/
```

---

## AI transparency

This project was developed through a mix of hands-on prototyping, open-source tools, and AI-assisted coding/documentation workflows.

AI was used to help with things like:

- code drafting
- revision
- debugging support
- documentation structure
- explanatory writing

All final decisions, testing, and integration were carried out by the project author.

More detail: [`docs/ai-transparency.md`](docs/ai-transparency.md)

---

## Open-source credits

This project depends on the work of many open-source tools, libraries, and communities.

That includes things like:

- MicroPython
- ESP32 tools and utilities
- JQ6500 libraries
- CAD and 3D tools
- BumpMesh
- slicers and fabrication software
- community examples and references

See [`docs/credits.md`](docs/credits.md).

---

## Licensing

The intention is to keep this project as open as possible.

Suggested split:

- **Code**: MIT
- **Documentation, images, and design files**: CC BY 4.0

That means people can build, adapt, share, and remix the project, including commercially, as long as they give credit.

See:

- [`LICENSE-CODE`](LICENSE-CODE)
- [`LICENSE-DESIGN`](LICENSE-DESIGN)

---

## If you build one

Please show me.

Open an issue, share a photo, link your remix, or send back improvements. These hands are meant to spread.

---

## Links

Add your project links here:

- Studio Tommy
- MakerWorld
- exhibition documentation
- website
- contact
