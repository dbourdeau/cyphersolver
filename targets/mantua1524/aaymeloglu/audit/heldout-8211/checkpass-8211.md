# Vat. lat. 8211 held-out passages: transcription notes and check pass

Output: heldout8211/transcription-8211.tsv (205 cipher/raised/struck segments plus the clear text of every page). Pass 1: work/p1_8211.txt. Blind pass 2: work/p2_8211.txt. Disagreements: work/diff_8211.md (one row per segment where the passes differ). Merge: work/merge_8211.py.

## Image quality
- All crops are 915x1282 px bitonal microfilm, so cipher signs are about 10 px tall.
- Crossbars (9 vs 9+, p vs p+ vs p#, I vs I=, e vs e+) are often 1 px or lost. That makes the 9/9+ and p+/p# distinctions the least reliable part of this transcription: 9+ appears only 12-17 times against about 145 uncrossed 9. On Vat. lat. 8214 the two were roughly equal, so many 9 here may really be 9+.
- **Effectively illegible:**
  - 72R lines 2-12: these are clear-text lines, but blotted and smudged. Their clear text is mostly `[...]`.
  - 76R lines 1-8: clear text, very faint.
  - 78L: the right edge is lost in the gutter.
  - Struck runs at 73L 3, 74R 9 and 77B 21.

## Method
1. **Pass 1:** I read 3.4x half-line crops, mostly from the denoised copy (the original only for 72R), with 4-5x zooms on doubtful spots.
2. **Pass 2:** an independent agent read blind. It did not see pass 1, only a locator (work/locator_8211.tsv) giving each line's position and the clear words around each run. It used 4-9x crops, original and denoised together, and decided crossbars on the original.
3. **Merge:** done by script.
   - Where both passes agree, the token is kept as read.
   - Where they disagree on a sign, the TSV gives `pass1{pass2}?`.
   - A sign seen by only one pass is `{+y}?` (pass 2 only) or `x{-}?` (pass 1 only).
   - A span the two passes segment differently is `[pass1 tokens / pass2 tokens]?`.
4. **Agreement:** 60 of 205 segments are identical in both passes. Most disagreements are crossbar presence, minim counts (m/n/i) and 7 vs 9.

## Segmentation fixes after pass 2
- **72R 13:** pass 1 had read the long group as one run. It is three runs: `a x 2 8 m i 9` / `I= p# 8` / `l a 2 x 9 s p# 2 8 o o m i 8 p# 2`. They are followed by `m i n o` and `7 4 2`, which both passes read.
- **Added from pass 2 only:** 78L 4 `a 2 x?` at the right edge and 78L 5 `o o 4`, written below the line.
- **74R 8 raised group:** it sits inside a bracket above line 9. The two readings disagree (`b 8 n e o` against `d{BOX}? . ss# a x b{6}?`); the TSV gives both.
- **Pass 2 flagged as possibly clear text, not cipher:** 76R 22 `d m i o` / `m i`, 78L 6 `c c c e`, and 72R 18 run 2 (it follows a che sign).

## Labels
- **`e`:** plain e with no crossbar. This is a new use, 4-5 places; it may be e+ with the bar lost.
- **`5`:** once, 76R 20, probably s.
- **Phi-shaped sign:** an oval with a straight stem through it. Pass 2 read it 6 times (72R 19, 73L 2, 76R 20 and 23, 78L 2, 77A 2) and wrote `q{9+}?`. Pass 1 mostly read it as `e+`. It is probably the same sign as 8214's `q` or `9+`, or a new one. Not resolved.
- **`?`:** an unreadable sign, one per estimated sign. Not counted.

## Coverage
Both passes found more signs than the PASSAGES.md estimates (about 790), because I transcribed every cipher run on each page, not only the listed lines:
- 73L lines 1-20: all runs.
- 77B: from line 11.
- 77A: lines 1-8.

## Line numbering
Lines are counted from the top, including the salutation and faint interlinear-height lines:
- **76R:** the faint line between "Ex[cellenti]a" and "che se ben" counts as line 4. That puts the cipher at line 9 and at lines 20-23. PASSAGES says 20-24; I found no 24th cipher line.
- **77B:** the faint top line counts as line 1, so the cipher runs over lines 11-21. PASSAGES says 15-22, so that numbering is probably offset by about 1-4.
- **77A:** cipher in lines 1-6 and 8. PASSAGES says 2-6.
