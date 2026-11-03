# Hispana sweep (2 Nov 2026)

Hispana (hispana.mcu.es) searched in the user's Chrome (Claude in Chrome), own tab, VPN on a UK exit. **Not blocked:** no 429
this time (the 28 Oct sweep, `research/bne_hispana`, got 429 on every request). The site search form is a POST
(`resultados_busqueda.do`, field `busq_general`; pages by `?id=<search id>&posicion=<n>`, 20 per page), so `?texto=` in the
URL does nothing. Searches ran as same-origin `fetch` from the tab, one request every 2.5 s; no check or CAPTCHA appeared.
Cookie banner on memoriademadrid.es declined ("Rechazar todas").

## Terms (any-field search, up to 8 pages of 20 per term; 4 for the second batch)
cifrada (99), cifrado (456), escritura cifrada (10), descifrado (95), cifrario (4), zifra (12), carta cifrada (27),
clave cifra (97), cifra (8607, capped), en cifra, cartas cifradas (16), contracifra (4), descifrar, nomenclator,
abecedario cifra, "escritura en cifra", criptografia manuscrito, carta en cifra (162), xifrat (54), cifras secretas (2),
real cédula cifrada (13), cédula cifrada, Conde de Añover cifrada (11), carta cifrada Gonzalo Fernández de Córdoba,
cifrada Fernando II, parcialmente cifrada, en parte cifrada, cifrada Felipe II, cifrada Carlos V, cifrada embajador,
minuta cifrada, despacho cifrado (4). About 700 distinct records; the list is dominated by theses, music ("cifra" =
guitar tablature) and printed books. Filter: dated before 1951, not music/print/photo, strong cipher term: 182, of which
about 60 manuscripts or letters.

## Result
- Most manuscript hits are the BNE items already in `bne_hispana` (Granvela series, Sessa, Nájera, Mirabel, Dormer ...)
  and the RAH Morillo and Isabel II records: not repeated.
- **New: the Philip III → conde de Añover cédulas (Biblioteca Histórica, Madrid, Memoria de Madrid), 1610-11, 11 records.**
  Eight have the decipherment bound in (closed, read at the time); four have none (one row, opened, page 2 viewed).
- Held back as unvetted: four Maqueda letters of Ferdinand II to the Gran Capitán (Biblioteca Virtual de Defensa, 1503-06;
  CNI published a decipherment in 2018, which letters it covers not checked) and UCM BH MSS 440 (1852 copy of the 1591
  Antonio Pérez intercepts, only the title page seen).

## Not reached
Hispana's 8,607 "cifra" hits beyond page 8; the 1909-1911 "Carta - Remitente Ministerio de Cultura" records (not opened,
probably unrelated); Biblioteca Digital de Castilla y León was not swept separately (it is reachable through Hispana
records); no web search on the BNE-known series (already leads). `research/COVERAGE.md` named in the task does not exist
in this checkout. Tomokiyo's Philip III page was not read (not held locally).
