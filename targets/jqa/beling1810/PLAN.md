# Held-out test of `code_table.tsv` on John Quincy Adams's despatches of 1810: plan and pass mark

Written on 22 Nov 2026 at 22:40 EST, before any score was run. The SHA-256 of this file is recorded in `PLAN.sha256` at the same moment. Author: Andrew Beling, with AI agents.

## What is tested

The table is `../code_table.tsv` as it stands on upstream main (commit 17177160), frozen and unchanged. It was rebuilt from 1811-12 material only: the clerk's decodes on M35 reel 3 and Ford vol. 4. No 1810 despatch went into it.

The texts are the coded passages of Adams's despatches Nos. 21-29 of 1810, on NARA M35 reel 2. Each passage is paired with an independent plaintext:

| Despatch | Passages | Plaintext witness |
|---|---|---|
| No. 21 (16 Aug 1810) | 1 | Ford, *Writings of JQA* 3:469 (italic, "Cypher") |
| No. 23 (5 Sep) | 7 (A-G) | the period decipherment, frames 156-158L (Ford 3:486-496 prints the same passages from another copy) |
| No. 24 (20 Sep) | 3 (A-C) | the period decipherment, frames 158R-159R (Ford 3:505-507) |
| No. 25 (30 Sep) | 7 (A-G) | the period decipherment, frames 169-172; not printed by Ford |
| No. 27 (12 Oct) | 2 (A, B) | the period decipherment, frames 178-179 (printed in *The United States and Russia*, 1980) |
| No. 28 (10/22 Oct) | 2 (A, B) | the period decipherment, frame 184 |

No. 29 (19/31 Oct) has no plaintext witness. It is not scored. It is decoded with the key sheet alone and labelled that way.

Transcriptions used: our first transcription of each passage, made from the film. These are:
- No. 21: the first rough reading.
- No. 23 and No. 24: the source-first files frozen before the period text was opened.
- No. 25: the second pass, made before the witness.
- Nos. 27 and 28: the only transcription. It was made after the period plaintext had been read, so it is not blind; this is stated wherever its numbers are given.

Rules for writing the transcriptions into `codes_1810.txt`:
- An alternative `[a/b]` or `a/b` takes the first reading.
- A `?` stays on the number.
- Marks are written as align.py's `^` (circle or caret above) and `+` (cross below).
- Clear words stay as words.
- Runs marked unread are left out.

## Measure

For each passage, `align.py`'s alignment (imported, unchanged) segments the witness plaintext over the groups, using the table alone.

1. **Agreement.** Count the groups that have a value in the table. Agreement is the share of these whose table value is aligned to the witness letters at that place ("known"), as against a value the witness contradicts ("mis"). Groups with no table value are counted apart as coverage.
2. **Control.** Repeat the same run with 100 tables in which the value sets are shuffled among the numbers (seed 20261122).
3. **Read words, strict.** A witness word counts as read only when every one of its letters is covered by a "known" group. Letters from a group with no value, from a contradicted group, or skipped by the alignment make the word a hole.

## Pass mark (fixed now)

PASS when, over all scored groups pooled, both hold:
- agreement is at least 0.80;
- agreement is at least the best of the 100 shuffled tables plus 0.30.

Otherwise the result is reported as a MISS. The read-word share is reported per despatch. It has no pass mark, because Nos. 23-28 are already read from the period decipherments; the test is of the table, not a new reading.

## Second transcriptions

No. 21 has an independent source-only reading. No. 24 and No. 29 were transcribed a second time, blind, by separate helper agents, from the film images alone and before scoring. Neither helper saw our first transcription, the table or the plaintext. Agreement between the two transcriptions of each is reported group by group after sequence alignment.

The other despatches (Nos. 23, 25, 27, 28) have one transcription. They are labelled single-reader.
