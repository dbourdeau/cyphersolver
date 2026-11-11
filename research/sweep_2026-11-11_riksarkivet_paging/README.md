# Riksarkivet, full paging of Oxenstierna's letters to the regency and the unviewed volumes (11 Nov 2026, cloud session)

Source key `riksarkivet_paging`. Continues `research/sweep_2026-11-11_riksarkivet_papers/`. **Result: 1 row in
`candidates.json`, no vetting block, none open.** No bare, unread cipher was found. Working notes, in viewing order: `notes.md`.

## Routes

- Images as before: `lbiiif.riksarkivet.se/arkis!<series>_<nnnnn>/full/900,/0/default.jpg` with the sok.riksarkivet.se
  Referer, about 1.2 s an image, no bot check. `pct:` region requests return 501: fetch `full/max` and crop locally.
- **Blocked:** the Oxenstierna database search (`sok.riksarkivet.se/oxenstierna?...`, the AOSB text editions) redirects
  to `/captcha`. Not pursued. The static pages of the project open.
- archive.org full text: four AOSB volumes and the Handlingar rörande Skandinaviens historia (HSH) register opened.
  HSH del 30 (which prints the one letter that matters) is not among the archive.org copies found. runeberg.org has no AOSB.
- DECODE `RecordsList?search=`: "1133.08", "Skrivelser", "konungen" 0 records; "Oxenstierna" 20 (Oxenstiernska samlingen,
  Rusdorff 1628, Wandersleben 1637, Chifferklaver keys), none from Skrivelser till konungen.

## 1. Skrivelser till konungen SE/RA/1133/1133.08/7-16, every image

All 3,393 images of the ten volumes were downloaded at 900 px (`dl.py`) and screened. Method: `digi.py` finds on each
image the 200x120 px window with the most isolated digit-sized glyphs; `dz.py` puts that window of every image, at
native scale, on sheets of 64, and every sheet was viewed. Volume 7 was also viewed whole-page (`page.py`). Each suspect
was then opened at 2000 px (`cz.py`, `hi.py`). Limit of the method: a short cipher passage away from the densest digit
area of a spread, or one that scores below ordinary script, could be missed; a full leaf of cipher could not.

Image numbers are those of the R-series viewer (`sok.riksarkivet.se/bildvisning/<series>_<nnnnn>`).

| Vol. | Series, images | Cipher, struck through and/or deciphered above (read) | Cipher with no decipherment on the passage |
|---|---|---|---|
| 7 (14/11 1632-25/3 1633) | R0001372, 317 | 204, 205, 207 (letter of 2 Mar 1633, marked as printed in HSH 25: 170) | none (59 is an inked-out clear passage) |
| 8 (26/3-24/5 1633) | R0001373, 289 | 5, 6, 7 | none |
| 9 (1/6-26/11 1633) | R0001374, 258 | 58, 59, 66, 67, 68, 70, 71, 196 | **31-32** (fol. 1208-1210): unglossed, but images 33-34 are the chancery's clear fair copy of the same letter, headed "Tryckt i Skand. Handl. del 26 p. 120". Read. |
| 10 (2/12 1633-1/3 1634) | R0001375, 295 | 62, 63, 64, 71, 72, 73, 75, 76, 246, 247 | none |
| 11 (29/3-2/6 1634) | R0001376, 333 | 57, 58 | none |
| 12 (20/6-6/12 1634, damp) | R0001377, 328 | 125, 308, 313, 314, 319-324; 325 (cancelled as a block, decipherment in the margin) | **129-130** (fol. 713-714, 30 July 1634): four passages, digits not struck, gloss mostly washed out. The candidate row. |
| 13 (13/12 1634-4/8 1635) | R0001378, 402 | 29-34, 37-39, 42, 146, 148, 187, 188, 191, 198, 199, 213, 214, 318, 319, 321; 4 (cancelled as a block, decipherment in the margin) | none |
| 14 (10/8-20/11 1635) | R0001379, 397 | none seen | none |
| 15 (11/12 1635-24/2 1636) | R0001380, 381 | none seen | none |
| 16 (25/2-30/5 1636) | R0001381, 393 | none seen | none |

The leaves in column 3 were judged from a 760x420 px window at 2000 px each, not transcribed; neighbours of a listed
image may carry a few more cipher lines. They are a large matched cipher/plaintext corpus for Oxenstierna's code of 1633-35.

## 2. Sheeted volumes now viewed (sample images, 12 or 24 a volume, low resolution: about 330 px a spread)

No cipher in any. A sample of this size only excludes volumes where cipher is common.

| Volume | Series (images) | Sample images viewed | Seen |
|---|---|---|---|
| Karl XIV Johan K 1058 "Papiers secrets" | A0076371 (346) | 24, images 2-332 (520 px tiles) | clear French copies and translations of despatches 1812-13 |
| K 1020 | A0076333 (294) | 24, 2-282 | clear royal letters |
| K 1033 | A0076346 (511) | 24, 2-490 | clear French/German letters |
| K 1041 | A0076354 (306) | 12, 2-141 | accounts, letters |
| Reuterholm E 5134, E 5137, E 5138, E 5139, E 5141 | R0003396 (246), R0003399 (581), R0003400 (464), R0003401 (580), R0003403 (339) | 12 each, spread over the volume | Piranesi's Italian letters, clear |
| C. F. Scheffer 001/I-VI | 40008907-40008912 | 24 each | patents, French and Swedish letters, clear |
| Ulrik Scheffer 002/16 | 40008926 (507) | 12, 254-486 | Swedish drafts |
| De la Gardie E 1330 | R7000027 (394) | 24, 2-378 | German/French letters, clear |
| Azzolino K 413, K 420 | R0003475 (307), R0003796 (571) | 24 each | Italian drafts, French letters, clear |
| 1133.07/6, /14, /25; 1133.08/2 | R0000781, R0000794, R0002220, R0001367 | 12 each | clear Swedish/German |

Sheets that exist in scratch but were **not** viewed in this pass: K 1042-1047, UD Berlin 1821-22 and Copenhagen 1836-37 / 1848,
Lovisa Ulrika K 261 and K 263, Christina K 93, K 94, K 97, Ericsberg vols 284-288, K 1035, Ulrik Scheffer 002/5 and 002/9.
E 5140 (R0003402) was never sheeted.

## 3. Stedingk and Ericsberg (resolved in `units.json`, 21 more units; log `resolve2.log`, `sheets3.log`)

| Volume | Series (images) | Viewed | Seen |
|---|---|---|---|
| Stedingk E 6588 Depescher 1790-91 | 90003434 (293) | 12, 2-135 | Stedingk's French drafts, several headed "chiffre" / "apostille chiffre": the clear drafts of what was sent in cipher |
| E 6589 Depescher 1792 | 90003435 (221) | 24, 2-212 | the same, clear drafts |
| E 6600 Depescher 1803-04 | 90003446 (428) | 24, 2-410 | the same |
| E 6700 Petersburg papers | 90003391 (419) | 24, 2-402 | clear copies and tables (image 367, a table headed "Signe", not looked at closely) |
| E 6628 letters Narichkin-Quillfelt | 90003530 (486) | 24, 2-466 | clear letters, print |
| Ericsberg autographs vol. 246, 250, 256 | A0040327 (405), A0040331 (270), A0040337 (368) | 24 each | single autographs with index cards, 18th-20th c., clear (microfilm) |

Resolved and sheeted but not viewed: Stedingk E 6595, E 6634, E 6706; Ericsberg vols 42, 162, 264, 270, 279.
Resolved, not sheeted: E 6585, E 6622, E 6626, E 6630, E 6632. The Stedingk archive holds the drafts, so the enciphered
originals of his despatches are to be looked for in Diplomatica Muscovitica, not here.

## Excluded

- Every glossed leaf in section 1 (read at the time). The previous pass's row for 1133.08/10 images 246-247 stays as it is.
- 1133.08/9 images 31-32: read, the clear fair copy is bound next to it.

## What remains

- HSH del 30 p. 91 and AOSB I:12 for the letter of 30 July 1634: this settles the one row.
- The unviewed and unsheeted volumes named above; the eight `1133.07` units with no images through `info.json`.
- Ericsberg: 311 autograph volumes not sampled (low yield expected: collected single autographs).

Scripts: `rik.py` (copied), `dl.py`, `digi.py`, `dz.py`, `cz.py`, `hi.py`, `page.py`, `zoom.py`, `dlall.sh`, `run3.sh`.
