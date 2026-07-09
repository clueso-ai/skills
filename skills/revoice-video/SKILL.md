---
name: revoice-video
description: >-
  Give an existing video a narration makeover — rewrite the script in a new
  tone (tighter, warmer, more formal, more energetic), pick a fitting voice,
  regenerate the voiceover, and re-align the visuals to the new timing. Use
  when the user says "make the narration less robotic", "rewrite the voiceover
  to sound friendlier", "this video sounds too stiff, revoice it", "change the
  tone of this video", or "redo the narration in a different style".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Revoice Video

A narration makeover for a video whose visuals are fine but whose voice isn't:
rewrite the script in the tone the user wants without losing a single technical
fact, regenerate it in a voice that matches, and re-align the visuals so every
on-screen moment still lands on its spoken word.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask the user: is it an existing Clueso project (name or link
   it), or a raw screen recording they'll upload? For a raw recording with
   spoken audio, bring it into a project and treat its speech as the source
   script to rewrite.
2. **The target tone** — tighter, warmer, more formal, more energetic, more
   conversational. Push past the adjective: "warmer for whom?" A tone brief is
   best captured as a sentence like "a helpful colleague showing a teammate,
   not a manual being read aloud."
3. **Voice preference** — a specific voice, qualities ("calm, low, neutral
   accent"), or "pick for me". Language stays the same by default.

Confirm the workspace before editing anything.

## Workflow

### 1. Understand what the video is doing

Before rewriting a word, inspect rendered frames of each scene alongside the
transcript. Note, per scene: what happens on screen, which narration phrase the
action is synced to, and where emphasis (zooms, callouts) lands on a specific
spoken word. These action-word anchors are what you must preserve through the
rewrite — a sentence can change shape, but the moment that says "click
**Export**" still has to say it while the cursor is on the button.

### 2. Rewrite the script, preserve every fact

Rewrite scene by scene, in the target tone, under hard constraints:

- **Every technical fact survives** — feature names, step order, settings,
  numbers, warnings. Tone changes; truth doesn't.
- **Keep roughly the same length per scene** — within about ±20% of the original
  line, so the visuals still fit. Tighter tone may shorten lines; that's fine,
  the re-alignment step absorbs it. A rewrite that doubles a line's length is a
  rewrite that breaks the scene.
- **Write for the ear** — short sentences, present tense, contractions if the
  tone is casual. Read each line aloud mentally; anything you'd stumble on, the
  voice will too.
- Show the user the rewritten script (old line → new line, per scene) and get a
  yes before generating anything. Script review is cheap; regeneration churn
  isn't.

### 3. Choose the voice

Pick a voice that matches the tone brief — an energetic script in a flat voice
lands worse than the original. If the user said "pick for me", choose one and
name one alternate. If they want to compare, generate one short scene in each
candidate rather than the whole video.

### 4. Regenerate and re-align

Generate the full narration in the chosen voice, then re-align the visuals to
the new timing: scene durations follow the new spoken length, and every zoom,
callout, and highlight is re-anchored to its action word from the step-1 notes.
Then verify the sync by inspecting frames at each anchor moment — the emphasis
must land while the word is being spoken, not a beat after.

No music or sound effects — the voice carries this video alone.

### 5. Review, then export

Share the review link and ask the user to listen to at least the opening scene
and one mid-video scene — tone judgments need ears, not transcripts. Iterate on
specific lines if asked (regenerate only those lines). Export only after their
nod.

## What good sounds like

- The first sentence sounds like a person, not a product sheet.
- No line the listener has to rewind to parse.
- Sync so tight the viewer never notices there is sync.
- A colleague who knew the old video says "same video, but suddenly it's good"
  — and can't point to a single changed fact.

## Watch out for

- **Tone drift across scenes** — rewrites done scene-by-scene can start warm and
  end formal. Re-read the full script top to bottom before generating.
- **Jokes and flourish in step instructions** — energy belongs in openings and
  transitions; steps stay clean and literal in any tone.
- **The original was mis-synced** — don't faithfully reproduce old sync bugs;
  fix them and mention it in the review notes.
