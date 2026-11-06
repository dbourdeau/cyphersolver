# ASF MAP whole-filza paging, pass 2: filza CXXXVII docs 571-1058 (6 Nov 2026)

This pass continues `research/sweep_2026-11_asf_map_paging/`, which paged CXXXVII docs 1-570 (image positions 1-1216). It
pages the rest of the filza: docs 571-1058, image positions 1217-2476, 1,260 pages. It used curl only, no browser. Images are
in the session scratchpad (`asf3/f137/w800` up to position 1941, `asf4/f137/w800` from 1942) and are not committed.

`make_candidates.py` writes two files:
- `candidates.json`: 7 rows, cls A/B/C, all `seen: image`.
- `keys.json`: 2 key-source items (cls K), kept apart because `merge.py` accepts only A/B/C.

`paging_flags.tsv` is the raw per-page flag list (35 lines). The image id is 132517 + position - 1.
MAP leads and catalogue items 2307-2389, and the rows of the earlier ASF passes, are not repeated.

## Method
- Image route as in pass 1. IIIF: `/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/00100137/A000NNNN.ptif`.
  Positions 1942-2476 were downloaded at 800 px, about one request a second.
- Position 2458 (doc. 1050 v) returns a 404 from the server ("TIFFReadEncodedTile failed") at every size, so it was not paged.
- Contact sheets: 4 pages side by side, each 390 px wide, autocontrast, 315 sheets. Four paging agents viewed them, never
  more than two at a time, and each wrote its flags after every sheet:
  - P1: positions 1217-1740
  - P2: positions 1741-1940
  - P3: positions 1941-2208
  - P4: positions 2209-2476
  Every sheet was viewed (315 progress lines).
- Every row's main page was then opened at the server maximum (1272-1411 px). The neighbouring documents were checked on the
  sheets for a filed decipherment or a clear copy.
- known.py was run on each document and on each writer: Corsi, Galeotto de' Medici, Giulio de' Medici, Guicciardini,
  Pandolfini, Pallavicino. Nothing matched outside this pass, except that the catalogued Pandolfini rows are a different set
  (MAP LXXII, 1514-15).

## What the range holds
- Docs 571-760: letters to Lorenzo di Piero and to the Medici government, 1512-1523. This is where all the cipher is: the
  Spanish embassy of 1513-14, the Swiss, Pandolfini in 1515, and Rome and Florence in 1520-21.
- Docs 760-1058: 16th-century private letters, accounts, inventories and notarial acts, and two small code-word lists at the end.
  - P2 (positions 1741-1940) flagged nothing.
  - P3 (1941-2208) flagged only four "unsure" pages, all dropped: a burnt illegible page (doc. 856), a letter in Greek
    (doc. 916), and a monogram and pen trials (docs. 950-951).

## Rows (candidates.json)

| Shelfmark (MAP CXXXVII) | Date | Correspondent | cls | Gloss | Image ids |
|---|---|---|---|---|---|
| 619 | 27 Oct 1513 | Francesco Guicciardini, Valladolid -> Lorenzo | B | bare, about 40 lines; head note "Decifrata ..."; clear text probably printed (Guicciardini's minutes) | 133841-42 |
| 620, 621 (copy), 622 (copy), 623, 627, 628 (copy), 633 (copy) | Oct 1513 - Apr 1514 | Giovanni Corsi, Valladolid/Madrid -> Lorenzo | A | bare, about 90 lines; copies duplicate the ciphertext | 133843-58, 133869-72, 133883-84 |
| 644 | 1514 | envoy at the Catholic King's court (signature unread) -> Lorenzo | B | bare, about 13 lines | 133915-18 |
| 666 | Sept 1515 | Francesco Pandolfini -> Otto di Pratica (copy) | A | bare, about 60 lines; Pandolfini pairs in LXXII | 133979-82 |
| 728 | 11 Jan 1521 | Galeotto de' Medici, Rome -> Florence | B | bare, 7 lines | 134171-74 |
| 733, 734 | May 1520/21 | Card. Giulio de' Medici, Florence -> Galeotto de' Medici, Rome | A | bare; two whole letters in two sign systems | 134185-92 |
| 747 | undated (1520s) | unidentified | C | unsure: dot-separated words that mostly do not read | 134235-38 |

## Key sources (keys.json)
- CXXXVII 626 (agent at Zurich, 11 Dec 1513) and 636 (Raffaello ..., May 1514): letter/figure cipher with superscript indices,
  with interlinear decipherment. They are the first test for the Corsi and Guicciardini rows.
- CXXXVII 1053 and 1054: two small code-word lists, undated. They pair meanings with numbered cover words and signs
  ("Lorenzo" 1, "el papa"/"el fratello", "Orlando Palavicino", "Parma", "Vinegia").

## Limits
- The four 1513-15 rows are not compared with each other or with the glossed 626/636 tables.
- Guicciardini's legation letters are printed (Canestrini 1864; Jodogne). The 619 row may be read in print already; this
  was not checked (no web search in this run).
- Years still to be read at full size:
  - the last numeral of 733-734 (MDXX? or MDXXI);
  - the month on 644.
- The signatures on 644, 626 and 747 are read only from the contact sheet.
- A single short cipher group inside a dense clear line can still be missed at sheet size. Glossed letters were not
  checked line by line for unglossed runs.
- Position 2458 (doc. 1050 v) is missing on the server.

## Next
- 619: look up the 27 Oct 1513 letter in Jodogne's *Le lettere*. If it is printed, it is a plaintext pair for the 1513-14
  Spanish embassy cipher.
- 666: test the LXXII Pandolfini table.
- 733-734: transcribe; 734 is a short sign alphabet.
- Filza CXXXVII is now fully paged. Still to page: the Laurentian embassy filze (L-LX, LXXXII, LXXXIX) and the 1510s-20s MAP
  filze (CVI-CXX), which may hold more of the 1513-23 correspondence.
