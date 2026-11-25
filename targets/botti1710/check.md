# Checks of the decode

Credit:

- DECODE, the database of historical ciphers of the DECRYPT project: records R8468 to R8470, R8617, R8618 and R8659 to R8718.
- DECODE's record pages: https://de-crypt.org/decrypt-web/RecordsView/ followed by the record number, for example https://de-crypt.org/decrypt-web/RecordsView/8659.
- The archive: British Library, Add MS 20443 (papers of Cardinal F. A. Gualterio).
- The database: Héder, M. and Megyesi, B. (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- No DECODE image is published.

## 1. The blind decode against the clerk (letters with dots)

- **What against what:** the decode of the key from the ciphertext, against the clerk's decipherment above the cipher rows.
- **Where:** the 29 letters with dots that carry it: R8669, and R8676 to R8717 among the letters with dots.
- **The rule,** written before any clear row was opened: each cipher row is paired with the clear row directly above it. Both texts are folded to 21 letters (j to i, k to c, v and w to u, y to i). The measure is the share of the decode's shown letters that fall in matching blocks of the two texts.
- **The chance floor:** each decode row against the clear row of another place, 50 rows later.
- **The true name of the measure:** a letter-match share. It is no read share by this ledger's rule, and it counts no words.

| Measure | Blind decode (fixed 16 Nov, 11:27 UTC−5) | The decode here (fixed 16 Nov, 12:13 UTC−5) |
| --- | ---: | ---: |
| Shown letters that match the clerk's row above | 75.3% of 14,279 | 75.0% of 15,460 |
| The same against a wrong row | 29.6% | 29.0% |
| The clerk's row below instead (a control) | 35.0% | 34.4% |
| Rows surely paired with their clerk's row | 81.5% (344 rows) | 82.0% (379 rows) |

- A row is "surely paired" when three tests pass. The rows above and below are clear rows. The cipher row has 8 or more codes. The clear row has 0.7 to 1.4 letters for each code.
- The decode here differs from the blind decode in one point: two letter-like signs (`a`, `u`) are codes, not masks. It came after the grade, so it is not blind on the 29 letters.
- By letter, the match runs from 48% (R8669, 48 letters) to 88% (R8692).
- Each code's agreement with the clerk at its places is in `key-and-read/key.tsv`. 16 of 21 codes agree at 92% or more. Code 17 agrees at 55%.
- Limits: the clerk abbreviates, and some clear rows may not belong to the cipher row below them. These limits can move the figure either way.
- This folder does not copy the clerk's text. So the figure cannot be computed again from this folder alone.

## 2. A control with a planted key

- Two texts of period Italian, each in a key that I planted.
- Each text has the exact layout and the doubt marks of the 46 letters with dots. About 12% of the code tokens were changed.
- On the held-out text, the same method read 99.2% of the clean letter tokens right, with no wrong letter shown. It gave no word code.

## 3. The language checks (letters with dots)

| Fit of the decode here | Score per code token (nats) |
| --- | ---: |
| Italian | −2.708 |
| The next distinct key | −3.240 |
| The same tokens in a shuffled order | −4.672 |
| A Spanish letter model | −4.143 |
| A Latin letter model | −3.514 |

- The two halves of the letters (1710; 1711 to 1713) give the same letter for 19 of their 20 frequent codes. Code 17 differs.

## 4. The letters without dots

- **The key test:** a page passes when the key scores above three kinds of control:
  - 20 wrong keys: the same codes, with the letter values permuted;
  - 3 copies with the page's digits shuffled;
  - the same procedure with a Latin and with a Spanish letter model.
- 19 of 22 tested pages pass. 6 pages are under 100 digits.
- The same test on the letters with dots, with their dots taken out: 122 of 127 pages pass. There the cut falls at the dots in 81% of words.
- Decoded words in an Italian word list: 53.5% of 1,578 (shuffled copies: 16.6%).
- **R8618:** page T003 has 31 words of the clerk's hand with 5 or more letters. 7 of them have a near match in the decode. Other pages of the same length give 2 to 5. This check is weak. It is no grade.
- **R8468 T007** passes the key test with the five sign values: −2.845 a letter; best wrong key −3.321; Latin −3.065. **R8468 T003** passes: −3.523; best of 220 wrong keys −3.641; Latin −4.277. Six routes were tried on T003, so a chance pass against the wrong keys is not ruled out (bound about .03).

## 5. The checks of this folder (19 November 2026)

- **The decode is the frozen read.** My repository shows 1,738 decoded rows of the letters with dots. Each equals its row in the frozen decode of 16 November.
- **The row labels.** In the letters with dots, each decode line was matched to its cipher row by its letters. 12 lines show too few letters to match. Their labels carry `≈` and rest on the order of the page.
- In the letters without dots, a line's label is its place in the decode of the page. On R8468 T007 the decode keeps no row breaks.
- 5 rows with cipher digits have no decode line. Their record pages name them.
- The runs behind sections 2 to 4 are not in this folder. Their numbers come from my own record.
- **The counts** in `README.md`, the record pages and `profile.json` come from the decode lines of the record pages.
- **Working readings (7 pure-blind dotted letters):** `scripts/verify_readings.py` checks `readings/rXXXX_reading.md` (`R8660`, `R8661`, `R8664`, `R8665`, `R8668`, `R8673`, `R8718`) mechanically against the unedited decodes in `rXXXX.md`: 524 of 804 cipher words sure (0.652), 280 holes, zero unmarked departures. All 51 documents remain filed as `"decoded, not read"` in `profile.json`; independent reading review and `docs/_check_reading.py` remain for the maintainer.
