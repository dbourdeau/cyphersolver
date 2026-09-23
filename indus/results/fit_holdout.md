# Fitted keys on unseen texts

- training: 2088 ICIT-derived lines of 3+ signs; held out: 975 M77-only lines of 3+ signs that do not repeat a training line. Key: the 250 commonest training signs, 47 possible values (consonant class x vowel class, bare vowels, bare consonants), 20000 hill-climbing steps on the vowel-aware score.

## H1-H2 Fitted in each language, read on the held-out texts

| language | training score | held-out score | held-out, shuffles of the fitted key median (range) | shuffles as good |
|---|---|---|---|---|
| Dravidian (DEDR) | 91.9% | 91.6% | 90.3% (86.6-91.8) | 1 of 100 |
| Sanskrit (Monier-Williams) | 94.0% | 93.6% | 91.7% (89.9-93.0) | 0 of 100 |
| Sumerian (ePSD2) | 88.5% | 85.0% | 81.5% (74.5-83.6) | 0 of 100 |
| Munda (JAMBU) | 84.2% | 79.8% | 77.2% (73.9-80.3) | 2 of 100 |
| Old Tamil (Sangam-cited Tamil Lexicon) | 81.2% | 76.3% | 64.6% (55.6-71.7) | 0 of 100 |
| Burushaski (Berger, Yoshioka) | 85.2% | 78.8% | 69.7% (60.3-74.2) | 0 of 100 |

## H3 The same fit on sign-shuffled training lines (memorising control)

| language | training score | held-out score | shuffles median (range) | shuffles as good |
|---|---|---|---|---|
| Dravidian (DEDR), shuffled training | 92.6% | 91.6% | 93.0% (91.5-93.7) | 99 of 100 |
| Sanskrit (Monier-Williams), shuffled training | 93.5% | 93.4% | 93.6% (92.8-94.1) | 68 of 100 |

## H4 Power: a synthetic language with a planted key

| setting | training score | held-out score | shuffles median (range) | shuffles as good |
|---|---|---|---|---|
| synthetic Dravidian, planted key | 96.7% | 95.3% | 93.3% (92.1-94.5) | 0 of 100 |

