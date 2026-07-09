---
name: extract-gif-moment
description: >-
  Pull the single best interaction from a video as a crisp looping GIF —
  delivered through a Clueso article/document, or as a short looping video
  clip if that fits the destination better — for changelogs, newsletters,
  and in-app tooltips. Use when the user says "make a GIF of this moment",
  "extract a GIF from this video", "I need a looping clip of the key
  interaction", "GIF for the changelog", or "grab the money shot as a GIF".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Extract GIF Moment

Find the one interaction in a video worth looping — the click that makes the
feature obvious — and turn it into a tight, embeddable GIF, produced through
Clueso's documentation route (or a short looping video clip when the destination
plays video).

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## What you need

- **The video.** Ask: is it an existing Clueso project (have them name or link it),
  or a raw screen recording they'll upload? If it's a recording, bring it into a new
  project first.
- **The moment.** Which interaction — or "pick the money shot", in which case scan
  the video for the beat where the feature's value is visible on screen (the click
  and its immediate payoff) and confirm your pick with the user before producing
  anything.
- **The destination.** Changelog, newsletter, in-app tooltip, or docs — it decides
  the delivery format below.

Confirm the target workspace before editing anything.

## How the GIF gets made

Be upfront with the user: the GIF is produced via Clueso's documentation side — the
moment is captured from the project's video into an article/document as a GIF,
which the user can then take from there. There is no direct GIF-file download from
the video export itself. If the destination can play video (most changelog tools,
docs platforms, and social embeds can), offer a short looping video clip instead —
it's sharper and smaller for UI content.

1. **Isolate the moment.** Target 3–8 seconds: start a beat before the action,
   end right after the result appears. A GIF that loops mid-action feels broken —
   pick in and out points where the screen is briefly at rest so the loop seam
   disappears.
2. **Frame it tight.** Crop or push in on the interaction region; a full-desktop
   GIF at newsletter width is unreadable. No narration dependence — the moment must
   explain itself silently, so add nothing that needs sound.
3. **Produce it via the article route** (or as the short looping clip, if agreed):
   capture the isolated moment as a GIF within a document tied to the project, then
   hand the user that document so they can pull the GIF for their destination.

## Review

Show the user the loop before finishing — does it read instantly, does the seam
hide, is the file/format right for the destination? Adjust in/out points on their
feedback.

## Avoid

- Promising a direct GIF file download from the video export — that's not the path.
- Loops longer than ~8 seconds or wider than the interaction needs.
- Moments that depend on narration or captions to make sense.
