---
name: add-callouts-and-arrows
description: >-
  Annotate an existing video with callout boxes and arrows that point at the
  exact buttons and fields the narration mentions, appearing and leaving in
  time with the voice. Use when the user says "add callouts", "add arrows",
  "annotate my video", "point at the buttons", "label the steps on screen",
  or "highlight where to click".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Add Callouts and Arrows

Turn "click the button in the corner" into an arrow that lands on that exact
button as the words are spoken. Callouts and arrows do the pointing so the
narration doesn't have to give directions.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (have them name or link
   it), or a raw screen recording they'll upload? Branch accordingly.
2. **What to annotate** — a list from the user, or "follow the narration" and
   derive the targets yourself.
3. **Brand colors** if the annotations should match a palette (default: workspace
   branding).

Confirm the target workspace before editing anything.

## Workflow

### 1. Find every target

Go through the narration transcript line by line: each mention of a control —
"click Save", "open the Settings menu", "paste it into the API key field" — is
an annotation candidate. Inspect rendered frames at those timestamps to locate
each control's exact on-screen coordinates.

### 2. Place the annotations

- **Arrows** point; use them when the narration says where to click. The tip
  must touch or nearly touch the control, angled in from empty screen space —
  never crossing over other UI the viewer needs to read.
- **Callout boxes** frame; use them when a region (a form, a panel, a value)
  needs attention for a few seconds. Snug around the region with a little
  padding, never covering the thing itself.
- **Timing follows the voice**: appear on the narration's action word, leave
  when the step's sentence ends or the click completes. Nothing lingers into
  the next step.
- One annotation on screen at a time in almost all cases. Consistent style and
  color throughout — annotations are wayfinding, not decoration.

### 3. Verify against frames

Re-inspect rendered frames while each annotation is visible: does the arrow tip
land on the button? Does the callout enclose the field without clipping it or
hiding neighboring labels the viewer needs? Adjust positions and sizes until
every annotation lands exactly, especially anywhere the UI moves or scrolls.

### 4. Review, then export

Share the review link and get the user's nod before exporting. Then export and
hand over the final link.
