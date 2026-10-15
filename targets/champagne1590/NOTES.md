# Champagne news-letters to the duc de Nevers, June 1590 (BnF fr. 3623 nos. 24, 25, 60; catalogue no. 30)

Status: read in part. The two-digit alphabet of nos. 24, 25 and 60 (June 1590, one hand), rebuilt from a few letters
glossed over the figures and from the alphabetical order of its values: 63 of 104 figures read, ten of the twelve
cipher passages in whole or in part. No. 78 (1591), one group of about six mixed signs in another code, is listed
here unread, with no claim that it shares the key.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). Until then this target also held two other
ciphers, each now with its own folder and page (a different cipher, with its own page):
- no. 23 (Bienvenut, Paris, 28 Feb 1590), a nine-entry name code read with its own key slip (f. 36r):
  [`targets/bienvenut1590/`](../bienvenut1590/NOTES.md). Its numbers conflict with this alphabet (there 35 = Mayenne,
  37 = M. de Nemours, 53 = Saint-Sorlin; here 35 = a, 37 = c, 53 = i), so it is a different key;
- Laurière's (Honoré Mauroy La Verrière's) letters of 1593 in Nevers key no. 57 (fr. 3625 nos. 55 and 10, fr. 3985
  f. 58): [`targets/lauriere1593/`](../lauriere1593/NOTES.md); their files moved there on 14 Oct 2026.

Session of 21 September 2026. Target: BnF fr. 3623 nos. 23, 24, 25, 60, 78 (Gallica `btv1b525245007`) and fr. 3625
no. 55 (Gallica `btv1b52511322v`), all "avec chiffre" in the BnF notice (catalogue item 30). The sections below that
concern this entry are kept as written; the others are pointers.

## Prior work checked

* Tomokiyo, cryptiana `code/nevers.htm` (copy in `research/gallica_siblings/src/nevers.htm`): the Nevers keys nos. 1–70 of
  fr. 3995 are catalogued there. **Correction (29 Sept 2026):** no. 57 (fol. 102, February 1593, "Mons. de Laveriere")
  is Laurière's key and reads no. 55; the first pass missed it because of the spelling La Verrière / Laurière. For
  fr. 3623, none of them is named, and his GL.htm list has no entry for
  either manuscript. Key no. 23 is not needed: the letter carries its own key (f. 36r). The two-digit key of
  nos. 24/25/60 is alphabetical, not one of the random-order Nevers tables such as no. 46 (`targets/nevers1593/key46.txt`:
  a = 34 74, d = 54 55; here d = 38, i = 53 54), so no. 46 does not fit.
* DECODE: records R9453 (no. 23, f. 35), R9454 (no. 24, f. 37), R9455 (no. 25, f. 38), R9459 (no. 60, f. 88),
  R9460 (no. 78, f. 111), all "Non-decrypted", from `research/catalogue_harvest/decode/list.json`. They give the folios.
  Siblings R9456 (no. 26, f. 39, a long letter entirely in figures with interlinear decipherment, "de Sy, XI
  janvier") and R9457 (no. 27, f. 41) are in another key (frequent 24 73 95 63; not the alphabetical table).
* No printed decipherment found (the items are not in the Mémoires de Nevers index in Tomokiyo's article).

## Access

Gallica IIIF: canvas = 2 × folio + 9 in fr. 3623 (f. 35r = canvas 79, f. 88r = 185, f. 111r = 233);
fr. 3625 f. 10r = canvas 31 (canvas = 2 × folio + 11 near the start). Full resolution is 4000 × 5800. Gallica
throttles (403/empty files) after about ten full-size requests; wait and retry. Images are git-ignored.

## No. 23: moved to bienvenut1590

Bienvenut's copy of 28 Feb 1590 with its key slip f. 36r is now `../bienvenut1590/`.

## Nos. 24, 25, 60: the two-digit alphabet (`ct_3623_twodigit.txt`, 104 figures measured)

No. 24 (f. 37r, "Du 15 juin 1590"), no. 25 (f. 38r, "Du cinquiesme juin 1590") and no. 60 (f. 88r, a slip, 7 June
1590) are in one hand. The cipher passages are short runs of two-digit figures inside clear text. No. 25 and
no. 60 have a few letters written over single figures (faint, the decipherer's hand); those anchor:
`dunion`-type glosses over 58 93 63 54, `a` over 34, `L u d o v i c` over no. 60's run, `n` over 64.

Reading the anchors against the contexts gives a table that rises with the alphabet:

    a 30 32? 33 34 35 · c 37 · d 38 · e 42 43 45 · f 46 · g 47 · h? 48 · i 53 54 · l 56 58 ·
    n 63 64 · o 67 · r 74? 75 · s 82 83 84 86 · t 92? · u/v 93 94? 95?
    words / nulls below 30 and at 39: 12 (de), 16, 17, 19, 39 (prefix or null, 5 times), 89, 99

Readings (C = from an interlinear gloss, I = from the alphabetical order and context):

| Place | Figures | Reading | Grade |
|---|---|---|---|
| 25, "la rupture de l'edict" | 12 58 93 63 54 67 64 19 | [de] l'union [19] | C/I |
| 25, "contre" | 56 34 56 54 47 93 43 | la ligue | C/I |
| 25, "Je a aussi" | 39 38 42 56 34 38 43 46 54 35 63 37 42 38 93 17 | [39] de la defiance du [17] | I |
| 25, "qu'on dict" | 17 33 53 56 82 45 38 45 46 54 43 38 93 39 | [17] ailse? … defie du [39] | I, first half open |
| 25, "qui faict les affaires" | 39 38 43 37 48 32 83 45 74 67 63 | [39] de Chazeron (48 = h, 32 = a) | I; Chazeron is named in clear in no. 24 |
| 25, "vostre" | 89 84 42 75 93 54 37 45 | [89] service | I |
| 60, "du sr" | 19 56 93 38 67 93 53 37 | [19] Ludovic | C |
| 60, "en est aussi" | 39 38 43 56 35 94 62 32 64 | [39] de la V?an | I, name open |
| 24, "du faict" | 99 38 39 45 30 93 38 67 92 52 37 | ? d ? e a u d o t ? c | open |
| 24, "mal disposé" | 16 39 56 43 99 95 93 35 92 05 54 86 | [16] ? le ? u u a t ? i s | open |

The alphabetical ordering is the check: every anchored value fell into the slot its letter predicts, and the
I-grade readings were made only with values inside their predicted slot. Code numbers 12, 16, 17, 19, 39, 89, 99
and the plain numbers in no. 24 (22, 51, 84, 44) have no key.

## No. 78 (f. 111r, 1591, on the tailles of the Nivernais)

A clear letter with one cipher group near the end, "... traictast de 96 □ 3 9̄ f 3 ..." (`ct_3623_78.txt`),
mixed figures and signs. Too short to read; probably a name. Open.

No. 78's group was also tried with Laurière's key no. 57 (29 Sept 2026): "ch ? da [Dauphiné] o da", no sense.

## Laurière's 1593 letters: moved to lauriere1593

Fr. 3625 no. 55 (Châlons, 9 Jul 1593), no. 10 (Courgenay, 13 Jul 1593) and fr. 3985 f. 58 (Poissy, 12 Aug 1593), the
first-pass table from no. 10, key no. 57 and setsunaatto's blind test are in `../lauriere1593/`. On 3 Oct 2026 key
no. 57 (its syllables and the whole word list) was applied to the two-digit runs of nos. 24/25/60: no sense ("qui pi
bo ni lo fi …"), a different, alphabetical two-digit system.

## Third pass (3 Oct 2026): two-digit search

* **Nos. 24/25/60, ciphertext-only (`anneal_twodigit.py`).** The anchored values rise with the alphabet, so each
  unknown letter value is bracketed between its known neighbours: 52 in h–i, 62 in l–n, 92 in s–v, 94 in u–v, 95 in
  u–z. The space is small (2 × 3 × 4 × 2 × 5 = 240), so it was enumerated rather than annealed and scored with
  `fr-1600-letters` over all ten runs, code numbers left out. Best: 52 = i, 62 = n, 92 = u/v (tie), 95 = y. That gives
  "de Launan" (no. 60, "en est aussi [39] de la V?an") and "…audovic" (no. 24, "du faict 99 38 39 45 30 93 38 67 92
  52 37"). **None of these passes the second-occurrence rule.** 52, 62, 94 and 95 occur once each. 92 occurs twice: in
  no. 24 line 22 it gives "le [99] y u a v [05] i s" with no sense. The code numbers (05 12 16 17 19 39 89 99) are words
  or names, and an LM cannot fill them. Count unchanged at 63/104.

## What is open

* The two no. 24 passages, the first half of one no. 25 passage, the name in no. 60, all code numbers of the
  two-digit key; no. 78's one group.

Measured on this entry's documents (14 Oct 2026): 63 of 104 figures of nos. 24/25/60, 0 of 6 of no. 78: 63 of 110
(57.3%). The earlier target figure (383/444, 86.3%) pooled the key no. 57 letters and is superseded.

## Files

* `ct_3623_twodigit.txt` — figures of nos. 24, 25, 60 (104 tokens, 40 distinct, measured).
* `ct_3623_78.txt` — the one group of no. 78.
* `anneal_twodigit.py` — bracketed LM search for the unknown two-digit letter values of nos. 24/25/60 (3 Oct 2026).
* `validation.tsv` — the anchored letter values of nos. 24/25/60 (14 Oct 2026; `docs/_validate.py`: too short).
* Images in `img/` (git-ignored, not committed), in the main checkout's `targets/champagne1590/img/` (shared with
  the two split-off entries).

## Remaining gaps

- Nos. 24/25/60 code numbers 12, 16, 17, 19, 39, 89, 99 and the plain numbers of no. 24 (22, 51, 84, 44) - blocker: open-codes; no key bound with these letters; the alphabetical two-digit table covers letters only
- No. 24 two passages, first half of the no. 25 'qu'on dict' passage, the name in no. 60 ('de la V?an') - blocker: open-codes; values fall outside the anchored slots of the alphabetical table (30-39, 48, 92-99 uncertain); no gloss over them
- No. 78 (f. 111r), one group of about six mixed signs - blocker: too-short; a single group, probably a name, in a different mixed code
- Nos. 24/25/60 runs tried with key no. 57 (words57.tsv, syllables): no sense ('qui pi bo ni lo fi ...'); a different, alphabetical two-digit system; bracketed exhaustive LM search (anneal_twodigit.py) proposes 52 i, 62 n, 92 u/v, 95 y but none verifies on a second occurrence - blocker: open-codes; no key or gloss for the code numbers, single-occurrence letter values cannot be checked

## Escalation

- [x] siblings: DECODE siblings R9456/R9457 (nos. 26, 27) checked, another key; fr. 3623 nos. 23-27 and 60 viewed
- [x] clear-pages: the interlinear glosses on nos. 25 and 60 used as anchors; no clear copy of nos. 24/25/60
- [x] known-keys: Nevers keys of fr. 3995 (Tomokiyo nevers.htm) reviewed; no. 46 tested against the two-digit table and does not fit; no. 57 tried on no. 78's group (no sense) and on the two-digit runs (3 Oct 2026, no sense); no. 23's name key conflicts with the alphabet
- [x] print: Tomokiyo nevers.htm and GL.htm, Memoires de Nevers index: no printed decipherment
- [x] key-rebuild: table bracketed by alphabetical order, the anchored slots filled; 3 Oct 2026 exhaustive LM search of the bracketed values (anneal_twodigit.py), none verifies on a second occurrence; the code numbers have no gloss to fit
- [x] retry: all ten runs re-scored with the bracketed candidates (3 Oct 2026); no change in the count
