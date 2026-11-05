# 容密 (Rongmi) key, June 1916

Key v2 (C83), recovered by Brice Dudout with Claude (Opus 5.5) in October 2026; published on the Wenmi site
(https://bdudout.github.io/wenmi/en/rongmi.html) and in https://github.com/bdudout/wenmi/tree/main/solver/numeric1916
(`common.py`, `verify.py`, `mingmi.py`). Licence: CC BY 4.0 (attribution: Brice Dudout, Wenmi). Free to reuse; please cite.

The forms are read in columns, right to left, top to bottom, sheet after sheet, in groups of four digits; the first two
groups, 1369 1378, are a clear prefix (= 容密) and are not enciphered.

## As a formula

For each group C: replace each digit by the table of its place, then P = (σ(C) + 0901) mod 10000 with
ordinary carries; P is the character number in the Chinese telegraph code (CTC).

| digit read | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| thousands | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 9 | 0 |
| hundreds | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| tens | 0 | 1 | 9 | 8 | 2 | 7 | 6 | 5 | 4 | 3 |
| units | 9 | 8 | 0 | 1 | 7 | 2 | 3 | 4 | 5 | 6 |

No group starts with 00: the encipherer writes 90. Example: σ(2081) = 2048, + 0901 = 2949 款; 9084 → 0047, + 0901 = 0948 國.

## As a renumbered 明密 code book (S. Tomokiyo)

This reading of the key is due to Satoshi Tomokiyo (Cryptiana, section "Mingmi (明密) Format Code: Gongmi, Rongmi,
Chenmi"; the section is undated, the page was last modified 24 Oct 2026 and Wenmi cites it as 23 Oct 2026, https://cryptiana.web.fc2.com/code/chinesecrypto_e2.htm). The clerk did no arithmetic: he used a copy of the standard 明密 telegraph code book
whose page, column and row numbers had been rewritten by hand for secret (密) use. The formula above describes the same
table by calculation.

Pages numbered cyclically from page 10: written page 01 = page 10, 02 = 11, …, 79 = 88, then 81 = 00, …, 90 = 09
(the "+ 0901" of the formula is this page shift plus one row).

| written digit | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| column | 0 | 1 | 9 | 8 | 2 | 7 | 6 | 5 | 4 | 3 |
| row (1-10) | 10 | 9 | 1 | 2 | 8 | 3 | 4 | 5 | 6 | 7 |

One cell differs from the formula: written page 80 is page 89 in Tomokiyo's numbering, 99 by the formula. The only group
concerned, 8012 (N25), read in neither case; with two adjacent digits swapped, 8102 gives 一 (一切到乞賜教). The reading
of N25 was corrected accordingly on the Wenmi site (32c6b9f, 22-23 Oct 2026); his simpler numbering is the more probable.
Cryptiana credits the finding that 8012 is an enciphering error for 8102 to Dudout; Wenmi credits Tomokiyo's note that it reads in neither version.

For all 10,000 group values the key splits exactly into page (first two digits), column (tens) and row (units), with no
residual carry (`mingmi.py`). In the book each column holds xxx1 to xxx9 and then, at the bottom, xxx0: this is what the
"carries" of the formula express.
