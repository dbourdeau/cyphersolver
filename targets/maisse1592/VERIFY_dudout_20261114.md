# maisse1592: independent decoder and a blind sample of f. 370 (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/maisse1592` reads only `key1.tsv` and `texts/f370_figures.txt` /
`texts/f373_figures.txt` (not `decode.py` or the `research/reading_audit` alignment scripts). It decodes the figures
and aligns the letters with the reading (accents, case and punctuation removed; u=v, i=j):

| | groups | decoded letters | align with the reading |
|---|---|---|---|
| f. 370 | 2,349 | 2,355 | 2,291 (97.3%) |
| f. 373 | 3,958 | 4,026 | 4,015 (99.7%) |

The reading has more letters than the figures give (codes, abbreviation bars, the gutter of f. 370v, the clear close
of f. 373), as `f370_figures_vs_copy.md` and `f373_figures_vs_copy.md` say. No new disagreement.

## Blind sample of f. 370 (image)
f. 373 had a blind second reader (`texts/f373_sr_blind.txt`); f. 370 had none. Five lines drawn with
`random.seed(370)` from the lines not yet seen in this check (r23-r30, v00-v31): **r30, v09, v10, v25, v29**, 182 groups.
They were read figure by figure from openapi.bnf.fr views 419-420 at native size, then compared with
`f370_figures.txt`: **177 groups agree, Dice 97.3%** (r30 38/39, v09 36/36, v10 37/39, v25 34/35, v29 32/33).
The differences:

- r30: `17?` (figures) / `7?` (blind). Both doubtful; *vous* needs 17.
- v10: `1 7` / `17`. The figures are right (*face*); a blind-reader error.
- v29: `9?` / **`8`**. The figure is a clear 8 (b) on the image. *contrainct* needs c (9), so this is a slip by the
  encipherer, not a misreading. Suggest `8` with a note, as is done for the other slips.
- v29: one more group (`21`, *luy*) is visible at the gutter where the figures stop with `G`.
- v25: **`23` / `25`**. The code for *pape* has, at v25 and also at r06 (checked on the image), a second digit shaped
  like the 5 of *les* (loop at the top, tail curling left) and not like the flat-topped 3 of 13 or 73. The code may be
  **25**, not 23. The value (*pape*) is not in doubt. Left to the maintainer.

## Read bar (README)
`v10_relabel.measure`: f. 370 1.0, f. 373 0.987, equal to the `read_share` recorded. Nothing to change.

Key correction: none to the letters. Possibly 25 for the code written 23 (see above).

## Not done
Only five lines of f. 370 were re-read. The Brienne copy and f. 373 were not re-read.
