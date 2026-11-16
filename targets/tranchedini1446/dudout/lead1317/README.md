# Lead 1317: the R5318 key (as K3) tested on three Tranchedini letters of 1447-49 that have period clear texts. Partial; no reading claimed

Brice Dudout, with Claude Opus 5.5 (14 Nov 2026). Lead 1317 (Nicodemo Tranchedini to Francesco Sforza, Florence, 1447-49), reserved
for Brice Dudout until 14 Dec 2026. Key sheet: DECODE R5318 "Nicodemus" (`../../r5318/`). Images: Gallica only, **no image is
included or derived here**; Source gallica.bnf.fr / BnF.

**What this is:** a key test. Each letter used here already has a clear text of the period or a later copy (ff. 34-36, f. 352, f. 70;
lead 1317, vetting of 29 Oct 2026), so its content is known. The contribution is the key (K3) and three single measurements against
those clears. The decodes in `results_*.json` are key-test outputs, **decoded, not read**: they are not readings and are not listed in
`profile.json` `outcome.texts`.

## Letters and clear texts (Gallica)
| cipher | date | clear text used as reference | Gallica |
|---|---|---|---|
| BnF italien 1585 f. 35r | 29 Feb 1448 | later clear copy ff. 34r-v, 36r (views 65, 66, 69) | [btv1b52525947w](https://gallica.bnf.fr/ark:/12148/btv1b52525947w), view 67 |
| BnF italien 1584 f. 353r | 14 Oct 1447 | copy f. 352 r-v (views 346-347; it covers L20 to the end only) | [btv1b100373864](https://gallica.bnf.fr/ark:/12148/btv1b100373864), view 347 |
| BnF italien 1585 f. 71 | 18 Jun 1449 | 15th-century decipherment f. 70 "Ex cifra Nicodemi" (view 135) | [btv1b52525947w](https://gallica.bnf.fr/ark:/12148/btv1b52525947w), view 137 |

The reference files (`texts/f34_36_reference.txt`, `texts/f352_reference.txt`, `texts/f70_reference.txt`) give, for each cipher run,
the words of those clears (the later copyist's for ff. 34-36 and 352; the 15th-century decipherer's for f. 70, transcribed in full in
`texts/f70_transcription.txt`). Credit for the plaintexts goes to them, not to this work.

## Protocol
For each letter, in this order: PREREG written and frozen by SHA-256; key frozen; two blind transcription passes (B and C, subagents
that saw neither key, values nor clear) and a blind settling on the image; transcription hashed; only then the clear read and the
reference written; one measurement; the letter is then burnt. Hashes and timestamps: `HASHES-1317.txt`, `HASHES-1317-K2.txt`,
`HASHES-1317-K3.txt`. The PREREGs are in French as frozen; English translations in `*.en.md`.

Metric (the same for the three): first value of each label; lower case, letters only, v=u, y=i, j=i, h dropped, doubled letters
simplified; score = 1 - sum Levenshtein / reference length. Controls: 200 keys shuffled inside classes (word signs / nulls /
letters-syllables). Thresholds written before each test: **read** if score >= 0.85 and >= best control + 0.30; **partial** if only
the second; otherwise **failed**.

## Results
| letter | key (frozen before the letter was opened) | signs (coverage) | score | 200 shuffles: mean / best | margin over best | z | verdict |
|---|---|---|---|---|---|---|---|
| 1585 f. 35r | R5318 crosswalk (`../../r5318/key_R5318_by_1448_label.tsv`) | 461 (83.3%) | **0.550** | 0.197 / 0.271 | 0.279 | 9.7 | failed (margin < 0.30) |
| 1584 f. 353r | K2 (`K2_key.tsv`) | 521 (91.6%) | **0.650** | 0.085 / 0.190 | 0.460 | 10.5 | partial |
| 1585 f. 71 | K3 (`K3_key.tsv`) | 1502 (93.9%) | **0.709** | 0.020 / 0.206 | 0.503 | 6.9 | partial |

None reaches 0.85, so no letter is called read. Each key was frozen before the letter it was measured on was opened: K2 was built on
R5318, ff. 28/30/35 and their clears; K3 on the same plus the burnt f. 353 and a blind review sheet of shape questions answered by
Brice Dudout (3/3 controls right; decisions in `planche/DECISIONS-K3.md`, French). With f. 71 every public letter of lead 1317 is now
used (ff. 28 and 30 in `targets/tranchedini1448/dudout/`); ital. 1583 ff. 126/132/133/162 have no public image.

## Declared deviations
- **f. 71, extra harmonisation pass (not in the PREREG).** The page was settled in two halves (L1-L21, L22-L41) by two blind
  arbiters; a further blind subagent then made the two halves use one label for each shape (`texts/f71_signs.txt`, header and Notes).
  This changed **71 signs** in substance (ET 17, @N01 17, de 12, da 8, @N03 9, diamstem 6, dumb 2) plus 29 pure renumberings of new
  shapes; no sign added or removed, nothing else re-read. It was done before f. 70 was opened and before any decoding, without key
  or values, but the PREREG did not provide for it. The two arbitrated halves before harmonisation are in `texts/f71_passes/`.
- **f. 35, passes.** The PREREG planned pass A by the lead agent; since that agent knew the key, both passes (B, C) and the settling
  were given to blind subagents instead.
- **f. 353, portion.** Runs R2 (83 signs) and R3 (1) have no counterpart in the copy f. 352 and were removed before decoding, as the
  PREREG provides (`texts/f353_signs_portion.txt`).

## Where the errors are (after the measurements; no change made to any key or transcription)
- **f. 71:** the decode follows the period decipherment almost word for word. Main losses: `ss` (б) is s or p and the two are not
  separated ("sraticato", "srestanza"); one sign valued ga where the sense wants h ("gaavere"); `htall` valued bi where the sense
  wants ra ("delibebit..."). f. 70 also leaves out the opening "Signore" and the last sentence of the cipher, which count against the score.
- **f. 353:** `CLOVER iI` read where the sign is the trefoil without a cross (`pe`, so "per"), `hookl` = re in this letter, the
  loops-and-cross sign = Sig. Federico (a separate sign from Sig. Sigismondo), "Signore" unvalued, copyist's blanks.
- **f. 35:** the crosswalk lacked values for the looped `<` (10 times, Re de Ragona on R5318), `rb` (13) and others; VEN = duca on
  R5318 where 1448 has Venetiani.

## Files
- `K3_key.tsv`, `sign_legend_K3.md` (shapes only), `HASHES-1317-K3.txt`, `PREREG-AMENDEMENT-1317-K3.md` (+ `.en.md`), `planche/DECISIONS-K3.md`.
- `K2_key.tsv`, `sign_legend_K2.md`, `HASHES-1317-K2.txt`, `PREREG-AMENDEMENT-1317-K2.md` (+ `.en.md`).
- `HASHES-1317.txt`, `PREREG-AMENDEMENT-1317.md` (+ `.en.md`) for f. 35 (key: `../../r5318/key_R5318_by_1448_label.tsv`, the
  translated copy of the frozen French crosswalk 04c8ae96..., same values).
- `texts/`: settled transcriptions `f35_signs.txt`, `f353_signs.txt` (+ `f353_signs_portion.txt`), `f71_signs.txt` (=
  `f71_signs_portion.txt`); passes `f35_passB.txt`, `f35_passC.txt`, `f353_passes/`, `f71_passes/`; references `f34_36_reference.txt`,
  `f352_reference.txt`, `f70_reference.txt`, `f70_transcription.txt`.
- `measure_f35.py` (run it through `run_f35.py`, which only points it at the key's path in this repository), `measure_f353.py`
  (`python3 measure_f353.py texts/f353_signs_portion.txt texts/f352_reference.txt`), `measure_f71.py`; outputs `results_f35.json`,
  `results_f353.json`, `results_f71.json` (all three re-run here and identical).
- Paths in the HASHES files are those of the working folders (the passes were hashed where they were written; the same files are
  here). The key-building scripts (`k2/`, `k3/`, hashed in the HASHES files) depend on local working paths and are not included;
  they only align the training letters with their clears to count values.

## Prior art
The plaintexts are known (above). Not checked: Cerioni 1970 (the Sforza cipher keys), which may print the key.
