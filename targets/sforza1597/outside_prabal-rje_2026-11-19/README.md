# Sforza chancery letters in cipher, cartella 1597: my decodes

This folder holds my own transcription, key and decode of 10 pages of 9 records of the Sforza chancery letters (Archivio di Stato di Milano, Carteggio Sforzesco, cartella 1597).

**Every document here is decoded, not read.** The decode is the plain output of the key on my rows. It has no word division. No reading in sentences stands yet, and no document counts as read. Where the key sheet gives a word or a name for one sign, the decode shows it in braces.

All pages here are from ciphertext: the key came from the cipher text alone, and no key sheet and no clear text checks it. For R5445 p1, the key table gives the values that my frozen read shows (`check.md`).

## The records

"Agree" is the share of the letters that my frozen read shows where the decode gives the same letter (`check.md`). Signs leave out the signs that my transcription does not read.

| Record and page | Ledger entry | Key | Language | Signs | Agree | Page |
| --- | --- | --- | --- | ---: | ---: | --- |
| R5415 p1 | 2401, C | from ciphertext | Latin | 914 | 95.9% | [r5415](r5415.md) |
| R5416 p1 | 2402, D | from ciphertext | Italian | 759 | 95.5% | [r5416](r5416.md) |
| R5419 p1 | 2402, D | from ciphertext | Italian | 1,031 | 83.5% | [r5419](r5419.md) |
| R5421 p1 | none | from ciphertext | Italian | 1,397 | 86.1% | [r5421](r5421.md) |
| R5432 p1 | none | from ciphertext | Italian | 1,443 | 79.6% | [r5432](r5432.md) |
| R5439 p1 | 2408, J | from ciphertext | Italian | 697 | 95.8% | [r5439](r5439.md) |
| R5445 p1 | 2403, E1 | from ciphertext | Italian | 225 | 100.0% | [r5445](r5445.md) |
| R5453 p1 | 2407, I | from ciphertext | Italian | 526 | 96.2% | [r5453](r5453.md) |
| R5453 p2 | 2407, I | from ciphertext | Italian | 185 | 94.4% | [r5453](r5453.md) |
| R5456 p1 | 2402, D | from ciphertext | Italian | 628 | 94.2% | [r5456](r5456.md) |

## Pages that this folder does not hold

- **The nine records R5425 to R5430 and R5463 to R5465:** my reads of these records are on my public repository (`sforza-1597/`). Their key uses labels joined across the pages, and this folder does not yet hold rows in those labels.

## How to read the files

- **Rows** (`transcription/<record>_p<page>_signs.txt`): one line for each cipher row (`C01` is row 1). A label names one sign shape of that page only. `?` is a sign that my transcription does not read.
- **Key** (`key/<record>_p<page>_key.tsv`): each label, its count, its value, the source of the value, and the letters that my frozen read shows for it. `·` is a null; `?` is a label with no value.
- **Decode** (`key/<record>_p<page>_decode.txt`): the key applied to the rows, sign by sign, with nothing edited. `[?]` is a sign that my transcription does not read.
- **Frozen read** (`key/<record>_p<page>_frozen-read.txt`): my read as it stands in my public repository, kept apart from the decode. Its marks are in its header. This folder adds no hash table and no other record of provenance.

## Counts by the word rule

The decodes have no word division, so I do not count cipher words, sure words or holes. Each page gives its signs instead. No document reaches the read bar, and the floor for short texts is not used.

## Credits

- **DECODE**, the database of historical ciphers of the DECRYPT project: the records named in this folder. Each record page links its DECODE record: https://de-crypt.org/decrypt-web/RecordsView/ followed by the record number, for example https://de-crypt.org/decrypt-web/RecordsView/5415.
- **The archive:** Archivio di Stato di Milano, Carteggio Sforzesco, cartella 1597. Each record page gives its cartella and number.
- M. Héder and B. Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- No DECODE image is published. DECODE's images are for research use only.

## Files

- `README.md`, `NOTES.md`, `TRANSCRIPTION.md`, `check.md`, `profile.json`.
- One page for each record: `r<number>.md`.
- `transcription/`: my rows.
- `key/`: the key table, the decode and the frozen read of each page.
