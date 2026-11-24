# The keys and the frozen read

Credit: DECODE, the database of historical ciphers of the DECRYPT project, records R4033 to R4054. Florence, Archivio Niccolini di Camugliano, Fondo antico 214, inserto 1. No DECODE image is published.

| File | What it holds | Source of the values |
| --- | --- | --- |
| `key-main.tsv` | the key of the main system: each code, its value, its count and its doubt | from ciphertext: my own key, found from the cipher text alone |
| `frozen-read.md` | the read of the main system as it stands on my public repository | from ciphertext |
| `key-table-R4033.tsv` | the key of the earlier system: my reading of the archive's key table, sign by sign, in two readings A and B, and one line for code 29 | from key: the archive's key table, DECODE record R4033; code 29 from ciphertext |
| `key-earlier-blind.tsv` | my own key of the earlier system, from ciphertext, made before the table was used | from ciphertext |

## The main key

- One fit found the cut into codes and the key together, from 100 random starts. 85 of the 100 starts reached the best score.
- The key shows 21 codes: 20 letter codes for 18 letters (a and o each have two codes), and code 74 for "che". Code 36 is read as a null and shows no value.
- Every other code stays open: each has fewer than 30 tokens.
- The read was fixed on 16 November 2026 at 16:15 (UTC−5). R4049 stayed out of the fit and was decoded with the same key by 16:35, with no further fit.
- The key went public on 19 November 2026 at 09:05 (UTC−5), with the read. It has not changed since.

## The decode and the frozen read

- The decode on each record page of the main system (R4039, R4041 to R4050, R4052 to R4054) is the key of `key-main.tsv` applied to the codes of the cut.
- The decode on each record page of the earlier system (R4034 to R4038) is the key of `key-table-R4033.tsv` (reading A, and the line for code 29) applied to the codes of the cut. The section below describes it.
- The frozen read hides each code that holds a doubtful digit. The decode shows the key's value for it, in `⟨ ⟩`.
- At 7 places the frozen read differs from its own key. `check.md`, section 4, lists them.

## The key of the earlier system

- The values of the earlier system come from the archive's key table, DECODE record R4033, with one value from ciphertext: code 29 = t.
- I read the table twice (readings A and B). The decode uses reading A, and shows both where they differ.
- `key-table-R4033.tsv` holds 99 lines below its header. 98 lines are the table: 29 letter signs, 68 word signs and 1 other sign. The line for code 29 is not a reading of the table. Its source column says so, and its two "sure" columns hold `-`.
- Some codes of the five letters are not in the key. The record pages show them as `[nn]`.

## Code 29

- Code 29 has 70 tokens in the five letters: 12 in R4035 and 58 in R4037.
- I looked at the table again for 29. The table shows no 29 without a bar. Its only 29 has a bar and is a word sign, "Madon̄a". The table gives t one sign, 79.
- So 29 = t is a value from ciphertext. It is the value of my blind read of the earlier system (`key-earlier-blind.tsv`, code 29, 70 tokens). That read was fixed on 16 November 2026 at 22:09 (UTC−5). It has been public on my repository since 19 November 2026 at 09:05 (UTC−5), in the file `cosimo-1537/key-earlier.tsv`, and it has not changed since.
- `check.md`, section 3, gives the checks of this value.

## The earlier blind key

- `key-earlier-blind.tsv` is my key of the earlier system, found from the cipher text alone, before I used the table. It was fixed on 16 November 2026 at 22:09 (UTC−5).
- On 17 November 2026 at 19:33 (UTC−5) I compared it with the table: 16 of its 17 shown codes agree with the table; the 17th, code 29, is a code that the table does not hold. `check.md`, section 3.
- The decode of the earlier letters takes one value from it: code 29 = t.

The times rest on my own record and on the dates of the public commits. This folder adds no hash table and no other record of provenance.

## Credits

- **DECODE**, the database of historical ciphers of the DECRYPT project: records R4034 to R4039, R4041 to R4050 and R4052 to R4054, and R4033 (the key table). The record pages: https://de-crypt.org/decrypt-web/RecordsView/4033, https://de-crypt.org/decrypt-web/RecordsView/4034, https://de-crypt.org/decrypt-web/RecordsView/4035, https://de-crypt.org/decrypt-web/RecordsView/4036, https://de-crypt.org/decrypt-web/RecordsView/4037, https://de-crypt.org/decrypt-web/RecordsView/4038, https://de-crypt.org/decrypt-web/RecordsView/4039, https://de-crypt.org/decrypt-web/RecordsView/4041, https://de-crypt.org/decrypt-web/RecordsView/4042, https://de-crypt.org/decrypt-web/RecordsView/4043, https://de-crypt.org/decrypt-web/RecordsView/4044, https://de-crypt.org/decrypt-web/RecordsView/4045, https://de-crypt.org/decrypt-web/RecordsView/4046, https://de-crypt.org/decrypt-web/RecordsView/4047, https://de-crypt.org/decrypt-web/RecordsView/4048, https://de-crypt.org/decrypt-web/RecordsView/4049, https://de-crypt.org/decrypt-web/RecordsView/4050, https://de-crypt.org/decrypt-web/RecordsView/4052, https://de-crypt.org/decrypt-web/RecordsView/4053, https://de-crypt.org/decrypt-web/RecordsView/4054.
- **The archive:** Florence, Archivio Niccolini di Camugliano, Fondo antico 214, inserto 1. The archive's key table (DECODE record R4033) gives the values of the earlier system, apart from code 29.
- **The database:** Mihály Héder and Beáta Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- **The transcription, the keys from ciphertext, the decode and the readings:** prabal-rje.

DECODE's images are for research use only. They may not be redistributed or published without permission from the archive. No DECODE image is published. The digit rows in `transcription/` are a transcription of the DECODE images. No DECODE transcription file is in this folder.
