# TKUA paging pass 3 (11 Nov 2026): the second-loop units, and Petkum finished

Brief: `research/_nov11/BRIEF.md`. Continues `research/sweep_2026-11-11_tkua_paging_2/` (same route, `ao.py`).

**Result: 4 new rows in `candidates.json`, all with a complete `open` vetting block; 1 key lead in `key_leads.json`;
`petkum_leaves.json` for catalogue entry 2530 (30 undeciphered pages listed, "Monsieur" identified).**
Rows are built by `build_candidates.py`. The pass stopped on budget: 19 of the 23 second-loop units were viewed in full
at 1 image in 4, two in part, two not at all. None of the further first-loop or 18th-century units was started.

## Rows

| Row | Unit, images | Seen | Block |
|---|---|---|---|
| Johann Schultetus, The Hague → Christian IV, Sep 1628 to May 1629: reports with code numbers, capital-letter cipher words and signs; one French letter in a two-digit cipher. No decipherment | TKUA Nederlandene B.41 (1608-34); unit 261377, images 426-475 | every image 425-475 at 1000 px; six frames at full size | open |
| Christian Pentz, Vienna → Christian IV, 26 Mar / 5 Apr 1636: seventeen lines of a two-digit number cipher, no decipherment | TKUA Kejseren, Gesandtskabsrelationer 1630-58; unit 260651, images 36-38 | three frames at full size | open |
| Johan Zobel, Paris → Christian IV, 20 Sep 1629: separate sheet with nineteen cipher words, no decipherment | TKUA Frankrig B.31 (1627-31); unit 261292, images 241-242 | both pages at full size | open |
| Peder Charisius, The Hague → "Monsieur", 7 June [1655]: one page, eleven passages in signs and numbers, no decipherment | TKUA Nederlandene B.44 (1646-59); unit 261381, image 441 | full size | open (class A: a possible deciphered sibling in Klingenberg's journal, unit 673416 image 433, not tested) |

Key lead: a copy of the ordinary cipher of the States General and their ambassadors, about 1655 (unit 261381, images
442-444): homophonic alphabet 4-69 and names 70-289.

## Petkum (unit 261267, catalogue 2530): `petkum_leaves.json`

Every image 337-657 was downloaded at 1000 px (`pet.py`) and viewed nine to a sheet (`petsheet.py`); every page with
cipher was then viewed again as a half-frame at 500 px a page (`halves.py`).

- **"Monsieur" is Biermann**, the secretary for foreign affairs. Address panels: image 360 ("A Monsieur Monsieur
  Bierman, Secretaire des affaires estrangeres de Sa Ma.te de Dennemarck Norvege") and image 616 ("Mons. Bierman premier
  Secretaire de la Chambre"). The first name Conrad is not on the leaves.
- **The entry's split needs correcting.** The chancery glossed most of the letters to Biermann between the lines too,
  not only the relations to the king. Undeciphered: 30 pages, about 209 lines of cipher, chiefly the letters to
  Biermann of 23 Nov 1665 to April 1666 (the largest: 30 Nov 1665, images 572-574, about 63 lines; 13 Apr 1666,
  image 641), some of Jan to June 1665, Salisbury 17 Sep 1665, and one relation to the king of 6 Apr 1666 (image 634).
- Line counts are estimates from 500 px pages; a very pale gloss could be missed at that size.

## Units covered (20 frames a sheet, 400 px a frame, 1 image in 4 unless stated)

| Unit | Series | Images | Viewed | Cipher |
|---|---|---|---|---|
| 260652 | Kejseren: agents 1629-49 | 461 | 1-461 | none seen |
| 260653 | Kejseren: agents 1649-63 | 801 | 1-797 | none seen |
| 260954 | Hamburg 1639, 1649-53 | 616 | 1-613 | none seen (faint film) |
| 260956 | Hamburg 1653-56 | 346 | 1-345 | none seen |
| 261415 | Polen B.24 | 949 | 1-949; 653, 829, 917 at full size | French letters 1658-59 and 1701-04 with a number code, deciphered between the lines on every leaf opened |
| 262098 | Bremen B.23, 1675 to May 1676 | 643 | 1-641; 97, 117, 413 at full size, 241, 341, 357, 393 at 1000 px | German three-digit code with signs, deciphered between the lines on every leaf opened (crib material for `targets/biermann1675` and catalogue 602) |
| 262100 | Bremen B.24, Jun-Dec 1676 | 714 | 1-713; 25, 109, 277, 293 at 1000 px | no bare cipher seen; dense leaves 349, 457, 473 not opened |
| 262105 | Bremen B.26, 1677-78 | 509 | 1-509 | none seen |
| 261378 | Nederlandene B.42, Tancke 1638-45 | 777 | 1-777 | none seen |
| 261381 | Nederlandene B.44, 1646-59 | 633 | 1-633; every image 400-480 | **row (441)**, key lead (442-444); 444 right deciphered |
| 261385 | Nederlandene B.46, 1661-63 | 424 | 1-421 | none seen |
| 261377 | Nederlandene B.41, 1608-34 | 475 | 1-473; every image 425-475 | **row (426-475)**; 181 is clear Dutch |
| 261291 | Frankrig B.30, 1625-61 | 365 | 1-365 | none seen |
| 261292 | Frankrig B.31, Zobel 1627-31 | 366 | every image 1-81, 162-294; 82-161 and 295-365 by 4 | **row (241-242)**, the only cipher seen |
| 260649 | Kejseren 1551-1625 | 637 | 1-637 | none seen |
| 260651 | Kejseren 1630-58 | 534 | 1-533; every image 30-44 | **row (36-38)**; Frankfurt relations 1657-58 (357, 381 at full size) deciphered between the lines |
| 261490 | Spanske Nederlande B.12, 1590-1644 | 346 | 1-345 | none seen (water-stained) |
| 261574 | Sverige B.84, agents 1622-39 | 688 | 1-685; 3-103 by 4 as well (each opening is filmed twice); 46-52, 106-112, 222-228 every image | Peder Vibe, Stockholm 1635-39: two-digit cipher. Deciphered between the lines in 1636 (image 109) and in the margin in 1639; short passages of 1635 (images 43, 47, 49) carry no gloss but read with the values on image 109 (two words read that way), so no row. Peder Galt 1622-25 (341-613): symbol cipher with marginal decipherment; 545, 549, 609 looked bare at 400 px and were not opened |
| 261584 | Sverige C.194, Peder Juel's copybook 1648-55 | 248 | 1-245 | none seen |
| 673416 | Klingenberg journal A 1665-67 | 740 | **1-77 and 401-477 only**; 433 at full size | sign cipher copied into the journal with marginal plaintext (433) |
| 673415 | Klingenberg journal B 1665-67 | 937 | **1-77 and 481-557 only** | none seen in those |
| 261593 | Jens Juel's copybook 1679-80 | 741 | sheeted, **not viewed** | - |
| 262102 | Bremen B.25 | 1005 | **not viewed** (two sheets made) | - |
| 261383 | Charisius 1659-60, images 193-465 | 465 | **not done** | - |

The first two sheets of 673416 and 673415 came out too small to judge (a tall cover image stretched the sheet); 1-77
there counts as not seen. "None seen" on a 400 px frame is a sample: a short passage in a clear letter can be missed.

## Excluded

- Polen B.24, Bremen B.23, Frankfurt 1657-58, Peder Vibe 1636-39: deciphered at the time on the leaf.
- Peder Vibe 1635: no gloss, but the 1636 interlinear values read it; a key lookup, not an open cipher.
- Peder Galt 1622-25: marginal decipherments; the three bare-looking leaves need opening before any claim. An edition
  search for Galt's despatches found nothing on archive.org or by web search (one query each).

## Not done

- Second loop: 262102, 261593, 261383 images 193-465; most of 673415 and 673416; Galt leaves 545, 549, 609; Bremen
  B.24 leaves 349, 457, 473.
- The remaining first-loop envoy archives and all 18th-century relations of the 236 units: not started.
- Schultetus: images 426-447 were seen at 400 px only; the letters are not listed one by one.
- Charisius row: the Klingenberg journal cipher was compared by eye only.

## Routes

- `api.rigsarkivet.dk/ao/v1/...` by curl: no block all day; two workers at once, 0.8-1 s pause each.
- `de-crypt.org/decrypt-web/RecordsList?search=`: open. archive.org full texts: open (Fridericia 1876/1881, Opel
  vol. 3; Opel's file names contain spaces, take them from `/metadata/<id>/files`). WebSearch used for each row.
- Scripts: `batch_c*.sh` (queues), `pet.py` (frames at 1000 px), `petsheet.py`, `sheet20.py`, `halves.py`, `crop.py`
  (full-size crops by fractions), `petkum_build.py`, `build_candidates.py`.
- Scratch: `/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5c` (`sh/` sheets,
  `pet/`, `zo/`, `ta/`, `nl/`, `kj/`, `pl/`, `br/`, `sv/`, `kl/`, `ed/` texts, `notes.txt`).
