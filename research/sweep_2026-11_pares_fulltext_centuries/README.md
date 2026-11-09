# sweep_2026-11_pares_fulltext_centuries (9 Nov 2026)

Result: **0 rows** in candidates.json (`[]`). Nothing padded.

## Route
PARES by curl, no 429 and no non-200 (about 330 requests, `run.py` = pares_ags `sweep.py` session recipe, 4 s delay plus
jitter, own hits.jsonl/progress.json). Facet `idFI=<century>` (start-date century) works for 15, 16, 17, 18, 20.
`all.sh` and `all2.sh` hold the term lists. Terms with 0 results return the PARES page "No se han encontrado datos"
(logged as an error page in progress.json: that is a genuine zero, not a block).

## Runs (facet x terms; 5,484 hit rows, 3,000+ unique ids)
- Batch 1, idFI=16/17/18/20: cifra, cifras, cifrado, cifrada, cifrados, "en cifra", descifrado, descifrada, "carta cifrada", clave, criptograma,
  jeroglífico, caracteres, números, contraseña, "papel cifrado". Zero results (any century): criptograma, jeroglífico, números, contraseña, "papel cifrado" (the
  accented forms; the unaccented forms were run in batch 2). cifra 47/51/58/73 (16/17/18/20), cifrada 326/183/13/4, descifrada 313/109/4/0, "en cifra" 41/30/52/58,
  clave 10/102/468/288 (noise: Hernando Clavé, Clavé street, "key" of an archive).
- Batch 2, idFI=15/16/17/18/20: zifra, zifras, cifrar, contracifra, abecedario, jeroglifico, numeros, contrasena, descifrar, descifrados, cifre, chiffre, "en zifra", plus
  cifra/cifrada/cifrado for 15th c. Zero for zifra(s), "en zifra", chiffre, contracifra (except 2 in 18th c.).
- Per-fonds runs not done as separate searches: the century facets already return every row for the cipher terms (totals fully paged; only "cifrada" 16th c.
  returned 326 of 330 because of PARES's unstable paging), so an `idA=` sub-facet could only re-list the same rows.

## Diff against earlier hit files (pares_ags, pares_cifra, spain_nobility_aca, diversos_19c, others)
Core cipher terms (cifra, cifras, cifrado, cifrada, descifrado, descifrada, "en cifra", "carta cifrada") per century gave **0 new ids** for 16th-18th c.:
the October term-only runs had already reached every row. (The `idFI=19` runs of the previous agent were new only because 19th c. was never faceted.)
New ids came only from: cifra (20th c., 15 rows, all surname "Cifra"/news agency CIFRA/tax "cifra"), cifrados (about 50, mostly Euzkadi/Santander
telegram files 1936-37 without images, Exteriores 1914-19 radiotelegraph files), clave and numeros (thousands, noise), caracteres, cifre/Cifre (Valencian surname),
abecedario, jeroglifico (Inquisition drawings 1662, not cipher).

## Opened and excluded
- AGS PTR,LEG,1,96,5 (1521, Comunidades; "originally enciphered in a letter of credence", id 12980846): image is a clear-text relation (a deciphered copy; the page carries
  a modern ACA stamp), no cipher groups.
- AGS EST,LEG,1934,10 (Vivas de Canyamas, Genoa 1618; the 7 letters EST 1934 nos. 10-27 hit on "cifrados" = the stolen cipher keys of Juan de Ossa): image plain text, no groups.
- AGS EST,LEG,1368,183 (Lope de Soria to Charles V, Sept 1531, hit on "descifrados"): contemporary decipherment, clear text with the paragraph marks A, B.
  Lope de Soria's archive is catalogued already (catalogue.json, RAH).
- AHN OSUNA,CT.11,D.2 (Penaranda to Albornoz, 1649): "Original y parrafos descifrados", decipherment filed. Excluded.
- Mº_EXTERIORES_H 1675/2482/2568 etc. (1905-19, "telegramas descifrados", 20th-c. telegram administration), PS-SANTANDER/GIJON/BARCELONA telegram files (no images online;
  20th-c.), INCORPORADOS 1466/1462 (1938-39 key correspondence, no images), FC-CAUSA_GENERAL 1564 Exp.20 (clave "Luci" 1937, telegrams captured; key-only/espionage dossier,
  not a letter lead), DIVERSOS-JOSE_GIRAL 12 N.11 and 1 N.83 ("clave" = slang/internal): not leads.
- Surname/noise: all "Cifre", "Cifra", "Clave"/"Clave" hits.

## Conclusion
PARES full text per century is exhausted for the cipher vocabulary: the century facets add nothing for 16th-18th c. beyond the term-only runs, and the only new
cipher-flavoured rows are 20th-c. telegram administration. Remaining unsearched ideas (not run here): descriptions that say "en guarismos", "en numeros" with images (the
noisy `numeros`/`clave` rows, 2,000+ in hits.jsonl, were screened by title regex only), and units whose description is empty, which full text over PARES descriptions
cannot reach (the Genoa 1618 and Soria 1531 letters show that empty-description units can hold cipher or its decipherment: only an image sweep of a series reaches them).
