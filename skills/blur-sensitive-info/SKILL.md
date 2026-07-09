---
name: blur-sensitive-info
description: >-
  Sweep an existing video for sensitive information — emails, names, API keys,
  customer data, internal URLs, amounts — and blur every instance for the full
  time it's on screen. Use when the user says "blur the sensitive info", "hide
  the customer data", "redact the emails", "there's PII in my recording",
  "mask the API keys", or "make this recording safe to share".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Blur Sensitive Info

Make a recording safe to publish: find every piece of sensitive information on
screen and keep it blurred for every frame it's visible. One leaked email in
one frame defeats the whole pass, so this skill is thorough by design.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (have them name or link
   it), or a raw screen recording they'll upload? Branch accordingly.
2. **What counts as sensitive** — defaults: email addresses, personal and
   customer names, tokens/API keys/passwords, monetary amounts, internal URLs
   and hostnames. Ask if the user wants to add or drop categories.

Confirm the target workspace before editing anything.

## Workflow

### 1. Sweep the whole video

Inspect rendered frames at regular intervals across the entire video — not just
where you expect trouble. Sensitive data hides in browser tabs and address
bars, account menus, notification pop-ups, table rows scrolling past, and
sidebars, not only in the main content. Use the narration transcript as a
second net: if the voice mentions a customer or an account, check those frames
extra carefully. Build a list: what, where on screen, and the full time window
it's visible.

### 2. Place the blurs

For each finding, add a blur covering its coordinates for its **entire
visibility window** — from the first frame it appears to the last, not just
while it's discussed. Size each blur with margin beyond the text's edges, and
make it strong enough that the content can't be squinted back into legibility.

If the content **moves or scrolls** during its window, check frames across the
window: split it into segments and reposition the blur per segment (or widen it
to cover the travel path) so the data never slips out from under the blur
mid-scroll.

### 3. Verify frame by frame

Re-inspect rendered frames across each blur's window — start, middle, end, and
during any scrolling. Is the data fully covered at every point? Then re-sweep
the untouched stretches once more for anything missed on the first pass. Adjust
until nothing sensitive is readable anywhere. When in doubt, over-cover.

### 4. Review, then export

Share the review link, tell the user what was blurred and where, and ask them
to confirm nothing was missed — they know their data better than the frames do.
Export only after their nod.
