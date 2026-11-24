# Francia 346, alternate digit key: R5634, R5638, and R5639

Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346. DECODE records `R5634` (ff. 190r to 190v), `R5638` (ff. 218r to 218v), and `R5639` (ff. 220r to 220v), from catalogue entry `880`.

- **State:** decoded, not read; cipher words not counted.
- **Method:** key recovered from ciphertext alone (`key.tsv`, 59 codes: 18 core firm two-digit letters, homophones, 8 single-digit nulls, 2 two-digit nulls, and tentative rare codes), frozen on 22 November 2026 (`branicki-1757` commit `681ed424`, SHA-256 in `FROZEN.sha256`) before opening any clerk's decipherment on these leaves.
- **Separate key from Ceva (`targets/francia346` / `targets/ceva1632`):** `scripts/test_ceva_mismatch.py` demonstrates on `lang/lexicons/it.json.gz` that the published Ceva key fits control `R5635` and fails on `R5634`, `R5638`, and `R5639`, whereas `key.tsv` fits `R5634`, `R5638`, and `R5639` (`Z = +14.1` to `+28.2` over 100 digit-shuffled controls; `45.3%` and `42.5%` >=5-letter Italian word coverage on R5638 and R5639 vs. `4.1%` and `8.2%` under Ceva) and fails on `R5635`.

## Records

| Record | DECODE | Folios | Rows | Digits | Letters | Nulls | Gaps | State |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [R5634](r5634.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/5634) | ff. 190r to 190v | 23 | 1211 | 557 | 122 | 54 | decoded, not read; cipher words not counted |
| [R5638](r5638.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/5638) | ff. 218r to 218v | 33 | 2874 | 1361 | 153 | 16 | decoded, not read; cipher words not counted |
| [R5639](r5639.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/5639) | ff. 220r to 220v | 30 | 2335 | 1103 | 134 | 57 | decoded, not read; cipher words not counted |

## Files

- `transcription/`: six cipher-row files (my own machine transcription of the DECODE images; no DECODE image is published).
- `key.tsv`: 59 codes with `source`, `count`, `grade` (`firm`, `probable`, `tentative`), and `note`.
- `r5634.md`, `r5638.md`, `r5639.md`: unedited mechanical decode row by row from `scripts/decode.py`, apart from any reading.
- `FROZEN.sha256`: SHA-256 digests and commit timestamp (`branicki-1757` commit `681ed424`, `2026-11-22 21:34:50 UTC-5`).
- `scripts/decode.py`: reproduces the mechanical decode directly from `key.tsv` and `transcription/`.
- `scripts/test_ceva_mismatch.py`: reproduces the Ceva mismatch test with `R5635` control and 100 shuffled-key nulls.
- `check.md`, `NOTES.md`, `profile.json`: checks, gaps, escalation, and fixed-field profile.
