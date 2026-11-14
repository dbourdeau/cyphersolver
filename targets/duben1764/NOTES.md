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

*Withdrawn for system B and the 5 Oct 1764 letter on 12 Nov 2026 (see the last two sections): the clear on 120 is the plaintext of 118-119R, and a key built from it passes a held-out test. Withdrawn for system A on 14 Nov 2026 too: key_c01 (PR #566), built on letter 96 and its clear only, decodes 6 Mar 1764 as its clear on 102R-103R and 15 Nov 1765 as its gloss (see the 14 Nov section). The fb.py failures below came from the clear running far beyond the cipher (6 Mar) and from the offset of the gloss (15 Nov), not from a changing key.*

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

The gloss is a positioned decipherment (checked on the image; *withdrawn 14 Nov 2026: decoded with key_c01 the cipher lags the gloss, see below*): the French sits over the groups it
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

*Withdrawn on 14 Nov 2026: the gloss is not positioned (it runs ahead of the cipher, about six lines by 125L.12) and one fixed key, key_c01, decodes the letter (14 Nov section). The paragraph is kept as the record of the reasoning.* So the values change through the text: an additive key, a table switched by sentence (the strokes and the
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

- System A (6 Mar 1764, 15 Nov 1765): both letters were deciphered at the time and key_c01 decodes both (14 Nov section). Open,
  all workable: the strict word count and English translation of each period decipherment (the 102R-103L.08 part of the clear
  for 6 Mar; the gloss for 15 Nov, rearranged to the cipher's order with key_c01), then `outcome.texts` entries; locating the cipher
  of the rest of the 6 Mar clear (103L.08 on: 100R-101L is a candidate); key_c01 is partial (197 groups with a value; 58 of the
  169 group types of 101R have none) and some values are mis-cut by the alignment ("kie" = je, "limp", "sama", "ontje");
  two group readings doubtful on the images (101 L09 last group 187 or 184; 96 L02 409 or 609). Identify the writer "C. F." of
  15 Nov 1765.
- System B: done for the two letters of the Chiffer n:o 2 folder (key rebuilt and tested on 12 Nov, re-tested and
  completed on 13 Nov against the clear on 127-128; see the 12 and 13 Nov sections below). Open: the 12 key tokens with no
  value (dates, 236, 339, 55, 234) and the single-occurrence values of key c04, which no further text tests.
- Chiffer n:o 1, 15 June 1764 (108R-110R): done through its clear 109R-110L (14 Nov, PR #582; strict 337 of 342 words). Open,
  workable: the end of the cipher on 110R is not in the frozen transcription; 74 groups differ between the two passes.
- The other letters of Chiffer n:o 1 (inventory in `dudout/system_a/INVENTORY_chiffer1.md`), workable from the online images:
  15 May 1764 (104R or 105R-108L; clear 106R-107L), 20/31 Aug 1764 (110R-115; clear 116-117), 100R (perhaps the rest of
  6 Mar), and the two without an identified clear, 87-89 (value profile unlike system A) and 90R-93L (94-95, a clear
  letter of 30 Jan, may belong to one of them).
- Read the other clear pages for any that is a true decipherment (no compositional corrections).

## Escalation

- Siblings: the clear pages filed with the ciphers are decipherments for 96 (97R-99L), 6 Mar 1764 (102R-103R), 5 Oct
  1764 (120) and 31 Dec 1764 (127-128); the earlier "no fit" for 6 Mar and 5 Oct is withdrawn. 109R-110L is the decipherment of
  15 June 1764 (PR #582). The other clear pages (106R-107L, 116-117, 94-95) are not yet checked.
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

*Superseded on 14 Nov 2026: the key and scripts came with PR #566 and the claim is checked in the 14 Nov section below.*

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

## 13 Nov 2026 — the clear of 121-124L is on images 127-128 (Brice Dudout, Claude Opus 5.5)

Images 127-128 ("Tillhör brev av den 31/12 1764") are the clear of the 31 Dec 1764 Chiffer n:o 2 letter (121, 122L, 123R,
124L, then 122R). This withdraws "No decipherment" for that document. One pre-registered re-test of the frozen 12 Nov
system B key (built on 118.00-119L.06 only) against this new clear, transcribed twice and hashed first: M 0.5353 vs
400 controls max 0.0593 (same metric and thresholds as on 12 Nov). Fourteen of 15 values read from context before the clear
was seen are confirmed. Key completed by alignment (dudout/c04/key_systemB_c04.json, 1,236 of 1,247 groups); the 5 Oct letter,
not used for those changes, rises from 0.699 to 0.825 against its clear. The letter is read from its contemporary clear;
system B now has no text without a clear in this volume. System A (6 Mar 1764, 15 Nov 1765) unchanged. See dudout/c04/README.md.

### Integration check of the 13 Nov contribution (PR #541, 13 Nov 2026)

Reproduced: `dudout/c04/scripts/measure_clair.py`, run with its paths pointed at the repository files (key_c03 =
`dudout/key_systemB_c03.json`, c03b_ajouts = `dudout/key_systemB_c03b_additions.json`, lecture_121-124L =
`tx/c-chiffer2-121-124.txt`, clear = `dudout/c04/frozen/127-128_norm.txt`), gives exactly M 0.5353 (1,032 of 1,247 groups
known; permuted keys max 0.0593, shuffled orders max 0.0586) and 0.6943 with the 25 context values. All ten SHA-256 values
in `dudout/c04/frozen/SHA256SUMS-PREREG` match the files (the lexicon line is `lang/lexicons/fr.json.gz`). The re-tested key
`key_systemB_c03.json` carries the hash frozen on 12 Nov and was committed in PR #477 on 12 Nov, before the 127-128
identification, so the key side of the test is externally dated; the order of events within 13 Nov (N_draft before the clear
was seen, the amendment before the clear was transcribed) is by the contributor's record. The 121-124L cipher had already
been decoded on 12 Nov with this key and 25 context values (declared by the contributor); the clear was not.

Own decoder (written from the key files, not importing the contributor's): c03 0.5353, c03 + additions 0.6943, c04 0.9461
against the 127-128 clear (the last is circular: c04 was completed from that clear). Unknown to c04: 12 group tokens (236 x3,
481, 150, 761, 790, 315, 339, 234, 55, and a stray "2" on 122R.00 that the contributor's parser skips). 5 Oct 1764 (118-119R)
against `tx/p1764-10-05.final.txt` normalised here (1,626 letters): c03 0.733, c04 0.854; the contributor's 0.699 -> 0.825
used another normalisation of the 120 clear; the rise of about 0.12 on a letter not used to build c04 reproduces.
Of the 15 N_draft values, 14 agree with key c04 (62 is "affair", not "vu"); several of the 14 rest on one occurrence in the
alignment (6, 40, 202, 376, 505), so "confirmed" means "agrees with the completed key".

Images (Riksarkivet IIIF, `lbiiif.riksarkivet.se/arkis!A0073297_00121`, `_00127`, `_00128`, full/max, curl, no bot check):
121 lines 1-4 and 13-14 (117 groups) agree with `tx/c-chiffer2-121-124.txt`, including the date groups 481 150 761 and 790;
127 is the clear as transcribed (head note "Tillhör brev av den 31/12 1764 und: 28 Jan 765", lines 1-10 and 19, 25 checked;
the interlinear "laisse" over a struck word on 127.19 and "equelala" on 127.25 are as transcribed).

Strict count of 121-124L, read through its period clear: 612 of 613 word tokens of the clear (elisions split) are sure;
the one hole is "equelala" (127.25 "et tres equelala verité"; the cipher has e-qu-el-a-la), whose sense is not settled
(the English translation marks it [?]). Read share 0.998. Method for this letter: read from existing decipherment (the
contemporary clear); the key c04 is the project's addition and stays partial (1,236 of 1,247 groups; about 100 values
added or corrected after the measure, many on one occurrence). Date groups 481 150 761 ("28 Novembre"), 790 + 315 ("31"),
and 236, 339, 55, 234 have no value.

"System B now has no text without a clear in this volume" holds for the Chiffer n:o 2 folder (118-127): its two system B
letters, 5 Oct 1764 and 31 Dec 1764, both have their clear (120, 127-128). The Chiffer n:o 1 letters 87-117 are not all
transcribed or profiled, so it is not checked that none of them is in system B.

The target stays **Status: in progress**: system A (6 Mar 1764 and 15 Nov 1765) is open with workable gaps, and the key of
issue #437 is still not in the repository. No page yet.

## 14 Nov 2026 — system A key key_c01 and the scripts of issue #437 (PR #566, Brice Dudout)

Files in `dudout/system_a/` (text only; README there). Transcriptions by one reader, an AI agent, not checked by a
palaeographer. `key_c01.json`: 217 groups (197 with a value; 20 empty, as nulls: 17 groups below 100 and 100, 400, 508; 16 = mo is the one
group below 100 with a value), a one-part syllabic
nomenclator with homophones (e.g. 107 a, 218/213 de, 540 que, 536 Panin, 569 roi, 158 Breteuil, 679 vous, 285 faire),
rebuilt by anchored EM alignment (`scripts/align_em.py`, 28 hand anchors in `anchors_c01.json`) from letter 96 + 97L
(`transcr/i096.txt`, `i097g.txt`, the letter beginning 15.73.100.347.503.401.107.536, early 1764) and its contemporary clear
97R + 98L + 99L (`clears/L096_clear_contemporary.txt`; archivist's note on 97R). `PROTOCOLE.md` is dated 27 Oct 2026 02:20,
before any decoding, by the contributor's record (no outside timestamp); it plans tests of the key tables 218-220 with a
"the key reads" bar, not the EM key, and no threshold was declared for the held-out check below.

- Held-out check on 101R (6 Mar 1764, `transcr/i101d.txt`) against its clear on 102R (`clears/L101_clear_contemporary.txt`,
  first page only): 178 of 232 known groups agree (0.767); three permuted keys 0.224-0.254 (`validation/`). No group of the key
  comes from 101R.
- `scripts/check2.py` on this repository's own transcriptions: 15 Nov 1765 against its gloss, 704 groups, coverage 0.776,
  0.545 against 200 permuted keys (max 0.061); 6 Mar 1764 against 102R-103R, 605 groups, 0.807, 0.261 (max 0.043; the clear
  is about 2.6 times longer than the cipher on 101R-102L, which covers it to 103L.08).
- The 15 Nov 1765 gloss is complete and runs ahead of the cipher; the "unglossed" lines carry text glossed above earlier lines.
- Nothing is claimed as a new reading: both letters were deciphered at the time. Method for them: read from existing
  decipherment; key partial.

### Integration check (14 Nov 2026)

Reproduced (scripts read first, run with `python3 -I` in the worktree): all 26 SHA-256 values in `SHA256SUMS` match;
`check2.py` gives exactly 704 / 0.776 / 0.545 / max 0.061 / mean 0.037 and 605 / 0.807 / 0.261 / max 0.043 / mean 0.025;
`check.py` gives the issue's 703 groups and 0.544 (its parser skips one group that `check2.py` keeps). Every one of the 217
key groups occurs in the 96/97L transcriptions; none was taken from 101R.

Not reproducible from a script: the 0.767 of the held-out check. The script that made `validation/val_L101.json` (an alignment
of 101R to its clear) is not in the PR. Recounted from that file: 175 of 228 groups with a key value agree (0.768); the three
control files give 0.214, 0.224, 0.225. Each control file holds its own alignment path, so the alignment was refitted with each
key: the measure is how well a key-guided alignment fits the clear, matched by its controls, not a decode compared word for word.

Own decoder (written from `key_c01.json`, not importing the contributor's code): 101R decoded with the key against the 102R
clear, share of clear letters in matching blocks of 4 letters or more, 0.325 against 200 permuted keys (max 0.062, mean 0.034).
The raw decode reads as the clear: "...deavoirrecu ... nsieurpanin maaprevenu ... ilmaavoitappel ... etcon..catparmesdi ...
luiavoitmar[que] ... nouv de ... luisisoit delapeine ..." against "Deux jours avant d'avoir reçu ... Monsieur Panin m'a prevenu
... Il m'avoit appellé exprès et commença par me dire qu'on lui avoit mandé une nouvelle de Stockholm qui lui faisoit de la
peine". On 96 itself (training) the same score is 0.363. Lines of 15 Nov 1765 without a gloss, decoded by me: 125L.12
"...tacheraaucon[tra]i[r]edeycon..." = gloss of 125L.06-07 "tachera au contraire d'y contribuer"; 125L.15
"edecette‹614›tativenepourraquenet" = gloss of 125L.10-11 "de cette tentative ne pourra qu'en être"; 125R.11
"...rter...dre..sama..andrele..decemois" = gloss of 125R.10 "porter l'ordre de St André le 30 de ce mois"; 126.13
"...enresulimpter..." = gloss of 126.12 "qui en Resulteront". The offset is about one line at 124R.07 and about six by 125L.12.

Images (Riksarkivet IIIF, `lbiiif.riksarkivet.se/arkis!A0073297_00101` and `_00096`, full/max, curl, no bot check): 101R
lines 1, 9 and 14 (60 groups) and 96 lines 1-3 (54 groups): 112 of 114 agree; doubtful on the image: 101R L09 last group
(transcribed 187, could be 184) and 96 L02 group 16 (transcribed 409, could be 609). The 102R clear was not compared with
its image.

Corrections made here: "the clear pages do not decipher the ciphers", "the gloss is a positioned decipherment" and "the values
change through the text" are withdrawn for system A; profile: documents 6 Mar 1764 and 15 Nov 1765 now carry their period
decipherments (read in part until the strict counts and translations are made), system types nomenclator / syllabic /
homophonic, key_c01 added to `key_file`, credit and two solution steps. The contributor's README calls `PROTOCOLE.md` "the plan
written before any decoding": it is that by the contributor's record, and it does not cover the key_c01 method or the 101R check.

The target stays **Status: in progress**: what remains for system A (strict counts and translations of the two period
decipherments, the cipher of the rest of the 6 Mar clear) and the other Chiffer n:o 1 letters with filed clears are workable,
not outside-blocked. No page yet.

## 14 Nov 2026 (second contribution) — key_c01 passes a pre-registered test on the 15 June 1764 letter (Brice Dudout, Claude Opus 5.5)

Files in `dudout/system_a/june1764/` and `dudout/system_a/INVENTORY_chiffer1.md`; script `dudout/system_a/scripts/val_L101.py`.

- Inventory of Chiffer n:o 1 (images 85-117) from the full-size images: table in `INVENTORY_chiffer1.md`. Letters with a filed clear:
  96 (97R-99L), 6 Mar 1764 (102R-103R), 15/4 May 1764 (106R-107L), 15 June 1764 (109R-110L), 20/31 Aug 1764 (116-117).
  Without an identified clear: 87-89 (value profile unlike system A) and 90R-93L (system A profile); 94-95 is a clear letter of
  30 Jan [1764] that may belong to one of them.
- **15 June 1764** (108R "St Petersbourg ce 15. Juin 1764", clear opening, then cipher on 108R-109L, end on 110R). Never seen by the key.
  `PREREG.md` hashed before transcription (key by SHA-256, one measure = the check2.py metric with seed 1764, 200 permuted keys,
  bar M >= 0.15 and >= controls max + 0.10, justified there); amendment with the transcription hashes before the decode.
  Cipher transcribed twice (second pass by a blind sub-agent; 478 groups alike, 74 differ, first reading kept with "?"), clear
  twice. **M 0.383 against controls max 0.057 (mean 0.035): pass.** The raw decode reads as the clear ("primo parceque je ne veux
  pas reveiller mal apropos ... l'Imperatrice ... la situation du Roy ... Elle concerte avec le Roi de Prusse ... tout se sait ...
  un mot ... sans dessein devant ... produit un effet que toutes negociations ne pourront ...").
- The clear runs past the cipher of 108R-109L; the rest ("de la tromper ... conscience. Je pourrai bientot quitter Pettersbourg
  ... un homme ruiné") is enciphered on 110R (three lines at the top, four inside a clear paragraph), placed by a decode made after
  the measure. The decipherer's meaningless string "ritedriibsdoucle" (110L.03) sits where the cipher decodes "ri te ... s doute".
- Reading through the contemporary clear: 342 word tokens, 337 sure, 4 probable, 1 unresolved: read by sense 99.7 % -> read
  (method: existing decipherment). English translation in `reading_1764-06-15_en.md`.
- `scripts/val_L101.py` is the missing producer of `validation/val_L101.json`: align_em.py with key_c01 as hard anchors, 1 iteration,
  ratio 2.7; it reproduces the stored path exactly (320/320) and gives 175/228 = 0.768. The stored control files are not reproduced
  by the same settings (0.231, 0.247, 0.247 vs 0.214-0.225).
- Not done: strict counts and translations of the 6 Mar 1764 and 15 Nov 1765 period decipherments; the other Chiffer n:o 1 letters.

## Integration check (14 Nov 2026, PR #582)

Checked by the project on the merged files; the contributor's section above is unchanged.

| claim | contributor | ours | how |
|---|---|---|---|
| hashes | PREREG c941c974... (text above the amendment), amendment set of 5, key 3fcecea8... | all match; the 26 lines of `SHA256SUMS` (PR #566) still match | sha256sum; `head` rule of `june1764/README.md` |
| the one measure, 15 June 1764 | 511 groups, coverage 0.761, 1,465 clear letters, M 0.3829, controls max 0.0573, mean 0.0347: pass | identical | `measure_june.py` run with `python3 -I` in a scratch copy |
| key has no group from 108-110 | yes | key_c01.json is byte-identical to the file of PR #566 (same SHA-256), whose groups all come from 96/97L; 133 of the 220 group types of the June cipher have a key value | hash; own count |
| own measure | - | own decoder, share of decoded 5-letter windows found anywhere in the clear: 0.380 against 200 permuted keys max 0.061 (mean 0.028) | own script |
| the decode reads | "primo parceque je ne veux pas reveiller mal apropos ..." | yes: "primoparcequekieneveupasreveillermal ... limperat[rice] ... lasituationduroy ... elleconce[r]te[av]ecleroide ... toutses[ait] ... unmot ... produitunef[f]etquetoutes ..." | `outputs/measure_result.txt` and own decode |
| images | - | 108R.01-04 compared with the Riksarkivet image (63 groups): 60 agree, the 3 others are the ones the transcription already marks "?" (108R.03); clear 109R.01-05 agrees | IIIF A0073297_00108, _00109 |
| word count of the clear | 342 word tokens: 337 sure, 4 probable, 1 unresolved; "read by sense 341/342 = 99.7 %" | 342 tokens recounted; **strict share 337/342 = 98.5 %** (sure words only; the 4 probable words and the unresolved string are holes) | own count |
| `val_L101.py` | reproduces the stored path 320/320; 175/228 = 0.768; controls 0.231, 0.247, 0.247, the stored control files not reproduced | identical: 175/228, path 320 of 320, controls 53/229, 55/223, 56/227; the stored control files count 0.214, 0.224, 0.225 | script run in a scratch copy |

- **Is it a pre-registered test?** By what the files show, yes: a written plan names the key by hash, the one measure, the
  number of controls and the seed, and a bar with its reasons; the plan's hash is filed apart from the amendment that
  freezes the transcriptions and the script. The order of events (plan 04:15, amendment 04:33, one commit 04:48 CET on
  14 Nov 2026) is by the contributor's record; nothing outside stamps it. Two limits to state with the result: the
  measuring script was hashed in the amendment, after the transcription and before the decode, not with the plan; and
  the bar (M at least 0.15 and at least 0.10 above the best control) was chosen with four earlier scores of the same
  key on the same measure in hand, so it is a low bar. The result does not lean on the bar: 0.383 is more than six times
  the best control and above the 0.363 of the training letter.
- **What it changes.** key_c01 now has two letters it never saw decoding as their filed clears: 101R (held out, no bar
  declared, PR #566) and 15 June 1764 (bar declared beforehand, passed). The 101R figure of record is 175/228 = 0.768;
  its controls with the reconstructed settings are 0.231-0.247, and the three stored control files are kept as filed,
  unreproduced.
- **The 15 June 1764 letter.** Text: the decipherment of the time on 109R + 110L (method: read from existing
  decipherment). Strict share 98.5 % (337 of 342); 99.7 % is the contributor's figure with the four probable words
  counted. Not settled: the cipher lines on 110R that carry the end of the letter were read once, after the measure,
  and are not in the frozen transcription; 74 of the 552 groups of 108R-109L differ between the two passes and stand
  as first readings.
- **Inventory.** `dudout/system_a/INVENTORY_chiffer1.md` is the contributor's survey; not re-checked image by image
  here. It supersedes the line "transcribe the other cipher letters (87-95, 100, 104-117)" under Remaining gaps.

The target stays **Status: in progress**: the strict counts and translations of the 6 Mar 1764 and 15 Nov 1765
decipherments, the letters of Chiffer n:o 1 with a filed clear (15 May, 20/31 Aug 1764, 100R) and the two without one
(87-89, 90R-93L) are all workable from the online images. No page yet.
