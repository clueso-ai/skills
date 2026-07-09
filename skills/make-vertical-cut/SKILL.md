---
name: make-vertical-cut
description: >-
  Reframe a landscape video into a 9:16 vertical cut for social and mobile —
  recompose every scene around the action area and turn captions on for
  sound-off viewing. Use when the user says "make a vertical version",
  "reframe this for Reels/Shorts/TikTok", "9:16 cut of this video", "make
  this portrait for LinkedIn", or "turn this into a mobile-friendly cut".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Make Vertical Cut

Produce a 9:16 version of a landscape video that looks composed for portrait — each
scene recentered on where the action is, captions on because most social viewers
watch with the sound off.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## What you need

- **The video.** Ask: is it an existing Clueso project (have them name or link it),
  or a raw screen recording they'll upload? If it's a recording, bring it into a new
  project first.
- **The platform.** LinkedIn, Shorts, Reels, or TikTok — mainly to sanity-check
  length expectations (social favors short; suggest trimming if the source runs
  long, but only with the user's agreement).

Confirm the target workspace before editing anything.

## How to reframe

1. **Work on a vertical copy.** Duplicate the project and switch the copy to 9:16
   so the landscape original stays intact.
2. **Recompose scene by scene — never just center-crop.** For each scene, find the
   action area (the control being clicked, the form being filled, the text being
   read) and frame the vertical viewport around it. A wide app window usually means
   pushing in on the region that matters and letting the rest go; empty chrome and
   sidebars are the first things to lose.
3. **Reposition overlays for portrait.** Callouts, text, and title cards designed
   for landscape will hang off the edges — move them into the vertical safe area,
   re-wrap text to the narrower measure, and keep them clear of the bottom strip
   where captions live.
4. **Captions on, always.** Enable captions for the full runtime — short lines,
   high contrast, sized for a phone held at arm's length. The cut must make sense
   with the sound off.
5. **Check every scene at phone scale.** If text in the recorded UI is too small to
   read in a given scene even after pushing in, tighten the framing further or flag
   that scene to the user.

## Review

Share a review link and have the user check it on their phone — that's the screen
this cut lives on. Get their nod before the final export.

## Avoid

- A single static center-crop across the whole video.
- Letterboxing the landscape frame with blurred bars — recompose instead.
- Overlays or captions that cover the action area.
