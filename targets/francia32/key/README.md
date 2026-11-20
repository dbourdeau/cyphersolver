# Francia 32: the key of the decode

Credit:

- DECODE, the database of historical ciphers of the DECRYPT project. Record pages: [R5612](https://de-crypt.org/decrypt-web/RecordsView/5612), [R5613](https://de-crypt.org/decrypt-web/RecordsView/5613), [R5614](https://de-crypt.org/decrypt-web/RecordsView/5614), [R5615](https://de-crypt.org/decrypt-web/RecordsView/5615), [R5616](https://de-crypt.org/decrypt-web/RecordsView/5616), [R5617](https://de-crypt.org/decrypt-web/RecordsView/5617), [R5618](https://de-crypt.org/decrypt-web/RecordsView/5618), [R5620](https://de-crypt.org/decrypt-web/RecordsView/5620), [R5621](https://de-crypt.org/decrypt-web/RecordsView/5621).
- Héder and Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- Archivio Apostolico Vaticano, Segreteria di Stato, Francia 32.
- No DECODE image is published.

## The key

- **The key:** A. Meister (1906), key no. 65, "cifra servita in legatione sub Sisto V", pp. 435-436.
- **Who tied it to Sega:** George Lasry (`targets/sega1591`).
- **The file that my decode used:** this ledger's `targets/sega1590/key.tsv`, written by Brice Dudout. My decode took its values from that file on 17 November 2026.
- **`key.tsv`** gives each value of the decode, its kind and its source. It also lists the symbols of the key that my decode does not apply.
- **`../scripts/decode.py`** holds these values and makes the decode from the rows.

## Values that come from my decode, not from the key

`key.tsv` marks each of them with the source "my decode".

- Three sign forms of my transcription are read as vowel signs of the key: 4 with an overline (i), a digit with a stroke through it (o), and a digit with a raised s or 2 (u).
- A lone 1 that opens no pair is a null. No pair of the key begins with 1.
- The sign ∞ gets the value con, with a doubt. This identification is mine. The ledger's notes give con as two verticals on a base line, and my decode does not apply that shape.

## How the decode reads a row

1. Clear words in a row are skipped.
2. An unsigned digit 2, 3, 4, 5 or 6 opens a pair. The next digit closes it.
3. A digit with a vowel sign stands alone. On 2 to 6 it gives the vowel of its sign. On 7, 8, 9 or 0 it is a null.
4. A lone unsigned 7, 8, 9, 0 or 1 is a null.
5. A dot on a digit closes a three-digit code.
6. A lone lower-case letter is a code letter. The signs ω and ∞ are symbols.
7. Where a sign has two readings, the decode takes the left one if it is a digit.

## No frozen read

Every decoded page here is "from key". This folder claims no read from the ciphertext alone, so it holds no frozen read. This folder adds no hash table and no other record of provenance.

## Limits

- The decode reads the rows exactly as my transcription gives them. A misread digit gives a wrong letter or a broken pair.
- The ledger's key note also allows a vowel sign on a pair. My decode does not apply that: a marked digit after an open pair gives `?`, then its own vowel.
- On some pages my transcription writes a vowel sign as a raised mark. The decode shows `?` there.
- Signs given in brackets, symbols other than ω, ∞ and #, and a bare ω leave no mark in the decode.
- Row labels inside a row (`{C01:` on f. 62v; `a:` and `b:` on f. 71v) are read as code letters.
- An unresolved span between complete units leaves no mark.
