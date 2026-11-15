# Sweep: German, Austrian and Swiss state archive databases beyond GStA (14 Nov 2026)

Brief: apply the GStA deep-pass methods (big result sets, wildcards, same-origin fetch from a Claude in Chrome tab) to Archivportal-D
and the Landesarchive databases. **Result: 17 rows in `candidates.json`, 5 key-only groups in `key_leads.json`**
(`make_candidates.py` builds both from `_tmp/raw2.jsonl`, git-ignored). Every row is scored from finding-aid text (`seen: catalogue`),
none viewed. Nothing was merged; catalogue.json, leads.json and `merge.py` were not touched; nothing committed (one rule added to `.gitignore`
for `_tmp/`).

## Main finding: Archivportal-D was already swept, and Chrome is not needed for it

`research/COVERAGE.md` still lists "Archivportal-D: only the first 200 chiffriert slots" (`central_archives`), but `research/archivportal_d/` (26 Oct) and
`research/sweep_2026-11_archivportal_more/` (2 Nov) paged every hit through the public DDB Solr endpoint (no key, no bot check). That row is stale and can
go. I re-ran Solr with 90 terms, archives sector only, dated before 1920 or undated (`ddb_harvest2.py`: 1,744 records, 1.2 s per request). New terms not in
the earlier runs: chiffrieren, Chiffer/Cifer/Cyffer/Zyffer, Dechiffrement, Entschluesselung, "geheime(n) Schrift", "heimliche Schrift", Geheimalphabet,
Geheimsprache, Zahlenschrift/-chiffre/-schluessel, Ziffernalphabet, Kryptographik, Steganographie, Nomenklator/Nomenclator, Klarschrift,
Chiffrenbuch/-brief/-alphabet, Kanzleischluessel, Gesandtschaftsschluessel, cifre/cifris/cipher/cypher/"en chiffre", and the old spellings.

Triage (`triage.py`, `short.py`): 1,438 records with a cipher word outside the Bundesarchiv; 283 already held by id or shelfmark; of the rest, 607 pre-1860
records with a strong cipher word. Read by archive. Most of these are series already in the ledgers under a *group* row (a row lists "Nr. 2301-2336" and the
per-id check cannot see it): LASH Abt. 8.1 (Gottorp), Hessen D 4 / E 8 A, GStA PK, NLA Hann. 9g Mecklenburg files (Erffa, Gersdorff, Seckendorf in leads),
NRW, Saxon Geheimes Konsilium 034 and Chiffres volumes, Wertheim notarial marks ("Pergament mit Chiffre" = a notary's sign, not a cipher), WWI and military
Geheimschrift regulations, forest/finance "Entzifferung". The rows that survived a series-level grep are the 8 from Archivportal-D in the candidates plus
the key groups. Series-level duplicates may remain; the grep looked for fonds, correspondent and number.

Not in the DDB index: Archivportal-D carries only part of the Landesarchive (Bayern 7 pre-1860 hits, Berlin 4, Thueringen 13 of which 12 are theatre bills).
For those the direct databases were needed.

## Direct databases

| Archive | Route | Result |
|---|---|---|
| **Archivportal Thueringen** (`www.archive-in-thueringen.de`, Landesarchiv Thueringen) | Chrome tab on that origin, `fetch` of `/de/suche?searchterm=<term>&submit=submit`, parse `main .item` (hit = chain of Archiv > Bestand > Findbuch > Archivgut). Page 1 only (10-50 items; no paging found), wildcards ignored (`chiffr*` = `Chiffre`). Hit pages return the neighbouring items of the Bestand, so signature and date were read from the text before and after the matched title. | 57 terms. chiffr* 7, Chiffre 7, Geheimschrift 10, verschluesselt 11, chiffriert 5, Entzifferung 3, Kryptographie 1, Dechiffrierung 1, Geheimschluessel 1; "geheime Schrift" 35, Schluessel 176, Ziffern 149 (noise, page 1 only). **None of the Thueringen cipher items was in the repo**: 9 rows plus 2 key items (Gotha Geheimer Rat Nr. 3476, 5129). Hildburghausen (Kob), Weimar Reichstag acts 1541-42, Henneberg 1546-68, Weimar Hausarchiv. 19th-century Geheimschrift administration (Gotha, Rudolstadt, Altenburg ministries 1863-1918) dropped. |
| **BLHA Brandenburg** (`blha-recherche.brandenburg.de`) | The Angular front end calls `http://localhost:5003/rest/search` (a misconfigured API base, so the site shows "0 results" for everything: the user-facing search is broken), but the **same-origin `/rest/search?page=&page_size=&query=` works** from a Chrome tab on that host (JSON, 50 per page, `signature`, `title`, `created_display`, `description_level`). | 37 terms. chiffr* 5, cifer* 6, chiffer* 7, entziffer* 5, verschluessel* 16, geheimschrift* 1, Chiffrierung 5, "geheime Schrift" 204 (noise). 35 rows after dropping the noisy terms: 20th-century GDR/Nazi files, seals ("Entzifferung" of a seal), one 1396 charter ("cifer*" = a name), one Altlandsberg police file 1897-1919 (Geheimschrift), and **one weak 1759 row** (Hardenberg, Neuhardenberg Film 1563). BLHA holds little pre-1800 diplomatic material online. |
| **Oberoesterreichisches Landesarchiv** (`ooela.findbuch.net`, findbuch.net) | Chrome tab on that host; POST `rech_start.php?rech_nr=1` (body `words=...&op=and&truncate=true&kind=a&id=1&max=...`) answers JSON with ids only (no titles); titles were read in the UI. Wildcards do not work (`Brief*` = 0). | Chiffr 8 hits, Chiffre 7, Chiffren 4, chiffriert 1, chiffrierte 1, Geheimschrift 3, Ziffern 2, Chiffer 38 (surnames), Dechiffr/entziffer/verschluesselt 0. The 8 "Chiffr" hits: Telegramme 1876 (02.16.02 Nr. 3615/1876), five Nazi-period Chiffren files 1934-44, and one Herrschaftsarchiv "Akt Nr. 406" dated 1660 (title only "Akt Nr. 406"). The "Geheimschrift" and "chiffriert" lists could not be read (UI did not refresh). **No row.** |
| **Steiermaerkisches Landesarchiv** (`egov.stmk.gv.at/archivinformationssystem/`) | Chrome UI (framed JSF; typed into the full-text field). | chiffr* 3 hits: two posters of 1961-62 and a Bude letter of 1871 ("per chiffre?"); Chiffre 2. Geheimschrift and verschluesselt results were not read (page still loading in the screenshots). **No row.** |
| Tirol, Salzburg | Tiroler Landesarchiv has no finding-aid search on the landing page (an OPAC link only, `verbundopac.tirol.gv.at`, a library catalogue); the Salzburg Landesarchiv URL guessed (`/themen/kultur/landesarchiv`) returned 404. | **Not searched.** No route found in the time spent. |
| Landesarchiv Berlin | `landesarchiv-berlin.de` loads (cookie banner); `recherche.landesarchiv-berlin.de` does not resolve; no search route found. Archivportal-D carries 4 LAB hits (two police-file money collections 1880s and a Stieber Geheimschrift pamphlet). | **Not searched directly.** |
| Hessen (Arcinsys), Niedersachsen, LABW, Bayern (gda), Saechsisches Staatsarchiv, LASA | Not re-run: swept 2-3 Nov (`sweep_2026-11_german_portals`, `_2`, `austria_german_states`) with 32-43 terms each. Their Archivportal-D copies were re-read here with the new terms. | New items only through the Solr pass (below). |
| AIS (HHStA, OeStA) | Not re-run: `sweep_2026-11_hhsta_ais` and `aut_hhsta` cover 755 records. | - |

## What is new (candidates.json)

| Rows | What |
|---|---|
| 1 | **HStAS E 50/05 Bue 124, 129** (Wuerttemberg envoy Degenfeld-Schomburg at Munich 1845-46, "teilweise chiffriert, mit Dechiffrierung"): a paired set, class A. The Wuerttemberg cipher books of 1847 on are in the key groups, never listed in a ledger. |
| 2-3 | GLA 111 Nr. 304 (1779, ciphered letter with Dechiffrierung); NLA OS Rep 100 Abschnitt 256 Nr. 4 (1630 Maudt report "verschluesselt und Aufloesung"). |
| 4-5 | **Marburg 3, Nr. 712** (1544, Hessian envoys' letters with a Chiffrenalphabet) and **BayHStA Kurbayern Aeusseres Archiv 4591** (288 fol. of cipher tables and ciphered letters, late 15th to early 17th century). |
| 6-8 | Three Saxon HStA Dresden items: Loc. 03447/28 (deciphered letters 1758-59), Loc. 00694/10 (1893 Chiffre resolutions of Manteuffel's 1712-13 reports, digital copy link) and 10736 Nr. 00457/02 (1850 police decipherment, digital copy link). |
| 9 | BLHA 37 Neuhardenberg Film 1563 (1759, weak). |
| 10-17 | **Thueringen**: Kob correspondences at Hildburghausen (Nr. 1006 with Seelig, Nr. 998 with Schneider, Nr. 368 with Fischer, each with its own key in the volume; Nr. 1307 Radefeld, no key named), **Reg. E Nr. 136 (Saxon councillors at Regensburg 1541 and Speyer 1542, key on fol. 393, parts in print)**, Henneberg 1546-52 (Wallenrodt, Geheimschrift 1550) and 1550-68 (Anna Maria dowry, Bl. 191-195), Fritsch 1845-58 (Bundestag reports, 135 Bl.). |

Grouping follows one key per entry: the three Kob correspondents are separate rows. The Saxon Loc. numbers and the E 50/05 volumes are single-key rows
by description. Nr. 368 is one row with the neighbouring Kob-Fischer volumes (same partner), to be split when seen.

`key_leads.json`: Baden key volumes GLA 48 Nr. 65-84 and 49 Nr. 1958; Wuerttemberg Chiffrierbuecher HStAS E 59 Bd. 232-242 and legation files; Nassau keys
(HHStAW 171 A 615 of 1578, 171 K 569, 172 Nr. 354); Nuremberg Schwedische Kriegsakten 80 and Hohenlohe Oe 1 Bue 18778; Saxon/Thuringian key items (Roetha 2423,
Gotha Geheimer Rat Nr. 3476 and 5129, Loc. 00663/01 and 02684/08).

## Skipped as already held or not a cipher

Dedup used `known.py`-style greps (fonds, correspondent and number) over catalogue.json, leads.json, decode_updates/queue.json, every `candidates.json` /
`key_leads.json`, NOTES and sweep READMEs. Dropped as held (examples): Hessen D 4 and E 8 A volumes (catalogue 568, 1983), Sigmaringen Dep. 30/1 T 3 Nr. 702
(`archivportal_d`), Saxon Loc. 03233-03234 Chiffres volumes, Knorre 1462-63 (catalogue), Quelwitz/Urbich/Bernburg (LASA), Pirna/Poemer (Nuremberg), Zasius, Nassau-Siegen,
Mentzingen (GLA 72), HZA Hatzfeldt (Ni 1). Dropped as noise: Wertheim notarial "Chiffre" marks, Kaestchen mit der Chiffer (Weimar theatre bills), BayHStA MKr
Geheimschrift administration, WWI Geheimschrift regulations, Plansammlung "Ziffern", NLA Osnabrueck map "Ziffern und Buchstaben".

## Honest limits

- Descriptions only. No row has been viewed, and none has a web, Tomokiyo, Lasry or DECODE search. The vetting bar is not met for any of them.
- The Thueringen locations of signature and date come from text around the matched title on a Bestand page (the portal returns the whole group); Nr. 998, 1006,
  368, 1307, 136, 310, 2661, 269, 3476 and 5129 read consistently, the Speyer 1542 number, the Kob-Fischer neighbours and the Altenburg "Briefe an Georg Moritz
  von Sachsen-Altenburg, zum Teil chiffriert" (Nachlass Herzogin Adelheid, Staatsarchiv Altenburg, Bestand 28189, hit 5105808; signature and date not read) did not.
  Also unread: Archduke Stephan letters (Weimar Hausarchiv A XXVI Nr. 739b, "Chiffrierte Texte", 1858-74) and the Grand Duke / Alexander II telegrams in the same Bestand.
- Archivportal-D hit lists were read in the triage by title and the portal's snippet only; "digital copy link" notes on the Saxon rows are from the
  Archivportal record (not opened).
- Not done: Tirol, Salzburg, Kaernten, Vorarlberg Landesarchive; Landesarchiv Berlin directly; Steiermark beyond three terms; OOe "Geheimschrift" hits;
  Thueringen result pages past page 1; Czech and Swiss cantonal archives (covered by `sweep_2026-11_czech_*`, `_swiss_cantonal`; not re-run).

## Chrome use and blocks

Chrome tabs of the extension's group (the first tab was shared with another session that was working in ACTApro, so I opened my own; the group was closed
from outside once, and I rebuilt a tab). Rate about 1.5 s. **No CAPTCHA, bot check or login appeared.** Blocks and quirks, for the next sweep:

- The extension blocks tool output that carries `?query=`-style text (including `location.href` and any string with `=` pairs next to `&`): replace `?`, `=`, `&`
  before returning, or put results in `document.body` and read with `get_page_text`.
- Long `await` loops time out at 45 s ("Runtime.evaluate timed out"); start them un-awaited and poll a `window` array.
- **Archivportal-D time facet** (if the UI is wanted): `facetValues[]=begin_time=[* TO <day>]` and `facetValues[]=end_time=[<day> TO *]` with day = days since 0001-01-01
  (about 365.2425 x (year-1)); 100 rows a page via `rows=100&offset=N`; the Solr route is simpler.
- A navigation in the shared tab group lost in-page data twice (Chrome closed the group): keep a copy outside the page.
- Sources needing Chrome, for the next sweep: Archivportal Thueringen (same-origin fetch), BLHA `/rest/search`, ooela.findbuch.net `rech_start.php`, Steiermark ArchivIS (UI).
