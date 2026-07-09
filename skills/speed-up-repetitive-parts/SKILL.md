---
name: speed-up-repetitive-parts
description: >-
  Compress the boring, repetitive stretches of a video — long form fills,
  waiting, repeated steps — by cutting the middle out and adding a brief
  "sped up" cue so the pacing stays honest. Use when the user says "speed
  up the boring parts", "time-lapse the form filling", "fast-forward
  through the waiting", "the repetitive section drags", or shares a video
  with long stretches of the same action repeating.
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Speed Up Repetitive Parts

Make the repetitive stretches of a video pass in seconds — show the start,
skip the middle, land on the result, with an on-screen cue so viewers know
time was compressed. Be honest with the user about the method: this isn't a
playback-speed change (there's no true fast-forward effect); it's a tight
cut that reads like one, and for most footage it looks cleaner anyway.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (name or link it),
   or a raw screen recording they'll upload? Branch accordingly.
2. **The sections to compress** — pointed out by the user, or "find them":
   look for long form fills, installation/processing waits, and the same
   step repeated for the third item in a row.

## Workflow

1. **Confirm the workspace** first.
2. **Identify the stretches** and confirm the list with the user — what
   you'll compress and what each stretch will collapse to.
3. **Compress by cutting, keeping the story beats:** for each stretch keep
   the first action (so viewers see how it starts), cut the repetitive
   middle, and keep the completed result (so they see where it ends). For
   repeated steps, show the first repetition in full and jump to the last.
4. **Add the honesty cue.** A small, consistent on-screen label over each
   compressed stretch — "sped up" or "3 of 12 shown" — appearing at the
   cut and gone by the landing. One style, one corner, every time.
5. **Keep narration truthful at the seams.** If the voice was describing
   the skipped middle, patch it to bridge instead ("...and the same for
   the rest — here's everything imported"). Regenerate only the lines you
   changed, then re-check that visuals still land on their words —
   regenerated narration retimes the clips.
6. **Share a review link** noting each compressed stretch and the runtime
   saved. Wait for the user's nod.
7. **Export** once approved.

## What good looks like

- Viewers always know time was skipped and never wonder what they missed.
- Each compressed stretch still shows its start and its result.
- The label is a whisper, not a banner — visible, consistent, unobtrusive.
