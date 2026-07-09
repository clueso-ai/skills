---
name: localize-video
description: >-
  Produce language variants of a finished video — for each target language,
  duplicate the project, translate the script idiomatically (glossary
  respected), narrate with a native-sounding voice, re-time the visuals, and
  localize on-screen text. Use when the user says "translate this video to
  Japanese", "we need this in German and French", "localize this video for our
  EU rollout", "make a Spanish version of this tutorial", or "dub this video
  in another language".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Localize Video

Turn one finished video into native-feeling language variants: per language, a
duplicated project with an idiomatic (never word-for-word) translation, a
native-sounding voice, visuals re-timed to the new narration length, and
on-screen text localized — while product names and UI labels stay exactly as the
glossary says.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask the user: is it an existing Clueso project (name or link
   it), or a raw screen recording they'll upload? A raw recording goes into a
   project first; its spoken audio becomes the source script.
2. **Target language(s)** — and, where it matters, the locale ("French or
   Canadian French?", "Brazilian or European Portuguese?").
3. **Glossary** — do-not-translate terms: the product name, feature names, UI
   labels as they appear in the product's localized (or non-localized) interface.
   If the user has none, propose one from the video's own vocabulary — every
   button and menu name the narration mentions — and get it confirmed. This
   single input prevents the worst localization bugs.

Confirm the workspace before creating anything.

## Workflow — once per language

Work one language at a time, completing each fully.

### 1. Duplicate first

Duplicate the source project and name the copy clearly (e.g. "Getting Started —
DE"). The original is never edited; it's the master every variant descends from.

### 2. Know the video before translating it

Inspect rendered frames of each scene with the transcript. Note where narration
is synced to on-screen action, which on-screen text elements exist (titles,
captions, callouts), and — critically — which words on screen are part of the
recorded product UI versus text elements laid on top. Only the latter can be
localized; the former can only be handled by the narration.

### 3. Translate for a native ear

Rewrite — don't transliterate — the script into the target language:

- Idiomatic phrasing over literal fidelity: translate what the sentence *does*,
  not its word order. A line that sounds like a translation has failed.
- Glossary terms appear verbatim, every time, correctly inflected around but
  never inside.
- If the product UI is not localized, the narration should name UI elements in
  the UI's language, glossed natively — the pattern is "Klicken Sie auf
  'Export'", not a translated button name the viewer will never find on screen.
- Expect expansion: German or French runs 20–30% longer than English. Where a
  translated line balloons, tighten the translation rather than letting the
  scene drag — same meaning, fewer words.

### 4. A voice that belongs to the language

Choose a native-sounding voice in the target language, matched to the original's
character (calm instructional stays calm instructional). Generate the narration,
listening for mangled glossary terms — English product names inside foreign
sentences are the most common defect; respell them phonetically in the narration
text if needed until they sound right.

### 5. Re-time and localize the canvas

Re-time each scene to its new narration length and re-anchor zooms, callouts,
and highlights to the translated action words. Then localize on-screen text
elements: titles, captions, lower-thirds, end-card CTAs — leaving glossary terms
and any UI-mirroring labels untouched. Check text fit after translation: longer
strings must not overflow their shapes; shrink type a step or rephrase shorter,
never let text clip. Verify by inspecting frames at every sync point and every
edited text element.

No music or sound effects — never add any.

### 6. Review, then export

Share the review link. If the user has a native speaker, ask for their pass on
this variant specifically — flag the two or three lines where you made a
judgment call. After the nod, export, then move to the next language.

## Deliverable

One exported video per language, consistently named, plus a per-language note of
glossary decisions and any UI-language caveats — so the next localization run
starts from answers, not questions.

## Watch out for

- **Half-localized screens** — translated caption over an English UI is fine
  when the narration handles it (step 3); a translated *UI label* over an
  English UI is a bug.
- **Cumulative drift** — re-timing scene by scene can slowly desync later
  scenes. After the last scene, spot-check sync at the start, middle, and end.
- **Locale assumptions** — dates, decimal separators, and formal/informal
  address (du/Sie, tu/vous) must match the audience; ask rather than default.
