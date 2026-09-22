# Van Swieten to Cobenzl, Bonn 1757–1759 (DECODE R955–R957)

Status: read (R955 from its own decipherment; R956/R957 96% of groups, key rebuilt ciphertext-only)

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

## R956/R957: the 1759 key (rebuilt ciphertext-only)

A different table, 100–442, but built the same way: an alphabetical list of letters and syllables with a few
word entries (nous, vous, pour, que, qui, comte, roi) and names filed alphabetically. Letter x = 438/439,
y = 441, z = 442 close the table.

Method: `msolve.py` anneals a non-decreasing map from each observed code to a sorted inventory of French
letters/syllables (at most 2 codes per unit), scored with `lang` model `fr-1750-nospace` (added for this
target) plus 1.5 per character. Validated first on a synthetic 274-token text encoded with a random
alphabetical table (recovered verbatim). On the real 491 groups, seed 5 of 8 random starts came out as
readable French ("la nouvelle convention…"); the other seeds did not. The key was then corrected by hand from
the clear text around each run (`overrides.json` over `key_auto.json` → `key.json`; `dec.py` prints the runs).
Four DECODE runs had dropped or doubled digits and were re-read from the images (runs.txt).

Counted: 553 groups in R956+R957, about 21 unread → 96%. R955: 89 groups, read from the decipherment.

## Remaining gaps
- code 232 (twice, R957), a name filed under G - blocker: open-codes; one name, sense of both sentences clear
- codes 147 100 126 148 (R956), the prince's name - blocker: open-codes; a name group, single occurrence
- codes 170 323 441 (R957) and 170 271 289 337 (R956) - blocker: open-codes; syllables read, words unresolved
- codes 290 313 316 313 373 (R956), the one marshal "qu'on estime" - blocker: illegible; digit division uncertain in the scan
- code 357 in R957 "supposition [pr] sans que" - blocker: open-codes; single awkward syllable

## Escalation
- [x] siblings: R955 opened; its 1757 table differs; no other record in inv. 1236 on DECODE
- [x] clear-pages: R955's clear copy read it; the clear text round every 1759 run used as crib
- [x] known-keys: no key record for this series on DECODE; R955's table tried on 1759, does not fit
- [x] print: web search, local Tomokiyo/cryptiana copies: nothing printed
- [x] key-rebuild: monotone annealing (msolve.py) + hand correction rebuilt the 1759 table
- [x] retry: every unread group rerun against the final key and the alphabetical brackets
