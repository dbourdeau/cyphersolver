# 共密 (Gongmi) key, June 1916

Key C51 (candidate), recovered by Brice Dudout with Claude (Opus 5.5) in October 2026; published on the Wenmi site
(https://bdudout.github.io/wenmi/en/gongmi.html) and in https://github.com/bdudout/wenmi/tree/main/solver/numeric1916
(`common.py`, `verify.py`, `mingmi.py`). Licence: CC BY 4.0 (attribution: Brice Dudout, Wenmi). Free to reuse; please cite.

The forms are read in columns, right to left, top to bottom, sheet after sheet, in groups of four digits; the first two
groups, 0364 1378, are a clear prefix (= 共密) and are not enciphered.

## As a formula

Replace the tens digit t by φ(t), then P = (9000 − C′) mod 10000 with ordinary borrowing; P is the CTC number.

| digit | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| φ (tens) | 9 | 7 | 6 | 1 | 4 | 0 | 5 | 2 | 8 | 3 |

Example: 1188, tens 8 → 8, 9000 − 1188 = 7812 黎; 7528, tens 2 → 6, 7568, 9000 − 7568 = 1432 就.

## As a renumbered 明密 code book (S. Tomokiyo)

This reading of the key is due to Satoshi Tomokiyo (Cryptiana, section "Mingmi (明密) Format Code: Gongmi, Rongmi,
Chenmi", 23 Oct 2026, https://cryptiana.web.fc2.com/code/chinesecrypto_e2.htm). The clerk did no arithmetic: he used a copy of the standard 明密 telegraph code book
whose page, column and row numbers had been rewritten by hand for secret (密) use. The formula above describes the same
table by calculation.

Pages numbered backwards: written page 89 = page 00, 88 = 01, …, 01 = 88 (89 − n). Tens give the column, units the
row counted from the bottom; the subtraction from 9000 is this double backward count.

| written digit | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| column | 0 | 2 | 3 | 8 | 5 | 9 | 4 | 7 | 1 | 6 |
| row (1-10) | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

For all 10,000 group values the key splits exactly into page (first two digits), column (tens) and row (units), with no
residual carry (`mingmi.py`). In the book each column holds xxx1 to xxx9 and then, at the bottom, xxx0: this is what the
"carries" of the formula express.
