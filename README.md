# Helping-Hands

# Helping Hands

*An open-source interactive sculpture platform for sharing stories from possible futures through touch, sound, and public installation.*

![Helping Hands hero image](assets/images/hero.jpg)

## What is this?

Helping Hands is a public-facing interactive sculpture project built around cast hands, simple electronics, audio playback, and modular 3D-printed hardware.

When someone touches a hand, it responds with light and sound. In the larger vision, multiple hands can also respond together, forming a connected network of voices and stories. The system is designed to be **replicable, adaptable, and open**, so other people can build their own versions, remix the hardware, and use the platform in their own places and communities.

This repository is the main source for the project. It brings together:

- firmware
- hardware notes
- 3D print files
- casting tools and process notes
- build instructions
- documentation for customisation
- development notes for the flashing/configuration tool

MakerWorld, print repositories, or other public postings may host individual print files, but this GitHub repository is the canonical home of the full system.

---

## Why make it open?

Helping Hands is meant to spread.

This is not just a single finished object. It is a system for making more hands, more stories, and more public interactions possible. The goal is to let others:

- build their own version
- adapt the enclosure and hand form
- swap in local stories, voices, or themes
- improve the firmware and documentation
- carry the project into new places and contexts

If you build one, adapt one, or learn from this repo, please credit the original project and share back improvements where you can.

---

## Current status

This is a **working but evolving** open-source project.

### Stable enough to build from
- core hand interaction
- ESP32-based firmware
- audio playback via JQ6500
- RTC support
- modular printed enclosure parts
- casting workflow and alignment tools

### Still developing
- multi-hand networking features
- improved setup and flashing workflow
- dedicated desktop flashing/configuration tool
- more polished documentation and build media

Some files and processes may change as the project develops.

---

## Repository structure

```text
helping-hands/
├─ README.md
├─ LICENSE-CODE
├─ LICENSE-DESIGN
├─ CONTRIBUTING.md
├─ CHANGELOG.md
├─ docs/
│  ├─ overview.md
│  ├─ build-guide.md
│  ├─ quick-start.md
│  ├─ hardware.md
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
│  ├─ main.py
│  ├─ rtc.py
│  ├─ jq6500.py
│  ├─ config.py.example
│  └─ tools/
├─ hardware/
│  ├─ bom/
│  ├─ wiring-diagrams/
│  ├─ schematics/
│  └─ supplier-notes/
├─ 3d-files/
│  ├─ hand/
│  ├─ enclosure/
│  ├─ printed-pcb-system/
│  ├─ casting-tools/
│  └─ editable/
├─ assets/
│  ├─ images/
│  ├─ diagrams/
│  └─ video/
├─ examples/
│  ├─ audio-packs/
│  ├─ configurations/
│  └─ installation-examples/
└─ community/
   ├─ workshop-examples/
   └─ remix-gallery/
```

---

## Start here

### I want to understand the project
Read these first:

1. [`docs/overview.md`](docs/overview.md)
2. [`docs/build-guide.md`](docs/build-guide.md)
3. [`docs/casting-hands.md`](docs/casting-hands.md)
4. [`docs/firmware.md`](docs/firmware.md)

### I want to build one
Go to:

1. [`docs/quick-start.md`](docs/quick-start.md)
2. [`docs/bill-of-materials.md`](docs/bill-of-materials.md)
3. [`docs/wiring.md`](docs/wiring.md)
4. [`docs/3d-prints.md`](docs/3d-prints.md)
5. [`docs/flashing.md`](docs/flashing.md)

### I want to customise the enclosure
Start with:

- [`docs/enclosure-customisation.md`](docs/enclosure-customisation.md)

This includes notes on editing surfaces and adding custom textures or graphics using open-source-friendly workflows, including BumpMesh.

---

## What you need to build a hand

The exact build may vary over time, but a typical hand currently uses:

- ESP32 development board
- JQ6500 audio module
- RTC module
- speaker
- LED ring or other light output
- battery / power board
- printed enclosure parts
- cast hand component
- fixings, wiring, and connectors

See [`docs/bill-of-materials.md`](docs/bill-of-materials.md) for the detailed parts list, rough costs, and sourcing notes.

---

## Main parts of the system

### 1. The hand
The cast hand is the main public interface. It is meant to feel tactile, human, and inviting.

### 2. The enclosure
The enclosure holds the electronics and acts as the base structure for the hand. It is designed to be printable, repairable, and modifiable.

### 3. The printed PCB-style system
This project also uses a 3D-printed board/carrier approach for some internal organisation and easy replication. This makes the build more accessible to people who want a tidy internal layout without designing a custom PCB.

### 4. The firmware
The firmware runs the interaction logic, audio playback triggers, timing behaviour, and related device functions.

### 5. The wider system
In its broader form, Helping Hands is not just one device. It is a replicable platform for distributed public interactions, shared voices, and connected installations.

---

## Firmware

Current firmware files include:

- `firmware/main.py` — main interaction logic
- `firmware/rtc.py` — RTC support and time handling
- `firmware/jq6500.py` — audio module communication
- `firmware/config.py.example` — configuration template

The firmware is documented in [`docs/firmware.md`](docs/firmware.md).

---

## Flashing and setup

A more guided flashing/configuration tool is in development.

For now, setup is handled manually. This includes:

- flashing firmware to the ESP32
- setting configuration values
- setting RTC time
- uploading audio tracks
- testing hardware connections

See [`docs/flashing.md`](docs/flashing.md) for the current workflow.

---

## 3D prints

This repository includes several types of printable files:

- hand-related parts
- enclosure/body parts
- printed PCB-style carrier parts
- casting alignment tools
- jigs for bolt positioning or repeatable assembly
- editable source files where available

See [`docs/3d-prints.md`](docs/3d-prints.md) for file descriptions, print guidance, and assembly notes.

---

## Casting hands

The casting side of the project is a key part of the build, not an optional extra.

The casting documentation covers:

- how the hand is made
- moulding and casting notes
- bolt alignment tools
- how 3D-printed parts are used to make casting more repeatable
- lessons learned from the process

See [`docs/casting-hands.md`](docs/casting-hands.md).

---

## Customisation

Helping Hands is designed to be changed.

You can customise:

- enclosure form
- surface textures
- light behaviour
- audio content
- mode timing
- installation context
- narrative theme

The enclosure customisation guide includes notes on using **BumpMesh** and related workflows to edit surfaces and add new visual identities to the box or body.

See [`docs/enclosure-customisation.md`](docs/enclosure-customisation.md).

---

## Documentation philosophy

This repo is intended to be useful to:

- makers
- artists
- designers
- students
- researchers
- community organisers
- technically curious builders

Because of that, the documentation aims to be:

- accessible first
- technical where needed
- honest about what is finished and what is experimental
- open about mistakes, revisions, and lessons learned

---

## AI transparency

Some parts of the software and documentation for this project were developed with the assistance of generative AI tools.

This includes support with:

- code drafting
- code revision
- debugging assistance
- documentation structuring
- explanatory writing

All AI-assisted material has been reviewed, selected, edited, and integrated by the project author, but it may still contain mistakes, oversights, or inefficient solutions.

If you are building from this repository:

- review the code before use
- test carefully
- treat all electrical and battery-related work with caution
- do not assume any generated code is production-ready

A fuller statement is available in [`docs/ai-transparency.md`](docs/ai-transparency.md).

---

## Safety

This is an experimental physical computing project.

Please use care when working with:

- batteries and charging boards
- power circuits
- soldering equipment
- speakers and audio electronics
- casting materials
- tools, drills, blades, and heated parts
- public installation contexts

You are responsible for checking that any build is safe, legal, and appropriate for its use context.

---

## Open-source tools and credits

This project depends on the work of many open-source tools, libraries, platforms, and communities. These should be credited clearly and consistently.

This may include, depending on the build and workflow used:

- MicroPython
- ESP32 toolchains and utilities
- JQ6500 libraries
- CAD and 3D tools
- BumpMesh
- slicer software
- any scripts, libraries, or examples that informed the build

A fuller list should be kept in [`docs/credits.md`](docs/credits.md).

If I have missed a credit that should be included, please open an issue or pull request.

---

## Licensing

The intention of this repository is to keep the project **as open as possible**.

Suggested structure:

- **Code**: MIT License
- **Documentation, images, and design files**: CC BY 4.0

This means people can build, adapt, and share the project, including commercially, as long as they provide attribution.

See:

- [`LICENSE-CODE`](LICENSE-CODE)
- [`LICENSE-DESIGN`](LICENSE-DESIGN)

---

## Contributing

Contributions are welcome.

This might include:

- bug fixes
- code improvements
- better wiring documentation
- clearer assembly instructions
- remixed enclosure files
- improved casting jigs
- alternative BOM options
- photos, examples, or translations

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution guidelines.

---

## Planned documentation pages

These are the core docs this repo is intended to grow into:

- overview
- quick start
- build guide
- bill of materials
- wiring
- firmware
- flashing
- networking
- 3D prints
- printed PCB-style system
- casting hands
- enclosure customisation
- AI transparency
- credits
- FAQ

---

## If you build one

If you make your own version of Helping Hands, I would love to hear about it.

Please consider:

- opening an issue
- sharing photos or videos
- linking back to this project
- documenting your changes
- contributing improvements back to the repo

These hands are meant to be connected, not just electronically, but socially.

---

## Project status note

This repository documents a real project and an evolving open-source build process. Some files, workflows, and scripts may be incomplete, experimental, or later replaced by improved versions.

Check documentation status notes, commit history, and release notes before relying on any specific workflow.

---

## Contact / project links

Add your preferred links here, for example:

- project website
- Studio Tommy
- MakerWorld
- exhibition documentation
- contact email

