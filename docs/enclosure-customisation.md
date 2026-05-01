# Enclosure Customisation

This guide covers simple ways to customise the Helping Hands enclosure, from surface decoration and painting to adding custom texture using displacement tools.

The enclosure has been designed to be adaptable. You can keep it plain, paint it, decorate it for a specific project, or generate a textured version for a more site-specific build.

---

## Quick overview

Common customisation options include:

- Painting the enclosure
- Adding project-specific decoration
- Using coloured or translucent filament
- Adding vinyl graphics or labels
- Adding physical props or attachments
- Applying custom surface texture with displacement

For the main build guide, see:

[`docs/instructions.md`](./instructions.md)

For print settings, see:

[`docs/3d-printing.md`](./3d-printing.md)

---

<details open>
<summary><strong>1. Simple decoration</strong></summary>

## 1. Simple decoration

The simplest way to customise the enclosure is through decoration.

For example, in the original urban flooding project, the enclosure was styled with visual references to **life rings**, public safety equipment, and civic infrastructure.

### Ideas

You could customise the enclosure with:

- Painted colour bands
- Vinyl lettering
- Warning-style graphics
- Project logos
- Local place names
- Numbered wayfinding labels
- Small plaques
- Reflective tape
- Weathering or ageing effects
- Attached props or symbolic objects

### Keep it functional

When decorating the enclosure, avoid covering:

- Speaker openings
- Cable holes
- Screw holes
- Key switch access
- LED diffusion areas
- Mounting slots
- Any areas that need to seal cleanly

</details>

---

<details open>
<summary><strong>2. Painting the enclosure</strong></summary>

## 2. Painting the enclosure

The enclosure can be painted if you want a specific finish or colour scheme.

### Basic painting process

1. Lightly sand the surface
2. Clean off dust and grease
3. Use a plastic-compatible primer
4. Apply thin coats of paint
5. Let each coat dry fully
6. Add a clear coat if needed

### Notes for translucent prints

If you are using translucent PET-G for the lighting effect, avoid painting areas where you want light to pass through.

You can also mask parts of the enclosure so that only selected areas glow.

</details>

---

<details open>
<summary><strong>3. Adding custom surface texture with BumpMesh</strong></summary>

## 3. Adding custom surface texture with BumpMesh

For customising the outside body texture, check out the open source tool:

[BumpMesh](https://bumpmesh.com)

BumpMesh lets you apply bump maps and displacement textures to 3D models. This can be used to give the enclosure a custom surface pattern before printing.

### Best use cases

BumpMesh is useful for adding:

- Subtle surface grain
- Project-specific patterns
- Topographic textures
- Water ripple textures
- Fabric-like texture
- Civic or architectural surface references
- Decorative patterns that help hide layer lines

### Recommended approach

You will usually get the best results by:

1. Applying textures to individual walls rather than the whole model at once
2. Keeping the texture subtle
3. Using textures on surfaces that are perpendicular to the build plate
4. Using cylindrical projection mapping where appropriate
5. Testing on a small sample before printing the full enclosure

### Why perpendicular walls work best

Textures tend to print most cleanly when they are on vertical walls.

This is because the printer can build the displacement detail gradually in the layer lines, rather than trying to resolve it across flat top surfaces.

### Cylindrical projection mapping

For rounded enclosure bodies, cylindrical projection mapping can help the texture wrap more naturally around the form.

This is especially useful if you want a continuous pattern around the outside of the enclosure.

</details>

---

## Customisation checklist

Before printing or installing a customised enclosure, check:

- [ ] Decoration does not block the speaker
- [ ] Decoration does not block the key switch
- [ ] Decoration does not block mounting holes
- [ ] Paint does not prevent the enclosure from closing
- [ ] Paint does not cover areas that need to glow
- [ ] Texture is not too deep for reliable printing
- [ ] Textured surfaces have been test printed
- [ ] Mounting and sealing surfaces are still flat
- [ ] The final enclosure still feels appropriate for public interaction

---

## Notes

Customisation should support the purpose of the hand.

A good enclosure design should still feel:

- Approachable
- Robust
- Easy to understand
- Safe to touch
- Connected to the place or project it belongs to
