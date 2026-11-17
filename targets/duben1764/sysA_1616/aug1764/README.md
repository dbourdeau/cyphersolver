# duben1764, system A: key_c02 tested once on the 20/31 August 1764 letter (pre-registered): FAIL at the 0.85 bar

Work of 17 Nov 2026 (Brice Dudout's session, Claude Opus 5.5, AI agent). Riksarkivet K 259 (IIIF A0073297), images 111R-117.
Text files only; images on the Riksarkivet IIIF server (`https://lbiiif.riksarkivet.se/arkis!A0073297_NNNNN/full/max/0/default.jpg`).

| file | what it is |
|---|---|
| `PREREG.md`, `SHA256SUMS-PREREG`, `SHA256SUMS-PREREG.time` | the plan, frozen with the key before any transcription or decode of this letter; Amendment 1 (block rule, after a look at reduced images), Amendment 2 (transcriptions frozen, block chosen) |
| (hash note) | the first `aug1764/PREREG.md` line of `SHA256SUMS-PREREG` is the text before the amendments, as committed in 75db2c7b1 (check from `sysA_1616/` on that commit); the last line (`PREREG.md`, run from `aug1764/`) is the text with Amendment 1; `SHA256SUMS-AMEND2` holds the final text |
| `SHA256SUMS-AMEND2` | hashes of the PREREG with both amendments and of the two frozen transcriptions |
| `scripts/measure_aug.py` | the one measure (frozen in the PREREG) |
| `transcr/aug1764_cipher_merged.txt` | the cipher, 51 number lines (112L 15, 112R top 6, 114R 15, 115 15), 1,019 groups of 100 or above (the figure "54" in Amendment 2 is wrong; the frozen file itself is unchanged) |
| `transcr/aug1764_clear_116-117.txt` | the contemporary decipherment on 116-117 (40 lines, 2,279 letters) |
| `transcr/passes/`, `transcr/disagreements_aug.txt` | pass 1 (this session) and pass 2 (blind sub-agent), and the 23 differences with their arbitration |
| `outputs/measure_result.json`, `outputs/measure_result_full.txt` | the result as printed, and the decode string |

## The letter
111R: "St Petersbourg le 20/31 Aout 1764. Mon tres cher Comte, Votre lettre du 3 de ce mois m'a fait un chagrin bien
sensible ..." in clear; the cipher follows on 112L (15 lines) and the top of 112R (6 lines); the clear then resumes on
112R ("J'ai appris avec la plus grande satisfaction ...") and ends on 113L, signed "Düben". 114R and 115 (15 + 15 lines)
are a further cipher sheet. The clear 116-117 (archival note "Till chifferbrevet av 20/31 aug. 1764") begins "Je n'ai
jamais osé garantir la sincérité des dispositions de Sa Majesté l'Impératrice" with no salutation.
No part of this letter, cipher or clear, had been transcribed or measured before (repository, all PRs and issues, and our
own files checked on 17 Nov 2026).

## Pre-registered result (run once)
| | value |
|---|---|
| groups >= 100 | 1,019 (key_c02 covers 93.3 %) |
| **CA** (share of decoded letters in matching blocks of >= 4 letters with the clear) | **0.831** |
| best of 200 permuted-key controls | 0.078 (mean 0.045) |
| M (share of clear letters covered, the check2.py metric) | 0.745 (controls max 0.084) |
| bar | CA >= 0.85 and CA >= controls max + 0.30 |
| **verdict** | **FAIL** (the second condition holds by 0.75; the first misses by 0.019) |

The verdict stands. The portion is burnt for any later key test.

## After the measure (not part of the test)
- The decode shows why CA is lower than the in-sample values: the frozen file follows the binding order (112L, 112R, 114R,
  115), but the text runs 112L -> 114R -> 115 -> 112R (the six lines at the top of 112R are the end of the decipherment,
  "... lui témoigner mon respectueux attachement ... très humbles et très soumis remerciments"). The block rule of
  Amendment 1 chose the right material (B1+B2, r = 2.24) but the PREREG fixed no reading order. Re-scored in the order
  112L, 114R, 115, 112R, the same key gives CA 0.938 (controls max 0.071) and key_c01 0.762; these numbers were made after
  the result was seen and are not a test.
- So 114R-115 is not an enclosure but the middle of the same enciphered passage; the clear 116-117 deciphers all of it.
- Reading of this letter is therefore from its contemporary decipherment (existing decipherment); no strict count or
  translation is made here.

## Limits
Transcriptions by AI agents (two passes, the second blind), not checked by a palaeographer. key_c02 includes about 48
values read by sense in 90R-93L (see `../keyc02/`); the measure is the only independent check of them, and it is a fail at
the pre-registered bar.

## Corrections after review (17 Nov 2026, later)
- Line count: the merged cipher has **51** number lines (112L 15, 112R 6, 114R 15, 115 15), not 54 as written in Amendment 2 and in an
  earlier version of this README. Amendment 2 is hashed and is left as it was; this note corrects it.
- Reading order: in effect the first PREREG (with its Amendment 1) bound the test to the binding order of the pages (112L, 112R, 114R,
  115), and that order was wrong: the text runs 112L -> 114R -> 115 -> 112R. The FAIL above is the result under that wrong order and
  stands. `../may1764/PREREG-C02b.md` is the **second** pre-registered test of the same, unchanged key_c02, on another letter, with the
  reading order fixed first from material evidence; it passed (CA 0.916 vs controls max 0.077).
- Normalisation: 90R-93L was normalised (370/420/580 -> 373/423/583) because in that letter the scribe's open 3 recurs in the same
  frequent groups and was read as 0 in pass 1; the August and May files keep what was written (open 3 read as 3 at transcription, no
  normalisation step), so that their frozen text is the raw reading.
