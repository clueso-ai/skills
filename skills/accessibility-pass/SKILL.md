---
name: accessibility-pass
description: >-
  Make one video accessibility-ready: captions on, on-screen text sized and
  contrasted to be readable, pacing checked so every step can be followed.
  Use when the user says "accessibility pass", "make this video accessible",
  "check WCAG for my video", "is this readable for everyone", or "prep this
  for an accessibility review".
license: Apache-2.0
metadata:
  author: clueso
  category: quick-edits
  subcategory: captions-and-accessibility
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Accessibility Pass

Audit and fix one video so it works for viewers who can't hear it, can't read
small low-contrast text, or need a moment longer to follow a step — captions,
legibility, and pacing in a single pass.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (have them name or link
   it), or a raw screen recording they'll upload? Branch accordingly.

Confirm the target workspace before editing anything.

## Workflow

### 1. Audit with frames and transcript

Inspect rendered frames across the video alongside the narration transcript,
building a fix list on three axes:

- **Captions** — can a viewer with no audio follow everything? Check the
  transcript for errors (names, terms) that would surface as wrong captions.
- **Text legibility** — every text overlay, label, and title: large enough to
  read on a phone, strong contrast against what's behind it, on screen long
  enough to be read twice, inside safe margins.
- **Pacing** — anywhere the narration names an action and the footage has
  already moved on, or a step flashes past faster than it can be followed.
  Also flag rapid flashing or strobing content outright.

### 2. Fix what the audit found

- Correct the transcript so captions will be right, and plan the export with
  captions burned in for sound-off viewing.
- Resize, recolor, or add backing shades behind failing text; extend anything
  that exits too fast. Fix contrast by checking the actual frame behind the
  text, not the text style in isolation.
- Extend the hold on rushed steps so the visual stays on screen a beat after
  the narration finishes describing it.

### 3. Verify against frames

Re-inspect rendered frames at every point you touched, plus the worst spots
from the audit: text now legible, nothing important covered, steps followable
at reading speed, captions accurate where speech is fastest. Iterate until the
whole video passes with the sound off.

### 4. Review, then export

Share the review link with a short summary of what was fixed, and get the
user's nod before exporting. Then export with captions on and hand over the
final link.
