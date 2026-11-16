# Wave 17 Chrome sweep: Internet Culturale, Manus Online, RAH (15-16 Nov 2026)

Continues the "Started and not finished" rows of `research/COVERAGE.md` for Internet Culturale and RAH, and runs more
cipher terms in Manus Online. The first agent (15 Nov) was cut off by a rate limit before writing notes; this README was
started on 16 Nov from its scripts and `raw/` files. `raw/` and `img/` are git-ignored.

Scripts: `manus_terms.py` (Manus full-text term search, POST `https://manus.iccu.sbn.it/o/manus-api/titles-search-post`,
form `monocampo=<term>&n=v&monocampo:tipo=ONLY&page=N`, plain HTTP works), `manus_detail.py` / `manus_show.py` (record
detail, GET `https://manus.iccu.sbn.it/o/manus-api/title?id=<id>`), `teca_get.py` (BNCF Teca images: `readBook` lists a
folder, `showImg` returns a page at about 900-1260 px, plain HTTP works).

## 1. Manus Online (plain HTTP, no block)

Terms run by the first agent (records kept in `raw/manus_hits.json`, 122 records in all): con cifre 49, non decifrata 20,
poligrafia 9, non decifrato 8, non decifrate 7, in parte cifrata 5, non decifrati 3, con cifra 3, crittogramma 3,
cifrario 3, lettere cifrate 2, cifera 2, testo cifrato 2, criptato 2, crittografato 2, parzialmente cifrato 1, in parte
in cifra 1, scrittura segreta 1, codice cifrato 1, linguaggio cifrato 1, cifrista 1, furtivis 1, ziferis 1
(counts = records gathered per term, ONLY mode). The "cifra/cifre" family itself was screened on 9 Nov
(`sweep_2026-11_manus_italian_libs`).

### BNCF Carte Machiavelli, 1510 legation to France

The "non decifrata" hits led to the BNCF Carte Machiavelli V: letters of the Dieci di Balìa (and private writers) to
Machiavelli at the French court, July-Sept 1510, many "interamente in cifra". The first agent pulled 26 records
(`raw/manus_mach_sel.json`) and the Teca images of V/124-133 and V/134-136. Checked on 16 Nov against the Manus
bibliography field:

- **Printed (clear minute in the Dieci registers, edited in Passerini-Milanesi, Le opere VI, and Bertelli, Legazioni e
  commissarie 1964):** V/124 (Opere VI 76-78), V/126 (81-82), V/127 (82-84), V/129 (84-85), V/131 (89-94), V/135 (72-74),
  V/138 (64-65), V/150 (34-37), V/151, V/69, V/71, V/72 (VI 117), IV/135 (V 450-51), I/16 and I/18 (III), V/63 (UTET 1984
  n. 198). These are known-plaintext material for the same cipher, not candidates.
- **Content summarised by the cataloguer, so a clear text exists somewhere (register minute or Machiavelli's own
  decipherment), not candidates:** V/136 (copy to Pandolfini, "decifrata solo in parte da mano moderna in un foglio
  separato"), V/137 (decipherment slip in Machiavelli's hand), V/145 (Tommasini II.2 pp. 1350-53), V/146 (first six lines
  deciphered by Machiavelli), V/70 and V/71bis (Antonio Della Valle, interlinear decipherment by Machiavelli).
- **No decipherment, no edition cited, no content summary: candidates.** V/125 "Summario di l(ette)ra d(e) 18 di",
  enclosure of V/124, 22 Aug 1510, "interamente in cifra ... non è decifrata" (Tommasini II.2 p. 1356 only); V/134, Dieci
  to Machiavelli, 17 Aug 1510, "interamente in cifra, ad eccezione delle prime due righe, e non decifrata" (Tommasini
  only). Both seen on the Teca images (`img/sheet_6930_a.jpg`, `img/sheet_6980_a.jpg`): V/125 about 25 lines of sign
  cipher with no gloss; V/134 about 14 lines, Dieci subscription, no gloss. Same sign repertoire as the printed siblings,
  so the key can be rebuilt from V/124 + Opere VI.
- Full triage of all 58 Carte Machiavelli hits (`mach_triage.py` -> `raw/mach_triage.txt`, 16 Nov): every other record
  is either printed (Opere III-VI, Legazioni 1964, UTET 1984: V/137, V/146, V/70 and V/71bis are printed too) or carries
  an interlinear / modern-slip decipherment (III/5-26, III/102-115, IV/81-84, IV/111, IV/136-138, IV/170-176, V/61, V/64,
  V/67, V/130, V/141-149). V/148bis ("non decifrate", a copy of V/148, printed Opere VI 32-33) is not a candidate. V/136
  (partial modern decipherment, Tommasini only) and V/145 (summary given, Tommasini II.2 pp. 1350-53 only) are left in the
  README: a reading exists or is likely in Tommasini. I/80 and I/81 are Machiavelli's own decipherments of 1510 Dieci
  letters: vetting must check that neither covers V/125 or V/134.
- Extra Manus terms run 16 Nov (ONLY mode): "interamente in cifra" 25 (all Carte Machiavelli), "in cifra e" 38 (all
  Machiavelli), "non è decifrata" 4 (V/125 and three Cotugno letter volumes, illegible signatures), crittografia 6
  (Casanatense gr. 306, Malatestiano S.I.3, Vallicelliana F 26, Palatino 504, Lonato 194, Perugia 1701: colophon or
  study material, all screened 9 Nov), cifrari 1 (Genova BU G.IV.8, a key, already in the repo); 0 hits: "parzialmente
  cifrata", "cifrata in parte", "tutta in cifra", "senza decifrato", "senza decifrazione". The other "non decifrat*"
  records are illegible signatures or notes (Cotugno letters S.Mart.395-400, Campobasso, Vigevano, Gregoriana), not
  cipher. Parma Palatina Parm. 728, "Collectio anonyma de Ziferis" (17th c.): a cipher treatise, not correspondence; not
  in the repo (known.py), noted here only.
- known.py: none of V/124-V/151, V/69-V/72 is in the repo; catalogue 1549 (I/3, Luppi) and leads 1548, 1550, 1551 are the
  only Carte Machiavelli rows.

## 2. Real Academia de la Historia, Biblioteca Digital (Chrome, 16 Nov)

Plain HTTP meets the Anubis check; Chrome opens the site (the check passed by itself, nothing clicked). Route: same-origin
`fetch` POST of `busq_general=<term>` to `/es/consulta/resultados_busqueda.do` (catalogue) or `/es/consulta/resultados_ocr.do`
(the "OCR" box). A single hit redirects to `/es/consulta/registro.do?control=RAH...`; record ids sit in the
`data-analytics-recordid` attribute of the result list. A Tab freezes on loops of more than ~6 requests in one call.

Term counts (catalogue = OCR box, identical again, so the OCR box does not search page text): cifra 4, cifras 13,
cifrada 3, cifrado 3, "en cifra" 1 (RAH20090018105), "carta cifrada" 1 (RAH20090050396), descifrada 0, descifrado 0.
All hits are the Morillo papers 1817-20 (Enrile, Herrera, Alós, Eguía to Morillo), the Isabel II / González Bravo /
Xiquena papers (1868-69, a ciphered telegram copy), maps and printed books: the same set the 2 Nov pass found, already
leads. Nothing new.

**Salazar y Castro images.** The digital library holds about 10,000 item records "Pertenece a la Colección Salazar y Castro"
(9,978 with a digital object). Each record carries "Referencias: Índice de la Colección Salazar y Castro, <inventory no.>"
and "Signatura: 9/<n>, fº ... — Signatura anterior: <letter>-<n>, fº ...". Searching `"Salazar y Castro, <inventory no.>"`
finds a digitised item directly (test: 20297 -> RAH20112002100, D-11 = 9/286 f. 96v, Reyes Católicos to Alexander VI,
1493, with images: `/es/catalogo_imagenes/grupo.do?path=<n>`). Checked the inventory numbers of the repo's cipher items:
952 (A-10), 958 (A-10), 1078 (A-11), 1127 (A-11), 60896 (N-23), 15272 (A-97), 675 (A-7), 966 (A-10), 1069 (A-11),
14452 (A-89), 60894 (N-23), 949 (A-9), 1571 (A-14), 14177 (A-87), 16354 (A-109), 15725 (A-103): **none is online**.
The 16th-c. "[Carta]" records that a search like "N-23" brings up are the Marqués de San Román autograph collection
(`2/Ms Caja ...`), not Salazar, and none is described as cipher. The digitised
Salazar part is mostly genealogy (costados, apuntamientos) plus some letter volumes (D-11 and others); the item records
do not mention cipher (so "cifra" finds none of them), and the A- and N-23 cipher letters of the Badator export are not
among them on these tests.

Teca image route: `https://teca.bncf.firenze.sbn.it/ImageViewer/servlet/ImageViewer?idr=BNCF0003856980&azione=readBook`
(folder of V/134-136), `...idr=BNCF0003856930...` (V/124-133); single page `idr=<image id>&azione=showImg`.

## 3. Internet Culturale: blocked, not swept (16 Nov)

- Plain HTTP (curl) returns the "Firewall Captcha Authentication" page (an arithmetic CAPTCHA, `raw/ic_test.html`): not
  answered.
- Chrome, 16 Nov: the first three loads gave `ERR_SOCKET_NOT_CONNECTED` (homepage included); the next load of
  `/it/16/search?q=cifrata` returned the WAF page "Error 403 - Web Page Blocked" (Attack ID 20000021). Stopped there, as for
  a 429. None of the requested IC terms ("in cifra", cifrata, cifrato, cifrate, cifrario, "lettera cifrata", "lettere
  cifrate", "scrittura segreta", crittografia, crittogramma, "non decifrata", "parzialmente cifrata", "con cifra") was run
  on IC in this wave. **Needs the owner** (a WAF block on this IP; try later or from another network). IC's manuscript
  records for BNCF autographs are the same Manus records, which were searched here instead (section 1).

## Results

`candidates.json`: 2 rows, both class A (seen on the Teca images): Carte Machiavelli V/125 and V/134 (1510, Dieci di
Balìa to Machiavelli, sign cipher, no decipherment, no edition cited). `make_candidates.py` writes it.

Keys and treatises seen, not rows: Parma Palatina Parm. 728 (cipher treatise, 17th c.); Genova BU G.IV.8 (key, already
known). Deciphered or printed letters: the rest of the Carte Machiavelli list above.

## Not done

- Internet Culturale, all terms (WAF block).
- RAH: no image check for Salazar volumes beyond the 16 inventory numbers listed; the Badator item numbers of
  catalogue 2867-2876 (volume ranges, no inventory numbers in the repo rows) were not tested one by one.
- Vetting of the two rows: Bertelli 1964, the Edizione Nazionale Legazioni (Salerno), I/80-I/81, the ASF Dieci register.
