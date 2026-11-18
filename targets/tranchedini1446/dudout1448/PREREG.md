# PREREG — 1448 Tranchedini table (BnF ital. 1585 ff. 27-30), issue #616

Frozen 14 Nov 2026 before any sign-by-sign look at the cipher of f. 30 (only the thumbnail of the whole leaf may have been
seen when the images were fetched). SHA-256 of this file is recorded in `HASHES.txt` and in the README.

## Data
- Training: f. 28 (cipher, Gallica view 54) aligned with f. 27 (later clear copy, view 52). Signs named with the labels of
  `texts/sign_legend.md` (Daniel's f. 139 / f. 134 names where the shape matches). Two passes of the f. 28 transcription:
  pass A (aligned by hand with f. 27) and pass B by a subagent that sees neither f. 27 nor pass A; disagreements are
  settled on the image and written in `texts/f28_signs.txt`.
- Held out: f. 30 (cipher, views 58-59) with f. 29 (copy, views 56-57). f. 30 is transcribed sign by sign by a subagent that
  sees neither f. 29 nor the table; shapes not in the legend get new labels `@Nxx`. The reference words for each run are
  taken from f. 29 by the clear words around the run on f. 30, BEFORE the run is decoded.

## Table
- For each label, the value is the majority of its settled training values (values marked `?` do not vote; `_` = null is
  a value). Ties: no value. Labels never seen in training: no value (decode to nothing).
- The table is written to `table_1448.json` and its SHA-256 recorded in `HASHES.txt` before the measurement.

## One measurement on f. 30
- Decode each f. 30 run with the frozen table: concatenate the values (word signs give their words).
- Normalise decoded text and reference alike: lowercase, letters only, v→u, y→i, j→i, h dropped, doubled letters single.
- Score = 1 − (sum over runs of the Levenshtein distance between decoded run and reference) / (sum of reference lengths).
- Controls: 200 tables made from the frozen table by permuting values among labels of the same class — letters/syllables
  (lowercase labels with a non-null value), nulls (value `_`), word signs (UPPERCASE labels). Seed 1448.
- Thresholds: **read** if score ≥ 0.85 AND score ≥ best control + 0.30; **partial** if score ≥ best control + 0.30 only;
  otherwise **failed**. z against the controls is reported too.
- If f. 30 has fewer than 300 cipher signs, the figures are reported as "below size bar" (the rule asks ≥ 300 characters);
  they stand as the one measurement all the same. After the measurement f. 30 is burnt for this table.

## Tests asked in #616 (after the measurement, no re-fitting of the table)
1. f. 134 gloss signs: does the 1448 table hold (a) the V with a small circle on each top corner, and with what value
   (1446 gloss: *Fiorentini*), and (b) the bent F with a foot (1446 gloss: *stantie*)? Pass = same shape with the same value.
   Also reported: the bar-o-bar-o sign (1446 gloss *duca*) and the double comb (*non*).
2. f. 139 (Daniel's `texts/f139_signs.txt`): crosswalk the f. 139 labels to the 1448 labels (`sign_legend.md`, column f139);
   - coverage = share of f. 139 run tokens whose label gets a 1448 value;
   - agreement = share of crosswalked label types whose 1448 value equals the Domnina/Lasry value Daniel uses;
   - decode: stretches of ≥ 3 valued signs scored per letter with `lang.lm` it-cinquecento order 5, no spaces, against 200
     within-class shuffles of the 1448 values (z), next to Daniel's own figure (-2.149, z 4.0).
   - **Join one entry** if test 1 passes for both signs AND on f. 139 the 1448 values give z ≥ 3 with a per-letter score at
     least as good as Daniel's -2.149 and a coverage at least his 62%. Otherwise the 1448 table is a neighbour's key and
     lead 1317 gets its own target.
