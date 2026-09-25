# Two-hundred-and-sixty-eighth registered predictions: decipherment loop 93, a grammar prior for the SIGN task

- development split: 0.00: 40.7% / 59.8%; 0.25: 40.6% / 59.8%; 0.50: 40.6% / 60.0%; 1.00: 40.8% / 60.1%; 1.50: 40.8% / 60.0%; 2.00: 40.9% / 60.2%; 3.00: 41.0% / 60.0%; alpha chosen 3.00.
- test (2340 signs): two-direction 39.9% / 61.8%; with grammar prior 39.8% / 62.1%.

## GP1 SIGN top-1 rises by 0.5 point or more
- 39.9% -> 39.8%.
- **GP1 fails.**

## GP2 SIGN top-5 does not fall
- 61.8% -> 62.1%.
- **GP2 holds.**

## GP3 the development split gives the grammar prior weight (alpha > 0)
- alpha 3.00.
- **GP3 holds.**

## GP4 progress rule: GP1 and GP2
- SIGN 39.8% / 62.1%.
- **GP4 fails.**

## Summary

Held: GP2, GP3. Failed: GP1, GP4.
