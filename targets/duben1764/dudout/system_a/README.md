# duben1764, system A: key_c01 and the scripts behind issue #437 (Brice Dudout, Europe chiffrée)

Riksarkivet A0073297 (Lovisa Ulrika's papers, C. W. von Düben's cipher letters, 1764-65). Text files only, no images.
Transcriptions by one reader (a Claude Opus agent); not checked by a palaeographer.

## What is here
| file | what it is |
|---|---|
| `PROTOCOLE.md` | the plan written on 27 Oct 2026, 02:20 CET, before any decoding (French, left as frozen) |
| `transcr/i096.txt`, `transcr/i097g.txt` | cipher of image 96 + 97 left (the letter that begins `15.73.100.347.503.401.107.536`) |
| `clears/L096_clear_contemporary.txt` | its contemporary decipherment, images 97 right + 98 left + 99 left (archivist's note on 97: "Hör till chiffreringen 15.73.100.347.503.401.107.536") |
| `anchors_c01.json` | the 28 hand anchors for the alignment |
| `scripts/align_em.py` | anchored EM alignment of cipher groups to the clear; produces the group -> value model |
| `key_c01.json` | the key: 217 groups -> value (one-part syllabic nomenclator, homophones, nulls < 100), built from 96/97 only |
| `transcr/i101d.txt`, `clears/L101_clear_contemporary.txt` | the held-out letter (101 right, 6 Mar 1764) and its clear (102 right), used only to measure |
| `validation/val_L101.*`, `validation/controls/` | the 27 Oct check on 101 right: 178 of 232 known groups agree (0.767); three permuted keys 0.224-0.254 |
| `scripts/decode.py` | decodes one of our transcriptions with the key |
| `scripts/check2.py` | the issue #437 check on YOUR files `tx/*.txt`: decodes groups >= 100, scores the share of clear letters covered by matching blocks of >= 4 letters (difflib), 200 permuted-value controls (seed 1616) |
| `scripts/check.py`, `scripts/dec.py` | the line-by-line raw decode shown in the issue |
| `outputs/` | raw decode of 15 Nov 1765 and the two diagnostics |

## Re-run (14 Nov 2026, from the repository root, nothing changed in the key)
```
python3 targets/duben1764/dudout/system_a/scripts/check2.py targets/duben1764/dudout/system_a/key_c01.json targets/duben1764/tx/g1765-11-15.txt targets/duben1764/tx/g_p.txt
groups: 704 cov 0.776 clear letters 1525 real 0.545 ctrl max 0.061 mean 0.037
python3 targets/duben1764/dudout/system_a/scripts/check2.py targets/duben1764/dudout/system_a/key_c01.json targets/duben1764/tx/c1764-03-06.txt targets/duben1764/tx/p1764-03-06.txt
groups: 605 cov 0.807 clear letters 2910 real 0.261 ctrl max 0.043 mean 0.025
```
(The issue said 703 groups / 0.544 for 1765; the re-run on the current `tx` gives 704 / 0.545.)
The 1764 score is low because the clear 102R-103R is about 2.6 times longer than the cipher on 101R-102L.

## Limits
- The key is partial (about 220 values of a repertory of perhaps 700); some values are cut badly by the alignment ("limp", "kie").
- The 1765 gloss runs one to three lines ahead of the cipher, so a positional comparison is not possible; the score is order-free within blocks.
- Nothing here is claimed as a new reading: both system A letters were deciphered at the time.

Licence CC BY 4.0. SHA-256 of every file in `SHA256SUMS`; `key_c01.json` is 3fcecea8afc3f0e8... as frozen on 27 Oct 2026.
