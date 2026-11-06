# Sweep: Czech regional archives that needed a browser (6 Nov 2026)

Follow-up to `research/sweep_2026-11_czech_slovak/` (same day), whose "Blocked / needs Chrome" list this pass works
through: SOA Litoměřice, SOA Třeboň, Zemský archiv v Opavě, and the Charles University thesis on the Gallas war
chancery ciphers.

**Result: 6 rows in `candidates.json`, 4 key-only items in `key_leads.json`** (built by `make_candidates.py`).
Five rows have ciphertext seen on photographs (RA Piccolomini, SOA Zámrsk, found through a 2017 thesis), one is
description-only (Rožmberk, SOA Třeboň). The portals themselves gave only keys (ZA Opava) and nothing early modern
(Litoměřice, Třeboň). `known.py` was run on every shelfmark, inventory number and correspondent: no duplicates.
`key_leads.json` is separate because `merge.py` accepts only cls A/B/C. This folder is not yet in `merge.py`'s sweep
list (outside this folder; add `sweep_2026-11_czech_chrome` there before merging).

## Routes

| Source | Route | Notes |
|---|---|---|
| **SOA Litoměřice digital reading room** (`digi.soalitomerice.cz/digitalnibadatelna/`) | Opens in Chrome with no challenge (the script-side `/human/verify` redirect does not appear). Bach "VadeMeCum" system: the form `searchForm` POSTs to `/digitalnibadatelna/vysledekList` (`patternTxt=<term>` plus the form's other fields); a `fetch()` of that POST from inside the page returns the result HTML; cards are `.minicard` (`.name`, `.zkratka`, `.dateOne`/`.vznik`, `.desc2`). | Item records cover district offices, town archives (SOkA), the Hartig family archive (Mimoň) and the Litoměřice bishopric collections. The **Clam-Gallas family archive (with the Gallas war chancery) and the Thun-Hohenstein archive (Děčín) have no item records and no finding aid in the portal** (searches Gallas 408 hits, Clam-Gallasů 86, Thun 554: all town, district or Hartig material; finding-aid filter: no Clam-Gallas or Thun aid). |
| **SOA Třeboň DigiArchiv** (`digi.ceskearchivy.cz`) | **No browser needed** once the call is known: `POST https://digi.ceskearchivy.cz/pages/search_result.php?id=&queryid=<any 32-hex>&doctree=10` with `sparam=<PHP-serialized query array>`, `sst=<offset, 10 a page>`, `lang=cs`; `searchtype` inside sparam picks the record type (13 finding aids, 14 inventory records, 12 fonds, 24 image notes ...). `digiarchiv.py` builds it; `da_sweep.py` runs the term list into `da_hits.jsonl`. Fond lists by department: `tree.php?menu=0&doctree=1Ga` (Třeboň), `1Gb` (Č. Budějovice), `1Gc` (Č. Krumlov). Fond record: `DA?id=<id>` or `/f/<id>`; a finding aid: `DA?menu=0&id=<921...>&pomid=<same>`. | 3.0 million records searchable, but item records reach the family archives only for the heraldic collection and the maps. The **Eggenberg** archive (NAD 222) is unprocessed ("nepřístupný"): one digitised unit (III 1G, 473 images), no finding aid. The finding aids of RA Schwarzenberg (Orlík 880 pp., Krumlov partial inventories), RA Buquoy (238 pp.), Historica Třeboň I-V (Rožmberk chancery, 1216-1659, ~1,600 pp.) and Cizí rody (Švamberk 224 pp.) are listed with page counts, but only their metadata is shown: the "Archivní pomůcka listinná (reprodukce)" scans do not appear for an anonymous visitor (no image pane; the PDF/XML/XLS buttons export the metadata record). Signing in might show them; not tried. |
| **Zemský archiv v Opavě digital reading room** (`digi.archives.cz/da/`) | The Radware page that blocks scripts (`/da/human/challenge`) cleared by itself in Chrome after a few seconds (no click). Same Bach system as Litoměřice: POST `/da/vysledekList`, further pages `GET /da/vysledekList?page=<n>` in the same session, detail `GET /da/vysledekDetail/<uuid>?page=<row+1>`, permalink `/da/permalink/<uuid>`. One long `fetch` loop froze the renderer for 45 s (it recovered); keep loops short. | Item level for the Olomouc archbishopric (NAD 1694, "nelistinná část", annual cartons of news and papers) and many estates. Gave the four keys in `key_leads.json`. |
| **theses.cz** | Search page `theses.cz/vyhledavani/?search=<terms>` works in Chrome; thesis pages and files sit behind a JavaScript SHA-256 proof-of-work page (curl gets only the script) that Chrome passes in a second. After that, `fetch()` from the thesis page reads the PDF and zip into memory: PDFs were read with pdf.js (`cdnjs ... pdf.js/4.0.379/pdf.min.mjs` imported into the page), the appendix zip with JSZip 3.10.1, and the photographs were drawn on a canvas in the tab and looked at with screenshots and zoom. Nothing was saved to disk. | The route that produced the Piccolomini rows. |
| Charles University thesis (Dolejší 2017, hdl 20.500.11956/91542) | `dspace.cuni.cz` and its mirror `dodo.is.cuni.cz` fail in Chrome as well as from scripts (the navigation ends on a Chrome error page: connection reset from this network). NUSL (`invenio.nusl.cz/record/368292`) has the record but "No fulltext". `core.ac.uk/works/192177705` holds at a Cloudflare challenge that did not clear by itself; `api.core.ac.uk` errors. SIS (`is.cuni.cz/webapps/zzp/`) answers 404. | **Not obtained**, so no Gallas item could be picked. Next: another network, or ask the author/library for the PDF. |

## Searched (hit counts)

- **Litoměřice**: šifr 23 (1873-1962 district telegrams; Becher's 1661 printed universal-character book in the bishopric library, inv. 4908, not a cipher), šifrovan 7, šifrovaně 1, dešifr 10, Ziffer 16 (surname, maps); chiffr, Chiffre, chiffriert, cifra, tajné písmo, Geheimschrift 0.
- **Třeboň DigiArchiv** (all record types): šifr* 50 (library books, "Sifrid" genealogies, a 20th-c. personal fond), šifrovan* 6 and šifrovaně 1 (library: includes Roubík 1931 on Wallenstein's ciphered letters), dešifr* 1 (Figl 1926), chiffr* 1, Ziffer* 20 (maps, surnames), tajným písmem 10 and kryptogra* 20 (noise), tajné písmo (OR search, noise); Chiffre*, šifrový, cifre, Geheimschrift, cifrato, chiffré, nomenklátor, zifra, Zifern 0. No early modern item record with a cipher.
- **Opava**: šifr 81 (all 19th-20th c. except the four keys and medieval "Sifridi" charters), šifrovan 34, šifrovaně 10, dešifr 7, chiffr 3, Chiffre 2, cifra 4, tajné písmo 4, Geheimschrift 1, Ziffer 110 (surnames), šifrovací klíč 18, zašifr 2, cifrou 1; šifrách, ciframi, chiffres, tajným písmem, kryptografick, "klíč k šifře", "číselná šifra", kryptogra, zifra, cifre, Chiffern 0. Gallas 527, Piccolomini 17, Wallenstein: no cipher item.
- **theses.cz** "šifrovaná korespondence" (976 hits, first page read): Vlnas 2017 (Piccolomini, below); Rajlichová 2011 (Pardubice; Ottavio and Francesco Piccolomini 1650-56, "v šifrované korespondenci Francesca a Ottavia"; full text only in the Pardubice repository, not reached); Pěnkava 2024 and Zelený 2021/2026 (Verdugo, citing J. Mírka, "Raně novověká šifrovaná korespondence ve fondech šlechtických rodinných archivů", Západočeské archivy 2012, pp. 44-73: the SOA Plzeň items already in `sweep_2026-11_czech_slovak`); Staněk 2026 (Rožmberk citation, row 6).

## Piccolomini microfilm frames (Vlnas 2017)

V. Vlnas, *Počítačová analýza šifrované korespondence rodu Piccolomini* (BA thesis, Univerzita Hradec Králové 2017,
theses.cz/id/p3p2kb). He searched the RA Piccolomini finding aids at SOA Zámrsk (the archive first told him there were
no ciphers), then found over 20 cipher frames on one microfilm and about 40 on a second, and says more microfilms
certainly hold more ("24 mikrofilmů jsou desítky"). He deciphered four (inv. 25039 French grid cipher; 24873 vowels
= odd digits; 24790 Claudia de' Medici's sign substitution; 25106) and photographed 76 more frames, left
undeciphered (appendix B), all from inventory numbers 24784-25115 and, where dated, 1646. All 90 photographs in his
zip were looked at (6 Nov 2026):

- **Glossed** (contemporary decipherment between the lines or in the margin; not rows, they are the key material):
  24784, 24786-24789, 24790, 24794, 24796, 24799 (+_1), 24806 (Claudia de' Medici, Innsbruck 1646); 24852, 24853
  (+_1, _2) (writer with enciphered signature); 24880 (+_1, _2); 24922; 25026 (troop list, 8 Feb 1646); 25039
  (margin); 25040; 25063, 25065, 25067 (+_1, _2), 25069 (+_1) (Spanish, Frankenthal 1646); 25076 (+_1, _2; glosses
  faint on the first page); 25077; 25079 (+_1, _2); 25080 (+_1-_3, margin); 25081 (+_1-_5, margin); 25082 (+_1-_3);
  25085; 25089 (+_1); 25090 (+_1-_3); 25091 (+_1-_3); 25093 (+_1, _2); 25099 (+_1, _2); 25104 (+_1, _2); 25115
  (+_1, _2).
- **Bare** (rows): 24793 and 24800 (Claudia de' Medici); 24854; 25071 (Frankenthal); 25054; 24874 and 24876
  (vowel-digit cipher, key printed by Vlnas).
- Not a cipher page: 24806_1 (blank verso with the archive label).

The frames are phone photographs of a microfilm reader screen, rotated 90°, legible at zoom. Every frame carries the
label "inv. č. <n> 31/2". The rest of the Piccolomini cipher correspondence (other microfilms, Vlnas's "dozens") is
unsurveyed: the next step is a visit or a scan order at SOA Zámrsk, starting from the microfilm that holds inv.
24784-25115.

## Key leads (`key_leads.json`, not rows)

ZA Opava, Arcibiskupství Olomouc: inv. 293 (German key by persons and places, /1640/), karton 105 ("Šifrovací klíče",
1679, with Polish and Upper Hungarian news), karton 114 ("2 šifrovací klíče", Feb 1683, with the Lisola and Tököly
papers). ZA Opava, Velkostatek Deštné inv. 140 ("Dešifrovací klíč, franc.", /1740/). No images online for any.

## Literature leads (not rows)

- Rajlichová 2011 (Pardubice BA thesis): ciphered letters of Francesco Piccolomini to Ottavio, 1650-56, RA
  Piccolomini; whether glossed or deciphered is not known (full text not reached).
- Dolejší 2017 (Charles University): list of every ciphered document of the Gallas war chancery; still not obtained.

## Not reached / left

- SOA Litoměřice: the Clam-Gallas and Thun family archives are not online at item or finding-aid level; the Gallas
  chancery needs the Dolejší list and an order to SOA Litoměřice (pobočka Děčín).
- SOA Třeboň: the scanned finding aids (Historica Třeboň, RA Schwarzenberg, RA Buquoy, Cizí rody) would be an OCR
  target like the Acta Clementina ones, if they can be displayed (registration may be needed; not attempted).
- katalog.soalitomerice.cz is the archive library's catalogue (VuFind), not searched.
