# Fitted keys on unseen texts, lexicons matched

20000 hill-climbing steps a fit, 5 draws of matched lexicons, 50 shuffles a test; z = (held-out score - mean of the shuffles) / their standard deviation.

## M1 Positive control: synthetic Dravidian

### synthetic Dravidian corpus (training 2088 lines, held out 975)

- matched lexicons: 2405 skeletons each (by consonant count: 1: 98, 2: 590, 3: 1060, 4: 486, 5: 127, 6: 44).

| lexicon | z-score of the held-out margin, mean (draws) | wins (largest z in a draw) |
|---|---|---|
| Old Tamil (Sangam-cited Tamil Lexicon) | 8.81 (7.2, 9.2, 10.1, 9.6, 8.0) | 4 of 5 |
| Munda (JAMBU) | 5.50 (8.8, 4.5, 4.4, 3.9, 5.9) | 1 of 5 |
| Sumerian (ePSD2) | 3.82 (3.7, 4.1, 4.5, 1.0, 5.9) | 0 of 5 |
| Burushaski (Berger, Yoshioka) | 3.02 (2.6, 3.6, 2.0, 4.9, 2.0) | 0 of 5 |
| Sanskrit (Monier-Williams) | 2.26 (3.1, 1.0, 4.0, 1.6, 1.5) | 0 of 5 |
| Dravidian (DEDR) | 2.02 (1.3, 3.1, 1.8, 1.0, 2.9) | 0 of 5 |

## M2 The Indus corpus

### ICIT-derived training (2088 lines), M77-only held out (975 lines)

- matched lexicons: 2405 skeletons each (by consonant count: 1: 98, 2: 590, 3: 1060, 4: 486, 5: 127, 6: 44).

| lexicon | z-score of the held-out margin, mean (draws) | wins (largest z in a draw) |
|---|---|---|
| Burushaski (Berger, Yoshioka) | 6.24 (6.8, 8.3, 4.3, 4.6, 7.3) | 3 of 5 |
| Sumerian (ePSD2) | 6.12 (6.5, 6.3, 4.6, 6.4, 6.7) | 0 of 5 |
| Sanskrit (Monier-Williams) | 5.98 (4.4, 5.0, 6.1, 8.0, 6.3) | 1 of 5 |
| Dravidian (DEDR) | 5.22 (3.4, 7.1, 4.4, 6.7, 4.5) | 0 of 5 |
| Old Tamil (Sangam-cited Tamil Lexicon) | 5.06 (4.7, 5.0, 7.0, 4.1, 4.5) | 1 of 5 |
| Munda (JAMBU) | 4.97 (4.7, 5.3, 5.2, 5.5, 4.1) | 0 of 5 |

## Reading

- Control (a corpus written in Dravidian): ta 8.8, mu 5.5, sux 3.8, bu 3.0, sa 2.3, dra 2.0. The Dravidian family comes first through Old Tamil (4 of 5 draws), but DEDR, the very lexicon the synthetic text was drawn from, comes last: cut to matched random skeletons of all Dravidian languages, it rarely holds the words used. The ranking depends on how a lexicon is made, not only on its language; the test tells families apart only roughly.
- Indus: bu 6.2, sux 6.1, sa 6.0, dra 5.2, ta 5.1, mu 5.0. No language stands out (the z-scores overlap from draw to draw). If the Indus texts behaved like the synthetic Dravidian corpus, Old Tamil should win most draws; it wins 1 of 5 and ranks 5 of 6. That is weak evidence against an Old-Tamil-like lexicon at best, given the noisy control. **Inconclusive: fitted keys, even with matched lexicons and unseen texts, do not identify the language.**
