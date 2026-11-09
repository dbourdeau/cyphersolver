# Austrian and German state portals (9 Nov 2026)

Result: **6 candidate rows** (`candidates.json`, built by `make_candidates.py`) and 3 key-lead bundles (`key_leads.json`).
Two rows were viewed on images (class A); four are scored from the finding aid.

## Routes that worked

| Portal | Route | Result |
|---|---|---|
| Sächsisches Staatsarchiv (archiv.sachsen.de) | `https://www.archiv.sachsen.de/cps/suche.html?q=<term>&offset=N&pagesize=10` (plain GET, server-rendered, pagesize is forced to 10; `sax_harvest.py`) | 19 terms; chiffriert/-e/-en/-er 26 each, Chiffre/Chiffren 56, Geheimschrift 23, dechiffriert 6, verschlüsselt 9, "Ziffern" 318 (not paged, numerals). 113 unique records. Nearly everything already held through Archivportal-D (Knorre 1462-63, Flemming, Beichlingen, Breinl 1749 = catalogue 595, Loc. 02974/09 = catalogue). New: Sackens 1773 (one row) and the Saxon "Chiffres" key volumes (key_leads). Only unrestricted records are online (about half). Camera icon marks scans: none of the cipher items had one. |
| Landesarchiv NRW and all NRW archives (archive.nrw.de) | The portal's own JSON API: `https://www.archive.nrw.de/sufservice/api/search?keyword=<term>&size=50&page=N` (no key, no bot check; `nrw_harvest.py`). The `keyword` parameter is the only one that filters (`q`, `term` return the whole index of 9.9 M records). Hits carry `disitalisat` DFG-Viewer links. | 22 terms: chiffriert 44, chiffrierte 9, Chiffre 18, Chiffren 11, Geheimschrift 12, dechiffriert 5, Dechiffrierung 4, Chiffrierung 5, Chiffrenschlüssel 8, verschlüsselt 27, "in/mit Ziffern" about 130 each (filtered to cipher words), others 0-2. 147 unique records after the filter. Most state-archive items were already in the repo (Velen U 132, Plettenberg B 001, Heinsberg AA 0582, Jülich-Berg AA 0031, Lucchesini V 061, Nathan von Dortmund L 74). New items come from the non-state holdings of the Vereinigte Westfälische Adelsarchive and local archives, which Archivportal-D does not carry. |
| LWL digitised files (`lwl.org/325dig-download/Lesesaal-Digitalisate/...`) | `mets.xml` lists the jpg URLs; plain GET, no check | Viewed Ber.A M 20 (leaves 003, 010, 030), Cap.C.I S 1199,11 (001, 002), S 1230,04 (001, 002) |

The NRW API makes a full cipher-term sweep of 9.9 M records cheap. Not yet run: Latin and French terms (cifra 1 hit, chiffré 0), "Geheimschrift" variants beyond the list, and a date-filtered pass over "verschlüsselt" (27 hits read only as lines).

## Viewed

- **Ber.A M 20** (Berleburg archive, "Pariser Korrespondenz mehrteils in Chiffren"): leaf 010 holds a three-digit number cipher at the end of a German paragraph; leaves 003 and 030 are plain French political reports. 234 images.
- **Cap.C.I S 1199,11** (Niebuhr to Stein, 11 Nov 1808): leaf 001 is two German lines then about 17 lines of numbers (up to about 3100), no plaintext between them.
- **Cap.C.I S 1230,04** (Prince Wilhelm of Prussia to Stein, Paris, 24 Jan 1808): four-digit code with French plaintext written between the number lines, so already read; it is a crib source for the Niebuhr letter, not a row. S 1116,1 (Goltz) and S 1230,08 (Humboldt) are catalogued "dechiffriert".

## Blocked or not reached

- **Steiermärkisches Landesarchiv** (`egov.stmk.gv.at/archivinformationssystem/`, JSF "ArchivIS-Web"): curl gets a TSPD bot page; in Chrome the full-text form works (`imdasWebFormId:searchVolltextFieldId`, submit button `imdasWebFormId:sucheVolltextFormSubmit`) and "chiffriert" gave no hits. Other terms not run (a same-origin fetch POST lost the ViewState; a second attempt needs the form clicked each time).
- **Thüringen** (archive-thueringen.de), **Sachsen-Anhalt**, **Mecklenburg**, **Hamburg**, **Schleswig-Holstein**, **Saarland**: the hostnames I guessed did not resolve from this network (not a bot check; the right hostnames were not found). Their holdings are partly in Archivportal-D, already swept.
- **BLHA Brandenburg** (`blha-recherche.brandenburg.de`): loads (Angular app), API not found. **Landesarchiv Berlin, Bremen**: front pages load, no search route tried.
- **Oberösterreichisches, Tiroler, Salzburger, Kärntner, Vorarlberger Landesarchiv, WAIS Vienna**: front pages only; no searchable finding-aid route found in the time spent (OÖ: "Recherche im Archiv" pages are guidance, Tirol URL 404). Not searched.
- **HandschriftenPortal**: front page loads (200); not searched (medieval manuscripts, unlikely to hold letters).

## Excluded

Key-only items (Saxon Chiffres volumes, Hin.A.Ak 676 and 2346, Lucchesini key AA 0606a 311), items already deciphered ("dechiffriert", interlinear: Cap.C.I S 1116,1, S 1230,04, S 1230,08, Lucchesini V 061 127), Saxon "Wackerbarth 1735 dechiffrierte Briefe", 19th-20th-century military and police Geheimschrift administration, newspaper "Chiffre-Anzeigen", art and exhibition "Chiffre" (metaphor), Telchi telephone ciphers, and everything already in the repo by `known.py` (Velen, Plettenberg, Heinsberg 1469, Jülich-Berg, Lucchesini, Nathan von Dortmund, Loc. 02974/09, Breinl 1749, Knorre).

## What remains

- A second NRW pass with other cipher words and a read of the 27 "verschlüsselt" and the "in Ziffern" hits that carry cipher words only in the abstract.
- Page all of Ber.A M 20 for key sheets; read the rest of Cap.C.I 1808 letters (S 1199-S 1250) for further numeric letters and for the code's key.
- Austrian Landesarchive via Chrome (Steiermark form works), Thüringen and Brandenburg portals with the right hosts.
