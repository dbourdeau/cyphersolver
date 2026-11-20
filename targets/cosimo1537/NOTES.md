# Cosimo I de' Medici to Agnolo Niccolini, 1537 to 1539

Florence, Archivio Niccolini di Camugliano, Fondo antico 214, inserto 1. DECODE records R4034 to R4039, R4041 to R4050 and R4052 to R4054: 19 letters. DECODE record R4033 is the archive's key table.

Status: in progress. This folder is a contribution from outside (prabal-rje), sent as a pull request. The maintainer sets the status, the class and the reading review.

## What the documents are

- Letters of Cosimo I de' Medici, Duke of Florence, to his envoy Agnolo Niccolini, December 1537 to August 1539. The letters are in clear Italian, with cipher passages inside them.
- R4040 (a letter of Maria Salviati, in another system with too few codes) and R4051 (no cipher) are not in this folder.

## The systems

- **The earlier system** (R4034 to R4038, December 1537 to March 1538): one- and two-digit codes for letters, and word signs, some under a bar. The archive's key table (R4033) serves it.
- **The main system** (R4039, R4041 to R4050, R4052 to R4054, October 1538 to August 1539): one- and two-digit codes with no spaces between them. a and o each have two codes. Code 74 stands for "che"; code 36 is read as a null. The archive's key table does not serve it.

## The keys

| Source | What it gives |
| --- | --- |
| The archive's key table, DECODE record R4033, as I read it (`key/key-table-R4033.tsv`) | every value of the earlier system's decode |
| My own key from ciphertext (`key/key-main.tsv`) | every value of the main system's decode: 21 codes with a value |
| My own blind key of the earlier system (`key/key-earlier-blind.tsv`) | no value of the decode; it is graded against the table in `check.md`, section 3 |

## The transcription

- My own transcription of the DECODE images: 19 files in `transcription/`, one for each letter.
- `TRANSCRIPTION.md` gives the form, the marks, the known challenges and the counts.

## The order of events

The order of events is part of the result. The times are UTC−5.

1. 16 November 2026, 16:15: my read of the main system, from the cipher text alone, fixed. R4049 was decoded with the same key by 16:35, with no further fit.
2. 16 November 2026, 22:09: my blind read of the earlier system, from the cipher text alone, fixed.
3. 17 November 2026, 19:33: that blind read compared with the archive's key table: "supports" (16 of 17 shown codes agree). Then the five letters were decoded with the table.
4. 19 November 2026, 09:05: the read of both systems public on my repository, https://github.com/prabal-rje/branicki-1757/tree/main/cosimo-1537.
5. 19 November 2026, after that: I looked up the affair of Biagio della Campana in Ferrai (1882) and Staffetti.
6. 19 November 2026, 15:31: the ledger's maintainer named Ferrai's footnote with a sister letter (issue 802). At 15:56 my read of R4054 was compared with it: "cannot tell" (`check.md`, section 2).

The check against the print came after the read. The times rest on my own record. This folder adds no hash table and no other record of provenance.

## The frozen read

- `key/frozen-read.md`: the rows as read, as they stand on my public pages, with the key `key/key-main.tsv`. Both went public on 19 November 2026 at 09:05 and have not changed since.

## The decode

- Each record page ends with the decode, row by row: the codes of the cut and the plain output of the key. Nothing in it is edited.
- The main system: 609 code tokens of the 14 letters have no value in the key.

## The readings and the counts

- The readings are the ones of my public pages, unchanged. They mark supplied letters with brackets, but not every letter that stands on a hidden code. The decode is the reference.
- Every document is marked "decoded, not read". `README.md`, "The counts by the word rule", gives the number of cipher words, the sure words and the holes of each document, and how they are counted.

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
- Some codes of the earlier letters are not in the table as I read it - blocker: no-key-material.
- R4043, R4044, R4045, R4050, R4052 and R4053 show short pieces only - blocker: too-short.
- The readings hold holes in most sentences - blocker: not-attempted; a reading pass against the images may close some.

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
- **The archive:** Florence, Archivio Niccolini di Camugliano, Fondo antico 214, inserto 1. The archive's key table (DECODE record R4033) gives the values of the earlier system.
- **The database:** Mihály Héder and Beáta Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- **The transcription, the keys from ciphertext, the decode and the readings:** prabal-rje.

DECODE's images are for research use only. They may not be redistributed or published without permission from the archive. No DECODE image is published. The digit rows in `transcription/` are my own transcription of the DECODE images. No DECODE transcription file is in this folder.
