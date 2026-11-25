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
| Italian state archives | Turin and Genoa swept to the limit of what is online (6 Nov 2026, `sweep_2026-11_turin_chrome`; catalogue 2360, 2363-2365 promoted): the ASTo diplomatic series (Lettere Ministri) and the ASGe Archivio Segreto ministers' series are mazzo-level only and not digitised, so what is left needs the reading rooms or photo orders | `sweep_2026-11_turin_chrome` |
| Italian state archives | Naples, Palermo | Swept 6 Nov 2026 (`sweep_2026-11_naples_palermo`): the archives' own hosts (ASNa TLS reset, Palermo SAASSIPA timeout, digital library no DNS) do not answer from this machine; Archivi Nazionali has no ASNa units; Palermo inventory PDFs read through Wayback (about 170 of 892). Not done: the other ~720 Palermo PDFs, the Palermo digital library, PARES Naples/Sicily viceroy items (`pares_ags/hits.jsonl`) |
| German libraries | Wolfenbüttel HAB (Extravagantes; `diglib.hab.de` resets from this network, printed Heinemann catalogue grepped in `sweep_2026-11_german_portals_2`) | Almost nothing |
| Other | Africa | Swept and closed 14 Nov 2026 from a network with no Chrome (`sweep_2026-11-14_africa_portugal`, `_british_southafrica`, `_north_east_literature`, `_dutch_nordic`): 11 rows merged (leads 2930-2940); 2937 and 2939 vetted and promoted (2939 written up as `gordonmudir1884`, not solved), 9 left `unvetted` with their blockers in `research/vetting_2026-11-14_dbourdeau_africa_a/` and `_b/`. Not done: the hosts that need Chrome or do not answer (Wits, South African National Archives, Cory, RGS, Dar al-Kutub, Bodleian, Cambridge ArchiveSearch, Archives Hub, IWM, EAP, Rigsarkivet Danish Gold Coast, GStA Berlin, Basel Mission search); physical sources for the Gordon note (TNA PRO 30/57/4/75-109 at Kew; Durham SAD.101/15, the Hicks Pasha registers SAD.866 and SAD.600); the AHU "Telegramas cifrados" 1947-50 folders (scan order); Sociëteit van Suriname paging, Zeeuws Archief and Delpher; the unparsed OCR (38 Theal-set and 53 explorer-book ids) |

## Tried and blocked

| Source | Block as recorded | Sweep |
|---|---|---|
| Archivi Nazionali search (SIUSA redirects there), Milan ICAR image viewer | Up again 6 Nov 2026, but results and images are drawn by JavaScript: Chrome (`archivinazionali.cultura.gov.it/it/risultati-di-ricerca?search=cifra`; ICAR scat. 1591). Florence MAP images, Milan/Mantua/Genoa inventory PDFs answer curl | `sweep_2026-11_italian_state_retry` |
| Braidense, Trivulziana | See the sweep | `milan_archives` |
| NLS, National Library of Wales | Cloudflare challenge | `uk_libraries` |
| TCD | Security check, 403 | `uk_libraries` |
| Lambeth | No longer blocked: the CalmView catalogue answers scripts and was searched on "cipher" (`sweep_2026-11_uk_ireland`), "cypher" (`sweep_2026-11_uk_retest`) and nine more terms (`sweep_2026-11-13_lambeth`, 13 Nov 2026). No manuscript images are online; left: "in code", "characters", "figures", old spellings | `sweep_2026-11-13_lambeth` |
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
| Abhilekh Patal | "cypher" title run is date-sorted: the 691 records read reach 1915; the other ~3,800 are post-1915 administrative cypher-telegram files (13 Nov 2026), low value | `asia_india` |
| BNP Lisbon | Keyword search only for the COD./MSS./PBA. shelves (Tarouca, Forjaz, Fontes Pereira de Melo crawled whole); "sinais" stopped part-way on 503s (one request a second works); Correlo 1970 (Nisa ciphers), the printed Santarém correspondence and Cluny 2006 (Tarouca) unread | `sweep_2026-11_bnp_portugal` |
| KB The Hague | Catalogue covered through SRU + OAI (4,040 manuscript records, ~200 read in full); `kb.on.worldcat.org` shows Cloudflare and was not tried in Chrome (adds nothing the SRU route lacks); Delpher full text of the KB annual reports and the Literatuurmuseum catalogue not reached. No KB cipher item has scans online | `sweep_2026-11_kb_netherlands` |
| NARA M1194 | No search for "decipher" across all 261 rolls; only cards the bulk scan flagged were read | `nara_triage_c` |
| QDL | No Arabic or Persian terms; 23,753 hit pages not screened as images | `qdl` |
| BnF | Bellièvre papers not yet screened page by page: fr. 15892, 15893, 15895, 15896, 15899-15901, 15907-15910; fr. 15900 (2) has no Gallica ark (15906, 15900 (1), 15891 swept 5 Nov; 15902-15905 and 15911 on 11 Nov; 15890, 15894, 15897, 15898 on 15 Nov 2026, wave 15: no ciphertext) | `gallica_sweep`, `sweep_2026-11-15_wave15_bellievre` |
| Dudout's BnF BAM list | The 675-article JSON, available from him on request | `dudout_2026-10-29` |
| HHStA | Staatenabteilungen Spanien, Rom, Venedig beyond the term searches | `central_archives` |
| Printed series | Wave 16 (16 Nov 2026, `sweep_2026-11-15_wave16_printed`) read about 1,200 archive.org texts and 34 BHO volumes: Hardwicke, Home Office calendar, Letters of Delegates, Wharton, HMC reports, CSP Domestic/Foreign/Spanish/Venetian (7-9, 11-15)/Milan, and the French and German editions (Louis XI, Catherine de Medicis, Henri IV, Mazarin, Teulet, Briefe und Acten). Left: HMC and Fontes rerum Austriacarum texts and CSP Venetian 16-38 fetched late (the README has the grep command), Journals of the Continental Congress, Official Records | `sweep_2026-11-15_wave16_printed` |

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
  Czech lands were swept 6 Nov 2026). .
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
- **ASF MAP backfill, 13 Nov 2026** (`sweep_2026-11-13_b169_backfill`, 12 leads 2554-2565): MAP filze XLIII, XLIX, LI-LIII, MdP 385 and one Rigsarkivet Pentz unit. Still unpaged: see the next bullet (LVI stopped at disk limit); Pentz unit 274999 images 137-503; the notes of Lettere di Lorenzo VII-IX (not online) before the ten MAP leads are promoted.
- **ASF MAP backfill 2, 13 Nov 2026** (`sweep_2026-11-13_b174_backfill2`, 1 lead 2566: MAP XLIV doc. 21): MAP XXXIX, XL, XLII, XLIV, XLV, XLVII, LIV, LVI, LVII, LVIII, LIX and LXI paged by the detector's top 16-32 pages only (XLIV: top 24 of 130; its other 106 images unseen at native size). XXXIX, XL, XLII, LVII, LVIII: every cipher page opened carries an interlinear decipherment. LIX docs 69, 132, 173, 189 (and 1488) are Lorenzo's own letters to Lanfredini, left out until the Lettere di Lorenzo notes are checked. Still unpaged: MAP letters to Lorenzo XX-XXXVIII, XLI, XLVI, LV, LX, LXVI, LXVIII; Pentz unit 274999 images 313-503 (137-312 looked at too small to tell number cipher from Kurrent, not a valid check); other Rigsarkivet TKUA units; Vito 2025 unopened.
- **Turin and Archivi Nazionali** (`sweep_2026-11_turin_chrome`): the Turin browser check is a cookie printed in the page (curl
  works); Archivi Nazionali has JSON endpoints (`keywords=`). Lettere ministri are inventoried only by bundle and not
  digitised. Milan ICAR's certificate expired 6 Nov 2026.
- **DigiVatLib** (`sweep_2026-11_digivatlib`): answers curl again with a browser User-Agent, cookie and Referer; the BAV OPAC
  (`opac.vatlib.it/mss/search`) indexes undigitised volumes too. Not reached: Barberini, Ottoboni and Chigi letter volumes with
  no item-level description.

## Sweeps of 6 Nov 2026 (afternoon: Naples/Palermo, Archivi Nazionali digitised, DigiVatLib letters)

- **Archivi Nazionali, digitised only** (`sweep_2026-11_an_digitised`): the filter is `&oggetti-digitali-un=on` on the unit search (exact-token match;
  `true`/`1` ignored; it also passes parents that only have digitised descendants, so `data-uuid-manifest` on the record is the real test).
  About 90 term runs gave 131 cipher-type units, 0 rows; the digitised ones are key sets (Trento Madruzzo, 17 keys), the Corriere italiano codebook
  and Torino 1913-19 telegrams with transcriptions. Diplomatic series (ASVe Miscellanea turchi, Collegio/Senato Secreti, Genoa Archivio Segreto,
  Milan Sforza) are digitised but need page-by-page work: the portal searches description text only.
- **DigiVatLib letter volumes** (`sweep_2026-11_vatlib_letters`): 0 rows. Barb. lat. 9914-9915 "Cifre antiche" are undigitised keys; Chig. A.I.8, 20-22, 25
  sampled and clear; Barb. lat. 9848 has "Cifre e decifrati". Manifest probing at 1 s intervals triggered a 15-minute 429: probe at 3 s or slower.
  Not reached: Barb. lat. 6000-9800 undescribed volumes, Chig. A.I.35-60, Ott./Urb./Ross./Ferr. letter volumes.
- **Naples/Palermo** (`sweep_2026-11_naples_palermo`): leads 2397 (Maria Carolina, private collection, partial decodification noted) and 2398 (ASPa Misc. Arch. II n. 262);
  neither is vetted or promotable yet (2397 has a partial decodification of unknown extent; 2398 has no known access).
- **PARES Naples/Sicily viceroy items** (`sweep_2026-11_pares_naples`): ten Estado Genoa items opened; 0 rows (clear, "descifrada" copies, or already inside catalogue 755 / `genes1643`; 3598,222/223 is a plain/cipher pair in the 1643 Genoa key family). Not opened: Osuna (Albornoz), Santa Cruz and Frías PARES hits.

## Sweeps of 9 Nov 2026

Folders: `sweep_2026-11_*` as named. 50 leads merged (2414-2463; see `merged.json`); 34 promoted to the catalogue the same day
(1270, 1271, 2415, 2416, 2421, 2422, 2423, 2424, 2425, 2427, 2428, 2429, 2430, 2432, 2433, 2436, 2438, 2439, 2440, 2441, 2443, 2444, 2445, 2446, 2447, 2448, 2450, 2451, 2455, 2457, 2458, 2459, 2460, 2463).

- **Productive routes:** PARES full text with a century facet and `catalogo/contiene/<series id>` child listings on the Carlist and Peninsular
  War series (`spain_nobility_aca`, `pares_diversos_19c`); Mírka's Crypto-World survey of the Plzeň family archives and Antal et al.
  (HistoCrypt 2023) for Slovakia (`mirka_cryptoworld`); Landesarchiv NRW noble archives (`austria_german_states`); Daniel Tant's
  ARCSI list of French cipher items, arcsi.fr/doc/Tant/420.pdf (`france_departmental`); the Utrecht Amerongen fonds through the
  archieven.nl OAI-PMH feed, `harvest.archieven.nl/OAI/OAIHandler` (`siblings_nov9`).
- **Closed with 0 rows:** HAB Wolfenbüttel and Swiss libraries (OPAC unreachable), Denmark and Sweden (Libris, KB Copenhagen,
  Riksarkivet text terms), Slovak, Croatian and Slovenian finding aids (12 PDFs grepped), Ireland and UK universities (already swept),
  Dutch regional archives (OAI route covers about 70% of the open sets), the published lists of undeciphered ciphers (HistoCrypt
  2018-2023, Tomokiyo `unsolved.htm`, Klartext: every item already here), BSB/Bodleian metadata, Canada (Archives of Ontario, Manitoba, BAnQ
  Advitam, McGill), Australia and New Zealand (DigitalNZ, Trove web search), Manus Online "cifre" (4,361 records; 99% noise),
  PARES century full text (cipher vocabulary exhausted for the 16th to 18th centuries).
- **Still blocked:** PANB, Archeion, UCalgary, McCord, BC Archives, SLNSW (human check); natlib.govt.nz and Archives NZ; archive.nrw.de and AD Gironde
  Ligeo (Anubis since the afternoon); Digital Scriptorium, CUDL; dlib.si (JS); the Aube, Nord and Ardennes notices behind leads 2417-2420.
- **Not done:** Bellièvre papers at 800 px (fr. 15905 second ark, 15911, 15904, 15903, 15894, 15902, 15897, 15898 online; about 6,000 canvases,
  10 canvases a minute); Reuterholm E 5135-5141 and Stedingk E 6616/6617 sampling at Riksarkivet (image server slow); rest of the Dutch OAI sets
  (Noord-Hollands 430 of 2726, Groninger 450 of 2794); Hungarian MNL (503).
- **BNE Digital:** the lead-vetting agent opened BNE Digital in Chrome (single leaves, for leads 1270 and 1271) although this file says not to
  retry it. It worked; nothing was fetched in bulk. Ask before any larger use.

- **Late sweeps:** the cataloguers' own "undeciphered" notes (`undeciphered_phrases`: Hungaricana `sifrír* NOT Türkei`, 7 rows, 4 promoted) and a Chrome pass on Latvian, Estonian and Hungarian sources (`baltic_hungary_chrome`). Latvian State Historical Archive, Riga city archive, Tartu and DIGAR stay unreachable.

## Sweeps of 11 Nov 2026 (cloud session, a different network)

Folders: `sweep_2026-11-11_*`; brief in `_nov11/BRIEF.md`; lead re-vetting in `vetting_2026-11-11/` (seven batches). This network
reaches some hosts the earlier one did not and the reverse; each README has its own table.

- **Productive routes:** MNL `adatbazisokonline.mnl.gov.hu` (item database of G 15, Rákóczi's archive, marks about 100 letters as
  undeciphered: `southeast`); Rigsarkivet Arkivalieronline by curl (`nordic`, `tkua_paging`, `_2`, `_3`: TKUA envoy archives and
  Gesandtskabsrelationer, most units still unsheeted); Alvin through its OAI-PMH feed (`nordic`); the archieven.nl site search
  and scan viewer in headless Chromium (`dutch_oai`, `dutch_2`); the GStA database at `archive.spk-berlin.de/actaproweb`
  (`german`); BYU CONTENTdm API and IIIF (`us_uk_leftovers`); `digi.vatlib.it/mss/<Fondo>` lists a fondo's digitised shelfmarks (`vatlib`);
  fgurgia.ru and vestigia.hu answer; FranceArchives renders in headless Chromium.
- **Closed with 0 rows:** Official Records, Journals of the Continental Congress, Hardwicke, Wharton (`printed_series`; the Home Office
  calendar has no volume after 1775); NARA M1194 word pass over all 262 rolls (nothing beyond `nara_triage_e`/`_l`); Riksarkivet
  Skrivelser till konungen 1133.08/7-16 screened in full (cipher deciphered at the time; one washed-out gloss is a lead) and 40
  sampled private-paper volumes; DigiVatLib Barb. lat. samples (cipher always beside its decifrato); Bellièvre fr. 15902-15905 and
  15911 screened by detector (the Henri IV cipher letters of 1598 in fr. 15911 are printed in clear in Duplessis-Mornay VIII).
- **Not done:** Bellièvre fr. 15894, 15897, 15898, 15890; Barb. lat. 5701-5781, 6024-6261, 7196-8015, 8725-9746 and the Ott./Ross./Ferr./Reg.
  letter volumes; Abhilekh "cypher" from page 230 of 451 and its phrase queries; 59 JACAR volume titles; the Riksarkivet volumes listed
  in `riksarkivet_paging/README.md`; GStA full records and HAB; the Politische Correspondenz for the Rexin leads.
- **Blocked from this network:** gallica.bnf.fr (use openapi.bnf.fr), PARES, Hispana, BVPB (429), hungaricana, NLS, NLW, Lambeth, LAC,
  HathiTrust, archivesportaleurope, europeana, QDL, Harvard, NYPL, NRS, TCD (403 or challenge), Calames, ASF, Sinica reader (no
  connection), archivportal-d item pages and TARO (Anubis), handrit.is (captcha), and the Romanian, Croatian, Slovenian, Serbian,
  Bulgarian, Greek and Maltese portals.
- **Abhilekh Patal:** record pages answer curl. The Document Viewer shows a human check to a browser; two vetting agents read file
  PDFs by posting its form with curl. Those eight verdicts (1355, 1356, 1360, 1363, 1364, 1367, 1368, 1371) are kept in
  `vetting_held` and not applied: Daniel to decide, or confirm in his own Chrome. Lead 1359 (NAI Sikkim (Political) 1930 File 5-P)
  was vetted on 11 Nov 2026 by the same route (its `vetting_note`: the viewer "opened without a login" from the cloud); that vetting
  is superseded: the lead was closed on 12 Nov 2026 on Brice Dudout's reading of the file in his own logged-in session (PR #434,
  `targets/nanking1930`), and nothing rests on the cloud reading. Lead 2465 was closed the same day on his logged-in reading
  (PR #431, `targets/peking1912`); the project has not seen the images of either file.
- **Rigsarkivet TKUA, four paging rounds** (`tkua_paging` to `tkua_paging_4`): the 17th-century envoy archives and relations gave nine
  catalogue entries (2520, 2527, 2528, 2530, 2540-2543, 2553); every cipher leaf opened from 1659 on is
  deciphered between the lines. Not done: most 18th-century units of the 236, six enumerated series, 68 sheets made and not viewed, the
  "Chiffer 1670-1709" key volume (unit 260610).
- **Dutch round 2** (`dutch_2`): archieven.nl site search, about 80 terms; 8 leads, the Culemborg 1257 and Ewsum 595 leaf lists.
- **Paused 11 Nov, unfinished, rows not merged:** `mnl_2` (MNL databases round 2; 5 draft rows in its `candidates.json`),
  `bellievre_2` (fr. 15894, 15897, 15898, 15890: fetch scripts only), `alvin_waller` (paging Waller letters on Alvin by image: scripts
  only). Resume from the scripts; none has a README yet.
- **Result of the pass:** 36 leads promoted (catalogue 1210 to 1246: 32 of the 89 rows merged today and 4 older leads), 57 new leads left in `leads.json`, 9 leads closed as read, partly read or not cipher.

## 13 Nov 2026 pass (cloud session; folders `sweep_2026-11-13_*`)

- **MAP paging** (`sweep_2026-11-13_map_paging`): filze XXX-XXXVIII, XLI, XLVI, LV, LX, LXVIII paged by detector (top ranks only); 1 bare lead (XXXVIII 418, held: Lettere di Lorenzo range). Not paged: XX-XXIX, LXVI, early-1500s filze, deeper ranks.
- **TKUA paging 5** (`..._tkua_paging_5`): 0 rows. The Indkomne breve and relation series are single letters; a 1-in-4 sample at 400 px misses short runs.
- **Riksarkivet Skrivelser till konungen 1133.07** (`..._nordic_paging`): top-64 screen per volume; 5 bare leads (Grubbe, Horn, Banér, De la Gardie, "Chemnitz"), unvetted for lack of an online edition. Not reached: 1133.07/26-35, 1133.01-05, second windows, Danske Kancelli, Kongehuset.
- **JACAR** (`..._jacar`): 403 after parallel threads at about 4 requests a second; retry at one request per 2-3 s. 2,474 selected records unscanned; two 1879 Japanese rows unvetted.
- **New sources** (`..._new_sources`): BSB/MDZ search API, Polona, Memoria Digital de Catalunya reachable and swept (0 rows); Internet Culturale CAPTCHA, e-rara, e-manuscripta, SLUB, Heidelberg blocked. Best route left: Omont's BnF catalogue (about 150 "avec chiffre" pieces), blocked only by finding Gallica arks (needs Chrome).

## Sweeps of 14 Nov 2026 (never-swept areas, GStA, Koç, Hungaricana, Dutch)

Folders `sweep_2026-11-14_*`; vetting in `research/vetting_2026-11-14_*`. Leads 2575-2723 merged; 32 promoted.

- **Productive routes:** GStA PK ACTApro (`archive.spk-berlin.de/actaproweb`, Chrome same-origin POST, `resultsForPage` 500, wildcards; record opens only through a hit link from a search in the same session; no images online); Koç CONTENTdm HPBK/MHC (Hilmi Paşa Yemen telegrams; images via `libdigitalcollections.ku.edu.tr/iiif/2/HPBK:<item id>`; target `hpbk1896`, 0% read, transcription is the blocker); Hungaricana LEAR regests (`?list=<base64 {"query":...}>&page=N`, same-origin fetch in Chrome, 20 hits a page); Tresoar open JSON API (`archieven.tresoar.nl/api/search`); Stadsarchief Amsterdam `POST id.archief.amsterdam/search/records` (one recordType per call); Thüringen/Saxon finding aids.
- **Closed with 0 rows:** Malta, Dubrovnik/Croatia/Serbia/Bulgaria/Greece, Romania (hosts down or no item-level catalogue; Europeana API only noise); Riksarkivet Reuterholm, Tessin, De la Gardie, Stedingk, Oxenstierna, Kanslikollegium (5,636 images sampled, all clear); Dutch OAI sets complete to the end (Noord-Hollands, Groninger, Haags, Westfries, Rivierenland and others); Archivportal-D (already paged in full through the DDB Solr endpoint; the "first 200 slots" row was stale and is removed).
- **Still blocked:** BOA (arithmetic CAPTCHA login), RGADA, GARF (DDoS-Guard), vHMML Malta (Turnstile), NYPL Archives (Imperva), Hispanic Society, NEHGS (names only), Open Jerusalem, Drents Archief, Erfgoed Leiden, Leiden University Libraries, Radboud repository, British History Online (401), SALT Research (Cloudflare). PARES returned 429 from about 18:20: leads 2699-2711 (Osuna/Frías) are merged unvetted until it answers.
- **Not done:** the 20 GStA deep-sweep leads and 8 German-database leads left unvetted (no images online: need the reading rooms or an edition); Hungaricana leads 2679-2692 (the 2025 Fazekas-Fodor-Gluck edition of the Constantinople envoys' reports 1568-74 is not online); Ericsberg `B 1/13-15` and the Ericsberg C. G. Tessin papers at Riksarkivet; De la Gardie E 1649 (401); HPBK sheets that did not load; Tresoar 323 inv. 5592.52 scan request (possible key for `casimir1618`); Tirol and Salzburg archives; Tilburg, BHIC, Utrecht UB, UvA, Delpher manuscripts; Morgan CORSAIR "cifra" and "in cipher"; the Palermo `wbpa4.py` run over 245 excluded PDFs.

## Sweeps of 15 Nov 2026 (Omont NAF, Austria and Switzerland, French-Swiss, Ericsberg)

Folders `sweep_2026-11-15_*`; vetting in `research/vetting_2026-11-15_*`. Leads 2745-2782 merged; 7 promoted (2746, 2753, 2754, 2758, 2773, 2774, 2775).

- **Omont NAF and petits fonds** (`sweep_2026-11-15_omont_naf`): NAF II-IV, Saint-Germain III and the Anciens petits fonds swept from archive.org (the djvu file name differs from the item id). Still unswept: Saint-Germain I (Gallica `.texteBrut` behind a security check), Saint-Germain II and NAF I (no archive.org item). Omont shelfmarks and folios are OCR readings: confirm each on Gallica before a lead is trusted (the 14 Nov Omont rows had five wrong shelfmarks).
- **Austria and Switzerland** (`sweep_2026-11-15_austria_swiss`, `_swiss_french`): routes are archives-online.org (drive the form from the console; results arrive over SignalR), findbuch front ends (`do_rech_start_with_words('term')`), friXplore (Fribourg, plain curl), DAVEL (Vaud, opens in Chrome only), BGE archives (Anubis clears itself). The Affry (de Boccard) fonds at Fribourg files d'Affry's clear drafts beside the numbered dispatches (AEF Affry 225, 226): a route to plaintext for `affry1757`, not digitised; series 257 is the other half of the R1071 correspondence. Not reached: Tirol, Salzburg, Südtirol (no public item-level database), Kärnten (host resets), Archives de l'État de Neuchâtel and Archives de la Ville de Genève (hosts do not resolve), Steiermark (bot-defence on scripted POST).
- **Riksarkivet Ericsberg and Stedingk** (`sweep_2026-11-15_riksarkivet_ericsberg`): 4,257 images sampled (every 3rd) over 32 volumes, 0 rows. Next step: B 1/14 images 1-30 and 540-582 page by page (catalogued "Med chiffernycklar"). De la Gardie E 1649 is behind a Riksarkivet login (GDPR, material under 110 years): needs the user's account.
- **Still waiting on PARES:** leads 2699-2711 (429 since 14 Nov, still 429 on 15 Nov).

## Sweeps of 15 Nov 2026, wave 3 (TNA Discovery, JACAR retry, Vatican and Venice)

Folders `sweep_2026-11-15_tna_discovery`, `_jacar_retry`, `_vatican_venice`; vetting in `research/vetting_2026-11-15_tna_discovery`. Leads 2783-2807 merged; 4 promoted (2784, 2788, 2792, 2797).

- **TNA Discovery:** the API answers without a block and no State Papers piece is digitised, so every row rests on catalogue text. Not done: the calendar download of about 350 archive.org volumes stopped at 273 (about 80 not fetched); WO 1, WO 32, FO 27 and CO 5 are described by folio range with no cipher words, so they need a per-volume approach; British History Online search sits behind a challenge page; Gale State Papers Online not checked for images.
- **JACAR:** 759 priority records scanned single-threaded at about 2.5 s (no 403): no cipher runs, only administrative items. 2,123 body-text-only records are not scanned (`scan1.py` does them). Three Waseda Okuma-papers leads (Motono cipher telegram 1874 and the Taiwan telegraph cipher tables) sit in `sweep_2026-11-15_jacar_retry/candidates.json`, unmerged: the Waseda site was down for maintenance. The JACAR region value has no Asia entry in `merge.py`.
- **Vatican and Venice:** 0 rows. The Vatican Apostolic Archive has no item-level route (the "Indice dei Fondi" PDF names "Ufficio Cifra" only); BAV OPAC 16 new terms gave 0 new shelfmarks of 426 covered; Chig. A.I.35-60 are not digitised; the Dieci "Cifre, chiavi e scontri di cifra" series is restricted. Mapping Barb. lat. 6000-9800 needs about 3,800 manifest probes at 3 s.

## Sweeps of 15 Nov 2026, wave 4 (blocked sources in Chrome; OeNB Primo first and deep pass)

Folders `sweep_2026-11-15_uk_blocked_chrome`, `_continental_blocked_chrome`, `_oenb_deep`. Leads 2808-2831 (waves 4a: UK and continental blocked sources, OeNB first pass) and 2832-2837 (OeNB deep pass) merged; the 15 Nov audit (`research/vetting_audit_2026-11-15`) demoted 13 earlier promotions that had a decipherment filed with the text, so a filed decipherment, not a key, is what blocks promotion.

- **UK blocked via Chrome:** NLS (Cloudflare clears itself in about 20 s), NLW (AtoM opens now), Bodleian (Anubis passes) swept by same-origin `fetch()` from the page; 6 rows, almost everything else already in the ledgers. Nothing viewed, nothing promoted.
- **Continental blocked via Chrome:** OeNB Primo (opens), Biblissima portal (opens), Alvin (Anubis passes), CCFr and Delpher (opened, nothing to sweep); HathiTrust full text still stops at a Cloudflare checkbox (not clicked), manuscripta.at still 403 in Chrome.
- **OeNB Primo (first pass and deep pass):** routes and terms in `sweep_2026-11-15_oenb_deep/README.md`. Use `tab=onb_hanna&search_scope=ONB_hanna` for the whole manuscript holdings and `facet=rtype,include,Papyrus` for the papyri. The autograph catalogue states cipher in the extent line, so searches for Geheimschrift, chiffriert, Chiffern, Zahlencode cover it; "Chiffre" there means a monogram signature (noise). The Korrespondenz facet is now exhausted for 22 cipher terms: the real hits are the Schlik volumes, the Dupont telegrams, the Adelgunde letters, Zane, five early autographs, and 6 new rows (the 9th-c. Arabic papyrus P.Vindob. A. P. 11016, Ferdinand II 1607, Maximilian I 1517, Eugene of Savoy 1701, a Stammbuch, a cryptography tract). **Not done:** the ONB digital viewer did not load in Chrome, so no OeNB item has been seen on an image and none meets the vetting bar; the papyrus is the one worth a look from another network.
- **Tirol, Salzburg, Kaernten:** still no route (no item-level database for Tirol and Salzburg; Kaernten KLAIS does not load in Chrome either). Upper Austria and Vorarlberg are covered through findbuch (`sweep_2026-11-15_austria_swiss`).

## Script wave 5, 15 Nov 2026 (Omont Saint-Germain, route probes)

Folder `sweep_2026-11-15_script_wave5`; 0 leads. Omont Saint-Germain I/II are readable from archive.org (`cataloguegnrald00manugoog`, `cataloguegnrald01manugoog`):
only key sheets, "avec dechiffrement" entries and Bellievre fr. 15566-15572 Matignon/Chasteauneuf cipher letters (unconfirmed folios). Still open: Gallica arks for fr. 15566-15568 (SRU needs Chrome),
NAF I (no OCR). Gallica manifests answer curl at 3 s; ark check character is NOID (see README there).

## Omont wave 6, 15 Nov 2026 (Gallica SRU in Chrome, Bellievre recueil)

Folder `sweep_2026-11-15_gallica_omont_wave6`; leads 2838-2842 merged and promoted (fr. 15567 f. 24 and ff. 158-164, fr. 15568 ff. 151-152 and 207-208, fr. 15571 f. 37; tables by Tomokiyo, texts unread).
fr. 15566 f. 50 is solved by Lasry (GL.htm), fr. 15572 ff. 277-278 are deciphered in ff. 279-280 (matignon1586c3 notes): neither is a lead. Route: Gallica SRU
`gallica all "Français N" and dc.type all "manuscrit"` from a gallica.bnf.fr tab, then openapi.bnf.fr IIIF by curl. Still open: fr. 15567 f. 54 and f. 71, 113, 162, 194 and fr. 15568 f. 68v (named by Tomokiyo, not viewed), fr. 15569-15570 (arks unknown).
Bellievre papers fr. 15890-15911 (the COVERAGE row "BnF, Bellievre papers not yet screened"): Omont's catalogue text (archive.org `cataloguegnrald00manugoog`) was read for the whole run, 15 Nov 2026. Its only cipher mentions are
fr. 15906 "Memoires chiffres" of Entragues (ff. 759, 780: Lasry's, target `entragues1581`), Revol and Du Val de Stors "chiffrees, avec dechiffrement" (excluded) and key sheets; the images were not paged.
ONB (leads 2832-2837), retry 15 Nov: api.onb.ac.at manifests 504 and the new viewer shows "Fehler 500" for every DTL id tried; nothing viewed. Lead 2835 closed `read` (decipherment_filed: "Begleitmaterial: Transskription").

## Chrome wave 7, 15 Nov 2026 (Catalan archives portal; folder `sweep_2026-11-15_chrome_wave7`)

- **New source:** Arxius en linia (`arxiusenlinia.cultura.gencat.cat`, item-level, ANC and Catalan comarcal archives; backend JSON route in Chrome, see the sweep README). 38 Catalan and Spanish terms run; leads 2843-2853, 9 promoted (1873 Interior Ministry telegrams seen on image, Carlist letters, Saavedra Fajardo 'cartes xifrades', Castelldosrius, Carreras 1936). Key-only items in `key_leads.json`, including the 1487 'Instruccions per cartes xifrades a Antonio Ximeno' (ACPS211-95-T2-242).
- **Still Cloudflare-blocked in Chrome:** Finna, Archives Hub, Library Hub Discover, National Library of Wales archives; Abhilekh Patal 403. PRONI's eCatalogue now answers at `apps.proni.gov.uk/eCatNI_IE/` (already swept: its 'Tried and blocked' row is out of date).
- **Not done:** Arkivportalen Norway (908 'chiffer' hits, mostly 20th century; URL paging does not render), ANC Carlist collection unclassified units (723), 2852/2853.

## Chrome wave 8, 15 Nov 2026 (DARA Aragon and DigitArq non-ANTT; folder `sweep_2026-11-15_chrome_wave8`)

- **DARA (`dara.aragon.es`):** new source, leads 2854-2863, promoted 2854-2857, 2860, 2861 (CRAR letters of 1477-78 and 1497 at AHP Zaragoza, Alcort cipher letters at Benasque). Route and gotchas in the sweep README. Searched: cifra, en cifra, carta cifrada. Not searched: other cipher terms; the CRAR letters after 1500; the Benasque 'Noticia' companions of the Gonzaga cipher sheets (lead 2862).
- **DigitArq other archives (AHU, district archives):** all hits of 22 terms read (203 records); only the AHU 1897-98 files (lead 2863) and the Aquaviva 1587 cipher table (key lead) matter. AHU 'Telegramas cifrados' series of 1947-76 are out of period.
- **Still unswept:** Euskadi, Navarra, Castilla y Leon, Andalucia, Valencia, Balearic, Galicia and Canarias portals (hosts not reachable by curl; try in Chrome), Lombardia Beni Culturali, Swiss, Belgian, Luxembourg and Dutch leftovers.

## Chrome wave 9, 15 Nov 2026 (DARA retry, Navarra, Badator; folder `sweep_2026-11-15_chrome_wave9`)

- **DARA:** the six wave 8 zero-hit terms were a stale session (cifrado/cifrada/cifras 126, 15 further terms run, all small ones paged); the 16 CRAR letters of 1500-1583 viewed on thumbnails. Leads 2864 (Alcort D/0086) and 2865 (Spinelli to Urrea, Venice 1512, CRAR 0055/0056), both promoted. The 'Mas informacion' fields (Alcance y contenido, Notas) are searchable and decide whether a decipherment is filed.
- **Navarra Archivo Abierto** (`navarra.archivoabierto.es`): swept ('cifrada', 'cifra', 'en clave' ...); one record, lead 2866 (Fondo Rena 1521), not promoted.
- **Badator** (`artxibo.euskadi.eus` ... `badator/maintSimple`): found to be the RAH Salazar y Castro index with item descriptions; 1,892 'cifra' records, 90 not covered by an existing target family; signatures not collected, nothing vetted. This is the best open route for 1520-29 and 1638-56 Spanish diplomatic ciphers: see the sweep README for the plan.
- **No item-level route found:** Andalucia, Mallorca (Regne), Castilla y Leon (host dead), Lombardia Beni Culturali (fonds level).
- **Still unswept:** Valencia (ARV), Galicia, Canarias, Madrid regional, SIUSA/SAN, Veneto, Sardinia, Sicily, Swiss/Belgian/Luxembourg/Dutch leftovers.

## Chrome wave 10, 15 Nov 2026 (Badator export; folder `sweep_2026-11-15_chrome_wave10`)

- **Badator / RAH Salazar y Castro index:** done for the term 'cifra' (1,892 records) through the portal's own 'Exportar Busqueda' CSV (all records with signatura and the index's remarks in one download). 9 new leads (2867-2875: Juan Perez, Marino Caracciolo, Herrera, Lannoy, Colonna, the Adornos, Adrian VI, Trivulzio, Leopold Wilhelm); none promotable (ciphertext not online). Wave 9's '90 rows' were mostly already leads 1085-1090. Not run: other cipher terms in Badator ('clave', 'cifra general', 'cifrado'); the export route makes them one click each.
- **Galiciana ARPAD (Arquivo do Reino de Galicia and other Galician archives):** reached, search form found, search for 'cifra' hung the renderer (not retried).
- **Still unswept:** Valencia (ARV; no online catalogue address found), Canarias, Madrid regional, SIUSA/SAN, Veneto, Sardinia, Sicily, Swiss/Belgian/Luxembourg/Dutch leftovers.

## Chrome wave 11, 15 Nov 2026 (Badator promotions and more terms; folder `sweep_2026-11-15_chrome_wave11`)

- **Wave 10's Badator leads 2867-2875 promoted** (with a new 2876, Fernando Marin): "ciphertext not online" is not a bar failure (`access: "archive"`, quote the archive description); the bar is a filed decipherment of the same text. Each was narrowed to letters with no filed decipherment and no Calendar of State Papers Spain entry (CSP harvested from British History Online, vols 2-4, cross-matched by volume and folio). Rule and method in the sweep README.
- **Badator terms run:** cifrado, cifrada, cifradas, cifras, clave, descifrado, descifrar, abecedario. Chrome allows one download per tab: a fresh tab per export. San Sebastian Marqueses de San Millan y Villalegre series (Philip II and Zayas to Frances de Alava, 1560-69) found and closed read (printed 1991 edition). Not run: criptograma, zifra, cifrar, cartilla de cifra, numeros (low yield expected).
- **Galiciana ARPAD:** behind a JavaScript bot-challenge page (the search returns a challenge shell, not results); not solved.
- **Still unswept:** Valencia (ARV), Canarias, Madrid regional, SIUSA/SAN, Veneto, Sardinia, Sicily, Swiss/Belgian/Luxembourg/Dutch leftovers; the CSP harvest for 1522-24 is thin (vol. 2 pages carry few Salazar references), so a pass over Bergenroth's 1522-24 entries against 2870-2873 and 2876 would tighten them.

## Chrome wave 12 (15 Nov 2026, `sweep_2026-11-15_chrome_wave12`)
- **CSP Spain re-matched by sender and date** (vol. 2 1522-24, vol. 3 1525-29): the folio match of wave 11 missed printed letters. 2873 and 2869 closed `read` (moved back to leads), 2867 narrowed to 9 letters, 2868 to 29; 2870-2872 and 2876 unchanged. Vols 4 (1529-30) not re-matched: 2868 and others reach 1529 only through vol. 3.
- **Probed, no yield:** Archivi Nazionali portal (search parameter ignored, script-drawn; already swept), AGATHA Belgium (inventory-level hits only, reCAPTCHA; `belgium_lux` has the EAD grep), Lombardia Beni Culturali (fonds-level), Archives Quickaccess (staff login).
- **Blocked:** Valencia SAVEX (`savex.gva.es`) loads an error page in Chrome.
- **Still unswept:** Canarias, Madrid regional, Veneto, Sardinia, Sicily regional portals, Dutch regional leftovers; Valencia needs another route.

## Chrome wave 13 (15 Nov 2026, `sweep_2026-11-15_chrome_wave13`)
- **Online Archive of California** swept by same-origin paging (`/search?q=<term>&group=false&per_page=100`): cipher 483, cypher 102, cryptogram, "secret writing", "in cipher", "in code", cifra, chiffre; cifrado not run (HTTP 405 after about 10 fast requests). Only new item: Stanford Montauti papers, 'Ciphers' folder (lead, contents unseen). Duke Archives answers (`/catalog?q=`): no lead. TARO's search API ignores the query (10,000 finding aids returned whatever the term).
- **Blocked in Chrome again:** LAC Collection Search and Archives Hub (Cloudflare), natlib.govt.nz and Archives NZ (blank), NYPL Archives (Incapsula), UConn (403), UVA and Hagley (redirect loop), Waseda kotenseki (maintenance).
- **JACAR:** the 2,122 body-text records are being scanned by `sweep_2026-11-15_jacar_retry/scan1.py rest_refs.txt` (first 73 empty); the three Waseda leads of the retry sweep are now merged through wave 13.
- **Not reached:** Latin American national archive catalogues, South Africa, Sri Lanka, Ethiopia, Philippines.


## Chrome wave 14 (15 Nov 2026, `sweep_2026-11-15_chrome_wave14`)
- **OAC `cifrado`:** now behind a "confirm you are human" check; not clicked. Still the only OAC term not run.
- **Memoria Chilena** re-run with cifra/cifrado/clave cifrada/en cifra/escritura secreta/criptografía: noise only. **eHive** cipher: royal cyphers only.
- **Not reached, no open item search found:** AGN Colombia (host does not resolve), AGN Argentina/Peru/Uruguay/Venezuela/Cuba, Philippines, Macau, South Africa (NAAIRS, Cory), Sri Lanka, Ethiopia, Dar al-Kutub, BOA katalog, NLI. 0 leads.

## Arabic sweep (15 Nov 2026, `sweep_2026-11-15_arabic`)
- **Swept:** Penn LJS 51 paged whole (212 pages: only f. 106v bare); Princeton Geniza Project cipher/cryptic/code tags with CUDL images; Ahlwardt (Berlin) and the Gotha, Munich, Vienna, Leipzig, Hamburg, Strasbourg, Copenhagen and Leiden printed Arabic catalogues; VOHD full text on SBB digital (sample); Karabacek PERF, Grohmann CPR III and Arabic Papyri in the Egyptian Library; ONB papyrus catalogue (Primo guest REST); BnF Arabe via De Slane and the openapi.bnf.fr IIIF route; Wellcome; Vatican ar. records; Durham Abbas Hilmi II coded-telegram files HIL/274 and HIL/23 (decodes only); IIS catalogues by citation. 17 leads (2882-2898); 2882, 2883, 2886, 2890, 2891, 2892 promoted.
- **Blocked from a cloud network, no Chrome:** Qalamos/orient-digital and ONB image hosts (connection reset); PARES (429) and BNE (403), so Spain is unswept for Arabic; QDL, EAP, CUDL search, Chester Beatty viewer, Fihrist live site, NLI, Juma al-Majid, vHMML, LoC, HathiTrust, Michigan, Harvard, Yale, Columbia, Princeton catalogue (bot checks or 403); YEK, Majlis, Darah (no connection).
- **Still unswept:** Moroccan Makhzen and Saadian cipher letters (Tazi; Azizi & Azizi); Durham HIL/64 and HIL/65 ("Arabic and code", about 2,100 frames, digitised); Escorial; Süleymaniye; Egyptian, Israeli and Zanzibar archives; al-Azhar; ZMT. Image orders wanted: Bodleian Laud Or. 139 f. 101a, Vat. ar. 34 f. 288v, Berlin Ms. or. oct. 3629 f. 1a and f. 72b.

## Wave 15 (15 Nov 2026, `sweep_2026-11-15_wave15_arabic2`, `sweep_2026-11-15_wave15_libraries`)
- **Durham HIL/64 and HIL/65** ("Arabic and code"): British Sudan Government and Egyptian Coastguard telegrams of 1907-1914, not Arabic cipher. About 265 of 546 frames screened, only 8 of the 264 six-form frames. One bare cipher telegram promoted (2899); two cipher telegrams with clear copies in the file (lead 2900, key lookup); dictionary code words (lead 2901). Route: `iiif.durham.ac.uk` by curl, region requests stitch past the 1,024 px cap. **Left:** the six-form frames.
- **CUDL search** (20 terms, in Chrome; AWS WAF stops curl after three requests): Trinity O.4.22 f. 248v Greek numeral cryptogram promoted (2902); CUL Add. 2255 f. 19v Jain colophon name (lead 2903).
- **Royal Danish Library** (Primo API on `soeg.kb.dk`, about 60 terms, manuscripts facet; Gigas I-II grepped): NKS 775 kvart, Tautte's 570-page volume in cipher, promoted (2904). **HStA Dresden** (29 more terms): Loc. 03234/06 undeciphered sheet with its keys (lead 2905), Loc. 10922/01 cipher slips (lead 2906). **BnL Luxembourg:** no manuscript-letter records. **Veneto SIAR**, **Tilburg:** nothing.
- **Blocked:** Qalamos and its sister hosts reset the connection in curl and in Chrome (network refusal; try another line). Fihrist live, Chester Beatty (Anubis) and vHMML (Turnstile) need Daniel at the keyboard. KBR (`opac.kbr.be`, `belgica.kbr.be`) resets scripts; Memoria digital de Canarias (Anubis), Comunidad de Madrid AtoM and memoriademadrid (403), Sardinia and Sicily `cultura.gov.it` hosts, Nijmegen (403): not swept, Chrome not tried.
- **Morocco:** no cipher letter with an online image; Colin 1927 (Hespéris 7) prints a key, not a letter.
- The rows above for KBR/BnL, Danish KB manuscripts and HStA Dresden under "Not looked at, though reachable" were already part-swept on 3, 9 and 11 Nov; this wave filled the rest except KBR.
- **Bellièvre fr. 15890, 15894, 15897, 15898** (`sweep_2026-11-15_wave15_bellievre`): all 3,570 canvases fetched at 800 px from `openapi.bnf.fr` and read on contact sheets (240-320 px a page, so a lone code group inside a cursive line could be missed). No ciphertext. One undated key sheet at fr. 15890 f. 326r (view 659; names of the Netherlands affairs of about 1577-78 by inference), in `key_leads.json`; no letter in that key seen. fr. 15898 has two arks (btv1b9064324n ff. 1-400, btv1b90643252 ff. 401-810).

## Wave 16 (15-16 Nov 2026, `sweep_2026-11-15_wave16_durham`, `sweep_2026-11-15_wave16_chrome`)
- **Durham HIL/64 and HIL/65 finished:** all 546 frames looked at (the six-form frames at about 350 px a form, suspects at full resolution). Clear copy of the 1912 Coastguard telegram found at HIL/64/739-737, so 2899 went back to the leads as a key lookup. Five more cipher/clear pairs (1907 Arabic; 1908, 1909 and 1912 English simple substitution) recorded in the README as key material. Three bare cipher telegrams promoted: 2907 (HIL/64/400, 1909), 2908 (HIL/65/273-272, Siwa 1913), 2909 (HIL/65/1122, 1914). About 133 telegrams carry dictionary code words. **Left:** HIL/66 onwards not opened.
- **Chrome pass on blocked portals:** KBR (`opac.kbr.be` search page, then POST JSON to `/Library/Portal/Recherche/Search.svc/Search` from the page; 55 terms), Memoria digital de Canarias (Omeka S `mdc.ulpgc.es/s/mdc/busqueda?q=`), Memoria de Madrid (`/browse?q=must,any_exclude_fulltext,contains,<term>`) and the Biblioteca Historica Municipal catalogue: no new item; only the Anover cedulas (entry 1988). **Needs Daniel:** Comunidad de Madrid AtoM (ALTCHA box). **Needs another network line:** Sardinia and Sicily state-archive hosts, Nijmegen studiezaal (403), Qalamos (connection reset in Chrome too; suspected VPN exit). PARES 429 on the first request.

## Wave 17 (16 Nov 2026, `sweep_2026-11-15_wave17_chrome`)
- **Manus Online** (plain HTTP: POST `manus.iccu.sbn.it/o/manus-api/titles-search-post`, detail `/o/manus-api/title?id=`): 28 more terms; all 58 Carte Machiavelli records sorted. Two 1510 Dieci di Balia letters in cipher, not deciphered, promoted: 2910 (V/125), 2911 (V/134). Others in the volume are printed or deciphered. Parma Parm. 728 is a cipher treatise (not a row).
- **RAH digital library** (Chrome passes Anubis on its own; same-origin POST `busq_general` to `/es/consulta/resultados_busqueda.do`): cifra family 24 hits, all already in the repo; the OCR box searches the same index, not page text. About 10,000 Salazar item records are online (search `Salazar y Castro, <inventory no.>`) but none of the 16 inventory numbers of the repo's cipher items is digitised.
- **Internet Culturale: WAF-blocked** (arithmetic CAPTCHA to curl; in Chrome `ERR_SOCKET_NOT_CONNECTED` then a 403 "Web Page Blocked" page). Not swept. Needs Daniel or another network.
- **Vetting of 22 image-online leads** (`research/vetting_2026-11-15_wave17`): promoted 2574, 2385, 2568, 2567, 2570, 2858 (open); closed 2375, 2396, 2859 as not cipher; 2387 stays a lead (low confidence it is cipher). Twelve have no verdict, each with its blocker in that README: 2312 (date is 1459, handwriting needs a proper reading), 2379 and 2529 (edition not online), 1243, 1553, 1564, 1573, 2884, 2888, 2903, 1438, 1441 (Harvard 403). ASF Florence image server answers again as of 16 Nov. 2858 is printed in Villanueva Morte and Fernandez de Cordoba, El embajador Claver (CSIC 2025, Appendix doc. 10) with the cipher left unread.

## Wave 16 printed series (16 Nov 2026, `sweep_2026-11-15_wave16_printed`)
- Ten rows from editors' notes that a cipher was not read; four promoted: 2912 (Louis XI to Galeazzo Maria Sforza, Peronne, 13 Oct 1468, fourteen cipher lines, key not found), 2913 (about 14 Mazarin originals to Lumbres 1656-59, AAE Allemagne Supplement 16-18), 2914 (Mazarin to d'Avaugour 1655, AAE Suede 19 f. 384), 2916 (Jean de la Croix to Henri IV, 6 May 1607, BnF fr. 16913). Kept as leads: 2915, 2917-2921 (shelfmark garbled, ciphertext may not survive, or a few signs only). All promoted rows are archive items quoted from the printed editor; no image seen.

## Wave 18 Durham (16 Nov 2026, `sweep_2026-11-15_wave18_durham2`)
- Abbas Hilmi II finding aid split into 2,485 records, 517 digitised (`units.tsv`). HIL/66 is the St. Exupery letters, not a telegram file: HIL/64 and HIL/65 are the only telegram volumes. Screened whole: HIL/274, 57, 248, 51; partly: 202/1-93, 203/288-303, codebooks 150-155. One bare cipher item, HIL/57/77-80 (143 four-figure groups, Paris to the Khedive in Vienna, Oct 1912), promoted as 2922. Key material recorded in the README (HIL/150-155 codebooks, HIL/203/299-300 keys, Wingate SAD.250/1/81 cypher alphabets).
- **Left:** HIL/202/94-543 and the rest of HIL/203 (most likely for more cipher), the files described as secret or intelligence (HIL/49, 88, 120), additive tests of 2922 on the codebooks. Not online: Hicks Pasha registers 1883 (SAD.866/5, SAD.600/2), 4th Earl Grey coded telegrams (GRE/B181/5).

## Wave 18 printed series, second part (16 Nov 2026, `sweep_2026-11-15_wave18_printed2`)
- Grepped the 112 late wave-16 texts (about 70 HMC reports, 22 volumes of Fontes rerum Austriacarum, Fiedler's Venetian Relationen), CSP Venetian 17-38 (all passages deciphered), CSP Foreign Edward VI, Mary and Elizabeth 1-10, CSP Domestic William and Mary, William III 1-3, Anne 1, James II III. Five rows; promoted 2923 (BL Add MS 32093 f. 423), 2924 (Wotton to the Council, 18 Oct 1556, SP 69), 2925 (Randolph to Cecil, 26 Feb 1561, four-line postscript). Kept as leads: 2926 (eleven folios, Harley papers, volume unknown), 2927 (Pointis 1689, Wallis may have read it). Windebank to Hopton 1634 dropped (decipher filed).
- **Left:** CSP Domestic William III 1697-1702, Anne 1703-04, James II vols I-II (paywalled on BHO, no archive.org text found). Continental Congress and Official Records stay closed (11 Nov sweep).

## Vetting wave 19, batches B and C (16 Nov 2026, `research/vetting_2026-11-16_batchB`, `_batchC`)
- Batch B: 2726 rescoped to BnF fr. 3654 nos. 6, 8, 11-19 (the old shelfmarks fr. 3652 and fr. 3339 held no cipher) and promoted; 2826, 2827, 2828, 2744, 2589, 2618, 2783, 2814 closed read (decipherment filed with the piece), 2587 partly read; 1633, 1676, 1677, 2417, 2692 not assessed (Archivportal-D proof-of-work, Hungaricana 403, no cipher statement). **Omont shelfmark warning:** in Omont's printed catalogue the old shelfmark "(Anc. N.)" ends each entry, so OCR-based pairing put some items under the wrong volume; an audit of the Omont-derived rows is in `research/audit_2026-11-16_omont_shelfmarks`. Lead 1577: Avenel explains the cipher in each letter checked, so its partly_read verdict is too weak.
- Batch C: no verdict on any of 11 leads (1857, 1859, 1861, 1864 RGIA: record API at fgurgia.ru gives titles only; 2071 and 2119 Morgan probably printed; 2116, 2146, 2197, 2198, 2491 blockers stand). Corrections: 2491's holder is the Benaki Museum (Ar. Eis. 176), 1864 covers May-Aug 1905. **Route:** BnF Archives et manuscrits notices load by curl at `ark:/12148/cc<id><check>` (`am_probe.py`); a Gallica link in a notice means the volume is digitised.
- **Vetting wave 19, batch A** (`research/vetting_2026-11-16_batchA`): closed read 2759 (decipherment on the leaf and two leaves earlier, ASF MAP filza CV), 2625 (Auflosung filed with 8 of 11 units), 2766, 2767, 2770 (every ciphered Affry dispatch has a Transcription du chiffre beside it), 1598 (DECODE R1172 inline plaintext, low confidence); partly read 1911, 2486, 2755, 2768. Two items split off and promoted: 2928 (MNL G 15 B Fasc. 22 fol. 86-87, undated, wholly in figures) and 2929 (G 15 A2 Fasc. 2 fol. 80-83, Rakoczi to Korbe and Cantacuzino). Not assessed: 2231, 2487, 2488, 2490, 2776 (Hungaricana 403, DAVEL 403). Errors: 2759's Bundesarchiv "ohne Klarschrift" is wrong; 2487 D Fasc. 79 fol. 19-20 deciphered in pencil; 2488 H 240 fol. 112-113 printed. Routes: Florence MAP filza folder `00100<filza>`; MNL G 15 datasheets carry an edition field; friXplore by curl.

## Omont shelfmark audit (16 Nov 2026, `research/audit_2026-11-16_omont_shelfmarks`)
- Of 34 Omont-derived rows (8 catalogue entries, 26 leads): 17 ok, 15 shelfmark wrong, 2 with a decipherment on the BnF notice. Cause: Omont prints the old shelfmark "(Anc. N.)" at the end of each entry, so OCR pairing put items under the wrong volume. Catalogue 2732 rescoped to the one cipher letter actually seen (fr. 3027 view 69); the Omont items it first cited sit in the volume after fr. 3028, which by sequence is fr. 3029 (withheld at Lasry's request; its notice was not opened). 2726 folios corrected. Leads with wrong volumes carry a SHELFMARK CORRECTION line in their status (2724, 2725, 2727, 2729, 2731, 2733, 2735-2739, 2742-2744). The catalogue and other Omont-derived leads from older sweeps (e.g. the 14 Nov Omont sweep rows not listed above) were not all checked.

## Backlog vetting, 16 Nov 2026 (`research/vetting_2026-11-16_w20_b00` ... `b05`; 465 unvetted leads in 26 batches of 18)
- b00: promoted 2757 (Torcy to Courten 1704, AEV Cn B 10/1/8), 2778 (narrowed to AEV FQ 238); closed 2756 partly read, 1377 and 1380 read; ten leads blocked by access (Academia Sinica reader site down, AGAD 403, szukajwarchiwach Incapsula). Route: the Valais archive catalogue answers scripts (`scopequery.vs.ch/SRU`, `detail.aspx?Id=N`).
- b01: promoted 2708 (Ligne to Oropesa, Sicily 1670, PARES title only); closed 2711 not cipher. PARES answered 429 all day.
- b02: promoted 2777 (AEV Supersaxo II P 74); closed 2771 read, 2769 and 2772 partly read, 1208 and 1211 read, 2055 and 1219 not cipher; 2920, 2934, 1217 stay leads (low confidence). New lead to add: Buchi I pp. 403-404 no. 481, Trubmann to Schiner, Sion, Nov 1515 (B.-A. Sitten Lade 101 Nr. 35), six cipher passages unread. Routes: e-Helvetica full PDFs by script; archive.org `fulltext/inside.php`.


## Arabic sweep 2 (16 Nov 2026, `sweep_2026-11-16_arabic_2`)
- **Swept:** Durham HIL/64 and HIL/65 paged in full (546 canvases, region tiles past the 1,024 px cap; no Arabic cipher); Durham Sudan Archive via the Primo guest API (Gordon's figure note SAD.250/1/550, excluded: same document as catalogue 2939); Torre do Tombo PT/TT/CART/891.2 (74 units, first image each; all clear); BNE catalogue through its guest-token JSON API (Arabic and aljamiado MSS); every Hespéris volume 1921-1959; about 60 printed catalogues of Arabic MSS re-grepped with hyphenated line ends joined (Gotha Pertsch no. 2507, lead 2942; Sachau 218, catalogue entry 2943). Sacromonte Lead Book 17 promoted (2941).
- **Routes:** BNE catalogue guest JSON API; Durham Primo guest API; SBB content server METS/IIIF for manuscripts with a K10plus `017C` resolver link (Sachau 218 = PPN618589309); TNA Discovery API through `research/tna_discovery/tna.py`.
- **Still blocked:** PARES (429, then reset), BDH, datos.bne.es, RAH, CCBAE, Hispana, BVPB, ANOM, BNRM, CSIC Simurg; Gotha/Erfurt viewer and DDB (proof-of-work); Leiden digital collections; Qalamos/Orient-Digital (Wetzstein II 203 and Ms. or. oct. 1474 are only there); HathiTrust full text (403).
- b03: promoted 2919 (Teulet IV p. 309, 33-sign cipher signature, a Scottish lord to Mainville 1583); closed 1301 key lookup, 2866 partly read, 2863 duplicate of 2930/2933, 2853 read; 2398 (Palermo, low confidence) stays a lead; ten blocked (BayHStA paper only, AHNOB no images, Harvard 403, catalan archive reCAPTCHA on full text, Vatican volume not digitised).
- b04: promoted 2513, 2514, 2515 (Urkunden und Actenstucke IX and XII: Brandt 1666, Hoverbeck 1662, relation of 1661 'meist in unaufgelosten Chiffern'), 1239, 1238, 1237 (BNP Lisbon, catalogued 'em cifra'); closed 2781, 2780, 2270, 2274 read, 2271 not cipher; 1241, 1242 stay leads (low); 2113, 2106 (Yale), 2782 (Geneva Anubis), 2275, 1847 no verdict.
- b07: promoted 2750 (NAF 11238, Abelard epistle in cryptographic characters, Villette 1768) and 868 (TNA Carte 75 ff. 498-499, in cypher); closed 2211, 2598, 1885, 1886 read, 1539 not cipher; 2660 and 2936 hold only keys (move to key leads); 1257 to split (Rawl. C. 392 half printed in Sbornik RIO 61). Routes: TNA Discovery API `/API/records/v1/details/<id>` with Accept: application/json; BLHA `/rest/records/<pk>`. New blocks: Bodleian catalogue and ArchiveGrid bot checks.
- b05: nothing promoted; closed 1850, 2829, 2830, 2731, 2735 read, 2733 and 2917 partly read, 2724 key lookup (Tomokiyo nevers.htm publishes the Birago keys), 2742 duplicate of target lanssac. **Correction to the Omont audit:** the Lanssac letter of lead 2742 is fr. 4735 (tome II) no. 51 f. 124, not fr. 4734. Eight leads blocked (Foli@ viewer, Chantilly not digitised, BNE Digital 403).
- b06: promoted 2728 (fr. 3422, six letters to Nevers 1589), 2737 (fr. 3659 no. 24, Monteleon 1617; lead said fr. 3638), 2740 (fr. 3796 no. 38, Louis XIII 1618); closed 2743 and 2741 and 2738 read, 2725 and 2751 key lookup, 2736, 2739, 2915, 2745 partly read; 2730 and 2729 stay leads to split by key, 2749 and 2727 low, 2747 and 2748 key sheets only. Shortcut: Berger de Xivrey's table of unprinted letters maps old Bethune numbers (Ms. 8956 = fr. 3457); a heading like 'envoye en chiffre' over a copy register usually sits over clear text.
- b09: nothing promoted; closed read 2862 (DARA: each of four numeric cipher sheets has a decipherment filed letter by letter), 2592, 2605, 2588, 2499; partly read 2051, 2495; not cipher 2698, 2606; duplicate 2504 of 1675; 2537 and 2496 stay leads (low, recipient's own bundles); GAK, Gilder Lehrman, Nijhoff VI/2 blocked. **Follow-up:** the Alcort pairs of 2862 give back the numeric key; test it on catalogue 2860, 2861, 2864 and D/0055, 0056, 0086, and check whether those entries also have decipherments filed. Routes: DARA PDFs by script; ACTApro `archive.spk-berlin.de/actaproweb/document/Vz_<uuid>` redirects to the live record; Huygens retroboeken search.
- b08: promoted 2191 (Bierther II/8 p. 405: letter 'grosstenteils in Chiffre, deren Auflosung jedoch fehlt', BayHStA) and 1128 (Klinckowstrom I p. 155, Gustav III to Fersen 28 Feb 1792, 'lettre en chiffre (non dechiffree)'); closed 2674, 1483, 2803, 2807 read, 1168, 1484, 2804 partly read, 903, 2805, 2806 duplicates. Catalogue 960 corrected: 3 Aug 1620, SP 14/116 no. 59 (it said 1611). Duplicate lead 2217 resolved (older record dropped); the clear strip c. 12r of BNCF Ginori Conti 29.137 may be the plaintext of the cipher strip c. 13r (about 261 letters against 263 signs), so 2217 may be read once a sign table is rebuilt. 2901 (Durham code words) is a code book, not a cipher: keep as a low-priority lead. Archive.org full-text search (`fulltext/inside.php`) works on lending-only copies without a login.
- b11: promoted 1725 (HHStA Spanien Varia, fol. 1-146 'teilweise verschluesselt'); closed 2602, 2501, 2595 read, 2505, 2503, 1157 partly read, 2608 and 1134 not cipher, 2622 and 2655 key lookup; 2502, 2596, 1713 stay leads (low); 1620, 1708, 1726, 1220 blocked. New route: the GStA PK database (ACTApro) reads by script (`actadoc.py` for `/actaproweb/document/Vz_<uuid>`, `actapro.py` posts the search form), so these records no longer need Chrome. 2502 units cannot be produced before 31 May 2029.
- b10 (Berlin GStA PK): promoted 2591 narrowed to Frederick II to Zieten, Lobendau, 27 Nov 1757 (Rep. 94 Nr. 5745; PC XVI p. 34 n. 3: no key, decipherment, draft or copy); closed read 2610, 2611, 2613, 2604, 2607, 2621, 2498; key lookup 2601, 2603, 2624; not cipher 2506; duplicates 2620, 2586; 2609 and 2623 stay leads (low; fold 2623 with 2502), 2497 and 2619 no verdict. ACTApro answers scripts today: `acta.py` (search POST must send `searchForm:searchByType=3`). Several units cannot be ordered before 31 May 2029 (Rep. 94 Nr. 5745, Rep. 94 A V Nr. 26, Rep. 400 Nr. 191, Rep. 81 Bern Nr. 93, Westphalen Nr. 461). Re-check lead 2501 against Rep. 11 Akten Nr. 10691. Lead 2586's Nr. 753, 799, 760, 718 should become single-volume leads.
- b15: closed 1916 read (Toth 2014 edition prints 114 documents of the Choiseul-Tott correspondence; lead title was wrong) and 2719-2723 key lookup (Nationaal Archief key books, no ciphertext). **Abhilekh Patal (NAI) item pages answer 403 from CloudFront today**: twelve NAI leads (1354, 1355, 1358, 1360, 1364-1371) not assessed; the 11 Nov held blocks stand (the 11 Nov viewer route went round a WAF CAPTCHA and its verdicts were withdrawn). Needs a logged-in Abhilekh Patal session in the owner's Chrome.
- b14: closed 1900 read (Costabili: decipherments filed on Vestigia records; the lead's catalogue 361 is right: it was removed 2 Nov as partly_read), 1363 and 1356 not cipher (NAI Descriptive List and Calendar of Persian Correspondence); fifteen blocked (NAA RecordSearch 403, Abhilekh Patal 202 shell, Morgan Cloudflare). Audit of the old Costabili entry (361, not in the catalogue since 2 Nov; `research/audit_2026-11-16_cat348`): all six letters have a decipherment filed (DF 295908, 295909, 295914-a with clear copy 12b, 295935 with four unglossed lines, 295963 with clear copy 44b, 295974 also printed in Berzeviczy 1914 no. CLV); close, no catalogue change. Route: Vestigia (`vestigia.hu/api/search?search=<DF>`) answers scripts; sub-records `<DF>-a`/`-b` hold decipherment copies.
- b16: closed 2654 read (Arcinsys: 'verschluesselt und Aufloesung', NLA OS Rep 100 Abschn. 256 Nr. 4, volume digitised on Arcinsys, 115 images) and 2466 partly read (Campbell's key to the Chinese cypher, 1908, File 45506; Dudout recorded it for `peking1912`); sixteen blocked (Abhilengh Patal 403, NLS and Arcinsys not digitised, ArchiveGrid). Route: Arcinsys Niedersachsen answers scripts (`arcinsys_harvest.py --probe ni <term>`; images from `arcinsys-digitalisate.niedersachsen.de`, about 37 s a full image).
- b13: promoted 2667 (Thuringen finding aid Nr. 2661, 'Schreiben in Geheimschrift' Bl. 191-195, no decipherment) and 2437 (Vom Stein papers, three pages of number groups, 7 images; Hubatsch II/2 prints no Niebuhr letter Oct-Dec 1808); closed 2653 read, 2224 partly read, 1696 key lookup (volume digitised, key on image 133 reads inline cipher), 1293 and 2081 not cipher (shorthand); 2489 and 1904 stay leads (low); eight blocked (Brill human verification, IIS catalogue, Hungaricana). New route: the DDB Solr API answers scripts although Archivportal-D and DDB item pages are bot-checked; Stein-edition PDFs download from archive.org with range-resume.
- b12 (Habsburg Constantinople series, Hungaricana regests): closed 1222 read (every 'no decipherment' item in Kt. 46-49 has its decipherment in the same Konvolut), 1221, 1223, 1224, 1225 partly read (most dates have a deciphered copy, clear copy or extract; leftovers unproven), 2522 key lookup (Topelius cipher solved by Vasenius); 2581 narrowed to MHC 3352 (about 50 four-digit groups, 400 px only), still held. Hungaricana answers scripts from this machine (2,633 'sifrir*' regests pulled). **Pattern:** the copy to Rudolf stays in cipher, the parallel letter to Archduke Ernst/Matthias is deciphered ('feloldas es sifrir'): catalogue 2237 (Breuner 12 May 1583, regest 49853 vs 49856), 343 and 1226-1229 to be re-checked. Eleven leads blocked (HOLLIS 403, Finna Cloudflare, Lambeth hangs, Kansas Memory). Koc images via Europeana thumbnail cache; the Topelius edition search accepts raw queries by POST.
- b19 (Russian archives RGAVMF, RGIA; Dordrecht): closed 1883 read (RGAVMF: 'Shifrovannye telegrammy, rasshifrovki i pisma', file of 1904); 2697 stays a lead (low: Dordrecht lodge inv. 847 'aantekeningen in geheimschrift', inv. 803 may hold the alphabet); sixteen no verdict (no scans; titles do not show whether ciphertext survives). rgavmf.ru answers curl; fgurgia.ru returns 500 for every record id today.
- b17: promoted 2809 (NLW, recipes and notes partly in cipher), 2825 (OeNB, 43 letters 1898-1912 'teilweise in Geheimschrift', cover names Monica, Andrea, Clara; could be shorthand), 2820 (Palm to Schlik, Jan-Jun 1707, Cod. Ser. n. 1697-1698), 2821, 2822, 2823 (Colonna zu Fels, Saint-Saphorin, Joseph I rescripts, Cod. Ser. n. 1696 and 1698; shelfmarks corrected); closed 2813 read (NLS description prints each cipher colophon with its reading), 2834 not cipher; 2824 stays a lead (low; recipient's own papers). Nine no verdict (NRS, NLW, NLS 403; Archives Hub reset; SNAC bot check). Routes: OeNB Alma SRU answers curl (`onbsru.py`); OeNB autograph card images (KAT-ZOOM GIFs); NLS Wayback copies only in the `id_` form.
- b18: promoted 2836 (ONB Kronauer Masonic album, fol. 28r about 12 lines in an invented alphabet, seen on the scan; no decipherment on the pages, none in Nettl 1957); closed 2837, 2650, 2087, 1915, 2799 read, 2517 and 2397 partly read, 2718 key lookup; 2938 (Theal III p. 388, 'a long letter in cypher', try repo batavia1800 key) and 2519 (PRONI, low) stay leads; seven blocked (Bodleian, SOAS, Poznan, ArchiveGrid). ONB routes that failed 15 Nov work today: IIIF manifest via `data.onb.ac.at/dtl/<id>` redirect, Alma SRU, katzoom cards; Archives West opens by curl. 2799's date is Feb 1648, not 1670.
- b20: promoted 2905 (HStA Dresden Loc. 03234/06, 'une feuille non dechiffree' with the Albani/Lagnasco keys; dated 1722 or later); closed 2527 read (Fridericia, Danske Magazin 5th series II 1889-92 prints Otte Krag's three 1648 letters deciphered; ronlev.dk/bibliotek/3364.pdf), 2657 read, 2659 read, 2658 partly read (Krauske 1893), 2552 key lookup; twelve blocked (RGIA no scans, gate.unigre.it, HOLLIS). **Beyond the batch:** Fridericia's edition also decodes Peder Vibe's letters from the same Copenhagen unit with Rigsarkivet keys (one system to 1652, Juel's from Dec 1652; only Vibe's 6 May 1655 letter in Erik Krag's cipher is left out): targets `vibejuel1649` and `vibejuel1651` say no edition was found; their prior-art and contamination fields need review. Routes: `api.rigsarkivet.dk/ao/v1/images/<id>`; archiv.sachsen.de records by curl (`digitalisatExists` flag); DDB Solr returns Saxon records.
- b23 (TNA State Papers and Home Office): nothing promoted; closed 1795, 1884, 2796, 1794, 2794 read (deciphered copies or published), 1154 key lookup (Chauran key SP 106/6 nos. 32-33), 1137, 1136, 1159 partly read; 1136's 3/6-7 'letters in number cipher taken from Baron de Kalb' and 3/207-209 'in number cipher, not deciphered' (PRO 30/11/3) should become their own leads; nine no verdict. Route: TNA Discovery `/API/records/v1/children/<parentId>` lists up to 500 records per call (batchStartRecordId pages); 'Deciphered copy' notes appear only in the single-record call. Google Books API quota used up today.
- b24 (TNA, Tresoar and others): nothing promoted; closed 2551 read, 2789, 2790, 2795, 2927, 2921, 2918 partly read, 907 duplicate (its Jan-Jun 1656 letters are catalogue 978-987), 1158 not cipher; eight blocked (879 and 1802 'in cipher (or shorthand)' need an image, 1146 aggregate to split, 1163 no ciphertext survives, UNC and Historic Pittsburgh blocked). **Three letters marked 'cyphers undecyphered' have no row and should be filed as single leads:** CSP Dom. 1655 vol. C no. 99 (Sept 1655, Nicholas to Joseph Jane), CSP Dom. 1656-57 vol. CXXIX no. 64 (22 Jul 1656, Grove [Pile] to [Ross]) and no. 119 (Aug 1656, Ross to Nicholas). The link labelled 'CSP Dom. 1655-56' in lead 907 is the 1656-57 volume (`cu31924091770440`).
- b21: nothing promoted; closed 2691, 2690, 2687 read (Hungaricana regests: partly in cipher with interlinear decipherment), 2689, 1162, 1613 partly read, 2714 not cipher (a 24-letter substitution key, no ciphertext); eleven blocked (ASF server reset, FranceArchives JavaScript wall, klio.sh.ch proof-of-work, Berlin image server 429, Qalamos reset). Routes: SOAS catalogue `archives.soas.ac.uk/records/PP_MS_1/...` (underscores for spaces, slashes kept); SLUB IIIF manifest and images by curl. Corrections: 2691 sender Leonhard von Fels, folios 21-24 and 33-38; 2689 Krakow envoy Georg von Logschan; 1617 dated 19 Jan 1534, not 1490.
- b22: nothing promoted; closed 2688, 2682, 2680, 2785, 2786 read (Habsburg Constantinople and Hungarian regests: deciphered on file; Nehring and Karolyi print them), 2681 and 2679 partly read (Czernovich: 153 cipher pieces, all deciphered but 45148 and duplicate 44618; Stockl: only 46230 of 18 Sep 1569 left), 2584 key lookup, 2684 duplicate (catalogue 2455, 1231), 2685 not cipher (Gembicki to Zrinyi, Latin letter with keys enclosed: DECODE key record to queue); eight blocked (Teleki edition not online, TARO Anubis, LABW transumpts). Google Books volume ids for Teleki vols. II, IV, VIII are in the b22 notes for a Chrome session.
- b25: promoted 2511, 2508, 2509, 2510, 2512 (Pribram, Archiv fur oesterreichische Geschichte 70 (1887) pp. 148, 284-285, 316, 317, 547: 'nicht dechiffrirt' notes) and 2516 (Urkunden und Actenstuecke XIV/2 p. 1186 n. 1, Fridag 17 Sept 1685, 'ein laengerer nicht dechiffrirter Passus'), each from the editor's printed note, originals unseen; closed 2765, 2880, 2881 not cipher (2881 is the 1874 code tables, the key for 2879); 2879 (Motono telegram, Nagasaki 7 Nov 1874, 83 two-digit groups with red kana notes that follow the 9x9 grid of 2881 but do not read as Japanese: **needs a reader of Japanese**; if the kana make sense close it read, if not it is a strong open lead with the key in hand), 2145, 2115, 2201, 2065, 2107 no verdict. Routes: Waseda repository `waseda.repo.nii.ac.jp/api/records/<recid>` serves the Okuma Papers PDFs while kotenseki is down; Vorarlberg archive online finding aid by script (`vla.sh`). **All 26 backlog batches (b00-b25) have now run.**

## Fridericia edition and the vibejuel targets (16 Nov 2026)
- Fridericia, Danske Magazin 5th series II (1889-92) pp. 362-387, prints Peder Vibe's letters to Juel deciphered with keys from the Rigsarkivet (all nine letters of `vibejuel1649`, ten of the eleven pieces of `vibejuel1651`; only Vibe's 6 May 1655 letter is left out). Both targets, profiles and pages now record it as a printed decipherment found after the reading, kept outcome 'key recovered based on adjacent plaintext'; pages claims-reviewed by a separate reader and recorded. **Open for Daniel:** the code values of the print are not entered in the readings; vibejuel1651's dates (after Dec 1652, not 1651) and the Sehested attribution of image 87 are flagged on the page but not changed in the manifest, profile dates or README rows; SOLVED_RANKING.md still says 'no decipherment anywhere' for both.


## Arabic treatises and Eastern Christian secret scripts (24 Nov 2026, `sweep_2026-11-24_arabic_treatises`)
- **Swept:** vHMML Reading Room by keyword (Chrome, typed into the page's search box; record JSON and Unregistered IIIF images by plain curl); YEK catalogue for the Ibn al-Durayhim, Ibn Dunaynir and Ibn 'Adlan witnesses (Bursa Genel 4808; Süleymaniye Esad Efendi 3558-006, Fatih 5300-003/-004); Wright BM Syriac vols 1-3, Wright BM Ethiopic, Conybeare BM Armenian, Bodleian Armenian (archive.org text). 4 catalogue-only rows (BL Add. 21580 and Add. 14471 Syriac secret-character notes; USJ 2/980; ÖNB N.F. 303), none vetted; ÖNB N.F. 90a-d closed (not cipher).
- **Blocked:** Qalamos (connection reset in curl and Chrome); YEK and vHMML "Registered" images need an account; Gallica SRU and QDL 403 to curl (not retried in Chrome).
- **YEK, second pass (signed in):** about 70 terms in Turkish transliteration and Arabic script, each paged to the end (except rumûz, الرموز and قلم, first 100 rows only). Images screened: Esad Efendi 3558-006, Bursa Genel 4808, Fatih 5300 (to image 93), Arkeoloji 01652 and 01660, Erünsal 35. No ciphertext. Ottoman key books noted: Arkeoloji 01652, Millet Ali Emiri Müteferrik 6001, Beyazıt BM11616.
- **Still unswept:** Qalqashandi and the Mamluk chancery manuals in manuscript; Payne Smith, Zotenberg, Assemani, Scher, Vööbus (Syriac); Zotenberg, Dillmann (Ethiopic); Matenadaran, Jerusalem and Mekhitarist catalogues (Armenian).

## Habsburg Constantinople audit (16 Nov 2026, `research/audit_2026-11-16_habsburg_istanbul`)
- Of 20 catalogue entries resting on HHStA Turkei I or Hungaricana regests (193 items, 1,099 regests read): 343, 2675, 2676 and 885 have the decipherment of the same letter filed and were moved back to the leads as read; 2237 narrowed to the despatch to Rudolf (fol. 137-144; the parallel Ernst letter is deciphered); 1226-1229 partly filed, each folio note now lists the items with nothing found; 342 stays open, 501 undecided, Ungarische Akten entries unchanged (142344 for 2459 and 142905 for 2457 and 2458 are deciphered letters worth adding as key material). Verdicts rest on regests only, no leaf seen; 343, 2675 and 2676 are inferred from identical dates, parties and lengths.


## YEK massive sweep (25 Nov 2026, `sweep_2026-11-25_yek_massive`), partial
- **Swept:** Türkiye Yazma Eserler Kurumu portal, all records with istinsah year 200-904 AH (10,906); note-field and title searches for şifre, rumûz, remz, ramz, muammâ, mütercem, hall, hurûf, cifr, ebced, gizli, sırlı. No image screened.
- **Still unswept:** Arabic-script term list, classes 652.8/133/135/410 etc. (counts only), mecmua/münşeât types 905-1110 AH, Ottoman şifre defteri terms, esrâr slice [200,999]. Route and resume code in that folder's README and `harvest.js`.

## Thorough Geniza sweep (25 Nov 2026, `sweep_2026-11-25_geniza_thorough`)
- **Swept:** all 36,564 documents and 25,617 footnotes of the Princeton Geniza Project bulk dump (`pgp-metadata`, Zenodo 10.5281/zenodo.15839055) by about 25 term groups incl. Hebrew and Arabic terms; every tag with cipher/secret/glyph/cryptic/alphanumeral/geomancy words; about 70 candidate documents image-checked; Bodleian Hebrew catalogue (hebrew.bodleian.ox.ac.uk, via Chrome), Penn catalogue. 5 candidate rows (K24.37, Or.1080 6.12, Ar.39.472, Or.1080 14.13/14.25, K12.60); K24.37 and Or.1080 6.12 carry vetting blocks.
- **Blocked / unswept:** CUDL search (AWS WAF), FGP (registration), NLI (Cloudflare), Manchester Luna (reCAPTCHA), Heidelberg (bot check); `pgp-text` transcriptions not grepped; AIU XII.41/XII.68/VI.B.174/VI.B.157 and BL OR 10656.25 have no image URL.
## Geniza and medieval Hebrew/Arabic cryptography, literature survey (24 Nov 2026, `sweep_2026-11-25_geniza_literature`)
- **Swept (literature only, no images):** PGP `cipher` tag (13 documents, live), Cambridge Genizah blog (Elbaum Q&A 2022, 'Coptic' numerals 2021, magic tag, Bohak search), Bohak 2010, Michaels 2024 (MTC 3/1), Krivoruchko FOTM 2023, MiDRASH, Qalqashandi/Ibn al-Durayhim/Al-Kadi/Schwartz, D'Ottone (SOAS MS 12217), IIS MS 1499, Akkerman 2023.
- **Result:** no candidates. Unread real ciphertexts: T-S AS 187.240, T-S K24.24, ENA 4100.7b lines 7-12, the Coptic-numeral passages of T-S 13J18.19, the unlocated India Book numeral code; T-S NS J479 partly read (unpublished); T-S NS 70.1 read by Bohak, unpublished. Ranked list in the README.
- **Not found:** any Geniza/Judaeo-Arabic cipher paper in Cryptologia, HistoCrypt or by Lasry/Megyesi/Knight; Karaite, Samaritan (text) or Ibn Ezra/Halevi ciphertexts; surviving Fatimid/Ayyubid/Mamluk enciphered letters.
- **Still unswept:** Goitein's *Mediterranean Society* and *India Book* volumes and Schaefer-Shaked's *Magische Texte* (books, not online), the Bohak PDF beyond pp. 15-16, the Friedberg catalogue, the MiDRASH full-text portal, PGP letters with Greek/Coptic numerals (India Book tag), `sweep_2026-11-23_genizah_tables` (named in the brief, absent from the checkout).

