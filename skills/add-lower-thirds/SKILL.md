---
name: add-lower-thirds
description: >-
  Add branded lower-third labels to an existing video — section names, feature
  names, speaker names — that slide in at the start of each segment. Use when
  the user says "add lower thirds", "add section labels", "label each part of
  the video", "add name titles", or "add branded segment titles".
license: Apache-2.0
metadata:
  author: clueso
  category: quick-edits
  subcategory: visual-emphasis
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Add Lower Thirds

Give a video broadcast-style wayfinding: a branded label in the lower third of
the frame that slides in as each new segment begins, telling viewers where
they are without interrupting anything.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (have them name or link
   it), or a raw screen recording they'll upload? Branch accordingly.
2. **The labels** — each label's text and the segment it applies to; or derive
   segment boundaries and names from the narration and confirm with the user.
3. **Brand** — colors and fonts, or "use workspace branding".

Confirm the target workspace before editing anything.

## Workflow

### 1. Map the segments

Read the narration transcript to find where each segment begins — topic shifts,
"next, we'll…", a new feature taken up. Pair each boundary with its label text:
short and functional, 2-5 words ("Setting up SSO", "Priya Shah — Support Lead").
Confirm the label list and timings with the user if you derived them.

### 2. Design one lower third, use it everywhere

One design for the whole video: a compact bar or plate in the lower-left (or
lower-center) with the label text, in brand colors and fonts. Slide or fade it
in at each segment start, **hold 4-6 seconds**, then exit cleanly — long enough
to read twice, short enough to not become furniture. Same position, size,
animation, and duration at every appearance; lower thirds are a system, not
individual title cards.

### 3. Place and verify against frames

Add the lower third at each segment boundary. Then inspect rendered frames
while each one is on screen: does it cover anything that matters down there —
a taskbar, a form's submit button, on-screen captions? Is the text legible
against the footage behind it at that moment, and inside safe margins? Nudge
position, add a solid backing, or shift timing a beat until every appearance
is clean, and re-check the frames after each fix.

### 4. Review, then export

Share the review link and get the user's nod before exporting. Then export and
hand over the final link.
