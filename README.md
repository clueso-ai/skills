# Clueso Video Skills

Agent Skills for creating and editing videos with [Clueso](https://clueso.io), built to
run on **the Clueso MCP and nothing else** — no external APIs, no local binaries, no
API keys. Install one, connect the Clueso MCP, and your agent can produce finished,
exported videos.

## Skills

| Skill | What it does | Requires |
|---|---|---|
| [brief-to-launch-video](skills/brief-to-launch-video) | Product brief → 30-60s launch-style motion-graphics video | Clueso MCP only |
| [article-to-video](skills/article-to-video) | Help article / blog post / changelog → narrated explainer video | Clueso MCP only |
| [polish-screen-demo](skills/polish-screen-demo) | Raw screen recording → polished, narrated product demo | Clueso MCP only |

## Installation

### Any agent (skills CLI)

```bash
npx skills add desklamp-developers/skills
```

Or a single skill:

```bash
npx skills add desklamp-developers/skills --skill brief-to-launch-video
```

### Claude Code (plugin marketplace)

```
/plugin marketplace add desklamp-developers/skills
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

1. Copy `template/` to `skills/<your-skill-name>/`.
2. Follow [spec/SKILL_SPEC.md](spec/SKILL_SPEC.md) — in particular the dependency
   rule: a skill must declare everything it needs in `metadata.requires` /
   `metadata.external-apis`, and Clueso-MCP-only skills are strongly preferred.
3. Open a PR. CI validates frontmatter, naming, and repo hygiene (no `.venv`, `.env`,
   binaries, or oversized files).

## License

[Apache 2.0](LICENSE)
