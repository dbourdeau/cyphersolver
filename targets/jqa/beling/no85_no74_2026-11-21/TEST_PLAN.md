> Repository copy of the plan frozen before the run (sha256 of the frozen file: 494b6a49967dcf9999e9c9aed7466f951c54f1fdf0799dec8c5dc875c152052d). Three local file paths, and the name of an earlier test that is not contributed, are replaced by descriptions; nothing else is changed. Its heading gives the writing time as 03:20-03:40 and the amendments as 03:50-03:55; by the file times the plan was written about 03:35 and amended at 03:47, before the run at 03:49.

# Test plan: our "1385 = the" table against the clerk's decipherment of John Quincy Adams's Nos. 85 and 74

Written Saturday 21 November 2026, 03:20-03:40 Eastern, by an AI agent (Claude), before any number of these two despatches was looked up in our table, and before the two blind transcriptions were finished. No person has checked it. Script: `scripts/run_test.py`; its sha256 and this file's are recorded in `SHA256_before_run.txt` before the run.

What the planner had already seen, said plainly: the notes and files of Daniel Bourdeau's repository for its target `jqa` (a local copy was saved), which include that repository's own transcription of frame 0168, its transcription of frame 0196 left, and a reading of the six unglossed lines at the foot of frame 0196 left made with that repository's table on 22 September 2026. The planner had not looked up any number in our own table and had not seen any decoding of the two passages on frame 0197. The two transcribers saw none of this.

## Question

Is our table ([a local JSON file of the code sheet], key `THE1385`, 1,571 readings, file sha256 `cfb85846e25bd949fbc72a6019da03a642f7c4daf71ae56e59b04479627a64a5`, taken from the State Department's own key sheet on National Archives microfilm M97 roll 13 frames 1056-1057, used unchanged) good enough, number by number, to be applied unchanged to the lines of these despatches that the Department's clerk left undeciphered?

## Data

Two blind transcriptions, A and B, of National Archives microfilm M35 roll 3 (files `trans_A/`, `trans_B/`): frame 0196 left (No. 85 duplicate, code with the clerk's words written over the groups), frame 0168 left and right (No. 74, code), frames 0170-0171 (the clerk's separate decyphered copy of No. 74). Parsing rules are in the script and are fixed here:

- A number token with `?` or `/` is doubtful; all alternatives after `/` are candidates when aligning. A group with `x` (digits lost), `[?]` or `GAP` is a hole. Struck groups `<...>` are dropped. The raised mark `^` and underline `_` are ignored.
- A number is SCORED only if the two transcribers' number streams (aligned with difflib) give the same number in the same place and neither marks it doubtful. Holes and disputed numbers still take part in the alignment but never count.
- Letters: lower case, letters only, `j` as `i`, `v` as `u`. A table reading `ij` or `uv` counts as `i` or `u`. A number that is not in the table cannot agree.
- The test is run twice, once on A's reading of everything (base A) and once on B's (base B).

## Part 1: No. 85, frame 0196 left, the lines with the clerk's words over the groups

Unit: the single code number. Data: every number from the start of the block to the last number that has clerk's writing over it; the unglossed lines after it are not in the test (they are what the table is to be applied to).

Rule (the same as a test run earlier the same night on other letters in this code, not yet contributed): consecutive numbers are chained into one segment when one of the two has nothing written over it and they are on the same or the next line; within a segment a monotone alignment of the numbers to the clerk's letters maximises the count of matched numbers, a number matching when its table reading equals the clerk's letters at the current position; clerk letters may be skipped. A scored number AGREES if it is matched. Score = agreeing scored numbers / scored numbers.

## Part 2: No. 74, frame 0168, against the clerk's separate copy

The clerk did not write over the groups of No. 74; his decipherment is a separate sheet. So the numbers have to be aligned to his running text, by this fixed rule:

- Number stream: left leaf line by line, then the right leaf. Every left-leaf line ends in the binding gutter, so a hole is placed at the end of each left-leaf line whether or not the transcriber marked one. A last left-leaf line consisting of one number equal to the first number of the right leaf is the catchword and is dropped.
- Clerk stream: the transcriber's copy of frames 0170-0171, letters only, from "How long" on.
- Adams wrote a few words in ordinary writing inside the code. They cut both streams into segments (a word not found in the clerk's stream is ignored and its two segments merge).
- Within a segment, a monotone alignment maximising the count of matched numbers, with bounded skipping: after a matched number at most 2 clerk letters may be passed over; an unmatched number may pass over at most 14; a hole at most 30.
- The three numbers the clerk copied in figures as an error (387, 1431, 1101 on the upstream transcription; taken from the transcribers' own reading of the clerk's sheet if it differs) are never scored: they are a target, not data.
- Score as in part 1.

## Pass mark

Each part: PASS if base A and base B both reach 0.85, base A exceeds the largest control score, and the control tolerance holds. Overall PASS needs both parts. Reason for 0.85: a table that is to be trusted on lines with no decipherment beside them should agree with the clerk on at least six numbers in seven where both can be compared; the known costs of the rule (a word the clerk corrected or wrote differently, a writer's slip, a word split differently) make 1.00 unreachable. A score between the control and 0.85 is a MISS and is reported as a miss.

## Controls

The table's readings shuffled among its 1,571 numbers, 1,000 shuffles, seed 20261121, scored on base A with the same rule. Tolerance: the largest control score may not exceed 0.25 in part 1 or 0.40 in part 2 (part 2's alignment over running text is more lenient by construction); above that the part is INCONCLUSIVE whatever the real score. Before the run, `run_test.py pilot` scores 200 synthetic tables (random letters with the lengths of the real readings; no real reading is used); if the pilot's maximum for a part is above its tolerance, the skip limits of part 2 are tightened, and that change is written here before the run.

## Not enough data

Fewer than 80 scored numbers in part 1 or 200 in part 2 (base A): NOT ENOUGH DATA for that part.

## What happens after

- One run of `python3 -I scripts/run_test.py run`, output saved as `TEST_RESULT.txt`.
- On an overall PASS the table is applied unchanged to (a) the unglossed lines at the foot of frame 0196 left, (b) the two passages on frame 0197 left, (c) the three error numbers of No. 74. Every number is shown with its reading; a number missing from the table is a gap; a number the transcribers dispute or doubt is shown with both readings and marked doubtful; nothing is filled in from sense without being marked as a conjecture.
- On anything other than a PASS the table output is still written down for the record but is labelled unvalidated, no reading is claimed and no package is prepared.
- The three error numbers: for each, list the table readings of the number itself, its two neighbours on each side (n-2 to n+2), every number one digit away, every adjacent transposition, and every number made by dropping or adding one digit. A proposal for what Adams meant is made only if one candidate is a one-step slip and makes grammatical sense between "How long this" and "Russia and Austria will be suffered to remain open"; it is labelled a conjecture, with the alternatives beside it.
- Any analysis of misses goes in a separate, labelled section and changes nothing above.

## Amendments made at 03:50-03:55 Eastern, after the transcriptions arrived and before the run (no table reading had been opened)

These adapt the script to the form in which the two transcribers wrote things down. None changes the rule, the pass mark or the tolerances.

1. A group written with `GAP`, `x` or `[?]` in any form (`45GAP`, `45xGAP`, `1576?GAP`, `157x`) is one hole and keeps the clerk's word written over it. Transcribers' remarks in square brackets inside the braces (`{again[cut]}`) are removed before the clerk's letters are taken.
2. The clerk's stream for part 2 is taken only from the transcriber's numbered text lines of frames 0170-0171; headings, catchwords, the foot note, remarks in square brackets and struck words in angle brackets are left out.
3. Transcriber B reads the first of the three error numbers on the code leaf as 887, transcriber A as 387; the clerk's sheet has 387.1431.1101 in both readings. The three numbers never scored are therefore identified as the pair 1431 1101 and the number before it.
4. The right leaf of frame 0168 has 20 lines of code (both transcribers), not about 17; all 20 are in the test.

Counts before the run (`run_test.py counts`, opens no table): part 1, 139 numbers of which 112 scored; part 2, 535 tokens (base A) of which 367 scored, 9 segments, 1,776 clerk letters; the three error numbers found.

Pilot (`pilot_control.txt`, 200 synthetic tables, no real reading used): part 1 maximum 0.045, part 2 maximum 0.163. Both under the tolerances (0.25 and 0.40), so the skip limits stay as written.
