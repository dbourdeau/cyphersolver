# coloma1622: the Marquis of Mirabel to Carlos Coloma, Lyon, 8 December 1622 (BNE RES/227/122; catalogue 1601)

Status: read in part (Brice Dudout, 11 Nov 2026; 349 of 421 cipher words = 82.9% by the README read bar, which leaves out unresolved and restored words and code values given by the sense; the word table has 337 certain, 47 probable, 31 restored, 6 unresolved, and the contributor's count of certain + probable is 384 = 91.2%; key partial by the contributor's protocol, two of four measurements failed: C02 0.761, H3 0.690, H5 0.814 on characters against contemporary clears). See the integration check of 12 Nov 2026.

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
| 11 Nov 2026 (this version) | 421 | 337 | 47 | 31 | 6 | 384 = 91.2% | 415 = 98.6% |

The last two columns are the contributor's count. **By the README read bar the share is 349/421 = 82.9%** (348/425 = 81.9% on
the 5 Nov version): 34 of the 47 probable words and one certain word are not counted, as set out in the integration check of
12 Nov 2026 below.

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

- 6 unresolved words (39 twice, bo, 2, "[ge]ia", "z cer zan") - blocker: open-codes; one or two places each, no clear in the training letters.
- 30 probable words that are code values placed by the sense (caso, casos, empresa, nuestro señor, Reina, Duque, estado, buena, buenos, govierna, capitulaciones, confianza, fuertes; and the 11 Nov proposals trata, trataba, Cristianísimo, cristianos, allanar, allanado) - blocker: open-codes; not counted as read; a contemporary clear with these codes would settle them.
- the BNE images and the clear of MSS/18428 fol. 31 were not seen by the project at this integration - blocker: needs-physical-access; BNE Digital answers 403 (Cloudflare) to a plain fetch and no browser session was available on 12 Nov 2026; the blind sheets, their rules, maps and answers are not in the repository, so the hashes and "rule hashed first" are by the contributor's record.
- 31 restored words, among them the code values at one place (127, 40, 264, 295, 35, 53, K, 68, 81, 139, 317, R, 62, L/54/y) - blocker: open-codes; a new letter of the same system with a contemporary clear is needed (MSS/18428 has some).
- The marked signs 4‡, q̲, x̤ and those seen on FL2-C (barred 0, xo with a v above, o with a cross, "fov") - blocker: open-codes; no value in any key or clear we have.

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

- [x] siblings: Feria's letters RES/227/120-121, 127, 128, 129 opened and used; RES/227/123-124 and 112 (Mirabel) have no cipher; MSS/18428 opened (same system).
- [x] clear-pages: the margin clears of Feria's letters used as keys and tests; the margin of MSS/18428 p. 15 found to be show-through.
- [x] known-keys: no published key of this system found (DECODE, Cryptiana, Lasry); the Gondomar ciphers (Rodríguez Gómez) noted, not checked.
- [x] print: three web searches (the third on 5 Nov 2026: Mirabel to Coloma, Lyon 1622) found no edition or study of this letter; Guill Ortega 2007 (Coloma biography), Herrero García 2023 and the Codoin index not read, named as the next print sources.
- [x] key-rebuild: CLE_C02 -> C03 -> C04 extended from the clears of RES/227/128-129.
- [x] retry: the whole letter re-read with C04 values (v4); two words moved after the shape sheet M16; 11 Nov: two more blind sheets (FL2-C, FS1) on the image, and the code values re-examined against the order of the nomenclator (`BLIND-REREADING.md`); 12 Nov: recount by the read bar at integration, 349/421 = 82.9%.

## Prior work

Catalogue 1601 was open, and there was no target, PR or issue for Mirabel, Coloma or RES/227 when checked through the GitHub
API (origin/main 895f21c4, 5 Nov 2026). Lead 1602 (Feria to Coloma) is vetted "partly_read" (margin clears); we used those
clears and credit the pointer. Nothing on DECODE, at Cryptiana (Tomokiyo) or in Lasry's lists. WAINUT and Brackx have no part
in this target. Not read: Guill Ortega 2007, Herrero García 2023 (see deviation 9).

## Credits

- `dudout`: transcription, key, the tests, the reading, the blind sheets (Brice Dudout answered them).
- `contemporary`: the margin clears of Feria's letters (RES/227/127-129) and of MSS/18428 p. 44, used to build and test the key; the clear copy of MSS/18428 fol. 31 (141 = ello, 318 = oficio).
- `bourdeau`: pointer (catalogue 1601, leads 1602 and 1271).

## Files

`transcription.txt`, `decryption.txt` (word by word: tokens, key values, word), `key.tsv` (CC BY 4.0), `validation.txt`,
`reading.md` (normalised text and word table), `translation.md`, `BLIND-REREADING.md` (11 Nov: new code values, sheets FL2-C and FS1,
hashes, counts), `profile.json`.
