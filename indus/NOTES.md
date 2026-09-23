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

## Fourth pass (23 Sept 2026): tablets, sign classes, measures, language controls, sound values

### Quick fix: M77 direction

M77 is not mirrored: only one line begins with the jar (1093.2, "342 82 342", Parpola's text 1093 with a repeated
sign), so Mahadevan's lines are already in reading order. The '4 + fig' tablets (H-289, H-290) are simply not in
M77; no M77 line has a numeral before the fig sign.

### 1. The copper tablets as bilinguals (`rebus/copper_tablets.tsv`, `copper.py`, `results/copper.md`)

Parpola 1994 Fig. 7.14 (PDF pp. 129-130 of the archive.org scan) gives the 46 prototype groups of the Mohenjo-daro
copper tablets (217 tablets): each group's inscription, its reverse (an image, or a sign in place of the image),
the number of copies, and the group linked to it by an identical inscription. Every ICIT copper-tablet text was
rendered in its drawn layout (`render_texts.py`) and matched to a group: 28 texts from ICIT, 15 read from the
drawing into ICIT numbers (marked approximate), 3 not transcribed. ICIT had kept only the sign side of several
linked groups (749, 341, 753, 777, "165 900 790"), which now have their inscriptions.

- **Seven sign = image equations** (same inscription, image on one tablet, sign on the other): 777 (fig+crab) =
  markhor goat (B9/C5) *and* horned archer (B19/C6); 749 = markhor goat (A2/C4); 341 = rhinoceros (B5/A11);
  753 = hare (B7/C2); a lens-shaped sign with two triangles = long-horned bull (B1/C1); "3 700 900 165" = bull
  with heart-shaped spots (B10/A7). The elephant text (706 33 923 740) also stands above a horned tiger (B12).
- **Name and title split.** Titles, shared by texts with different images: 845 (61) 407 (hare, knot, archer,
  bull-tiger), 142 615 615 (long-horned bull, composite animal, rhinoceros, and the lens sign that equals that
  bull), 705 33 (hare, rhinoceros), 503 615 (short-horned bull, rhinoceros). Names, specific to one image across
  different texts: 806 233 = markhor goat (A1, A2); 235 233 (222 740) = rhinoceros (B15a, B15b, B16);
  255 435 690 = short-horned bull (B4, C3); 905 32 597 = composite animal (B17). A minimal pair: 503 615 740 =
  rhinoceros (B5), 503 615 752 740 = short-horned bull (B11).
- **One image, several names.** The markhor goat goes with four texts and two signs (749, 777); the rhinoceros with
  three texts and one sign (341). The images are not one-to-one with names: several beings (or several names of
  one) share an image, and one sign (777) names two images, which is why Parpola reads both as one deity.
- **The names do not transfer to the seals.** No tablet name occurs on seals with its tablet animal more than
  chance (best 235 233 with the rhinoceros, 1 of 9 seals, p = 0.14). With the second pass (no sign-motif link on
  1,107 seals) this says the seal texts are not labels of the seal animal.

### 2. Sign classes from slots (`slots.py`, `results/slots.md`)

106 signs (15+ occurrences) clustered by their left and right neighbours (PPMI, cosine, 24 classes, 50 bootstrap
runs). The method recovers what is known from shape: the fish series falls into one class (54% of pairs share a
class against 6% by chance; 220, 240, 235, 233, 231 together in 90%+ of runs); the short numerals cluster (4, 5, 16
stable); 405 and 407, which share one glyph in the database font, are inseparable. New: the leaf-in-oval signs 803
and 806 and the crab 798 fall in the fish class, the class that fills the name slot on the tablets; the signs
counted by long strokes (520, 923, 845, the pots 705/706) form another class; the ending 740 groups with 156, 154,
158, and 400 is a class of its own. The long-stroke numerals do not cluster (0 of 10 pairs): each behaves like part
of the word it counts.

### 3. Numbers and measures (`numerals.py`, `results/numerals.md`)

- The weight hypothesis fails. Harappan weights run 1, 2, 4, 8, 16, 32, 64 then decimal. Written values go 1-8, 12
  and one sign for 24 (10 times); no 16, 32 or 64. Powers of two are 63% of numeral tokens against 66% expected if
  small numbers are simply commoner; the tiered series avoids them (7%). The numbers are not weight units.
- Counting is in rows of at most four (6 = 3+3, 7 = 4+3, 8 = 4+4, 12 = 4+4+4), no decimal grouping.
- Counted versus fixed: signs whose number varies are counted things (the pot 700: 2, 3, 4, 6; 390; 900; 590;
  405/407; 140; the plain fish; the jar after tiered numbers 6, 7, 12). Pairs whose number never varies are fixed
  terms: the short pair before the name signs (240, 235, 803, 806, 798, 231, 61: 82-97% one value), 3 long + 520,
  923, 845 (94-100%), tiered 7 + 585 and 575 (100%), the long pair + fish 220 (91%). '3 + 156', the Harappa tablets'
  whole text, is 3 in 35 of 40.
- Combining and counting forms: before the plain fish (the star-name compounds) the numbers are short or tiered
  45 times and long 5; before the pot (counted goods) long 42 and short 6.

### 4. Second-language control (`lang_control.py`, `results/lang_control.md`)

Same baseline as R4, rerun on Sanskrit (Monier-Williams, Cologne csl-orig, 25 star names ending in a word for
star, 23 first members) and Sumerian (ePSD2, ORACC, CC0, 48 constellation names):

| | Tamil (Parpola's -min list) | Sanskrit (MW) | Sumerian (ePSD2) |
|---|---|---|---|
| picture concepts giving a star name (strict, first sense) | 15% (30% loose) | 19% | 10% (the picture is itself a constellation) |
| a word for 'fish' that is also a word for 'star' | min (the everyday word for both) | rsi (a fish; the Seven Sages = Great Bear), ilvala (a fish; the stars of Orion's head) | mul ('star'; also 'a fish') |
| fig = pole star | vata 'banyan' = vata 'north' (vata-min) | dhruva 'the Indian fig-tree' = dhruva 'the pole star' | none |
| numbers that begin a star name | 3, 4 (homophone), 5, 6, 7 | none | none |

On pictures, the Tamil check is no stronger than Sanskrit's or Sumerian's. The fish = star pun is not Dravidian
only: Parpola (1994: 214) knew of Lezgi and set it aside as not old; Sumerian mul is as old as the Indus script, and
Sanskrit has two. Sanskrit even repeats the fig = pole-star pun. What is specific to Tamil is the numeral + star
names; they cover 73% of the numeral + fish tokens but predict a 5 + fish that never occurs and miss the 1 and 12
that do. So the language question stays open; the numerals are the one place where Dravidian fits better than
the controls.

### 5. Sound values against the structure (`sound_tests.py`, `results/sound_tests.md`)

The published ending proposals (Parpola 1994: 94-96): the Finnish team's 1969 paradigm, nominative zero, genitive
= jar 740, dative = arrow 520 (abandoned by Parpola); the Soviet jar = oblique *-at(tu)*, dative *-kku*; Parpola
1994, jar = cow's head *a* 'cow' = possessive *-a*, and 'man' (90) = *al* 'servant'.

- What the corpus supports: 740 and 520 never touch (0 and 0), 15 signs take both directly, and they alternate
  mostly after fish-sign names; 740 is followed by 400 (166) or the 'man' 90 (85), the shape of a genitive with a
  head noun ("X's man"), which fits Parpola's jar = possessive and man = *al*; 520 is final 87% of the time and
  follows a fish-sign name 55% of the time.
- What it does not support: 520 comes straight after a bare '3' (long strokes) 45 times with a value that never
  varies, a lexical compound rather than a case ending.
- Rebus support in DEDR: *a* 'cow' (Malayalam, Proto-Dravidian) gives the possessive -a; no Dravidian word for
  jar, pot or pitcher (156 forms, 21 languages) has a genitive shape; no word for arrow (54 forms, 16 languages) has
  the dative shape -kku; the only suffix-shaped arrow word is Tamil *utu*, matching the sociative *-otu* 'with'
  (grade C, a candidate, not a reading).
- The numeral constraint fits Dravidian combining forms (*mu-*, *aru-*, *elu-* in compounds, *munru*, *aru*,
  *elu* alone) but equally Sanskrit (*tri-* / *trayah*) and others, so it does not choose the language.
- The name + epithet formula 845 (61) 407 and the tablet signs 749, 341, 753 have no reading in Parpola's 1994
  table; of the seven sign = image equations his system reads one (777, *koli*).

## Fifth pass (23 Sept 2026): seven leads

Scripts: `equation_rebus.py`, `leads.py` (L2, L5, L6, L7), `sanskrit_key_test.py`, `elamite.py`; results in
`results/equation_rebus.md`, `leads.md`, `sanskrit_key_test.md`, `elamite.md`.

1. **The tablet equations as rebuses (negative for every language).** Of the four signs the tablets tie to
   pictures, 341 (= rhinoceros) is itself a drawing of a horned quadruped: a logogram. The other three are
   compounds: 777 fig + crab (= goat, archer), 749 jar with limbs and three strokes (= goat), 753 jar with a wheel
   inside (= hare). For each language, the best sound match between words for the component pictures (alone or
   two joined, starting with the target's first sound) and words for the animal, ranked against 24 control
   animals with ties counted against the true one (1 = best of 25): Dravidian 19, 23, 12, 23; Sanskrit 13, 24,
   18, 17; Sumerian 8, 13, 6, 21. Chance is about 13. No language's puns pick out the tablet animals; the
   compound signs behave as logograms (word signs), not rebuses. The corpus hardly writes their parts as
   sequences (820 + 740 twice).
2. **Names against titles across sites (negative).** On seals from Mohenjo-daro and Harappa, two-sign units that
   contain a name sign are no more tied to one site than openings and endings (standardised skew 1.13 against
   1.00-1.09; permutation p = 0.44). If they are names, they are names shared between cities (deities, clans or
   offices), not local people.
3. **A published Sanskrit decipherment under the same controls (Yajnadevam; key from github.com/yajnadevam/lipi,
   xlits.csv, 716 signs on about 20 letter classes).** Under the key the ending slot reads 740 = -an, 520 = -n,
   and 400/90/151 = i/a/y; the openers 817/820/861 all read r; the marked fish 235/240/233 have no value. Null
   test: texts become consonant skeletons and are parsed into Monier-Williams headwords; the real key covers
   88.3% of consonants with words of 3+ consonants, 200 keys shuffling its values among signs of similar
   frequency give a median 87.0% (range 79.1-91.0%), and 63 of 200 do as well: the key reads no better than
   chance. His readings of the copper tablets never name the picture on the other side (0 of 11; the goat
   tablet M-548 reads 'one who kills with an arrow', the text Parpola links to the archer). Mahadevan's readings
   are not machine-readable online; Parpola's were tested in the second pass.
4. **Proto-Elamite as the structural parallel.** In the Proto-Elamite accounts (1,467 tablets; SFU remap of the
   CDLI corpus), entries measured in the grain-capacity system name different things from entries in the counting
   systems (Jensen-Shannon 0.362 bits, 0 of 500 permutations; 6,274 entries). The Indus split between short and
   long strokes is of the same kind and stronger (0.592). The Indus numerals are an accounting device of the
   Proto-Elamite family. Linear Elamite has no corpus online to compare.
5. **Time depth.** Kenoyer and Meadow (2010, CISI 3.1: xliv-lviii) date object types at Harappa: square seals with
   an animal from late Period 3A (c. 2450 BC) to 3C; bar seals with script only in Period 3C alone (c. 2200-1900
   BC); tablets mid-3B to 3C. Late bar seals against square seals: the grammar is unchanged (740 in 50% of both,
   opening 17-18%, second ending 3-5%); the vocabulary moves: the leaf-in-oval 806 goes from 2% to 16% of
   objects, 405/407 and 154 rise, 741, 390, 520 and 368 fall. The frame is stable and the names change.
6. **The short stroke pair is part of the opening.** 326 of its 583 tokens (56%) follow the openers 817/820/861;
   35% precede a fish, leaf or crab sign; in the same frame it alternates with 60 and a single stroke. The
   opening is [817/820/861] + [2 | 60 | 1] + name; 97 seals open exactly so.
7. **The West Asian seals lack the Indus grammar.** Of 11 seals from the Gulf, Mesopotamia, Iran and unprovenanced
   round/cylinder seals, 2 end in 740/520/400/90 (South Asia 55%; binomial p = 0.016), none begins with an opener
   (21%; p = 0.075), 9 carry a numeral (57%). This supports Parpola's view that they write non-Indus (local)
   names in Indus signs; matching them to Meluhhan names in cuneiform needs sound values nobody has.

## Sixth pass (23 Sept 2026): ending grid, opening formula, Proto-Elamite shape, a fourth family

Scripts: `sixth.py` (G1, G2, O1), `pe_formula.py`, `fish_star_world.py`; results in `results/sixth.md`,
`pe_formula.md`, `fish_star_world.md`. (profile.json not updated for this pass, at the user's request.)

1. **The ending grid (Kober).** 2,560 lines: no ending 1,208, 740 894, 520 202, 740 400 158, 740 90 79,
   520 400 11, 740 151 8. The choice of ending is strongly predicted by the last sign of the stem (mutual
   information 0.865 bits, 0 of 1,000 permutations): stems ending in a fish sign take 520 in 50% of lines,
   all other stems in 4%; stems ending in 176, 752, 923, 803, 61, 222, 630, 636 always take 740; stems ending
   in a single stroke usually take none. So 520 is the ending of the fish (god/star) names and 740 the
   ending of the rest: a class split like noun classes, or 520 a word that follows divine names.
2. **The second slot goes with the genre.** After 740, the 'man' 90 is a seal formula (48 of its 79 lines on square
   seals; Mohenjo-daro 43) and 400 a tablet formula (139 of 158 on incised and moulded tablets, 138 at
   Harappa); mutual information with object type 0.394 bits, with site 0.323, with the stem 0.639 (all p <
   0.001). 'X-740 man' on seals, 'X-740 400' on Harappa tablets.
3. **The opening formula.** 317 texts open [817 | 820 | 861] + [2 | 60 | 1]: 817 and 861 take only the stroke
   pair, 820 also takes 60 (22) and a single stroke (11). The opener does not depend on whether a name sign
   follows (p = 0.81); it varies with site and object type (p < 0.001) and a little with what follows
   (p = 0.006); not significantly with the field animal (p = 0.06). Three regional or genre variants of
   one heading, not three different titles.
4. **Proto-Elamite text shape.** Proto-Elamite entries (signs before a number) end in a two-sign tail shared by
   3+ different heads in 38% of 1,598 entries (commonest M218 M288, after 20 different heads), the Indus lines in 64% (740 400, 760 740, 740 90 ...). 66% of Proto-Elamite texts open with a
   heading line without a number. Same architecture (heading, entries with a fixed final element), the
   Indus more formulaic.
5. **A fourth family and the world base rate of the fish = star pun (CLICS4, 2,895 languages with both
   words).** Identical words for 'fish' and 'star' in 3 languages (0.1%: Lezgian, two Chatino varieties),
   near-identical in 6 more; the control ('three' against 'star') 1 of 2,681. Burushaski (fish tum / cumo,
   star asii / sii), Indo-Aryan (Hindi, Bengali, Marathi, Nepali ...) and modern Dravidian basic lists (which
   give 'star' as the loan natcattiram) have no pun; Munda is absent from CLICS; Santali star is ipil (Bodding), and
   the Santali fish word (hako, from memory) is not yet checked against a dictionary. So in basic vocabulary the fish = star pun is rare worldwide and, among
   the four South Asian families, belongs to Dravidian alone (Old Tamil *min*); the Sumerian and Sanskrit
   cases of the fourth pass are specialised fish names, not the ordinary words. This restores part of the
   Dravidian case: the first step of the fish readings is distinctive, even though the compound check built
   on it is not.

## Seventh pass (23 Sept 2026): Tamil star names, ritual pictures, time, a slot grammar, Meluhhan names

Scripts: `tamil_stars.py` (+ `rebus/tlex_star_min.tsv`), `seventh.py` (R1, T1, P1), `meluhha.py`; results in
`results/tamil_stars.md`, `seventh.md`, `meluhha.md`. (profile.json not updated, at the user's request.)

1. **Numeral + fish against the Tamil star names actually attested.** The Tamil Lexicon (Madras 1924-36,
   searched on DSAL: all 111 headwords ending in -min, and full text for Pleiades, constellation, asterism,
   Ursa) has numeral + min star names for 3 (mum-min, Mrgasiras), 5 (ai-m-min, Hasta/Rohini), 6 (aru-min,
   ara-min, Pleiades) and 7 (elu-min, Ursa Major, the only one cited from Sangam poetry, Narrinai 231); none
   for 1, 2, 4, 8 or 12. In the corpus, stroke numerals before a fish sign (pairs left out, 86 tokens) have an
   attested value in 43% of cases against 63% before other signs: the star-name values are
   *under*-represented (one-sided p = 1.0). By value: 6 + fish is enriched 3.4 times (11 tokens; the Pleiades
   reading survives), 12 + fish 3.1 times (10, no Tamil name), 1 + fish 1.7 times (33, no name); 3 is
   depleted (0.7), 5 absent, 7 + fish once against 56 sevens before other signs (0.2). With the pairs
   included, 211 of 297 numeral + fish tokens are the short or long pair, for which no star name exists. So
   the numeral + fish series as a whole is not the Tamil numeral + min series; only '6 + fish = Pleiades'
   fits, and that is also the reading with the widest cross-cultural parallels (the Pleiades as a group of
   six or seven).
   Munda check: Campbell's Santali-English dictionary (1899, archive.org cu31924096339464) confirms hako
   'a fish' and ipil 'a star' (no pun) and names the Pleiades Sorenko (the Soren clan's totem), not by a
   numeral.
2. **Is the 520 ending a mark of divine names?** No sign of it. On objects with a ritual picture
   (anthropomorphic figure, scene, tree, composite animal, cross; 98 with text) 6.1% of texts end in 520,
   on unicorn seals 12.4%, on other animal seals 6.6% (ritual against animal p = 0.18). Fish name + 520
   occurs on 3 of 100 ritual objects against 6.2% of all pictured objects (binomial p = 0.12), and the
   fish + 520 names sit mostly on unicorn (76 of 1,018) and zebu (7 of 44) seals. Ritual tablets carry
   740 names (the 'cross' tablets 104 645 590 235 240 740 90 in six copies). If the fish names are divine,
   the pictures do not show it; they behave like owners' names on ordinary seals.
3. **Time depth (object type as the clock, Kenoyer and Meadow 2010).** All sites: the late bar seals (Period
   3C only) end in 520 half as often as square seals (4.7% against 10.3%, p = 0.009) and more often have no
   ending (56.5% against 46.0%, p = 0.004); 740 unchanged (39% against 44%, p = 0.17). At Harappa alone the
   same direction, not significant (60 bar seals). Fish + 520 names fall from 5.4% of square seals to 2.2% of
   bar seals, while fish signs as such do not (37% against 34%). The late seals drop the 520 class and the
   ending more than they change the grammar: a shift in naming or in seal use, not evidence of sound
   change. (Per-object stratigraphy is in CISI 3.1's data list, not online, so period comes from type only.)
4. **A slot grammar as a predictor.** Hiding each sign of 1,200 complete one-line texts in turn
   (leave-one-text-out): commonest sign top-1 11.4%, left neighbour 29.7%, both neighbours 46.3% (top-5
   68.3%; last sign 64.8%); adding the G1 ending grid gives nothing (45.0%). The known structure is local:
   two neighbours capture it, and nearly half of all signs are predictable from them. A damaged-sign
   restorer is possible in principle, but the corpus file marks no internal damage (every text is flagged
   complete), so there is nothing to restore without the ICIT damage codes.
5. **The Meluhhan names.** The only two probable Meluhhan personal names, Na-na-za and Sab-ma-ar
   (Laursen and Steinkeller 2017: 83-84; Nisaba 15 371, Urusagrig, Su-Suen 6, via harappa.com), are 2-3
   syllables. On one-line square seals the name slot (text less opener formula and ending) is 1-3 signs in
   52% of 1,148 seals, so names of that length fit the seals easily; a slot opening with a doubled sign
   (as Na-na-) is no commoner than a doubled sign anywhere in a slot (2.2% against 1.9%). With two names
   this rules nothing in or out. CDLI's search could not be queried from the command line to look for
   more.

## Eighth pass (23 Sept 2026): 12 + fish and 1 + fish, the tablets as a genre, a decipherment test bench

Scripts: `tamil_stars.py` (extended), `tablets.py`, `bench.py` (+ `keys/`); results in `results/tamil_stars.md`,
`tablets.md`, `bench.md`. (profile.json not updated, at the user's request.)

1. **12 + fish and 1 + fish are artifacts.** Seven of the ten 12 + fish tokens are one seal impressed on seven
   Lothal sealings (705 500 741 1 55 220 740 90). The single stroke before a fish is mostly the stroke of the
   opener formula (820 1 240; 817 2 1 240) or part of Harappa tablet formulas made in many copies
   (171 32 31 240 636 740 400; 692 1 240 636 740). Counting each distinct text once and leaving out the
   opener-slot stroke: 12 + fish x1.3 (4 tokens), 1 + fish x1.3 (18), 4 x1.0, 3 x0.9, 7 x0.2 (1 token), 5 absent,
   **6 + fish x4.8** (10 of 59 numerals before a fish against 3.5% elsewhere; binomial p = 4 x 10^-5). The one
   numeral + fish unit beyond chance is 6 + fish, often text-initial and in the fixed unit 16 220 520 (H-98,
   H-789, H-942; K-150 with the short 6). The Pleiades reading is the only star name the numerals support.
2. **The Harappa tablets are a genre.** 96% of incised and 85% of moulded tablets are from Harappa. Texts
   repeat: 1.86 and 1.66 objects a text (square seals 1.07); 21 tablet texts exist in 5+ copies (the commonest:
   501 405 2 240 520 x29, all with the unicorn; 176 740 400 x27; 3 156 x22; 33 700 x14). Most copied texts keep
   one picture (or a picture on some copies and none on others). Tablet vocabulary: the pot 700 (57 against 9
   on square seals), 400 (247/53), 501, 436, 137, 158, 636; 711 and 318 never on seals; the seal-only signs
   are 585, 595, 632, 70, 621, 742, 923. 18% of distinct tablet texts (less the ending) occur whole inside a
   square-seal text, against a median 10% for the same texts shuffled (range 7-12%): tablets repeat the
   names and titles of the seals. **Number + one sign as the whole text**: 9% of tablets (3 156 x22, long
   3 + pot x14, long 4 + pot x7, long 2 + pot x7), 5% of square seals, 30% of inscribed pottery. **The pot
   takes the long strokes**: 45 of the 51 numerals before 700 on tablets are long strokes, 6 short. With the
   fifth pass (long and short strokes are two numeral systems, split like Proto-Elamite's capacity and
   counting systems), 'long N + pot' reads as a capacity measure, and the tablets that carry nothing else as
   tokens or tallies of a quantity; the others copy seal names with a tablet ending (740 400), as issued
   tokens of a seal-holder would.
3. **A test bench for decipherments (`bench.py`, `keys/`, `results/bench.md`).** Prior tooling
   (joyboseroy/indus_decipher, leameiners/decipherement_protocol) tests whether the signs behave like
   writing; neither scores a proposed sign key. The bench takes any key (sign -> value in the claimed language,
   ICIT ids) and scores: B1 coverage; B2 reading against 200 shuffles of the key (values permuted among keyed
   signs of similar frequency), on consonant skeletons parsed into Monier-Williams, DEDR and ePSD2 words, in
   the claimed language and the other two; B3 the copper-tablet anchors (signs 341, 749, 753, 777/778 and
   eight texts on the back of a picture); B4 numerals, the short/long strokes, endings and openers; B5
   controls. Keys: Yajnadevam 2024 (681 signs, his xlits.csv), Parpola 1994 (30 signs, from Fig. 15.2 and the
   ending proposals), Mahadevan 1998/2014 (5 signs: 740 -(a)nru, 520 -(a)mpu, the 'merchant of the city'
   phrase 255 435 690 740 = mar-kol-pat-anru, his Fig. 2 = M-857), Kak 1988 (7 of his Table 4 Brahmi values
   whose drawings match one ICIT sign without doubt). Other published keys are not usable without a sign
   concordance: Fairservis 1992 (about 230 signs, his own codes, archive.org), Hunter 1934 (Brahmi comparison
   table), the Soviet team (drawings); Rao 1982 and Jha and Rajaram 2000 are not online.
   - **Controls.** A planted key reads 96.5-98.7% of a synthetic corpus of real words against 85.9-89.5%
     for its shuffles (best shuffle 87-91%): the test can see a true key. But a key fitted to the real
     corpus by hill-climbing (one consonant class a sign, 250 signs) reads 94.0% of it as Sanskrit, 93.1%
     as Dravidian and 93.1% as Sumerian: any language can be read at a higher rate than any published key
     reaches, so a reading rate alone is no evidence.
   - **Yajnadevam:** Sanskrit 75.3% against shuffles 75.1% (87 of 200 as good); Dravidian 71.9% (32 of
     200). Anchor signs: none read as their animal (341 = m, 749 = isan, 753 = r); anchor texts naming their
     animal 4 of 8, shuffles 2.6 on average, 45 of 200 as many. Numerals: 12 of 22 stroke signs get a
     one-letter value that starts the number word (the chance rate is about 1 in 8 a sign), none the word;
     short and long strokes of a number get the same value; the three openers all read r.
   - **Parpola 1994:** Dravidian 54.0% against 44.6% (59 of 200 shuffles as good), Sanskrit 52.2% against
     43.7% (54 of 200): not above chance, and not language-specific. (A first run with coarser shuffle
     bands of five signs showed 8 of 200; with bands of three it is chance, so the apparent edge came from
     where the long morpheme values sit, not from the language.) 6 of 8 keyed numerals are read as the
     number word, by construction; 777/778 koli matches DEDR kal 'Nilgiri ibex' by sound (a goat: the
     tablets tie 777 to the goat), a single chance-level hit; anchor texts 2 of 8, shuffles 2.3.
   - **Mahadevan, Kak:** too few signs for a reading test. **Key-independent test of Mahadevan's
     gender reading of the endings:** a gender suffix belongs to the noun, so each name should take one
     ending only. Whole names (the text before 740 or 520, with or without 400/90/151 after) seen with
     both endings: 5 of 881, against a median 46 (33-57) with the endings shuffled among lines. The endings
     are fixed per name, as gender or any lexical class would be; by last sign, only the fish signs 220 and
     240 (and 400, 460) take both freely. This supports a noun-class reading of 740/520 (Mahadevan's
     masculine/non-masculine, or any other lexical class), not his sound values.

## Ninth pass (23 Sept 2026): M77 as a replication sample, segmentation, the sign list, an in-browser bench

Scripts: `merge_m77.py`, `replicate_m77.py`, `segment.py`, `allographs.py`, `export_bench.py`; results in
`results/merge_m77.md`, `replicate_m77.md`, `segment.md`, `allographs.md`; page `docs/indus-bench.html` with
`docs/indus_bench.json`. `signs.load()` takes `with_m77=True` / `only_m77=True`.

1. **M77 merged.** Mahadevan's 1977 concordance (2,906 texts, mapped to ICIT ids through
   `icit_m77_map.tsv`; 588 tokens of 149 M77 signs have no counterpart and stay unknown) against the 2,543
   ICIT-derived objects: 1,242 M77 texts match an ICIT object (840 exactly, 402 within a quarter of their signs,
   each object used once), 1,664 do not. Site blocks recovered from the matches: Mohenjo-daro 1000-3399,
   Harappa 4000-5299, Lothal 7000s, Kalibangan 8000s; 635 additions stay 'unknown' site. The merged corpus has
   4,200 objects, but 102 additions repeat an ICIT text exactly (extra copies, or one object counted twice) and
   no object type is known, so the additions are used as an independent **replication sample**, not pooled
   blindly.
2. **Every structural finding replicates on the M77-only texts** (`replicate_m77.md`): endings fixed per name
   (4 of 385 names take both, shuffled median 26); fish-final names take 520 in 61% of lines, other names 5%;
   740 and 520 never adjacent; **6 + fish** 8 of 24 numerals before a fish against 2.9% elsewhere (ratio 11.5,
   p = 2 x 10^-7), 7 + fish never; the short and long strokes precede different signs (JSD 0.774 bits, 0 of
   500 permutations); neither published key beats its shuffles (Yajnadevam 65.0% against 67.6%; Parpola 54.9%
   against 45.3%, 37 of 100 as good). On the merged corpus: 6 + fish 17 of 81 (ratio 6.5, p = 7 x 10^-10).
3. **Unsupervised segmentation** (Goldwater's Dirichlet-process unigram model, Gibbs-sampled, told nothing
   of the structure). It cuts after the opening formula in 95% of cases (M77: 90%), and before the ending
   740/520 in only 22% (M77: 30%) against 52% (50%) of other gaps: the ending binds to the name as a suffix,
   not a word of its own. On sign-shuffled lines it cuts 83-100% of gaps everywhere. Mean word 1.66 signs
   (53% one sign, 32% two). Recurrent words found without supervision include [861 2], [817 2], [820 2],
   [740 400], [740 90], [32 220], [3 156], [33 700], [255 435 690] (Mahadevan's 'merchant of the city'),
   [503 615 752 740] and the 29-copy tablet text.
4. **Is the sign list over-split?** For the 223 signs with 5+ tokens: of the 248 pairs in the top 1% by shape
   (rendered glyphs, Dice overlap), 20.6% are also in the top 5% by context (positive-PMI neighbour vectors),
   four times the 5% expected if shape and context were independent. Merging every such pair shrinks 223 signs
   to 180 (-19%), and many merged groups are paradigmatic sets (3 ~ 4, the pair ~ one stroke, the fish
   series 220 240 235 233 231, 803 806 838 382), not variants. True variants (e.g. 405 ~ 407, 527 ~ 526,
   226 ~ 234) are a minority: the working inventory stays in the hundreds, the logo-syllabic range.
5. **The bench in the browser** (`docs/indus-bench.html`): paste a key, it scores B2 against 100 shuffles in
   the three lexicons and the anchor texts, with the bundled Parpola, Mahadevan and Kak keys (Yajnadevam's is
   not bundled: no licence stated). Checked against `bench.py`: the Parpola key gives the same real-key scores
   (52.2 / 54.0 / 25.4%). `docs/_check_writeup.py` now treats atlas, keys, secret and indus-bench as tool
   pages (TOOL_PAGES), not write-ups missing a PAGES entry.

6. **Fairservis 1992 on the bench.** His Appendix A (238 signs, Dravidian values with DEDR numbers) was
   transcribed from the archive.org page images and matched to ICIT glyphs by drawing
   (`keys/fairservis1992_raw.tsv`: 23 sure, 83 likely, 110 unsure, 22 unmatched; his example seals are cited by
   Marshall/Mackay plate numbers, so no match could be confirmed through a seal). `build_fairservis.py` makes
   two keys: sure + likely (97 signs, 64% of tokens) and with the unsure matches (172 signs). His key reads
   Dravidian 87.7% against 86.5% for its shuffles (71 of 200 as good), Sanskrit 85.6% against 85.2%; the wide
   key 92.8% against 92.4% (70 of 200). Anchor texts naming their animal 5 of 8, shuffles 5.4 on average. No
   anchor sign keyed (341, 749, 753, 777 unmatched or unsure). He reads both endings as third-person suffixes
   (740 an 'honorific', 520 ar), which does not separate the two classes of names they mark. Like every key
   tested, it reads no better than its own shuffles; with whole-word values the raw rate is high for any
   arrangement.

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

Done: the M77 map (`align_m77.py`), CISI vol. 1 (third pass), Parpola 1994's 24 readings (R3), the copper-tablet
bilinguals, slot classes, numbers and measures, the Sanskrit and Sumerian controls, the ending proposals (fourth
pass); the leads of the fifth to seventh passes. Open:

1. The full ICIT corpus (4,537 objects; account from Andreas Fuls) and CISI vol. 2 (H-396, H-568, H-598, H-602):
   rerun everything; the copper-tablet side-A texts of M-603/604 need a sharper image than CISI vol. 1's scan.
2. The seven sign = image equations are the firmest meaning anchors: a reading of 749, 341, 753 and the lens sign
   should fit markhor goat, rhinoceros, hare and bull, in whatever language is proposed.
3. Done in the sixth and seventh passes: the fish = star word is Dravidian-only among the South Asian
   families, but the numerals before the fish do not follow the Tamil numeral + min star names; only 6 + fish
   (Pleiades) fits. Open: 12 + fish and 1 + fish (enriched, no Tamil name), and the ICIT damage codes for a
   sign restorer.
4. The readings of Parpola 1997 and 2003 not in the 1994 table.

## Prior work

The lecture is published and its readings go back to Parpola 1994. Computational work on these corpora
exists: Rao et al. 2009 (entropy), Yadav et al. 2010, Farmer et al. 2004, and the indus_decipher toolkit (2026).
None of these checks Parpola 2005's specific counts and cited seals, his 1994 numeral restriction, or the
chance rate of his Tamil-compound control as done here; the counts and tables in `results/` were all
computed in these two sessions.

Draft write-up page: `unpublished/indus.html` (not on the site; see `unpublished/README.md` for publishing).
