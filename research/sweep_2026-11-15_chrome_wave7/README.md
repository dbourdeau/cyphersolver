# Chrome wave 7 (15 Nov 2026): Catalan archives portal and blocked-source probes

Brief: sweep Chrome-reachable sources not yet producing. **Result: one new source, Arxius en linia (Catalan archives portal), 11 leads (2843-2853), 9 promoted (2843-2851).**

## Arxius en linia (`arxiusenlinia.cultura.gencat.cat`)

Covers the Arxiu Nacional de Catalunya (ANC), the comarcal archives, Girona and other Catalan municipal and private archives. Earlier sweeps wrote "no item-level catalogue" for the ANC; this portal is item-level.
- **Route:** Angular app; in Chrome the page's own backend answers same-origin `fetch`: `https://backend.arxiusenlinia.cultura.gencat.cat/unitat/search/basic?text=<term>&cercarEn=QUALSEVOL&tipusDoc=TOTS&nomesDigitals=false&page=1&size=100&sort=data_inici_dt,asc&fromSearch=true` (JSON, `totalPages`, `results[].codiReferencia/titol/descripcio`). Images: `.../unitat/objects?codiReferencia=<ref>` gives `mediaUrl` (static host, opens in a Chrome tab). Detail pages are hash routes `#/cercabasica/detallunitat/<ref>` and need a page reload per record. Long loops past about 45 s time out the tool call but keep running in the page.
- **Terms run (38):** xifrat/-s/-ada/-ades/-ar, desxifrat/-ada/-ar, "en xifra", "clau xifrada", "carta xifrada", telegrama xifrat, cifra, cifrada, cifrado/-s, cifrar, descifrado, criptograma, criptografia, encriptat/-ada, nomenclator, cifre, chiffre, cipher, cypher and others. 1,411 distinct units fetched; most are noise (a notary surnamed Xifra, figured-bass 'acompanyament (xifrat)' in the Olot music archive, 'en cifras' statistics, street nomenclators). About 25 true cipher records.
- **Found:** 3 digitised numeric telegrams of the Interior Ministry, 1873 (Clave L.13, Clave N.34; seen on image), Carlist cipher letters of 1835 and 1842 (ANC1-1391), Philip IV's 'cartes xifrades' to Saavedra Fajardo (ANC1-53-T-702), two cipher letters to the marquis of Castelldosrius (ANC1-167-T-3773), typescript telegrams of 1936 with keys (ANC1-171-T-183).
- **Keys and instructions only (`key_leads.json`, not leads):** the Requesens 'xifrat general/particular' volumes 1562-76 (ANC1-960-T-891 to -895), the Alcudia cipher tables of 16 Jun 1840 (ANC1-1391-T-14), **'Instruccions per cartes xifrades a Antonio Ximeno', 1487** (ACPS211-95-T2-242, Medinaceli-Pallars; pre-1497, for the oldest-cipher search), Weyler 'Clau de xifrat' (ANC1-1458-T-62/63).
- **Excluded:** ANC1-1141-T-29/30 (Agullana 1595, decipherment by Marti de Riquer filed), ANC1-1391-T-87 and -113 (the letter reports a deciphered Metternich message), ANC1-1452-T-87 (Lagunilla 1879, 'telegrames desxifrats' filed), Vilaseca 1875 telegrams (ANC1-739: plaintext copies, viewed), 1940s Girona civil-government files (modern).
- **Left as leads, not promoted:** 2852 (ANC1-408-T-1891, 1937 Mexico embassy copies: not stated whether ciphertext), 2853 (ANC1-1-T-7519, 96 images not paged through).
- **Not done:** the portal's 'cifra' hits are mostly numbers; the 723 unclassified units of the Carlist collection were not read one by one (descriptions of the 357 Rocaberti items only mention cipher in the rows above).

## Blocked or already done (probes this pass)

| Source | Result |
|---|---|
| Finna (finna.fi) | Cloudflare 'verify you are not a bot' page in Chrome, not cleared; not retried |
| Archives Hub (archiveshub.jisc.ac.uk), Library Hub Discover (discover.libraryhub.jisc.ac.uk), Archives and Manuscripts of the National Library of Wales (archives.library.wales) | same Cloudflare check; stopped |
| Abhilekh Patal | CloudFront 403 in Chrome as well |
| PRONI eCatalogue | now at `apps.proni.gov.uk/eCatNI_IE/SearchPage.aspx` (Chrome form, 'cipher' = 39 hits); every hit was already in the ledgers (D572/17, D3030, T3158, HA/32/1/311) |
| Kalliope | opens in Chrome; 'chiffrierter brief' 14 hits, all already known (Wessenberg, Vadiana) |
| dLOC (Digital Library of the Caribbean) | full text of printed books and newspapers; cipher/cifrado filtered to Manuscripts/Archival/Correspondence: 0 usable rows |
| Arkivportalen (Norway) | 'chiffer' 908 hits, nearly all 20th-century military files; paging by URL does not render (SPA), not swept further |
