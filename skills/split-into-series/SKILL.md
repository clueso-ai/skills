---
name: split-into-series
description: >-
  Cut one long video — a webinar, training session, or full walkthrough —
  into a series of short standalone videos, each with its own title and
  intro line. Use when the user says "split this into a series", "break
  this webinar into short videos", "make bite-sized videos out of this
  training", "turn this into separate videos per topic", or shares one long
  recording that should become several.
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Split Into Series

Turn one long video into several short ones that each stand on their own:
a viewer who opens part 3 first should never feel like they walked into the
middle of a conversation. Each part gets its own title and a one-line intro
that sets its context.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (name or link it),
   or a raw screen recording they'll upload? Branch accordingly.
2. **How to split** — by topic (default) or by target length (e.g. "parts
   of about 3 minutes"). Any naming convention for the series titles.

## Workflow

1. **Confirm the workspace** first.
2. **Propose the split.** Read the transcript and find self-contained
   units: one task, one question answered, one topic. Present the proposed
   parts — title, what it covers, rough runtime — and get the user's
   agreement before cutting. Topic beats stopwatch: never split
   mid-explanation just to hit a length.
3. **Build each part as its own standalone video** — one project per part,
   containing only that part's footage, so each exports independently.
   Cut at sentence boundaries, in silence.
4. **Make each part self-sufficient:**
   - **Title** — parallel across the series ("Getting Started with X — 2:
     Importing Data"), shown briefly at the top of the video.
   - **Intro line** — one narrated sentence of context written fresh for
     that part ("Now that your account is connected, let's import your
     data"), in the same voice as the original.
   - **Cleanup** — strip references that only made sense in the long cut
     ("as I said an hour ago", "we'll cover that later" when "later" is a
     different part; point to the part by name instead).
5. **Re-check alignment** on any clips whose narration you touched — new
   or edited lines retime them.
6. **Share review links for all parts** as a set, with the series outline,
   and wait for the user's nod.
7. **Export each part** once approved.

## What good looks like

- Any part watched alone makes complete sense.
- Titles and intros follow one consistent pattern across the series.
