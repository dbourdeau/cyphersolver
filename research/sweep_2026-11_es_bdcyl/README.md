# BDCyL sweep (2 Nov 2026)

Biblioteca Digital de Castilla y Leon (bibliotecadigital.jcyl.es), searched in the user's Chrome (Claude in Chrome), own tab,
same-origin fetch of `resultados_busqueda.do?busq_general=<term>`, one request per 2.5 s, 20 queries. No check, no login, no CAPTCHA.

## Terms
The host answers (HTTP 200, earlier timeout in `research/bne_hispana/jcyl.py` not repeated). Native BDCyL hits:
- cifrada, descifrado, criptografia, contracifra, "cartas cifradas", "carta reservada": 0 native records.
- cifra / "en cifra": 3, all printed (Pedro de Ledesma, Summa, Salamanca 1603-1621; "cifra" = summarise).
- cifras: 3, printed (Dozy 1877; Camargo y Salgado 1642; a Santa Maria la Real de Nieva circular 1799), not ciphers.
- clave: 19, printed or modern (Martin Gaite diary, Flores' Clave geografica, Clave de los suenos ...), none a cipher.
- cifrado, nomenclator, abecedario: 0 native list.
- jeroglifico: redirected to one record (Documentos para una historia de la familia Juan / Codice Centelles): hieroglyphic
  emblems, not a cipher.
- The Europeana pass-through block under each search (e.g. "cifrada", 31) repeats RAH Morillo/Enrile/Herrera 1817-20 records,
  already leads/printed (see `research/bne_hispana`); nothing new.

## Result
0 candidate rows. BDCyL carries no item described as ciphered. Not reached: BDCyL full-text search (separate form,
not queried), Hispana and BVPB (HTTP 429 in earlier pass; not retried), BNE Digital (not touched, by instruction).
`candidates.json` is an empty list.

## Addendum: full-text pass (2 Nov 2026, UK VPN, second Chrome tab)
The catalogue form posts to `/es/consulta/resultados_ocr.do` (fields `busq_general`, `general_ocr=on` for full text,
`busq_idclasiftipodoc`, `secc_*`); a GET on `resultados_busqueda.do` only returns the Europeana block, which is why earlier
searches looked empty. Same-origin POST works and the host did not block. About 30 requests at 2 s.
- Document type "Manuscritos" (DGB8208) is the Carmen Martin Gaite archive (20th c. notebooks): cifr*/clave/descifrar* hit only
  her diaries. No historical cipher manuscript is described as ciphered.
- Full text (OCR of printed books): "carta cifrada" 94, "en cifra" 2,466, "carta en cifra" 18, "cartas cifradas" 12,
  "escrito en cifra" 28, contracifra 24. Read: contracifra (dictionaries, Covarrubias, Antonio Perez editions, sermons),
  "carta en cifra" (CODOIN, Danvila's Comunidades 1897-99, Pellicer 1668, Foronda's Estancias de Carlos V, Arribas Arranz seals
  with a 1503/1506 Gran Capitan cipher letter noted only as a seal description), "cifrada" + Paleografia (visigothic cipher
  script, Munoz y Rivero 1919, Garcia Villada 1923). All are printed books, i.e. edition/literature sources, not ciphertext.
  "carta cifrada", "escrito en cifra", "cartas cifradas" were counted but their hit lists not read item by item.
- Result stays 0 rows. Use: Danvila vol. III p. 73 and CODOIN XXXI p. 155 as printed-edition prior art for Comuneros /
  Philip II cipher letters if a target arises.
