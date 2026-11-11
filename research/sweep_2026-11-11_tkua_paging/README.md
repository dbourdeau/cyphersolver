# TKUA paging pass (11 Nov 2026): envoys' archives on Arkivalieronline, and the Sehested 1657 lead

Brief: `research/_nov11/BRIEF.md`. Continues `research/sweep_2026-11-11_nordic/` (Rigsarkivet route by curl, `ao.py`).

**Result: 2 rows in `candidates.json` (1 with a complete `open` vetting block), `sehested_note.json` (verdict: read).**
Rows are built by `build_candidates.py`. The pass was cut short: 21 units were sheeted, of 221 left.

## Rows

| Row | Unit | Seen | Block |
|---|---|---|---|
| Peder Vibe → resident Peder Juel, 1649-55: about twenty letters with number-cipher passages, five leaves wholly in cipher, no decipherment (one leaf partly glossed) | TKUA Sverige, Peder Juels og Mogens Høegs gesandtskabsarkiver, Ordrer og breve 1648-55; unit 261583, images 57-93 | scan, all images; 5 at full size | open |
| Christian V → Jens Juel and Christoffer Lindenov, 25 May 1673: order in a three-digit code; the closing 13 lines have no decipherment on film | TKUA Sverige, Jens Juels gesandtskabsarkiv; unit 261588, images 7-11 | scan, all 62 images; 5 at full size | none: the loose decipherment leaf (image 9) may continue on an unfilmed verso; editions not opened. Class A lead: the 1674 orders (images 33-43) are deciphered between the lines |

## Sehested, Vienna 1657 (`sehested_note.json`)

All of images 108-172 of unit 260651 were downloaded and viewed. It is not an open cipher: a monoalphabetic number
substitution with a word divider and some twenty signs; the chancery deciphered it in 1657 (separate leaves 112-115,
interlinear on 132, 138, 140, with the signs glossed in the margin of 132), and Gigas read and quoted the letters
(Rebolledo, 1883, pp. 282-284 notes, opened on archive.org; he prints no full text). Most letters have no plaintext
beside them in the volume (list in the note), but with the values on image 132 they read at sight: I read the opening
of the letter of 7/17 Feb (image 118) that way. Suggested: close the lead as `read`.

## Units covered (Arkivalieronline `bsid`; contact sheets of every 8th image unless stated, 400 px a frame)

| Unit | Series | Images | Viewed | Cipher |
|---|---|---|---|---|
| 261576 | Sverige: Peder Vibes gesandtskabsarkiv 1635-43 | 284 | 1-281 by 8 | none seen (letters, accounts) |
| 261577 | Sverige: Tage Thott 1635 | 9 | sheeted, not viewed | - |
| 261583 | Sverige: Juel/Høeg, Ordrer og breve 1648-55 | 95 | 1-89 by 8, then **every image 57-95** | **yes: row 1** |
| 261587 | Sverige: Hannibal Sehested 1660 (label: 1660-75 forskellige) | 104 | 1-97 by 8 | none seen |
| 261588 | Sverige: Jens Juel (1673-74 orders) | 62 | **every image 1-48**, 49-57 by 8 | **yes: row 2**; 1674 orders deciphered interlinearly |
| 261590 | Lund 1679-80: Korrespondance | 29 | sheeted, not viewed | - |
| 261578 | Brømsebro 1644-45: Ordrer, breve og koncepter | 306 | 1-281 by 8 | none seen |
| 261580 | Brømsebro: koncepter og afskrifter | 266 | sheeted, not viewed | - |
| 261589 | Lund 1679-80: instructions, orders | 518 | 1-89, 193-281, 385-473 by 8 | none seen |
| 261592 | Lund: Akter fra forhandlingerne | 480 | sheeted, not viewed | - |
| 261591 | Lund: Koncepter til relationer 1676-80 | 318 | 1-89 by 8 (sheeted to about 281, sheeting then stopped) | none seen |
| 261386 | Nederlandene: Frederik Günther 1618-44 | 16 | sheeted, not viewed | - |
| 261387 | Nederlandene: Ulfeldt and Rosenkrantz 1621 | 96 | 1-89 by 8 | none seen |
| 261389 | Nederlandene: Vosbergen 1626-28 | 254 | 1-89 by 8 | none seen |
| 261388 | Nederlandene: Palle Rosenkrantz 1628 | 39 | sheeted, not viewed | - |
| 262200 | Nederlandene: Charisius, "Fragmenter" | 170 | 1-169 by 8 | not letters: medieval parchment binding strips |
| 417522 | Spanien: Hannibal Sehested 1640-41 | 383 | 1-185 by 8 | none seen (colour scans, clear copybook) |
| 417523 | Spanien: Eiler Ulfeldt 1641-43 | 17 | sheeted, not viewed | - |
| 260773 | Brandenburg: Ditlev Ahlefeldt, royal orders 1657-77 | 299 | 1-185 by 8 | none seen (orders in clear) |
| 260774 | Brandenburg: Ahlefeldt, list of orders | 15 | sheeted, not viewed | - |
| 262107 | Bremen: Klingenberg/Heespen 1676-78 | 361 | 1-89, 193-281 by 8 | none seen (copybook) |
| 260706 | Rigsdagen: Bernstorff, Frankfurt 1741-43 | 79 | 1-73 by 8 | none seen |
| 260651 | Kejseren: Gesandtskabsrelationer 1630-58 | 534 | **every image 108-172 at full size** | Sehested 1657, see note |

"None seen" at 1 image in 8 on a 400 px frame is a sample: a short cipher passage inside a clear letter can be missed.

## Not done

- The 17th-century Gesandtskabsrelationer listed in `batch_a.sh` (second loop: Sverige 261575, Spanien 261473, Spanske
  Nederlande 261490, Nederlandene 261377/261380/261383/261385, England 261267, Hamburg 260954/260956, Kejseren agents
  260652, Klingenberg/Sehested/Charisius 673416/673415, Polen 261415, Kejseren 260649, Bremen 262098-262105, the Juel
  and Lund copybooks 261584/261593) were **not sheeted**. Russia and the later Sweden relations are not among the
  scanned TKUA series listed by the Nordic pass.
- Uppsala Waller Italian letters: not started.
- Row 2: Danmark-Norges Traktater and Fridericia's "Danmarks ydre politiske Historie" not opened.
- Row 1: KB NKS 1299 e fol. (the old shelfmark stamped on the Vibe leaves) not searched in the KB catalogue.

## Routes

- `api.rigsarkivet.dk/ao/v1/...` by curl: no block, 0.8 s an image. `ao.py` here decodes JPEGs at reduced scale
  (`draft`), which cut a 12-image sheet from about 90 s to about 15 s; one request at a time, 0.8 s pause.
- `de-crypt.org/decrypt-web/RecordsList?search=` answers curl; archive.org full texts (Fridericia, Gigas) opened.
- Scratch: `/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5` (`sh2/` sheets, `pj/`, `jj/`, `seh/` full-size leaves).
