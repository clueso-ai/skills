---
name: highlight-cursor-actions
description: >-
  Make every click in a screen recording legible: add a brief visual emphasis
  on the cursor at each click and selection so viewers never lose the pointer.
  Use when the user says "highlight my clicks", "make the cursor visible",
  "viewers can't see where I'm clicking", "add click effects", or "emphasize
  the mouse actions".
license: Apache-2.0
metadata:
  author: clueso
  category: quick-edits
  subcategory: visual-emphasis
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Highlight Cursor Actions

A cursor is a few pixels on a busy screen. This pass marks every click and
selection with a brief, consistent emphasis at the exact spot, so viewers
following along never have to hunt for the pointer.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## Inputs

1. **The video** — ask: is it an existing Clueso project (have them name or link
   it), or a raw screen recording they'll upload? Branch accordingly.

Confirm the target workspace before editing anything.

## Workflow

### 1. Find every click

Use the narration transcript to find the action moments ("click", "select",
"open", "choose"), then inspect rendered frames around each one to pin down
exactly when the click happens and the cursor's coordinates at that instant —
menus opening, buttons changing state, and dialogs appearing tell you the
frame of the click even when the cursor itself is hard to spot. Sweep the
footage for clicks the narration never mentions too; those are precisely the
ones viewers lose.

### 2. Place the emphasis

At each click's time and coordinates, add a small, brief emphasis — a subtle
ring or pulse centered on the cursor:

- **Small and short.** It marks the click and gets out of the way — roughly the
  size of the control being clicked, gone within a beat.
- **One consistent style** for the whole video: same shape, color, and duration
  at every click. Variety here reads as noise.
- Understate it. This is legibility, not decoration; if a moment deserves real
  emphasis, a zoom or spotlight is the right tool, not a bigger pulse.
- Text selections and drags get the same treatment across their short duration,
  following the cursor's path.

### 3. Verify against frames

Re-inspect rendered frames at each click: is the emphasis centered on the
cursor at the moment of the click — not where the cursor was a second earlier?
Does it obscure the control or its label? Adjust timing and position until
every marker sits exactly on the action.

### 4. Review, then export

Share the review link and get the user's nod before exporting. Then export and
hand over the final link.
