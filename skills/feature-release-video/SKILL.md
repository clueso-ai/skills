---
name: feature-release-video
description: >-
  Turn release notes or a changelog entry into a tiered feature announcement
  video — a 60-90s big-launch cut with an animated hook, demo, and CTA, or a
  20-30s quick-hit for minor releases — built around real demo footage of the
  feature. Use when the user says "make a feature announcement video", "we're
  shipping X, make a release video", "turn these release notes into a video",
  "changelog video", or "launch video for this new feature".
license: Apache-2.0
metadata:
  author: clueso
  category: video-creation
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Feature Release Video

Turn a changelog entry, release notes, or a PRD blurb into a polished feature
announcement video sized to the launch: a 60-90 second big-launch cut with an
animated hook, real demo footage, and a CTA — or a 20-30 second quick-hit for a
minor release. The demo footage is the star; the motion graphics frame it.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

Collect these before building. Ask for anything missing rather than inventing it:

1. **The release material** — release notes, changelog text, or a PRD blurb.
2. **Launch tier** — how big is this release?
   - **T1 (big launch):** 60-90s — animated hook, chaptered demo, CTA outro.
   - **T2 (notable):** 40-60s — short hook, demo, CTA.
   - **T3 (minor):** 20-30s — one-scene quick-hit: name it, show it, link it.
   If the user isn't sure, ask how they'd announce it (blog post + email = T1;
   changelog line = T3) and confirm your recommendation.
3. **A demo video of the feature — required.** Ask: is it an **existing Clueso
   project** (have them name or link it), or a **screen recording they'll
   upload**? Branch accordingly — reuse the project's footage in the first case,
   bring the uploaded recording in as demo clips in the second. If they have
   neither, screenshots of the feature are an acceptable fallback for T2/T3;
   for T1, push for real footage — a big launch deserves motion.
4. **CTA** — the one action a viewer should take (try it, read the docs, join
   the beta), with the link.
5. Optional: brand colors/logo (or "use workspace branding"), and whether they
   also want a **short looping cut** of the key interaction for the changelog
   or newsletter.

## Workflow

1. **Confirm the workspace** the video should live in before creating or
   editing anything.
2. **Check for an existing template** that matches a launch/announcement style
   and offer the best fits before building from scratch. If they pick one, its
   design leads; otherwise commit to a brand-derived palette up front.
3. **Script to the tier.** Write in the product's messaging voice — lift the
   verbs and framing from the release notes rather than paraphrasing them flat.
   - T1 arc: hook (the pain or the promise) → feature reveal by name → demo
     beats, one capability per beat → proof or "why it matters" line → CTA.
   - T3 arc: one breath — "You can now <do the thing>. Here's what it looks
     like." → CTA line. No hook scene, no outro card beyond the CTA.
   Estimate the spoken length and trim until it fits the tier's window. Show
   the user the script before composing — this is the cheapest moment to
   change direction.
4. **Build the hook (T1/T2).** An animated, on-brand motion scene that states
   the promise in a few words — kinetic text, a bold stat, or a stylized tease
   of the UI. Keep it under 8 seconds; the demo is the payoff, not the hook.
5. **Cut the demo scenes.** From the provided footage, keep only the moments
   where the new capability is visibly doing its job. Guide the eye at each
   beat: zoom into the control being used, call out the new element, dim what
   doesn't matter. A viewer who watches muted should still see exactly what's
   new and where it lives.
6. **CTA outro.** One scene, one action, stated once — on-brand card with the
   link. For T3, the CTA can be a closing line over the final demo frame
   instead of its own scene.
7. **Narrate and sync.** Confident, energetic but not breathless. Each demo
   beat's visuals should land as the narration names them. No music, no sound
   effects — the voice and the product carry it.
8. **Review before export.** Share the review link and walk the user through
   the cut (hook, demo beats, CTA). Apply their notes, then export.
9. **The changelog cut (if requested).** After the main export, pull the single
   best interaction as a short silent looping cut sized for an embed. If a GIF
   file specifically is needed and isn't available as a direct output, deliver
   a short looping video instead and say so.

## What good looks like

- The new capability is on screen within the first 15 seconds (T1) or
  immediately (T3).
- Every second of demo footage shows the *new* thing — no logging in, no
  navigating menus the viewer already knows.
- One CTA, stated once. Two CTAs is zero CTAs.
- The tier discipline holds: a T3 that balloons to 60 seconds trains the
  audience to skip release videos.

## Fallbacks

- **Footage shows unfinished UI or placeholder data** → flag it to the user
  before building around it; offer to blur or crop rather than ship it.
- **Release notes are a dry bullet list** → ask one question — "what can a
  user do today that they couldn't yesterday?" — and script around the answer.
- **Screenshots only (T2/T3)** → compose them as animated still scenes with
  movement and callouts so the video never feels like a slideshow.
