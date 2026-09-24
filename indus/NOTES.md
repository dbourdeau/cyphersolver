# Indus script: Parpola's 2005 lecture tested against two corpora

Status: in progress (write-up republished 24 Sept 2026 at the owner's request as docs/indus.html, rewritten to cover sets 1-166; the in-browser bench stays withheld)

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
   Dravidian 87.7% against 86.2% for its shuffles (63 of 200 as good), Sanskrit 85.6% against 85.2%; the wide
   key 92.8% against 92.7% (90 of 200) (tenth-pass run). Anchor texts naming their animal 5 of 8, shuffles 5.4 on average. No
   anchor sign keyed (341, 749, 753, 777 unmatched or unsure). He reads both endings as third-person suffixes
   (740 an 'honorific', 520 ar), which does not separate the two classes of names they mark. Like every key
   tested, it reads no better than its own shuffles; with whole-word values the raw rate is high for any
   arrangement.

## Tenth pass (23 Sept 2026): a real decipherment as control, more languages, Meluhha, weights

Scripts: `elamite_control.py`, `bench.py` (vowel-aware mode B2v, Munda / Old Tamil / Burushaski lexicons, B5c),
`meluhha_oracc.py`, `weights.py`; results in `results/elamite_control.md`, `bench.md`, `meluhha_oracc.md`,
`weights.md`. Source data (scratchpad, not committed): JAMBU (github.com/moli-mandala/data: Pinnow 1959, Munda
1968, Zide 1982, Santali survey, Kharia; Berger and Yoshioka for Burushaski), the Madras Tamil Lexicon entries
citing Sangam works, Hallock 1969 Glossary of Achaemenid Elamite (archive.org OCR), the Elamicon/OCLEI Linear
Elamite corpus with its sign-value table, ORACC epsd2 (CC0), Hemmy (Marshall 1931, Mackay 1938) and Vats 1940
weight tables typed from the page images.

1. **The bench on a real decipherment (Linear Elamite, Desset et al. 2022).** 168 lines, 2,520 signs, 246 sign
   variants keyed with 61 sound values; lexicon Hallock's Achaemenid Elamite headwords (a thousand years later,
   OCR). With consonants only, the real key reads 60.7% against 62.4% for its shuffles (156 of 200 as good): **the
   consonant-skeleton test cannot see a correct key on a small corpus.** With the vowels kept (three classes,
   `bench.skelv`), the real key reads 25.7% against 19.6% (2 of 100 as good in the first check). So the
   bench's null results for the Indus keys in the consonant mode (eighth pass) are weaker evidence than they
   were stated to be; the vowel-aware mode (B2v) is the one with power, and the Indus keys are now also scored
   in it (see 2).
2. **The Indus keys, vowels kept, in six languages** (B2v; the new lexicons are Munda from JAMBU, 14,430
   forms; Old Tamil, 5,127 Tamil Lexicon headwords cited from Sangam works; Burushaski, 16,619 forms from Berger
   and Yoshioka). 100 shuffles each.
   - Yajnadevam (Sanskrit): Sanskrit 53.0% against 44.8% (10 of 100 as good, not significant); **Dravidian
     70.4% against 61.2% (0 of 100)**; Sumerian, Munda, Old Tamil, Burushaski at chance. Without his values for
     the ending signs (740 an, 520 n, 400/90/151) the Sanskrit edge goes (42.6% against 43.9%, 29 of 50) and the
     Dravidian one stays (57.6% against 52.5%, 2 of 50). A key tuned by its author to give pronounceable
     syllables keeps an advantage over its shuffles on a lexicon of short CV-CV words, whatever the language;
     the Dravidian edge of a Sanskrit key is that effect, not evidence for Dravidian. The vowel-aware test is
     necessary, not sufficient.
   - Fairservis 1992: below its shuffles in every language (Dravidian 92.7% against 97.4%, 97 of 100 as good;
     with the unsure matches 95.8% against 98.4%).
   - Parpola 1994: below its shuffles (Dravidian 77.3% against 92.5%, 100 of 100 as good): his whole-word values
     sit where the parse cannot join them into longer words.
   - So no published key passes the vowel-aware test in its own language. (Controls in this run: the planted
     keys 96-99% against 86-90% for their shuffles; fitted keys 92.7-93.8%; Linear Elamite 25.7% against 19.2%,
     4 of 100 with the vowels kept, 80 of 100 with consonants only.)
3. **Meluhha in cuneiform** (`meluhha_oracc.py`; 161 ORACC attestations in 121 texts, 77 Ur III, 91
   administrative). Nanaza and Samar are on three Irisagrig tablets of Šu-Suen 6 (Nisaba 15 371, CUSAS 40 1354
   and 1582; months 3 and 12), always as 'oil allotment of the men of Meluhha, royal donated slaves, shepherds of
   bezoars': a standing allotment. The first name is written na-na-za twice and na-na-sa3 once, a z/s
   alternation that can mark a sound Sumerian spelling lacked. Every other person tied to Meluhha has a Sumerian
   or Akkadian name: Ur-Lamma son of Meluhha (Girsu, 5 texts), Ur-Igalim son of Meluhha, Lu-sunzida 'man of
   Meluhha', Ili-ahi, Elum-Meluh, an overseer of Meluhha, the envoy Utu-illat who went to Meluhha. 'Son of
   Meluhha' names a second generation at Girsu (the 'village of Meluhha' near Gu'abba). No further Meluhhan
   personal names; the two known ones stay the only language evidence. Goods: abba wood (furniture, a weapon)
   20, carnelian 14, copper 10, mes wood 9, Meluhha-style chairs and tables 5, boats 5, the dar bird, the
   ur-DAR animal.
4. **The weights and the numerals** (`weights.py`; 472 weights: Hemmy in Marshall 1931 and Mackay 1938, Vats
   1940 without the 107 values where print confuses 3 and 8). The binary-then-decimal series (1, 2, 4 ... 64,
   160, 200, 320, 640, 1600 ...) fits 81% of them within 5% on a unit of 0.8585 g (Kenoyer's 0.871 g), against 2%
   (best 29%) for random series: the transcription is sound and the system is real. The stroke numerals do not
   follow it: the short and long strokes are dominated by 3 (160 and 209 tokens), which the series lacks; the
   tiered numerals by 7, 6 and 12 (6% of tiered tokens are powers of two). The numbers written on seals and
   tablets count things, or the capacity measure of the long strokes (seventh pass), not weight units.

## Eleventh pass (23 Sept 2026): the ending class as a language test; new sign = picture anchors

Scripts: `noun_class.py`, `anchors.py`; results in `results/noun_class.md`, `results/anchors.md` (+ `anchors.png`).
Grammar sources read: Hoffmann 1903 Mundari Grammar, Bodding 1929 Materials for a Santali Grammar, Phillips 1873
Grammar of the Santhal Language (archive.org full texts).

1. **Which names take 520** (ICIT-derived and M77 additions pooled; 1,957 name + ending lines, 520 in 14.1%;
   the name's last sign as its head). 520 is a small closed class: the fish series takes it in 154 of 254 lines
   (220 65/106, 240 44/65, 233 28/32, 231 9/14, 235 8/13; Fisher p = 6 x 10^-83), plus one fixed unit, long 3 +
   520 (56 of 63), sign 70 (20 of 20), and in part 400 (10/21), 460 (6/19), 31 (5/11). Everything Fairservis
   identifies as a human figure, animal, plant, object, tool, building or landscape takes 740: 24 of 754 lines
   with 520 (the horned man 100 0/105, grain 390 0/51 and 405 0/44, bow 900 0/49, shield 923 0/33, settlement
   861 0/14, the long pair 32 0/76). So the object at the end of a name does not decide its class: a 'he of
   the X' title (Mahadevan's reading of 740) takes the personal ending whatever X is, and the 520 names are the
   fish names, Parpola's stars.
2. **Against the class systems of the candidate languages.** A split of persons (740) from stars (520) is what
   Old Tamil's rational / non-rational (uyartinai / aḵrinai), Proto-Dravidian masculine / non-masculine (Old
   Telugu, Mahadevan 1998) and Sumerian human / non-human do. Sanskrit gender fits in part (the nakshatra names
   are mostly feminine; some are masculine and neuter). **Munda does not fit**: Hoffmann (1903: 'Distinction
   between living beings and inanimate objects') counts 'all heavenly bodies as well as the causes of natural
   phenomena, such as rain, thunder, lightning, hail' as living beings, and marks the distinction by number
   only, with no class suffix on a singular noun: a Munda language would put star names with persons and would
   not write a two-way singular ending at all. Caveats: the test rests on 740 marking persons and the fish names
   being stars; and the signs Fairservis calls sun and moon (803, 920, 820) take 740 (2 of 40), so if those
   identifications hold the 520 class is narrower than 'heavenly bodies' (which again fits gender or rationality
   better than Munda animacy). The first language test in this project that excludes a candidate family on
   grammar alone, without sound values; it cannot separate Dravidian from Sumerian.
3. **New sign = picture candidates** (`anchors.py`). Over 1,360 distinct (text, picture) units the sign-level
   test finds only object-type confounds (400, the tablet ending, with the tablet pictures). Texts always written
   with one picture add 18 pairings beyond the copper tablets, mostly moulded tablets (the gharial with four
   different texts; the multi-headed animal with 347 741 176 740 90 on 8; a cross with 104 645 590 235 240 740 90 on
   7; a tree with 465 806 158 on 5; fish with 27 32 740 400 on 3 incised tablets). Judged by eye on the render
   sheet:
   - **347**, a horned, crested quadruped drawn like 341 (the copper tablets' rhinoceros): with the multi-headed
     animal on 8 of its 9 objects (one text, 8 moulded tablets; the ninth a gaur seal). Candidate anchor, a
     logogram for the animal on the other face.
   - **460**, three tall cones on a base: with the tree / plant picture in 4 of its 5 distinct tablet texts (354
     460 798 740, 15 460 798 740, 495 460 740 400, 415 240 495 460 752 740; p = 0.0005). The best supported of the
     new candidates, since it rests on four different texts, if the cones are trees or shoots. 460 takes 520 in
     6 of 19 lines, the only non-fish sign besides 400 to do so often: plants are non-rational in Tamil.
   - **645** (an X) with the cross motif, and **318** (a bar with teeth) with the gharial: one text each, weak.
   The copper tablets' seven equations stay the firm set; 347 and 460 are the two additions worth carrying to the
   bench as anchors, marked provisional.

## Twelfth pass (23 Sept 2026): word order, female names, the keys on the new anchors

Scripts: `typology.py`, `anchors_bench.py`; results in `results/typology.md`, `results/anchors_bench.md`.

1. **Word order (T1).** The man sign 90 (178 tokens, both corpora) stands right after the ending 740 in 112
   (63%) and ends the text in 117; it opens a text 27 times, and those texts are 90 90 ..., 90, 90 400 - only
   one (90 500 740) has the 'man + name + ending' shape. The seal formula is 'X-740 man': possessor (or the name
   with its personal suffix) first, head noun last. Sumerian and Elamite put the head first ('lu2 X-ak', as the
   cuneiform itself writes 'lu2 me-luh-ha', man of Meluhha); Dravidian, Indo-Aryan, Munda and Burushaski put
   the possessor first.
2. **Female names (T2).** The woman-figure signs (Fairservis A-2 93, A-3 95/96) end or sit in only four names (93
   three times with 740, 95 once with 520): too few to test Proto-Dravidian's non-masculine women against Tamil
   and Sumerian.
3. **The two grammar tests together (T3).** A class suffix on the singular noun that separates persons from
   stars (eleventh pass): Dravidian yes (-an against -am / -tu, rational / non-rational), Elamite yes (animate -r
   against inanimate -me), Indo-Aryan in part (three genders across many declensions), Sumerian, Munda and
   Burushaski no (class shown by agreement or number, not on the singular noun). Possessor before head: Dravidian,
   Indo-Aryan, Munda, Burushaski yes; Sumerian and Elamite no. **Only Dravidian passes both outright;
   Indo-Aryan in part.** Conditional on 740/520 being suffixes of the name (fixed per name, final, bound to it
   by the segmenter), 90 being a head noun, and the fish names being stars. It is the strongest argument for
   the language family in this folder, and it uses no sound values.
4. **The keys on the provisional anchors** (`anchors_bench.py`; sign 460 = tree, ten texts written with a
   tree, the gharial or fish). No key gives 460 a word for tree (Yajnadevam d; Fairservis murYal, his 'three
   conical structures'; the others have no value). Anchor texts containing a word for their picture: Yajnadevam 5
   of 10 (shuffles 4.7), Fairservis 7 (7.5), Mahadevan 6 (4.1; 32 of 200 shuffles as good), Parpola 3 (4.4), Kak
   0. None above chance; with short Dravidian and Sanskrit words, 4-7 of 10 texts contain some picture word by
   chance, so this form of the test is weak.

## Thirteenth pass (23 Sept 2026): fitted keys on unseen texts

Script: `fit_holdout.py`; result `results/fit_holdout.md`. The one validation the prize commentary asks for that a
fitted key can be put through: fit a syllabic key to the ICIT-derived lines (2,088; 250 commonest signs, 47 values
= consonant class x vowel class, bare vowels, bare consonants; 20,000 hill-climbing steps), then read the 975
M77-only lines that do not repeat a training line, against 100 shuffles of the fitted key. Credit: consonants
covered by words of 3+ consonants (with vowels credited, a random key already scored 95%: the vowel-aware parse
saturates when every sign is a syllable).

- Every language's fitted key keeps an edge on the unseen texts: Dravidian (DEDR) 91.6% against 90.3% (1 of 100
  shuffles as good), Sanskrit 93.6 / 91.7 (0), Sumerian 85.0 / 81.5 (0), Munda 79.8 / 77.2 (2), Old Tamil
  76.3 / 64.6 (0), Burushaski 78.8 / 69.7 (0).
- A key fitted to sign-shuffled training lines does not (Dravidian 91.6 against 93.0, 99 of 100; Sanskrit 68 of
  100): the fitted keys learn the script's real recurrent sign sequences, which any lexicon can partly map onto its
  words, not the language. A planted synthetic Dravidian key generalises too (95.3 against 93.3, 0 of 100).
- The margins do not rank the languages: they are largest for the smallest lexicons (Old Tamil +11.7 points,
  Burushaski +9.1) and smallest for the densest (DEDR +1.3, Monier-Williams +1.9), i.e. they measure lexicon density.
  **Hold-out generalisation of a fitted key does not identify the language.** A key fitted by statistics alone
  cannot be the decipherment the prize asks for; the language evidence in this folder remains the two grammar tests
  (eleventh and twelfth passes), which point to Dravidian conditionally.
- **Matched lexicons** (`matched_holdout.py`, `results/matched_holdout.md`): every lexicon cut to the same 2,405
  skeletons with the same spread of consonant counts, 5 draws, z-score of the held-out margin. Positive control, a
  synthetic corpus written in Dravidian: Old Tamil wins 4 of 5 draws (z 8.8), but DEDR, the lexicon the text was
  drawn from, comes last (2.0): the ranking depends on how a lexicon is made. Indus: Burushaski 6.2, Sumerian 6.1,
  Sanskrit 6.0, DEDR 5.2, Old Tamil 5.1, Munda 5.0, overlapping from draw to draw. Inconclusive; if anything weakly
  against an Old-Tamil-like lexicon, which ranks fifth where the control says it should win. Fitted keys do not
  identify the language even with matched lexicons and unseen texts.

- **CDLI full-text search for Meluhhan names** (23 Sept; cdli.earth, transliteration search 'me-luh', ATF export
  paged, 223 texts, 149 not in the ORACC set). The additions are lexical lists (Meluhha wood, carnelian, the Meluhha
  bird), royal inscriptions (Sargon's boats of Meluhha, Gudea, Shulgi's 'speckled dog of Meluhha'), Neo-Assyrian
  texts where Meluhha means Nubia (irrelevant), Ur III inventories, a 'field of Meluhha' (ZA 74 65) and a granary
  'in Meluhha' village (BM 025318). The only people named: Šu-ilišu, 'translator of Meluhha' (his seal, CDLI seal
  014339; an Akkadian name) and Dadi, 'soldier of the Meluhha boat' (BIN 8 298, Old Akkadian). No further foreign
  Meluhhan personal names: Nanaza and Samar remain the only direct evidence of the language in cuneiform.

## Fourteenth pass (23 Sept 2026): Tamil-Brahmi names, registered predictions

Scripts: `tamil_brahmi.py`, `predict_test.py`; `PREDICTIONS.md` (committed before the test, 70e563ca8);
results `results/tamil_brahmi.md`, `results/predict_test.md`.

1. **Tamil-Brahmi names** (Mahadevan 2003, Early Tamil Epigraphy, Appendix II, archive.org OCR, parsed; about 100 full
   names). 68% end in a masculine suffix (-an, -on, -ko, -antai, -nanti, -porai), 5% are marked feminine, the rest
   are mostly OCR debris; mean 1.6 words a name. The Indus endings split 86% (740) / 14% (520); names are 1-6 signs
   (mean 3.2). Agreement in shape: one dominant class suffix on the last element, a small second class, possessor
   first (X-an makan). But the Indus minority class is the fish names, not women's names; only a rational /
   non-rational reading maps one onto the other. Consistent with Dravidian, without power against Sanskrit.
2. **Registered predictions from the Dravidian model failed.** P1 (a rational plural sign replacing 740 on the same
   names): none; the candidates replace 740 less often than chance. P3 (520 stems alternate no more than 740 stems):
   10.9% against 8.0%, fails narrowly. The model makes no correct prediction beyond the data it was built on.

3. **Literature check** (`results/lit_check.md`, background agent; Parpola 1994 read in a clean archive.org OCR). Known
   before: jar/arrow exclusivity (Parpola 1994: 94; Mahadevan's arrow essay as gender suffixes); fish + arrow (Parpola
   1994 fig. 6.6, Mukhopadhyay 2019), without rates; the head-final 'X-jar man' order against Sumerian, Elamite and
   others (Parpola 1994: 86-89, 95-97, 125, 130) - so the word-order half of the twelfth-pass argument is Parpola's;
   the opening phrase (Parpola's position I; Yadav et al. 2010); short vs long strokes (Parpola 1994: 82), the pot as a
   measure on tablets (Wells 2015), tablets as tokens (Meadow and Kenoyer 2000, Rao 2018); earlier segmentations
   (Soviet team, Yadav 2008, Fuls 2015); the copper-tablet equations (Parpola 1994: 107-112, 2008); fitted keys not
   identifying the language (Raghavendra 2026, arXiv 2608.02999, synthetic corpus). Not found before: the per-name
   fixedness count, the closed 520 class by depicted category, the class-suffix test and the combined two-test
   argument, the opener-variant test, the numeral systems against Proto-Elamite and the weights, the numeral + fish
   enrichment test (against Parpola's 3 + fish), the shuffle bench validated on Linear Elamite, the late bar seals,
   anchors 347/460. Not read in full: Wells 2011/2015, Fuls 2013-2020, Mahadevan 1970/1986/2014, Parpola 2008/2015.

4. **Outside evidence** (background agent; files in the scratchpad `outside/`, not committed). No partial
   bilingual exists: no object carries both Indus signs and a readable text (Ur U.7683 has cuneiform and no Indus
   signs; Šu-ilišu's seal is Akkadian). Laursen 2010 lists 29 Indus-inscribed Gulf-type seals; only three carry
   sequences known in the Indus Valley, and the 'twins' sign begins 4 Bahrain texts: non-Indus names in Indus signs,
   a test bed rather than a key. Witzel 1999 (EJVS, free) gives the Vedic substrate words (Para-Munda, 'Language X',
   Meluhhan loans), extracted to CSV but not hand-checked. The Dholavira signboard is already in both corpora;
   4MSR/Binjor, Kotada Bhadli, Sanauli and newer Rakhigarhi seals are in neither.
5. **A fuller ICIT-derived corpus** (4,578 objects, 5,559 texts, same sign numbers) turned out to be built into the
   JavaScript of indusscript.net. The data are ICIT's (Wells, Fuls); used here only locally, not redistributed
   (`replicate_full.py`, `results/replicate_full.md`, aggregate numbers only). Every structural finding holds on it:
   endings fixed per name 9 of 1,014 (shuffled 69); fish-final names take 520 in 62% of lines (other names 8%); 740
   and 520 never adjacent; 6 + fish ratio 4.7 (p = 9e-6), 7 + fish once; short vs long strokes 0.61 bits (0 of 500);
   the man sign after 740 106 times, text-initial 16. On the 1,203 objects the indus-website dump lacks (mostly short
   texts): same directions (fixed endings 1 of 162 against 4; fish 520 62% against 7%; 6 + fish ratio 3.8, p = 0.02).

## Fifteenth pass (23 Sept 2026): restoration, periods, Gulf control, substrate words, paper draft

Scripts: `icit_full.py` (reader for the fuller corpus: '/' separates lines, '000' is a missing sign, ']' left / '['
right mark broken edges; replaces the rough parse of replicate_full.py), `restore.py`, `periods.py`, `gulf.py`,
`substrate.py`; results `results/restore.md`, `periods.md`, `gulf.md`, `substrate.md`; `PAPER_DRAFT.md`.

1. **Restoration against intact twins.** 157 broken single-line texts have an intact copy that fixes the lost sign
   (93 broken at the reading start, 64 at the end; twins disagree in 105). Grammar-only prediction, with every text
   containing the legible part withheld: commonest sign at the edge 6% top-1 (15% top-5); commonest neighbour 24% (55%);
   neighbour at the line edge 27% (41%). Lost endings (740/520) restored in 10 of 13; lost heading signs 0 of 9.
2. **Periods.** The records carry Mackay's periods (Mohenjo-daro: Early 48, Intermediate 425, Late 328) and HARP's (Harappa
   3B 186, 3C 169, B/C 402). Earlier against later: headings and endings do not change (Jensen-Shannon z 0.0 at
   Mohenjo-daro, 0.2 at Harappa); stroke numerals do (z 3.7, 3.2; short 3 falls from 14% to 4% of numerals at
   Mohenjo-daro, long 4 from 29% to 11% at Harappa); name signs change at Harappa (z 1.9, p 0.04), not at Mohenjo-daro.
   520 share of name lines 16% / 12% and 19% / 17%: stable. The grammar holds; counting practice moves.
3. **The Gulf and West Asian texts as a foreign-language control** (20 intact objects). Indus signs (84% of tokens are
   signs common at home), but endings on 11% of lines against 43% at home (Fisher p = 0.007), no heading (0 of 20), and
   45% of sign pairs attested at home against 70% for home texts (22% if shuffled). The two West Asian texts that end in
   740 are square seals (Kish, Gonur), the Indus type. The endings belong to the Indus language, not the script.
4. **Witzel's substrate words.** No test possible: the sound-pattern model fails its positive control (Witzel's Dravidian
   loans score -0.02, no more Dravidian-like than ordinary Sanskrit words) and his 'Meluhhan' is seven reconstructed
   forms (-0.08). Recorded as the main alternative position (Para-Munda north, Meluhhan south).
5. **Paper draft** for Lasry: `PAPER_DRAFT.md` (bench validated on Linear Elamite, structure, language, negative results,
   what is new, limitations).

## Sixteenth pass (23 Sept 2026): second registered predictions, restoration model, period detail, famous-target rule

1. **Second registered predictions hold** (`PREDICTIONS.md`, committed before the test; `predict_test2.py`). Q1: the
   ending follows the name's last sign (MI excess 0.307 bits held out) far more than its first (0.052); names sharing a
   last sign agree in ending 95.4% (first sign 83.1%). Q2: a fish sign inside the name but not last takes 520 in 8.2%
   (held out), fish-final 55.0%, no fish 5.4%. Head-final compound with a class suffix; against Sumerian and Elamite;
   does not separate Dravidian from Indo-Aryan.
2. **Restoration, interpolated model** (two edge signs + neighbour + edge prior): 24% top-1, 51% top-5 - no better than
   the neighbour-at-edge model (27%): with parallels withheld, two-sign contexts are too sparse.
3. **Periods, which name signs move.** Mohenjo-daro, earlier -> Late: 760, 798, 240, 527, 806 gain; 156, 390, 100, 892
   lose. Harappa 3B -> 3C: 440 (0 -> 7% of objects) and 416 (1 -> 7%) appear; the pot 700 falls (32 -> 24%). Mackay's
   sub-phase numbering was not used (its direction is ambiguous in the records).
4. **Gulf catalogue not added**: Laursen 2010's 29 seals are given only as drawings (his Fig. 11); not transcribed.
5. **Famous targets keep no profile.json** (owner's rule): indus/, voynich/, beale/ profiles removed; `FAMOUS` in
   `docs/_check_writeup.py` is honoured by the write-up checker, `_check_profile.py --audit` and
   `_export_profiles.py`; CLAUDE.md updated. `PAPER_DRAFT.md` is a standalone article, not paper data.
6. **Site**: new section 'Predictions, restorations and foreign names' on docs/indus.html.

7. **Second literature check** (`results/lit_check.md`, 'Second pass (full texts)'). Earlier than thought:
   restoration of deleted signs (Rao et al. 2009; Yadav et al. 2010, 74%); West Asian seals quantified as foreign to
   the Indus model (Rao et al. 2009); stroke series, Proto-Elamite parallel, pot + number, tablets as tokens (Wells 2006);
   sign-pair stability over Mohenjo-daro periods (Rao and Mahadevan 1987); head-final order (Mahadevan 1982, 1986);
   exclusivity of the endings (Hunter 1934). Contradictions: Wells 2006: 200-208 prefers Munda on word structure;
   Mahadevan 1970: 46 finds opener proportions the same at every site. Site, dossier and draft corrected.

## Seventeenth pass (23-24 Sept 2026): Wells and Mahadevan tested, third predictions, grammar model, sign classes, seals

Scripts: `wells_test.py`, `predict_test3.py`, `grammar_model.py`, `name_classes.py`, `anchors_full.py`; results in
`results/wells_test.md`, `predict_test3.md`, `grammar_model.md`, `name_classes.md`, `anchors_full.md`.

1. **Wells 2006 (Munda) tested.** His case (pp. 203-208) is that Indus words use prefixes ('initial clusters') and
   insertions, which PDr lacks. On the corpus: the heading is not a prefix selected by a root (pairs sharing the next
   sign share the opener only 6 points above chance, against 16 points for the ending on the name's last sign); no
   small set of name-initial signs combines with many roots (the five commonest initial signs cover 27% of names, the
   five final 30%, with similar productivity); the 31 insertions are mostly fish-type signs and numerals, i.e.
   attribute + head compounds, ordinary in Dravidian. His arguments do not survive the data.
2. **Mahadevan 1970 on the openers: confirmed; our claim withdrawn.** In M77, 817 and 861 are one sign (both map to
   MSg267). In the ICIT-derived corpus, Mohenjo-daro against Harappa with all three openers: MI 0.002 bits, p = 0.66.
   The 'site / object-type effect' of the sixth pass (O1) came from Lothal (817 13 of 22) and the TAG:B sealings (817
   10 of 10), impressions of a few seals. Site, dossier and draft corrected.
3. **Third registered predictions fail** (R1 numerals as attributes: 26% of name-internal numerals stand last; R2
   stacked possessives: 11% against 34%). Tally: 2 held, 4 failed.
4. **Slot grammar against n-grams on unseen texts** (2,140 held-out lines): unigram 6.23 bits/sign, bigram 5.07,
   trigram 4.99, slot grammar 5.11 (bigram names) / 5.04 (trigram names). The explicit rules capture what local
   n-grams capture, no more.
5. **Sign classes inside names** (84 signs with 15+ tokens; SVD-reduced neighbour profiles + position + ending,
   k-means k = 8, 30 bootstraps): name-final 740-class heads (176, 760, 798, 752, 923 ...; 66% final, 520 in 1 of 600);
   the fish group with the stroke pair, 60, 741, 803, 806 (58% inside, 520 in 158 of 282); name-initial first elements
   (32, 920, 255, 590, 61, 415 ...; 45-59% initial). Stability 0.35-0.70: tendencies, not sharp classes.
6. **Seals: the text does not follow the picture.** 1,556 distinct seal texts of the fuller corpus: one sign-animal
   association survives Bonferroni (700 with the short-horned bull, 3 of 17 texts); no sign goes with the standard or
   the trough. Seal texts do not name their animal; no new anchors.

7. **Linear B as a second known-answer control** (`linb_control.py`, `results/linb_control.md`; DAMOS corpus, 4,988
   lines of 3+ syllabic signs read without word dividers; Greek LSJ headwords + Homeric forms, 136,872). The real key
   does not beat its shuffles: consonants only 32.7% against 29.4% (11 of 100 as good), vowels kept 40.7% against 38.9%
   (27 of 100); with the Greek list adjusted to Linear B spelling 12 and 41 of 100. **The bench cannot reliably
   recognise a correct decipherment**; its Linear Elamite success does not generalise. Its null results for the Indus
   keys show that reading rates prove nothing, not that the keys are wrong. Site, bench page, dossier and draft
   corrected.

## Eighteenth pass (24 Sept 2026): are 520 names divine names and 740 names personal names?

Registered first (PREDICTIONS.md, fourth set, commit 8aa138d62), then tested (`predict_test4.py`,
`results/predict_test4.md`; 795 intact seals of the fuller corpus). Hypothesis T: if fish = star = god (Parpola), 520
names are shared divine / astral names or titles and should recur on more seals and across more sites than 740 ('X's
man') personal names, at the same length. **Both parts fail**: length-matched recurrence -2.9 points (p = 0.84); spread
over 2+ sites 54% against 57%, both at or under a site-shuffled null. Recurrence is set by name length alone. Tally of
registered predictions: 2 held, 6 failed. Unregistered observation: recurring names of both classes are not local.

## Nineteenth pass (24 Sept 2026): do same-name seals come from the same level?

Registered first (PREDICTIONS.md, fifth set, commit fcfc471e3), then tested (`predict_test5.py`,
`results/predict_test5.md`). Hypothesis V: a recurring name marks one holder or one generation, so same-name seals
should share a period (V1) and a depth (V2). **Both fail**: same period 47% against 46% shuffled (36 pairs, p = 0.49);
Mohenjo-daro depth difference 4.7 ft against 5.0 ft (71 pairs, p = 0.37). Names run across Intermediate and Late
Mohenjo-daro, which fits names or titles handed on. Weak test: coarse periods, datums differ by area, pairs not
independent. Tally 2 held, 8 failed.

## Twentieth pass (24 Sept 2026): sealings and seal names

Registered first (PREDICTIONS.md, sixth set, bdda56a55), tested (`predict_test6.py`). Hypothesis W: sealings are
made at home by holders of common names. **W1 fails**: 0 of 17 name-matched sealings have a same-name seal at their
site; significant 'away' (p = 0.001) only because 10 are one Lothal batch; with distinct texts (7) p = 0.50. **W2
fails** (+3.9 points, p = 0.27). Lothal, Rupar and Dholavira sealings match Mohenjo-daro seals; check Frenez on
Lothal. Tally 2 held, 10 failed.

## Twenty-first pass (24 Sept 2026): where seal texts break lines

Registered first (PREDICTIONS.md, seventh set, 203feed52), tested (`predict_test7.py`). Hypothesis X: breaks fall
between words. **X1 fails** (breaks on heading/ending boundaries 1-6 of 69, no more than random); **X2 holds**: the 30
highest-PMI sign pairs are never split across lines (0 of 31 gaps against 18%, p = 0.003; 0 of 21 interior gaps
without the heading pairs, p = 0.009). **Found while testing:** multi-line line order in the fuller corpus is
ambiguous (listed order: ending last on 34 of 66; reversed, as data/corpus.tsv: heading first on 12). icit_full.py
keeps the listed order, with `LINES_REVERSED` to flip; the test holds either way. Tally 3 held, 11 failed.

## Twenty-second pass (24 Sept 2026): foreign names, bound pairs and free signs

Registered first (PREDICTIONS.md, eighth set, 5f2553547), tested (`predict_test8.py`). Hypothesis Y: foreign names on
West Asian seals are spelled with sound signs. **Y1 fails narrowly** (bound pairs 5.6% against 12.7%, p = 0.06);
**Y2 holds** (West Asian tokens use freer signs, +0.184 against +0.084, p = 0.03). Y fails as registered. Tally 4
held, 12 failed. Freedom scores (residual neighbour diversity) are a candidate way to pick out phonetic signs.

## Twenty-third pass (24 Sept 2026): same-text tablets and levels (power check for V)

Registered first (PREDICTIONS.md, ninth set, 3b09eeb34), tested (`predict_test9.py`). Hypothesis Z: identical
Harappa tablets lie in the same level. **Holds**: same level 25% against 21% (3,470 pairs, p = 0.0003); depth 4.2
against 5.2 (4,600 pairs, p = 0.0001). The effect is small; the fifth-set seal test (36 / 71 pairs) could not have
seen it, so V's failure is uninformative and 'names handed on' is withdrawn. Harappa seals: 3 of 4 same-name pairs
share a level (unregistered, tiny). Tally 6 held, 12 failed (counting parts).

## Twenty-fourth pass (24 Sept 2026): optional signs

Registered first (PREDICTIONS.md, tenth set, 80cc3a454), tested (`predict_test10.py`). Hypothesis AA: optional signs
are phonetic complements. **AA1 holds weakly** (added sign freer, +0.061 against +0.009, p = 0.016); **AA2 fails the
other way**: added signs stand first in 195 of 310 pairs, last in 98 (44% expected last). Names grow at the front
(attribute + head), which fits the head-final reading, not complements. Tally 7 held, 13 failed (counting parts).

## Twenty-fifth pass (24 Sept 2026): replications and a candidate sound-sign shortlist

Registered first (PREDICTIONS.md, eleventh set, 36d7be384), tested (`predict_test11.py`). **All four hold**: bound
pairs are not split on 362 M77 multi-line texts (1 of 155 against 24%); freedom agrees between seals and tablets
(rho 0.34); the West Asian effect holds with M77-only freedom (p = 0.001); in Linear B syllabograms are freer than
word signs (AUC 0.77). Shortlist (`sound_shortlist.py`): 46 Indus signs free in every source, 34 on both sides; the
rule's precision on Linear B (Knossos / Pylos) is 96%, recall 55%. Headed by the jar-with-strokes signs 741 / 742 /
745. Candidates only; no values. Tally 11 held, 13 failed.

## Twenty-sixth pass (24 Sept 2026): the sound-sign shortlist tested

Registered first (PREDICTIONS.md, twelfth set, fbb83702b), tested (`predict_test12.py`). **SL1 fails** (listed signs
30% of West Asian tokens against 32% at home); **SL2 fails** (candidate swaps share a site 46% against 49%); **SL3
fails** (object type 61% against 57%, p = 0.18). The shortlist is not supported; its commonest swaps are fish-series
heads. Freedom itself stands (RF1, RC, Y2, RF2). Tally 11 held, 16 failed.

## Twenty-seventh pass (24 Sept 2026): ten hypotheses at once

Registered first (PREDICTIONS.md, thirteenth set, d28f127a1), tested (`predict_test13.py`), then checked
(`robust13.py`). Held: H3 (graphic families share contexts; mostly fish), H5 (frequent signs simpler, both samples),
H7 (names grow at the front from attested names; partly numerals), H8 (first sign more site-informative; not robust:
tablet batches), H10 (heads from a smaller inventory; robust). Failed: H1 (doubling ~ numerals; p 0.086 / 0.059), H2
(bound pairs not specially fixed; order is fixed generally), H4 (names do not diverge with distance; grammar signs do,
rho 0.45, p 0.037, reverse of prediction), H6 (two-ending texts not on tablets), H9 (variants not regional). Tally 16
held, 21 failed.

## Twenty-eighth pass (24 Sept 2026): fifteen hypotheses toward the language

Registered first (PREDICTIONS.md, fourteenth set, 663a85e87), tested (`predict_test14.py`). **One held (K1)**: human-
figure heads take 740 (81/82, 29/29; mostly sign 100). K15 fails on B's small n but 90 ('man') follows only 740, 96
of 96. Both fit 740 as the person class (Mahadevan's -an). Near misses: K8 (heads steadier than attributes over time,
p = 0.052), K12 (free signs simpler, B p = 0.061). Failed and informative: K13 (fish heads do not keep sky company),
K9 / K10 (the H4 and H1 leads do not replicate), K4 (agreement in A only). Tally 17 held, 35 failed.

## Twenty-ninth pass (24 Sept 2026): morphology and sound signs

Registered first (PREDICTIONS.md, fifteenth set, 675e2f358), tested (`predict_test15.py`), checked (`robust15.py`).
**N4 holds and survives the repetition check**: once-only names use freer signs (A +0.228, B +0.120; with freedom from
name-free texts +0.097, +0.057). Failed and informative: **N2** (520 is counted like a noun, 22% after a numeral,
more than heads; 740 only 6-7%, N1): the two endings differ, 520 looks like a countable word; N9 (400 is not plural;
reverse); N3 (741 as oblique form: A yes, B no); N6 (tablets do not carry seal names); N7, N8, N5, N10. Tally 18
held, 44 failed.

## Thirtieth pass (24 Sept 2026): twenty-five hypotheses on the leads

Registered first (PREDICTIONS.md, sixteenth set, fb621fc96), tested (`predict_test16.py`), checked (`robust16.py`).
**The Linear B control (P25) holds: the rare-word freedom effect is general, so N4 is withdrawn as evidence of sound
spelling** (with P1, P2, P22, P23). **520 is preceded almost only by the long 3 (33-520), a fixed unit; N2 corrected.**
New structure: tablet variants differ at numerals (29%) far more than seal-name variants (13%) (P11, P12); heads
steadier than attributes over time at Harappa (P13); fixed attribute slots (P14); human heads rarely counted (P10);
head + ending and ending + 90/400/151 are never split by a line break (P17, P18: 1-3% against 23-25%). Tally 31 held,
56 failed.

## Thirty-first pass (24 Sept 2026): twenty-five hypotheses on the surviving leads

Registered first (PREDICTIONS.md, seventeenth set, bc91e75ff), tested (`predict_test17.py`), checked (`robust17.py`).
Held: tablets record 'long-stroke N + 700 (measuring container)' (U1-U3; 48% of tablet numerals precede 700, seals 4
cases), 400 after an ending is a tablet / sealing sign (U5, distinct texts 78/101 against 14/71), heads select
attributes (U12), humans are heads (U14), head-to-ending rule transfers A to B at 95% against 88% (U15), headed names
use other heads (U17), pots lack the heading (U20), unicorn seals carry longer, more often headed texts (U21, U22),
cylinder seals lack endings even at Indus sites (U24). 33-520 is a seal-closing formula, not an ending (U6-U10 fail).
Tally 43 held, 69 failed.

## Thirty-second pass (24 Sept 2026): the two genres

Registered first (PREDICTIONS.md, eighteenth set, c46ce5f43), tested (`predict_test18.py`), described
(`describe18.py`). Held: N700 tablets are a Harappa count-token class (W1, W2, W7, W8): 318 of 361 are bare 'long
3 / 4 / 2 + 700', one unit per piece, no endings, 29% of Harappa tablets against 2% at Mohenjo-daro (likely known from
the HARP reports). Sealings are seal texts (W11); tiered numerals are seal numerals (W15); the closing formula is
'705 / 706 + 33 + 520' (W16). Eighteen failed, including W12 (sealings do not share the tablets' 400) and W25 (heading
later only at Harappa). Tally 50 held, 87 failed.

## Thirty-third pass (24 Sept 2026): published readings as predictions

Registered first (PREDICTIONS.md, nineteenth set, 1f2362fc4), tested (`predict_test19.py`). Held: X1 (700 counted with
long strokes, 96%: Fairservis's measure fits), X8 (human heads never 520), X10 (84% of heads fix their ending; the
fish series is the exception), X18 (same-value count tokens lie together), X21 (numbered fish take 520: the one result
siding with Parpola's star names), X22 (90 is a seal sign), X23 (moulded and incised tokens count different values).
Failed: X9 (fish heads 61% 520, against a strict gender suffix), X11 (740 not followed by a possessed noun, 9%), the
numeral-like tests X2-X6 (test insensitive), X13 (degenerate), X14 (706 absent from M77). Tally 57 held, 105 failed.

## Thirty-fourth pass (24 Sept 2026): ten best hypotheses

Registered first (PREDICTIONS.md, twentieth set, 999bc85e1), tested (`predict_test20.py`), checked (`robust20.py`).
Held: Z2 (705 and 706 one sign in the closing formula), Z3 (740 heads are people, weapons, implements, measures:
47% against 22% without fish), Z6 and Z7 (400 and 740 never begin a line: bound forms), Z8 (count values differ by
technique in both excavations, differently), Z10 (heads fix endings on seals alone, 81%). Failed: Z1 (numbered-fish
result holds in B only: withdrawn to suggestive), Z4, Z5 (90 too rare in M77), Z9. Tally 63 held, 109 failed.

## Thirty-fifth pass (24 Sept 2026): how much can be read, and the lines that fit no template

`readable.py` (descriptive): 53% of intact lines fit a template (name + ending 38%, count token 9%, numbers only 4%,
closing formula 1%, count + other 1%); 43% of sign tokens have a known function (numbers 19%, endings 12%, heading,
clitics, formula and measure signs 10%, human figures 3%); 57% are content signs known only by position. Registered
(PREDICTIONS.md, twenty-first set, 17f2f40a7), tested (`predict_test21.py`): bare lines keep the head-final order (R1,
R3, R4) and on seals are a less formal, regional form (R9, R11, R12), but many are records with numerals (R5), longer
than names (R19 reverse); tablets close lines with 400 / 90 without an ending (R25); pot marks are single numbers
(R16, R17); the head / attribute classes cover only half of B's tokens (R14 fails). Tally 73 held, 124 failed.

## Thirty-sixth pass (24 Sept 2026): classes of the content signs

Registered first (PREDICTIONS.md, twenty-second set, 73d793ccb), tested (`predict_test22.py`; 1,000 rather than 10,000
permutations for Q8, Q9, Q11). The contextual clustering works on Linear B (Q2) but does not gather the Indus
numerals (Q1 fails), so its 8 clusters are not validated word classes. They are reproducible across transcriptions
(Q3, Q12), differ in ending (Q5), picture category (Q6), complexity (Q10) and object (Q8), and cover 93% of B's
tokens (Q13); they are not positional classes (Q4, Q14), human figures scatter (Q7), heads spread (Q15). Tally 81
held, 131 failed. The site page is withheld (24 Sept); results kept in indus/ only.

## Thirty-seventh pass (24 Sept 2026): ligatures, and a classification that must pass its check

Registered first (PREDICTIONS.md, twenty-third set, 52a1bdcc7), tested (`predict_test23.py`). One held: 555 behaves as
550 + 482 in sequence (G3, p = 0.0009); 154 as 151 + 740 narrowly misses (p = 0.068); all 4 testable ligatures score
higher as sequences than as modified bases (G7 fails only on its 5-ligature bar). No clustering variant passes the
numeral check (C1: left 2.5, right 1.2, both + positions 2.9, k = 12 2.1, bar 3), so the classification lead is
closed. Tally 82 held, 143 failed.

## Thirty-eighth pass (24 Sept 2026): reading order, numbers, seals as owned objects

Registered first (PREDICTIONS.md, twenty-fourth set, 545049378), tested (`predict_test24.py`). Held: recorded
left-to-right directions are right (M1) and come from the smaller places (M2); Mahadevan's line order is supported
(M3); tiered numerals are for 5-8 (M6); bar seals carry suffix-less names (M12). **M4 settles the fuller corpus's line
order: reversed (13 against 3), as data/corpus.tsv; icit_full.py's listed order is wrong for most multi-line texts**
(default kept for reproducibility; use LINES_REVERSED = True from now on). Reverse findings: numerals side by side put
the smaller first (M5); numbers before fish are smaller (M7); after an ending it is always 90 then 400 (M8). Same-name
seals do not share animal, shape or heading beyond chance (M9-M11). Tally 87 held, 150 failed.

## Thirty-ninth pass (24 Sept 2026): affixed signs, direction, numbers, bar seals

Registered first (PREDICTIONS.md, twenty-fifth set, a68602bb0), tested (`predict_test25.py`, fuller corpus with lines
reversed). Held: left-to-right writing avoids seals and goes with short texts, other animals and bar seals (O24, O9,
O8, O20); long-stroke numerals count containers and devices (37% against 3%), short strokes go with fish (O12, O13);
400 after a name is an incised-tablet feature (O22, O14). Failed: affixed strokes and carets are not written
sequences (O1-O5); bar seals later only narrowly (O15: MD p = 0.041, Harappa 0.054). Tally 95 held, 167 failed.

## Fortieth pass (24 Sept 2026): tablet records, numbers, direction, variants

Registered first (PREDICTIONS.md, twenty-sixth set, 2b74eaca1), tested (`predict_test26.py`). Held (15): incised name
tablets with 400 are a Harappa-only genre (T10, 83 of 83) naming seal-holders (T4, 53% of names also on seals against
23% on moulded), mostly persons (T7), without the heading (T5), counting in long strokes (T3) but never in 700 (T9
fails), numbers before the name (T2 reverse), earlier not later (T6 reverse); the long count's value depends on the unit
(N1); fish take the stroke pair (N2); tiered numerals can head a name (N7); counts close lines (N5); tablets count long
(N6); direct writing runs left to right more (D2); affixed variants are attributes that alternate with their base (V2,
V3, V4); copper tablets carry no endings (X2). Tally 110 held, 177 failed.

## Forty-first pass (24 Sept 2026): the Harappa name records, numbers, labels

Registered first (PREDICTIONS.md, twenty-seventh set, 687e3fdd9), tested (`predict_test27.py`). The name tablets are
copies: same-name tablets carry the same number in all 25 pairs (L2 fails) and lie in one level (L3, 86%); the format is
'[number] [short name]-740 400', 400 always last (L5), names shorter than on seals (L6), numbers unlike the tokens'
(L9). The stroke-pair fish take 520 (L11, +39 points). 700 is counted 3, 740 counted 2 (L12). Long strokes open lines
(L15) and count containers on seals too (L25). Fish variants alternate with 220 (L16). Pots run left to right 20% (L19);
copper-tablet texts are recurring labels (L21). Tally 121 held, 191 failed.

## Forty-second pass (24 Sept 2026): receipts, the fish split, units, habits

Registered first (PREDICTIONS.md, twenty-eighth set, 2bef1f5f1), tested (`predict_test28.py`). Receipts name a
seal-holder by the end of the seal name (E3, 51 of 83; E4, half one sign), copies buried together (E1), numbers 1-2
(E21), never a human head (E22 reverse). '32 740' is a later formula, tokens earlier, larger counts deeper (E7, E20).
The stroke pair belongs with the fish and those names carry the heading (E11, E12). In every notation the number
depends on the following sign: numeral + sign pairs are idioms, not free counts (E14-E16). Copper tablets carry no
numbers (E19). Tally 135 held, 202 failed.

## Forty-third pass (24 Sept 2026): receipts, number idioms, titled names

Registered first (PREDICTIONS.md, twenty-ninth set, 0c033b95c), tested (`predict_test29.py`). Receipts name Harappa's own
seal-holders (J1: 76% of matches at Harappa against 17% of seal names) who are persons (J3: 98% 740), by a head sign
(J2: 82%). Numeral + sign are bound idioms (J7: split by a line 6% against 26%; J8: the commonest value 70% per sign);
'numeral + 700' is a tablet formula (J25: 4 of 1,607 seals). Stroke-pair fish names are seal names with the 861
heading (J12, J13). Count tokens shift from incised to moulded over time (J16); other-animal seals carry more numerals
(J20). J21 invalid (the heading contains the stroke pair). Tally 145 held, 217 failed.

## Forty-fourth pass (24 Sept 2026): the Harappa system in detail

Registered first (PREDICTIONS.md, thirtieth set, 9a7a91f7d), tested (`predict_test30.py`). Receipts lie near the seals
of the people they name (HA1); moulded name tablets are a different genre (HA5); a receipt head is shared by several
seal-holders (HA3). **Correction: the receipt number stands inside the name, never directly before it (HA6, 0 of 19):
it is a name idiom, not a count.** Moulded tokens count less (HA11). Headed stroke-pair fish names are mostly 740
(HA15 reverse). Other-animal seals: more 520 names, shorter names (HA16, HA17). Copper tablets: never headed, all
Mohenjo-daro (HA20, HA21); small objects carry labels (HA22). Tally 154 held, 233 failed.

## Forty-fifth pass (24 Sept 2026): labels, moulded names, idioms, the heading

Registered first (PREDICTIONS.md, thirty-first set, a05254f78), tested (`predict_test31.py`). **Copper tablets: same
text, same picture in 92% of pairs (I3); no copper text is a seal name (I1, 0 of 139); different openers (I4), fewer
fish (I2): the text names or describes what is pictured.** Moulded name tablets carry 520, the heading, later dates
(I8, I9, I12); receipts are 740 persons without fish (I14). Numeral idioms are whole names or heads (I15, I16). The
heading never changes the ending (I18, 14 of 14); Kalibangan uses it less (I25). Tally 168 held, 244 failed.

## Forty-sixth pass (24 Sept 2026): pictures as outside labels for meaning

Registered first (PREDICTIONS.md, thirty-second set, f084a687c), tested (`predict_test32.py`). **Correction: the
'firm' copper equations of the sign list (341 rhino, 749 / 778 goat, 753 hare) never occur in the copper labels of their
own picture in the ICIT texts (CT5: 0); they came from Parpola's reverse drawings and are withdrawn as text anchors.**
The moulded anchors hold (CT9). Copper labels are picture-specific names (CT1 markers: hare 705 321 235, elephant 923
706, goat 3 421 176 100 790, anthropomorph 61 806 850 900; CT2 one or two texts per picture; CT3 shared final element;
CT22 head before 740 in 34 of 36). Moulded: same text, same picture 95% (CT7). No link across object types (CT6, CT10,
CT14, CT24, CT25 fail). Tally 176 held, 261 failed.

## Forty-seventh pass (24 Sept 2026): picture markers across label genres

Registered first (PREDICTIONS.md, thirty-third set, 3a63231fc), tested (`predict_test33.py`; 1,000 permutations for
PL2, PL12, PL16). The label head depends on the picture on copper (PL1) and moulded tablets (PL11); copper labels of one
picture have one length (PL6), no marker is an animal sign (PL5). **Nothing crosses to seals**: elephant seals never
carry 923 / 706 (PL17), goat seals never the goat markers (PL18), seal animals have no markers (PL15). Parpola's
equations are reverse-side substitutions: 8 of his 10 linked groups pair an image reverse with a single-sign reverse
over the same inscription (PL3). Tally 184 held, 278 failed.

## Forty-eighth pass (24 Sept 2026): labels against names, and the labels' dates

Registered first (PREDICTIONS.md, thirty-fourth set, 5d8261ae3), tested (`predict_test34.py`; LB10 1,000 draws). The
unicorn moulded labels carry a titled 520 fish name (LB11, LB12), but 29 of 39 are one text, '501 405 2 240 520'; the
anthropomorph copper labels all end in 740 (LB17), one text '806 845 61 407 850 900 740': both single-text results.
Label heads are name heads in seal names (LB1, LB2 reverse). Moulded labels share the seal vocabulary, copper labels do
not (LB4). Harappa moulded pictures change over time and were made in batches (LB7, LB9, LB10). Tally 193 held, 294
failed.

## Forty-ninth pass (24 Sept 2026): the core findings, city by city

Registered first (PREDICTIONS.md, thirty-fifth set, 38d6a2fff), tested (`predict_test35.py`). **Robust in both
Mohenjo-daro and Harappa**: the last sign decides the ending (SR1), heads are a small inventory (SR2), human heads take
740 without exception (SR3, 53/53 and 26/26), the head fixes the ending (SR16), affixed fish are attributes (SR8),
tiered numerals write 5-8 (SR10), long strokes count containers (SR11), the number depends on the following sign
(SR12), long numbers open lines (SR20), frequent signs are simpler (SR18). Rule transfer between cities 88.6% / 93.2%
(SR4, just under the bar one way). **Harappa-only**: stroke pair + fish (SR9), tablets varying in numbers (SR13),
longer unicorn texts (SR14), seals avoiding left-to-right (SR19). Too few cases per city: SR5, SR6, SR7, SR15, SR17.
Tally 203 held, 304 failed.

## Fiftieth pass (24 Sept 2026): the core findings beyond the two cities and over time

Registered first (PREDICTIONS.md, thirty-sixth set, b48cd1e3a), tested (`predict_test36.py`). At the other sites
(491 objects) seven of the ten core findings hold (OS1, OS8, OS10, OS11, OS12, OS20, OS18). **The head-to-ending rule
of the two cities does not transfer to them (OS4: 81.2% against an 83.3% baseline)**: the last sign decides the ending
everywhere, but which ending a head takes is local. Unicorn seals carry longer texts at the other sites too (OS14): a
Mohenjo-daro exception, not a Harappa habit. Over time at Mohenjo-daro only the number-sign dependence holds in both
periods (OT12); the others lack power in one. Tally 212 held, 315 failed.

## Fifty-first pass (24 Sept 2026): regional name habits (round 1 of 10)

Registered first (PREDICTIONS.md, thirty-seventh set, f8c01f9fa), tested (`predict_test37.py`, helpers `rtools.py`).
Names look alike across regions (RG1-RG5, RG8-RG10 fail); four Sindh-only heads (RG6) and regional numeral notation
(RG7) hold. Tally 214 held, 323 failed.

## Fifty-second pass (24 Sept 2026): the longest texts (round 2 of 10)

Registered first (thirty-eighth set, d09e1ff3d), tested (`predict_test38.py`; LT6 1,000 shuffles). Long lines hold two
endings more (LT1), numbers more (LT3), recur less (LT7); they are not two attested texts joined (LT6: 0 of 210), not
more titled, not off the seals. Single longer compositions. Tally 217 held, 330 failed.

## Fifty-third pass (24 Sept 2026): Harappa over time (round 3 of 10)

Registered first (thirty-ninth set, dc9014a5d), tested (`predict_test39.py`). Grammar and numbers stable across
Harappa's levels (HT1-HT3); receipts, larger counts and left-to-right writing are earlier, and the heads change (HT5,
HT6, HT9, HT10); the 520 share is stable (HT7). Tally 224 held, 333 failed.

## Fifty-fourth pass (24 Sept 2026): the core in Mahadevan's transcription (round 4 of 10)

Registered first (fortieth set, b28b2cdfb), tested (`predict_test40.py`). Nine of ten core findings replicate on B
alone (number system, affixed fish, head-ending rule, fish variants, number idioms); long lines with two names narrowly
miss (MB8, p = 0.060). Tally 233 held, 334 failed.

## Fifty-fifth pass (24 Sept 2026): repeated and doubled signs (round 5 of 10)

Registered first (forty-first set, cfaa7469f), tested (`predict_test41.py`). Adjacent doubles are deliberate and
non-adjacent repeats inside a name are avoided (DB1, DB6). A doubled sign is not a variant of the single sign (no
alternation, DB4) and doubling is not tied to genre, site or line length; nearly half the doubles are sign 615. Tally
236 held, 341 failed.

## Fifty-sixth pass (24 Sept 2026): sign order inside the name (round 6 of 10)

Registered first (forty-second set, df6bc48ae), tested (`predict_test42.py`). Sign order in name bodies behaves as a
single transitive ranking of slots (5% cyclic triples), identical across transcriptions and cities; names extend to the
left of the head, and the head is best predicted by its neighbour. Individual pairs still vary in order. Tally 244 held,
343 failed.

## Fifty-seventh pass (24 Sept 2026): the slot ranking (round 7 of 10)

Registered first (forty-third set, 57cc9703f), tested (`predict_test43.py`). A one-number rank per sign predicts about
70% of adjacent orders out of sample (A to B, city to city, seals to other objects); the pairwise order is transitive
but not reducible to a scalar position. Rank is stable over body length; inversions sit in one-off names. Tally 247
held, 350 failed.

## Fifty-eighth pass (24 Sept 2026): lines without a name (round 8 of 10)

Registered first (forty-fourth set, 512e3a236), tested (`predict_test44.py`). Lines with no 740/520 are half the corpus
and form their own genre: shorter, numeral-rich, off the seals, commoner at Harappa, rarely ending in a head sign; a
fifth embed an attested name body. Tally 254 held, 353 failed.

## Fifty-ninth pass (24 Sept 2026): names inside the other formulas (round 9 of 10)

Registered first (forty-fifth set, cb47618d7), tested (`predict_test45.py`). Non-name lines are number-first formulas
(numeral first 47% against 24%; numeral + sign in half the 2-sign lines). The names they embed are the common names and
are followed by varied signs (often 845, 151, 156). 400 after a name and 400 in these formulas are separate uses: in
formulas it never follows a name body. Tally 260 held, 357 failed.

## Sixtieth pass (24 Sept 2026): replicating rounds 5-9 (round 10 of 10)

Registered first (forty-sixth set, 6f792f8eb), tested (`predict_test46.py`). Nine of ten findings from rounds 5-9
replicate on held-out data (smaller sites, or Mahadevan's transcription alone): deliberate doubling, no distant repeats,
transitive leftward-growing name order, and the number-first non-name genre. SK7 (inversions in one-off names) does
not. Tally 269 held, 358 failed.

Summary of rounds 1-10 of this loop (sets 37-46, 100 hypotheses): 52 held. What stands up: (1) names are built
leftward from a head in one transitive order of slots, the same in both cities and both transcriptions, though not a
single number per sign; (2) half the lines are a second genre, short number-first formulas off the seals that can cite
a common name without its ending; (3) adjacent doubling is deliberate and mostly one sign (615), and is not a variant
spelling; (4) the core name and number grammar survives on Mahadevan's transcription alone and over time at Harappa.
None of this gives sound values; it is structure, not a reading.

## Sixty-first pass (24 Sept 2026): inside the number-first formulas (loop 2, round 1)

Registered first (forty-seventh set, 74ec8ae5d), tested (`predict_test47.py`). Formulas use the count-token number
grammar (kind set by the next sign, idiomatic value-sign pairs) and 39% recur with only the number changed: tally
entries. Numeral-first is a Harappa and tablet habit. Tally 278 held, 359 failed.

## Sixty-second pass (24 Sept 2026): objects with more than one line (loop 2, round 2)

Registered first (forty-eighth set, 682e78113), tested (`predict_test48.py`). Only 78 intact multi-line objects; where
they exist, a name line tends to pair with a formula (not a count), mostly at Mohenjo-daro, and a numeral tends to sit
in one line only (borderline). Most tests are too thin. Tally 282 held, 365 failed.

## Sixty-third pass (24 Sept 2026): the tally entries (loop 2, round 3)

Registered first (forty-ninth set, 8afb1c4f6), tested (`predict_test49.py`). Two thirds of tally formulas are the known
700 count tokens; the rest (156, 861, 390, 405, 817 390) are single items with their own typical count, spread over
sites. Counts above 4 are rare. Tally 288 held, 369 failed.

## Sixty-fourth pass (24 Sept 2026): numbers on seals against tablets (loop 2, round 4)

Registered first (fiftieth set, b2d090112), tested (`predict_test50.py`). Seal counts are a separate practice: larger,
tiered, headed, in longer formulas that sometimes cite a name, counting other signs (390 with 3-9). Not tied to the
motif and not site-specific among seals. Tally 296 held, 371 failed.

## Sixty-fifth pass (24 Sept 2026): the seal count formulas (loop 2, round 5)

Registered first (fifty-first set, 4b79fb709), tested (`predict_test51.py`). Seal counts count ordinary non-head name
signs (390, 405, 220, 156, 151) across wide value ranges, with no fixed template and mostly the same signs as tablet
counts. Tally 300 held, 377 failed.

## Sixty-sixth pass (24 Sept 2026): where the order is free (loop 2, round 6)

Registered first (fifty-second set, e4aa4d94f), tested (`predict_test52.py`). Order is best modelled by pairwise
precedences (66 against 12 over the scalar rank). Numerals and fish attributes float, mostly inside long names; order
does not depend on the ending or the city. Tally 307 held, 380 failed.

## Sixty-seventh pass (24 Sept 2026): how predictable each genre is (loop 2, round 7)

Registered first (fifty-third set, 67dcbd266), tested (`predict_test53.py`). Reversed expectation: name lines are the
repetitive, closed genre (more repeated pairs, fewer signs, fewer hapaxes); formulas are open and varied. Harappa and
tablet lines are the most repetitive. Tally 309 held, 388 failed.

## Sixty-eighth pass (24 Sept 2026): signs used only in formulas (loop 2, round 8)

Registered first (fifty-fourth set, f23751354), tested (`predict_test54.py`). 173 rare signs never enter names; they
close longer, uncounted formulas, more often on seals than tablets, and the class replicates in B. Tally 314 held, 393
failed.

## Sixty-ninth pass (24 Sept 2026): other endings on seals (loop 2, round 9)

Registered first (fifty-fifth set, 3b5cb5cad), tested (`predict_test55.py`). Some short seal lines are names closed by
something other than 740/520: the post-name signs 400 and 151 without the ending, and three new candidate closers
(527, 156, 154) that follow heads and alternate with the regular endings on 42 bodies. Tally 320 held, 397 failed.

## Seventieth pass (24 Sept 2026): replicating loop 2 (loop 2, round 10)

Registered first (fifty-sixth set, 552c0784d), tested (`predict_test56.py`). Tally formulas, the next-sign rule for
numeral kinds, pairwise precedence, the closed-name/open-formula contrast and the alternative closers replicate on
held-out data; the seal/tablet contrasts cannot be tested at the smaller sites (9 tablet numerals) and FO1 does not
replicate. Tally 326 held, 401 failed.

Summary of loop 2 (sets 47-56, 100 hypotheses): 57 held. What stands up: (1) formulas are tally-like, sharing the
count-token number grammar and recurring with only the number changed; (2) seal counts are a separate practice
(larger, tiered, headed, citing names) but count the same ordinary signs as tablets; (3) name order is a set of
pairwise precedences with numerals and fish attributes floating in long names; (4) names are the closed, repetitive
genre and formulas the open one, with 173 rare formula-only signs; (5) short seal names can close with 400, 151 or a few
other signs in place of 740/520. Still structure only; no sound values.

## Seventy-first pass (24 Sept 2026): the other closers (loop 3, round 1)

Registered first (fifty-seventh set, 0bf150836), tested (`predict_test57.py`). The alternative closers of the
fifty-fifth set do not hold up: with an attested body required, closer lines are mostly one-sign 'X 151' and 'X 156'
pairs, the new closers are not post-name signs, and 400 without an ending is too rare to test. Withdrawn as a finding.
Tally 328 held, 409 failed.

## Seventy-second pass (24 Sept 2026): the fish signs (loop 3, round 2)

Registered first (fifty-eighth set, d51359e6a), tested (`predict_test58.py`). The fish series is name-internal,
stackable (different fish adjacent, no fixed order), often counted, chosen by both neighbours and slightly by city;
fish-final bodies take either ending. Tally 335 held, 412 failed.

## Seventy-third pass (24 Sept 2026): the headings (loop 3, round 3)

Registered first (fifty-ninth set, 7b97bf3db), tested (`predict_test59.py`). 'Heading + 2' is one optional seal-line
unit, independent of city and ending; the three heading signs also occur inside lines (25% of tokens). HD2/HD3 are
confounded by the 2 being a numeral. Tally 341 held, 416 failed.

## Seventy-fourth pass (24 Sept 2026): are rare signs variants? (loop 3, round 4)

Registered first (sixtieth set, c3512b34b), tested (`predict_test60.py`). Frame matching does not identify rare signs as
variants of common ones: the best match is unstable across transcriptions and does not share position or ending. Rare
signs lean to formulas. Tally 345 held, 422 failed.

## Seventy-fifth pass (24 Sept 2026): recurring units inside names (loop 3, round 5)

Registered first (sixty-first set, b5e8d716f), tested (`predict_test61.py`). About a hundred recurring two-sign units
cover 46% of name-body tokens, are shared by both cities, reused across name lengths and often stand alone as names;
many are number + item or fish + item. The inventory is transcription-sensitive (29% carry over to B). Tally 352 held,
425 failed.

## Seventy-sixth pass (24 Sept 2026): sign classes from context (loop 3, round 6)

Registered first (sixty-second set, c647a8825), tested (`predict_test62.py`). Context similarity recovers fish,
numeral, head and look-alike classes as groups; it does not give stable sign-level neighbours across transcriptions
(0.44) or cities (0.39). Tally 357 held, 430 failed.

## Seventy-seventh pass (24 Sept 2026): sign 700 and counted signs (loop 3, round 7)

Registered first (sixty-third set, f99a63df6), tested (`predict_test63.py`). 700 is a count sign only (values 2-4 in
98%), never a name sign; most 'uncounted' 700s are count tokens running the other way ('700 33'), a direction signal
worth using. Most counted signs take several numeral kinds. Tally 360 held, 437 failed.

## Seventy-eighth pass (24 Sept 2026): lines running the other way (loop 3, round 8)

Registered first (sixty-fourth set, e56bf97dc), tested (`predict_test64.py`). Reversed count tokens ('700 33') are a
Harappa moulded-tablet feature (24% of TAB:B counts against 9% of TAB:I), possibly mirror images; names essentially
never run backwards; the catalogue direction field does not mark them. Tally 366 held, 441 failed.

## Seventy-ninth pass (24 Sept 2026): moulded against incised tablets (loop 3, round 9)

Registered first (sixty-fifth set, 6cd622b18), tested (`predict_test65.py`). Moulded tablets are Harappa objects whose
text and picture go together (same text, same picture); otherwise their texts resemble incised ones. The motif field
stores 'None' as a string: fixed here; earlier sets reading it need an audit.

## Eightieth pass (24 Sept 2026): replicating loop 3 (loop 3, round 10)

Registered first (sixty-sixth set, 89d874502), tested (`predict_test66.py`). The fish series, the two-sign units and
text-picture pairing replicate on held-out data; the optional heading, headed seals at the smaller sites and reversed
count tokens (none in A) do not. Tally 377 held, 450 failed.

Summary of loop 3 (sets 57-66, 100 hypotheses): 51 held. What stands up: (1) the fish series is a stackable,
context-chosen, often counted set of name qualifiers; (2) names are largely built from about a hundred recurring
two-sign units, many standing alone as short names; (3) context recovers broad sign classes (fish, numerals, heads,
look-alikes), not sign-level identities, and rare signs cannot be matched to common ones; (4) 700 is a count sign
only, values 2-4; (5) on tablets the text goes with the picture, on moulded and incised alike. Withdrawn or weakened:
the alternative closers of the fifty-fifth set, and the reversed count tokens as an object feature. A motif-field bug
('None' read as a motif) was found and fixed in the sixty-fifth set; earlier sets need an audit. Still structure
only; no sound values.

## Eighty-first pass (24 Sept 2026): seal text and seal picture

Registered first (sixty-seventh set, 3a3c0532e), tested (`predict_test67.py`). On seals the picture is nearly
independent of the name (no motif-specific signs, no within-city head effect), but a text shared by a seal and a tablet
keeps the same picture on both (p = 0.006). Tally 381 held, 456 failed.

## Eighty-second pass (24 Sept 2026): tablets that copy seal texts

Registered first (sixty-eighth set, 52779dd3d), tested (`predict_test68.py`). Most tablet lines matching seal lines are
the count tokens 33 700 and 34 700 and a few short Harappa names; tablets do not in general reproduce seals. Matches
are local (same site). Tally 386 held, 461 failed.

## Eighty-third pass (24 Sept 2026): twenty hypotheses on names as names

Registered first (sixty-ninth set, 7d77b5ab7), tested (`predict_test69.py`). The names behave like a local stock of
personal names: 81% one-off, one-offs built from stock units, repeats short, names and repeated seal texts tied to one
site, cited names local to the citing formula. 'A name ending in a name' is not a local family link. Harappa names are
shorter, with fewer numerals and slightly more 520; counted fish are mostly 2; unicorn seals carry pure names more
often. Tally 399 held, 468 failed.

## Eighty-fourth pass (24 Sept 2026): the local name stocks

Registered first (seventieth set, b6cb4a74f), tested (`predict_test70.py`). 520 names are fish names (74% against 37%
of 740 names). One-off names pair a rare first element with a common head, draw on their own city's units, and live on
seals; repeated names are short and off the seals, especially at Harappa. Closing pairs are shared between the cities
more than opening pairs. Tally 411 held, 476 failed.

## Eighty-fifth pass (24 Sept 2026): why 520 goes with fish

Registered first (seventy-first set, 00fe0d73d), tested (`predict_test71.py`). 520 is mainly the ending of fish-headed
names (the effect does not survive stratifying by head); among fish heads 220, 240 and 233 lean 520 and 222 always
takes 740. Unregistered lead: stroke 2 + fish -> 520 (31 of 34) against stroke 3 + fish -> 740 (9 of 11), to be tested
on distinct names. The link holds in B, at Harappa and at Mohenjo-daro, not at the small sites. Tally 423 held, 484
failed.

## Eighty-sixth pass (24 Sept 2026): does the ending agree with the number?

Registered first (seventy-second set, 12f1bda22), tested (`predict_test72.py`). No: over distinct names the 2+fish ->
520 / 3+fish -> 740 lead disappears (29 counted fish names; 6 of 9 against 7 of 17), and the value before any head does
not set the ending. The lead was an artefact of repeated seals. The sign before a non-fish head adds a little to the
ending (0.034 bits). Tally 425 held, 502 failed.

Post-test check (not registered): on distinct names the fish-520 link stands, 115 of 163 distinct 520 names contain a fish against 371 of 926 distinct 740 names (71% against 40%, p < 1e-12), and 67 of 163 are fish-headed against 45 of 926.

## Eighty-seventh pass (24 Sept 2026): the findings recounted on distinct texts

Registered first (seventy-third set, 509839418), tested (`predict_test73.py`). Sixteen of twenty findings survive
counting each line and name once, including the whole core and the fish-head/ending rule. Repeat-inflated and now
unconfirmed: 520 avoiding 400 (EF17), tally recurrence (FI5), larger seal values (SC1), 520 on fewer unicorns (EF19);
the Harappa numeral-first effect shrinks from +26.5 to +5.9 points. Tally 441 held, 506 failed.

## Eighty-eighth pass (24 Sept 2026): heads as roles, openers as persons

Registered first (seventy-fourth set, efbc411ca), tested on distinct names (`predict_test74.py`). Names split into a
shared head (few types, at both cities, kept in long names, carrying the ending, which depends on its shape category;
fish heads take 520) and a more local, more varied opener that does not affect the ending. Openers are not unique to
single names, so the opener is not simply a personal name. Tally 453 held, 514 failed.

## Eighty-ninth pass (24 Sept 2026): how the name is put together

Registered first (seventy-fifth set, 445ccf781), tested on distinct names (`predict_test75.py`). Names are right-
branching, [opener [middle head]]: the middle binds to the head, (middle, head) and the last two of four signs form
attested names, and numerals stand before the head. The common heads are the counted things of the formulas and stand
alone as names. Locality does not separate opener from head (both local), and motifs track neither. Tally 462 held,
525 failed.

## Ninetieth pass (24 Sept 2026): the name as a noun phrase

Registered first (seventy-sixth set, 349d56287), tested on distinct names (`predict_test76.py`). The head selects both
its modifier (by shape category) and its number (replicated in B, Harappa, Mohenjo-daro); the number tends to stand
before a modifier ([N [mod head]]). Names and formulas do not share counting conventions, and 'heads are the counted
things of the formulas' reduces to frequency. Tally 470 held, 537 failed.

## Ninety-first pass (24 Sept 2026): numbers in names, and two systems

Registered first (seventy-seventh set, 83f3a4f89), tested on distinct names and lines (`predict_test77.py`). Numbers in
names are real, varied counts, not fixed name parts. 'N [mod head]' with an attested [mod head] name is common, often
'N [fish head]'. Names and formulas are two systems over one sign set: fewer shared pairs than chance, different
neighbours for the same sign, the counted item closes formulas only. Tally 479 held, 548 failed.

## Ninety-second pass (24 Sept 2026): the grammar of the formulas

Registered first (seventy-eighth set, b445293c9), tested on distinct lines (`predict_test78.py`). Formulas read as
[header] [N item] ([N item]): the header (a name in 23%) selects the item, the item sets the count, a header takes
several items, two-count formulas list different items, and headers are commoner on seals. Items are somewhat more
often formula-only signs. Tally 491 held, 556 failed.

## Ninety-third pass (24 Sept 2026): formulas as records

Registered first (seventy-ninth set, 0871bb2d9), tested on distinct lines (`predict_test79.py`). The record reading
fails: 'name headers' are single signs that are also 1-sign names, not seal owners, and entries do not recur. Kept:
headers are short, numeral-first formulas are a Harappa form, and the cities count different items. Tally 495 held,
572 failed.

## Ninety-fourth pass (24 Sept 2026): case or class?

Registered first (eightieth set, 458c296cd), tested on distinct lines and names (`predict_test80.py`). The ending is a
class of the head, like grammatical gender: fixed per head in both cities and both transcriptions, with no concord and
no change by object, city, heading or counting. The 520 class is fish plus a few other heads (1, 175, 382, 70, 33, 72).
Post-name signs 90 and 151 attach only to 740 (740 90 x69, 520 90 x0). Names cited in formulas lean 520. Tally 506
held, 581 failed.

## Ninety-fifth pass (24 Sept 2026): what the two classes are

Registered first (eighty-first set, 3a3228581), tested on distinct names and lines (`predict_test81.py`). The 520 class
= fish heads, the numerals 1 and 33 ('N 520', as if 520 were counted) and 175, 382, 70, 72; it takes fish modifiers
even on non-fish heads (A + B and B). Classes agree 47 of 47 with F. After 740, 90 and 400 are each selected by their
own set of heads (Jaccard 0.13). Tally 516 held, 591 failed.

## Ninety-sixth pass (24 Sept 2026): counted 520 and the suffixes

Registered first (eighty-second set, 3be2cf466), tested on distinct lines (`predict_test82.py`). 'N 520' is the fixed
phrase '705/706 33 520' (46 of 55), not counted 520. After the ending: 400 is the Harappa tablet suffix; 90 (with its
look-alike 151) is the seal suffix of one-off names; each head takes one of them, chosen by the head's shape category.
Tally 529 held, 598 failed.

## Ninety-seventh pass (24 Sept 2026): what the suffixes do

Registered first (eighty-third set, e63a28acb), tested (`predict_test83.py`). 400 marks an early Harappa incised-tablet
entry, usually without a picture, added to names that also occur bare (often on seals), but not linked to local seal
owners. 90 is not a clear owner mark; its seal bias is a city pattern. Tally 538 held, 609 failed.

## Ninety-eighth pass (24 Sept 2026): how the writing changed at Harappa

Registered first (eighty-fourth set, 11b0ef33f), tested (`predict_test84.py`). Later Harappa texts are longer, more
often headed, less often receipts (400), and on seals and moulded tablets rather than incised tablets; the grammar
(genres, classes, numerals, 520 share) is stable across the periods. Tally 547 held, 620 failed.

## Ninety-ninth pass (24 Sept 2026): one grammar, two cities

Registered first (eighty-fifth set, ec4c83c16), tested within each city (`predict_test85.py`). Every core rule holds
separately at Mohenjo-daro and at Harappa (classes, right-branching, tiered 5-8, sign-set numeral kind, fish-520, pair
order). Local style: Mohenjo-daro longer, headed names; Harappa suffixed receipts and more formulas, different counted
items and some different common heads. Tally 563 held, 624 failed.

## Hundredth pass (24 Sept 2026): recent findings on held-out data

Registered first (eighty-sixth set, 187d09005), tested (`predict_test86.py`). The number system holds at the smaller
sites; the name grammar (fish-520, classes, right-branching, common heads) does not show there. In B and the fuller
corpus the name findings hold; FG3 (header selects item) and the N-mod-head order are not confirmed in F.

Summary of sets 84-86: Harappa's writing lengthens and moves to seals and moulded tablets over time with its grammar
unchanged; Mohenjo-daro and Harappa share one grammar with different local styles; the smaller sites share the
numerals but not the name system. Tally 575 held, 632 failed.

## Hundred-and-first pass (24 Sept 2026): regional name systems

Registered first (eighty-seventh set, e720f92c5), tested (`predict_test87.py`). No regional name system: Gujarat,
Kalibangan and Chanhu-daro use the city heads at city rates, the cities' units, and no region predicts head, ending or
formula opening. The eighty-sixth set's small-site failures are read as too little data. Gujarat writes more formulas.
Tally 579 held, 648 failed.

## Hundred-and-second pass (24 Sept 2026): lines with two names

Registered first (eighty-eighth set, 2d9dfe0d0), tested (`predict_test88.py`). Two-ending lines are rare (23 distinct,
nearly all Mohenjo-daro) and do not split into two names: the first part is rarely a name, never suffixed or headed.
A medial 740/520 is read as part of a long compound name. Tally 582 held, 665 failed.

## Hundred-and-third pass (24 Sept 2026): the three heading signs

Registered first (eighty-ninth set, 6b556222f), tested (`predict_test89.py`). 817, 820 and 861 are interchangeable in
front of the same names and are not chosen by name, city or object; they differ in the stroke sign that follows (817
and 861: 2 or 368; 820: 2, 60 or 1). Headed names are shorter, repeat more, and are suffixed less; the heading unit
stands in for part of the name. 861 heads formulas more. Tally 590 held, 677 failed.

Summary of sets 87-89: no regional name systems (small sites share the city stock); lines with two endings are long
single names, not pairs; the three heading signs are variants of one heading slot.

## Hundred-and-fourth pass (24 Sept 2026): the minor media

Registered first (ninetieth set, e629b0fbc), tested (`predict_test90.py`). Each medium has its own text type: copper
tablets are Mohenjo-daro fixed labels, not names or seal texts; bangles carry short formulas; graffiti are short and
varied. Stamped pots and tags do not match surviving seals. 520 names are twice as common on seals as on other media.
Tally 602 held, 685 failed.

## Hundred-and-fifth pass (24 Sept 2026): endings in mid-line

Registered first (ninety-first set, c892aece9), tested (`predict_test91.py`). A mid-line 740 usually closes a short
real name ('176 740', '220 740'), followed by a 1-3 sign tail that is not a name (often a numeral or a fixed sign),
mostly on one-off seals. Revises the eighty-eighth set's 'long compound' reading to 'name + annotation'. Tally 612 held,
695 failed.

## Hundred-and-sixth pass (24 Sept 2026): the jar signs 700, 705, 706

Registered first (ninety-second set, 352a3ee87), tested (`predict_test92.py`). 705 and 706 are free variants of one
sign, bound to a following long 33 (95%; 75% of 33s follow them): '705/706 33' is a fixed unit, with 520 only after
value 3. It is not related to the count sign 700. Seal texts, commoner at Mohenjo-daro.

Summary of sets 90-92: each medium has its own text type (copper tablets fixed labels; 520 a seal-name feature); a
mid-line 740 closes a short name followed by an annotation; '705/706 33' is a fixed unit, not a jar count. Tally 623
held, 704 failed.

## Hundred-and-seventh pass (24 Sept 2026): frozen numbers and real counts

Registered first (ninety-third set, 4cb5c2b4d), tested (`predict_test93.py`). Only 4 of 66 counted signs have a fixed
number (236 = 2, 632 = 2, 717 = 2, 923 = 3), all Mohenjo-daro, long-stroke, stable in B; the rest, including 700, are
real variable counts. Tally 627 held, 720 failed.

## Hundred-and-eighth pass (24 Sept 2026): copper tablets and their pictures

Registered first (ninety-fourth set, 56e46b01d), tested (`predict_test94.py`). Copper tablet texts are labels for their
pictures: each picture has a dominant text (anthropomorph 10 of 10, hare 12 of 12), and the picture predicts text,
length and last sign. Copper labels count with long strokes, are never headed and write differently from seals while
using the same signs. Both fixed labels contain 845 and 407; the hare label contains '705 33'. Tally 640 held, 727 failed.

## Hundred-and-ninth pass (24 Sept 2026): the single stroke '1'

Registered first (ninety-fifth set, 9e534130c), tested (`predict_test95.py`). '1' is an ordinary count except in two
places: after an ending, where it opens a short line-final tail (21 cases, never '2' or '3'), and after the heading
820 (the only heading that takes it). The post-ending use is rare in Mahadevan's transcription.

Summary of sets 93-95: counts are real (only 4 frozen number-sign pairs); copper tablets carry fixed labels matched to
their pictures (anthropomorph and hare labels share 845 and 407); '1' has two special slots. Tally 647 held, 740
failed.

## Hundred-and-tenth pass (24 Sept 2026): how the copper labels are built

Registered first (ninety-sixth set, d72a49420), tested (`predict_test96.py`). Copper labels form their own vocabulary
(82% of 845 and 61% of 407 are on copper) and almost never appear on seals; labels are copied whole per picture and
'845 ... 407' marks animal/figure labels. Caveat: F name counts include copper labels, which inflated a few 'common
names' in earlier sets (503 615 752 740 x28 is copper only). Tally 655 held, 752 failed.

## Hundred-and-eleventh pass (24 Sept 2026): the name findings without copper tablets

Registered first (ninety-seventh set, e196b1108), tested (`predict_test97.py`). Eighteen of twenty F-based name
findings survive removing copper tablets; AM10 (Harappa prefers 520) does not and is withdrawn, and the Mohenjo-daro
fixed-class share is 79% (just under 80%). Tally 673 held, 754 failed.

## Hundred-and-twelfth pass (24 Sept 2026): picture labels across media

Registered first (ninety-eighth set, 7b88589fd), tested (`predict_test98.py`). The text-picture link is real within
each medium (copper, moulded, incised) but does not carry across media: the same picture gets different texts on
copper and on moulded tablets. 845 is essentially a copper word; 407 also ends seal lines.

Summary of sets 96-98: copper labels are a separate vocabulary (845, 407, fixed units like '3 42x'); removing copper
leaves the name findings intact (AM10 withdrawn); picture labels are medium-specific. Tally 683 held, 764 failed.

## Hundred-and-thirteenth pass (24 Sept 2026): position specialists

Registered first (ninety-ninth set, 1fea03ca4), tested (`predict_test99.py`). 7 opener signs (heading-type, followed
by numerals, on seals) and 14 closer signs (740, 520, 400 and a set of formula/tail closers 151, 154, 156, 527, 565,
621, 679) hold their positions in both transcriptions and both cities (93%, 90%). Tally 692 held, 775 failed.

## Hundred-and-fourteenth pass (24 Sept 2026): variant forms of one sign

Registered first (hundredth set, 48a85973a), tested (`predict_test100.py`). Catalogue neighbours (shape families) share
contexts in A + B, B and F; candidate same-sign pairs 435/436, 526/527, 336/337, 554/555, 705/706. They are not split by
city or period, so they are free variants, not regional spellings. Mohenjo-daro has 13 signs unseen at Harappa. B
merges 57 of A's signs, a caveat for B replications. Tally 700 held, 787 failed.

## Hundred-and-fifteenth pass (24 Sept 2026): recent findings on held-out data

Registered first (hundred-and-first set, d8e23cd31), tested (`predict_test101.py`). Twelve of fourteen F' tests of the
medial-ending, heading, '1', opener, jar, frozen-count and shape-family findings replicate; not 861-formulas (HS4)
and openers-on-seals (PZ12), now unconfirmed. B tests are mostly degenerate because B merges or lacks the signs
involved (no 817, 705 = 706).

Summary of sets 99-101: 7 opener and 14 closer signs hold their places everywhere; catalogue shape families share
function and give 5 candidate free-variant pairs; the recent findings replicate on the fuller corpus. Tally 715 held,
792 failed.

## Hundred-and-sixteenth pass (24 Sept 2026): shape blocks and what they do

Registered first (hundred-and-second set, b0b9de0e7), tested (`predict_test102.py`). Shape families (catalogue blocks)
weakly predict genre, counting, class, ending, medium and city; block 1 is a head block, block 3 a formula block, and
same-family signs cluster side by side. Position is not set by family. Tally 726 held, 801 failed.

## Hundred-and-seventeenth pass (24 Sept 2026): the formula closers

Registered first (hundred-and-third set, 64c4a157f), tested (`predict_test103.py`). Lines ending in one of 11 closer
signs are a second family of seal inscriptions, mostly Mohenjo-daro: no 740/520, longer than formulas, a name-head
sign before the closer in two thirds, each closer with its own heads, one closer per line. Partly restores the
alternative-closer idea of the fifty-fifth set. Tally 737 held, 810 failed.

## Hundred-and-eighteenth pass (24 Sept 2026): line templates

Registered first (hundred-and-fourth set, 3ff7b1716), tested (`predict_test104.py`). About half of all distinct lines
follow ten role templates (X, XE, XNX, NX, XNXE, HNXE, XC, XES, HNX, XN), the same in A and B; templates vary with
medium, city and Harappa period, with the widest range on seals and at Mohenjo-daro.

Summary of sets 102-104: shape families weakly predict use (block 1 heads, block 3 formulas); lines ending in a closer
are a second seal-inscription family at Mohenjo-daro; ten role templates cover half the corpus. Tally 746 held, 821
failed.

## Hundred-and-nineteenth pass (24 Sept 2026): closer against name inscriptions

Registered first (hundred-and-fifth set, 08a088f8a), tested (`predict_test105.py`). Closer inscriptions share the
seals, animals, openers and heads (740 side) of name inscriptions, but their bodies are shorter, rarely attested
names, less unit-built and less fishy; each closer selects its own heads and openers. They are a seal type at both
cities (19-20% of seal inscriptions), not a Mohenjo-daro speciality. Tally 759 held, 828 failed.

## Hundred-and-twentieth pass (24 Sept 2026): bare lines

Registered first (hundred-and-sixth set, 656e720a2), tested (`predict_test106.py`). Bare lines (no role signs) are short
name-shaped sequences (opener ... head) that are not attested names, on tablets and potsherds, somewhat Harappan, and
rich in formula-only signs: a third, practical genre beside names and counts. Tally 769 held, 838 failed.

## Hundred-and-twenty-first pass (24 Sept 2026): sets 102-106 on held-out data

Registered first (hundred-and-seventh set, dea9bde3b), tested (`predict_test107.py`). All twenty replications held on
the fuller corpus without copper, the smaller sites and B: shape blocks (1 heads, 3 formulas, clustering), the closer
inscriptions (a quarter of small-site seal inscriptions too), line templates, and bare name-shaped lines.

Summary of sets 105-107: seal inscriptions come in two sister types, name + 740/520 and name-like body + closer (740
side of the head inventory, fewer fish), at every site; bare name-shaped lines without any role sign form a practical
third genre on tablets and pots. Tally 789 held, 838 failed.

## Hundred-and-twenty-second pass (24 Sept 2026): the four genres as systems

Registered first (hundred-and-eighth set, 9f09dec3f), tested (`predict_test108.py`). The genres share one vocabulary
(only 15% of common signs are genre-bound, mostly name signs) and are defined by their frames: the last sign predicts
the genre far better than the first. Object and city shift the mix only slightly. Tally 796 held, 851 failed.

## Hundred-and-twenty-third pass (24 Sept 2026): the bare-line closers

Registered first (hundred-and-ninth set, 86fc334b7), tested (`predict_test109.py`). No single closer class: 368 is a
seal sign that also fills the heading slot (after 817/861), 390 a seal sign counted 3+, 615 the doubled sign, and bare
400 a different sign-use from post-name 400 (disjoint predecessors). Tally 804 held, 863 failed.

## Hundred-and-twenty-fourth pass (24 Sept 2026): sets 108-109 on held-out data

Registered first (hundred-and-tenth set, 10b965156), tested (`predict_test110.py`). Eighteen of twenty replications
held across F', B and the smaller sites: genres share a vocabulary and are defined by their last sign; 368, 390, 615 and
the two 400s keep their separate uses.

Summary of sets 108-110: the four genres are frames on one shared vocabulary, recognised by their closing sign; the
signs that close bare lines each have a distinct job (368 heading-slot and seal sign, 390 a high-count seal sign, 615 the
doubled sign), and 400 has two unrelated uses. Tally 822 held, 865 failed.

## Hundred-and-twenty-fifth pass (24 Sept 2026): one sign, many genres

Registered first (hundred-and-eleventh set, 63b81bee3), tested (`predict_test111.py`). Signs keep their position,
company, units, numeral kind and typical count across names, counts and closer lines (replicated in B and F'). Names and
counts are two uses of one sign language, not two codes; the seventy-seventh set's 'two systems' is qualified. Tally 839
held, 868 failed.

## Hundred-and-twenty-sixth pass (24 Sept 2026): the number system across genres

Registered first (hundred-and-twelfth set, 1c3925f7f), tested (`predict_test112.py`). One number system for all genres:
tiered 5-8 everywhere, the same signs and notation; values differ slightly (counts larger, seal counts more tiered). 2
is the commonest value; the value-12 peak is one sign (55). Compound-order tests were confounded by the heading '2'.
Tally 852 held, 875 failed.

## Hundred-and-twenty-seventh pass (24 Sept 2026): sets 111-112 on held-out data

Registered first (hundred-and-thirteenth set, 3ac04923f), tested (`predict_test113.py`). Signs keep position and
company across genres in F', B and the smaller sites; the number system is one across genres; a sign's typical count
carries over in B but not in F'. Two-sign numeral runs put the smaller value first even without headings (an open
question whether that first stroke is a numeral).

Summary of sets 111-113: the script is one sign language used in several text frames: each sign keeps its position,
company, units and numeral notation across names, counts, closer and bare lines, and one number system serves them all.
Tally 869 held, 878 failed.

## Hundred-and-twenty-eighth pass (24 Sept 2026): small-then-large numeral runs

Registered first (hundred-and-fourteenth set, d2dd55e39), tested (`predict_test114.py`). The '2' in '2 N X' is a prefix,
not an addend (X's usual count equals N 27 times, N + 2 never); it acts like the heading unit's '2' without the heading
sign, on seals, counting 220 and 390 mostly. So 'small-then-large' runs are not compound numbers. Tally 880 held, 887
failed.

## Hundred-and-twenty-ninth pass (24 Sept 2026): structural predictions of published proposals

Registered first (hundred-and-fifteenth set, 9920848a3), tested (`predict_test115.py`). Parpola's six/seven-fish
pattern does not appear (fish are counted 2 mostly), though fish variants behave as distinct words in personal names;
740 behaves as a suffix with 400/90/151 stacking after it (Mahadevan, Parpola); Farmer et al.'s singletons, short texts
and low repetition hold but fit name texts too; language-like predictability holds only partly. Caveat: authors' views
summarised from memory, and the ICIT sign numbering may differ from theirs. Tally 891 held, 896 failed.

## Hundred-and-thirtieth pass (24 Sept 2026): sets 114-115 on held-out data

Registered first (hundred-and-sixteenth set, fafc35587), tested (`predict_test116.py`). Nineteen of twenty replicate: the
'2' prefix is not part of the count in F', B and the smaller sites; fish-variant minimal pairs, 740 as a suffix, low
repetition, Zipf-like frequencies and one-off numeral + fish names hold on held-out data.

Summary of sets 114-116: 'small-then-large' numeral runs are a '2' prefix (the heading '2' without its heading sign)
before a real count; published structural claims split: 740-as-suffix and fish variants as distinct words fit, the
six/seven-fish pattern does not, and the statistics fit both linguistic and non-linguistic views. Tally 910 held, 897
failed.

## Hundred-and-thirty-first pass (24 Sept 2026): the lines no genre claims (loop start)

Registered first (hundred-and-seventeenth set, 4e862aee8), tested (`predict_test117.py`). Start of a self-directed
test-learn-propose loop. The 'other' lines are names with tails, bare lines with a fish, closer lines with tails and
headed words; only 3 lines of 2,722 remain unassigned. Lead: closers take the 400 suffix like 740 (25 of 31 closer
tails), so closers may be endings. Tally 919 held, 903 failed.

## Hundred-and-thirty-second pass (24 Sept 2026): are the closers endings?

Registered first (hundred-and-eighteenth set, dcd7ea8af), tested (`predict_test118.py`). Yes: closers alternate with
740 on the same bodies (40), heads split between 740 and closers (Spearman 0.79), closers take 400 at 740's rate (as a
Harappa tablet form), and 90 never follows them. They either replace 740 or stack after it ('740 + closer', 34 lines).
Revised model: name body + ending, where the ending slot holds 740, 520 or one of 11 closers, optionally followed by 400
(or, after 740 only, 90). Tally 932 held, 905 failed.

## Hundred-and-thirty-third pass (24 Sept 2026): the ending slot as a paradigm

Registered first (hundred-and-nineteenth set, 66d2af39c), tested (`predict_test119.py`). The ending slot is a paradigm
chosen by the head: 740, 520, a closer, or 740 + one of six stacking closers (151, 161, 527, 565, 621, 679); fixed
order, no second suffix after a stack, 26 bodies with 3+ fillers. Tally 941 held, 911 failed.

## Hundred-and-thirty-fourth pass (24 Sept 2026): two kinds of closer

Registered first (hundred-and-twentieth set, f7ec29b80), tested (`predict_test120.py`). No second class: stacking and
plain closers differ only in whether they may follow 740 (and plain ones take 400 slightly more). The ending-slot thread
is close to exhausted; next targets: what separates the 740 and 520 classes beyond fish, and sign choice inside slots.
Tally 944 held, 923 failed.

## Hundred-and-thirty-fifth pass (24 Sept 2026): what else marks the 520 class

Registered first (hundred-and-twenty-first set, 2e6dc3370), tested (`predict_test121.py`). No contextual cue beyond the
head predicts the 520 class; class is lexical, per head. 90 never follows 520 anywhere; 520 names are dominated by a few
repeated names. This line of questioning is exhausted on internal evidence. Tally 948 held, 931 failed.

## Hundred-and-thirty-sixth pass (24 Sept 2026): the model as a predictor

Registered first (hundred-and-twenty-second set, be1ccb443), tested (`predict_test122.py`). On held-out lines: heads
and openers are a nearly closed inventory (95%, 88% seen), the head predicts the ending 90% (but the 740 base rate is
~85%), the last sign predicts the genre 77%, bigrams save 1.8 bits per sign and trigrams a further 0.6. These are the
benchmark numbers for any future model. Tally 960 held, 934 failed.

## Hundred-and-thirty-seventh pass (24 Sept 2026): does structure improve prediction?

Registered first (hundred-and-twenty-third set, 35326462e), tested (`predict_test123.py`). Yes: role classes cut held-out
cross-entropy by 0.5 bits per sign, genre by 0.2, and position alone beats the bigram (5.43 against 6.38). The cities'
sequences differ only slightly (0.14 bits). BM4 (direction) was ill-posed for a bigram. Tally 967 held, 939 failed.

## Hundred-and-thirty-eighth pass (24 Sept 2026): one combined model

Registered first (hundred-and-twenty-fourth set, 2b9d6a5b8), tested (`predict_test124.py`). Benchmark model: position
in the line + two-sign context = 4.92 bits per sign held-out (5.69 on new F lines; unigram 8.21, bigram 6.38). Role
classes and genre add nothing once position and context are included: the structural rules are largely positional and
local. Tally 972 held, 944 failed.

## Hundred-and-thirty-ninth pass (24 Sept 2026): beating the benchmark

Registered first (hundred-and-twenty-fifth set, bb3eaea13), tested (`predict_test125.py`). Lines are anchored at their
end (distance from the end predicts 0.57 bits better than from the start); shape blocks predict unseen signs (new lines
5.69 to 5.44 bits). Better smoothing gives a new benchmark of 4.66 bits per sign. Length, first sign and finer positions
add nothing. Tally 978 held, 948 failed.

## Hundred-and-fortieth pass (24 Sept 2026): is the line composed from the end?

Registered first (hundred-and-twenty-sixth set, d314a7a01), tested (`predict_test126.py`). The end anchoring is the ending
(last-position entropy 1.4 bits in names) plus the head-ending pair selecting the modifier; no backward generative
advantage overall. Nothing new beyond the right-branching name structure. Tally 982 held, 953 failed.

## Hundred-and-forty-first pass (24 Sept 2026): the rare signs

Registered first (hundred-and-twenty-seventh set, a9efeb530), tested (`predict_test127.py`). Rare signs fill the frames
of common signs from their own catalogue block and neighbourhood (weak support for family variants or compounds; not
in B) and sit in longer lines; otherwise they behave like common signs. Tally 985 held, 960 failed.

## Hundred-and-forty-second pass (24 Sept 2026): forbidden pairs and a family grammar

Registered first (hundred-and-twenty-eighth set, 7dc3d2db3), tested (`predict_test128.py`). 20 expected-but-absent pairs
(17x chance), e.g. fish never directly before 390 or 400, 415 never before 740; a quarter of common signs never precede
740. Shape families carry only 5% of the order information: sequencing is sign-specific. Tally 990 held, 965 failed.

## Hundred-and-forty-third pass (24 Sept 2026): the strong pairs as compounds

Registered first (hundred-and-twenty-ninth set, 48756472d), tested (`predict_test129.py`). The strong pairs are loose,
chaining collocations shared across genres, cities and transcriptions, not fixed two-sign words (order not rigid, weak
dependency, under half are units). Tally 996 held, 969 failed.

## Hundred-and-forty-fourth pass (24 Sept 2026): material and size

Registered first (hundred-and-thirtieth set, 92f1530f5), tested (`predict_test130.py`). New physical variables: seal
size tracks text length (0.42), headed seals are bigger and closer seals smaller, later Harappa seals are bigger
(23 to 30 mm); moulded tablets are faience, faience texts are short, and 520 names are a steatite (seal) feature.
Field 31 read as size by inference. Tally 1005 held, 972 failed.

## Hundred-and-forty-fifth pass (24 Sept 2026): size beyond text length, and seal shapes

Registered first (hundred-and-thirty-first set, 7c59f3fba), tested (`predict_test131.py`). Headed/closer size effects
were text length; later Harappa seals are bigger in their own right (+6.7 mm). Rectangular seals are a separate kind:
pictureless (96%), more counting, more Harappan. Tally 1013 held, 976 failed.

## Hundred-and-forty-sixth pass (24 Sept 2026): the rectangular seals

Registered first (hundred-and-thirty-second set, f7f0f4e15), tested (`predict_test132.py`). Rectangular seals are
pictureless steatite seals with fewer names, fewer 520 names and more formula words, but no different in date, region,
heading or repetition. Tally 1018 held, 983 failed.

## Hundred-and-forty-seventh pass (24 Sept 2026): the physical findings within each city

Registered first (hundred-and-thirty-third set, 6999d0408), tested (`predict_test133.py`). Size-length, pictureless
rectangular seals, faience moulds and short faience texts hold in each city; the 520-steatite link is a copper-label
effect (absent at Harappa). Tally 1027 held, 984 failed.

## Hundred-and-forty-eighth pass (24 Sept 2026): our genres against ICIT's text codes

Registered first (hundred-and-thirty-fourth set, 19fddf009), tested (`predict_test134.py`). Our genres agree with ICIT's
independent text codes (VN = counts 95%, LP/IT/SP/MT = names 78%, SC = bare lines); the closer inscriptions are new,
not an ICIT category. Tally 1037 held, 984 failed.

## Audit (24 Sept 2026): the motif-field 'None' bug in sets 17-40

The ICIT motif field stores 'None' where no motif is recorded (found in the sixty-fifth set; 1,677 of the 3,681 clean
F objects). Audit of the earlier readers (`predict_test17`, 18, 21, 24, 27, 29, 30, 31, 34, 35, 36 `make_tests`, 39,
40): each already excluded 'None' and '-' wherever having a motif mattered, and otherwise only tested for Bull1. Rerun
with the same seeds and 'None' mapped to no motif: output identical to the unpatched run in all twelve, and to the
recorded results except one unrelated permutation p-value (twenty-seventh set L16, 0.0001 to 0.0002, still holds). No
verdict changes; the scripts now carry the explicit check. Tally unchanged: 1037 held, 984 failed.

## Hundred-and-forty-ninth pass (24 Sept 2026): does a proposed reading respect the structure?

Registered first (hundred-and-thirty-fifth set, 277f25082), tested (`predict_test135.py`); cross-reference values
('ref:...') excluded after a first run mistook them for readings. The readings stored in the ICIT dump (source not
identified) are a consistent sign-by-sign phonetic substitution (1.8 letters per sign; first sign fixes first letter),
but they give 740 no fixed sound, which conflicts with 740's rigid suffix behaviour. Consistency check only. Tally 1045
held, 986 failed.

## Loop end (24 Sept 2026): saturation of internal hypothesis testing

Self-directed test-learn-propose loop, sets 117-135 (224 hypotheses). What it added: (1) the 'other' lines are
extensions of the known genres (3 of 2,722 unassigned); (2) the closers are endings, alternating with 740 on the same
bodies, taking 400, stacking after 740 in a fixed order, so the ending slot is a head-chosen paradigm; (3) held-out
benchmarks (heads 95% known, head predicts ending 90% against an 85% base rate, 4.66 bits per sign with position +
context; roles add nothing once position and context are in; lines anchored at their end; shape blocks help unseen
signs); (4) forbidden sign pairs at 17x chance, with order sign-specific rather than family-level; (5) physical side:
seal size tracks text length, later Harappa seals are bigger at equal length, rectangular seals are a pictureless
steatite type, moulded tablets are faience; (6) our genres agree with ICIT's independent text codes, the closer
inscriptions being new; (7) the Sanskrit-based readings stored in the dump are a consistent sign-by-sign substitution
that gives 740 no fixed sound. Why stop: the last rounds on each thread returned nulls or replications (sets 120,
121, 126, 127, 129, 133); the 520 class is lexical per head with no contextual cue left to test; every record field
with content has now been used; what remains unknown (sound values, meanings, what the counts record) cannot be
reached by further internal hypothesis tests and needs outside evidence (a bilingual, a secure cognate language, or
archaeological context tying texts to contents). Tally 1045 held, 986 failed (2031 registered).

## Hundred-and-fiftieth pass (24 Sept 2026): the West Asian texts against the later grammar

Registered first (hundred-and-thirty-sixth set, 4a48d36ee), tested (`predict_test136.py`). The 18 West Asian lines lack
the ending slot, name units and home openers and score 6.5 bits per sign under the home model, as foreign names should.
New: they are full of stroke signs used inside the line (78% against 56%), hinting at phonetic use of strokes when
spelling foreign names. Tally 1052 held, 989 failed.

## Hundred-and-fifty-first pass (24 Sept 2026): sign shapes

Registered first (hundred-and-thirty-seventh set, e6dab3485), tested (`predict_test137.py`) on font-rendered glyphs.
Catalogue neighbours look alike (the blocks are shape families); the free-variant pairs, the fish and the closers each
form shape families. Shape does not predict use in general, and a pixel containment test finds no compound effect.
Better glyph data (photographs, stroke-level drawings) would be needed for compound analysis. Tally 1057 held, 994 failed.

## Hundred-and-fifty-second pass (24 Sept 2026): Parpola, Mahadevan, Knorozov structural claims

Registered first (hundred-and-thirty-eighth set, 9ceb0d054), tested (`predict_test138.py`) with claims taken from the
OCR text of Parpola 1994. In ICIT's transcription '2 + fish' dominates (113) and '6 + fish' is rare (8), against
Parpola's 'most frequent sequence'; '3 + fish' second and the '7 + fish' seal do hold. The roof fish is a modifier, not
a head. The Soviet-team inflection claims fail as stated. Possible sign-identification difference with Parpola's corpus
noted. Tally 1060 held, 1001 failed.

## Hundred-and-fifty-third pass (24 Sept 2026): a second transcription (Parpola's CISI)

Registered first (hundred-and-thirty-ninth set, d3781d240). The open CISI digitisation (mayig, MIT, M-1 to M-184) was
loaded (`cisi.py`, `data/cisi_mayig.tsv`) and joined to ICIT by CISI number: 157 intact objects. The editions agree on
length (96%), positions (92%) and last signs (98%); the ending paradigm holds in Parpola's numbering (88%). In
Parpola's own transcription of these seals '2 + fish' is the commonest count and '6 + fish' does not occur, so the
set-138 discrepancy is not ICIT's sign identification. Tally 1069 held, 1002 failed.

## Hundred-and-fifty-fourth pass (24 Sept 2026): find spots inside Mohenjo-daro

Registered first (hundred-and-fortieth set, 8a36ae13b). ICIT fields 4 (area) and 5 (block/house, street) were used for
the first time. Text content does not follow find spot: no co-location of same text or same head, no household
vocabulary, no area effect on genre, ending, motif or length. Copper tablets alone cluster by area (VS-A, the citadel
mounds; none in DK-G North). Seals were lost across the city independently of what they say. Tally 1070 held, 1011
failed.

## Hundred-and-fifty-fifth pass (24 Sept 2026): language type from sign order

Registered first (hundred-and-forty-first set, 3ff32f82e). Numerals precede the counted sign (472:106), openers are an
open class, there is no number agreement; there is no preposed genitive, no plural reduplication, no long suffix
chain, and the counted sign is usually a modifier, not the head. Order typology: numeral-first, head-final, no
agreement, short closed ending slot: compatible with Dravidian or Indo-Aryan order, against Sumerian, not separating
the first two. Tally 1074 held, 1017 failed.

## Hundred-and-fifty-sixth pass (24 Sept 2026): line breaks as word boundaries

Registered first (hundred-and-forty-second set, 474c26fb4). On 77 multi-line texts (both line orders), line breaks
never split a bound pair and almost never a name unit; each line is a well-formed text and ends in a marker twice as
often as chance; the second line of a name text is a separate field. The scribes' breaks confirm the statistical
segmentation from outside. Tally 1080 held, 1019 failed. Correction: line breaks were tested before (X2 in
the seventh set, RB, U10, J7 on M77); LK2 replicates X2, and LK1, LK3, LK4, LK6, LK8 are the new parts.

## Hundred-and-fifty-seventh pass (24 Sept 2026): numerals used for their sound

Registered first (hundred-and-forty-third set, b6d0db129). Inside names numerals are lexicalised: the value depends
on the following sign and on role, numerals alternate with lexical signs far more than with other numerals (6% against
a 17% token share; NP2 had no registered baseline), and a numeral is the head of 23% of numeral names (long pair 32
before 740). Consistent with number words in names or phonetic use, not decisive between them. Tally 1085 held, 1020
failed.

## Hundred-and-fifty-eighth pass (24 Sept 2026): the ending slot over time

Registered first (hundred-and-forty-fourth set, 4bb652350). All eight failed: the 520 share, closers, 400/90,
stacking closers and count texts are flat between early and late levels at both cities, with no Harappa trend. Heads
new in the late level take 740 in 34 of 34 (against 83%): 740 is the productive default, the 520 class closed and old.
Tally 1085 held, 1028 failed.

## Hundred-and-fifty-ninth pass (24 Sept 2026): Mahadevan 2014, the 'merchant of the city' phrase

Registered first (hundred-and-forty-fifth set, 5729984d7), claims read in the text of Mahadevan 2014. The phrase 255
435 690 740 is a real unit (22 lines, three sites, nine preceding signs) that splits AB | CD, but AB alternates with a
bearer closer ('255 435 156') rather than qualifying other heads, and the bearer signs he reads as names are closers
(1 of 196 as heads). Tally 1089 held, 1032 failed.

## Hundred-and-sixtieth pass (24 Sept 2026): scribal workshops

Registered first (hundred-and-forty-sixth set, f2ebc44ca). Graphic variants agree within an object and across copies
of one text, depend on medium and (weakly) on Mohenjo-daro sub-area; no Harappa, house or time effect. CISI allograph
features (now stored by cisi.py) agree within an object (12 pairs). Some candidate pairs are distinct fish, so the
area and medium effects may be lexical. Writing habit shows at object and maker level only. Tally 1094 held, 1036
failed.

## Hundred-and-sixty-first pass (24 Sept 2026): how many names existed

Registered first (sets 147-151 together, 2ea4fc25d). Capture-recapture over Mohenjo-daro and Harappa seals: whole
names estimated at 3,000-5,500 (585 seen, 92% on one seal), heads at 150-220 (129 seen). Shared names are short.
The pattern of personal names composed from a closed stock of elements, not a small set of titles. Estimates are
upper-side (local fashions reduce overlap). Tally 1099 held, 1038 failed.

## Hundred-and-sixty-second pass (24 Sept 2026): productivity of the endings

Registered first (2ea4fc25d). 520 names use 26 heads in 163 names; at equal size 740 always has more; one-site heads
take 740 (93% against 84%) and new 740 heads are rare signs. Baayen's P is underpowered (91 hapax heads) and does not
separate the endings. 740 is the open ending, 520 a small fixed set. Tally 1102 held, 1042 failed.

## Hundred-and-sixty-third pass (24 Sept 2026): closers as head + ending in one sign

Registered first (2ea4fc25d). Closers occupy the length of a head + ending (stem 3.02 against 2.97) but do not
replace any particular head: a closer's commonest alternative covers 39% (chance level), and the bearer closers
alternate with 900 / 752 / 760 more than with 690. The set-145 alternation is one case, not a rule. Tally 1103 held,
1046 failed.

## Hundred-and-sixty-fourth pass (24 Sept 2026): numeral compounds as a shared vocabulary

Registered first (2ea4fc25d). Numeral compounds spread to more sites than matched bigrams, but the value before a
given sign differs between Mohenjo-daro and Harappa (same commonest value for 39% of 69 signs; the '2 + fish' pairs
are the shared exception). The compounds are fixed locally, not a common vocabulary. Tally 1104 held, 1050 failed.

## Hundred-and-sixty-fifth pass (24 Sept 2026): copper tablets by area

Registered first (2ea4fc25d). On 65 copper tablets with a sub-area, the picture depends on the area: text-only
tablets in DK-G South, the animal series in VS-A, anthropomorphs and composites on the citadel mounds; texts do not
cluster, and an area's tablets span levels. Picture sets kept in particular quarters. Tally 1107 held, 1052 failed.

## Hundred-and-sixty-sixth pass (24 Sept 2026): capture-recapture calibrated on Linear B

Registered first (sets 152-156 together, 9f410531e). On DAMOS Linear B (Knossos, Pylos), persons give 3.6 times the
observed, 18% shared, 71% on one document; titles 1.6 times, 50% shared, 51%. Indus names (5.1, 15%, 92%) match the
persons profile on all three; Indus heads match the titles profile. Set 147's personal-name reading is calibrated.
Tally 1112 held, 1053 failed.

## Hundred-and-sixty-seventh pass (24 Sept 2026): capture-recapture inside one city

Registered first (9f410531e). Inside Mohenjo-daro (DK against HR: estimate 7.4 times observed; early against late:
5.5 times) and Harappa (early against late), names are a large population and heads a closed one (1.13-1.15 times).
Set 147 does not depend on regional fashion. Tally 1117 held, 1053 failed.

## Hundred-and-sixty-eighth pass (24 Sept 2026): same name, same person?

Registered first (9f410531e). Underpowered: only 14 long names recur (6 usable Mohenjo-daro pairs). Long-name pairs
share a site somewhat more (61% against 41%, p = 0.051) but not an area, level or motif. Same-name seals cannot be
tied to one owner; one name per seal (92%) is the fact that fits personal seals. Tally 1118 held, 1058 failed.

## Hundred-and-sixty-ninth pass (24 Sept 2026): names from two interchangeable elements?

Registered first (9f410531e). Name elements come from one pool used in every position (65% of heads also open names;
87% of middle signs are also openers or heads), but order is fixed except among stacked fish (the 6 reversed pairs are
fish). DT3 was ill-posed (distinct pairs against shuffles). A shared element pool, not free-order dithematic names.
Tally 1122 held, 1058 failed.

## Hundred-and-seventieth pass (24 Sept 2026): numerals in names as birth-order or clan numbers

Registered first (9f410531e). Name numerals are small (83% worth 4 or less; slightly more than in count texts) and
29 name pairs differ only in the number, but these are mostly 'N + one head' (2/3/4/6 + fish), the counting
construction. Birth-order or rank numbers and counts are not separated. Tally 1125 held, 1059 failed.

## Hundred-and-seventy-first pass (24 Sept 2026): which kinds of text are names, which titles?

Registered first (fe60adf86). All seal genres (740, 520, closer) and the count texts have the open, person-like
capture-recapture profile; only the copper-tablet texts have the closed, title-like one. Because count texts are
not people, the profile measures openness (free composition), not personhood: sets 147/152 show seal names are an
open population over closed elements, and 'personal names' is one reading of that, not the only one. 520 names and
closers are not a small shared title set. Tally 1127 held, 1064 failed.

## Hundred-and-seventy-second pass (24 Sept 2026): Ur III seal legends as a read control

Registered first (b4aade90e). ORACC Ur III (CC0) streamed by `ur3_seals.py` into `data/ur3_seals.tsv`: 6,521 distinct
seal legends. Ur III owner and father names have the title-like, recurring profile (Sumerian names are a limited
stock), titles are closed, and only whole legends are open (17.5 times, 3% shared). So the capture-recapture profile
measures how individual a whole text is, not personhood: Indus seal texts are as individual as whole Ur III legends,
but the Indus format has no filiation line (1.6% two names against 65%) and rarely a title field (13% against 71%).
Qualifies sets 147/152/157: 'individual compositions', either a larger name stock or name + office/lineage packed into
one unit. Fuls's Corpus (2022) and Sign Catalog (2023), previews supplied by the user: the per-sign totals shown
(e.g. 923 45, 752 53, 906 16) match this project's ICIT export, so the books describe the same data; the previews
add no texts. Tally 1130 held, 1068 failed.

## Hundred-and-seventy-third pass (24 Sept 2026): the packed-legend reading and word dividers

Registered first (sets 159-160 together, 210b1fe5b). Openers of 3+-sign names are title-like (closed, 63% shared
between cities) and carry more information about the seal motif than heads do (z 2.5 against 0.95), while name cores
are strongly person-like (8.9 times observed): 'office / lineage + personal name' packed into one unit. Fuls 2024
supported: signs 1 and 2 are not word dividers (Wells rejected). PL5 degenerate. Tally 1135 held, 1073 failed.

## Hundred-and-seventy-fourth pass (24 Sept 2026): the new findings on independent samples

Registered first (210b1fe5b). In the M77 additions: 520 narrow, numeral values local, names open (6.0 times), heads
closed (1.2). Gujarat seals: names open. Controls replicate on new splits (Linear B persons inside Knossos; Ur III
Umma against Nippur). RP7 degenerate (no titles in series D); Harappa moulded tablets intermediate. Tally 1143 held,
1075 failed.

## Hundred-and-seventy-fifth pass (24 Sept 2026): the opener as an office - largely withdrawn

Registered first (sets 161-162 together, e16ba7393). Openness grows with unit length (1-sign names title-like,
2-sign just person-like), so set 159's 'openers title-like, cores person-like' is mostly an artefact of comparing
single signs with multi-sign units. The 'shared openers' are frequent signs and numerals, as common on copper labels
and pictureless seals as on seal names; the motif link is weak once length is split. Openers attach freely to cores.
Set 159's packed-legend support is withdrawn except a weak motif link. Tally 1148 held, 1080 failed.

## Hundred-and-seventy-sixth pass (24 Sept 2026): office + name, further checks

Registered first (e16ba7393). The office-emblem tests fail (no shared emblem per opener across cities, no motif
concentration, no size or quarter effect); the head sets the ending (z 22.7). B repeats the opener/core contrast with
set 161's length caveat. New: frequent openers begin 90% of long names on sealings (tags) against 57% on seals, and
become more common in late levels (+0.26): standardised name openings over time. Tally 1154 held, 1084 failed.

## Hundred-and-seventy-seventh pass (24 Sept 2026): length-matched and shuffled baselines

Registered first (sets 163-164 together, 3af4b42ab). At equal length (3 and 4 units) Indus names have the Linear B
person profile (ratios 3.0 against 3.7 and 3.4); sharing falls with length in both scripts. Real names recur 25 times
beyond sign shuffles (Linear B persons 33, Ur III legends 3); 520 names recur more than 740 names beyond chance (50
against 19). Set 152's comparison survives length control. LM9 degenerate. Tally 1163 held, 1085 failed.

## Hundred-and-seventy-eighth pass (24 Sept 2026): standardisation over time and seal types

Registered first (3af4b42ab). Mohenjo-daro long names beginning with a frequent opener rise from 39% to 66% (Harappa
already 75% early); the rise holds on square seals alone, is not numerals, and is spread over several openers.
Rectangular seals are later and use the frequent openers more. Names stay individual (no more recurrence late).
Mohenjo-daro converges on Harappa's name openings. Tally 1168 held, 1090 failed.

## Hundred-and-seventy-ninth pass (24 Sept 2026): does Mohenjo-daro converge on Harappa?

Registered first (sets 165-166 together, bfebc0d63). No: heads, all signs and numeral notation at Mohenjo-daro do not
move towards Harappa from early to late, and the rising openers are not specifically Harappa's. Only name length moves
slightly. Set 164's 'converges on Harappa' is corrected to a local shift towards frequent openings. Tally 1171 held,
1097 failed.

## Hundred-and-eightieth pass (24 Sept 2026): the names that recur

Registered first (bfebc0d63). Fifteen names occur at 3+ sites ('590 390 740' at five), but shared names are not fish
names, 520 names reach fewer sites than matched 740 names, sharing does not fall with distance (five sites), and
same-name seals do not share a motif beyond chance: the name is independent of the seal's animal. Ur III shared owners
are shorter, as Indus shared names are; Linear B shared persons are not. Tally 1173 held, 1105 failed.

## Hundred-and-eighty-first pass (24 Sept 2026): administration, survival and scribal hands

Registered first (sets 167-168 together, ff42dfa9c). Most seals are lost: 6 of 42 sealing texts match a known seal
(estimate about 6 times the known seal texts, inflated by Lothal's thin seal record). Second lines of two-line seals
are shorter but not title fields; rising openers are not sealing openers; no in-city locality of numeral compounds;
a scribe's hand across pairs is borderline (p = 0.059). AD9 ill-posed; 5 of 16 foreign stroke runs precede signs
never counted at home. Tally 1177 held, 1111 failed.

## Hundred-and-eighty-second pass (24 Sept 2026): controls on published claims and on the count texts

Registered first (ff42dfa9c). '2 + fish' is commonest with copies counted and in M77 too: three transcriptions agree
against Parpola's '6 + fish'. Ur III legends avoid repetition as Indus lines do (9.5% against 13.4% at 5-7 units), so
Farmer-Sproat-Witzel's repetition argument fails on a same-genre control. Linear B counts are about as local between
palaces (47%) and as open as Indus count texts, so set 150's 'local naming customs' is withdrawn to 'local, as counts
are'. The copper-tablet picture signs never occur in seal names. Tally 1183 held, 1115 failed.

## Hundred-and-eighty-third pass (24 Sept 2026): writing-system statistics against two read scripts

Registered first (sets 169-170 together, 359f0528e). At 5,000 tokens the Indus signs (495 types) fall between Linear B
signs (198) and Linear B words (2,128), nearer the signs, on types, hapax share, conditional entropy and relative
predictability: a logo-syllabic inventory. On concentration measures (top ten, normalised entropy, doubling) the Indus
signs look like Ur III seal legends instead: the formulaic seal genre. Tally 1190 held, 1118 failed.

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
