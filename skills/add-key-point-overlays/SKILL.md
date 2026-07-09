---
name: add-key-point-overlays
description: >-
  Put the takeaway on screen: add short text overlays that surface the key
  point of each section of an existing video as it's narrated. Use when the
  user says "add key points on screen", "add takeaway text", "put the main
  points as text overlays", "reinforce the message visually", or "viewers
  skim — make the points readable".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Add Key Point Overlays

Viewers remember what they read, not just what they hear. This pass distills
each section of a video into one short line and puts it on screen at the
moment the narration makes that point.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (have them name or link
   it), or a raw screen recording they'll upload? Branch accordingly.
2. **The key points** — from the user, or "extract them from the narration"
   and distill them yourself.
3. **Brand** — colors and fonts, or "use workspace branding".

Confirm the target workspace before editing anything.

## Workflow

### 1. Distill the points

Read the narration transcript and split it into sections — one idea each. Write
one overlay line per section: **3-8 words**, the takeaway rather than a
paraphrase ("Invite unlimited viewers free", not "Now we look at inviting
users"). Not every section earns an overlay; a point per section is the
ceiling, not a quota. Show the user the list of lines before placing anything.

### 2. Place the overlays

Time each overlay to appear as the narration reaches its point and hold for
its section, exiting before the next point arrives. For position, inspect
rendered frames across each overlay's window: put the text over quiet screen
space — never covering the control, data, or cursor path the section is about.
Keep one consistent position, style, and subtle entry animation throughout,
inside safe margins, sized to be readable on a phone. One overlay on screen at
a time.

### 3. Verify against frames

Re-inspect rendered frames while each overlay is visible: legible against
what's behind it (add a backing shade if the background is busy), not clipping
the action, on brand, no typos, and nothing important appearing beneath it
mid-window as the screen changes. Adjust position, timing, or contrast until
every line sits cleanly for its whole duration.

### 4. Review, then export

Share the review link and get the user's nod before exporting. Then export and
hand over the final link.
