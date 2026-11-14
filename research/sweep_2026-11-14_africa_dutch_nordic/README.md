# Dutch and Danish/Swedish/Brandenburg colonial Africa sweep (14 Nov 2026)

Run by a cloud sweep agent (Claude Sonnet 5.5) for the African sweeps of 14 Nov 2026, following `research/SWEEP.md` and
`research/archive_sweep_2026-10/BRIEF.md`. No Claude-in-Chrome tools in the session.

**Result: 0 candidate rows (`candidates.json` is `[]`), 5 key leads (`key_leads.json`).** Nothing unread with ciphertext in
view was found for Dutch, Danish, Swedish or Brandenburg Africa. The sweep is a documented negative: every term below
was run, the Elmina/WIC/Guinea inventories were read whole, and four scanned volumes were paged. What this means is that
the **catalogue words do not reach African ciphers** (Dutch African papers are not described with cipher words), not that
there are none.

## Routes that worked

| Host | Route | Notes |
|---|---|---|
| Nationaal Archief | `zvt.nationaalarchief.nl/api/search/eads?q=` (archive level), `.../search/eads/<ead>?q=` (item level), `.../api/eads/<ead>/clevels?page=N` (full listing), `.../clevels/<inv>` (scan list with IIIF) | Answers curl, one request per 2.5 s, no block. Listing pages skip part of the tree (1.05.01.01: 628 of 3,890 items seen), so term search and listing grep are complementary. |
| Nationaal Archief IIIF | `service.archief.nl/iip/iipsrv?IIIF=<path>.jp2/full/<w>,/0/default.jpg` | Works for thumbnails and half-size pages (`scans.py`, `sheet.py`). |
| archive.org | `advancedsearch.php`, `download/<id>/<id>_djvu.txt`, full-text `services/search/beta/page_production` | The full-text endpoint ORs the words: two-word queries (cipher + place) give page hits where the words are far apart, so it cannot test co-occurrence. Used for Castries only. |
| DDB (Archivportal-D) Solr | `api.deutsche-digitale-bibliothek.de/2/search/index/search/select?q=` | Boolean queries work (`ddb.py`). |
| Riksarkivet (Sweden) | `data.riksarkivet.se/api/records?text=` with `User-Agent: curl/8.0` | `rasw.py`. |
| DECODE | `research/sweep_2026-11-11_german/decode_search.py` | Africa terms below. |

## Blocked or unreachable

- **Rigsarkivet Collections Search `cs.rigsarkivet.dk`** (the only item-level route to the Danish Gold Coast / Guinea records, found through a web search): connection reset by peer on every try (curl error 35), WebFetch got HTTP 503. Arkivalieronline (`arkivalieronline.rigsarkivet.dk/en/other/other-collection/101`, "The Gold Coast (West Indies)") answers but lists only series names (Guinean copybook 1816-93, drafts 1816-74, journal 1776-1893, journal files 1794-1893); it has no text search. The Danish Gold Coast is therefore **not swept**: not blocked by a bot check, no route.
- **Basel Mission archive**: `baslerafrika.ch` redirects to a JS shell; `www.bmarchives.org` (Omeka) answers 200 but its `items/browse?search=` returns an empty list for every term tried, including "letter" and "Akropong", so the search does not work from a script. Terms tried: cipher, cypher, chiffre, Chiffre, Geheimschrift, Ziffernschrift, code, Geheimsprache. Not swept.
- **Brandenburg (GStA PK Berlin, Brandenburgisch-Afrikanische Compagnie)**: no item-level route; DDB carries only a few GStA records (below).
- Het Zeeuws Archief item search (Memorix key route declined in an earlier sweep), Delpher: not tried.

## Terms and hit counts

**Nationaal Archief, archive level** (number of inventories with a hit, `na_arch_*.json`): cijfer 147, cijfers 415, cijferschrift 35, ontcijferd 13, ontcijfering 7, geheimschrift 29, chiffre 1, gecijferd 0, cijferbrief 0. Of these 541 inventories, those relating to Africa carry no cipher word: the Africa-related inventories were identified by 24 title searches (Guinea, Elmina, Marokko, Algiers, Tunis, Tripoli, Kaap de Goede Hoop, Zuid-Afrika, Goudkust, Barbarije, Levantsche Handel, Slavenhandel, Senegal, Angola, Congo, Egypte, Abessinie, Oranje Vrijstaat, Transvaal, Mauritius, St. Helena, Leyds, Livingstone, Mozambique, Madagaskar, Ethiopie ...; `na_africa_archives.json`).

**Nationaal Archief, item level** (`na_run.py`, `na_run2.py`; 19 terms each: cijfer, cijfers, cijferschrift, chiffre, chiffres, gecijferd, ontcijferd, ontcijfering, geheimschrift, cijfferschrift, cijffer, sleutel, cifra, cijferbrief, chiffre with accent, dechiffrement, gechiffreerd, cypher, cipher; run 2 also cijfertelegram(men)). Run 1 covered 42 inventories, run 2 19 (798 + 361 calls):

- Run 1, total item hits per term: cijfer 7, cijferschrift 1, ontcijfering 1, geheimschrift 6, sleutel 8; all other terms 0. Inventories searched: 1.05.14 (Nederlandse Bezittingen ter Kuste van Guinea, Elmina), 1.05.01.01 (Oude WIC), 1.05.01.02 (WIC 2), 1.05.03 (Sociëteit van Suriname), 1.05.06, 1.05.13.01, 1.05.11.11, 1.11.06.14, 1.11.06.18, 2.01.28.01-.03, 1.02.19 (Marokko), 1.02.21.01-.02 (Tunis), 1.02.00, 1.03.01 (Levantse Handel), 2.05.15.15/.17/.05, 2.05.22 (Tanger), 2.05.14.11 (Elmina consulate 1872-80), 2.05.30, 1.10.62 (Nijssen, Tunis), 1.10.72 (De Ruyter), 1.01.46, 1.01.47.15-.16 (Admiralty), 2.19.190 (Kinsbergen), 2.21.479 (Swellengrebel), 1.10.69, 1.10.30, 1.10.56, 1.10.59 (Nederburgh), 2.10.01, 2.10.03, 2.01.27.02, 2.01.27.05, 1.02.20, 1.02.22, 1.02.16, 1.02.18.
- Run 2: 2.21.105 (Leyds), 2.05.121, .70, .128, .123, .124, .125, .119, .122, .12, 2.18.18.02 (NZASM), 2.21.167, .174, .011, 2.05.14.12, 2.05.15.06, 2.05.30, 1.10.07 and 1.04.02 (VOC). Nothing outside the VOC. VOC: cijffer 253 volumes, cijfer 29, cijfers 1, sleutel 564, all from handwriting-recognition text; the hits are stationery lists ("pennemessen ... cijffer leijen") and "a nul in the cijffer" (arithmetic), as the Oct sweep found. The few real mentions are Asian volumes (inv. 8922 f. 169, a letter in cipher in a hearing, Ceylon/Malabar 1707; 8772 f. 389, a letter "in Cijffer" from Alexander Hume to a French captain, 1733; 7603 f. 116, "a period in Cijffer", 1783-84; 9452 f. 247, two different ciphers, 1755-57). **None is African; not opened as rows** (outside this area; noted for a VOC sweep). No VOC Kaap volume matched.
- Targeted after the archive-level hits: 2.21.046 Daendels (geheimschrift 1: inv. 137), 2.21.008.69 Hogendorp (geheimschrift 1, cijferschrift 1, cijfers 2).

What the item-level hits were (all keys, office papers or Brazil, none an African ciphertext):

| Item | What | Status |
|---|---|---|
| 1.05.01.01 inv. 44, 167, 168 | Pina's key (1646), Telles da Silva codes with key (1649), Dutch Brazil | Published (HistoCrypt 2023, articles 693 and 392); closed by the first pass |
| 1.02.20 inv. 17, 164, 628, 686, 785; 1.02.22 inv. 112; 1.02.18 inv. 75 | keys of Turkey legation, Smyrna consulate, Portugal legation | keys, not Africa; in `sweep_2026-11_ottoman_turkish` |
| 1.10.59 inv. 1578; 2.01.27.02 inv. 317, 209; 2.01.27.05 inv. 12; 2.21.046 inv. 137; 2.21.008.69 inv. 38 | keys / office papers | `key_leads.json`; all already in `research/nationaal_archief/enriched.json` |

**Inventories read whole** (EAD listing dumped, wide regex cijf/chif/ciph/cyph/cifra/geheim/secre/sleutel/code/teken/signa; `dumps/*.gz`, `grep_dumps.py`): 1.05.14 Elmina (1,272 unique items, 1,145 scanned), 1.05.01.02 (1,881), 1.05.01.01 (628 of 3,890: the listing is partial), 1.05.06 (546), 1.05.03 Sociëteit van Suriname (601), 1.03.01 (384), 1.02.21.01 (57), 1.02.21.02 (7), 2.01.28.01 (420), 2.05.22 (110). No cipher word in any title or note. Items about "secrete" papers on Guinea: 1.05.14 inv. 77 (register of secret letters to the WIC directors), 1.05.01.02 inv. 907A (liasse of secret letters from the Guinea coast, Curaçao, St. Eustatius, Spain), 1.05.06 inv. 893/894 (secret cupboard of the Zeeland chamber; physical), 2.01.28.01 inv. 31-41 (secret minutes of the Guinea committee 1791-1805). 1.02.19 (Marokko) was dumped whole by the Ottoman sweep: keys only.

**Leaves looked at** (thumbnails, contact sheets; scratch only):
- 1.05.14 inv. 77 (Elmina, secret letters to the WIC directors 1771-73): all 20 scans; clear Dutch, no cipher.
- 1.05.01.02 inv. 907A ("Liasse van secrete brieven" no. 3): all 241 scans at about 420 px a scan; clear Dutch letters, signed, sealed covers; no cipher run seen. A short cipher group inside a clear page could be missed at this size.
- 1.05.03 inv. 219 (Sociëteit van Suriname, letters from Suriname 22 Oct 1688 - 21 Jun 1689, 575 scans): scans 1-240 as contact sheets, plus scans 333-337 at 1,400 px. **Scan 335 (f. 315r) is a full page of number-and-symbol cipher** (about 20 lines, no interlinear decipherment on the page) facing a clear Dutch inventory of goods and enslaved people in Suriname, signed 21 April 1689 (the name Cipriani appears). It is **DECODE R7841, marked "Decrypted"**, so not a lead. Siblings: DECODE R8049 holds the "Old and New Key 1739" of the same Society. Scans 66-69 and 209-225 hold lists with brand marks and initials of enslaved people (signs in the margin), which are not cipher. Scans 241-575 and the other 190 letter volumes of this series (inv. 212-403) are **not paged**: the catalogue describes none of them with a cipher word, but this item shows one hides there. Suriname is outside Africa; noted as the best catch-all next job for the slave-trade/colonial correspondence.

**archive.org (printed editions).**
- H. de Castries, *Les sources inédites de l'histoire du Maroc*, 1re série, Pays-Bas and the other series (16 volumes, OCR grepped for chiffr/cijfer): the Dutch material is printed as text; where a cipher occurs the editor gives the text. One find, recorded in `key_leads.json`: Pieter Maertensz. Coy's cipher alphabet of 18 March 1606 (key printed in the edition), and the editor's remark that Coy's ciphered correspondence is no longer in the Rijksarchief. Series from Spanish and French archives hold dozens of "original en partie chiffré, avec déchiffrement officiel" items: glossed, printed, not leads.
- 14 full-text queries (`ia_fts.py`, `ia_hits.jsonl`): "in cijfer" Elmina (7 total), cijferschrift Guinea (262), "in cijffer" Guinea (12), "in cijfer" Kaap (145), "in cijfer" Marokko (53), "in cijfers" Tunis (796), ciphers Elmina (2,430), "in cipher" "Gold Coast" Dutch (7,381), "in cypher" Elmina (200), "in cypher" "Cabo Corso" (57), "in Ziffern" Friedrichsburg (232), Chiffern Groß-Friedrichsburg (32), chiffer Guinea Kompagni (87), "i chiffer" Christiansborg (14). The endpoint ORs the words; the page snippets showed no co-occurring cipher and African place; nothing kept.

**Other hosts.**
- DDB/Archivportal-D, 4 boolean queries (Afrika/Guinea/Friedrichsburg/Goldküste/Arguin AND chiffriert/Chiffre/Chiffren/Geheimschrift/"in Ziffern": 11 hits, all noise; "Afrikanische Compagnie" AND cipher words: 0; Kamerun AND chiffriert/Geheimschrift: 0; "Afrikanische Compagnie" 14, Friedrichsburg Guinea 4, Brandenburgisch-Afrikanische 3, Goldküste Brandenburg 10, all museum objects, a printed source collection and finding-aid titles, no cipher).
- Riksarkivet (Sweden): "Afrikanska kompaniet" 16 records (agent, series, fonds, volumes: finance and shipping), Cabo Corso 1, Carolusborg 0, "Guinea chiffer" 0, "Afrika chiffer" 0, "Cabo Corso chiffrerad" 0. The Swedish Africa Company left no cipher record under these words. The earlier `riksarkivet` sweep ran chiffer* generally.
- DECODE (`decode_search.py`): Marokko/Morocco 0, Elmina 2 (both false: Wolff to Wilhelmina), Guinea 0, Kaap 0, Gold Coast 0, Algiers 1 (TNA SP 106/7, English), Tunis 0, Tripoli 1 (Vienna key), Egypt 0, Tangier 0, Africa 3 (BL IOR/E/4/861, East India Company), Suriname 2 (R7841 above, R8049), Guldkysten 0, Brandenburg 0, Basel Mission 0, Ethiopia 0, Abyssinia 0, Congo 0, Cape 3 (Venice, Kew; false), Nederburgh 0, Coy 1 (false).
- Web searches (Elmina cipher; Danish Gold Coast chiffer; Coy cipher; Cryptiana Dutch Africa): nothing new. Tomokiyo's `unsolved.htm` snapshot has one African item, the British consulate telegram of 1911 (not in this area).

## Finds, ranked

No candidate rows. Key leads (`key_leads.json`), best first:
1. Coy 1606 cipher alphabet (printed key; ciphertext lost or unlocated) - useful only if a Coy letter turns up in Staten-Generaal Marokko.
2. NA 1.10.59 inv. 1578, Van de Spiegel key (physical).
3. NA 2.01.27.02 inv. 317 / 209, Elout and Van Grasveld cipher; secret missive with ciphered rendering for Batavia, 1801 (physical; Asia).
4. NA 2.21.046 inv. 137, Daendels notes on secret writing (physical).
5. NA 2.21.008.69 inv. 38, Hogendorp keys (physical).

## Excluded

Telles da Silva and Pina (Brazil, published); Suriname R7841 and its page (DECODE decrypted); the VOC "cijffer" hits (stationery and arithmetic; the Asian real mentions are outside the area); Castries items with an official decipherment printed; the "secrete" registers of WIC, Guinea committee and the Society (clear text); the African consular series 1.02.19 and 1.02.21.01-.02 (e.g. inv. 28 of 1.02.21.01, letters of consuls in the Barbary States 1759-1813: physical only, no cipher word in any title).

## What is left

1. **Danish Gold Coast** (Rigsarkivet): retry `cs.rigsarkivet.dk` from another network or in Chrome; the Guinean copybooks, journals and drafts on Arkivalieronline are scans without text.
2. **Basel Mission** (`bmarchives.org`): the search needs a browser.
3. **Elmina inventory (1.05.14), 1,145 scanned volumes** and the **WIC 2 Guinea letters** (1.05.01.02, 1,670 scanned volumes): only the "secrete" ones were paged. A leaf-by-leaf survey of the incoming letters from the directors (inv. 24-56) and the governor's outgoing series is the only way to find a cipher the catalogue does not name; start with the 1780s-1810s volumes, the period of Daendels and of the Guinea committee.
4. **Sociëteit van Suriname letters** (1.05.03 inv. 212-403): after R7841, page the remaining volumes (DECODE R8049's 1739 key is the key for the late ones).
5. **Staten-Generaal Marokko lias** (1.01.02; Coy's ciphered letters): item level not reachable; see `research/nationaal_archief` (Secrete kas envoy volumes are physical only).
6. Brandenburg-African Company (GStA PK), Swedish Africa Company items (SE/RA/757/16, SE/RA/1135/IX/9/799 not opened), Zeeuws Archief MCC/WIC items, VOC Kaap volumes through the HTR text with more terms, Delpher.

## Scripts

`na.py` (API helpers, archive-level search), `na_items.py`, `na_run.py`, `na_run2.py` (item-level term runs), `dump_ead.py` (listing dump, 2.5 s a page), `grep_dumps.py` (wide regex over `dumps/*.gz`), `scans.py` (IIIF thumbnails of one item), `sheet.py` (contact sheets), `ia_fts.py`, `ddb.py`, `rasw.py`. Result files: `na_arch_*.json`, `na_items_*.json`, `na_run*.log`, `ia_hits.jsonl`, `na_africa_archives.json`. Images are in the session scratch directory only.
