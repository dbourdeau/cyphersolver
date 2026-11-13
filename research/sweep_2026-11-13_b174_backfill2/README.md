# Backfill sweep 2, 13 Nov 2026 (b174)

Second cloud pass to replace solved items with vetted new leads, after b169 (`sweep_2026-11-13_b169_backfill`, 12 rows).
Plain curl only, default user agent, no logins, no browser. Page images were held in scratch and deleted; none are in the repo.
Row schema as in `research/archive_sweep_2026-10/BRIEF.md`, with a `vetting` block and at least three `searches`.

## Result

1 row in `candidates.json`, verdict `open`. No `id` (assigned at merge). The target was 15+; it was not met.

| Archive | Rows | cls A | cls B | cls C |
|---|---|---|---|---|
| ASF Mediceo avanti il Principato, filza XLIV | 1 | 0 | 0 | 1 |
| Total | 1 | 0 | 0 | 1 |

- MAP XLIV doc. 21: Puccio Pucci to Cosimo de' Medici at Ferrara, 21 Feb 1437/8, with copies of Neri di Gino Capponi's
  letters of Oct 1437. About 20 cipher words in invented signs and code numbers inside clear text. Bare.

Gate check (`scripts/build_check.py`, own re-implementation of the `_check_catalogue.py` rules; repo script not run): `result: pass`.

## Why so few

The MAP filze assigned to this pass are dominated by letters whose cipher is **glossed between the lines** by the
recipient's chancery (Lorenzo's secretaries, or Lanfredini in Rome). A glossed letter is read, so it is not a lead.
Every cipher page that was opened at native size in XXXIX, XL, XLII, LVII and LVIII carried an interlinear decipherment.
LIX's bare cipher letters are all Lorenzo's own letters to Lanfredini (1488). These are covered by the Lettere di Lorenzo
edition, which is not online, so they cannot be vetted.

## Routes

- ASF MAP viewer `/map/ricerca/ricerca-su-filza/?f=F&d=D&c=` answers 302 to `/map/riproduzione/?id=N` (200). The viewer page
  lists every image (doc / carta / side), parsed by `scripts/labels.py`.
- ASF IIIF / IIP `iipsrv.fcgi?FIF=/data/iip-data/asfi/mediceo_avanti_principato/001000FF/A0000NNN.ptif&WID=1272&CVT=jpeg`: 200.
- The paging pipeline was `scripts/page.sh`: 3 parallel plain curls. It runs the b169 detector `det4.py` (b169 sweep scripts) and then the b169
  `sheet.py`, which makes 400 px sheets of the top-ranked pages. Candidate pages were then cut into native-width bands
  (`scripts/stack.py`, `scripts/crop.py`, `scripts/strip.py`) to check for glosses.
- Rigsarkivet image list `api.rigsarkivet.dk/ao/v1/billedviser/billed-reference-lister?bsid=274999` and `/ao/v1/images/<id>`: 200
  (`scripts/rasheet.py`, 4x4 sheets at 300 px).
- Rigsarkivet search API (JSON POST, b169 `srch.py`): ziffer 2 hits, chiffreskrift 0, dechiffrering 2 (1798 keys, 1940s
  telegrams), cifre 2,169 (noise from "fire-cifrede" etc.). No new pre-1800 cipher unit.
- DECODE `de-crypt.org/decrypt-web/RecordsList?search=`: 200 (Lanfredini 0, Puccio 0, Capponi 0, 1437/1438 no Florentine record).
- Tomokiyo `cryptiana.web.fc2.com/code/italian.htm`: 200 (https; http gives 302).
- Gutenberg 74973 (Ross, Lives of the Early Medici, 1910): 200, full text grepped.
- dspace.ut.ee (Vito 2025 PDF): connection reset again; not retried, no other route tried.
- litbit.ru copy of Ross: JavaScript bot check; not retried (Gutenberg text came from a separate search result).

## Filze paged (image counts from the viewer pages) and what was viewed

| Filza | Images | Viewed | Finding |
|---|---|---|---|
| XXXIX | 1,340 | top 32 + native crops | cipher on 10 pages, all glossed (incl. slip doc. 453, 28 Feb 1486) |
| XL | 1,054 | top 32 + native crops | cipher on 7 pages, all glossed |
| XLII | 576 | top 24 + native crops | cipher on 4 pages, all glossed |
| XLIV | 130 | top 8 by chain sum + 16 by longest chain | **doc. 21 bare (lead)** |
| XLV | 807 | top 24 | no cipher seen (princes' letters) |
| XLVII | 978 | top 24 | no cipher seen (princes' letters) |
| LIV | 503 | top 24 | no cipher seen |
| LVI | 315 | top 16 | no cipher seen |
| LVII | 458 | top 32 + native crops | Lanfredini's in-letters: cipher on 10 pages, all glossed |
| LVIII | 384 | top 24 + native crops | cipher on 12 pages, all glossed |
| LIX | 679 | top 32 + native crops | 7 glossed; 4 bare but all Lorenzo's own letters (excluded, below) |
| LXI | 329 | top 16 | no cipher seen |

Image total: 1,340 + 1,054 + 576 + 130 + 807 + 978 + 503 + 315 + 458 + 384 + 679 + 329 = 7,553.

## Excluded after checking (not in candidates)

- MAP LIX doc. 69 (cc. 76bis-77bis; Lorenzo to Lanfredini, Florence, Nov 1488), doc. 132 (c. 142v; Mar 1488), doc. 173
  (c. 183r; Jun 1488), doc. 189 (c. 199r; Jul 1488). The cipher passages look bare, but each letter is Lorenzo's own. The
  Lettere di Lorenzo volumes for 1488 would cover them and were not opened (not online). Under the vetting rule there is
  no vetting block. Recommend a paper check of the Lettere notes before filing these as leads.
- MAP LVII pos 23, 115, 131, 141, 155, 177, 215, 216, 277, 316: glossed between the lines (Lanfredini's decipherments).
- MAP LVIII pos 170, 179, 186, 276, 279, 288, 359, 366, 367, 373, 374, 375: glossed.
- MAP XL pos 71, 333, 499, 543, 783, 849, 850: glossed (71 and 499 faintly).
- MAP XXXIX pos 27, 65, 291, 1007, 1153-1155, 1175, 1275, 1313: glossed. The viewer image for doc. 355 (pos 795) carries an ASF
  note that a decipherment slip by Niccolò Michelozzi is attached.
- MAP XLII pos 457, 471, 510, 521: glossed.
- Nothing from b169's 12 leads or its dropped list was re-filed.

## Not done

- Pentz unit 274999 images 137-503. Sheets were fetched for 137-489 at 300 px and 137-312 were looked at. At that size,
  number cipher cannot be told from German Kurrent, so this is **not** a valid check. Images 313-503 were not viewed.
- Other Rigsarkivet TKUA units: only the search API was run (above). No unit was paged.
- Riksarkivet Diplomatica, MDZ, Gallica/openapi.bnf.fr, BAV DigiVatLib, Estense: not reached. The repo already has
  sweeps for Riksarkivet, Gallica, DigiVatLib and Modena (`research/`), so new leads there need fresh paging.
- In each filza only the detector's top 16-32 pages were viewed. Bare cipher can rank lower. Short cipher words inside
  clear text, like XLIV doc. 21, score low on this detector. MAP XLIV's other 106 images were not viewed at native size.
- Not paged by anyone as far as the repo shows (no catalogue/leads row; only stray `00100020/24/36` strings in research files,
  not checked): MAP filze of letters to Lorenzo XX-XXXVIII, XLI, XLVI, LV, LX, LXVI, LXVIII.
- Vito 2025 (HistoCrypt) could not be opened. Its Florentine polyalphabetic key may bear on 15th-c. MAP letters.
