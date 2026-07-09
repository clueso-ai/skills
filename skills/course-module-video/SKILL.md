---
name: course-module-video
description: >-
  Turn a lesson outline or SME notes into an LMS-ready course module video with
  learning objectives up front, a chaptered demo mapped one-to-one to those
  objectives, mini-recaps, and a final recap with a knowledge-check prompt.
  Use when the user says "make a course module", "turn this lesson outline
  into a video", "LMS video for this topic", "academy lesson video", or
  "training module video for our customers".
license: Apache-2.0
metadata:
  author: clueso
  category: video-creation
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Course Module Video

Turn a lesson topic, outline, or SME notes into an LMS-ready course module
built on instructional-design structure: objectives stated up front, a
chaptered demo where every chapter maps to exactly one objective, a mini-recap
after each chapter, and a final recap with a knowledge-check prompt the LMS can
pick up. Calm, instructional narration throughout.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

Collect these before building. Ask for anything missing rather than inventing it:

1. **Lesson topic and learning objectives.** If the user has an outline but no
   explicit objectives, derive 2-4 and confirm them — each phrased as
   something the learner can *do* afterward ("configure X", "run a Y report"),
   not something they'll "understand".
2. **Module material** — an outline, SME notes, or an existing doc.
3. **Demo material.** If the module demonstrates software (most do), ask: is
   the demo an **existing Clueso project** (name or link it), or a **screen
   recording they'll upload**? Branch accordingly. Screenshots work as a
   fallback for short modules.
4. **Audience** — who's learning, and what they already know. This sets the
   pace and how much you explain vs. assume.
5. **Length target** — default 3-6 minutes. Longer than ~8 minutes, suggest
   splitting into two modules; completion rates fall off a cliff.

## Workflow

1. **Confirm the workspace** before creating or editing anything.
2. **Check for an existing template** matching a course/lesson style and offer
   the best fits before building from scratch.
3. **Map objectives to chapters.** One chapter per objective, in the order a
   learner needs them. If an outline section doesn't serve an objective, cut
   it or move it to "further reading" — this is the core discipline of the
   skill. Show the user the objective→chapter map before building.
4. **Open with the objectives.** A short branded scene: "By the end of this
   module, you'll be able to…" with each objective appearing as it's spoken.
   15-20 seconds, no throat-clearing about the company or the course.
5. **Build each chapter.**
   - Open on a chapter title card with the chapter number and the objective it
     serves — visible structure helps learners place themselves.
   - Demo the skill from the provided material, trimmed to just the steps that
     matter. Guide attention on every step: zoom to the control in play, call
     out the field being filled, keep the cursor easy to follow.
   - Narrate like a patient teacher: name the action, do the action, state the
     result. Present tense, second person, one idea per sentence.
   - Close with a 5-10 second **mini-recap**: the chapter's takeaway restated
     in one line over a simple card.
6. **Final recap and knowledge check.** Restate all objectives as "you can
   now…" lines, then end on a knowledge-check prompt scene — one question per
   objective, phrased for the LMS quiz that follows ("Which menu holds X?").
   The video poses the question; the LMS grades it.
7. **Narrate and sync.** One calm instructional voice for the whole module.
   Unhurried pacing — a learner following along in a second window must be
   able to keep up. No music, no sound effects.
8. **Review before export.** Share the review link, flagging the
   objective→chapter map for the user to verify. Apply notes, then export.

## What good looks like

- A learner can state what they'll be able to do within the first 20 seconds.
- Every chapter earns its place by serving exactly one stated objective.
- Chapter markers make the video scannable on rewatch — learners come back to
  chapter 3, not minute 4:12.
- The recap contains nothing new. If a point matters, it lives in a chapter.

## Fallbacks

- **SME notes are a brain dump** → draft the objectives yourself, get them
  confirmed, then keep only the notes that serve them.
- **Demo recording covers more than this module** → use only the relevant
  stretch; suggest the rest seed the next module.
- **No demo material for a hands-on objective** → ask for a recording; a
  hands-on skill taught with static slides doesn't transfer. Screenshots with
  step callouts are the floor, not the goal.
- **Too many objectives for the length target** → propose splitting the module
  rather than rushing the pace.
