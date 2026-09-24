# Hundred-and-seventy-sixth registered predictions: decipherment loop 1, structure and roles

- baseline mixture (tri + pos + end, EM weights): 4.712 bits per sign.

## LP1 adding role
- 4.712 against 4.712 (gain 0.000; weight 0.00); threshold 0.03.
- **LP1 fails.**

## LP2 adding cls
- 4.712 against 4.712 (gain -0.000; weight 0.00); threshold 0.03.
- **LP2 fails.**

## LP3 adding nval
- 4.712 against 4.712 (gain -0.000; weight 0.00); threshold 0.02.
- **LP3 fails.**

## LP4 the best combination
- all three 4.712 against 4.712 (gain -0.000; weights tri 0.52, pos 0.11, end 0.36, role 0.00, cls 0.00, nval 0.00); threshold 0.05.
- **LP4 fails.**

## LP5 the modifier role
- R 56.2% -> 76.9% (+2485 modifier tokens, numerals already counted).
- **LP5 holds.**

## LP6 modifiers stay in name bodies
- test tokens of training modifiers inside name bodies: 295 of 515 (57%); threshold at least 80%.
- **LP6 fails.**

## LP7 heads stay heads
- test name-body tokens of training heads that are heads: 68 of 77 (88%); threshold at least 50%.
- **LP7 holds.**

## LP8 the gain holds on B
- B: 4.562 against 4.562.
- **LP8 holds.**

## Summary

Held: LP5, LP7, LP8. Failed: LP1, LP2, LP3, LP4, LP6.
