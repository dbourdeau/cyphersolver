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
- [ ] print: catalogue vetting (NY Colonial Documents vol. 10, web searches) found nothing; Brice Dudout found the 7 June 1759 abstract of despatches (NY Col. Docs X 974-975, a summary of the 10 and 16 April letters only); Casgrain, the RAPQ and ANOM F3 16 not yet searched
- [x] key-rebuild: table cells corrected from context across the four letters (key/overrides.json)
- [x] retry: the two unread groups re-looked at on the enlarged table cell; 323 not settled; the alphabetical sheets not used

## Second reading: Brice Dudout (PR #268)

Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents, read this letter separately from the same images with the same 1757 table, and sent it as PR #268 (opened 4 Nov 2026, 22:52 UTC) with 1389, 1390 and a reading of 1391. His 1391 is not merged: `targets/vaudreuil1760/` keeps its own reading of 1391. His files are in `dudout/`: `transcription_1390.txt`, `decryption_1390.txt`, `reading_1390.md` (French), `translation_1390.md` (English). They are kept as a second reading beside this folder's, not merged into it.
- Order: the PR was public about 14 hours before this folder's reading was committed (5 Nov 2026, 06:54-07:25 CST). Whether this session saw it is not recorded, so the two readings are a cross-check, not independent verifications of each other.
- His count (certain + probable words, restored words not counted as read): 210 words, 99.5% (205 certain, 4 probable, 1 restored, 0 unresolved). This folder counts cipher groups: 2 groups unread of 354 (99.4%). The two measures differ in unit and are not compared.
- Transcriptions (`dudout/compare.txt`, aligned digit sequences): 354 groups in both; 98.0% of ours sit in matching runs; 7 places differ (323/523, 403/405, 389/309, 488/498, 351/354 and two cut groups). Not reconciled; neither file was changed.
- Key and validation: see `targets/vaudreuil1759a/dudout/` (`key.tsv`, `validation.txt`, `compare.txt`); they cover all three letters.
- Where his reading differs from the gaps listed above (candidate fills, not applied here; check them on the image first):
  - f.75v "les [?] [?] sont trop grands" (2 groups, 323 + s here): he reads "les risques sont trop grands pour qu'il puisse payer" (his cell is 523, "risque"; cell 323 is "ju").
  - The two groups kept as written here where the sense is clear (389 "m" for "seront", 488 "Iroquois" for "d'elle-même"): in his transcription they are 309 ("se") and 498 ("elle"), so they look like digit slips (3/5/8/9) in one of the two transcriptions, not wrong table values.
- Print: he found the "Abstract of despatches" of 7 June 1759 (New York Colonial Documents X, pp. 974-975), which summarises the letters of 10 and 16 April 1759 in a sentence or two; this letter agrees with it according to him; not re-checked here. Casgrain (Lévis collection), the RAPQ and ANOM F3 16 are not checked. The print step below stays unticked until they are searched.

## Files

`transcription.txt`, `decode.txt`, `reading.md`, `reading_en.md`, `reading_notes.md`, `ct.txt`, `key/`, `tools/`, `WORKLOG.md`, `profile.json`, `dudout/` (second reading, see above). Images are fetched, not stored: `curl -L "https://central.bac-lac.gc.ca/.item?id=<id>&op=img&app=nf"`.
Image credit: Library and Archives Canada (LAC) / Archives nationales d'outre-mer (ANOM), via New France Archives.
