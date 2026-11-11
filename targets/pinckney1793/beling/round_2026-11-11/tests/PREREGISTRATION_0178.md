# Held-out test on frame M30-002-0178 (Pinckney, London, Nov 1793)

Written 2026-11-11T05:55-0500, after the blind transcription of 0178 came back and before any printed text of the
25 Nov 1793 letter (American State Papers, Foreign Relations 1:327-28) or the clerk's "Explication" on frame 0179 was
opened for this test. The 0179 image is downloaded but has not been looked at. The ASP pages have not been fetched.

Known before writing this, and disclosed: the earlier v4 decode of 0178 (round 2 report) "reads as Pinckney pressing
Grenville on the posts"; Bourdeau's frame note says the 0179 Explication is the plaintext of 0178 and quotes a few phrases
from it ("relinquish the posts", "for nine years", "retire to France", "a frigate"). I have read that note.

## Keys

- **Primary, K1**: `frozen_key_v1.tsv` (311 groups, sha256 `e88b2c7f792e0759a38b56f9f14a8809aeaa3f464f06db687edfde379f7e55f4`)
  minus every row whose source is `bourdeau-c14c822` and whose group, in Bourdeau's `key.tsv` (local clone at ebb365f, Code 16
  rows, unchanged since c14c822), lists `M30-002-0178` among its sources. Reason: those values were read by Bourdeau partly
  from 0178 against the Explication, so they are not held out. The removed groups are listed in the result file.
  Nothing else is changed. K1 is written to disk and hashed before the truth text is fetched.
- Reported alongside, not used for the verdict: K0 = `frozen_key_v1` unchanged (contaminated, for comparison);
  K2 = `frozen_key_v1` rows from Tunis and Lear only (no Bourdeau values at all); and the new key v5 of this folder, frozen
  by sha256 before scoring, minus the same 0178-derived Bourdeau groups.

## Groups

Primary: groups of the blind transcription (`transcriptions/M30-002-0178/groups.tsv`) that carry no `?`, no `_`, are not
`___` and not struck, AND that are identical (digits only) to the corresponding group of Bourdeau's transcription
(`targets/legation1788/transcription/pinckney_m30.tsv`, frame 0178) after a longest-common-subsequence alignment of the two
sequences. Groups not meeting this are dropped (counted as absent, not as uncovered). Reported first: share of identical
groups between the two transcriptions. Secondary: all certain groups of the blind transcription alone.

## Truth

The text of the 25 Nov 1793 letter as printed in ASP Foreign Relations 1:327-28 (all of it that the print gives, letters
only). The measure lets the first match start anywhere, so text before or after the coded part does no harm.
If ASP prints only an extract that does not contain the matter of the coded page (no "posts"/"nine years"/"frigate"
content), the test is reported as "print does not cover 0178", and the same test is run once against the clerk's
Explication on frame 0179 (paragraphs 2-4), transcribed from the image, and labelled as such.

## Measure (same as the Eaton 22 Oct 1802 preregistration)

One stretch (the whole page in order). Take the key values of the covered groups in order. Count the largest number that
can be laid on the truth text in order as substrings, a matched value starting within 12 x (k+1) letters of the previous
match's end, k = groups skipped since that match. Score = matched / covered. Also reported: covered / groups.
Code: `eaton_heldout_score_2026_11_10.py` functions `ordered_match` and `score`, unchanged, imported.

Baseline: the key's values dealt at random to its groups, 200 shuffles, seed 17931125; mean and maximum.
Pass if score >= 0.85 and score minus shuffled maximum >= 0.30. One run. Whatever the number is, it is reported.
No key value is changed on the strength of this text.

## Keys as written to disk (added 2026-11-11T05:58-0500, still before any truth text was fetched)

- K1 `K1_frozen_v1_minus_0178.tsv`: 276 rows, sha256 `7106b738bc4c34fddc9b534aa3c306233df9acd8db7c799d8e1c7d7b239a3aa3` (35 Bourdeau rows removed).
- K2 `K2_frozen_v1_tunis_lear.tsv`: 136 rows, sha256 `7b322e2b8f4c324f8b0159e4ace0757bf8135448da9f514ab934f0fde4336352`.
- Transcription agreement: 290 of the blind reader's 299 certain groups are identical to Bourdeau's (0.970); `0178_groups_agreed.json`.

## Key v5 frozen (added 2026-11-11T06:03-0500, before any truth text was opened)

- `../code16_key_v5.tsv`: 549 groups, sha256 `17e3a2efee7b66e1d9a3462c7929919f87adb055994858e956174a90ae29773a` (built from v4 with
  `scripts/build_key_v5.py`; nothing from 0178 used).
- K5 `K5_key_v5_minus_0178B.tsv`: v5 minus the grade-B rows whose Bourdeau source lists 0178; 539 rows,
  sha256 `c7a1358d0b8b836d3577c3450ab1617091758f29f38ab9a41bd66244fbd13b15`. Reported alongside; K1 decides the verdict.
- The ASP volume OCR (`sources/raw/code16_pinckney_2026-11-11/asp_fr1/americanstatepap_c11unit_djvu.txt`) was downloaded at 05:55
  for the 1 Oct 1795 letter (p. 536); its 25 Nov 1793 section had not been opened.
