---
name: shorten-to-length
description: >-
  Get a video under a hard time limit by deciding what to cut and what to
  compress, while protecting a must-keep list and the core message. Use
  when the user says "get this under 2 minutes", "shorten this to 60
  seconds", "it needs to fit in 90 seconds for the campaign", "cut this
  down but keep the demo", or gives a video plus a time budget it
  currently blows through.
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Shorten To Length

Bring a video in under a hard time budget by making editorial calls — what
gets cut entirely, what gets compressed, what is untouchable — instead of
shaving everything evenly into mush.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (name or link it),
   or a raw screen recording they'll upload? Branch accordingly.
2. **The target length** — a hard number.
3. **The must-keep list** — sections, moments, or claims that must survive
   intact. If the user doesn't give one, propose one from the content and
   confirm it.

## Workflow

1. **Confirm the workspace** first.
2. **Budget before cutting.** Note the current runtime and the gap. List
   the sections with their durations and triage each: **keep** (on the
   must-keep list or load-bearing), **compress** (needed but wordy or
   slow), **cut** (nice-to-have, repetition, tangents).
3. **Get sign-off on the plan.** Show the user the triage with the
   projected new runtime before touching anything — the cuts are editorial
   decisions and they should own them.
4. **Cut whole sections first.** Removing one tangent cleanly beats
   nibbling at ten sections. Then compress the "compress" bucket: tighten
   narration to fewer words, trim dead time inside the footage, let one
   example stand where three stood.
5. **Estimate as you go.** Re-estimate spoken length after each pass and
   iterate until the projection is safely inside the budget — leave a
   couple of seconds of headroom rather than landing exactly on the line.
6. **Regenerate the changed narration and re-check alignment.**
   Regeneration retimes clips; walk the full video and fix any seams where
   visuals no longer land on their words.
7. **Share a review link** with old vs. new runtime and a list of what was
   cut. Wait for the user's nod.
8. **Export** once approved.

## What good looks like

- Under budget, with the must-keep list untouched.
- The short cut feels designed at that length — not a long video with
  holes in it.
