# Notes: thirty Sessa cipher records decoded with the ledger's key

Status: decoded, not read (all 30 records).

## The documents

- The Duke of Sessa to Charles V, Rome, April 1524 to June 1525.
- DECODE records R9873 to R9881, R9883 to R9887, R9889 to R9901 and R9903 to R9905.
- Real Academia de la Historia, Madrid, Colección Salazar y Castro A-31 (9/31) and A-34 (9/34).
- Some records are copies of one dispatch: R9874 is the last leaf of R9873; R9875 is probably its duplicate; R9876 copies part of it; R9878 is the duplicate of R9877; R9879 and R9880 copy the cipher of R9881; R9892 copies R9893 (`check.md`, section 7).

## The system and the key

- The cipher of this target: a mixed nomenclator with three-letter code groups, single signs for letters, the switch `f~` and the opener `v db` (`key_working.md`).
- The key of the decode is KS4 (Brice Dudout), with two departures (`qes` = es from `key_working.md` pass 3; the value before the slash for `njn`), 63 values that I added (62 from clear texts of the same letters, `cib` from two copies of one dispatch) and 34 labels that I read as clear words (`key/added-values.tsv`).
- `key/key.tsv` gives each label of my rows, its value, its source and the date when I took it. `key/decode.py` applies it to the rows.

## The reading

- No record here builds sentences. Each page gives a short summary of what the decode carries, and the decode row by row.
- The ledger's own reading of R9873 and of f. 128 (R9877, R9878) stays the reading of those letters.

## Remaining gaps

- 3,407 cipher units with no value - blocker: no-key-material; no clear text fixes them by the rules of `check.md`, section 4.
- 1,094 cipher units with a value of the clerk copies only - blocker: no-key-material; these values come from a key fitted on the clerks' texts, so the decode shows them and does not count them.
- 2,200 doubtful units - blocker: illegible; my rows doubt the sign, my sign names change from page to page, or the clerk copy differs from the key.
- 4,910 `?` positions of my rows - blocker: not-attempted; my rows do not tell clear writing from signs that I did not read.
- The sentences of all 30 records - blocker: open-codes; the decode has holes in most rows.

## Escalation

- [x] key: the ledger's key KS4 applied; values added only from clear texts of the same letters (18 November 2026)
- [x] clear texts: BNE MSS/20214/52-1; RAH A-31 ff. 140, 172, 324, 482, 485, 516; the ledger's readings of R9873, R9898 and f. 128
- [ ] a reading in sentences, record by record, against the images

## Credit

- DECODE, the database of historical ciphers of the DECRYPT project: records R9873 to R9905 (30 records with rows; R9902 has none).
- The record pages: https://de-crypt.org/decrypt-web/RecordsView/ followed by the number, for example https://de-crypt.org/decrypt-web/RecordsView/9873.
- Real Academia de la Historia, Madrid, Colección Salazar y Castro A-31 (9/31) and A-34 (9/34).
- Héder and Megyesi (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- No DECODE image is published.
