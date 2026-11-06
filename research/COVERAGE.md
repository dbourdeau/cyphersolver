# Sweep coverage: what has not been swept

As of 6 Nov 2026 (sweeps A, B and D of 4 Nov added at the end; Riksarkivet Turcica/Polonica and Calames rows updated 5 Nov; BNP and KB swept 5 Nov; Czech lands and the Italian state archives retry added 6 Nov). This is an index: each sweep's own README or `coverage.md` holds the detail, and the folder named on
each row is the source. No archive was contacted to write this file, so a block is as the sweep recorded it, and may
have lifted since. A sweep that closes a gap removes its row here.

"Swept" mostly means catalogue level: few sweeps looked at pages, and a catalogue that does not note cipher hides its
ciphers from any term search.

## Never swept

No sweep is named for these. This list is an absence, found on 2 Nov 2026 by keyword search of the sweep notes,
`catalogue.json` shelfmarks and `research/leads.json`. Read it as "no sweep found", not as proof that nothing was
done, and search with `research/archive_sweep_2026-10/known.py` before starting.

| Area | Archives | Found in the repo |
|---|---|---|
| Malta | The Order's archive, National Library | One passing mention in sweep notes, no entries |
| Balkans | Dubrovnik/Ragusa, Croatia, Slovenia, Serbia, Bulgaria, Greece | No entries |
| Russia | RGADA, AVPRI | No sweep notes or shelfmarks match |
| Ottoman | Istanbul state archives (BOA) | No sweep notes or shelfmarks match |
| Rome | Jesuit archive (ARSI), Propaganda Fide | No sweep notes or shelfmarks match |
| Northern and eastern Europe | Finland, Norway, Iceland, the Baltics, Ukraine, Belarus | Almost nothing |
| Romania | Cluj, Sibiu | Only the DECODE-sourced shelfmarks |
| Hungary, Slovakia | MNL; Slovak archives (no item-level portal found 6 Nov 2026) | Only through other sweeps |
| Italian state archives | Turin (database behind a "Verifica del browser" check: Chrome, `archiviodistatotorino.cultura.gov.it/Patrimonio`); Genoa (Archivio Segreto inventory PDF lists five 1761-97 cipher bundles, not digitised) | `sweep_2026-11_italian_state_retry` |
| Italian state archives | Naples, Palermo | Shelfmarks, but no sweep of the archives themselves |
| German libraries | Wolfenbüttel HAB (Extravagantes; `diglib.hab.de` resets from this network, printed Heinemann catalogue grepped in `sweep_2026-11_german_portals_2`) | Almost nothing |
| Other | Africa | Little or nothing |

## Tried and blocked

| Source | Block as recorded | Sweep |
|---|---|---|
| Archivi Nazionali search (SIUSA redirects there), Milan ICAR image viewer | Up again 6 Nov 2026, but results and images are drawn by JavaScript: Chrome (`archivinazionali.cultura.gov.it/it/risultati-di-ricerca?search=cifra`; ICAR scat. 1591). Florence MAP images, Milan/Mantua/Genoa inventory PDFs answer curl | `sweep_2026-11_italian_state_retry` |
| Braidense, Trivulziana | See the sweep | `milan_archives` |
| NLS, National Library of Wales | Cloudflare challenge | `uk_libraries` |
| TCD, Lambeth | Security check, 403 | `uk_libraries` |
| PRONI, NAI, NRS Jacobite catalogue | Bot wall, 403 or not tried | `uk_tna` |
| manuscripta.at, ÖNB Primo, Vaud | 403 in both browsers (2 Nov 2026); ÖNB Digital and Basel were swept in a browser pass (two Basel leads) | `swiss_austrian`, `browser_pass_oenb_basel_geneva` |
| Hispana, BVPB | HTTP 429; not tried in the Chrome pass, nor was BDCyL | `bne_hispana`, `chrome_pass_2026-11` |
| Biblissima, CCFr | Anubis; redirect to an authentication page | `calames_biblissima` |
| Alvin | Anubis; five searches only | `scandinavia` |
| HathiTrust full text and catalogue | Blocked; that sweep's "single biggest gap" | `hathitrust` |
| New-York Historical (NYU finding-aid search), Maryland Center (site search returns nothing) | Human check; site fault. Reached only through ArchiveGrid | `sweep_2026-11_us_blocked` |
| Benson finding aids in TARO | API ignores the query | `sweep_2026-11_us_blocked` |
| BYU CONTENTdm images (`cdm15999.contentdm.oclc.org`) | Times out from this network; holds the Sfondrati letters | `sweep_2026-11_us_blocked` |
| NYC, other: NYPL archives catalogue, Hispanic Society, Center for Jewish History, Brooklyn Public Library; Columbia terms beyond cipher/cypher/cryptogram | N-YHS/Brooklyn History (NYU search) and Columbia finding aids were searched 4 Nov 2026 for cipher/cypher/cryptogram; the others not touched | `nyc_sweep` |
| Morgan Library (`themorgan.org` record pages, `corsair.themorgan.org` catalogue) | Cloudflare checkbox that returns after 2 to 4 requests; owner clears it in Chrome. Record pages add nothing to ArchiveGrid and show no images. CORSAIR keyword search works (206 records for cipher/cypher/cryptogram); chiffre, cifra, decipher and 11 bib ids unread | `nyc_sweep` |
| LAC collection search | Cloudflare; `nouvelle-france.org` is the working route | `canada_lac` |
| AGN Argentina, national libraries of Peru, Argentina and Colombia, dLOC | Unreachable or JS-only | `canada_latam` |
| ABNB (Bolivia) | Cloudflare | `latam_southcone` |

**BNE Digital:** blocked access outright on 2 Nov 2026. Do not retry from another network: ask BNE, or resume with its
permission (`chrome_pass_2026-11`).

## Not looked at, though reachable

| Source | Sweep |
|---|---|
| KBR, Bibliothèque nationale de Luxembourg | `belgium_lux` |
| Danish KB manuscripts, Krigsarkivet beyond the NAD notes | `scandinavia` |
| GStA's own database, HStA Dresden | `archivportal_d` |
| Departmental archives with their own viewers | `calames_biblissima` |
| Boston: Massachusetts Archives (no searchable catalogue found), BU Gotlieb, UMass Boston, NEHGS, Congregational Library; MIT, Tufts, Brandeis return 403 (BPL, Athenaeum, BC, Northeastern, Digital Commonwealth done) | `boston_sweep` |

## Started and not finished

| Run | What is left | Sweep |
|---|---|---|
| BNE Digital | Rest of "cifra" (from 500 of 790), "cifras" (from 125 of 177), "nomenclator" (from 50 of 88), all of "xifrada"; needs BNE's permission | `chrome_pass_2026-11` |
| szukajwarchiwach | 564 records of 1900-50 and 115 Radom records untriaged. **The harvest is only in that Chrome profile's localStorage (`szh`)** | `chrome_pass_2026-11` |
| Internet Culturale | Full text, 28,624 hits for "cifra"; only the manuscripts filter was read | `chrome_pass_2026-11` |
| RAH | OCR text probably not searched; Salazar index not reached | `chrome_pass_2026-11` |
| PARES | Bare terms "cifra" and "descifrado" | `pares_ags` |
| DECODE Sforzesco | R5297-R5587: 13 thumbnails and one PDF of 169 records | `venice_milan_decode` |
| JACAR | 144 undated volume hits not opened; `cands_raw.json` is git-ignored | `jacar` |
| Abhilekh Patal | "cypher" paged to 691 of 4,505 | `asia_india` |
| BNP Lisbon | Keyword search only for the COD./MSS./PBA. shelves (Tarouca, Forjaz, Fontes Pereira de Melo crawled whole); "sinais" stopped part-way on 503s (one request a second works); Correlo 1970 (Nisa ciphers), the printed Santarém correspondence and Cluny 2006 (Tarouca) unread | `sweep_2026-11_bnp_portugal` |
| KB The Hague | Catalogue covered through SRU + OAI (4,040 manuscript records, ~200 read in full); `kb.on.worldcat.org` shows Cloudflare and was not tried in Chrome (adds nothing the SRU route lacks); Delpher full text of the KB annual reports and the Literatuurmuseum catalogue not reached. No KB cipher item has scans online | `sweep_2026-11_kb_netherlands` |
| NARA M1194 | No search for "decipher" across all 261 rolls; only cards the bulk scan flagged were read | `nara_triage_c` |
| QDL | No Arabic or Persian terms; 23,753 hit pages not screened as images | `qdl` |
| BnF | Bellièvre papers not yet screened: fr. 15890, 15892-15905, 15907-15911; fr. 15900 (2) has no Gallica ark (15906, 15900 (1) and 15891 swept 5 Nov 2026) | `gallica_sweep` |
| Dudout's BnF BAM list | The 675-article JSON, available from him on request | `dudout_2026-10-29` |
| Archivportal-D | Only the first 200 "chiffriert" slots, no other terms | `central_archives` |
| HHStA | Staatenabteilungen Spanien, Rom, Venedig beyond the term searches | `central_archives` |
| Printed series | Hardwicke, Journals of the Continental Congress, Official Records, Home Office calendar after 1775 | `ia_pass2_b` |

## Swept at catalogue level, ciphers hidden

These need browsing by volume, because descriptions rarely note cipher: Riksarkivet beyond Diplomatica and Stedingk (every
digitised Diplomatica volume was sheeted 5-6 Nov 2026, `sweep_2026-11_riksarkivet_turcica`, `_west` and `_consuls`; the other
105 Stedingk volumes and the Barthelemy, De la Gardie, Tessin and Reuterholm papers were not), the Oxenstiernska
samlingen and the Kanslikollegium series, and Rigsarkivet TKUA envoy reports (`scandinavia`); TNA State Papers (`uk_tna`);
AGATHA's envoy series (`belgium_lux`).

## Needs Daniel

- **Logins:** MIA (`medici_bia`), Abhilekh images (`asia_india`), Sejarah Nusantara (`asia_anri`), AGATHA DiVa and ANLux
  eAccess (`belgium_lux`). CEHM images, SIAN and Chile ClaveÚnica come from the 2 Nov review of the Latin American sweeps;
  check the sweep before asking. CEHM scans have since opened in Chrome with no login (`vetting_2026-10/BRIEF.md`).
- **API key:** Trove (`oceania_naa`).

## Sweeps of 4 Nov 2026 (A half-done runs, B unswept south, D east and north)

Folders: `sweep_2026-11_A_halfdone`, `sweep_2026-11_B_unswept_south`, `sweep_2026-11_D_east_north`. 57 leads merged.

- **Closed:** Internet Culturale full text (printed books and newspapers only, 0 archival rows); szukajwarchiwach
  1900-50 and Radom (agrees with `polish_harvest`; the `szh` harvest is now exported to
  `chrome_pass_2026-11/szh_export.json`); PARES bare terms "cifra" and "descifrado".
- **New route:** PARES-HTR (`pares.cultura.gob.es/pares-htr`, ACA Cancilleria 1479-1556) is a plaintext index of "En cifra"
  registers, not a source of new ciphertexts. ICCU Manus Online API and the Wayback Machine work for Italian inventories.
- **Still never swept:** Dubrovnik (no item-level catalogue online; ask the State Archives about "sifra" bundles), Malta
  (vHMML Turnstile), ARSI and Propaganda Fide (only the printed MHSI volumes), Slovakia, Russia, Belarus (Turin and the
  Czech lands were swept 6 Nov 2026). About 6,000 Manus "cifre" records unscreened.
- **Blocked:** Finna (Cloudflare), BOA (login with CAPTCHA), hrcak.srce.hr, Harvard hosts (403), Abhilekh Patal (403 on the
  user's network on 4 Nov; its 18 image leads stay unvetted).
- **Not done:** ACA reg. 3225 (1435) not reached.

## Sweeps of 6 Nov 2026 (overnight)

- **Czech lands** (`sweep_2026-11_czech_slovak`): ARON item search at MZA Brno, SOA Plzeň, Zámrsk and SOA Praha, NA VadeMeCum,
  OCR of the Acta Clementina finding aids; 19 leads (2288-2306). Not reached: SOA Litoměřice, Zemský archiv Opava and SOA Třeboň
  viewers (bot check or JS: Chrome), the Charles University thesis on the Gallas war-chancery ciphers (dspace.cuni.cz resets),
  Roubík 1931. Mírka's survey of the Plzeň family-archive ciphers (Crypto-World 2012-13) names further items.
- **Italian state archives retry** (`sweep_2026-11_italian_state_retry`): the cultura.gov.it outage is over. ASF Mediceo avanti il
  Principato gave 6 leads (2307-2312); MAP vol. 4, the MAP key sheets and the PAD Mediceo del Principato runs continue in
  `sweep_2026-11_asf_florence`. Modena: no item-level inventory online.
- **Riksarkivet** (`sweep_2026-11_riksarkivet_west`, `sweep_2026-11_riksarkivet_consuls`): all 59 remaining digitised Diplomatica
  volumes and 59 Stedingk volumes sheeted at 600 px; the 25 consular volumes (Maroccana, Algerica, Tunisica, Tripolitana) paged
  in full. Short code groups inside clear sentences (Logie's form) show only at 800 px.
- **ASF Florence** (`sweep_2026-11_asf_florence`, `_2`, `asf_map_paging`): MAP inventory vol. 4 OCR'd, every unopened "in cifra"
  item of the PAD Mediceo del Principato filze 330-460 opened. Not online: Mediceo del Principato 461-659 (the appendix filze
  with the most cipher), Dieci di Balìa. The MAP inventory misses cipher letters: page filze, do not trust it.
- **Turin and Archivi Nazionali** (`sweep_2026-11_turin_chrome`): the Turin browser check is a cookie printed in the page (curl
  works); Archivi Nazionali has JSON endpoints (`keywords=`). Lettere ministri are inventoried only by bundle and not
  digitised. Milan ICAR's certificate expired 6 Nov 2026.
- **DigiVatLib** (`sweep_2026-11_digivatlib`): answers curl again with a browser User-Agent, cookie and Referer; the BAV OPAC
  (`opac.vatlib.it/mss/search`) indexes undigitised volumes too. Not reached: Barberini, Ottoboni and Chigi letter volumes with
  no item-level description.
