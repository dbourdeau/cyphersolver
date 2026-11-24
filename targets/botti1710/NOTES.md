# The Botti letters to Cardinal Gualterio, 1710 to 1713

British Library, Add MS 20443 (papers of Cardinal F. A. Gualterio). DECODE records R8468 to R8470, R8617, R8618 and R8659 to R8718: 51 records, 194 pages with cipher rows.

Status: in progress. This folder is a contribution from outside (prabal-rje), sent as a pull request. The maintainer sets the status, the class and the reading review.

## What the documents are

- Letters to Cardinal Filippo Antonio Gualterio, 1710 to 1713, by the year numbers on the pages.
- The British Library's catalogue ([record](https://searcharchives.bl.uk/catalog/040-002090742)) describes the volume: "LETTERS of the Abbate Carlo Camillo Botti, and his uncle, the Abbate Lazaro Botti, to Card. Gualterio; Ravenna, etc., 19 Jan. 1708-26 Mar. 1713."
- It adds: "Chiefly holograph. Many in cipher, with decipherings."
- **A doubt:** so the letters may have two writers. I do not know which letters each wrote. The volume also holds copies of Gualterio's letters to Botti (from f. 294). I take each letter here to go to Gualterio; that is a doubt too.
- This ledger's catalogue entry 295 names "DECODE R8617-R8718, 48 records". DECODE has three more records of the volume with cipher: R8468, R8469 and R8470. This folder covers all 51.

## The system

- **The letters with dots (46):** number codes with a dot after each code, and spaces between groups. Most codes from 0 to 21, and two letter-like signs, stand for letters. Some codes of two to four digits stand for words, names and some letters.
- **The letters without dots (5):** the same codes, written with no dots. Some pages write signs of their own.
- The cipher writes double letters twice.
- `key-and-read/key.tsv` gives each code, its value, the source of the value, its count and the clerk's agreement at its places.

## The key

| Source | What it gives |
| --- | --- |
| The ciphertext (my own key) | 21 codes for letters; code 17 as r, open between r and q |
| The clerk's decipherment on the page | 14 values: 110 Mons.re, 116 subito, 145 ue, 50 cardinale, 53 abbate, 5u Card., 62 Ruffo, 65 conte, 93 Ferrara; and the letter values of 00, 01, 18, 1u and 71 |
| A page of the letters without dots | the values of sign labels on six pages (`key-and-read/key-page-signs.tsv`) |
| Open | 90 rare codes (191 tokens in the letters with dots) |

- No value came from another person's key. The Gualterio cipher tables (British Library, Add MS 20244) were not opened.
- The decode of the letters with dots uses the values from the ciphertext only. It shows the 14 values from the clerk as `·`. The decode of the letters without dots uses them.

## The transcription

- A transcription of the DECODE images: two readings of each page and a reconciliation.
- 191 files, one for each page with cipher digits: 2,568 rows, 59,042 digits, 3,261 doubt marks and 1,596 notes.
- The rows of the 1710 letters are the hardest: there the two readings of a page agree least.
- Clear words inside a cipher row are not copied: `[not copied]` stands in their place.
- `TRANSCRIPTION.md` gives the marks and the counts for each record.

## The frozen read

- The read as it stands in my repository, https://github.com/prabal-rje/branicki-1757/tree/main/botti-1710, from its commits of 19 November 2026 (09:05 and 09:11, UTC−5).
- The key was fixed on 16 November 2026 before any clear row of the clerk was opened. `key-and-read/README.md` gives the order of events.
- This folder adds no hash table and no other record of provenance.

## The decode

- Each record page gives the decode row by row, and names the cipher row of each line.
- 35,235 code tokens and decode units on 143 pages: 26,044 code tokens of the letters with dots and 9,191 decode units of the letters without dots. 34,561 show a value.
- No document builds sentences. By the read bar, each of the 51 documents is "decoded, not read" in `profile.json`.

## Why no word count

This ledger's rule of 19 November 2026 counts sure cipher words. I give no word count, for three reasons:

1. No reading divides these decodes into words. The spaces of the page do not mark every word: many groups run several words together.
2. The decode also breaks at the notes of the transcription. So one word can stand in two or three groups.
3. A fully decoded group is only the output of the key. No reading checks it as a word.

So each record page counts code tokens, open codes and items that are not codes, under those names. The floor for texts of under 40 words is not used: no document is claimed read.

## Earlier readers

- **The clerk of the time:** 29 letters with dots carry a decipherment above the cipher rows, and R8618 carries a few words of the clerk's hand. DECODE marks inline plaintext on these 30 records. This folder does not copy that text. 14 code values come from it, and `check.md` grades the blind decode against it.
- **The Gualterio cipher tables** at the British Library (Add MS 20244): this ledger's catalogue names them for entry 295. They are not on DECODE, and they are not online by this ledger's note. I did not open them.
- **DECODE:** all 51 records give status "N/A" and cipher type "Unknown" (checked 16 November 2026).
- **This ledger:** entry 295 stands in the list of letters readable with keys in hand. No target folder and no reading names Add MS 20443 (checked 16 November 2026). Two key files of `targets/bay1706` (`keys/DOC_R588_D2150_2150.txt` and `keys/DOC_R556_D2828_2828.txt`) hold the name "Bottigor" or "Bottiger", not "Botti". They are not about these letters (read on 19 November 2026).
- **Print:** not searched.

## Remaining gaps

- Code 17 (255 tokens): r or q - blocker: open-codes; the clerk writes r 66 times and q 39 times at its places.
- Code 17 before code 10 (`17.10.`): 74 places in the rows of the letters with dots where both signs are sure, and 26 more where a sign is doubtful (100 in all, by the leading reading of each doubtful sign). At one more place (R8695 T003 C13), a sign marked `[?]` follows 10. At the 72 sure places on pages decoded here, the decode gives 52 groups, most often raesto (8), raale (5), raesta (4) and rael (3); with 17 = q and 10 = u, these four read questo, quale, questa and quel. Some groups read with r, for example fratello, tragedia and ringrazio - blocker: open-codes; the key keeps 17 as r and 10 as a.
- 90 rare codes with no value (191 tokens in the letters with dots) - blocker: no-key-material; the Gualterio cipher tables (Add MS 20244) may give them; not opened.
- Five pages not shown (R8662 T003, R8666 T003, R8674 T001, R8677 T001, R8710 T004) - blocker: unknown; their decode was made, and it is not sure.
- R8618 T002 - blocker: unknown; several tries on 16 to 18 November did not decode it; one code stands between spaces, and the word breaks are not known.
- R8468 T003 and T007 - blocker: illegible; T003 is a clipped fragment; on T007 the values of five sign labels are not sure.
- 45 pages under 100 digits or with no cipher digit - blocker: too-short.
- No reading in sentences for any document - blocker: not-attempted.

## Escalation

- [x] siblings: one key for all 51 records (the letters without dots read with the key of the letters with dots; `check.md`)
- [x] clear-pages: the clerk's decipherments on 29 letters, as a grade and for 14 code values (`check.md`)
- [ ] known-keys: the Gualterio cipher tables (BL Add MS 20244) not opened
- [x] known-keys: the two key files of `targets/bay1706` name "Bottigor" or "Bottiger"; they are not about these letters
- [ ] print: not searched
- [x] key-rebuild: the key from the ciphertext alone (`key-and-read/`)
- [ ] retry: a reading in sentences of the decode

## Files

| File | What it holds |
| --- | --- |
| `NOTES.md` | these notes |
| `profile.json` | the profile |
| `README.md` | the summary, the numbers and the table of records |
| `check.md` | what was checked against what |
| `r8468.md` to `r8718.md` | one page for each of the 51 records |
| `key-and-read/` | `key.tsv`, `key-page-signs.tsv` and the order of events of the frozen read |
| `TRANSCRIPTION.md` | the transcription: what it is, its marks and its counts |
| `transcription/` | the cipher rows: one file for each page with cipher digits |

The record pages, the key and the summaries come from my repository, https://github.com/prabal-rje/branicki-1757/tree/main/botti-1710. The changes for this folder:

- Each record page names the cipher row of each decode line.
- Each record page gives counts, and marks the summary as a guess.
- `key.tsv` gains one credit line.
- No value and no decoded row changed.

The scripts of the read, the grade and the decode are not in this folder.

## Credit

- **DECODE**, the database of historical ciphers of the DECRYPT project: records R8468 to R8470, R8617, R8618 and R8659 to R8718 (51 records; the table of records lists them). Each record page links its DECODE record page, `https://de-crypt.org/decrypt-web/RecordsView/<n>`.
- **The archive:** British Library, Add MS 20443 (papers of Cardinal F. A. Gualterio): letters of the Abbate Carlo Camillo Botti and of his uncle, the Abbate Lazaro Botti, to Cardinal Gualterio, 1708 to 1713 ([British Library catalogue](https://searcharchives.bl.uk/catalog/040-002090742)).
- **The database:** Héder, M. and Megyesi, B. (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- **The clerk of the time** who wrote decipherments on 29 of these letters: 14 code values of the key come from that text. `key-and-read/key.tsv` marks each one.

DECODE's images are for research use only. They may not be redistributed or published without permission from the archive. No DECODE image is published.

## 24 Nov 2026 - code 17 checked by a blind reader (Brice Dudout, with Claude), `dudout/`
A blind sheet of 14 questions (11 signs, 3 controls, 3/3) asked which digit follows the 1 in the "17" groups of R8469
and R8470. At 9 sites it is a 7, and every site with a sure context is q (quale, questa, quanto, qua); at 2 sites
(proprio, risposi) it is a 2, i.e. code 12 = r misread as 17. Proposal, {probable}: 17 = q, and 10 after 17 = u. On the
11 groups, 2 give an Italian word before and 9 after, with no sure word broken. The other "17" tokens are not switched
(dinari, rema would break). Details and files in `dudout/README.md`; no DECODE image is committed.
