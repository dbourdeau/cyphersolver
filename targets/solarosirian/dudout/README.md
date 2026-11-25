# solarosirian — working files of the contributor's attempt (C13)

These are the files of our single pre-registered measurement (16 Nov 2026), copied byte for byte from our working folder so that anyone can recompute the SHA-256 values and M. They are in French, as written at the time. No image or crop of the IFAO plates is included: the transcription is in sign codes (Gardiner where possible, named classes otherwise).

## frozen/ (frozen before the measurement)
- `PREREG-C13.md`: the pre-registration (frozen first). `PREREG-C13.sha256`: the frozen hashes. Its paths are those of our working folder: `working/c13/X` = `frozen/X`, `cryptanalysis/c13/X.py` = `scripts/X.py`. All 12 hashes match the files here.
- `AVENANT-1-C13.md`: the one amendment, frozen before the measurement.
- `table-v5.json`: the frozen sign table used for the measurement.
- `transcription-passe1.json`, `transcription-passe2-api.json`, `transcription-arbitree.json`: the two model transcription passes and the arbitrated transcription of the held-out portion (sign codes).
- `lecture-aveugle-C13.md`, `decodage-mecanique.md`: the blind reading and the mechanical decoding, frozen before the published reading was opened.
- `reference.json`: the reference alignment (unit by unit, after Darnell & Darnell 2018 and Piankoff 1952; short labels only).
- `table-v6.json` (SHA-256 474875ec…): a later table (C14) built mechanically from v5. It was **not measured**: the only held-out portion is used up.

## scripts/
`measure_c13.py` (the measuring script), `pass1.py`, `arbitrage.py`, `decode_c13.py`, `compare_passes.py`. Measurement, from our working folder: `python3 -I cryptanalysis/c13/measure_c13.py working/c13/table-v5.json transcription-arbitree.json reference.json mesure.json`.

## results/
- `mesure.json`, `mesure-C13.md`: the measurement (M = 27/65 = 0.415 against the bar of 0.454).
- `fiche-lecture-C13.md`: the unit sheet (sure / probable / restored / unresolved, by Daniel's rule).
- `RELECTURE-BRICE-PLANCHE.md`: Brice Dudout's blind shape check of 12 doubtful signs (8 neither shape, 1 agrees, 3 do not).
