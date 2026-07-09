---
name: software-training-video
description: >-
  Turn a steps list, SOP doc, or rough recording into an internal software
  training video — role-framed intro, numbered step scenes with visible step
  markers, attention guided to every field and click, and a "what changes for
  you" close. Use when the user says "make a training video for this tool",
  "teach the team how to use X", "onboarding video for this workflow",
  "rollout video for the new system", or "turn this SOP into a training video".
license: Apache-2.0
metadata:
  author: clueso
  category: video-creation
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Software Training Video

Turn a steps list, an SOP doc, or a rough screen recording into an internal
training video that employees actually follow: a role-framed intro that says
why this matters to *them*, numbered step scenes with visible step markers,
the eye guided to every field and click, and a "what changes for you" close.
Built for L&D and change-management rollouts.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

Collect these before building. Ask for anything missing rather than inventing it:

1. **The tool or process being trained**, and the specific workflow if the
   tool is big ("submitting expenses in Concur", not "Concur").
2. **Source material** — a steps list, an SOP doc, or a rough recording of
   someone doing the task. If it's a recording, ask: is it an **existing
   Clueso project** (name or link it), or a **screen recording they'll
   upload**? Branch accordingly.
3. **The audience's role** — who watches this, and what they do all day. The
   intro is framed around their job, not the software.
4. **What changed** (if this is a rollout or migration) — the old way, the new
   way, and the cutover date. Change-management videos live or die on
   contrast.
5. Optional: length target (default 2-4 minutes), brand preferences.

## Workflow

1. **Confirm the workspace** before creating or editing anything.
2. **Check for an existing template** matching a training/walkthrough style
   and offer the best fits before building from scratch.
3. **Extract the canonical steps.** From the source material, write the
   numbered step list — each step one action with one visible result. Merge
   trivial clicks into their parent step; split anything with a decision in
   it. Confirm the step list with the user before building; it is the spine
   of the video.
4. **Open role-first.** 10-15 seconds: "If you <do this part of the job>,
   here's what's changing and why it helps you" — the viewer's workload,
   not the vendor's feature list. For rollouts, name the cutover date here.
5. **Build one scene per step, with a visible step marker.** A persistent
   "Step 3 of 7" style marker so a viewer pausing to follow along always
   knows where they are.
   - Show the real screen doing the real step, trimmed of dead time.
   - Guide the eye every time: zoom to the field being filled, call out the
     button before it's clicked, dim or blur what doesn't matter. The rule:
     if the narration names a control, something on screen points at it.
   - Narrate the pattern *action → location → result*: "Click Submit — top
     right — and the request moves to Pending."
6. **Handle the forks.** If a step branches ("managers see an extra approval
   screen"), show the main path fully and cover the branch with a short
   labeled aside — don't interleave two paths in one sequence.
7. **Close with "what changes for you."** A summary card restating the 2-3
   things the viewer now does differently, plus where to get help. For
   migrations, a simple old-way/new-way table scene lands this best.
8. **Narrate clearly and unhurriedly.** Second person, present tense, no
   jargon the audience's role wouldn't use. Pacing should let a viewer follow
   along live in a second window. No music, no sound effects.
9. **Review before export.** Share the review link — ask the user to check
   the step list against reality one last time (stale steps are the #1
   training-video defect). Apply notes, then export.

## What good looks like

- A viewer can pause at any step and see exactly where they are and what to
  click next.
- The intro answers "why do I care" in the viewer's own terms before any UI
  appears.
- Every click the narration mentions is visually pointed at on screen.
- The close tells them what's different tomorrow morning, not what was covered.

## Fallbacks

- **Rough recording wanders or backtracks** → keep only the clean take of
  each step; if a step was never done cleanly, ask for a re-record of just
  that step.
- **Steps list and recording disagree** → the recording is evidence, the list
  is intent; surface the mismatch to the user instead of guessing.
- **Sensitive data visible in the recording** (real names, amounts,
  credentials) → blur it for the full time it's on screen before review.
- **The workflow is too long for one video** → propose splitting by natural
  hand-off points into a short series rather than compressing the pace.
