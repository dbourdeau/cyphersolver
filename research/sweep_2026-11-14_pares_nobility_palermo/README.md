# PARES nobility, Palermo ASPa PDFs, ASNa (14 Nov 2026)

Result: **13 candidate rows** (all description-only, from the PARES hit list; none opened this sweep), 0 new Palermo or Naples rows.
`candidates.json` is built by `make_candidates.py`; regions and periods are in merge.py's allowed lists; no ledger touched.

## Blocks
- **PARES answered 429 to every request from about 18:20 on 14 Nov** (curl show and description pages; also Chrome, own tab, same
  429 page), so it is an IP block, probably set off by parallel sessions. Not retried in a loop (one probe every 10-20 minutes, all 429
  through about 20:10). Part (1) therefore worked from `research/pares_ags/hits.jsonl` plus the other PARES hit files (31,297 ids,
  245 in nobility fonds, 147 not mentioned in any ledger or sweep README), and no date, legajo or image was checked live. Hit-list rows carry
  the image flag; descriptions do not show where the cipher word occurs, so every row says "description only".
- **Altamira, Medinaceli, Hijar**: no row of any of these fonds is in any PARES hit file for the cipher terms (Baena: only C.38 D.267-268,
  already catalogue 2443; Fernan Nunez: C.418 D.52 and C.1526 D.48 carry transcriptions, so not open). A fonds-limited search was not possible
  with PARES down.
- **Wayback CDX** returned 503 for the big query; paged by upload month (`cdxpage.py`, `cdxretry.py`): 560 PDFs (some months still failed;
  the May-Sep 2020 uploads, where the inventories are, came through). The 6 Nov sweep's 892 count is not reproduced.
- **ASNa**: archiviodistatonapoli.cultura.gov.it CDX 503; the two older beniculturali hosts have no Wayback PDFs. Archivi Nazionali was swept on
  6 Nov (0 ASNa units); not repeated.

## Palermo (`wbpa3.py`, `wbpa3_hits.jsonl`)
136 PDFs fetched by curl via Wayback and grepped (cifr, decifr, chiffr, zifra, "in codice", cifrario ...), the ones the 6 Nov sweep had not
done (`wbpa4.py` = same with a looser name filter for the 245 names excluded as admin/notarial/pergamene; written, **not run**), 5 fail/stall.
Real hits only: Misc. Arch. I.68 Torrearsa repertory (about 20 items in cipher, 1848-49; already leads 2209 and 2210),
Prefettura di Palermo Gabinetto 1926-45 "Cifrari" (admin keys, no ciphertext), Archivio Belmonte n. 987 "Lettere dirette a D. Ferdinando Monroy,
marchese di Garsigliano, in parte cifrate" (no date, no writer, key lead only), the ASPa school programme "Dai cifrari ottocenteschi alla firma
digitale" (SED_OFN 2020-21; shows a 19th-century cipher holding, no shelfmark). Everything else is "cifra" = figure/number or "decifrare" = read.

## Dedup
Not in the repo (known.py and grep): OSUNA C.1634, C.1635, C.1977, CP.56, CT.15, CT.18, CT.80, CT.260, CT.535; FRIAS C.635, C.1389, C.1815,
C.1887; MICHELENA C.18. Already covered and skipped: Osuna CT.2/CT.7/CT.11/CT.13 and C.1978-1982 (catalogue 747, albornoz1648, pares_ags rows 44-45),
Santa Cruz C.47-C.57 (pares_ags rows 19-23, 46), Frias C.28, C.61, C.81, C.1397, C.1442, C.128, Fernan Nunez C.418/C.1526, Baena C.38, Toreno C.71.
Skipped as noise: Cifre/Cifra surnames, "abecedario" indexes, "clave" archive keys, 19th-20th c. telegram files (Toreno C.7, Mendigorria C.38).
Not rows: OSUNA C.3456 D.109 (6449434, a king's cipher key given to Diego de Saavedra for Bavaria) and OSUNA C.538 D.99 (6065801) are key leads;
FRIAS C.642 D.74 "Tabla de descifrado de mensajes" 1802 (3949058) is a key table.

## Next, when PARES answers again
Open the 13 rows' first ids (4 s apart, one cookie jar each); check the `Osuna C.1634` neighbours (D.125-126 Alvaro de Bazan, D.133-148, D.322-347
Idiaquez as ambassador at Genoa 1574 onward) and C.1977 for filed decipherments.
