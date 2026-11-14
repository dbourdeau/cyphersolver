# coloma1622: the Marquis of Mirabel to Carlos Coloma, Lyon, 8 December 1622 (BNE RES/227/122; catalogue 1601)

Status: read in part (Brice Dudout, 13 Nov 2026; **346 of 421 cipher words sure = 82.2%** at the integration of 13 Nov, counting sure words only: the certain words of the word table except 'casa' (code _60_ placed by the sense); probable, restored and unresolved words are holes. The word table has 347 certain, 42 probable, 28 restored, 4 unresolved; the contributor's count of certain + probable is 389 = 92.4%. Key partial by the contributor's protocol, two of four measurements failed: C02 0.761, H3 0.690, H5 0.814 on characters against contemporary clears). See the integration checks of 12 and 13 Nov 2026. **Second document since 14 Nov 2026 (PR #560, folded in, one key one entry):** the Marquis of Mirabel to the Count of Gondomar, Paris, early 1622 (BNE MSS/18428, viewer images 13 right - 15 left; files in `mss18428/`), read in part, **182 of 250 cipher words sure = 72.8%**; its extended key CLE_M02 failed one measurement (M01) and is partial on the other (M02): not validated. See the integration check of 14 Nov 2026.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents (and, on 11 Nov 2026, one text-only Claude Fable 5.2 run). Catalogue entry 1601 (Chrome pass, BNE Digital).
The key comes from the Duke of Feria's letters to Coloma (lead 1602), whose cipher passages carry a contemporary clear in the
margin, and the last test used one page of BNE MSS/18428 (Mirabel to Gondomar, lead 1271).

## Document

Madrid, BNE RES/227/122 (Mss. 18.692), 2 leaves (BNE Digital, CC BY 4.0). Antonio Dávila y Zúñiga, Marquis of Mirabel,
Spanish ambassador in France, to Don Carlos Coloma, Spanish ambassador in London; Lyon, 8 December 1622. Clear opening and
close; the body in cipher: 969 tokens (f.1r 25 lines, f.1v 36 lines), plus two tokens read on the image that were missing
from the frozen transcriptions. Signature and postscript autograph.

The scans are not kept in the repository. The site write-up shows one crop (f.1v ll. 1-7, viewer image 6), credited, under BNE Digital's CC BY 4.0; it was captured from the viewer in Chrome (a plain curl gets a 403 from Cloudflare), so a sweep of BNE Digital should go straight to Chrome.

## System and key (`key.tsv`, `validation.txt`)

A syllabary on a grid (fV = tV, xV = nV, cVr = rV, xVr = sV, sVr = cV, sVn = pV, fVn = pVr, frV = gV, Vs = mV), two-digit
numbers for letters and syllables, three-digit numbers and underlined tokens for code words (309 negocio, 204 estado,
_123_ Duque, 308 nuestro señor…), and the ligatures faz / fez / fuz = que. Marked signs are distinct signs (▽ ≠ V, 94‡ ≠ 94,
20ʳ ≠ 20, checked on the clears of RES/227/128-129). `key.tsv` is CLE_C04, the last frozen key.

| test | held-out passage | key | characters | best of 200 controls | result |
|---|---|---|---|---|---|
| C01 | Mirabel f.1v ll. 12-21 (no clear; M5) | K-C01 | M5 0.333 | 0.169 | failed |
| C02 | Feria, RES/227/127 f.1r | C02 | 0.761 | 0.437 | partial |
| H3 | Feria, RES/227/128 f.1v | C03 | 0.690 | 0.419 | failed (gap 0.271) |
| H4 | MSS/18428 p. 15 left | C04 | - | - | no measurement: the margin was the verso seen through the paper; reserve burned |
| H5 | MSS/18428 p. 44 right | C04 | 0.814 | 0.466 | partial |

Thresholds fixed in advance: >= 0.85 and >= 0.30 above the best control. **Partial by our protocol, not validated.**

## Reading (`reading.md`, `translation.md`)

| version | words | certain | probable | restored | unresolved | certain + probable | with restored |
|---|---|---|---|---|---|---|---|
| 5 Nov 2026 (PR #279) | 425 | 338 | 37 | 29 | 21 | 375 = 88.2% | 404 = 95.1% |
| 11 Nov 2026 (PR #417) | 421 | 337 | 47 | 31 | 6 | 384 = 91.2% | 415 = 98.6% |
| 13 Nov 2026 (this version) | 421 | 347 | 42 | 28 | 4 | 389 = 92.4% | 417 = 99.0% |

The last two columns are the contributor's count. **Counting sure words only, the share is 346/421 = 82.2%** (13 Nov table;
integration check of 13 Nov below). The figure of 12 Nov, 349/421 = 82.9%, was taken by a looser rule that also counted 13 probable
words read with the key (integration check of 12 Nov below); it is kept there as history.

**Read in part** (`reading_review` grade B). 5 Nov: a blind shape sheet of 16 questions (M16, pre-registered and hashed
before it was built, shapes only), answered by Brice Dudout, confirmed the transcribed token in eight places and moved
"puede" and "cosa" to probable. 9-11 Nov (details and SHA-256 in `BLIND-REREADING.md`): 141 = ello and 318 = oficio held by
the contemporary clear of MSS/18428 fol. 31; code values proposed by a text-only Claude Fable 5.2 run from sense and the
alphabetical order of the nomenclator (30 ALLA, 35 AMISTAD, 48 TRATA, 52 CRISTIAN, 127 DIFICULTAD, 40 BAJO, 264 HONRA,
295 MANDA, 53 CARDENAL, L/54/y "religion catolica romana"; one place = restored, two places = probable); a blind sheet
FL2-C on the signs these proposals depend on (controls 2/2; 3 points for, 4 against, 5 new marked signs); and a blind sheet
FS1 of four conjectures by sense (controls 2/2; 4 of 4 shapes confirmed: "hízosele", "deseaba", "bastaría", "este Rey"),
each word at best probable. Unresolved now: 39 (two places), bo, 2, "[ge]ia" and "z cer zan".

**Content.** Mirabel reports Louis XIII's proposals to the Duke of Savoy (restitution of the Valtellina, help in case of a
rupture, the enterprise of Geneva), the French answer, and the Duke's return home from Avignon. He then reports his talk with
the Queen Mother on the deposit of the Valtellina forts, a Lorraine garrison and the "capitulaciones de Aranjuez", and
describes Richelieu: "although he is not of this King's Council, it is he who governs the Queen Mother".

## Declared deviations

1. **The key is not validated.** Of four measurements, two are partial and two failed (C01, H3). A fifth reserve (H4) was
   burned without a measurement: its margin was the verso seen through the paper, not a contemporary clear. That rule was
   fixed in advance, so H4 was not replaced that day; a dark-ink test was added by a hashed amendment before H5.
2. **Three marked signs have no value.** On the shape sheet the reader saw a mark the pre-registration did not foresee: 4‡
   ("4+", a barred 4) in *grande*, q̲ ("shape 2 with an extra stroke below") in *libre*, and x̤ ("x with two dots below") in
   *llegase*. In this cipher a mark makes a different sign, and these three are in no key or clear we have, so the three
   words stay restored. Ignoring the marks would have given 88.7% on the 5 Nov count.
3. **About ten restorations correct a transcribed token from the sense**; the sheet confirmed the token in eight of them.
4. **C01's held-out lines are part of the target letter** (measured with an earlier key, then read with the later one).
5. **One reader**: an AI agent transcribed and read; Brice Dudout answered the shape sheets only (M16, FL2-C, FS1). No palaeographer checked.
6. **Position bias on the sheet FS1.** After the shuffle, the six expected shapes (4 conjectures + 2 controls) all fell in
   position "shape 3" (chance about 0.14%), and all six answers are "shape 3", so on that sheet the controls cannot tell a
   reading of the shape from an answer by position. Brice Dudout confirmed afterwards that he chose each answer by the
   shape. The 4 words it moved (+4 probable) rest on that confirmation; without them: 380/421 = 90.3%.
7. **Machine proposals.** Most new code values (section above) are proposals of one text-only Claude Fable 5.2 run, from
   sense and the order of the nomenclator (order test on the 37 values held by a clear: tau 0.750 vs at most 0.463 for 200
   shuffled controls; 14 of our 16 earlier sense values fall in their code's window, controls max 11). Only 141 and 318
   rest on a contemporary clear. Values at one place cannot be tested and stay restored. The exact figures of the order
   test are not reproducible from the repository, and two proposals do not fit strict order (integration check below).
8. **Two counting rules.** The class rule of the word table ("probable = two places or more, or a near spelling") makes
   probable three xe words (xe for xer = se) that the M16 pre-registration kept restored, and three two-place proposals
   (trata, trataba, cristianos). Under the stricter count: 378/421 = 89.8%. Read in part either way.
9. **Not read: two studies.** M. Á. Guill Ortega, *Carlos Coloma* (2007), and Herrero García (*Avisos*, 2023, on the
   Mirabel-Gondomar letters of MSS/18428: its page blocked our fetch) were not read, nor a full index of the *Colección de
   documentos inéditos*. If either prints this letter or its key, we will credit it.

## Remaining gaps

- 4 unresolved words (bo, code 2, "[ge]ia", "z cer zan") - blocker: open-codes; one place each, in no clear we have (39 resolved 13 Nov).
- 21 probable words that are code values placed by the sense (caso, casos, empresa, Reina, Duque, estado, govierna, confianza; and the 11 Nov proposals trata, trataba, Cristianísimo, cristianos, allanar, allanado; nuestro señor, buena, buenos, capitulaciones and fuertes are held by clears since 13 Nov) - blocker: open-codes; not counted as read; a contemporary clear with these codes would settle them.
- the BNE images, the clear of MSS/18428 fol. 31, the clears of MSS/18428 aligned on 13 Nov (v5 d - v7 d, v33 g, v39 d - v40 g) and the raised sign on the two 34 of the letter were not seen by the project - blocker: needs-physical-access; BNE Digital answers 403 (Cloudflare) to a plain fetch (again on 13 Nov 2026) and no browser session was available at either integration; the blind sheets, their rules, maps and answers are not in the repository, so the hashes and "rule hashed first" are by the contributor's record.
- 28 restored words, among them the code values at one place (127, 40, 264, 295, 35, 53 twice, K, 68, 81, 139, 317, R, 62, L/54/y) - blocker: open-codes; none of these codes occurs in the clears of RES/227/120-129 or MSS/18428 (all seven cipher letters of MSS/18428 now aligned, 13 Nov); a new letter of the system with a contemporary clear is needed.
- The marked signs q̲, x̤ and those seen on FL2-C (4‡ = g since 13 Nov) (barred 0, xo with a v above, o with a cross, "fov") - blocker: open-codes; no value in any key or clear we have, except that the clear copies of MSS/18428 give an o with a cross = t ("trae", "ministros"; PR #560, by the contributor's record); whether the FL2-C sign of this letter is that sign was not checked.
- MSS/18428 letter (images 13 right - 15 left, `mss18428/`): 20 unresolved words (codes 24, 322, _1_, _13_, _41_, md, 87, 48~ and a few signs), 11 restored and 36 probable (signs with no value read by sense: xix, c̣ir, f‡, fir, fizt, 20~, g‡, p‡, D‡, x‡, zan; code _A_ Reina) - blocker: open-codes; none of these is in a clear of RES/227/120-129 or MSS/18428, and no unseen passage of the system is left in MSS/18428 to test the extended key; a letter of the system with a contemporary clear elsewhere (Gondomar papers, Real Biblioteca; Coloma's papers) is needed.
- MSS/18428 letter: the images not seen by the project (BNE Digital 403 to a script again on 14 Nov 2026); part B in one transcription pass; the tests' files (pre-registrations, scripts, hashes) are in the contributor's working folder, so their order is by the contributor's record - blocker: needs-physical-access.

## 13 Nov 2026: the other contemporary clears of MSS/18428

Every cipher passage of BNE MSS/18428 that carries a contemporary clear was aligned with it (learning only: the volume had been
seen at the inventory of 9 Nov, so no held-out passage is left in it and nothing was measured; the key file stays C04). The
values below are read directly on a clear of the time, the same status as 141 = ello and 318 = oficio (fol. 31). Views are the
BNE Digital image numbers; the scans are not in the repository.

| clear (MSS/18428) | cipher | clear | value |
|---|---|---|---|
| copy v39 d - v40 g of the letter of 17 Mar 1622 | xo chu _140_ zen fi x̣o **_39_** fi Δ fo xo Δ | no fuera pequeño **bien** que esto nos | **_39_ = BIEN** |
| same | car x̣ **_49_ 30** sor fri 93 | (si allaran) **buena** acogida | **_49_ = BUEN** |
| same | 78 f **_56_** sir 62 x Δ for as n cir m | las **capitulaciones** de Madrid | **_56_ = CAPITULA** |
| same | 78 98 69 xar as f **225** san car 78 | la causa mas **fuerte** para la | **225 = FUERTE** |
| same; margin v6 g | fi **308** Δ _136_ ; 94 fo 96 f **308** f ; se 84 fa 8 **308** f | porque **nuestros** enemigos ; de todos **nuestros** emulos ; el estar **nuestras** armas | **308 = NUESTRO** |
| copy v33 g of the letter v34 d | 62 g cer xir 96 se tu **308 34ʳ** fi xo car fi chi 98 car | ofrecido el Rey **nuestro S.r** que no ratificara | 308 34ʳ = nuestro señor (34ʳ = SR, as in key C04) |
| margin v6 d | sor tt 81 f **4‡** c̣ir xor xe Δ | con los **G**risones | **4‡ = g** |
| margin v5 d | 55 tt **y** c̣ir xor xe Δ | en **G**risones | y = g (homophone) |
| margin v7 d | xer 66 **60** 40 | se ve**i**a | **60 = i** |
| margins v39 g, v6 g, v7 d; v5 d, v34 d | 66 **sa** fo 80 xa ; **sa** 98 8 ; **sa** _136_ ; f fi **+** 81 ; fe x̣ fi **+** | Valtolina ; alçar ; al enemigo ; aqui lo ; que aqui | sa = al ; + = i after qu |

Also confirmed: _141_ ELLO (three more places), 202 ESPAÑA, 213 FRANCIA, 221 FUERZA, 246 GENTE, 260 HECHO, 261 HEREGE, 280 ITALIA,
_136_ ENEMIGO, _89_ CUYDADO, _100_ DIOS, _113_ DUQUE DE FERIA (three places), 319 OTRO, ar = ma, fi = que.

Effect on the letter (`reading.md`): 1r.06 "o **bien** en caso de rompimiento" (unresolved -> certain); 1r.18 "el Cardenal _39_ 55"
= BIEN + e = "**viene**" (unresolved -> probable: the code used for its letters, as _60_ CAS- and _141_ d-ELLO-s); 1r.07 "{hizo}
{grande} instancia" (restored -> probable: 60 = i and 4‡ = g held by clears; the barred 4 of this letter is the "4+" seen blind
on sheet M16, and the shapes were compared by the agent, not blind). **The two 34 of the letter carry a raised sign** (seen on the
image, 13 Nov; transcribed plain 34 before) and both follow "se tu 308" = el Rey nuestro, as in v34 d: so 1r.12 reads "el Rey
nuestro señor, **en** que esperaba" (the certain word "bien" becomes "en") and 1v.17 "el Rey nuestro señor {había} dudado"
(restored "havia", mechanical "biavia", becomes a-ui-a = avia, probable). Words held by these clears move from probable to
certain: nuestro señor (twice, 4 words), buena, buenos, capitulaciones (twice), fuertes. Count: 421 words = 347 certain,
42 probable, 28 restored, 4 unresolved; 389 = 92.4% (99.0% with restored). The same rule as the integration check of 12 Nov
(the README read bar) gives 363/421 = 86.2% (349 + 14: bien, viene, nuestro señor x2 = 4 words, buena, buenos, capitulaciones
x2, fuertes, grande, hizo, havia); this recount is the contributor's.

Still under 95% (400 words needed, 11 more). Nothing in the clears of RES/227/120-129 or MSS/18428 for: _53_ (twice), 295, 2,
bo, ge, "z cer zan", 127, _40_, 264, _K_, _R_, _68_, _81_, _139_, 317, _35_, _62_, L/54/y, 48, _52_, _30_, _60_, _123_, _A_/_L_,
204, 250, _79_, _138_, q̲, x̤. The one cipher letter of the system in MSS/18428 without a clear (v13 d - v15 g, about 35-40 lines)
cannot settle a code value; it is the only passage of the system never decoded, so it is kept for a future lexical test.

## Integration check (13 Nov 2026, PR #543)

- **Counts reproduce.** The word table of `reading.md` (426 rows, multi-word rows counted as words) gives 421 words = 347
  certain, 42 probable, 28 restored, 4 unresolved. Against the table of 12 Nov exactly 13 rows change: 39 bien (unresolved ->
  certain), hizo and grande (restored -> probable), the two "308 34ʳ" nuestro señor (probable -> certain; the following
  certain "bien" becomes "en", same count), viene (unresolved -> probable), buena, buenos, capitulaciones twice, fuertes
  (probable -> certain), havia (restored -> probable). 337 + 1 + 4 + 2 + 2 + 1 = 347.
- **Second decoder.** Written from `key.tsv` plus the values the reading now takes from clears (_39_ BIEN, 4‡ g; the que
  ligatures; 141 ELLO): it reproduces the values column of `decryption.txt` on 414 of 423 rows; the other 9 are notation
  only (img: prefix, A>B re-readings, 141 written as a code). So `decryption.txt` is no longer the mechanical output of
  `key.tsv` alone: _39_ = BIEN and 4‡ = g are not rows of the key, and the clears give 308 = NUESTRO (nuestros enemigos,
  nuestras armas) where the key row has NUESTRO SEÑOR. The key rows stay C04 by design; the key header now lists these.
- **Alignments.** The clear passages as transcribed in the 13 Nov table decode with the key rows consistently where the key
  has values (car x̣ _49_ 30 sor fri 93 = ra·?·BUEN·a·co·gi·da "buena acogida"; 78 98 69 xar as f 225 san car 78 =
  la·ca·u·sa·ma·s·FUERTE·pa·ra·la; xer 66 60 40 = se·u·i·a "se veia"). The clears themselves were not seen (BNE Digital 403
  on 13 Nov 2026; no browser session), so the alignments and the raised sign on the two 34 are by the contributor's record.
- **Learning only.** No held-out passage is left in MSS/18428; nothing was measured; the key's test record is unchanged.
- **Strict count: 346/421 = 82.2%.** Sure words only (the owner's rule of 13 Nov for all targets): the 347 certain words except
  "casa" (code _60_ = CAS, placed by the sense, as on 12 Nov). The contributor's "363/421 = 86.2% by the README rule" is the
  looser rule of the 12 Nov integration (which also counted 9 probable words read with the key through a spelling or doubtful
  token and the 4 FS1 words) plus 14 words: the 10 moved to certain and 4 that stay probable (hizo and grande rest on 60 = i at
  one place and on a shape of 4‡ compared by the agent, not blind; havia on the raised sign seen by the agent; viene on code 39
  used for its letters). Under the strict rule the 13 earlier probable words and those 4 are holes. Not used.
- `_check_reading.py` on the 13 Nov files: 81 of 251 sentences clean, 0.323 (the notes added to `reading.md` add sentences; 72 of 206 on 12 Nov).
- Still under 95% (400 sure words needed, 54 more). The open codes and signs are as listed in the section of 13 Nov above.

## Integration check (12 Nov 2026)

On integration of PR #417 the project recounted the files; an independent verifier's report is the basis of this section.

- **The contributor's counts reproduce.** The word table of `reading.md` gives 421 words = 337 certain, 47 probable,
  31 restored, 6 unresolved (384 = 91.2%; 415 = 98.6% with restored), and the table of `origin/main` gave 425 = 338 / 37 /
  29 / 21 (375 = 88.2%). The table covers the transcription in order (975 tokens). Exactly 4 tokens of `transcription.txt`
  changed (1v.05, 1v.10, 1v.14, 1v.18, the four FS1 re-readings). `validation.txt` gains three lines; the tests are unchanged.
  A second decoder written from `key.tsv` reproduces the values column of `decryption.txt` on 423 of 423 rows, once the que
  ligatures (faz / fez / fuz, not rows of `key.tsv`) and the four FS1 re-readings are applied.
- **The figure published is 349/421 = 82.9%, read in part.** The README read bar counts a word only if it is not a hole, not
  restored, and not a nomenclator value given by the sense. Rule applied, on the word table as it stands:
  - counted: the certain words (337) except "casa" (code _60_, see below), so 336; the 9 probable words read with the key
    through a spelling or a doubtful token (el, Ginebra, proposición, ministros, puede, cosa, confianza written out,
    resolvió, nada); and the 4 words re-read blind on sheet FS1 (hízo, deseaba, bastaría, este). 336 + 9 + 4 = 349.
  - not counted: the 6 unresolved and 31 restored words; the 30 probable words that are code values placed by the sense,
    whether on 5 Nov (24: caso three times and casos, empresa, nuestro señor twice = 4 words, Reina three times, Duque three
    times, estado twice, buena, buenos, govierna, capitulaciones twice, confianza as code _79_, fuertes) or by the text-only
    model run of 11 Nov from sense and alphabetical order (6: trata, trataba, Cristianísimo, cristianos, allanar,
    allanado); "ofreciéndole", a proposal of the same run that needs one sign changed; and the 3 xe words (acomodarse,
    deseando, conservase), which the M16 pre-registration kept restored and which became probable only by a class rule
    written after that result (deviation 8).
  - "casa" (1r, code _60_ = CAS) is classed certain in the table while the other four places of the same code are probable
    and the 5 Nov notes say _60_ was resolved by the sense; the strict count treats the five places alike.
  - The same rule on the 5 Nov table gives 348/425 = 81.9%. The 88.2% published then counted the code values placed by the
    sense at two or more places; that count is the contributor's and is now given as such.
  - Other counts, for comparison: 384/421 = 91.2% (the contributor's); 378/421 = 89.8% (his stricter count, deviation 8);
    374/421 = 88.8% (his count before sheet FS1); 345/421 = 81.9% by the rule above without the four FS1 words, whose sheet
    cannot exclude an answer by position (deviation 6).
  - "aquí" (+ = i after que) and "igual" (sa = al) are counted certain on the contributor's statement that those values are
    held by clears of Feria's letters; the clears were not seen at this integration.
- **The order test is not reproducible from the repository.** The list of the 37 clear-held code values and the script are
  not in the folder. Recomputed on the code words of `key.tsv`: Kendall tau 0.74 on 45 code words, 0.93 without the 8 that
  were placed by the sense, against a maximum of 0.31-0.34 for shuffled controls; so the nomenclator is alphabetical and the
  test holds in kind, but the figures 0.750 / 0.463 and "14 of 16 in the window, controls at most 11" are the contributor's.
  The position-bias chance "about 0.14%" is (1/3)^6 = 0.137%.
- **Two proposals do not fit strict alphabetical order.** 127 DIFICULTAD lies between 121/123 DUQUE and 136 ENEMIGO, where
  strict order wants a word between DUQUE and ENEMIGO. _52_ CRISTIAN lies between _49_ BUEN and the CA- group that starts at
  _53_ (CARDENAL), where strict order wants a word between BUEN and CA-. Both stay sense proposals; neither is counted.
- **A slip in the word table.** The note on 264 HONRA cites "267 INDIAS" as the upper end of its window; 267 is not in
  `key.tsv`. The window as the key has it is 261 HEREGE to 280 ITALIA, which HONRA fits.
- Further points on the proposals: 48 TRATA has no anchor in its series (the table says "USA not excluded"); "cristianos no
  resolvió" gives no clear sense, and sheet FL2-C read xo, not +, there, so the "two places" of _52_ are one good place.
- **`key.tsv` and `reading.md`.** `key.tsv` is the frozen key C04 and `decryption.txt` is its mechanical output, so its rows
  were left unchanged; its header now lists each value the reading uses that the file does not carry: _30_ (TERMI in the key,
  ALLA in the reading), _35_ (CORRESPONDENCIA / AMISTAD), bo (la / unresolved), + (null / i after que), sa (a / al), and 141
  (not in the key / ELLO), with 318 OFICIO now held by a clear and the sense proposals 48, _52_, 127, _40_, 264, 295, _54_.
- The key hash quoted in `BLIND-REREADING.md` and in the key header (714f70ba...) is not the hash of `key.tsv` in the
  repository (3a608469..., the same on main before this PR); it is probably the hash of the contributor's working copy.
- Not checked: the images (BNE Digital 403, no browser session), the clear of MSS/18428 fol. 31, and every sheet, rule,
  map and answer hash (files not in the repository).
- `_check_reading.py`: 72 of 206 sentences clean, 0.350 (70 of 202 before the sentence added to the head of `reading.md` at
  this integration; 52 of 148 on 5 Nov); the Spanish construes clause by clause where
  it is unmarked, and the translation follows it.

## Escalation

- [x] siblings: Feria's letters RES/227/120-121, 127, 128, 129 opened and used; RES/227/123-124 and 112 (Mirabel) have no cipher; MSS/18428 opened (same system). 14 Nov: the one cipher letter of MSS/18428 without a decipherment of the time read in part (PR #560, `mss18428/`).
- [x] clear-pages: the margin clears of Feria's letters used as keys and tests; the margin of MSS/18428 p. 15 found to be show-through.
- [x] known-keys: no published key of this system found (DECODE, Cryptiana, Lasry); the Gondomar ciphers (Rodríguez Gómez) noted, not checked.
- [x] print: three web searches (the third on 5 Nov 2026: Mirabel to Coloma, Lyon 1622) found no edition or study of this letter; Guill Ortega 2007 (Coloma biography), Herrero García 2023 and the Codoin index not read, named as the next print sources.
- [x] key-rebuild: CLE_C02 -> C03 -> C04 extended from the clears of RES/227/128-129.
- [x] retry: the whole letter re-read with C04 values (v4); two words moved after the shape sheet M16; 11 Nov: two more blind sheets (FL2-C, FS1) on the image, and the code values re-examined against the order of the nomenclator (`BLIND-REREADING.md`); 12 Nov: recount by the read bar at integration, 349/421 = 82.9%; 13 Nov: every cipher passage of MSS/18428 that has a contemporary clear aligned (v5 - v7 margins, the clear copies v33 g and v39 d - v40 g, v41 margins), see the section "13 Nov 2026".

## Prior work

Catalogue 1601 was open, and there was no target, PR or issue for Mirabel, Coloma or RES/227 when checked through the GitHub
API (origin/main 895f21c4, 5 Nov 2026). Lead 1602 (Feria to Coloma) is vetted "partly_read" (margin clears); we used those
clears and credit the pointer. Nothing on DECODE, at Cryptiana (Tomokiyo) or in Lasry's lists. WAINUT and Brackx have no part
in this target. Not read: Guill Ortega 2007, Herrero García 2023 (see deviation 9).

## Credits

- `dudout`: transcription, key, the tests, the reading, the blind sheets (Brice Dudout answered them).
- `contemporary`: the margin clears of Feria's letters (RES/227/127-129) and of MSS/18428 p. 44, used to build and test the key; the clear copy of MSS/18428 fol. 31 (141 = ello, 318 = oficio); the clear copies v33 g and v39 d - v40 g and the margin clears of v5 d - v7 d of MSS/18428 (39 = bien, 4‡ = g, 60 = i, 49 BUEN, 56 CAPITULA, 225 FUERTE, 308 NUESTRO, 34ʳ SR).
- `dudout` (PR #560, 14 Nov 2026): the MSS/18428 letter of images 13 right - 15 left: inventory of the volume (issue #367), transcription, key CLE_M02, measurements M01 and M02, reading and translation.
- `contemporary`: for the MSS/18428 letter, the decipherments by Gondomar's secretary of the six other cipher letters of the volume (`mss18428/CONTEMPORARY-CLEARS.md`).
- `bourdeau`: pointer (catalogue 1601, leads 1602 and 1271 = catalogue entry 1271 for MSS/18428).

## Files

`mss18428/`: the MSS/18428 letter (PR #560): transcription, decryption, reading, translation, key CLE_M02, validation, contemporary clears.
`transcription.txt`, `decryption.txt` (word by word: tokens, key values, word), `key.tsv` (CC BY 4.0), `validation.txt`,
`reading.md` (normalised text and word table), `translation.md`, `BLIND-REREADING.md` (11 Nov: new code values, sheets FL2-C and FS1,
hashes, counts), `profile.json`.

## Integration check (14 Nov 2026, PR #560): the MSS/18428 letter folded in

PR #560 (Brice Dudout) brought the letter of BNE MSS/18428, viewer images 13 right - 15 left (the Marquis of Mirabel to the Count of
Gondomar, Paris, early 1622; catalogue 1271) as a new target `mirabel1622`. It is the same system as this target and its key CLE_M02 is
key C04 of this folder extended from the clears of MSS/18428, so under one key, one entry it is folded in here as a second document:
files in `mss18428/` (the contributor's NOTES and profile kept as `NOTES_PR560.md` and `profile_PR560.json`; the key extension as
`mss18428/key.tsv`). `key.tsv` of this folder stays C04 (the frozen key behind `decryption.txt`).

- **Reproduction.** An own decoder from `mss18428/key.tsv` over the token column of `mss18428/decryption.txt` gives the same values on
  231 of 237 rows; the other 6 are notation (faz / fez = que, which are not rows of the key file; + written as a null). The word table
  counts 250 cipher words: 183 certain, 36 probable, 11 restored, 20 unresolved, as stated.
- **Strict count: 182/250 = 72.8%.** The 183 certain words less "Reina" (code _A_), a value placed by the sense in this folder's key and
  counted here as a hole; every other certain code word rests on a clear (REY, ELLO, BIEN, OTRO, FRANCES, NUESTRO, SR, HECHO, CAPITULA)
  or on C04 rows built from Feria's clears (MUY, MENTE, AUNQUE, ALGUNA). The contributor's figures: 183/250 = 73.2% sure, 219/250 =
  87.6% certain + probable. Read in part. Part A alone (contributor): 166 words, 124 / 21 / 7 / 14; part B: 84 words, 59 / 15 / 4 / 6.
- **Tests: failed and partial, published as such.** M01 (part B, image 15 left, 192 tokens, key CLE_M01, lexical score with the cipher
  runs segmented alone): score -2.381 against the threshold -2.35, gap 0.499 to the best of 200 controls against 0.60: **failed**. M02 (part A,
  images 13 right - 14 right, 349 tokens, key CLE_M02, a whole-text lexical metric recalibrated after M01 on burned passages only):
  -2.383 against -2.25, gap 1.029 against 0.30: **partial** by the contributor's protocol. The extended key is not validated. The metric of
  M02 was changed after M01 failed; that is a new rule for a new passage, not a re-scoring of M01. Pre-registrations, scripts and
  hashes are in the contributor's working folder: the order of events is by the contributor's record. The 0.921 agreement on the 39
  aligned segments of the six deciphered letters is learning data (the added values come from them), not a test.
- **H4 and M01.** Part B is the passage that was reserve H4 of this target (burned without a measurement on 5 Nov because its margin was
  show-through). It was measured for the first time as M01.
- **o with a cross = t, and the H5 transcription.** The contributor reads the sign of "trae" and "ministros" in the clear copy of images
  39 right - 40 left and in the H5 margin passage (image 44 right, "is xi Δ ō cor f" = ministros) as an o with a cross, value t, a sign
  distinct from Ð = n; the H5 transcription of 5 Nov had it as Ð. This explains the "Ð (n? / t) in conflict" loss recorded under H5 in
  `validation.txt` (a transcription slip, not a key fault). It is applied as a note: the H5 score stays as measured (0.814, partial), and
  the two Ð of the Lyon letter (conveniencias, rompimiento, Ð = n) are unaffected. The images were not seen by the project, so the
  re-reading is by the contributor's record.
- **_0_ REBELDE.** C04 had _0_ = REVES; the clear copy on image 33 left gives "sus rebeldes" twice. _0_ does not occur in the Lyon
  letter, so its reading is unchanged.
- **g doubtful.** The clear copies give g = p (v39 d) and g = f (v33 g); g does not occur in the MSS/18428 letter.
- **Images.** BNE Digital answered 403 to a script again (14 Nov 2026, bdh-rd.bne.es viewer); no browser session. The transcription and
  every alignment with the clears are by the contributor's record.
- **Prior art.** Not on DECODE; nothing at Cryptiana or in Lasry's lists; no target or PR for MSS/18428 before issue #367 (inventory) and
  this PR; Herrero García (*Avisos* 100, 2023) and the *Correspondencia oficial* of Gondomar (Documentos inéditos, 1936-1945) not read.
- **Catalogue 1271** (MSS/18428) leaves the catalogue: six of its seven cipher letters carry a decipherment of the time and the seventh is
  read in part here.
