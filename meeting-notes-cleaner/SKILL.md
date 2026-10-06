---
name: meeting-notes-cleaner
description: Cleans up rough meeting notes into a tidy summary with decisions, action items, and open questions. Use when the user pastes meeting notes, a call transcript, or says "clean up these notes", "summarize this meeting", or "pull out the action items".
---

# Meeting Notes Cleaner

## Purpose

Turn messy meeting notes into a short, consistent summary that someone who was
not in the meeting can read in one minute.

## Instructions

1. Read the notes the user pasted. If there are none, ask the user to paste them.
2. Find the meeting title, date, and attendees. If one is missing, write
   "Not stated" for it. Do not guess.
3. Pick out the decisions. A decision is something the group agreed to do or
   not do. Write each as one sentence.
4. Pick out the action items. An action item has a task, an owner, and a due
   date. If the owner or due date is not in the notes, write "Unassigned" or
   "No date". Do not invent either.
5. Pick out the open questions. These are things raised but not answered.
6. Write the summary using the layout in `assets/notes-template.md`.
   Copy its headings exactly and in the same order.
7. If a line in the notes is unclear, keep it in a final section called
   "Needs checking" instead of guessing what it meant. If you are unsure how
   to word something, read `references/style-guide.md`.
8. Show the finished summary and stop. Do not add advice or commentary.

## If you cannot read the template file

Use this layout:

```
# <Meeting title>
Date: <date>
Attendees: <names>

## Summary
<two or three sentences>

## Decisions
- <decision>

## Action items
- <task> (Owner: <name>, Due: <date>)

## Open questions
- <question>

## Needs checking
- <unclear line>
```

## Rules

- Never invent names, dates, or numbers that are not in the notes.
- Never leave out an action item, even a small one.
- Keep the summary under 200 words, not counting the lists.
- Leave out a section's items if there are none, and write "None" under its heading.

## Example

Input:

> mon sync w/ sam, priya. launch moves to nov 14, agreed. priya to send the
> new deck by fri. do we need legal review? nobody knew

Output:

```
# Monday sync
Date: Not stated
Attendees: Sam, Priya

## Summary
The team agreed to move the launch to November 14. Priya will send an
updated deck. Whether legal review is needed is still unknown.

## Decisions
- Launch moves to November 14.

## Action items
- Send the new deck (Owner: Priya, Due: Friday)

## Open questions
- Is legal review needed?

## Needs checking
- None
```
