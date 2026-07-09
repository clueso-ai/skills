---
name: reorder-scenes
description: >-
  Restructure a video's narrative by re-sequencing its sections into a
  better order and smoothing the narration seams so the new flow sounds
  intentional. Use when the user says "reorder the scenes", "move the
  pricing part to the end", "lead with the outcome", "restructure this
  video", or wants the same material told in a different order.
license: Apache-2.0
metadata:
  author: clueso
  category: quick-edits
  subcategory: structure-and-timing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Reorder Scenes

Retell an existing video in a better order — lead with the outcome, group
related steps, push the caveats to the end — and re-stitch the narration so
the seams disappear. Be upfront with the user: this is a careful
restructure, not an instant drag-and-drop, because moving a section also
means rewriting the connective tissue around it.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (name or link it),
   or a raw screen recording they'll upload? Branch accordingly.
2. **The desired order** — an explicit sequence, or a goal like "lead with
   the outcome" / "put setup last" that you translate into one.

## Workflow

1. **Confirm the workspace** first.
2. **Map the current structure.** List the video's sections with what each
   covers and where its boundaries fall. Propose the new order back to the
   user as a simple before/after list and get agreement before moving
   anything.
3. **Check for broken dependencies.** A section that says "the account we
   just created" can't run before the creation step. Flag any ordering the
   material won't support and offer the closest order that works.
4. **Re-sequence the sections.** Split cleanly at the agreed boundaries and
   rebuild the timeline in the new order. Depending on what the platform
   supports, this may mean duplicating sections into their new positions
   and removing the originals — do it carefully and verify the result
   scene by scene rather than assuming a single move did it.
5. **Smooth the narration seams.** This is where reorders live or die:
   rewrite the first and last line of each moved section so transitions
   make sense in the new order ("now that you've seen the result, here's
   the setup..."), and strip stale connectives ("as we saw earlier") that
   now point the wrong way. Regenerate only the lines you changed.
6. **Re-check visual alignment** at every seam — regenerated lines retime
   their clips, so confirm actions still land on their words.
7. **Share a review link** with the old vs. new outline, and wait for the
   user's nod.
8. **Export** once approved.

## What good looks like

- A first-time viewer can't tell the video was ever in another order.
- No dangling references to things "we just did" that now come later.
