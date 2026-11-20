# The transcription

Credit: DECODE, the database of historical ciphers of the DECRYPT project, records R4034 to R4039, R4041 to R4050 and R4052 to R4054. Florence, Archivio Niccolini di Camugliano, Fondo antico 214, inserto 1. No DECODE image is published.

## What it is

- My own transcription of the DECODE images. My pipeline read each page in two passes, and a third pass joined them into one reading.
- The files in `transcription/` hold the digit rows of the cipher passages only, one line for each row of the transcription.
- Clear words inside a cipher row, stretches that do not read, raised writing and deleted writing each show as `[?]`.
- Later marks are left out: foliation, endorsements, dates and margin notes. Lines written between the rows are left out, and so are clipped views of a neighbouring page.
- No DECODE image and no DECODE transcription file is in this folder.

## The form of a file

- File name: `<record>_digits.txt`. The rows carry DECODE's image number of the record, not a folio, because my transcription is by image.
- Four header lines start with `#`. Then each row is one line: the image number, the row label and the row, separated by tabs.
- Row labels: `Cnn` is a cipher row of the transcription; `Lnn` is a line that holds cipher digits inside clear text.

| Token | Meaning |
| --- | --- |
| a digit | one cipher digit |
| `~` after a digit | the digit is doubtful; the row gives its reading |
| `‾` after a digit | the digit stands under a bar (earlier system only) |
| `[?]` | a clear word, or a stretch of the row that does not read |
| `#` | a sign that is not a digit |
| a space, `.`, `/` | a visible space, a point and a slash of the row |

## Known challenges

- **R4041, image 1, L05:** a row of four digits stands on a line that the transcription marks as prose. The read of record keeps it. Another build of my rows left it out, so it gives R4041 11 rows; this folder has 12.
- **The variant of o:** R4039 writes o as code 2; the later letters write it as code 15.
- The two passes agree on only part of the text, so a share of the digits can be wrong. A wrong digit gives a wrong letter or a broken cut.

## The counts

| Record | Rows | Digits | Doubtful digits | Breaks `[?]` | Signs `#` | Barred digits |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| R4034 | 25 | 668 | 25 | 2 | 0 | 12 |
| R4035 | 7 | 221 | 1 | 0 | 0 | 0 |
| R4036 | 2 | 57 | 4 | 1 | 0 | 0 |
| R4037 | 36 | 1,535 | 11 | 6 | 0 | 0 |
| R4038 | 8 | 388 | 3 | 1 | 0 | 0 |
| R4039 | 57 | 3,446 | 73 | 23 | 2 | 0 |
| R4041 | 12 | 258 | 3 | 1 | 1 | 0 |
| R4042 | 13 | 479 | 9 | 1 | 0 | 0 |
| R4043 | 9 | 171 | 12 | 1 | 0 | 0 |
| R4044 | 6 | 88 | 2 | 1 | 0 | 0 |
| R4045 | 6 | 167 | 15 | 4 | 1 | 0 |
| R4046 | 5 | 159 | 2 | 1 | 0 | 0 |
| R4047 | 24 | 1,188 | 30 | 9 | 0 | 0 |
| R4048 | 4 | 107 | 6 | 0 | 0 | 0 |
| R4049 | 13 | 597 | 2 | 3 | 0 | 0 |
| R4050 | 3 | 49 | 3 | 3 | 0 | 0 |
| R4052 | 9 | 207 | 6 | 1 | 0 | 0 |
| R4053 | 4 | 114 | 5 | 0 | 0 | 0 |
| R4054 | 63 | 2,157 | 27 | 23 | 3 | 0 |
| **All 19** | **306** | **12,056** | **239** | **81** | **7** | **12** |

The main system has 9,187 digits in 14 letters; the read of record uses 8,590 digits of 13 letters, and R4049 (597 digits) was decoded with its key afterwards. The earlier system has 2,869 digits.
