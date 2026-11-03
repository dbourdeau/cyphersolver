# BVPB sweep in Chrome (2 Nov 2026, after the VPN switch to a UK exit)

Portal: Biblioteca Virtual del Patrimonio Bibliografico, bvpb.mcu.es. This replaces the earlier note of the same day
(429 on both page loads, before the VPN change). With the UK exit the host answers in the user's Chrome: no 429, no
Cloudflare, no CAPTCHA. Result: **0 candidate rows**; `candidates.json` is `[]`.

## How it was searched

- The GET URL `busqueda.do?texto=...` only opens the empty form. The form (`formBusqueda`) POSTs to
  `/es/consulta/resultados_ocr.do` with `busq_general`, `general_ocr` (on = full-text OCR search, off = catalogue
  fields only) and one `secc_*` checkbox per section. I sent that POST as a same-origin `fetch` from my own tab, one request
  every 2.3-2.5 s, restricted to the sections Manuscritos (antiguo, moderno), Correspondencia (epistolario, telegramas,
  postales) and Documentos (archivos personales, documentos manuscritos).
- Catalogue-field search (OCR off), about 40 terms and forms: cifra, cifrado, cifrada(s), descifrado, "en cifra",
  "carta cifrada", "cartas cifradas", contracifra, clave, "clave secreta", criptograf*, cript*, enigma*, jeroglifico,
  abecedario, nomenclator/nomenclador, chiffre, cifrario, zifra, xifr*, steganograf*, "tinta simpatica", "escritura
  secreta", numeral*, "papel de cifra", "billete cifrado", "telegrama cifrado", "despacho cifrado", "palabras convenidas",
  secret*, alfabeto*, signos. Result: **0 records** for every cipher term. The few non-zero answers are noise
  (cifr* 10 incl. a Galdos telegram from "San Cifiean", a surname; clave* 5, all surnames; xifr* 3, a printed Catalan
  prayer book; secret* 35 and "secreta" 4, e.g. Monita secreta, secretario).
- Full-text OCR search, same terms: cifra 110, "en cifra" 28, clave 35, cifras 39, cifrado 8, descifrado 5, cifrada 5,
  cifradas 2, jeroglifico 5, abecedario 5, nomenclator 2; contracifra, criptograf*, chiffre, cifrario, cipher,
  "carta cifrada", "clave secreta" 0. I opened the record page (`registro.do`) for every hit filed as a manuscript or
  document that the facets exposed (607725, 607738, 607741, 607748, 607740, 591733) and the Epistolario hit 602569.

## What the hits are

BVPB's "Manuscrito antiguo hasta s. XIX / Manuscrito moderno" sections include digitised printed books with OCR (e.g.
Hartzenbusch, Cuentos y fabulas, 1925; Instrucciones para la catalogacion de Manuscritos, 1910; Valle-Inclan 1960).
Their OCR hits for "cifra/cifrada" are the ordinary Spanish senses (figure, "cifrada en palabras"). The real manuscripts
(Gratian, Fuero Juzgo, patristic codices, Galdos letters) carry no cipher word in their catalogue records.
The OCR full-text layer exists only for printed books, so ciphered manuscript leaves cannot be found by text here.

## One item worth a look, left unvetted (not a row)

- **Cartas del cardenal don Fray Francisco Jimenez de Cisneros dirigidas a don Diego Lopez de Ayala**, ed. Gayangos and
  De la Fuente, Madrid 1867, BVPB record `registro.do?id=602569` (section Epistolario, CC BY 4.0, 271 p.). The 26 OCR hits
  for "en cifra" are editors' notes and tags in the printed text, e.g. pp. 144, 165, 169: "(En cifra.)" before text, and
  footnotes saying the letter is "en cifra" at Simancas, ff. 108, 120-123 of the collection. It reads as a printed
  decipherment (the cipher letters are printed in clear), so it is edition evidence, not a ciphertext lead. I saw only the OCR
  snippets, not the page images, and did not search DECODE, Tomokiyo, Lasry or the literature for it. It is the
  edition that catalogue 746 (Charles I to Cisneros, 1516; lead note "check Gayangos & de la Fuente (1867, 1875)") and the
  `ayala1516` target already name; the 1875 *Cartas de los secretarios* is the companion volume. Next step if wanted:
  open pp. 144-170 in the viewer and compare with the Cisneros 1516 cipher folios in `targets/ayala1516`.

## Not reached

- Image-level inspection of any BVPB manuscript: BVPB lists 130-odd holding libraries (AGS, AHN, RAH, BNE
  copies, university libraries). A ciphered letter whose record does not use a cipher word (catalogued only as "carta",
  "despacho", "correspondencia") would not be found by this method; no browse of the Correspondencia or Documentos sections
  by library or century was done (it would be thousands of records).
- The last terms in the final batch (jeroglifica*, and the tail of the batch) returned 0 before I stopped.
- Prior-art web searches (DECODE, Tomokiyo, Lasry): none, because there was no row to check.
- `research/COVERAGE.md` does not exist in this checkout; the brief's other files were read.

## Files

Only this README and `candidates.json`. The search helper was page JavaScript and is not saved; the endpoint and field
names above reproduce it. Tab opened by me was closed.
