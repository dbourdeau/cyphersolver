# A test bench for Indus decipherments

2088 lines of 3+ signs (ICIT-derived corpus). Lexicon skeletons: Sanskrit (Monier-Williams) 67795, Dravidian (DEDR) 8257, Sumerian (ePSD2) 3830.

## Key-independent: the endings as gender classes

Mahadevan (1998) reads 740 and 520 as the masculine and non-masculine singular suffixes. Gender is a property of the noun, so a name should take one of them, not both.

- last sign of the name before the ending (740 or 520, with or without 400/90/151 after it), signs with 10+ lines: 32; taking the minority ending in 20%+ of lines: 4 (220 30/40, 240 16/36, 400 10/7, 460 12/4).
- whole names (the text before the ending) seen with both endings: 5 of 881; with the endings shuffled among the lines: median 46 (range 33-57). The endings are fixed per name, as a gender (or any lexical class) would be.

## Yajnadevam 2024 (github.com/yajnadevam/lipi, xlits.csv)

**B1 shape.** 681 signs keyed; 93% of sign tokens have a value; 46 of the 50 commonest signs keyed; 49 distinct consonant skeletons among the values.

**B2 reading against shuffled keys** (share of consonants covered by words of 3+ consonants; 200 shuffles):

| lexicon | real key | shuffles median (range) | shuffles as good | 
|---|---|---|---|
| Sanskrit (Monier-Williams) (claimed) | 75.3% | 75.1% (66.2-79.0) | 87 of 200 |
| Dravidian (DEDR) | 71.9% | 69.5% (59.6-74.6) | 32 of 200 |
| Sumerian (ePSD2) | 46.5% | 44.2% (21.8-55.3) | 73 of 200 |

**B2v the same, vowels kept** (three vowel classes; the version that passes the Linear Elamite control, B5c; 100 shuffles):

| lexicon | real key | shuffles median (range) | shuffles as good |
|---|---|---|---|
| Sanskrit (Monier-Williams) (claimed) | 53.0% | 44.8% (35.1-59.1) | 10 of 100 |
| Dravidian (DEDR) | 70.4% | 61.2% (52.6-69.8) | 0 of 100 |
| Sumerian (ePSD2) | 19.7% | 17.5% (7.6-28.5) | 34 of 100 |
| Munda (JAMBU) | 41.8% | 42.1% (24.2-55.1) | 53 of 100 |
| Old Tamil (Sangam-cited Tamil Lexicon) | 12.6% | 9.9% (4.7-16.9) | 19 of 100 |
| Burushaski (Berger, Yoshioka) | 40.4% | 41.7% (21.8-53.1) | 57 of 100 |

**B3 the copper-tablet anchors.**

- anchor signs: 341 (rhinoceros) = m: no; 749 (goat) = isan: no; 753 (hare) = r: no; 777 (goat/archer) = ras: no; 778 (goat/archer) = ras: no.
- anchor texts naming their own animal (a sa word for it, 2+ consonants, inside the reading): 4 of 8; naming another tablet animal: 2.2 on average; shuffled keys: mean 2.65, as many or more in 46 of 200.

**B4 structure.**

- stroke numerals keyed: 22 of 22; value = the number word: 0; value = only its first consonant: 12 (one-letter values match some number by chance: the chance a one-consonant value starts the right number word is about 1 in 8). 31=1 long "a", 32=2 long "s", 33=3 long "j", 34=4 long "c" (initial), 35=5 long "p" (initial), 36=6 long "s" (initial), 1=1 short "a", 2=2 short "v", 3=3 short "j", 4=4 short "c" (initial), 5=5 short "p" (initial), 6=6 short "s" (initial), 7=7 short "s" (initial), 13=3 tiered "t" (initial), 14=4 tiered "s", 15=5 tiered "p" (initial), 16=6 tiered "s" (initial), 17=7 tiered "s" (initial), 18=8 tiered "as" (initial), 19=8 tiered "n", 55=12 tiered "j", 56=24 tiered "j".
- short and long strokes of one number: 3/33 = j/j; 4/34 = c/c; 5/35 = p/p; 6/36 = s/s; 1/31 = a/a; 2/32 = v/s.
- endings 740 / 520 = 'an' / 'n'; second slot 400 / 90 / 151 = 'i' / 'a' / 'y'; openers 817 / 820 / 861 = 'r' / 'r' / 'r'.

## Fairservis 1992, The Harappan Civilization and its Writing, Appendix A

**B1 shape.** 97 signs keyed; 64% of sign tokens have a value; 34 of the 50 commonest signs keyed; 71 distinct consonant skeletons among the values.

**B2 reading against shuffled keys** (share of consonants covered by words of 3+ consonants; 200 shuffles):

| lexicon | real key | shuffles median (range) | shuffles as good | 
|---|---|---|---|
| Sanskrit (Monier-Williams) | 85.6% | 85.3% (78.8-93.7) | 94 of 200 |
| Dravidian (DEDR) (claimed) | 87.7% | 86.2% (79.4-93.1) | 63 of 200 |
| Sumerian (ePSD2) | 69.1% | 71.0% (43.9-82.8) | 119 of 200 |

**B2v the same, vowels kept** (three vowel classes; the version that passes the Linear Elamite control, B5c; 100 shuffles):

| lexicon | real key | shuffles median (range) | shuffles as good |
|---|---|---|---|
| Sanskrit (Monier-Williams) | 89.1% | 95.8% (88.8-98.0) | 99 of 100 |
| Dravidian (DEDR) (claimed) | 92.7% | 97.4% (91.5-99.0) | 97 of 100 |
| Sumerian (ePSD2) | 62.2% | 64.8% (39.0-73.9) | 64 of 100 |
| Munda (JAMBU) | 78.5% | 84.5% (76.5-87.9) | 97 of 100 |
| Old Tamil (Sangam-cited Tamil Lexicon) | 62.3% | 60.6% (29.0-77.4) | 40 of 100 |
| Burushaski (Berger, Yoshioka) | 83.5% | 88.1% (80.0-92.6) | 86 of 100 |

**B3 the copper-tablet anchors.**

- anchor signs: 341 (rhinoceros): no value; 749 (goat): no value; 753 (hare): no value; 777 (goat/archer): no value; 778 (goat/archer): no value.
- anchor texts naming their own animal (a dra word for it, 2+ consonants, inside the reading): 5 of 8; naming another tablet animal: 4.2 on average; shuffled keys: mean 5.39, as many or more in 171 of 200.

**B4 structure.**

- stroke numerals keyed: 8 of 22; value = the number word: 2; value = only its first consonant: 1 (one-letter values match some number by chance: the chance a one-consonant value starts the right number word is about 1 in 8). 31=1 long "daṇḍi", 1=1 short "*ā", 2=2 short "*il" (full), 13=3 tiered "il-ā", 17=7 tiered "in", 18=8 tiered "eṭṭu" (initial), 19=8 tiered "*toḷ", 55=12 tiered "paṉir" (full).
- short and long strokes of one number: 1/31 = *ā/daṇḍi.
- endings 740 / 520 = 'āṇ' / 'ār'; second slot 400 / 90 / 151 = 'cīppu' / 'āḷ-āṇ' / 'kā'; openers 817 / 820 / 861 = None / 'tiṅgal' / 'pāl-ūr'.

## Fairservis 1992, The Harappan Civilization and its Writing, Appendix A (with unsure matches)

**B1 shape.** 172 signs keyed; 80% of sign tokens have a value; 42 of the 50 commonest signs keyed; 110 distinct consonant skeletons among the values.

**B2 reading against shuffled keys** (share of consonants covered by words of 3+ consonants; 200 shuffles):

| lexicon | real key | shuffles median (range) | shuffles as good | 
|---|---|---|---|
| Sanskrit (Monier-Williams) | 91.6% | 91.1% (84.5-95.7) | 71 of 200 |
| Dravidian (DEDR) (claimed) | 92.8% | 92.7% (89.1-95.7) | 90 of 200 |
| Sumerian (ePSD2) | 73.5% | 76.1% (44.1-83.9) | 142 of 200 |

**B2v the same, vowels kept** (three vowel classes; the version that passes the Linear Elamite control, B5c; 100 shuffles):

| lexicon | real key | shuffles median (range) | shuffles as good |
|---|---|---|---|
| Sanskrit (Monier-Williams) | 90.9% | 94.6% (89.4-97.0) | 95 of 100 |
| Dravidian (DEDR) (claimed) | 95.8% | 98.4% (95.1-99.2) | 94 of 100 |
| Sumerian (ePSD2) | 60.4% | 60.9% (35.3-68.0) | 55 of 100 |
| Munda (JAMBU) | 78.0% | 79.9% (74.2-84.6) | 85 of 100 |
| Old Tamil (Sangam-cited Tamil Lexicon) | 63.0% | 59.6% (28.1-71.4) | 41 of 100 |
| Burushaski (Berger, Yoshioka) | 84.5% | 85.3% (77.3-89.7) | 61 of 100 |

**B3 the copper-tablet anchors.**

- anchor signs: 341 (rhinoceros): no value; 749 (goat): no value; 753 (hare): no value; 777 (goat/archer): no value; 778 (goat/archer): no value.
- anchor texts naming their own animal (a dra word for it, 2+ consonants, inside the reading): 6 of 8; naming another tablet animal: 4.6 on average; shuffled keys: mean 6.04, as many or more in 171 of 200.

**B4 structure.**

- stroke numerals keyed: 13 of 22; value = the number word: 4; value = only its first consonant: 2 (one-letter values match some number by chance: the chance a one-consonant value starts the right number word is about 1 in 8). 31=1 long "daṇḍi", 32=2 long "*iru" (full), 33=3 long "*mun" (initial), 34=4 long "*nāl" (full), 1=1 short "*ā", 2=2 short "*il" (full), 5=5 short "*cayN", 6=6 short "*caṟu", 13=3 tiered "il-ā", 17=7 tiered "in", 18=8 tiered "eṭṭu" (initial), 19=8 tiered "*toḷ", 55=12 tiered "paṉir" (full).
- short and long strokes of one number: 1/31 = *ā/daṇḍi; 2/32 = *il/*iru.
- endings 740 / 520 = 'āṇ' / 'ār'; second slot 400 / 90 / 151 = 'cīppu' / 'āḷ-āṇ' / 'kā'; openers 817 / 820 / 861 = None / 'tiṅgal' / 'pāl-ūr'.

## Kak 1988, A frequency analysis of the Indus script (Cryptologia 12(3), 129-143)

**B1 shape.** 7 signs keyed; 17% of sign tokens have a value; 5 of the 50 commonest signs keyed; 6 distinct consonant skeletons among the values.

**B2 reading against shuffled keys:** not applicable; 7 signs are too few for a reading test (the keyed signs rarely stand next to each other).

**B3 the copper-tablet anchors.**

- anchor signs: 341 (rhinoceros): no value; 749 (goat): no value; 753 (hare): no value; 777 (goat/archer): no value; 778 (goat/archer): no value.
- anchor texts naming their own animal (a sa word for it, 2+ consonants, inside the reading): 0 of 8; naming another tablet animal: 0.2 on average; shuffled keys: mean 0.08, as many or more in 200 of 200.

**B4 structure.**

- stroke numerals keyed: 0 of 22; value = the number word: 0; value = only its first consonant: 0 (one-letter values match some number by chance: the chance a one-consonant value starts the right number word is about 1 in 8). .
- short and long strokes of one number: not both keyed.
- endings 740 / 520 = 'sa' / 'ai'; second slot 400 / 90 / 151 = None / 'ta' / None; openers 817 / 820 / 861 = None / None / None.

## Mahadevan 1998 and 2014

**B1 shape.** 5 signs keyed; 15% of sign tokens have a value; 4 of the 50 commonest signs keyed; 5 distinct consonant skeletons among the values.

**B2 reading against shuffled keys:** not applicable; 5 signs are too few for a reading test (the keyed signs rarely stand next to each other).

**B3 the copper-tablet anchors.**

- anchor signs: 341 (rhinoceros): no value; 749 (goat): no value; 753 (hare): no value; 777 (goat/archer): no value; 778 (goat/archer): no value.
- anchor texts naming their own animal (a dra word for it, 2+ consonants, inside the reading): 3 of 8; naming another tablet animal: 2.6 on average; shuffled keys: mean 2.01, as many or more in 67 of 200.

**B4 structure.**

- stroke numerals keyed: 0 of 22; value = the number word: 0; value = only its first consonant: 0 (one-letter values match some number by chance: the chance a one-consonant value starts the right number word is about 1 in 8). .
- short and long strokes of one number: not both keyed.
- endings 740 / 520 = 'anru' / 'ampu'; second slot 400 / 90 / 151 = None / None / None; openers 817 / 820 / 861 = None / None / None.

## Parpola 1994 (Deciphering the Indus Script, CUP), Fig. 15.2 and pp. 94-96, 179-280

**B1 shape.** 30 signs keyed; 28% of sign tokens have a value; 13 of the 50 commonest signs keyed; 15 distinct consonant skeletons among the values.

**B2 reading against shuffled keys** (share of consonants covered by words of 3+ consonants; 200 shuffles):

| lexicon | real key | shuffles median (range) | shuffles as good | 
|---|---|---|---|
| Sanskrit (Monier-Williams) | 52.2% | 43.7% (35.6-58.5) | 63 of 200 |
| Dravidian (DEDR) (claimed) | 54.0% | 44.7% (38.9-59.4) | 59 of 200 |
| Sumerian (ePSD2) | 25.4% | 22.8% (12.4-30.6) | 42 of 200 |

**B2v the same, vowels kept** (three vowel classes; the version that passes the Linear Elamite control, B5c; 100 shuffles):

| lexicon | real key | shuffles median (range) | shuffles as good |
|---|---|---|---|
| Sanskrit (Monier-Williams) | 67.9% | 84.6% (67.6-86.9) | 97 of 100 |
| Dravidian (DEDR) (claimed) | 77.3% | 92.5% (77.5-94.6) | 100 of 100 |
| Sumerian (ePSD2) | 38.6% | 37.1% (23.7-61.8) | 37 of 100 |
| Munda (JAMBU) | 66.7% | 67.0% (52.3-85.9) | 53 of 100 |
| Old Tamil (Sangam-cited Tamil Lexicon) | 50.4% | 47.9% (38.4-72.9) | 38 of 100 |
| Burushaski (Berger, Yoshioka) | 76.1% | 91.1% (75.4-93.4) | 92 of 100 |

**B3 the copper-tablet anchors.**

- anchor signs: 341 (rhinoceros): no value; 749 (goat): no value; 753 (hare): no value; 777 (goat/archer) = koli "fig + crab, the fig tree Ficus": names it by the sound, = gole "notched extremity or horn of a bow."; kal "nilgiri ibex."; koḷai "hold as of a string in a bow, determinat"; 778 (goat/archer) = koli "fig + crab": names it by the sound, = gole "notched extremity or horn of a bow."; kal "nilgiri ibex."; koḷai "hold as of a string in a bow, determinat".
- anchor texts naming their own animal (a dra word for it, 2+ consonants, inside the reading): 2 of 8; naming another tablet animal: 1.8 on average; shuffled keys: mean 2.27, as many or more in 165 of 200.

**B4 structure.**

- stroke numerals keyed: 8 of 22; value = the number word: 6; value = only its first consonant: 0 (one-letter values match some number by chance: the chance a one-consonant value starts the right number word is about 1 in 8). 32=2 long "vel", 33=3 long "mu" (full), 3=3 short "mu" (full), 4=4 short "nal" (full), 13=3 tiered "cul", 14=4 tiered "nal" (full), 16=6 tiered "aru" (full), 17=7 tiered "elu" (full).
- short and long strokes of one number: 3/33 = mu/mu.
- endings 740 / 520 = 'a' / None; second slot 400 / 90 / 151 = None / 'al' / None; openers 817 / 820 / 861 = None / None / None.

## B5 Controls

- (a) power, Sanskrit (Monier-Williams): planted key reads 98.8% of its synthetic corpus; its shuffles median 88.9%, best 90.4%.
- (a) power, Dravidian (DEDR): planted key reads 97.0% of its synthetic corpus; its shuffles median 85.5%, best 87.0%.
- (a) power, Sumerian (ePSD2): planted key reads 96.8% of its synthetic corpus; its shuffles median 84.2%, best 86.1%.
- (b) ceiling, Sanskrit (Monier-Williams): a key fitted by hill-climbing (one consonant class per sign, 250 commonest signs, 3,000 steps, 1,000 lines) reads 94.0% of those lines.
- (b) ceiling, Dravidian (DEDR): a key fitted by hill-climbing (one consonant class per sign, 250 commonest signs, 3,000 steps, 1,000 lines) reads 93.1% of those lines.
- (b) ceiling, Sumerian (ePSD2): a key fitted by hill-climbing (one consonant class per sign, 250 commonest signs, 3,000 steps, 1,000 lines) reads 92.7% of those lines.
- (c) a real decipherment, Linear Elamite (Desset 2022 values, Elamicon corpus, Hallock 1969 Elamite lexicon), consonants only: 60.7% against shuffles 62.3% (54.6-66.7), 80 of 100 as good.
- (c) a real decipherment, Linear Elamite (Desset 2022 values, Elamicon corpus, Hallock 1969 Elamite lexicon), vowels kept: 25.7% against shuffles 19.2% (12.7-26.0), 4 of 100 as good.

## Summary

| key | claimed | consonants only: key / shuffles / as good | vowels kept: key / shuffles / as good | best other language, vowels kept |
|---|---|---|---|---|
| Yajnadevam 2024 (github.com/yajnadevam/lipi, xlits.csv) | sa | 75.3% / 75.1% / 87 of 200 | 53.0% / 44.8% / 10 of 100 | dra 70.4% / 61.2% / 0 of 100 |
| Fairservis 1992, The Harappan Civilization and its Writing, Appendix A | dra | 87.7% / 86.2% / 63 of 200 | 92.7% / 97.4% / 97 of 100 | ta 62.3% / 60.6% / 40 of 100 |
| Fairservis 1992, The Harappan Civilization and its Writing, Appendix A (with unsure matches) | dra | 92.8% / 92.7% / 90 of 200 | 95.8% / 98.4% / 94 of 100 | ta 63.0% / 59.6% / 41 of 100 |
| Kak 1988, A frequency analysis of the Indus script (Cryptologia 12(3), 129-143) | sa | too few signs for a reading test | | |
| Mahadevan 1998 and 2014 | dra | too few signs for a reading test | | |
| Parpola 1994 (Deciphering the Indus Script, CUP), Fig. 15.2 and pp. 94-96, 179-280 | dra | 54.0% / 44.7% / 59 of 200 | 77.3% / 92.5% / 100 of 100 | ta 50.4% / 47.9% / 38 of 100 |
