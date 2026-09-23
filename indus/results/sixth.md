# Sixth pass: the ending grid and the opening formula

## G1 The ending grid

- lines of 2+ signs: 2560; endings: (none) x1208, 740 x894, 520 x202, 740 400 x158, 740 90 x79, 520 400 x11, 740 151 x8.
- mutual information between the stem's last sign and the ending type (none / 740 / 520), last signs with 10+ lines (1990 lines): 0.865 bits; permutations as large: 0.000.

| stem ends in | lines | 740 | 520 | none |
|---|---|---|---|---|
| 70 | 14 | 0% | 93% | 7% |
| 33 | 53 | 8% | 83% | 9% |
| 233 | 27 | 15% | 74% | 11% |
| 240 | 60 | 27% | 72% | 2% |
| 231 | 12 | 25% | 58% | 17% |
| 235 | 12 | 42% | 50% | 8% |
| 220 | 93 | 33% | 47% | 19% |
| 460 | 19 | 63% | 32% | 5% |
| 1 | 15 | 0% | 13% | 87% |
| 31 | 24 | 25% | 12% | 62% |
| ... | | | | |
| 61 | 16 | 100% | 0% | 0% |
| 803 | 15 | 100% | 0% | 0% |
| 176 | 92 | 100% | 0% | 0% |
| 222 | 16 | 100% | 0% | 0% |
| 636 | 16 | 100% | 0% | 0% |
| 923 | 28 | 100% | 0% | 0% |
| 630 | 14 | 100% | 0% | 0% |
| 752 | 41 | 100% | 0% | 0% |

- stems ending in a fish sign take 520 in 120 of 238 lines (50%); other stems 76 of 1752 (4%).

## G2 The second slot after 740

- lines ending 740 + second sign: 245 (400 x158, 90 x79, 151 x8).
- with site: 0.323 bits, permutations as large 0.000.
- with object type: 0.394 bits, permutations as large 0.000.
- with stem's last sign: 0.639 bits, permutations as large 0.000.
- by site: Harappa {'90': 22, '400': 138, '151': 4}; Lothal {'90': 9}; Mohenjo-daro {'90': 43, '400': 17, '151': 2}
- by object type: SEAL:S {'90': 48, '151': 4, '400': 7}; TAB:I {'90': 7, '400': 70}; TAB:B {'400': 69, '151': 4, '90': 16}; SEAL:R {'400': 5, '90': 1}; TAG:L {'90': 5}; ROD {'400': 7}

## O1 The opening formula

- texts opening [817/820/861] + [2/60/1]: 317; openers {'861': 104, '820': 105, '817': 108}; second element {'2': 284, '60': 22, '1': 11}.
- opener by second element: {('861', '2'): 104, ('820', '2'): 72, ('817', '2'): 108, ('820', '60'): 22, ('820', '1'): 11}.
- opener against the sign after the formula (317 texts): 0.589 bits, permutations as large 0.006.
- opener against whether that sign is a name sign (317 texts): 0.001 bits, permutations as large 0.811.
- opener against site (317 texts): 0.108 bits, permutations as large 0.000.
- opener against object type (317 texts): 0.121 bits, permutations as large 0.000.
- opener against field animal (seals with a motif) (247 texts): 0.222 bits, permutations as large 0.058.
  - 817 + pair is followed by: 48 x11, 240 x8, 235 x8, 4 x6, 233 x6, 503 x5
  - 820 + pair is followed by: 803 x7, 240 x6, 32 x6, 235 x6, 3 x5, 798 x5
  - 861 + pair is followed by: 240 x9, 235 x8, 32 x6, 798 x6, 3 x6, 16 x4

