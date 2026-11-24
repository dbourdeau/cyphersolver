# The Botti letters to Cardinal Gualterio, 1710 to 1713: a decode from ciphertext

These are letters of the Abbate C. C. Botti, and perhaps of his uncle, the Abbate Lazaro Botti, to their patron, Cardinal Filippo Antonio Gualterio. DECODE's note and the British Library's catalogue name the correspondence. I take each letter to go to Gualterio; the volume also holds copies of his letters to Botti, so the direction of a letter is a doubt. The year numbers on the pages run from 1710 to 1713.

This folder decodes the cipher of 51 DECODE records of British Library, Add MS 20443. The key of the letters is from ciphertext. Fourteen code values are from the clerk's decipherment on the pages. Seven pure-blind dotted letters (`R8660`, `R8661`, `R8664`, `R8665`, `R8668`, `R8673`, `R8718`; none carries any contemporary clerk decipherment) now carry strictly aligned word-divided Italian readings (`readings/`) and English translations verified by `scripts/verify_readings.py` (`508` of `781` cipher words sure = `0.650`). The other 44 letters stay **decoded, not read**.

## Credit

- **DECODE**, the database of historical ciphers of the DECRYPT project: records R8468 to R8470, R8617, R8618 and R8659 to R8718 (51 records; the table of records lists them). Each record page links its DECODE record page, `https://de-crypt.org/decrypt-web/RecordsView/<n>`.
- **The archive:** British Library, Add MS 20443 (papers of Cardinal F. A. Gualterio): letters of the Abbate Carlo Camillo Botti and of his uncle, the Abbate Lazaro Botti, to Cardinal Gualterio, 1708 to 1713 ([British Library catalogue](https://searcharchives.bl.uk/catalog/040-002090742)).
- **The database:** Héder, M. and Megyesi, B. (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- **The clerk of the time** who wrote decipherments on 29 of these letters: 14 code values of the key come from that text. `key-and-read/key.tsv` marks each one.

DECODE's images are for research use only. They may not be redistributed or published without permission from the archive. No DECODE image is published.

## The state

| Part | State |
| --- | --- |
| The key: 21 codes for letters | from ciphertext |
| Code 17 | decoded r; open between r and q |
| 14 code values: 8 words and names, 1 word part, 5 letters | from the clerk's decipherment on the page |
| 90 rare codes (191 tokens in the letters with dots) | open |
| 7 pure-blind dotted letters (`R8660`, `R8661`, `R8664`, `R8665`, `R8668`, `R8673`, `R8718`) | read in part (`508/781` sure cipher words = `0.650`, `readings/`) |
| Remaining 44 documents | decoded, not read |

## The numbers

| What | Value |
| --- | --- |
| Records | 51: 46 with dots between the codes (R8659 to R8718), 5 without dots (R8468 to R8470, R8617, R8618) |
| Pages with cipher rows in my transcription | 194 |
| Pages decoded here | 147 |
| Pages with no decode here | 47: too small or no cipher digits (45), not shown because the decode is not sure (1), does not decode yet (1) |
| The letters with dots: code tokens on all their pages | 27,432; 98.1% show a letter in the frozen decode |
| The letters with dots: code tokens on the pages decoded here | 26,566; 26,075 show a value. The other 866 stand on pages with no decode here. |
| The letters without dots: decode units on the pages decoded here | 9,191; 8,987 show a value. A unit is one letter of the decode; `·` there can stand for a stretch that no code covers. |
| A letter-match share against the clerk (29 letters) | 75.3% of the 14,279 letters that the blind decode shows match the clerk's row above; a wrong row gives 29.6% |

The last figure is a share of letters. It is no read share by this ledger's rule. `check.md` gives it in full, and `NOTES.md` says why no word count is given.

## What the letters say (a guess from the decode; it is no reading)

- **1710 (R8659 to R8674).** Botti asks again and again for leave to travel for a few days. He complains of persecution by the local government. A sword fight and an arrest; an armed clash with the constables ("sbirri"); two officers go to prison; then the affair is settled. Satirical verses against an official.
- **The letters without dots, 1710 (R8468 to R8470, R8617, R8618).** A dispute over precedence in the street with the provincial treasurer, Conti. A quarrel at Bertinoro that involves don Antonio, nephew of Ruffo. Botti is ill with fever; Ruffo orders another injunction ("precetto") against him.
- **1711 (R8675 to R8703).** A water dispute over broken embankments. Factions among the nobles. Pardons and releases sold for money. Foreign troops hold a tower. Comacchio is named (R8685, R8689, R8691; also R8712).
- **1712 to 1713 (R8705 to R8718).** The communal dispute is settled. Help over a church benefice for a relative. Stronger foreign troops on the border despite peace rumours.
- **Names in the decode:** Ravenna (R8660, R8661, R8664, R8717); Rasponi (R8660, R8668, R8670, R8689, R8691, R8717); Bosetti (R8668 to R8670). Code 62 ("Ruffo", a value from the clerk) has 31 tokens in the letters with dots; their decode shows it as `·`.

These lines are guesses where the decode is broken. No document is read.

## The records

- "Clerk": DECODE's mark of inline plaintext on the record.
- "Shown": code tokens of the decode here with a value.
- "Open": the `·` of the decode. In the letters with dots, it is a code that the key leaves open. In the letters without dots, it is a letter that the decode leaves open.
- "Not codes": items of the rows with dots that the decode does not take as codes (`?`).

| Record | DECODE record page | Year | Codes | Clerk | Pages with cipher rows | Decoded here | Code tokens | Shown | Open | Not codes | State |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| [R8468](r8468.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8468) | 1710 | without dots | no | 8 | 7 | 3,088 | 2,996 | 92 | 0 | decoded, not read |
| [R8469](r8469.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8469) | 1710 | without dots | no | 8 | 5 | 3,197 | 3,173 | 24 | 0 | decoded, not read |
| [R8470](r8470.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8470) | 1710 | without dots | no | 5 | 4 | 1,145 | 1,066 | 79 | 0 | decoded, not read |
| [R8617](r8617.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8617) | 1710 | without dots | no | 4 | 3 | 1,388 | 1,384 | 4 | 0 | decoded, not read |
| [R8618](r8618.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8618) | 1710 | without dots | yes | 3 | 2 | 373 | 368 | 5 | 0 | decoded, not read |
| [R8659](r8659.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8659) | 1710 | dots | no | 3 | 2 | 293 | 284 | 9 | 112 | decoded, not read |
| [R8660](r8660.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8660) | 1710 | dots | no | 4 | 3 | 849 | 830 | 19 | 76 | decoded, not read |
| [R8661](r8661.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8661) | 1710 | dots | no | 4 | 3 | 551 | 538 | 13 | 21 | decoded, not read |
| [R8662](r8662.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8662) | 1710 | dots | no | 4 | 3 | 817 | 793 | 24 | 143 | decoded, not read |
| [R8663](r8663.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8663) | 1710 | dots | no | 7 | 2 | 454 | 446 | 8 | 23 | decoded, not read |
| [R8664](r8664.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8664) | 1710 | dots | no | 2 | 2 | 467 | 458 | 9 | 30 | decoded, not read |
| [R8665](r8665.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8665) | 1710 | dots | no | 2 | 1 | 268 | 265 | 3 | 26 | decoded, not read |
| [R8666](r8666.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8666) | 1710 | dots | no | 2 | 1 | 113 | 108 | 5 | 8 | decoded, not read |
| [R8667](r8667.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8667) | 1710 | dots | no | 4 | 2 | 279 | 255 | 24 | 22 | decoded, not read |
| [R8668](r8668.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8668) | 1710 | dots | no | 5 | 3 | 627 | 621 | 6 | 62 | decoded, not read |
| [R8669](r8669.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8669) | 1710 | dots | yes | 2 | 1 | 68 | 62 | 6 | 4 | decoded, not read |
| [R8670](r8670.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8670) | - | dots | no | 4 | 3 | 441 | 433 | 8 | 89 | decoded, not read |
| [R8671](r8671.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8671) | - | dots | no | 4 | 2 | 379 | 373 | 6 | 111 | decoded, not read |
| [R8672](r8672.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8672) | 1710 | dots | no | 4 | 3 | 350 | 342 | 8 | 20 | decoded, not read |
| [R8673](r8673.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8673) | 1710 | dots | no | 4 | 2 | 479 | 476 | 3 | 6 | decoded, not read |
| [R8674](r8674.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8674) | - | dots | no | 4 | 4 | 384 | 356 | 28 | 71 | decoded, not read |
| [R8675](r8675.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8675) | 1711 | dots | no | 3 | 2 | 217 | 215 | 2 | 41 | decoded, not read |
| [R8676](r8676.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8676) | 1711 | dots | yes | 4 | 3 | 551 | 543 | 8 | 35 | decoded, not read |
| [R8677](r8677.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8677) | - | dots | yes | 4 | 3 | 723 | 708 | 15 | 81 | decoded, not read |
| [R8678](r8678.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8678) | 1711 | dots | yes | 2 | 2 | 333 | 324 | 9 | 29 | decoded, not read |
| [R8679](r8679.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8679) | 1711 | dots | yes | 3 | 1 | 174 | 172 | 2 | 9 | decoded, not read |
| [R8680](r8680.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8680) | 1711 | dots | yes | 5 | 5 | 1,480 | 1,473 | 7 | 117 | decoded, not read |
| [R8681](r8681.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8681) | - | dots | yes | 4 | 4 | 972 | 964 | 8 | 21 | decoded, not read |
| [R8682](r8682.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8682) | 1711 | dots | yes | 4 | 2 | 279 | 272 | 7 | 25 | decoded, not read |
| [R8683](r8683.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8683) | 1711 | dots | yes | 4 | 3 | 926 | 908 | 18 | 56 | decoded, not read |
| [R8684](r8684.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8684) | 1711 | dots | yes | 4 | 3 | 890 | 877 | 13 | 42 | decoded, not read |
| [R8685](r8685.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8685) | 1711 | dots | yes | 6 | 4 | 1,092 | 1,085 | 7 | 108 | decoded, not read |
| [R8688](r8688.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8688) | 1711 | dots | yes | 4 | 4 | 674 | 651 | 23 | 20 | decoded, not read |
| [R8689](r8689.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8689) | - | dots | yes | 3 | 3 | 520 | 517 | 3 | 20 | decoded, not read |
| [R8691](r8691.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8691) | 1711 | dots | yes | 4 | 4 | 695 | 691 | 4 | 51 | decoded, not read |
| [R8692](r8692.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8692) | - | dots | yes | 2 | 1 | 145 | 144 | 1 | 1 | decoded, not read |
| [R8693](r8693.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8693) | 1711 | dots | yes | 3 | 2 | 358 | 356 | 2 | 11 | decoded, not read |
| [R8695](r8695.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8695) | 1711 | dots | yes | 4 | 4 | 798 | 794 | 4 | 114 | decoded, not read |
| [R8698](r8698.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8698) | - | dots | yes | 4 | 3 | 741 | 731 | 10 | 59 | decoded, not read |
| [R8699](r8699.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8699) | - | dots | yes | 4 | 4 | 1,027 | 1,013 | 14 | 35 | decoded, not read |
| [R8702](r8702.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8702) | 1711 | dots | yes | 4 | 4 | 872 | 863 | 9 | 128 | decoded, not read |
| [R8703](r8703.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8703) | - | dots | yes | 3 | 2 | 484 | 477 | 7 | 16 | decoded, not read |
| [R8705](r8705.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8705) | 1712 | dots | yes | 4 | 4 | 1,025 | 1,017 | 8 | 34 | decoded, not read |
| [R8707](r8707.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8707) | - | dots | yes | 3 | 2 | 492 | 489 | 3 | 24 | decoded, not read |
| [R8708](r8708.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8708) | - | dots | yes | 3 | 2 | 494 | 480 | 14 | 12 | decoded, not read |
| [R8710](r8710.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8710) | 1710 | dots | yes | 3 | 3 | 457 | 446 | 11 | 4 | decoded, not read |
| [R8712](r8712.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8712) | 1712 | dots | yes | 4 | 3 | 645 | 633 | 12 | 90 | decoded, not read |
| [R8714](r8714.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8714) | 1712 | dots | yes | 3 | 3 | 731 | 717 | 14 | 179 | decoded, not read |
| [R8715](r8715.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8715) | 1712 | dots | yes | 3 | 3 | 613 | 606 | 7 | 70 | decoded, not read |
| [R8717](r8717.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8717) | 1713 | dots | yes | 4 | 4 | 1,003 | 939 | 64 | 21 | decoded, not read |
| [R8718](r8718.md) | [DECODE](https://de-crypt.org/decrypt-web/RecordsView/8718) | 1713 | dots | no | 2 | 2 | 336 | 330 | 6 | 14 | decoded, not read |
| **All 51** | | | | | **194** | **147** | **35,757** | **35,062** | **695** | **2,291** | |

## How to read the decode

Each record page ends with the decode, row by row. It is the output of the key on my rows, with nothing edited.

| Mark | Meaning |
| --- | --- |
| a letter | the value of a code |
| `·` | a code that the key leaves open; in the letters without dots, a letter that the decode leaves open |
| `?` | an item of the row that the decode does not take as a code: a sign with a doubt mark, a note of the transcription, or a stretch that is not read |
| capital words | in the letters without dots: word codes with a value from the clerk's decipherment |
| a space | a space of the page, or a break at a note of the transcription |
| `≈` before a row label | the row is placed by its order on the page |

## What stays open

- **Code 17** (255 tokens): decoded r. At its places the clerk writes r 66 times and q 39 times.
- **Code 10** (a): at 208 of the 1,830 places where it aligns with the clerk's text, the clerk writes u or v. The transcription may read the sign for u as 10. Not checked.
- **Rare codes:** 90 codes stay open. In the letters with dots, the decode shows the 14 values from the clerk as `·`; `key-and-read/key.tsv` gives them.
- **The letters without dots:** the cut of their digits into codes is not sure. The key did not move.
- **R8468:** page T003 is a fragment; on page T007 the values of five sign labels are not sure.
- **One page is not shown,** because its right margin is clipped and its decode is not sure: R8662 T003. Four other dotted pages earlier withheld (R8666 T003, R8674 T001, R8677 T001, R8710 T004) were decoded on 22 November 2026 outside the 19 November frozen read using the unchanged ciphertext-only key (`scripts/decode_four_pages.py`).
- **R8618 T002** does not decode yet: one code stands between spaces, and the word breaks are not known.
- **Two writers:** the British Library's catalogue names two writers for this volume: the Abbate Carlo Camillo Botti and his uncle, the Abbate Lazaro Botti. I do not know which letters each wrote. The volume also holds copies of Gualterio's letters to Botti (from f. 294).

## Files

- `NOTES.md`, `profile.json`: the notes and the profile of this target.
- `check.md`: what was checked against what, with the numbers.
- `r8468.md` to `r8718.md`: one page for each record: the state, the counts, a summary marked as a guess, and the decode row by row.
- `scripts/decode_four_pages.py`: reproduces the unedited mechanical decode of R8666 T003, R8674 T001, R8677 T001, and R8710 T004 directly from `key-and-read/key.tsv`.
- `key-and-read/`: the key with the source of each value, the sign labels of single pages, and the order of events of the frozen read.
- `TRANSCRIPTION.md` and `transcription/`: my own transcription of the cipher rows, one file for each page with cipher digits.
