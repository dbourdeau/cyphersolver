# Dutch regional archives through archieven.nl: OAI-PMH feed and site search (11 Nov 2026, cloud session)

Brief: `research/_nov11/BRIEF.md`. Continues `research/sweep_2026-11_siblings_nov9` (OAI harvest left unfinished) and
`research/sweep_2026-11_netherlands_regional` (routes blocked from the desktop).

**Result: 8 candidate rows (`candidates.json`), 5 with a complete `open` vetting block, 3 of them with the cipher seen on the
scans; 8 key-only items (`key_leads.json`).** Both files are built by `make_candidates.py`.

| Row | Shelfmark | Seen | Block |
|---|---|---|---|
| Van Malen to his brother, 1615-1619, symbol cipher, French and Dutch | Gelders Archief 0372 Huis Ammerzoden inv. 52 | all 8 scans | open |
| Johan van Ewsum, cipher notes with their own key alphabet, 1533-1557 | Groninger Archieven 696 inv. 595 | scan 1 (+40 sampled) | open |
| Goslinga to Reinhard van Reede, number code, 1730 | Gelders Archief 0613 Bentinck inv. 3889 | all 79 scans | open (one letter has a contemporary decipherment slip) |
| Marteville, Stockholm 1752, 2 letters | Gelders Archief 0525 Rosendael inv. 577 | not online | open |
| Van Meeteren to the Dordrecht Patriots, 14 Oct 1783 | RA Dordrecht 325 inv. 44 | not online | open |
| Arent van Wassenaer with Helvetius, Mesnager, Portland, 1707-1711 | Gelders Archief 0525 Rosendael inv. 1240 | not online | none (bundle; Heinsius edition not opened) |
| Duke George of Saxony to Cesar Pflug, 29 cipher letters of 1514 | HStA Dresden Loc. 8183 / Tresoar toegang 1 (microfilm) | not online | none (inventory maker summarises most letters) |
| Waldeck's register 1654-55, cipher letters with the Elector | Gelders Archief 0370 Culemborg inv. 1257 | 60 of 856 scans, cipher not located | none |

## Routes from this network

| Route | Result |
|---|---|
| `harvest.archieven.nl/OAI/OAIHandler` (OAI-PMH, `oai_ead`) | Works with plain GET, no key, no bot check. `ListIdentifiers` gives 50 ids in about 6 s; `GetRecord` one EAD in 1-5 s. `oai_get.py` lists a set's ids once (cached in `*.ids.<set>.txt`), then fetches records with 2-3 workers: about 2,000 EADs in 15 minutes, against 3 records per 10 s for the `ListRecords` paging of the 9 Nov script. Two proxy errors in the whole run, retried. |
| `www.archieven.nl/nl/zoeken?...&mizk_alle=<term>` (the site's own search) | **New route.** JavaScript only, but headless Chromium (Playwright) reads it; no challenge page met. It searches *all* participating archives, including the ones with (almost) nothing in the open-data sets: Tresoar, Gelders Archief, Drents Archief, BHIC, HC Limburg, NIOD. `anl.js`: table view of the inventories that hold a term (`miview=tbl&mif3=4`, 15 a page), then each inventory with the term (`miview=inv2&micode=<toegang>`), click `button.mi_btn_toggle` ("Bekijk gevonden archiefstukken") and read the highlighted item descriptions. The search is whole-word (gecijferd, cijferbrief, chiffré: 0). |
| Scans in the archieven.nl viewer | Work in headless Chromium (`anl_view.js`: open the found item, click the first thumbnail, type the page number into the viewer frame, screenshot; about 5 s a page). The IIIF manifest `proxy.archieven.nl/iiif/<adt>/<guid>` answers curl, but its image URLs answer "Geen rechten"; `proxy.archieven.nl/thumb/<adt>/<guid>` gives 201x300 thumbnails only. |
| `www.geldersarchief.nl` | 502 from this network (also for `proxy.archieven.nl/37/<guid>`, which redirects there). The same inventories and scans open through www.archieven.nl. |
| `de-crypt.org/decrypt-web/RecordsList?cmd=search&search=` | Answers curl (`decode_q.py`); used for every row. |
| `cryptiana.web.fc2.com` | Answers curl; `code/GL.htm` and `code/crypto.htm` fetched and grepped. |
| `zvt.nationaalarchief.nl/api/search` | Answers. The search is fuzzy (cijffer also matches "Cliffort"). |

A container restart killed the background jobs once; all of them resume from their progress files.

## OAI harvest: what was read

`oai_get.py out.jsonl SET[:skip] ...` writes every EAD component whose title, scope note or odd matches the cipher regex (wider than on
9 Nov: also cijfertelegram, geheim schrift, geheime code/taal/teken, code-, codebrief/-telegram/-boek, nomenclat*, cryptogra*,
"sleutel van/voor/tot ... cijfer/code/geheim"), and logs every fonds read in `*.fonds.tsv` (set, guid, toegang, title, components, bytes,
hits). `show.py` filters the hits (drops "gecodeerd met", cijferlijst, music notation, "niet te ontcijferen", items dated after 1900).
Note: the `id` field is the first `unitid`, which in several sets is the GUID, not the inventory number.

| Set | EADs read here | Notes |
|---|---|---|
| 236 Noord-Hollands Archief | 2,243 (records 431-2,673 of the id list) on the first pass | finishes the set left at 430 on 9 Nov; see "Re-read" below |
| 5 Groninger Archieven | 2,327 (records 441 on) | finishes the set left at about 450 |
| 59 Haags Gemeentearchief | 2,352, the whole set | was 1,434 of 2,386 |
| 136 Westfries Archief | 2,113, the whole set | was 1,237 of 2,151 |
| 46 RA Dordrecht | 1,170, whole set (new) | one find: 325 inv. 44 |
| 2231 NIMH | 295, whole set (new) | all hits 20th century (Nuboer's cryptography papers, WW2 codes) |
| 128 Langstraat Heusden Altena 763, 137 Zaanstad 629, 126 Voorne-Putten 491, 386 Noordwest Utrecht 370, 319 Rijnland 278 of 289, 434 NoVA 53, 150 Schieland 47, 111 Sittard-Geleen 23, 28 Eemland 3 | whole sets (new) | no early-modern cipher item |
| 102 Rivierenland, 239 Zeeuws Archief, 26 Achterhoek-Liemers, 142, 184 | see "Re-read" | |

Sets that are empty or nearly so in the feed (45 Deventer, 131 Waterland, 103 Roermond, 105 Alphen, 35 Flevoland, 1950, 62, 72, 1949, 15,
2557, 2803, 2801, 1648): nothing to read. Gelders Archief (37), HC Overijssel (141), BHIC (235) and Het Utrechts Archief (39) were done
on 9 Nov; Tresoar, Drents Archief, Amsterdam and Leiden are not in the feed at all.

Early-modern cipher components in the OAI sets read here: RA Dordrecht 325 inv. 44 (row); RA Dordrecht 383 inv. 803 and 847 (masonic
cipher papers and undated notes "in geheimschrift" of the lodge La Flamboyante: excluded, lodge alphabet, no date); Noord-Hollands
Archief 3248 Penninck Hoofd inv. 141 ("Briefje in geheimschrift (met codering) en tekeningetje, z.d.": undated note with its key,
not a row); Groninger Archieven 696 inv. 595 (row), 561 inv. 439 (key lead), 623 inv. 1597 ("Datering in geheimschrift": a date only),
1109 inv. 487 and 2393 inv. 353 (already excluded on 9 Nov). Everything else is modern: classification codes, grade lists, code books of firms.

## archieven.nl site search: terms and hit counts (inventories holding the term)

geheimschrift 51, cijferschrift 14, cijfercode 19, chiffre 3, chiffres 5, geheimtaal 7, codeschrift 2, cipher 5, cyfer 2, ontcijfering 6,
ontcijferd 20, ontcijferde 7, cijfercodes 6, cryptografie 4, cijfer 477 (315 listed, about 250 opened before the run was stopped),
cijfers 1,251 (not worked: statistics), "in cijfer" 398 (word search, same noise; not opened).
Zero: gecijferd, cijfersleutel(s), cijferbrief/-brieven, gechiffreerd(e), cijfferschrift, chiffer, cypher, cijferalfabet, cijfertabel,
geheimcode, codebrief/-brieven, déchiffré, chiffré, cifra, cryptogram, cijfertelegram.
Output: `anl_hits.jsonl` (one line per term and inventory, with the item descriptions found); `show_anl.py` prints it.

About 16 inventories returned by the search showed no item list (no "Bekijk gevonden archiefstukken" button; the term probably sits in the
introduction or in file names): Tresoar 2 (microfiches of the Saxon government papers), 7-02, 7-06, 7-14, 273-03; Zeeuws Archief 7107; Rotterdam
412-01; NHA 3005; Utrecht 1003; NIOD 244. Tresoar 7-02 and 7-06 are already covered by the APE sweep (catalogue 1950, 1953; leads 1951-1956).

## Found, and what was done with it

- **New rows**: see the table above.
- **Already in the project** (APE sweep, 9 Nov sweeps): Gelders 0439 inv. 124-126 (catalogue 1945, lead 1946), Tresoar 326 inv. 925
  (catalogue 1949), Tresoar 7-03 inv. 311 (= KHA A23-311), Tresoar 7-05 inv. 8 (Hendrik Casimir I 1640: the KHA entry in the catalogue),
  Zeeuws Archief 202.90 no. 4 (lead 1947), Het Utrechts Archief 1001 inv. 3577 and 1010 inv. 1191, 4515, Groningen 2100 (lead 1948).
- **Key leads** (`key_leads.json`): Bingerden 144 and 518 (Hendrik Hop, England 1723; "Cleef/pour dechiffrer"), Bentinck 3973 (Reinhard van
  Reede's key, before 1747: try on the Goslinga row and on catalogue 2446), Waardenburg 782I-II (Merode's embassy to Spain 1660-62),
  Tresoar 323 inv. 5592.52 and 5535 (Willem Lodewijk's cipher explained: try on catalogue 1950, 1953), Drents Archief 0185 inv. 496 and
  0617 inv. 724, Van Lynden van Hoevelaken 12, Groningen 561 inv. 439.
- **Excluded**: Gelders 0001 nos. 1738.01-0055 and 1735.1-0078 (letters that *mention* a cipher letter, Charles of Guelders), Gelders
  0370/1257 kept only as a lead (cipher not found in the sample), KZGW 3864 (notes of 1837 *about* cipher letters), Groningen 835 inv. 256
  (Julsing's diary: printed 2006), Westfries 0778 inv. 374 and the music "cijferschrift" items, the IMOE guide entries to RGADA (Matveev to
  Golovin 1703, "in cipher code": Moscow holdings described in a Dutch guide, outside this sweep), all 20th-century items (NIMH, NIOD,
  burgomasters' "geheimschrift" circulars of 1919-1967).

## Nationaal Archief

`research/nationaal_archief` already ran the title search for the main cipher words. `na_terms.py` ran terms it had not (cijffer, cijffers,
cyfer, cyffer, chiffer, ciffre, codebericht, codetelegram, gecodeerd, cryptogram, geheimtaal, cijfertelegram, cijferbrief/-brieven,
cijfercode(s), gechiffreerd(e), cypher, cipher, dechiffreren, ontcijferen, cijferalfabet, cijfertabel, ontcijferde, gedechiffreerd(e),
codeschrift, correspondentiecijfer, geheimschriften, cijferschriften, chiffreren, sijfer, chijfer; VOC 1.04.02 skipped because its hits are
handwriting-recognition noise). Raw output `na_hits.jsonl` (4,145 lines, mostly fuzzy-match noise; multi-word terms such as "in code" match
any one word and were stopped). What the old spellings add is all keys or office papers, and all already known: 1.10.29 inv. 1207-1267
("Cijffers" for envoys: the Fagel key books, on DECODE), 2.21.227 inv. 335 (Correspondentiecijffer, target toulon1803), 1.10.110 inv. 179
and 183 (Burmania's and Buys's "cijffer": key-only). No new ciphertext item. Not done: the item-by-item walk of envoy series that carry no cipher word.

## What remains

1. Page through Gelders Archief 0370 inv. 1257 (856 scans) for the Waldeck cipher leaves; open Erdmannsdörffer before vetting.
2. Order scans: Rosendael 577 and 1240, RA Dordrecht 325 inv. 44, Bentinck 3973 (key), Bingerden 144/518 (keys).
3. Saxon dukes 1514: ask Tresoar how Baks summarised the cipher-only despatches (key rebuilt?), and HStA Dresden for images of Loc. 8183.
4. Ewsum 595: 158 of 199 scans not viewed. Goslinga 3889: pair the decipherment slips with their letters.
5. The same archieven.nl search with fonds-specific walks (envoy and family correspondence without a cipher word), which no keyword route finds.
6. The 16 inventories whose hits did not expand (above), and the rest of the "cijfer" inventory list.
