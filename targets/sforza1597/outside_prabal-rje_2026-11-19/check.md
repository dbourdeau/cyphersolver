# The check of the decodes

## 1. What was compared

- **My rows against my frozen read:** the rows give the signs in the order of the read. On most pages, the count of signs (the signs that I do not read left out) equals the count of places in the read. On a page whose read gives one line for each cipher row (R5445 p1, R5521 p3, R5542 p1), the read keeps a place for each sign that I do not read, and the counts agree with those signs included.
- **The decode against my frozen read:** on each place where the frozen read shows a letter, does the key give the same letter? "Agree" counts these places.
- **The key of each page:** "a run file's key" is the key of my solve of that page or of its group; "the frozen read's table" gives each label the value that the frozen read shows most often.

## 2. The pages from ciphertext

| Page | Key | Signs | Letters shown in the frozen read | Agree | Labels with two or more letters |
| --- | --- | ---: | ---: | ---: | ---: |
| R5415 p1 | a run file's key | 914 | 813 | 780 (95.9%) | 12 of 41 |
| R5416 p1 | a run file's key | 759 | 719 | 687 (95.5%) | 9 of 39 |
| R5419 p1 | a run file's key | 1,031 | 901 | 752 (83.5%) | 18 of 33 |
| R5421 p1 | a run file's key | 1,397 | 1,028 | 885 (86.1%) | 21 of 43 |
| R5432 p1 | a run file's key | 1,443 | 1,076 | 857 (79.6%) | 21 of 42 |
| R5439 p1 | a run file's key | 697 | 640 | 613 (95.8%) | 13 of 55 |
| R5445 p1 | the frozen read's table | 225 | 161 | 161 (100.0%) | 0 of 44 |
| R5453 p1 | a run file's key | 526 | 502 | 483 (96.2%) | 11 of 50 |
| R5453 p2 | a run file's key | 185 | 179 | 169 (94.4%) | 5 of 26 |
| R5456 p1 | a run file's key | 628 | 571 | 538 (94.2%) | 15 of 38 |

In all: 5,925 of 6,590 shown letters agree (89.9%).

## 3. Which key each page rests on

- **A run file's key:** R5415 p1, R5416 p1, R5419 p1, R5421 p1, R5432 p1, R5439 p1, R5453 p1, R5453 p2, R5456 p1.
- **The frozen read's table:** R5445 p1.
- **Key not confirmed:** R5445 p1. It has, on average, under 9 signs for each label, and no key sheet and no clear passage checks its key.

## 4. Limits

- No key sheet and no clear text checks the pages from ciphertext. "Agree" compares my decode with my own read; it does not measure whether a letter is right.
- On a page that rests on the frozen read's table, the table comes from that read, so "Agree" there is high by construction.
- The ledger's checker `docs/_check_reading.py` did not run on this folder.
- This folder adds no hash table and no other record of provenance.

Credit: DECODE, the database of historical ciphers of the DECRYPT project (the records named here; https://de-crypt.org/decrypt-web/RecordsView/ followed by the record number); Archivio di Stato di Milano, Carteggio Sforzesco; M. Héder and B. Megyesi (2022), HistoCrypt, https://doi.org/10.3384/ecp188397. No DECODE image is published.
