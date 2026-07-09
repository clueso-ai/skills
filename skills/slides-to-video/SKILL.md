---
name: slides-to-video
description: >-
  Turn an uploaded slide deck (PPT) into a narrated video that doesn't feel
  like a deck: slide text rewritten into spoken narration instead of read
  aloud, slides that don't earn screen time cut or merged, motion added to
  the slides that matter, and clean transitions at section boundaries. Use
  when the user says "turn this deck into a video", "convert my PowerPoint to
  video", "narrate these slides", "make a video from this presentation", or
  uploads a deck and wants a video version.
license: Apache-2.0
metadata:
  author: clueso
  category: video-creation
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Slides to Video

Convert a slide deck into a narrated video that watches like a video, not like a deck
on autoplay. The craft is threefold: narration written for the ear instead of read off
the slide, an honest edit that cuts slides that don't earn screen time, and motion that
directs attention on the slides that matter. Built for enablement and L&D teams whose
content lives in decks but whose audience won't sit through one.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

Collect these before building. Ask for anything missing rather than inventing it:

1. **The deck** — a PPT file the user uploads.
2. **Narration notes** — per-slide speaker notes if they exist, or "write it for me."
   If the deck has speaker notes, use them as the narration's raw material; they're
   usually closer to spoken language than the slide text is.
3. **Target length** — and hold to it. A 40-slide deck does not become a 40-slide
   video; expect to propose cuts.
4. **Which slides matter most** — the 3-5 slides that carry the argument. These get
   the motion budget.
5. Optional: voice preference, the audience and purpose (training, pitch, briefing) —
   this sets the narration's register.

## Workflow

### 1. Confirm the workspace and check for a fitting template

Confirm with the user that the active workspace is the intended one. Then look for an
existing template that fits a presentation-to-video style; if there's a strong match,
offer it before building from scratch.

### 2. Import and audit the deck

Bring the deck in so each slide becomes a scene. Then audit every slide against one
question: **does this earn screen time in a video?**

- **Cut**: agenda slides, dividers with no content, thank-you slides, legal boilerplate
  (offer to fold anything essential into narration), slides that repeat the previous
  point.
- **Merge**: consecutive slides making one point — keep the strongest visual, let
  narration carry the rest.
- **Keep**: slides with a visual that words can't replace — the diagram, the chart,
  the screenshot, the one-line claim.

Present the proposed cut list to the user as slide numbers with a one-line reason each,
and get agreement before proceeding. This edit is where deck-videos are won or lost —
a 30-slide deck often makes a better video as 12 scenes.

### 3. Rewrite the text into narration

The cardinal sin of deck-videos is narration that reads the slide. The viewer can read;
narration must add what the slide doesn't say. For each kept slide:

- Write spoken language: contractions, short sentences, direct address ("you'll see").
- Say **why the slide matters**, not what it says. If the slide reads "Revenue up 40%",
  the narration is "That bet paid off — revenue grew forty percent in two quarters",
  never "Revenue increased by 40%."
- Bridge between slides so sections flow as one argument instead of a sequence of
  disconnected pages.
- Estimate the spoken duration of the full script against the target length; cut words
  (or more slides) rather than letting the pace rush.

Show the user the narration script alongside the slide list before generating audio.

### 4. Add motion where it pays

Motion is a budget — spend it on the slides the user flagged as mattering most:

- **Builds**: reveal bullet-style content line by line as the narration reaches each
  point, so the viewer never reads ahead of the voice.
- **Emphasis**: on dense slides (charts, diagrams, tables), zoom or highlight the
  region being discussed at the moment it's discussed.
- **Section transitions**: a clean transition at each section boundary so the video's
  chapters are felt; simple cuts within sections.

Ordinary slides get at most a subtle entrance. A video where everything moves is as
flat as one where nothing does.

### 5. Narrate and sync

Choose a voice that fits the purpose — measured for training, warmer and more
energetic for a pitch. Generate the narration and let each scene's duration follow its
spoken length; sync builds and emphasis moments to the exact lines that call for them.

### 6. Review, then export

Share a review link and ask the user to check: does it flow as a video, are the cuts
right, does any slide linger after its narration ends? Apply changes, get their nod,
then export and hand back the final link.

## What good looks like

- Nobody could reconstruct the slide text from the narration — the two complement,
  never duplicate.
- No scene outstays its narration; the pace never waits for the voice to catch up.
- A viewer who never saw the deck follows the argument completely.
- Sections are felt: transitions mark them, and the narration bridges them.

## Avoid

- Reading the slide. If narration and slide text ever match word for word, rewrite one.
- Keeping slides out of politeness. Screen time is earned, and the review step is
  where the user protects anything you cut wrongly.
- Uniform scene lengths — a title beat needs three seconds, a diagram may need twenty.
- Music or sound effects — pacing and narration do that work.
