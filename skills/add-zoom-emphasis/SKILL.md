---
name: add-zoom-emphasis
description: >-
  Add smooth zoom-ins at the moments that matter in an existing video — clicks,
  form fills, small UI the viewer would otherwise miss — then pull back out.
  Use when the user says "add zooms", "zoom into the clicks", "zoom in on the
  important parts", "emphasize the action", "the UI is too small to follow",
  or "add camera movement to my recording".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Add Zoom Emphasis

Give a flat screen recording camera direction: push in on the control being
used at each key moment, hold while the action happens, and release back to
full frame — so viewers always know where to look.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (have them name or link
   it), or a raw screen recording they'll upload? Branch accordingly.
2. **What to emphasize** (optional) — specific moments or features; otherwise
   find the emphasis-worthy moments yourself.

Confirm the target workspace before editing anything.

## Workflow

### 1. Find where and when

Read the narration transcript and inspect rendered frames at candidate moments.
Emphasis belongs where attention is earned: a click on a specific control, a
value typed into a field, a toggle flipped, small or dense UI the narration is
describing. Note, for each moment, the on-screen coordinates of the action and
the time window when the narration talks about it.

### 2. Place the zooms

For each moment, add a zoom centered on the action's coordinates, starting just
before the narration's action word and releasing once the result is visible.
Craft rules:

- **One move per step.** Push in, hold, release. Constant zooming reads as
  seasickness; zero zooms read as unedited.
- **Modest magnification** — enough that the control is unmistakable, not so
  much that viewers lose context of where they are on the screen.
- **Ease in and out.** No snap cuts to a zoomed state.
- Leave breathing room between moves; if two actions are seconds apart, cover
  both with one framing instead of two zooms.

### 3. Verify against frames

Re-inspect rendered frames at each zoom's hold point: is the control centered
and fully in frame? Is nothing important cropped out? Is text legible at the
zoom level? Adjust center and scale until every hold frames its action cleanly.

### 4. Review, then export

Share the review link and get the user's nod before exporting. Then export and
hand over the final link.
