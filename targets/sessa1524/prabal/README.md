# Sessa to Charles V, 1524 to 1525: thirty cipher records decoded with the ledger's key

Luis Fernández de Córdoba, Duke of Sessa, imperial ambassador in Rome, writes to the Emperor Charles V. Thirty DECODE records of his letters, April 1524 to June 1525, hold cipher passages. This folder decodes all thirty with the key of this target, with values that I added. It joins the target `sessa1524`: one key, one entry.

**State of every record here: decoded, not read.** The decode does not build sentences. So this folder gives no reading and no translation, and it adds no word to the read figure of the target.

## What this folder holds

- `transcription/`: a transcription of the DECODE images, one file for each record (1,347 rows).
- `key/key.tsv`: the table of the decode. Each label of my rows has its value, its kind and its source.
- `key/decode.py`: a short script. It applies `key/key.tsv` to the rows files and gives every decode line (`python3 key/decode.py --check`).
- `key/added-values.tsv`: the values that I added to the ledger's key, each with its source and the date when I took it.
- `r9873.md` to `r9905.md`: one page for each record: its counts, a short summary, the credit of earlier readings, and the decode row by row.
- `TRANSCRIPTION.md`: what the rows are, their marks and their counts.
- `check.md`: what I checked against what.
- `NOTES.md`: the open items.

## The key

- **The ledger's key:** KS4 of Brice Dudout (29 Oct 2026, `dudout/key_KS4.tsv`). KS4 is Daniel Bourdeau's `key_working.md` with values from period cipher and clear pairs.
- **Two departures from KS4:**
  - `qes` reads es, the value of `key_working.md` pass 3. KS4 keeps franceses, the value of pass 1. This touches 174 units (19 of them my label `ges`, which the label map joins to `qes`).
  - Where KS4 gives two values (`njn` = ha / han), the decode shows the value before the slash. This touches 40 units.
  - No other value of KS4 changes.
- **The names of my labels:** my rows name some groups and signs differently from the ledger's transcriptions. A map of 41 Latin labels and 19 sign labels joins the two. I made it by aligning my rows with the ledger's transcriptions of R9873, R9898 and f. 128 (14 pages). My sign names change from page to page, so a sign read through the map off its aligned page is marked doubtful.
- **Values that I added (63):** codes that KS4 does not hold. 35 come from clear texts of the time, and 27 from this ledger's readings of R9873, R9898 and f. 128. One, `cib` = su, comes from two copies of one dispatch (R9879, R9880) read with the key, with a weak value of the clerk copies. 31 rest on 2 or more agreeing places. 32 rest on one place that agrees with a value of the clerk copies (16 strong and 16 weak clerk values). 47 of the 63 rest wholly or in part on files of this target: the ledger's readings of R9873, R9898 and f. 128, and Daniel Bourdeau's transcriptions of the period decipherments ff. 140, 172 and 324. `key/added-values.tsv` names the source of each one. They read 1,186 units here; 246 of these units carry my `~` doubt in the rows, and the decode does not mark them doubtful.
- **Against `key_working.md`:** 4 of the 63 values are already in `key_working.md`, though not in KS4 (`cao`, `qel`, `lar`, `z y`). So 59 are additions to `key_working.md`. 20 of the 59 give the same value as a KS4 code one sign away; they may be my spellings of the ledger's codes.
- **Clear words (34 labels, 364 units):** short labels of mixed rows that are clear Spanish words, not cipher. The decode marks them `_x_`. They are not counted as cipher units.
- **Clerk values (1,094 units):** values from a key that I fitted on the clerks' decipherments of the time. They are not in the ledger's key. `key/key.tsv` lists them as kind "clerk value", and the decode shows them as `[x]`. I never count them as read.

## The counts by record

These counts are units. One unit is a code group or a sign: a word, a syllable or a letter. The words follow in the next section, as an estimate.

| Record | Cipher units | Ledger key, no doubt (letters) | Switch marks and openers | Doubtful | Added entries (letters) | Added entries (nulls) | Clerk value only | No value | `…` positions | Clear words cut |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [R9873](r9873.md) | 2,742 | 2,018 | 109 | 203 | 81 | 15 | 58 | 258 | 500 | 43 |
| [R9874](r9874.md) | 492 | 339 | 0 | 56 | 13 | 0 | 4 | 80 | 33 | 1 |
| [R9875](r9875.md) | 2,075 | 1,159 | 41 | 320 | 144 | 13 | 72 | 326 | 511 | 44 |
| [R9876](r9876.md) | 550 | 315 | 16 | 98 | 53 | 7 | 4 | 57 | 16 | 1 |
| [R9877](r9877.md) | 98 | 69 | 0 | 12 | 2 | 0 | 8 | 7 | 44 | 0 |
| [R9878](r9878.md) | 78 | 31 | 1 | 16 | 2 | 0 | 2 | 26 | 58 | 0 |
| [R9879](r9879.md) | 265 | 135 | 10 | 66 | 6 | 1 | 5 | 42 | 26 | 2 |
| [R9880](r9880.md) | 258 | 154 | 2 | 41 | 18 | 9 | 2 | 32 | 41 | 1 |
| [R9881](r9881.md) | 263 | 164 | 9 | 39 | 8 | 0 | 14 | 29 | 16 | 1 |
| [R9883](r9883.md) | 451 | 202 | 8 | 31 | 31 | 5 | 17 | 157 | 406 | 34 |
| [R9884](r9884.md) | 265 | 179 | 0 | 31 | 14 | 4 | 15 | 22 | 158 | 6 |
| [R9885](r9885.md) | 8 | 2 | 0 | 0 | 0 | 0 | 1 | 5 | 73 | 2 |
| [R9886](r9886.md) | 154 | 94 | 1 | 7 | 10 | 6 | 5 | 31 | 36 | 6 |
| [R9887](r9887.md) | 581 | 326 | 53 | 52 | 14 | 2 | 19 | 115 | 60 | 5 |
| [R9889](r9889.md) | 384 | 204 | 45 | 51 | 30 | 5 | 18 | 31 | 128 | 5 |
| [R9890](r9890.md) | 263 | 114 | 0 | 44 | 20 | 1 | 20 | 64 | 411 | 18 |
| [R9891](r9891.md) | 449 | 216 | 1 | 57 | 29 | 7 | 21 | 118 | 183 | 18 |
| [R9892](r9892.md) | 89 | 59 | 0 | 9 | 2 | 0 | 5 | 14 | 79 | 1 |
| [R9893](r9893.md) | 158 | 86 | 10 | 21 | 11 | 0 | 10 | 20 | 61 | 5 |
| [R9894](r9894.md) | 129 | 62 | 0 | 30 | 4 | 0 | 9 | 24 | 55 | 5 |
| [R9895](r9895.md) | 284 | 143 | 0 | 55 | 14 | 1 | 9 | 62 | 201 | 14 |
| [R9896](r9896.md) | 1,875 | 1,027 | 133 | 180 | 80 | 6 | 250 | 199 | 253 | 31 |
| [R9897](r9897.md) | 1,641 | 851 | 92 | 200 | 77 | 22 | 121 | 278 | 302 | 31 |
| [R9898](r9898.md) | 3,183 | 1,974 | 133 | 198 | 253 | 10 | 106 | 509 | 566 | 50 |
| [R9899](r9899.md) | 218 | 106 | 1 | 56 | 12 | 0 | 6 | 37 | 51 | 2 |
| [R9900](r9900.md) | 1,206 | 816 | 4 | 82 | 25 | 4 | 98 | 177 | 148 | 0 |
| [R9901](r9901.md) | 41 | 12 | 0 | 7 | 2 | 0 | 2 | 18 | 32 | 8 |
| [R9903](r9903.md) | 1,438 | 811 | 37 | 145 | 30 | 1 | 86 | 328 | 72 | 2 |
| [R9904](r9904.md) | 534 | 268 | 1 | 64 | 26 | 12 | 25 | 138 | 165 | 10 |
| [R9905](r9905.md) | 826 | 415 | 53 | 29 | 28 | 16 | 82 | 203 | 225 | 18 |
| **All 30** | **20,998** | **12,351** | **760** | **2,200** | **1,039** | **147** | **1,094** | **3,407** | **4,910** | **364** |

- **Cipher units** are the units of my rows less the 364 clear words: the units that I classify as cipher. The `?` positions of my rows (`…` in the decode) are not counted: they are clear writing, interlinear writing, or signs that I did not read. My rows do not tell these apart, so some `?` positions may be cipher.
- **Ledger key, no doubt:** units with a letter value of the ledger's key and no doubt mark.
- **Doubtful:** units that the ledger's key reads, with a doubt mark: a sign that I doubt in my rows, a sign read through the map off its aligned page, or a value of the clerk copies that differs from the key's value.
- **Added entries:** units read by the 63 values that I added. "Nulls" are entries that read as no letter. 246 of these units carry my `~` doubt.
- **Clerk value only:** units that only a value of the clerk copies reads. Not counted as read.
- **Note of the maintainers (20 November 2026, integration of pull request 826):** the 9 units written `f~`, the switch between clear and cipher (R9875 2, R9883 2, R9900 2, R9904 3), are counted under "Doubtful", because the rule that a unit ending in `~` is doubtful also takes the `~` of the switch's own label. So 760 switch marks and openers and 2,200 doubtful units can also be read 769 and 2,191, and the share below 14,306 of 20,998 where it gives 14,297: 68.1% either way. The decode is the same either way, since a switch shows nothing.

**About "68.1% of 20,998 units".** Our repository gives this number. It is a share of units, not a read share by the rule of this ledger. It counts 12,351 units with a letter value of the ledger's key, 760 switch marks and openers, and 1,186 units of the added entries: 14,297 of 20,998. It leaves out the 2,200 doubtful units and the 1,094 units with a clerk value only. By the word rule of 19 November 2026, every record here is "decoded, not read", so the folder adds no read words.

## Words, estimated

The decode is not divided into words. So I give the words as an estimate: the tokens of the decode lines.

- A run of units joined by hyphens counts as one word. A code value of several words (`V. Md.`) counts its words. A clear word and a `…` position do not count.
- The estimate is low where a spelled run holds several words. It is high where a code for a syllable stands apart (`manda do`).
- **Sure:** every cipher unit of the token has a letter value of a key, with no doubt mark and no `~` in my rows. I give it twice: with the ledger's key alone, and with my added values too.
- **Holes:** the other tokens. Each counts as one word.
- These numbers do not make a read share: no record is read. R9885 (8 words) and R9901 (29 words) fall under 40 words. The floor for short texts is not used, because they are not read.
- All 30: 9,640 words; 4,343 sure by the ledger's key alone (0.451); 4,906 sure with my added values (0.509); 4,734 holes.

| Record | Words, estimated | Sure by the ledger's key alone | Sure with my added values | Holes |
| --- | ---: | ---: | ---: | ---: |
| [R9873](r9873.md) | 1,091 | 638 | 677 | 414 |
| [R9874](r9874.md) | 196 | 83 | 91 | 105 |
| [R9875](r9875.md) | 904 | 379 | 465 | 439 |
| [R9876](r9876.md) | 137 | 44 | 57 | 80 |
| [R9877](r9877.md) | 40 | 19 | 20 | 20 |
| [R9878](r9878.md) | 48 | 14 | 14 | 34 |
| [R9879](r9879.md) | 112 | 58 | 62 | 50 |
| [R9880](r9880.md) | 116 | 64 | 71 | 45 |
| [R9881](r9881.md) | 106 | 47 | 51 | 55 |
| [R9883](r9883.md) | 303 | 98 | 122 | 181 |
| [R9884](r9884.md) | 183 | 111 | 118 | 65 |
| [R9885](r9885.md) | 8 | 2 | 2 | 6 |
| [R9886](r9886.md) | 60 | 25 | 30 | 30 |
| [R9887](r9887.md) | 294 | 145 | 155 | 139 |
| [R9889](r9889.md) | 179 | 94 | 110 | 69 |
| [R9890](r9890.md) | 188 | 72 | 86 | 102 |
| [R9891](r9891.md) | 278 | 118 | 138 | 140 |
| [R9892](r9892.md) | 56 | 33 | 34 | 22 |
| [R9893](r9893.md) | 95 | 46 | 51 | 44 |
| [R9894](r9894.md) | 62 | 27 | 29 | 33 |
| [R9895](r9895.md) | 165 | 63 | 70 | 95 |
| [R9896](r9896.md) | 707 | 293 | 305 | 402 |
| [R9897](r9897.md) | 802 | 340 | 380 | 422 |
| [R9898](r9898.md) | 1,482 | 679 | 849 | 633 |
| [R9899](r9899.md) | 119 | 47 | 56 | 63 |
| [R9900](r9900.md) | 592 | 336 | 351 | 241 |
| [R9901](r9901.md) | 29 | 7 | 8 | 21 |
| [R9903](r9903.md) | 633 | 236 | 255 | 378 |
| [R9904](r9904.md) | 281 | 105 | 120 | 161 |
| [R9905](r9905.md) | 374 | 120 | 129 | 245 |
| **All 30** | **9,640** | **4,343** | **4,906** | **4,734** |

## How to read the decode

Each record page ends with the decode, row by row. It is the plain output of `key/key.tsv` applied to the rows file. Each line gives the record, the image page and the row.

| Mark | Meaning |
| --- | --- |
| `abc` | a value of the ledger's key |
| `abc?` | a value of the ledger's key, with a doubt mark |
| `{abc}` | a value that I added (`key/added-values.tsv`); here this mark does not mean a probable word |
| `[abc]` | a value of the clerk copies that is not in the key; never counted as read |
| `_abc_` | a clear word of a mixed row, not cipher |
| `·` | a unit that no key holds |
| `…` | a `?` position of my rows: not cipher, or not read |
| `a-b-c` | units joined by hyphens: letters spelled sign by sign, with the units next to them |

- A value of no letters (the switch `f~`, the opener `v db`, a null) does not show.
- The spaces of the decode are not word divisions. A code value for a syllable stands apart (`manda do`), and a spelled run can hold several words.

## Who read these letters before

- **This ledger.** It read f. 128 (R9877, with the duplicate R9878) in part, from 18 September 2026. It read R9873 in part (`r9873_reading.md`, 23 October 2026) and decoded R9898 (`r9898_reading.md`). It read the cipher of R9881, R9883, R9884, R9890, R9893 and R9897 against their clear texts to build its key (`key_working.md`, passes 1 to 14), and the margin of R9899 (pass b23). Each record page credits this.
- **Brice Dudout** aligned R9873 with its period clear, BNE MSS/20214/52-1, and built KS4 from it and from other period pairs (29 October 2026).
- **The clerks of the time.** Decipherments of the time stand with R9881 (f. 140), R9883 and R9884 (ff. 172-173), R9890 (f. 324), R9893 (f. 485), R9895 (f. 516) and R9897 (ff. 14v-15), and in the margins of R9898 and R9899 (the ledger's notes). A clear copy of the time also stands with R9889, R9896, R9900 and R9901 (`check.md`, section 5).
- **The Calendar of State Papers, Spain** (vols. ii and iii.1, G. A. Bergenroth) summarises several of these letters in English. The ledger's notes give the numbers (for example nos. 636 to 638 for R9873, no. 663 for R9894).

## Limits

- Every record is decoded, not read. The decode has holes in most rows. No record here builds sentences.
- **The rows** are a transcription of the DECODE images. Two passes over the same pages agree on about two thirds of the three-letter codes. A misread sign gives a wrong value or a hole.
- **The sign names** of my rows change from page to page. Off the 14 aligned pages, a sign read through the map is doubtful.
- **27 of the added values** rest only on the ledger's own readings of R9873, R9898 and f. 128. Those readings use some values that the ledger marks as adopted on sense. So these 27 values are only as sure as those readings.
- **16 of the added values** rest on one place and a weak value of the clerk copies. The check of that rule passed on few units (15 right, 0 wrong).
- **The clear words:** 25 of the 34 labels were cut on the evidence of a word list alone (97 units). A few of them may be cipher.
- **The summaries** on the record pages give the sense of what the decode carries. They are not readings. For R9873, R9877 and R9878, the ledger's readings are fuller, and the summaries may follow them in places. The page of R9877 says which part comes from the ledger's reading.
- **Two choices move the numbers:** the 20 added values that may be my spellings of ledger codes, and the 25 clear-word labels on a word list alone. Either can move units among "ledger key", "added" and "cipher".

## Credit

- **DECODE**, the database of historical ciphers of the DECRYPT project: records R9873 to R9881, R9883 to R9887, R9889 to R9901 and R9903 to R9905. Record pages: https://de-crypt.org/decrypt-web/RecordsView/ followed by the number, for example https://de-crypt.org/decrypt-web/RecordsView/9873. Héder and Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- **The archive:** Real Academia de la Historia, Madrid, Colección Salazar y Castro A-31 (9/31) and A-34 (9/34).
- **The key:** Daniel Bourdeau (`key_working.md`) and Brice Dudout (KS4).
- **The clear texts of the time behind the added values:** Biblioteca Nacional de España, MSS/20214/52-1; the clear leaves of the Real Academia de la Historia, A-31 ff. 140, 172, 324, 482, 485 and 516.
- **The ledger's readings behind the added values:** R9873, R9898 and f. 128.
- **Dates:** the Calendar of State Papers, Spain, vols. ii and iii.1.

DECODE's images are for research use only. They may not be redistributed or published without permission from the archive. No DECODE image is published. The rows in `transcription/` are a transcription of the DECODE images. No DECODE transcription file is in this folder.
