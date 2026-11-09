# Undeciphered-phrase sweep (9 Nov 2026)

New query axis: search cataloguers' own notes that a cipher is NOT deciphered ("undeciphered", "feloldas nelkul", "nierozszyfrowany",
"unentziffert" ...), not cipher words. Result: **7 rows** in `candidates.json` (`make_candidates.py`), all cls B, `seen: catalogue`.
Six are Hungaricana regests of HHStA Ungarische Akten 1529-1530 (Ferdinand I's war with Zapolya), one is TNA SP 35/4/47 (Keill, 1715).
Everything else the axis reached was already in the repo.

## Routes
| Source | Route | Result |
|---|---|---|
| Hungaricana Levéltári iratgyűjtemények | Chrome same-origin `fetch('/hu/lear/search/results/?query=...')`; `NOT` operator works (`sifrír* NOT Türkei` 103 hits vs 2,633); paging via base64 `list={"query":...}&page=n`; result rows = `div.d-flex` holding `table.table-sm`. Long loops time out the tool: run them as background async and poll `window.OUT`. | megfejtetlen 0, sifrózott 0, feloldatlan 0, kulcs nélkül 2, nem fejtették meg 1, sifrírt 5, sifrírozott 96 (all but 7 Türkei I, already swept), `sifrír* NOT Türkei` 103 (65 without any decipherment word; 21 after removing Nádasdy Fasc. 309/310/313/314/327, already covered). New: AA Fasc. 13, 10, 16, Misc. 431 (rows). |
| TNA Discovery API (`research/tna_discovery/tna.py`) | curl, 2.5 s | undeciphered 54, "not deciphered" 143, "undecoded" 51, "not decoded" 54, "undecyphered" 2, "without key" 4. All the real hits already in catalogue/leads (SP 106/10, SP 84/165, SP 36/66, SP 91/6, SP 35/46, PRO 30/11/6, D(W)1778, SP 87/13, SP 95/136); Surrey History Centre G52/G85 Nicholas letters are deciphered by Nicholas. New: SP 35/4/47 (row). |
| DDB Solr (Archivportal-D) `ddb.py`, `ddb2.py` | public endpoint, 1.5 s | 22 negation phrases AND cipher words. Real hits: Lucchesini Nachlass V 061 (Stein reports; V 061, 209 "chiffrierten Passagen nicht dechiffriert") and BayHStA MA 16 (1813 cipher tables "nicht aufgelöst"): both already known. Rest noise (Schlüssel = lock key). |
| ARON (MZA, SOA Plzeň, Zámrsk, Praha, portal.nacr) `aron_run.py` | POST listview | nerozluštěno 1, bez rozluštění 2, nerozluštitelný 1 (all inscriptions or deeds, noise); nerozluštěný*, nedešifrovaný*, nedešifrováno, nerozlúštené 0. "bez klíče" matches keys/locks. Zero rows. |
| PARES `pares/` (run.py, 4 s) | curl, no 429 | The full-text search ignores quotes: "sin descifrar" returned 24 rows, all already in leads/catalogue (AHNOB Santa Cruz C.50-51 Felipe IV, ESTADO 20/B, ESTADO 3130, DIVERSOS-COLECCIONES 142, Cuba 1747718); "no descifrada"/"sin la clave"/"sin clave" returned 488/1437/1437 noise rows (word-bag matches). The run was left to finish its term list; hits file removed. Zero rows. |
| szukajwarchiwach (Chrome) | Liferay form POST from the home page (`document.forms[0]`, field `*_keywords`); result rows `.search-result`; page size options 20-200. Scans are viewable in Chrome only (photos host answers curl with an Imperva stub). | "nierozszyfrowany" 34 rows. **Trap: AGAD uses "nierozszyfrowany" for unidentified senders.** AGAD 1/335/0/-/279a 480a (Ignacy Potocki 1782, "nierozszyfrowane lub nierozszyfrowane częściowo", 3 scans) viewed: plain Polish letters, no cipher; 1/352/0/4/D444 (Przezdziecki) = unidentified senders. Already known: 1/338/0/1/131 (Betański), 1/346/0/-/1066, 1/358/0/-/363. Other terms (bez odczytania, szyfr nieodczytany) not run. |
| FranceArchives (`fa.py`) | curl + cookie jar | phrase quotes ignored; "non déchiffré" = 15 hits (Aix archbishopric Latin letters, 1870s, noise); others 0. |
| Manus Online API `manus.py`, `manusd.py` | POST | quotes break the API; indecifrato 1 (Osimo, Molin's invented alphabet, not a letter), indecifrata 1 (a seal), indecifrabile 54 (handwriting). Zero rows. |
| Archives Hub | Cloudflare check for curl; not opened in Chrome | not run. The 2 Nov sweep already took cipher/cypher (about 490 hits), which contain any "undeciphered" item. |

## Excluded
Türkei I (all swept), Nádasdy Fasc. 309/310/313 (deciphered separately or in catalogue), Fasc. 311 B, 314, 327 (earlier sweeps), AA Fasc. 15 D fol. 56, Fasc. 16 C fol. 9, Fasc. 18 B/E, Fasc. 6 A (deciphered "feloldással/sorközben"), AA Fasc. 10 C 28-30 (interlinear), Hoffinanz Ungarn 1654 (6-line cipher beside a seal, no letter).

## Not done
Czech/Slovak "bez klíče" noise only; Polish `szyfr nieodczytany`, `bez odczytania`; Hungaricana `sifrír*` with Türkei I excluded only (Türkei I was covered by the Türkei sweeps, not re-read); HHStA AIS item views and Archives Hub not opened; no Calendar/edition check beyond two web searches per group.
