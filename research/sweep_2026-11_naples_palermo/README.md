# Naples (ASNa) and Palermo (ASPa) sweep, 6 Nov 2026

Scope: Archivio di Stato di Napoli and Archivio di Stato di Palermo (Carte Farnesiane, Esteri/Segreteria, Sommaria,
Collaterale, Borbone; Real Segreteria, Protonotaro, Tribunale del Real Patrimonio, viceroy letters), by every route
that answered from this machine. **Result: 2 candidate rows, both description only; no digitised cipher found; no
images seen.** Honest summary: neither archive's own site can be reached from here, and the one portal that does
answer (Archivi Nazionali) carries only fonds-level records for Naples and a handful of fonds records for Palermo.

## Hosts and what happened (6 Nov 2026)

| Host | Result |
|---|---|
| archiviodistatonapoli.cultura.gov.it | resolves (2.42.229.31), TCP accepted, TLS handshake reset every time (curl, 20 s). **Chrome (Claude in Chrome) also fell back to `chrome://newtab`** (the pane never loaded the page; same as the 4 Nov sweep). Not retried further. Appears to refuse non-Italian clients. |
| asna.cultura.gov.it, patrimonio.archiviodistatonapoli.it | no answer / no DNS |
| archiviodistatopalermo.cultura.gov.it, www.archiviodistatopalermo.it | no DNS (Palermo's real host is `saassipa.cultura.gov.it`) |
| saassipa.cultura.gov.it (Palermo, SAASSIPA, inventories) | resolves (2.42.228.128), times out. Not reachable. |
| digitalibrary-saassipa.cultura.gov.it (Palermo digital library, DSpace-CRIS) | no DNS from here (also NXDOMAIN at 8.8.8.8); Wayback holds only the empty Angular shell, no item pages. |
| inventari-san.cultura.gov.it | no answer; the two SAN inventory PDFs a web search surfaced (ids 2359 and 746, Farnese) are not in Wayback. |
| asmo.cultura.gov.it (Modena) | answered on 6 Nov morning (retry sweep), not now; PDF read via Wayback. |
| archivinazionali.cultura.gov.it | **works by curl** (see the Turin sweep README for the endpoints). Used here. |
| web.archive.org | works with **curl** (urllib got 429 from the same IP while curl got 200: use curl). One request per 9 s; stalls on some large PDFs. |
| pares.mcu.es | answers (`ParesBusquedas20/catalogo/description/<id>` works); not swept again (see below). |

Chrome was only needed to confirm the ASNa block; nothing in this sweep was read through Chrome.

## Routes used

1. **Archivi Nazionali unit search** (`denominazione-un` and `contenuto-un`, paginated 50) for 27 terms: cifra, cifre,
   cifrata/e/o/i, cifrario/i, zifra/e, ziffra/e, ciffra/e, chiffre, decifrazione, decifrato/a/i, cifrare, cifrado,
   descifrado, crittografia/o, criptografia, cifras, "in cifra", "lettere cifrate", "chiave cifrata", "cartella cifrata";
   then nomenclatore, "scrittura segreta", "segni convenzionali", telegramma/i cifrato/i, "carattere cifrato", "alfabeto
   cifrato", chiave, cifrario. 287 distinct units from the first batch; the holder is in "Conservato/vigilato da".
   **Zero units held by Archivio di Stato di Napoli; one by Palermo** ("Appunti di storia", Carte Minghetti, noise).
   The portal has only fonds-level records for ASNa (6,210 fonds hits for the archive name, 295 units, mostly Palermo
   Diplomatico/Pergamene Trabia and Lucca).
2. **Archivi Nazionali fonds search** (`patrimoni-documentari`, `keywords=`) for 18 terms, 227 distinct fonds; 17 with
   Naples/Palermo/Sicily in the record. Opened 8: only two real hits (below); the rest are "cifre" = numerals, a
   Venice despatch series for Naples (ASVe Senato, Dispacci, Napoli: "cifre" in the drawings), a 1909-39 Messina
   prefecture "cifrari" line, a Corleone sub-prefecture 1872-1929 "corrispondenza riservata e cifrata" line.
3. **Global search** (`keywords=`): Carte Farnesiane (11: Farnese family Lettere 1539-1723, Borbone family 1713-1890,
   Casa e corte farnesiana: fonds records only), Real Segreteria Palermo, Protonotaro: fonds only; "Guide e inventari"
   hold 3 "cifra" hits, none ASNa or ASPa.
4. **Wayback copies of the Palermo SAASSIPA inventory PDFs** (892 PDFs in the CDX; 210 selected by name, about 170 fetched and
   grepped with pdftotext for cifr/decifr/chiffr/cypher/zifra/"scrittura segreta"/"alfabeto segreto"; the fetch ran
   alphabetically to "Misc. Arch. I.66", then a second pass took Real Segreteria, Protonotaro, TRP, Luogotenente,
   Consulta, Ministero, Cancelleria, Maestro). Hits are in `wbpa_hits.jsonl`; texts in git-ignored `_dl/wb/`.
5. **Web searches** (about 8, Italian/English/Spanish) for ASNa and ASPa cipher material, Carte Farnesiane ciphers, Maria
   Carolina's letters, and the Naples/Sicily viceroy ciphers. Found only published or Simancas material (below).
6. **ASE Modena, Carteggio ambasciatori, Napoli** inventory (Wayback copy of the asmo.cultura.gov.it PDF, 2,500 lines):
   one cipher entry ("congiunta una cifra"), a key.
7. dedup: `known.py` for napoli, naples, palermo, sicilia, Farnese, "Maria Carolina", the Genoa/Naples EST legajos.

## Candidates (`candidates.json`, 2 rows; `make_candidates.py` writes them)

1. **Maria Carolina of Naples and Sicily, three letters partly in cipher with "parziale decodificazione", 1809, 1810
   (Palermo), 1812** (private owner; Archivi Nazionali fonds record ca_9568899; Soprintendenza of Emilia-Romagna,
   declared of historical interest 25 Oct 2018). Two earlier letters (1794) announce a cipher sheet not attached. Best
   row of the sweep as a historical object (the queen's cipher in the Palermo exile), but **no images, private owner**,
   partial decodification on the letters. `needs_archive_scan: yes`.
2. **ASPa Miscellanea archivistica II serie n. 262**, "Lettera in codice e in cifrato" of the early 19th century (the list
   dates the entry 1861). No decipherment mentioned (the neighbour, n. 263, has one). `needs_archive_scan: unknown`
   (the Palermo digital library may hold scans; host not reachable).

Both are description only (`seen: "catalogue"`), neither vetting-ready.

## Key leads (`key_leads.json`)

Misc. Arch. I n. 142 "cifrario dei Gesuiti" (ASPa); Misc. Arch. II n. 263 (18th-c. Bourbon-subversives cipher with
alphabet and typed transcription, so read); Mazzini's 1860 advice on changing the cipher (II n. 202); the Palermo
Prefettura's "Cifrario anarchico" (Gabinetto 1860-1905, 1904 bundle, item 8.9) and a long run of prefecture telegraph
cipher keys 1862-1901, 1906-25, 1946-65 (administrative, no ciphertexts); Corleone sub-prefecture 1922-26; Modena ASE
Napoli "una cifra".

## Not found / dead ends

* **ASNa Carte Farnesiane**: no item-level cipher listing reachable. The cipher fasci are already in the catalogue
  (via Cauchie and Van der Essen 1911 and the ia_pass2_c sweep: "Ask ASNa for the fascio list"). The new SAN Farnese
  inventory PDFs (inventari-san ids 2359 and 746) surfaced by web search could not be fetched.
* **ASNa DECODE block** (R9532-R9590): already in the repo or Decrypted (4 Nov sweep).
* **Real Segreteria Incartamenti repertories, Protonotaro, Tribunale del Real Patrimonio (incl. Lettere viceregie),
  Consulta dei Reali Domini, Luogotenenza Polizia repertories 1819-1855**: grepped through Wayback, no cipher mention
  beyond the 1848-49 Torrearsa items already leads 2209/2210 (Misc. Arch. I.65-I.68; I.68 was not fetched, I.65-I.67
  show nothing new).
* Published, so not open: Bucuré, "Nápoles 1547: cartas cifradas y secretos de Estado" (Estudios Románicos 2025), four
  Naples letters of 1547 from AGS Estado leg. 1037, cipher analysed and edited; Parisi 2020 (Frederick of Aragon 1497);
  Della Casa-Farnese 1546-47 (Unimi edition, appendix of cipher letters).
* **PARES (AGS) Naples/Sicily viceroy items** exist in `research/pares_ags/hits.jsonl` (e.g. EST,LEG,3595,83 Paterno 1638;
  3598,150 and 222 Medina de las Torres 1642-43; 1412,172/175/184 Doria 1579; 3637,33 and 39 Caracena/Onate 1650-51,
  all "no descifrada" or "carta cifrada" hits, images online) but they sit in the Estado *Genoa* negotiation legajos, are
  not in the repo (known.py: no hit), and belong to the PARES sweep. PARES description pages answered today; I did not
  open them or the images (outside the Naples/Palermo archives). They are the best Naples-viceroy material with images
  online if the main session wants a follow-up.

## Not reached

ASNa and ASPa item-level catalogues (blocked); the 100-odd SAASSIPA PDFs of the selected 210 not fetched (the stall at
Misc. Arch. I.68, then a time stop; mostly the S-Z private families and Tribunale series); the remaining 680 PDFs of the
892 were excluded by name (notaries, personnel, state-civil registers, admin). Sicilian regional portals (SIAS,
Regione Siciliana libraries), Monreale/Messina/Catania archives, Archivio Pignatelli-Monteleone and Sommaria/Collaterale
specifics: no route found. For COVERAGE.md: Naples and Palermo are "inventory level only; both own sites blocked from
non-Italian IPs; Palermo inventories reachable through Wayback".

## Scripts

`an.py` (Archivi Nazionali unit search helper), `harvest.py` (unit sweep), `fonds.py` (fonds sweep), `wbpa.py` and
`wbpa2.py` (Wayback fetch and grep of the Palermo PDFs, curl-based), `make_candidates.py`.
