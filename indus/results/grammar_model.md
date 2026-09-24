# A slot grammar against n-grams on unseen texts

- training lines: 2562 (ICIT-derived); held-out lines: 2140 (M77 additions + fuller-corpus texts not in the dump), 9713 sign positions incl. the end of line; vocabulary 622; held-out lines that parse into the slots: 2140 (100%).

| model | cross-entropy, bits per sign (held out) |
|---|---|
| unigram | 6.234 |
| bigram | 5.074 |
| trigram | 4.989 |
| slot grammar (bigram names) | 5.107 |
| slot grammar (trigram names) | 5.038 |

A slot grammar that does as well as, or better than, a trigram with far fewer free choices captures the structure the n-grams learn; the difference in bits per sign is the part of the texts the rules do not explain.
