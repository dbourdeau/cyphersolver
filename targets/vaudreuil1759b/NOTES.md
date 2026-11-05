# Vaudreuil to the minister (Berryer), cipher letter, Montréal, 10 Apr 1759

Status: in progress

Class: read (external key matched), 99.1% of 1221 groups; read as sentences against the images on 5 Nov 2026 (a model reading, no outside reader).

Catalogue 1389. ANOM, COL C11A 104, ff.68-72 (CABAC_PIAF_60892); LAC e000874969-e000874973 (5 images); [record](https://nouvelle-france.org/eng/item/details?id=27479). Pierre de Rigaud de Vaudreuil de Cavagnial, governor of New France, to the minister of the Marine. French.
1221 number groups (253 distinct); in clear: Monseigneur, the closing formula.

## What the document is

Vaudreuil sends the minister Montcalm's letter of 27 February, a memorandum and his own plan of operations; Montcalm's opinions had become public among officers and people, and Vaudreuil, asking Montcalm to stop it, says he would otherwise arrest the officers concerned and send them to France; he has told Montcalm he is to command at Carillon.

## System and key

Syllabary-nomenclator of 700 numbered entries (words, names, syllables, letters), the same table as catalogue 1391 (`targets/vaudreuil1760/`, where the table, its
transcription and the context corrections are described). The key is the 1757 Vaudreuil table, ANOM COL C11E 10 f.289 (LAC e001295274), copied here as
`key/key274.json` and `key/overrides.json`. It fits this letter from the first line; no group falls outside the table.

## The reading

`transcription.txt` (groups), `decode.txt` (decode, syllabic spelling as written), `ct.txt` (groups only), `tools/decode.py`. Outcome method: **external key matched**.
Measured: 1221 groups (the written ordinals 1o-3o and the date 27 are figures, not groups); 11 unread (0.9%), so 99.1% read as sense (`reading.md`, English in `reading_en.md`, supplied and unread groups in `reading_notes.md`).
Reader pass: all five images compared line by line with the transcription; three groups corrected (353 -> 553 obser, 381 -> 581 faire, 613 -> 615 em); seven cut groups supplied from visible digits and sense.

## Remaining gaps
- f.68v "de l diver m es re ment e c es" (8 groups), f.70v "j'aurois [?] Monseigneur effectué" (1 group, 301) and "les [?] [?] de la douceur" (2 groups, 431 + s) - blocker: open-codes; cells 139, 301, 431 do not give the words; scattered, no sentence is lost

## Escalation
- [x] siblings: the other cipher letters of the same hand (cat. 1388-1391) decoded with the same table; 1392 (Trémais) uses another code
- [x] clear-pages: no clear copy or decipherment found on the leaves of this record
- [x] known-keys: both numerical sheets of C11E 10 tried; sheet e001295274 fits
- [x] print: only the catalogue's vetting (NY Colonial Documents vol. 10, web searches); nothing found
- [x] key-rebuild: table cells corrected from context across the four letters (key/overrides.json)
- [n/a] retry: the unread groups are on cells that need the alphabetical sheets; not retried here

## Files

`transcription.txt`, `decode.txt`, `reading.md`, `reading_en.md`, `reading_notes.md`, `ct.txt`, `key/`, `tools/`, `WORKLOG.md`, `profile.json`. Images are fetched, not stored: `curl -L "https://central.bac-lac.gc.ca/.item?id=<id>&op=img&app=nf"`.
Image credit: Library and Archives Canada (LAC) / Archives nationales d'outre-mer (ANOM), via New France Archives.
