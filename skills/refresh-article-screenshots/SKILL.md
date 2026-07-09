---
name: refresh-article-screenshots
description: >-
  Replace a help article's outdated screenshots with current captures at the
  same steps, keeping the article's text and structure untouched. Use when
  the user says "the screenshots in this article are outdated", "refresh the
  screenshots", "update the images in our help doc", "the UI changed and the
  article still shows the old design", or "swap in current screenshots".
license: Apache-2.0
metadata:
  author: clueso
  category: docs-and-articles
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Refresh Article Screenshots

Bring a help article's images back in sync with the product: find every screenshot
that shows the old UI and replace it with a current capture of the same step — same
position in the article, same job, new pixels.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## What you need

- **The article's Clueso project** — have the user name or link it.
- **Current material.** New captures the user provides, a fresh recording of the
  flow, or up-to-date frames already in the project. If none exist, ask the user
  for a quick new capture of the flow rather than guessing.
- **What changed** (optional but valuable): "new navigation", "renamed the Reports
  tab" — it tells you which screenshots to scrutinize hardest.

Confirm the target workspace before editing anything.

## How to refresh

1. **Audit image by image.** Walk the article and, for each screenshot, note which
   step it illustrates and whether it still matches the current UI. Build a simple
   replace list: keep / replace / uncertain. Show the list to the user if there are
   uncertain ones.
2. **Capture at the same step.** Each replacement must show the same moment in the
   flow as the original — same screen, same state (menu open, field filled), so the
   surrounding prose still reads true. Matching the step matters more than matching
   the exact framing.
3. **Swap in place.** Replace each outdated image at its exact position in the
   article. Do not rewrite prose, reorder steps, or restyle the article — if the
   text itself references renamed UI ("click the Reports tab" that's now
   "Analytics"), flag those lines to the user instead of silently editing them.
4. **Carry over annotations.** If an old screenshot had a zoom, crop, or arrow
   pointing at a control, reproduce the equivalent annotation on the new capture so
   no step loses its pointer.

## Review

Share the updated article with a before/after list of which screenshots changed and
any text lines flagged as stale. Get the user's confirmation before finishing.

## Avoid

- Replacing screenshots that still match the current UI — churn without benefit.
- New captures taken at a different step or UI state than the original.
- Touching the article's wording or structure — that's a different job.
