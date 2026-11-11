# Dutch regional archives through archieven.nl, second pass (11 Nov 2026, cloud session)

Brief: `research/_nov11/BRIEF.md`. Finishes what `research/sweep_2026-11-11_dutch_oai` left (its "What remains" items 1, 4, 6 and part
of 5). Nothing here was written outside this folder; page images are in the session scratch directory only.

**Result: two leaf lists for existing catalogue entries, 8 candidate rows (`candidates.json`, none with a vetting block, none
viewed), 3 key-only items (`key_leads.json`).** `make_candidates.py` builds both files.

## 1. Leaf lists (existing catalogue entries, not re-listed as candidates)

| File | Scans viewed | Cipher |
|---|---|---|
| `culemborg_1257_leaves.json` (Gelders Archief 0370 inv. 1257) | 856 of 856 | 14 scans, all between 715 and 819, 11 Aug - Sept 1655, six pieces, about 170 lines, no interlinear decipherment |
| `ewsum_595_leaves.json` (Groninger Archieven 696 inv. 595) | 199 of 199 | one opening only (scan 193, shown again as scan 1), about 30 lines with its key |

Culemborg 1257, what is new against the first pass (which saw scans 715 and 795):

- The cipher is **not** only the Elector's: Waldeck's own letters to the Elector of 7 Sept (scans 787-789) and Königsberg 14 Sept 1655
  (813-814) carry passages in the same small number cipher, so both directions are there.
- The Elector's pieces: a "Postscriptum" wholly in cipher (717; the slip on 715 is its foot), the letter of Cöslin 4 Sept (793-795)
  with a P.S. (797-798), and a letter of September naming Radziwill (819).
- **Scan 723-724, the Elector's letter of 17 Aug 1655, is in a different system**: a code with numbers up to four digits and single
  letters between them. The catalogue entry describes only the 1-23 alphabet.
- Scan 819 has the number groups underlined and notes in the left margin in another hand. It was not read; it may be a contemporary
  summary or part decipherment and should be looked at before that leaf is called undeciphered.
- Scans 1-712 and 820-856 are clear (drafts, memorials, muster and pay tables, blanks).

Ewsum 595: the first pass took scan 1 for the front of the register. It is the same opening as scan 193, near the end, repeated at the
head of the scan order. The facing pages (scan 192) hold clear household recipes, and the clear Latin caption after the cipher reads
"ad perforandum caput gallinae", so the cipher notes are probably recipes or tricks, not business. The dark slips in scans 57-158 are
blotting paper, not writing.

Limits, stated in both files: contact sheets at 220-330 px a scan show number or symbol cipher where it fills a line; a single short
group inside a clear page could have been missed.

## 2. The inventories whose hits did not expand

The first pass counted about 16; `anl_hits.jsonl` in fact had 78 term-and-inventory pairs with no item list outside "cijfer" and 120
under "cijfer". The cause was the script (it kept only links holding the highlighted word, and the word is usually in a note that the
collapsed line does not show), not the site. `anl_exp.js` clicks "Bekijk gevonden archiefstukken" and keeps every found item;
`anl_det.js` opens an item and reads its note. All 198 pairs were re-run (`jobs_n0.tsv`, `anl_exp.jsonl`); 30 still show no list (the
term sits in the introduction or a file name: NHA 3005, Groningen 755, Tresoar 12-11, 1, 2 for some terms, and others).

What the 16 named ones hold:

| Inventory | Found | Outcome |
|---|---|---|
| Tresoar 2 (microfiches, Brussels Audience papers) | no. 255: letter on fiche inv. 293 f. 167 in cipher, f. 170 "geeft de ontcijfering"; no. 258 | deciphered at the time: excluded |
| Tresoar 7-02 | 51, 191, 195, 198 | in the project (catalogue 1950, 1953; leads 1951-1956) |
| Tresoar 7-06 | 347 Andreae | in the project |
| Tresoar 7-14 | 713: unsigned cipher letter of 3 Sept 1787 | **row** |
| Tresoar 273-03 | 311: nun's invitation in secret script, 19th c. | **row** (low; probably read by the archivist) |
| Zeeuws Archief 7107 | cabinet papers 1952-1967 | modern: excluded |
| Rotterdam 412-01 Hudig | letter books 57-58 "in een moeilijk leesbaar geheimschrift, deels in het Engels" | **row** (may be shorthand) |
| NHA 3005 | no item list | not resolved |
| Utrecht 1003 | 191: draft "gedeeltelijk in cijfers", scans online | **row** (cipher discussed in print: Cornelissen) |
| NIOD 244 | diaries 1940-45 | excluded |
| Gelders 0001 | 7 items of Charles of Guelders | **row** for three with no solution noted; 1703.1-0160 (solved by Nijhoff, key and transcription added) and 1733.1-0071 (transcription above) excluded; 1738.01-0055/-0056 mention or name only |
| Groningen 623, 1109, 696; Dordrecht 325 | as in the first pass | already handled there |
| Utrecht 1001 Amerongen | 3486-3488 Torck, 3534 Hyndford, 3577 | all in the catalogue |
| HC Limburg 01.075 no. 589, Utrecht 57 no. 359, Groningen 2100 no. 1462.491 | | in the catalogue or leads |
| Huis Bergh 0214 no. 1154 | minute book 1574 with "een aantal sleutels voor cijferschrift", scans online | key lead |
| Rotterdam 37-01 Van Teylingen | 17: Orangist letters of 1787 with a "geheime cijfercode" for names | **row** |
| Tresoar 7 | 808: Van Reyd and Wier 1595-97, "enige woorden in cijfercode" | **row** |
| Utrecht 83 | Boursier 1727: veiled language (a marriage as cover), not cipher | excluded |

## 3. The rest of the "cijfer" list

The table view lists 477 inventories for "cijfer"; the first pass listed 315. `anl_list.js` (START=300) listed entries 300-477
(`anl_list_cijfer.jsonl`, 177 inventories, none seen before). 110 are plainly modern by title (municipalities after 1850, firms,
schools, NIOD, societies) and were not opened; the other 67 were queued in `jobs_cijfer2.tsv` and expanded into
`anl_exp_cijfer2.jsonl` (all 67 done): "cijfer" is a number, a date figure or a mark in every one (charters, maps, music, one
Groningen resolution on traitors' letters); no cipher item. In the 120 "cijfer" pairs re-run from the
first pass the word means a number, a mark or a statistic every time (Eindhoven municipal classification codes are 60 of them); the
only pre-1800 groups are the Gelderse Landdagsrecessen (Gelders 1707, 34 regests: "cijfer" as a figure) and town registers.

## 4. New terms in the site search

Phrases in double quotes work (`"in cijfers"` 109 inventories against 949 unquoted). A trailing `*` works on some stems (`cijfer*`
2,104) and not others (`cijferbr*` 0). Counts of inventories (`anl_list.jsonl`):

"in cijfers" 109, "en chiffres" 1, "in cijfer" 1, "geheim schrift" 2, gecodeerd 98, "in code" 21, "geheime code" 3, "geheime tekens" 1,
codetaal 4, "in cijffers" 1, cijffers 6, cyffers 1, codetelegram 3, codebericht 3, cijfertelegrammen 1, "geheime correspondentie" 36,
"geheime brieven" 24, nomenclator 1, decodering 3, ontcijferen 40, "niet ontcijferd" 5, chiffrée 1, Chiffren 1, cijfertaal 1,
tekenschrift 28, "sleutel tot" 22, "sleutel van het" 38, "sleutel voor" 29, "sleutel op" 21, "met sleutel" 26, "in geheimschrift" 24,
"in cijferschrift" 11, "onzichtbare inkt" 3, "secrete correspondentie" 4, chiffreur 1, "gecodeerde brieven" 2, "gecodeerde brief" 1,
"gecodeerd bericht" 1, "verborgen schrift" 1, "onleesbaar gemaakt" 33.

Zero: "geheime taal", "in chiffre", "in chiffres", "in cijffer", "in cyfer", "in cyffers", cyffer, chiffer, gechiffreerde,
"gedeeltelijk in cijfer", "gedeeltelijk in code", codebrieven, cijferbericht, cryptogram(men), gedecodeerd, déchiffrement, dechiffré,
chiffrées, "lettres chiffrées", chiffrierte, chiffriert, "in Ziffern", cifra, cijferletters, "geheim alfabet", cijfersleutel,
steganografie, "geheime inkt", "sympathetische inkt", dechiffreren, gedechiffreerd, dechiffrering, "in secreet", getalcode,
cijferalfabet, telegraafcode, onontcijferd, vercijferd.

397 term-and-inventory pairs were expanded (`anl_exp2.jsonl`; not opened: ontcijferen, tekenschrift, "onleesbaar gemaakt" and the
"sleutel van het / voor / op / met" phrases, which are about reading old hands and keys of buildings). "code-" (2,149) is noise and was
not worked. What they add beyond section 2:

- Tresoar 323 inv. 5592.23, 5592.45, 5592.51: Willem Lodewijk letters partly in cipher, next to the key list 5592.52 (**row**).
- Tresoar 323 inv. 4036-4047: travel journals of Johan Vegilin van Claerbergen 1707-1716, "voor een deel in geheimschrift, in het
  Grieks": Greek letters used as a private script; left out (not a cipher in the project's sense), noted here.
- Drents Archief 0185 inv. 564: Van Heiden Reinestein's extract *from* a coded letter, 1800 (clear text, no ciphertext): excluded.
  Inv. 493 (414 letters 1766-1803) is returned for "in geheimschrift" but the note was not found in the part of the description read.
- BHIC 346 Cuypers van Velthoven inv. 990: letter "in code" of Prince Maurice to Breda, with Cuypers's translation: read, excluded.
- Tresoar 319 inv. 2419 and HC Leeuwarden 1759 inv. 87: key leads.
- Everything under gecodeerd, "in cijfers", "in code", codetaal, decodering and the telegram words is 20th century (NIOD, NIMH, civil
  defence, classification schemes); "geheime correspondentie / brieven" are secret registers of 1813-1940, not cipher.

Archives named in the task: Tresoar, Gelders Archief, Drents Archief, BHIC, Het Utrechts Archief and Zeeuws Archief all return hits
through the site search and are covered by the terms above. **Historisch Centrum Overijssel, Regionaal Archief Nijmegen, Het
Scheepvaartmuseum and the Koninklijk Huisarchief returned no inventory for any cipher term**: they are either not searchable through
archieven.nl or have nothing under these words (not checked which). KHA holdings appear only where Tresoar describes them (7-02 to
7-14).

## 5. Candidates

None has a vetting block: for each, a printed work that could hold a reading was not opened (named in the row's `verify`), and none
has been seen. known.py was run on every shelfmark and name (no hits beyond siblings); DECODE was searched with `decode_q.py`
(Teylingen, Reigersman, Larrey, Van der Hoop, Hudig, Reyd, Wier, Harlingen, Torre: nothing relevant); the cryptiana index, `GL.htm` and
the repo `unsolved.htm` were grepped for the same names (0).

| Row | Shelfmark | Note |
|---|---|---|
| Orangist letters to Van Teylingen, 1787, number code for names | Stadsarchief Rotterdam 37-01 inv. 17 | best new lead; not online |
| Willem Lodewijk to Boner, Juckema, Bourtange, 1589-1593 | Tresoar 323 inv. 5592.23, .45, .51 | key list in the same bundle |
| Van Reyd with Wier, 1595-1597 | Tresoar 7 inv. 808 | some words only |
| Unsigned cipher letter of 3 Sept 1787 | KHA, via Tresoar 7-14 inv. 713 | |
| Holland Mission draft partly in cipher | Het Utrechts Archief 1003 inv. 191 | scans online, not viewed; cipher discussed by Cornelissen |
| Charles of Guelders, three letters | Gelders Archief 0001, 1703.1-0062, 1738.01-0057, 1738.01-0059 | Nijhoff VI/2 not found online |
| Hudig letter books | Stadsarchief Rotterdam 412-01 inv. 57-58 | cipher or shorthand not known |
| Sister Padentiana's invitation | Tresoar 273-03 inv. 311 | trivial |

## Routes

- `www.archieven.nl` search, inventory and scan viewer in headless Chromium: works, no challenge. Four or five browser sessions at
  once made the scan viewer drop tiles (white blocks) or fail to open ("pages 0"); `white.py` finds such screenshots, and a single
  session with a 9 s wait per page (`anl_view2.js`, WAIT=9000) refetched them cleanly. Plan about 6 s a scan with two sessions.
- archive.org full text: the six "Gedenkwaardigheden uit de geschiedenis van Gelderland" files there are parts I-V and VI/3, not VI/2;
  AAU 12 (1884) and Cornelissen's Romeinsche bronnen were not found by title search.
- A container restart or usage stop killed the browser jobs once; all scripts resume from their output files.

## Scripts

`anl_list.js` (inventories per term), `anl_exp.js` (found items per inventory), `anl_det.js` (item notes), `anl_view.js` /
`anl_view2.js` (scan screenshots), `white.py` (bad screenshots), `sheetr.py` (numbered contact sheets), `ink.py`, `decode_q.py`,
`probe.js` and `dbg.js` (page inspection), `show_exp.py`, `make_candidates.py`. `anl.js`, `anl_item.js`, `sheet.py`, `show_anl.py` are
copies from the first pass.

## What remains

1. Culemborg 1257: read the margin of scan 819; transcribe the six pieces (the small alphabet should fall quickly; scan 723 is a
   separate code problem). The catalogue entry should be widened to both directions and the second system.
2. Ewsum 595: transcribe scan 193 with its key.
3. Het Utrechts Archief 1003 inv. 191: open Cornelissen I p. 643 n. 2 and AAU 12, then view the 63 scans.
4. Scan orders: Rotterdam 37-01 inv. 17 and 412-01 inv. 57; Tresoar 323 inv. 5592.23/.45/.51/.52 and 7 inv. 808; Gelders 0001.
5. Huis Bergh 0214 inv. 1154: view the scans for the 1574 keys.
6. HC Overijssel, RA Nijmegen, Het Scheepvaartmuseum, KHA: their own sites, since archieven.nl returns nothing for them.
7. The 110 modern-titled "cijfer" inventories of entries 300-477 were not opened.
