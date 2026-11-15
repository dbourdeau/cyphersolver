# Held-out test, follow-up keys (written 14 Nov 2026 before either key was scored)

Same held-out set, scorer and shuffles as `test/TEST_PLAN.md`: no. 228 (12 June 1760), C13A 42 ff. 48v-49r,
`transcriptions/heldout_no228_1760-06-12.txt`, 253 code groups; `scripts/heldout_test.py <key> <heldout> 200`
(shuffle seed 1759). None of the keys below was built from those two pages.

Keys, frozen (sha256 in `test/TEST_PLAN_followup.sha256`, written before the first score):

1. `key/key_clerks_only_frozen.tsv`: the 164 codes of `key/key_manuscript.tsv` (clerks' pairs from nos. 194 and
   228 f. 48r) plus every code whose value was forced by the tiling of the clerks' text in the further glossed
   despatches (basis a, `scripts/clerks_segment.py`). No value comes from Pusch's table; the 164 seed codes were
   themselves cut with his table as the aligner's dictionary (see NOTES), which is the one dependence left.
2. `key/key_clerks_enlarged_frozen.tsv`: key 1 plus the codes whose clerk's pieces were cut with Pusch's table as
   dictionary (basis b); the value is the clerk's piece, not Pusch's entry.

Report for each key: hits / 253, and mean, median and maximum of the 200 shuffled keys. No pass mark is set; the
figures are compared with the committed-key figures (78.3% for the 164-code key; 91.7% for the union of the two
committed key files, as re-run by the maintainer). The 96.0% of the first test used Pusch's full printed table,
which is not in this folder.
