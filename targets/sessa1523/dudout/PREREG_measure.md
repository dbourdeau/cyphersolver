# PREREG — sessa1523, R9660 ff.141v-146v sign-by-sign re-read (written before any decoding of the re-read)

Frozen inputs (SHA256_transcription.txt, 2026-11-12 12:16:25): transcription_reread.txt, changes.tsv,
doubts_reread.tsv, make_reread.py. No re-read line has been decoded before this file was frozen.

## Question
Does the re-read transcription carry more Spanish than Daniel Bourdeau's b34 (a) transcription of the same lines,
when both are decoded by one fixed mechanical key?

## Portion
Every line listed in changes.tsv (lines where the re-read differs from b34 (a) after the notational renaming of
part-2 ꝺ to ɞ). Cipher only: clear-text quotes (tracked across lines), f~, v:db / ▷db, "/", "..", parentheses dropped.
Must decode to ≥ 300 letters; otherwise the measure is void.

## Decoder (one key, both texts)
- Code groups and any token not listed below: the most frequent non-"?" value Daniel gives that token in the
  (a)/(b) alignment of b34 (align.py, lines whose token and piece counts agree). No value: the token is an open
  group, decoded as a word break.
- Fixed sign values: ɞ r · ꝛo s · ꝺ u · ꝗ d · ɔ q · ∠ ñ · 6 e · ⅄ z · ꝍ r (b34 only) · Ɉ open · L open ·
  ne / nf / nꝑ p · v m · b v · Є h · ε h · qes es.
- Letter signs are run together; a code-group value is set off by spaces.
- Spanish model: lang es-golden-age (order 5), norm 'early'.

## Statistic
S = per-character log score of the whole decoded portion (one string, line order).

## Controls (seed 1523)
- 200 permuted keys: the values of the single-letter signs are permuted among themselves; group values kept; applied
  to the re-read text.
- 200 shuffles: the cipher tokens of each line of the re-read are shuffled within that line; same key.

## Criteria (all set now)
1. S(re-read) above every one of the 400 controls (empirical p < 1/401).
2. S(re-read) > S(b34 (a)) under the same key.
Pass both → the re-read is the better transcription for the measure; then the 95 % count is done on the reading.
Fail 2 → no update PR on the strength of the measure.
One run. The result is written to measure_result.txt, unedited.

## Reference only (not a criterion)
Daniel's own measure_read.py on his hand reading of the same lines, reported as is.
