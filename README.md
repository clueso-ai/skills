# Clueso Video Skills

Agent Skills for creating and editing videos with [Clueso](https://clueso.io), built to
run on **the Clueso MCP and nothing else** — no external APIs, no local binaries, no
API keys. Install one, connect the Clueso MCP, and your agent can produce finished,
exported videos.

## Skills

All 55 skills require the Clueso MCP and nothing else.

### Motion graphics

| Skill | What it does |
|---|---|
| [brief-to-launch-video](skills/brief-to-launch-video) | Product brief → 30-60s launch-style motion-graphics video |
| [kinetic-text-video](skills/kinetic-text-video) | Announcement, stat, or quote → kinetic-typography video |
| [animated-explainer-video](skills/animated-explainer-video) | Problem → solution 60-90s animated explainer |
| [science-style-animation](skills/science-style-animation) | Concept or process → educational animation with labeled diagrams |
| [stats-infographic-video](skills/stats-infographic-video) | Numbers → animated data story with counters and payoff scene |
| [ui-concept-animation](skills/ui-concept-animation) | UI screenshot/mockup → animated interaction teaser |
| [branded-intro-outro](skills/branded-intro-outro) | Logo + tagline → matched intro/outro stinger pair |

### Create videos

| Skill | What it does |
|---|---|
| [article-to-video](skills/article-to-video) | Help article / blog post / changelog → narrated explainer video |
| [screenshots-to-walkthrough](skills/screenshots-to-walkthrough) | Ordered UI screenshots → narrated cursor-walkthrough video |
| [feature-release-video](skills/feature-release-video) | Release notes + demo footage → tiered feature announcement video |
| [course-module-video](skills/course-module-video) | Lesson outline → LMS-ready course module with objectives and recaps |
| [academy-course-trailer](skills/academy-course-trailer) | Course syllabus → 30-45s enrollment-driving trailer |
| [software-training-video](skills/software-training-video) | Steps list or rough recording → internal tool/process training video |
| [sop-video-and-doc](skills/sop-video-and-doc) | One procedure → SOP walkthrough video + step-by-step written SOP |
| [sales-pitch-training](skills/sales-pitch-training) | Talking points → pitch/objection-handling training video |
| [soft-skills-scenario-video](skills/soft-skills-scenario-video) | Behavioral topic → animated scenario story with takeaways |
| [slides-to-video](skills/slides-to-video) | Slide deck → narrated video that doesn't feel like a deck |
| [demo-for-every-persona](skills/demo-for-every-persona) | One master demo → persona-targeted variants |

### Edit videos

| Skill | What it does |
|---|---|
| [polish-screen-demo](skills/polish-screen-demo) | Raw screen recording → polished, narrated product demo |
| [rebrand-video-library](skills/rebrand-video-library) | Apply a new brand (colors, fonts, logo) across an existing video |
| [refresh-outdated-video](skills/refresh-outdated-video) | Surgically replace stale sections and narration lines |
| [revoice-video](skills/revoice-video) | Rewrite the tone, pick a better voice, regenerate narration |
| [localize-video](skills/localize-video) | Produce native-voice language variants of a finished video |
| [repurpose-for-channels](skills/repurpose-for-channels) | One video → social cut + GIF + embed-ready versions |

### Quick edits

| Skill | What it does |
|---|---|
| [add-zoom-emphasis](skills/add-zoom-emphasis) | Zoom into the key actions at the right moments |
| [add-callouts-and-arrows](skills/add-callouts-and-arrows) | Annotate the buttons/fields the narration mentions |
| [spotlight-key-areas](skills/spotlight-key-areas) | Dim everything except the active area per step |
| [blur-sensitive-info](skills/blur-sensitive-info) | Find and blur PII, credentials, and internal data |
| [highlight-cursor-actions](skills/highlight-cursor-actions) | Make every click legible with cursor emphasis |
| [add-key-point-overlays](skills/add-key-point-overlays) | Surface each section's takeaway as on-screen text |
| [add-lower-thirds](skills/add-lower-thirds) | Branded lower-third labels per segment |
| [add-animated-captions](skills/add-animated-captions) | Burned-in captions for sound-off viewing |
| [accessibility-pass](skills/accessibility-pass) | Captions, readable text, followable pacing |
| [remove-filler-words](skills/remove-filler-words) | Strip ums, false starts, and rambling from the narration |
| [tighten-narration](skills/tighten-narration) | Cut the script to hit a target length |
| [fix-pronunciations](skills/fix-pronunciations) | Fix mispronounced names in the voiceover |
| [swap-voice](skills/swap-voice) | Change the narration voice, script untouched |
| [add-opening-hook](skills/add-opening-hook) | Replace a cold open with a 5-second payoff-first hook |
| [trim-dead-air](skills/trim-dead-air) | Remove silences, loading screens, and hesitation gaps |
| [chapterize-video](skills/chapterize-video) | Split a long video into titled chapters |
| [reorder-scenes](skills/reorder-scenes) | Restructure the narrative order and smooth the seams |
| [stitch-videos](skills/stitch-videos) | Combine multiple videos into one coherent piece |
| [split-into-series](skills/split-into-series) | Cut one long video into standalone shorts |
| [shorten-to-length](skills/shorten-to-length) | Get a video down to a hard time limit |
| [speed-up-repetitive-parts](skills/speed-up-repetitive-parts) | Compress the boring stretches honestly |
| [apply-brand-colors](skills/apply-brand-colors) | Recolor every overlay and background to the brand palette |
| [add-logo-watermark](skills/add-logo-watermark) | Persistent, unobtrusive corner logo |
| [add-cta-end-card](skills/add-cta-end-card) | Append a branded end card with the next action |
| [smooth-transitions-pass](skills/smooth-transitions-pass) | Consistent, subtle transitions at every boundary |
| [make-vertical-cut](skills/make-vertical-cut) | Reframe a landscape video for 9:16 with captions |
| [extract-gif-moment](skills/extract-gif-moment) | Pull the best interaction as a looping GIF |

### Docs & articles

| Skill | What it does |
|---|---|
| [video-to-help-article](skills/video-to-help-article) | Video project → publish-ready help article with annotated screenshots |
| [refresh-article-screenshots](skills/refresh-article-screenshots) | Replace outdated screenshots at the same steps |
| [annotate-article-screenshots](skills/annotate-article-screenshots) | Zoom, crop, blur, and arrow every screenshot |
| [restructure-help-article](skills/restructure-help-article) | Rework an article for scanability and self-serve deflection |

## Installation

### Any agent (skills CLI)

```bash
npx skills add clueso-ai/skills
```

Or a single skill:

```bash
npx skills add clueso-ai/skills --skill brief-to-launch-video
```

### Claude Code (plugin marketplace)

```
/plugin marketplace add clueso-ai/skills
/plugin install clueso-video-skills@clueso-video-skills
```

### Prerequisite: the Clueso MCP

Every skill here drives the [Clueso MCP](https://clueso.io). Connect it in your agent
(e.g. via claude.ai connectors or your agent's MCP configuration) before running a
skill. No other dependency is needed — that's the point.

## What's an Agent Skill?

A skill is a folder with a `SKILL.md` file: instructions an agent loads on demand to
perform a specialized task. See the [Agent Skills spec](spec/SKILL_SPEC.md) for the
format these skills follow, and [`template/`](template) for a starter skill.

## Repository structure

```
skills/          One folder per skill (SKILL.md + optional references/)
spec/            The frontmatter + authoring spec skills in this repo follow
template/        Starter template for new skills
scripts/         CI validation
```

## Contributing

1. Copy `template/SKILL.template.md` to `skills/<your-skill-name>/SKILL.md`.
2. Follow [spec/SKILL_SPEC.md](spec/SKILL_SPEC.md) — in particular the dependency
   rule: a skill must declare everything it needs in `metadata.requires` /
   `metadata.external-apis`, and Clueso-MCP-only skills are strongly preferred.
3. Open a PR. CI validates frontmatter, naming, and repo hygiene (no `.venv`, `.env`,
   binaries, or oversized files).

## License

[Apache 2.0](LICENSE)
