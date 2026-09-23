# Parpola 2005 against Mahadevan's M77 corpus

Corpus: 3573 lines, 2906 texts, 14153 sign tokens, 418 sign types (MSg0 = unread sign, counted as a token).

- mean signs per text: 4.87; longest: text 2847 26, text 1623 26, text 8101 24 (p. 45: "the longest text is merely 26 signs").
- sign types occurring once: 112 of 418 = 27%.
- most frequent sign: MSg342, 1395 tokens = 9.9% (p. 47: "almost 10%"); it ends 974 lines and begins 4.
- MSg342 beside itself: 1 time(s): [('9901.0', 'MSg178 MSg53 MSg97 MSg342 MSg342')] (p. 47: never in the Indus Valley; once on a round seal probably from Mesopotamia).
- doubled signs, West Asian finds (9xxx): 5 of 164 adjacent pairs = 3.0%; {'MSg342': 1, 'MSg1': 1, 'MSg245': 1, 'MSg21': 1, 'MSg59': 1}
- doubled signs, all other texts: 192 of 9660 adjacent pairs = 2.0%; {'MSg245': 69, 'MSg1': 13, 'MSg153': 10, 'MSg328': 10, 'MSg176': 9, 'MSg391': 9, 'MSg375': 9, 'MSg121': 9}

## The sign claims on M77

Sign groups from the ICIT alignment (align_m77.py, data/icit_m77_map.tsv): fish series MSg59-75, crab MSg53/58, fig MSg348/367/370/371, eye MSg375, water MSg294, pot MSg328; numerals 97=1 99=2 102=3 103=3 104=4 106=5 109=6 112=7 114=8 86=1 87=2 89=3 96=5 121=12 (short, two-tier and long strokes).

- numerals read immediately before the plain fish, by value: 1: 6, 2: 83, 3: 20, 4: 4, 6: 16, 7: 1, 12: 9
- whole lines that are numeral + plain fish: 4009.0 (7); 4171.0 (6); 4853.0 (6); 4873.0 (6)
- 6 + fish: 16 (shuffled mean 4.4; 0 of 300 shuffles as high)
- 7 + fish: 1 (shuffled mean 1.6; 257 of 300 shuffles as high)
- any numeral + fish: 139 (shuffled mean 49.6; 0 of 300 shuffles as high)
- any numeral + pot: 209 (shuffled mean 104.3; 0 of 300 shuffles as high)
- fig + fish: 2 (shuffled mean 0.9; 67 of 300 shuffles as high)
- fig + anything: {'MSg342': 23, 'MSg59': 2, 'MSg225': 1, 'MSg0': 1, 'MSg87': 1, 'MSg380': 1, 'MSg308': 1}
- crab + plain fish: 2 (shuffled mean 5.6; 295 of 300 shuffles as high)
- crab + fish series: 31 (shuffled mean 16.6; 1 of 300 shuffles as high)
- eye + eye: 9 (shuffled mean 4.9; 0 of 300 shuffles as high)
- water + eye: 6 (shuffled mean 1.1; 0 of 300 shuffles as high)
- lines ending water + eye: ['1221.0', '2138.0', '4027.0', '4169.0']; lines that are only water/eye signs: []
- crab tokens with a fish sign beside them: 53 of 137 (shuffled mean 33.0; 0 of 300 as high)
