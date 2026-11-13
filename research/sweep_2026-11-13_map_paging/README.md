# MAP paging, letters to Lorenzo (13 Nov 2026, cloud session)

Folder `research/sweep_2026-11-13_map_paging/`. Goal: bare cipher in Archivio di Stato di Firenze, Mediceo avanti il Principato (MAP)
filze that no earlier pass paged (the b174 backfill listed XX-XXXVIII, XLI, XLVI, LV, LX, LXVI, LXVIII as unpaged).

## Result

1 row in `candidates.json`, **no vetting block** (the date lies inside the range of the Lettere di Lorenzo il Magnifico edition,
whose notes are not online). cls A.

- **MAP XXXVIII doc. 418 (old c. 428), pos 913-914, viewer id 51734**: Pierfilippo Pandolfini, Rome, to Lorenzo, 27 Mar 1482.
  Recto: about 19 lines of symbol-and-figure cipher with clear words between runs; no interlinear, marginal or foot decipherment.
  Sibling of lead 2559 (MAP LIII doc. 13, Pandolfini, Apr 1483). DECODE search "Pandolfini": no records (13 Nov 2026).

Every other cipher page opened at native size in these filze carried an interlinear (or light-ink between-the-lines) decipherment.

## Filze paged (viewer `f=` number = Roman filza, checked on page stamps; images downloaded at 1272 px)

| Filza | Images | Dates seen | Viewed | Finding |
|---|---|---|---|---|
| XXX | 2,179 | 1473-75 | top 16 | no cipher |
| XXXI | 775 | 1473-78 | top 16 | no cipher |
| XXXII | 1,218 | 1475-77 | top 16 | no cipher |
| XXXIII | 2,164 | 1474-76 | top 16 | no cipher |
| XXXIV | 1,219 | 1475-77 | top 16 | pos 577 (1477 Jan) cipher, interlinear glosses: read |
| XXXV | 1,985 | 1477 | top 16 | no cipher |
| XXXVI | 2,883 | 1478-79 | top 24 | no cipher |
| XXXVII | 1,401 | 1479 | top 24 | no cipher |
| XXXVIII | 1,176 | 1480-86 | top 36 | **pos 913 bare (row)**; pos 227 (doc. 104, Rome) glossed interlinear; 735 clear |
| XLI | 1,216 | 1489-90, Naples | top 16 | pos 1147, 1091, 1038 cipher with interlinear glosses |
| XLVI | 1,170 | cardinals' letters | top 16 | no cipher |
| LV | 650 | 1485-94 | top 16 | pos 84 (doc. 41, Vettori, Jan 1485) and 189 (doc. 73): glossed |
| LX | 1,365 | 1490s | top 16 | pos 168, 12, 2: interlinear glosses |
| LXVIII | 1,403 | 1466-1520s | top 16 | pos 154 glossed; 140 is a 1466 arbitration text |

Total 21,000+ images fetched, about 4,700 pages looked at in 400 px sheets (top by detector), roughly 75 opened at native size.
Not done: XX-XXIX (1470-74 and older), LXVI, early-1500s filze (LXXVI onward, CVII-CXIX): the time ran out; the sommario numbering
used to date them was unreliable after item 64, so no dating of those was attempted.

## Method and limits

- Route: `.../map/ricerca/ricerca-su-filza/?f=N&d=1&c=` lists every image (label parsed with b174 `labels.py`);
  IIIF `iipsrv.fcgi?FIF=/data/iip-data/asfi/mediceo_avanti_principato/00100NNN/A0000PPP.ptif&WID=1272&CVT=jpeg`, 4 parallel curls, about 3 images/s,
  no block or throttle seen. The `det4.py`/`sheet.py` of b169/b174 are not in the repo, so `scripts/det.py` (small isolated glyph
  count), `scripts/det2.py` (runs of small similar glyphs), `scripts/combo.py` (contact sheet: top 8 by det + top 8 by det2) and
  `scripts/page.sh` were written here.
- **The detector ranks dense handwriting as high as cipher.** It finds full-page cipher (tested on MAP XLVIII 143, LXXV 131, XLIV 43) but
  misses short sign runs inside clear lines (LXXII 171/172 not found). Only the top 16-36 pages per filza were viewed, so short or
  low-ranked bare passages can be missed. XXXVIII pos 913 ranked 9th of 1,176 by det and about 4th by det2.
- Glossed means decipherment between the lines, over the groups, or on a slip: not a lead (brief).
- DECODE `de-crypt.org/decrypt-web/RecordsList?search=Pandolfini`: 200, "No records found". `known.py` on the shelfmark: no hit; on "Pierfilippo Pandolfini": only lead 2559.
- Printed edition: Lettere di Lorenzo il Magnifico covers 1460-92 and its notes are not online, so row 1 is left unvetted.
- Blocked or untried here: nothing blocked; Gallica etc. not needed.

## What remains

MAP XX-XXIX, LXVI and the early-1500s filze; deeper ranks (beyond the top 16-36) of every filza above; a hand check of the
Lettere di Lorenzo notes for 27 Mar 1482 before the row is vetted.
