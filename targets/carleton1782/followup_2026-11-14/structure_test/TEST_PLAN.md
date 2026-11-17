# Pre-written test: what the two numbers of a word code are (written 14 Nov 2026, before the new cipher pages were opened)

Written by our AI agent (Andrew Beling, with AI agents) after studying the 174 codes of `key/word_codes.tsv` and before
any cipher figure of the later Carleton letters in B.45 (BL Add MS 21705 ff. 73-82, reel H-1649's sister reel H-1434,
frames about 976-979) was looked at. The clear texts of those letters (B.45 p. 60, frame 975) had been seen: one page,
read for orientation, not aligned.

## Hypothesis (from the 174 known codes, not held out)

A word code `a-b` is read with `b` = the place of the word's first letter in a 24-letter alphabet with I/J and U/V
counted as follows: a1 b2 c3 d4 e5 f6 g7 h8 i/j9 k10 l11 m12 n13 o14 p15 q16 r17 s18 t19 u20 v21 w22 x23 y24;
and `a` = the word's number inside that letter's list (1 to at least 58), in an order that is not alphabetical.
165 of the 174 codes fit; the 9 that do not are listed in `STRUCTURE.md`.

## Test (held out)

Material: every word code (unmarked pair, not a spelled group) in the cipher copies of Carleton's letters in B.45
ff. 73-82 that are not the 6 or 25 Sep letters, aligned word for word with the clear copies in B.45 pp. 60-61.

1. **Initial-letter test.** For every aligned code whose clear word is unambiguous, predict the clear word's first
   letter from `b` alone. Pass if at least 80% of the aligned codes (minimum 20 codes) have the predicted first letter,
   and the best of 200 controls (the `b` values shuffled among the same codes, seed 1782) scores below 40%.
2. **Table test.** For codes already in `key/word_codes.tsv`, predict the word from the table (any listed reading
   counts). Pass if at least 80% agree (minimum 10 codes).
3. The alignment is done by hand from the images; the alignment file is written before the score script is run, and
   both are kept whatever the result.

If the B.45 cipher pages turn out not to be transcribable from the images, or hold fewer than 20 word codes, the test
is reported as not run, and the structure stays an observation on the 174 known codes.

## Addendum (written 14 Nov 2026 before the material below was read at a legible size)

The B.45 cipher pages turned out not to exist as transcripts: B.45 p. 61 (frame H-1434/976) says the ciphers of
ff. 73-84 were not copied, only decoded (pp. 57, 60, 61) or cross-referenced to B.148. So the B.45 test is not run.

Same test, same thresholds, applied instead to the next held-out material in reach: the cipher letters of late 1781 in
B.147 (Robertson to Haldimand, 31 Oct 1781, p. 406, frame H-1649/1057, which shows number pairs with words written
between the lines; Clinton to Haldimand, p. 382 with an "Explanation" p. 385), if they use word codes of the form a-b.
Only codes whose clear word is given on the page (interlined or in the explanation) are scored. Seen before writing
this: frame 1057 at 600 pixels (illegible) and Brymner's calendar entries. If the 1781 letters turn out to be all
spelled (line-letter), the test is reported as not run.
