# meeting-notes-cleaner (course practice skill)

A small, complete skill folder for practicing the Agent Skills format.

## What each file is for

| File | Role | Loaded when |
|---|---|---|
| `SKILL.md` frontmatter (`name`, `description`) | Lets the assistant know the skill exists and when to use it | Discovery: always, at the start |
| `SKILL.md` body | The step-by-step instructions | Activation: when your request matches the description |
| `assets/notes-template.md` | The exact output layout | Execution: when step 6 tells the assistant to use it |
| `references/style-guide.md` | Extra wording guidance | Execution: only if the assistant is unsure (step 7) |
| `tests/test-prompts.md` | Prompts for you to try | Never loaded; for you |
| `README.md` | This file | Never loaded; for you |

## Try it in each assistant

Follow your course instructions for how each product accepts a skill. If you are
unsure, this fallback works anywhere:

1. Paste the full contents of `SKILL.md` into the chat as your first message,
   with a line above it: "Use these instructions when I send meeting notes."
2. Paste `assets/notes-template.md` too, or rely on the fallback layout inside
   `SKILL.md`, which is why that section exists.
3. Run the prompts in `tests/test-prompts.md`.

Write down what changed between assistants. Differences usually point to a step
that was not spelled out clearly enough.

## Things to try changing

- Make the description vaguer ("helps with notes") and see whether Test 4 starts
  wrongly triggering.
- Delete the "Rules" section and rerun Test 2.
- Remove the example and compare how closely each assistant follows the layout.
