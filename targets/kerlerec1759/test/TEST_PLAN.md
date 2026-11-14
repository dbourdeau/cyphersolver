# Held-out test of the Kerlérec key, written before the held-out text was transcribed

Written 13 Nov 2026, 22:40 EST. Nothing from the held-out pages had been transcribed or read for the key when this
was written; the pages had been seen only as a thumbnail to find their folio numbers.

## Keys under test (frozen)

| key | file | sha256 |
|---|---|---|
| merged key (clerk's pairs + Pusch 2008 Table 2 where we have no pair), 548 codes | `work/key_frozen_merged_LOCAL.tsv` (local only: it carries Pusch's entries) | `b54686fb9b253cd0f1d089539fe0e4ace3ea4f0f0f949e6550ecc2c4b85cba89` |
| manuscript-only key (most frequent clerk reading per code), 164 codes | `key/key_manuscript_frozen.tsv` | `87f8ad9bc2d2a2e6ab0be7464652e4a90094c7547c018d65f41a52a4bb3ea9ef` |
| the build pairs both keys come from | `pairs/pairs_build.tsv` | `13e0fca25e7cd356934435b198ae306f26ad3d1e931c5a7c42e4dee4a73e62f7` |

Build set: no. 194 of 6 May 1759 (C13A 41 ff. 51r-52v, all legible lines) and no. 228 of 12 June 1760, f. 48r only
(C13A 42).

## Held-out set

No. 228 of 12 June 1760, ff. 48v and 49r (images FRANOM50_C13A_42_0098 and 0099): every code group on those two pages,
with the clerk's interlinear plaintext. Expected well over 80 groups. If those two pages give fewer than 80 legible
groups, f. 49v (image 0100) is added before scoring, and that is the only permitted change.

## Measure

1. Each held-out group is decoded with the key (the lower number of a stacked pair; groups lost in the gutter or
   illegible, and plain numerals, are not scored).
2. The decoded values are aligned with the clerk's plaintext for the same pages (lower case, accents and punctuation
   removed) by the same dynamic-programming aligner used to build the pairs (`scripts/kcommon.py: align`), with the key
   under test as its only dictionary. A group scores 1 when its decoded value equals the clerk's text at its place in
   the alignment, else 0. Groups whose code is absent from the key score 0.
3. Share = groups scoring 1 / groups scored.
4. Null: 200 shuffled keys, each a random permutation of the same values over the same codes (seed 1759), scored the
   same way.

## Pass rule (merged key)

The merged key passes if its share is **at least 0.85** and is above the highest share among the 200 shuffled keys.
The manuscript-only key is reported with the same measure and its own 200 shuffles; no threshold is set for it, since
it covers only the codes met in the build set.

A failure is kept and reported as a result.
