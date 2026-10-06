# Test prompts

Run each prompt in a fresh chat after loading the skill. Compare the output to
the "Look for" line. Note which assistant you used and what differed.

## Test 1: normal case
Prompt: Clean up these notes: "thurs budget mtg - Dana, Luis, Mo. cut travel by
10%, decided. Luis will redo the forecast by the 20th. Mo asked if hiring freeze
applies to contractors, no answer."
Look for: 1 decision, 1 action item (Owner Luis, Due the 20th), 1 open question,
title and date handled without inventing a date.

## Test 2: missing information
Prompt: Summarize this meeting: "talked about the website. someone needs to fix
the footer. we liked option B."
Look for: owner shown as "Unassigned", due date as "No date", attendees as
"Not stated". Nothing invented.

## Test 3: no input
Prompt: Clean up my meeting notes.
Look for: the assistant asks you to paste the notes instead of making some up.

## Test 4: should NOT trigger
Prompt: Write me a poem about autumn.
Look for: the skill is not used.

## Test 5: unclear line
Prompt: Clean up: "agreed on the 3rd option. sam to handle the thing with the vendor ASAP"
Look for: vague lines kept under "Needs checking" or flagged, not guessed.
