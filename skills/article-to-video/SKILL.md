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
and export. The "intelligence" (reading, distilling, scripting) is yours; the media
work is Clueso's.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

One of:

- **Pasted text** — the article body in the conversation.
- **A Clueso article** — fetch it from the workspace by name or link.
- **A file** — ask the user to paste the content or attach it; do not reach for
  external fetching tools this skill doesn't require.

Plus: intended audience and target length if the user has one (default: 60-90s for a
how-to, 30-45s for a changelog).

If the article contains images/screenshots the user can provide, collect them — real
screenshots beat anything generated.

## Workflow

### 1. Confirm the workspace

List the available workspaces, confirm the active one with the user, and switch if
needed.

### 2. Distill — don't transcribe

An article read aloud is not a video script. Extract:

- **The one-sentence point** of the article (this becomes the hook).
- **3-6 steps or ideas**, each collapsed to its action and its outcome. Cut caveats,
  edge cases, and anything parenthetical — the article remains the reference for those.
- **The payoff** — what the viewer can now do.

Write the voiceover script: hook → steps/ideas in order → payoff. One scene per step.
Conversational, second person, present tense ("Click **Export** and pick a format" not
"The user may then choose to export"). Estimate the spoken duration; trim until it
fits the target length.

Show the user the script before composing.

### 3. Pick the visual direction

Search for an existing template (clueprint) in a tutorial / explainer / changelog
style — if a strong match exists, offer it and follow its design. Otherwise pull up
Clueso's design guide, commit to a palette (workspace brand colors first if
available), and follow the guide.

### 4. Build the project

Create the project, then add one clip per scene with durations from the script.
Before composing the first scene, check which element options Clueso actually exposes
and compose with real ones, not guessed ones.

Scene composition by content type:

- **Step with a screenshot available** → upload the image, wait for processing, place
  it, then keyframe attention: a zoom toward the relevant region, a traveling
  highlight rectangle, or a callout that pops in on the key phrase of the narration.
- **Step without a screenshot** → kinetic typography carrying the step's action words
  (masked reveals, slides, typewriter effects; word-level reveals for emphasis beats),
  plus simple keyframed shapes (a rectangle standing in for a panel, a progress bar
  growing, a toggle flipping). Do NOT mock up the product's actual UI from
  imagination — abstract shapes, not fake screenshots.
- **Conceptual idea (non-UI)** → consider a generated animation for a mechanism or
  chart, but only if a few keyframed rectangles genuinely can't carry it. Boxed, not
  full-canvas, when the scene also has text.
- **Lists in the article** → reveal items one at a time synced to the voice, swapping
  or dimming previous items — never a static bullet wall.

### 5. Narrate and sync

- Pick a voice (ask if the user has a preference) and generate narration for all
  scenes in one pass.
- Run an automatic sync, then pin any reveal that must land on a spoken word — in
  tutorials this matters most on UI-action words ("click", "select", "drag").

### 6. Verify, review, then export

Render a mid-scene frame per clip: legible at video scale, palette consistent,
screenshots sharp, nothing static for more than a beat. Fix what's off, then share
the project review link with the user. Export only after they confirm, and give them
the export link.

If the source was a Clueso article and the user wants the video embedded alongside
it, offer to attach the export to the article.

## Fallbacks

- **Article too long for one video** → propose splitting into a short series (one video
  per section) instead of a 4-minute monolith; build the first, confirm, repeat.
- **No screenshots available for UI steps** → abstract keyframed shapes + kinetic type;
  tell the user real screenshots would upgrade specific scenes and which ones.
- **Can't locate the Clueso article / wrong article comes back** → ask the user to
  paste the text.
- **Voiceover pacing collides with a dense scene** → split the clip and spread the
  reveals rather than speeding the voice.
