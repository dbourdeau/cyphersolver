# A Venetian secretary to the Venetian ambassador in England, 1625, in a three-figure syllabic code (TNA SP 106/10 ff. 193-195, DECODE R722; worksheets R656, R661, R662, R663, R667, R684, R701 p. 3, R702 p. 1, R703, R720)

Status: attempted, not solved — the code is not broken; 420 groups (117 types) transcribed, the endorsement and the
clear passages read, four values fixed from clear-text junctions; annealing does not converge.

**Split on 14 Oct 2026** from `sp106box10` under the one-key rule (George Lasry, 14 Oct 2026). Until then the whole
SP 106/10 codebreaker's file was one entry; this letter and the worksheets on it are in a second three-figure code,
built like the "Venetian Cifer" of R664/R660 but with a different table. The other ciphers of the file have their own
entries and pages (a different cipher in each): [`sp106box10`](../sp106box10/NOTES.md) (system B, the "Venetian Cifer"),
[`sp106r725`](../sp106r725/NOTES.md) (system A, key R725), [`sp106r704`](../sp106r704/NOTES.md) (system C) and
[`sp106r931`](../sp106r931/NOTES.md) (1645, not part of the file). The work below was done in the sp106box10 sessions
of 21 Sept 2026 (catalogue items 66 and 58) and is carried over from its NOTES; `r722_groups.txt`,
`r722_transcription.txt` and `solve722.py` moved here from `sp106box10/cat58/` on 14 Oct 2026. Images: main checkout
`targets/sp106box10/img/` and `r722/` (git-ignored; shared, not moved), R656 and R662 in `sp106c58/decode/`.

Catalogue item 66 (R703), removed as "explained" on 21 Sept 2026, is restored for this entry, narrowed to the letter's
code (attempted, open).

## R722, the intercept

R722 (TNA_SP106/10_UND_(0193-0195), 3 pp.) has 48 numbered lines (DECODE: "48 in sum total, roughly 500 codegroups"),
written half in clear Italian, half in groups 200-599, with the codebreaker's trial syllables between the lines. The
endorsement (p. 1, f. 195v) reads:

> **"Cypher of a Venetian Secretary to the Embassador of that nation in …"**, and on the fold "1625".

The clear passages give the letter's matter: *Parmi che …*, *Io mi credo che questi siano …*, *Ho visto chiaramente
che V. E. …*, *Il S[igno]re … di dire a V. E. che … gran pratica*, *proposito che ella procurasse*, *di satisfattione
con honor di …*, **il Spinola sotto Breda**, **di Bruselles si è inteso …**, *di Roma*, and lines 45-46 *"… soliti
concetti del Pontifice il quale disse a Bethune di voler esser risarcito di 150 m[ila] …"*: Philippe de Béthune,
French ambassador in Rome, and the Pope's demand to be compensated (the Valtelline forts, 1625). Spinola's siege of
Breda ran from August 1624 to 5 June 1625, so the letter is of the first half of 1625: a Venetian secretary
(plausibly in the Low Countries or at Rome) writing to the Venetian ambassador in England.

Transcription: `r722_groups.txt`, all 48 lines, **420 groups, 117 types** (counted 14 Oct 2026 from the file, clear
words excluded), plus the clear Italian; `r722_transcription.txt`, the first pass.

DECODE and the old sp106box10 notes put R722 with the letter-plus-figure records (system C) following DECODE's
pointer "704; 720; 721"; nobody had looked at it until 21 Sept 2026. Its page 2 line 1 ends `540 212 una di questi
matine`, the fragment R703 quotes as `l.1 540 212 una che`; line 3 carries `280 367 464 432` (R720 `l.2`), line 6
`340 367 misciandosi` (R703 `l.6 340 367 misciendosi`), line 8 `245 510 Almeno` (R684 `l.7 … 510 al meno`), line 15
`297 506 395 … e che quello` (R703 `l.14`); the codebreaker's line count runs one behind the page's numbers in places.

## The worksheets on this letter

| record | ff. | what it is |
|---|---|---|
| R703 | 184-185 | p. 2 a positional index headed *linea*: every group 200-399 with the lines where it stands (`201. 5.13.19.21.26.31.33`, `280. 2.6.9.20 ф 24.25`), notes ("201 is a finall sillable after an entire word") and counts. p. 1 (half upside down) glossed fragments under "Finall sillables" and "Entire wordes assured by reiteration" (`l.1 540 212 una che`, `l.7 245 510 Almeno`, `l.14 297 506 395 e che quello`, `l.46 540 464`) and grids of trial syllables and words (*Rovere, Rogare, Rolare, Romano*) |
| R661 | 141-143 | an English political draft in clear (Spain's treasure from the Indies, Portugal), reused: fragments by line with trial words ("il Re", "lo haveva", "bisogno") |
| R667 | 164-166 | count grid of every group 200-577 in ruled boxes with counts and a few values (244 ra, 245 re, 246 ri, 247 ro; 541 dal, 542 del, 543 dil); dictionary trawl for *gra-/gua-* |
| R684 | 170-171 | lines of the intercept (l. 2-27) with trial syllables; groups by frequency (244 fifteen times); `l.7 504 207 495 … 510 al meno`, `l.25 495 391 540 395 207` |
| R701 p. 3 | 177 | **his partial key** (below) |
| R702 p. 1 | 181 | Italian-English dictionary trawl (Bala-, Cola-, Fala-, Mala-) against numbered lines: `li.25 495 391 540 395 207` "a ta n do", `li.32 495 464 491 540 244 436` "al re s ta ua no", `li.38 525 495 541` "si a te" |
| R720 | 188-189 | fragments (`l.2 280 367 464 432 434`, `l.6 542 290 | 280 367 464 432`, `l.16 350 541 513 507`, `l.22 che 525 245 541 449`), trial words |
| R656 | 67 | back of an English Exchequer draft (a sheriff's answer; Nosse, Rowley, Sherborne, Franke) reused for fragments by line: `l.12 313 541 377 238 254` (R722 line 12 verbatim), `l.21 350 495 395 207`, `l.38 495 541 280 495 201` … |
| R662 | 8 | torn strip of his English memorandum on how the code is built: "series of sillables beginning …", "the vowels a.e.i. for every consonant", "commonly m. 540", "the most frequent … di" |
| R663 | 20 | Italian syllable drills and an Italian-English word list, with a few groups of this code |

DECODE lists R656, R662 and R722 as catalogue 58's "4 ciphertexts" (with R931), R703 as catalogue 66 and the rest
as catalogue 62. DECODE's "mid 17th century" and "mostly solved" on R662 are wrong; its note on R656 ("unlikely that
the cleartext is the solution") is right.

## The codebreaker's partial key (R701 p. 3)

A syllabary with the vowel carried in the last digit:

    209 va 210 ve 211 vi 212 vo 213 vu · 231 sa 232 se 233 si 234 so 235 su · 244 ra 245 re
    333 cha 334 che 335 chi 336 cho · 322-326 pr- (pra … pru?) · 313 cu(?) 314 cn(?)
    366 la 367 le 368 li 369 lo 370 lu · 375 da 376 de 377 di 378 do · 510 sta(?) 511 ste 512 sti(?)

It is not the table of R658 (there 244 pi, 245 po, 433-437 la-lu): a second table built the same way. The same syllable
can stand in two series (do = 207 and 378). On the worksheets alone it valued four of R703's 28 groups, and the
codebreaker's glosses conflict with it in places (R702 li.32 glosses 244 *ta*, the key *ra*; 540 *una* and *n*).

## The attack (21 Sept 2026)

Fixed values (C = confirmed by clear context):
- crib, line 24: *che* **525 245 541 449** *lo haveva assecurato* = *che il Re glie-lo haveva*: 525 il, 245 re, 541 gli,
  449 e (C);
- line 8: **245 510** *Almeno* = *resta. Almeno*: 510 sta (C), matching R701 p. 3's 510-514 sta-stu;
- 334 che (C: R701 p. 3 333-336 cha-cho, and the codebreaker glosses 334 "che" throughout).

R701 p. 3's table is right where it can be checked: 209-213 va-vu, 231-235 sa-su, 244 ra, 245 re, 322-326 pra-pru,
333-336 cha-cho, 366-370 la-lu, 375-378 da-do (377 di, 9 occurrences), 510-514 sta-stu.

`solve722.py` anneals the remaining groups against `it-cinquecento` (5-gram, per-character baseline, at most two groups
per syllable, bonus for R701-style runs of five). Four configurations were run (free; length-normalised; R701 values
fixed; R701 fixed + strong run bonus + no word groups), 12-20 restarts of 400k steps each. **Failed**: every restart
ends in different Italian-sounding word salad, and no two agree beyond the fixed values. With about 70 free groups
over 420 tokens the text does not determine the code. The codebreaker did not break it either.

## Remaining gaps
- R722, the code groups (420 tokens, 117 types; the types left free by the solver were about 70, the rest take a value from R701 p. 3 or the clear junctions, none confirmed by a reading) - blocker: no-key-material; no key on DECODE or in print, the codebreaker's partial key and glosses conflict, and annealing over the one letter does not converge (underdetermined at 420 tokens)
- another letter in the same code - blocker: needs-physical-access; the Venetian correspondence of 1625 (ASVe, or SP 99 at Kew) and the unimaged SP 106/10 leaves are not online

## Escalation
- [x] siblings: R656, R661, R662, R663, R667, R684, R701, R702, R703, R720 placed as worksheets on this letter; every fragment matched to its line
- [x] clear-pages: the clear passages and the endorsement read; the codebreaker's glosses checked against R701 p. 3
- [x] known-keys: R701 p. 3 applied; R658 (system B) is a different table
- [ ] print: not done — CSP Venice vol. 19 (1625-26) not searched for a letter quoting Bethune's 150,000 and Spinola at Breda
- [x] key-rebuild: crib values fixed, four annealing configurations (solve722.py), no convergence
- [n/a] retry: nothing new to retry with; a careful pass fixing only values forced by clear-text junctions is the next step if taken up
