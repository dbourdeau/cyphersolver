# Reading

The letter strings obtained by decrypting with the keys are in `data/plaintext.txt`. Below they are divided into words and then turned back into ordinary writing.
X is the separator, Q stands for CH. Bold letters are letters that are wrong as plaintext (the cipher text has that letter).

## Frame 0993 (Luftgaukommando VII to Flugabwehrkommando Schwarzwald, 17 May 1940, four parts)

1. `GKDOS X ERSTENS KLAMMER FLAKGRUPPE X FRIEDRICHSHAFEN X GIBT AN FLUGABWEHRKOMMANDO X SCHWARZWALD X AB DOPPELPUNKT X EINS X UND X DREI X ZUG DER X DREI X BAT`**`B`**`ERIE X RES X LEI X FLAKABTEILUNG X NEUNDREIZWO X KLAMMER`
2. `X HERBERTINGEN X KLAMMER X DIE BEIDEN ZUEGE WERDEN DURQ FLUGABWEHRKOMMANDO X SCHWARZWALD X TRANSPORTI`**`W`**`RT UND GEM X FERN`**`N`**`UENDLIQER BESPREQUNG EINGESETZT X ZWOTENS KLAMMER FLAKGRUPPE X FRIEDRICHSHAFEN X`
3. `SETZT X DREI X ZUG FLA X M X G X RES X KOMP X DREINULLVIER X KLAMMER X SIGMARINGEN X KLAMMER BEIM SQUTZOBJEKT X HERBERTINGEN X EIN X TRANSPORT DURQ FLAKGRUPPE X FRIEDRICHSHAFEN X DIE NEUEN STELLUNGEN`
4. `UND FEUERBEREITS`**`X`**`AFT ZU MELDEN X LUFTGAUKOMMANDO X ROEM X SIEBEN X STRIQ ROEM X EINS X ANTON X OP X ZWO X NR X ZWOAQTFUENFEINS X STRIQ X VIERNULL X G X KDOS `**`Q`**

In ordinary writing:

> G.Kdos. 1.) Flakgruppe Friedrichshafen gibt an Flugabwehrkommando Schwarzwald ab: 1. und 3. Zug der 3. Batterie Res. Lei. Flakabteilung 932 (Herbertingen). Die beiden Züge werden durch Flugabwehrkommando Schwarzwald transportiert und gem. fernmündlicher Besprechung eingesetzt. 2.) Flakgruppe Friedrichshafen setzt 3. Zug Fla. M.G. Res. Komp. 304 (Sigmaringen) beim Schutzobjekt Herbertingen ein. Transport durch Flakgruppe Friedrichshafen. Die neuen Stellungen und Feuerbereitschaft zu melden. Luftgaukommando VII/Ia op 2 Nr. 2851/40 g.Kdos.

This has the same content as the recipient's fair copy (frames 0994-0995).

## Frames 1025-1027 (from Flugabwehrkommando Schwarzwald Ic, 17 May 1940, two parts)

1. `GEHEIME KOMMANDOSAQE X AM X EINSSEQS X FUENF X VIERNULL X WURDE DEM X FLGABW X KDO X SCHWARZWALD DER X ROEM X EINS X ZUG X ZWO X STRIQ X NEUNDREIZWO X KLAMMER X ZWO X CENTIMETER KLAMMER VON FLAKGRUPPE X FRIEDRICHSHAFEN X ZUGETEILT X DER ZUG IST SEIT`
2. `ZWOZWODREINULL X UHR IN STELLUNG X DREINULLDREIEINS X WESTL X TUELLINGEN X FEUERBEREIT X ER IST ABT X NEUNVIERZWO X UNTERSTELLT X FLGABWKDO X SCHWARZWALD X ROEM X EINS X CAESAR X NR X FRITZ X EINSSEQSEINS X STRIQ X VIE`**`E`**`NULL X G`**`H`**`DOS`

In ordinary writing:

> Geheime Kommandosache. Am 16.5.40 wurde dem Flgabw.Kdo. Schwarzwald der I. Zug 2./932 (2 cm) von Flakgruppe Friedrichshafen zugeteilt. Der Zug ist seit 22.30 Uhr in Stellung 3031 westl. Tüllingen feuerbereit. Er ist Abt. 942 unterstellt. Flgabw.Kdo. Schwarzwald Ic Nr. F 161/40 g.Kdos.

This has the same content as the teleprinter message of the same day (frame 1024).

## Spelling conventions (as seen in these two messages)

- X separates words. It stands before and after names, numbers and abbreviations; ordinary running words are written together (`DIEBEIDENZUEGEWERDEN`).
- CH is written Q (`DURQ`, `SQUTZOBJEKT`, `STRIQ`); names keep CH (`FRIEDRICHSHAFEN`, `SCHWARZWALD`).
- Numbers are spelled digit by digit and run together (`NEUNDREIZWO` = 932, `ZWOAQTFUENFEINS` = 2851); 2 is ZWO.
- "1.)" and "2.)" are `ERSTENS KLAMMER` and `ZWOTENS KLAMMER`; brackets are `KLAMMER`, the colon is `DOPPELPUNKT`, the slash is `STRIQ`.
- Roman numerals are preceded by `ROEM` (`ROEM SIEBEN` = VII, `ROEM EINS` = I). Single letters are spelled by name (`ANTON` = a, `CAESAR` = c, `FRITZ` = F).
- The first five-letter group of each part is the key indicator group and is not part of the text. The parts end at word boundaries.

## Wrong letters (7 of 1,023)

| Place | Plaintext | Cipher-text letter | Remark |
|---|---|---|---|
| 0993 part 1 | BAT**B**ERIE | letter 8 (TE**B**DA) | typed B; an error for T |
| 0993 part 2 | TRANSPORTI**W**RT | letter 49 (EXW**W**U) | typed W; an error for E |
| 0993 part 2 | FERN**N**UENDLIQER | letter 18 (RN**N**RA) | typed N; an error for M |
| 0993 part 4 | FEUERBEREITS**X**AFT and the final **Q** | letter 32 (M**X**NLB) and letter 30 (MLEF**Q**) | exchanging the two letters gives SQAFT and a final X |
| 1027 | VIE**E**NULL | letter 137 (R**E**TEZ) | written e; an error for R |
| 1027 | G**H**DOS | letter 194 (IZN**H**) | h and k are close in this hand; may be K |

The five letters in frame 0993 are those letters in the typed cipher text, also when enlarged. We take them to be errors made in enciphering or in relaying the message (there is nothing to check this against).
