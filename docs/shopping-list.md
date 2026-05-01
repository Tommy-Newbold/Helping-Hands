# Shopping List

This is the basic shopping list for building a Helping Hand. It includes the core electronics, hand casting materials, and general hardware.

> [!NOTE]  
> Links are starting points, not fixed suppliers. AliExpress listings change constantly, so check the photos, dimensions, pinouts, reviews, and delivery times before ordering.

---

## Quick build options

There are two common build routes:

| Build type | Use this if | Main difference |
| --- | --- | --- |
| Indoor / exhibition build | You are making a display hand or prototype | Plaster hand, simpler power setup |
| Outdoor / public build | You need a stronger, more weather-resistant hand | Cold-cast polyurethane hand, better sealing, more robust power |

For the full build process, see:

[`docs/instructions.md`](./instructions.md)

For printing guidance, see:

[`docs/3d-printing.md`](./3d-printing.md)

---

## Electronics

| Part | Notes | Link |
| --- | --- | --- |
| ESP32 WROOM dev board | Main controller. Use a common ESP32-WROOM development board with USB. | [AliExpress search](https://www.aliexpress.com/w/wholesale-ESP32-WROOM-dev-board.html) |
| JQ6500 MP3 player | Audio playback module. Usually loaded over USB Mini. | [AliExpress search](https://www.aliexpress.com/w/wholesale-JQ6500-MP3-player-module.html) |
| Adafruit BQ25185 solar charger | Recommended for solar installs. USB/DC/solar charging with 5V boost output. | [Adafruit product page](https://www.adafruit.com/product/6106) |
| DS3231 RTC module | Optional, but improves day/night and quiet-hour reliability. | [AliExpress search](https://www.aliexpress.com/w/wholesale-DS3231-RTC-module.html) |
| 18650 battery holder | For a removable Li-ion cell. Choose one with leads or a JST connector where possible. | [AliExpress search](https://www.aliexpress.com/w/wholesale-18650-battery-holder-JST.html) |
| 18650 Li-ion cell | Only Purchase Cells from a supplier & producer you know and trust, the supplied link is for the UK | [Nu Battery](https://www.nubattery.co.uk/) |
| 3W 8Ω 67mm speaker driver | Main audio output. Check the diameter against your printed speaker mount. | [AliExpress search](https://www.aliexpress.com/w/wholesale-3W-8-ohm-67mm-speaker.html) |
| 24 LED COB / NeoPixel ring 67mm OD | Light feedback. Use a 5V addressable RGB ring, WS2812B/NeoPixel compatible. | [AliExpress search](https://www.aliexpress.com/w/wholesale-24-bit-WS2812B-LED-ring-5V.html) |
| Key switch | For turning the hand on/off. Small two-position key switches work well. | [AliExpress search](https://www.aliexpress.com/w/wholesale-small-key-switch-2-position.html) |
| Waterproof USB-C connector | For external charging. | [AliExpress search](https://www.aliexpress.com/w/wholesale-waterproof-USB-C-panel-mount-connector.html) |

Optional BMS if solar is not required:

| 1S Li-ion charger/protection board with 5V boost | Cheaper non-solar power option. Often sold as an 18650 charger/protection/boost module. | [AliExpress search](https://www.aliexpress.com/w/wholesale-18650-lithium-battery-charger-protection-5V-boost-module.html) |

### Electronics buying notes

- Check voltage carefully. Most of the system expects **5V power**.
- Check connector types before ordering battery holders and charger boards.
- Avoid very cheap 18650 cells with unrealistic capacity claims.
- Buy a few spare ESP32 boards, LED rings, and small modules if budget allows.
- The cheap non-solar power board should be for a **single-cell Li-ion / 18650 setup** with charging, protection, and 5V boost.
- “BMS board with 5V buck” is probably better written as **1S Li-ion charger/protection board with 5V boost**, because a single 18650 needs to be boosted up to 5V.

---

## Hand casting materials

There are two hand-making routes:

1. Plaster hand
2. Cold-cast polyurethane hand

A plaster hand is cheaper and suitable for indoor use or protected displays. A cold-cast hand is stronger and more suitable for outdoor or public-facing installs.

---

### For plaster hands

| Material | Notes | Link |
| --- | --- | --- |
| Alginate | For making the hand mould. Around 500g per hand is a useful starting point. | [AliExpress search](https://www.aliexpress.com/w/wholesale-alginate-life-casting.html) |
| Herculite plaster | Strong casting plaster. Herculite 2 or similar is recommended. | [AliExpress search](https://www.aliexpress.com/w/wholesale-Herculite-2-plaster.html) |
| M5 threaded rod | Embedded mounting point. Cut to length before casting. | [AliExpress search](https://www.aliexpress.com/w/wholesale-M5-threaded-rod-stainless-steel.html) |
| Mixing cups / tubs | For alginate and plaster. Use containers you do not mind ruining. | [AliExpress search](https://www.aliexpress.com/w/wholesale-disposable-mixing-cups-resin.html) |
| Mixing sticks | Disposable sticks are useful. | [AliExpress search](https://www.aliexpress.com/w/wholesale-wooden-mixing-sticks.html) |
| Gloves | Strongly recommended. | [AliExpress search](https://www.aliexpress.com/w/wholesale-nitrile-gloves.html) |

---

### For cold-cast “metal” hands

| Material | Notes | Link |
| --- | --- | --- |
| Alginate | For the original hand mould. | [AliExpress search](https://www.aliexpress.com/w/wholesale-alginate-life-casting.html) |
| Herculite plaster | For the master / test casts. | [AliExpress search](https://www.aliexpress.com/w/wholesale-Herculite-2-plaster.html) |
| M5 threaded rod | Embedded mounting point. | [AliExpress search](https://www.aliexpress.com/w/wholesale-M5-threaded-rod-stainless-steel.html) |
| Brush-on silicone | For reusable moulds. Smooth-On Rebound 25 or similar. | [AliExpress search](https://www.aliexpress.com/w/wholesale-brush-on-silicone-rubber-mould-making.html) |
| Atomised aluminium powder | For the cold-cast metal effect. Other atomised metals can also be used. | [AliExpress search](https://www.aliexpress.com/w/wholesale-atomized-aluminium-powder-resin-casting.html) |
| Polyurethane resin | Final cast material. A short pot-life resin works, but move quickly. | [AliExpress search](https://www.aliexpress.com/w/wholesale-polyurethane-casting-resin.html) |
| Gloves and respirator | Follow resin safety guidance. | [AliExpress search](https://www.aliexpress.com/w/wholesale-organic-vapour-respirator-resin.html) |

> [!WARNING]  
> Resin, silicone, metal powders, and solvents can be hazardous. Follow the manufacturer’s safety guidance, work with ventilation, and use appropriate PPE.

---

## Other hardware and consumables

| Part | Notes | Link |
| --- | --- | --- |
| 147mm gasket | For the enclosure seal. Confirm size against your enclosure version. | [AliExpress search](https://www.aliexpress.com/w/wholesale-147mm-rubber-gasket.html) |
| Jubilee clips / screws | For mounting to poles, railings, or street furniture. | [AliExpress search](https://www.aliexpress.com/w/wholesale-jubilee-hose-clamps-stainless-steel.html) |
| Wall plugs / anchors | Depends on installation site. | [AliExpress search](https://www.aliexpress.com/w/wholesale-wall-plugs-screws-assortment.html) |
| Heat shrink | For safer wiring and strain relief. | [AliExpress search](https://www.aliexpress.com/w/wholesale-heat-shrink-tubing-assortment.html) |
| Silicone sealant | Optional. Use carefully so the enclosure can still be serviced. | [AliExpress search](https://www.aliexpress.com/w/wholesale-clear-silicone-sealant-waterproof.html) |
| Labels / plaque | For storyteller identity and interaction prompt. | [AliExpress search](https://www.aliexpress.com/w/wholesale-small-engraved-metal-plaque.html) |
| Patience | Not optional. | — |

---

## Minimum useful kit

If you are just trying to get one hand working on the bench, start with:

- ESP32 WROOM dev board
- JQ6500 MP3 module
- Speaker
- LED ring
- DS3231 RTC module
- 18650 holder
- Power board
- 18650 cell
- Key switch
- Copper tape
- Flexible wire
- One plaster hand

You can add the cold-cast hand, waterproof connector, solar charging, and final mounting hardware later.

---

## Buying checklist

### Electronics

- [ ] ESP32 WROOM dev board
- [ ] JQ6500 MP3 player
- [ ] Power board: BQ25185 or cheaper 5V boost option
- [ ] 18650 battery holder
- [ ] 18650 Li-ion cell
- [ ] 3W 8Ω speaker
- [ ] 24 LED ring
- [ ] Key switch
- [ ] USB Mini cable
- [ ] DS3231 RTC module
- [ ] Copper tape
- [ ] Flexible wire

### Optional / install-dependent electronics

- [ ] Waterproof USB-C connector
- [ ] Solar panel, if using the BQ25185 for solar charging
- [ ] Spare JST connectors
- [ ] Spare header pins

### Casting

- [ ] Alginate
- [ ] Herculite plaster
- [ ] M5 threaded rod
- [ ] Mixing cups
- [ ] Mixing sticks
- [ ] Gloves

### Cold casting

- [ ] Brush-on silicone
- [ ] Atomised aluminium powder
- [ ] Polyurethane resin
- [ ] Respirator / PPE

### Installation

- [ ] 147mm gasket
- [ ] Jubilee clips or screws
- [ ] Wall plugs / anchors
- [ ] Heat shrink
- [ ] Silicone sealant
- [ ] Plaque or label
