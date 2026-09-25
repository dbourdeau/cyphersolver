# Two-hundred-and-fifty-seventh registered predictions: decipherment loop 82, an infill component for the SIGN task

- development split: 0.00: 40.7% / 59.8%; 0.25: 40.9% / 60.0%; 0.50: 40.7% / 59.6%; 1.00: 40.2% / 59.4%; 1.50: 39.9% / 58.9%; 2.00: 39.2% / 58.7%; 3.00: 37.8% / 57.8%; alpha chosen 0.25.
- test (2340 signs): two-direction 39.9% / 61.8%; with infill 39.4% / 62.2%.

## IF1 SIGN top-1 rises by 0.5 point or more
- 39.9% -> 39.4%.
- **IF1 fails.**

## IF2 SIGN top-5 does not fall
- 61.8% -> 62.2%.
- **IF2 holds.**

## IF3 the development split gives the infill weight (alpha > 0)
- alpha 0.25.
- **IF3 holds.**

## IF4 progress rule: IF1 and IF2
- SIGN 39.4% / 62.2%.
- **IF4 fails.**

## Summary

Held: IF2, IF3. Failed: IF1, IF4.
