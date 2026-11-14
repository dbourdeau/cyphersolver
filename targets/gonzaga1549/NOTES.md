# gonzaga1549 — Charles V and Prince Philip → Ferrante Gonzaga, Modena (catalogue 1560 and 1561)

Status: read in part, written up 3 Nov 2026; WAINUT's work on the same letters and on Prince Philip's (formerly targets/ferrante1549) folded in on 14 Nov 2026 as `wainut/`, see the section of that date

Status: in progress. The page stands (read in part, 3 Nov 2026), but since the fold of 14 Nov 2026 the entry has workable gaps: the 23 open differences between the two readings and the unresolved lines are each a look at an open image, not yet done (Remaining gaps, Escalation).

Lead 1560 in `research/leads.json` (the page `docs/solve/1560.html` on the site). Biblioteca Estense Universitaria,
Modena, Autografoteca Campori, Lettera K, Karl V, sfasc. I / III / IV. Emperor → Ferrante I Gonzaga, governor of Milan.
Spanish, signed Carlos / secretary Vargas (1552) or Perezius (1549). Licence CC BY-NC-SA.

## Access (worked 2 Nov 2026, plain curl, no bot check)
- Manifest: `https://edl-jarvis.cultura.gov.it/meta/iiif/<uuid>/manifest` (IIIF v2); images `.../images/iiif/db/<img-uuid>`.
- The server refuses output over roughly 1800 px wide / 2.5 Mpx. Full pages: `/full/1200,/0/default.jpg`.
  Crops at native detail: `/x,y,w,h/1800,/0/default.jpg` (pages are ~3000 x 4200).
- Record IDs for all 151 Karl V → Gonzaga items: search page
  `lodovico.medialibrary.it/media/ricercadl.aspx?ricdccreator=Karl+V+(Carlo+V%3b+imperatore)&ricaddrrel=Gonzaga,+Ferrante+I+(conte+di+Guastalla)&rictip=documenti+manoscritti&nris=48&page=N`
  (N = 1..4, parse `schedadl.aspx?id=`). Saved in `allids.json` / `labels.json`; `fetch.py` downloads the eight letters below.

## What is in the file (viewed 2 Nov 2026)
| Letter | Cipher | Decipherment in the file |
|---|---|---|
| 13 May 1549, sfasc. III cc. 29-30 (Brussels) | signs, 8 lines on c.30r | slip c.29r, 5 lines (money and materials for a work; the slip names no place) |
| 15 Jul 1549, sfasc. IV cc. 40-42 | **numbers** (13, 16, g, ...), whole body | c.41, full decipherment ("Su Mag.d dize") |
| 23 Dec 1549, sfasc. IV cc. 76-78 | signs, two passages on c.76r | c.77, three paragraphs |
| 1 Jul 1552, sfasc. I cc. 81-84 (Villach) | signs, ~20 lines on c.81r, a different sign set | c.82-83, full page "Descifrado de Su Mag.d" (contents not rechecked) |
| 14 Nov 1549 cc. 60-63; 20 Nov 1549 cc. 64-65; 30 Sep 1549 cc. 50-53; 11 Aug 1542 cc. 109-110; undated cc. 131-132 | signs | none: the unread targets |

Cc. 131-132 is not in the Karl V → Gonzaga listing (151 ids); locate it by shelfmark.

## Observations
- 1549 sign cipher (c.30r, c.76r, c.60r): about 15 tokens per line, 8 lines for roughly 270 plaintext letters on the slip
  -> about 2.3 letters per token, so syllabic. Tokens such as `mo`, `no`, `lo`, `co`, `as/ap` recur as separate glyphs.
- 1552 cipher (c.81r) looks like a different, denser sign set with Latin-letter-like tokens; its plaintext is on c.82.
- The 15 Jul 1549 numeric cipher is a third system.

## Second look (2 Nov 2026, after viewing every page at 1200 px and c.30r at 1800 px)
- **The unread letters are mostly clear Spanish with short cipher passages, not whole ciphered letters.**
  30 Sep 1549 (c.50): about 4 cipher lines in the body plus a clear marginal note. 20 Nov 1549 (c.64): 2 cipher lines at the foot.
  14 Nov 1549 (cc.60-63): the largest sign passages (c.60r about 12 lines, more on 60v-62).
- **11 Aug 1542 (cc.109-110) is a numeric cipher** with clear Spanish words embedded (a nomenclator): same family as 15 Jul 1549.
  Its key can come from the 15 Jul 1549 decipherment on c.41, which gives a full-letter known plaintext.
- 15 Jul 1549 numeric: numbers 3-21 with dots and superscripts (e.g. `13. 16. g. 3^3 ...`), clear words such as `don vana`, `fon`, `conssu`
  left in the text. About 35 lines on c.40r.
- 13 May 1549 c.30r: the cipher is **6 lines** (not 8), about 20-24 visual units per line, 120-130 in all, against about 215 plaintext letters
  and 77 Spanish syllables on the c.29 slip. Units look like a base sign plus a recurring second element (`ap`, `mo`, `no`, `lo`), so a
  syllabic or base+vowel-marker structure is likely; it is not settled. Line crops are made by the recipe in Access (x,y,w,h at native width, upscale with PIL).

## Systems identified (2 Nov 2026, from Tomokiyo's Cryptiana, `cryptiana.web.fc2.com/code/spanish2.htm`)
Keys saved in `ref/` (S. Tomokiyo's images; credit before any publication).
- **Sign letters (13 May, 14 Nov, 20 Nov, 30 Sep 1549) = the Imperial Cipher of 1544-1554** (Charles V, Philip, Granvelle, Ferrante Gonzaga,
  Mendoza; Meister p.212 `ref/CharlesV2.jpg`, Bertomeu Masia 2009 reconstruction `ref/CharlesV3.gif`): alphabet signs, a syllabary with vowel
  indicators (ba be bi bo bu ...), signs for ll rr ss tt ff, 8 nulls. Glyphs such as `mo`, `no`, `ap`, `lo` are real signs of the key, not letters.
- **15 Jul 1549 numeric = the Doria-Figueroa-Philip cipher of 1548** (`ref/CharlesV1548.jpg`): a numeric syllabary.
  Consonant numbers (syllables): b 2, c 3, d 4, f 5, g 6, h 7, l 9, m 10, n 12, p 13, qu 14, r 15, s 16, t 17, v 18, x 19, z 21; alone-letter row
  r 16, s 17, e 5 (dotted), n 3^3, ll = H^o, rr, ss. Vowel marks: a = dots before and after (or the bare numeral), e = dot below,
  i = two dots above, o = dot after, u = superscript 0 (3^0 = cu ...); `dan` = tra, `don` = tro are real signs. **Checked by eye on the first 30 tokens of
  c.40r against c.41r: po r la pi de la ca r ta que va co n e s ta e n te n de re y s lo que nu e s ... all fit.** The numeral 1 is written with its
  own dot (i3 = 13), which is why base-only reading failed; the other clear words (vana, in, fon, consu, filo, pos, mul, fen, lab, ben, gis...)
  are probably more signs, not nulls.
- **11 Aug 1542 numeric (cc.109-110) is a different, earlier system** (single digits with stacked superscript digits); no key found yet.
- **20 Nov 1549 (cc.64-65) is a clear letter** (papal election after Paul III, Parma, Duke of Florence) with 5 short cipher passages (c.64r last 2 lines,
  c.64v about 14 lines in all) and clear marginal notes in a later hand that summarise each passage:
  `a Parma en nombre de la yglesia`; `mueva ninguna cosa en Parma de nuestra parte ni en otro lugar`; `que no se mover? guerra a la yglesia`;
  `offender y ocupar en esta occasion el estado de la casa Farnesa por la vezindad que tiene con el del Duque de Florencia`;
  `tentar en tal tiempo`; `paresciere otra cosa y diere occasion se podra facilm. hazer`. These are the cribs.
- 30 Sep 1549 (cc.50-53): clear letter with a short cipher passage on c.50r and a clear marginal note.

## c.64v first attempt (2 Nov 2026): no reading
- Passage 2 (end of line 5 and line 6 of c.64v, underlined, crib `mueva ninguna cosa en Parma de nuestra parte`, then clear `ni en otro lugar`):
  about 22 glyphs. Read at 3x (crops `crops/t_all.jpg`): line 5 tail `Lp` (= mu in Masia's key), `c`, `w.`, `b` with dot below, `o`-with-dots, `ap`, `o` + cross-stroke;
  line 6 `5`, `j` with dot and hook, `w ap`, `L:` (= ma in Masia's key), `no`, `Li`, `x o`, `gieri`, `L:`, `no`, `+`. The count fits a syllabary (mu-e-va ni-n-gu-na co-sa en Par-ma de nues-tra par-te),
  but only `Lp` = mu and `L:` = ma match the key with any confidence; `L: no` occurs twice. Not enough to commit a reading.
- The key image `ref/CharlesV3.gif` does not cover every glyph used here (several glyphs have no counterpart: `5`, `gieri`, the `w` forms),
  and the hand varies; a reading needs a glyph catalogue made from the letters themselves (13 May c.30r + c.76r with c.29 / c.77 as known plaintext,
  then the 1552 pair), not only the printed key.

## Glyph catalogue made (2 Nov 2026), see `glyph_catalogue.md`
- c.30r against the c.29 slip is a one-sign-per-unit syllabary: lines 1-3 (about 60 signs) are read, 30 glyph values fixed, most confirmed by key and by repeats.
- First transfer: c.64v passage 2 reads `... cosa en Parma de nuestra parte`, matching the clerk's margin note. The Estense letters therefore use a single series
  of the Imperial Cipher and the catalogue applies across letters.

## c.64v readings so far (2 Nov 2026, by eye with the catalogue)
- Passage 4 (3 lines) read: `ofender y ocupar en esta ocasion el estado de la casa Farnesa por la vezindad que tiene con el ...`, one sign per syllable, equal to the clerk's note.
- Passage 3 ends `... a la iglesia`; passage 2 `... cosa en Parma de nuestra parte`. See `glyph_catalogue.md`.
- Passage 5 read (`tentar en tal tiempo`; `paresciere otra cosa y diere occasion se podra facilmente hazer`), both equal to the clerk's notes.
- Passage 1 (end of c.64r + first line of c.64v) uses signs with dots below: a second series, not catalogued, not read.
- Not read: passage 1, the rest of passages 3 and 2, the text after `con el` in passage 4.
- So 4 of the 5 ciphered passages of the 20 Nov 1549 letter are read in whole or in large part, every one equal to its marginal note. Everything is by eye.
- Still to do for the write-up: profile.json (not created yet), solution steps, DECODE, `docs/` page. The target stays `Status: in progress`.

## 13 May 1549 finished, 30 Sep located (2 Nov 2026, second sitting)
- c.30r: all six lines align with the c.29 slip; the whole block reads (`13may1549_decryption.txt`, `13may1549_reading.txt`); three signs unfixed.
- c.50r (30 Sep 1549): cipher block of 5 lines (about 90 signs) at the end of `... lo mismo`, no slip. The clear margin note beside it reads
  `y aunque va con fin de tratar al Prior di Lombardia castillo ... de tal manera que fuese tanto como echarle de alli por meter dentro a Mos de Brissac`
  (Brissac, Piedmont; the Prior of Lombardy = the Order's prior; this is the summary of the block). Line 1 begins with signs `ri? n ga? n ...`; the table does not yet
  settle them, so nothing is read there. This is a real decipherment problem (a crib of ~25 words for ~60 syllables), unlike c.30r and c.64v where a slip or note matched sign for sign.

## 30 Sep 1549, c.50r block: one anchor found (2 Nov 2026, third sitting)
- Line 3 of the block carries `[ca = ring with dot][s = mo][ti = triangle two dots][ll = L-shaped sign, dot after][o = ap+] [de = x-o]` = `castillo de`, which is the word
  `castillo` of the clerk's margin note and the key's own `ll` sign (L, Masia). The letter's clear text says the Duke of Savoy wanted to go to Nice (`tema de yrse a Niza`),
  so `castillo de Niza` is the likely continuation; the next signs (ring-dot, flat-ta, l-o ...) were not matched to `ni-za`.
- Lines 2 and 4 hold about 20 signs not in the table (a d-shaped sign, a 6-with-ring, a loop-p, a Lambda with a ring, a crossed-ring) and the table values `de a r po mo`, but no phrase
  that can be checked against the note. The block is a real decipherment (about 60 syllables, margin note a summary, one sure word), not read.
- Next: extend the table from c.76r / c.77 (23 Dec 1549) and c.81r-83 (1 Jul 1552, other series) before returning to this block.

## c.76r / c.77 (23 Dec 1549): crib found (2 Nov 2026, fourth sitting)
- c.77 is not a letter of its own: it continues the first cipher passage of c.76r in clear (`La consideracion que hazeis sobre lo de Niça ... el Prior de Lombardia`,
  then `que se den al dicho Prior a cuenta de la dicha paga ... residir en el Castillo`, `la venida aca del Crasso ...`). Passage 1 line 1 reads `so b re lo de ni ca si e n do a` sign for sign.
- The Prior of Lombardy and the castle are also the subject of the 30 Sep block (c.50r); c.77 gives its vocabulary (Niça, plaça, Prior, Lombardia, castillo, residir).
- Not done: signs of lines 2-3 of passage 1, passage 2 (`Los quales hareys ...`, three lines at the foot of c.76r) against paragraph 2 of c.77, and the short passages near the top of c.76r.

## c.76r aligned against c.77 (2 Nov 2026, fifth sitting)
- Passage 1 lines 1-3 and the first line of passage 2 align with c.77, sign for sign except two stretches: `ça` (one extra sign) and `fuera della` (7 signs for 7-8 units).
  So the cipher is one sign per syllable throughout the Estense letters; the sign table is now about 70 values, checked on three pages (c.30r, c.64v, c.76r).
- The 30 Sep block (c.50r) is the same business (Prior of Lombardy, castle of Nice); with the table and c.77's wording it should now be readable. Not yet attempted again.
- Not done: lines 2-3 of passage 2 (c.76r foot) against the rest of paragraph 2 of c.77; the short cipher passages at the top of c.76r (`quanto a lo de ...`, `Duq octauio` note); a transcription file per page.

## 30 Sep 1549 (c.50r), corrected 2 Nov 2026
- Signs match the margin note in line 3 up to `que`, in line 4 (one extra sign, me/te unsure) and in line 5 up to `de`. `fuese tanto`, `Brissac` and lines 1-2 did not map, apart from `y aunque` at the start.
  An earlier version of `30sep1549_decryption.txt` entered `al prior de lombardia` and `fuese tanto` from the note, not from the signs; removed.
- Meaning not established. An earlier note here called the block an instruction from Charles V and named the Duke of Savoy's men as the actors; neither the signs nor the note say that. The note says only that something aimed at dealing with the Prior of Lombardy over the castle, amounting to removing him to put the French lord in.

## How far to trust the table (corrected 2 Nov 2026)
- Every passage before 14 Nov was read with its plaintext already in view (slip, c.77, margin note). Those alignments are fitted, not tests, and `sign for sign` overstated them.
- c.30r: lines 1-4 were aligned sign by sign; lines 5-6 were only looked at. `13may1549_decryption.txt` is the slip text, not an independent decryption, and 117 is the slip's unit count, not a measured sign count.
- The table has unresolved conflicts: ring with two dots is ci, di and ni; 7 with two dots is bi and si; mo and no both give r; 6 with a dot is la, plain 6 unsure. `about 70 values` was never counted (about 50 table rows).
- The table has no transcription file behind it and no statistical validation.

## 14 Nov 1549 (cc.60-63): first blind test (2 Nov 2026)
- 60r has two large blocks, 60v and 61r are solid cipher, 61v and the top of 62r continue; the rest of 62r and 62v are clear. No decipherment leaf or margin notes seen on the contact sheet (low resolution). Clear words sit inside the cipher (`Pollo` on 60r).
- With no crib, line 2 of block 1 gave `do al particular de la determinacion con que`, needing one new value, d = r, which Masia's key has. Line 3 gave `... apuntar y (ca?)pitular con el`, first half unread. See `14nov1549_decryption.txt`.
- This is the first evidence not fitted to a known text. It is about 40 signs out of several hundred, by eye. Next: the rest of 60r, then 60v-62r; the 62r/62v clear text should be read for context.

## 14 Nov 1549, c.60r first block read without a crib (2 Nov 2026)
- `y viniendo al particular de la determinacion con que quedava desde [..] apuntar y (ca?)pitular con el [Duque] O(ct?)avio sobre la empresa de Par(ma?) ... algunas de las consideraciones que ... para despues ... daros a entender nuestra intencion y voluntad`. Files: `14nov1549_decryption.txt`, `14nov1549_60r_block1.tsv`.
- 142 signs: 116 firm, 11 doubtful, 15 unread (counted from 14nov1549_60r_block1.tsv). By eye. No slip or margin note was in view, but values for new signs were chosen by what made Spanish, so this is not a controlled test and no one outside has checked it.
- New values: theta = s (Masia's s column), d = r, x-p = nu, L with one dot = tra, Saa = Duque (c.76r writes it with the gloss `Duq octauio` above). The base shape appears to carry the consonant (8 = c, open j = n, ring = d) and the dots the vowel, which should resolve the ci / di / ni conflict; not yet checked back on c.30r and c.76r.
- Still unread in the block: the sign before `apuntar`, most of the end of line 4, the start of line 5, the start and end of line 6.

## 14 Nov 1549, c.60r second block (2 Nov 2026)
- `14nov1549_60r_block2.txt`. Line 1 runs through: `teniendo respeto al poco fundamento que`. Line 5 nearly so: `dinero estando en desgracia del Pollo como por`. Lines 2-4 and 6 partial, lines 7-12 viewed but not decoded. No sign file for this block, so nothing counted.
- Values for f-bar (re), n-p (fu), R with dot (gra) and the sign read ze were chosen because they made Spanish; treat them as doubtful until they recur.
- Clear words sit in the cipher: `Pollo` (line 5) and underlined letters in line 9. `Pollo` may be a cover name; not established.

## Working hypothesis: base shape = consonant, mark = vowel (2 Nov 2026)
- Seen in c.60r: triangle t, Lambda p, 6 l, 8 c, open j n, sideways loop d, g r, 7/y s, ys v, L m. One dot = a, two dots = i, o-loop = o, p-tail = u, cross-bar = e. Cryptiana describes vowel indicators for this cipher.
- If it holds, `ring with two dots = ci / di / ni` was my own lumping of three different bases (8, loop, j), not a conflict in the cipher. Not yet rechecked on c.30r, c.64v or c.76r.
- Does not cover everything: x with stroke = de and L with one dot = tra sit outside it; g-bar and f-bar both come out re.

## Rule test (2 Nov 2026)
- `rule_test.tsv`: 21 hits, 3 misses, 1 not viewed out of 25. Not blind: those pages had been read earlier in the session.
- The independent evidence is Masia's key as reproduced by Tomokiyo (`ref/CharlesV3.gif`, 573 px wide, read at that low resolution). Its rows ma, pa, ta, la, sa, ra, va show one base with marks in the rule's order.
- The key also corrects the rule: ne and nu are not on the j base (theta-like with bar; x with p-tail); tra is its own inverted-T base, so `L with one dot = tra` is not an exception; b is the 7 base and s the y base, which settles `7 two dots = bi, y two dots = si`; de has x-o as a listed form; do has 9 with dot as a variant.
- Doubtful values the key supports: fu = n with p-tail (fa row), nu = x with p-tail, gra = lambda-like sign (low resolution). `re` from f-bar and `ze` are not confirmed.
- The rule also goes against two readings in block 1 of c.60r. `capitular`: its first sign is 8 with two dots, which is ci, not ca, so `capitular` is not supported unless the dots were misread. `Parma`: the last sign was entered as L-p, which is mu, not ma. Both need rechecking at higher zoom; do not quote them as read.

## Sign table rebuilt (2 Nov 2026)
- `sign_table.tsv`, from Masia's key (Tomokiyo's image), enlarged. Conflicts in the old table are gone: ring with two dots was my lumping of three bases; `mo` is s and `no` is r in the key, so any `mo = r` on c.76r was a misreading of mine, not yet corrected there.
- The two readings the rule put in doubt were my misreadings. At higher zoom the capitular sign is 8 with one dot (ca), and the Parma sign is L with a dot (ma), no p-tail. `capitular` and `Parma` stand, and block 2 has `como la de Parma`.
- Reread of block 1 with the table: 142 signs: 132 with a value, 3 doubtful, 7 unread. New: `Ottavio` (the key's tt sign), `se to(ca?)ran aqui algunas de las consideraciones que`, `nos o(c?)urren para despues`. Block 2: `del dicho` (u = c, ho).
- Key values were applied with the context in view, so this is agreement with a published key, not a controlled test. The key is itself read at low resolution.
- Open: signs with dots below (`ap`, `a+`, `n`, and all of c.64v passage 1). They are not in the key image. Nulls or the second series; not established. Bare m (with f-bar on c.60r) is not in the key either.

## 14 Nov 1549, c.60r second block reread with the table (2 Nov 2026)
- `14nov1549_60r_block2.txt`. Lines 1-8 now mostly run: Ottavio is a poor foundation for an enterprise such as Parma, both for what is known of it and for lack of money, being in disgrace with the `Pollo`, and because he has no other suitable lands to get it from. Lines 9-12 are fragments.
- New from the key: dash = ss (`assi`), 9 = u (`una`), L = ll (`della`, `alli`), Gamma = rr (`tierras`), R-shape with a dot = ra (second form in the key row).
- Correction: that last value means `gra` in `desgracia` (same R-shape) is not supported by the key as I said; the key's gra is a different sign. The word stays doubtful. Likewise pa and pi on Lambda are hard to tell apart: the key draws pa with a colon at the side, so a Lambda with two side marks is not always pi.
- Lead, not tested: signs with two dots below may just be the plain sign. `ap` with dots below gives n in `contra` (L12), and `n` with dots below would give the first a of the c.64v passage 1 note `a Parma en nombre de la yglesia`. This could open passage 1.
- Doubtful or unread signs are listed in the file. No sign file, so no count for this block.

## 14 Nov 1549, c.60v begun (2 Nov 2026)
- `14nov1549_60v.tsv`, 96 signs: 82 with a value, 5 doubtful, 9 unread (lines 1-4 of about 28). Reads: `no seria (o mo?) que romper la guerra con [..] la yglesia, teniendo Su Santidad como agora tiene a Parma en [..] nombre della y no de la casa Ferne[..] [..]ando assi mismo que bi[..] esta empresa se [..]en`.
- Agrees with the clerk's notes on c.64v (20 Nov), `a Parma en nombre de la yglesia` and `que no se movera guerra a la yglesia`. Those are a later letter's notes; the agreement is on subject, and I knew them while reading, so it is not independent.
- `yglesia` is spelled y, g, le, si, a. The same group stands in c.60r block 2 line 9, which should now begin `de la yglesia`; not yet rewritten there.
- Correction: n with a cross is fe in the key, not fa. So `Farnesa` on c.64v and `casa Ferne..` here should both be Fer-; the spelling is the cipher's.
- `Su` in line 2 looks like clear letters with dots below, followed by an unread sign before `Santidad`, whose `sa` is a 7 with a dot rather than the key's y.

## 14 Nov 1549, c.60v lines 5-10 (3 Nov 2026)
- `14nov1549_60v.tsv`, 240 signs: 209 with a value, 18 doubtful, 13 unread (lines 1-10 of about 28). Reads from line 4's `esta empresa se [..]en`: `en favor de Ottavio como esta a la ro(?) que se hara capitulando con el, pareceria que se quisie[.]sse [..]do(?) tener y a no sa(?)r [.] de(?) rea[.] por mejor que el [.] m pe ra(?) o bien da si(?) que teniendo nos e s(?) te y [.] gualmente en Parma y en P(?)la ze(?) ncia nunca havemos querido emprender hasta qui ninguna cosa por via de [.] gue...`
- Lines 9-10 run without a gap to speak of: `en Parma y en Plazencia nunca havemos querido emprender hasta qui ninguna cosa por via de gue..`. Line 5 runs into line 6 through `capitulando con el`. Lines 7-8 up to `teniendo` do not form sentences yet.
- These lines rise to the right, so level crops lost the line ends. `comp.py` now takes a slope argument. Several signs first read from level crops changed when seen whole: `pre` in line 5 is `se`, `be` in line 9 is `ve` (`havemos`), and the tail of line 9 is `que ri do`, not my first guess `te ni do`.
- New values used: e with one dot = ha; open j drawn reversed, one dot na and two dots ni; ys with a bar = ve; Lambda with two side marks = pi in `capitulando`. Lambda with a side mark also gives pa in `Parma`, so the two are not cleanly told apart.
- 7 with two dots gives si in `yglesia`, `quisiesse`, and bi in `bi`+`en` (lines 7-8). The key table has this base as b. Whether the 7 base also serves for s is not established; `Santidad` line 2 needs it too.
- `N` in line 9 is taken as p of `Plazencia` from the word alone. It has no support in the key as I read it.
- **Lead, contradicts the earlier one.** Signs with two dots below may be nulls, not plain signs. Four of them stand where the word runs without them: inside `quisie.sse` (line 6), before `gualmente` (line 8), before `guerra` (line 10), before `nombre` (line 3). The earlier lead rests on `contra`, c.60r block 2 line 12, and the first a of the c.64v note. Recorded in the sign file as `null?`. Not tested: this rests on 4 cases chosen while reading, and `y` + null + `gualmente` is itself a guess at the word.

## 14 Nov 1549, c.60v lines 11-14 (3 Nov 2026)
- `14nov1549_60v.tsv`, 343 signs: 305 with a value, 23 doubtful, 15 unread (lines 1-14 of about 28). Reads from line 10's `por via de gue`: `guerra a vierta, esta a la ro(?) que se verna a en [.] la que [.] car el derecho que se pretende nuestra parte, allende que, capitulandose con el dicho Ottavio y muriendo el Pollo, se vernia luego a las manos con vo[.] se sso r`
- Lines 12-14 run: `el derecho que se pretende nuestra parte, allende que, capitulandose con el dicho Ottavio y muriendo el Pollo, se vernia luego a las manos`. English: the right that is claimed on our side; besides which, if terms were made with the said Ottavio and the Pollo died, it would come to blows at once. `de` is not written before `nuestra`; I read one x-stroke-o across a panel boundary.
- `Pollo` is written in clear again (line 14, as at c.60r block 2 line 5). Inference, not established from the cipher: it stands for the Pope, Paul III. `estando en desgracia del Pollo` and `muriendo el Pollo` both fit an old pope at odds with his grandson Ottavio. Paul III died on 10 Nov 1549, four days before this letter's date, which the writer could not yet have known. That date is from general knowledge and is not sourced here. Why a clear word stands in cipher is not explained.
- Correction to line 7: the signs after `de re` are u = c and the o-looped hook = ho, the same pair as line 12. So line 7 has `derecho`, not the `re a [.]` of my earlier running text. The sign file is changed.
- New values used: o-looped hook = ho; L with a p-tail = mu; 6 with a p-tail = lu; inverted T with a side mark = tra (doubtful); bare 6 = a in `a vierta`.
- `esta a la ro(?) que se` comes twice (lines 5 and 11), with different signs for `ro`. Not read: the phrase does not make sense yet, though `a lo que se` would.
- The null lead weakens: the sign read `vi` in `a vierta` (line 11) has dots both above and below, and is read as itself. In line 11 a g with o and marks stands before `car`, where a null would leave no word.

## 14 Nov 1549, c.60v lines 15-18 (3 Nov 2026)
- `14nov1549_60v.tsv`, 441 signs: 394 with a value, 26 doubtful, 21 unread (lines 1-18 of about 28). Reads from line 14's `con vo[.] se sso r`: `sin poder escusar de meter en [.] y [.]o la discussion del derecho pretendido por las partes y veniendose al [.] fin a [.] tarde dar recompensa a la yglesia en caso que se hallasse se [. . .] e l dere...`
- This is the longest connected run so far. English, with the gaps: without being able to avoid putting into [..] the discussion of the right claimed by the parties, and it coming in the end, [late], to giving compensation to the Church, in case it were found [..] the right.
- `dere` at the end of line 18 is presumably `derecho`, the third on this page; line 19 is not read yet. `tarde` is `ta r de` after an unread sign, so `a [.] tarde` is not settled, and `late` is a guess at the sense.
- Word-level checks across lines: `derecho` lines 7, 12, 16 with the same de-re-c-ho signs; `yglesia` line 18 spelled like line 1 except that g is the o-first form the key gives; L with a tick = ll in `hallasse` and `allende`.
- New values used: q with a bar = s, from `escusar` alone; 8 with a p-tail = cu; n with two dots = fi; o-first dash = g, as the key has it; y base with an o-loop = so in `caso`.
- A tall s with dots below in line 17 stands before `fin`, a fifth sign of that kind where the word runs without it. The null question stays open, see line 11.
- Line 15 `en [.] y [.]o la` and the end of line 18 are unread.

## 14 Nov 1549, c.60v lines 19-22 (3 Nov 2026)
- `14nov1549_60v.tsv`, 535 signs: 482 with a value, 30 doubtful, 23 unread (lines 1-22 of about 28). Reads from line 18's `e l dere`: `[dere]cho de las dichas tierras e l [.] da que pretenderia por otra parte ratificacion por razon de lo capitulado con el, por donde verniamos a hallarse embaraçado y car[.]gado por ambas partes [)]`
- English: the right to the said lands [..] which he would claim, on the other side ratification by reason of what was agreed with him, whereby we should come to find ourselves hampered and burdened on both sides.
- Line 19 confirms line 18's `dere` as `derecho`. `el [.] da` in line 19 is not settled, and who `he` is there is inferred.
- `hallarse` follows `verniamos` although first person would be expected. I read the signs that way and have not changed them. `embaraçado` is spelled with c, which the cipher's signs cannot tell from ç.
- New values used: R-shape with a dot = ra at the start of `ratificacion`, the same form as the key's second ra; crossed V with an o = zo in `razon`; ring with one dot = ga in `cargado`; inverted-T form with a side mark = tra in `otra`, as in `nuestra`, line 12.
- The null lead gains a second case inside a word: `car.gado` (line 22), with `quisie.sse` (line 6). The counter-cases in line 11 still stand, so it is not settled.
- A crescent stands at the end of line 22, after `partes`, with the rest of the line blank. It may be punctuation closing this cipher passage. Not established.

## The rest of the 14 Nov letter (3 Nov 2026)
- The user said to go as far as possible and publish. c.60v lines 23-28 by the main session; c.60r block 2, c.61r, c.61v, c.62r, c.50r, c.30r, c.76r and c.64r by subagents under one brief, by eye, sense in view. One line (c.61v L15) checked against its crop by the main session. The rest of the subagents' work is not checked line by line.
- All signs: 3032 (2780 value, 128 doubtful, 51 null, 25 clear words, 48 unread), `counts.json`. `build_texts.py` makes the decryption files and `validation.tsv`; `sign_values.tsv` lists every sign name with its values.
- Reading in `14nov1549_reading.txt`, English in `14nov1549_en.md`.
- The cipher runs through without a break: c.60r block 2 ends `lo qual & romper la guerra contra la yglesia o` and c.60v opens `no seria .. que romper la guerra con la yglesia`; c.60v ends `lo qual no con` and c.61r opens `vergia`.
- Pollo: c.60v L2 `teniendo Su Santidad como agora tiene a Parma`, c.62r L1 `estando Parma en manos del Pollo`, c.61v L5 `en sede vacante o en vida del Pollo`, 60v L14 `muriendo el Pollo`. So Pollo = the Pope, Paul III, inferred. He died 10 Nov 1549; the letter is dated Brussels, 14 Nov, and the 20 Nov letter deals with the vacancy in clear. Date of death: general knowledge, confirmed by Wikipedia on Ottavio Farnese / the War of Parma.
- mus/mms fits para everywhere it occurs. inta and em stand where the Church is expected, nerp where France is; vela/bela reads like a place news comes from (Rome?). All from the sense only.
- Camillo Orsini, Orazio Farnese, Dragut as named people: the reading gives Ursino and Horacio; Dragut is a guess from `Drigui`.
- Dots below: they usually drop out inside a word (siem.pre, de.llo, Par.ma, en.tre, car.gado, quisie.sse), but c.60r L12 needs g, pe, e from dotted signs, and c.64r does not read either way. Not settled.
- Corrections to earlier notes: c.64v line 1 is not a second series with dots below: its signs are plain (a Parma en nonbre de la yglesia). `saber` in 13may1549_decryption.txt is `haver`. 30sep: the signs do give `al prior de lombardia`, against the correction of 2 Nov, with the note in view.
- Validation: `docs/_validate.py` against es-golden-age passes; figures in `profile.json` outcome.validation. It tests the key as a whole, not each word.

## 14 Nov 2026: issue #618 (Brice Dudout), the Simancas sheet of 1866 for this cipher, and the code words

The sheet (one page, PDF of the Archivo General de Simancas, Biblioteca, D/00203, no. 243, "Copias de las cifras
originales"; reproduction prohibited, so only values are quoted here): `https://www.cultura.gob.es/dam/jcr:bfe499e7-ee87-4bdd-b172-d687f189a705/cifra.pdf`. Opened here
14 Nov 2026. **It is not a table of the period.** Its heading reads "Secretaría de Estado = Flandes = Leg. n.º 501:
folios 42 = 111, 157, 178, 181, 183, 187 y 188 = Abecedario y silabario sacado de documentos en cifras que hay en dichos
folios, relativos á los Secretarios Ydiaquez y Vargas para descifrar su correspondencia, la de Granvela, del Emperador y
del Principe Andrea Doria; formado por el oficial de 3.er grado Don Nemesio Ruiz de Alday en el Archivo general de
Simancas á 6 de Marzo 1866", with "Es del año de 1545" beside it. So it is an archivist's reconstruction of 1866 from
ciphered letters of 1545 that carry decipherments, which is how Satoshi Tomokiyo describes it (Cryptiana, spanish2.htm,
note of July 2020 at the end of the section on the Imperial Cipher of 1544-1554: "a nineteenth century reconstruction of
this cipher"). The issue calls it a period table; it is a second reconstruction, independent of Meister's and of
Bertomeu Masiá's, and of the two made in this repository. The copy of Tomokiyo's page cached in
`targets/vasto1527/prior/spanish2C_now.htm` has his later note (June 2026) on a sheet by the same archivist with the
same date, under another link: he sets it beside the earlier cipher Lu.31 of 1537-39, where mus for para and dis for
Armada are the same and the codes for Papa and Embajador are not. Why Luo's list and this sheet differ there is not
known.

It has an alphabet, the syllable rows, double letters, a note on nulls ("Nulo será todo lo que tubiere dos puntos debajo
… y algunos otros signos como et") and a list of code words, read here from the PDF: Alemania mi, Armada dis,
Cardenal ager, Concilio mens, dineros tus, Duque saa, Embajador quod, Embajador de Inglaterra et ud, Emperador sis,
Españoles breues, Franceses em, Francia nec (with an end mark), guerra tem, Iglesia sor, Inglaterra ca, Italia ob,
lea tu, legado ven, Levante brius, Milan mon, principe tac, necesidad tem, nuestro pre, Papa pollo, para mus, religion
dot, reino ceet, Rey deco, Rey de Francia gacez, Rey de Inglaterra et fu, Rey de Romanos mori, Señor viru, Señoria dita,
Serenissimo cia, Sicilia popli, Su Magestad dide, Su Santidad inta, tiempo du, tierra vre, tregua auze, Trento trio,
Tunez dess, Venecia ams, voluntad (b)imi, Vuestra gien, V. S. vitis, gente sem, galera tum, persona mbel, cifra con
(the rest not copied; small hand, one reader).

**Checked against keys that do not depend on it.** `wainut/key.tsv` (then `targets/ferrante1549/`) (WAINUT; built on Prince Philip's
letters to the same Ferrante Gonzaga with their contemporary decipherments, frozen before the 14 Nov letter was read)
has six code words learned from those decipherments: dide Su Magestad, quod Embaxador, gien vuestra, em franceses,
gaces Rey de Francia, mus para. The sheet gives the same value for all six. Seen here on the Estense images as well:
Philip's letter sfasc. I c. 15r has `dide`, `quod` and `tac` in the cipher where its clear slip c. 17r has "Su Magestad",
"al Ambaxador Figueroa" and "al Prin[cipe]" (issue #615). In `targets/vargas1552/` the decipherment on the letter gives
ager = Cardenal three times and pollo = Papa four times, as the sheet does.

**The code words of this target** (counts from `14nov1549_reading.txt`; the issue's counts differ by one or two):

| code | uses | read here | sheet of 1866 | other evidence | result |
|---|---|---|---|---|---|
| Pollo | 6 | the Pope, from the sense | Papa | vargas1552, decipherment of 1552 | confirmed |
| mus, mms | 6 | para, from the sense | para | ferrante1549 frozen key | confirmed |
| inta | 2 | "where the Church is expected" | Su Santidad | none | corrected: "fuera de las manos de Su Santidad", "que no fuesse Su Santidad o el Duque Ottavio" |
| em | 1 | "where the Church is expected" | Franceses | ferrante1549 frozen key | corrected: "meterle dentro en nonbre de Franceses para hazer nos alli una frontera" |
| gien | 1 | unexplained | Vuestra | ferrante1549 frozen key | settled: "con vuestra satisffacion" |
| nerp | 1 | France, from the sense | Francia is `nec` with an end mark | ferrante1549 reads the same word `nep` | sense confirmed ("el rey de Francia"); the letters of the code word differ and want a look at the image |
| et ud | 1 | unexplained | "Embajador de Inglaterra et ud"; the nulls note names `et` | none | open: neither gives sense in "las de la yglesia, de {et ud} y {tu}" |
| tu | 1 | unexplained | "lea tu" | none | open (the issue reads lea as liga, doubtful) |
| vela, bela | 2 | a place news comes from | not on the sheet | none | open |

So of nine open code words, five are settled or confirmed (16 of 21 uses), one is confirmed in sense, three stay
open. Two of the five change the reading of the 14 Nov letter: Orazio would be put into Parma "in the name of the
French", not of the Church, and Parma is to stay in the hands "of His Holiness".

**Dots below.** The sheet's note that everything with two dots beneath is null agrees with the rule kept here (dotted
signs drop out inside a word). The counter-cases, c. 60r line 12 and the end of c. 64r, were not looked at again.

**Sign shapes.** The sheet keeps `pre` (a syllable sign) apart from `de`, as `sign_table.tsv` does. Not compared row by
row: that is the next step and it is workable, because the sheet is public.

**Not done here, on purpose.** The reading files, `profile.json` `codes_open` and the read share are unchanged in this
round: the three targets that hold this cipher are to be put in order together (below), and the code values should go
into the readings once, with a strict recount, when that is decided.

**One key, three folders.** WAINUT's folder (then `targets/ferrante1549/`, in progress; now `wainut/`) reads the same letter of 14 Nov 1549, and the
passages of 13 May, 30 Sep and 20 Nov, from its own transcription and its own table, together with Philip's letters in
the same cipher. Neither folder cited the other before today. `targets/vargas1552/` is a third letter in the cipher by
Tomokiyo's identification and two code words. The recommendation written for the owner is in the round's report
(R14_ib.md); nothing is merged here.

## 14 Nov 2026 (evening): targets/ferrante1549 folded in. One key, one entry, two readings

Owner's decision on issue #618 (Brice Dudout pointed out in #615 and #618 that the two folders concern the same Campori
letters and the same cipher; the check of #615 found that both read the same letter of 14 Nov 1549). WAINUT's folder
`targets/ferrante1549/` is now `wainut/` in this folder, **as filed**: nothing in it is rewritten. Its notes and profile
are `wainut/NOTES_ferrante1549.md` and `wainut/profile_ferrante1549.json` (they keep the old folder name in their text).
WAINUT's scripts run from `wainut/` unchanged.

**What is whose.** Two readings of the same letters were made apart, on 2 and 3 Nov 2026, from separate transcriptions
and separate tables; neither folder cited the other before 14 Nov. That they were made apart is by the two records
(the files and notes of each side); it is not stamped from outside.

| part | who | where |
|---|---|---|
| Identification of the letters of 1549 to Ferrante Gonzaga as the Imperial Cipher of 1544-1554; the key images | Satoshi Tomokiyo (Cryptiana, spanish2.htm); the reconstruction pictured is Bertomeu Masiá's (2009), Meister 1906 p. 212 | `sign_table.tsv` header |
| Reading 1: transcription of five Charles letters (3,032 signs), sign table extended from Bertomeu Masiá's key as pictured, reading of 14 Nov, sign readings of 13 May, 30 Sep (first passage), 20 Nov, 23 Dec | the project | this folder, files without `wainut` in the name |
| Reading 2: transcription of twelve letters of Charles V and Prince Philip, the table `key.tsv` recovered from the contemporary decipherments of Philip's letters and frozen (`key_frozen_1547.tsv`), the held-out tests, the reading of 14 Nov, Philip c. 10r, c. 26r, c. 28r read in part, three Philip letters decoded; the marginal decipherments of 30 Sep, 20 Nov and c. 28r found and transcribed; four catalogue corrections | WAINUT (GitHub LcCompany), a Dutch AI company, with AI language-model agents | `wainut/` |
| The contemporary decipherments (slip c. 29, c. 77, c. 14r, c. 11, the margin notes) | the imperial chancery and the recipient's clerks | on the leaves |
| The same-documents link (ferrante1549 and gonzaga1549; cc. 131-132 = renard1549; 11 Aug 1542 = gonzaga1542); two more Philip letters (cc. 15-17, cc. 32-34); the Simancas sheet applied to the code words | Brice Dudout, issues #615 and #618 | sections of 14 Nov above |
| The code list used as a third witness: AGS, Biblioteca, D/00203 no. 243 | reconstruction of 1866 by Nemesio Ruiz de Alday, located by Satoshi Tomokiyo (note of July 2020); cited, not reproduced | section of 14 Nov above |
| The comparison, the carrying of the code values, the recount, the fold | the project, 14 Nov 2026 | `compare_readings.py` and its outputs |

### The two readings of 14 Nov 1549 compared (`compare_readings.py`)

Done on the files, by alignment; **no image was opened for it**. Outputs: `comparison_14nov1549.tsv` (every word of both
readings side by side, with a category and a verdict), `comparison_signs.tsv` (WAINUT's 160 key rows against the values
this folder's sign files have at the aligned places), `comparison_summary.json`.

| level | figure |
|---|---|
| signs | 2,536 (reading 1) and 2,543 (reading 2); 2,523 places aligned; **2,312 carry the same value (91.6%)** |
| words sure and the same in both | 725 |
| sure in both, close in their letters: spelling, division or one sign (ratificacion / gratificacion, hallarse / hallarnos, curar / procurar, seguro / segura are here) | 25 |
| sure in both, unlike words (de / no five times, con / contra, bien / si, hasta / hastaqui, a division) | 8 |
| sure in one, the other gives the same word with a mark (doubt, repair or proposal) | 77 |
| sure in reading 1 only | 25 |
| sure in reading 2 only | 36 |
| the same word, marked in both | 15 |
| sure in neither | 104 (mostly the 129 unresolved sign values of reading 1) |

The alignment is by similarity, so these are close figures, not exact ones.

**Differences between two sure words: 33, of which 10 settled, 23 open.** A difference is settled only where a
contemporary decipherment decides the value, or the two readings have the same letters and differ in division, or one
reading's own sign file decides it. No difference was settled on the sense alone.

| reading 1 | reading 2 | verdict | basis |
|---|---|---|---|
| ratificacion | gratificacion | settled: gratificacion | the sign R is gra in the contemporary decipherments of Philip's letters (WAINUT's frozen key); reading 1 needs gra for the same shape in desgracia |
| a [.] tarde dar | a tratar de dar | settled: tratar de | same signs ta r de; reading 1 had the sign before unread and divided wrongly |
| que bien esta empresa; bien nuestro nombre | que si esta empresa; si en nuestro nonbre | settled: si, si en | the sign (7 with two dots) is si in yglesia and quisiesse in reading 1 itself |
| con la yglesia | contra la yglesia | settled: contra | reading 1's sign file has an unread sign between con and la (c.60v line 1) |
| consta re-estar; fines que; hasta qui; assi mismo; haver lo; sobre ello | constara estar; fin es que; hastaqui; assimismo; hauer lo; sobrello | settled (division) | the same letters |
| Ottavio (9), remittimos (2) | Octauio, remictimos | **open** | one sign: tt in Bertomeu Masiá's key as pictured on Cryptiana, ct in WAINUT's table (a value from this letter). The word is the same |
| de / no (5 places: "forma de haver", "no la tiene", "no haviendo", "si no las", "no se tomasse") | no / de | **open** | the two signs (X and x in WAINUT's names) are exchanged; the sense favours reading 1 at these five places; a look at the image decides |
| hallarse | hallarnos | **open** | one sign; the first person is expected after verniamos, and reading 1 noted that |
| de curar | procurar | **open** | xo = pro is in WAINUT's frozen key; x with an o-loop = de in the key as pictured. Sense favours procurar |
| apuntar, pretende, dezes, seguro (… justificada) | apontar, pretiende, dezis, segura (… justificado) | **open** | one vowel mark or one sign each |
| nombre | nonbre | open (spelling) | |

Other points the comparison shows, none settled here:
- Where reading 1 has sign values that do not form words (129 tokens, now enclosed in ‹ › in `14nov1549_reading.txt`),
  reading 2 mostly has words: "sostener y aprobar su derecho por mejor que el imperio", "esta claro que", "enflaquecer el
  derecho", "con su sucessor … meter en juyzio", "es de creer que por pura imposibilidad", "al cabo con su aguelo",
  "no podemos dexar de approbarle", "encargamos con toda eficacia", "muy gran aduertencia", "el sucesso", "la tregua".
  Several of these are repairs or proposals in reading 2. They are the lines to reread with both tables.
- Where reading 2 has a proposal or a hole, reading 1 is sure at 25 places: quedava ([?quedays]), voluntad
  ([?somontado]), "sacar la gente" ([...]), "como desesperado" ([?nos] [?es] esperado), meterle (meterse), "hazer nos alli"
  ([?desde]), sacaria (saca).
- The end of c.60r: reading 1 counts "lo qual & romper la guerra contra la yglesia o" as text and c.60v repeats the words;
  reading 2 takes the line (A19) as a repeat struck by the clerk and leaves it out of its count.
- Tables (`comparison_signs.tsv`): of WAINUT's 160 rows, 124 occur in this letter; at 93 of them the project's sign
  files have the same value at more than half the places (the code-word rows count as different only because the
  sign files hold the code word itself). Systematic differences: `+` ct / tt (11 places), `fh` f / ff (4), `R` gra / ra
  (2), `N` pl / p doubtful (4), `X` de and `x` no exchanged at 11 places, `ys` su / unread or ua (7 of 8), `v` do / bare d
  (8; WAINUT marks these as repairs), `xo` pro / de or no (2 of 3). `9` (d and u) and `c` (rr and c) are doubtful in both.
- 13 May 1549: both sign readings give "haver los dineros" where WAINUT's transcription of the slip has "sauer" (the
  project first read "saber" there too). 30 Sep, first passage: the same text in both, Brissiuc / Brissiu, and one unread
  sign in reading 1. 20 Nov: reading 1's "‹qui si ss e [.] mos› mover guerra" stands where the margin has "que no
  queremos mouer guerra". WAINUT found seven marginal decipherments on the 30 Sep letter and six on 20 Nov; the project
  had read one cipher block of 30 Sep and five passages of 20 Nov. (Claims review, 14 Nov 2026: WAINUT's own files
  disagree on 30 Sep. `wainut/reading_ch1549_0930_1120.md` lists seven; the status table of
  `wainut/NOTES_ferrante1549.md` says six and `wainut/clear_margins_charles.txt` has six lines, M2 missing. Left as filed.)

### Code values carried into both readings

| code | value | basis | reading 1 | reading 2 |
|---|---|---|---|---|
| Pollo | Papa | Simancas list of 1866; decipherment of 1552 in vargas1552; both readings | 6 uses | 6 |
| mus, mms | para | WAINUT's frozen key (contemporary decipherments); list of 1866 | 6 | already para |
| inta | Su Santidad | list of 1866 | 2 | 2 (was [?la Yglesia]) |
| em | Franceses | WAINUT's frozen key; list of 1866 | 1 | already franceses |
| gien | vuestra | WAINUT's frozen key; list of 1866 | 1 | already vuestra |
| saa | Duque | list of 1866; the gloss "Duq octauio" over the sign on c.76r; reading 1 | 1 | 1 (fills the hole at A03, `5 a a`) |
| nerp / nep | Francia | both readings by the sense; the list has Francia as nec with an end mark | 1 | 1 (was [?Francia]) |
| vela / bela | open | not on the list; "Roma" is WAINUT's proposal | 2 | 2 |
| et ud, tu | open | on the list as Embajador de Inglaterra and lea; no sense here | 2 | 1 hole |

The project's reading file carries them as `{code = value}`. WAINUT's filed reading is not touched: the same text with the
three changed values is `14nov1549_reading_wainut_codes.md`, written by `compare_readings.py`.

### One strict recount per document

Rule (README Conventions, the read bar): sure words only. Reading 1: a word with (x?), [.], an open {code}, or inside
‹ › is a hole. Reading 2: a repair (°), a proposal [?word] and [...] are holes. A settled code word counts.

| document | reading | strict | other figures, once |
|---|---|---|---|
| Charles, 14 Nov 1549 | 1, the project | 837 of 1,007 tokens, **83.1%** | 129 of the tokens are sign values, not words, so the share of words is higher than this; the 93.4% carried until today was the share of *signs* given a value |
| Charles, 14 Nov 1549 | 2, WAINUT | 817 of 910 words, **89.8%** (811 before the code values) | WAINUT's "with repairs": 864 of 910, 94.9%; Brice Dudout's rerun with the code values: 867 of 908, 95.5% (his file not sent) |
| Charles, 13 May 1549 | 1, fitted to the slip c. 29 | 45 of 45 | |
| Charles, 23 Dec 1549 | 1, fitted to c. 77 | 46 of 48 | passage 2 lines 2-3 not transcribed |
| Charles, 30 Sep 1549 | 1, first of seven passages, margin in view | 33 of 35 | the other six passages: WAINUT's blind pass, unrepaired, and the margins |
| Charles, 20 Nov 1549 | 1, fitted to the margins | 49 of 65 | two lines of c.64r unread, not in the count |
| Philip, 4 Aug 1548, c. 10r | 2 | 75 of 80, 93.8% | with repairs 78 |
| Philip, 24 Nov 1551, c. 28r D-E | 2 | 56 of 66, 84.8% | with repairs 62 |
| Philip, 24 Nov 1551, c. 26r | 2 | 75 of 91, 82.4% | with repairs 82 |

**Class: read in part.** No letter without a contemporary decipherment reaches 95% in either reading. 13 May and 23 Dec
reach it, with the chancery's own decipherment beside them. The two readings together would cover more (reading 2 is
sure at 36 word places where reading 1 is not, reading 1 at 25 where reading 2 is not), but a joint text has not been
checked on the image and is not counted.

### Philip's letters (catalogue 1561), now documents of this entry

All WAINUT's work; details in `wainut/NOTES_ferrante1549.md`.

| document | state | strict | files in `wainut/` |
|---|---|---|---|
| 4 Aug 1548, Felipe II sfasc. I c. 10r | read in part | 75/80 | `reading_1548_c10r.md` |
| 24 Nov 1551, c. 28r, passages D and E | read in part | 56/66 | `reading_1551_c28r.md` |
| 24 Nov 1551, c. 26r | read in part | 75/91 | `reading_1551_c26r.md` |
| 8 Mar 1549, c. 12r | covered by the decipherment on c. 14r; the table was built on it | | `transcription_1549_c12r.txt`, `clear_1549_c14r.txt` |
| 23 May 1547, cc. 9r-9v | covered by c. 11; table extended on it, lines 11-16 of 9v held out | | `transcription_1547_c09.txt`, `clear_1547_c11.txt` |
| 25 Jun 1546, 14 Mar 1553, the letter catalogued 16 Jun 1563 | decoded from one rough blind pass, not read | | `decryption_philip_1546_1553_x_blind.txt` |
| cc. 15-17 (cipher and clear slip), cc. 32-34 (Monzón, 6 Oct 1552) | not transcribed (issue #615) | | |

WAINUT's catalogue corrections stand: marginal decipherments exist for c. 28r and c. 64v and for every passage of
30 Sep and 20 Nov; c. 14r begins "De Su Mt."; the copy on c. 12r is not abridged; the letter catalogued 16 Jun 1563
opens "El Principe" and is addressed to Ferrante (died 1557), so it is not of 1563.

### WAINUT's frozen key and held-out tests: the validation evidence

Reading 1 had no frozen-key test (its statistical validation tests the key as a whole). Reading 2 has them, with
their real results:

| test | table | reader | letters in order | runs of 4+ | 200 shuffled tables, max | result |
|---|---|---|---|---|---|---|
| Philip 23 May 1547, 9v lines 11-16 | frozen | not blind | 0.888 | 0.857 | 0.418 / 0.239 | above the controls |
| Charles 13 May 1549 | frozen | not blind | 0.978 | 0.932 | 0.431 / 0.374 | above the controls |
| Charles 30 Sep 1549, 408 signs | frozen | blind (no table, no clear text) | 0.728 | 0.595 | 0.420 / 0.532 | above the controls on both |
| Charles 20 Nov 1549, 140 signs | frozen | blind | 0.652 | 0.323 | 0.519 / 0.355 | above on order, **fails on runs of 4+** |

The two blind rows were rerun here after the move (`python wainut/scripts/score_blind.py key_frozen_1547.tsv`): the same
figures. The two rows that are not blind were not rerun. WAINUT declared no pass bar beforehand, so these are held-out
tests against shuffled controls, not pre-registered tests. That the table was frozen before the Charles letters were
opened is by the contributor's record. WAINUT's own blind checks of the 14 Nov reading: a second reader without the
table agrees on 80.8% of 2,132 signs (A08-D23); an independent reader with the table in view differs on 39 of 425 signs
(D14-E03); on c. 10r at half scale 43 of 212 signs differ. A second measure now exists that neither side made: the
91.6% agreement of the two transcriptions above.

Six code words of the frozen key (dide, quod, gien, em, gaces, mus) have the same value on the Simancas list of 1866.

### Outcome method, per part

- Reading 1 of 14 Nov: read after matching with key from external sources (Bertomeu Masiá's reconstruction as pictured by Tomokiyo).
- Reading 2 of 14 Nov and Philip c. 10r, c. 26r, c. 28r D-E: key recovered based on adjacent plaintext (WAINUT, from the decipherments on c. 14r and c. 11).
- 13 May, 30 Sep, 20 Nov, 23 Dec 1549, Philip 8 Mar 1549, 23 May 1547, c. 28r passage C: read from existing decipherment (the chancery's slips and margins).

`vargas1552` stays a separate entry (the same cipher by Tomokiyo's identification and two code words; no sign of it is
transcribed), cross-linked.

## Remaining gaps
- 14 Nov 1549: 23 differences between sure words of the two readings (Ottavio / Octauio and remittimos / remictimos; de / no at five places; hallarse / hallarnos; procurar / de curar; four vowel marks) and the systematic table differences (R, N, f / ff) - blocker: not-attempted; each is one sign on the Estense images, which are open; `comparison_14nov1549.tsv` lists the places
- 14 Nov 1549, reading 1: 129 tokens of sign values that do not form words (c.60v lines 7-8 and 23-27, c.61r L4-5 and L16-18, c.61v L18 and others) - blocker: not-attempted; reading 2 gives words at most of them, not yet checked sign by sign against the sign files of reading 1
- 14 Nov 1549, reading 2: 53 repairs, 38 proposals, 2 holes (A14 `lalgunte`, A16 `et ud y tu`); differences of WAINUT's blind pass on A08-D23 not all settled; A00-A07 one pass - blocker: not-attempted; reading 1 is sure at 25 of these places; a zoom reading of A00-D13
- Code words: vela/bela, et ud, tu, and the letters of nerp / nep - blocker: open-codes; not on the Simancas list of 1866 or not making sense with it
- 20 Nov 1549, last two lines of c.64r; 30 Sep and 20 Nov not yet editions (reading 1 has the first of seven passages of 30 Sep; WAINUT's blind pass covers all, unrepaired) - blocker: not-attempted; the marginal decipherments give the text, a line-by-line sign pass is owed
- Philip c. 10r, c. 26r, c. 28r: one primary pass each; the vicariate passage on c. 26r is unsafe - blocker: not-attempted
- Philip 25 Jun 1546, 14 Mar 1553, the letter catalogued 16 Jun 1563: decoded, not read - blocker: not-attempted; need a pass in a named sign set
- Philip, sfasc. I cc. 15-17 (cipher c. 15r, clear slip c. 17r) and cc. 32-34 (Monzón, 6 Oct 1552): not transcribed (issue #615) - blocker: not-attempted; the first is a third pair for the key or a second held-out test
- Bertomeu Masia 2009, Corpus documental de Carlos V vol. III, Druffel, the Simancas minutes (Estado 1196) - blocker: needs-physical-access; not online; whether the 14 Nov letter or its minute is printed is unknown
- 15 Jul 1549 and 11 Aug 1542 numeric, 1 Jul 1552, cc. 131-132 - blocker: no-key-material; other ciphers, not part of this entry (`gonzaga1542`, `renard1549`)

## Escalation
- [x] siblings: c.29, c.41, c.77 used; c.82-83 (1 Jul 1552) is another sign set; c.64v and c.50r margins used. WAINUT fetched all listed letters of catalogue 1560 and 1561 and built the table on Philip's letters with a decipherment
- [ ] siblings, 14 Nov 2026 (issue #615, Brice Dudout): Philip sfasc. I cc. 15-17 and cc. 32-34 opened, neither transcribed; the other Felipe II records of the search (39 in all) and the other Karl V items (151) not opened one by one
- [x] clear-pages: the slip c.29, c.77 and the margin notes are the decipherments; c.62r-62v clear text read for context; WAINUT found the marginal decipherments on c. 28r, c. 64v and on every passage of 30 Sep
- [x] known-keys: Meister and Masia/Tomokiyo images of the Imperial Cipher; the 1548 numeric key belongs to 15 Jul only; WAINUT checked the repository keys (mendoza1548 is the same chancery syllabary, not compared value by value)
- [x] known-keys, 14 Nov 2026: the two tables of this entry compared on the 14 Nov letter (`comparison_signs.tsv`); the code list of the Simancas reconstruction of 1866 used for the code words
- [ ] known-keys: the syllable rows of the Simancas reconstruction of 1866 not compared with either table; it could decide tt / ct, f / ff, R and N
- [x] print: Cryptiana read; CSP Spain IX, CSP Venice V and the DBI opened by WAINUT; Bertomeu Masia 2009, Corpus documental III, Druffel and the Simancas minutes not
- [x] key-rebuild: reading 1 extended by hand to 277 sign names; reading 2 rebuilt from the contemporary decipherments and extended on 14 Nov
- [ ] retry, 14 Nov 2026: the open differences and the unresolved lines of reading 1 are to be reread on the image with both tables in view; not done in the round of the fold
- [x] retry: c.60r block 1 unread signs, c.60r block 2, c.30r and c.50r retried with the extended table; WAINUT reread ten lines at zoom after its independent check
