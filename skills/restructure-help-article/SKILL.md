---
name: restructure-help-article
description: >-
  Rework a help article for scanability and self-serve deflection — one
  heading per step, prerequisites up top, troubleshooting at the end, tight
  prose a stressed reader can skim. Use when the user says "restructure this
  help article", "make this doc scannable", "this article is a wall of text",
  "reformat this for our help center", or "improve this article so customers
  stop filing tickets".
license: Apache-2.0
metadata:
  author: clueso
  category: docs-and-articles
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Restructure Help Article

Reshape an existing article into the form self-serve readers actually use: state
what they need before they start, one clearly-headed step at a time, and the
what-if-it-didn't-work answers at the end — so they solve it themselves instead of
filing a ticket.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## What you need

- **The article's Clueso project** — have the user name or link it.
- **Style/template preferences** (optional): the help center's heading conventions,
  tone rules, or a model article to match.

Confirm the target workspace before editing anything.

## The target shape

1. **Title that matches the search.** Name the task the way a customer types it
   ("Export your billing history"), not the feature's internal name.
2. **One-line promise.** A single opening sentence: what the reader will have done
   by the end. No feature marketing.
3. **Prerequisites up top.** Required role or plan, things to have ready, links to
   setup that must exist first — as a short list before step one, so nobody
   discovers a blocker at step six.
4. **A heading per step.** Each step is its own numbered heading starting with the
   verb ("3. Choose the export format"), followed by one to three tight sentences
   and its screenshot. A scanner reading only the headings should be able to
   complete the task.
5. **Troubleshooting at the end.** The two to four most likely failure points as
   "If X happens → do Y" entries, mined from the flow itself (and from the user, if
   they know what tickets this article should deflect). This section is the
   deflection engine — don't skip it.

## How to work

- Reorganize and tighten the article's existing content into this shape; preserve
  every fact, requirement, and warning. Cut throat-clearing, merge duplicated
  explanations, split any step that hides two actions.
- Keep screenshots attached to the step they illustrate as content moves around —
  an image orphaned from its step is worse than no image.
- Write plain, second-person, present-tense instructions. Readers arrive
  mid-frustration; every extra clause costs you some of them.

## Review

Share the restructured article with a short note on what moved and what was
tightened. Get the user's confirmation before finishing.

## Avoid

- Rewriting facts or inventing steps not present in the source material.
- Burying prerequisites inside steps, or troubleshooting inside the intro.
- Headings that describe topics ("Exporting") instead of actions ("Export the
  report").
