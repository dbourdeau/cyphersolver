# Archivi Nazionali portal, digitised-only cipher sweep (6-7 Nov 2026)

Follow-up to `research/sweep_2026-11_turin_chrome/` section 2. Scripts here: `an.py` (curl wrapper, 1.2 s between requests, browser UA), `harvest.py` (term runner, writes `units.json`, `counts.json`), `rec.py` (record page fetch, shows cipher-word context and `data-uuid-manifest`). `fonds_counts.json` has the per-fonds tally. Python needs PYTHONUTF8=1.

## The digitised filter
Unit search form field: checkbox `oggetti-digitali-un` ("Con oggetti digitali contenuti"). Working value: **`&oggetti-digitali-un=on`** appended to the unit search URL of the earlier README (`true` and `1` are echoed in params but ignored). Check: `cifra` 89 -> 51, `cifrari` 92 -> 1, `decifrazione` (ASVe 5 May 1547, not digitised) 1 -> 0.
Caveats found:
- Match is exact token (no stemming, no wildcard): `cifrata` 1 unfiltered but 0 filtered; `cifrate` likewise; `cifr*` 0. Multi-word terms behave as OR of words (noisy).
- "Contains digitised objects" includes units with digitised descendants (tree flag `hasDescendantsOggettiDigitali`; children via `...&p_p_resource_id=%2Ftree%2Fsearch%2Fchildren&..._DetailUnitaArchivisticaPortlet_entitaId=<id>`, returns `nodi`). The Milan Potenze sovrane Sforza folders (ua 20556045, 20555979, 20555991) pass the filter but only some child fascicoli are digitised (Galeazzo Maria 03.07, 03.08, 03.20; Bianca Maria 01.01, 01.04; GMS 01.05, 01.08), none of them the ones the description says hold cipher lines (n. 17 of 1455, n. 317 of 1467, nn. 69-186 of 1465-66). So no digitised Milan cipher letter was found.
- Record page `data-uuid-manifest` is the reliable per-unit test. Viewer token: `POST /o/external/api/ipac/security-context?sistemaUUID=...` (GET returns 405) gives a bearer token for the Teca viewer, but the manifest URL pattern is built inside the Teca iframe app and was not found; images were looked at in Chrome.

## Terms run (units, `denominazione-un` / `contenuto-un`, filter on)
cifra 51/36, cifre 26/23, "in cifra" 46/29, cifrato 8/1, cifrati 23/21, cifrario 18/17, cifrari 1/1, zifra 3/3, ziffra 7/7, "dispacci cifrati" 14, "lettere in cifra" 5/4, "lettera in cifra" 14/4, "carattere segreto" 7/7, "lettere segrete" 5/5, "scritto/scritta in cifra" 1, "en cifra" 3, "telegramma cifrato", "non cifrato" 1, "tavola di cifra" 1, nomenclatura 8, gergo 1, stenografia 1, decifrare 4, crittografico 1, code 3. Broad words (chiave 59/18, chiavi 32/28, segreta 10, segreti 8, caratteri 44/38, numeri, segno, segni, alfabeto 15, codice 136) were run only to look for cipher context, all noise. Zero hits: cifrata, cifrate, ciffra, ciffre, chiffre(s), cifrado/a/os, cifras, cyfra, cyfry, decifrazione, decifrato, decifrati, decifrate, crittografia, crittogramma, geroglifico, steganografia, contraccifra, cipher, encrypted, enciphered, zifre, sifra, "parole convenzionali". 1,536 distinct units collected, 131 on a cipher-type term, 50 on a cipher-specific term (cifrario/cifrari/cifrato/cifrati/zifra/ziffra/telegramma cifrato/dispacci cifrati).

## Where the 131 sit (fonds, units)
Trento Capitolo del Duomo 32 (17 keys + parchments whose "cifra" is a rent figure or dorsal numeral); Torino Stampa censurata 23 (WWI censorship, cipher telegrams with transcriptions); Lucca Diplomatico 22 and Pisa 12, Firenze 5, Bassano 5, Genoa San Giorgio 4, Siena, Cremona, Bari, Ascoli (all "cifra" = sum or numeral in parchment regests: noise); Rome Matteotti trial 11 (clear transcriptions of cipher telegrams, the Corriere italiano codebook); Milan Potenze sovrane 3 (see above); ASVe Patrimonio 3; Salvatorelli letters 2 (stylistic "cifra"); Chieti Matteotti 1.

## Candidates: none
`candidates.json` is empty. No digitised unit with ciphertext of a classical (pre-1950) system and no attached decipherment was found through the portal's descriptions. Looked at and dropped:
- ASVe Miscellanea documenti turchi n. 87 (ua 43015035, 23 Jan 1503): Senate letter on Santa Maura sent with a "non cifrato" copy (n. 86). Viewed page 1 of 3 in Chrome: clear Italian cursive, no cipher (the viewer then stalled, as the earlier note warned). The fonds is digitised; its descriptions give no other cipher hit (the 1547 "Decifrazione" unit is not digitised). Other Miscellanea hits ("lettere segrete", "segreta", "chiavi", "segni") are secret matters, not ciphers.
- ASVe Collegio, Lettere secrete registers 1436-38, 1484-85, 1500 (ua 42632391/397/415) and Senato Secreti registers: digitised, "secret" in the sense of confidential; not checked for cipher passages (reading them would be a page-by-page job).
- Trento keys (see key_leads.json), Matteotti, Torino censorship: keys/transcriptions, not rows.
- Genoa Archivio Segreto "Lettera segreta" 1351 (ud 17070045): description only, not cipher.
Prior art web search was not run for rows, as there are none.

## Fonds ranking (digitised, cipher-specific units)
1. Trento Capitolo del Duomo (17 keys), 2. Torino Stampa censurata (23 telegram/dispatch units, 1913-19), 3. Rome Corte di assise Matteotti (11, plus Chieti). Nothing earlier than 1546 and no diplomatic ciphertext.

## Not reached
Images of the Trento keys (descriptions and manifests only), the Torino telegram leaves beyond the earlier note, Collegio/Senato Secreti register pages, the Milan digitised fascicoli (no cipher noted in them). The portal's search covers only description text; digitised diplomatic series (ASVe Miscellanea turchi, Senato Secreti, Genoa Archivio Segreto, Milan Sforza) cannot be searched for cipher by this route unless the cataloguer wrote the word. Chrome was used once, for the ASVe 1503 viewer.
