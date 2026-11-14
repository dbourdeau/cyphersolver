# Post-test layer (13 Nov 2026)

Everything in this folder was made after the 25 September clear copy had been opened. The frozen table and the
frozen predictions (`../carleton_1782-09-25/preclear/`) are not changed; the 12 November scoring and comparison
(`../carleton_1782-09-25/postclear/`) are kept as the record of that day and are superseded by the files here.

## How this layer came about

A second AI agent of ours, given the branch but not our conclusions, reran the predictions (byte for byte the
frozen ones), rechecked 26 cipher and spelled groups on the images (24 confirmed, 2 wrong, both corrected below),
and found a scoring error. Its record is outside the repository. The packaging agent then checked each point on the
images itself (frames 1077, 1183, 616 and 1205) before making the changes below.

## The scoring error

`postclear/score.py` set the clear word equal to the prediction for every unit not in its hand-made exception
lists, so a disagreement in those units could not show. `clear_alignment_25sep.tsv` now gives each of the 200 units
a clear word typed from B.148 p.102 (frame 1183) without reference to the predictions, and `rescore.py` compares
every unit. One unqualified prediction changes:

- **Unit 59, code 22-19**: the table says *thence*; both clear copies say "and to march from **there** to the open
  of Pines Creek" (B.148 p.102 and B.146 p.54). The same hand writes *thence* two lines further down (unit 131,
  "escaped from thence"), so it is not a misreading of the copy. It counts as a failure. It is a debatable one: the
  sense is the same, and a clerk writing out the decipherment may have put *there* for the cipher's *thence*, which
  is the reading the code gives everywhere else (Clinton twice, unit 131 here). We count it because the test was
  defined as agreement with the clear copy, word for word.

## Corrected score of the frozen predictions

| prediction class | units | result |
|---|---:|---|
| unqualified word codes | 58 | **55 agree, 3 fail**: 22-19 thence (clear there), 43-19 hundred (clear thousand), 9-8 has (clear have) |
| qualified word codes | 25 | 21 in the predicted set, 3 fail (13-14 in/on near; 5-22 who Whom; 11-1 an any), 1 with no clear counterpart |
| spelled groups | 43 | 36 exact, 6 differ, 1 extra |
| word codes not in the table | 56 | no prediction |

Shuffled-table control (`rescore.py`, seed 1782): the readings of the 100 frozen codes permuted among the codes
200 times give a mean of 0.44 agreements on the same 58 units (sd 1.43), a maximum of 15 (when *the* lands on 5-19),
and none of the 200 reaches 55.

## Corrections (`corrections.tsv`)

1. **43-19 is thousand in February too.** Clinton's clear quadruplicate (B.148 p.8, frame 1077) reads "with about
   One thousand French and Spaniards"; our 12 November alignment had misread it as *Hundred*, and that value went
   into the frozen table. So 43-19 is *thousand* in both letters. It stays a failed prediction of the frozen table,
   but it is our misreading, not a conflict in the code, and it needs no British Library check.
   `../clinton_1782-02-22/alignment.tsv`, `CLEAR_COPY.md` and `CIPHER_READING.md` are corrected; the frozen table
   (`../carleton_1782-09-25/preclear/evidence/clinton_word_constraints.tsv`) and its copy
   `../clinton_1782-02-22/word_constraints.tsv` keep *hundred*, as frozen.
2. **escapedo is escaped.** On B.148 p.123 column 4 (frame 1205) the group reads x29-6 -22 -42 -16 -1 -6 -7 and 5-6
   follows directly; there is no -9. The extra pair was probably taken from the neighbouring column. The cipher
   spells *escaped* exactly. The frozen score keeps it as one of the 6 differing groups (it is what was frozen);
   after the correction 5 of the 6 are differences in the source and 1 was our transcription slip.
3. **The 25 September clear copy** (`CLEAR_COPY_25sep.md`): "from there", not "from thence"; p.102 spells "the
   principle one" where B.146 p.54 has "Principal".

Not checked: the verifier's note that the Clinton pair before 4-14 43-19 on p.11A column 2 may read 31-1 rather than
21-1 (*about*).

## What the freeze can and cannot show

- The order of events rests only on our own agents' files and file times: the freeze (`FREEZE.json`) is dated
  23:44 UTC on 12 November, and the 25 September clear-copy images (frames 1183, 1184, 616 at full size) were saved
  two to three minutes later. Nothing outside this machine (a commit, an email, a published hash) dates the freeze.
- The checkpoint before the clear copy was opened (`../carleton_1782-09-25/CHECKPOINT.md`) was made by our own AI
  coordinator, not by anyone outside the project.
- Already on disk before the freeze, from another of our agents earlier on 12 November: an 800-pixel copy of the
  second clear copy (B.146 p.54, frame 616, saved 02:58 local time) and the OCR of Brymner's 1887 calendar (02:31),
  whose summaries name Potter, Fort Munsey, Irwin, Fort Pitt, Lake Erie, Paterson, Verplanck and the L'Aigle, and, in its entry for Haldimand's
  private letter to Ross, "Potter, with 400 continental troops" and "Irwin, of 1,000 men". The freezing agent's input manifest
  (`../carleton_1782-09-25/preclear/input_provenance.json`) lists only the key and the Clinton table, and its
  protocol says no clear transcript was opened. We can show what it declared as inputs; we cannot show that it never
  looked at those files. The word predictions are table lookups, so such knowledge could only have affected how
  pairs were grouped and read; against tuning, *hundred* was kept for 43-19 although the calendar says 1,000.
- The table is not purely from February: whether a code was "qualified" (and so outside the 58) partly comes from
  the 6 September clear text, recorded in the table's `prior_carleton_readings` column (for example 11-1 *an* was
  qualified because 6 September reads *any*). All such entries come from 6 September, none from 25 September.
- All three letters are in one system, from one headquarters, with clear copies. This is a held-out test inside a
  corpus whose table was fitted on the same system, not a blind decipherment.
