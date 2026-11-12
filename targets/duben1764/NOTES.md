# duben1764: C.W. von Düben's code letters to Gyldenstolpe and Lovisa Ulrika, 1764-1765

Status: in progress

Unsolved Catalogue no. 450. Riksarkivet, Kungliga arkiv, Drottning Lovisa Ulrika, Utgångna skrivelser,
SE/RA/710003/02/008/b/K 259 ("Lovisa Ulrikas hemliga korr. m.m.", 1752-1773 spridda år), 223 images,
IIIF manifest https://lbiiif.riksarkivet.se/arkis!A0073297/manifest, viewer
https://sok.riksarkivet.se/bildvisning/A0073297_00107. Images are git-ignored (img/); fetch with
`https://lbiiif.riksarkivet.se/arkis!A0073297_NNNNN/full/max/0/default.jpg`.

## What the volume holds (survey of all 223 images, 26 Oct 2026)

| Images | Content |
|---|---|
| 1-76 | Clear French and Swedish letters (queen's correspondence, other years) |
| 77-84 | Film targets; folder sheet 84 "C.W. von Düben till N.P. Gyldenstolpe och Lovisa Ulrika 1764-1765" |
| 85-86 | Swedish clear text "Nyheter från Finland", headed "Chiffer n:o 1" |
| 87-117 | **Chiffer n:o 1**: St Petersburg letters to "Mon cher Comte" (Gyldenstolpe), Feb-Aug 1764, all-cipher pages with clear decipherment pages in a second hand filed among them; 113 signed "Düben" |
| 118-127 | **Chiffer n:o 2**: Düben to the Queen ("Sire votre Mté"), 5 Oct 1764 - 15 Nov 1765; clear text of the 5 Oct letter on 120 |
| 128-215 | Other clear correspondence (folder 129 "N.P. Gyldenstolpe ... C.W. von Düben ... Lovisa Ulrika 1764-1766") |
| 216-220 | Folder "Chiffernycklar" and three key tables |

The archivist's notes on the clear pages tie them to the ciphers: 102R "Hör till chiffermeddelandet
"4.83.445.196.552" etc 6 mars 1764 n.st." (the cipher on 101R starts with exactly those groups), 97R
"... "15.73.100.347.503.401.107.536."" (cipher on 96), 106R "Till chifferbrevet av den 15/4 maj 1764",
109R "... 15 juni 1764", 116 "... 20/31 aug. 1764". The clear pages are bound out of order (the clear page
facing a cipher usually belongs to another letter).

Cipher letters seen (first groups): 87-89 (no date seen), 90R "96.70.171..." , 91-93, 96 (Jan 1765? / 1764?,
"15.73.100.347..."), 97L, 100R-101L, 101R-102L (6 Mar 1764, "4.83.445.196.552"), 104R (15 May,
"179.479.409..."), 105R (15/4 May, "Mon cher Comte," then "66.74.100.347..."), 107R ("448.6.361.226..."),
108R-109L (15 June 1764, "No 1"), 110R-111 (20/31 Aug 1764), 112, 114-115, 118-119 (5 Oct 1764, to the
Queen), 121 (31 Dec 1764 v.st.), 122-124 (15 Nov 1765). Not yet counted page by page.

## The key tables (218-220)

- 218: a Swedish key (values 121-999, syllables in alphabetical blocks with names: "Sena: Duben" 951,
  "Felt Mar: Fersen", "Senat: Ribbing", "Senat: Horn", Panin, Petersburg). Rule written on it: two
  meaningless numbers at the start and end of each period or ciphered word; zeros added at will; read by
  threes.
- 219: the crown prince's travel cipher, 1770-71 (a later copy; note: printed in Svenska Akademiens
  Handlingar 29 p. 259).
- 220: a "marque ###" key (111-948; Votre Mté, Panin, Bestucheff, Comte Solms, Grand Duc); seven leading nulls,
  zeros mark apostrophes.

None fits the letters as is: the letters use 1-~790 with nothing in 8xx-9xx, and the most frequent groups
(218, 107, 7) are not in the right places in these tables.

## The system (so far)

Numeric groups 1-~760 separated by dots, scribe's vertical strokes between runs, a few groups underlined or
dotted. Flat frequencies (top groups about 4% each; 204 distinct in 821 groups on 5 Oct, 228 in 641 on
6 Mar). Not identified. (An earlier note here said the 5 Oct opening matched the draft "word for word"; that
was a count coincidence and is withdrawn.)

## The clear pages do not decipher the ciphers (as far as tested)

*Withdrawn for system B and the 5 Oct 1764 letter on 12 Nov 2026 (see the last two sections): the clear on 120 is the plaintext of 118-119R, and a key built from it passes a held-out test. Still standing for system A (6 Mar 1764 and 15 Nov 1765): issue #437 reports the opposite, but its key and scripts are not in the repository (see below).*

Two pairs transcribed in full:

| Pair | Cipher | Clear | Ratio |
|---|---|---|---|
| 6 Mar 1764 | tx/c1764-03-06.txt, 101R-102L, 641 groups, 49 ? | tx/p1764-03-06.txt, 102R-103R, 626 words, 2733 letters | 4.3 letters/group |
| 5 Oct 1764 | tx/c1764-10-05.txt, 118-119R, 821 groups, 55 ? | tx/p1764-10-05(.final).txt, 120, 373 words, 1682 letters | 2.0 letters/group |

The 5 Oct clear page is a draft in the writer's own composition (struck phrases rewritten, "n'ay epargné" ->
"n'ai negligé"), not a decipherment. Both the cipher page and the draft open "Sire Votre Majesté", so they
are the same despatch, but:

- fb.py (soft EM over all segmentations, each group = null or 1-4 letters, fixed length penalty) solves a
  control exactly: the 5 Oct draft enciphered in a synthetic syllabic code with nulls (top-share 1.0), and
  still 0.985 with 7% of the groups corrupted.
- On the real pairs it finds nothing: 5 Oct 0.454 (0.464 with plaintext skips, 0.443 with the cipher
  reversed); 6 Mar with skips 0.445.
- One group per letter at offsets 0-39: 0.567 against 0.544 for shuffled ciphers (max 0.58): nothing.
- Repeats do not line up either: "215 9 549 317" at 7%, 14%, 39% of the 5 Oct cipher, "Votre M" at 34%,
  52%, 92%, 99% of the draft; "d'une revolution totale" at 30% and 78% of the 6 Mar clear, "255 505 196 55x"
  at 31% and 60% of the cipher.

So the cipher is not its filed clear text enciphered in order with a fixed table of short values. Open
explanations: the clear pages are the open (ostensible) letters or drafts sent alongside a separate secret
text; or the text was rearranged before encipherment (lines or blocks out of order, a route); or the values
change through the text (an additive or a changing table, e.g. one of the keys at 218-220 used with a
running offset). The earlier hard-EM runs (wem.py, lem.py) were void: they failed their own control.

## Ciphertext-only attempt (5 Oct 1764)

homo.py anneals a group -> letter map scored on lang/ `fr-1750-nospace` (order 5), with an optional
letter-count penalty. Control first, at the same size: the first 821 letters of the 6 Mar clear text in 204
homophones (203 used). The true text scores -1.92/char; the solver stops at -2.21 to -2.29 in e-flood or
gibberish optima (200k-2M moves, several temperatures and penalty weights). The control is not recovered and
the failure is in the search (the truth outscores everything found), so the real 821-group text was not
judged by this tool: its output would mean nothing. This is the same ceiling goertz1717 hit (809 letters,
174 homophones, control never recovered). At about 4 occurrences per group the letter is near the limit of
homophonic solving; a syllabic reading (fewer letters per group, more types) would be harder still.

## Two systems, and one letter deciphered at the time (26 Oct 2026, second pass)

Value profiles split the transcribed texts into two systems:

| System | Letters | Groups | Cosine within | Shared bigrams |
|---|---|---|---|---|
| A | 6 Mar 1764 (101R-102L); 15 Nov 1765 (124R-126) | 641 + 742 | 0.753 | 65 |
| B ("Chiffer n:o 2") | 5 Oct 1764 (118-119R); 31 Dec 1764 (121), 122L-R, 123R, 124L | 821 + 1,247 | 0.923 | 269 |

Between A and B the cosine is 0.08-0.10 with 0-1 shared bigrams.

**The 15 Nov 1765 letter (system A) has an interlinear decipherment** over 36 of its 47 number lines
(tx/g1765-11-15.txt). It opens in clear ("Monsieur, Ne soyés pas étonné, mon cher Comte, du Silence que j'ay
gardé..."), then glossed cipher ("Si bien auroit il été Superflu de rien ajouter a ce que j'ai eû l'honneur
de Vous ecrire..."), on the King's approach to the Russian court about the Crown Prince's marriage and the
orders of the Seraphim and St Andrew. Signed with a monogram read "C. F.?", postscript "un million de
complimens, à Mme Mörner". The writer is therefore not certainly Düben; to identify.

The gloss is a positioned decipherment (checked on the image): the French sits over the groups it
renders, the scribe's strokes fall at sentence breaks under it ("517 | 584" where "Si bien..." starts,
"583 | 358" under "a propos de | prendre", "213 | 39" under "depart. | Les Suites"), and horizontal rules
fence off the unglossed lines (125L.09, 12-16; also 125R.05/11/12, 126.13). 56 75 100 135 517 is a preamble.

But it does not yield a fixed table:
- fb.py gets 0.61-0.64 against it (controls 0.985-1.0).
- For every group seen on 3+ glossed lines, no letter string is common to all their French lines (218 on 15
  lines: not even "de" or "es").
- Repeated plaintext takes different groups: "L: L: M: M:" over 555 215 424 526 (124R.08) and 584 143 401 171
  (125L.03), no constant difference; "l'Imperatrice" and "l'ordre" twice each with no shared groups.
- A few runs recur ("540 347" three times, "620 660" twice under "mariage" and once elsewhere).

So the values change through the text: an additive key, a table switched by sentence (the strokes and the
preamble could be indicators), or a book/keytext position code. A hand rebuild of a single table is not
possible, and there is no key yet to test on 6 Mar 1764.

**System B pooled**: 2,072 groups, 291 distinct (about 7 per symbol). A same-size homophonic control
(2,072 letters, 291 homophones) is still not recovered by homo.py (orders 4 and 5, chi-square and KL
letter penalties, 1.5M moves): e-flood or gibberish. The real pooled text was not judged.

## Brice Dudout's report (email of 27 Oct 2026)

Catalogue 450: Frederick II's letter of 3 March 1765 in this group is printed in the *Politische Correspondenz*,
vol. 24, no. 15458. That covers one letter only. Düben's own code letters (systems A and B above) are not affected. Next:
identify which K 259 images hold the 3 March 1765 letter and compare them with the PC text as a crib for its system.

## Remaining gaps

- System A: the 15 Nov 1765 gloss shows the values vary (above). Next: align the gloss word by word to its
  groups by position (strokes as anchors) and test variable-key models against those pairs: an additive
  with short period (differences between groups for the same syllable), a table switched at each stroke
  (the 5-group preamble as indicator), a book code (group = position in a page). Identify the writer
  "C. F." of 15 Nov 1765.
- System B (2,072 groups pooled): the Python homophonic annealer fails its control even at this size;
  an AZdecrypt-class solver is the next ciphertext-only step; a block-order test
  (align cipher lines or stroke segments against the draft out of order); group-by-group tests of the
  three key tables at 218-220, including with constant offsets.
- Transcribe the other cipher letters (87-100, 104-117, 121-127) to pool statistics: the code may be
  shared across letters of one series.
- Read the other clear pages for any that is a true decipherment (no compositional corrections).

## Escalation

- Siblings: the clear pages filed with the ciphers were tested as plaintext for two letters (6 Mar,
  5 Oct 1764) with a control-validated aligner: no fit. The other clear pages are not yet checked.
- Known keys: the three tables at 218-220 were checked by value range only; a group-by-group test is
  still to do once some values are known.
- Print: no edition found (web search 26 Oct 2026); check Svenska Akademiens Handlingar 29 and the
  Malmström / Odhner literature on Lovisa Ulrika's 1764-66 intrigues for printed extracts.

## Bryan Payne / Codex contribution, 28 October 2026

Additional research is preserved in [payne2026/NOTES.md](payne2026/NOTES.md), with a concise [report](payne2026/REPORT.md). It adds the 870-group preliminary May transcription, preliminary tables 218–220, samples of the 162–168 vocabulary key, the public F474 page map and archival leads. Key 219 positively matches the separate printed February 1771 fragment cited on the sheet: [source and literal readings](payne2026/KEY219_PROVENANCE.md). This supplies a fragment decode only; neither the May letter nor the whole 1771 letter is claimed read. Existing research above is preserved; the contribution's provisional 126 pairing does not replace the positioned-gloss work above. Failed-control outputs remain unaccepted.

## 12 Nov 2026 — system B key rebuilt and passed a held-out test; 121-124L read in part (Brice Dudout, Claude Opus 5.5)

Worked in `dudout/` (see `dudout/README.md`). The 120 clear is the plaintext of the 5 Oct 1764 cipher (118-119R)
(it carries struck and rewritten phrases and omits the closing formula, so it is a draft of the letter, not certainly a
clerk's decipherment; the contributor calls it the decipherment): the cipher's repeats fall at the clear's repeats (155.453 = Votre Majesté at 0.36/0.52/0.90/0.97 vs 0.34/0.52/0.93/1.00;
403.240.709 = dis-po-si- at 0.21/0.73 vs 0.21/0.74). System B is a fixed two-part syllabic nomenclator with homophones
(614 n, 119 r, 354 e, 136 de, 453 majesté, 54 interet; 549 = apostrophe, 9 = j; not all groups under 100 are nulls).
A key built by anchored EM alignment on 118.00-119L.06 only was measured once, as pre-registered, on the held-out
119L.07-119R.05 (328 groups): 0.563 against 400 controls (max 0.083). With 25 values added afterwards from context,
121-124L (to "mon cher Comte": Count Osterman, the Empress's support for the King at the coming Diet, Düben's failure
"ce n'est assurément pas ma faute") is read in part: 442 of 744 word tokens sure (59.4% by the README rule: the 77 probable
words use the 25 context values or restored letters and are holes); the contributor's sure + probable count is about 70%.
This withdraws, for system B, "the clear pages do not decipher the ciphers" and the 5 Oct "not a decipherment" verdict above
(the draft is the cipher's plaintext).

### System A claim of issue #437 (Brice Dudout, 11 Nov 2026), not verifiable here

The issue says that both system A letters (6 Mar 1764; 15 Nov 1765) were deciphered at the time, that the gloss of 15 Nov
1765 runs ahead of the cipher by one to three lines, and that one fixed key (key_c01, 217 values, rebuilt from image 96 and
the clear 97R-99L) reads both (coverage 0.544 against controls max 0.061; 0.261 against 0.043). Its key, its transcription of
101 d and its scripts are not in the repository nor in PR #477. Not checked: the key, the coverage figures, the 28 anchors, the
offset beyond six printed lines, the "unglossed lines". Checked on this repository's own transcriptions, without his key
(12 Nov 2026): over the whole 15 Nov 1765 letter, of 450 pairs (cipher group seen 6 times or more against a gloss word seen
4 times or more, by position in the text), the two best are exactly the issue's values, 540 = que and 218 = de (mean position
gap 0.0103 and 0.0114; 100 shuffles of the cipher give a best of 0.0122 or worse), so these two groups behave as fixed
values through the letter; for 6 Mar 1764, 107 = a ranks third and 218 = de, 540 = que are not distinguishable from shuffles;
the six decoded lines printed in the issue use one table without a conflict (19 values used two or three times) and
124R.07 decodes "de rien ajouter a ce que j'ai eu l'honneur" where the gloss line 124R.07G begins "a ce que", the direction
of the claimed offset. This is support for "values do not vary" on two values, not a decipherment. The statement "values
vary through the text" above is left as written until the key is shared; catalogue 1616 is not changed to "existing
decipherment".

### Integration check (12 Nov 2026)

Reproduced: `dudout/scripts/measure.py` (seed 450, start 978) gives M 0.5633 on 328 held-out groups (255 known), controls
max 0.0833 (permuted keys) and 0.0756 (shuffled text), margin 0.480; my own decoder gives the same decoded string as
`measure_result.json`. The frozen SHA-256 values match all ten present files (the clear on 120 is Daniel's file, unchanged).
No held-out group uses a key value that is absent from the build part (0 of 255). The order of events (hash list before the
measure) is by the contributor's record. anchors_final.json holds 29 entries, not 26. Corrections made: the 120 clear is a
draft (above); 121-124L strict share 59.4% (70% labelled the contributor's); the contributor's own "Status: read in part"
line in `dudout/README.md` was reworded; the target status stays **in progress** because system A and 40% of 121-124L are open
without an outside blocker. Not checked: the held-out and build transcriptions against the Riksarkivet images; the 121-124L
reading beyond the sample read. No write-up page is written until system A or the escalation steps are done (a system-B page
is owed if the maintainer wants one). The 25 post-measure values are not validated by a second held-out text.
