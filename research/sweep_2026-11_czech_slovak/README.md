# Sweep: Czech lands and Slovakia (6 Nov 2026)

First sweep of the Czech archives themselves (`research/COVERAGE.md`, "Never swept"). Earlier passes
(`sweep_2026-11_hungary_czech`, `sweep_2026-11_D_east_north`) had found no Czech item: Archives Portal Europe has no
Czech cipher records, and no item-level Czech portal had been reached. This sweep found the routes.

**Result: 19 rows in `candidates.json`, 7 key-only items in `key_leads.json`** (built by `make_candidates.py`).
All rows are `seen: "catalogue"`: none of the items has digitised images in the portals (ARON reports zero digital
objects on every record), so `needs_archive_scan: "yes"` throughout. `known.py` was run on every fonds, correspondent
and shelfmark; only Lustrier is already in the repo (catalogue #1227, HHStA), and the Collalto Lustrier row is kept as a
second archive of that cipher. `key_leads.json` is separate because `merge.py` accepts only cls A/B/C.

## Routes that work

| Source | Route | Notes |
|---|---|---|
| **ARON, Moravský zemský archiv** (`www.mza.cz/aron`) | `POST https://www.mza.cz/aron/api/aron/apu/listview` with JSON `{"size":100,"offset":0,"filters":[{"field":"type","operation":"EQ","value":"ARCH_DESC"},{"operation":"FTX","value":"šifr*"}]}`; record `GET .../api/aron/apu/<uuid>`; public page `https://www.mza.cz/aron/apu/<uuid>`. **MZA's nginx answers 403 unless the request has a browser User-Agent, `Origin: https://www.mza.cz` and a `Referer`** (`aron.py` sets them). After ~60 quick detail requests the host started resetting connections from this network (rate limit); keep 1-2 s between calls. | Item level for G 140 Dietrichstein (Mikulov), G 169 Collalto (Brtnice), Laudon, Hompesch and many state fonds. The best route of the sweep. |
| **ARON, SOA Plzeň** (`aron.soaplzen.cz`) | same API (no special headers) | Item level for the West Bohemian family archives (Trauttmansdorff, Nostitz-Rieneck, Nostitz Planá, Windischgrätz, Verdugo ...). Items have a `WRITING` field; one says "šifrované písmo". |
| **ARON, SOA Zámrsk** (`aron.vychodoceskearchivy.cz`) | same API | Item level for East Bohemian family archives (Thun Choltice, Kinský, Černín-Morzin, Bubna, Valdštejn-Vartemberk, Leslie, Trauttmansdorff Litomyšl ...). Piccolomini (Náchod) and Colloredo-Mansfeld (Opočno) are **not** item-indexed. |
| **ARON, SOA Praha** (`aron.soapraha.cz`) | same API | Item level mostly for district offices: 19th-century ciphered governor's telegrams only. |
| ARON, national portal (`portal.nacr.cz/aron`) | same API; ARCH_DESC returns 0 here | Fund and finding-aid level only (fund descriptions, literature and editions fields). Found Valdštejniana (below). |
| **VadeMeCum, Národní archiv** (`vademecum.nacr.cz/vademecum`) | requests session: GET home; POST `/vademecum/SearchBean.action` with the home form's hidden `_sourcePage`, `__fp`, `searchFrom`, plus `patternFulltext=<term>`, `searchFulltext=`, `wordPosition0=1` (substring), `wordOperator0=1`; detail pages from the result's `VysledekBean.action?show=...` links in the same session; permalink `permalink?xid=<uuid>` | 277,305 inventory records (a minority of NA holdings). Scanned typescript finding aids ("Analogová pomůcka") are viewable: `Zoomify.action?entityRef=...` gives `zoomifyImgPath` + `IMAGE_PROPERTIES`; tiles at `<path>/TileGroup<g>/<tier>-<x>-<y>.jpg`; the next page is the `PaginatorMedia.action?...row=<n+1>` link. `vmc.py`, `vmc_harvest.py`, `vmc_scans.py` (tier 3, ~1240 px, OCR with Windows.Media.Ocr). |

## Searched (hit counts)

- **MZA ARON** (item level): šifr* 56, šifrovan* 30, šifrovací 16, šifrovaný 13, šifrované/šifrovaně 8 each, Ziffer* 24 (surnames), dešifr* 5, tajné písmo 4 (1924 circulars), cifra/cifry 5 (planning figures), kryptograf* 1, šifer 3, číslicemi 125 and "tajná korespondence" 113 (noise: manuscripts' numbering, 20th-c. Zbrojovka secret files); Chiffre*, chiffr*, dechiffr*, Geheimschrift, cifrato, chiffre, cipher, nomenklátor 0. Of the 56 šifr* hits, 15 are early modern (all used below); the rest are 1860s-1940s official telegrams and keys, pseudonym signatures ("pod šifrou") and surnames.
- **SOA Plzeň ARON**: šifr* 11 (6 early modern, all used), šifrovací 6, everything else 0.
- **SOA Zámrsk ARON**: šifr* 22 (19th-20th c. official telegrams, signatures "šifrou"; Seykora 1831 memoir in a number cipher), Ziffer* 2 (surname), tajné písmo 1 (1935 thieves' signs), kryptograf* 1 (Thun, [1825], "kryptografických (těsnopisných?) poznámek", probably shorthand), číslicemi 66 and "tajná korespondence" 14 (noise).
- **SOA Praha ARON**: šifr* 23, šifrovan* 20 (all 1869-1908 governor's ciphered telegrams to district offices), cifr* 1, šifer 1 (surname).
- **NA VadeMeCum**: šifr 12 (Tuscan Habsburg archive 1798-99 used; the rest 1906-1954), cifr 2 (Tuscan legation Paris 1837 "Cifra numerica", key lead), zifr 1, Ziffer 1; chiffr, Chiffre, Geheimschrift, dechiffr, decifr, dicifr, cifre, chiffré, cifrat, cipher, nomenklátor, tajné písmo, tajným písmem, "klíč k šifře", "šifrovací klíč" 0.
- **NA ARON (fund level)**: šifrované 4 (Valdštejniana NAD 189; the rest 20th c.), šifry 1, Chiffre/chiffriert/cifra 0.
- **Kramerius** (MZK `api.kramerius.mzk.cz/search/api/client/v7.0/search`, models manuscript/archive/graphic): šifr*, cifr* 0; chiffr* 2 (a map, a harp tutor). NK Kramerius API returned non-JSON.

## Best leads

1. **Rambaldo Collalto's papers (MZA G 169, 1624-1630)**: Lustrier from Constantinople, 26 pieces mostly cipher (inv. 1774; sibling of catalogue #1227);
   abbot Scaglia from Madrid/Turin, 17 mostly cipher (1775); Rossi, 66 partly cipher (1862); Eggenberg, 19 partly cipher (1719); Tilly/Gallas/
   Questenberg/Aldringen/Trauttmansdorff, 10 partly cipher (1740); Ferdinand II, one ciphered (1698); a ciphered imperial ruling on the Mantuan
   felony, 12 Feb 1630 (143); an intercepted Mantuan cipher letter to Paris, 1630 (142); and a Collalto-Harrach key with more letters (1776).
2. **Fossombroni to Marulli, 1798-99** (NA, Tuscan Habsburg archive, Ferdinand III, inv. 7, kart. 1): ciphered letters of the Tuscan foreign minister
   to his envoy at Milan, filed with the Grand Duke's cipher tables.
3. **Nostitz in Stockholm, 1685-1690**: partly ciphered reports to Dietrichstein (MZA G 140 inv. 69) and the embassy's key (SOA Plzeň, Nostitz-Rieneck
   inv. 91): ciphertext and key in two Czech archives.
4. **Saponara's cryptographic letters to FML Leslie, 1679-80** (MZA G 140 inv. 676), with their number key in the file.
5. **Lobkowitz in Paris, 1685-88** (MZA G 140 inv. 34), partly ciphered reports to Dietrichstein.
6. **Christian II of Anhalt-Bernburg to Wilhelm Verdugo, 1621-27** (SOA Plzeň, RA Verdugo inv. 13), "šifrované písmo".
7. **Ciphered letter to Metternich, 1812** (NA, Acta Clementina inv. 96, kart. 36, fol. 16-17), filed beside "Noty a šifry" (inv. 98): found by
   OCR of the scanned finding aid.

## Key leads (`key_leads.json`, not rows)

Acta Clementina: a decipherment key for the Metternich-Lieven letters, 1822 (finding aid 623, vol. IX fol. 4; the letters are largely
printed) and a list of ciphers of the Metternich-Floret correspondence (inv. 322, finding aid 1242). Collalto inv. 1887 (key of "Archduke Maximilian" with Wallenstein, and a general key); Laudon inv. 73 (Prussian key of the Silesian fortresses,
1758); Windischgrätz inv. 1403 item 5 (keys of Gottlieb, Ernst Friedrich and Leopold Viktorin Windischgrätz; check against `targets/windischgraetz1720`
and DECODE R7928); NA Tuscan legation in Paris 1837 "Cifra numerica" (inv. 56, kart. 44); NA Acta Clementina, Hudelist papers 1818, a "dešifrovací klíč"
filed with Stürmer's despatches from Constantinople (finding aid no. 621, p. 9). Trauttmansdorff inv. 148 (Dohna 1644) and Nostitz Planá inv. 306 (agents'
reports 1686-1702) each have a key attached but are kept as rows, since a correspondence file with its key implies ciphered letters.

## Literature leads (not rows: no item seen)

- **Valdštejniana (NA, NAD 189)**: the fund's literature field cites F. Roubík, "Šifrované dopisy v registratuře Albrechta z Valdštejna", *Friedrichův
  sborník* (Praha 1931), pp. 359-368: an article on the ciphered letters in Wallenstein's registry. No item-level inventory online. Many Wallenstein letters
  are printed (Hallwich, Documenta Bohemica Bellum Tricennale), so check print before treating any as open.
- **Gallas war chancery**: Charles University BA thesis (2017), "Šifrovaná korespondence v písemnostech válečné kanceláře Matyáše z Gallasu", with a list of
  every ciphered document (hdl 20.500.11956/91542; NUSL record nusl-368292); MA thesis 2024 (hdl 20.500.11956/191516) edits Ferdinand III's 1635-38 cipher
  letters to Gallas (already in `targets/ferdinand1634` and `ferdinand3` notes). dspace.cuni.cz resets from this network.
- "Raně novověká šifrovaná korespondence ve fondech šlechtických rodinných archivů Státního oblastního archivu v Plzni", *Západočeské archivy* 2012,
  pp. 44-73 (author not shown; record on mus.knihovny.cz behind a "go-away" bot check). Probably lists the SOA Plzeň items found here and more.
- Slovakia: the SAV/FEI STU group (Antal, Duchoňová, Kudzbelová, Zajac; HistoCrypt 2023) works on cipher keys in Slovak noble archives; their records are on
  HCPortal (hcportal.eu), already harvested in `research/catalogue_harvest/hcportal/index.json`, so nothing from there is repeated here.

## Blocked / needs Chrome

- SOA Litoměřice digital reading room (Clam-Gallas, Gallas war chancery, Thun-Hohenstein Děčín): `https://digi.soalitomerice.cz/` redirects to
  `/digitalnibadatelna/human/verify`. needs Chrome: https://digi.soalitomerice.cz/
- Zemský archiv v Opavě (Olomouc archbishopric, i.e. Cardinal Dietrichstein's episcopal papers): `https://digi.archives.cz/da/` answers with a Radware bot page.
  needs Chrome: https://digi.archives.cz/da/
- SOA Třeboň (Rožmberk, Schwarzenberg, Buquoy, Eggenberg Český Krumlov): `digi.ceskearchivy.cz/DA` is a JavaScript application; not scripted. needs Chrome:
  https://digi.ceskearchivy.cz/DA?lang=cs (no ARON instance found for Třeboň).
- mus.knihovny.cz (Czech historical bibliography): "go-away" bot check. dspace.cuni.cz: connection reset (network). core.ac.uk: Cloudflare.
- MZA: `www.mza.cz/a8web/` 403 (old system); `www.mza.cz` began resetting every connection from this network after a burst of ~60 ARON
  detail calls and was still doing so more than an hour later. So the fund marks were not read from ARON: "G 140" (Dietrichstein) and
  "G 169" (Collalto) in the shelfmarks are MZA's usual numbers, to be confirmed; the Laudon and Hompesch fund marks are not given. The
  "Digitalizované pomůcky" PDF list (`www.mza.cz/brno/fondove-skupiny/dig/`, digitised MZA finding aids, a route to fonds not item-indexed
  in ARON, e.g. G 436 Kaunitz) was not fetched.

## Acta Clementina finding aids (OCR pass)

The Metternich family archive (NA, NAD 611/4) has no item records in VadeMeCum, but ten of its fifteen typescript finding aids (A. Haas,
1967-68) are scanned: nos. 593, 607, 621, 622 (Gentz), 623 (Lieven), 1232 (name index), 1237, 1238, 1241, 1242, 652 pages in all.
`vmc_scans.py` stitched each page from Zoomify tier 3 (~1215 x 1700 px, six parallel tile requests, ~3 s a page), `deline3.py` blanked the
typed "=====" underlines (Windows OCR silently drops underlined lines, i.e. every item title, until they are removed), and `ocr.ps1`
(Windows.Media.Ocr, en-US, ~0.5 s a page) wrote the text. The OCR text is kept in `acta_clementina_ocr/fa_<finding aid>.txt` for later
greps (OCR renders š as ä/S/E, so grep `ifr`, not `šifr`). Hits: inv. 96 and 98 (row and note above), the Lieven key (623), the Floret
cipher list (1242, inv. 322), and the Hudelist 1818 key (621). Nothing in the Gentz or Austria political-correspondence inventories.
Images stayed in the session scratchpad.

## Left out (checked)

- MZA G 140 inv. 30 (Trautson, Madrid 1677-78): the description says Trautson was busy writing ciphered reports, not that ciphertext is in the file.
- MZA Hompesch inv. 2073, 2076 (Goldstein correspondence 1796, "Šifra 'E'", "Šifra 'K–r'"): in Czech inventories "šifra" here is a pseudonym or monogram
  of the writer (as in "List podepsaný šifrou A.C.C.", Černín-Morzin inv. 733, 1677, and "pod šifrou" for a journalist), not a cipher.
- All 1860s-1940s official ciphered telegrams, cipher-key registers of district offices and gendarmerie, Gestapo-decrypted 1941-44 radio messages (NA
  Německé státní ministerstvo inv. 391, 757, 777): modern administrative or already deciphered.
- Thun Choltice inv. 2361 ([1825], "kryptografických (těsnopisných?) poznámek"): the archivist suspects shorthand.
- Tuscan Leopold II personal correspondence with Fossombroni 1825-34 (NA 1044/3): no cipher mentioned.

## Not reached

- MZA G 436 (Kaunitz, Slavkov) and the Žerotín, Salm, Liechtenstein fonds returned no šifr* hits; whether they are item-indexed in ARON was not checked.
- Other NA scanned finding aids (Stará manipulace vols. 1-5, ~1,500 pages, a subject/place index; Staré militare; České gubernium -
  Militare 222 pages) were not OCRed; the same `vmc_scans.py` + `deline3.py` + `ocr.ps1` pipeline applies.
- Slovak archives: state-archive finding aids are PDFs on minv.sk (e.g. Košice "Rodové archívy I", 192 pp., grepped: nothing; text layer lacks
  diacritics). The SNA family archives (Pálffy, Erdődy, Zay, Révay) have no online item list found.
- Slovak National Archives: no item-level portal found (`slovenskearchivy.sk`, `archivportal.sk` do not resolve per the D sweep); Slovakiana and
  Monasterium (charters) not searched for letters.
