# Francia 32: the rows

Credit:

- DECODE, the database of historical ciphers of the DECRYPT project. Record pages: [R5612](https://de-crypt.org/decrypt-web/RecordsView/5612), [R5613](https://de-crypt.org/decrypt-web/RecordsView/5613), [R5614](https://de-crypt.org/decrypt-web/RecordsView/5614), [R5615](https://de-crypt.org/decrypt-web/RecordsView/5615), [R5616](https://de-crypt.org/decrypt-web/RecordsView/5616), [R5617](https://de-crypt.org/decrypt-web/RecordsView/5617), [R5618](https://de-crypt.org/decrypt-web/RecordsView/5618), [R5620](https://de-crypt.org/decrypt-web/RecordsView/5620), [R5621](https://de-crypt.org/decrypt-web/RecordsView/5621).
- Héder and Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- Archivio Apostolico Vaticano, Segreteria di Stato, Francia 32.
- No DECODE image is published.

## What the rows are

- My own transcription of the DECODE images, finished on 13 November 2026.
- No DECODE image and no transcription file of DECODE is in this folder.
- R5619 has no images on DECODE, so it has no rows.
- The decode, the measures in `check.md` and the page groups all use these rows.

## Where the rows are

- `transcription/`: one file for each of the 30 cipher pages.
- File name: `<record>_f<folio>_digits.txt`, as in `targets/francia346/transcription/`.
- Four header lines start with `#`. Then each cipher row is one line: its label, a space, its body.
- The files hold a selection: the rows with 10 or more digit signs. Shorter cipher groups inside clear text are not in them. For example, f. 71r has more short groups in the ledger's `targets/sega1590/transcription.txt` than rows here.
- Most labels are cipher rows: C01, C02, .... Where cipher and clear text share manuscript lines, the label is the manuscript line (L02, L27, ...). This is so on R5615 ff. 50v to 52v and on R5616 ff. 62r and 62v. The decode lines of the record pages use the same labels.
- Each row body is my transcription with these changes:
  - clear text became `‖`;
  - most notes on the place of the row on the page were cut;
  - some sign notes were renamed: they now say "unresolved" or "#-shaped";
  - backticks around some rows were removed.

## Marks

| Mark | Meaning |
| --- | --- |
| a digit, alone or with a mark | one cipher digit; the mark above it is a vowel sign (2̈, 3̂, 4̄, 5⁺ ...) or a dot |
| `[d?]` | one doubtful digit |
| `[a\|b?]` | one sign with two readings; the decode takes the left one if it is a digit |
| `[?]` | one sign not read |
| a lone lower-case letter | a sign that the transcription reads as a letter; the key reads it as a code letter |
| `⟨...⟩`, `[... sign]`, `[... glyph]` | a sign that the transcription describes and does not read as a digit |
| `ω`, `∞`, `△`, `Δ`, `#` and other symbols | signs that the transcription gives as symbols |
| `^{...}` | a raised mark above the digit before it |
| `[unresolved span]` and other `[unresolved ...]` notes | a span not read, of unknown length |
| `⟦ ... ⟧` | the transcription marks the enclosed cipher as tentative |
| `//` | a break in the cipher run |
| `{C01: ...}` | on f. 62v, a cipher group inside a manuscript line |
| `‖` | clear text stood here; this folder does not copy it |

## The counts

Counted from the files in `transcription/`. "Digit signs" are the digits that the decode reads, with their marks; a sign with two readings counts once when its left reading is a digit. The digits of the row labels inside f. 62v (`{C01:` to `{C08:`) are not counted. "Doubtful" counts the digit signs written as `[d?]` or `[a|b?]`.

| Record | Cipher pages | Rows | Digit signs | Doubtful |
| --- | --- | ---: | ---: | ---: |
| R5612 | f. 17r, f. 17v | 15 | 573 | 16 |
| R5613 | f. 45v | 7 | 324 | 15 |
| R5614 | f. 47r, f. 48r | 18 | 694 | 23 |
| R5615 | f. 49v, f. 50r, f. 50v, f. 51r, f. 51v, f. 52r, f. 52v, f. 53r, f. 53v, f. 54r, f. 54v | 205 | 8,551 | 225 |
| R5616 | f. 61v, f. 62r, f. 62v, f. 63r, f. 63v, f. 71r, f. 71v | 84 | 2,965 | 131 |
| R5617 | f. 106v, f. 107r | 9 | 321 | 14 |
| R5618 | f. 184v | 2 | 143 | 9 |
| R5620 | f. 190r | 29 | 2,101 | 25 |
| R5621 | f. 229v, f. 231r, f. 231v | 14 | 558 | 34 |
| **All 9** | **30** | **383** | **16,230** | **492** |

My repository gives 13,429 digits for the 24 pages of the main group. That figure came from the page counts of 17 November, by another rule. This folder counts 13,797 digit signs on the same pages.
