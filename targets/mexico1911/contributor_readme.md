# Mexico City, 19 May 1911: a warning about General Huerta

A coded telegram to the Maderista agent Federico González Garza at El Paso, signed by Fausto E. Miranda and S. Herrera Moreno. It passes on a warning from General Huerta: a military mutiny against the addressee is feared in the capital.

- **Where:** CEHM-Carso, Mexico City, Fondo CMXV (Archivo Federico González Garza), CMXV.18.1770.2-4. A Western Union form, addressed to the alias "W. Olliphant".
- **Scans:** the CEHM online catalogue, https://www.cehm.org.mx/ , record CMXV.18.1770.2-4.
- **Ledger:** catalogue 1462 at https://github.com/dbourdeau/cyphersolver lists this telegram as "partly read", from the archive's catalogue record.

## What it says

- Go to Julio Peña for the translation.
- Last night three agents [of Pineda?] left for the north.
- General Huerta told the writer that a military mutiny against the addressee is feared in the capital, because of Díaz's resignation.
- The writers advise precautions, "or do not come".

Read it: [Spanish](reading.md), [English](translation.md).

**Context.** Díaz resigned on 25 May 1911, six days later. Huerta led the coup against Madero in February 1913. The "usted" may mean González Garza, or Madero, for whom González Garza acted. The telegram does not say which.

## The key

This telegram was read with the archive's own key card, not from the ciphertext alone. The card is headed "Herrera. Moreno." (CMXV.16.1557.1, scan 7), and one signer of the telegram is S. Herrera Moreno.

It is a shifted alphabet that counts ch, ll and ñ as letters. `key.tsv` gives it.

## Checks

- **The key is right.** The same card reads a telegram of the next day by the same signers (CMXV.18.1777.5-6). A hand of the time glossed that telegram in pencil. All ten coded words agree with the card, and one of them has one wrong letter.
- **Three words keep a doubt.** "KINEDA" may be a name, and "Pineda" is a guess that needs one wrong letter. "VENFA" is read as "venga", with one wrong letter. "ono" is read as clear "o no".

## Earlier work

As far as I checked, nobody has published this reading. That is not proof that nobody has.

- **The archive's record** says "Texto en clave y palabras descifradas", with the subject "Armisticio fue firmado". But no decipherment stands on the sheet, and its pencil notes do not touch the coded words. The record does not mention Huerta.
- **The period decipherments.** The same fonds holds a typed list of period decipherments, January to May 1911 (CMXV.18.1795.1). Its dated run goes from 16 May to 20 May, with no entry for 19 May.

**Checked:**

- the four records of the file;
- all 45 images of the typed list, partly by OCR;
- CEHM catalogue searches by the signers' names.

**Not checked:**

- the recipients' papers, such as Madero's;
- González Garza's own printed work;
- Narváez's 2019 book on Mexican cryptography;
- Mexican state archives with no online images.

So this telegram may already be in print. Someone with these books should check them.

## Status

A short text, read in full with the period key. Three words keep a doubt. The reading is with the cipher ledger as issue #330: https://github.com/dbourdeau/cyphersolver/issues/330.

## Files

- `reading.md`: the telegram in Spanish, with the coded words in capitals
- `translation.md`: the telegram in English
- `transcription.txt`: the telegram as typed
- `decryption.txt`: each coded word with its letter-for-letter reading
- `key.tsv`: the key card's alphabet

© 2026 Prabal Gupta. First published here, 7 November 2026. Released under CC BY 4.0: reuse it, and credit me.
