---
name: apply-brand-colors
description: >-
  Recolor every overlay, text element, background, and shape in an existing
  video to the brand palette in one pass, leaving footage, narration, and
  timing untouched. Use when the user says "apply our brand colors", "make
  this video on-brand", "recolor the overlays to our palette", "fix the
  colors to match our brand", or "this video doesn't match our brand kit".
license: Apache-2.0
metadata:
  author: clueso
  category: quick-edits
  subcategory: branding-and-polish
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Apply Brand Colors

Take a video whose overlays and text drifted off-brand and bring every designed
element — text styles, callouts, shapes, backgrounds, title cards — onto the brand
palette in a single consistent pass, without touching the footage, narration, or
timing.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## What you need

- **The video.** Ask: is it an existing Clueso project (have them name or link it),
  or a raw screen recording they'll upload? If it's a recording, bring it into a new
  project first — then the pass runs the same way.
- **The brand.** Colors and fonts from the user, or "use workspace branding" — if
  the workspace has branding set, default to it and confirm rather than re-asking.

Confirm the target workspace before editing anything.

## How to run the pass

1. **Map the palette first.** Decide the role of each brand color before touching
   anything: one primary for emphasis (callouts, highlights, key text), one
   background/base, one neutral for body text, at most one accent. Every decision
   below follows this map — that's what makes the result read as one system instead
   of a re-tint.
2. **Audit the whole video.** Walk every scene and list each designed element with
   its current color: text, callout boxes, arrows, rectangles, spotlights, lower
   thirds, backgrounds, intro/outro cards. Screen-recording footage itself is not
   recolored — only what was added on top of it.
3. **Recolor by role, not one-by-one.** Apply the map: all emphasis elements get the
   primary, all backgrounds get the base, all body text gets the neutral. Swap fonts
   to the brand typefaces where text styles are off. Keep sizes, positions, timings,
   and animations exactly as they are.
4. **Check contrast.** Anywhere brand colors land text on a similar-toned
   background, adjust the text to the palette's readable counterpart. On-brand but
   unreadable is a failure.

## Review

Share a review link with a short note of what changed (e.g. "12 callouts, 3 title
cards, all backgrounds recolored; footage and narration untouched"). Get the user's
nod before the final export.

## Avoid

- Recoloring the recorded product UI — the pass covers overlays only.
- Introducing colors outside the brand palette "to make something pop".
- Changing any timing, wording, or layout — this skill changes color and type only.
