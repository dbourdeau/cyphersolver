# Paris nunciature, bishop of Bergamo, 1585–86 (ASV Segr. Stato Francia 18; DECODE R15, R16) — NOTES

**Result: read** (R16 0.974 measured, 21 Sept 2026; open: name codes 18/48 and scattered transcription slips; see
Remaining gaps). R15 read before (Lasry); R16 read here with the same F18 key. Write-up: docs/bergamo1585.html.

**Split on 14 Oct 2026** under the one-key rule (George Lasry, 14 Oct 2026): R17 (Francia 18/3), filed in the same
volume but in Meister's key no. 40, moved to [`targets/morosini1588/`](../morosini1588/NOTES.md) (page
`morosini1588.html`, "a different key, with its own page"), with `R17_transcription_decode.txt`,
`R17_decryption.txt` and `R17_words.txt`. Its record is kept below for the history of the entry.

Catalogue entry 242. Checked on 2026-09-21 as part of a sweep of the Paris-nunciature records on DECODE (see
[targets/damiata1624/](../damiata1624/NOTES.md) for the 1625 volume).

## The three records

- **R15** (Francia 18/1, ff. 7r–v): **already read.** Lasry's decryption (DOC D3102) with the F18 key (D3103,
  fixed-length homophonic; "also found in Meister p. 324 and in the French book, Ragazzoni"). Nothing added.
- **R16** (Francia 18/2, f. 206r–v; cleartext heading "3 di Marzo 1586"): **decrypted here, in part.** DECODE's
  decryption file for R16 (D3104) is byte-for-byte the R15 decryption (19,639 bytes, same text), attached to the
  wrong record, so R16 had never actually been decrypted. The F18 key (D3105, same as R15's) applied to the DECODE
  transcription D1610 (TimB) with `decode_with_key.py` gives readable Italian at once: 1,410 letter pairs, 66
  unknown (transcription slips and phase breaks). Output in `R16_decryption.txt`.
  Content: *hoggi il [58] mi ha mandato a dire … la bolla … la congregatione del clero … mal contenti dela
  concessione dela bolla … l'alienatione … appellarsi ad futurum concilium …* — the French clergy's resistance
  to the papal bull permitting the alienation of church property, 1586.
  **Nomenclator (same day):** Meister p. 324 no. 2 prints Ragazzoni's 1583 Paris key, the same letter alphabet with
  its nomenclator (OCR in the main checkout's `targets/vatican5/meister.txt`, ll. 59655–59920; realigned in
  `meister324_nomenclator.txt`). Added to the decoder with a one-digit resync for transcription slips: unknowns fall
  from 66 to 18. Confirmed by context: 26¸ che, 36¸ per, 28+ questi, 98+ essere, 20- non, 0^. con, 34 Re
  Christianissimo, 58 Duca di Guisa (who asks for Metz), 14 Nostro Signore. **Not confirmed:** 18 and 48 (Meister's
  Ferrara/Parma) turn up where no duke fits; the 1586 table may have moved them. The letter: Guise will not let the
  King sell church property under the bull unless he gets Metz and money; the clergy's assembly means to appeal to a
  future council, hoping for the Pope's help.
  **Open (was):** about 20 nomenclator codes marked with a cedilla, + or – (26¸, 28+, 36¸, 20-, 58, 34, 70, …) are
  not in Lasry's key. 26¸ behaves like *che*, 20- like *non*, 58 is a person (probably the King or a prelate), 34
  another (probably the Pope). Filling them needs context work or Meister's full table.
- **R17** (Francia 18/3, ff. 233r–235v): **moved to morosini1588 on 14 Oct 2026** (different key). Record of 21 Sept: Meister p. 393 no. 40 (Morosini, 1587), already
  keyed in `targets/morosini1588/decrypt.py`, reads DECODE's transcription D1611 on all five pages with 5 unknown codes:
  the Duke of Lorraine and Guise, the German reiters, the Queen Mother, Schomberg (`R17_decryption.txt`). So R17 is
  a Morosini-period letter (1587–88), not Bergamo/Nazareth. Earlier note: DECODE's key (D3186, ASV F22) is a different system:
  variable-length and *not deterministic* (1–3 digit elements, 8 and 80–89 null). The note says it is incomplete
  and that the full key is Meister p. 393 no. 40. DECODE's decryption file is a Java crash (NullPointerException),
  so R17 had no decryption before this.

## Files

`key_F18_lasry.txt` (DECODE D3105), `R16_transcription_decode.txt` (DECODE D1610), `decode_with_key.py`,
`R16_decryption.txt`. Images are on DECODE (login); not re-transcribed here: the R16 reading rests on TimB's
transcription.

## Remaining gaps

- R16 nomenclator codes 18 and 48 - blocker: open-codes; Meister's Ferrara/Parma values do not fit the contexts; the 1586 table may have moved them
- R16 remaining ~16 unknown pairs - blocker: open-codes; unknowns after the one-digit resync; mostly transcription slips in TimB transcription D1610, images not re-read

## Escalation

- [x] siblings: R15-R17 all opened; R16 decryption file found to be a copy of R15; R17 is in another key (now morosini1588)
- [n/a] clear-pages: no clear pages or interlinear decipherments are reported on R15-R17
- [x] known-keys: Lasry F18 key (D3105) and Meister p. 324 no. 2 (Ragazzoni 1583) fit R16; Meister p. 393 no. 40 (Morosini) fits R17 only
- [x] print: Meister 1906 key tables used; no printed decipherment of R16 sought beyond Meister
- [ ] key-rebuild: not done - fill 18/48 by alphabetical bracketing and LM context over Ragazzoni-period letters
- [ ] retry: not done - re-read the R16 images for the slip positions, then rerun decode_with_key.py

## Assumptions for George's review

- Credit: George is credited here with the F18 key (D3103/D3105) and his R15 decryption (D3102), which his DECODE
  files document; R16 is read with that key. His R18 file for Morosini's key (D3175) and his F22 note on R17 (D3186)
  belong to the Meister no. 40 entry, `morosini1588`, not here.
