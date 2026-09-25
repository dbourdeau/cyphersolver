# Three-hundred-and-forty-fifth registered predictions: decipherment loop 170, an adaptive alpha for the true-duplicate referent pool

- alpha 0.00250: 100 units, FDR 10.1%, coverage 2.82%.
- alpha 0.00225: 99 units, FDR 9.3%, coverage 2.80%.
- alpha 0.00238: 99 units, FDR 9.6%, coverage 2.80%.
- alpha 0.00244: 100 units, FDR 10.2%, coverage 2.82%.
- alpha 0.00241: 100 units, FDR 9.8%, coverage 2.82%.
- chosen alpha 0.00241, coverage 2.82%; Linear B: recovered a-mo-ta, ko-wa; wrong none.

## AB1 the adaptive alpha covers more than 2.80% with FDR <= 10%
- alpha 0.00241: 2.82%.
- **AB1 holds.**

## AB2 Linear B with it: 2+ of 4 control words, none wrong
- recovered 2, wrong 0.
- **AB2 holds.**

## AB3 progress rule: AB1 and AB2 (the referent line uses the adaptive alpha)
- AB1 True, AB2 True.
- **AB3 holds.**

## Summary

Held: AB1, AB2, AB3. Failed: none.

## Audit after the test (added before recording)

The gain is one unit (2.80% -> 2.82%), and the chosen alpha sits where the FDR estimate crosses 10%: estimates from 100
shuffles with different seeds vary by about a point (0.00244 gave 10.2%, 0.00241 9.8%), so the choice selects on the
noise of the estimate. Withdrawn: the line stays at 2.80%. Lesson: an alpha step must clear the FDR rule by more than
the estimate's noise.
