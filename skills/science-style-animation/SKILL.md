---
name: science-style-animation
description: >-
  Teach a concept, mechanism, or process as an educational animation with
  labeled diagrams, step-by-step cause-and-effect scenes, and measured
  teacherly narration. Use when the user says "science-style animation",
  "educational animation about X", "explain how X works with a diagram video",
  "teaching video for this concept", "animate this process", or has a concept,
  system, or workflow they want taught visually to learners.
license: Apache-2.0
metadata:
  author: clueso
  category: motion-graphics
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Science-Style Animation

Build an educational animation in the style of a good science video: a concept
decomposed into cause-and-effect steps, each shown as a labeled diagram scene
whose annotations appear exactly when the narration mentions them, closed by a
recap of the whole system. Made for customer education and L&D teams teaching
how something actually works.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

Ask for anything missing rather than inventing it:

1. **The concept or process to teach** — a mechanism, system, or workflow.
2. **Audience level** — novice or expert; this sets vocabulary and how much you
   may assume.
3. **Source material** (optional) — a doc, article, or SME notes. If provided, it
   is the ground truth; never contradict it or invent facts beyond it.
4. **Length** — let the concept set it if unspecified; most single concepts teach
   well in 60-120 seconds.
5. Brand colors/fonts, or "use workspace branding".

## Workflow

### 1. Set up

Confirm the target workspace with the user. Look for an existing educational or
diagram-style template that fits; offer a strong match before building fresh.

### 2. Decompose the concept

Break the concept into a **stepwise cause-and-effect chain**: A happens, which
causes B, which enables C. Each link in the chain becomes one scene — typically
**4-7 mechanism scenes**, plus an opening framing scene and a closing recap.
If a step hides two mechanisms, split it; a scene teaches exactly one thing.
Order matters: never show an effect before its cause has been taught.

Write the narration for each step in a measured, teacherly voice — short
sentences, plain words scaled to the audience level, new terms defined the
first time they appear. **Estimate the spoken length of the full narration
before laying out scenes**; educational pacing should feel unhurried, so if it
runs long, cut scope (teach less), don't compress delivery.

Show the user the step chain and narration before building.

### 3. Design the diagram scenes

Each mechanism scene is a **labeled diagram**: a clear visual of the parts
involved, with text labels, arrows, and callouts annotating them. The craft
rules:

- One consistent diagram style across all scenes — same palette (brand colors,
  with one accent reserved for "the thing currently being explained"), same
  line weight and label typography, same level of abstraction throughout.
- **Annotations appear exactly when narrated.** A label or arrow enters the
  moment the voice names that part — never earlier, never as a pre-loaded wall
  of labels. This synchrony is the whole teaching trick of the format.
- Persist what's been taught: as the chain advances, earlier parts stay visible
  but dimmed, so the viewer watches the system grow rather than reset.
- Motion shows causality — a flow travels along an arrow, a part reacts —
  rather than decorating.

Generate each scene's animation from a precise description of the diagram, its
motion, and its pacing against that step's narration line.

### 4. The recap scene

End with **one scene showing the whole system at once**: every step's diagram
element assembled into the complete picture while the narration replays the
chain in one or two sentences ("So: A drives B, B enables C — and that's why
X works"). This is where the learning consolidates; never skip it.

### 5. Narrate and sync

Generate the narration in a calm, clear voice. Scene durations follow the
narration; leave a breath of hold after each step's last annotation lands so
the viewer can absorb the diagram before moving on.

### 6. Review, then export

Verify: every annotation lands on its spoken word, labels are legible at video
scale, nothing appears before it's explained, the recap matches the steps
taught. Share the review link with the user and get approval **before**
exporting. Then export and deliver the link.

## What to avoid

- Music or sound effects — never add them.
- Pre-labeled diagrams where everything is visible from frame one.
- Metaphor drift — one visual metaphor per concept, held for the whole video.
- Racing the narration; comprehension needs silence-shaped pauses, and a slow
  scene beats a re-watched one.
