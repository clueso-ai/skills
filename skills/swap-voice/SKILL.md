---
name: swap-voice
description: >-
  Change a video's narration voice — accent, gender, energy — without
  touching the script, offering a shortlist of three fitting voices first.
  Use when the user says "change the voice", "use a different narrator",
  "make it a British accent", "I want a warmer/more energetic voice",
  "swap the voiceover voice", or wants the same words spoken by someone
  else.
license: Apache-2.0
metadata:
  author: clueso
  category: quick-edits
  subcategory: narration
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Swap Voice

Replace the narrator of a finished video while leaving every word of the
script exactly as it is. The user picks from a short, well-argued shortlist
— not a wall of voice names.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (name or link it),
   or a raw screen recording they'll upload? Branch accordingly.
2. **Voice direction** — a specific preference (accent, gender, energy,
   language) or "suggest some". Either way, the shortlist step below still
   applies unless they name an exact voice.

## Workflow

1. **Confirm the workspace** first.
2. **Read the room.** Skim the transcript and note the video's job — a
   calm training module wants a different voice than a launch teaser. Note
   the language too; the new voice must sound native in it.
3. **Offer a shortlist of 3.** Browse the available voices and pick three
   that fit the direction and the content, each with a one-line reason
   ("warm and unhurried — suits step-by-step training"). Present them and
   let the user choose; don't pick silently on their behalf.
4. **Apply the chosen voice and regenerate the narration.** The script is
   untouched — same words, same order, same everything. If the user asks
   for wording changes mid-way, flag that that's a different job and
   confirm before doing it.
5. **Re-check visual alignment.** A new voice paces differently, so
   regeneration retimes the clips. Walk the video and confirm every
   action, zoom, and callout still lands on its line; fix any drift.
6. **Share a review link** and wait for the user's nod — voices are a
   taste call, so expect a possible second pick from the shortlist.
7. **Export** once approved.

## What good looks like

- The new voice fits the content's register, not just the user's adjective.
- Zero script drift: the transcript before and after is identical.
- Timing feels native to the new voice — no visuals outrunning the words.
