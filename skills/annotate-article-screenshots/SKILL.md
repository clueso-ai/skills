---
name: annotate-article-screenshots
description: >-
  Annotate every screenshot in a help article — zoom, crop, blur, and arrows —
  so each image points at exactly the control its step describes. Use when the
  user says "annotate the screenshots", "add arrows to the images in this
  article", "zoom the screenshots in on the right buttons", "blur the
  sensitive bits in the doc images", or "make the article's screenshots
  clearer".
license: Apache-2.0
metadata:
  author: clueso
  category: docs-and-articles
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Annotate Article Screenshots

Turn an article's raw full-window screenshots into images that do their job: each
one cropped and zoomed to the region that matters, with an arrow or marker on
exactly the control the step tells the reader to use, and anything sensitive
blurred.

## Before you start

Ensure you can access Clueso MCP. If not, ask the user to add the Clueso MCP
connector with this URL: https://connect.clueso.io/mcp. If you can add it yourself,
do it and ask the user to authenticate. If the user wants to learn more, go to
https://help.clueso.io/mcp-setup.

## What you need

- **The article's Clueso project** — have the user name or link it. The article's
  own step text drives the annotations; no other input is required.

Confirm the target workspace before editing anything.

## How to annotate

1. **Pair each screenshot with its instruction.** For every image, read the step it
   sits under and identify the one control the reader must find: the button to
   click, the field to fill, the toggle to flip. That control is the image's
   subject — everything else is context.
2. **Crop and zoom to the subject.** Trim away browser chrome, unrelated panels,
   and dead space so the control area fills the frame while keeping just enough
   surrounding UI that the reader can locate it on their own screen. A screenshot
   where the target is a 20-pixel speck in a full desktop has failed.
3. **Point at it once.** One arrow or highlight per image, landing on the control
   the step names. If a step genuinely involves two controls, prefer numbered
   markers over a forest of arrows. Keep annotation style identical across the
   whole article — same color, same weight — so the article reads as one document.
4. **Blur what shouldn't ship.** Sweep each image for emails, names, tokens, real
   customer data, and internal URLs; blur them for good. When example data is
   distractingly fake-looking or sensitive, note it to the user rather than
   inventing replacements.
5. **Match text to picture.** If an annotation reveals a mismatch — the step says
   "Save" but the UI shows "Apply" — flag it to the user; don't quietly rewrite the
   step or annotate the wrong control.

## Review

Share the updated article and have the user skim image-by-image: can they find each
control from the picture alone? Adjust on feedback before finishing.

## Avoid

- More than one arrow per image without numbering.
- Cropping so tight the reader loses where the control lives in the app.
- Mixed annotation colors or styles within one article.
