# Vaudreuil to the minister (Berryer), cipher letter, Montréal, 10 Apr 1759

Status: in progress

Class: read (external key matched), 99.2% of 1221 groups; read as sentences against the images on 5 Nov 2026 (a model reading, no outside reader).

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
Measured: 1221 groups (the written ordinals 1o-3o and the date 27 are figures, not groups); 10 unread (0.8%), so 99.2% read as sense (`reading.md`, English in `reading_en.md`, supplied and unread groups in `reading_notes.md`).
Reader pass: all five images compared line by line with the transcription; three groups corrected (353 -> 553 obser, 381 -> 581 faire, 613 -> 615 em); seven cut groups supplied from visible digits and sense.

## Remaining gaps
- f.68v "de l diver m es re ment e c es" (8 groups), f.70v "les [?] [?] de la douceur" (2 groups, 431 + s) - blocker: open-codes; cells 139, 431 do not give the words; scattered, no sentence is lost

## Escalation
- [x] siblings: the other cipher letters of the same hand (cat. 1388-1391) decoded with the same table; 1392 (Trémais) uses another code
- [x] clear-pages: no clear copy or decipherment found on the leaves of this record
- [x] known-keys: both numerical sheets of C11E 10 tried; sheet e001295274 fits
- [ ] print: catalogue vetting (NY Colonial Documents vol. 10, web searches) found nothing; Brice Dudout found the 7 June 1759 abstract of despatches (NY Col. Docs X 974-975, a summary of the 10 and 16 April letters only); Casgrain, the RAPQ and ANOM F3 16 not yet searched
- [x] key-rebuild: table cells corrected from context across the four letters (key/overrides.json)
- [n/a] retry: the unread groups are on cells that need the alphabetical sheets; not retried here

## Second reading: Brice Dudout (PR #268)

Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents, read this letter separately from the same images with the same 1757 table, and sent it as PR #268 (opened 4 Nov 2026, 22:52 UTC) with 1389, 1390 and a reading of 1391. His 1391 is not merged: `targets/vaudreuil1760/` keeps its own reading of 1391. His files are in `dudout/`: `transcription_1389.txt`, `decryption_1389.txt`, `reading_1389.md` (French), `translation_1389.md` (English). They are kept as a second reading beside this folder's, not merged into it.
- Order: the PR was public about 14 hours before this folder's reading was committed (5 Nov 2026, 06:54-07:25 CST). Whether this session saw it is not recorded, so the two readings are a cross-check, not independent verifications of each other.
- His count (certain + probable words, restored words not counted as read): 692 words, 97.7% (669 certain, 7 probable, 15 restored, 1 unresolved). This folder counts cipher groups: 10 groups unread of 1,221 (99.2%). The two measures differ in unit and are not compared.
- Transcriptions (`dudout/compare.txt`, aligned digit sequences): 1,222 groups here (the count includes partial digits of cut groups), 1,220 there; 98.7% of ours sit in matching runs; 15 places differ, mostly the hand's 3/5 and cut groups. Not reconciled; neither file was changed.
- Key and validation: see `targets/vaudreuil1759a/dudout/` (`key.tsv`, `validation.txt`, `compare.txt`); they cover all three letters.
- Where his reading differs from the gaps listed above (candidate fills, not applied here; check them on the image first):
  - f.70v "j employ e les sans s de la douceur" (2 groups, 431 + 235 here): he reads "j'employe les voyes de la douceur" (451 + 255).
  - f.68v "de l diver m es re ment e c es" (8 groups): his reading has "du précis du ‹…› de mes opérations générales" with one cut group open, which reads differently from the 8 groups here; the two transcriptions of that line need a side-by-side look at the image.
- Print: he found the "Abstract of despatches" of 7 June 1759 (New York Colonial Documents X, pp. 974-975), which summarises the letters of 10 and 16 April 1759 in a sentence or two; this letter agrees with it according to him; not re-checked here. Casgrain (Lévis collection), the RAPQ and ANOM F3 16 are not checked. The print step below stays unticked until they are searched.

## Files

`transcription.txt`, `decode.txt`, `reading.md`, `reading_en.md`, `reading_notes.md`, `ct.txt`, `key/`, `tools/`, `WORKLOG.md`, `profile.json`, `dudout/` (second reading, see above). Images are fetched, not stored: `curl -L "https://central.bac-lac.gc.ca/.item?id=<id>&op=img&app=nf"`.
Image credit: Library and Archives Canada (LAC) / Archives nationales d'outre-mer (ANOM), via New France Archives.
