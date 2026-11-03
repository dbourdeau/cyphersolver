# US sources that blocked earlier sweeps (3 Nov 2026)

ArchiveGrid, the US societies (APS, Gilder Lehrman, Virginia, New-York Historical, Maryland), the Yale detail pages and UT
Benson, all listed as blocked in `research/COVERAGE.md`. Run in Claude in Chrome. Where Cloudflare showed a checkbox the
owner cleared it; Claude clicked none. `make_candidates.py` builds `candidates.json` (108 rows), merged into
`research/leads.json`. `apply_vetting.py` holds the five vetting blocks, `review.py` the review pass (keyed on shelfmark, so it
survives a renumbering) and `aspace_harvest.py` and `pdf_grep.py` the reusable harvesters. Nothing here was viewed on an image: all rows rest on archive descriptions.

## Result by source

| Source | Route | Result |
|---|---|---|
| **ArchiveGrid** | Chrome, same-origin `fetch` of `/archivegrid/?q=..&offset=..&limit=100`, 1.5 s spacing. The check passes alone after about 10 s or takes one human click; it comes back after about 40 minutes | 59 phrase terms, then bare "cipher" (761) and "cypher" (229). 1,582 records kept after noise filters; about 360 of the 384 with cipher wording on the card were read in the sweep and 1,193 of the other 1,198 whole records in the review pass (5 kept failing with server errors). Spanish terms return BNE records already in the leads. Catches holders no sweep had reached: Morgan, BYU, Indiana, Duke, Connecticut, Michigan, Chile, South Africa, State Library of Victoria |
| **Gilder Lehrman** | Chrome, `/site-search?keys=` with `items_per_page=100`; item pages `/collection/glcNNNNN` are public. `/collection` itself redirects to a sign-up page and scans need a login: no account was made | 20 terms, 127 items, item-level. Best single source for American letters |
| **APS** | Chrome, `search.amphilsoc.org/collections/search?keyword=`, then whole EADs from `/collections/data/ead/<id>-ead.xml` | 14 terms, 19 finding aids, grepped in full. Franklin Papers calendars give letter-level notes |
| **Virginia** | Virginia Heritage is now **ARVAS**: `search.arvasarchive.org/catalog.json` in Chrome (curl gets 202). The old `ead.lib.virginia.edu` search redirects there | 22 terms, 380 records. Covers UVa, William & Mary, Mount Vernon, Virginia Tech, LVA, WVU. VMHC's own catalogue was not found: `vmhc.catalogaccess.com` is an error page |
| **Yale detail pages** | `archives.yale.edu` answers 403 even in Chrome, including after the owner's check. **`ead-pdfs.library.yale.edu/<resource id>.pdf` is open to curl**, and Quicksearch result rows give the resource id | 230 collections hit; 17 historical ones grepped (`pdf_grep.py`). Confirms four of the "cipher matched" rows and overturns one |
| **UT Benson** | Chrome, `collections.lib.utexas.edu/api/search` (fuzzy; results filtered on real cipher words) | Nothing among digital assets. Finding aids stay in TARO, whose API ignores the query; three Benson collections reached through ArchiveGrid wait to be read there |
| **New-York Historical** | `specialcollections.library.nyu.edu/search` shows a "confirm you are human" page; `findingaids.library.nyu.edu/nyhs/` denies access | **Not swept directly.** ArchiveGrid gave 13 N-YHS records and 4 rows |
| **Maryland** | `mdhistory.libraryhost.com` (ArchivesSpace 3.2) loads for curl, but its search returns "No Records Found" for every word, even "letters" | **Not swept**, a fault on the site. ArchiveGrid gave no Maryland Center record with cipher |

## Catalogue

Five leads passed the gate and were promoted, all "not online" with the archive's description quoted: **2118** Philip IV to
Velada 1636-41 (35 letters, "23 of the letters are not deciphered"), **2078** Lilly Library cryptographic manuscript (15 pp.
"undeciphered code"), **2060** Humphrey's journal 1776-77, **2079** letter to Benjamin Farar 1754, **2061** Smith to Tomlinson
postcards 1880. Six rows closed in review; 97 stay leads with no vetting block.

## Review pass (3 Nov 2026)

The owner asked whether the leads had been fully reviewed; they had not. What the pass did:

- **Prior art on the promoted entries.** All 320 text pages of cryptiana were mirrored and grepped, and `GL.htm` too, for every
  name in the promoted rows. No hit. The vetting blocks now say so; before they rested on one web search.
- **Unread ArchiveGrid records.** Search cards show only the first 500 characters, so 1,198 records had no cipher word visible.
  Reading the whole records found 39 new rows (the `# Review pass` block in `make_candidates.py`), including the best item of the
  sweep, Philip IV to Velada. The cheap filter had been hiding it. The cost was about four hours at 14 records a minute.
- **Rows kept without the sentence read.** Terriesi was closed (only "Keeper of the cipher"). Loosey was upgraded: "54 telegrams to
  and from Maximilian and Empress Carlota, many of them in code, 1866-1867". The three Benson rows could not be read: still weak.
- **Named print sources**, where reachable.

Closed: 2101 Wellington to Popham (printed, Gurwood ix); 2068 Mary of Guise 1560 (key on cryptiana, SP53/23 no. 2/8); 2056 Morris
and Livingston to Franklin 1782 (WE008; five decoded on cryptiana); 2072 Bossuet 1698 (`GL.htm`, key in volume); 2091 Craig 1781
(Common cipher, Saberton 2019); 2076 Terriesi (not a cipher).

**Not done.** No scan was viewed for any row. Morgan record pages stayed behind a Cloudflare checkbox, so all Morgan rows rest on
ArchiveGrid's copy. Print not compared: Kline (Burr), Ribier (Henry II), Akkerman (Elizabeth of Bohemia), Poynting (Charles I),
Arckenholtz (Christina), Saberton's Cornwallis Papers (Rawdon), Papers of Franklin for Wharton 1778. Each lead's vetting block is
still to write. In reading, record keyword extracts were read rather than whole records, and about 190 hits were dropped by a
second noise filter ("undeciphered" signatures, "en clave", BNE "cifrada" already swept). Yale: 213 of the 230 collections remain
ungrepped.

## Best leads, not promoted

1. **Sfondrati letters, BYU Vault MSS 771**: 27 items of 1583, mostly Carlo d'Aragona Tagliavia (duke of Terranova, governor
   of Milan) to Paolo Sfondrati, plus four to the future Gregory XIV, "many ... partially or entirely in code". All digitised
   at `archives.lib.byu.edu/repositories/14/resources/7631/digitized`, but the images sit on `cdm15999.contentdm.oclc.org`,
   which times out from this network. Web search found no study. Try another network first: this could be promoted, and
   worked, the same day.
2. **Burr to Alston, July 1804 (GLC01523)**: pp. 2-3 and a Biddle enclosure in digits, Roman numerals and signs; image on
   Google Arts & Culture. Kept out only because Kline's edition (1983) could not be checked: archive.org lends it and its
   search-inside returned nothing.
3. **Imperial Mexican consulate telegrams 1866-67 (Loosey papers, N-YHS)** and the **Lilly's Maximilian correspondence**; the
   Diccionario telegráfico (Mexico, 1866) on cryptiana telegraph2.htm is the first key to test.
4. **Christina to Alexander VII 1655 (letter and cipher copy)**, **Lake to Murray 1804 (clear copy exists)**, **Pescara 1562**,
   **Henry II 1551 and 1558**: Morgan, reached only through ArchiveGrid; the Morgan's own record pages stayed on their check.
5. **Essex to Bouillon, 1596 (Morgan)**: partly deciphered between the lines, so the rest may be solvable from the interlinear.
   **Charles I's 66 "secret letters" of 1648, names in numerical cipher (Beinecke, Hopkins petition)**. **Wilkinson-circle coded
   letters of 1790 (Beinecke)**. **Richard Vance's 19 coded diary volumes (Kentucky)**.
6. **Wharton to Bancroft, May 1778 (APS Franklin Papers XLVII, 114-115)**: Papers of Franklin could not identify the code
   numbers in his 1777 letter.

## Seen and left out

- **Rufus King to Pickering, 9 Nov 1797 (GLC04798)**: Gilder Lehrman says "unable to be uncoded". King's *Life and
  Correspondence* ii prints it: "R. King to Secretary of State, No. 52. Wholly in cipher. London, Nov. 9, 1797". Printed
  since 1895. A warning for every other "undecoded" here.
- Read at the time or key with it: Cather diaries 1864-65 (deciphered in the WVU transcript), Cornwallis to Wemyss, Balfour to
  Saunders, Rochambeau 1782, Goodricke 1766, Beauregard, Thomson to Jay 1780, Monroe 1796, Trist 1847, Jefferson items,
  Hanbury-Williams, Bralley's pigpen, Guerrant, Bailey Willis, Herbert's journal, Gamage (translated), Elmendorf (printed),
  Prestwood (Browder), Wigglesworth, Wesley.
- From the review pass: Sinclair Lewis diaries 1900-07 (Yale finding aid lists a translation of the coded passages); Constantijn
  Huygens jr. journal 1649-50 (KB KA 53, Heijbroek, "Het geheimschrift van Huygens ontcijferd"); Louis-Philippe to Marie-Amélie
  1810 (the record says the numbers "don't mean anything": lemon juice); Pickering to King (deciphered between the lines); Evelyn to
  Pepys 1689 (Pforzheimer catalogue prints a partial transcription); Ballard diary 1816-18 (a researcher's key is with it); Hayes-Tilden telegrams; Grant's marked
  "(Cipher)" drafts, which are clear; Fernando el Católico to John II and Fernández de Córdoba 1622-29 (BNE, swept by
  `sweep_2026-11_es_hispana`; lead 1598 holds the 1478 letter).
- The Yard letters of Oct 1699 ("almost entirely in cipher, undeciphered" in the PDF) are `targets/yard1699`, already read.
- Madison to Pinkney and Monroe (GLC04924, 07466): State Department code and Papers of Madison, key lookups.
- BNE items in ArchiveGrid (Mirabel, Leopold I, Hurtado de Mendoza, Carpi, Caracena) are already leads.

## Corrections to older rows

Catalogue statuses 801, 802, 804, 805, 806 now quote the Yale PDFs. **Catalogue 802 (Orrery to Danby) came with its key and
Danby decoded it**, so it is a removal candidate; it is left in for the owner's decision.

## Key leads

Saberton, *Decoding British ciphers used in the South, 1780-81* (Virginia Historical Society typescript); Kingston's three
grille cards 1777-79 (GLC04764.01-.03); printed 1781 nomenclator, Livingston's (GLC01450.601); Stager cipher (GLC06233);
Army of the Potomac code 1863 and State Department code 1827 (Chicago History Museum); Page's 1789 letter to Tucker;
Perwich's cypher (Osborn File 1410); Dumas's cipher (APS, XVII-XVIII); Poley's and Stanhope's memoranda of cipher (OSB MSS 2);
Sarah Marlborough's cipher to Mrs Clayton (OSBORN FC110). From the review pass: **KB KA 169, keys used in letters to Alva and others**
(early 17th c.); Francis I to Mesnage 1545-46 with "a key to the cipher" (Morgan, 14 letters); Ludwig I of Bavaria "Code für
Geheimschrift"; Thompson's Confederate cipher; Luzerne 1782 (a note says 8 pages of cipher went with it; they are not there).

## Tool notes

- A record-reading loop in a background Chrome tab dies every 30 to 60 minutes: the tab gets a new id and freezes. Save to `localStorage`
  every 5 rows, then open a new tab, close the old one and restart from what is saved. `get_page_text` returns 50,000 characters where
  `javascript_tool` returns about 1,000: write the rows into a page element and read that.
- Chrome tabs running harvests side by side were swapped for new tab ids and froze, losing page variables. Run one harvest at a
  time and save to `localStorage` after each term. ArchiveGrid's check lapses in a long run (403): reload the page and go on.
- Noise: arithmetic "cipher books", monograms, the Cypher Society at William & Mary, the shorthand items at Alabama (Foster).
