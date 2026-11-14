# Held-out test: result (run 13 Nov 2026, after TEST_PLAN.md was written and hashed)

Plan: `test/TEST_PLAN.md`, sha256 `0bae19f6d9540be32442c3e72e473a60f738fbe1711a52bca11bd05ad793fc97` (checked OK
before the run, `test/TEST_PLAN.sha256`). Keys re-hashed before the run and unchanged:
merged `b54686fb...cba89`, manuscript-only `87f8ad9b...a9ef`. Raw output: `test/heldout_result.txt`.
Script: `scripts/heldout_test.py`. Held-out set: no. 228 of 12 June 1760, ff. 48v-49r (C13A 42, images 0098-0099),
transcribed after the freeze (`transcriptions/heldout_no228_1760-06-12.txt`): 267 groups, of which 253 are code groups
scored (14 lost in the gutter, under a blot, or plain numerals, not scored).

| key | held-out groups decoding to the clerk's word | 200 shuffled keys: mean / max |
|---|---|---|
| merged (clerk's pairs + Pusch where no pair), 548 codes | **243 / 253 = 96.0%** | 10.8% / 17.8% |
| key from the clerks' glosses, segmented with Pusch's table, 164 codes | 198 / 253 = 78.3% | 16.4% / 24.1% |

Pass rule (merged key: at least 85% and above every shuffle): **passed**.

The 10 merged-key misses are clerk's spelling or encoding slips and the aligner's handling of them (e.g. 16 *ai*
against the clerk's *ay*; 395 *hu* against *heu* in *heureuse*; 233 *aucun* where the clerk wrote *entretiens*), not
wrong key values; see `pairs/pairs_heldout_after_test.tsv` (column how = conflict).

What the test does not show: Pusch built his table from all 30 glossed despatches, no. 228 among them, so the merged
key is not independent of the held-out despatch for the codes it takes from Pusch. The key from the clerks' glosses
is built only from no. 194 and f. 48r of no. 228, but its pairs were cut out of the running gloss with Pusch's table as
the aligner's dictionary, so it is not independent of Pusch either; its 78% is the share of held-out
groups whose codes were already met in the build pages, all of which decoded to the clerk's word or a spelling of it.

Post-test change to the decoding key (not used in the test): code 208 corrected from *eu* to *cu*, an OCR error in our
extraction of Pusch's Table 2 (his own text, p. 469, gives 208 = *cu* in *parti-cu-li-er*).

Reproduced: a second AI agent of ours, not shown the readings, reran the test on 14 Nov 2026 with identical numbers.
The merged key file (`key_frozen_merged_LOCAL.tsv`, sha256 above) is not in this repository because it carries Pusch's
whole table; it is the union of `key/key_manuscript_frozen.tsv` and Pusch's Table 2.
