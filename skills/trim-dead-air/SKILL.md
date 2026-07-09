---
name: trim-dead-air
description: >-
  Remove silences, loading screens, and hesitation gaps from a video so it
  keeps moving, with a light, standard, or tight aggressiveness setting.
  Use when the user says "trim the dead air", "cut the silences", "there's
  too much waiting around", "remove the loading screens", "make it feel
  faster without changing anything", or shares a recording full of pauses
  and idle screens.
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Trim Dead Air

Cut the moments where nothing happens — silences between sentences, spinner
screens, pauses while the presenter finds the button — so the video moves at
the speed of its content. Nothing is rewritten and nothing is reordered;
time is simply removed.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (name or link it),
   or a raw screen recording they'll upload? Branch accordingly.
2. **Aggressiveness** — default **standard** if unspecified:
   - **light** — cut only clear dead stretches (over ~3s of nothing);
     keep a relaxed rhythm.
   - **standard** — cut anything idle beyond ~1.5s; leave a beat (~0.5s)
     after each completed action so viewers register the result.
   - **tight** — cut everything beyond ~0.75s of idle; demo-reel pacing.
     Warn the user this can feel breathless for training content.

## Workflow

1. **Confirm the workspace** first.
2. **Map the dead zones.** Use the audio to find silences and the visuals
   to find idle screens: loading spinners, unchanged frames, cursor
   wandering, long typing into a field. Note each gap's start, end, and
   what surrounds it.
3. **Cut at the chosen aggressiveness.** Split around each dead zone and
   remove the middle. Always leave the "result frame" — the moment the page
   has loaded or the action has completed — so cause and effect stay
   readable.
4. **Protect intentional pauses.** A pause after a key statement or before
   a reveal is rhetoric, not dead air. When in doubt, keep it at light and
   standard; only tight may take it.
5. **Check the seams.** Play across every cut: no clipped words, no jump
   that hides an action the viewer needed to see.
6. **Share a review link** with the before/after runtime and how many gaps
   were cut. Wait for the user's nod — offer to go one level tighter or
   looser if it doesn't feel right.
7. **Export** once approved.

## What good looks like

- The video never idles, but every action and its result remain visible.
- Speech is untouched — only the space between it is gone.
