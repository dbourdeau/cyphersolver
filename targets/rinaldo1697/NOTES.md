# Rinaldo d'Este, duke of Modena, to "Marchese Taddeo", 6 Jun 1697, cc. 73r-73v (Biblioteca Estense)

Status: in progress. Not yet written up: no site page or README row. Read in part, with escalation steps still open (see Remaining gaps and Escalation). The status below is the contributor's.

Not in the catalogue; found in a sweep of the Estense digital collections for letters with cipher. No catalogue number.

Status, 3 Nov 2026: **read in part**. Every letter group is read with a key recovered from the interlinear decipherment.
Many code groups (two- and three-digit numbers used for words) are still open or carry only a proposed value. A
contemporary hand wrote the decipherment between the lines over most of the cipher, so this is a **transcription job,
not a break**. The letter key is a reversed alphabet. On 73v it gives text where the gloss is faint or missing.

Contributed by WAINUT. The work was done with AI language-model agents. No human palaeographer has checked it. An
independent agent made the blind check in `VERIFY.md` and its corrections are applied below.

## Count

`scripts/check_marks.py`, output in `validation/check_marks_output.txt`. A word split over a line end is counted once.

| | words |
|---|---|
| verbatim from letter groups | 28 |
| with a marked repair (double letter written once, or a doubtful sign) | 5 |
| holding a code whose value is read from the gloss over that place | 12 |
| holding a code with a proposed value only | 12 |
| holding a code not identified | 11 |
| **total** | **68** |

Read as sense (the first three rows): **45 of 68 (66%)**. That is well below the 95% bar, so the status is read in part.
Weak places that count as read: `cot.` (L03, probably *cotesta*, no gloss seen), `compendo` (V01, as written: the
sense needs *comprendo* or *compiendo*, so a letter is missing or the word is unclear), `lon{?g}o` (L07, doubtful 1).

**Correction to the earlier count.** The first version of this folder gave 79 words, 46 read (58%), and the independent
check repeated that figure. Its counter counted each half of a word split over a line end as a word (five words), and it
split code values with dots inside (`M.ta`) into extra words. The applied fixes then changed the reading: *ministro*,
the V06 group, the gloss values for 187, 131, 189, 110, 190, 188 and 19P, and the split of V12-V13. The 68 above is the
recount with the corrected counter on the corrected reading.

## Document

- Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera R, Rinaldo, duca di Modena, cc. 73-74
  (4 canvases). Record: "Lettera parzialmente cifrata (ma decifrata in interlinea). Destinatario incerto." Address at the
  foot of 73r: "Marchese Taddeo". Dated "1697, 6 Giugno" in a later hand.
- IIIF manifest: https://edl-jarvis.cultura.gov.it/meta/iiif/eea09124-7484-4e51-bbbc-448138b5972c/manifest
  (CC BY-NC-SA). No images are in this folder; `scripts/fetch.py` fetches the regions used. The cipher is on 73r
  (11 lines with groups) and 73v (16 lines). 74r-74v were not examined.

## The system

- Letters are two-digit numbers in a reversed Italian alphabet: a 24, c 22, d 21, e 20, f 19, g 18, h 17, i 16, l 15,
  m 14, n 13, o 12, p 11, r 9, s 8, t 7, u 6, z 4. Groups are often separated by dots. Double letters are written once.
- Codes are three-digit numbers (107-196) and a few two-digit numbers outside the alphabet (25, 55, 57, 91, 94), used
  for words and parts of words. Values read from the gloss over at least one place, checked on full-size crops:
  186 per, 160 spedizione, 187 che (V09, V14), 131 S.M.C. (V09), 189 le (V12, L05), 110 ordin- (V08, V12), 190 del
  (L05, V03), 188 la (L05), 19P ma (L05). Proposed only: 130 M.ta, 94 Francia, 139 bene, 116 Svezia, 25 sudditi,
  183 -zione, 107 Leg., and 189, 190, 19P where no gloss was read over that place. In 19P the third digit is a crossed
  rho shape that matches no digit of this hand.
- 19P = *ma* gives "il male della" (L05), "Ma in ogni caso" (L07) and "massime del suo stato" (L08). Only L05 has the gloss.

## How the key was obtained; held-out test

1. Signs came first. Both pages were read in two passes on bands cut so that the interlinear decipherment is masked, with
   no key and no gloss given. **All four passes were vision-model runs** (73r: two separate runs; 73v: two different
   models): `validation/pass1_R.txt`, `pass2_R.txt`, `pass1_V.txt`, `pass2_V.txt`. An earlier version of this note said
   73r pass 1 was by eye. That was wrong; the independent check found it. Disagreements were settled by an AI agent on the
   band images (`validation/adjudication.tsv`). No digit was moved toward the gloss. The gloss was read afterwards, first
   by a model run with no key (`validation/gloss_raw.txt`, `gloss_raw_V.txt`), then on close crops.
2. The letter key was built from the 73r pairs (pericoloso, longo, sue funzione, suo stato) and frozen (rows `frozen` in
   `key.tsv`).
3. Held-out test: 73v decoded with the frozen key.
   - **Against the gloss.** The key-free model reading of the 73v gloss pairs 43 single gloss letters with a letter group.
     33 of 43 (76.7%) agree with the frozen key. 1000 shuffled tables give a mean of 2.3 and a best of 15. We looked at
     the ten that disagree: five are on V03, where that reading has "vescovo" over 21 20 22 12 9 12; on the crop the gloss
     is "deco" + "o", as the key gives (the r is faint). The other five (V07, V08, V09, V11, V14) we did not settle on a
     crop; on V14 that reading has "vero" where the groups give "gres(s)o", and it took 18 9 as one number. The gloss
     reading is noisy, so this test is a lower bound.
   - The independent check read the gloss by eye over V08, V09, V11, V12 and V14. It agrees with the key wherever it was
     legible.
   - **Coverage.** 89 two-digit groups on 73v (88 letters plus the doubtful V06 group 52?). 83 have a frozen value
     (93.3%). The other six are the codes 25, 55 (twice), 57, 91 and the doubtful 52.
   - **Bigram score**, weak and secondary. Letter-bigram model trained on 3,941 characters of 16th-century Italian (the
     Italian reading lines of `targets/ercole1544/reading_0078_0079.md`, in `validation/italian_train.txt`): frozen key
     -2.624 per bigram, 1000 shuffled tables mean -3.825, best -2.919, none as high. An earlier run with another short
     training text gave a margin of nil (-2.943 against a best of -2.940); the result depends on the training text.

## Corrections after the independent check (3 Nov 2026)

All checked on full-size crops of the images.

- V15 *ministro*: the groups are 14 16 13 16 8, not 14 10 13 10. The second group is a clear 16. The fourth is blotted and
  fits 16; it is marked doubtful. The key row "10 = i" is gone; it came from this misread.
- V06: the line ends in a sign pair written like "Sʀ.", earlier taken as clear text "Sp.". The first sign has the form of
  this hand's 5 and the second the rho-shaped 2. A gloss word ("Caggio"?) stands beside it, at the margin. It is now
  transcribed `52?` and read as an open code. "of Sp." is out of the translation. If it is clear text after all, the
  count drops by one open code.
- Gloss values used: 187 che, 131 S.M.C., 189 le, 110 ordin-, all checked on crops. Also 190 del and 188 la (L05, gloss
  "Male della") and 190 del (V03), and 19P ma (L05). These were not in the check's list; we saw them on the crops of the
  same lines.
- V12-V13: the gloss reads "a p le n i p o t e" over 24 . 11 189 13 16 11 12 7 20. So the text is "a p[le]nipotenz.
  catolici", to the Catholic plenipotentiaries, not "the Catholic powers".
- Weak places now named in the reading: `cot.`, `compendo`, `listu[183]`, `lon{?g}o`, the V06 group. `sime` (L08) is now
  read `[19P ?ma]{+s}sime`, *massime*, with 19P proposed there.
- `listu[183]` (V07): the gloss over 183 ends "zione"; the gloss over the letter groups before it reads more like "sistu-"
  than "listu-". The groups give l i s t u. *l'istruzione* would need an r the cipher does not have. Not settled.
- Scripts that called a private model helper (the blind sign pass and the gloss reading) are not in this folder. Their
  outputs are in `validation/`.

## Remaining gaps

- Open codes: 196 (twice), 193, 191, 130 (L06), 175, 91, 57, 55 (twice) and the V06 group. Proposed only: see above.
- 19P: the third digit is not identified.
- The gloss over 196 on L09 may begin "Tutt-"; not settled.
- No pass by eye of the whole page; sign reads are by AI agents. The independent check read 214 groups blind
  (73r L02-L11 and all of 73v).
- The clear text was read only around the cipher. 74r-74v were not examined.
- Recipient: "Marchese Taddeo". Identifying him as Taddeo Rangoni is a suggestion and was not checked.

## Prior art

Checked 3 Nov 2026: Dan Bourdeau's catalogue, leads, targets and research notes (origin/main) and the open PRs, for
Rinaldo, Rangoni and Taddeo. There is no entry for this letter (`targets/rangone1530` is unrelated). Two web searches
(Rinaldo d'Este 1697 cifra Taddeo Rangoni; Rinaldo d'Este 1697 lettera cifrata Rangoni Ryswick plenipotenziari Estense
Campori) found no edition or decipherment, only biographies and unrelated records. That is not proof that none exists.

## Files

`transcription_c73.txt`, `key.tsv`, `key_frozen.tsv` (the frozen rows only), `decryption_c73.txt`,
`reading_marked_c73.txt`, `reading_c73.md` (Italian and English), `scripts/` (fetch.py, bands.py, check_marks.py),
`validation/`, `VERIFY.md` (the independent check, unchanged; its counts predate the corrections above).
