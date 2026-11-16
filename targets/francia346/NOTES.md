# Barberini to Nuncio Ceva, Rome, 1633: 22 later cipher letters of Francia 346

Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346. DECODE records R5626, R5635, R5636, R5637, R5640, R5642, R5643 and R5645 to R5659: 22 records, 35 cipher pages.

Status: in progress. This folder is a contribution from outside (prabal-rje), sent as a pull request. The maintainer sets the status, the class and the reading review.

## What the documents are

- Letters of 1633 from Rome to Francesco Adriano Ceva, extraordinary nuncio in France. Their clear endorsements name Cardinal Barberini.
- They belong to the same dossier as `targets/ceva1632` (DECODE R74 to R84), and to catalogue entry 880 (DECODE R5625 to R5686).
- Of entry 880, this folder covers 22 records. R5625 is a letter in clear. The 17 records R5667, R5668 and R5672 to R5686 use other signs and stay open.
- Our repository also has pages for the other 22 records of the entry. They are not in this pull request (`README.md`, "The other records in our repository").

## The system

It is the cipher of `targets/ceva1632`.

- A lone 6 is a word space. The ten pairs 2x are nulls.
- Two-digit codes stand for letters and syllables.
- Three-digit codes stand for words and names.

`key-and-key-free-read/key.tsv` gives every code, its value on the pages, its grade, the source of the value and a ledger mark.

## The key

| Source | What it gives |
| --- | --- |
| The published key: George Lasry, Beáta Megyesi and Nils Kopal (2020); DECODE key note of 24 October 2020 | 61 pair codes: 40 letter codes for 19 letters, and 21 syllable codes |
| This ledger, `targets/ceva1632/cipher.py` | the form (6 and 2x); 23 three-digit values, of which the first pass kept 22 |
| This ledger, `targets/ceva1632/NOTES.md`, re-read of 22 to 23 October 2026 | 5 more three-digit values (541, 171, 473, 497, 491); 104 is Olandesi, not Svedesi; pair 88 is del, not quel; pair 33 is gli |
| This ledger, the readings of R75 and R84 (`R75-R84_reread_log.md` and the two reading files) | 19 values read off the decipherments of 1632 and not adopted; the second pass shows them as conjectures |
| Our own | no value of the decode |

- **The 28 values.** The first pass used 28 three-digit values from this ledger: 22 from `cipher.py`, and 6 from the re-read (the 5 new values and 104). The column "ledger mark" of `key.tsv` marks each one `one of the 28`.
- **The check of 14 November 2026.** Each of the 28 values, and pairs 88 and 33, equals the value in the ledger file that its source cell names. The one exception is 129: `cipher.py` keeps regno, the re-read log drops it, and the graded pages leave it open. The ledger's `targets/ceva1632/` files did not change after 13 November.
- **The second pass** grades each value: 14 certain, 7 probable, 25 conjecture. `README.md`, "The grades of the code values", gives the test.
- The ledger's `R75-R84_reread_log.md` drops 129 (regno) in favour of 171. `cipher.py` keeps 129. The first pass used it; the graded pages leave it open.
- The published key gives no three-digit code a value.

## The transcription

- A machine transcription of the DECODE images. Each page had three model passes: a draft, a source check and a reconciliation.
- No person verified it against the images.
- It holds 35 cipher pages, 539 rows and 28,643 read digits, with marks for doubtful digits and gaps.
- `TRANSCRIPTION.md` gives its known challenges and its counts for each record, and says where the rows are.

## What came first

The order of events is part of the result. `key-and-key-free-read/README.md` gives it in full.

1. A key found from the ciphertext alone, on 13 records, fixed at 01:27 on 12 November 2026 (UTC−3). The 13 records are R74 to R78 and earlier transcriptions of 8 records here: R5626, R5635, R5636, R5637, R5640, R5643, R5647 and R5648.
2. The published key, first opened from 01:40 to 02:00 the same day, to compare my fixed key with it. The comparison is in `francia-346-leaves/check.md` in our repository. I changed no value of my key after it: code 07 still reads l, where the published key has h.
3. A read of the 22 records with that unchanged key and no new fit, fixed at 17:00 the same day.
4. The published key applied to the 22 records, at about 17:05. The grade and the full decode came after it.

## The frozen key-free read

This is the part found without the published key. `check.md` grades it against the published key.

- Of the true letters that it shows, 98.8% are right (6,930 of 7,017). All 87 wrong letters are code 07: the key gives h, the key-free key gives l.
- But only 62.0% of its graded shown tokens are letter codes (7,017 of 11,324). The rest are syllables, nulls or false pairs of its cut.
- On the 8 records inside the key's fit: 99.0% right (3,091 of 3,122). On the 14 records outside it: 98.6% right (3,839 of 3,895).
- Its cut has no three-digit codes. So it reads none of the words and names.
- `key-and-key-free-read/` holds its key (`key-free-key.tsv`), its declaration (`DECLARE.md`) and the read (`READ-digit.md`). The two frozen files are edited copies; their note lists the kinds of edit. No number, rule or decoded row changed.
- The times rest on our own record. We add no hash tables to our files.

## The decode with the published key

- 10,919 code tokens. In the first pass, 10,081 had a value (92.3%). The graded pages give 515 three-digit tokens a value (142 certain, 131 probable, 242 conjecture) and leave 639 open. So 10,245 code tokens (93.8%) show a value. (`README.md`, "The numbers".)
- Each record page (`r5626.md` to `r5659.md`) gives a summary, a reading in Italian, an English translation, the names and the decode row by row.
- The readings are partial. Most sentences hold one or more holes. By the README read bar, we mark each document "decoded, not read" in `profile.json`. A reader's review can change this.
- Some ledger values do not fit these letters. For example, code 470 ("hor") stands where no "hor" can stand. Each record page lists such places.

## Earlier readers

- **Decipherment leaves of the time:** R5626 (f. 155r), R5637 (f. 212v) and R5646 (f. 269r). Brice Dudout's notes of 29 October 2026 (`research/dudout_2026-10-29/`) add R5655 (f. 324).
- `check.md`, section 7, aligns the decode with the three leaves: 58.0%, 71.1% and 78.7% of the shorter text align with equal letters. The leaves of other records give 31.7% to 48.9%.
- **DECODE:** on 12 November 2026, the public record pages of R5625 to R5659 give the status "N/A" and the cipher type "Unknown". They mark the ciphertext as private. The word "Decryption" appears on each page. Its documents need a login, and we did not open them.
- **This ledger:** entry 880 lists R5625 to R5686 as "N/A", with no decipherment filed. The notes of 29 October 2026 decode R5630, which is not in this set.
- **Print:** `README.md` names one study and no edition of these letters.
- **Clear drafts:** A. Leman (1920) used the Barberini library's minutes of Francesco Barberini's cipher despatches to Ceva. We did not check which letters those minutes hold. So clear drafts of some of these letters may have been in use in print since 1920.

## Reports in issue 501 that this folder does not apply

- **bdudout, comment of 13 November 2026:** four code values from the decipherment of the time on f. 155 of R5626, which that user reports as not in this ledger: 951 = Madrid, 749 = Commissarii, 444 = come (probable) and 901 = Legatione (probable). In the same place, that user reads pair 25 as a null.
- **bdudout, comments of 13 and 14 November 2026:** a second transcription and decode of R5640 (f. 237v), for comparison only. That user claims no reading from it.
- The maintainer's comments of 14 November record these values on catalogue 880 as that user's report.
- This folder does not use these values or that second reading. We make no claim on them, and we did not check them.

## Remaining gaps

- 639 three-digit tokens have no value after the second pass (803 after the first) - blocker: no-key-material; the published key and the ledger give no value for these codes.
- Four pages in three records do not read: R5642 f. 246r, R5656 f. 337r and R5657 ff. 342r–v - blocker: not-attempted; on these pages 8 is rare and 6 is common, so the transcription may read some 8s as 6. A declared correction of misread digits failed its own check on a page that reads. This folder keeps the first transcription. Our repository decodes a second machine reading of these pages (`francia-346-full/rereads.md`). No person read the images.
- R5643, R5658 and R5659: most cipher rows hold no read digit - blocker: not-attempted in this folder; the same second machine reading covers these pages.
- Ledger values that do not fit these letters, such as 470 - blocker: open-codes.
- The 17 records in other signs (R5667, R5668, R5672 to R5686) - blocker: not-attempted; a test before the key found another system.

## Escalation

- [x] siblings: the 13 records of the key-free fit (R74 to R78 and 8 records here); `targets/ceva1632` for the published key and the ledger's values
- [x] clear-pages: the decipherment leaves of R5626, R5637 and R5646, as a check only (`check.md`, section 7); not used for any value
- [x] known-keys: the published key of Lasry, Megyesi and Kopal (2020), with the ledger's values
- [ ] print: not searched for this pull request; the minutes that Leman (1920) used are not checked
- [x] key-rebuild: a key from the ciphertext alone, before the published key (`key-and-key-free-read/`)
- [ ] retry: no person checked the transcription; a second machine reading of ten pages is in our repository, not in this folder

## Files

| File | What it holds |
| --- | --- |
| `NOTES.md` | these notes |
| `profile.json` | the profile |
| `README.md` | the summary of the decode, the numbers, the grades, the table of records and the marks of the decode |
| `check.md` | the grade of the frozen read against the published key, and the checks of 13 November |
| `r5626.md` to `r5659.md` | one page for each of the 22 records |
| `key-and-key-free-read/` | `key.tsv` (the key of the decode), `key-free-key.tsv`, `DECLARE.md` and `READ-digit.md` (the frozen key-free read), and a note |
| `TRANSCRIPTION.md` | the transcription: what it is, its known challenges, its counts, and where the rows are |
| `transcription/` | the digit rows: one file for each of the 35 cipher pages |

`README.md`, `check.md`, the 22 record pages and the files of `key-and-key-free-read/` come from our repository, https://github.com/prabal-rje/branicki-1757/tree/main/francia-346-full. These changes adapt them to this folder or correct them:

- **A correction kept from our draft:** `r5653.md`, English translation, C01–C07: "I have seen" became "I have [?seen]", to keep the doubt of the Italian "Ho [?visto]". Its summary now says "Rome has [?seen]".
- **The same correction in `r5648.md`:** English translation, f. 279v, C14–C17: "I have seen" became "I have [?seen]", for the Italian "Ho [?veduto]".
- **A new correction:** `key-and-key-free-read/README.md` called the key-free column "the last column". It now names the column.
- **`check.md`, the credit line:** "records R5626 to R5659 of this folder" became "records R5626 to R5659", because this folder holds 22 of them.
- **Links:** paths to files outside this folder now link to our repository.
- **`README.md`** keeps only the 22 records of this folder. It drops the sections on the records added on 13 November, and one short section points to them in our repository. Its credits and its list of files name this folder.
- **`key-and-key-free-read/`:** `key.tsv` gains the column "ledger mark". `key-free-key.tsv` is our public `francia-346-leaves/key.tsv` with one credit line added.

The scripts of the read, the grade and the decode are not in this folder.

## Credits

- **DECODE**, the database of historical ciphers of the DECRYPT project: records R5626, R5635 to R5637, R5640, R5642, R5643 and R5645 to R5659. https://de-crypt.org/decrypt-web/RecordsList
- **The archive:** Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346.
- **The key:** George Lasry, Beáta Megyesi and Nils Kopal, "Deciphering papal ciphers from the 16th to the 18th Century", *Cryptologia* 45(6), 2021 (online 2020), doi:10.1080/01611194.2020.1755915.
- **The ledger's values:** `targets/ceva1632`.
- **The decipherment leaves:** Brice Dudout's notes of 29 October 2026.
- **The transcription, the key-free read, the decode and the readings:** prabal-rje.

DECODE's images are for research use only. They may not be redistributed or published without permission from the archive. This folder holds no image.
