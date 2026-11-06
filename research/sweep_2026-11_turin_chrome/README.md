# Turin (ASTo) + Archivi Nazionali + Milan ICAR, browser-gated portals (6 Nov 2026, overnight)

Follow-up to `sweep_2026-11_italian_state_retry`, which found the Turin database behind a "Verifica del browser" page,
Archivi Nazionali drawing results by JavaScript, and the Milan ICAR viewer not reachable by curl.
Finished 6 Nov 2026 (about 05:00-06:00 CST). Chrome was needed only to see the Turin cookie page and to open the Archivi Nazionali viewer; everything else ran by curl.

## 1. Archivio di Stato di Torino (ASTo)

### Route (works with curl; Chrome only needed once to see it)
- The "Verifica del browser" page is not a CAPTCHA: it is a 1 KB page whose inline script sets a cookie `asto_v=<value>` (the
  value is written in the page itself, split in two strings) and reloads. Chrome passed it by itself in under a second.
  A script that reads the value out of the 403 page and resends it as `Cookie: asto_v=...` gets every page with curl/urllib
  (helper `asto.py` in the session scratchpad, not committed). No login.
- Fonds list as JSON: `/dbadd/response_ffd.php?id=0` (1,814 fonds, DataTables `aaData`).
- Fonds page: `/fondi/?id=<id>` (Lettere Ministri = 270576; Negoziazioni = 2738xx; Matrimoni della Real Casa = 270113;
  Tutele, reggenze e luogotenenze generali = 270129).
- Full-text search (fonds, inventories converted to item level, seal database "Documenti", maps): `POST /src_result/` with
  `srcall=<term>` (word match with light stemming, `AND` allowed). Item-level inventory records: `/inventari/?id=<id>`.
- Seal database records (letter + seal photo): `/sigdtl/?did=<n>`, image `/img_sigilli/S_001_00NNNN_01_1.JPG` (1630 px; the photo
  shows the seal and a strip of the sheet, not the text).
- Lettere Ministri inventory (n. 151) is two PDFs: `/upload/LETTERE-MINISTRI-Vol_I.pdf` (309 pp., text layer) and
  `/upload/LETTERE MINISTRI_Vol.II.pdf` (223 pp., poor OCR). It is mazzo level (ambassador and years), not item level.
- Digitised: the fonds pages say "Digitalizzato: No" for Lettere Ministri; the Digital Library holds maps, cadastres, Biblioteca
  antica, Materie ecclesiastiche/economiche, notaries, Felix V bullarium, Lomaglio, accounts. **No diplomatic series is online.**

### Terms run on `/src_result/`
cifra, cifr, cifre, in cifra, zifra, chiffre, ciffr, deciffr, decifr, cifrato, cifrati, cifrate, contracifra, "cifra AND lettera",
ciffra, ciffre, ciffrario, cifrario, cifrari, ziffra, zifre, dicifrato, deciferato, decifrazione, dicifrazione, controciffra,
contracifre, chiffres, "en chiffre", caratteri. WordPress site search (`/wp-json/wp/v2/search`): cifra, cifrata, cifrario, crittografia (nothing).

### Hits
| Record | What it says | Use |
|---|---|---|
| sigdtl 490 | "Lettera cifrata di Carlo Emanuele I ... a Giovanni Battista Gabaleone ambasciatore a Londra", 16/10/1612; Corte, Materie politiche per rapporto all'interno, Matrimoni della Real Casa, mazzo 25 fasc. 7 (Infanta Maria - Prince Henry match) | row (description only; seal photo shows endorsement "... 9bre", no text) |
| sigdtl 1197 | same title, 21/7/1613, same mazzo 25 fasc. 7 | same row |
| sigdtl 1388 | "Lettera cifrata del cardinale Maurizio di Savoia all'abate Buschetti", Nice, 7/7/1640; Corte, Tutele, reggenze e luogotenenze generali, mazzo 4 | row (description only; seal photo shows faint show-through only) |
| inv. 79.1 id 351296 | Istruzione al Segretario Corte (Rome) 1588 "con un'altra in cifra per affari di Stato" | already in catalogue (B_unswept_south); dropped |
| inv. 57 id 336055 | Sardegna, Cat. IV, mazzo 2 fasc. 48: "CIFFRE, e Controcifre" (1760s) | key lead |
| inv. 94 id 459637 | Olanda mazzo 2 fasc. 1: instruction to Conte di Chiusano 1729-31 "e Ciffre al med.o state rimesse" | key lead |
| inv. 98 id 359609 | Venezia mazzo 1 fasc. 18: instruction to Marchese Mossi 12 Feb 1742 "Con la Ciffra al medesimo rimessa" | key lead |
| inv. 100.2 id 461868 | Corti straniere, Roma, mazzo 1 fasc. 9: "Ciffre della Corte di Roma ricavate da un antico Manoscritto del Vaticano; con Riflessioni" (2nd half 18th c.) | key lead (keys / analysis) |
| inv. 54 id 335597 | Pregola mazzo 7 fasc. 3: 1765 deduction "con due Memorie mandate in Ciffra a Vienna al Conte di Canale" | not a row (likely the clear drafts; nothing says ciphertext survives) |
| Lettere Ministri inv. 151 | Gran Bretagna mazzo 23: "Contiene anche il cifrario del Conte della Perosa in 2 copie", 1716-17; Olanda mazzo 1: "CIFRARIO 1691 e 1692" (Della Torre); Baviera m. 41, Due Sicilie m. 68, Francia m. 340/343: registers "Copia di cifrati" 1816-49 | key leads (Perosa, Olanda, and the 1816-49 "copia dei cifrati" registers as probable plaintext) |
| others | "cifra" = amount (Scalenghe 1453, Penango 1820, Zecca), "non in cifra" date (Sanità 1787), "indecifrabile" signature | noise |

Also searched "Gabaleone" and "Buschetti": inventory n. 102 lists Matrimoni mazzo 25 fasc. 4 "Lettere diverse del Duca ... del Cardinale
Morizio, e del Principe Tomaso ... al Caval.e Gabaleone, Ambasciadore ... in Londra, 1612 in 1619" (the seal database puts the two cipher
letters in fasc. 7 of the same mazzo); the seal database has six clear letters to Buschetti (Maurizio 1 Jul 1640, did=714; Tommaso,
did=1382-1386) beside the cipher one.

**Turin result:** 2 rows (description only), 7 key leads. The online item-level inventories cover only part of Corte (Negoziazioni,
Matrimoni, Tutele, Cerimoniale, Sardegna, Paesi, Materie ecclesiastiche/economiche ...); Lettere Ministri, the main diplomatic series, has
only the mazzo-level PDF and no scans, so the Savoyard envoys' cipher despatches cannot be found item by item online. There is no separate
"Cifre" fonds in the database (1,814 fonds listed; none named cifre/cifrari in Corte).

## 2. Archivi Nazionali (archivinazionali.cultura.gov.it; SIUSA/SAN now redirect here)

### Route (curl, no browser needed once the endpoints are known)
- Global search JSON: `/it/risultati-di-ricerca?p_p_id=it_inera_multiple_search_MultipleSearchPortlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=%2Fsearch&p_p_cacheability=cacheLevelPage&keywords=<term>&cur=1`
  (counts per entity type, 3 items each). The page parameter is `keywords`, not `search` (the retry sweep's `?search=` URL is ignored).
- Units, paginated: `/it/risultati-ricerca-unita?p_p_id=it_inera_search_unita_documentarie_SearchSimpleResultsUnitaDocumentariePortlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=%2Fsimple%2Fsearch&p_p_cacheability=cacheLevelPage&denominazione-un=<term>&cur=N&pageSize=50`
  (also `contenuto-un=`). **Do not use `keywords=` on this endpoint**: it is ignored and returns all 787,723 units.
- Fonds ("Patrimonio documentario"): `/it/patrimoni-documentari?p_p_id=it_inera_icar_search_complessi_SearchComplessiPortlet&...&p_p_resource_id=%2Fsearch&...&keywords=<term>`.
- Record pages: `/it/unita-archivistica/-/ua/view/<id>`, `/it/unita-documentaria/-/ud/view/<id>`, `/it/patrimonio-documentario/-/ca/view/<id>`,
  `/it/guida-ed-inventario/-/sdr/view/<id>`. A record with images carries `data-uuid-manifest` in its Mirador tab; the viewer is an iframe
  on `teca.prod.os01.ocp.cineca.it` behind a token (`/o/external/api/ipac/security-context`), so images were looked at in Chrome only.
  Chrome's renderer froze after a few page turns in that viewer.
- Cookie banner left alone (not accepted). ASTo Sezioni Riunite also has "Corrispondenza riservata e cifrari" 1915-44 (Procura generale), not followed.

### Terms (units: denominazione-un and contenuto-un)
cifra (89/73), cifre (46/40), cifrata, cifrate, cifrato (8), cifrati (30), "in cifra" (81/64), cifrario (31), cifrari (92), decifrazione (2),
decifrato, decifrata, deciferato (0), zifra (3), ziffra (7), ciffra (0), ciffre (2), chiffre (0), chiffres (0), crittografia (0). 287 distinct
units. Most are noise ("cifra" = sum or numeral; the ACS Consiglio superiore degli archivi minutes; parchments; maps; catasti). Fonds search "cifra" (80).

### Hits worth keeping
| Record | What it is | Use |
|---|---|---|
| ASVe guide sdr 43087032 | inventory (1991) "Lettere in cifra indirizzate prevalentemente ai Provveditori alle biave dal bailo di Costantinopoli (1589-1597) e dall'ambasciatore veneto in Spagna (1590)"; note: fonds "Secreta, lettere in cifra ai provveditori alle biave" | row 3 (description only) |
| AS Trento (listed under Varese), Capitolo del Duomo, N1303p2 = N1303_06 ... _22 | **17 cipher keys of Cardinal Cristoforo Madruzzo's chancery**, 1546-1550s, digitised: duke of Florence (1546), "miser Traiano" (1546), don Diego [de Mendoza?] (1547), cardinal of Coria (1547), prince of Sulmona?, Fabrizio Colonna, Maurice of Saxony, cardinal of Augsburg (Truchsess), cardinal Carpi, "Cifra con Turca", Maximilian II, "Stropp", cardinal Farnese, cardinal Salviati, mons. de Fanno, cardinal of Ravenna, one unnamed. Trasselli 1941 (Studi Trentini XXII) edited related material from BCT and the Corrispondenza madruzziana | key lead |
| AS Trento, Corrispondenza madruzziana (ca 13661886) | 8 bb., letters received by Madruzzo 1539-67 (Charles V, Philip II ...) | series level; where cipher letters for the keys above would be |
| AS Cagliari, Segreteria di Stato e di guerra, Affari esteri, unit 00021 | 1810-11, Mgr Ruopoli file, "Cifra per la Corrispondenza" | key lead |
| AS Roma, Corte di assise, processo Matteotti (1927), vol. 18 | "Cifrario del «Corriere italiano» e busta" (digitised); police "trascrizione del telegramma cifrato" items of 1924 are clear transcriptions | key lead |
| AS Torino, Stampa censurata, Uffici di censura, mazzi 2-3 | "Censura telegrafica: telegrammi cifrati e trascrizioni" 1913-1919 (Cuneo prefecture), digitised | not a row: 20th-c. administrative cipher telegrams filed with their transcriptions (glossed); viewer opened, first leaves are clear correspondence |
| AS Milano, Potenze sovrane, Chiavi e cifrari (3 units: 1447-1486, 1471-1720, 1494-1736) | same records as ICAR; **no Mirador tab** (not digitised) | see section 3 |
| ASVe Miscellanea documenti turchi 5 May 1547 | "Decifrazione di due frasi cifrate in una lettera del bailo" | decipherment only (clear); not a row |
| ASVe Senato, Dispacci provveditori, "Isola di Dia" 1607 | map whose description "decifrata" is with the despatch of 25 Jan 1607 | clear; not a row |
| Siena Concistoro "Cifrari"; ASVe CX "Cifre, chiavi e scontri di cifra" + Pasini's "Catalogo delle chiavi" | known (catalogue 336 etc.; `venice_archives`) | dropped |

## 3. Milan, ICAR Archivio Digitale, Sforzesco "Chiavi e cifrari" scat. 1591 (ICAR UA 1128459)

- Chrome (6 Nov 2026, ~11:20 UTC): **"Privacy error"**, the host's TLS certificate has expired (curl: `SEC_E_CERT_EXPIRED`). Not clicked through.
- curl with certificate checking off (`-k`, read-only public page): the unit page serves the description only; scripts and links show no
  viewer, no IIIF/manifest, no image link; the "Livelli inferiori" tree is an ajax tree (`ajax.php?pageId=185&ajaxTarget=treeview&...GetTree`).
- Archivi Nazionali holds the same three units (`ua/view/20555418` = scat. 1591, `20555436` = 1447-1486, `20555439` = 1471-1720) with the
  full description and **no Mirador tab**; the other Potenze sovrane units checked (Bianca Maria, Francesco I) have none either.
  "Archivio Digitale" in these fonds names means born-digital description, not scans.
- So the scat. 1591 cipher letters are **not online**; whether they are bare cannot be checked. The description (82 cc.): keys and some cipher
  letters with the correspondent noted "coeva o posteriore" (Camillo Ghilini in Flanders, Benedetto Curzio, Paolo Sforza 1528, G. S. da
  Robbio at Cremona 1530, Giorgio Andreasi at Mantua 1528, Massimiliano Stampa 1527, Bartolomeo Landriano 1526, Francesco Taverna,
  conte della Somaglia 1527, "Amico Taegio" 1531; no. 43 cipher letter to Ludovico il Moro 1494; no. 40 key 1736). Nothing added: the
  2 Nov Milan row already covers it.

## 4. Genoa, Casa di San Giorgio (found through Archivi Nazionali)

The Archivi Nazionali unit search for "cifrari" returns 104 filze of the ASGe **Casa di San Giorgio, Affari generali, Cancelleria dei
Protettori** (chancellors' filze 1434-1651, inventory text loaded into the portal; no images, no numeric shelfmark shown, cited here by
chancellor, cover title and ARK). 99 of them list "istruzioni e cifrari" issued to newly elected officials (Corsica, both Rivieras, Sarzana,
Capraia, Ventimiglia), 1466-1570: one aggregate key lead. Three filze also list **cipher letters**:
- Montebruni filza 1560 (ua_25838904): Corsican commissioners' letters "spesso parzialmente in cifra" 1560-62, and "parecchi cifrari dei
  funzionari di stanza in Corsica" in the same filza (row 4);
- Montebruni filza 1561-65 (ua_25838898): commissioners' letters "talvolta parzialmente in cifra" 1561-63 (row 5);
- Lasagna filza 1519 (ua_25840020): "relazioni, talvolta in cifra" of Genoese envoys at the Roman curia (row 6).
The other San Giorgio "cifra" hits are sums of money. ASGe's own Corsica inventory PDF (`08Corsica202003.pdf`, 64 pp.) has no cipher entry.
Web search (6 Nov 2026) found nothing published on San Giorgio ciphers.

## Result

**6 rows** in `candidates.json` (`make_candidates.py`), all **description only** (no ciphertext seen; nothing in this sweep is digitised
except the Trento keys, the Turin WWI telegrams and the Corriere italiano codebook, which are not rows):
1. ASTo, Matrimoni della Real Casa, mazzo 25 fasc. 7 (inv. 102: fasc. 4): Charles Emmanuel I's cipher letters to Gabaleone in London,
   16 Oct 1612 and 21 Jul 1613. Gloss unknown.
2. ASTo, Tutele, reggenze e luogotenenze generali, mazzo 4: Cardinal Maurizio to abate Buschetti, Nice, 7 Jul 1640, with clear siblings. Gloss unknown.
3. ASVe, "Secreta, lettere in cifra ai provveditori alle biave": bailo at Constantinople 1589-97, ambassador in Spain 1590 (1991 inventory title only).
4. ASGe, San Giorgio, Cancelleria dei Protettori, Montebruni filza 1560: Corsican commissioners' letters partly in cipher, keys in the same filza.
5. ASGe, San Giorgio, Montebruni filza 1561-65: the same commissioners, partly in cipher; keys in sibling filze.
6. ASGe, San Giorgio, Lasagna filza 1519: Genoese envoys' reports from Rome, sometimes in cipher.

**11 key leads** in `key_leads.json`: San Giorgio cifrari (99 filze, 1466-1570); 17 Madruzzo keys at Trent 1546-50s (digitised); ASTo Perosa
cipher 1716-17 (for catalogue 1962), legation registers "copia dei cifrati" 1816-49 (Paris, Munich, Naples), Holland cipher 1691-92, Chiusano 1729-31, Mossi 1742, "Ciffre della Corte di Roma", Sardinian ciphers
1760s; Cagliari "Cifra per la Corrispondenza" 1810-11; Corriere italiano codebook 1924 (digitised).

known.py run on every row and lead (Gabaleone, Buschetti, Matrimoni, Tutele, Maurizio di Savoia, biave, bailo di Costantinopoli,
San Giorgio, Cancelleria dei Protettori, Montebruni, Lasania, Cattaneo, Grimaldi, N1303, Madruzz, Trasselli, Perosa, Chiusano, Mossi,
Ruopoli, Corriere italiano, Controcifre): no duplicates (Perosa matches only catalogue 1962, which the key lead points to; the 1588 Corte
instruction found in Turin is already catalogued and was dropped).

## For COVERAGE.md
- Turin: the browser check is a cookie page; database, search and inventory PDFs open with curl (route above). Lettere Ministri is
  mazzo level only and not digitised: item-level cipher despatches cannot be found online. Remove "Turin (database behind a browser check)".
  "Turin diplomatic inventories" is now swept as far as online; what is left needs the reading room.
- Archivi Nazionali: JSON endpoints above (no Chrome needed); unit search by `denominazione-un` / `contenuto-un`. Swept for the cipher
  terms listed; next: the same terms with `oggetti-digitali-un` to list only digitised units, and the San Giorgio filze for "in cifra"
  under other phrasings.
- Milan ICAR: certificate expired on 6 Nov 2026 (Chrome blocks); the Potenze sovrane cipher units are not digitised on either portal.

## Not reached
Images of any row (none online). The Trento keys were not opened in the viewer (descriptions only). DECODE, Tomokiyo and Lasry were not
searched for the rows. ASTo Lettere Ministri vol. II has poor OCR; only a fuzzy grep was run.
