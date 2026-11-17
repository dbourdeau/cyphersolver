# Held-out test result (run 14 Nov 2026, after TEST_PLAN.md was written and the table frozen)

- Frozen table: `table_frozen_v1.tsv`, 686 groups, sha256 `2c2358a47ccca4e7ad266db3e4f6c158a8149a7271a246b1a7aae371c3a98cd1`
  (`table_frozen_v1.sha256`), built by `scripts/build_table.py` from `pairs.tsv` with `HOLDOUT=M31-006-0235`
  (snapshot of the pairs at freezing: `work/pairs_at_freeze_v1.tsv`). No frame of No. 262 contributed a pair.
- Held-out: No. 262, Madrid, 24 Feb 1801, M31 roll 6 frame 0235, 164 groups transcribed (`holdout/no262_transcription.txt`).
  29 groups excluded under the plan (digits uncertain, or the reference split not fixable: the year spelled in five
  groups, "the model", "article", "person", etc.). 135 groups scored.
- Run: `python3 -I scripts/holdout_test.py table_frozen_v1.tsv holdout/no262_transcription.txt` (output `holdout/TEST_RUN_v1.txt`).

| | score (share decoding to the clerk's element) | coverage | precision |
|---|---|---|---|
| Frozen table | **0.956** (129 of 135) | 0.963 | 0.992 |
| 200 shuffled tables | max 0.030, mean 0.001 | | |

**PASS** on both criteria (score >= 0.55 with precision >= 0.85; score above every shuffled table).

Misses: five groups absent from the table (1304 foreign, 561 never, 1300 carried, 815 true, 501 establish) and one
partial (1292 table "pe", reference "pel"; "com-pel-l-ed" vs "pe-ci-al" elsewhere: the element is probably "pel", with
"es-pe-ci-al" written es-pel-ci-al? left as is).

Caveats, stated plainly:
- The reference split of words into elements was written by me from the interlined gloss and the 1917 printed text. I
  knew many table values by then, so the split is not blind; where the split was not forced by the gloss or by the
  number of groups, the group was excluded (29). The score therefore measures agreement on the elements that the
  gloss fixes, which is the meaningful part.
- The held-out passage is from 1801 and the target passages from 1799; the 1791 and 1799-1801 crib pages show the same
  values throughout (994 the, 240 of, 565 to, 1467 have, 1122 ing, 1385 order...), so one code over 1791-1801 is
  well supported.

Groups from the held-out reference used later as context values in the readings (not added to the frozen table):
561 never, 1300 carried. They are marked basis "H" in `readings/context_values.tsv`.
