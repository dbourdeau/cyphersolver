# The Botti letters: the key and the frozen read

This folder holds the key of the decode, with the source of each value, and the order of events of the frozen read.

Credit:

- DECODE, the database of historical ciphers of the DECRYPT project: records R8468 to R8470, R8617, R8618 and R8659 to R8718.
- DECODE's record pages: https://de-crypt.org/decrypt-web/RecordsView/ followed by the record number, for example https://de-crypt.org/decrypt-web/RecordsView/8659.
- The archive: British Library, Add MS 20443 (papers of Cardinal F. A. Gualterio).
- The database: Héder, M. and Megyesi, B. (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- No DECODE image is published.

## The files

| File | What it holds |
| --- | --- |
| `key.tsv` | each code: its value, the source of the value, its count in the letters with dots, the clerk's agreement at its places, and its doubt |
| `key-page-signs.tsv` | the value of a sign label on one page of the letters without dots |
| `r8468-t007-signs.tsv` | the five sign labels of R8468 page T007, read as digit forms; not sure |

`key.tsv` and `key-page-signs.tsv` are the files of my repository, https://github.com/prabal-rje/branicki-1757/tree/main/botti-1710, with one credit line added to `key.tsv`. `r8468-t007-signs.tsv` lists the values that the record page of R8468 states.

## The sources in `key.tsv`

- `from ciphertext`: my own key, from the cipher text alone (21 codes).
- `the clerk's decipherment on the page (the value only)`: 14 values, read off the clerk's text. They are not from my key.
- Code 17: decoded r; the source column gives the clerk's letters at its places.
- `open`: 90 codes with no value.
- `key-page-signs.tsv`: values from the ciphertext of that page, with the key of the codes fixed.

## Which values each decode uses

- **The letters with dots:** only the values `from ciphertext`. The 14 values from the clerk show as `·`.
- **The letters without dots:** the values from the ciphertext, the 14 values from the clerk, and the sign values of `key-page-signs.tsv`.
- **R8468 T007** also uses five label values that are not sure: `r8468-t007-signs.tsv`.

## The order of events

All times are UTC−5. They rest on my own record.

1. **16 November 2026, 11:27:** the blind decode of the 46 letters with dots was fixed. Its key came from the cipher text alone.
2. **16 November, 11:39 to 11:41:** the rule of the grade was written; then the one grade against the clerk's rows (`../check.md`, section 1).
3. **16 November, 12:13:** the decode here was fixed: the same method, with two letter-like signs as codes. It is not blind on the 29 graded letters.
4. **16 November, 12:16:** the 14 values from the clerk's text.
5. **17 November, evening:** the five letters without dots, with the same key.
6. **18 November, evening:** R8468 pages T003 and T007.
7. **19 November, 09:05 and 09:11:** the read was published in my repository. The frozen read of this folder is that state.

This folder adds no hash table and no other record of provenance.
