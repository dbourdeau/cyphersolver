# Checks of the decode

Credit:

- DECODE, the database of historical ciphers of the DECRYPT project: records R9873 to R9905 (30 records with rows; R9902 has none).
- The record pages: https://de-crypt.org/decrypt-web/RecordsView/ followed by the number, for example https://de-crypt.org/decrypt-web/RecordsView/9873.
- Real Academia de la Historia, Madrid, Colección Salazar y Castro A-31 (9/31) and A-34 (9/34).
- Héder and Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- No DECODE image is published.

All numbers are real unless marked "planted".

## 1. What kind of decode this is

- From key: the ledger's key KS4, with the values that I added. No key was searched or fitted for the decode.
- Two departures from KS4: `qes` reads es (`key_working.md` pass 3; 174 units), and `njn` (ha / han) shows the value before the slash (40 units).
- Every record is decoded, not read. No record builds sentences, so no record has a reading, a translation or a read share. Section 3 gives the words as an estimate.
- I did not run `docs/_check_reading.py`.

## 2. The decode is the output of the key

- `key/decode.py` applies `key/key.tsv` to the rows files alone. It gives every decode line of the record pages: 1,347 of 1,347 rows.
- The lookup puts a unit in lower case, reads the long s as s and drops a final `~` (the switch `f~` keeps it). It looks in the scope of the page, then in scope `all`.
- Apart from the opener, each label has one value in its scope. The opener rule stands outside the table: `v` followed by `db` is `v db`, with no letter.
- A ledger-key value is marked doubtful when the unit ends in `~` or the table names a doubt.

## 3. The units, counted by kind

| Kind | Units |
| --- | ---: |
| Cipher units, as I classify them (the units of the rows less 364 clear words) | 20,998 |
| Read by the ledger's key, a letter value, no doubt mark | 12,351 |
| Switch marks and openers (no letter), no doubt mark | 760 |
| Read by the ledger's key, with a doubt mark | 2,200 |
| Read by an added entry, a letter value | 1,039 |
| Read by an added entry, a null | 147 |
| (of the 1,186 added-entry units: with my `~` doubt in the rows, not marked in the decode) | (246) |
| A value of the clerk copies only (`[x]`), not counted as read | 1,094 |
| No value (`·`) | 3,407 |
| `?` positions of the rows (`…`), not counted as cipher units; some may be cipher signs that I did not read | 4,910 |

- The number "68.1%" of our repository is (12,351 + 760 + 1,039 + 147) / 20,998 = 14,297 / 20,998. It is a share of units. It is not a read share by the word rule of this ledger.

**Words, estimated** (the tokens of the decode lines; see README.md, "Words, estimated"):

| Kind | Words |
| --- | ---: |
| Words | 9,640 |
| Sure by the ledger's key alone | 4,343 |
| Sure with my added values | 4,906 |
| Holes | 4,734 |

## 4. The added values

62 values were fixed from clear texts of the same letters, and `cib` from two copies of one dispatch read with the key (`key/added-values.tsv`):

- Each cipher row, read with the key, was aligned with a clear text. A row counted only when it aligned better than every row aligned with an unrelated Spanish text of the 15th century.
- A unit with no value got a candidate where the units on each side matched the clear text letter for letter, with 2 or more exact letters on each side.
- A value entered the key when 2 or more places agreed, or when one place agreed with a value of the clerk copies. These rules changed no value of the ledger's key.

**Checks before the real run.** "Wrong" counts units. The go rule: at most 0.10 wrong.

| Check | Units | 2 or more places | 1 place and a clerk value | 1 place alone |
| --- | ---: | --- | --- | --- |
| Planted letter (planted) | 841 open | 548 right, 0 wrong | not run | 125 right, 2 wrong |
| Harder planted letter: rare labels, 0.10 label errors (planted) | 1,024 open | 192 right, 0 wrong | not run | 287 right, 106 wrong |
| Known answers on the real rows, period decipherments | 1,537 hidden | 1,040 right, 0 wrong | 181 right, 0 wrong | 195 right, 54 wrong |
| Known answers on the real rows, published texts | (the same) | 108 right, 0 wrong | 38 right, 0 wrong | 112 right, 18 near |

- One place alone failed two checks. So its values stay out of the key and out of this folder.
- In the "1 place and a clerk value" column, weak clerk values gave 15 right and 0 wrong. That is few units.

**Held out.** Values fixed on one part of the clear texts; places of the other part compared with them.

| Split | Compared | Same | Share | Floor (values shuffled) |
| --- | ---: | ---: | ---: | ---: |
| By dispatch, part A to part B | 5 | 3 | 0.600 | 0.088 |
| By dispatch, part B to part A | 3 | 2 | 0.667 | 0.107 |
| By rows, half 1 to half 2 | 13 | 9 | 0.692 | 0.057 |
| By rows, half 2 to half 1 | 17 | 10 | 0.588 | 0.054 |

- The counts are small.

**The ledger's key against the clear texts.** Units that the key reads, between two exact neighbours:

- period decipherments: 626 agree, 68 differ by one letter, 22 differ more;
- published texts: 882 agree, 77 differ by one letter, 15 differ more.
- Most of the larger differences are abbreviations in the clear text. I changed no value of the key.

**The clerk copies.** The 308 units with a clerk value that the "2 or more places" values read all equal the clerk's value.

## 5. The ledger's key against the decipherments of the time (17 November 2026, before the added values)

- For 632 rows of 13 records, a clerk's clear text stands beside the cipher: in a clear copy, in the margin or between the lines.
- Measure: the share of read letters that fall in blocks of 3 or more letters that match the clerk's text. Floor: the same measure against the clerk's text of another row.
- All 632 rows: 0.369 (13,389 read letters); floor 0.068.
- By record: R9893 0.774; R9881 0.666; R9896 0.530; R9889 0.490; R9897 0.463; R9884 0.442; R9895 0.431; R9883 0.406; R9900 0.335; R9890 0.326; R9899 0.193; R9898 0.182; R9901 0.068.
- The ledger built its key in part from these decipherments. So this is agreement, not a held-out test.

## 6. These rows against the ledger's readings (17 November 2026, before the added values)

| Records | Ledger text | Blocks of 8 letters | Floor | Blocks of 3 letters | Floor |
| --- | --- | ---: | ---: | ---: | ---: |
| R9873 and R9874 | reading of R9873 | 0.453 | 0.104 | 0.842 | 0.757 |
| R9877 and R9878 | reading of f. 128 | 0.248 | 0.000 | 0.776 | 0.459 |
| R9898 | reading of R9898 | 0.213 | 0.067 | 0.772 | 0.746 |

- Blocks of 3 letters match often by chance on long texts. Blocks of 8 are the better measure.
- 27 of the added values rest only on these three readings. So they are not a check of those values.

## 7. Copies among the records (17 November 2026)

The decode of one record against the decode of another, in blocks of 8 letters. The floor uses a third record.

| Pair | Match | Floor | Reading of the pair |
| --- | ---: | ---: | --- |
| R9874 and R9873 | 0.712 | 0.011 | the same letter |
| R9892 and R9893 | 0.544 | 0.000 | a copy |
| R9880 and R9881 | 0.379 | 0.053 | a copy |
| R9876 and R9873 | 0.373 | 0.029 | a copy of part |
| R9879 and R9881 | 0.299 | 0.000 | a copy |
| R9875 and R9873 | 0.275 | 0.088 | probably the duplicate |
| R9883 and R9884 | 0.194 | 0.096 | shared passages |
| R9889 and R9890 | 0.166 | 0.043 | shared passages |
| R9904 and R9905 | 0.156 | 0.090 | shared passages |
| R9896 and R9897 | 0.097 | 0.057 | different letters |
| R9877 and R9878 | 0.056 | 0.000 | poor rows in R9878 |

## 8. One key for all pages (17 November 2026)

- Groups of pages from the counts of sign pairs on each page, with no key, could mean different keys.
- Each of the four groups matches the clerks' texts above its floor: 0.558 (floor 0.076), 0.310 (0.066), 0.193 (0.074) and 0.326 (0.055).
- This supports one key for all pages. It does not rule out small differences between keys, and it does not show what else makes the groups differ.

## 9. Not checked

- The English summaries, line by line.
- Whether the clear leaves of R9892, R9893 and R9895 are the same leaves as the clerk texts behind the clerk values. If they are, some added values rest on one source twice.
- The clear texts as I transcribed them (BNE MSS/20214/52-1 and the leaves ff. 482, 485 and 516): they have uncertain places of their own.
- The ledger's checker `docs/_check_reading.py`: it did not run.
