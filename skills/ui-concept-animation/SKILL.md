---
name: ui-concept-animation
description: >-
  Bring a product UI to life from a screenshot or mockup: an animated scene of
  the interface with a choreographed interaction — cursor journey, panels
  sliding in, states changing — plus captions or tight narration naming the
  benefit. Use when the user says "animate this screenshot", "animate this
  mockup", "make our UI move", "UI animation for this feature", "turn this
  design into a demo animation", or shares a product screenshot/mockup and
  wants a short polished clip showcasing an interaction.
license: Apache-2.0
metadata:
  author: clueso
  category: motion-graphics
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# UI Concept Animation

Turn a static screenshot or mockup into a short animated product moment: the
real interface, one interaction choreographed across it, and a caption or
narration line naming the benefit as it happens. The output is a crisp 10-30
second clip for launches, changelogs, landing pages, and social.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

Ask for anything missing rather than inventing it:

1. **The UI** — a screenshot or mockup image (preferred), or a precise
   description of the interface if no image exists.
2. **The interaction to showcase** — what happens: a click path, a panel
   opening, a state changing, data filling in.
3. **Feature name** and the one-line benefit it delivers.
4. **Output format** — video, or a GIF-style loop (see step 6).
5. Brand colors/fonts for captions and framing, or "use workspace branding".

## Workflow

### 1. Set up

Confirm the target workspace with the user. Look for an existing UI-showcase
template that fits; offer a strong match before building from scratch.

### 2. Ground the animation in the real UI

Bring the user's image in and use it as the **visual reference** for the
animated scene — the generated interface must be recognizably theirs: same
layout, same colors, same labels. Never substitute an invented mockup for a
real product's UI; if the image is too low-resolution to read, ask for a
better capture instead of guessing at details.

### 3. Choreograph one interaction

Script the interaction as a beat-by-beat sequence before generating anything —
typically **3-5 beats** in a single scene (or two scenes for a before/after):

- **Establish** — the UI settles in, framed with breathing room on a brand-
  colored backdrop; a half-second of stillness so viewers orient.
- **The journey** — the cursor (or touch point) moves with intent: one
  deliberate path, easing into each stop, never teleporting. Panels slide,
  menus open, toggles flip in reaction to it.
- **The change** — the state visibly updates: the result appears, the number
  refreshes, the view transforms. This is the money moment; give it the most
  motion and a subtle emphasis (a gentle zoom toward the changed region works
  well).
- **Rest** — hold the end state long enough to absorb.

One interaction per video. If the user wants three features shown, that's
three beats of one flow or three separate clips — never a frantic tour.

### 4. Name the benefit at each moment

Pair the choreography with words, one of two ways:

- **Captions** (default for social/changelog): short on-brand text labels —
  3-6 words — appearing in sync with each beat, naming the benefit, not the
  mechanics ("Approvals in one click", not "Click the approve button").
- **Tight narration**: 2-3 spoken sentences max. **Estimate the spoken length
  first and size the scene timing to it**, so the state change lands exactly
  on the sentence that names it.

### 5. Review

Check the loop: the UI is faithful to the source image, the cursor path reads
at a glance, text is legible at video scale, every caption lands on its beat,
brand colors frame the piece. Share the review link with the user and get
their approval **before** exporting.

### 6. Export in the requested format

Export as video by default. If the user asked for a GIF: a directly
downloadable GIF file isn't always available at export — offer the nearest
supported path (a short, seamlessly looping video export, or a GIF produced
through a help-article embed) and confirm which they want before delivering.

## What to avoid

- Music or sound effects — never add them.
- Cursor ballet — wandering pointers, double-back paths, or speed that outruns
  comprehension.
- Animating every region at once; motion means attention, so spend it on the
  one thing that changed.
- Captions that transcribe UI labels instead of naming the benefit.
