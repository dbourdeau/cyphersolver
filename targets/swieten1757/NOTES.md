# Van Swieten to Cobenzl, Bonn 1757–58 (DECODE R955): the 1757 table

Outcome: read from existing decipherment (the clear copy under the numbers); the 1757 table aligned from it.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): the two letters of 1759 (R956, R957) use a
different table (100–442), a different cipher with its own page and folder, `../swieten1759/` (`docs/swieten1759.html`),
where the solver, key, runs and validation files now live. This entry is R955 only.

ARA Brussels, Secrétairerie d'État et de Guerre, inv.nr. 1236. Gottfried van Swieten (Bonn) to Count
Johann Karl Philipp von Cobenzl, Brussels. Letters in French with ciphered passages in numbers.

| Record | Folio | Date | Cipher |
|---|---|---|---|
| R955 | f. 141 | undated (1757–58; Hanau in French hands) | 89 dotted 3-digit groups (202–586), decipherment written below in clear |
| R956 | ff. 344–345 | Bonn, 4 Feb 1759 | ~20 runs of unseparated digits inside clear text, groups 100–442 |
| R957 | ff. 327–328 | Bonn, 14 Jan 1759 | 2 runs, 210 groups, 100–442 |

## Prior art

Nothing in print found (web search; local Tomokiyo/cryptiana copies have no van Swieten entry). DECODE
transcriptions by SofPe (2019) and XL (2020), marked non-decrypted.

## R955: the 1757 key (read from its own decipherment)

The clear text under the numbers is the decipherment: "on a délibéré ici dans une députation de Magistrat
sur le parti à prendre au cas que les François fussent obligés d'abandonner Hanau, on a osé opiner pour la
neutralité et conclure même; on garde cependant un profond secret là-dessus comme de raison."
Aligning it gives an **alphabetical syllabary** with letters at the head of their sections and a few
homophones: a 202/203, ab 205, an 216, ar 220, as 223, at 224, au 228, be 241, bl 243, c 250, ç 251, ci 263,
cl 264, d 279, da 280, de 282/290, en 308, er 313, es 314, et 315, fr 333, fu 337, gi 343, ha 355, i 364/369,
is 380, l 387, le 388, les 389, li 390, m 394, ma 396, n 409, na 410, ne 411, ns 418, o 422/423, on 435,
p 447, pi 452, po 453, pr 455, pu 459, que 465, r 469/470, ra 471, re 472, s 480/491, se 484, su 488, t 494,
ta 496, te 498, ti 500, tr 503, u 511, ur 512, ut 522.

## Remaining gaps
- groups 400, 297, 586 inside "conclure même" - blocker: too-short; each occurs once, the decipherment gives the word but not the split

## Escalation
- [x] siblings: R956, R957 opened; a different (1759) table, now swieten1759
- [x] clear-pages: the clear lines under the numbers are the decipherment
- [x] known-keys: no key record for this series on DECODE
- [x] print: web search, local Tomokiyo/cryptiana copies: nothing printed
- [n/a] key-rebuild: the values come from the alignment with the decipherment; nothing to rebuild
- [n/a] retry: every group is under the decipherment; the three unsplit groups occur only once

Reveal: `build_reveal955.py` writes `docs/reveal/swieten1757.json` from the values above (86 of 89 groups valued).
