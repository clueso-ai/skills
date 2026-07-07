---
name: article-to-video
description: >-
  Convert a help-center article, blog post, changelog entry, or any pasted
  document into a narrated explainer video using only the Clueso MCP. Use when
  the user says "turn this article into a video", "make a video version of this
  doc", "video from these release notes", "explain this guide as a video", or
  pastes long-form text and asks for a video.
license: Apache-2.0
metadata:
  author: clueso
  category: video-creation
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Article to Video

Turn written long-form content into a narrated explainer video: distill the text into
a scene-by-scene script, compose each scene with native Clueso elements, narrate it,
and export. Only Clueso MCP tools are used — the "intelligence" (reading, distilling,
scripting) is yours, the media work is Clueso's.

## Requirements

- Clueso MCP connected. Nothing else — no scrapers, no external APIs.

## Inputs

One of:

- **Pasted text** — the article body in the conversation.
- **A Clueso article** — fetch it with `get_article`.
- **A file** — ask the user to paste the content or attach it; do not reach for
  external fetching tools this skill doesn't require.

Plus: intended audience and target length if the user has one (default: 60-90s for a
how-to, 30-45s for a changelog).

If the article contains images/screenshots the user can provide, collect them — real
screenshots beat anything generated.

## Workflow

### 1. Confirm the workspace

`find(type='workspaces')`; confirm with the user; `switch_workspace` if needed.

### 2. Distill — don't transcribe

An article read aloud is not a video script. Extract:

- **The one-sentence point** of the article (this becomes the hook).
- **3-6 steps or ideas**, each collapsed to its action and its outcome. Cut caveats,
  edge cases, and anything parenthetical — the article remains the reference for those.
- **The payoff** — what the viewer can now do.

Write the voiceover script: hook → steps/ideas in order → payoff. One scene per step.
Conversational, second person, present tense ("Click **Export** and pick a format" not
"The user may then choose to export"). Check pacing with `estimate_duration`; trim
until it fits the target length.

Show the user the script before composing.

### 3. Pick the visual direction

`find(type='clueprints', query='tutorial / explainer / changelog style')` — if a strong
match exists, offer it and follow its design. Otherwise `get_design_guide`, commit to a
palette (workspace brand colors first if available), and follow the guide.

### 4. Build the project

- `create_project`, then `add_clips` — one clip per scene, durations from the script.
- `get_element_schema` before the first `add_elements`.

Scene composition by content type:

- **Step with a screenshot available** → `upload_file` + `check_uploads`, place the
  image, then keyframe attention: a zoom toward the relevant region, a traveling
  highlight rectangle, or a callout that pops in on the key phrase of the narration.
- **Step without a screenshot** → kinetic typography carrying the step's action words
  (`animation_setting` presets: `masked_reveal`, `slide`, `typewriter`;
  `apply_to_unit: 'word'` for emphasis beats), plus simple keyframed shapes
  (a rectangle standing in for a panel, a progress bar growing, a toggle flipping).
  Do NOT mock up the product's actual UI from imagination — abstract shapes, not fake
  screenshots.
- **Conceptual idea (non-UI)** → consider `generate_media(kind='animation')` for a
  mechanism or chart, but only if a few keyframed rectangles genuinely can't carry it.
  Boxed, not full-canvas, when the scene also has text.
- **Lists in the article** → reveal items one at a time synced to the voice, swapping
  or dimming previous items — never a static bullet wall.

### 5. Narrate and sync

- `set_voice` (ask if the user has a preference), `voiceover_batch` for all scenes at
  once.
- `auto_sync`, then `add_sync_point` wherever a reveal must land on a spoken word —
  in tutorials this matters most on UI-action words ("click", "select", "drag").

### 6. Verify and export

Render a mid-scene frame per clip with `get_clip(render=true, timestamp=<middle>)`:
legible at video scale, palette consistent, screenshots sharp, nothing static for more
than a beat. Fix via `update_elements`/`update_clips`, then `export_project` and give
the user the link.

If the source was a Clueso article and the user wants the video embedded alongside it,
offer to attach the export via `update_article` / `add_article_media`.

## Fallbacks

- **Article too long for one video** → propose splitting into a short series (one video
  per section) instead of a 4-minute monolith; build the first, confirm, repeat.
- **No screenshots available for UI steps** → abstract keyframed shapes + kinetic type;
  tell the user real screenshots would upgrade specific scenes and which ones.
- **`get_article` returns nothing / wrong article** → ask the user to paste the text.
- **Voiceover pacing collides with a dense scene** → split the clip (`split_clip`) and
  spread the reveals rather than speeding the voice
