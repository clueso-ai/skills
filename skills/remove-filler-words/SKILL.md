---
name: remove-filler-words
description: >-
  Strip ums, ahs, false starts, and rambling from a video's narration —
  clean the transcript, regenerate the voiceover, and keep the visuals
  aligned to the new timing. Use when the user says "remove the filler
  words", "clean up the ums and ahs", "the narration sounds rambly",
  "tidy up the voiceover", or shares a video whose spoken track is full
  of hesitations and false starts.
license: Apache-2.0
metadata:
  author: clueso
  category: quick-edits
  subcategory: narration
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Remove Filler Words

Take a video whose narration is littered with "um", "uh", "so basically",
false starts, and mid-sentence restarts, and return the same video with a
clean, confident spoken track. The message stays identical — only the noise
goes.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (have them name or
   link it), or a raw screen recording they'll upload? Branch accordingly —
   open the project, or bring the recording into a new project first.

That's the only required input. Everything else you can find in the video.

## Workflow

1. **Confirm the workspace** you're working in before touching anything.
2. **Read the full transcript** section by section. Mark every filler
   ("um", "ah", "like", "you know"), every false start, every sentence that
   restarts itself, and any rambling detour that adds no information.
3. **Clean, don't rewrite.** Delete the fillers and stitch the sentences
   back together so they read as if spoken cleanly the first time. Keep the
   speaker's vocabulary, order, and every factual claim exactly as they were
   — this skill removes noise, it does not change the message. When a
   passage is so tangled it can't be untangled, ask the user before
   paraphrasing it.
4. **Regenerate the narration** from the cleaned script.
5. **Re-check visual alignment.** Regenerating narration retimes the clips
   — the cleaned lines are shorter, so every section ends sooner. Walk
   through the video and confirm each on-screen action, zoom, and callout
   still lands on the words that describe it; re-sync any seam that
   drifted.
6. **Share a review link** with the user, with a note on roughly how much
   shorter the video got. Wait for their nod.
7. **Export** once approved.

## What good looks like

- The narration sounds like a prepared take, not a censored one — no
  audible gaps where fillers used to be.
- Runtime drops a little; meaning drops not at all.
- Nothing visual was edited except timing re-alignment.
