# Second round: the held-out test on doubly read groups only — plan and pass mark

Written on 22 Nov 2026 at 23:15 EST, before any second-round score was run; its SHA-256 is in `PLAN2.sha256`, recorded at the same
moment. Author: Andrew Beling, with AI agents. The first round (`../PLAN.md`, `../heldout_1810.txt`) is left exactly as
registered and run.

## Why a second round

The first registered test **missed**: pooled agreement 0.730 against the 0.80 mark (best shuffled table 0.125). Its
passages were our single first transcriptions, and two independent readings of the film agreed at only 0.716 (No. 24)
and 0.751 (No. 29), mostly on 0/6/8 and 3/8. So the first round measured our transcription as much as the table. This
round tries to separate the two by scoring only what two blind readers agree the film says. It is a second test, run
after a miss, and is labelled so everywhere; it does not replace the first.

**Not counted:** the post hoc rescoring of No. 24 on its second transcription (0.814, `../heldout_no24_second.txt`)
plays no part in this round or its pass mark.

## Transcriptions (all blind, all from the NARA M35 reel 2 frames alone)

Fresh blind readings were made on 22 Nov 2026 by separate helper agents (Claude Opus 5.5), each given only the frame
images, with no plaintext, no table, no earlier transcription and no candidate readings, and told to mark washed-out
groups unreadable instead of guessing (`../transcriptions_round2/`; each file's header gives reader, time and images):

| Despatch | Reading 1 | Reading 2 |
|---|---|---|
| No. 23 | X (frames 143L, 143R, 144L, 145L, 145R, 150S) | Y (same frames) |
| No. 24 | the blind second reading of round 1 (`../transcriptions/no24_second.txt`) | Z (154L, 154R, 155S) |
| No. 25 | X (167R, 168L, 168R) | Y (same) |
| No. 27, No. 28 | X (176R, 177, 182, 183) | Y (same) |
| No. 29 | the blind second reading of round 1 (`../transcriptions/no29_second.txt`) | Z (185R, 186L, 188, 189L) |

No. 21 already has two independent readings that agree at 33 of 33; it is scored on that agreed text.

## Which groups are scored

Per passage, the two readings are aligned as sequences (difflib, numbers and clear words as tokens). A group is kept
when the two readings give the same number, or when one reading's alternatives `[a/b]` include the other's number (the
shared number is kept). Marks are taken from reading 1. Every other group (different numbers, a group in one reading
only, `[illegible]`, `[clipped]`, unreadable runs) becomes a hole token `0`, which has no value in any table: the
alignment may lay plaintext letters on it, but it is not counted as a scored group. Clear words kept only when both
readings have them. Numbers above 1600 count as written (they have no table value).

Passages are matched to the witness texts by page position and the clear words quoted around them, as in round 1:
No. 23 A = 143L; B = 145R; C = 145L run 1; D = 145L run 2 + 143R; E = 144L run 1; F = 144L run 2 + 150S top line;
G = 150S run 2. No. 24 A = 154L + 154R run 1; B = 154R run 2; C = 155S. No. 25 A-G by the letters written on the page
(E = 168L run 3 + 168R run 1). No. 27 A = 176R; B = 177 run 1 + the clear sentence "I said I believed this opinion
correct" + 177 run 2. No. 28 A = 182; B = 183. Witness texts, `align.py` and `../code_table.tsv` are exactly those of
round 1 (`../codes_1810.txt`), unchanged.

## Measure, control and pass mark (unchanged from round 1)

`../heldout_1810.py` run once on `codes_1810_round2.txt` with 100 shuffled tables (seed 20261122). Agreement =
scored groups whose table value the alignment places on the witness letters / scored groups with a table value.
**PASS** when pooled agreement >= 0.80 and >= the best shuffled table + 0.30; otherwise **MISS**, reported as such,
and no further round or tuning. Also reported: agreement between the two blind readings per despatch, groups scored,
coverage, and strict read words (a witness word counts only when every letter comes from a confirmed group; a word
touching a hole token is a hole).

## No. 29

No witness: not scored. Decoded with the M97 sheet (`../../../morris1813/beling/key/codebook_M97_13_transcription.csv`)
on the agreed groups only; every other group is a hole. The words of `../no29_reading.md` are then recounted: a word
counts only when every group it rests on is an agreed group.
