# Sweep coverage: what has not been swept

As of 4 Nov 2026 (sweeps A, B and D of that day added at the end). This is an index: each sweep's own README or `coverage.md` holds the detail, and the folder named on
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
| Hungary, Czech lands, Slovakia | MNL, Národní archiv, Moravian archives | Only through other sweeps |
| Italian state archives | Turin, Genoa | No shelfmarks |
| Italian state archives | Naples, Palermo | Shelfmarks, but no sweep of the archives themselves |
| German libraries | Wolfenbüttel HAB (Extravagantes; `diglib.hab.de` resets from this network, printed Heinemann catalogue grepped in `sweep_2026-11_german_portals_2`) | Almost nothing |
| National libraries | Portuguese BNP, Dutch KB | No sweep |
| Other | Africa | Little or nothing |

## Tried and blocked

| Source | Block as recorded | Sweep |
|---|---|---|
| `*.cultura.gov.it`: Milan, Mantua, Modena, Florence and Cremona state archives, SIUSA, Antenati | Connection refused or timeout, looked like an outage; retry first | `italian_catalogues`, `milan_archives`, `medici_bia` |
| Braidense, Trivulziana | See the sweep | `milan_archives` |
| DigiVatLib | Connection reset in Chrome, TLS error in curl; needs another network | `chrome_pass_2026-11` |
| NLS, National Library of Wales | Cloudflare challenge | `uk_libraries` |
| TCD, Lambeth | Security check, 403 | `uk_libraries` |
| PRONI, NAI, NRS Jacobite catalogue | Bot wall, 403 or not tried | `uk_tna` |
| ÖNB, manuscripta.at, Basel, Geneva, Vaud | 403 to scripts, not tried in a browser | `swiss_austrian` |
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
| Calames | About 330 of 2,203 bodies read | `calames_biblissima` |
| JACAR | 144 undated volume hits not opened; `cands_raw.json` is git-ignored | `jacar` |
| Abhilekh Patal | "cypher" paged to 691 of 4,505 | `asia_india` |
| NARA M1194 | No search for "decipher" across all 261 rolls; only cards the bulk scan flagged were read | `nara_triage_c` |
| QDL | No Arabic or Persian terms; 23,753 hit pages not screened as images | `qdl` |
| BnF | fr. 15906, 15900, 15891 | `gallica_sweep` |
| Dudout's BnF BAM list | The 675-article JSON, available from him on request | `dudout_2026-10-29` |
| Archivportal-D | Only the first 200 "chiffriert" slots, no other terms | `central_archives` |
| HHStA | Staatenabteilungen Spanien, Rom, Venedig beyond the term searches | `central_archives` |
| Printed series | Hardwicke, Journals of the Continental Congress, Official Records, Home Office calendar after 1775 | `ia_pass2_b` |

## Swept at catalogue level, ciphers hidden

These need browsing by volume, because descriptions rarely note cipher: Riksarkivet Diplomatica, the Oxenstiernska
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
  (vHMML Turnstile), ARSI and Propaganda Fide (only the printed MHSI volumes), Turin diplomatic inventories ("Lettere
  ministri"), Czech lands, Slovakia, Russia, Belarus. About 6,000 Manus "cifre" records unscreened.
- **Blocked:** Finna (Cloudflare), BOA (login with CAPTCHA), hrcak.srce.hr, Harvard hosts (403), Abhilekh Patal (403 on the
  user's network on 4 Nov; its 18 image leads stay unvetted).
- **Not done:** Riksarkivet: six contact sheets built and not viewed, 40 volumes with no manifest. ACA reg. 3225 (1435)
  not reached.
