# Francia 32: Filippo Sega, nuncio in Paris, to Rome, 1590 to 1591 (DECODE R5612 to R5618, R5620, R5621)

Archivio Apostolico Vaticano, Segreteria di Stato, Francia 32. DECODE records R5612 to R5618, R5620 and R5621: 9 records, 30 cipher pages. R5619 has no images on DECODE.

Status: decoded, not read. This folder is a contribution from outside (prabal-rje), sent as a pull request. The maintainer sets the status, the class and the place of each record.

Credit:

- DECODE, the database of historical ciphers of the DECRYPT project. Record pages: [R5612](https://de-crypt.org/decrypt-web/RecordsView/5612), [R5613](https://de-crypt.org/decrypt-web/RecordsView/5613), [R5614](https://de-crypt.org/decrypt-web/RecordsView/5614), [R5615](https://de-crypt.org/decrypt-web/RecordsView/5615), [R5616](https://de-crypt.org/decrypt-web/RecordsView/5616), [R5617](https://de-crypt.org/decrypt-web/RecordsView/5617), [R5618](https://de-crypt.org/decrypt-web/RecordsView/5618), [R5620](https://de-crypt.org/decrypt-web/RecordsView/5620), [R5621](https://de-crypt.org/decrypt-web/RecordsView/5621).
- Héder and Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- No DECODE image is published.

## What the documents are

- Letters of Filippo Sega, bishop of Piacenza and nuncio in Paris, to Rome, from November 1590 to July 1591.
- Most of these letters are mostly in clear, with cipher passages and short groups. The duplicate R5615 is almost all in cipher.
- They belong with `targets/sega1590` and `targets/sega1591b`, as the maintainer asked. `README.md`, "Where this folder goes", maps each record.

## The system

Meister's key no. 65, as `targets/sega1590` describes it:

- letters as digit pairs;
- vowels as signs on a single digit;
- nulls 7, 8, 9 and 0;
- code letters and symbols for common words;
- three-digit codes for names, with a dot on the last digit.

Key no. 65 gives .58 and .60 units with a value on R5618 and R5620. I make no claim about their system beyond that.

## The key

| Source | What it gives |
| --- | --- |
| A. Meister (1906), key no. 65, pp. 435-436 | every value of the key |
| George Lasry (`targets/sega1591`) | the tie of key no. 65 to Sega's letters |
| This ledger, `targets/sega1590/key.tsv` (Brice Dudout) | the file that my decode used |
| This ledger, the notes of `targets/sega1590/transcription.txt` | the shape of the symbol in (ω), and the shape of con (two verticals on a base line) |
| My decode | three sign forms read as the key's vowel signs; a lone 1 as a null; con for the sign ∞, with a doubt |

`key/key.tsv` gives each value, its kind and its source. `key/README.md` gives the rules by which the decode reads a row.

## The transcription

- My own transcription of the DECODE images, finished on 13 November 2026.
- 30 cipher pages, 383 rows, 16,230 digit signs, of which 492 doubtful.
- The rows hold the cipher runs of 10 or more digit signs. Shorter groups are not in them.
- `TRANSCRIPTION.md` gives the marks and the counts. The rows are in `transcription/`.

## The decode

- The decode of 28 pages with key no. 65, made on 17 November 2026. `scripts/decode.py` makes it again from the rows.
- On the 24 pages of the main group, .80 to .99 of the units of each page have a value in the key (`check.md`, section 2, with the faults of that count).
- The folder holds no reading in sentences. So every decoded document is "decoded, not read".
- Each record page gives a summary in English, its source, and one concrete doubt.

## The checks

`check.md` gives them in full.

- **R5621:** of the 250 letters of the decode, 212 match the decipherment of the time on f. 230r, in order (.848). With the pair values shuffled: .172.
- **R5613:** of the 144 letters of the decode, 123 match the decipherment of the time on f. 46r, in order (.854). With the pair values shuffled: .138.
- For R5621, Brice Dudout's held-out test came before mine. The share .848 is a second measure of that letter, with no held-out protocol of its own.

## Earlier readers

- **Brice Dudout** (`targets/sega1590`, `targets/sega1591b`, 29 October 2026): f. 17 (R5612), f. 71 (R5616), R5615 in part, and the held-out test on R5621.
- **George Lasry** (`targets/sega1591`): the Paris copy of the letter of 9 January 1591, which R5613 also holds.
- **The clerks of 1591:** the decipherments on f. 46r (R5613) and f. 230r (R5621).

## Remaining gaps

- No reading in sentences for any document - blocker: not-attempted; the decode is not divided into words in this folder.
- R5618 and R5620: no key - blocker: no-key-material; key no. 65 gives .58 and .60 units with a value, and no other key is known.
- Signs that key no. 65 does not hold, shown as `<...>` in the decode - blocker: open-codes.
- Faults of the decode: row labels read as code letters on ff. 62v and 71v, and signs that leave no mark (`README.md`, "How to read the decode") - blocker: not-attempted.
- Short cipher groups under 10 digit signs are not in the rows - blocker: not-attempted.
- R5616 f. 71v does not read (.67 units with a value) - blocker: not-attempted; no second transcription of this page was made.

## Escalation

- [x] siblings: the records R5612 to R5621 on DECODE; the ledger's `sega1590`, `sega1591b` and `sega1591`
- [x] clear-pages: the decipherments of the time on f. 46r and f. 230r, as a check only; no value of the key comes from them
- [x] known-keys: Meister's key no. 65, as this ledger gives it
- [ ] print: not searched for this pull request
- [ ] key-rebuild: not attempted; the key is a printed key
- [ ] retry: no second transcription of any page

## Files

| File | What it holds |
| --- | --- |
| `NOTES.md` | these notes |
| `profile.json` | the profile |
| `README.md` | the summary, the map to `sega1590` and `sega1591b`, the numbers, the counts and the marks of the decode |
| `check.md` | the two measures against the decipherments of the time, the units with a value, and the page groups |
| `r5612.md` to `r5621.md` | one page for each record |
| `key/` | `key.tsv` and its note |
| `scripts/decode.py` | the decoder: rows in, decode lines out |
| `TRANSCRIPTION.md` | what the rows are, their marks and their counts |
| `transcription/` | the rows: one file for each of the 30 cipher pages |

The check script is not in this folder. It needs the clerk's lines, and this folder does not copy them.

## Credits

- **DECODE**, the database of historical ciphers of the DECRYPT project: records R5612 to R5618, R5620 and R5621 (links above).
- Héder and Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- **The archive:** Archivio Apostolico Vaticano, Segreteria di Stato, Francia 32.
- **The key:** A. Meister (1906), key no. 65; tied to Sega by George Lasry; written as `targets/sega1590/key.tsv` by Brice Dudout.
- **The earlier readings:** Brice Dudout and George Lasry.
- **The transcription, the decode and the checks:** prabal-rje (id `prabal` in `contributors.json`).

DECODE's images are for research use only. They may not be redistributed or published without permission from the archive. No DECODE image is published.
