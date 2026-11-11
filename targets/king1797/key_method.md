# King's code (the = 769): how `key.tsv` was built

`key.tsv` has one row per code group: `group, value, grade, n, on_element_list, source`. It holds 764 groups. The code has
about 1,600 numbers, so this is a partial key.

## Sources

The source of the key is the State Department clerks' interlinear decipherments of King's despatches on NARA M30 rolls 4-8
(1797-1803). On these copies a clerk wrote the plain word over each coded word, often with a rule drawn over the further groups
of the same word. Of 57 coded despatch copies found on the film, 48 are interlined like this (NOTES.md).

`corpus/interlined_spans.tsv` holds 8,459 rows from 72 frames: 13,603 code groups, each row being one interlinear word and the
groups under it. The columns are `source` (which transcription batch), `frame`, `page`, `line`, `span_no`, `groups`,
`interlinear`, `placement` (clear / ambiguous) and `note`. Seven AI agents transcribed the frames on 10-11 Nov 2026 from the
full-resolution NARA images. They worked in batches, without any key in view. Batches 1-6 covered 71 frames between them; three
interrupted frames were finished by batch 7, which also added three frames. Frame 004-0249 was transcribed separately
(`interlined_0249`). The working notes counted "75 frames" because they included the three frames batch 7 revisited; the corpus
has 72 distinct frames. Marks: `?` doubtful digit, `_` digit hidden by the binding, `^` the caret-like mark after a group, `v` a
small v after a group, `{}` clear words on a code line.

## Grades

| grade | n | meaning |
|---|---|---|
| D | 405 | one unmarked group under one interlinear word; majority reading over all such rows (`n` = rows). A tie is not entered. A lone value not on the element list is not entered. When two groups claim one word, only the better attested is kept (32 set aside: `build/key_v1_summary.json`) |
| S1 / S2 | 129 / 183 | frame solver: every multi-group word must split into elements of the printed 1600-element list, one element per group. The value is the only element that survives at every occurrence (`n` = occurrences; S1 = one word). No language model and no scoring |
| A | 24 | aligned to a clear text after the test: No. 59 against the Department's clear copy, and No. 30 and the 1801 items against C. R. King's print. Dynamic programming over groups and letters. A value is accepted only if it is an unowned list element and every occurrence took the same letters, either pinned by exact hits on both sides or seen twice or more. Calibration: with a tenth of the key hidden, ten times, 94 values were proposed for 220 hidden groups and 92 were right (0.979) |
| R | 15 | read on 11 Nov 2026, while reading No. 29, from the clerks' multi-group words in the corpus. Every occurrence found is listed in the `source` column, and two values (li, ty) were also checked against King's print. Six of the R rows correct D values (below) |
| I | 8 | inferred from the context of No. 29 alone: 717 dul, 389 lect, 1279 major, 1074 ock, 1490 hol, 507 wed, 1440 esteem, 269 "the?". They are doubtful, and `[?word]` in the reading |

Rough correspondence with the README grades: D, S2, A and R correspond to C (from known plaintext), S1 to M, and I to I.

The 1600-element list (`on_element_list`) is the union of the elements of Weber's WE023-WE028 (R. E. Weber, *United States
Diplomatic Codes and Ciphers 1775-1938*, 1979), taken from the text layer of the book. Weber prints the same alphabetical list
with different numberings for several State Department codes. The list is not repeated here: it is bundled once, in
`../legation1788/beling/key/weber_1600_family_vocab.txt` (pass it as `--elements`). King's code was assumed to be built on the
same printed form, and 382 of the 411 single-group values read directly from the clerks are on the list. The prior-art check found
no outside source that confirms this (NOTES.md, Prior work).

## Rebuilding it

```
python3 scripts/king_code.py build --elements <list> --out rebuild          # key_v1.tsv (723 groups)
python3 scripts/king_code.py score --key rebuild/key_v1.tsv                # the declared test on No. 59
python3 scripts/king_code.py align --elements <list> --key rebuild/key_v1.tsv --out rebuild   # key_v2.tsv (747)
python3 scripts/king_code.py decode --key key.tsv no29_transcription.txt
```

With Weber's union list, `build` reproduces `build/key_v1.tsv` byte for byte (sha256 `6a9a1d8c...9f064`, the hash recorded
before the test). `score` reproduces `test_no59/heldout_result.json`, and `align` reproduces `build/key_v2.tsv`. All three were
checked on 11 Nov 2026.

Without Weber's book, pass the WE028 sheet already in this repository instead:
`../morris1813/beling/key/codebook_M97_13_transcription.csv`. That is the Monroe cipher transcribed from NARA M97 roll 13, on
the same printed list. The build then gives 736 groups. 715 of the 723 are identical, 3 differ (84 pl/ple, 902 bl/blo, 1560
manufactur/manufacture), 5 drop out and 18 are added. On No. 59 that key scores 0.948 at coverage 0.772. This rerun is not the
declared test.

`key.tsv` = `build/key_v2.tsv` plus the R and I rows of 11 Nov 2026. The script does not make those rows; they are recorded
by hand with their evidence.

## The declared test

The test was written at 2026-11-10 19:43 -0500 (`test_no59/PREREGISTRATION.md`), before any batch came back. Despatch No. 59
of 23 Dec 1797 is wholly in bare code: 297 groups on frames 004-0272/0273, transcribed without a key. It is not in any batch.
The truth is the Department's clear text of the triplicate on 0273. The key values of covered groups are laid on the clear
text in order: a value must start within 12 x (k+1) letters of the previous match, where k is the number of groups skipped.
The score is matched / covered. The pass rule was score >= 0.85 and score minus the best of 200 shuffled keys >= 0.30. There
was one run.

Result (`test_no59/heldout_result.json`): coverage 0.742 (224 of 302 tokens; the five dashes on the code lines count as
uncovered), 212 matched, **0.946**. The shuffled keys gave a mean of 0.108 and a best of 0.165. Pass.

## Known conflicts and weak points

- **107 groups** have two or more different words written over them as single groups on different pages
  (`build/key_v1_conflicts.tsv`). Most are a clerk's slip or a word that runs over further bare groups, for example 10 = a (92)
  against "very" and "ray" once each. The majority value was taken and ties were left out. The `source` column of `key.tsv` lists
  the minority readings.
- **Words wider than their group.** A D value is wrong when the clerk wrote a whole word over its first group and the rest of
  the word's groups were bare. Six such values were found and corrected on 11 Nov 2026 from the multi-group words: 1097 prepared
  to pre, 926 mer to er, 246 prove to pro, 1338 change to dec, 287 line to li. The sixth is 128, which the clerks write as Mr or
  M. (44 times). Its element is the letter m (Symptoms, Thomson, terms, and Mr. Fox = m-r-f-o-x in No. 30), so the key now has
  m. Others of this kind may remain. For example, 550 "case" (4) looks like ca: Cabinet = 95 550 1027 1159 in No. 59 (the first
  group is "this"), and cables = 550 1028^. It was not corrected.
- **1105** is "all" five times as a single group but "al" in a dozen multi-group words (national, commercial, proposal). It is
  left as "all", with a note.
- **S1 values** rest on one word each.
- **Values after the test.** The A, R and I rows were added after the test. No. 59 helped make the A values, so a decode of No. 59
  with `key.tsv` is not a test.
- Doubtful digits: groups 1-1599 are dense, and one 1600 was read plainly ("according", 005-0138 R20). The transcribers' notes
  treat 1599 as the upper bound, and they marked readings of 1608, 1645, 1646, 1813 and 1893 doubtful for that reason. Most
  have a likely in-range reading (1045, 1046, 1093, 1508).
