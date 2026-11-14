# Catalogue 1773 (Simon Dörffler to Charles XI, 1686-89): numeric table and three failed measures (Brice Dudout, Europe chiffrée)

Riksarkivet SE/RA/2115/I/19/102 (R0003596) and 19/100 (R0003594), Public Domain Mark. Text files only, no images.
Everything here is an **attempt**: three pre-registered measures, all FAILED. No reading is claimed.

## The table
- `table/TABLE-C03.json`: first table, built from the glossed training pages 470, 475, 467, 468 (transcriptions in `training/`) by a Claude Fable 5.2 run; `table/ALIGN.tsv` and `table/UNCERTAINTIES.md` are that run's alignment and its list of doubtful values.
- `table/TABLE-C04.json`: the same table corrected on training evidence only (470, 475, 467, 468, 476), frozen before page 474 was opened; every change and its evidence in `table/TABLE-C04-CHANGES.md` (French).
- System: 14-39 and 40-65 = two a...z sets (28/54 = n); 66-145 = 16 consonants x 5 vowels (ba...zu); 146-231 = words (der, die, und, von, nicht...); 255 and up = names (Bischof 260, König 317, Pohlen 331...).

## The three measures (each pre-registered and frozen by SHA-256 before the held-out page was transcribed)
| step | held-out portion | measure | result | threshold | verdict |
|---|---|---|---|---|---|
| C03 (`c03/`) | 19/102 img. 476 | gloss alignment S | 0.735 vs controls max 0.264 | 0.75 | FAIL |
| C04 (`c04/`) | 19/102 img. 474, two independent cipher passes (144/151 agree), two gloss readings | gloss alignment S | 0.660 vs max 0.250; only 112 scored groups of the 120 required | 0.75, +0.30 | FAIL |
| C05 (`c05/`) | 19/100 img. 277 + 304 (1682), 619 groups | lexicon share W (`c05/run.py`, `c05/LEXICON.txt`) | 0.488 vs max 0.343 | 0.55, +0.25 | FAIL |

Diagnostics written after each verdict (they do not change it): `c03/DIAG-POSTHOC-C03.txt`, `c04/DIAG-POSTHOC-C04.txt`. The gloss is not word for word and runs across the cipher's line ends; word boundaries are unmarked, which defeats a word-lexicon measure. 474, 476 and 277/304 are spent for us. A fair next test needs a fresh portion and a character-level measure.

## Scripts
`c03/measure.py` (gloss alignment, 200 permuted-value controls), `c04/galign.py`, `c05/run.py` (decode / measure; reads `TABLE.json` and `LEXICON.txt` from `INPUT_DIR`), `tools/` (the EM experiments that preceded the table).
Several protocol files are in French (`TABLE-C04-CHANGES.md`, reconciliation notes); the PREREGs are in English.

Transcriptions: one reader (Claude agents), the C04 cipher in two independent passes. Licence CC BY 4.0. SHA-256 in `SHA256SUMS`.
