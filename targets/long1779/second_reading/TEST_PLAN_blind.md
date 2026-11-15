# Blind second reading of Enoch Long's cipher: test plan

Written 15 November 2026, before any blind reader was started. All work by AI agents; no person has checked any of it
against the images.

## What is frozen before the test

| file | sha256 |
|---|---|
| `wt-long1779/targets/long1779/reconciled_transcription.tsv` (current reading, commit 0aad0574f) | `da404fafbf51f48da2575c5e21d2505b9285038911bd87ae89cbd3605fce90bf` |
| `wt-long1779/targets/long1779/reconciled_source.txt` | `9e349fb4d889a1fc6284bfc708feb19bea1e226b1f0322c1a67d1ebc4a84e1ae` |
| `work/targets.tsv` (word list, categories, sample flag; no readings in it) | `647c658d8d44cc92b22523b30fe6b2c2a638d1160397ec34ebe65b7e77da14d9` |
| `work/linemap.tsv` (where each source line lies on the image) | `780d173a886075b6ff5081a5145d98abc96240d3b8a5cc2f7838ec80729013b9` |
| `work/crop_key.tsv` (crop code to image, side, line) | `c4f00858d68f668d74e897feb02c6cdc2e9fd76af2fca9ca7c61ecf1d9d12afe` |
| `work/crops_SHA256SUMS` (the 241 line crops) | `43b20ead224031e11d760c7bc0240b0db3622b9a6121349acecea3c13b8393c9` |

## Images

The National Archives Catalog's IIIF service gives 2064 x 2689 pixels at `full/max` for these objects, pixel for pixel the
same as the JPG we already hold (checked on image 16: mean absolute difference 0). Fold3's viewer (Andrew's signed-in
session, viewed only, nothing downloaded) shows the same scan, no sharper. So the test runs on the images we have, at
about 15 pixels for a lower-case letter. Crops are cut from them, contrast-stretched and enlarged 2.4 times for viewing
only.

## Crops

Every cipher line of the journal (241 lines; the line positions found by ink profile and checked by eye against the
line-by-line source) is cut as one crop: an upper panel showing the line with a few neighbours and red rules above and
below the target line, and a lower panel with the target band enlarged. Crops are named K001-K241 in a shuffled order
(seed 1779), so a reader does not see the lines in reading order. Six lines (13R lines 11-16, the invisible-ink recipe,
settled on the image) are kept out of the test and given to the readers as worked examples of the first alphabet; the
second alphabet is given as Long's own two rows of signs (16R, 4 October) with the letter values we infer for them.

The brief asked for a crop of "the word and its line". We crop the line and ask for every word in it, so that the
target words cannot be picked out by the reader and the same readings serve the confident-word sample.

## Readers

Eight Opus readers, one batch of about 30 crops each (`work/blind/batch1.tsv` ... `batch8.tsv`; 235 crops). They are
given only: the sign chart (text description of both alphabets, the six worked-example lines with their reading, Long's
own alphabet rows) and their crops. They are told not to open anything else (the worktree, notes, earlier readings).
For each line they write every word in order: plain words in braces, cipher words sign by sign with the best letter for
each sign and any alternative, a count of legible signs, and, separately, a word if the letters make one.

## Comparison rules (fixed now)

- The blind line is aligned with the current line by the order of cipher words (dynamic alignment on letter similarity
  where the counts differ). Every alignment is checked by me afterwards against the crop.
- Letters are compared sign by sign. Equal signs count as agreement; so do pairs that are one sign in the key: in the
  first alphabet o and u (Long writes o for u); in the second alphabet e, n and z (all dashes in his own alphabet rows), r
  and s, and m and w only where the reader marks the sign as unsure between them.
- A word **agrees** if every sign agrees and the counts are equal. Agreement rates are reported for (a) all weak words
  (probable, doubtful, unread, nonsense), (b) the named passages, (c) the 60-word sample, (d) all words.

## Resolution rules (step 4 of the brief)

- A word becomes or stays **confident** only if both readings agree sign for sign, or its signs are individually clear
  on the image when I look at it, AND the word is English that fits the sentence.
- If the signs allow two words, both are given.
- A word that context suggests but the signs do not support stays unread. In the intimate passages no gap is filled
  from expectation.
- An unread word stays unread, with the number of legible signs.
- A confident word on which the blind reader disagrees is re-examined on the crop; it is lowered to probable or
  doubtful unless the signs are individually clear.

## Confident-word sample (step 5)

Rule, fixed now: from the confident words of two or more signs outside the six worked-example lines (633 words, in
file order), take word number floor(i x 633/60) for i = 0 ... 59. Pass mark: **95% agreement sign for sign**. If it is
under 95%, all confident words in the private passages are re-examined (they are re-read blind in any case, because
every line is in the test).

## Named people

Every name in cipher (Polly, each Kimball, Nessy/Nelly, the whipped soldier's name, the creditor on image 28) is in the
list below and is compared sign by sign. "married" in the 6 October dream (17L line 4) is in the list; if it does not
agree sign for sign and is not clear on the image, the sentence will not assert it.

Appendix (the word list) follows; it is generated from `work/targets.tsv`.
## Appendix A. Words that must be re-read (weak, or in a named passage or a name)

Format: image side line: word numbers in that line (category). Word numbers count cipher words in the line, as in `reconciled_transcription.tsv` (column `word`). The current reading of these words is deliberately not repeated here.

- 11- l02: 4[H;name], 5[L;weak], 6[U;weak]
- 11- l03: 1[X;weak], 4[L;weak], 7[H;name]
- 11- l05: 5[U;weak]
- 11- l06: 1[U;weak], 2[U;weak], 3[U;weak], 6[M;weak]
- 11- l09: 3[U;weak], 4[U;weak], 5[U;weak]
- 11- l10: 4[L;weak], 5[U;weak]
- 11- l11: 3[X;weak], 4[U;weak]
- 11- l12: 1[U;weak]
- 11- l13: 1[U;weak]
- 11- l14: 5[U;weak]
- 11- l15: 1[U;weak], 2[L;weak]
- 11- l16: 1[L;weak], 2[U;weak], 3[L;weak], 4[U;weak], 5[L;weak], 6[L;weak], 7[U;weak]
- 11- l17: 3[U;weak], 4[L;weak], 5[U;weak], 6[U;weak]
- 11- l18: 1[U;weak], 2[M;weak], 3[U;weak], 6[U;weak]
- 11- l19: 1[U;weak]
- 11- l20: 1[U;weak]
- 11- l21: 1[U;weak], 2[U;weak], 3[U;weak]
- 11- l22: 1[U;weak], 2[U;weak], 3[U;weak], 4[U;weak]
- 11- l23: 1[U;weak], 2[U;weak], 3[U;weak]
- 12L l07: 1[U;weak]
- 12L l09: 1[M;weak], 3[U;weak], 4[U;weak]
- 12L l17: 1[M;weak], 2[M;weak]
- 12L l18: 1[M;weak], 2[M;weak]
- 13R l01: 3[U;weak]
- 13R l03: 2[U;weak,name], 3[H;name]
- 13R l04: 2[M;weak], 4[H;name], 5[H;name]
- 13R l08: 2[L;weak], 4[U;weak], 5[U;weak]
- 13R l09: 1[U;weak], 2[U;weak]
- 13R l10: 2[U;weak], 4[U;weak]
- 13R l18: 1[U;weak], 2[M;weak]
- 14L l07: 1[L;weak], 2[U;weak]
- 14L l11: 3[U;weak]
- 14L l14: 2[L;weak]
- 14L l17: 2[L;weak]
- 14L l18: 5[U;weak]
- 14L l19: 1[U;weak], 2[U;weak], 3[U;weak]
- 14L l20: 1[U;weak], 6[L;weak]
- 14L l21: 2[L;weak], 3[L;weak]
- 14L l23: 5[M;weak], 7[U;weak], 8[U;weak]
- 14L l24: 2[L;weak], 3[L;weak]
- 14L l25: 3[U;weak], 4[U;weak], 6[U;weak]
- 14L l26: 1[M;weak], 2[U;weak]
- 14L l27: 2[M;weak], 3[U;weak], 7[U;weak]
- 14L l28: 1[L;weak], 5[M;weak], 6[U;weak]
- 14L l29: 1[U;weak]
- 14L l30: 1[U;weak], 4[U;weak], 5[U;weak]
- 14L l31: 2[U;weak]
- 14R l01: 1[U;weak], 2[U;weak]
- 14R l04: 3[U;weak], 4[U;weak], 5[M;weak]
- 14R l12: 4[M;weak]
- 14R l14: 1[L;weak]
- 14R l18: 1[U;weak]
- 14R l19: 3[M;weak], 4[M;weak]
- 14R l21: 1[U;weak,punishment,name], 2[H;punishment], 3[L;weak,punishment], 4[U;weak,punishment], 5[H;punishment], 6[U;weak,punishment], 7[H;punishment], 8[U;weak,punishment]
- 14R l22: 1[H;punishment], 2[U;weak,punishment], 3[H;punishment], 4[H;punishment], 5[H;punishment], 6[H;punishment], 7[H;punishment], 8[H;punishment], 9[H;punishment]
- 15L l06: 1[L;weak], 3[U;weak], 4[U;weak]
- 15L l07: 3[U;weak]
- 15L l14: 1[U;weak]
- 15L l16: 6[H;name]
- 15L l17: 2[U;weak]
- 15L l18: 2[U;weak]
- 15L l20: 1[U;weak], 5[U;weak], 6[U;weak]
- 15L l21: 1[U;weak], 2[L;weak], 4[M;weak], 5[L;weak]
- 15L l24: 3[L;weak,name], 6[U;weak]
- 15L l25: 2[U;weak], 5[U;weak]
- 15R l03: 2[H;name]
- 15R l10: 2[L;weak]
- 15R l11: 4[H;name]
- 15R l15: 1[U;weak], 2[U;weak]
- 15R l18: 2[M;weak]
- 16L l01: 1[H;intimate_Sep], 2[U;weak,intimate_Sep], 3[H;intimate_Sep], 4[H;intimate_Sep], 5[H;intimate_Sep]
- 16L l02: 1[H;intimate_Sep], 2[H;intimate_Sep], 3[U;weak,intimate_Sep], 4[L;weak,intimate_Sep]
- 16L l03: 1[H;intimate_Sep], 2[H;intimate_Sep], 3[H;intimate_Sep], 4[H;intimate_Sep], 5[H;intimate_Sep], 6[H;intimate_Sep]
- 16L l04: 1[H;intimate_Sep], 2[H;intimate_Sep], 3[U;weak,intimate_Sep], 4[H;intimate_Sep], 5[H;intimate_Sep]
- 16L l05: 1[H;intimate_Sep], 2[H;intimate_Sep], 3[H;intimate_Sep], 4[H;intimate_Sep], 5[H;intimate_Sep]
- 16L l06: 1[H;intimate_Sep], 2[H;intimate_Sep], 3[H;intimate_Sep], 4[H;intimate_Sep], 5[U;weak,intimate_Sep]
- 16L l07: 1[H;intimate_Sep], 2[U;weak,intimate_Sep], 3[H;intimate_Sep], 4[H;intimate_Sep], 5[U;weak,intimate_Sep]
- 16L l08: 1[H;intimate_Sep], 2[H;intimate_Sep], 3[H;intimate_Sep], 4[H;intimate_Sep], 5[H;intimate_Sep], 6[H;intimate_Sep], 7[U;weak,intimate_Sep]
- 16L l09: 1[H;intimate_Sep], 2[H;intimate_Sep], 3[H;intimate_Sep], 4[H;intimate_Sep], 5[H;intimate_Sep], 6[H;intimate_Sep]
- 16L l10: 1[H;intimate_Sep]
- 16L l13: 5[M;weak]
- 16L l16: 3[U;weak]
- 16L l20: 1[L;weak,name], 2[L;weak,name]
- 16L l22: 1[L;weak]
- 16L l23: 1[U;weak]
- 16L l24: 1[U;weak], 2[U;weak]
- 16L l25: 1[U;weak], 2[U;weak]
- 16R l06: 1[H;intimate_4Oct], 2[H;intimate_4Oct], 3[H;intimate_4Oct], 4[H;intimate_4Oct]
- 16R l07: 1[H;intimate_4Oct], 2[H;intimate_4Oct], 3[H;intimate_4Oct], 4[H;intimate_4Oct], 5[H;intimate_4Oct]
- 16R l08: 1[H;intimate_4Oct], 2[H;intimate_4Oct], 3[L;weak,intimate_4Oct,name], 4[H;intimate_4Oct,name]
- 16R l09: 1[H;intimate_4Oct], 2[H;intimate_4Oct], 3[H;intimate_4Oct], 4[H;intimate_4Oct], 5[H;intimate_4Oct], 6[H;intimate_4Oct]
- 16R l10: 1[H;intimate_4Oct], 2[H;intimate_4Oct], 3[H;intimate_4Oct], 4[H;intimate_4Oct], 5[H;intimate_4Oct]
- 16R l11: 1[H;intimate_4Oct], 2[H;intimate_4Oct], 3[H;intimate_4Oct], 4[H;intimate_4Oct], 5[U;weak,intimate_4Oct], 6[U;weak,intimate_4Oct]
- 16R l12: 1[H;intimate_4Oct], 2[H;intimate_4Oct], 3[U;weak,intimate_4Oct], 4[U;weak,intimate_4Oct], 5[H;intimate_4Oct], 6[H;intimate_4Oct]
- 16R l13: 1[H;intimate_4Oct]
- 16R l15: 1[H;intimate_8Oct], 2[H;intimate_8Oct], 3[H;intimate_8Oct], 4[H;intimate_8Oct], 5[H;intimate_8Oct]
- 16R l16: 1[H;intimate_8Oct], 2[H;intimate_8Oct], 3[H;intimate_8Oct], 4[H;intimate_8Oct], 5[H;intimate_8Oct], 6[H;intimate_8Oct]
- 16R l17: 1[H;intimate_8Oct], 2[H;intimate_8Oct], 3[H;intimate_8Oct], 4[H;intimate_8Oct], 5[H;intimate_8Oct]
- 16R l18: 1[H;intimate_8Oct], 2[H;intimate_8Oct], 3[H;intimate_8Oct], 4[H;intimate_8Oct], 5[H;intimate_8Oct], 6[U;weak,intimate_8Oct]
- 16R l19: 1[H;intimate_8Oct], 2[H;intimate_8Oct], 3[H;intimate_8Oct], 4[L;weak,intimate_8Oct]
- 16R l20: 1[H;intimate_8Oct], 2[L;weak,intimate_8Oct], 3[L;weak,intimate_8Oct], 4[H;intimate_8Oct], 5[L;weak,intimate_8Oct]
- 16R l21: 1[H;intimate_8Oct], 2[H;intimate_8Oct], 3[H;intimate_8Oct], 4[H;intimate_8Oct], 5[U;weak,intimate_8Oct]
- 16R l22: 1[U;weak,intimate_8Oct], 2[U;weak,intimate_8Oct], 3[U;weak,intimate_8Oct]
- 17L l01: 1[H;mother_dream], 2[H;mother_dream], 3[H;mother_dream]
- 17L l02: 1[H;mother_dream], 2[H;mother_dream], 3[H;mother_dream], 4[H;mother_dream], 5[H;mother_dream]
- 17L l03: 1[H;mother_dream], 2[H;mother_dream], 3[H;mother_dream], 4[H;mother_dream], 5[H;mother_dream], 6[H;mother_dream]
- 17L l04: 1[L;weak,mother_dream], 2[H;mother_dream]
- 17L l05: 1[L;weak,mother_dream], 2[H;mother_dream], 3[H;mother_dream], 4[U;weak,mother_dream], 5[U;weak,mother_dream]
- 17L l06: 1[H;mother_dream], 2[H;mother_dream], 3[H;mother_dream], 4[H;mother_dream], 5[H;mother_dream]
- 18R l03: 4[M;weak]
- 18R l05: 1[U;weak]
- 18R l06: 2[L;weak], 4[U;weak], 5[L;weak]
- 18R l07: 2[L;weak], 4[L;weak]
- 18R l08: 3[U;weak]
- 19L l02: 1[H;money], 2[H;money], 3[U;weak,money]
- 19L l03: 1[U;weak,money]
- 19L l04: 1[H;money], 2[H;money], 3[H;money], 4[H;money], 5[U;weak,money]
- 19L l05: 1[H;money], 2[L;weak,money]
- 19L l06: 1[U;weak,money], 2[U;weak,money], 3[U;weak,money], 4[U;weak,money]
- 19L l07: 1[H;money], 2[U;weak,money], 3[U;weak,money], 4[U;weak,money]
- 19L l08: 1[H;money], 2[H;money], 3[H;money], 4[U;weak,money]
- 19L l09: 1[H;money], 2[U;weak,money]
- 19L l10: 1[U;weak,money], 2[H;money], 3[H;money], 4[U;weak,money], 5[U;weak,money], 6[U;weak,money]
- 19L l11: 1[H;money], 2[L;weak,money], 3[H;money], 4[H;money], 5[U;weak,money]
- 19L l12: 1[H;money], 2[H;money], 3[U;weak,money], 4[U;weak,money]
- 19L l16: 1[H;money], 2[U;weak,money]
- 19L l17: 1[H;money], 2[U;weak,money]
- 22L l03: 5[L;weak]
- 22L l04: 3[M;weak], 4[U;weak], 5[U;weak]
- 22L l05: 5[U;weak]
- 22L l06: 3[L;weak]
- 22L l07: 5[U;weak]
- 22L l08: 1[M;weak], 2[U;weak], 3[U;weak], 4[U;weak]
- 22L l11: 4[H;name]
- 22L l14: 1[L;weak], 3[U;weak]
- 22L l15: 1[U;weak], 2[L;weak]
- 22L l16: 1[H;name], 2[U;weak], 4[U;weak]
- 22L l17: 1[U;weak]
- 22L l18: 1[U;weak], 2[U;weak], 3[U;weak], 4[U;weak], 5[U;weak]
- 22L l19: 1[U;weak], 3[L;weak]
- 22L l20: 1[U;weak], 2[U;weak], 4[U;weak], 5[U;weak]
- 22L l21: 2[U;weak], 3[U;weak], 4[U;weak]
- 22L l22: 1[U;weak], 2[U;weak]
- 24L l03: 1[X;weak], 2[X;weak]
- 24L l06: 1[U;weak], 2[U;weak]
- 24L l07: 1[U;weak], 2[U;weak], 3[U;weak], 4[U;weak]
- 24L l08: 1[U;weak]
- 25L l02: 1[L;weak], 2[U;weak], 3[U;weak]
- 25L l03: 1[U;weak], 2[U;weak]
- 25L l04: 1[U;weak], 6[H;name]
- 25L l05: 3[L;weak], 4[U;weak], 5[U;weak], 7[U;weak]
- 25L l06: 1[L;weak], 3[U;weak], 4[U;weak], 5[U;weak]
- 26- l02: 1[U;weak,money], 2[U;weak,money]
- 26- l03: 1[U;weak,money], 2[L;weak,money], 3[U;weak,money], 4[U;weak,money]
- 26- l04: 1[U;weak,money]
- 28- l01: 1[H;money], 2[L;weak,money], 3[U;weak,money], 4[U;weak,money]
- 28- l02: 1[H;money]
- 28- l03: 1[U;weak,money], 2[U;weak,money]
- 28- l04: 1[U;weak,money], 2[U;weak,money], 3[H;money], 4[L;weak,money]
- 29- l01: 1[U;weak,prayer], 2[U;weak,prayer]
- 29- l03: 1[H;prayer], 2[U;weak,prayer], 3[H;prayer], 4[H;prayer], 5[M;weak,prayer], 6[H;prayer], 7[U;weak,prayer]
- 29- l04: 1[H;prayer], 2[U;weak,prayer], 3[H;prayer], 4[H;prayer], 5[U;weak,prayer]
- 29- l05: 1[L;weak,prayer], 2[H;prayer], 3[L;weak,prayer], 4[H;prayer], 5[H;prayer], 6[L;weak,prayer]
- 29- l06: 1[H;prayer], 2[U;weak,prayer], 3[U;weak,prayer], 4[H;prayer], 5[L;weak,prayer], 6[H;prayer]
- 29- l07: 1[L;weak,prayer], 2[H;prayer], 3[H;prayer], 4[L;weak,prayer], 5[U;weak,prayer], 6[U;weak,prayer]

Total: 482 words.

## Appendix B. The 60 confident words in the check sample

- 11- l02 w1; 11- l05 w2; 11- l08 w4; 11- l12 w3; 11- l17 w1; 11- l22 w6; 12L l10 w2; 12L l15 w2; 13R l02 w6; 13R l05 w1; 13R l07 w7; 14L l13 w1; 14L l16 w7; 14L l21 w1; 14L l23 w2; 14L l27 w1; 14L l30 w2; 14R l01 w5; 14R l03 w3; 14R l06 w1; 14R l12 w2; 14R l15 w5; 14R l18 w2; 14R l22 w1; 15L l06 w7; 15L l10 w5; 15L l13 w2; 15L l16 w6; 15L l18 w7; 15L l20 w4; 15L l23 w6; 15L l26 w3; 15R l03 w3; 15R l07 w3; 15R l10 w1; 15R l14 w4; 15R l17 w7; 16L l02 w2; 16L l05 w2; 16L l08 w4; 16L l11 w5; 16L l13 w6; 16L l18 w1; 16L l19 w5; 16R l07 w3; 16R l09 w6; 16R l13 w1; 16R l17 w2; 16R l20 w4; 17L l02 w5; 17L l06 w3; 18R l08 w1; 19L l08 w2; 22L l02 w4; 22L l06 w1; 22L l10 w2; 22L l13 w1; 22L l17 w4; 25L l05 w1; 29- l04 w1
