---
name: add-animated-captions
description: >-
  Burn captions into an existing video so it works with the sound off —
  accurate, well-timed subtitles baked into the exported file. Use when the
  user says "add captions", "burn in subtitles", "make it watchable on mute",
  "add subtitles to my video", "captions for social", or "hardcode the
  captions".
license: Apache-2.0
metadata:
  author: clueso
  category: quick-edits
  subcategory: captions-and-accessibility
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Add Animated Captions

Most viewers watch with the sound off. This pass delivers a video with
captions burned into the file itself — every spoken word readable on screen,
timed to the voice, on every platform with zero player settings.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (have them name or link
   it), or a raw screen recording they'll upload? Branch accordingly.
2. **Style preference** — default is clean captions matched to the video.

Confirm the target workspace before editing anything.

## What to promise

Commit to **burned-in captions**: subtitles rendered into the exported video,
following the narration. That path works reliably. Heavily stylized per-word
animation — karaoke-style word pops in custom brand treatments — may not be
controllable; don't promise it. If the user wants big, branded, animated text
on screen, offer the supported alternative: **key-point text overlays** —
short brand-styled lines surfacing each section's takeaway (see the
`add-key-point-overlays` skill) — on their own or layered on top of the
burned-in captions.

## Workflow

### 1. Get the words right first

Captions are only as good as the transcript beneath them. Read the narration
transcript and fix anything that would embarrass the video burned in at the
bottom of the screen: product names, acronyms, technical terms, homophones.
If the video has no narration, captions have nothing to carry — offer
key-point overlays instead.

### 2. Export with captions burned in

Produce the export with captions baked into the frames, timed to the
narration.

### 3. Verify against frames

Inspect rendered frames at several points — fast speech, product-name
mentions, moments where on-screen action sits low in the frame: are the
captions legible, correctly spelled, in sync, and not covering UI the viewer
needs (or colliding with other overlays)? If a stretch fails, fix the
transcript or shift the conflicting element and re-export until the sound-off
experience holds end to end.

### 4. Review, then hand over

Share the review link and get the user's nod before the final export. Then
hand over the final link.
