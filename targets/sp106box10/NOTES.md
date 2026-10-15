# TNA SP 106/10: the codebreaker's "Venetian Cifer", c. 1623-24 (DECODE R664, R660; his grid R658; glossed strings R702 p. 2)

Status: in progress (R664 and R660 not yet decoded through with the rebuilt table; see Remaining gaps).
Outcome: read in part (2026-09-20, table 2026-09-21). About 45 values of the three-figure syllabic code aligned from the
codebreaker's interlinear glosses on R664; his own grid R658 rebuilds the code as a systematic syllabary of 117 values,
checked on his glossed strings on R702 p. 2 (46/46 groups). Phrases deciphered; neither letter read through.

**Split on 14 Oct 2026** from the old one-folder entry for the whole SP 106/10 codebreaker's file, under the one-key
rule (George Lasry, 14 Oct 2026). The file held one English codebreaker's work on several different ciphers; each now
has its own entry and page (a different cipher in each):

- [`sp106r725`](../sp106r725/NOTES.md): system A, the two-figure nomenclator with bar and tick marks; his key sheet
  R725 and the worksheets R657. The dating of the file to 1623-24 rests on that key's vocabulary and is set out there.
- [`sp106r722`](../sp106r722/NOTES.md): the second three-figure code, the 1625 letter of a Venetian secretary (R722),
  with the worksheets R656, R661, R662, R663, R667, R684, R701 p. 3, R702 p. 1, R703 and R720.
- [`sp106r704`](../sp106r704/NOTES.md): system C, the letter-and-figure syllabary of R704 and R721.
- [`sp106r931`](../sp106r931/NOTES.md): R931, an English royalist letter of September 1645 in a numerical code, which
  only shares the box with the file (catalogue 58).

This folder keeps system B, the three-figure code the codebreaker calls "the Venetian Cifer" (R701 p. 1), because the
old page's reading and its hero line were of this code. Not part of any entry: a five-line letter cipher on R701 p. 2
(about 120 letters; `cat62/mono701.py`, simple-substitution annealing in five languages failed; too short).

## The documents

| record | ff. | what it is |
|---|---|---|
| R664 | 167-169 | intercept, ~500 groups (DECODE), 45 numbered lines, half in clear Italian, glossed by the codebreaker |
| R660 | 139-140 | intercept, 15 lines, solutions written above the groups |
| R658 | 125 | **the codebreaker's grid of the code**: every group 136-565 in columns by hundreds, his count under each and his value over it; side list of word groups (238 esser, 369 nostro/nostra/nostre, 411 qui, 430 passato/passata, 467 questo, 568 vostro, 440 Spagn-). Upside down in the scan. |
| R702 p. 2 | 182 | his group strings of this code with his glosses (p. 1 belongs to sp106r722) |
| R701 p. 1 | 175 | his heading "Wordes marked with letters in the Venetian Cifer": 369° nostro, 340° misura(?), 467° questo, 369ᵉ nostre, 420' altri, 233ʳ esser, 121ᶜ, 430ᵃ passata (p. 3 belongs to sp106r722, p. 2 is the letter cipher above) |

DECODE lists them as separate anonymous "partially decrypted" ciphertexts, "1558/1625" (the volume's span).
Images fetched from DECODE with the project cookie (git-ignored, main checkout `targets/sp106box10/img/`, rotated
copies in `rot/`).

## System B read in part (R664, R660), 2026-09-20

R664 and R660 are letters written half in clear and half in code: the writer encodes only what matters and leaves
the connective Italian open, which is what made them breakable. R664 f. 1 line 44 is wholly clear:

> "potrete continuare nel modo cominciato, osservando però il [mutamento … alle volte … col … numeri suppositi]"

The code is **syllabic**: one three-figure group per letter or syllable. Values recovered by aligning the
codebreaker's interlinear solutions against the groups (each confirmed by at least one unambiguous word):

    111 al    145 nume(ri)  146 nu    151 ra    152 re    153 tri   154 ro    165 che
    211 del   233 ?         240 et    245 si    252 se    253 si    254 so    255 sa
    260 ta    261 te        262 ti    263 to    312 ?     316 ta?   319 cu    320 in
    340 lette(re) 344 el    356 i     357 l     359 n     366 col   367 ?     411 qui/que
    430 a     433 la        434 le    436 lo    439 ?     456 o     459 r     461 ve
    463 volte 468 quel(lo)  515 da    516 de    518 do    533 ?     535 mi    536 mol
    537 mu    542 quan      544 gua   560 za    568 vostre

(260, 262, 263 and 459 as corrected by the grid, below.) Worked example, R664 f. 1 line 38:

    211 433 436 154 253 319 152 560 312 359 518 367 433
    del la  lo  ro  si  cu  re  za  ·   n   do  ·   la
    → "della loro sicurezza … -ndo … la"

and line 41: `240 | hoggi terzo giorno | 468 434 516 146 456 461 252 359` + line 42 `560`
→ "et hoggi terzo giorno quelle de nuovo senza…". The one apparent conflict (252 sen/se, 359 za/n) resolves when
*senza* runs over the line break (252 se + 359 n + 560 za), which confirms the alignment.

## The grid R658 and "the Venetian Cifer", 2026-09-21

R701 p. 1 names the three-figure code with superscript word-endings "the Venetian Cifer", and those words (369
nostro, 467 questo, 430 passato) are the ones on R658's side list, so the grid R658 is that code, the code of R664
and R660. The grid shows it is a **systematic syllabary**: each consonant takes five consecutive rows in the order
a e i o u, and each hundreds column a different consonant:

    row  x51-x55: 1 ra-ru   2 sa-su   3 sca-scu  4 stra-stru  5 sta-stu
    row  x42-x46: 1 na-nu   2 pa-pu   3 ?        4 pra-pru    5 qua-quo
    row  x60-x64: 1 ?       2 ta-tu   3 tra-tru  4 va-vu      5 za-zu
    row  x56:     a  e  i  o  s(?)     x57-x59: single consonants (157 b, 257 f, 357 l, 457 p; 158 c, 258 g, 358 m, 458 q; 159 d, 359 n, 459 r)
    x33-x37: 4 la-lu, 5 ma-mu;  x15-x19: 3 ca-cu, 5 da-du;  words: 339 liga, 340 lettere, 439 per, 165 che, 465 quel

A word group takes a superscript letter for its ending (369° nostro, 369ª nostra, 369ᵉ nostre). The table is in
`cat62/venetian_code.tsv` (grade H where the codebreaker wrote the value, P where only the pattern predicts it):
117 values, 102 written by him, 15 predicted.

**Check.** `cat62/check_r702.py` decodes every group string the codebreaker glossed on R702 p. 2: 46/46 groups
fall in the table, and each string gives his gloss:

    356 318 436 143 435   i co lo ne li      "i colonelli"
    341 433 436 154       del la lo ro       "della loro"
    252 359 518 253       se n do si         "sendosi"
    167 252 459 [459] 253 con se r (r) si   "conservarsi"
    165 245 556 253 156 526 445 534 261 459  che po s si a mo pro me te r  "che possiamo prometter"
    260 359 263           ta n to            "(in) tanto"
    260 261               ta te              "(capi)tate"

He also glossed "di 24 di maggio", "del campo", "per nome suo", "sono capitate", "nol portar", "efficacia",
"medesime conciette" on the same sheet: the letter he was reading dates from late May and speaks of a camp and of
colonels, which fits 1624 (Mansfeld's levies) or 1625 but is not proof.

**Corrections to the 2026-09-20 values** (from gloss alignment on R664 alone): 260 is ta (not "mento"), 262 ti (not
to), 263 to (not ti), 459 r (not v), 411 is qui in the grid (R664 gloss "que"); 316 "ta" does not fit the
ca-cu run 315-319 and is doubtful.

**Which code is "the Venetian Cifer"?** The R703 session first read R701's heading as naming the code of the 1625
letter (now sp106r722). The heading's words are the words of R658's side list, and R658 is the grid of the R664/R660
code (152 re, 154 ro, 165 che, 560 za, all fixed on R664). The 1625 letter's table (R701 p. 3: 244 ra, 245 re,
366-370 la-lu) is different (R658: 244 pi, 245 po, 433-437 la-lu). So the label belongs to this code; the 1625
letter, whose endorsement calls it a Venetian secretary's, is in a second table built the same way.

## Date

The letters carry no date that has been read. The file they sit in is dated 1623-24 by the vocabulary of the
codebreaker's system-A key (sp106r725: Marques Inichiosa, C. Barberino, Palatinato); R702 p. 2 adds a 24 May and
colonels. Taken here as c. 1623-24, not proved for these two letters.

## Remaining gaps
- R664 ff. 1-3 and R660 continuous reading - blocker: not-attempted; code rebuilt to 117 values from R658, the letters never transcribed group by group and decoded through with it
- groups seen on R664 f. 1 but not valued (233, 312, 367, 439, 477, 534, 551, 556, 566) - blocker: open-codes; to be retried once the letters are transcribed in full
- sender, recipient - blocker: not-attempted; depends on the continuous reading

## Escalation
- [x] siblings: every record of the file R656-R725 opened and placed (the other ciphers are the entries listed above)
- [x] clear-pages: the codebreaker's interlinear glosses on R664 and his glossed strings on R702 p. 2 aligned (46/46 groups)
- [x] known-keys: the codebreaker's own grid R658 applied
- [ ] print: not done — CSP Venice vol. 18 (1623-25) and CSP Domestic 1623-25 not searched for these letters ("di 24 di maggio", colonels, "la loro sicurezza")
- [x] key-rebuild: code rebuilt as a systematic syllabary (cat62/venetian_code.tsv, 117 values)
- [ ] retry: not done — transcribe R664 and R660 in full and decode them with venetian_code.tsv

## Files

- `cat62/venetian_code.tsv`, `cat62/check_r702.py`: the table and its check (this entry).
- `cat62/fetch.py`, `cat62/img.py`: image fetchers for the whole file (shared with the sibling entries).
- `cat62/mono701.py`: the failed attack on the R701 p. 2 letter cipher (not part of any entry).
- Images: main checkout `targets/sp106box10/img/` and `rot/` (all records of the file; git-ignored).
