# The key of the decode

## Files

- `key.tsv`: every label of my rows, the value that the decode gives it, its kind, its source and the date when I took it.
- `decode.py`: applies `key.tsv` to the rows files and gives every decode line. From the folder `prabal/`: `python3 key/decode.py --check`.
- `added-values.tsv`: the values that I added to the ledger's key, each with its source, its places and the date.

## The kinds of value in `key.tsv`

| Kind | Source | Taken |
| --- | --- | --- |
| ledger key | KS4 (Brice Dudout, 29 Oct 2026), with the source code of KS4: Daniel Bourdeau's `key_working.md`, or a period cipher and clear pair; two departures: `qes` = es (`key_working.md` pass 3), and the value before the slash for `njn` | 17 Nov 2026 |
| added entry | a clear text of the time, or this ledger's reading, of the same letters (named in each row); for `cib`, two copies of one dispatch read with the key | 18 Nov 2026 |
| clear word | a clear word of a mixed row, not cipher | 18 Nov 2026 |
| clerk value | a key that I fitted on the clerks' decipherments; not in the ledger's key; shown `[x]` in the decode; never counted as read | 17 Nov 2026 |
| no value | none | |

- **Scope.** A label of 1 to 4 Latin letters or digits is one code in all records: scope `all`. A sign is one page: scope `<record>/<page>`, because my sign names change from page to page. A digit that is read through a sign map has the scope of its page. Look up the page scope before `all`.
- **The label map.** The column `source` says "label map" or "sign map" where my label differs from the ledger's label. I made the map by aligning my rows with the ledger's transcriptions of R9873, R9898 and f. 128.
- **Doubt.** The column `doubt` names a doubt that holds at every place of the label: "sign map off its aligned page" or "the clerk-copy value differs". A unit that ends in `~` in my rows is doubtful as well.
- **The lookup.** A unit is put in lower case, with the long s as s and a final `~` dropped (the switch `f~` keeps it).
- **One rule outside the table.** `v` followed by `db` is the opener `v db` (no letter). The table's rows for the opener only name it. So `v` and `db` each have two rows in `key.tsv`: a letter, and the opener. A decoder skips the opener rows and applies this rule, as `decode.py` does.

## The added entries

- **Rule "fixed":** 2 or more places in the texts below agree on the value.
- **Rule "once+clerk strong" or "once+clerk weak":** one place gives the value, and the clerk-copy key holds the same value for the label (a strong or a weak clerk entry).
- **Clear texts of the time (35 entries):** BNE MSS/20214/52-1, the period decipherment of R9873 (transcribed for this work); the period decipherments ff. 140, 172 and 324 (Daniel Bourdeau's transcriptions in this target); the clear leaves ff. 482, 485 and 516 (transcribed for this work).
- **This ledger's readings (27 entries):** R9873, R9898 and f. 128.
- **Two copies of one dispatch (1 entry):** `cib`, from R9879 and R9880 read with the key.
- **The column `in_key_working`** is "yes" for the 4 entries that `key_working.md` already holds. So 59 entries are additions to `key_working.md`.
- **The note column** also names an entry whose value equals a KS4 code one sign away (20 of the 59). Such an entry may be my spelling of the ledger's code.
- **The column `places`** gives the re-read's count of agreeing places. For 5 entries the places by file sum to 3 while `places` is 2. Both numbers come from the re-read's tables; I did not resolve the difference.

## Clear words

- 34 labels (364 units) are clear Spanish words of mixed rows.
- For 9 labels the clerk copies give evidence. For 25 labels (97 units) a word list of 15th-century Spanish is the only evidence.

No value of KS4 changes, apart from the two departures above (`qes` = es; the value before the slash for `njn`).
