# Twenty-second registered predictions: classes of the content signs

- content signs clustered (A, 10+ tokens): 115.
  - cluster 0 (19 signs, 522 tokens): 920(F), 61, 790, 416(Q), 350, 501(K), 850, 165(K), 384(E), 809, 91, 97(A), 877, 321, 382(E), 905, 243, 484(K)
  - cluster 1 (25 signs, 853 tokens): 176, 415(Q), 100(A), 550(I), 845, 923(H), 440(I), 388, 585, 335(L), 630, 482(K), 236, 555, 222, 175, 48, 320
  - cluster 2 (18 signs, 863 tokens): 590(G), 760, 255, 840(O), 140, 892(H), 692, 575(G), 125(A), 752(J), 904, 632, 104, 500(K), 645, 831, 95, 890(H)
  - cluster 3 (17 signs, 1366 tokens): 390(E), 60, 615(G), 741(J), 407, 405(E), 700(J), 900(H), 368, 690(K), 460(G), 455(N), 595, 413(E), 480(P), 190, 297
  - cluster 4 (11 signs, 288 tokens): 156, 527, 154(A), 158, 226, 621(I), 679, 526, 565, 161, 241
  - cluster 5 (5 signs, 119 tokens): 435, 70, 636, 436, 921
  - cluster 6 (7 signs, 199 tokens): 503(K), 142(A), 171(K), 832, 495(D), 137, 711
  - cluster 7 (13 signs, 1345 tokens): 220(Q), 240(Q), 235(Q), 233, 803(F), 806(F), 798(Q), 231(Q), 717(I), 742, 745, 491, 838

## Q1 validation: numerals cluster together
- numerals clustered: 15; same-cluster rate for numeral pairs 0.17, for all pairs 0.13; ratio 1.3; threshold 3.
- **Q1 fails.**

## Q2 validation: Linear B sign kinds cluster together
- Linear B signs: 152 (78 syllabograms, 74 word signs); same-kind share of same-cluster pairs 0.95; p = 0.0001.
- **Q2 holds.**

## Q3 A clusters predict B contexts
- signs with 10+ tokens in B: 64; B-context cosine same cluster minus different +0.028; p = 0.0001.
- **Q3 holds.**

## Q12 a clustering of B agrees with A
- signs clustered in both: 64; pairs together in both 74; p = 0.0002.
- **Q12 holds.**

## Q4 clusters differ in position in B
- B name tokens in A clusters: 1164; MI(cluster; position) 0.100 bits; p = 0.3596.
- **Q4 fails.**

## Q14 clusters have a dominant position
  - cluster 0: inside 42%, first 35%, last 23%
  - cluster 1: last 53%, inside 27%, first 20%
  - cluster 2: last 50%, inside 31%, first 18%
  - cluster 3: last 44%, inside 42%, first 14%
  - cluster 4: inside 50%, first 50%
  - cluster 5: inside 72%, last 24%, first 3%
  - cluster 6: first 58%, last 22%, inside 19%
  - cluster 7: first 43%, inside 35%, last 22%
- clusters with 60%+ of tokens in one position: 1 of 8; threshold 4.
- **Q14 fails.**

## Q5 clusters differ in the ending
- B names with a clustered last sign: 443; MI(cluster; ending) 0.241 bits; p = 0.0041.
- **Q5 holds.**

## Q13 coverage of B
- B tokens covered: 5083 of 5451 (93.2%); threshold 70%.
- **Q13 holds.**

## Q6 clusters and picture categories
- categorised content signs: 50; MI 1.335 bits; p = 0.0048.
- **Q6 holds.**

## Q7 human figures cluster together
- human-figure signs clustered: 97:0, 100:1, 125:2, 142:6, 154:4; same-cluster share of their pairs 0.00; p = 1.0000.
- **Q7 fails.**

## Q15 heads are concentrated
- head-class signs clustered: 15; largest share in one cluster 7 (cluster 1, 47%); threshold 50%.
- **Q15 fails.**

## Q8 seals and tablets use different clusters
- seals and tablets: units 3184; MI 0.0142 bits; p = 0.0010 (1,000 permutations: token lists per unit).
- **Q8 holds.**

## Q9 Mohenjo-daro and Harappa seals use different clusters
- Mohenjo-daro and Harappa seals: units 1294; MI 0.0009 bits; p = 0.8312 (1,000 permutations: token lists per unit).
- **Q9 fails.**

## Q11 foreign texts use different clusters
- West Asian and home lines: units 3788; MI 0.0013 bits; p = 0.0919 (1,000 permutations: token lists per unit).
- **Q11 fails.**

## Q10 clusters differ in graphic complexity
- signs with a glyph: 115; between-cluster variance of complexity 86469; p = 0.0102.
- **Q10 holds.**

## Summary

Held: Q2, Q3, Q12, Q5, Q13, Q6, Q8, Q10. Failed: Q1, Q4, Q14, Q7, Q15, Q9, Q11.
