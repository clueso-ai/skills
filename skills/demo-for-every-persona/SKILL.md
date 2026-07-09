---
name: demo-for-every-persona
description: >-
  Turn one master product demo into N persona-targeted variants: duplicate
  the demo per persona, re-script the narration around each persona's pains
  and outcomes, reorder and trim so every variant leads with what that
  audience cares about, and close with a persona-specific CTA. Use when the
  user says "make a version of this demo for each persona", "tailor this
  demo for admins vs execs", "persona variants of my demo video", or "one
  demo, different audiences".
license: Apache-2.0
metadata:
  author: clueso
  category: video-creation
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Demo for Every Persona

One master demo, N audiences. This skill produces a tailored variant of a product demo
for each persona — same underlying footage, but each variant re-scripted around that
persona's pains, reordered to lead with what they care about, trimmed of what they
don't, and closed with their CTA. An exec buyer should never sit through the admin
setup walkthrough; an admin should never get the ROI pitch first. Built for product
marketing and digital CS teams who need coverage without recording N demos.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

Collect these before building. Ask for anything missing rather than inventing it:

1. **The master demo.** First ask: is it an existing Clueso project (have the user
   name or link it), or a raw screen recording they'll upload? Branch accordingly —
   open the existing project, or take the upload in as a new project.
2. **The persona list** — e.g. admin / end-user / exec buyer. Two to five personas is
   the sweet spot; beyond that, ask which ones actually get distributed.
3. **One line per persona on what they care about** — their pain, their success
   metric, the question they bring to a demo. If the user can't supply this, draft it
   from the product context and confirm before scripting; this line steers everything.
4. **Per-persona CTA**, if different — trial signup for end-users, "talk to sales" for
   exec buyers, setup docs for admins. Default: one shared CTA, re-worded per persona.

## Workflow

### 1. Confirm the workspace

Confirm with the user that the active workspace is the intended one before creating or
duplicating anything. N variants means N projects — the right workspace matters twice
as much here.

### 2. Map the master demo

Watch the master end to end and build a section map: what each segment shows, what
value it demonstrates, and how long it runs. Then score each section per persona —
lead / keep / trim / cut. Share this map as a simple table (sections down the side,
personas across the top) and get the user's agreement before touching anything. This
table is the whole strategy; the rest is execution.

### 3. Produce each variant

For each persona, duplicate the master into its own clearly named project (e.g.
"Acme demo — Exec buyer") so the master stays untouched, then:

- **Reorder** so the variant leads with that persona's highest-scoring section. The
  first 15 seconds must show the thing this persona came to see — never make them
  wait through someone else's priorities.
- **Trim or cut** the sections marked irrelevant for them. Shorter and pointed beats
  longer and complete: a tight 90-second exec cut outperforms the full 5-minute tour.
- **Re-script the narration** in that persona's language — their vocabulary, their
  pains, their success metric. The screen may show the same feature in two variants
  while the voice tells two different stories: to the admin, "provision your whole
  team in one screen"; to the exec, "your team is productive on day one, no IT
  project required." Smooth the seams where sections were reordered so narration
  still flows as one argument.
- **Persona intro line** — open by naming the viewer's world in the first sentence
  ("If you manage the rollout…"), so they know within seconds this video is for them.
- **Persona CTA** — close each variant with its own next step, framed as the natural
  consequence of what they just saw.

Regenerate the narration per variant and let timing follow the new script; re-align
visuals wherever reordering or trimming moved the action.

### 4. Review every variant, then export

Share a review link for each variant — not just the first one — with a one-line
summary of what changed versus the master (lead section, cuts, CTA). Ask the user to
spot-check that each variant's opening and CTA actually fit its persona. Apply edits,
get their sign-off, then export all variants and hand back a link per persona.

## What good looks like

- Each variant's first 15 seconds would survive that persona's attention span.
- Variants differ in order, length, and language — not just an intro slapped on the
  front of an identical video. If two variants are 90% the same cut, the persona map
  wasn't sharp enough; go back to step 2.
- The master demo remains untouched and reusable.
- Narration seams are inaudible: nobody can tell the sections were rearranged.

## Avoid

- The "intro-swap" shortcut — a persona variant is a re-argued video, not a re-badged
  one.
- Feature vocabulary for outcome audiences. Exec variants talk results and risk;
  keep the how for admin and end-user cuts.
- Letting variants sprawl. Every persona cut should be shorter than the master.
- Music or sound effects in any variant.
