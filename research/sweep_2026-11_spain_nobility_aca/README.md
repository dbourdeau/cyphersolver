# sweep_2026-11_spain_nobility_aca (9 Nov 2026)

Result: **4 rows** in `candidates.json` (3 with images seen, 1 description-only) and 3 key-only items in `key_leads.json`.

## Routes
- **PARES answered** from this machine (no VPN needed): `pares.cultura.gob.es/ParesBusquedas20/` search, `catalogo/show/<id>`,
  `catalogo/description/<id>` and `ViewImage.do?accion=42&txt_descarga=1&dbCode=<db>&txt_id_imagen=<n>&txt_zoom=10...` all
  returned 200 with curl; 4 s between requests, one cookie jar per record, no 429. About 60 requests in all.
  (`pares.mcu.es` 302-redirects.) `fetch.py` = description + images; `more.py` = chosen image numbers; `run.py` = the
  session search of `research/pares_ags/sweep.py` with a 3 s delay.
- Web search (4 queries) found nothing on the Carlist items, the Catalan side or the RAH.
- Not tried: Hispana/BDCyL (swept before), BNE Digital (off limits), Biblioteca Digital Hispanica, Arxiu Nacional de Catalunya
  and Biblioteca de Catalunya catalogues (no item-level search reached; ANC EPICAT family letters only surfaced by web search),
  RAH catalogue, Archivo Historico Provincial catalogues.

## Terms run (new hits not in `research/pares_ags/hits.jsonl`)
xifra 38 (all surnames Xifra, 0 useful), xifrat 0 (PARES error page), "papel en cifra" 8, cifrado 208 (238 new ids in all; read by title:
Genoa 1647 Briceno Ronquillo duplicates are the 1643-51 Genoa family already in `genes1643`/catalogue 755; 1808 Consejo de Castilla
file, 1914-1950 telegrams and the 1960s AGA "Cifrado Especial" files are not leads), contrasena 0 (error page).
Files: `hits.jsonl` (254 lines), `screen.json` (the Oct hit list's nobility/ACA/Diversos rows with a known/unknown flag from `screen_known.py`).

## What was checked and excluded
- **ACA reg. 3225 (1435)**: already a target (`targets/maria1435/`, DECODE R10171). COVERAGE.md's "not reached" is out of date.
- **ACA Diversos Sastago 193 Lio B nos. 79/58-79/83 (1495-98)**: Escriva letters read by Parisi, DECODE R10172-R10180, already in the repo.
- **AHNOB Osuna, Philip IV to the Rome embassy 1642-52**: grouped in catalogue 747 (69 shelfmarks; `targets/albornoz1648/`); CT.2/CT.7 letters
  carry contemporary plain copies. Opened and dropped this sweep: OSUNA,CT.13,D.15 (Tursis to Infantado, 5 images: cipher pp. 1-3, decipherment on p. 4),
  CT.13,D.16 (Melchor Centelles de Borja, Messina 9 Aug 1650, 'nueva cifra', marginal decipherment beside the cipher passage), CT.13,D.8 ("Una carta cifrada
  esta descifrada"), CT.13,D.6 (hit "descifrada"). These are crib material for OSUNA,C.1981,D.113 (catalogue 730).
- Frias C.61 D.106-162 (Charles II to Fuensalida 1688 'con sus traducciones'), Fernan Nunez C.418,D.52 and C.1526,D.48 (with transcriptions): decipherments on file.
- Jardet to Marmont and the other 1811-12 French intercepts (DIVERSOS-COLECCIONES,133 and 134): `targets/marmont1812/`.
- OSUNA,C.1634-1635 (duque de Arcos letters 1520s): hit on the word in a description, no cipher in the titles; not opened.
- Baracaldo to Felipe, 1856 (DIVERSOS-TITULOS_FAMILIAS,3549,LEG.13,Exp.1, PARES 1353704, 35 images, Maria Cristina archive): numeric
  cipher groups seen on image 14, but the recipient wrote a plain word above many groups (interlinear decipherment), so it is a partial
  existing decipherment; not a row.
- Frias C.1887 D.93-98 (Ligne to Oropesa 1670) and C.1407 D.22: cipher letters, no images; not screened further (no Osuna-style siblings read).
- Santa Cruz C.57 D.172 "carta de cifrar" is a key sheet; Santa Cruz C.49-51 Philip IV letters are the Oct sweep's grouped rows.
- DIVERSOS-ARCHIVO_CARLISTA,113,Exp.1 (1872): "lenguaje cifrado" in names only, no cipher text claimed.

## Rows
1. DIVERSOS-COLECCIONES,161,N.2 (Azuares, London 1837): letter-substitution runs seen on images 3 and 5. Class A.
2. DIVERSOS-COLECCIONES,161,N.5 (Villafranca, St Petersburg 1837): a full cipher sheet seen on image 14. Class A.
3. DIVERSOS-COLECCIONES,195,N.14 (Van Halen, Igualada 1840): numeric cipher seen. Class A.
4. TORENO,C.71,D.35-59 (Garcia Montes, 1875): cipher letters plus alphabet per the PARES description; no images. Class B.

All four are 19th-century Carlist-war material, found because the hit list's Oct screening only read titles of the Osuna/Frias/Santa Cruz
groups. The wider "Correspondencia carlista / isabelina" series of the Deposito de la Guerra (DIVERSOS-COLECCIONES 161 and 195, series
5.1.26.1.1.12.1.16-17) is probably richer: PARES full text only returns items whose description says "cifra", so unlabelled cipher letters
there stay hidden.

## What remains
- ACA and Catalan archives: no new item found; ACA PARES hits are Sastago (done) and one 1604 lawsuit ("en cifra" a sum, no images).
  ANC, Biblioteca de Catalunya, Arxiu Historic de la Ciutat catalogues not reached.
- RAH (manuscript catalogue PDFs, Cifra nova Indiae Orientalis 1601 is a key), Archivos Historicos Provinciales: not reached.
- Browse DIVERSOS-COLECCIONES 161 and 195 page by page (about 20 + 60 items) for further cipher letters of 1837-40.
- AHNOB Osuna CT.13 (Infantado 1650) D.1-D.30 not all opened; only 4 items.

## Second pass (9 Nov 2026): AHN Carlist-war series

Coordinator merged rows 1-4 above as leads 2421-2424; they are **excluded from the new batch** (`candidates_batch2.json` holds only new rows;
`candidates.json` keeps all five).

- Route: PARES series listing `catalogo/contiene/<series id>` + displaytag pages (`series.py`), then `catalogo/description/<id>` for each child
  (`descs.py`), then images on contact sheets (`sheet.py`). Series 3735630 "Correspondencia carlista" (1833-1837, 61 units: legajos 161, 168, 190)
  and 3900022 "Correspondencia isabelina" (13 units, legajos 195, 167, 139, 205, 412, 415, 417). Legajos 160, 162, 194, 196 do not appear in either series
  listing (not found as Carlist correspondence on PARES). No 429; PARES became slow on large images (about 15 s each).
- All 74 unit descriptions read (`carlista_desc.json`, `isabelina_desc.json`). Only four say anything on cipher: 161,N.1 ("Varias cartas estan cifradas"),
  161,N.2, 161,N.5 and 195,N.14. The rest are personal letters, covers and reports (cataloguer flags cipher when present, so unflagged items were not opened).
- Opened and dropped: 161,N.3 (Gomez Labrador, Paris, Sept 1837, 13 images: clear), 167,N.19 (134 pp. of clear reserved letters of the Ejercito de Reserva de
  Andalucia 1837-38; one letter sends a key: listed in `key_leads.json`).
- **New row:** 161,N.1 Conde de Alcudia, Vienna 1837 (PARES 3735700): ciphertext on images 11-12 and 20-36+ of 61, many pages, no decipherment seen. known.py and
  two web searches: nothing.
- Not opened: 161,N.1 images 41-61; 161,N.4, N.9 (Ripoll), N.8 (a valise key letter), and the 168 units (unflagged).
