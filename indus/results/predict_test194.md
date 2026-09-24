# Hundred-and-ninety-fourth registered predictions: decipherment loop 19, graphic families as context

- fixed split: base 4.7124 (weights {'tri': 0.5555555555555556, 'pos': 0.11111111111111112, 'end': 0.3333333333333333}), with families 4.6973 (weights {'tri': 0.5, 'pos': 0.08333333333333334, 'end': 0.33333333333333337, 'ftri': 0.08333333333333334}).

## FB1 S improves on the fixed test
- S 4.7124 -> 4.6973 (gain 0.0151); threshold 0.005.
- **FB1 holds.**

## FB2 the gain replicates A -> B
- trained on 1916 A lines, tested on 1175 B lines: 5.2593 -> 5.2372 (gain 0.0221).
- **FB2 holds.**

## FB3 random families gain less
- decade gain 0.0151; random gains -0.0024, -0.0017, -0.0017, -0.0017, -0.0014, -0.0012, -0.0012, -0.0012, -0.0012, -0.0012, -0.0012, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0004, 0.0004, 0.0004, 0.0004; decade larger in 20 of 20.
- **FB3 holds.**

## FB4 decades beat hundred blocks
- gain decade 0.0151, hundred blocks -0.0012.
- **FB4 holds.**

## FB5 ftri gets weight
- fixed 0.083, A->B 0.077.
- **FB5 holds.**

## FB6 progress rule
- FB1 True, FB2 True.
- **FB6 holds.**

## Summary

Held: FB1, FB2, FB3, FB4, FB5, FB6. Failed: none.
