# Audit of catalogue entries promoted from leads 2538-2831 (15 Nov 2026)

Bar: ciphertext seen, and no decipherment of this text on or with it. A key held or filed in the volume does not
disqualify (3 Nov rule); a filed decipherment of the same text means there is nothing open to solve.
There is no demote command in `docs/_check_catalogue.py`, so the 13 entries below were moved from `catalogue.json` to
`research/leads.json` with ids unchanged, `vetting.verdict` = `read` (nearest existing value) and a `vetting.closed`
note starting "decipherment_filed". All 79 promoted entries of 2538-2831 were read; the others stay.

## Demoted (decipherment filed with the same text)

| id | reason |
|---|---|
| 2585 | Neuchatel Nr. 695: reports 'teils chiffriert mit Entzifferung', Entzifferung filed in the volume |
| 2599 | Rep. 81 Dresden Nr. 782: each cipher order 'mit Aufloesung in franzoesischer Sprache' |
| 2600 | Rep. 81 Dresden Nr. 798: both letters 'mit Aufloesung' |
| 2612 | Neuchatel Nr. 952: 'mit gleichzeitiger Entschluesselung' |
| 2614 | Neuchatel Nr. 749: 'mit gleichzeitiger Entzifferung' |
| 2615 | Neuchatel Nr. 855: 'chiffrierten und entzifferten Berichten' of Goltz |
| 2617 | Rep. 81 Frankfurt Nr. 173: 'chiffrierte Schreiben mit Aufloesung' |
| 2626 | OBA 23682: 'Original in Chiffern; mit Aufloesung' |
| 2627 | OBA 27533: cipher letter 'mit Aufloesung' |
| 2652 | Wuerttemberg Bue 124 / 129: 'mit Aufl.' / 'mit Dechiffrierung' |
| 2670 | Dundas papers: the cypher copy is a copy of the clear memorandum in the same folder |
| 2677 | HHStA Busbecq 6 Aug 1559: interlinear decipherment on the sheet |
| 2819 | OeNB Maximilian-Dupont telegrams: contemporary solution written on each sheet |

## Kept, with the rationale recorded in `vetting.audit_note` (case b: partial, key only, or narrowed)

| id | reason |
|---|---|
| 2538 | decipherment covers 14 of 29 letters; entry narrowed to the 15 despatch-only letters (the 14 pairs are the crib) |
| 2539 | already narrowed 12 Nov to pieces not read in the Friedrich Wilhelm target |
| 2616 | archive does not say a decipherment is filed (unlike 2615) |
| 2646, 2647 | clerk's overwritten letters/words are a partial per-symbol reading, no full plaintext written out |
| 2661-2663, 2808, 2753, 2754, 2758 | a key is filed or held, but no decipherment of the ciphertext is recorded |
| 2773 | already narrowed to the 20 letters without a 'Decryptage' piece |
| 2788 | the one interlinear letter (SP 46/146/63-64) is excluded and kept as the crib |

The other kept entries (2541-2543, 2547, 2553, 2564-2566, 2575, 2577, 2580, 2582, 2583, 2628-2645, 2649, 2664,
2666, 2668, 2675, 2676, 2694, 2695, 2713, 2716, 2732, 2746, 2774, 2775, 2784, 2792, 2797, 2815-2818) mention no filed
decipherment of their text (2675 'nincs feloldva', 2676 only the date solved).

Not checked: the generated pages `docs/solve/<id>.html` and search shards for the 13 demoted ids; the rebuild
workflow regenerates them from `catalogue.json`.
