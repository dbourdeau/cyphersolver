# Hundred-and-twenty-fifth registered predictions: beating the benchmark

- benchmark (tri + pos) 4.915 bits per sign.

## BB1 lines are anchored at the end
- distance-from-end 5.457, from-start 6.022; threshold 0.1.
- **BB1 holds.**

## BB2 end distance in the benchmark
- tri + end 4.902 against 4.915; threshold 0.05.
- **BB2 fails.**

## BB3 better smoothing
- add-one bigram 6.384, discounted 4.987; threshold 0.5.
- **BB3 holds.**

## BB4 better smoothing inside the benchmark
- with discounting 4.680 against 4.915; threshold 0.1.
- **BB4 holds.**

## BB5 shape blocks help unseen signs
- new F lines: 5.690 without, 5.444 with block backoff; threshold 0.1.
- **BB5 holds.**

## BB6 line length matters
- with length-position 4.915 against 4.915; threshold 0.05.
- **BB6 fails.**

## BB7 the first sign sets the line
- with first-sign term 4.911 against 4.915; threshold 0.05.
- **BB7 fails.**

## BB8 under 4.8 bits
- best model (kn + extra end term) 4.659; threshold 4.8.
- **BB8 holds.**

## BB9 under 5.5 on new lines
- new F lines 5.644; threshold 5.5.
- **BB9 fails.**

## BB10 the gain holds on B
- B benchmark 4.712, best 4.515.
- **BB10 holds.**

## Summary

Held: BB1, BB3, BB4, BB5, BB8, BB10. Failed: BB2, BB6, BB7, BB9.
