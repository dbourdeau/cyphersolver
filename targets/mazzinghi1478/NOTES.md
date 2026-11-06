# Rome, January 1478 (st. fior.): Giovanni Mazzinghi and a second writer to the Medici, cipher (catalogue 2307, 2320)

Read in part, 6 Nov 2026: key recovered from the contemporary decipherment of the sibling MAP LXXII 170; 76.1% of the
cipher signs of the two bare letters read (measure.py); reading and translation in `reading.md`.

## The documents

All three are in the Archivio di Stato di Firenze, Mediceo avanti il Principato (MAP). Images from the ASF MAP viewer
(full server size, 1272 px wide), fetched with `getdoc.py FILZA DOC` into `img/` (git-ignored).

| Catalogue | MAP | Date as written | Writer | State |
|---|---|---|---|---|
| 2307 | LXXXIX 142 (recto; verso is show-through plus endorsement) | "In nome di Dio a dì xvj di gennaio 1478" (no place; Rome by content) | Giovanni Mazzinghi (verso: "1478 ad 16 di gennaio / da G. Mazinghi / Cifra") | bare: about 40 lines of cipher words with clear connectives, no decipherment |
| 2320 | CXXXVII 252 (recto) | "a dì 13 di gennaio 1478" | unsigned (same signs and hand as 2307) | bare: about 17 lines, no decipherment |
| (lead 2308, closed read) | LXXII 170 (recto) | "a dì 2? di gennaio 1478" | same system | the key source: a decipherment written over the cipher words in a second hand |

**Dating.** All three say "gennaio 1478". A Florentine writer counted the year from 25 March, so this is very probably
January **1479** in modern style: nine months after the Pazzi conspiracy (26 April 1478), during the Pazzi War, with
Florence under Sixtus IV's interdict. 2307 names no place; the content (the Pope, the Cancelleria, Castel Sant'Angelo in the sibling) puts the writers in Rome. The overnight vetting (batches n08, n10, c32, c33)
called them January 1478 and Lorenzo's *Lettere* II-III were searched for both years without a hit; the catalogue
entries are corrected to "January 1478 st. fior. (1479)".

## The system (first look)

Words are enciphered one by one and left as words, separated by spaces or dots; clear words ("com[e]", "che", "quanto",
"papa", numerals) stand between them. The signs are letter-like (o, +, double-barred crosses, q, 4, r, z, t, s, b, m,
n, l, p, 8, x, =). Probably a homophonic substitution of letters with word division kept. The glossed letter LXXII 170
gives cipher-word / plain-word pairs.

Not the system of `targets/siena11` (Acciaiuoli, Rome, June 1478, Lasry's key).

## Plan

1. Glyph inventory and transcription of LXXII 170 with its glosses (`glyphs.md`, `t170.tsv`).
2. Transcribe 2320 and 2307 with the same tokens.
3. Fit the key on the 170 pairs; hold out a share of the pairs to test it.
4. Decipher 2320 and 2307; read, translate, check against the 1479 events.

## Prior work checked

- Lorenzo de' Medici, *Lettere* II and III (Google Books ids 1hpdAAAAMAAJ, MBxdAAAAMAAJ): no citation of LXXXIX 142
  or CXXXVII 252 (Chrome passes c32, c33, 6 Nov 2026). The Pazzi War letters of early 1479 fall in vol. III-IV;
  vol. IV was searched for LXXII 171 only. To repeat for these two shelfmarks.
- DECODE has no MAP records; Tomokiyo and Lasry's GL.htm have nothing on them (vetting batch n08).

## Draft reading (6 Nov 2026)

Files: `t170.tsv` (glossed sibling), `t252.tsv`, `t142.tsv` (transcriptions), `build_key.py` -> `key.tsv` (69 gloss
pairs; held-out letters 57-74%), `refine.py` -> `key_refined.tsv`, `decode.py` -> `draft252.txt`, `draft142.txt`.
The key is a homophonic letter substitution (a +, ^, d; e x, y, c; i s, 5, 1, 3; o r; u/v q, u; t H; tt {Hp}; r 6;
l 2+, #?, l; n n; s 4, f; m 8; g m; p p, {pbar}, {dbar}; c {sg}; d o; b =; f b; ss g), words kept whole, clear
words between. Numerals are persons: 10 (glossed "Duca di Calabria"? in 170), 12 (glossed Zanobi), 30, 40, 51, 231.

**252, 13 Jan 1478/9 (unsigned).** The writer writes only to tell them that the Pope ("S.S.") has sent a brief;
a letter was presented yesterday morning to [10]; the king is so enraged that the writer fears they will seize
Antonio del Palagio, Pagolo Rucellai and Lionardo di Giunta and put them in Castel [Sant'Angelo]; Tornabuoni has
asked [10] ...; a fante was sent; "comandate niente", written in haste.

**142, 16 Jan 1478/9, Giovanni Mazzinghi.** "Io, persona fidata": this morning a bull under lead was published in the
Cancelleria annulling all the privileges the Church had granted ...; a very cruel process against them ("contra di
voi molto crudele"), "dannando la croce addosso a voi ... credo abbino el diavolo in corpo". Iacopo de' Rossi of
Pistoia, who stays in the house of ..., has told him many times about "la fine vostra"; he could not get anything out
of him yet; [10] told him he can trust Mazzinghi; another Pistoiese called Cola; at [10/3] o'clock [10?] called
Iacopo, "et quello ordinò la morte di [30] e mostra sia d'ordine sopra a voi"; if he learns anything certain he will
come in person; "aiutatevi l'occhio, ché ogni cosa fanno per la vostra fine". Later: [51] promised ...; [40] wrote to
[10] a letter ...; messer Lorenzo da Castello ... has become very bold; two men in disguise; the Lucchese ambassadors.

If [30] is Lorenzo, this is a warning of a murder plot nine months after the Pazzi conspiracy. Not yet claimed:
the code numbers need identifying from the content and the other MAP letters, and the misread look-alikes fixing.

## Remaining gaps

- 92 cipher words (394 signs) that do not decode to sense, listed in `measure.py` (UNREAD) - blocker: illegible; signs
  are 8-14 px at the ASF server's maximum (1272 px), rechecked at 5-6x (`recheck.tsv`) and tried against look-alike
  variants (`variants.py`); no higher-resolution image online
- code numerals 10, 30, 40, 51, 231, 10/3 and the recurring group OLDP/DLDP/EDP - blocker: open-codes; only 12 =
  Zanobi is glossed in LXXII 170 (10 perhaps "lo Duca di Calabria"), no code list for this cipher found

## Escalation

- [x] siblings: LXXII 170 (glossed) used as key source; LXXII 169, 171 and CXXXVII 251, 253 opened (171 is another system)
- [x] clear-pages: none filed with 142 or 252; the 142 verso is the endorsement only
- [x] known-keys: siena11 (Acciaiuoli, Rome 1478) compared, a different system; MAP LXXII 178-188 key sheets use other signs
- [x] print: Lorenzo de' Medici, Lettere II-IV searched for the shelfmarks (Chrome passes c32, c33): no citation; web search for Mazzinghi and the Pistoiese plot found nothing
- [x] key-rebuild: hard-EM on the gloss pairs (build_key.py), LM fill (refine.py), context fixes, image recheck (recheck.tsv)
- [x] retry: every unread word retried with look-alike variants against a period word list (variants.py)
