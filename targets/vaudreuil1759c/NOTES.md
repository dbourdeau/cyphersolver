# Vaudreuil to the minister (Berryer), cipher letter, Montréal, 16 Apr 1759

Status: in progress

Class: read (external key matched), 99.4% of 354 groups; read as sentences against the images on 5 Nov 2026 (a model reading, no outside reader).

Catalogue 1390. ANOM, COL C11A 104, ff.75-76 (CABAC_PIAF_60895); LAC e000874976-e000874977 (2 images); [record](https://nouvelle-france.org/eng/item/details?id=27482). Pierre de Rigaud de Vaudreuil de Cavagnial, governor of New France, to the minister of the Marine. French.
354 number groups (130 distinct); in clear: Monseigneur, the closing formula.

## What the document is

Vaudreuil asks the minister to have the munitionnaire's correspondents in France pay the freight of the ships in Canada, and presses for a supply convoy on which the colony's conservation depends.

## System and key

Syllabary-nomenclator of 700 numbered entries (words, names, syllables, letters), the same table as catalogue 1391 (`targets/vaudreuil1760/`, where the table, its
transcription and the context corrections are described). The key is the 1757 Vaudreuil table, ANOM COL C11E 10 f.289 (LAC e001295274), copied here as
`key/key274.json` and `key/overrides.json`. It fits this letter from the first line; no group falls outside the table.

## The reading

`transcription.txt` (groups), `decode.txt` (decode, syllabic spelling as written), `ct.txt` (groups only), `tools/decode.py`. Outcome method: **external key matched**.
Measured: 354 groups; 2 unread (0.6%), so 99.4% read as sense (`reading.md`, English in `reading_en.md`). Of the 352 read, 348 carry the table value as written; 2 cut groups are restored from the visible
digits and the sense (337 loi, 271 r) and 2 give a wrong value where the sense is clear (389 m for "seront", 488 Iroquois for "d'elle-même"; kept as written, listed in `reading.md`).
Reader pass: both images compared line by line with the transcription; one group corrected (393 -> 593, "l'année prochaine"). The letter asks that the munitionnaire's correspondents in
France replace any ship taken, that freight be paid in Canada, and for a supplement of provisions on which the Colony's preservation depends.

## Remaining gaps
- f.75v "les [?] [?] sont trop grands" (2 groups: 323 + s) - blocker: open-codes; cell 323 reads "pu" on the table crop ("ju" was set on cat. 1391), neither gives the word; the sense is "les frets/prix sont trop grands"

## Escalation
- [x] siblings: the other cipher letters of the same hand (cat. 1388-1391) decoded with the same table; 1392 (Trémais) uses another code
- [x] clear-pages: no clear copy or decipherment found on the leaves of this record
- [x] known-keys: both numerical sheets of C11E 10 tried; sheet e001295274 fits
- [x] print: only the catalogue's vetting (NY Colonial Documents vol. 10, web searches); nothing found
- [x] key-rebuild: table cells corrected from context across the four letters (key/overrides.json)
- [x] retry: the two unread groups re-looked at on the enlarged table cell; 323 not settled; the alphabetical sheets not used

## Files

`transcription.txt`, `decode.txt`, `reading.md`, `reading_en.md`, `reading_notes.md`, `ct.txt`, `key/`, `tools/`, `WORKLOG.md`, `profile.json`. Images are fetched, not stored: `curl -L "https://central.bac-lac.gc.ca/.item?id=<id>&op=img&app=nf"`.
Image credit: Library and Archives Canada (LAC) / Archives nationales d'outre-mer (ANOM), via New France Archives.
