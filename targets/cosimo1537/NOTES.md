# Cosimo I de' Medici to Agnolo Niccolini, 1537 to 1539

Florence, Archivio Niccolini di Camugliano, Fondo antico 214, inserto 1. DECODE records R4034 to R4039, R4041 to R4050 and R4052 to R4054: 19 letters. DECODE record R4033 is the archive's key table.

Status: in progress. This folder is a contribution from outside (prabal-rje), sent as a pull request. The maintainer sets the status, the class and the reading review. What was set on 20 November 2026 is in the section "The maintainers' review at integration" below.

## What the documents are

- Letters of Cosimo I de' Medici, Duke of Florence, to his envoy Agnolo Niccolini, December 1537 to August 1539. The letters are in clear Italian, with cipher passages inside them.
- R4040 (a letter of Maria Salviati, in another system with too few codes) and R4051 (no cipher) are not in this folder.

## The systems

- **The earlier system** (R4034 to R4038, December 1537 to March 1538): one- and two-digit codes for letters, and word signs, some under a bar. The archive's key table (R4033) serves it.
- **The main system** (R4039, R4041 to R4050, R4052 to R4054, October 1538 to August 1539): one- and two-digit codes with no spaces between them. a and o each have two codes. Code 74 stands for "che"; code 36 is read as a null. The archive's key table does not serve it.

## The keys

| Source | What it gives |
| --- | --- |
| The archive's key table, DECODE record R4033, as I read it (`key/key-table-R4033.tsv`) | every value of the earlier system's decode, apart from code 29 |
| My own key from ciphertext (`key/key-main.tsv`) | every value of the main system's decode: 21 codes with a value |
| My own blind key of the earlier system (`key/key-earlier-blind.tsv`) | one value of the decode: code 29 = t, from ciphertext, which the table does not hold (`key/key-table-R4033.tsv` holds it on a line of its own); the key is graded against the table in `check.md`, section 3 |

## The transcription

- A transcription of the DECODE images: 19 files in `transcription/`, one for each letter.
- `TRANSCRIPTION.md` gives the form, the marks, the known challenges and the counts.

## The order of events

The order of events is part of the result. The times are UTC−5.

1. 16 November 2026, 16:15: my read of the main system, from the cipher text alone, fixed. R4049 was decoded with the same key by 16:35, with no further fit.
2. 16 November 2026, 22:09: my blind read of the earlier system, from the cipher text alone, fixed.
3. 17 November 2026, 19:33: that blind read compared with the archive's key table: "supports" (16 of 17 shown codes agree). Then the five letters were decoded with the table.
4. 19 November 2026, 09:05: the read of both systems public on my repository, https://github.com/prabal-rje/branicki-1757/tree/main/cosimo-1537.
5. 19 November 2026, after that: I looked up the affair of Biagio della Campana in Ferrai (1882) and Staffetti.
6. 19 November 2026, 15:31: the ledger's maintainer named Ferrai's footnote with a sister letter (issue 802). At 15:56 my read of R4054 was compared with it: "cannot tell" (`check.md`, section 2).
7. 19 November 2026, in the evening: I looked at the archive's table again for code 29. It shows 29 only with a bar, as a word sign. The decode of the earlier letters then took 29 = t from ciphertext, and I made the readings of R4034 to R4038 from that decode.

The check against the print came after the read. The times rest on my own record. This folder adds no hash table and no other record of provenance.

## The frozen read

- `key/frozen-read.md`: the rows as read, as they stand on my public pages, with the key `key/key-main.tsv`. Both went public on 19 November 2026 at 09:05 and have not changed since.

## The decode

- Each record page ends with the decode, row by row: the codes of the cut and the plain output of the key. Nothing in it is edited.
- The main system: 609 code tokens of the 14 letters have no value in the key.

## The readings and the counts

- The readings of the main system are the ones of my public pages; R4046 has one change, which its page states. They mark supplied letters with brackets, but not every letter that stands on a hidden code. The decode is the reference.
- The readings of R4034 to R4038 are not on my public pages. I made them on 19 November 2026 from the decode of this folder, with code 29 = t. They mark every letter and word that the key does not give. Together they have 446 cipher words: 346 sure and 100 holes (295 sure if every word on code 29 is a hole).
- Every document was filed as "decoded, not read". Maintainers' note, 20 November 2026: R4035, R4037 and R4038 are now marked "read in part" (next section); the other 16 documents stay "decoded, not read". `README.md`, "The counts by the word rule", gives the number of cipher words, the sure words and the holes of each document, and how they are counted.

## The maintainers' review at integration (20 November 2026)

This section is not the contributor's. It records the review of pull request 822, made for the maintainers by an AI agent. No person has checked it. The rest of these notes are the contributor's own words, apart from the lines marked as a maintainers' note or as added at integration.

**What was checked**

- A decoder written by the reviewer from `key/key-table-R4033.tsv` and the digit rows gives the decode of the record pages on 78 of 78 rows of R4034 to R4038. The 1,791 code tokens are 1,667 with a value from the table, 70 on code 29, 17 on a code that the key does not hold and 37 doubtful.
- An alignment of the five readings with the decode finds no place where a reading departs from the decode without a mark. The recount of the cipher words agrees with the contributor's counts.
- All 70 tokens of code 29 fall on a t of the readings, with no change.
- The file `cosimo-1537/key-earlier.tsv` of the contributor's public repository, in its commit of 19 November 2026, 14:05 UTC, is byte for byte `key/key-earlier-blind.tsv` and holds 29 = t.
- Not checked: the digit rows and the key table against the DECODE images. The reviewer did not have them.

**The states of R4034 to R4038**

| Record | State | Cipher words | Sure | Holes | Read share | Why |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| R4034 | decoded, not read | 112 | 77 | 35 | 0.688 | it builds sentences only in passages 4, 6 and 8; the clear words around its short cipher runs are not in the folder |
| R4035 | read in part, grade B | 29 | 26 | 3 | 0.897 | two coherent clauses; three holes of one letter each, which is one hole over the floor for a text under 40 cipher words |
| R4036 | decoded, not read | 12 | 1 | 11 | 0.083 | two rows; no sure sense can be given |
| R4037 | read in part, grade B | 243 | 201 | 42 | 0.827 | five passages of coherent Italian, raw: 22 of the 42 holes are words with one to three letters marked inside, 8 are unread words on the codes 1 1 and 10 |
| R4038 | read in part, grade B | 50 | 41 | 9 | 0.820 | two coherent sentences; seven of the nine holes are one or two letters inside a word |

- The 14 letters of the main system stay "decoded, not read", as the contributor filed them.
- The grade is a model's reading of the Italian against the English, recorded in `profile.json` (`reading_review`). It is not the contributor's, and no person has checked it.
- By the sentence score of `docs/_check_reading.py` (a sentence is clean with at most one hole in ten words) the three letters have 1 of 2, 1 of 7 and 0 of 2 clean sentences, as their pages say. That is why they were filed as "decoded, not read". The README makes the reading as sentences the test, not that score, and the grade B rests on it: most holes are one to three letters marked inside a word that otherwise stands in the decode.
- The target as a whole: 3 of the 19 documents are read in part. `profile.json` gives the class "read in part" and names the method from the part that reads, "read with known key" (the archive's table). The main key, from ciphertext, is the second part: key obtained, text not read.
- Of the 6,842 code tokens of the 19 letters, 1,327 are tokens with a value and no doubt in the three letters that are read in part (0.194). By cipher words in those three letters: 268 of 322 sure (0.832).

**The count rule for code 29**

- Code 29 = t stands in `key/key-table-R4033.tsv`, a key file that `profile.json` names in `outcome.key_file`, on a line of its own with the source "from ciphertext". It is the value of the contributor's blind read, public since 19 November 2026, 14:05 UTC, before the review asked about it.
- A word on code 29 counts as given by the key. The main system is counted the same way: its whole key is from ciphertext.
- So the counts of record are 26 of 29 for R4035 and 201 of 243 for R4037. With every word on code 29 as a hole they are 17 of 29 and 159 of 243. No state depends on the choice.

**Three checks on the images, proposed to the contributor and not made**

- Whether the sign transcribed 29 in R4035 and R4037 is the table's 79.
- Whether the codes 1 1 and 10 of R4037 carry the bar of the table's word signs.
- Whether the second 4̅6̅ line of the table is 4̅7̅.

"Remaining gaps" lists them with what is known.

## Other support of the main system

- **The two halves solved apart agree:** the letters of 1538 and of 1539, each read alone, give the same values for every shown code (`check.md`, section 1).
- **The language checks:** the read scores as Italian above a shuffled text, Spanish and Latin.
- **The names that fit outside sources:** Bartolomeo Valori and his sons, Francesco Valori, Giulio the natural son of Duke Alessandro, Gian Francesco da Mantova. Some hold supplied letters.
- **The printed affair:** the passage of R4054 fits the affair of Biagio della Campana in Ferrai (1882).

## Earlier readers and print

- **The archive:** the key table R4033 is of the time.
- **Print:** Ferrai (1882), p. 136, note 1, to p. 137, prints the wording of a sister letter of R4054: Cosimo to Pirro Musefilo, 8 August 1539. It does not print R4054 itself. Luigi Staffetti, *Il cardinale Innocenzo Cybo*, pp. 211 to 214, tells the same affair. I found no print of the other letters.
- **Drafts:** Staffetti cites a draft of Cosimo to Niccolini of 12 October 1538 in the "Minute", filza I, of the Archivio di Stato di Firenze. A draft of these letters there would check the reading word by word. I did not look.

## Remaining gaps

- 609 code tokens of the main system have no value - blocker: open-codes; each of these codes has fewer than 30 tokens, except code 36 (45 tokens), which the read gives as a null.
- The main key is not checked against a key - blocker: no-key-material; the archive's table serves the earlier system only.
- 17 code tokens of the earlier letters hold a code that the key does not hold - blocker: no-key-material. Code 29 (70 tokens) takes t from ciphertext; no key checks it.
- R4043, R4044, R4045, R4050, R4052 and R4053 show short pieces only - blocker: too-short.
- The readings hold holes in most sentences - blocker: not-attempted; a reading pass against the images may close some. In R4034 to R4038, 2 of 21 sentences and fragments have at most one hole in ten words.

Added at integration (20 November 2026), from the maintainers' review:

- R4034 builds sentences only in passages 4, 6 and 8 - blocker: not-attempted; 77 of 112 cipher words are sure. Rows L10, L12, L14 and L26 are lines of clear text with cipher inside, and the clear words are not in the folder.
- R4036 gives no sure sense - blocker: too-short; two rows, 35 code tokens, 4 of them doubtful, 1 of 12 cipher words sure.
- The sign transcribed 29 in R4035 and R4037 (70 tokens) may be the table's 79 - blocker: not-attempted; 29 occurs only in R4035 and R4037, where 79 never occurs, and 79 only in R4034 and R4038, where 29 never occurs. If the images show 79, the table gives t. The same question stands for 52 in "[c]he" (57 = c) and 82 in "re[s]peto" (87 = s).
- R4037: the eight unread words `[...]` stand on the codes 1 1 (three times, after "del" or "dal") and 10 (five times, after "il" or "l") - blocker: not-attempted; the table has the barred word signs 1̅1̅ (Imꝑʳᵉ) and 1̅0̅ (Papa), and the rows of R4035 to R4038 mark no bar. Whether the images show a bar is not looked at.
- R4034, image 1, C03: code 4̅7̅ has no value - blocker: not-attempted; the table as read has 4̅6̅ on two lines between 4̅5̅ and 4̅8̅ ("stato di firenze", "questo stato"). Whether the second is 4̅7̅ is not looked at on the table's image.

## Escalation

- [x] siblings: the earlier and the main system of the same file; the earlier blind read graded against the archive's table
- [x] clear-pages: four marks above cipher rows tested; all are pen strokes
- [x] known-keys: the archive's key table R4033, for the earlier system
- [x] print: Ferrai (1882) and Staffetti; a printed sister letter compared with R4054 (`check.md`, section 2)
- [x] key-rebuild: the main key from the cipher text alone
- [ ] retry: the drafts in the Archivio di Stato di Firenze are not checked

## Files

| File | What it holds |
| --- | --- |
| `NOTES.md` | these notes |
| `README.md` | the summary, the numbers, the counts by the word rule and the marks of the decode |
| `check.md` | the checks |
| `profile.json` | the profile |
| `r4034.md` to `r4054.md` | one page for each of the 19 letters |
| `key/` | the keys and the frozen read |
| `TRANSCRIPTION.md`, `transcription/` | the digit rows |

The record pages, the keys and the frozen read come from my repository, https://github.com/prabal-rje/branicki-1757/tree/main/cosimo-1537. This folder adds the digit rows, the codes of the cut, the decode of each row, my reading of the archive's table and the counts.

## Credits

- **DECODE**, the database of historical ciphers of the DECRYPT project: records R4034 to R4039, R4041 to R4050 and R4052 to R4054, and R4033 (the key table). The record pages: https://de-crypt.org/decrypt-web/RecordsView/4033, https://de-crypt.org/decrypt-web/RecordsView/4034, https://de-crypt.org/decrypt-web/RecordsView/4035, https://de-crypt.org/decrypt-web/RecordsView/4036, https://de-crypt.org/decrypt-web/RecordsView/4037, https://de-crypt.org/decrypt-web/RecordsView/4038, https://de-crypt.org/decrypt-web/RecordsView/4039, https://de-crypt.org/decrypt-web/RecordsView/4041, https://de-crypt.org/decrypt-web/RecordsView/4042, https://de-crypt.org/decrypt-web/RecordsView/4043, https://de-crypt.org/decrypt-web/RecordsView/4044, https://de-crypt.org/decrypt-web/RecordsView/4045, https://de-crypt.org/decrypt-web/RecordsView/4046, https://de-crypt.org/decrypt-web/RecordsView/4047, https://de-crypt.org/decrypt-web/RecordsView/4048, https://de-crypt.org/decrypt-web/RecordsView/4049, https://de-crypt.org/decrypt-web/RecordsView/4050, https://de-crypt.org/decrypt-web/RecordsView/4052, https://de-crypt.org/decrypt-web/RecordsView/4053, https://de-crypt.org/decrypt-web/RecordsView/4054.
- **The archive:** Florence, Archivio Niccolini di Camugliano, Fondo antico 214, inserto 1. The archive's key table (DECODE record R4033) gives the values of the earlier system, apart from code 29.
- **The database:** Mihály Héder and Beáta Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- **The transcription, the keys from ciphertext, the decode and the readings:** prabal-rje.

DECODE's images are for research use only. They may not be redistributed or published without permission from the archive. No DECODE image is published. The digit rows in `transcription/` are a transcription of the DECODE images. No DECODE transcription file is in this folder.
