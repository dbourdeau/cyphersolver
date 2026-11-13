# Key states v3 to v10 of the Bonde number table: what each added, and from where

One number table serves the memorial (key v3) and Bonde's Swedish despatches 1676-1678 (keys v4 to v10). Each state was frozen
(md5 below) before the pages it was first used on were transcribed, by the session logs (the contributor's record; no RFC 3161
stamp covers v4 to v10). Files: v3 `../key.tsv`; v4 to v8 `../despatch1677/gloss/key_history/KEY_v4.tsv` ... `KEY_v8.tsv`;
v9 `../despatch1677/key.tsv`; v10 `keys/KEY_v10.tsv` (new in this addition). Each file's header gives the evidence for its new rows
(gloss image, line, cipher and gloss as read; or the context decode they came from).

**Gloss values and context values are counted apart.** Gloss = tiers A, B (the 1675 chancery decipherment of image 102R and its
107L/105L control), G (a letter) and H (a word code) from chancery glosses of 1676-1678 in the same volume. Context = tiers F, P
(read on the memorial's image 324), Q (values proposed after the memorial decodes, never counted there) and T (read off decodes of
the 1676 despatches). C = weak guess (shown in capitals, never counted read); W, U = open codes.

| state | md5 | frozen (UTC, 12 Nov 2026) | rows | gloss rows (A+B+G+H) | context rows (F+P+Q+T) | C | W+U | first used on (first pass) |
|---|---|---|---|---|---|---|---|---|
| v3 | 8e1d93d1 | 02:55:22 (b99) | 128 | 63 (57+6+0+0) | 52 (29+23+0+0) | 4 | 9 | the memorial (French); French copy of 24 Nov/4 Dec 1677 |
| v4 | 8e6d8c77 | 03:19:29 (b103) | 147 | 63 (57+6+0+0) | 73 (29+23+19+2) | 2 | 9 | 13/23 Oct 1676, 327R lines 4-10 |
| v5 | 12bcb08e | 03:20:57 (b103) | 151 | 63 (57+6+0+0) | 77 (29+23+19+6) | 2 | 9 | 13/23 Oct 1676, 328L lines 1-13 |
| v6 | 09e50de4 | 03:33:24 (b104) | 155 | 63 (57+6+0+0) | 81 (29+23+19+10) | 2 | 9 | 13/23 Oct 1676, 328L line 14 to 330R |
| v7 | 63ddef1c | 04:43:15 (b111) | 156 | 61 (55+6+0+0) | 84 (29+23+19+13) | 2 | 9 | 6/16 Oct 1676, 317R, 318L/R, 319L |
| v8 | 9bda6437 | 05:52:50 (b117) | 158 | 66 (55+6+3+2) | 84 (29+23+19+13) | 1 | 7 | 6/16 Oct 1676, 319R, 320L, 320R top |
| v9 | af29e81f | 06:08:58 (b118) | 164 | 73 (55+6+4+8) | 83 (29+22+19+13) | 1 | 7 | 3/13 Nov 1677; 17/27 Nov 1677; 24 Nov/4 Dec 1677 (in `../despatch1677/`); 1/11 Dec 1677; 29 Dec 1677/8 Jan 1678; 5/15 Jan 1678 |
| v10 | f780c0f3 | 07:22:14 (b122) | 179 | 91 (55+6+5+25) | 82 (29+21+19+13) | 1 | 5 | 12/22 Aug 1676; 12/22 Feb 1676 |

Rows counted by script over the key files (tier column). Q is 19 from v4 on: 17 new rows, plus 21 and 103 moved from C to Q.

## What each state changed

- **v4** (b103): v3 + 17 Q values (post-hoc values of the memorial, `../holes.md` 2: 145 l, 109 ff, 99 st, 124 st, 157 st, 120 q,
  129 y, 44 x, 155 x, 162 o, 76 g, 111 h, 134 h, 130 p, 115 ll, 139 ll, 123 ss) + 21 C å -> Q ff, 103 C l -> Q a + 2 T values
  read off the structure-test lines 1-3 of image 327R (113 k, 92 i). All context. So 327R lines 1-3 are training; only lines 4-10
  count.
- **v5** (b103): v4 + 4 T values read off the single decode of 327R (163 u, 146 k, 114 l, 158 s). Context. 327R is training for v5.
- **v6** (b104): v5 + 4 T values read off the 328L lines 1-13 decode (127 w, 166 h, 96 w, 65 t). Context.
- **v7** (b111): v6 + 152 w (T) and two gloss values overwritten from context: 66 å (A) -> y (T), 89 n (A) -> l (T), from the
  13 Oct 1676 decodes. Context.
- **v8** (b117): v7 + gloss only: 176 ö (G; was U), 63 k (G; was C), 962 u (G), 335 E.K.M:t (H; was W), 397 Konung (H).
- **v9** (b118): v8 + gloss only: 131 r (G; replaces P q), word codes 434 ordinarie, 254 allierade, 478 tractat, 326 declaration,
  479 tractera, 292 churfurst (H). Gloss pairs: `../despatch1677/gloss/gloss_pairs.tsv`.
- **v10** (b122): v9 + gloss only, read at full resolution on glossed despatches of Jan 1678 (images 504L, 517L/R, 518L/R, 519L/R,
  522L/R, 523L): 144 l (P) -> b (G); 331 and 348 W -> H (348 value changed fransöske -> frankrike); 15 new word codes (H): 358
  fred, 441 parlemente, 266 affaire, 418 march, 443 pommern, 435 preussen, 431 ordre, 449 quarteer, 476 engeland, 277 bäyern, 436
  pohlen, 437 polnisk, 302 conservera, 496 regement, 349 fransk. Each with image, cipher and gloss in the header of KEY_v10.tsv.

## Where context values sit in the read units

Per despatch, `counts.txt` gives the numbers inside the read (S) units by the source of their value (gloss against context) and how
many read units use at least one context value. In every despatch most read units use one: the figures rest on context values as
much as on gloss values.

## Key-state cautions

- 144: v10 makes it b from 1678 glosses. In the Aug 1676 despatch it decodes where l is wanted ('ansenbig' = ansenlig); in the
  Feb 1676 despatch it reads b 8 times of 8. Either a homophone of both or a change of table between 1676 and 1678: not settled.
- 66 and 89: v3 (from the 1675 gloss) gives å and n; v7 changed them to y and l from context. The 1675 gloss and the 1676-77
  despatches may use the table differently.
- v10 adds word codes from Jan 1678 glosses and is then used on Feb and Aug 1676 text: the gloss values are applied across two
  years.
