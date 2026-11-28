# Pass 3 variant without decoder rules C4 and C5: declared before the run

Why: C4 (`Cl Tq` = rte) and C5 (x = ch in the chi-rho-iota abbreviation) are decoder rules that are NOT on the key leaf f. 99r (`RULES_V3.md`). The separate judge could not give a figure without them (`JUDGE_P3_RESULT.md`, "H1 without decoder rules C4 and C5: not done").

What is run: the frozen key `KEY_V3.tsv` and the frozen transcriptions `tx/f015r_p3.txt`, `tx/f025r_H4.txt`, `tx/PENT_S2.txt` (hashes asserted against `FREEZE_P3.txt`), with a copy of the frozen `scripts/decode_p3.py` changed in two places only (`make_variant.py`): the pair `('Cl','Tq'):'rte'` removed (C4 off), `chi=False` (C5 off). Three outputs: noC4, noC5, noC4C5. Nothing else changes. This is a variant run after the pass 3 decode and after its judging; it is not a first pass and not held out.

Scoring rule, fixed here before the run:
- Every word the variant leaves unchanged keeps the separate judge's central call (`JUDGE_P3_RESULT.md`), and the judge's low and high calls for the range.
- Every word the variant changes is scored by this session with the judge's brief (`judge/BRIEF.txt`): S, E (one slip), N; a word holding [?] is S only if recognisable with at most one further slip. These calls are the solver side's, NOT the separate judge's, and each is listed.
- Where a changed word's call is open to doubt, two figures are given: "as called" and "strict" (every changed word N). No pooled figure.
2026-11-25T08:07:22Z
