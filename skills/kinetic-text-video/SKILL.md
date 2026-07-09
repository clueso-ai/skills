---
name: kinetic-text-video
description: >-
  Turn a short message — an announcement, a stat, a quote, a manifesto line —
  into a 20-40 second kinetic-typography video where animated words are the
  only actor on screen. Use when the user says "kinetic text video", "animated
  text video", "typography video", "make this quote/stat into a video", "text
  animation for this announcement", or gives you a few lines of copy and wants
  them turned into motion.
license: Apache-2.0
metadata:
  author: clueso
  category: video-creation
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Kinetic Text Video

Make a pure kinetic-typography video: no footage, no illustrations — just words
on brand-colored backgrounds, revealed with rhythm and intent. Best for
announcements, bold stats, quotes, and manifesto-style messages of 20-40 seconds.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

Ask for anything missing rather than inventing it:

1. **The message** — the announcement, stat, or quote (required). Raw copy is fine;
   distilling it is your job.
2. **Length** — default 20-40 seconds.
3. **Brand** — colors and fonts, or "use workspace branding".
4. **Narrated or silent** — with a voiceover reading the words, or text-only.

## Workflow

### 1. Set up

Confirm the target workspace with the user before creating anything. Then look for
an existing template that fits a kinetic-text style; if there's a strong match,
show it and ask whether to build from it before starting from scratch.

### 2. Distill the copy into beats

Cut the message down to **5-8 beats, one idea per beat, one beat per scene**.
Each beat is a short punchy line — 3-8 words is the sweet spot. If a sentence
carries two ideas, split it; if two sentences say one thing, merge them. The last
beat is the landing line (the CTA, the stat, or the quote attribution).

Show the user the beat list before building. This is the cheapest moment to
change direction.

### 3. Commit to one type treatment

Pick **one** reveal style for the whole piece — scale pops, masked reveals,
typewriter, or word-by-word slides — and keep it consistent from first scene to
last. Variation comes from rhythm and emphasis, not from switching techniques:

- Reserve the biggest scale and the boldest weight for the one or two words that
  carry the message. Everything else stays quieter.
- Alternate scene energy: a fast multi-word scene, then a single held word.
  Monotone pacing is the most common failure of this format.
- Backgrounds are flat brand colors; you may flip between two brand colors across
  scenes for contrast, but never introduce off-palette colors or imagery.
- One typeface family throughout. Use weight and size for hierarchy, not new fonts.

### 4. Time the scenes to the words

If narrated, write the narration first (usually the beats themselves, read
naturally) and **estimate its spoken length before laying out any scene** — scene
durations come from the narration, never the other way around. Each word or line
should appear as it is spoken, hold while relevant, then exit before the next beat.

If silent, time by reading speed: give viewers roughly 0.4 seconds per word plus
a half-second of hold per scene. Err slower on the landing line.

Never let a frame sit fully static for more than a beat — a line entering, a line
exiting, or a slow drift should always be in motion.

### 5. Build

Create the project and build one scene per beat with text on brand backgrounds,
using the committed treatment and timings. If narrated, generate the voiceover in
a voice that matches the copy's register (bold copy wants a confident read, a
quote wants a warmer one) and align every reveal to the spoken word.

### 6. Review, then export

Check every scene: text legible at video scale, inside safe margins, palette
consistent, reveals landing on their words, total length inside the target.
Share the review link with the user and get their nod **before** exporting.
Then export and hand over the final link.

## What to avoid

- Walls of text. If a scene needs more than two short lines, it is two scenes.
- Mixed reveal styles — the piece must feel like one voice, not a demo reel.
- Music or sound effects — never add them.
- Decorating with stock imagery or generated visuals; in this format, the
  typography IS the visual. If the message truly needs pictures, suggest an
  animated explainer instead.
