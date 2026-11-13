# r7475: independent check of the key (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

`verify_dudout_20261114.py targets/r7475` takes the first (majority) value of each number in `R7475_key.tsv`, decodes the
cipher lines (`C:`) of `R7475.txt`, and aligns the result with the gloss lines (`G:`) after removing the clear Latin
words, the bracketed notes and the spaces.

- Numbers: 2441 legible + 3 blots = 2444, the count in R7475.txt; one lone `1` (L64) has no value.
- Agreement: 2374 of 2443 decoded letters (97.2%). The 69 others fall at the conflicts and slips listed at the end of
  R7475.txt (50 glossed z, 47 glossed p, 57 glossed w, 22 glossed d/k/z, single slips), at clear words not put in
  quotes on the cipher line (L20 "super"), and at the code group 600 (krol szwedzki).
- Key correction: none. The table's layout (alphabetical blocks: a 17-18, b 20-21, ... z 56-57, vowels e 11-14, o 7-8,
  u 5-6, y 3-4) agrees with every majority value; the minority glosses fit the 50/56, 47/42, 57/52 shape confusions
  already named in R7475.txt.
- Read bar (README): `v10_relabel.measure` on `texts/R7475_reading.md` gives 0.968 over 449 words, the recorded value.
- Not done: the images are DECODE's and were not fetched.
