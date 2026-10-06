---
name: portable-skill-builder
description: Creates and checks new SKILL.md skills that work unchanged in both Claude and local models such as IBM Granite (run in LM Studio). Use when the user wants to build, draft, tidy, or port a skill, says "make a skill for...", "turn this workflow into a skill", or asks whether a skill will work in Granite as well as Claude.
---

# Portable Skill Builder

## Purpose

Turn a repeatable task into a SKILL.md that behaves the same in Claude and in a
smaller local model. A skill is just plain instructions in a file, so the whole
trick is writing them so a smaller model can follow them without help.

## Instructions

Follow these steps in order. Do not skip step 1.

1. **Get four facts from the user.** If any are missing, ask for them (one short
   message, all four at once):
   - What task should the skill do? (one sentence)
   - What phrases would the user say that should trigger it? (2-4 examples)
   - What does the user give it, and what should come out?
   - Does it touch private data? (yes = local-only repo, no = either repo)
2. **Pick a name.** Lowercase letters, numbers, and hyphens only, under 40
   characters, matching the folder name (example: `meeting-notes-cleaner`).
3. **Write the description.** One or two sentences, third person. Say what the
   skill does, then "Use when..." followed by the real trigger phrases from step 1.
   Maximum 600 characters. This is the only text the model sees before deciding
   to use the skill, so put the trigger words in it.
4. **Write the body** using the layout in `references/skill-layout.md`.
   Apply every rule in the Portability rules section below.
5. **Add helpers only if needed.** If a step is exact arithmetic, parsing, or
   file conversion, put it in a small script under `scripts/` that uses only the
   Python standard library, and also write the same steps out in plain words
   under a heading "If code cannot be run" so a model without code tools can
   do it by hand.
6. **Check it.** If you can run code, run:
   `python3 scripts/check_skill.py path/to/skill-folder`
   Fix everything it reports as FAIL. Read each WARN and fix it unless there is
   a clear reason not to. If you cannot run code, go through
   `references/portability-checklist.md` line by line instead.
7. **Save it** to the right place:
   - private data involved: `AI-Skills-Local/<skill-name>/` (never add a git remote)
   - otherwise: `AI-Skills-Claude/<skill-name>/`, and a copy in Local if Granite
     should use it
8. **Report back** in this order: the skill name and where it was saved, the
   result of the check, and one sentence on how to trigger it. Then stop.

## Portability rules

These keep the skill working in smaller models. Every skill you write must follow them.

- **One job per skill.** If the description needs the word "and" more than
  once, split it into two skills.
- **Plain steps.** Numbered steps, one action each, starting with a verb.
  Short sentences. Spell out anything that is implied.
- **No tool names.** Say "read the file", "search the web", "run the script"
  rather than naming a product-specific tool. Not every model has the same tools.
- **Say what to do when a capability is missing.** Example: "If you cannot
  search the web, ask the user to paste the data."
- **Show the output.** Include one short example of the exact output format.
  Small models copy examples closely, so make the example correct.
- **Keep it short.** Body under 150 lines. Put long reference material in
  `references/` and say exactly when to read it.
- **Hard rules go in a list** near the end, each one a single sentence
  ("Never...", "Always...").
- **No private data inside the skill.** Put names, account numbers, and real
  figures in separate data files that stay in the Local repo, never in SKILL.md.
- **Do not rely on cleverness.** Do not write "use your judgment" without
  saying what to weigh. Give a default and say when to depart from it.

## Rules

- Never save a skill that failed the check.
- Never put a skill touching private data in the Claude (GitHub-synced) repo.
- Never invent trigger phrases; use the ones the user gave you.
- Always ask for the four facts in step 1 before writing anything.

## Example

User: "Make a skill that cleans up my meeting notes."

Good first reply:

> Four quick questions before I draft it:
> 1. Cleaning means what exactly (fix typos, add action items, reformat)?
> 2. What would you say to trigger it ("clean up these notes"...)?
> 3. What do you paste in, and what should come back?
> 4. Are the notes ever private (client or personal)?

Good final reply:

> Saved `meeting-notes-cleaner` to AI-Skills-Claude. Check: 0 FAIL, 0 WARN.
> Trigger it with: "clean up these meeting notes".

## Notes

- Claude loads only the description at first and reads the body when the skill
  triggers. Local models in LM Studio may need the skill pasted in or loaded by
  your own setup, so keep SKILL.md self-contained.
- The shape here follows the `_templates/SKILL-template.md` already in this repo.
