---
name: animated-explainer-video
description: >-
  Create a classic 60-90 second animated explainer video — hook, problem,
  solution, how-it-works, CTA — from generated animations, on-screen text, and
  warm narration. Use when the user says "make an explainer video", "animated
  explainer for X", "explain our product in a video", "60-second explainer",
  "problem-solution video", or describes a product, feature, or concept they
  want explained to an audience in an engaging animated format.
license: Apache-2.0
metadata:
  author: clueso
  category: motion-graphics
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Animated Explainer Video

Produce the classic 60-90 second explainer: a narrated story that takes a viewer
from "here's a pain you recognize" to "here's the thing that fixes it and how it
works", told through generated animated scenes in one consistent visual style.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

Ask for anything missing rather than inventing it:

1. **What's being explained** — product, feature, or concept.
2. **Audience** — who is watching and what they already know.
3. **The pain and the promise** — the problem it solves and the outcome it delivers.
4. **CTA** — the one action the viewer should take at the end.
5. **Length** — default 60-90 seconds.
6. **Voice preference** and brand colors/fonts (or "use workspace branding").

## Workflow

### 1. Set up

Confirm the target workspace with the user. Look for an existing explainer-style
template that fits; if there's a strong match, offer it before building from
scratch.

### 2. Script first, always

Write the narration script as a five-part arc before touching any visuals:

| Beat | Job | Share of runtime |
|---|---|---|
| Hook | Name the pain in the audience's words | ~10% |
| Problem | Make the cost of the pain concrete | ~15% |
| Solution | Introduce the product/concept as the turn | ~15% |
| How it works | 2-3 steps or capabilities, one at a time | ~45% |
| CTA | Restate the promise, one clear action | ~15% |

Conversational register, second person, no feature-list monotone. **Estimate the
spoken length of the script before laying out any scenes** — if it overshoots the
target, cut words, never speed the voice. Show the user the script and get a nod;
rewriting a script is cheap, rebuilding scenes is not.

### 3. Storyboard: one scene per script beat

Map each script line (or pair of lines) to exactly one scene — typically **7-10
scenes** for 60-90 seconds. Each scene makes **one point**; if a scene needs to say
two things, split it. For every scene write a one-line visual description of what
the animation shows: the metaphor for the problem, the product as the reveal, one
diagrammed step per how-it-works beat, a clean branded card for the CTA.

### 4. One visual style, carried through

Before generating anything, commit to a single style recipe — palette (brand
colors at video intensity), one typeface, illustration flavor (flat geometric,
line-art, soft gradient — pick one), and motion character (snappy vs. floaty) —
and describe that same recipe in every scene you generate. The most common
explainer failure is scenes that look like they came from different videos.

Generate an illustrative animation for each storyboard scene, paced so its motion
fits inside that scene's narration line. Keep on-screen text minimal — a short
keyword or label per scene, never the narration transcribed.

### 5. Narrate and sync

Generate the voiceover in a warm, confident voice (honor the user's preference).
Let every scene's duration follow its narration line, and time each scene's key
motion — the reveal, the step appearing, the state change — to land exactly when
the narration mentions it. Nothing on screen should reference something not yet
spoken.

### 6. Brand pass

Sweep every scene: colors traceable to the brand palette, consistent typography,
logo present in the closing CTA scene. The outro should hold long enough to read
the CTA comfortably.

### 7. Review, then export

Watch it end to end for style drift, orphaned motion (animation that outlives its
narration), and pacing dead spots. Share the review link with the user and get
their approval **before** exporting. Then export and deliver the final link.

## What to avoid

- Music or sound effects — never add them.
- Scenes that carry two ideas, or narration that races to fit an overstuffed script.
- Faking the user's real product UI with invented mockups — if the how-it-works
  beats need real UI, ask for screenshots and build around them.
- On-screen paragraphs. The voice explains; the screen shows.
