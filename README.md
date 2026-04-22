# Helping Hands

*An open-source interactive sculpture platform for sharing stories from possible futures through touch, sound, light, and connected public installation.*

![Helping Hands hero image](assets/images/hero.jpg)

Helping Hands is a modular system for creating interactive cast-hand sculptures that invite people to physically hold, listen to, and reflect on shared stories of the future.

At its core, the project combines tactile sculpture, embedded electronics, printed hardware, audio playback, and open documentation. A single hand can operate as a standalone interactive object, but the wider system is designed as a connected platform: multiple hands can be configured as part of larger installations, responding across a shared environment and extending the project from one encounter into a distributed public experience.

This repository is the main home of the project. It brings together the firmware, 3D files, build logic, hardware notes, casting methods, setup workflow, and customisation guidance needed to understand, reproduce, and adapt the system.

---

## What this project includes

Helping Hands is not just one object. It is a wider build ecosystem that includes:

- interactive hand sculptures
- modular enclosure and mounting parts
- a printed PCB-style internal hardware system
- firmware for interaction, timing, and audio behaviour
- a guided flashing and configuration workflow
- casting tools and alignment jigs
- customisation guidance for surfaces and enclosure forms
- a structure for connected multi-hand installations
- open documentation intended to support replication and remixing

MakerWorld, print repositories, or other public posts may host individual assets, but this GitHub repository is the canonical source for the full system.

---

## Why make it open?

Helping Hands is intended to travel.

The project is designed so that other people can build their own versions, adapt the enclosure and interaction, swap in new stories or local voices, and carry the idea into new places and communities. The goal is not simply to preserve one finished artefact, but to make the system itself reusable.

By keeping the project open, this repository aims to support:

- individual makers and students
- artists and designers
- workshop facilitators
- community organisers
- researchers and educators
- anyone interested in public, tactile, story-led interaction

If you build from this repo, remix part of it, or carry the idea into a new context, please credit the original project and share back what you learn where possible.

---

## System overview

A typical Helping Hands build brings together five main layers:

### 1. The hand
The hand is the main public interface. It is cast as a tactile, human-scale object designed to be held, noticed, and approached instinctively.

### 2. The enclosure
The enclosure houses the electronics and gives the project a repairable, printable, and adaptable structural body. The enclosure system is modular and can be reworked for different installation contexts.

### 3. The internal hardware system
The build uses accessible off-the-shelf electronics organised through a replicable internal layout, including a printed PCB-style carrier approach for easier assembly, maintenance, and documentation.

### 4. The firmware and setup workflow
The device logic handles touch interaction, timed behaviour, lighting, audio playback, and configuration. A companion setup workflow supports flashing, variable tuning, RTC time setting, and media/configuration management as part of the broader build system.

### 5. The wider networked platform
Helping Hands is designed as a connected installation platform, where multiple hands can respond together, communicate across a space, and contribute to a larger shared experience.

---

## Core features

- tactile hand-based interaction
- cast and printed hybrid build process
- ESP32-based control system
- audio playback via JQ6500
- RTC-supported timed behaviour
- modular enclosure system
- printed PCB-style internal organisation
- configurable firmware structure
- guided setup and flashing workflow
- support for connected multi-hand installations
- open files for replication, modification, and reuse

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
│  ├─ quick-start.md
│  ├─ build-guide.md
│  ├─ bill-of-materials.md
│  ├─ hardware.md
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

### To understand the project
Read:

1. [`docs/overview.md`](docs/overview.md)
2. [`docs/build-guide.md`](docs/build-guide.md)
3. [`docs/casting-hands.md`](docs/casting-hands.md)
4. [`docs/firmware.md`](docs/firmware.md)

### To build a hand
Go to:

1. [`docs/quick-start.md`](docs/quick-start.md)
2. [`docs/bill-of-materials.md`](docs/bill-of-materials.md)
3. [`docs/wiring.md`](docs/wiring.md)
4. [`docs/3d-prints.md`](docs/3d-prints.md)
5. [`docs/flashing.md`](docs/flashing.md)

### To customise the enclosure
Start with:

- [`docs/enclosure-customisation.md`](docs/enclosure-customisation.md)

This includes guidance on changing forms, adjusting surfaces, and developing custom visual identities using open workflows, including BumpMesh.

---

## Build ecosystem

The repository is structured around the full making process, not just code.

### Hardware
The hardware side of the project combines off-the-shelf electronics, printed components, connectors, fixings, and power systems. The build documentation is intended to make the physical assembly legible and repeatable.

### 3D prints
This includes enclosure parts, internal carrier parts, casting tools, jigs, and editable models where available. The 3D system is part of what makes the project reproducible and adaptable.

### Casting
Casting is a central part of the build. The project includes process guidance for moulding and casting hands, positioning hardware connections, and using printed tools for repeatable assembly and bolt alignment.

### Firmware
The firmware layer brings together interaction logic, audio handling, timed behaviours, and configurable variables for tuning the build to different contexts.

### Setup workflow
Helping Hands includes a guided setup approach for programming and configuring devices as part of a broader build ecosystem. This covers firmware flashing, RTC setup, configuration values, and media preparation.

### Connected installations
Beyond a single sculpture, the system is designed to support installations made up of multiple communicating hands, allowing experiences to spread spatially and socially through a site.

---

## Firmware files

Current firmware components include:

- `firmware/main.py` — core interaction logic
- `firmware/rtc.py` — RTC support and time handling
- `firmware/jq6500.py` — audio module communication
- `firmware/config.py.example` — configuration template
- `firmware/tools/` — supporting setup and workflow utilities

The firmware structure is documented in [`docs/firmware.md`](docs/firmware.md).

---

## 3D prints and editable files

This repository is intended to hold several categories of printable and editable assets:

- hand-related printed parts
- enclosure/body parts
- printed PCB-style carrier parts
- casting alignment tools
- bolt placement jigs
- editable CAD files
- installation-specific adaptations where relevant

See [`docs/3d-prints.md`](docs/3d-prints.md) for file descriptions, print settings, and assembly notes.

---

## Casting hands

The hand itself is a key part of the project’s identity and interaction.

The casting guide is intended to cover:

- moulding and casting workflow
- materials and process notes
- how printed tools are used to support repeatability
- bolt and fixing alignment
- lessons learned from testing and iteration

See [`docs/casting-hands.md`](docs/casting-hands.md).

---

## Customisation

Helping Hands is designed to be adapted.

Possible areas of customisation include:

- enclosure form
- surface textures
- embedded text or patterning
- LED behaviour
- timing and interaction states
- audio content
- installation context
- local storytelling themes

The enclosure customisation guide includes notes on using **BumpMesh** and related workflows to modify surfaces, add new identity layers, and create site-specific versions of the system.

See [`docs/enclosure-customisation.md`](docs/enclosure-customisation.md).

---

## Documentation approach

This repository is written in a maker-first voice.

It aims to support people coming from different directions, including making, art, design, electronics, installation, and public engagement. The documentation is therefore intended to be:

- clear before technical
- visual where possible
- practical and replicable
- honest about process
- open to modification and reuse

---

## AI transparency

This project was developed through a combination of hands-on prototyping, open-source tools, and AI-assisted coding and documentation workflows.

Generative AI was used to support parts of the development process, including:

- code drafting
- code revision
- debugging assistance
- documentation structuring
- explanatory writing

All final decisions, testing, selection, and integration were carried out by the project author.

A fuller note on AI use can be found in [`docs/ai-transparency.md`](docs/ai-transparency.md).

---

## Safety

Helping Hands is a physical computing and fabrication project.

Please take care when working with:

- batteries and charging boards
- power circuits and wiring
- soldering equipment
- speakers and audio electronics
- casting materials
- cutting tools, drills, and heated hardware
- public installation contexts

You are responsible for checking that any build is safe, legal, and appropriate for its intended use.

---

## Open-source tools and credits

This project depends on the work of many open-source tools, libraries, and communities. These should be credited clearly and consistently.

This may include, depending on the workflow used:

- MicroPython
- ESP32 tools and utilities
- JQ6500 libraries
- CAD and 3D tools
- BumpMesh
- slicer software
- community examples, scripts, and references that informed the build

A fuller list should be maintained in [`docs/credits.md`](docs/credits.md).

If something should be credited and is missing, please open an issue or pull request.

---

## Licensing

The intention of this repository is to keep the project as open as possible.

Suggested structure:

- **Code**: MIT License
- **Documentation, images, and design files**: CC BY 4.0

This means others can build, adapt, share, and remix the project, including commercially, provided attribution is given.

See:

- [`LICENSE-CODE`](LICENSE-CODE)
- [`LICENSE-DESIGN`](LICENSE-DESIGN)

---

## Contributing

Contributions are welcome, including:

- firmware improvements
- bug fixes
- clearer build documentation
- alternative hardware notes
- remixed enclosure files
- better casting tools or jigs
- improved diagrams
- translations
- photos, examples, and derivatives

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution guidance.

---

## Planned documentation pages

The repository is designed to grow into a full project guide covering:

- overview
- quick start
- build guide
- bill of materials
- hardware
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

If you make your own version of Helping Hands, I would love to see it.

Please consider:

- opening an issue
- sharing images or video
- linking back to this project
- documenting your changes
- contributing improvements back to the repo

These hands are meant to be connected, not just electronically, but socially.

---

## Links

Add your preferred project links here, for example:

- project website
- Studio Tommy
- MakerWorld
- exhibition documentation
- contact email
