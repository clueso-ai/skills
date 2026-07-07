---
name: polish-screen-demo
description: >-
  Turn a raw screen recording into a polished, narrated product demo using only
  the Clueso MCP — trim dead time, split at step boundaries, add zooms,
  highlights, captions, and a generated voiceover, then export. Use when the
  user says "polish this recording", "clean up my screen recording", "make this
  recording into a demo", "add voiceover and zooms to this capture", or uploads
  a raw screen capture and wants it presentable.
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Polish Screen Demo

Take an unedited screen recording and return a demo you'd put on a landing page:
tightened pacing, camera motion, visual emphasis, narration, and clean bookends.
Everything runs through Clueso MCP tools.

## Requirements

- Clueso MCP connected. Nothing else.

## Inputs

1. **The recording** — either:
   - a file the user provides → `upload_file`, then poll `check_uploads` until
     processed; or
   - a fresh capture → `record_screen` (available when the workspace has recording
     enabled — check with `get_capabilities`; if unavailable, ask for a file instead).
2. **What the demo shows** — the feature/flow name and the 1-line takeaway per major
   step. If the user can't list steps, derive them by watching the recording's
   structure (clip timestamps + any narration via `analyze_audio`) and confirm your
   step list with the user before editing.
3. **Tone** — narrated product demo (default) or captions-only silent demo.

## Workflow

### 1. Confirm workspace, ingest the recording

`find(type='workspaces')` → confirm → `create_project` → ingest the recording
(`upload_file`/`record_screen`, `check_uploads` until ready), `add_clips` to place it
on the timeline.

If the recording has spoken audio, run `analyze_audio` first — the existing narration
tells you where the step boundaries and dead time are.

### 2. Cut the dead time

Raw captures are mostly waiting. Use `split_clip` at each step boundary, then:

- Remove or compress stretches where nothing meaningful happens (page loads, typing
  long form fields, mouse wandering) — `remove_clip` the dead segments or tighten with
  `update_clips`.
- Target: no shot where the screen is effectively idle for more than ~2 seconds.
- Keep one breath (~0.5s) after each completed action so viewers register the result.

### 3. Write the narration against the cut

One or two sentences per step: what's being done and why it matters. Present tense,
second person. `estimate_duration` per step — where narration outruns footage, either
tighten the words or let the footage of that step run slightly longer; never rush the
voice.

Skip this if the user chose captions-only.

### 4. Direct the viewer's eye

Fetch `get_element_schema`, then per step:

- **Zoom & pan** — keyframe scale/position so the camera pushes toward the region
  being used, holds, and releases. One move per step; constant zooming reads as
  seasickness, a static full-screen recording reads as unedited.
- **Highlights** — a keyframed rectangle or ring landing on the control as it's
  clicked, timed to the narration's action word.
- **Captions** — short step labels (3-6 words) entering with `animation_setting`
  presets (`slide`, `masked_reveal`), swapped out as steps change. For captions-only
  demos these carry the narration's job: slightly longer, but still one line at a time.

### 5. Bookends

- **Intro clip** (~3s): product/feature name + one-line promise, kinetic type on the
  committed palette (brand colors if the workspace has them; otherwise
  `get_design_guide` and pick).
- **Outro clip** (~3s): the CTA. One action.

### 6. Audio pass

- Narrated: `set_voice` → `voiceover_batch` for all steps → `auto_sync`, then
  `add_sync_point` so each zoom/highlight lands on its action word.
- Optional bed: `add_audio` for subtle background music; `analyze_audio` /
  `update_audio` to keep it well under the voice.
- Captions-only: music bed slightly more present, sync captions to the action instead
  of a voice.

### 7. Verify and export

`get_clip(render=true, timestamp=…)` at each step's action moment: is the zoom framing
the right region, is the highlight on the control, is the caption legible and current?
Watch the pacing math: total runtime should be a fraction of the raw capture (a 4-min
raw take usually makes a 60-90s demo). Fix, then `export_project` and hand over the
link.

## Fallbacks

- **`record_screen` unavailable** → ask for an uploaded file; don't attempt any local
  recording tooling.
- **Upload fails or stalls** → report the `check_uploads` state and ask the user to
  retry; don't silently proceed without the footage.
- **Recording quality too low to zoom** (tiny text, low resolution) → keep zooms
  gentle, lean harder on highlights and captions, and tell the user a higher-resolution
  capture would let the demo push in closer.
- **User's step list doesn't match the footage** → trust the footage; show the user
  the discrepancy before cutting.
