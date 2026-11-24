# Francia 346: the key table and the frozen key-free read

This folder holds two things. One is the key that the decode uses, with the source of each value. The other is the read that I made with my own key. I fixed that key before I first opened the published key, and no value of the published key entered the read. Every number here is real.

Credit: DECODE, the database of historical ciphers of the DECRYPT project, records of Francia 346. Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346.

## The files

| File | What it holds | Where it comes from |
| --- | --- | --- |
| `key.tsv` | every code of the decode: its value on the pages, its grade, the source of the value, the published value and my key-free value | the published key; the cipher ledger's files; my frozen key |
| `DECLARE.md` | the method of the key-free read of the 22 records, written before any count on them | my frozen file of 16:12, 12 November 2026 (UTC−3) |
| `READ-digit.md` | that read, row by row, with its measures | my frozen file of 17:00, 12 November 2026 (UTC−3) |
| `key-free-key.tsv` | the key found from the ciphertext alone | fixed at 01:27, 12 November 2026; the same rows as [`francia-346-leaves/key.tsv`](https://github.com/prabal-rje/branicki-1757/blob/main/francia-346-leaves/key.tsv) in our repository, with one credit line added |

- **The two frozen files** are edited copies. Each copy says so in its opening note. No number, no rule and no decoded row changed. The unchanged files stay in my own records. The kinds of edit:
  - local paths and file names became "a local file";
  - one work-log number and the model names were cut;
  - the names of my working sessions became plain words, such as "the earlier key-free work";
  - one sentence on what nobody may publish now names the DECODE images, as it meant;
  - the list of local code and result files at the end of the read became one line;
  - the declaration's file name lost a session label (`DECLARE.md`).
- **The decode itself** is in the record pages of [this target](../): read with the known key, from a machine transcription that nobody verified.

## The order of events

All times are UTC−3, on 12 November 2026.

1. **01:27:** the key-free key was fixed. Its fit used 13 records: R74 to R78, and earlier transcriptions of R5626, R5635, R5636, R5637, R5640, R5643, R5647 and R5648.
2. **01:40 to 02:00:** I opened the published key for the first time, to compare my fixed key with it. The key and that check are in our repository. My key did not change after it.
3. **16:12:** the declaration of the method of the read.
4. **17:00:** the read of the 22 records was fixed.
5. **About 17:05:** I applied the published key to these 22 records. The grade and the full decode came after it.

These times rest on my own record. This folder adds no hash table and no other record of provenance.

## The key of the decode (`key.tsv`)

- **Pair codes:** the published key gives 61 pair codes: 40 letter codes and 21 syllable codes. Its authors are George Lasry, Beáta Megyesi and Nils Kopal (2020; DECODE key note of 24 October 2020).
- **The form:** a lone 6 is a word space, and the ten pairs 2x are nulls. The cipher ledger rebuilt this form from Lasry's readings (`targets/ceva1632/cipher.py`).
- **Two pair values** come from the ledger's re-read of 22 to 23 October 2026: 88 is del, not quel; 33 is gli.
- **Three-digit codes:** the published key gives none. The values come from the ledger.
  - 14 are "certain" and 7 "probable": values that the ledger adopted.
  - 25 are "conjecture". Six of them are adopted values that these letters put in doubt.
  - The other 19 conjectures are values that the ledger read off decipherments of 1632 but did not adopt.
  - 129 (regno) is open: the ledger's re-read drops it in favour of 171.
  - `../README.md`, "The grades of the code values", gives the test behind the grades.
- **The column "key-free shown value"** gives the letter that my key-free key shows for each pair code, or `·` where it shows none.
- **The column "ledger mark"** marks each value from the cipher ledger:
  - `one of the 28`: the 28 three-digit values of the first pass, 22 from `cipher.py` and 6 from the re-read;
  - `ledger pair`: pairs 88 and 33, from the re-read;
  - `ledger form`: the word space 6 and the ten null pairs 2x;
  - `ledger, not adopted`: the 19 values that the ledger read off decipherments of 1632 but did not adopt.

## The numbers

- **The frozen read, graded** (`../check.md`): of the true letters that it shows, 98.8% are right (6,930 of 7,017). All 87 wrong letters are code 07: the published key gives h, my key gives l. Only 62.0% of its graded shown tokens are letter codes (7,017 of 11,324).
- **The decode of the 22 records** (`../README.md`): 10,919 code tokens. In the first pass, 10,081 had a value (92.3%). The graded pages give 515 three-digit tokens a value (142 certain, 131 probable, 242 conjecture) and leave 639 open. So 10,245 code tokens (93.8%) show a value.

## Words in the frozen files

- **pool "one2":** the 13 records of the key's fit. Pool "all" adds six records (the appendix key of `key-free-key.tsv`).
- **"H6":** the cut: a lone 6 is a word space, a lone 2 is a null, and the other digits form pairs.
- **"twin":** an artificial test text with a known key.
- **P5:** the odd share of the runs between two 6 signs that hold no 2.
- **"the earlier key-free work":** the work that found the key from the ciphertext alone ([`francia-346-leaves/`](https://github.com/prabal-rje/branicki-1757/tree/main/francia-346-leaves) in our repository).

## Limits

- The transcription is a machine transcription of the DECODE images. Nobody verified it.
- A. Leman (1920) used the Barberini library's minutes of the cipher despatches to Ceva. I did not check which letters those minutes hold.
- The scripts of the read, the grade and the decode are not in this folder.
- The digit rows that the read used are in [`../transcription/`](../transcription/).

## Credits

- **DECODE**, the database of historical ciphers of the DECRYPT project. https://de-crypt.org/decrypt-web/RecordsList
- **The archive:** Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346.
- **The key:** G. Lasry, B. Megyesi and N. Kopal, "Deciphering papal ciphers from the 16th to the 18th Century", *Cryptologia* 45(6), 2021 (online 2020), doi:10.1080/01611194.2020.1755915.
- **The ledger's values:** the cipher ledger, https://github.com/dbourdeau/cyphersolver, `targets/ceva1632`.
