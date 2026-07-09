---
name: fix-pronunciations
description: >-
  Fix mispronounced product names, acronyms, and jargon in a video's
  voiceover by respelling them phonetically and regenerating only the
  affected lines. Use when the user says "it's pronouncing our product name
  wrong", "fix the pronunciation of X", "the voiceover says the acronym
  weirdly", "make it say KYOO-bee not cube", or points at specific words
  the narration gets wrong.
license: Apache-2.0
metadata:
  author: clueso
  category: quick-edits
  subcategory: narration
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Fix Pronunciations

Surgically fix the words a video's voiceover mispronounces — product names,
acronyms, technical terms — without touching anything else. Only the lines
containing those words get regenerated; the rest of the video stays exactly
as it was.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (name or link it),
   or a raw screen recording they'll upload? Branch accordingly.
2. **The words** — which terms are wrong, and how each should sound. If the
   user can only say "it sounds off", have them describe the correct
   pronunciation in plain syllables (e.g. "Clueso = CLUE-so, not
   clue-OH-so").

## Workflow

1. **Confirm the workspace** first.
2. **Find every occurrence.** Search the transcript for each problem word,
   including inflections and plurals — a fix that misses one instance is
   worse than no fix.
3. **Respell phonetically.** In the narration text only, replace each
   problem word with a spelling that forces the right sound: syllables and
   capitals for stress ("koo-BER-net-eez"), hyphens to break up acronyms
   ("S-S-O"), or a spaced-out letter run for initialisms. Test alternatives
   if the first respelling still reads ambiguously.
4. **Keep on-screen text untouched.** The phonetic respelling lives only in
   the spoken script — captions, titles, and overlays keep the real
   spelling.
5. **Regenerate only the affected lines.** Don't re-render the whole
   narration; touch just the clips whose text changed.
6. **Re-check alignment on those clips.** Regenerating a line retimes its
   clip slightly — confirm the visuals at each patched spot still line up
   with the words, and fix any drift at the seams.
7. **Listen back to every patched line**, then share a review link listing
   which words were fixed. Wait for the user's nod.
8. **Export** once approved.

## What good looks like

- The fixed words are indistinguishable in tone and pace from the lines
  around them — no audible "patch".
- Every instance of every problem word is corrected, everywhere it occurs.
