# Two-hundred-and-seventh registered predictions: decipherment loop 32, blind key fitting on Linear B

- seed 1, Greek: held-out real -2.762, shuffled -2.787, gain 0.024 bits/char.
- seed 1, Sanskrit: held-out real -2.451, shuffled -2.812, gain 0.361 bits/char.
- seed 1, Dravidian: held-out real -3.018, shuffled -3.215, gain 0.197 bits/char.
- seed 1, Sumerian: held-out real -3.174, shuffled -3.369, gain 0.195 bits/char.

## KF1 Greek has the largest gain
- order: Sanskrit 0.361, Dravidian 0.197, Sumerian 0.195, Greek 0.024.
- **KF1 fails.**

## KF2 by 0.05 bits/char or more
- Greek 0.024, next Sanskrit 0.361.
- **KF2 fails.**

## KF3 the fitted Greek key agrees with Ventris
- 0 of 30 commonest signs ().
- **KF3 fails.**

## KF4 second seed
- order: Sanskrit 0.328, Dravidian 0.247, Greek 0.216, Sumerian 0.157.
- **KF4 fails.**

## KF5 every gain positive
- seed 1 Greek 0.024, Sanskrit 0.361, Dravidian 0.197, Sumerian 0.195.
- **KF5 holds.**

## KF6 progress rule
- KF1 False, KF4 False.
- **KF6 fails.**

## Summary

Held: KF5. Failed: KF1, KF2, KF3, KF4, KF6.
