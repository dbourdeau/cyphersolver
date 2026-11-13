# Partial reads of R5463, R5464 and R5465: keys, decodes and checks

These are partial reads from the ciphertext alone, not checked against a key. They are not readings. By this repository's read bar, letters judged by language models are not a reading, and we accept that bar.

A sign is one written sign, as the ledger's `tokens.txt` gives it. A shown letter is not a letter read.

## The files

- `<record>/key.tsv`: our key, in the sign labels of `ctts/<record>_best/tokens.txt`.
  - `letter`: the best key of the main hill.
  - `firm`: whether the 20 best keys agree on that letter.
  - `tokens`: the number of signs of that label.
  - `decoded_as` and `share`: the value that the decode gives the label most often, and its share. `null` is a sign with no letter.
- `<record>/decode.txt`: our decode. It has one line for each line of `tokens.txt` and one character for each sign.
  - A letter is a shown letter.
  - `.` is a sign with no shown letter, including a sign that the decode takes as a null.
  - R5464 line 50 (30 signs) is all dots. We left it out as the archive stamp.
  - The letters fold u and v to `u`, i, j and y to `i`, and c and k to `c`.
- The decode uses a fitted sign table, so `key.tsv` alone does not give `decode.txt`.

## The method in ten lines

1. The letter model: the printed Milanese ambassadors' dispatches of the 1460s and 1470s (Mandrot; Gingins-La Sarra), 1.32 million letters.
2. 100 starts for each record, each annealed for 600,000 moves on an order-5 letter model.
3. 50 fresh starts (5 from the sign counts, 45 random) and 50 starts from the best fresh key with 15% of labels changed.
4. No start used this folder's keys or a key sheet.
5. A start is on a hill when it gives the hill's letter on at least 90% of the signs.
6. EM fits a table of P(sign | letter), with nulls and missed letters, from each distinct key of the main hill.
7. The decode takes the most probable letter at each sign, under an order-4 letter model.
8. A letter shows only when its label is firm, all main-hill decodes agree, and its probability is at least 0.7.
9. We fixed the table form and the 0.7 on artificial letters, before any real result.
10. Artificial letters of each size measure how many shown letters are right.

## The numbers

| Record | Signs | Signs that show a letter | Shown letters that make sense, by two blind readers | The same, of all signs | Fresh starts on the main hill |
| --- | ---: | ---: | ---: | ---: | ---: |
| R5463 | 1,372 | 78.0% (1,070) | about 65% to 75% | 51% to 59% | 16 of 50 |
| R5464 | 3,249 | 86.4% (2,808) | about 65% to 70% | 56% to 61% | 36 of 50 |
| R5465 | 5,828 | 68.0% (3,961) | about 55% | 37% | 31 of 50 |

- The blind readers are two large language models. Each saw our decode and two shuffled copies, with no name, date or source. Their shares are estimates, not counts.
- On R5464, the maintainer found that our shown letters equal the letters of the refined key in `ctts/r5464_best/` on 89.7% of the shown signs. Our main key gives that key's letter on 86.6% of all signs.

## The artificial letters

Each artificial letter is a printed dispatch from a volume that the letter model of the tests leaves out. A key shaped like a key of 1446 in the same box enciphers it. A simulated sign reader then misses, adds, splits and joins signs.

| Size of | Lower noise: shown letters right | Twice the noise: shown letters right |
| --- | --- | --- |
| R5463 | 86.5%, 90.0% and 85.6% | 88.2%; 48.9% with a wrong key |
| R5464 | 94.7%, 92.3% and 92.8% | 89.9%; 0.3% with a wrong key |
| R5465 | no test | no test |

## The limits

- No key sheet and no clear text checks these reads. Nobody has checked a decoded word against the ink.
- The signs are this folder's machine transcription, with about 10% errors by the maintainer's estimate. Our keys share its errors.
- At each tested size, one artificial letter of five ended on a wrong key. The display rule did not catch it.
- R5463 has a rival hill: 17 fresh starts, 5.2 lower in score. It differs on 15 labels, and 125 of the 1,070 shown letters fall on them.
- A pair-keeping shuffle of R5463 still shows a letter on 55% of its signs. So the shown share is no evidence by itself.
- R5465 has no artificial letters of its own, so its accuracy is not measured.
- Our letter model can write words that are common in the dispatches. A single word proves little.

## What did not read

The same method did not read family E1 (R5437, R5443, R5444, R5445, R5447 and R5467, `ctts/e1.txt`). No fresh start ended on a main hill, and the 100 starts ended on 95 hills. We dropped lines 1, 25 and 26 as clear writing before the fit.

## Credits

- DECODE, the database of historical ciphers of the DECRYPT project: records R5463, R5464 and R5465. The documents are in the Archivio di Stato di Milano, Carteggio Sforzesco, cartella 1597.
- The sign transcription is the work of this repository's maintainer. Every key here uses his labels and his tokens.
- He read part of R5464 first (7 November 2026), and his key found its main letters first.
- He saw fragments of R5463 first: "desideroso", "sperare" and "perche".
- Our public pages, with the readings of R5463 and R5464 in Italian and English: https://github.com/prabal-rje/branicki-1757/tree/main/sforza-1597
