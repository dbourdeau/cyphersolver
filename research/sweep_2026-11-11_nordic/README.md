# Nordic sweep from the cloud network (11 Nov 2026)

Brief: `research/_nov11/BRIEF.md`. Sources that were blocked on the earlier network: Alvin, Finna, the Danish Royal
Library and Rigsarkivet scans, Norway, Iceland.

**Result: 7 rows in `candidates.json`, 4 with a complete `open` vetting block; 9 key leads in `key_leads.json`.**
Rows are built by `build_candidates.py` (+ `rows_extra.json`, `keys_extra.json`). All rows passed `known.py`; DECODE was
searched live at `de-crypt.org/decrypt-web/RecordsList?search=<term>` (the dump is not in this checkout).

## Rows

| Row | Shelfmark | Seen | Block |
|---|---|---|---|
| "Kloge Søren's" Cyprianus, 1858: a cunning man's book of cures, about 85 pages in a sign cipher under clear Danish headings | KB Copenhagen, Dansk Folkemindesamling, DFS 1997/020 | scan, 13 openings | open |
| Ruggieri and Rossetto (Este envoys, Rome) to Ercole II, 17 Feb 1543: 14 lines of cipher | Uppsala UB, Waller Ms it-01133 | scan, all 3 images | open |
| Johan Peter Carlsson, diary 1863-64 and 1869-73, "mainly written in cipher", 1,686 pages | Linköpings stadsbibliotek, B 168 | not online | open |
| Anonymous German prayer book, 18th c., "partly in cipher writing" | KB Copenhagen, Acc. 1990/229 | not online | open |
| Christoffer Sehested, Vienna, to Frederik III and the chancellor, Jan-May 1657: about 40 pages wholly in cipher | Rigsarkivet, TKUA, Kejseren, Gesandtskabsrelationer 1630-58 | scan | none: Gigas deciphered the letters for Fridericia (1894, note 62); slips with part of it lie in the volume. Class A lead |
| Topelius, "Chifferskrift 1832" | National Library of Finland, Coll. 244.182 | not online | none: title only, SLS edition not checked |
| Gendarmerie letter "containing the gendarmerie's cipher", 1913-18 | Kansallisarkisto, Santarmihallinto 2906 | not online | none: may be a key |

## Routes from this network

| Source | Route | Terms and counts | Outcome |
|---|---|---|---|
| **Alvin** | HTML search and record pages still show Anubis to curl (not circumvented). **The OAI-PMH feed is open**: `https://www.alvin-portal.org/oai/oai?verb=ListRecords&metadataPrefix=oai_dc`. The resumption token is `<stamp>/alvin/oai_dc/<cursor>/<size>/set/from/until/`; size 1000 is accepted, but the server then advances its own cursor by only 100, so `alvin_oai.py` sets the cursor itself. `GetRecord` with `metadataPrefix=ksamsok-rdf` gives the full description, shelfmark and the attachment URLs; `/alvin/attachment/download/alvin-record:<id>/ATTACHMENT-000N` (TIFF) and `/attachment/record/...` (small JPEG) answer curl | **All 692,145 records** harvested in about 55 minutes and matched against chiff, ziffer, cipher, cypher, cifr, lönnskrift, hemlig skrift, kryptogra, krypter, dechiff, geheimschrift, chifr, cryptogr, steganogr, siffror, sifferskrift: 174 raw hits, 35 after dropping Schiff/chiffonjé/namnchiffer/tokens | 2 rows (Carlsson diary, Rossetto letter), 4 key leads. Everything else was known from the October browser searches (Gustav III F 414/415, the green portfolio) or is not a ciphertext |
| **Finna** | `https://api.finna.fi/v1/search` answers curl (no Cloudflare here). `finna.py`: 40 terms x formats Document/Manuscript/Letter/OtherText/Other, year <= 1950; a second pass without the date filter | salakirjoitus is stemmed loosely (2,923 archive units, almost all "salainen" = secret); with a cipher word in title or summary: 22 units, all 1906-1948 (police, gendarmerie, military, legations) except Topelius 1832. chiffer 37, chiffre 548, cipher 1,444, cifra 303 are printed books | 2 leads, 1 key lead. Finland has no pre-1900 enciphered letter described as such in Finna. The 1918 Lindahl "secret letters" (Espoo museum) are invisible ink, transcribed 2020: left out |
| **Rigsarkivet scans (Arkivalieronline)** | All by curl, see `ao.py`: Daisy series page gives `epid`; `api.rigsarkivet.dk/ao/v1/billedviser/indeks-top?epid=`, `billed-reference-lister?bsid=`, `ao/v1/images/<id>` (full-size JPEG, about 1 MB, 1-2 s). The search API takes `"accessibility": ["online"]` and `"arkivskaber"` (`ra_online.py`): **578 TKUA series are scanned**, among them the envoy reports (Gesandtskabsrelationer) for the Emperor, Brandenburg-Prussia (1693-1765 complete), the Netherlands, France, Poland, England, Spain, Saxony, Sweden, Danzig, Hamburg | 57 series enumerated (236 units, about 119,000 images). Contact sheets (12 a sheet, every 25th-40th image) for 15 units, about 450 images; single leaves at full size where cipher showed | Cipher is everywhere in these volumes, **but it is deciphered**: between the lines from the 1660s on (Sehested, Paris 1662-65; Berlin 1711-13; Paris 1744 and 1748; Danzig; even the "Duplikata" series for Berlin and Poland 1704-68), on a separate lettered sheet earlier (resident in Stockholm, March 1636, Sverige B.84 images 121-133), or in the margin (symbol cipher of 1622, same unit image 576). The one large body without decipherment on the leaves is Sehested's Vienna relations of 1657 (row 5) |
| **KB Copenhagen** | Primo JSON as in `sweep_2026-11_denmark_sweden_more` (`kbdk.py`, scope MyInstitution); digitised items at `digitalesamlinger.kb.dk` with IIIF on `kb-images.kb.dk` | 25 more terms: chifferskrift 2, cifferskrift 4, lønskrift 7, "i chiffer" 13, chiffernøgle 2, ciffre 32, cifre 65, ziffern 310, kryptogram 8, Geheimschrift 8, hemmelig skrift 32 ... (manuscript records only were read) | 2 rows (Cyprianus, prayer book), 4 key leads (NKS 1416 4to, NKS 2003 g 4to, Thott 2186 4to, Thott 844 4to) |
| **nb.no** | `api.nb.no/catalog/v1/items?q=&filter=mediatype:<brev|privatarkivmateriale|manuskripter>` | 11 terms x 3 media types: all 0 except privatarkivmateriale chiffre 3, kode 3 (none a cipher) | nothing. The 5,046 "chiffer" hits are newspapers and books |
| **handrit.is** | `handrit.is/search?q=` | - | 403 with an "Öryggisathugun" captcha page. **Blocked, not swept** |
| Digitalarkivet / Arkivportalen | home page answers; Arkivportalen was swept on 2 Nov | - | not repeated |

## Excluded, with the reason

- TKUA envoy reports with interlinear or attached decipherments (above): read at the time. They are class A reference
  material: thousands of pages of French and German number-cipher with the plaintext over it, online and free.
- Sehested 1657 has no block because Fridericia thanks E. Gigas for "en Dechifrering af Sehesteds Breve". The slips in
  the volume (images 124, 125, 137, 138) give the letter to the chancellor of 7/17 Feb 1657 with the nomenclator signs
  unresolved; the long letters to the king (images 116-119, 126-136, 139-170) have no plaintext beside them that I saw.
- Alvin 492335 (Uppsala F 415, "Hertigens Apostille ... chifrerad"): Gustav III's clear copy, transcribed in the record.
- Alvin: Forsskål's and Linnaeus's letters that only mention a cipher; Mandelgren's notes on rune alphabets; the 1697
  dissertation on secret writing; D 1601 a (treatise, key lead).
- Finna: all 20th-century police and military cipher files (keys, courses, decrypts).

## What remains

- **Rigsarkivet scans**: only 15 of the 236 scanned envoy-report units were sheeted, each at 1 image in 25-40. The
  envoys' own archives (gesandtskabsarkiver: Peder Vibe 1635-43, Peder Juel, Charisius, Jens Juel 1679-80), where
  incoming orders in cipher may lack a decipherment, were enumerated (`ao.py epid`) but not viewed. Other creators
  (Danske Kancelli, Sønderjyske Fyrstearkiver, private archives) were not listed with `ra_online.py`.
- **Sehested 1657**: match slips to letters, then it is a ready cipher-and-crib target; test KB NKS 1416 4to and the
  Rigsarkivet "Christoffer Sehested keys 1650-70".
- **Alvin**: descriptions only; a letter whose record does not say cipher cannot be found this way. The Waller
  Italian collection (Uppsala) has thousands of digitised 16th-century letters and would repay paging.
- **KB Copenhagen**: NKS/GKS/Thott letter volumes are not described at item level.
- handrit.is (captcha), Topelius edition, Linköping and KB scan orders.
