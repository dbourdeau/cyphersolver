# Francia 346, the later letters: the check of the frozen read

This page grades my read of the 22 later digit records against the published key. I made that read without the key and froze it before the check. Every number here is real.

The transcription is a machine transcription of the DECODE images, made in my pipeline. Nobody verified it.

Credits: DECODE (DECRYPT project), records R5626 to R5659; Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346; the key: G. Lasry, B. Megyesi and N. Kopal (2020); the ledger values: the cipher ledger, https://github.com/dbourdeau/cyphersolver.

## 1. What was compared

- **My read:** a key found from the ciphertext alone on 13 records, fixed at 01:27 on 12 November 2026 (UTC−3). It was applied to the new pages with no fit, and that read was fixed at 17:00 the same day.
  - The 13 records include an earlier transcription of 8 of the 22 records here: R5626, R5635, R5636, R5637, R5640, R5643, R5647 and R5648. So those 8 are not independent of the fit.
  - The other 14 records were not in the fit.
  - The cut: a lone 6 is a word space, a lone 2 is a null, and the other digits form 80 pair codes.
  - The display: 69 of the 80 pair codes show a letter. The other 11 show a gap mark.
- **The key:** George Lasry's key, published on DECODE (key note of 24 October 2020). See G. Lasry, B. Megyesi and N. Kopal, "Deciphering papal ciphers from the 16th to the 18th Century", *Cryptologia* 45(6), 2021 (online 2020), doi:10.1080/01611194.2020.1755915.
- **Two pair values** come from the cipher ledger's re-read of 22 to 23 October 2026: 88 is del (the published key has quel), and 33 is gli. The first check used the same two values.
- **The truth:** the key applied to the same digits that my read used. The cut into codes is a reconstruction from the key, made with the same method and settings as the first check ([`francia-346-leaves/check.md`](https://github.com/prabal-rje/branicki-1757/blob/main/francia-346-leaves/check.md) in our repository).
- **The rebuild:** I rebuilt the frozen read with its own code. All 539 rows equal the frozen rows.
- **The times (12 November 2026, UTC−3):** my key was fixed at 01:27. The published key was first opened from 01:40 to 02:00, for a comparison with that key. The read of these records, with my key unchanged, was fixed at 17:00. The published key was applied to these records at about 17:05. Nothing in the read changed.

## 2. The letters

Precision is the share right of the true letters that my read shows. Recovery is the share right of all true letter tokens. The groups come from a key-free check of code counts, made without the published key.

| Records | True letter tokens | Shown | Right, of shown | Recovery | Shown tokens that are letter codes |
| --- | ---: | --- | --- | --- | --- |
| All 22 | 7,576 | 92.6% (7,017) | 98.8% (6,930 of 7,017) | 91.5% | 62.0% (7,017 of 11,324) |
| The 12 that fit | 4,874 | 94.1% (4,585) | 98.8% (4,532 of 4,585) | 93.0% | 63.7% (4,585 of 7,194) |
| The 6 that differ | 2,017 | 92.1% (1,858) | 98.7% (1,833 of 1,858) | 90.9% | 58.4% (1,858 of 3,179) |
| The 4 too small to judge | 685 | 83.8% (574) | 98.4% (565 of 574) | 82.5% | 60.4% (574 of 951) |
| The 8 inside the key's fit | 3,309 | 94.3% (3,122) | 99.0% (3,091 of 3,122) | 93.4% | 65.5% (3,122 of 4,767) |
| The 14 outside the key's fit | 4,267 | 91.3% (3,895) | 98.6% (3,839 of 3,895) | 90.0% | 59.4% (3,895 of 6,557) |

- **All 87 wrong letter tokens are code 07.** The key makes it h. My key reads l. The first check found the same fault.
- **The six that differ** are as good on letter codes as the twelve that fit. So the difference in their code counts does not come from a wrong letter key.
- **The four too small to judge** have fewer shown letters, because their pages hold many doubtful digits.

## 3. All shown tokens

My read shows 11,743 pair tokens with a letter. 419 of them touch a doubtful digit or a place that the truth does not cut. They are not graded. The table gives what the other 11,324 are in the truth.

| In the truth | Shown tokens |
| --- | ---: |
| a letter, right | 6,930 |
| a letter, wrong (all code 07) | 87 |
| a syllable, shown as its first letter | 250 |
| a syllable, shown as another letter | 1,237 |
| a null | 707 |
| no true code at this place (a wrong cut) | 2,113 |

So 61.2% of the graded shown tokens show the true letter (6,930 of 11,324). In the first check, on 13 records, this share was 65.7%.

## 4. The cut

- True tokens with a token of mine at the same place and length: 78.7% (11,373 of 14,448).
- My cut has no three-digit codes. The truth holds 1,054 three-digit tokens on these pages: 332 with a ledger value and 722 with no value.
- The full decode counts 1,154 three-digit tokens. It reads a doubtful digit with its first reading, and it keeps the short stretches that my read masked. This check masks them, as my read did.
- After a three-digit code, my pairs run out of step until the next word space.

## 5. By record

| Record | True letters | Right, of shown | Shown tokens that are letter codes |
| --- | ---: | --- | --- |
| R5626 | 450 | 99.8% (402 of 403) | 63.4% (403 of 636) |
| R5635 | 308 | 98.6% (290 of 294) | 68.9% (294 of 427) |
| R5636 | 823 | 99.4% (787 of 792) | 68.9% (792 of 1,150) |
| R5637 | 618 | 99.1% (582 of 587) | 68.1% (587 of 862) |
| R5640 | 477 | 98.9% (457 of 462) | 67.1% (462 of 689) |
| R5642 | 331 | 97.8% (265 of 271) | 44.0% (271 of 616) |
| R5643 | 20 | 100.0% (16 of 16) | 50.0% (16 of 32) |
| R5645 | 142 | 98.6% (137 of 139) | 65.0% (139 of 214) |
| R5646 | 539 | 98.0% (487 of 497) | 55.4% (497 of 897) |
| R5647 | 28 | 95.5% (21 of 22) | 44.9% (22 of 49) |
| R5648 | 585 | 98.2% (536 of 546) | 59.2% (546 of 922) |
| R5649 | 279 | 97.3% (255 of 262) | 63.7% (262 of 411) |
| R5650 | 516 | 99.0% (480 of 485) | 61.7% (485 of 786) |
| R5651 | 704 | 99.4% (662 of 666) | 61.3% (666 of 1,087) |
| R5652 | 411 | 99.2% (375 of 378) | 60.3% (378 of 627) |
| R5653 | 121 | 99.1% (115 of 116) | 68.6% (116 of 169) |
| R5654 | 150 | 97.9% (139 of 142) | 63.4% (142 of 224) |
| R5655 | 389 | 98.4% (359 of 365) | 63.5% (365 of 575) |
| R5656 | 223 | 97.9% (188 of 192) | 62.3% (192 of 308) |
| R5657 | 370 | 98.7% (297 of 301) | 57.4% (301 of 524) |
| R5658 | 75 | 98.5% (66 of 67) | 68.4% (67 of 98) |
| R5659 | 17 | 100.0% (14 of 14) | 66.7% (14 of 21) |

R5642 has the lowest share of letter codes (44.0%). Its page f. 246r has a high share of 6 and a low share of 8. I suspect that the transcription reads some 8s as 6.

## 6. Limits

- **No reference reading.** The truth is the key applied to the same machine transcription that I read. A misread digit hurts both sides in the same way.
- **The truth's cut** is a reconstruction. On four earlier records with a published cut, the same method agreed within 0.5 percentage points.
- **Doubtful digits:** 927 true tokens hold one. They are not graded.
- **u and v** count as one letter, and so do **i and j**.
- The check ran once. It changed no value of my key and no row of my read.

## 7. A check against the decipherment leaves

Three records hold a decipherment in Italian on another leaf of the same record. My pipeline transcribed these leaves too, by machine. This check does not use my frozen read.

- **Method:** I join the letters of the key's decode of the record, and the letters of the leaf. An edit-distance alignment pairs them. The measure is the share of the shorter text that aligns with equal letters.
- **Control:** the same decode against the letters of the other records' leaves, cut to the same length.

| Record | Leaf | Letters: leaf, decode | Equal, of the shorter text | Control |
| --- | --- | --- | ---: | ---: |
| R5626 | f. 155r | 870, 848 | 58.0% | 31.7% |
| R5637 | f. 212v | 1,221, 1,023 | 71.1% | 33.6% |
| R5646 | f. 269r | 1,891, 1,088 | 78.7% | 48.9% |

- The leaves are cursive and their transcription is a machine draft. So 100% is not the target.
- For five more records, a prose leaf of the same record is a possible decipherment: R5642, R5645, R5648, R5649 and R5651. For each, the lengths differ much, or the control comes out as high. So this check does not decide them.


## 8. The frozen read on the records added on 13 November

This is a check on records that carry a decipherment of the time. I applied the frozen key-free read of 12 November, unchanged, to the 22 records with "Inline Plaintext: Yes". There was no fit and no change of key, cut or rule. The key was known when I ran it, so the check is not blind.

| Record | Shown true letters | Right, of shown | Shown tokens that are letter codes | Pages that pass the key-free page test |
| --- | ---: | --- | ---: | --- |
| R5627 | 534 | 99.8% (533) | 67.0% | 2 of 2 |
| R5628 | 895 | 99.3% (889) | 68.6% | 2 of 2 |
| R5629 | 485 | 98.1% (476) | 63.2% | 2 of 2 |
| R5630 | 240 | 98.8% (237) | 68.2% | 1 of 1 |
| R5631 | 479 | 99.4% (476) | 66.7% | 1 of 1 |
| R5632 | 378 | 97.9% (370) | 70.7% | 0 of 1 |
| R5633 | 857 | 99.6% (854) | 69.6% | 1 of 2 |
| R5641 | 16 | 100.0% (16) | 41.0% | 0 of 1 |
| R5644 | 60 | 96.7% (58) | 61.9% | 1 of 1 |

- On the eight records that read, the frozen read is as good as on the first 22 records (section 5).
- **The 13 records in another cipher** (R5634, R5638, R5639, R5660 to R5666, R5669 to R5671) give 99.2% to 100% "right" by this measure. That number means nothing there. The "truth" is the published key, and the published key does not read them. Both keys give the same letters to most pair codes, so they agree. Their letter-code share is 32% to 44%, against 62% to 71% for the records that read.
- The key-free page test fails on 23 of the 24 pages of R5660 to R5671. R5666 f. 398v passes only because it has too few runs to judge (17). The test passes on five of six pages of R5634, R5638 and R5639.
- For these 13 records, sections 8 and 9 count all their cipher rows, by the rule of [`francia-346-full/README.md`](https://github.com/prabal-rje/branicki-1757/blob/main/francia-346-full/README.md) in our repository. These are the rows that the transcription labels as cipher, and 117 rows that it labels as text.

## 9. Against the decipherment of the time

A clerk wrote a decipherment between the cipher rows of these 22 records. My pipeline transcribed it with the cipher, by machine. I compared each read with the clerk's line just above each cipher row, by the method of section 7. The control is the same read against the other records' decipherments, cut to the same length.

| Record | Clerk's letters | Decode with the published key: equal, of the shorter text (control) | Frozen key-free read: equal (control) |
| --- | ---: | --- | --- |
| R5627 | 1,090 | 81.8% (34.1%) | 69.7% (40.5%) |
| R5628 | 1,573 | 74.8% (31.3%) | 65.1% (33.3%) |
| R5629 | 1,092 | 77.1% (36.3%) | 65.7% (39.1%) |
| R5630 | 505 | 82.4% (30.3%) | 72.4% (40.6%) |
| R5631 | 823 | 73.8% (32.7%) | 67.1% (31.0%) |
| R5632 | 688 | 73.2% (32.8%) | 67.5% (36.3%) |
| R5633 | 1,628 | 77.5% (33.3%) | 74.2% (38.0%) |
| R5644 | 157 | 63.7% (37.0%) | 57.1% (42.9%) |

- **The eight records that read** agree with the clerk at 64% to 82%, against 30% to 37% for the control.
- **The 13 records in another cipher** give about the same share for their own decipherment and for the control. So neither key reads them.
  - Eleven records enter: R5662 and R5666 are left out (see below).
  - The decode with the published key: 29.7% to 68.7% own, 28.3% to 67.0% control; own minus control lies between −2.3 and +1.7 points.
  - The frozen key-free read: own minus control lies between −3.4 and +1.6 points.
  - R5663 gives the highest shares (68.7% own, 67.0% control), because its decode has only 115 letters.
- R5641 (46 clerk letters) and R5662 (21) are too small. R5666 has almost no clerk's text beside its cipher rows (5 letters).
- Both sides are machine transcriptions, so 100% is not the target.
