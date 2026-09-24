# Two-hundred-and-fifth registered predictions: decipherment loop 30, a key scorer against the Linear B gate; two-direction WORD

- design (odd lines), order 2: real -4.544, shuffles median -4.692, as good 4 of 100.
- design (odd lines), order 3: real -4.430, shuffles median -4.631, as good 0 of 100.
- design (odd lines), order 4: real -4.410, shuffles median -4.651, as good 0 of 100.
- design (odd lines), order 5: real -4.291, shuffles median -4.572, as good 0 of 100.
- chosen order 5.

## GA1 Greek model: Ventris's key beats 95 of 100 shuffles
- real -4.247 bits/char; shuffles median -4.565 (-4.730 to -4.473); 0 of 100 as good.
- **GA1 holds.**

## GA2 Sanskrit model: not language-blind
- real -4.702; shuffles median -4.756; 9 of 100 as good.
- **GA2 holds.**

## GA3 larger margin with Greek
- margin over shuffle median: Greek 0.318, Sanskrit 0.054 bits/char.
- **GA3 holds.**

## GA4 two-direction WORD, fixed test
- top-10 forward 3.0%, two-direction 3.9% (232 names).
- **GA4 fails.**

## GA5 and A -> B
- top-10 forward 2.5%, two-direction 2.5% (81 names).
- **GA5 fails.**

## GA6 progress rule
- gate True; WORD False.
- **GA6 holds.**

## Summary

Held: GA1, GA2, GA3, GA6. Failed: GA4, GA5.
