# Second gloss test of the lee1779 rule (written before any crop, helper or look-up for it)

Written 14 November 2026, 21:58 EST, by the worker (Claude Opus 5.5). This is the **second attempt, after the first
test failed its pass mark** (54 of 71, `gloss1778/TEST_RESULT_gloss.md`). It will be reported as such whatever it shows.

## Why a second test

The first test's look-up was blind, but the transcription of the figures was made by a worker who had already seen
the glosses, and three of its misses were that worker's misreadings of the clerk's figures. This test separates the
two steps fully: the figures are read by a helper who never sees the glosses, and looked up by a second helper who
never sees the glosses or the letter images.

## What is frozen (sha256)

| File | sha256 |
|---|---|
| `targets/lee1779/check/BLIND_FREEZE.txt` (the rule as written) | 8f31b439959b058ae7d8574600f0487068641089cd94acd4f02e1b4f20fb3e34 |
| `targets/lee1779/key.tsv` | f16ea6917562d25044a5ba3c2ae7ec68f1065b21677e8414c16dc8685a27f8e8 |
| first test's glosses, `lee1779_gloss_test/glosses.tsv` (scoring key, unchanged) | 3d8f29aa73131a29cd5e12a66c795988ccefc11d7f215dada230672cd4bdb123 |
| first test's figures, `lee1779_gloss_test/groups_numbers.tsv` (used only to map rows to ids after the freeze) | 91a522e5b307a740b13f48adcf7987aa2ad153393c26bc484f84a5b67262ebfc |

The rule is unchanged: Entick, *New Spelling Dictionary*, London 1776; "page, column, line" = the Nth headword entry
down that column, not counting the running head, letter headings or indented run-over lines; pp. 454-455 Christian
names in five columns a-e; endings after the group are the writer's.

## Known non-independence (stated before the run)

- **I, the worker, am not blind.** Before writing this plan I re-read the 17 misses of the first test on 1600-pixel
  images and on the 1776 dictionary pages, and I believe nine of them are misreadings of the figures. The helpers are
  not told this, nor any gloss, figure or word.
- The same 71 groups as the first test (Papers of the Continental Congress, item 83 vol. 1 images 258, 259, 261;
  vol. 2 images 232, 233, 237), so this test is not new material; it measures the rule with a cleaner transcription.
- Three groups (channels, Congress, loan; six occurrences) were anchors when the edition was chosen. Reported with and
  without them.

## Procedure (one run)

1. **Crops.** From the 1600-pixel images (`sources/raw/lee1779_push_2026-11-15/pcc83/`) I cut one horizontal band per
   line that carries code groups, from just below the interlined glosses to just below the line. I check every band
   at full size; a band in which any letter of a gloss is visible is recut or, if it cannot be cut clean, the groups in
   it are left out of the test and counted as "not tested". If more than 10 of the 71 cannot be hidden reliably, the
   test is not run. Bands are numbered at random (`band_key.tsv`, kept by me).
2. **Transcription helper (Opus).** Given only the bands, plus three seed bands from the letter book (item 102 vol. 3)
   whose figures I already know, it writes every group it sees, in order, as page, column, line and ending, with a
   confidence mark. It is told nothing about the content. A batch that misreads any seed group is rejected and
   redone by a new helper. It freezes `transcribed.tsv` (sha256, time).
3. **Look-up helper (Opus, a different agent).** Given only the frozen figures (shuffled, with three seed groups whose
   1776 words I know), the rule, and the 1776 dictionary page images (`sources/raw/entick_dictionary/` and
   `sources/raw/entick_dictionary_2/`), it writes the headword at each group, plus the controls: C1 page +1, C2 page -1,
   C3 the other column (not on pp. 454-455), C5 the 1781 printing (`11280377bsb`, OCR text). It is not shown the
   letter images, the glosses, the package's key or readings, or any notes. A batch that misses a seed is rejected and
   redone. It freezes `lookup2.tsv` (sha256, time).
4. **Scoring.** Only then I map bands back to ids and score against the first test's `glosses.tsv`, unchanged, with the
   first test's categories: same, other form (hit); one off; different. A group the transcriber read differently from
   the figures on the page is still scored as transcribed (the test measures the whole chain).

## Pass mark (the same as the first test)

- Real rule: hits in at least 80% of the tested occurrences (57 of 71, or the same share of those tested).
- C1, C2, C3 and C5: each under 10% hits.
- Passes only if the real rule and all four controls meet their marks.

## Not allowed

No change to the rule, the glosses, the scoring categories or the pass mark after this file is written. No second run.
Second looks after the score go in a separate section and do not change it.
