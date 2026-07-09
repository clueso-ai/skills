---
name: stitch-videos
description: >-
  Combine two or more videos into one coherent piece with consistent
  styling and bridging narration between the parts. Use when the user says
  "stitch these videos together", "combine these recordings into one",
  "merge these two videos", "join my clips into a single video", or has
  several separate captures that should play as one.
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Stitch Videos

Join multiple videos into a single piece that flows like it was made as
one: consistent styling, a sensible order, and a bridging narration line at
each junction so the parts hand off instead of colliding.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The videos (2+)** — for each, ask: existing Clueso project, or a raw
   screen recording they'll upload? This matters here more than usual:
   - **Uploaded recordings** combine directly — bring them all into one
     project and sequence them. The easy path.
   - **Existing Clueso projects** can't be merged in place. Be upfront:
     each project to merge must take one extra hop — export it as a
     finished video, then bring that export in as footage alongside the
     rest. It works fine; it just costs a round trip, and the imported
     part arrives as flattened footage (its individual edits are no longer
     separately editable). Confirm the user is okay with this before
     starting.
2. **The order** — the desired sequence, or "figure out what flows best".

## Workflow

1. **Confirm the workspace** first.
2. **Gather all footage into one project** via the paths above, and place
   it in the agreed order.
3. **Unify the look.** Match aspect ratios and framing, and carry one set
   of brand colors/fonts across any titles or overlays so the seams don't
   announce themselves. If the parts have different narration voices, pick
   one voice for anything you add (and offer to revoice the rest — a
   separate job — if the mismatch is jarring).
4. **Bridge the junctions.** At each join, add one short narrated line
   that hands off ("with the account set up, let's import your data") —
   over the incoming footage or a brief title card, matching the video's
   pacing. Trim any redundant intros/outros inside the parts ("hi, in this
   video...") that made sense standalone but not mid-stream.
5. **Re-check alignment** wherever you added or changed narration — new
   lines retime their clips.
6. **Share a review link** and wait for the user's nod.
7. **Export** the single combined video once approved.

## What good looks like

- One continuous piece — a viewer can't find the joins.
- No leftover per-part intros, outros, or duplicate explanations.
