# Hundred-and-twenty-third registered predictions: does structure improve prediction?

- bigram 6.384 bits; role weight fitted on training slice 0.50.

## BM1 roles improve prediction
- bigram 6.384, with roles 5.856; threshold 0.1 bit.
- **BM1 holds.**

## BM2 genre helps
- bigram 6.384, genre-mixed 6.170; threshold 0.1 bit.
- **BM2 holds.**

## BM3 position helps
- unigram 6.330, position-aware 5.429; threshold 0.5 bit.
- **BM3 holds.**

## BM4 the recorded direction reads better
- forward 6.384, reverse 6.384; threshold 0.05 bit.
- **BM4 fails.**

## BM5 the ending helps find the head
- without 38.2%, with 41.6%; threshold +5 points.
- **BM5 fails.**

## BM6 common heads fix the ending
- accuracy 89.6% over 202 names; threshold 95%.
- **BM6 fails.**

## BM7 signs avoid repeating
- bigram 6.384, no-repeat 6.392; threshold 0.02 bit.
- **BM7 fails.**

## BM8 names have longer dependencies
- trigram gain names 0.736, counts 0.654 bits.
- **BM8 holds.**

## BM9 each city has its own sequences
- Harappa test: Harappa-trained 6.638, Mohenjo-daro-trained 6.777; threshold 0.3 bit.
- **BM9 fails.**

## BM10 names and counts are different sequences
- names 5.524, counts 7.552; threshold 1 bit.
- **BM10 holds.**

## BM11 the transcriptions write alike
- B test: B-trained 5.961, A-trained 6.820; threshold within 1 bit.
- **BM11 holds.**

## BM12 roles help most where data is thin
- role gain on small sites 0.599, on held-out lines 0.529.
- **BM12 holds.**

## Summary

Held: BM1, BM2, BM3, BM8, BM10, BM11, BM12. Failed: BM4, BM5, BM6, BM7, BM9.
