# Francia 32: the checks

Credit:

- DECODE, the database of historical ciphers of the DECRYPT project: records [R5612](https://de-crypt.org/decrypt-web/RecordsView/5612), [R5613](https://de-crypt.org/decrypt-web/RecordsView/5613), [R5614](https://de-crypt.org/decrypt-web/RecordsView/5614), [R5615](https://de-crypt.org/decrypt-web/RecordsView/5615), [R5616](https://de-crypt.org/decrypt-web/RecordsView/5616), [R5617](https://de-crypt.org/decrypt-web/RecordsView/5617), [R5618](https://de-crypt.org/decrypt-web/RecordsView/5618), [R5620](https://de-crypt.org/decrypt-web/RecordsView/5620), [R5621](https://de-crypt.org/decrypt-web/RecordsView/5621).
- Héder and Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- Archivio Apostolico Vaticano, Segreteria di Stato, Francia 32.
- No DECODE image is published.

## 1. The key against the decipherments of the time

Two letters carry a decipherment of the time in the same record. My transcription covers those leaves too. This folder does not copy them, so these two measures cannot be re-run from this folder alone.

| Record | Cipher pages | Decipherment of the time | Letters of the decode | Letters of the decipherment | Matched letters of the decode | Share | With the pair values shuffled |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| R5613 | f. 45v | f. 46r | 144 | 509 | 123 | .854 | .138 (of 159 letters) |
| R5621 | ff. 229v, 231r, 231v | f. 230r, dated 26 March 1591 | 250 | 645 | 212 | .848 | .172 (of 274 letters) |

### What the share counts

- **The letters of the decode:** the decode of the cipher rows with key no. 65. Code letters, symbols, three-digit codes, signs not in the key, `?` and clear words are removed. Only rows with 10 or more digit signs count.
- **The letters of the decipherment:** my transcription of the clerk's lines. For a sign with two readings, the left one counts.
  - f. 230r: lines L29 to L42 of my transcription, the clerk's text.
  - f. 46r: every line after the heading "Decifrato". These lines also hold the words of the archive's stamp.
- **On both sides:** accents are dropped; u and v count as one letter, and so do i and j; a doubled letter counts once.
- **The share:** the matching blocks of the two letter strings, in order, found by Python's `difflib.SequenceMatcher` (no junk rule). Their total length is divided by the letters of the decode.
- **The control:** the 22 pair values of the key shuffled once, with a fixed seed (3). Everything else is the same. The shuffled decode has its own number of letters, and its share divides by that number.

### What the share does not show

- **It is a second measure on R5621.** Brice Dudout's held-out test of this letter came before mine (`targets/sega1590`: 268 of 287 characters, 56 of 65 words). My measure uses other units. This folder documents no held-out protocol of its own.
- **It counts letters, not words.** A letter matches when it falls in a matching block. The share does not test whether the decode makes sense.
- **It does not use the whole decipherment.** The clerk's text is longer than the decode, because it also covers clear words of the letter. The share divides by the letters of the decode.
- **The stamp on f. 46r.** Matching blocks can change when letters are added. I ran the R5613 check once more on lines L20 to L30 only, without the stamp: 478 letters of the decipherment, 123 of 144 decode letters matched, .854 again.
- **Re-run.** I ran the check script again on 19 November 2026, with this ledger's `targets/sega1590/key.tsv`. It gave the same four numbers. The numbers rest on that run; the script and the clerk's lines are not in this folder.

## 2. Which pages share the key

- Before the decode, my digit-pair counts grouped the pages, with no key. The output of these counts is not in this folder.
- One group holds 24 pages (the main group). R5618 and R5620 fall apart from it.
- Four pages hold fewer than 70 pairs. The counts cannot place them: ff. 17v, 71v, 106v and 231v.

### Units with a value in the key

The shares below were counted on 17 November 2026 by the decoder, on the rows before the clear text was cut.

- **A unit** is a pair, a lone vowel sign, a code letter, a symbol or a three-digit code that the decode makes. Nulls are not units.
- **With a value:** a pair or a sign that the key holds, a code letter, the symbols ω, ∞ and #, and a three-digit code.
- **With none:** a pair that the key does not hold, a sign that the decode cannot place, and a digit that opens a pair but is not followed by a plain digit.

The rule has faults, which this folder states and does not correct:

- the symbols ∞ (con, doubtful) and # (no value) count as units with a value;
- the code {449}, which has no value, counts as a unit with a value;
- on f. 62v, the row labels `{C01:}` to `{C08:}` give 8 code letters `[per]` that count as units with a value; on f. 71v the span labels `a:` and `b:` give 2 more;
- a `?` at the end of a row does not count;
- signs that the decode drops do not count: signs given in brackets (for example `[two uprights on a baseline]`), symbols other than ω, ∞ and # (for example △), and a bare ω outside angle brackets;
- on f. 231r the old rows held two backticks, which the count read as a break: it gives 15 units with none; the rows of this folder give 14.

Three of these faults put 32 units among those with a value: 20 for ∞, 1 for #, 1 for {449} and 10 for the labels. The dropped signs were not counted. I did not count the shares again with the faults removed.

| Record | Page | Group | Digit signs (this folder) | Units with a value | Units with none | Share |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| R5612 | f. 17r | main group | 532 | 293 | 9 | .97 |
| R5612 | f. 17v | under 70 pairs | 41 | 19 | 2 | .90 |
| R5613 | f. 45v | main group | 324 | 149 | 21 | .88 |
| R5614 | f. 47r | main group | 391 | 183 | 28 | .87 |
| R5614 | f. 48r | main group | 303 | 161 | 2 | .99 |
| R5615 | f. 49v | main group | 251 | 113 | 28 | .80 |
| R5615 | f. 50r | main group | 740 | 368 | 35 | .91 |
| R5615 | f. 50v | main group | 736 | 362 | 18 | .95 |
| R5615 | f. 51r | main group | 395 | 193 | 22 | .90 |
| R5615 | f. 51v | main group | 1,184 | 610 | 26 | .96 |
| R5615 | f. 52r | main group | 945 | 405 | 92 | .81 |
| R5615 | f. 52v | main group | 712 | 356 | 53 | .87 |
| R5615 | f. 53r | main group | 1,311 | 622 | 68 | .90 |
| R5615 | f. 53v | main group | 779 | 396 | 25 | .94 |
| R5615 | f. 54r | main group | 676 | 350 | 15 | .96 |
| R5615 | f. 54v | main group | 822 | 418 | 37 | .92 |
| R5616 | f. 61v | main group | 409 | 199 | 39 | .84 |
| R5616 | f. 62r | main group | 437 | 209 | 23 | .90 |
| R5616 | f. 62v | main group | 204 | 102 | 18 | .85 |
| R5616 | f. 63r | main group | 722 | 332 | 77 | .81 |
| R5616 | f. 63v | main group | 936 | 435 | 68 | .86 |
| R5616 | f. 71r | main group | 167 | 86 | 2 | .98 |
| R5616 | f. 71v | under 70 pairs | 90 | 30 | 15 | .67 |
| R5617 | f. 106v | under 70 pairs | 23 | 10 | 1 | .91 |
| R5617 | f. 107r | main group | 298 | 135 | 14 | .91 |
| R5618 | f. 184v | another cipher? | 143 | 32 | 23 | .58 |
| R5620 | f. 190r | another cipher? | 2,101 | 531 | 347 | .60 |
| R5621 | f. 229v | main group | 328 | 159 | 16 | .91 |
| R5621 | f. 231r | main group | 195 | 89 | 15 | .86 |
| R5621 | f. 231v | under 70 pairs | 35 | 15 | 4 | .79 |

- Key no. 65 gives .58 and .60 on R5618 and R5620. I make no claim about their system beyond that. Brice Dudout's notes reject key no. 65 for R5618 too.
- F. 71v gives .67. It is decoded, but it does not read.

## 3. Limits

- **The rows are my own transcription of the DECODE images.** A misread digit gives a wrong letter or a broken pair. The vowel signs above the digits are the weakest part.
- **Sign forms.** On some pages my transcription writes a vowel sign in another form. `key/key.tsv` lists the forms that the decode reads as the key's signs. A raised mark gives `?`.
- **The decode** keeps the faults listed in section 2: row labels read as code letters, dropped signs, and no mark where an unresolved span stands between complete units.
- **No reading.** The decode is not divided into words, and this folder gives no reading in sentences. So it gives no read share by the rule of 19 November 2026.
- **The ledger's checker** (`docs/_check_reading.py`) did not run on this folder.
