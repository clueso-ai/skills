---
name: chapterize-video
description: >-
  Split a long video into titled chapters with a clean title card at each
  boundary. Use when the user says "add chapters", "chapterize this",
  "break this into sections with titles", "add section title cards", or
  shares a long training or walkthrough video that runs as one unbroken
  stream.
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Chapterize Video

Turn one long unbroken video into a clearly sectioned piece: a split at
every topic boundary and a short, consistent title card announcing each
chapter. The content itself is not cut or rewritten — it just gets signposts.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (name or link it),
   or a raw screen recording they'll upload? Branch accordingly.
2. **The chapter list** — titles and rough boundaries, or "detect the
   sections". Brand colors/fonts if the title cards shouldn't use workspace
   branding.

## Workflow

1. **Confirm the workspace** first.
2. **Find the boundaries.** If detecting: read the transcript for topic
   shifts ("next, let's...", a new screen, a new task) and confirm your
   proposed chapter list — titles plus timestamps — with the user before
   cutting. A chapter should be a task a viewer might seek directly to;
   3-7 chapters suits most videos, and a chapter under ~20 seconds is
   usually a step, not a chapter.
3. **Write the titles.** Short and parallel in form — verb-first works
   well ("Connect your account", "Import the data", "Review and publish").
   Number them if viewers are expected to go in order.
4. **Split at each boundary**, cutting in the silence between sentences,
   never mid-word or mid-action.
5. **Insert title cards.** One short card (~2-3s) per chapter: chapter
   number and title on a brand-colored background, one consistent design
   and entry animation across all cards. No narration needed on cards —
   the pause is the punctuation. Keep the cards silent design-wise too:
   no sound effects.
6. **Check every seam.** Play across each card: narration shouldn't be
   clipped, and the card shouldn't interrupt a sentence.
7. **Share a review link** with the chapter list and timestamps, and wait
   for the user's nod.
8. **Export** once approved.

## What good looks like

- A viewer can scrub to any chapter and land at a clean starting point.
- Cards are identical in style and rhythm — signposts, not scenes.
