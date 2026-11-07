# PARES: Naples and Sicily viceroy items from the 27 Oct hit list (6 Nov 2026)

Follow-up to `sweep_2026-11_naples_palermo`, which pointed at `research/pares_ags/hits.jsonl` (10,328 rows, 2,027 distinct ids). 66 ids mention
Naples, Sicily, Cerdeña or a viceroy; 44 have images. Ten Naples/Sicily items in the Estado Genoa legajos were opened on the images
(PARES answered, no 429; one request every 4 s, fresh cookie jar per record; `fetch_imgs.py`, zoom 10, 800-900 px).

| PARES id | Signatura | What is on the images | Verdict |
|---|---|---|---|
| 3618662 | EST,LEG,3595,83 | Moncada, president of Sicily, Palermo 16 Jan 1638: clear letter, verso blank | no cipher; not a row |
| 3624586 / 3624598 / 3624627 | EST,LEG,1412,172 / 175 / 184 | Doria letters 1579, headed "descifrada": clear contemporary decipherments | not cipher |
| 3659327 | EST,LEG,1383,193 | news from Constantinople via the viceroy of Sicily, 1553: clear | not cipher |
| 3557316 | EST,LEG,3598,150 | Medina de las Torres to Eraso, 12 Apr 1642: clear copy | not cipher |
| 3558606 / 3558616 | EST,LEG,3598,222 / 223 | Medina de las Torres (viceroy of Naples) to Eraso, 19 Jun 1643. 223 opens in clear and goes into 2 pages of the 1643 Genoa-embassy cipher (syllabic figures 22 35 58, ax, sal, gan, gon); **222 is the clear copy of the same text** ("Continuando su Mag.d el deseo que siempre ha tenido de la quietud de Italia") | existing decipherment on file; same cipher family as `targets/genes1643/` (`key_K4b.tsv`): key lookup, not an open target. Not promoted |
| 3641213 / 3641220 | EST,LEG,3637,33 / 34 | 33: Caracena to Oñate, Milan 31 Dec 1650, one full page of cipher after a clear opening; **34 is its clear decipherment** (Milan, 31 Dec 1650: the Inquisitors of State at Genoa) | covered by catalogue 755 / `targets/genes1643/` notes ("3637,33/12 existing decipherments") |
| 3641240 / 3641224 | EST,LEG,3637,39 / 35 | 39: Oñate to Caracena, Naples 9 Jan 1651, two pages of cipher; 35 is a cover note ("las dos copias de cartas de 9 y 29 de enero ... se han excusado de descifrarlas"), not a decipherment | already in catalogue 755's scope (3637,39/14); different system from 1643 (the 1650-51 family) |

Neighbours of 3637,33 were read from their descriptions (3637,30-42: Caracena, Oñate and Giannettino Doria's case, Dec 1650-Feb 1651); only 33, 34, 35 and 39 concern the cipher letters.

## Result
0 rows. The Naples/Sicily viceroy items in the PARES hit list are either clear, headed "descifrada", or already inside catalogue 755 and `genes1643`.
`candidates.json` is empty. Other Naples/Sicily-flavoured PARES hits not opened: Osuna fonds (Philip IV's "carta cifrada" to Cardinal Albornoz, 1644-48,
OSUNA CT.2 D.8, D.16, D.34; the Albornoz letters are already worked elsewhere in the repo, `docs/albornoz1648.html`), Santa Cruz fonds (Philip IV to the
2nd marquis, galleys 1618-35; many "sin descifrar" items), Frías C.28 D.1.

## Route note
PARES: `catalogo/show/<id>` (cookie jar) then `ViewImage.do?accion=42&txt_descarga=1&dbCode=<db>&txt_id_imagen=<n>&txt_zoom=10...`; descriptions at
`catalogo/description/<id>`; whole-signatura search `catalogo/find?nm=&signatura=EST,LEG,3637,34` returns the show id. All answered curl from this machine on 6 Nov.
