# Vaudreuil to the minister (Berryer), cipher letter, Montréal, 16 Apr 1759

Status: in progress

Class: not read (decoded, not read). The whole letter decodes mechanically as French; a reader review and translation are what is missing.

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
Measured: 99.4% of groups carry a settled value (352 of 354); 0 sit on a doubtful table cell and 2 are cut at the gutter. The decode reads as French
throughout; no reader has yet reviewed it as sentences and there is no English translation.

## Remaining gaps
- 2 groups cut by the binding - blocker: illegible; microfilm image; a clear copy would restore them
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
