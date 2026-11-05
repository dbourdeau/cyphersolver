# Sweep D: eastern and northern gaps (4 Nov 2026)

Scope: Russia (RGADA, AVPRI, RGIA, printed), Ottoman, Hungary / Czech lands / Slovakia, Scandinavia beyond catalogue level, Baltics,
Ukraine, Belarus. Read first: `sweep_2026-11_russia`, `_ottoman_turkish`, `_hungary_czech`, `_malta_nordic_baltic`,
`_riksarkivet_volumes`, `_balkans_greek`, `scandinavia`, `central_archives`, `polish_archives`, `oldest/scan_2026-09-23/central_north.md`.

**Result: 31 rows in `candidates.json`** (all validated against the BRIEF.md schema and de-duplicated against `catalogue.json`, `leads.json`
and `known.py`): 21 from Lang's Hungarian repertory (catalogue level), 10 from Riksarkivet images (`seen: image`).
Scripts are in this folder (`cand.py` validates and appends; `rows_*.py` hold the rows). No Do-not-touch file was edited, nothing committed.
`merge.py` does not list this folder yet: add `sweep_2026-11_D_east_north` to its `SWEEPS`.

## The 10 best finds

1. **Pylyp Orlyk, Bender, Nov-Dec 1713**: Latin number-cipher despatches with the Latin plaintext written between the lines, a "clavis" heading.
   Riksarkivet, Diplomatica Muscovitica, Cosacica, `SE/RA/2113/2113.2/2`, images 37-42 of R0000481 (images public). Class A. Hetman-in-exile
   of the Zaporozhian Host; not in the repo, not on DECODE (Nordic dump). https://sok.riksarkivet.se/arkiv/rp6JwGDAFasc5R6mtPZn00
2. **Gyorgy II Rakoczi to Charles X Gustav, Dec 1656-Mar 1657**: Latin letters with graphic sign-cipher passages, one full page (about 500
   signs) with partial glosses. Riksarkivet, Turcica bihang Transylvanica, `SE/RA/2119/2119.5/4`, images 18, 20, 22, 23 (R0003533).
   Not in Lang's repertory. https://sok.riksarkivet.se/arkiv/Twx98TOXEaEFk8kcjTgJY3
3. **Hopken/Carlson, Constantinople, 1734-1742** (Turcica 9/22-9/29, nine more volumes beyond the 9/20-9/21 rows of 2 Nov): the same four-digit
   code, whole openings of numbers with Swedish or French written between them (9/26 image 147, 9/27 images 50 and 93, 9/28 images 227 and 482).
   `SE/RA/2119/2119.1/I/9/22` to `/29`. Class A; one key for all, so an editor may fold the eight rows into one entry.
4. **Breuner, Constantinople, 12 May 1583**: wholly enciphered German despatch, undeciphered per Lang; HHStA Turkei I Karton 48 Konv. 3
   ff. 137-151; keys DECODE R1384 and R1590 held. (Sister of cat. 342/343.)
5. **Teleki Mihaly, 13 letters Jan-Mar 1678** (Teleki Mihaly levelezese VIII, nos. 9-87): printed number ciphers; Hegedus (NyelvVilag 23, 2020)
   solved C.Tel.15 and says the clavis differs from 1666, so it probably serves the others. Class B.
6. **HHStA Wien, Ungarische Akten, Allgemeine Akten Fasc. 12 Konv. B ff. 45r-47v (1529)**: envoy's report, Latin graphic signs, "nincsen
   feloldva"; the same system is solved in-letter in Fasc. 10 Konv. B f. 68 (C.Jel.02). Class A.
7. **Gyorgy I Rakoczi to Istvan Racz (envoy at the Porte), 1642**: monoalphabetic letter cipher, "nincs feltorve"; MNL OL E 190 43. doboz no. 597.
8. **Mednyanszky to Gyorgy II Rakoczi, 1658-59, eleven letters** (E 190 44. doboz) with key tables in MNL OL P 497 that Lang marks unresolved.
9. **Archduchess Maria Christierna to Archduchess Maria, 1597, three letters** (MTT II/11 nos. 7, 29, 32), German numbers, undeciphered.
10. **Bathory Andras (1553-54, 3 letters) and Kerecsenyi (1555-56, 4 letters) to Tamas Nadasdy** (MTT IV/6-7), Hungarian signs, undeciphered.
    Plus Kuefstein to Ferdinand III, 27 Oct 1629 (ELTE G. 4 Fol. Tom. V p. 1461), with sibling drafts that carry the plaintext over the signs.

## What worked

| Source | Route | Result |
|---|---|---|
| Lang 2015 repertory (`real-d.mtak.hu/922/7/dc_758_13_doktori_mu.pdf`, 17 MB, text layer) | download to scratchpad, PyMuPDF, split on `C.xxx.nn` IDs: 918 rows, status column "megfejtetlen" (56), "nincs feltorve", "feloldatlan", "nincsen feloldva" | 21 rows. Earlier notes (`oldest/.../central_north.md`) had named only Ungnad, Sinzendorff, Wesselenyi Fasc. 327 and a few Teleki letters |
| Riksarkivet (SE) | `data.riksarkivet.se/api/records?text=&only_digitised_materials=true&facet=PartOfArchive:<series>` (141 digitised Diplomatica volumes), `.jsonld` for the IIIF id, `lbiiif.riksarkivet.se/arkis!R######_#####/full/320,/0/default.jpg`; 20-image contact sheets (`rik_sheet.py`, `rik_multi.py`, `rik_pick.py`) viewed by eye | 10 rows; the catalogue never says "cipher" for any of these volumes |
| Hungaricana full text | `www.hungaricana.hu/hu/search/results/?list=<base64 {"query":..}>&per_page=100&page=N`, server-rendered, plain `requests` works | "rejtjeles" 1,977 and "rejtjel" 2,796 hits: communist-era files and newspapers. Dead end. `hung_h.py` |
| Estonian AIS (`ais.ra.ee`, reachable since the 2 Nov reset) | `GET /et/description-unit/search?q=<term>&size=100&page=N`, server-rendered (the `from`/`until` date filter did not take; filtered by year locally) | 14 terms in Estonian, German, Russian: all 20th-century files. Only "Eingegangene Geheimschreiben 1845-1849" (EAA.1878.1.531), not shown to be cipher. `ais_ee.py` |
| Libris (`libris.kb.se/xsearch?query=..&format=json`) | plain `requests`, 14 terms | 2,609 records, almost all books; 9 manuscript records, none a ciphertext (Chifferlexikon D 1086a keys; Gortz papers I.g. 18) |
| NB.no API (`api.nb.no/catalog/v1/items?q=chiffer`) | reachable, 5,044 hits for "chiffer" | not harvested (printed books); a route for a later pass |
| Alvin (Uppsala etc.) | in Chrome only: navigate to `resultList.jsf?searchType=EXTENDED&query=..&noOfRows=50` and `get_page_text`; a scripted `fetch` from the page failed, and the JS tool blocks output with a query string | "chiffer": 18 hits, same as the October sweep (Gustav III F 414 "Chiffrée" letters nos. 18, 21 = clear originals; F 525 Beylon; F 480; F 422 with content matches). Nothing new |
| RGADA `http://rgada.info/` (plain http; https resets) | `/kueh/index.php?T1=<term>` (unique items: a showcase of 1 hit) and `/poisk/` (inventories, not cases) | Reachable but no case-level catalogue; cases sit in `online.archives.ru` (registration) |

## Blocked, or reached with nothing

* **Finna** (Finland): Cloudflare "Just a moment" in Chrome, did not clear in 12 s; not clicked (rule). Needs Daniel to clear it once in a tab.
* `dspace.cuni.cz` (Czech theses) and `archives.openjerusalem.org` (Ottoman Interior Ministry cipher items; an Open Jerusalem record title mentions a cipher
  to the ministry): connection reset or timeout from Python and from Chrome, so the network, not a bot check.
* `prlib.ru` search: a browser-check page for scripts ("Проверка безопасности"); `garf.su`, `rusneb.ru` 403; `archives.ru`, `rusarchives.ru`, `raduraksti.lv`,
  `dom.lndb.lv` time out; `avpri.mid.ru`, `skjalaskrar.is`, `elib.nlb.by`, `dlib.nlu.org.ua`, `slovenskearchivy.sk`, `archivportal.sk` do not resolve or refuse;
  `archives.gov.ua`, `cdiak.archives.gov.ua` 403 (not tried in Chrome: no time); `digar.ee` Cloudflare; `katalog.devletarsivleri.gov.tr` (BOA) login with a CAPTCHA (not touched).
* `goskatalog.ru`, `manuscriptorium.com` (no search API reachable), Kramerius (`kramerius5.nkp.cz/search/api/v5.0/search`, works but searches printed matter only; two
  Czech phrase queries gave nothing), `vademecum.nacr.cz` (opens, not searched), `mza.cz/actapublica` (parish registers only).
* Czech lands: **no archive item found**, only literature (below).

## Literature leads from web searches (not rows: no shelfmark with a visible cipher)

* Czech: Charles University theses on Ferdinand III's ciphered letters to Gallas 1635-38 (decrypted edition, core.ac.uk/works/192177705) and on the ciphers in Gallas's war
  chancery with a list of every ciphered document (dspace.cuni.cz/handle/20.500.11956/91542; could not be opened); *Raně novověká šifrovaná korespondence ve fondech šlechtických
  rodinných archivů SOA Plzeň*, Západočeské archivy 2012, pp. 44-73 (not online here); Mírka, Crypto-World 3-4/2013 (Rozmberk ciphers in Trebon). Lupa.cz piece (June 2024) on Czech cipher history.
* Ottoman: Bingöl, Cryptologia 2022 and 2023 on Ottoman diplomatic ciphers 1797-1877 (BOA HR.ŞFR series); Karabacak Yilmaz (TTK).
* Ukraine: Mazepa's letter to Leszczynski of Dec 1708, intercepted by the Russians and called enciphered (Siverianskyi litopys); the Orlyk volumes above are the first archival
  Orlyk cipher this project holds.
* Hungary: Hegedus's blog (kripto.blog.hu, 12 Mar 2016) solved Teleki to Szechy Maria, 6 Jul 1666 (C.Tel.68): a key lead for the Teleki rows.

## Key leads (bare keys, not rows)

DECODE R4310 ("Siebenbürgen Schauis" number key) and R4296 (1632 key), both already in the repo, for Rakoczi letters of the 1630s in Turcica 2119.5/4. Lang's tables T.Med.01
and T.Med.05 (MNL OL P 497 3. csomo, Mednyanszky keys), T.Kuf.01 (Kuefstein key reconstructed by Donath, Magyar Konyvszemle 1964), the Fasc. 10 Konv. B f. 68 system.

## Left out (checked)

* From Lang's list, left out because the table shows the cipher resolved or the key at hand: Gerendi 1529 (C.Jel.02-06), Zrinyi/Gembicki 1669 (key f. 77), Teleki to Szechy 1666,
  Kuefstein drafts (plaintext over the signs), Karolyi/Bercsenyi 1704-06 (overlap the Hungary sweep rows and the Commons-scan catalogue entries); Ungnad, Sinzendorff, Wesselenyi
  Fasc. 327 already tracked; Wesselenyi to Nadasdy 10 Oct 1663 (Fasc. 310 Konv. A ff. 32-35) is probably the "one more" of catalogue entry 1231 (ff. 36-37 and one more); MOL R 316 Misc. 27 f. 4
  (C.Mis.01, "nincs feltorve", c. 1650) belongs with the existing lead for R 316 item 27 (its keys), so no new row.
* Riksarkivet: Cosacica 2113.2/1a image 224 has a two-line cipher postscript (about 45 numbers) under a clear 1655/56 Latin letter to "Serenissima Christina": too short.
  Sheeted with no cipher: Turcica 2119.4/2 (Lagerberg 1710-11, fire damaged), 2119.4/1 (envoys 1592-1742), Polonica 12/60 (Dorffler 1667-70), 20/106 (1697), 22/110 (1700-07).
* Estonian AIS, Libris, Hungaricana: see the table.

## What remains

* Riksarkivet: sheets were made but **not viewed** for Muscovitica 2113.1/1/45/115, /47/118, /55/157, Gallica 24/54 (Bonde 1674-78), Italica 5/4 (Piranesi), Hollandica 5/7 (they sat in the
  session scratchpad, not the repo). 40 digitised volumes have no IIIF manifest (the whole 1709-14 Turcica run, Funck 6/9, 6/11). Polonica 12/61-62, 19/101, 20/105, Muscovitica 36/82 not
  sampled; each volume was sampled at only 20 of 150-1,000 images, so a volume marked "no cipher" is only "none seen". The Hopken volumes 9/22-9/27 were identified from thumbnails and need
  full-size confirmation. Images of Turcica 9/20-9/29 should be read as one code.
* Hungary: Lang's rows for 1536-1548 and the Rakoczi War items beyond those listed were not reviewed for "other" statuses (311 rows with no status word); MNL OL E 190 record pages and any
  image route were not opened; the Teleki editions (Gergely 1905-26) and MTT volumes are not located free online except RMPE 6 (Bethlen Miklos).
* Finna (needs a human to clear Cloudflare), Alvin by script, BOA (login), Open Jerusalem and dspace.cuni.cz (network), Russian and Ukrainian state archives (network or 403), Czech and
  Slovak archives (no item-level portal reached), Baltic Latvian/Lithuanian archives (see `sweep_2026-11_malta_nordic_baltic`).
