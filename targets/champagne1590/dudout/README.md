# champagne1590 (dudout/): blind shape plates on the places where the two readers of no. 25 disagree

Status: read in part (cipher words 41 of 46 sure, was 40; no. 25 21 of 22 = 95.5%, no. 24 18 of 21, no. 60 2 of 3; proposed, not applied to the profile figures).

This folder adds one check to the work of Michael Brackx (key no. 25 and the reading of no. 25, issue #96) and of
Andrew Beling (nos. 24 and 60, and a second reading of no. 25, PR #422). None of their files is changed. The key, the
transcriptions and the readings are theirs. Tomokiyo's catalogue of the Nevers keys gave the lead to key no. 25.

## What was asked

The profile lists two open questions that are questions of shape: the end of the l. 34 run of no. 25 (barred 39,
"M. de La Noue", Brackx; or barred 9, "Roy", Beling), and the ~30 places where the two readings of no. 25 differ.
For ten of these places one sign decides between the two readings. We put that sign on a blind shape plate.

## Method (blind shape plates)

- Each question shows one boxed sign of the Gallica image (BnF fr. 3623, `btv1b525245007`, f85 = no. 25, f83 = no. 24,
  f185 = no. 60), next to two or more examples of each candidate shape, cut from sure places of the same hand. No value,
  word or reading is shown. The reader picks a shape, or "none", and may add a remark.
- Three hidden controls of known answer are mixed in. The order of questions and options is drawn from a fixed seed.
- The selection rule, the boxes (`scripts/boxes.py`) and the integration rule were written and hashed (SHA-256) before
  any thumbnail was made. The answers were exported by the page and hashed on receipt. Plate building and scoring:
  AI agents (Claude Opus 5.5). Reader: Brice Dudout (human reviewer). He compares shapes only; he does not read the text.
- No image, crop or thumbnail is in this folder. The plate pages are not included, because they hold the thumbnails.

The three plates:

| plate | date | questions | controls | result |
|---|---|---|---|---|
| a (`plate_a/`) | 26 Nov 2026 | 10 targets + 3 controls | 2 of 3 | not used alone. K3 (an r) had a look-alike: after t this r is round, like the c of this hand. One amendment before any answer: T6 box moved. |
| b (`plate_b/`) | 26 Nov 2026 | 9 targets + 3 new controls | 2 of 3 | not used alone. K3 (the final r of "pour") has a curled tail, unlike the r examples. One amendment before any answer: one example box widened, one removed. |
| c (`plate_c/`) | 27 Nov 2026 | the same 9 targets + 3 new controls, no r | **3 of 3**, no remark | valid |

Rule of plate c, written before its answers: a target counts only if its answer on c is conclusive (one value, no remark
against it) and equal to the conclusive answers of a and b. Plates a and b can only restrict, never add. A reading
against both readers (T3) is flagged and not applied without a second look.

Each folder holds the rule (`REGLE-SELECTION.md`, in French) and its hash file, the frozen `scripts/boxes.py` (box
coordinates on the full-resolution Gallica pages), the answers as exported with their hash, and the answer key revealed
after scoring (`key-revealed-*.json`). These files are byte-identical copies of the frozen files; check them with
`shasum -a 256 -c` in each folder. Two hashes in the rule files of a and b cannot be checked here: the boxes before the
amendment (replaced) and `make_planche.py` of plate b (not included: it holds local paths). The answers with their
meaning in English are in `sign_check_2511/results.tsv`.

## Result

Six places are settled. In every case the answer agrees with Beling:

| target | place | Brackx | Beling | answers a / b / c | counted |
|---|---|---|---|---|---|
| T1 | no. 25 l. 34, sign under the bar (cipher) | barred 39, M. de La Noue | barred 9, Roy | 9 / 9 / 9 | yes: **Roy** |
| T4 | no. 25 l. 2, initial | Compiegne | Gonnesse | G / G / G | yes |
| T6 | no. 25 l. 21, 2nd letter | [?force] | [?Ruelle] | u / u / u | yes, as {Ruelle} (probable) |
| T8 | no. 25 l. 30, 3rd letter | d'Arques | d'Auvergne | u / u / u | yes |
| T9 | no. 25 l. 44, initial | riviere | commerce | c / c / c | yes |
| T10 | no. 25 l. 49, initial | misericorde | puissance | p / p / p | yes |

Not counted:
- **T3** (no. 24 l. 9, "36" or "56" in "de Ludouic"): **3** on all three plates. 36 = b gives "Budouic", against both
  readers. This is flagged as an alternative, not applied. A second look by a third reader is needed. If it held,
  no. 24 would go from 18 to 17 of 21.
- **T5** (no. 25 l. 8, flatteries / platines): plate a "none, capital H", then pl on b and c. Not counted (a not
  conclusive). Beling himself withdrew "platines". Open.
- **T7** (no. 25 l. 27, treuvons / croions): c on all three, but plate a had a remark ("not really the same as form 1"),
  so a is not conclusive. Not counted. c would favour Beling's "croions". Open.
- **T2** (no. 60, gloss over 64, y or n): plate a only, answer "none, Y". A y changes nothing; dropped. Launan/Launay open.

The reading of no. 25 with the six places applied is `n25_reading_plate2511.md`. It is Brackx's text with only those
six places changed and marked.

## Count (Daniel's rule: cipher words only, as in the profile of 16 Nov 2026)

Sure / {probable} / [restored] / ‹unresolved›, by words:

| letter | cipher words | sure | {probable} | [restored] | ‹unresolved› | share sure |
|---|---|---|---|---|---|---|
| no. 25 | 22 | **21** (was 20: the l. 34 run now ends "du Roy") | 0 | 0 | 1 (the isolated figure 3) | **95.5%** |
| no. 24 | 21 | 18 | 1 ([?Paris], margin figure) | 2 (lu[y], au[o]it) | 0 | 85.7% (T3 not applied) |
| no. 60 | 3 | 2 | 1 (Launan, gloss Launay) | 0 | 0 | 66.7% |
| all | 46 | **41** | 2 | 2 | 1 | **0.891** (was 0.870) |

As before, "l'union" (58 on the page for 56) is counted read as the encipherer's slip. The three letters are read as
sentences over their whole text (no. 25 alone has 892 words), well over 300 characters.

Clear text of no. 25 (not in the measure): four words that were disputed are now sure (Gonnesse, d'Auvergne,
commerce, puissance), one hole of Brackx is closed as probable ({Ruelle}), and two small words follow as probable
({elle demeura}, {du}). About 25 of the ~30 differences between the two readers stay open.

Class: read in part, unchanged. No. 25 passes 95% on its cipher words, but no. 24 and no. 60 do not. We did not change
`fraction_read` or the `read_share` values in `profile.json`: that is for the maintainer to decide.

## Still open

- T3 "Budouic" against "Ludouic" (above).
- T5 and T7, and the ~25 other word differences of no. 25.
- Michael Brackx has not been asked about l. 34. The plates agree with Beling and with the independent verifier.
