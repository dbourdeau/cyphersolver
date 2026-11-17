# Chrome wave 10 (15 Nov 2026): Badator export of the RAH Salazar y Castro index

**Result: leads 2867-2875 (9), none promoted** (the ciphertext of a Salazar y Castro index entry is in the RAH volumes and not online, so no lead meets "ciphertext seen").

## Badator: use the portal's own export, not paging
Badator (`artxibo.euskadi.eus`, `badator/maintSimple`) has a documented **'Exportar Busqueda'** link on the result page (CSV, `;`-separated, UTF-8 with BOM). One click after the search 'cifra' (1,892 records) downloads **all** records in one file, with the columns the list page hides: `Signatura` (volume and folios, e.g. 'A-87, fº 86. El fº 87 es el sobrescrito'), full `Titulo/Descripcion` (including the index's remarks 'Original, en cifra', 'descifrado al margen', 'sin que exista a continuacion el texto descifrado'), `Fecha`, and the record order of the index. No 'Ver ficha' link had to be followed and no HDIV token was touched. The file lands in the browser's Downloads folder; `badator_parse.py` turns it into `badator_rows.json` (companion 'Texto descifrado' rows linked to the original they follow).
- The simple search is an AND of literal words ('telegrama cifra Aguirre Prieto' gives 0); the search form is `#searchForm` (`termino`), submit with `form.submit()` three seconds after the page loads.
- Per-row classification (`badator_groups.py`): a row has a decipherment filed if the next row is its 'Texto descifrado', or its own remark says deciphered in the margin/between the lines/following; duplicates ('Ejemplar duplicado') of a deciphered letter count as filed. 'sin que exista a continuacion el texto descifrado' and 'pendiente de descifrar' count as **not** filed.

## What was already in the repo
Leads 1085-1090 are the RAH 1638-56 families (Philip IV and the Cardinal-Infante to Sarmiento A-87, Juan Jose de Austria A-103-107, the Medici cardinals A-109, Terranova A-97), made from the printed index earlier; wave 9 counted them as new by mistake. The pre-1520 rows are in ledgers 1041-1075; Alonso Sanchez, Lope de Soria, Fernandez de Cordoba, Lope Hurtado, Juan Manuel and Hugo de Moncada have their own targets.

## New leads (one sender/key each)
| lead | sender | cipher rows | filed decipherment | open |
|---|---|---|---|---|
| 2867 | Juan Perez (secretary, Rome), A-32 to A-44, 1524-29 | 94 | 66 (with duplicates) | 28 |
| 2868 | Marino Caracciolo, protonotary (later cardinal), A-34 to A-44, 1525-29 | 114 | 47 | 67 |
| 2869 | Miguel de Herrera, A-36/37, 1525-26 | 8 | 3 | 5 |
| 2870 | Charles de Lannoy, viceroy of Naples, 1522-27 | 11 | 1 | 10 |
| 2871 | Prospero Colonna, 1522-23 | 3 | 0 | 3 |
| 2872 | Girolamo / Antoniotto Adorno, 1522-24 | 18 | 8 | 10 |
| 2873 | Adrian VI to Charles V, 1522-23 | 4 | 0 | 4 |
| 2874 | Cardinal Trivulzio (Tribulcis) to Haro, A-98, 1652-54 | 5 | 0 | 5 |
| 2875 | Leopold Wilhelm to Haro / Philip IV, A-92, 1650-56 | 5 | 1 | 4 |

The filed decipherments make each of 2867 and 2868 a crib-rich series (many plaintext/ciphertext pairs once images exist). The Calendar of State Papers (Spain) quotes some of the Juan Perez letters with their deciphers (Salazar A-38), and a Venetian source says ciphered despatches of Charles V's ambassador at Rome were shown to the Signory on 18 Jun 1526 (Zuan Soro): web search 15 Nov 2026, no cipher study of these letters found. Tomokiyo and GL.htm: nothing under these names (grep of the repo copy of GL.htm).

Not made into leads: the Conde de la Roca to Haro (A-88, 1643-44: 7 of 8 deciphered in the margin), Rodrigo Nino (2 letters, 1 filed), Rafael de Medicis 1521 (2, 1 filed), the 1630s Philip IV copies (K-8), single letters (Pascual de Aragon A-99 f.66-70, Auersperg A-97 f.12, Vatteville A-97 f.143, Juan Jose A-107 f.193, Philip IV to Guzman Ponce de Leon M-73 f.251), the 'Cifra general nueva 1637' key leaf (A-87 f.1) and key sheets A-15 ff. 1-25 (cifras of the viceroy, general, Silva-Garcilaso ...), I-7 f.148 (Samper's cipher), N-65 f.201 (Carlos II cipher key).

## Other Badator hits (not from the Salazar y Castro index)
- Fundacion Indalecio Prieto, Fondo Victor Salazar: 25 Jun 1937 note of the Estado Mayor Gabinete de Cifra (typed, clear: 'Quedando aproximadamente por descifrar unas diez palabras') and the 2 Jul 1937 'telegrama en cifra' of Aguirre to Prieto: viewed (`Ver imagen`): both are clear typed texts (the telegram is already deciphered). No cipher text, no lead.
- The remaining 1930s-40s hits are 'cifra' = a figure (budgets) and telegram regesta without images of cipher.

## Galiciana (Arquivo do Reino de Galicia and 60 other Galician archives)
`arquivo.galiciana.gal/arpadweb/gl/consulta_archivos/busqueda.do` loads in Chrome (form `#formBusqueda`, POST to `/arpadweb/gl/consulta/resultados_ocr.do`, field `busq_general`), but the search for 'cifra' (both a same-origin `fetch` and a real form submit) never returned within 60 s and froze the renderer; not retried.
