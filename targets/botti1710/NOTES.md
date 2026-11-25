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

- The frozen read of the initial 143 pages stands in my repository, https://github.com/prabal-rje/branicki-1757/tree/main/botti-1710, from its commits of 19 November 2026 (09:05 and 09:11, UTC-5).
- Four previously withheld dotted pages (R8666 T003, R8674 T001, R8677 T001, and R8710 T004) were decoded on 22 November 2026 (`branicki-1757` commit `681ed424180eb3690b2fd33928fce4de9ace553d`, 2026-11-22 21:34:50 UTC-5) and are outside the 19 November frozen read. R8666 and R8674 carry no clerk's decipherment; R8677 and R8710 carry a clerk's decipherment that had already been opened for grading the 29 glossed letters on 16 to 19 November, so those two pages are not claimed as blind. The decode of all four pages here is the unedited mechanical output of the unchanged 16 November ciphertext-only key (`scripts/decode_four_pages.py`), showing all 14 clerk-derived values as `·`.
- The key was fixed on 16 November 2026 before any clear row of the clerk was opened. `key-and-read/README.md` gives the order of events.
- This folder adds no hash table and no other record of provenance.

## The decode

- Each record page gives the decode row by row, and names the cipher row of each line.
- 35,757 code tokens and decode units on 147 pages: 26,566 code tokens of the letters with dots (including 522 tokens across the four pages added on 22 November 2026) and 9,191 decode units of the letters without dots. 35,062 show a value.
- Seven pure-blind dotted letters (`R8660`, `R8661`, `R8664`, `R8665`, `R8668`, `R8673`, `R8718`; none carries any contemporary clerk decipherment, and their mechanical decodes use only the 21-letter ciphertext-only key with all 14 clerk-derived values hidden as `·`) have working word-divided Italian readings (`readings/rXXXX_reading.md`) and English translations (`readings/rXXXX_en.md`) linked from `profile.json` and awaiting maintainer reading review. `scripts/verify_readings.py` verifies zero unmarked departures from the unedited mechanical decodes: 524 of 804 cipher words sure (0.652; R8718 57/72 = 0.792, R8673 77/103 = 0.748, R8661 85/124 = 0.685, R8668 88/129 = 0.682, R8660 124/203 = 0.611, R8665 34/61 = 0.557, R8664 59/112 = 0.527). All 51 documents remain filed as "decoded, not read" in `profile.json` pending maintainer review.

## Word counts

For the seven pure-blind letters with readings (`readings/rXXXX_reading.md`), `scripts/verify_readings.py` applies the rule of 19 November 2026: every unmarked sure word appears verbatim in unbroken order in the unedited mechanical decode of `rXXXX.md`, and every bracketed restoration `[x]` (including `17 -> [q]` and `10 -> [u]`/`[v]`), every open code `·`, and every unread span `[...]` counts as one hole. For the remaining 44 records without sentence-level readings, no word count is given, for three reasons:

1. No reading divides those 44 decodes into words. The spaces of the page do not mark every word: many groups run several words together.
2. The decode also breaks at the notes of the transcription. So one word can stand in two or three groups.
3. A fully decoded group is only the output of the key. No reading checks it as a word.

So those 44 record pages count code tokens, open codes and items that are not codes, under those names. The floor for texts of under 40 words is not used.

## Earlier readers

- **The clerk of the time:** 29 letters with dots carry a decipherment above the cipher rows, and R8618 carries a few words of the clerk's hand. DECODE marks inline plaintext on these 30 records. None of the seven letters with readings in `readings/` carries any clerk decipherment (`plaintext.location = ["none"]`). This folder does not copy any clerk text. 14 code values come from it (kept hidden on all dotted pages), and `check.md` grades the blind decode against it.
- **The Gualterio cipher tables** at the British Library (Add MS 20244): this ledger's catalogue names them for entry 295. They are not on DECODE, and they are not online by this ledger's note. I did not open them.
- **DECODE:** all 51 records give status "N/A" and cipher type "Unknown" (checked 16 November 2026).
- **This ledger:** entry 295 stands in the list of letters readable with keys in hand. No target folder and no reading names Add MS 20443 (checked 16 November 2026). Two key files of `targets/bay1706` (`keys/DOC_R588_D2150_2150.txt` and `keys/DOC_R556_D2828_2828.txt`) hold the name "Bottigor" or "Bottiger", not "Botti". They are not about these letters (read on 19 November 2026).
- **Print:** web search on 23 November 2026 for `"Carlo Camillo Botti"`, `"Lazaro Botti"`, `"Gualterio"`, and `"Add MS 20443"` returned only the British Library catalogue entry and DECODE records; no printed edition or modern decipherment found.

## Transcription doubts

The 191 digit files in `transcription/` are reconciled two-pass AI transcriptions of the DECODE images; no person has checked them against the scans. Every doubtful sign (`?`) and every polyphonic or open code stays open and is counted as a hole in `scripts/verify_readings.py`.

- Code `17` (`r`/`q`) and code `10` (`a`/`u`/`v`) across the 1710-1713 letters (e.g. `R8718 T004 C08 ruesta`, `R8661 T001 C05 raaenna`, `R8660 T005 C08 raesto`, `R8668 T005 C04 ruali`) - read: kept literal `r`/`a` in the unedited mechanical decodes, marked `[q]`/`[u]` in `readings/`; checked: decode (not checked by a human against scans); open between `r`/`q` and `a`/`u` without BL Add MS 20244, every instance counted as a hole.
- Doubtful digit marks `?` and unread notes in the 7 letters with readings (`R8718` 14 items, `R8673` 11, `R8661` 21, `R8668` 47, `R8660` 58, `R8664` 31, `R8665` 25) - read: `[...]` or bracketed `[x]` in `readings/`; checked: decode (not checked by a human against scans); two-pass AI reconciliation left these signs doubtful, and every affected word counts as a hole.
- Clipped right margin on `R8662 T003` and clipped fragment `R8468 T003` - read: withheld / open; checked: decode; physical margin clipping prevents reliable decoding.

## Remaining gaps

- Code 17 (255 tokens): r or q - blocker: open-codes; the clerk writes r 66 times and q 39 times at its places.
- Code 17 before code 10 (`17.10.`): 74 places in the rows of the letters with dots where both signs are sure, 26 more where a sign is doubtful, and 1 (`R8695 T003 C13`) with a sign marked `[?]` after 10 (101 in all) - blocker: open-codes; at the 72 sure places on pages decoded here, the decode gives `raesto` (8), `raale` (5), `raesta` (4) and `rael` (3), which read *questo*, *quale*, *questa* and *quel* with 17 = q and 10 = u; some groups read with r (*fratello*, *tragedia*, *ringrazio*); the key keeps 17 as r and 10 as a, and every `[q]`/`[u]` restoration in `readings/` is counted as a hole.
- 90 rare codes with no value (191 tokens in the letters with dots) - blocker: no-key-material; the Gualterio cipher tables (BL Add MS 20244) are offline and not opened.
- One page not shown (`R8662 T003`, right margin clipped) and `R8468 T003`/`T007` - blocker: illegible; clipped margins and five unsure sign labels on T007.
- `R8618 T002` (one code between spaces, unknown word breaks) - blocker: unknown; several tries on 16 to 18 November did not settle its key.
- 45 pages under 100 digits or with no cipher digit - blocker: too-short.
- 44 remaining records (29 carrying contemporary clerk decipherments, 5 undotted letters, and 10 sparser blind letters) have no sentence-level reading yet - blocker: not-attempted; working readings have so far been prepared only for the 7 pure-blind dotted letters in `readings/`.

## Escalation

- [x] siblings: one key for all 51 records (the letters without dots read with the key of the letters with dots; `check.md`)
- [x] clear-pages: the clerk's decipherments on 29 letters used as a grade and for 14 code values (`check.md`), kept hidden on all dotted decodes and absent from all 7 blind letters with readings
- [ ] known-keys: checked `targets/bay1706` (unrelated "Bottigor"/"Bottiger"); the Gualterio cipher tables (BL Add MS 20244) are offline and were not opened
- [x] print: web search (23 Nov 2026) for Carlo Camillo Botti, Lazaro Botti, Gualterio, and BL Add MS 20443 found only the BL catalogue and DECODE entries, no published edition or decipherment
- [x] key-rebuild: 21-letter key recovered from ciphertext alone (`key-and-read/`)
- [x] retry: added strictly aligned working Italian readings and English translations for 7 pure-blind letters (`readings/`, verified by `scripts/verify_readings.py`: 524/804 sure cipher words = 0.652)

## Files

| File | What it holds |
| --- | --- |
| `NOTES.md` | these notes |
| `profile.json` | the profile |
| `README.md` | the summary, the numbers and the table of records |
| `check.md` | what was checked against what |
| `r8468.md` to `r8718.md` | one page for each of the 51 records (unedited mechanical decodes) |
| `readings/` | strictly aligned Italian readings and English translations for 7 pure-blind letters (`r8660`, `r8661`, `r8664`, `r8665`, `r8668`, `r8673`, `r8718`) |
| `key-and-read/` | `key.tsv`, `key-page-signs.tsv` and the order of events of the frozen read |
| `TRANSCRIPTION.md` | the transcription: what it is, its marks and its counts |
| `transcription/` | the cipher rows: one file for each page with cipher digits |
| `scripts/decode_four_pages.py` | reproducible unedited mechanical decode of R8666 T003, R8674 T001, R8677 T001, and R8710 T004 from `key-and-read/key.tsv` |
| `scripts/verify_readings.py` | verifies zero unmarked departures from the unedited decodes and prints exact sure cipher-word and hole counts |

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
