# Layout for a new SKILL.md

Copy this shape. Delete any section the skill does not need, but keep the
frontmatter, Purpose, Instructions, and Rules.

```
---
name: skill-name-here
description: <What it does.> Use when <real trigger phrases>.
---

# Skill Name Here

## Purpose
One or two sentences.

## Instructions
1. Verb-first step.
2. Verb-first step.
3. If <capability> is missing, <fallback>.

## Output format
Show the exact shape of the answer in a short example.

## If code cannot be run
Plain-words version of any script step. (Only if the skill has scripts.)

## Rules
- Never ...
- Always ...

## Notes
Edge cases found while using it.
```

Folder shape:

```
skill-name-here/
  SKILL.md
  references/   (long material, loaded only when SKILL.md says to)
  scripts/      (standard-library Python only)
  assets/       (templates and fixed files the output should copy)
```
