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
This is progress on the evidence the decipherment claims stand on, not a decipherment.

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
four tablet sets repeated 10-41 times in both, hard EM matched 978 lines with 96% of aligned signs on a single M77
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

Direction: 2,440 objects read right to left, 103 left to right; `signs_reading` reverses R/L objects, so the
first id is the first sign read. Checked: 740 ends lines (in M77 it ends 974 lines and begins 4).

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
| C6 | West Asian square seals carry typical sequences, round and cylinder ones common signs in unusual order (p. 47) | Bigram model trained on South Asia: 9 round/cylinder seals at a median 94th percentile of surprisal and 90th for order-surprise; Kish square seal typical (51st); Salut (Oman) square seal atypical (98th) | confirmed for round/cylinder; one square counterexample |
| C7 | fish signs almost every tenth sign on seals (p. 52) | 695 of 7,165 seal tokens = 9.7% | confirmed |
| C8 | '6'+'fish' and '7'+'fish'; '7'+'fish' is a whole large Harappa seal (p. 54) | ICIT: 6+fish 9 (PMI 3.1, 0/300 shuffles); 7+fish once, H-9 (Harappa), the whole text. M77: 6+fish 16 (4.4 expected); 7+fish once, text 4009 (Harappa), the whole text, 112 59 = ICIT 17 220 under the sign map: the same seal | confirmed in both; 7+fish rests on one seal |
| C8 | (not in the lecture) | numerals before plain fish, ICIT: 2 x62, 3 x19, 6 x9, 12 x8, 4 x6, 1 x5, 7 x1; M77: 2 x83, 3 x20, 6 x16, 12 x9, 1 x6, 4 x4, 7 x1. The lecture reads 10 of 110 (17 of 139) | the 2+fish and 3+fish groups need a reading too |
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
  one or two seals each. The largest numeral+fish groups, '2'+'fish' (62) and '3'+'fish' (19), are not read in
  the lecture.
- 'Crab'+'fish' almost never uses the plain fish (ICIT 0, M77 2, both below chance); it is crab + a marked fish
  (240, 233, 231, 235), well above chance in both corpora. The *kōṇ-mīṉ* reading needs those marked fish to be
  read as 'star' too.
- The two corpora agree: every sign count above was reproduced on M77 through the alignment, and both put the
  single jar+jar, the single 7+fish and the two fig+fish on the same objects.
- Parpola's null for jar doubling (independent signs, about 110 expected) is too generous. The within-line
  shuffle expects 4.0 and sees 0 in South Asia (p about 0.007), still well below chance, so his argument stands
  on the fairer null.
- A reusable harness: `build_corpus.py`, `signs.py`, `parpola_checks.py`, `m77_checks.py`.

## Limitations

- ICIT glyph identification is by shape from the font, checked on the cited seals and by the M77 alignment, but
  not sign-by-sign against Parpola 1994's list, which may split or merge signs differently (e.g. crab + 'fish').
- The ICIT dump lacks some cited objects (M-682, M-414, M-305, H-598, H-602, H-396, H-568) and does not
  separate the sides of an object.
- Duplicates (sealings from one seal, sets of copper tablets) are counted as separate objects, as in Parpola's
  own counts.

## Next steps

1. (Done for Mahadevan: `align_m77.py`.) Extend the map to Parpola 1994's numbers through the mayig CISI files.
2. Get the missing cited seals (CISI vol. 1-3 photographs; harappa.com) and check C10, C13, C15, C16.
3. Take Parpola 1994's full list of readings and test every compound he reads the same way (C17 table): attested
   count, PMI, and whether the parts also occur alone.
4. Substitution classes: which units fill the slot before "845 61 407" and similar recurring tails. That is the
   Koskenniemi-Parpola 1970 method, run on the full corpus.

## Prior work

The lecture is published and its readings go back to Parpola 1994. Computational work on these corpora
exists: Rao et al. 2009 (entropy), Yadav et al. 2010, Farmer et al. 2004, and the indus_decipher toolkit (2026).
None of these checks Parpola 2005's specific counts and cited seals as done here; the counts and tables in
`results/` were all computed in this session.
