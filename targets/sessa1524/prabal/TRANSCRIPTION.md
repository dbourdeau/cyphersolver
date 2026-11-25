# The transcription

Credit:

- DECODE, the database of historical ciphers of the DECRYPT project: records R9873 to R9905 (30 records with rows; R9902 has none).
- The record pages: https://de-crypt.org/decrypt-web/RecordsView/ followed by the number, for example https://de-crypt.org/decrypt-web/RecordsView/9873.
- Real Academia de la Historia, Madrid, Colección Salazar y Castro A-31 (9/31) and A-34 (9/34).
- Héder and Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- No DECODE image is published.

## What it is

- My own transcription of the DECODE images of the thirty records. Each page was read in several passes, and a last pass reconciled them.
- Two passes agree on about half of all units and on about two thirds of the three-letter codes.
- R9902 has no cipher rows in my transcription, so it is not here.
- No DECODE image and no DECODE transcription file is in this folder.

## How the rows were cut

- A row is a cipher row when its label says cipher or mixed, or when it holds 3 or more code groups.
- A clear word inside a mixed row became `?`. Raised and interlinear writing also became `?`.
- A run of Latin letters of 1 to 3 letters is one unit. A longer run was cut into pieces of 1 to 3 letters by the counts of the groups that stand alone.
- Each other sign is one unit. The long s is read as s.
- Some short Latin units of mixed rows are clear words that the cut did not catch. 34 such labels (364 units) are marked as clear words in the key (`key/added-values.tsv`) and are not counted as cipher.

## The files

- One file for each record: `transcription/<record>_<folios>_rows.txt`.
- Four header lines start with `#`.
- Then one line for each row: `<page>/<row>`, a space, and the units separated by spaces. `<page>` is the image page of the DECODE record. The row label is the label of my transcription.
- An empty row has a label and no units.

| Token | Meaning |
| --- | --- |
| Latin letters, digits or a sign | one unit |
| `?` | writing that is not cipher, or a sign that I did not read; my rows do not tell these apart |
| a unit that ends in `~` | a unit that I doubt |

## Sign names

- My transcription named the non-Latin signs page by page. One sign can have different names on different pages.
- Some codes have spellings of my transcription that differ from the ledger's, for example a long s read as f or p.
- `key/key.tsv` gives each label with its scope: one code everywhere for 1 to 4 Latin letters or digits, one page for a sign.

## The counts

| Record | Rows file | Rows | Units | `?` positions | Units that I doubt (`~`) |
| --- | --- | ---: | ---: | ---: | ---: |
| R9873 | `transcription/R9873_ff79-86_rows.txt` | 147 | 2,785 | 500 | 276 |
| R9874 | `transcription/R9874_ff86-87_rows.txt` | 20 | 493 | 33 | 75 |
| R9875 | `transcription/R9875_ff88-95_rows.txt` | 132 | 2,119 | 511 | 385 |
| R9876 | `transcription/R9876_f96_rows.txt` | 21 | 551 | 16 | 156 |
| R9877 | `transcription/R9877_ff128-129_rows.txt` | 7 | 98 | 44 | 17 |
| R9878 | `transcription/R9878_ff130-131_rows.txt` | 9 | 78 | 58 | 27 |
| R9879 | `transcription/R9879_f135_rows.txt` | 13 | 267 | 26 | 55 |
| R9880 | `transcription/R9880_f137_rows.txt` | 13 | 259 | 41 | 57 |
| R9881 | `transcription/R9881_ff139-140_rows.txt` | 13 | 264 | 16 | 37 |
| R9883 | `transcription/R9883_ff168-169_rows.txt` | 55 | 485 | 406 | 48 |
| R9884 | `transcription/R9884_ff170-173_rows.txt` | 22 | 271 | 158 | 42 |
| R9885 | `transcription/R9885_ff197-199_rows.txt` | 14 | 10 | 73 | 0 |
| R9886 | `transcription/R9886_ff201-203_rows.txt` | 9 | 160 | 36 | 8 |
| R9887 | `transcription/R9887_ff274-277_rows.txt` | 37 | 586 | 60 | 81 |
| R9889 | `transcription/R9889_ff320-321_rows.txt` | 28 | 389 | 128 | 54 |
| R9890 | `transcription/R9890_ff322-325_rows.txt` | 57 | 281 | 411 | 85 |
| R9891 | `transcription/R9891_ff361-364_rows.txt` | 39 | 467 | 183 | 82 |
| R9892 | `transcription/R9892_ff481-482_rows.txt` | 15 | 90 | 79 | 11 |
| R9893 | `transcription/R9893_ff483-485_rows.txt` | 12 | 163 | 61 | 26 |
| R9894 | `transcription/R9894_ff504-508_rows.txt` | 11 | 134 | 55 | 42 |
| R9895 | `transcription/R9895_ff510-517_rows.txt` | 25 | 298 | 201 | 35 |
| R9896 | `transcription/R9896_ff6-9_rows.txt` | 95 | 1,906 | 253 | 277 |
| R9897 | `transcription/R9897_ff10-16_rows.txt` | 114 | 1,672 | 302 | 246 |
| R9898 | `transcription/R9898_ff150-156_rows.txt` | 193 | 3,233 | 566 | 295 |
| R9899 | `transcription/R9899_ff194-195_rows.txt` | 15 | 220 | 51 | 51 |
| R9900 | `transcription/R9900_ff271-272_rows.txt` | 61 | 1,206 | 148 | 124 |
| R9901 | `transcription/R9901_ff300-303_rows.txt` | 5 | 49 | 32 | 19 |
| R9903 | `transcription/R9903_ff351-352_rows.txt` | 57 | 1,440 | 72 | 143 |
| R9904 | `transcription/R9904_ff379-382_rows.txt` | 54 | 544 | 165 | 99 |
| R9905 | `transcription/R9905_ff383-388_rows.txt` | 54 | 844 | 225 | 48 |
| **All 30** | | **1,347** | **21,362** | **4,910** | **2,901** |
