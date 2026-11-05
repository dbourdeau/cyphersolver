# 辰密 (Chenmi) key, June 1916

Key C92, recovered by Brice Dudout with Claude (Opus 5.5) in October 2026; published on the Wenmi site
(https://bdudout.github.io/wenmi/en/chenmi.html) and in https://github.com/bdudout/wenmi/tree/main/solver/numeric1916
(`common.py`, `verify.py`, `mingmi.py`). Licence: CC BY 4.0 (attribution: Brice Dudout, Wenmi). Free to reuse; please cite.

The forms are read in columns, right to left, top to bottom, sheet after sheet, in groups of four digits; the first two
groups, 6591 1378, are a clear prefix (= 辰密) and are not enciphered.

## As a formula

P = 100 × page + 10 × T(tens) + U(units), with ordinary carry; P is the CTC number.
Page = the first two digits, counted backwards over the numbers without a zero: 99 = page 00, 98 = 01, …, 91 = 08,
then 89 = 09 (90 is skipped), 88 = 10, …, 11 = 80. Hence no Chenmi group has a 0 in its first two digits.

| digit read | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| tens T | 3 | 9 | 8 | 7 | 1 | 0 | 2 | 6 | 4 | 5 |
| units U | 1 | 9 | 5 | 4 | 3 | 2 | 6 | 7 | 8 | 10 |

Units 9 stands for 10 and carries. Example: 9950 4220 6219 → 0001 5281 3500 = 一興灰 (6219: page 62 → 34, tens 1 → 9,
units 9 → 10: 3400 + 90 + 10 = 3500 灰, the day code for the 10th).

## As a renumbered 明密 code book (S. Tomokiyo)

This reading of the key is due to Satoshi Tomokiyo (Cryptiana, section "Mingmi (明密) Format Code: Gongmi, Rongmi,
Chenmi"; the section is undated, the page was last modified 24 Oct 2026 and Wenmi cites it as 23 Oct 2026, https://cryptiana.web.fc2.com/code/chinesecrypto_e2.htm). The clerk did no arithmetic: he used a copy of the standard 明密 telegraph code book
whose page, column and row numbers had been rewritten by hand for secret (密) use. The formula above describes the same
table by calculation.

The key was already a renumbering (pages counted backwards over the numbers without a zero); Tomokiyo shows it
directly on a page of the book. The unit 9 that "counts as 10" is the bottom row, xxx0.

| written digit | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| column | 3 | 9 | 8 | 7 | 1 | 0 | 2 | 6 | 4 | 5 |
| row (1-10) | 1 | 9 | 5 | 4 | 3 | 2 | 6 | 7 | 8 | 10 |

For all 10,000 group values the key splits exactly into page (first two digits), column (tens) and row (units), with no
residual carry (`mingmi.py`). In the book each column holds xxx1 to xxx9 and then, at the bottom, xxx0: this is what the
"carries" of the formula express.
