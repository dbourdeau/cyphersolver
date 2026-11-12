# Blind re-reading of the cipher digits on the images - D.107 (Ridolfi, Rome 8 May 1646) - 11 Nov 2026

Short English version of our working file (planche-c06/RESULTAT.md). Reader: Brice Dudout. The images (PARES, AHNOB
OSUNA,C.3456,D.107) and the thumbnails of the sheet are private and not included; the key of the sheet (which shape is
which digit) is not included either.

## Rule and answers (hashed)

- Integration rule, written and hashed before the sheet was opened (French working file REGLE-INTEGRATION.md):
  SHA-256 `b61a4fd7446559b170195e52c46cb8a83b4834f01e17565350137fba5dfe3adf`; checked before it was applied.
- Brice Dudout's exported answers (reponses-brice-2026-11-11.json):
  SHA-256 `c692c679177bdabd9cd9b80d22018233ade6b89b80eedd90b395aa94f0c46ee6`.
- The sheet: 19 questions (the doubtful digit of 19 corrected groups behind restored words) and 2 controls with a known
  answer, in random order. Each question shows the line, the group enlarged and two reference shapes of the digit at the
  same position (tens or units), taken from certain words elsewhere in the letter, plus "other / illegible / don't know"
  and a remark. No value or gloss on the sheet.
- Rule: a shape chosen replaces the digit of transcription v1 at that place (v1 stays frozen); if the word then reads
  entirely with the frozen key it passes from restored to certain; if the shape chosen is the v1 digit, the word stays
  restored (image matches v1, probable cipher-clerk error); "other", "illegible" or "don't know" leave it restored. If
  either control fails, nothing is integrated.

## Result

- Controls: 2.05 group 15 (expected 8, "partito") passed; 1.19 group 10 (expected 7, "questo") passed. Rule applied.
- Confirmed (12, now certain): il (1.01), atacatto (1.16), lontano and miglia (1.21), perche (2.13), risolutione (3.19;
  Brice Dudout: "it is a 23; the 4 was a botched character rewritten as 3"), al and Signor (4.02), al (4.04), mandero
  (4.11), termini (4.17), oferte (5.05).
- Image matches transcription v1, still restored (probable cipher-clerk error): Bologna (2.03), il (1.16), al (3.08),
  loro (4.01), quando (3.08), Milano (2.03).
- Undecided: quando (1.12), answer "other", remark "5 or 9" (recorded; not a confirmation).
- Not on the sheet: di (1.06, a group left out; the image shows the normal space, nothing to judge) and lunghezza (5.02,
  47 = z is a question of value, not of shape).

## Recount

Same counting script as `scripts/decompte.py` (only the input folder changes), run on `v2/lecture-v2/`, a copy of
`LECTURE-p1-4.txt` and `LECTURE-p5.txt` where the 12 confirmed words lose their marks < >; 431 words, unchanged.
Output in `v2/decompte_v2.out`: 390 certain, 27 probable, 9 restored, 5 unresolved.
**certain + probable = 417/431 = 96.8% >= 95% -> read** (was 405/431 = 94.0%, read in part).

Reservation: "certain" for the 12 words follows the hashed rule (the word reads entirely with the validated key once the
digit is replaced); one reader, no second reader.
