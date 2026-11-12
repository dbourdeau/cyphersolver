# Validation of the "Clave G.A." card against decipherments of the time (12 Nov 2026)

Brice Dudout, with Claude (Opus) as the model. One preregistered measure, run once.

## Question and logic

The card in `key.tsv` is the archive's own key (CMXV.16.1557.1, scans 12-13). Telegram CMXV.15.1432.1-4 has no decipherment on the sheet and is absent from the typed list of decipherments CMXV.18.1795.1, so its reading cannot be checked against a clear of the time. The card is therefore tested on sibling telegrams of the same San Antonio - El Paso traffic (March-April 1911) whose clear WAS written at the time (pencil glosses over the coded words, the same text as in 1795.1). If the card, applied as transcribed and unchanged, reproduces those clears on at least 300 cipher letters, it is validated as the key of this traffic, and the reading of 1432.1-4 stands on a validated key.

## Protocol (fixed and hashed before any decoding)

- Cipher text transcribed blind: the scans were filtered so that only the violet typewriter ink was kept and the grey pencil glosses were erased; the glosses were not looked at before the cipher transcription was hashed. One telegram (CMXV.14.1363.1-2, neutral ink) could not be masked, its gloss was seen, and it was dropped. Doubtful letters were left as "?" (never counted as agreeing).
- Period clear transcribed afterwards, from the pencil glosses (1795.1 gives the same text; where 1795.1 substitutes an editorial word, e.g. "Madero" for the gloss "Dr", the gloss was kept), and hashed.
- Inclusion filter using no clear and no body value of the card: a telegram enters if at least 80% of its cipher letters form pairs of the card's shape (row letter + column letter).
- Statistic A = sum over segments of (max(|D|,|R|) - Levenshtein(D,R)) / sum of max(|D|,|R|), D = mechanical decryption with the card, R = period clear (a-z).
- Controls (seed 1462): 200 tables with the card's body values permuted among the cells, and 200 texts with the order of the cipher pairs shuffled within each segment (decrypted with the true card).
- Thresholds declared in advance: validated if A >= 0.85, A - best control >= 0.30, and at least 300 cipher letters.

SHA-256 of the frozen files (kept in the working folder, not in this repository): preregistration amendment 35805084842e269b9322bdbb1408df467881fcd8268e7bddd90f636cbde2e7d1; measuring script 15c404f47cca1a21268cedbdd6e0583a82da323d3984abfa9e36dc325bcc8429; blind cipher transcription a97a76fcd7d6ad0ed3a70e011b9dfe52e313bdf313268128684bcff2d35a6ec1; period clear 1d1b7b019eb29d3bfc456fb671e0ce435a1b4155cb0191b9e1e385d91bf1b4e3; card transcription (made the day before) 1a00b607279291d02efcf1d18a14058baad1fcdfc12c937b52cccfebbfe9a2e0.

## Result

**Validated: A = 0.866 on 769 cipher letters (28 segments, 8 telegrams); best of 400 controls 0.257 (permuted tables: max 0.147, mean 0.078; shuffled text: max 0.257, mean 0.218); margin +0.609.**

| Telegram (CEHM-Carso) | cipher letters | card-shaped pairs | included |
|---|---|---|---|
| CMXV.14.1363.2-2 | 176 | 0.932 | yes |
| CMXV.14.1392.1-2 | 104 | 0.981 | yes |
| CMXV.14.1404.4-4 | 82 | 0.951 | yes |
| CMXV.14.1411.4-4 | 158 | 0.987 | yes |
| CMXV.15.1458.4-6 | 48 | 0.917 | yes |
| CMXV.15.1462.1-2 | 50 | 0.920 | yes |
| CMXV.15.1489.4-7 | 123 | 0.878 | yes |
| CMXV.16.1516.2-2 | 28 | 0.929 | yes |
| CMXV.16.1561.3-13 | 127 | 0.378 | no (another system) |

Segment by segment (decryption with the card as is / clear of the time / edit distance):

| Telegram | decryption with the card | clear of the time | distance |
|---|---|---|---|
| CMXV.14.1363.2-2 | youngdeshaftxr | youngdeshafter | 1 |
| CMXV.14.1363.2-2 | remitiera | remitiera | 0 |
| CMXV.14.1363.2-2 | suconducto | suconducto | 0 |
| CMXV.14.1363.2-2 | arregladoyremitireci??comiltr??inta??r??i????a | arregladoyremitirecincomiltreintatreinta | 12 |
| CMXV.14.1363.2-2 | cuarentaycuatro | cuarentaycuatro | 0 |
| CMXV.14.1392.1-2 | proveyr | proveer | 1 |
| CMXV.14.1392.1-2 | dr | dr | 0 |
| CMXV.14.1392.1-2 | hastadosmilquinientos | hastadosmilquinientos | 0 |
| CMXV.14.1392.1-2 | cuantodesearemita??ehoy | cuantodesearemitalehoy | 2 |
| CMXV.14.1404.4-4 | felienemi | felixnemi | 1 |
| CMXV.14.1404.4-4 | presidi?? | presidio | 2 |
| CMXV.14.1404.4-4 | consigparlecinco??iltiros | consignarlecincomiltiros | 3 |
| CMXV.14.1411.4-4 | cienm | cienmil | 2 |
| CMXV.14.1411.4-4 | diez | diez | 0 |
| CMXV.14.1411.4-4 | economiceensurtiraldryasanc??ez | economiceensurtiraldryasanchez | 2 |
| CMXV.14.1411.4-4 | sheltonypayne | sheltonypayne | 0 |
| CMXV.14.1411.4-4 | selescubrirnremesa | selescubriraremesa | 1 |
| CMXV.14.1411.4-4 | valentine | valentine | 0 |
| CMXV.15.1458.4-6 | migueldiabold | migueldiabold | 0 |
| CMXV.15.1458.4-6 | lare??o | laredo | 2 |
| CMXV.15.1458.4-6 | ma??ar | matar | 2 |
| CMXV.15.1462.1-2 | refuerzosfedera??es | refuerzosfederales | 2 |
| CMXV.15.1462.1-2 | ojin??ga | ojinaga | 2 |
| CMXV.15.1489.4-7 | de????acamentodu??anaosinmuniciones | destacamentodurangosinmuniciones | 7 |
| CMXV.15.1489.4-7 | repyie?auen | replieguen | 3 |
| CMXV.15.1489.4-7 | co????eosde????acamento | correosdestacamento | 8 |
| CMXV.16.1516.2-2 | ojina??a | ojinaga | 2 |
| CMXV.16.1516.2-2 | escasos | escasos | 0 |

Most "?" come from single wrong or dropped letters in the typed telegrams (a dropped letter breaks the pairing until the next pair). CMXV.15.1489.4-7 agrees least. These remarks were made after the measure; nothing was changed in the card or in the transcriptions.

## What this does not check

- The card transcription is ours (CEHM image, scans 12-13), not checked by a second reader; the measure shows it reproduces the period decipherments as it stands.
- No one outside the project has compared the transcriptions with the scans. The CEHM images are study copies and are not redistributed here.
