# SOLVE_LOG: baselANV9 (adjacent plaintext; TRAIN = ff. 4r, 4v against clear ff. 101r-102r)

All runs read only tx/f004r.txt, tx/f004v.txt, tx/CLEAR_TRAIN.txt (scripts/solve.py). Held-out files never opened.

## Run 1 (failed in part; logged)
Output kept as work/solve_out_run1.txt and work/KEY_run1.tsv.
- 300 word pairs; D2 rule 34/43; diaeresis rule 14/20.
- Two modelling faults, both seen on TRAIN only:
  1. The dots above the oe-sign (`Oe"`, the word *quod*) were split off as a doubling mark, so the oe-sign took the
     value "quo" and the "doubling" mark the value "d" in six words. Fix: on the oe-sign the dots form a sign of
     their own (scripts/common.py), as the bar and the superscript m already did.
  2. A sign could emit at most 3 letters, so one-sign words *quam*, *quae* (4 letters) could not align and were
     skipped; *aliquam* gave the x-sign a spurious "iq". Fix: base signs may emit up to 4 letters.

## Run 2 (the key of record, if frozen unchanged)
- Word alignment: 301 pairs, 0 cipher words unpaired, 1 clear word unpaired (*igitur*, written as one abbreviation
  sign `5~` that the model gives no letters). All 301 pairs kept (per-letter cost below 2.5).
- D2 (two dots on the line) = the nearest preceding vowel of the word: 34 of 43 (79%); some earlier vowel of the word:
  43 of 43. Adopted (bar 70%).
- Diaeresis on a sign = that sign's letter twice: 14 of 14. Adopted.
- 62 tokens with a value. Ambiguous in training and decoded with the majority value: `Cl` r 9 / i 6;
  `Dl@` s 9 / us 8 / as 7 / is 2; `6L` es 8 / en 3; `Oe~` quas 2 / quae 2; `1` b 16 / nothing 4.
