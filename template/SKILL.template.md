---
name: my-new-skill
description: >-
  One or two sentences: what this skill produces, then the trigger phrasing —
  "Use when the user says …".
license: Apache-2.0
metadata:
  author: clueso
  category: video-creation
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# My New Skill

One paragraph: what the agent will have produced when this skill is done.

## Requirements

- Clueso MCP connected. Nothing else (or list exactly what else, and mirror it in
  `metadata`).

## Inputs

What to collect from the user before acting. Ask rather than invent.

## Workflow

### 1. Confirm the workspace

`find(type='workspaces')` → confirm with the user → `switch_workspace` if needed.

### 2. …

Number the steps. Name the exact Clueso MCP tools each step uses. Fetch schemas at
runtime (`get_element_schema`, `get_design_guide`) instead of hardcoding parameters.

### N. Verify and export

Render frames with `get_clip(render=true, timestamp=…)`, check them against the
design intent, fix with `update_elements` / `update_clips`, then `export_project`.

## Fallbacks

What to do when each risky step fails. A skill that only works on the happy path
isn't done.
