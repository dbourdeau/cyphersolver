# coloma1622: the Marquis of Mirabel to Carlos Coloma, Lyon, 8 December 1622 (BNE RES/227/122; catalogue 1601)

Status: read in part (Brice Dudout, 5 Nov 2026; 375 of 425 cipher words = 88.2% without restorations; key partial by our protocol: C02 0.761, H3 0.690, H5 0.814 on characters against contemporary clears).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Catalogue entry 1601 (Chrome pass, BNE Digital).
The key comes from the Duke of Feria's letters to Coloma (lead 1602), whose cipher passages carry a contemporary clear in the
margin, and the last test used one page of BNE MSS/18428 (Mirabel to Gondomar, lead 1271).

## Document

Madrid, BNE RES/227/122 (Mss. 18.692), 2 leaves (BNE Digital, CC BY 4.0). Antonio Dávila y Zúñiga, Marquis of Mirabel,
Spanish ambassador in France, to Don Carlos Coloma, Spanish ambassador in London; Lyon, 8 December 1622. Clear opening and
close; the body in cipher: 969 tokens (f.1r 25 lines, f.1v 36 lines), plus two tokens read on the image that were missing
from the frozen transcriptions. Signature and postscript autograph.

**No image, crop or thumbnail is included** (BNE scans used for research only).

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

| words | certain | probable | restored | unresolved | certain + probable | with restored |
|---|---|---|---|---|---|---|
| 425 | 338 | 37 | 29 | 21 | 375 = 88.2% | 404 = 95.1% |

**Read in part** (`reading_review` grade B). A blind shape sheet of 16 questions (pre-registered and hashed before it was
built, shapes only), answered by Brice Dudout, confirmed the transcribed token in eight places (those words stay restored)
and moved "puede" and "cosa" to probable. Code words resolved at all their places: 309 negocio (also held by the clear of
RES/227/128), _49_ buen-, _60_ cas-. Restored from sense at one place each: _53_ Cardenal, _81_ Consejo, _K_ respuesta,
_68_ ciudad, _139_ efecto, 317 obligación, 318 oficio, _35_ correspondencia, _R_ razón. Unresolved: 141, 48, 39, 295, _2_,
127, _40_, 264, _52_ (second place) and the group _L_ _54_ _y_ ("la Valtelina" or "la religión católica").

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
   words stay restored. Ignoring the marks would give 88.7%.
3. **About ten restorations correct a transcribed token from the sense**; the sheet confirmed the token in eight of them.
4. **C01's held-out lines are part of the target letter** (measured with an earlier key, then read with the later one).
5. **One reader**: an AI agent transcribed and read; Brice Dudout answered the shape sheet only. No palaeographer checked.
6. **Not read: two studies.** M. Á. Guill Ortega, *Carlos Coloma* (2007), and Herrero García (*Avisos*, 2023, on the
   Mirabel-Gondomar letters of MSS/18428: its page blocked our fetch) were not read, nor a full index of the *Colección de
   documentos inéditos*. If either prints this letter or its key, we will credit it.

## Remaining gaps

- 21 unresolved words and the code words 141, 48, 39, 295, 2, 127, 40, 264, 52 (second place), L/54/y - blocker: open-codes; one or two places each, no clear in the training letters.
- The marked signs 4‡, q̲, x̤ and the 29 restored words - blocker: open-codes; a new letter of the same system with a contemporary clear is needed (MSS/18428 has some).

## Escalation

- [x] siblings: Feria's letters RES/227/120-121, 127, 128, 129 opened and used; RES/227/123-124 and 112 (Mirabel) have no cipher; MSS/18428 opened (same system).
- [x] clear-pages: the margin clears of Feria's letters used as keys and tests; the margin of MSS/18428 p. 15 found to be show-through.
- [x] known-keys: no published key of this system found (DECODE, Cryptiana, Lasry); the Gondomar ciphers (Rodríguez Gómez) noted, not checked.
- [x] print: three web searches (the third on 5 Nov 2026: Mirabel to Coloma, Lyon 1622) found no edition or study of this letter; Guill Ortega 2007 (Coloma biography), Herrero García 2023 and the Codoin index not read, named as the next print sources.
- [x] key-rebuild: CLE_C02 -> C03 -> C04 extended from the clears of RES/227/128-129.
- [x] retry: the whole letter re-read with C04 values (v4); two words moved after the shape sheet.

## Prior work

Catalogue 1601 was open, and there was no target, PR or issue for Mirabel, Coloma or RES/227 when checked through the GitHub
API (origin/main 895f21c4, 5 Nov 2026). Lead 1602 (Feria to Coloma) is vetted "partly_read" (margin clears); we used those
clears and credit the pointer. Nothing on DECODE, at Cryptiana (Tomokiyo) or in Lasry's lists. WAINUT and Brackx have no part
in this target. Not read: Guill Ortega 2007, Herrero García 2023 (see deviation 6).

## Credits

- `dudout`: transcription, key, the tests, the reading.
- `contemporary`: the margin clears of Feria's letters (RES/227/127-129) and of MSS/18428 p. 44, used to build and test the key.
- `bourdeau`: pointer (catalogue 1601, leads 1602 and 1271).

## Files

`transcription.txt`, `decryption.txt` (word by word: tokens, key values, word), `key.tsv` (CC BY 4.0), `validation.txt`,
`reading.md` (normalised text and word table), `translation.md`, `profile.json`.
