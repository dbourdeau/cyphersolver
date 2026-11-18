# Dutch archives, own search sites (14 Nov 2026)

Brief: sweep the archives missing from the archieven.nl OAI feed (Tresoar, Drents Archief, Stadsarchief Amsterdam, Erfgoed Leiden,
Nationaal Archief re-run, Leiden/other libraries) on their own sites for cipher words, pre-1920, at item level.
**Result: 12 rows in `candidates.json` (built by `make_candidates.py`), all scored from finding-aid text except one key page that was viewed.
Two are strong (Tresoar: Duke George of Saxony 1514, Willem Lodewijk 1589-93).** Nothing merged, no ledger touched.

## Routes that worked (go straight here next time)
| Archive | Route | Notes |
|---|---|---|
| Tresoar | `https://archieven.tresoar.nl/api/search?q=<term>&page=&limit=100` (open JSON, no key, no bot check); `/api/nodes/<id>`, `/api/toegangen/<id>`, `/api/nodes/by-trefwoord?field=twd&value=Geheimschrift`, `/api/trefwoorden?q=` | Found by loading archieven.tresoar.nl in Chrome and reading its network calls (`www.tresoar.nl/zoeken` leads to Alle Friezen, not archives). Search covers titles and notes (`__match_field`). Wildcards `*` and quoted phrases work; stems (geheimschrift matches 'geheimschrift*' and the keyword index). `harvest: tres_harvest.py`, hits `tres_hits.json`, filtered `tres_filtered.txt` |
| Stadsarchief Amsterdam | `POST https://id.archief.amsterdam/search/records?lang=nl` with `{"pagination":{"page":1,"perPage":100},"query":{"type":"AndQuery","queries":[{"type":"FieldQuery","operator":"equals","field":"data.recordType.id","value":"File"},{"type":"FullTextQuery","query":""},{"type":"FullTextQuery","query":"<term>"}]}}` | Body read from the beta site (`beta.archief.amsterdam/zoeken`). **Pass one recordType per call (File, Series, Fonds); the comma form the site puts in its URL returns 0.** IIIF at `id.archief.amsterdam/resources/iiif/3/<uuid>/full/1000,/0/default.jpg`. The old `archief.amsterdam/archieven` (Memorix widget) is dead (503). `am_search.py`, `am_harvest.py`, `am_h2.py` |
| Nationaal Archief | `zvt.nationaalarchief.nl/api/search/eads...` as in `research/nationaal_archief/harvest.py`; `na_rerun.py` (39 spelling variants) and `na_rerun2.py` (codeboek, stenografie, secrete correspondentie ...) write only hits not already in that sweep's `hits.jsonl` | 199 + 103 new hits; 192 of the first batch are VOC handwriting-text noise (stationery 'cijfer', already judged). Real new ones: `1.10.110` inv. 2 section 2.11 'Cijfers' (Battier 184-186, Rechteren 187, Buijs 183, Burmania 179) and `2.21.227` inv. 336 |

## Blocked or not reached
- **Drents Archief**: its archive search is the Mais Internet widget (`drentsarchief.nl/onderzoeken/archiefstukken?view=maisinternet`) which is the same
  engine as archieven.nl; `mizig=0` only returns inventory/collection-level cards (44 hits for cijferschrift, all newspaper or file collections), results are
  loaded by JS with no API call visible in the network log. Item search needs a per-toegang page. Not swept. Web search found only Coevorden/Maatschappij van
  Weldadigheid noise. Open Archives (openarch.nl) carries Drents person records only.
- **Erfgoed Leiden**: `erfgoedleiden.nl/collecties/archieven/archievenoverzicht/search/list/keywords/<term>` renders empty in Chrome (iframe placeholder, no
  text); no API host found (`id.`/`archieven.` subdomains do not resolve). Not swept.
- **Leiden University Libraries** (`digitalcollections.universiteitleiden.nl`): curl and Chrome time out or show an error page on the search path (home page
  returns 200); `catalog.leidenuniv.nl` does not resolve. BPL/Vossius codices not searched; WebSearch found nothing on cipher codices there.
- **Regionaal Archief Tilburg, BHIC, Erfgoed 's-Hertogenbosch, Brabant, Utrecht UB, UvA, KB/Delpher manuscripts**: not tried (JS/Memorix portals with no
  open API found; the OAI list has only 41 sets: Zeeuws, Gelders, Noord-Hollands, Eindhoven, HC Overijssel, Utrechts, Noordwest Utrecht, BHIC (1 EAD) plus those
  harvested in `sweep_2026-11-14_dutch_oai`). KB manuscripts were covered by the earlier SRU sweep (COVERAGE).
- archieven.nl `www.archieven.nl/mi/` returns 403 to curl; the search page itself loads in Chrome but gives collection-level results only.
- Staten-Generaal (1.01.02), Collectie Fagel and Aanwinsten: no new cipher-word item found with the extra spellings beyond what the Oct 2026 sweep listed;
  the Secrete kas envoy letters stay physical-only (see `research/nationaal_archief/README.md`). 1.01.19, 1.01.50, 1.02.20 'secrete correspondentie' hits are
  titles of ordinary secret registers, not ciphers.

## Rows (best first)
1. Tresoar, fonds 1 nos. 1134-1432: **Duke George of Saxony's 1514 ciphered letters to Cesar Pflug**, about 30, 9 with 'afschrift (ontcijfering)', Dresden Loc. 8183 originals, Tresoar film and regests (A)
2. Tresoar, fonds 323 no. 5592: **Willem Lodewijk's ciphered letters 1589-93 to Boner and Juckema plus the list explaining the States' cipher** (A)
3. Tresoar, fonds 7-05 no. 8: Hendrik Casimir I, 1640 letters partly in cipher, 'partly deciphered' (B)
4. Tresoar, fonds 2 inv. 588-589: Parma/Rennenberg 1579-82 letters partly in cipher, fiche of Brussels originals (B)
5. Amsterdam, 292 Hasselaer inv. 156: **digitised key 'Cyffer tot de correspondentie te houden met de Heer Pensionaris Vogelsangh'**, viewed (C, key only)
6. Tresoar, fonds 323 nos. 4036-4047: Vegilin journals 1707-16 partly in Greek-letter script (C, probably a transliteration)
7. Tresoar, fonds 2 inv. 646/2-646/6 'Formulaires et chiffres' (C, date misprinted 1199-1221)
8-11. NA 1.10.110 inv. 2 section 2.11: envoy key books Battier (184-186), Van Rechteren (187), Buijs (183), Van Burmania (179); years are placeholders (C)
12. NA 2.21.227 no. 336: Van Toulon 'Sleutels voor geheimschriften' (C)

## Dropped as duplicates or not rows
- Tresoar 7-03 inv. 203 (Deventer 1629, 'grotendeels in geheimschrift') = KHA A23-203, catalogue already; 7-03 inv. 352, 7-03 inv. 223, 7-06 inv. 347, 7-02 inv. 51/191/195/198, fonds 326 inv. 925 (Maurits to Starckenborgh) are catalogue or leads 1949-1956; 7-03 inv. 311 = KHA A23-311, target casimir1618.
- Tresoar fonds 323 no. 5535 (1726 'Tabel met cijfers, bedoeld voor een geheimschrift'), fonds 319 no. 2419 ('tafel voor geheim schrift', undated): single key tables, no ciphertext; not made rows (candidates if wanted).
- Amsterdam: Olie 1538 inv. 143 (1845 school exercise with a 'sleutel voor geheimschrift'), Deutz 234 inv. 269 and Doopsgezinde 565.A inv. 2005 ('ontcijferen' = reading old hands), 'Obligaties met geheime tekens' (316 inv. 79, security marks), Volkszang 1911 'cijferschrift' (music numerals), Marlof 'Chiffres' (coach-painter model book). 'cijfer*' there is statistics and diary noise.
- Tresoar 'cijfer*', 'gecijferd', 'cijffer*' hits are mostly noise (dates in numerals, accounts); the Saxon regests and 'geheimschrift' notes carry the signal.
- 1.10.110 'Boreel' etc. and the NA 1.01.02 volumes: already in the Oct 2026 NA sweep.

## Caveats
- All scoring is from finding-aid text. The only images viewed are the two Vogelesangh scans. The Saxon rows rest on Tresoar's regests (it lists 'expeditie' and 'afschrift (ontcijfering)' per letter); whether the decipherments are complete or only partial is not checked, nor whether the Dresden originals are online.
- Identification of the Pensionary Vogelesangh and the key's date are not verified (Pieter Vogelesangh, 1616-63, is the section heading in the Hasselaer finding aid).
- Item-level cipher words in Tresoar are searched through its title and note fields; the API's `total` is exact, but deeper unindexed text (volume-level descriptions inside long inventories) may hold more.
- Dedupe: `known.py` and shelfmark greps against catalogue.json, leads.json, targets and sweeps; no DECODE, Tomokiyo or Lasry search made for any row except one German WebSearch on the Saxon letters.
- Browser: Chrome tab used for site probing, closed. Cookie banner on beta.archief.amsterdam answered with 'only necessary cookies'. No CAPTCHA met.
