# Third test of the lee1779 rule (Arthur Lee to Henry Laurens, 7 Dec 1778): result

Plan: `TEST_PLAN_gloss3.md` (frozen before the images were fetched; two addenda before any gloss was read). One run.
Worker: Claude (Opus 5.5). Strips cut by a separate Opus agent; figures transcribed by blind Opus readers.
No person has checked any reading.

## Result: FAIL (third attempt, after two misses)

| | Hits | Share | Mark |
|---|---|---|---|
| Real rule, 1776 | 10 of 19 (same 8, other form 2) | 53% | 80% |
| Real rule, without the abbreviated gloss "S-p-h" | 9 of 19 | 47% | |
| Control C1 page +1 | 0 of 19 | 0% | under 10% |
| Control C2 page -1 | 0 of 19 | 0% | under 10% |
| Control C3 other column | 0 of 19 | 0% | under 10% |

The controls pass; the rule misses the mark by far.

## Seeds

Readers C and D both read the seed 81,b,XX as 84 and were rejected; the redo readers E and F were used. E again read
84 (81 as alternative); F read all seeds right. As the plan's addendum says, E's file is used with this failure stated.
Agreement E with F on the 19 groups: 12 of 19 in all three parts.

## Why it missed (second look after scoring; the score is not changed)

Of the nine misses, seven are misread figures in the hand of this sent letter (presumably Lee's own; not compared with a sample): its 1 was read as
5 three times (170, 176, 179 read 570, 576, 579, pages that do not exist), 218 read as 210/410, 384 read as 924/224,
283 read as 203/403, and column b read as a once (115,b,XXXVIII Dean). With the figures the glosses imply, six of the
seven fall on the glossed word by the frozen rule (Junto, Triumph, Plunder, Friend, German+y, Dean; four counted on OCR
entry tables, two in key.tsv); "golden" at 179,a,IX is not explained (the OCR count gives Gondola there). One group is
under a blot ("W...") and one could not be read from its strip.

## Non-independence, stated

- Four of the ten hits are groups that recur in the 1779-80 letters (Doctor 134aVI, Congress 99aXVII, Country 107bXXX,
  Spanish 348a near 348aXXIV); they are not new evidence about the rule.
- The second look used key.tsv for 218bIII, 170bXV and 115bXXXVIII.

## What it shows

The same as the first two tests, more strongly: when the figures are read right, the 1776 rule gives the glossed word;
the weak step is reading the numerals, and in this hand AI readers misread 1 as 5 and confuse 2, 3, 8 and 9.
