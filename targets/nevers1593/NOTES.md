# Nevers to Pisany, 8 September and 14 October 1593, in cipher no. 46 (catalogue no. 21)

Split on 14 Oct 2026 under the one-key rule (George Lasry): this entry is key no. 46 and the two letters to Pisany
(fr. 3985 f. 209, fr. 3986 f. 168). The five letters to Revol are in the Court symbol cipher no. 60 and are now their
own entry, [`targets/revol1593/`](../revol1593/) (a different cipher, with its own page, revol1593.html), with
`key60.txt`, `decode60.py`, `atlas60.md`, the f. 146v and f. 157v transcriptions and `f88/`.
`instruction_31aug_print.txt` (the printed Instruction of 31 Aug, a crib for no. 60) stays here because other
targets' French corpora glob `../nevers1593/*.txt`.

Session of 17 September 2026. Target: the seven "lettres avec chiffre" of Louis de Gonzague, duc de Nevers, in
BnF fr. 3985 (nos. 66, 88, 116) and fr. 3986 (nos. 68, 75, 81, 101), all copies, written during his embassy to Rome
for Henri IV's absolution. Catalogue task: apply Tomokiyo's Nevers cipher no. 46 to all seven and measure coverage.

## Result in one paragraph

Cipher no. 46 is the key of the **two letters to Pisany** (fr. 3985 no. 116 = f. 209, 8 Sept; fr. 3986 no. 81 = f. 168,
14 Oct) and of nothing else in the set. Every figure of both letters resolves in the key (122/122 and 268/269 tokens).
The 8 September letter reads continuously; the 14 October letter reads in long stretches with some passages still
garbled by the copyist's figures. The **five letters to Revol** were written in a different key, the Court's symbol
cipher (Tomokiyo's no. 60, "Montreau, août 1593", fr. 3995 f. 108–110), as Tomokiyo's Henri IV article already says:
the 27 August copy (fr. 3985 f. 113–114v) turned out to be entirely in clear, the 9 October copy (fr. 3986 f. 157v)
has two and a half lines of symbol cipher, and nos. 88, 68 and 101 were not reached on the image in this session.
So the catalogue premise "seven letters in one office's key" was wrong: two keys, one numerical (Pisany), one symbolic
(Court). Coverage of no. 46: 2 of 7.

## Sources and routes

* fr. 3985 = Gallica `btv1b90606498` (485 canvases, microfilm, all labelled NP; canvas ≈ 2 × folio: f. 109 = c. 218,
  f. 113 = c. 226, f. 202 = c. 407, f. 209 = c. 419). fr. 3986 = `btv1b9060631k` (481 canvases, same rule: f. 64 = c. 118,
  f. 146 = c. 286, f. 152 = c. 298, f. 156 = c. 306, f. 168 = c. 332). IIIF `full/full` gives 4700–4950 px wide pages,
  enough for two-digit figures at 2–3× crops; the 1400 px canvases are not.
* The item numbers of the BnF notice map to folios only by reading the pencil foliation; the OAI record
  (`services/OAIRecord?ark=`) gives the item list. Item 116 is the 8 Sept Pisany letter (Tomokiyo's "fol. 209"), item 81
  the 14 Oct one (his "fol. 168"). Item 94 is "même contenu que le n° 88", a second copy of the 2 Sept Revol letter (not
  located). Item 77 is the King's Instruction to Nevers of 31 Aug 1593 "avec chiffre et déchiffrement" (not located):
  with fr. 3986 f. 152 (Henri IV to Nevers, Chartres 6 Oct 1593, symbol cipher with interlinear decipherment, c. 298) it
  is the route into the Court key no. 60.
* Key no. 46: fr. 3995 f. 87 (Gallica `btv1b525085665` canvas 169, endorsement "Chelles, octobre 1592" on f. 86 =
  canvas 168), read from the full-resolution image (7677 × 5792, landscape sheet). Transcribed in `key46.txt`.
  Tomokiyo's `nevers_no46.png` is 225 × 300 px and unreadable; his example image gives the reading of one passage.
* Ground truth for the conventions: Girolamo Gondi to Pisany, Florence 22 Sept 1593, fr. 3986 ff. 64–65v (c. 118–121),
  same cipher, with the office's interlinear decipherment: `personne` 52 79 22 17 26 57 57 79, `rencontre`
  22 79 57 92 26 58 13 42 79, `congregation` 92 26 57 40 32 69 40 34 12 63 26 57, `absoudre` 34 90 17 26 15 54 22 79,
  `sainct` 17 34 63 57 92 13, `siege` 17 73 69 40 69, `ladicte` 53̄ 54 63 92 13 79, `Romme` 22 26 49 50 79; `10̄` = qui,
  plain `87` = si. This confirms the alphabet as read from the table.

## The key (no. 46) as read

Two-digit alphabet with homophones: a 34 74 · b 90 · c 92 95 · d 54 55 · e 79 69 · f 71 · g 40 · h 27 · i 63 73 83 (87)
· l 65 77 · m 49 50 · n 57 58 · o 26 36 46 · p 52 21 · qu 19 · r 22 32 42 · s 17 18 · t 12 13 · u 15 25 35 · x 14 · y 76
· z 86. Nulls 66 96 80 (1)99 100; in the letters the single digit 1 (and 0) is also intercalated as a null, as the
sister key no. 45 prescribes ("5 5 1 4 6 8 3 1 2" = d·o i t). Three word series: barred figures 99–2 (au … retirer:
80̄ de, 56̄ je, 51̄ luy, 53̄ la, 26̄ par, 11̄ que, 9̄ quil, 38̄ ne, 73̄ est, 85̄ ce, 97̄ alle, 82̄ come, 19̄ pour, 5̄ recherche …);
plain figures not in the alphabet for S–V words and provinces (24 sa, 28 sans, 29 se, 87 si, 41 temps, 45 tout, 62 vous,
72 Italie …); double-dotted figures for names (99 Pape, 98 Roy, 88 Duc de Nevers, 70 Cardinal Gondi, 89 Duc de Mantoue,
54 Revol, 55 Beaulieu, 34 De Pizany, 1 Ambassadeur …) and a sign for Monsieur. Full table in `key46.txt`.

## fr. 3985 f. 209, Nevers to Pisany, 8 September 1593 (`ct_3985_f209.txt`, `decode_f209.txt`)

One page, three passages in figures inside a clear letter. Transcribed from the full-resolution image, 122 tokens.

1. After "Car j'estois sur ce mesme faict": `50̄ 54 73 17 25 74 55 1 46 83 12 99̈ 80̄ 5̄ 1 42 99̈ 51̄ 76̄ 79 18 53̄ 90 17 36 77
   25 12 83 29` = **l'on dissuadoit [Pape] de rechercher [Pape] luy don[n]es[t] l'absolutio[n]**. Tomokiyo's reading of
   this passage (with 14 for 74 and "Beaulieu") is confirmed and corrected. One of the two 99̈ is probably a slip for
   98̈ Roy ("l'on dissuadoit le Roy de rechercher que le Pape luy donnast l'absolution"); the copy has 99̈ both times.
   Final 29 (se) stands where 26/36/46 + 57/58 (on) is expected.
2. After "Car": `88̈ 97̄ 40 36 76 13 9̄ 38̄ 73̄ 46 76 12 90 69 17 46 73 58 9̄ 34 61 74 13 28 85̄ 53̄ 26̄ 29 11̄ 63 77 38̄ 71 69 42
   83 12 32 63 79 58` + "de" `54̈` = **[Duc de Nevers] alléguoit qu'il n'estoyt besoin qu'il a[l]la[s]t sans cela, parce
   qu'il ne feroit rien … de [Revol]** (61 is a slip for 65 l; Tomokiyo read "atat" and "Beaulieu" for 54̈ = Revol).
   Nevers speaks of himself in the third person, or the copyist substituted the name sign for "je".
3. After "Je suys d'opinion que": `65 46 58 57 34 11 46 77 26 58 13 55 14 69 92 36 57 12 74 58 13 79 42 77 69 21 / 34 52
   79 19 35 79 65 26 58 58 57 83 84 77 65 1 79 21 46 76 57 13` = **l'on n'a [11] volonté d[14]e contanter le Pape, que l'on
   n'[y a]ille poynt**, followed in clear by "Et suys bien ayse que soyez de mesme volonté". 11 stands where u (15) is
   expected and 14 (x) inside "de"; 57 83 84 where y a i is expected. Sense: if there is no will to satisfy the Pope,
   do not go to Rome at all.

## fr. 3986 f. 168, Nevers to Pisany, 14 October 1593 (`ct_3986_f168.txt`, `decode_f168.txt`)

Written the day after Possevino's message at Poschiavo. Seven full lines of figures after "ce qu'il en dit et", a
short run after "fait aussi qu'il", and one more line lower down; 269 tokens, 268 resolve. Continuous readings:

* Line 1: **[Duc de Nevers] ne sera receu come [Ambassadeur] pour pluseurs resons. Je luy a-** (66 and 80 unmarked
  are nulls here, 1 is intercalated in 9·5) — Tomokiyo's fragment, confirmed.
* Line 2: **-y demandé** (55 69 45̄ 58 80̄ = de-ma-n-dé) … **se [Pape] voloit que** … **e[ll]e m'a dit**
* Line 3: **n'avoir autre charge, ne me declarans que** … **je me** …
* Line 4: **conten[t]** … **qu'il de cela et luy** … **[p]l[a]inte de lettre m'est** …
* Line 5: **faict aller** … **pluseurs resons** … **pour en par**…
* Line 6: **[Cardinal Gondi] [Duc de Mantoue] avec de m'avancer de plus pour faire ce que m'a esté escrit, qui est
  conforme**
* Line 7: **au nostre. Ce qu'il faict tenir secret, et le … dans sa … [Cardinal Gondi] a …**
* Last line: **s'est nostre [q]uestion est bruit … secrete, tout yra …**

The garbled stretches (listed in the header of the ct file) are figure-reading problems on a microfilm copy in a
hand where 1/7, 0/8 and 3/5 are close; the segmentation scorer `segscore.py` (lexicon from the repo's French corpora)
did not resolve them. They are the next pass, with the Gondi decipherment as the guide to this copyist's habits.

## What was not done

* No control runs: the key is a recovered table, not a solver output, and the decipherment of Gondi's letter by the
  office is the check.
* Tomokiyo's partial reading of f. 168 stops at "Je luy ay demandé"; nothing else published on these letters was found.
* DECODE was not searched for these items (organisation policy on account creation; metadata search is possible
  without login and was not needed here).

## Files

`key46.txt` (the table), `decode46.py` (decoder; conventions in its docstring), `segscore.py` (lexicon scorer for
alternative segmentations), `ct_3985_f209.txt`, `ct_3986_f168.txt` (transcriptions), `decode_f209.txt`,
`decode_f168.txt` (decoder output). Page crops for the write-up in `docs/nevers1593_*.jpg`. The no. 60 files are in `targets/revol1593/`.

## The Revol letters: split off

The five letters to Revol (fr. 3985 ff. 88, 115, 176; fr. 3986 ff. 146v, 157v, 198) and key no. 60, with the
sessions of 17 Sept and issue #32 (12 Oct 2026), are in `targets/revol1593/NOTES.md`.

## Remaining gaps
- fr. 3986 f. 168, Pisany 14 Oct, garbled stretches of lines 2-8 - blocker: illegible; microfilm copy, 1/7, 0/8, 3/5 confusable; segscore.py did not resolve them

## Escalation
- [x] siblings: Gondi to Pisany, Florence 22 Sept 1593 (fr. 3986 ff. 64-65v), same key, interlined by the office: used as ground truth for the conventions
- [x] clear-pages: the clear parts of both letters read; no decipherment of either letter on the leaves
- [x] known-keys: Tomokiyo's no. 46 (fr. 3995 f. 87) transcribed at full resolution and applied; sister key no. 45 gives the null convention
- [x] print: Tomokiyo (cryptiana nevers.htm) reads passage 1 of f. 209 and line 1 of f. 168; nothing else published on these letters was found (17 Sept 2026)
- [n/a] key-rebuild: the key is the archive table, every figure of both letters resolves (122/122, 268/269); the gaps are figure readings, not key values
- [x] retry: f. 168's doubtful figures re-scored with segscore.py over alternative null placements; not settled
