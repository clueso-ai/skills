---
name: tighten-narration
description: >-
  Cut a video's script down to its essentials so it hits a target length —
  trim redundancy, keep every step, regenerate the narration, and re-align
  the visuals. Use when the user says "tighten the narration", "the
  voiceover is too wordy", "get this script down to 60 seconds", "make the
  narration punchier", or gives a video plus a target length the current
  script overshoots.
license: Apache-2.0
metadata:
  author: clueso
  category: quick-edits
  subcategory: narration
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Tighten Narration

Compress a video's script until it fits a target length — cutting
repetition, hedging, and throat-clearing while keeping every step and every
fact. The visuals stay; only the words get leaner.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (name or link it),
   or a raw screen recording they'll upload? Branch accordingly.
2. **Target length** — e.g. "90 seconds" or "about a third shorter". If the
   user doesn't have one, propose one based on the current runtime.

## Workflow

1. **Confirm the workspace** first.
2. **Read the full transcript** and note the current runtime. Estimate the
   spoken length of the script as it stands so you know the gap to close.
3. **Cut in passes, cheapest first:**
   - hedges and qualifiers ("basically", "go ahead and", "what we want to
     do is");
   - repetition — anything said twice, said once;
   - long wind-ups that restate what the viewer is about to see anyway.
   Never cut a step, a warning, or a number. If the target can't be reached
   without losing one of those, stop and tell the user what would have to
   go.
4. **Estimate as you cut.** After each pass, re-estimate the spoken length
   of the trimmed script. Iterate until the estimate lands on the target —
   don't regenerate audio just to measure.
5. **Regenerate the narration** from the final script.
6. **Re-check visual alignment.** Regeneration retimes the clips — shorter
   lines mean every section ends earlier. Walk the video and make sure each
   action, zoom, and annotation still lands on its line; fix any seams.
7. **Share a review link**, noting the old vs. new runtime, and wait for
   approval.
8. **Export** once approved.

## What good looks like

- The script sounds decisive, not rushed — cut words, don't speed speech.
- A viewer following along can still complete every step.
- Final runtime is within a few seconds of the target.
