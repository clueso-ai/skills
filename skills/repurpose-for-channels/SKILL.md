---
name: repurpose-for-channels
description: >-
  Turn one finished video into a channel kit — a captioned, resized social cut
  of the strongest 15–30 seconds, a looping GIF of the key interaction for
  newsletters and in-app embeds, and the embed-ready full version. Use when the
  user says "cut this for LinkedIn", "make a social version of this video",
  "turn this demo into a GIF for the newsletter", "repurpose this video for
  our channels", or "I need short cuts of this for socials and the changelog".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Repurpose for Channels

One finished video, three deliverables: a captioned, resized social cut built
around its strongest 15–30 seconds; a looping GIF of the single key interaction
for newsletters and in-app surfaces; and the embed-ready full version — a
channel kit from work that already exists.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The finished video** — ask the user: is it an existing Clueso project (name
   or link it), or a raw screen recording they'll upload? A raw recording goes
   into a project first; if it's genuinely unpolished, warn that a social cut of
   rough footage stays rough, and offer a quick cleanup as a follow-up.
2. **Target channels** — LinkedIn/X, in-app, newsletter, help center. This
   decides the social cut's aspect ratio (square or vertical for feeds,
   landscape for embeds) and whether captions must carry the video sound-off.
3. **The one takeaway** the social cut should land — a single sentence. If the
   user can't name it, propose one after watching and get agreement first;
   cutting without a thesis produces montage, not message.

Confirm the workspace, and always duplicate before cutting — the source project
is never modified.

## Workflow

### 1. Watch the whole thing first

Inspect rendered frames of each scene alongside the transcript. You're hunting
for two things: the **strongest 15–30 second narrative** (a self-contained arc —
a pain named, an action shown, a result visible — that pays off the takeaway
without needing anything before it), and the **money shot** — the single
interaction where the product visibly does its magic, ideally 3–6 seconds from
input to result. Note both with timestamps and tell the user what you picked and
why.

### 2. The social cut

Duplicate the project, then cut down to the chosen span:

- Trim to the arc — in at the moment of tension, out on the result. No throat
  clearing; the first two seconds decide whether anyone stops scrolling.
- Resize for the channel and recompose each surviving scene so the action area
  stays dominant in the new frame — a landscape screen recording naively
  squeezed into vertical is illegible.
- Captions on, always: feeds autoplay muted. Short lines, high contrast, never
  covering the UI region the moment is about.
- If the cut opens mid-explanation, patch just the first narration line into a
  standalone hook; leave the rest untouched.
- A closing beat with the product name or CTA — one card, one action.

### 3. The looping GIF

Isolate the money shot as a tight loop: start a beat before the interaction, end
a beat after the result, so the loop reads even when a viewer joins mid-cycle.
Keep it short — a good UI GIF is 3–6 seconds — and crop close so the interaction
is legible at newsletter width.

**Delivery caveat:** if a direct GIF file isn't available from the video
pipeline, deliver it via the docs/article route (capture the moment as a GIF
inside an article and hand over that embed) or as a short looping video, and say
plainly which form the user is getting. Never promise a .gif file before
confirming the route works.

### 4. The embed-ready full version

The lightest pass: export the full video at embed-friendly quality with captions
available, confirming the opening frame looks intentional as a static thumbnail
(if the video opens on a blank or mid-motion frame, note the best thumbnail
moment for the user).

No music or sound effects on any of the three — never add any.

### 5. Review the set, then export

Share review links for the social cut and the GIF moment together, framed as a
kit: what each piece is for, where each should be posted or embedded. The most
common revision is "use this other moment for the GIF" — that's a cheap swap, so
invite it. Export the full kit only after the nod.

## What good looks like

- The social cut makes sense with the sound off, from second one.
- The GIF loops so cleanly it feels engineered, and needs no caption to be
  understood.
- Nothing in the kit required new footage — that's the point.

## Watch out for

- **Cramming the full argument into 20 seconds** — the social cut earns a click,
  it doesn't close a deal. One takeaway, ruthlessly.
- **Caption collision** — vertical crops leave little safe area; check captions
  against every scene's action region, not just the first.
- **Editing the original** — every cut happens in a duplicate. If the source
  project changed, something went wrong; say so and restore.
