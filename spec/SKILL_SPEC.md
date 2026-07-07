# Skill authoring spec

Every skill in this repository is a folder under `skills/` containing a `SKILL.md`
file, optionally alongside `references/` (extra markdown the agent can read on
demand). No scripts, no vendored environments, no binaries.

## SKILL.md frontmatter

```yaml
---
name: my-skill-name
description: >-
  What the skill does AND the phrases/situations that should trigger it.
  This is the only text agents see before deciding to load the skill —
  make it carry the routing.
license: Apache-2.0
metadata:
  author: clueso
  category: video-creation | video-editing
  requires: clueso-mcp
  external-apis: none        # or a comma-separated list — must be exhaustive
  external-tools: none       # local CLIs/binaries — must be exhaustive
  demo: <optional URL of an example output video>
---
```

### Field rules

- **`name`** — required. Lowercase, hyphens, 3-50 chars. Must equal the folder name.
- **`description`** — required, ≤1024 chars. Include explicit trigger phrasing
  ("Use when the user says …").
- **`license`** — required. `Apache-2.0` for skills in this repo.
- **`metadata`** — string values only.
  - `requires` — the capability surface. For this repo: `clueso-mcp`.
  - `external-apis` / `external-tools` — **the dependency contract.** `none` is the
    strongly preferred value and what this repo exists to showcase. If a skill truly
    needs something external, list every item; an undeclared dependency is a
    validation failure and grounds for rejection.

## Body conventions

The markdown body is what the agent follows once the skill triggers. Skills in this
repo keep a consistent shape:

1. **Requirements** — restate the dependency contract in prose.
2. **Inputs** — what to collect from the user before acting, and what to ask for
   rather than invent.
3. **Workflow** — numbered steps naming the exact Clueso MCP tools
   (`create_project`, `add_clips`, `get_element_schema`, `voiceover_batch`, …).
   Schemas are fetched at runtime (`get_element_schema`, `get_design_guide`) rather
   than hardcoded, so skills stay correct as the MCP evolves.
4. **Verification** — how the agent checks its own output (e.g.
   `get_clip(render=true, …)` frame checks) before `export_project`.
5. **Fallbacks** — what to do when a step fails. A skill that only works on the
   happy path isn't done.

## Hygiene (enforced by CI)

- No `.venv/`, `node_modules/`, `.env*`, compiled artifacts, or media binaries.
- No single file over 1 MB; no skill folder over 5 MB.
- `SKILL.md` present, frontmatter parses, required fields valid, `name` matches the
  folder.
