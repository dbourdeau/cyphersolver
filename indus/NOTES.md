# Indus script: Parpola's 2005 lecture tested against two corpora

Status: in progress

Target given: <https://old.harappa.com/script/indusscript.pdf>. It is not an inscription but Asko Parpola,
"Study of the Indus Script", special lecture at the 50th ICES, Tokyo, 19 May 2005 (Transactions of the
International Conference of Eastern Studies 50, pp. 28-66; 39 pages). The site sits behind Cloudflare; a plain
`curl` gets a block page, one with a browser user agent gets the PDF. The PDF is not committed (copyright);
fetch it from the URL.

The lecture has two parts: a reply to Farmer, Sproat and Witzel 2004 ("the Indus signs are not writing"), and
Parpola's Proto-Dravidian rebus readings with their controls ('fish' = *mīn* 'star'; '6'+'fish' = Pleiades;
'7'+'fish' = Ursa Major; 'roof'+'fish' = *mai-m-mīn* Saturn; 'fig'+'fish' = *vaṭa-mīn* north star; 'crab' =
*kōḷ* planet; 'crab'+'fish' = *kōṇ-mīṉ*; 'fig'+'crab' = *kōḷi*, the archer god; 'eye'+'eye' = *kaṇ-kāṇi*
overseer; 'water'+'eye' = *nīr-k-kaṇṭi* irrigation officer). Both parts rest on counts in the corpus: sign
frequencies, one sign that never doubles, sequences that recur, pairs that behave as units. Those counts can be
checked, and that is what this folder does. No phonetic reading can be verified from the corpus alone (Parpola
p. 42: statistics cannot prove or disprove writing; Sproat agreed, n. 20). The Indus script remains undeciphered.
The first two passes test the evidence Parpola's readings stand on; the third ("toward a reading") sets out the
structural layer a reading must fit, the step that came before sound values in Linear B and proto-cuneiform:
two numeral systems, an ending paradigm, a name + epithet formula, and signs whose meaning pictures fix.

## Corpora

1. **ICIT-derived** (`data/corpus.tsv`, built by `build_corpus.py` from `population-script.sql` in
   <https://github.com/yajnadevam/indus-website>, GPL-3.0): 2,543 objects, 2,375 with CISI numbers, 52 sites,
   direction per object, one row per object with line breaks. Glyph ids are that database's sign numbers
   (Wells/ICIT family). The data are transcriptions; the database owner's own "Sanskrit decipherment" is not used.
   11,253 tokens, 572 types after splitting fused repeats (measured on `data/signs_reading.txt`).
2. **Mahadevan M77** (`m77_checks.py`), the independent transcription with Mahadevan's 417-sign list: 2,906 texts,
   3,573 lines, 14,153 tokens, from `data/m77_indusscript_real_corpus.csv` in
   <https://github.com/joyboseroy/indus_decipher> (MIT; itself a logged-in export of indusscript.in, so not
   copied here). No site or object type; the 9xxx texts are the West Asian finds.

The two sign lists were tied together by aligning the texts the corpora share (`align_m77.py`): seeded with
four tablet sets repeated 10-41 times in both, hard EM matched 991 lines (978 before the direction fix) with 96% of aligned signs on a single M77
counterpart (`data/icit_m77_map.tsv`). It recovers the known values (jar 740 = M77 342, fish 220 = M77 59) and
gives the fish series = M77 59-75, crab = 53/58, fig = 348/367/370/371, eye 809 and 832 = 375, water = 294,
pot = 328, numerals 97-121. The sign claims were then rerun on M77 (`results/m77_checks.md`).

The CISI digitisation at <https://github.com/mayig/indus-valley-script-corpus> (Parpola's own sign numbers) covers
only M-1 to M-199 (179 texts), too few to use.

## Sign identification

The ICIT glyph ids carry no names, so the signs were identified by rendering the site's own font
(`render_glyphs.py`, `signs_key.png`) and matching Parpola's descriptions and Fig. 3/4 drawings. The groups are in
`signs.py`:

| Parpola | ICIT glyph | shape |
|---|---|---|
| most frequent sign ('jar') | 740 | U-jar with two ear strokes |
| plain 'fish' | 220 | |
| fish series | 219-244 | fish with diacritics: roof 235/236, stroke 231/232, chevron 233, horns 240, between strokes 226 |
| 'crab' | 798 (no feet), 794 (feet) | |
| 'fig' (three branches) | 772, 773, 776, 783-786 | Fig. 3 a-i |
| 'fig'+'crab' ligature | 777, 778, 782 | Fig. 3 no. 124 |
| 'eye' dot-in-circle | 809; 832 (stroke in oval) | 'eye'+'eye' is fused as glyph 792 = 809+809 |
| 'water' two curved lines | 904 | Parpola sign 175 |
| 'pot' U/V | 700 | Fig. 1 |
| numerals | 1-7 short strokes, 13-19 two tiers (16 = 6, 17 = 7), 31-36 long strokes, 55 = 12 | |

The database fuses some repeated pairs into one glyph (219 = fish+fish, 792 = eye+eye, 698 = pot+pot, 617 =
grid+grid, 821, 791, 401 ...). `signs.SPLIT` splits them back, so repetition is counted as sequence; stroke
numerals such as 34 stay whole. Sign 740 is never fused with itself.

Direction: 2,440 objects are written right to left, 103 left to right, but the dump stores every text in one
normalised order (the jar, which ends texts, is at the start of the stored order for 839 of 840 R/L and 29 of
30 L/R objects), so `signs_reading` is the reverse of the stored order for all objects. (Corrected in the third
pass: the first two passes left the 103 L/R objects backwards; the counts below are rerun.) In M77 the jar
ends 974 lines and begins 4.

## Results, claim by claim

Full output: `results/parpola_checks.md` (ICIT) and `results/m77_checks.md` (M77). Nulls are within-line shuffles
(each line keeps its signs, order randomised), which keep inscription length and composition.

| # | Parpola's claim (page) | Result | Verdict |
|---|---|---|---|
| C1 | average text about five signs (p. 36) | M77 4.87 per text; ICIT 4.43 per object | confirmed |
| C1 | longest text 26 signs (p. 45) | M77 texts 1623 and 2847, 26 each; ICIT's longest is 17 (M-314), since the dump does not join sides | confirmed (M77) |
| C2 | 25-50% of signs occur once (p. 36, Farmer) | M77 27% of 418; ICIT 34% of 590 | confirmed, low end |
| C4 | most frequent sign almost 10% (p. 47) | M77 342: 9.9%; ICIT 740: 11.3% | confirmed |
| C5 | it never stands beside itself in the Indus Valley; once, on a round seal probably from Mesopotamia (p. 47) | Once in each corpus, on the same seal: ICIT sealid 3889, round, unprovenanced, reads 467 550 1 740 740, which the sign map turns into 178 216 97 342 342; M77 9901 reads 178 53 97 342 342 (four of five signs agree; the second is read differently). South Asia 0. The 13 South Asian lines that hold the jar twice would put the two side by side 4.0 times on average if their order were shuffled; only 0.7% of 5,000 shuffles give 0. Under independent signs, 110 would be expected | confirmed (p about 0.007); "very often" overstates the null (4, not 110) |
| C6 | West Asian square seals carry typical sequences, round and cylinder ones common signs in unusual order (p. 47) | Bigram model trained on South Asia: 9 round/cylinder seals at a median 95th percentile of surprisal and 95th for order-surprise; Kish square seal typical (54th); Salut (Oman) square seal atypical (98th) | confirmed for round/cylinder; one square counterexample |
| C7 | fish signs almost every tenth sign on seals (p. 52) | 695 of 7,165 seal tokens = 9.7% | confirmed |
| C8 | '6'+'fish' and '7'+'fish'; '7'+'fish' is a whole large Harappa seal (p. 54) | ICIT: 6+fish 10 (PMI 3.2, 0/300 shuffles); 7+fish once, H-9 (Harappa), the whole text. M77: 6+fish 16 (4.4 expected); 7+fish once, text 4009 (Harappa), the whole text, 112 59 = ICIT 17 220 under the sign map: the same seal | confirmed in both; 7+fish rests on one seal |
| C8 | (not in the lecture) | numerals before plain fish, ICIT: 2 x62, 3 x19, 6 x9, 12 x8, 4 x6, 1 x5, 7 x1; M77: 2 x83, 3 x20, 6 x16, 12 x9, 1 x6, 4 x4, 7 x1. The lecture reads 10 of 110 (17 of 139). Correction (second pass): the "2" here lumps the long pair (51/67), which Parpola 1994 reads as 'intermediate space' (*vel-min*), with the short pair (11/16); 3+fish is read in 1994 | not read in the lecture; read in the 1994 book, see R1-R3 |
| C9 | 'roof'+'fish' sign (p. 54) | 235: 186 tokens, 236 (between strokes) 21 | exists, frequent |
| C10 | 'fig'+'fish' on M-172 and M-414 (p. 55) | M-172 = 850 786 220 1 18 405: yes. M-414 not in the ICIT dump; M77 has fig+fish exactly twice. Fig is followed by the jar 19 times (M77 23), by the fish once (M77 twice); not above chance | confirmed; the reading rests on two seals |
| C11 | 'crab' more than 125 times; usually beside fish signs (p. 57) | ICIT 110 tokens (798+794), 48 (44%) beside a fish sign, 28.7 expected, 0/500 shuffles as high. M77 137 tokens (53+58), 53 beside a fish sign, 33.0 expected, 0/300 | confirmed in both (M77 count above 125) |
| C12 | 'crab'+'fish' three times; M-57 and M-387 parallel (p. 58) | crab + plain fish: ICIT 0, M77 2 (5.6 expected, i.e. below chance). Crab + fish series: ICIT 28, M77 31 (16.6 expected), mostly the horned and chevron fish 240/233. M-57 = 693 2 798 231 32 226, M-387 = 920 60 742 798 32 226: the parallel holds with the fish variant 231 | 'three times' matches only if his 'fish' includes a variant; crab goes with the marked fish, not the plain one |
| C12 | (new) crab+fish fills a one-sign slot | copper tablets: "845 61 407" follows 798 240 (6 tablets) and the single sign 806 (10); "845 407" follows 235 705 33 and 415 220 | supports crab+fish as one unit |
| C13 | 'fig'+'crab' on copper tablets, 7 examples, same obverse as the archer set, 14 examples (Fig. 4) | 777 alone on 6 tablets (M-603, M-604, M-1555-1558); the Fig. 4 inscription 806 845 61 407 850 900 740 on 10. The dump has one text per object, so the side pairing cannot be checked here | consistent; pairing not checkable here |
| C13 | H-598 and L-11 have similar contexts (p. 57) | L-11 = 817 2 778 255 435 705 590; H-598 not in the dump | half checked |
| C14 | 'eye'+'eye' a frequent phrase (p. 60) | ICIT 9 (all fused 792), 0.1 expected; M77 9 (4.9 expected) | a real unit, but 9 is not "frequent" |
| C15 | 'water'+'eye' is the whole of H-602 and ends H-396, H-568, M-205 (p. 61) | ICIT: M-205 ends 904 832; also M-370 (not cited); H-602, H-396, H-568 missing. M77: water+eye 6 times (1.1 expected), ending lines 1221, 2138, 4027, 4169 (two Mohenjo-daro, two Harappa); no line is water+eye alone. 'Water' is followed by the jar 17 of 33 times | the ending confirmed; H-602 as a whole text not found in either corpus |
| C16 | repetitions in M-682, K-10, M-634, 1093, M-1169, M-357 (pp. 37-38) | M-634: 820 x3 not in a row, 10 signs, yes. M-357: bar seal, 8 signs, 806 twice, yes. M-1169: 11 signs, 32 twice, yes. K-10: 10 signs; the repeated pair is 368+2 / 368+32 (short and long two-stroke), so it holds only if those are one sign. M-682 and 1093 not in the dump | 3 of 4 checkable confirmed, K-10 depends on the sign list |
| C16 | Farmer: too little repetition for phonetic writing (p. 36) | Lines with a repeated sign, numerals excluded, against random draws of the same length: length 4: 5.2% vs 13.8%; 5: 9.9% vs 20.6%; 8: 12% vs 47% | Farmer's observation holds: repetition is about half of chance. It fits word-level (logo-syllabic) seal legends as well as non-writing, as Parpola argues |

## What this adds

- Parpola's structural claims check out on two independent transcriptions: the jar at about 10%, never
  doubled at home and doubled once on the round seal 9901/3889; fish at about a tenth of seal signs; crab
  clustering with fish; West Asian round seals using common signs in unusual order; lengths and singletons.
- The compounds behind the readings are not equally supported. 'Eye'+'eye', 'water'+'eye', '6'+'fish',
  numeral+'pot' and crab+fish-series are units well above chance. '7'+'fish' (1 seal) and 'fig'+'fish'
  (1 in this corpus, 2 in Parpola) are single attestations, so the Ursa Major and north-star readings rest on
  one or two seals each. The largest groups before the plain fish, the long stroke pair (51/67) and 3 (19/20),
  are not read in the lecture; the 1994 book reads both (the pair as 'intermediate space', *vel-min* 'Venus';
  3 as *mu-m-min*), see the second pass.
- 'Crab'+'fish' almost never uses the plain fish (ICIT 0, M77 2, both below chance); it is crab + a marked fish
  (240, 233, 231, 235), well above chance in both corpora. The *kōṇ-mīṉ* reading needs those marked fish to be
  read as 'star' too.
- The two corpora agree: every sign count above was reproduced on M77 through the alignment, and both put the
  single jar+jar, the single 7+fish and the two fig+fish on the same objects.
- Parpola's null for jar doubling (independent signs, about 110 expected) is too generous. The within-line
  shuffle expects 4.0 and sees 0 in South Asia (p about 0.007), still well below chance, so his argument stands
  on the fairer null.
- A reusable harness: `build_corpus.py`, `signs.py`, `parpola_checks.py`, `m77_checks.py`.

## Second pass (23 Sept 2026): Parpola 1994, the Dravidian lexicon, CISI vol. 1, motifs

New sources:
- **Parpola 1994**, *Deciphering the Indus Script* (CUP), public scan and OCR on archive.org
  (`decipheringtheindusscriptaskoparpolabookmarked_300_F`, Digital Library of India). Used: Fig. 15.2 (pp.
  275-7), the table of all 24 interpretations with pictorial meaning, Dravidian word and attestation; the
  Appendix (pp. 279-83), the 99 Tamil Lexicon compounds ending in *min* (34 star names, 65 fish names), typed
  as `rebus/min_compounds.tsv` (89 rows as transcribed, first member simplified); p. 194 on numerals + fish.
  Not committed.
- **Dravidian Database** v1.1 (Merriam & Fuls 2026, Zenodo 10.5281/zenodo.22215802, CC BY 4.0): 72,091 DEDR
  lemmata with glosses, 13,768 of them Tamil. Read from the scratchpad, not copied.
- **CISI vol. 1** (Joshi & Parpola 1987, *Collections in India*), an 862-page scan supplied by the user
  (library no. 76884). The scan is about 100 dpi, image only; OCR works on the page headers (plate index) but
  not on the data table. Not committed.
- **Motifs**: the ICONOGRAPHY table of the indus-website dump (1,622 objects) is now the `motif` column of
  `data/corpus.tsv`.

### 1. Chance baseline for the rebus check (`rebus_checks.py`, R4)

Parpola's control on a reading is that the compound it yields is attested in Tamil ('fig' *vata* + 'fish'
*min* = *vata-min*, a star). How often would an arbitrary picture pass that control? For 98 picture concepts
fixed before the run (things Indus signs are commonly said to show), take every Tamil word whose DEDR gloss
names the concept and ask whether one of them is the first member of a Tamil star name in *-min* from
Parpola's own list:

| gloss used | strict match | with the latitude the readings use (ai/ay/ey, final -am/-u/-i) | any *-min* compound, strict |
|---|---|---|---|
| first sense only | 15% | 30% | 44% |
| any sense | 27% | 48% | 68% |

A concept has a median of 16 Tamil candidates. So an arbitrary sign placed before 'fish' has between a
one-in-seven and a one-in-two chance of giving an "attested Tamil star name". The control is real but weak:
one matching compound is not evidence; a reading needs many interlocking matches or a prediction about the
corpus that comes true.

Numerals: counting homophones (*nal* 'four' = *nal* 'day', *nal-min* 'asterism'), Tamil gives star names for
3, 4, 5, 6 and 7, not for 1, 2, 8 or 12.

### 2. Parpola 1994's own readings against the corpora (`rebus_checks.py`, R1-R3)

- **The numeral restriction does not hold.** Parpola 1994: 194: numbers before the fish "are restricted to 3,
  4, 6 and 7. The hypothesis of a Dravidian pun offers an alternative which explains this restriction".
  Counting stroke numerals before the plain fish (leaving out the long pair, his 'intermediate space', and the
  short pair, a non-numeral for him): 1 (ICIT 5 / M77 6), 3 (19/20), 4 (6/4), 6 (10/16), 7 (1/1), 12 (8/9); 5
  never. The pun predicts 5 (*ai-m-min*, a Tamil asterism), which never occurs, and cannot give 1 or 12, which
  do. 73% of the tokens (36/49, 41/56) have a number with a Tamil star name.
- **The frequency order is reversed.** He calls 6+fish the most frequent and 3+fish next; in both corpora
  3+fish (19, 20) outnumbers 6+fish (10, 16).
- **"Ligatured fish are never preceded by numbers" (1994: 196)** holds only if the short stroke pair is not a
  number (it stands before a ligatured fish 135 times). Single and triple strokes still stand before
  ligatured fish 36 times (ICIT) and 23 (M77). "Never doubled" holds: no ligatured fish is doubled; the plain
  fish is, 6 and 7 times.
- **The 24 readings of Fig. 15.2** (R3 table in `results/rebus_checks.md`). Real units in both corpora:
  3+fish, 6+fish, eye+eye, hearth+rings (15/27 against 0.1-0.2 expected), rings+'space' (29/34 against
  1.7-1.8), 'space'+fish (51/67 against 7-11). At or below chance: fish+fish, 7+fish (one seal), fig+fish
  (M-172, M-414), fig+'space' (1), crab + plain fish (0/2, below chance). 4+fig with the three-leaf fig occurs
  3 times in ICIT (H-289, H-290 and an unnumbered tablet, all incised tablets from Harappa, all three with the
  pipal-leaf motif on the reverse, as Parpola says of H-289), 0 in M77 (whose left-to-right texts are stored
  mirrored). The branched sign 405/407 after 4 is a separate, strong unit (18/24). The 'squirrel' of
  no. 13 was not found in ICIT.

The readings split in two. Those built on frequent, recurrent pairs (rings+space *Muruku-Vel*, hearth+rings,
space+fish *vel-min*, 3/6+fish) rest on real sequences. The two best-known star names after the Pleiades,
Ursa Major (7+fish) and the North Star (fig+fish), rest on one and two seals.

### 3. CISI vol. 1 photographs

- **M-414** (PDF p. 136, printed p. 100): bar seal, three signs; the impression reads (right to left) an
  unclear crossed sign, the U-shaped 'fig' with barred branches (Parpola 2005 Fig. 3 i), the plain fish.
  Parpola's second fig+fish seal is confirmed.
- **Copper tablets** (PDF pp. 162-189). The archer tablets M-585 to M-588 have the archer on side B and the
  inscription recorded in ICIT (806 845 61 407 850 900 740) on side A. M-604 has the fig+crab ligature on side
  B and a worn inscription on side A; M-603 A is also worn. At the scan's resolution the side-A texts of
  M-603/604 cannot be read, so whether they repeat the archer text (Parpola 2005 Fig. 4) stays open. The ICIT
  dump records only the ligature for these tablets and drops their side A.
- **Concordance check.** CISI's "Basic data" gives each object's FC number, which Parpola says mostly equals
  Mahadevan's. For 10 objects on table p. 367 that have an ICIT text, the ICIT text mapped through
  `icit_m77_map.tsv` equals the M77 text of that number in 8; M-108 differs in its last sign, M-107 throughout
  (perhaps a number misread from the scan). That checks both the sign map and the crosswalk.
- Not in this volume: H-396, H-568, H-598, H-602 (Harappa objects here stop at H-381; the rest are in vol. 2,
  Pakistan, print only; the archive.org "vol. 3 part 1" is 17 pages of front matter).

### 4. Signs and field motifs (`motif_checks.py`)

- **Seals**: 1,107 seals with a motif (unicorn 939, gaur 76, zebu 44, elephant 28, rhinoceros 20). Of 333
  sign-motif pairs (103 signs, 5 motifs), none occurs together more than chance: the best has p = 0.006
  (hypergeometric), what the smallest of 333 p-values gives by chance, and none passes a 2,000-permutation
  test at p <= 0.001. Seal texts do not name or qualify the animal.
- **Copper tablets**: the reverse. Of 7 texts on 3 or more tablets with a named motif, 6 go with a single
  motif: 235 705 33 845 407 321 407 = hare (12/12); 806 845 61 407 850 900 740 = archer (10/10); 706 33 923
  740 (+/- a final stroke) = elephant (11/11); 415 220 845 407 = 'loop' (3/3); 3 421 176 100 740 790 = goat
  (3/3). The exception, 798 240 845 61 407 (crab + fish ...), goes with tiger x2 and gaur x1. Parpola's
  "pictorial bilingual" holds on the tablets for three images, not only the archer. The shared pieces (845
  ... 407 in the hare and archer texts, 33 in the hare and elephant texts) are what any reading of these
  bilinguals has to account for.

### 5. The full corpus

Not freely online: the full ICIT (4,537 objects, 19,616 sign occurrences) needs an account from Andreas Fuls
(fuls@epigraphica.de), and CISI vol. 2 is print only. The request is the user's to send. The scripts rerun
unchanged on a fuller export in the indus-website schema; ICIT's own export would need a converter.

## Third pass (23 Sept 2026): toward a reading, the structural layer (`structure.py`)

Scripts without a bilingual have been read by first finding what the signs mean as a class, before any sound
value. Kober's inflected "triplets" came before Ventris's grid in Linear B; the numeral systems came first in
proto-cuneiform; Proskouriakoff read Maya dates and events before the syllabary. This pass sets out that layer
for the Indus texts from the corpus itself, with the image-bearing objects as anchors. Output:
`results/structure.md`. Grades: **A** = a fact of the corpus at p < 0.001; **B** = anchored in images or in
more than one test; **C** = interpretation, stated so it can be tested.

1. **Two numeral systems (A).** Short strokes and long strokes precede different classes of sign, even at the
   same value: for 1, 3, 4, 5 (both stroke pairs left out) short strokes stand before 390, 156, 900, the plain
   fish 220, 405/407; long strokes before 520, the pot 700, 923, 845 and the jar (Jensen-Shannon 0.59 bits,
   0 of 1,000 permutations). With the pairs included the split is sharper (0.52; the short pair goes before the
   marked fish 240/235/233/231, the long pair before the plain fish and the jar). Long 3 + pot is by itself the
   whole text of 22 Harappa tablets (M77: 111). *Proposal (C):* long strokes count goods and vessels (the pot's
   own picture confirms it on the Fig. 1 tablets M-478/479, where 4 + pot accompanies a person offering a pot);
   short strokes are numbers inside names, as in the star names 3/6/7 + fish. A language reading has to give
   the two series two forms: Dravidian does have them (adjectival *mu-*, *aru-*, *elu-* in compounds, counting
   *munru*, *aru*, *elu* on their own), but so do many languages, so this narrows the reading without choosing
   the language.
2. **Counted nouns (A).** Signs that follow a numeral far more often than chance: 597 and 417 (always, after 2),
   48, the pot 700 (78% of its occurrences), 384, 585, 226, 156, 803, 900, 840, 140, 923, the fish 220, 575,
   390. These are nouns for countable things (table S2).
3. **An ending slot with alternants (A, Kober).** The line-final class is 740 (71% of its tokens end a line),
   400 (89%), 520 (87%), 90, 156, 151, 700, 407, 527, 154. 58 stems occur with two or more different endings,
   e.g. 840 32 + {740, 740 400, nothing}; 235 240 + {740 90, 740 151, 520}; 240 100 + {740 400, 740 151, 740};
   13 840 + {740, 740 400}. The endings stack in a fixed order: 740 400 166 times against 400 740 11; 740 90
   85 against 0; 740 151 9 against 0. 520 and 740 never stand side by side, as two alternants of one slot
   would not. *Proposal (C):* 740 is a grammatical ending (Parpola's genitive), and 400, 90, 151 a second slot
   after it (titles or case endings); 520 is a different filler of the first slot.
4. **A formula after names (A/B).** The sequence 845 (61|63) 407 occurs in 10 distinct texts (37 objects, seals
   and copper tablets). In all 10 the phrase before it contains a sign of the fish series or the leaf-in-oval
   806; a random stretch of the same length does so with probability 0.27 (binomial p = 1.8e-6). On the copper
   tablets the phrase before the formula changes with the image: 235 705 33 = hare, 806 = archer, 415 220 =
   'loop', 798 240 = tiger (x2) / gaur (x1), while 845 (61) 407 stays. On three seals the jar comes just before
   it (... 740 845 407; ... 740 140 845 407). *Proposal (C):* NAME (+ 740) + 845 (61) 407 is a name followed
   by an epithet or title; the name carries a fish sign, Parpola's god/star sign, and on the tablets names the
   being in the picture. The elephant tablets have a different pattern: 706 33 923 740 (elephant) against
   705 33 923 740 1 (composite animal), where the first sign alone changes with the picture.
5. **Picture anchors (B).**
   - 'Fig' (ICIT 783/785): the three '4 + fig + jar' tablets from Harappa (H-289, H-290, one unnumbered) all
     show a pipal leaf on the reverse; the pipal motif occurs on 4 objects in all. The sign means 'fig'.
   - 'Pot' (700): 4 + pot on M-478/479 beside a scene of a pot offered to a tree (Parpola 2005, Fig. 1).
   - Fig + crab ligature (777) = the horned archer (Parpola's copper-tablet pairing), and the archer's own text
     begins with the leaf sign 806: the archer is tied to fig imagery twice.
   - Seals: no sign goes with the seal animal (second pass), so seal texts are not names of the animal.
6. **Words (C).** Cutting lines where the pair cohesion is low (PMI < 2 bits or fewer than 3 examples) gives a
   segmented corpus with 1,208 distinct units; the commonest units of two or more signs are 861 2 (92), 740 400
   (89), 817 2 (78), 740 90 (55), 820 2 (52), 176 740, 32 220, 760 740, 3 156, 590 390, 840 32 (table S5). The
   line-initial class (817, 820, 861 followed by the short pair 2; 920, 503, 692) is a second fixed slot at the
   start, the counterpart of the endings.

Put together, a typical seal text has the shape [opening sign + short pair] [counted or named units, with
short-stroke numbers inside names] [ending 740/520] [second ending 400/90/151], and a copper-tablet text
[name with a fish or leaf sign] [epithet 845 (61) 407]. A phonetic proposal now has constraints it did not
have from single signs: it must make 740/520 alternate as endings, 400/90/151 follow them, 845 (61) 407 an
epithet after names, and give numbers two forms. None of this is a reading; it is the grammar a reading must
fit, and the places (name slots on the copper tablets, 'fig', 'pot') where meaning is fixed by pictures.

## Limitations

- ICIT glyph identification is by shape from the font, checked on the cited seals and by the M77 alignment, but
  not sign-by-sign against Parpola 1994's list, which may split or merge signs differently (e.g. crab + 'fish').
- The ICIT dump lacks some cited objects (M-682, M-414, M-305, H-598, H-602, H-396, H-568) and does not
  separate the sides of an object. M-414 was checked in CISI vol. 1; the four Harappa ones need vol. 2.
- R4 depends on a hand-typed list (`rebus/min_compounds.tsv`, 89 of Parpola's 99 compounds, OCR-read) and on
  DEDR glosses; a concept "has" a Tamil word when the English gloss names it, which is generous, as the
  method is.
- Duplicates (sealings from one seal, sets of copper tablets) are counted as separate objects, as in Parpola's
  own counts.

## Next steps

1. (Done for Mahadevan: `align_m77.py`.) Extend the map to Parpola 1994's numbers through the mayig CISI files.
2. (Done for vol. 1.) H-396, H-568, H-598, H-602 need CISI vol. 2 (print); M-603/604 side A need a sharper image.
3. (Done: R3.) Next: the readings of Parpola 1997 and 2003 that are not in the 1994 table.
4. A second-language control for R4: the same baseline with a Sanskrit (or Sumerian) star-name list, to see
   whether Tamil fits the attested Indus pairs better than a language taken at random.
5. Substitution classes: which units fill the slot before "845 61 407" and similar recurring tails. That is the
   Koskenniemi-Parpola 1970 method, run on the full corpus.

## Prior work

The lecture is published and its readings go back to Parpola 1994. Computational work on these corpora
exists: Rao et al. 2009 (entropy), Yadav et al. 2010, Farmer et al. 2004, and the indus_decipher toolkit (2026).
None of these checks Parpola 2005's specific counts and cited seals, his 1994 numeral restriction, or the
chance rate of his Tamil-compound control as done here; the counts and tables in `results/` were all
computed in these two sessions.
