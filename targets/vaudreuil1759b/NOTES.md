# Vaudreuil to the minister (Berryer), cipher letter, Montréal, 10 Apr 1759

Status: in progress

Class: not read (decoded, not read). The whole letter decodes mechanically as French; a reader review and translation are what is missing.

Catalogue 1389. ANOM, COL C11A 104, ff.68-72 (CABAC_PIAF_60892); LAC e000874969-e000874973 (5 images); [record](https://nouvelle-france.org/eng/item/details?id=27479). Pierre de Rigaud de Vaudreuil de Cavagnial, governor of New France, to the minister of the Marine. French.
1225 number groups (256 distinct); in clear: Monseigneur, the closing formula.

## What the document is

Vaudreuil sends the minister Montcalm's letter with his own reflections: Montcalm's way of thinking had become public among officers, bourgeois and soldiers; Vaudreuil asks that the officers who spread such talk be sent to France.

## System and key

Syllabary-nomenclator of 700 numbered entries (words, names, syllables, letters), the same table as catalogue 1391 (`targets/vaudreuil1760/`, where the table, its
transcription and the context corrections are described). The key is the 1757 Vaudreuil table, ANOM COL C11E 10 f.289 (LAC e001295274), copied here as
`key/key274.json` and `key/overrides.json`. It fits this letter from the first line; no group falls outside the table.

## The reading

`transcription.txt` (groups), `decode.txt` (decode, syllabic spelling as written), `ct.txt` (groups only), `tools/decode.py`. Outcome method: **external key matched**.
Measured: 97.3% of groups carry a settled value (1192 of 1225); 1 sit on a doubtful table cell and 32 are cut at the gutter. The decode reads as French
throughout; no reader has yet reviewed it as sentences and there is no English translation.

## Remaining gaps
- 32 groups cut by the binding - blocker: illegible; microfilm image; a clear copy would restore them
- 1 groups on table cells still doubtful - blocker: open-codes; cells read from a small image of the table; the alphabetical key sheets e001295267/69 are not yet used to settle them
- reader review and English translation of the whole letter - blocker: not-attempted; not yet done

## Escalation
- [x] siblings: the other cipher letters of the same hand (cat. 1388-1391) decoded with the same table; 1392 (Trémais) uses another code
- [x] clear-pages: no clear copy or decipherment found on the leaves of this record
- [x] known-keys: both numerical sheets of C11E 10 tried; sheet e001295274 fits
- [x] print: only the catalogue's vetting (NY Colonial Documents vol. 10, web searches); nothing found
- [x] key-rebuild: table cells corrected from context across the four letters (key/overrides.json)
- [n/a] retry: the unread groups are on cells that need the alphabetical sheets; not retried here

## Files

`transcription.txt`, `decode.txt`, `ct.txt`, `key/`, `tools/`, `WORKLOG.md`, `profile.json`. Images are fetched, not stored: `curl -L "https://central.bac-lac.gc.ca/.item?id=<id>&op=img&app=nf"`.
Image credit: Library and Archives Canada (LAC) / Archives nationales d'outre-mer (ANOM), via New France Archives.
