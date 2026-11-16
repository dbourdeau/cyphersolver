# The transcription

Credit: DECODE, the database of historical ciphers of the DECRYPT project. Records R5626, R5635 to R5637, R5640, R5642, R5643 and R5645 to R5659. Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346.

## What it is

- A machine transcription of the DECODE images. Each page had three model passes: a draft, a source check and a reconciliation.
- No person verified it against the images.
- The decode, the key-free read and `check.md` all use this transcription.
- DECODE's public record pages mark the ciphertext of these records as private. Their documents need a login. We did not check whether DECODE holds a transcription of its own.

## Known challenges in the source

The files keep the reconciled reading in each case below.

- **R5635, f. 205r:** a later source check reads 5 where the reconciliation gives 1, at two places (C01, position 13; C03, position 1).
- **R5637, f. 213v:** at the end of C08, a source check reports digit-like signs after the last read digit. Their count and their readings are not known.
- **R5648, f. 279v:** the transcription marks five rows as tentative: C01, C07, C11, C16 and C17.

## Where the rows are

The digit rows are in `transcription/`: one file for each of the 35 cipher pages. They are my own transcription. No DECODE image and no DECODE transcription file is in this folder.

- File name: `<record>_f<folio>_digits.txt`, the file form of the digit files in `research/dudout_2026-10-29/`.
- Four header lines start with `#`. Then each cipher row is one line, `C01 <body>`, in page order.
- The decode lines of the record pages use the same row labels. So each decode line points to one row.
- The decode, the key-free read and `check.md` used these rows. Each row body is unchanged. Only the header lines and the form of the row label are new.

| Token | Meaning |
| --- | --- |
| a digit | one cipher digit |
| `[d?]` | one doubtful digit |
| `[a\|b?]` | one sign with two or more readings; the first is the reconciled reading |
| `[?]` | one unread sign |
| `[overwritten glyph]`, `[X-shaped sign]`, `[V-shaped sign]` | one sign that the transcription does not read as a digit |
| `[unresolved cipher run]`, `[illegible]`, `[overwritten cipher signs: illegible]`, `[glyph count disputed]` | an unread span of unknown length |
| `[gap: cleartext dropped]` | clear text stood here; the file does not copy it |
| another note in brackets, such as `[rule to the right]` | a mark with no position |
| `⟦...⟧` around a whole row | the transcription marks the whole row as tentative |

- The decode reads a doubtful digit with its first reading, and marks the code `⟨a⟩`.
- Clear text never enters a row.

## The counts

Counted from the files in `transcription/`. "Digits" are digits read without doubt. "Doubtful" counts doubtful digits, unread signs and signs that the transcription does not read as digits. "Gaps" are unread spans of unknown length. "Breaks" mark clear text inside or next to the cipher.

| Record | Cipher pages | Rows | Digits | Doubtful | Gaps | Breaks |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| R5626 | f. 154r | 23 | 1,573 | 181 | 8 | 0 |
| R5635 | f. 205r | 20 | 1,077 | 2 | 9 | 0 |
| R5636 | f. 211r, f. 211v | 40 | 2,836 | 25 | 12 | 0 |
| R5637 | f. 213r, f. 213v | 28 | 2,154 | 16 | 3 | 0 |
| R5640 | f. 237v | 22 | 1,723 | 1 | 0 | 0 |
| R5642 | f. 246r, f. 246v | 24 | 1,756 | 12 | 2 | 1 |
| R5643 | f. 249r, f. 249v | 32 | 113 | 3 | 33 | 4 |
| R5645 | f. 261r | 11 | 508 | 3 | 1 | 7 |
| R5646 | f. 268r, f. 268v | 33 | 2,158 | 10 | 3 | 7 |
| R5647 | f. 272r | 5 | 168 | 6 | 4 | 3 |
| R5648 | f. 279r, f. 279v | 36 | 2,249 | 26 | 12 | 11 |
| R5649 | f. 281r | 17 | 955 | 5 | 0 | 6 |
| R5650 | f. 288r, f. 288v | 29 | 1,918 | 24 | 7 | 2 |
| R5651 | f. 297r, f. 297v | 37 | 2,631 | 94 | 13 | 0 |
| R5652 | f. 303r, f. 303v | 26 | 1,513 | 4 | 6 | 8 |
| R5653 | f. 310r | 7 | 406 | 1 | 3 | 2 |
| R5654 | f. 315r | 11 | 537 | 1 | 0 | 4 |
| R5655 | f. 323r, f. 323v | 22 | 1,416 | 95 | 2 | 1 |
| R5656 | f. 337r | 16 | 979 | 5 | 1 | 0 |
| R5657 | f. 342r, f. 342v | 28 | 1,620 | 3 | 29 | 0 |
| R5658 | f. 344r, f. 344v, f. 345r | 50 | 284 | 8 | 45 | 1 |
| R5659 | f. 351r | 22 | 69 | 1 | 21 | 0 |
| **All 22** | **35** | **539** | **28,643** | **526** | **214** | **57** |

- R5643 f. 249r, R5658 ff. 344r and 344v, and 21 of the 22 rows of R5659 f. 351r hold cipher rows with no read sign.
- On R5642 f. 246r and R5657 f. 342r, the transcription marks each row as tentative.
