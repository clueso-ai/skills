---
name: spotlight-key-areas
description: >-
  Dim everything on screen except the area being explained, so viewers can't
  look at the wrong thing while a step is narrated. Use when the user says
  "spotlight the important area", "dim the background", "focus attention on
  this part of the screen", "darken everything except the button", or "the
  screen is too busy — isolate what matters".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Spotlight Key Areas

Busy screens bury the point. A spotlight darkens everything except the active
region while a step is explained, then lifts — the strongest form of visual
emphasis, reserved for the moments that deserve it.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (have them name or link
   it), or a raw screen recording they'll upload? Branch accordingly.
2. **The moments/areas to isolate** — from the user, or derive them from the
   narration yourself.

Confirm the target workspace before editing anything.

## Workflow

### 1. Find the regions worth isolating

Read the narration transcript for the moments where one region carries the
whole step — a settings panel being configured, a chart being interpreted, a
form being filled on a cluttered page. Inspect rendered frames at those
timestamps to get each region's exact bounds. Spotlights are for dense screens;
if the frame is already simple, skip that moment rather than dim for effect.

### 2. Place the spotlights

- Cover the active region with **generous padding** — a spotlight cropped tight
  to a button feels claustrophobic; include the control plus its immediate
  context (its label, its row).
- **Timed to the explanation**: fade the dim in as the narration starts on that
  region, hold while it's discussed, lift before the viewer needs to see the
  rest of the screen again.
- One spotlight at a time, and use them sparingly — a few per video. Rapid
  dim/undim cycling is strobing, not emphasis.
- Keep the dim strong enough to kill distraction but light enough that viewers
  still sense where they are on the page.

### 3. Verify against frames

Re-inspect rendered frames during each spotlight: is the active region fully
inside the lit area — nothing the narration mentions left in the dark? Does
anything the viewer must read sit outside it? Adjust bounds and timing until
every spotlight isolates exactly what the voice is explaining.

### 4. Review, then export

Share the review link and get the user's nod before exporting. Then export and
hand over the final link.
