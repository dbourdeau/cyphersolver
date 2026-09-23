# Hugo de Moncada to Charles V, Monaco, 6 October 1524

Status: found already solved: printed 1854 (CODOIN XXIV); key rebuilt here and the print's gap filled (22 Sept 2026)

- Catalogue 273 (new-solves sweep, 22 Sept 2026): "Hugo de Moncada, from Monaco, to Charles V", BNE Digital viewer
  8b55d967-e74e-4bad-bec4-bdfd44c43886 ("Carta 9"), given as undeciphered after Tomokiyo (spanish2C, 8 June 2026),
  who could not find the decipherment that the pencil note in the margin points to.
- The letter is **BNE MSS/20213/12** (folio stamp "20213/12-9", "Monago 6 octubre 1524"), and it is also on DECODE as
  **R1191** "NLS_MSS_20213_12", 1524, status "Decrypted", no sender or receiver, two images, authentication required.
  The BNE viewer is behind a Cloudflare challenge; the DECODE images (970 × 1395 px) were fetched with the cookie
  (`img/`, git-ignored).
- One leaf. f. 1r: clear text with about 17 lines of cipher runs mixed into the clear (442 signs). f. 1v: the close
  of the letter in clear and the signature "Don Hugo de Moncada". Moncada was captain-general of the galleys in
  1524, at Monaco; he was viceroy of Naples only from 1527.

## The note in the margin, and the print

The pencil note beside cipher lines 4–6 reads "Descifrada en t.° 24 Col. Doc. inéd.": the decipherment is printed
in *Colección de documentos inéditos para la historia de España*, vol. XXIV (Madrid 1854), in the documents that
follow Gaspar de Baeza's *Vida de Don Hugo de Moncada*: "Carta de D. Hugo de Moncada á Carlos V, avisándole que el
ejército había llegado á Niza... Monago 6 de octubre de 1524. (Original) (Salazar, C. V., 1524, p. 3.)", pp. 417–419
of the volume. The editors printed the ciphered passage from the secretariat's decipherment ("descifrado después de
letra de la secretaría de Carlos V como todas las semejantes que tienen una hoja á continuación, que dicen CLARO"),
with a gap: "me rogaba que le llevase .... muchas razones para ello". Text: `prior/codoin_1854b.txt` (Internet
Archive `bub_gb_VGwxkA0412wC`, djvu text; lines 16710–16780). Tomokiyo and the catalogue missed it because the OCR
spells the name "Moneada".

## Work here

1. Transcribed the cipher runs from the DECODE image (deskewed −2.7°, cropped 3–8×): `ct.txt`, 442 signs, 17 runs.
2. Aligned each run with the 1854 text by EM (`em_align.py`, output `em_out.txt`) and by hand: a homophonic
   substitution of Spanish letters, 2–5 signs per common letter, no syllables; a double cross after a base sign
   makes a separate sign; a few code groups in Latin letters (`lay` = yo, `ne` = duque). Key in `KEY.md`.
3. The print agrees with the cipher throughout the runs checked (tienen pan, si el duque de Genoua querra dexar yr las
   galeras, las de España mal en orden, que su persona ouiese de yr, que fuese fuerte, yo sere con el, largamente
   sobre esto, yo deterne esta yda, tornando a este negocio viene muy mal contento, de la Mota).
4. Read the gap with the rebuilt key: "que le lleuase **a España**, [99] **diziendome** muchas razones para ello".
   So Bourbon, after the failed siege of Marseille, asked Moncada to carry him to Spain in the galleys. The print
   also leaves out three code groups (below).

Reading: `reading.txt`.

## Outcome: read (found already solved; gap filled)

428 of 442 cipher signs read as sense (96.8%). The key is recovered (`KEY.md`); the text class is "already solved"
(the 1854 print) with the gap filled here.

## Remaining gaps
- code groups =D. , P#D , =P#D.f (12 signs) - blocker: too-short; each occurs once, no key, and the print gives no counterpart except "duque" for the first
- 99 at the end of cipher line 2 (2 signs) - blocker: too-short; two signs set apart at the margin, either "a a" or line-end nulls; nothing else in the letter settles it

## Escalation
- [x] siblings: DECODE BNE MSS/2021x records listed (R1170-R1191); none is by Moncada or in this cipher. CODOIN XXIV prints other Moncada ciphered letters of 1524 from the Salazar collection, deciphered at the time; their originals are not on DECODE
- [x] clear-pages: f. 1v is the clear close of the letter, not a decipherment; the CLARO leaf is not with the original at BNE
- [x] known-keys: Soria 1523 keys A and B (soria1523/) compared: code groups of three letters, a different system; Kolosova keys ruled out by Tomokiyo
- [x] print: CODOIN XXIV (1854) pp. 417-419 found and used; CSP Spain II does not calendar it
- [x] key-rebuild: key rebuilt from the whole letter against the print by EM alignment (em_align.py) and by hand (KEY.md)
- [x] retry: gap re-read with the rebuilt key at 6-8x (a España, diziendome); code groups and 99 tried against the letter's context, no value fits better than another
