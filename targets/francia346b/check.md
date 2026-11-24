# Checks: Francia 346 alternate key (R5634, R5638, R5639)

## 1. Frozen ciphertext-only provenance

- The key (`key.tsv`, 59 codes), all six transcription files, and the initial working readings were committed to `prabal-rje/branicki-1757` at commit `681ed424180eb3690b2fd33928fce4de9ace553d` on `2026-11-22 21:34:50 -0500` (`2026-11-23T02:34:50Z`), before opening, copying, or checking against any clerk's decipherment on `R5634`, `R5638`, or `R5639`.
- Exact SHA-256 digests of both the frozen `branicki-1757` blobs and the files in this folder are listed in `FROZEN.sha256`.

## 2. Reproducible mechanical decode (`scripts/decode.py`)

Running `python3 targets/francia346b/scripts/decode.py` reproduces every decode row in `r5634.md`, `r5638.md`, and `r5639.md` strictly from `key.tsv` and `transcription/` with zero external language model and zero manual post-editing:

| Record | Folios | Rows | Digits | Code units | Letters | Nulls | Unread gaps |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `R5634` | ff. 190r to 190v | 23 | 1211 | 679 | 557 | 122 | 54 |
| `R5638` | ff. 218r to 218v | 33 | 2874 | 1514 | 1361 | 153 | 16 |
| `R5639` | ff. 220r to 220v | 30 | 2335 | 1237 | 1103 | 134 | 57 |
| **Total** | **6 pages** | **86** | **6420** | **3430** | **3021** | **409** | **127** |

## 3. Test that the published Ceva key does not fit R5634, R5638, or R5639 (`scripts/test_ceva_mismatch.py`)

Evaluated with an Italian character 4-gram model and >=5-letter Italian word coverage built directly from `lang/lexicons/it.json.gz`, comparing the published Ceva key (`targets/francia346/key-and-key-free-read/key.tsv`) against this folder's `key.tsv` and 100 digit-shuffled ciphertext controls (holding each key fixed to preserve key-output vowel frequency), with `R5635` (`targets/francia346/transcription/R5635_f205r_digits.txt`) as a positive control where the Ceva key fits:

| Record | Digits | Ceva LM4 vs digit-shuffle null (Z) | Ceva >=5-ltr word cov | Alt-key LM4 vs digit-shuffle null (Z) | Alt >=5-ltr word cov |
| --- | ---: | ---: | ---: | ---: | ---: |
| R5635 (Ceva control) | 1077 | -3.446 vs -3.790 +/- 0.078 (Z=+4.4) | 23.1% | -4.390 vs -4.415 +/- 0.093 (Z=+0.3) | 0.0% |
| R5634 | 1211 | -3.554 vs -3.865 +/- 0.091 (Z=+3.4) | 14.4% | -3.285 vs -4.328 +/- 0.074 (Z=+14.1) | 19.7% |
| R5638 | 2874 | -3.417 vs -3.859 +/- 0.052 (Z=+8.5) | 4.1% | -2.848 vs -4.242 +/- 0.050 (Z=+28.0) | 45.3% |
| R5639 | 2335 | -3.323 vs -3.822 +/- 0.054 (Z=+9.3) | 8.2% | -2.865 vs -4.228 +/- 0.048 (Z=+28.2) | 42.5% |

The test shows a clean double dissociation:

- On positive control `R5635`, the published Ceva key gives `23.1%` >=5-letter Italian word coverage (`LM4 = -3.446`, `Z = +4.4` over digit-shuffled controls), while `targets/francia346b/key.tsv` drops to `0.0%` word coverage (`LM4 = -4.390`, `Z = +0.3`, noise).
- On `R5638` and `R5639`, the published Ceva key drops to `4.1%` and `8.2%` word coverage (`LM4 = -3.417` and `-3.323`), while `targets/francia346b/key.tsv` jumps to `45.3%` and `42.5%` word coverage (`LM4 = -2.848` and `-2.865`, `Z = +28.0` and `+28.2`). On shorter, gap-heavy `R5634`, `targets/francia346b/key.tsv` scores `-3.285` (`Z = +14.1`, `19.7%` word coverage) vs. Ceva `-3.554` (`14.4%`). (The mild residual Ceva LM4 offset above shuffled digits comes from one shared code value, `18 = e`, and Ceva's fixed two-digit Italian syllables; all other core codes differ, e.g. `17=a` vs. Ceva `i`, `55=i` vs. Ceva `chi`, `44=s` vs. Ceva `che`, `36=o` vs. Ceva open.)

## 4. Not checked yet

- The machine transcriptions in `transcription/` have not been verified digit-by-digit by a human against the DECODE scans.
- The contemporary clerk's decipherments on the leaves of `R5634`, `R5638`, and `R5639` have not been opened or compared against this decode.
