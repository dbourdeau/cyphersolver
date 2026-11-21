# Charles II to the conde de Fuensalida, governor of Milan, 1688 and 1690 — AHNOB FRIAS,C.61,D.106-162 (PARES 3962172, 3962173)

Status: read in part (decoded, read in part, key not validated: the one letter of 1688 filed without translation decodes to sense with a key that failed every preregistered held-out test at the 0.85 bar; no figure here is a validated reading).

## Documents
The two PARES units hold the cipher letters of Charles II's Secretariat of State (countersigned Don Alonso Carnero) to the
conde de Fuensalida. Almost every letter is filed as cipher, blank verso, address, and a period **traducción** (the
decipherment). The cover note of the 19th-century archivist (3962172, images 1-2) says all the letters come with their
translation except one of 25 November 1688 ("lugares esguízaros"). The cover of the second unit (image 6) says four have
no translation, three of 9 November and one of 30 November, and that their content is summarised on the back.
* PARES dates both units 1688, but **3962173 (D.137-162) is of 1690** (letters of 26 Oct, 9 Nov, 30 Nov and 31 Dec 1690).
* **D.141** (9 Nov 1690, duplicate, winter quarters of the imperial troops in Piedmont) has its period translation in
  the same unit (images 19-20, stamped FRIAS 61/144). It is **existing**, and we use it only as a test pair. Our earlier
  provisional reading had two sense errors that the translation corrects ("del Monferrato", "en este tiempo").
* **25 Nov 1688** (3962172 image 62, Buen Retiro), the letter without translation, is the target read here (exploratory).
* **30 Nov 1690** (3962173 images 25-26, address no. 146), in the same system without translation, is decoded only.
  Images 28-29 ("Dais quenta en carta de 20...") are not its translation.
* D.139, D.140 and images 14, 15, 21 of 3962173 (9 Nov 1690) use **another system**, a code of 3-digit groups only. It is
  not treated here.

## The cipher
The system mixes four elements. (1) A nomenclator of 3-digit code words (101-964: 120 Duque, 189 Rey, 306 Saboya,
344 carta, 333 orden ...), sometimes followed by 34 (a mark) or f (plural s); the codes are grouped by initial letter,
with no order inside a group. (2) Numbers of 1-2 digits for letters and syllables, with homophones. (3) Vowel + letter pairs
with a substituted consonant (as da, ey se, ob lo, en re, ex ne, al ga; ez el, az al; eʃ es/er/os). (4) Punctuation and
null groups. Three hands write it: A (barred figures, long ʃ), B (no bars, "es") and C (z, y, v, iy). The same key runs from
4 Mar 1688 to 31 Dec 1690. `K5.tsv` has 347 entries.

## Prior art
No target, lead, PR or issue on Fuensalida or FRIAS C.61 in this repository (checked 3, 14 and 17 Nov 2026). The bundle
appears only as a pointer in research/pares_ags. The 25 Nov 1688 letter has no known translation, period or modern.

## Measurements (each preregistered and frozen by SHA-256; the held-out cipher was sealed and decoded before its translation was opened; 200 value-permuted controls, seed 1688)
| Key | Held-out pair | Characters | Words | Best control (chars / words) | Verdict |
|---|---|---|---|---|---|
| K1 | D.137 / D.138 (26 Oct 1690) | 0.627 | 0.506 | 0.569 / 0.157 | below the original criterion (words >= 0.60) |
| K2 | D.112 / D.113 (18 Mar 1688) | 0.768 | 0.636 | 0.608 / 0.171 | met the original words criterion; below the 0.85 character bar adopted on 30 Oct |
| K3 | D.130 / D.131 (28 Oct 1688, hand C) | 0.733 | 0.540 | 0.623 / 0.150 | **not validated** |
| K3 | D.141 / D.144 (9 Nov 1690) | **0.789** | 0.619 | 0.668 / 0.153 | **not validated** (0.789 < 0.85) |
| K4 | D.132 / D.133 (10 Nov 1688) | 0.786 | 0.636 | 0.631 / 0.182 | **not validated** |
| K4 | images 58-59 / 61-62 (31 Dec 1690, one blind pass) | **0.738** | 0.513 | 0.645 / 0.152 | **not validated** (0.738 < 0.85) |
| K5 | images 36-37 / 39 (30 Nov 1690) | 0.899 | 0.801 | 0.703 / 0.180 | **not validated**: >= 0.85, but below the preregistered margin (best control + 0.30 = 1.003) |

Every key ranked first of 201, but none passed the bar ">= 0.85 characters and >= best control + 0.30". After the K5 test
we found, on used-up pairs only, that the value-permuted controls decode to text about 2.25 times longer than the clear.
The character score is a recall, so it rises with length, and unrelated Spanish of the same length scores 0.66-0.72. A
margin of +0.30 in characters therefore cannot be reached with this control. We wrote a revised prereg (characters >= 0.85,
words >= best control + 0.30, letter precision >= 0.85) before seeing any new image. The next bundle searched (PARES
3962184, FRIAS C.60) holds only clear originals, so the revised test has **not been run**. The K5 result stands as "not
validated".

## Reading of 25 Nov 1688 (`reading/`, exploratory)
The cipher was transcribed in two blind passes (148/148 tokens, agreement 0.905) and the differences were settled on the
image. With K5: 62 words, 54 sure, 8 probable, none unread. With K4, earlier and on one pass: 63 words, 50 sure,
10 probable, 1 supplied, 2 unread (95.2%). The text: in reply to Fuensalida's letter of the 11th of the previous month,
which enclosed the Prince-Abbot of Saint Gall's letter to Count Casati about the French seizing and sacking some Swiss
places, the King approves what Fuensalida has done and asks to be kept informed of the negotiation and of the French
negotiations. This agrees with the archivist's "lugares esguízaros". The key is not validated, so the reading is
exploratory and is **not** claimed as "read".

## Remaining gaps
- 30 Nov 1690 (3962173 images 25-26), 29 of 152 words - blocker: open-codes; codes 335, 357, 103, 460, 44, 667, 607 unknown; two blind passes, disagreements not yet settled on the image; decoded with K5 to 80.9% (exploratory).
- validation of K5 on a fresh cipher / translation pair of 300+ tokens - blocker: needs-physical-access; no unused pair is left in 3962172 or 3962173, 3962184 holds only clear originals, and the other units of "Funciones militares" (3962171: 3962187, 3962185, 3962174 ... in the order fixed by the revised prereg) still have to be opened on PARES.

Not part of this target: the second system (3-digit code, D.139, D.140, images 14, 15, 21 of 3962173). Only the dorsal
summaries are a crib for it, and it is not attacked here.

## Escalation
- [x] siblings: every image of 3962172 (1-69) and 3962173 (1-65) opened; 3962184 (FRIAS C.60) opened; 3962171's other units listed.
- [x] clear-pages: every traducción paired with its cipher; this found D.141's translation (D.144) and showed that images 28-29 are not the translation of images 25-26.
- [n/a] known-keys: no published key of Carnero's secretariat cipher is known to us; the key was rebuilt from 23 period cipher / translation pairs instead.
- [n/a] print: no edition of the Charles II - Fuensalida correspondence is known to us; the search went no further than this repository and the PARES notes.
- [x] key-rebuild: K1-K5 by alignment on the period pairs, K5 by hard-EM / DP alignment over 23 pairs, leave-one-pair-out 0.84-0.87.
- [x] retry: 25 Nov 1688 re-read with K5 on two blind passes; 30 Nov 1690 decoded with K5.

## Files
* `transcription/c62_25nov1688_cipher.txt` (arbitrated) and `c62_25nov1688_pass2.txt` (second blind pass).
* `transcription/d145_30nov1690_cipher.txt` and `d145_30nov1690_pass2.txt`.
* `K5.tsv`: key frozen on 14 Nov 2026 (SHA-256 0a66e65b...), not validated.
* `reading/c62_25nov1688_reading_K5.txt`, `c62_25nov1688_reading_K4.txt`, `c62_25nov1688_en.md`, `d145_30nov1690_decoding_K5.txt`.

Images: AHNOB via PARES, not included (study use only).
