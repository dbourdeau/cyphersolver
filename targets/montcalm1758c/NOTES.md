# Montcalm to the Marine minister, Carillon, 1 Sep 1758 (ANOM COL F3 15 f.194): the figures, tested blind against the code I table

Status: draft for Daniel (nothing pushed). Contributed by Brice Dudout with AI agents (Claude Opus 5.5), 23 Nov 2026.
Images: Archives nationales d'outre-mer (France), COL F3 15 f.194, IREL images FRANOM82_247MIOM013_F3_015_336-337
(free reuse, ANOM decision 2018-1, with credit); images are not in this folder.

## What this is
`targets/montcalm1758i/NOTES.md` ("Known plaintext of a second letter in this code (cipher unseen)") asks for the figures
of F3 15 f.194 to test the frozen table e001295272 on a text it has never seen. ANOM's IREL viewer now serves the
microfilm of F3 15 (ark 665694.3072240, 653 views). The letter is in figures (groups of 1-3 digits separated by dots,
values up to 697), with the **period decipherment written above every line**, signed by Montcalm.

## Prior work
Already solved: the clear text is the interlinear period decipherment; LAC's transcript (C-10528, frames 1188-1189)
copied it and montcalm1758i already quotes it; Richard 1899 summarises it. We add the figures and the test only.

## Test (protocol hashed before any computation: PREREG_fr.md, SHA-256 c29c5c8e...)
- Key: `table_e001295272.tsv` as frozen upstream (SHA-256 d13fcfac..., identical to `key/FREEZE.txt`), no correction.
- Portion: the whole letter, 311 groups (cipher.txt), against the gloss (gloss.txt), both hashed before the run.
- Measure: difflib character ratio after normalisation (a-z only); 200 shuffled tables, `random.Random(20261123)`.
- Criterion fixed in advance: >= 0.85 and >= best control + 0.30.
- **Result: 0.8465; best control 0.2325; mean 0.148. Margin met; absolute threshold missed by 0.0035 → verdict "weak".**
- Words: 131/194 gloss words (67.5%) supported letter for letter.
- Exploratory, declared after the measurement (not a pass): the same table with the Lévis close-up readings
  (`levis_detail_concordance.tsv`, agreed_reading) gives **0.891** (controls best 0.236), 145/194 words (74.7%).
  Gains: cells 2 *nécessaire*, 16 *n*, 355 *homme* (frozen *honteuse*), which the Lévis copy supplies.

## What it shows
The 1 Sep 1758 letter is in code I (the Marine cipher Moras sent Montcalm), as montcalm1758i supposed. Remaining
misses are cells 1-20 absent from the LAC photograph, a few doubtful cells and probably some of our misreadings
(4 marked *, 7 groups cut at the page edge). Useful for settling cells: e.g. 582 445 382 under "armée pour", 615 16
under "Canadiens" (16 = n confirmed by the Lévis reading).

## Files
cipher.txt, gloss.txt, measure.py, result_frozen.txt, result_exploratory_levis.txt, PREREG_fr.md.
