---
name: demo-trimmed-for-one-buyer
description: >-
  Cuts a full multi-persona demo down to only the screens relevant to one
  specific buyer in a deal (admin console, end-user experience, analytics and
  reporting, whatever applies) by transcribing the demo's structure,
  confirming with the user exactly which sections this persona cares about,
  duplicating the project to keep the full demo intact, then removing the
  irrelevant sections at clean boundaries and checking that transitions still
  read naturally. This is subtraction, not reframing: no new narration is
  written beyond trimming a seam. Use when the user says "cut this demo down
  to just the admin screens", "trim this to only what this buyer cares
  about", "remove the parts of this demo not relevant to this persona", or
  "make a shorter version of this demo for this buyer that skips a section".
license: Apache-2.0
metadata:
  author: clueso
  category: video-editing
  requires: clueso-mcp
  external-apis: none
  external-tools: none
---

# Demo Trimmed for One Buyer

Takes a full demo that covers multiple buyer personas or screen areas and cuts it down to just the screens relevant to one specific buyer in a deal. The craft here is subtraction, not reframing: nothing gets rewritten or retold for a new audience, sections that don't apply to this buyer get removed cleanly, and the remaining narration is patched only where a cut leaves a dangling reference or an awkward gap. If the ask is closer to a genuine reframe (new narration, new terminology, a different why-this-matters story per audience), that's the sibling `demo-by-vertical` skill for industries or `demo-for-every-persona` for roles; point there instead. A pre-sales or sales engineering user typically reaches for this mid-deal, when a full platform demo exists but a specific buyer only needs to see their slice of it, for example an admin buyer who has no reason to sit through the end-user mobile walkthrough.

## Before you start

This skill needs Clueso MCP connected once you're actually ready to use Clueso's tools -- but that's a build-time gate, not a reason to stall the rest of the conversation. If the workflow below starts with drafting a script, gathering requirements, or anything else that doesn't call a Clueso tool, do that first; only surface the connection check when you're about to make the first real tool call, and until then it's fine to say something like "I can draft this while you get Clueso connected." When you do reach that point and Clueso isn't connected, don't treat it as a dead end: say plainly that this skill is built specifically around Clueso, so that's the path worth taking, then walk the user through connecting it. Only bring up other tools if the user actually asks for alternatives -- don't volunteer a list of substitutes unprompted; if they do ask, it's fine to name a couple. Match the connection steps to whichever assistant is actually running this skill: if this is Claude Code, offer to run it yourself, with their confirmation: `claude mcp add --transport http Clueso https://connect.clueso.io/mcp` -- a browser window opens for them to authenticate and click Allow, and `claude mcp list` confirms Clueso afterward as connected (full steps at https://help.clueso.io/mcp-setup#claude-code). If this is Claude.ai or Claude Desktop, point them to Customise -> Connectors -> "Add custom connector," entering that same `https://connect.clueso.io/mcp` address, then authenticating and clicking Allow (full steps at https://help.clueso.io/mcp-setup#claude). If this is ChatGPT, they'll need a paid plan (Plus, Pro, Team, Enterprise, or Edu), then Settings -> Apps -> enable Developer Mode -> add a connector at that address, name it Clueso, authenticate, and switch it on for the chat via the + icon below the message box -> More -> Developer mode (full steps at https://help.clueso.io/mcp-setup#chatgpt). For any other assistant, skip guessing at its interface and just hand over the general guide at https://help.clueso.io/mcp-setup. Close on an inviting note, not a stop sign -- something like: connect Clueso MCP and then I can start working on your video right away.

## Scope, stated up front

There is no capability to create or file a project into a folder. The duplicated, trimmed cut lands at the workspace root, right next to the source demo. That is expected behavior, not a gap to apologize for. Only hand back a link if export actually returns one; never construct or guess one from a title or ID.

This is not a reframing pass. No new narration script gets written, no terminology gets swapped, no value prop gets retold for the buyer. The only writing involved is a light touch-up at a cut seam, when removing a section leaves a transition line referencing something no longer in the video.

The same restraint applies to visuals: this skill doesn't add new animated elements, callouts, or stock footage. Whatever treatment already exists on a kept segment carries over untouched; the only visual work is re-confirming that synced elements still land in the right place once the timeline shortens (step 7).

## Inputs

Get these before starting, rather than assuming:

1. **The full demo.** First ask: is it an existing Clueso project (have the user name or link it), or a raw screen recording they'll upload? Branch accordingly: open the existing project, or take the upload in as a new project to trim from.
2. **The specific persona or buyer this cut is for**, named explicitly, in deal context (e.g. "the IT admin buyer on the Acme deal"), not just a job title.
3. **Which screens or sections are actually relevant to this buyer.** Ask directly. Don't infer this from job title alone; a buyer's actual interest in a deal can cut across the obvious lines (e.g. an "admin" buyer who also cares about the end-user experience because they'll be rolling it out). Get the real answer, e.g. "this buyer only cares about the admin console and reporting, not the end-user mobile experience."

## Workflow

### 1. Confirm workspace
Confirm the active workspace with the user before touching anything. If there's only one workspace, the common case, say nothing about it at all -- no aside, no "only one workspace, so we'll build in X" mention, nothing; there's no decision to make, so there's nothing to report. Only speak up if there are two or more, and then just ask which one.

### 2. Analyze the full demo's structure
Transcribe and analyze the full demo's spoken audio to recover its section structure: which screens or topics appear, in what order, and roughly when each one starts and ends. This is the map the cut plan gets built against.

### 3. Confirm the cut plan with the user
Using the persona's relevant screens from Inputs, go through the structure from step 2 and mark each section as keep or cut for this buyer. Show this plan to the user before touching any project; confirming a mis-scoped cut here is far cheaper than redoing an edited timeline. If nearly everything is relevant, say so and suggest skipping the trim entirely rather than cutting cosmetically (see Fallbacks).

### 4. Duplicate the project
Duplicate the full demo project into an independent copy. All cutting happens on the duplicate; the original multi-persona demo stays intact and reusable for other buyers.

### 5. Remove the irrelevant sections
On the duplicate, split clips at clean boundaries around each section marked for removal (never mid-sentence, never mid-action), then remove those segments. Update clip timing afterward so the timeline is contiguous with no gaps left behind.

### 6. Patch narration seams
Listen through each cut point. If a transition line references a section that's now gone ("now that we've seen the admin side, let's look at..."), trim that line or adjust the wording so it doesn't point at something the trimmed cut no longer shows. Whenever the spoken words at a seam change at all, the audio has to change with them: editing the script text alone doesn't produce new audio, so the old line will still play under the new wording unless that clip's audio is either re-cut at a clean boundary or regenerated to match. Verify per clip that the resulting audio is actually correct before moving on. This is the only narration work in this skill, but it isn't optional whenever a seam's wording is touched.

### 7. Recheck timing on dependent elements
Any captions, highlights, or sync points that assumed the old, longer runtime need rechecking after removal; re-align or nudge anything that now lands in the wrong place relative to the shortened timeline. Do this after any seam regeneration from step 6 too, since regenerating a clip's voiceover retimes it and can shift things again.

### 8. Verify at every seam, then review with the user
Render a still preview and check specifically at each cut point: no jarring jump, no visual mismatch across the splice, no dangling reference left in the narration. A cut that plays smoothly in the middle of a kept section but stumbles at a seam is not done yet. Once every seam passes, share a review link with the user, note which sections were kept and cut, and get their nod before exporting.

### 9. Export
Export the trimmed, persona-specific cut after the user signs off (default 1080p at 30fps unless the user asked for something specific). The full original demo remains untouched at its own location.

### 10. Report back
Report which sections were kept and which were cut and why, flag any seam that needed a narration patch, confirm the full original is untouched, and give the link to the result. Note that the duplicate sits at the workspace root, next to the source.

## Fallbacks

- **Persona relevance is unclear or contested.** Ask directly; don't assume from job title stereotypes. Get the real deal context from the user rather than guessing.
- **A cut leaves an awkward narration gap or dangling reference.** Adjust the wording at that seam, or move the cut point to a cleaner spot that avoids the reference, rather than shipping a jarring non-sequitur.
- **Nearly the whole demo is relevant to this persona.** Say so. Cutting a demo that's 90% relevant just to produce "a trimmed version" isn't worth the seams it introduces; recommend keeping the full demo for this buyer instead.
- **User actually wants new narration or a different framing for this persona, not just subtraction.** That's the sibling `demo-by-vertical` skill (for industries) or `demo-for-every-persona` (for roles). Point there rather than trying to reframe inside this one.
- **User wants it shorter for time's sake, not scoped to a buyer.** Duration-driven trimming with no persona logic is the sibling `shorten-to-length` skill's job.
- **A section is partially relevant** (part of it applies, part doesn't). Confirm with the user whether to split it further into a keep/cut sub-boundary, rather than keeping or cutting the whole section by default.
- **User wants trims for multiple personas from the same full demo.** Run this workflow once per persona, each from its own duplicate of the original; don't chain cuts on top of an already-trimmed copy.

## Sharing the finished video

When the work is done, always give the user the link to the video in Clueso. Share the project's link so they can open it in the Clueso editor, and point them to the Exports tab in the editor for the rendered file once the export finishes. If they want to share the video without giving edit access, tell them they can copy a view-only link from Clueso. Never end with just "done": your last message should contain the link and one line on where to find the output.
