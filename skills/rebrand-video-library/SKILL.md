---
name: rebrand-video-library
description: >-
  Apply a new brand across existing videos after a rebrand — audit every scene
  for old colors, logos, fonts, and dated intros/outros, swap them for the new
  brand kit, and leave narration and timing untouched. Use when the user says
  "we rebranded, update our videos", "swap the old logo in this video", "apply
  our new brand colors to this video", "our video library still has the old
  branding", or "replace the intro with our new one".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Rebrand Video Library

The post-rebrand fire drill, handled: take a video (or a whole library of them)
made under the old brand and bring every scene onto the new one — colors, fonts,
logo, intro and outro — without re-recording anything and without touching a
single word of narration.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video(s) to rebrand** — ask the user: is each one an existing Clueso
   project (have them name or link it), or a raw screen recording they'll upload?
   For an existing project, work on it directly. For a recording, bring it into a
   new project first, then treat it the same way.
2. **The new brand kit** — colors (hex values if they have them), fonts, the new
   logo, and the new intro/outro if one exists. If the workspace already carries
   the new branding, confirm that and use it. If the user has nothing formal, ask
   for the two or three anchor colors and the logo at minimum.
3. **Scope** — one video, a named list, or "everything in this folder". For a
   batch, confirm the list before starting and process one video fully before
   moving to the next.

Confirm which workspace you're working in before editing anything.

## Workflow

### 1. Look before you touch

Never rebrand blind. Walk the whole video first: inspect rendered frames of each
scene alongside the transcript, and build an audit list of every old-brand
artifact — old palette on backgrounds and shapes, the old logo anywhere it
appears (intro, watermark, outro, inside a slide), old fonts on titles and
callouts, a dated intro or outro sequence, styled text elements carrying legacy
colors. Note the scene and timestamp for each. This audit is your work order and,
later, your before/after report.

Be suspicious of near-misses: a background that is *almost* the new blue, a logo
baked into the recorded screen itself (that one can't be swapped — flag it), a
lower-third using the old accent color.

### 2. Swap, don't redesign

Work through the audit list scene by scene:

- **Backgrounds and shapes** — recolor to the new palette. Map old colors to new
  ones consistently (old primary → new primary, old accent → new accent) rather
  than choosing per scene.
- **Text styles** — new fonts and text colors on every title, caption, callout,
  and lower-third. Keep sizes and positions as they were; this is a rebrand, not
  a relayout.
- **Logos** — replace every placed logo with the new one at the same position and
  scale. Check corners and watermarks, not just the intro.
- **Intro/outro** — replace the dated intro and outro with the new ones. If no
  new intro exists yet, build a minimal one: logo moment plus title on the new
  palette, matching the original's duration so downstream timing is unmoved.

### 3. What you must not touch

Narration, script, scene order, cuts, and timing stay exactly as they are. The
video should sound identical before and after. If a narration line literally
speaks the old company or product name, don't fix it silently — flag it to the
user and offer a separate narration patch as a follow-up, outside this pass.

No music or sound effects — never add any.

### 4. Verify like a brand reviewer

Re-inspect frames at every point your audit flagged, plus the intro, outro, and
one frame per scene. You're checking: no old color survives, the new logo is
crisp and correctly placed, text is legible against any recolored backgrounds
(fix contrast by adjusting the background shade within the new palette, not by
moving text).

### 5. Review with before/after notes

Share the review link with the user along with a short change log: for each
scene touched, one line — what was old, what it is now ("Scene 3: background
#1A2B3C → new navy; old logo watermark replaced"). Include anything you flagged
but could not change (branding baked into the screen recording, narration that
names the old brand). Wait for their nod.

### 6. Export

Only after approval, export. For a batch, deliver the videos one by one as each
is approved, and keep a running list of which are done and which remain.

## Watch out for

- **Branding inside the footage itself** — a recorded screen showing the old
  product logo can only be fixed by re-recording; say so plainly rather than
  attempting cover-up patches that look worse than the original.
- **Partial brand kits** — if the user gives colors but no fonts, change only
  what you were given and note what was left as-is.
- **Contrast regressions** — the most common rebrand bug. Every recolor gets a
  legibility check.
