---
name: screenshots-to-walkthrough
description: >-
  Turn an ordered set of UI screenshots into a screen-recording-style
  walkthrough video using only the Clueso MCP: each step narrated, the relevant
  control spotlighted, and a keyframed cursor that glides to it and clicks —
  bracketed by branded intro/outro cards. Use when the user says "make a
  walkthrough from these screenshots", "turn these screenshots into a demo
  video", "cursor walkthrough", "make it look like a screen recording", or
  provides step-by-step UI images and wants a guided video.
license: Apache-2.0
metadata:
  author: clueso
  category: video-creation
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Screenshots to Walkthrough

Build a narrated walkthrough that feels like a polished screen recording — from static
screenshots. Each step is narrated, the control being discussed is spotlighted, and a
cursor travels to it and clicks, all synced to the voiceover. Branded intro and outro
cards bookend the flow. Everything runs through Clueso MCP tools.

## Requirements

- Clueso MCP connected. Nothing else.

## Inputs

1. **Screenshots** — ordered image files, one per step of the flow.
2. **Topic/title** — e.g. "Connect the MCP to your editor".
3. **Brand** — name, accent color, and logo file if available (prefer a
   colored-on-dark logo variant for dark cards). If no brand is given, use the
   workspace's brand; ask if neither exists.
4. **Voice** — optional; otherwise the project default.

## Workflow

### 0. Understand the flow before building

Look at every screenshot in order. For each, note: what page it is, what action it
shows, and the on-screen location of the key control (button/field/row/code block).
Derive the end-to-end story, then decide the clip list — one screenshot may become
multiple clips if it shows multiple steps (e.g. a 3-step panel → 3 clips reusing the
same image).

### 1. Get assets in

- Upload each screenshot with `upload_file(file_name)`, complete the returned upload
  step with the real local path, and use the returned `mcp_upload_id`. For public
  URLs, pass `file_url` instead.
- Upload the brand logo the same way.

### 2. Create the project and clips

- `create_project(title=<topic>)` — this creates clip 0 (use it as the intro).
- `add_clips(kind='blank')` for one clip per planned step plus the outro.
- Set a dark, slightly tinted background on every clip (e.g. `#0B0710`) — tint toward
  the accent, never pure black.

### 3. Voiceover FIRST — it retimes the clips

- Write concise, friendly narration per clip, 1-2 sentences. Spell out symbols the
  voice would garble ("slash mcp", "config dot toml"). Intro: what this is and roughly
  how many steps. Outro: the payoff plus one CTA.
- Run `voiceover_batch` (`set_and_generate`) for ALL clips, and `set_voice` if the
  user chose one. **Generating speech resets each clip's duration to the spoken
  length** — so narrate first, then `get_project` to read the final durations before
  timing any spotlight or cursor keyframe.

### 4. Place the screenshots — crop the chrome

- Add each screenshot as an image element cropped to the product only: for a full
  browser-window capture, `crop = { position:[0, 0.155], size:[1, 0.845] }` removes
  the top ~15.5% (tabs + URL bar + bookmarks). Tune the fraction to your captures.
- Match the element box's aspect ratio to the cropped aspect — no distortion.
- Frame it as a card on the dark background: near-full-width with a small margin,
  `cornerRadius: 2`, `shadow: 12-15` (screenshots are rectangular cards, so a shadow
  is correct here — see the cursor exception below).
- `end_time` = the clip's real post-voiceover duration.

### 5. Spotlights — one focus per beat

- Use `element_type:'spotlight'`: its bounds are the BRIGHT cut-out; everything else
  dims. Start from
  `type_data:{ backgroundOpacity:60, borderRadius:10-30, entryTransitionTime:0.4, exitTransitionTime:0.3 }`.
- Place it over the exact control the narration names, timed to that beat. Multiple
  spotlights per clip are fine as long as they don't overlap in time (e.g. the URL
  field early, a list item later).

### 6. The keyframed cursor — the signature motion

- Cursor assets (transparent PNGs served by Clueso):
  - arrow: `https://publicassets.in.prod.clueso.io/desktop/cursors/default-cursor.png`
  - typing I-beam (only when a step types into a field):
    `https://publicassets.in.prod.clueso.io/desktop/cursors/typing-cursor.png`
- Element size 72×72 with `shadow: 0` — **always**; a shadow renders as a grey box
  around a transparent PNG.
- Position by the cursor TIP, not the box: arrow `x = Px-22, y = Py-17`; I-beam
  `x = Px-37, y = Py-36` (where Px,Py is the target point).
- Animate with position keyframes (`positionX`/`positionY`, clip-relative seconds):
  `easeInOut` for travel, `easeOut` on arrival. Per clip: travel to the control → a
  small click-dip (down ~6px and back over ~0.3s) on the click → hold.
- **Continuity:** each clip's first cursor keyframe = the previous clip's last
  position (same screen ⇒ no jump). Fade the cursor in on its first clip and out on
  its last. No cursor on intro/outro cards.
- **Glyph swap** for typing steps: two time-gated cursor elements (arrow → I-beam →
  arrow) with the tip position identical at each handoff.

### 7. Branded intro and outro cards

- Dark background (same tinted dark as the clips). Add a full-canvas radial-gradient
  glow rectangle (accent at center → transparent) for depth.
- Logo (image element, `shadow: 0`) top-center, fading in.
- Title ~96-100px, white, weight 700, up to 2 lines, entering with a per-line
  slide-up.
- Accent underline: a thin rectangle (`borderRadius: 50`, accent color),
  left-anchored, width keyframed 0→W as a draw-in (rectangles can't fade).
- Subtitle ~38px in a muted tint of the accent. Stagger `start_time`s roughly
  0.2 / 0.6 / 1.0 / 1.6s.
- Accent = the brand's color **at video intensity** — web-UI opacities look timid on
  screen. Derive the muted text color from the accent, not grey.

### 8. Verify — don't trust t=0

- Still renders default to t=0; use `get_clip(render=true, timestamp=T)` at each
  interaction moment to confirm the cursor tip lands on the target and the spotlight
  frames the right element.
- Freshly uploaded assets can render blank once (load lag) — re-render before
  assuming a real failure.
- Don't export while iterating. When the walkthrough is right, report the project URL
  and offer tweaks; `export_project` when the user confirms.

## Style rules

- Design for video, not a webpage: nothing fully static, motion synced to the
  narration, one accent color, neutrals tinted toward it.
- Cursor motion calm and intentional — never jumpy, one journey per beat.

## Fallbacks

- **A screenshot is too low-resolution to spotlight tightly** → widen the spotlight
  to the containing region and let the narration carry the specificity; tell the user
  a sharper capture would let the video zoom in.
- **The control's location is ambiguous** → ask the user rather than guessing where
  the cursor should land.
- **Upload stalls** → poll `check_uploads`; report and continue with remaining steps
  rather than blocking the whole build.
- **Cursor lands off-target in verification renders** → re-check the tip offsets
  (arrow -22,-17 / I-beam -37,-36) against the element's box before re-timing
  keyframes.
