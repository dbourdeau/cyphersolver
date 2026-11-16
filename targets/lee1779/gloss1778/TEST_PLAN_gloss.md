# Test plan: Arthur Lee's glossed dictionary-code groups of 1778-79 against the frozen lee1779 rule

Written 2026-11-14 20:41 EST, before any group on these pages was looked up in Entick.
Worker: Claude (Opus 5.5). Look-ups by a separate Opus 5.5 helper who is not shown the glosses.

## What is frozen (sha256, taken 2026-11-14 20:41 EST)

Worktree `output/push_2026-11-14/wt-lee1779`, branches `lee1779-beling` 8ea1d264d and `lee1779-beling-writeup` cde351331.

| File | sha256 |
|---|---|
| targets/lee1779/check/BLIND_FREEZE.txt (the rule as written) | 8f31b439959b058ae7d8574600f0487068641089cd94acd4f02e1b4f20fb3e34 |
| targets/lee1779/key.tsv | f16ea6917562d25044a5ba3c2ae7ec68f1065b21677e8414c16dc8685a27f8e8 |
| targets/lee1779/decoding.tsv | d149e8310ff2a5af1ff4274274087156b174afd5928cdf2bef8d79c3d60d9252 |
| targets/lee1779/scripts/reader/build_table.py | 9aabf0ea177dd16c23c3c1e334ee74632adce6474a5e9a9b57a5aac2ad524784 |
| targets/lee1779/scripts/reader/lookup.py | b569a4edcff0aec5644e2cefbaf02bef686f96eaf1deadea77550413e91f865d |
| output/arthur_lee_1779_2026-11-14/work/table_1776.tsv (OCR line table) | 21eb6a52cd7d7e0f0b2369d8cbfc0f4e27fd0aaa358cf5b85a3e0b6e6f295e2a |
| output/arthur_lee_1779_2026-11-14/work/table_1773.tsv | 7b86fdca48fd4c2e9bdfeb1879dbb701079c075df0c1de00c606e4ecf5ccd149 |
| output/arthur_lee_1779_2026-11-14/work/table_1781.tsv | c12039ef256a8dec8a01473d2176ae27fed01ca6d6df71308f68e1c2cf193c4e |

The rule: Entick, *New Spelling Dictionary*, London 1776 printing; group "page, column, line" = the Nth headword
entry counted down that column, skipping the running head, letter headings and run-over (continuation) lines;
pages 454-455 are Christian names in five columns a-e. Endings written after the group (-s, -d, -g, -a ...) are
inflections added by the writer. Nothing in this plan changes the rule.

## Test set

Every glossed group on: Papers of the Continental Congress (National Archives microfilm M247), item 83 vol. 1
(catalog 502957718) images 258-259 (Lee, 27 August 1778, 38 groups) and image 261 (Lee, 31 August 1778,
19 groups); item 83 vol. 2 (catalog 502958158) images 232-233 and 237 (Lee, 21-22 May 1779, 14 groups).
71 group occurrences expected. If my transcription from the images finds a different count, the count from the images rules.

## Procedure (one run)

1. Step one, numbers only. I transcribe the groups (figures only) from the images into `groups_numbers.tsv`.
   A separate Opus helper looks each group up in the 1776 scans by the frozen rule, without access to the glosses,
   the finder's notes, the PCC images, or the package's key/decoding/readings, and writes the headword to
   `lookup_blind.tsv` together with the controls. That file is frozen (sha256, time) in `FREEZE_lookup.txt`.
2. Step two. I write the glosses from the images into `glosses.tsv` and score `lookup_blind.tsv` against them
   in `scored.tsv`. No look-up is changed after the freeze; second looks at misses are recorded separately.

## Scoring (per group occurrence, against the gloss written above it)

- **same**: the headword is the glossed word.
- **other form**: same headword, another form the writer intended (plural, tense, participle, derived word: the
  written ending usually says which; e.g. Charge for "charges", Succour for "succouring", Conquer for "conquered").
- **one off**: the glossed word is the entry directly above or below in the same column.
- **different**: anything else, including no entry at that line.
Hit = same + other form.

## Controls (same groups, same scoring)

C1 page +1; C2 page -1; C3 the other column (a<->b; on 454-455 not applicable); C4 the 1773 printing at the same
page/column/line; C5 the 1781 printing (BSB copy on the Internet Archive, 11280377bsb). Controls are looked up from
the OCR line tables and hOCR by the same helper, by the same counting rule.

## Pass mark (fixed now)

- Real rule: hits in at least 80% of occurrences (57 of 71, or the same share of the count found).
- C1, C2, C3 and C5: each under 10% hits.
- C4 (1773): known beforehand to be set almost line for line like 1776 (the package's edition note: the two
  differ at court, 108a9 in 1776 vs 108a10 in 1773). It is therefore not a control of the rule, only of the edition. It is
  reported, not held to the 10% mark; it counts against 1776 only if 1773 scores higher than 1776.
- The test passes only if the real rule and all four of C1, C2, C3, C5 meet their marks.

## Known non-independence, stated before running

- Three groups of the 27 August 1778 letter (082b05 channels, 099a17 Congress, 229a37 loan), as printed by Tomokiyo, were
  among the anchors the package used to choose the edition and counting rule (`tests/edition_anchor_check.tsv`).
  They stay in the test set; the score is also reported without them.
- Several groups recur in the 1779-80 letters (for example 99a17, 108a9). The look-up is done fresh from the
  dictionary, not from key.tsv, but a recurring group is not new evidence about the rule. Reported separately.
- I (the worker) saw the finder's transcription, glosses included, before writing this plan. The blinding of the look-up
  rests on the helper, not on me. My number transcription from the images may be biased toward the finder's.
