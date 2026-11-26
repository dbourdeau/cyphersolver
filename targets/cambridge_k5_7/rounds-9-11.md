# K5.7 and T-S Misc.22.218, rounds 9–11

## Round 9. How far is each row from one complete Hebrew alphabet?

The five tests were four separate row minima and a joint minimum with one Hebrew value for the repeated sign X. For a 22-cell row, count each secure occurrence of a letter after the first. Each excess occurrence requires one change, and that many changes suffice if all unresolved cells may be filled freely. I tried every value of X and every way of omitting one interior position from the longer row 2. Lost cells, doubtful readings, and unidentified signs other than X were free. Costs count cell substitutions, independently by occurrence. A systematic misidentification could affect more than one occurrence.

| Row | Repeats among secure letters before assigning X or omitting a cell | Minimum substitutions |
|---|---|---:|
| 1 | waw twice, kaph twice | 2 |
| 2 | waw, yod and nun twice each | 2 after one omission |
| 3 | he twice, waw twice | 2 |
| 4 | waw three times | 2 |
| All four with a shared X | Minimum over 506 combinations of omission and value | 8 plus one omission |

Lamed, pe and resh each attain eight. For every other ordinary Hebrew value the minimum is nine to eleven. The omissions that attain eight are interior positions 2, 3, 8, 11, 17 and 22 in row 2. The common feature of the three best values is that none adds a duplicate to the relevant securely read rows. A previously suggested visual resemblance of X to resh cannot turn this inventory tie into an identification. The bound tests the specific model of one complete alphabet per row, with the ordinary 22 consonants as outputs. It leaves other uses of alphabets or permutations open.

## Round 10. Five new routes for the seven-sign recipe sequence

I kept the published consonant values and searched the 4-by-22 interior for the recipe sequence in either direction. Each trial permitted a single row 2 omission. Counts are distinct, fully secure, oriented seven-letter strings, pooled across omissions. Windows with an unresolved cell supply no positive evidence and were excluded.

| Route | Distinct strings | Best positional agreement out of seven |
|---|---:|---:|
| Alternate between two rows while advancing a column | 224 | 2 |
| Bounce diagonally between the top and bottom rows | 64 | 2 |
| Wrap diagonally, advancing one row and one or two columns per step | 216 | 2 |
| Follow a rectangular spiral from a corner | 161 | 2 |
| Alternate between opposite ends of a row, working inward | 40 | 1 |

No complete visible match. This search cannot exclude a route through a damaged or uncertain cell.

## Round 11. Five possible second substitutions

I tested the seven-sign recipe sequence against fully secure horizontal windows in K5.7, including the legible borders and both orientations. There were 28 distinct oriented strings. Each of the following produced zero exact matches.

1. A constant alphabetic shift modulo 22.
2. An invertible affine substitution modulo 22.
3. Separate constant shifts at odd and even positions.
4. An arbitrary one-to-one substitution fixing aleph, yod, he and waw.
5. An arbitrary one-to-one substitution that is its own inverse.

As a positive control, I replaced the recipe target with the known seven-letter interior opening of the even rows. Every method recovered that opening. The control checks detection of an exact match and does not address manuscript damage. These five models were tested on horizontal windows, independently of the five routes.

Rounds 10 and 11 yielded no new reading, witness, or independently supported rule. This reached the two-round stopping condition. [Runnable tests](recipe_rounds.py) · [Source transcription](check.py) · [Recipe witness and source](NOTES.md)
