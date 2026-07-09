---
name: refresh-outdated-video
description: >-
  Surgically update a stale video after a UI or feature change — replace only
  the outdated sections with new material and patch only the narration lines
  that mention old names or flows, leaving everything else untouched. Use when
  the user says "this video shows the old UI", "update this video, the feature
  got renamed", "refresh this outdated tutorial", "the flow changed, fix the
  video", or "patch this video without redoing it".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Refresh Outdated Video

Surgery, not a remake: find exactly which sections of a stale video no longer
match the product, swap in current footage there, patch only the narration lines
that mention old names or flows — and leave every other frame and every other
word exactly as it was.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The stale video** — ask the user: is it an existing Clueso project (name or
   link it), or a raw screen recording they'll upload? Existing project is the
   normal case here; if it's a raw recording, bring it into a project first.
2. **What changed** — new UI on certain screens, a renamed feature, a reordered
   flow, a removed step. Get this in the user's words; it seeds your search but
   doesn't replace it.
3. **Updated material** — a fresh recording or screenshots of the changed
   screens, or explicit permission to capture the product again. Without one of
   these you can patch narration but not visuals; say so up front.

Confirm the workspace before editing anything.

## Workflow

### 1. Diagnose before cutting

Watch the whole video the way a reviewer would: inspect rendered frames of each
scene against the transcript, and compare what's on screen with what the user
says changed. Build a precise list of stale spans — scene, timestamp range, and
what's wrong (old button label, moved menu, renamed feature spoken aloud,
vanished step). Check beyond the spots the user pointed at: a renamed feature
usually appears in more scenes than anyone remembers, both on screen and in the
voiceover.

Present this list to the user before touching anything: "these N sections are
outdated, everything else is current". Agree on the scope. The whole value of
this skill is that the blast radius is known and small.

### 2. Replace only the stale visuals

For each stale span, cut precisely around it and drop in the new material —
trimmed so the new footage covers the same step at roughly the same duration.
Match the visual grammar of the surrounding video: if neighboring scenes zoom
into the active control, the new section should too; if they run full-frame and
calm, don't suddenly add emphasis. The patch should be invisible.

If the replacement footage runs meaningfully longer or shorter than the
original span, adjust that section's narration pacing rather than letting the
seams drift.

### 3. Patch only the affected narration

Read the transcript and change *only* the lines that state something now false —
old feature names, "click X then Y" orders that reversed, references to removed
steps. Rewrite each patched line in the same tone, tense, and sentence rhythm as
its neighbors, then regenerate narration for those lines only, in the same voice
as the rest. Never regenerate untouched lines: even the same voice can render a
line subtly differently, and a wholesale regeneration turns a patch into a
remake.

### 4. Check the seams

The failure mode of surgical edits is the seam. At each boundary between old and
new material, inspect frames and listen for: an audio gap or clipped word, a
visual jump (different zoom level, different window size), a pacing hiccup where
the new section rushes or drags against its neighbors. Fix by nudging cut points
and section timing until each transition is unremarkable.

### 5. Review, then export

Share the review link with a short patch report: which sections were replaced,
which narration lines were rewritten (old line → new line), and confirmation
that everything else is untouched. When the user approves, export.

No music or sound effects at any point.

## Watch out for

- **Scope creep** — the user says "while you're in there…" mid-edit. New asks
  become a listed follow-up, not silent additions; the agreed patch list is the
  contract.
- **A change too big for a patch** — if more than roughly half the video is
  stale, a refresh will look like a quilt. Tell the user honestly and recommend
  a rebuild instead.
- **New footage at a different resolution or window size** — visible as a jolt
  at the seam. Ask for a capture matching the original's framing, or crop/scale
  the patch to match.
