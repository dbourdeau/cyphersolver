# ASF MAP whole-filza paging (6 Nov 2026)

Continues `research/sweep_2026-11_asf_florence/` and `_2/` (routes there). The MAP printed inventory misses most cipher, so
whole filze were paged leaf by leaf, rectos and versos. curl only, no browser. Images are in the session scratchpad
(`asf3/`) and are not committed.

`make_candidates.py` writes two files. `candidates.json` has 16 rows (A/B/C, merge fields checked; all `seen: image`).
`keys.json` has 5 key-source items (cls K, kept apart because `merge.py` accepts only A/B/C). `paging_flags.tsv` is the raw
per-page flag list from the paging (436 lines: filza, image position, doc, kind, note). The image id is the filza's
first id + position - 1, with the first ids listed in `make_candidates.py` `FIRST`. Leads and catalogue items 2307-2312,
2320-2324 and 2350-2353, and the rows of the two earlier ASF passes, are not repeated.

## Method
- Image route: as in the earlier passes. `/map/ricerca/ricerca-su-filza/?f=<filza>&d=1&c=` lists every image of a filza
  (`rip_<id>` + "doc. N r/v"). IIIF is at `/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/001000FF/A0000NNN.ptif`
  (NNN = image position). The server maximum is about 1228-1465 px wide.
- Downloaded every page at 800 px, about 1 request a second: 6,566 images in all. That is LXXII 946, LXXIII 1059,
  LXXIV 530, LXXV 468, XLVIII 903 and CXXXVII 1941; the last was stopped after position 1941.
- Contact sheets: 4 pages side by side, each about 390 px wide and contrast-stretched. At this size, sign runs inside a clear
  line were recognisable on known test pages (LXXII 177, 189, 196).
- The sheets were viewed by paging agents, at most two at a time, each writing its flags after every sheet. They opened the
  800-px original of any doubtful page.
- Every row was then opened at the server maximum and cropped, unless its status says otherwise. Neighbouring docs were checked
  for a filed clear text.
- An automatic ink test first set aside 237 pages as blank. A spot check showed that many of them were faint text, so all 237
  were paged as well. Four were show-through of cipher rectos that had already been flagged; none added a row.
- Limits:
  - A single short cipher group inside a dense clear line can still be missed at sheet size. The agents say so for
    Niccolini (LXXIV) and Pandolfini 1484 (XLVIII 17-53).
  - Glossed letters were not checked line by line for unglossed runs.

| Filza | Content (dates seen) | Pages paged | Flags |
|---|---|---|---|
| LXXII docs 1-159 | Piero di Lorenzo's agents 1492-94, Michelozzi, 1512-17 letters | 376 | 16 |
| LXXII docs 241-444 | 1460s-90s letters, Lorenzo's letters to his orators, Pandolfini embassy 1514-15 | 556 (1 image missing: pos 1100) | 108 |
| LXXIII (all) | Piero di Lorenzo 1491-94; Rome 1481-82; Naples 1491 | 1059 | 21 |
| LXXIV (all) | Niccolini Milan 1492-93; Alamanni, Ridolfi Milan 1493-94 | 530 | 77 |
| LXXV (all) | French embassy 1493-94 (Vespucci/Capponi, della Casa, Sassetti) | 468 | 43 |
| XLVIII (all) | Rucellai Milan 1482-85; T. Soderini Milan 1477, 1481; J. Guicciardini Ferrara 1483 | 903 | 139 |
| CXXXVII pos 1-1216 (docs 1-570) | 15th-c. miscellany, 1440s-1490s | 1216 | 23 |

## Rows (candidates.json)

| Shelfmark (MAP) | Date | Correspondent | cls | Gloss | Image ids |
|---|---|---|---|---|---|
| CXXXVII 40 | 19 Mar 1443 or 1447 | family letter (Tornabuoni, Benedetto, Albertaccio named) | B | bare: short digit-like runs (z3z3z4z3 ...) | 132599-600 |
| XLVIII 11-15 | Jun-Jul 1477 | Tommaso Soderini, Milan -> Lorenzo | C | unsure whether cipher at all (words in Latin letters that mostly do not read) | 59537-46 |
| XLVIII 63 | Aug 1481 | Tommaso Soderini, Milan -> Lorenzo | A | bare: full page plus postscript, about 1,500 symbols | 59657-58 |
| XLVIII 101, 158, 188, 189, 191, 196, 199 | 1482-83 | Bernardo Rucellai, Milan | A | bare pieces; about 60 glossed siblings and 4 decipherment pairs in the filza | 59749-50, 59909, 59981-92, 60011, 60017-18 |
| LXXII 403 | 20 Aug 1486 | Lorenzo -> Baccio Ugolini (copy, his hand, "Abram") | C | bare: about 6 code signs; key sheet LXXII 181 | 80136-37 |
| CXXXVII 504 | c. 1488-89 | Lorenzo -> Giovanni Lanfredini, Rome (minute) | A | bare: about 14 runs | 133573-76 |
| LXXIV 42, 49, 81, 90 | Aug 1492 - Jan 1493 | Angelo Niccolini, Pavia/Milan | B | bare short passages; glossed siblings | 81477, 81503, 81651, 81697 |
| LXXIV 96 | 25? Apr 1494 | Piero Alamanni, Milan | A | bare: about 25 lines | 81733-36 |
| LXXIV 112, 113, 115 | 16-30 Oct 1494 | Giovan Battista Ridolfi, Milan | A | bare; 11 glossed siblings | 81807-12, 81819 |
| LXXV 50 v | 26 Apr 1494 | Vespucci and Capponi, en route to France | B | bare 4-line postscript | 81955-56 |
| LXXV 106 | 1493 | unsigned slip (French embassy?) | B | bare: figure code; 110 possibly its clear text, not matched | 82151-52, 82161 |
| LXXV 15 | June 1494 | Cosimo Sassetti | C | bare 2 lines; glossed 14, 17 | 81858 |
| LXXII 77 | 4 Oct 1494 | Bernardo Dovizi da Bibbiena, camp in Romagna -> Piero de' Medici | B | bare names in signs; glossed key LXXII 81 | 79280-89 |
| LXXIII 3 | 1494 | "Iacobo ...", Rome | C | unsure (dot-separated words in Latin letters) | 80240-41 |
| LXXII 130, 140 | 7 Mar 1512, 6 Jun 1513 | Antonio Maria Bonanni, Piacenza -> ser Giovanni da Poppi | B | bare (superscript index figures) | 79426-27, 79446-47 |
| LXXII 297, 307, 309, 310, 311, 322, 333 | 1514-15 | Francesco Pandolfini, Paris | A | no decipherment identified; about 15 pairs of the same system in the filza | 79828-29, 79856-57, 79864-73, 79910-11, 79946-49 |

Fourteen of the sixteen rows are before 1500. CXXXVII 40 (1443/1447) is the oldest cipher found in this pass, and XLVIII 11-15
(1477) the oldest after it, if it is a cipher.

## Key sources (keys.json)
1. LXXII 81: Piero de' Medici, 28 Oct 1494, glossed. It is the key for LXXII 77.
2. LXXIV, Milan embassy 1492-94: the glossed letters of Niccolini and Ridolfi.
3. LXXV, French embassy 1493-94:
   - all eight inventory pairs confirmed: 27/29, 30/90 ("Desifrata"), 32/31, 33/34, 35/36, 37/46, 40/41, 42/43;
   - plus 51/47, a two-level stacked system dated 29 Apr 1493, with 47 the working decipherment ("nul" marks);
   - della Casa's nomenclator additions in 53-54 (Paris, 17 Jul 1493; numbers 90-94);
   - Sassetti's glossed letters 14 and 17.
   - The Vespucci/Capponi key is also listed in ASF Carte Strozziane I f. 23 (see `research/oldest/scan_2026-09-23/italy.md`).
4. LXXIII and CXXXVII glossed letters, 1481-94:
   - Tornabuoni and others, Rome 1481-82 (LXXIII 383, 387-389);
   - Rome, 5 Feb 1489 (LXXIII 432);
   - della Valle, Naples, Jan 1491 (LXXIII 437);
   - Paolantonio Soderini, Venice, 28 Oct 1494, two pages almost entirely cipher (LXXIII 183-184);
   - the camp letter of 26 Aug 1494 (LXXIII 117);
   - LXXIII 354 and 356, clear "Copia di cifrato";
   - CXXXVII 470 (1482/3), 484 (Piero Capponi, 1486), 487 (Rucellai, Naples 1486), 499 (Piero Vettori, Naples 1488),
     509-510 (Alamanni, Pavia 1489) and 516 (Soderini, Naples 1489).
5. XLVIII:
   - Rucellai's glossed corpus 1482-85 and his pairs: 201/208 bis, 220 cc. 229/228, 239-240/241, 243 cc. 253/254, 294 cc. 306/276;
   - Jacopo Guicciardini, Ferrara 1483 (307, 310, 314, 316, 317, 331);
   - Gaddi, Rome 1483 (5);
   - Pierfilippo Pandolfini, Milan 1484 (53).

## Notes for existing leads and catalogue entries (no new rows)
- **Catalogue 2309 (XLVIII 214)**: XLVIII 294 (Rucellai, Milan, Feb 1484 st. fior. = 1485, signed "Bernardus Oricellarius") is
  three sides in the same sign family: "##", numerals 31, 87, 150, 18. Its clear text is filed with it as c. 276 ("Scripsi adi 22
  et questa per fante mandero quanto vedrai qui appresso ..."), which makes a plaintext pair for the 214 system. 214's
  neighbours 212-216 are glossed Rucellai letters of July 1483; none is a clear copy of 214. The decipherment slips at 241
  (of 239-240) and c. 254 (of 243) also belong to the same correspondence.
- **Lead 2350 (LXXII 196-206, Rucellai 1482 via Leonardo Spina)**: XLVIII continues the same "Lionardo" cover-address series
  into 1483-85, with dozens of glossed slips. The paging agents read the verso addresses as "Lionardo Co[gnati?] et compagni" in
  1483; not checked.
- **Leads 2320/2321 (CXXXVII 252, 63)**: re-paged. No filed clear text beside either (251/253 and 62/64 are unrelated clear letters).
- **Lead 2311 (LXXIII 371)**: re-paged; verso only show-through. LXXIII 354 ("Copia di cifrato") and 356 (headed "Copia") are short
  clear passages and were not tested against 371.
- **Lead 2351 (LXXII 192, Acciaiuoli 1513)** and **row LXXII 130/140**: the superscript-figure style is shared with Pandolfini 1514-15.
- **Lead 2324 (LXXII 216, Naples 1485)**: the 1486-89 Naples letters glossed in CXXXVII (487 Rucellai, 499 Vettori, 516 Soderini)
  are candidate key texts.

## Flagged but not rowed
- **CXXXVII 19** (Dieci di Balìa, Florence, 28 Sept, year not read; Pisa/Lucca war): about 17 lines of sign cipher, partly glossed.
  Its gloss coverage was not checked at full size.
- **CXXXVII 227** (28 Sept 1467): crossed signs standing alone in a clear note, perhaps person marks.
- **XLVIII 103 and 126** (1482): words in Latin letters that read only in part. Like XLVIII 11-15, these may be jargon or
  disguised text.
- LXXII:
  - 154: a clear unheaded slip from Rome, 1494;
  - the unheaded Pandolfini clear copies (284, 306, 316, 332, 337, 344, 347, 350, 365-366, 419): probably decipherments;
  - 358 and 434 (Lorenzo / "Abraham"): possible code;
  - 329, 381, 449: blank gaps in clear copies.
- LXXIII:
  - 63: "66" twice, perhaps a code number;
  - 247: show-through;
  - 810, 819: unsure.
- LXXV:
  - 60, 61 (della Casa, Orléans 1493): short glossed groups;
  - 133 (Gentile Becchi and Soderini, 8 Feb 1493/4): the code number "60" for a person.

## Prior art (known.py)
I ran known.py on every row's shelfmark and documents and on the correspondents' names: "filza CXXXVII, doc. 40", "filza XLVIII,
docs. 11", "doc. 63", "docs. 101", "doc. 294", "LXXII, doc. 403", "CXXXVII, doc. 504", "filza LXXIV/LXXV, doc", "LXXII, doc. 77",
"LXXIII, doc. 3", "docs. 130", "docs. 297", Tomaso/Tommaso Soderini, Bonanni, Sassetti, Ridolfi, Niccolini, Lanfredini,
Pandolfini, Baccio Ugolini, Dovizi, Moncallero, Alamanni, Vespucci.

None of the documents is in the catalogue, the leads or a target. The name hits are other letters:
- Pier Filippo Pandolfini 1481 and Lanfredini 1537 (different men or items);
- Matteo Niccolini 1510;
- Piero Alamanni's Rome 1492 letter;
- the Carte Strozziane I f. 23 key listing in `research/oldest/scan_2026-09-23/italy.md`;
- the note in lead 2311's vetting that Moncallero's Epistolario di Bernardo Dovizi da Bibbiena (1955) prints MAP cipher letters of
  1490-94 deciphered. That is relevant to LXXII 77/81 and LXXIII 117; not opened.

DECODE, Tomokiyo and Lasry were not searched beyond the repo dumps. The Lettere di Lorenzo de' Medici volumes (Fubini, Rubinstein,
Mallett, Butters) were not opened for XLVIII 63, CXXXVII 504 or LXXII 403. Marco Vito's database of encrypted MAP letters of
1486-1491 (`research/medici_bia/README.md`) may cover CXXXVII 504 and the 1486-89 glossed letters.

## Not reached
- CXXXVII positions 1217-2476 (docs ~571-1058): downloaded to position 1941, not paged.
- Full-size checks were done on a sample only:
  - LXXII 140, 309-311, 322 and 333 at 800 px;
  - LXXIV 49, 81 and 90 and the Ridolfi versos at 800 px;
  - LXXV 15 at 800 px;
  - the XLVIII Rucellai bare pieces at 800 px.
- No attempt to align any pair or to apply the key sheets (LXXII 178-188, CXIX 115-127) to the rows.
- Other filze where cipher has turned up (LXXXII, LXXXVII, LXXXIX, XCVII, L-LX for Lanfredini) were not paged.

## For COVERAGE.md
- ASF MAP paged leaf by leaf (contact sheets, ~390 px per page; flagged pages at full size): LXXII (all), LXXIII, LXXIV, LXXV,
  XLVIII, and CXXXVII docs 1-570.
- Next: CXXXVII docs 571-1058, and the Laurentian embassy filze (L-LX, LXXXII, LXXXIX).
