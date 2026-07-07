---
name: brief-to-launch-video
description: >-
  Turn a short product brief into a 30-60 second launch-style motion-graphics
  video using only the Clueso MCP — script, scenes, kinetic typography,
  voiceover, and export. Use when the user says "make a launch video for X",
  "announcement video", "product launch reel", "promo video from this brief",
  or gives you a product name plus a few selling points and wants a video.
license: Apache-2.0
metadata:
  author: clueso
  category: video-creation
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Brief to Launch Video

Produce a 30-60 second launch/announcement video from a written brief. Everything —
project creation, scene composition, motion, voiceover, and export — happens through
Clueso MCP tools. No external APIs, no local binaries, no scripts.

## Requirements

- Clueso MCP connected (`create_project`, `add_clips`, `add_elements`, `voiceover_batch`,
  `export_project` and friends must be available). Nothing else.

## Inputs

Collect these before building. Ask for anything missing rather than inventing it:

1. **Product name** and one-line positioning.
2. **Audience** — who the video speaks to.
3. **3-5 key points** — features, outcomes, or proof points, in priority order.
4. **Call to action** — what the viewer should do at the end.
5. Optional: brand colors / logo / product screenshots. If the user has real product
   footage or screenshots, use them — never fake their product with stock or generated
   imagery.

## Workflow

### 1. Confirm the workspace

Call `find(type='workspaces')` and confirm with the user that the active workspace is
the intended one before creating anything. Use `switch_workspace` if not.

### 2. Look for a clueprint first

Call `find(type='clueprints', query='<product launch / announcement style the user wants>')`.

- **Strong matches** → show the best 2-3 (name, what it's for, why it fits) and ask
  whether to build from one. A clueprint's design — colors, typography, layout, motion —
  is the direction; follow it.
- **Weak or no matches, or the user asked to start blank** → call `get_design_guide`
  and follow it. Commit to a palette before building: brand colors if provided
  (applied at video intensity), otherwise one accent with real contrast and neutrals
  tinted toward it.

### 3. Write the script before touching the timeline

Draft the voiceover script as 5-7 beats in a classic launch arc:

| Beat | Job | Length |
|---|---|---|
| Hook | Name the pain or the promise | ~1 line |
| Reveal | Product name + positioning | ~1 line |
| Points 1-3 | One key point per beat, concrete | 1-2 lines each |
| Proof | Number, quote, or before/after (skip if none provided) | ~1 line |
| CTA | One action, stated once | ~1 line |

Rules: conversational register, no feature-list monotone, every sentence earns its
seconds. Call `estimate_duration` on the script; if it lands outside 30-60s, cut or
split beats — don't speed up the voice to fit.

Show the user the script and get a nod before composing. This is the cheapest moment
to change direction.

### 4. Create the project and build one clip per beat

- `create_project` with a name like "<Product> launch video".
- `add_clips` — one clip per beat, durations from the script estimate.
- Call `get_element_schema` before your first `add_elements` call and compose with
  real element parameters, not guessed ones.

Composition rules (from the design guide — read it, these are the load-bearing ones):

- **Kinetic typography is the default for word-driven beats.** Reveal lines in time
  with the voiceover using text `animation_setting` presets — `slide`, `pop`,
  `masked_reveal`, `typewriter`, with `apply_to_unit: 'word'` or `'line'`. Swap old
  lines out as the script moves on; never pile lines into a wall of text.
- **Keyframes are the main source of motion.** Bars that grow, cards that slide and
  settle, highlights that travel — native text/rectangles/images with position + size
  keyframes look expensive and stay on-brand. Vary entrance direction and easing
  between elements.
- **Nothing static.** If a frame would hold unchanged for more than a beat, add a
  reveal, a swap, or a slow drift.
- **Vary the technique beat to beat.** Real screenshots for product beats
  (`upload_file` + `check_uploads`), stock only for generic atmosphere
  (`find(type='videos'|'images', source='stock', query='…')` — one type per call),
  `generate_media(kind='animation')` only when the motion is genuinely beyond
  keyframed elements. First ask: can this beat be a few rectangles and text with
  keyframes? If yes, build it that way.
- Size type for video, not for a web page.

### 5. Voiceover and sync

- Pick a voice with `set_voice` (list options with `find` if the user has a preference).
- Generate narration for all beats in one `voiceover_batch` call.
- Align visuals to the narration: `auto_sync` first, then `add_sync_point` for any
  reveal that must land on a specific word. Each on-screen line should appear as it's
  spoken (`start_time` on that VO beat), hold while relevant, then exit.

### 6. Verify before export

For each clip, render a mid-beat frame with `get_clip(render=true, timestamp=<middle>)`
and check:

- Text is legible at video scale and inside safe margins.
- Generated animations sit inside their boxes.
- Palette is consistent — every color traces back to the committed palette.
- Total duration is within 30-60s.

Fix issues with `update_elements` / `update_clips` / `update_audio`, re-render, then
`export_project`. Report the export link to the user.

## Fallbacks

- **No clueprint match** → design guide + committed palette (step 2).
- **User has no screenshots for a product beat** → ask for them; if none exist, use an
  abstract keyframed composition for that beat — do not fake their UI.
- **`estimate_duration` says a beat is too long** → cut words, not pace.
- **Upload stuck processing** → poll `check_uploads`; if it fails, continue with the
  remaining beats and tell the user which beat needs their asset re-uploaded.
- **A generated animation renders off-box or illegible** → re-render the frame after
  tuning `animation_duration` / box size via `update_elements`; if still wrong, replace
  the beat with keyframed native elements.
