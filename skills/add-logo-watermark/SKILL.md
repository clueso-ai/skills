---
name: add-logo-watermark
description: >-
  Add a persistent, unobtrusive corner logo watermark to an existing video —
  one corner, low opacity, present for the full runtime without covering any
  action. Use when the user says "add our logo to this video", "watermark
  this video", "put our logo in the corner", or "brand this video with our
  logo".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Add Logo Watermark

Place the user's logo as a quiet, persistent corner mark across the whole video —
visible enough to claim the content, subtle enough that viewers stop noticing it
after two seconds.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## What you need

- **The video.** Ask: is it an existing Clueso project (have them name or link it),
  or a raw screen recording they'll upload? If it's a recording, bring it into a new
  project first.
- **The logo.** A file from the user, or the workspace's brand logo if one is set —
  prefer a version that survives small sizes (mark-only beats full wordmark).
- **Preferences.** Which corner (default bottom-right) and how transparent (default
  around 60–70% opacity — present, not loud).

Confirm the target workspace before editing anything.

## How to place it

1. **Check the corner against the footage.** Scan the video for anything living in
   the chosen corner — persistent UI, captions, lower thirds, the cursor's favorite
   resting spot. If the default corner collides, propose the emptiest corner instead
   of stacking the logo on top of content.
2. **Size it small.** Roughly 5–8% of the frame width. If the logo has a light and a
   dark variant, pick the one that reads against what's typically in that corner.
3. **Place it once, everywhere.** Same corner, same size, same opacity on every
   scene, for each scene's full duration, with a consistent margin from the edges.
   No entry or exit animation — a watermark that slides in is an interruption, not
   a watermark.
4. **Spot-check the worst frames.** Look at the busiest moments (dense UI, dialogs
   near that corner). The logo should never cover a control being demonstrated; if
   it does at one specific moment, flag it to the user rather than silently moving
   the logo for just that scene.

## Review

Share a review link and confirm corner, size, and opacity feel right to the user
before the final export.

## Avoid

- Full-opacity or oversized logos — this is a watermark, not an intro card.
- Different corners on different scenes.
- Animating the watermark or adding a background plate behind it.
