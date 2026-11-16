# Held-out test, written before the run (14 Nov 2026)

Split: the printed cipher letters in reading order (pass-1 transcription, person signs and clear text removed),
segments A1-A9 (the first 383 of 651 letters, about 59 per cent) are the training part; segments A10-B2 (268 letters)
are held out. (Two-thirds by segment boundary falls inside A10; the split is at the A9/A10 boundary so no segment is cut.)

Procedure: (1) derive a key from the training part only (solver plus hand cribs from the training part only);
(2) freeze it (sha256 of keys/frozen_key.json recorded in NOTES before step 3); (3) decode the held-out part with the
frozen key, choosing among a letter's frozen values by the same quadgram model (no change to the key);
(4) score: mean quadgram log-probability per letter of that reading; (5) control: 200 keys made by shuffling the
frozen key's values among the cipher letters (same set of value-sets, same number of two-valued letters), each
decoded the same way.

Success means all three:
- the frozen key's held-out score is above all 200 shuffled keys (empirical p < 0.005);
- the held-out reading contains at least five English words of four letters or more that were not used as cribs and
  that fit the context of the clear text around them (Brittany, Montpensier, Bouillon, Biron, the King, those of the
  religion, the army);
- it was not tuned on the held-out letters.

Anything less is reported as a failure of the held-out test, not as a reading.

## Frozen before the test run
keys/frozen_key.json: shifts (7, 8, 10) chosen on training letters only (350 letters, A1-A9; the 383 figure above was an estimate, the actual split is 350 training / 301 held out). sha256 70077576e3a9d501cb088b07203d26ccdb9e45f1136fb64d8c107a61fab3ce6f. Runner-up on training: (4, 7, 10), -4.092 against -4.082.
