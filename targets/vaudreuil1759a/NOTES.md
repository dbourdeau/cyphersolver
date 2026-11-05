# Vaudreuil to the minister (Berryer), cipher letter, Montréal, 8 Apr 1759

Status: in progress

Class: read (external key matched), 99.4% of 3633 groups; read as sentences against the images on 5 Nov 2026 (a model reading, no outside reader).

Catalogue 1388. ANOM, COL C11A 104, ff.54-66 (CABAC_PIAF_60891); LAC e000874955-e000874967 (13 images); [record](https://nouvelle-france.org/eng/item/details?id=27478). Pierre de Rigaud de Vaudreuil de Cavagnial, governor of New France, to the minister of the Marine. French.
3633 number groups (385 distinct); in clear: Monseigneur, the closing formula.

## What the document is

Vaudreuil reports to the minister on the winter and the defence plan: famine and loss of draught animals, the census of the three governments (about 13 000 militia), a British army of 25-30 000 against Carillon and 10 000 each against the Belle Rivière and Niagara, Fort Duquesne evacuated, Montcalm's refusal to pursue the enemy in 1758, and his own plan to fall back on Québec with the troops and fight there; numbered requests for battalions, munitions and provisions (full French in [reading.md](reading.md), English in [reading_en.md](reading_en.md)).

## System and key

Syllabary-nomenclator of 700 numbered entries (words, names, syllables, letters), the same table as catalogue 1391 (`targets/vaudreuil1760/`, where the table, its
transcription and the context corrections are described). The key is the 1757 Vaudreuil table, ANOM COL C11E 10 f.289 (LAC e001295274), copied here as
`key/key274.json` and `key/overrides.json`. It fits this letter from the first line; no group falls outside the table.

## The reading

`transcription.txt` (groups), `decode.txt` (decode, syllabic spelling as written), `ct.txt` (groups only), `reading.md` (French), `reading_en.md` (English), `reading_notes.md` (corrections, supplied and unread groups), `tools/sib.py`. Outcome method: **external key matched**.
Measured: 3633 groups (the written ordinals 1o-4o are figures, not groups); 23 unread (0.6%), so 99.4% read as sense; no group is cut at the gutter.
Reader pass: all 13 images compared with the transcription in half-page crops; 21 groups corrected (the hand's 5 taken for 3, or the reverse; 301 trou is 501 ois in six places, the same slip as in cat. 1389 f.70v);
four table cells settled from the letter (656 q, 505 am, 9 possession, 289 os). The reading builds sentences throughout; the checker rates it readable (0.843).

## Remaining gaps
- f.64r "toutes les s u tu r es des s u l in s" (10 groups) - blocker: open-codes; the groups do not spell a word the sense wants (the seigneurs' seed or stores are a guess); no sentence is lost
- f.60v "le transport des ap se e ment de leur armée" (4 groups), f.59v "la sur co de cette capitale" (2), f.66r "il n'est point d i que" (2) and 5 single groups (f.56v 389, f.58r 84, f.61r 235, f.63r 65, f.63v 686) - blocker: open-codes; scattered, none leaves a sentence unread

## Escalation
- [x] siblings: the other cipher letters of the same hand (cat. 1388-1391) decoded with the same table; 1392 (Trémais) uses another code
- [x] clear-pages: no clear copy or decipherment found on the leaves of this record
- [x] known-keys: both numerical sheets of C11E 10 tried; sheet e001295274 fits
- [x] print: only the catalogue's vetting (NY Colonial Documents vol. 10, web searches); nothing found
- [x] key-rebuild: table cells corrected from context across the four letters (key/overrides.json)
- [x] retry: the unread groups were re-run against the images and the alphabetical key (cells 656, 505, 9, 289 and the 5/3 slips settled); 9 places remain (listed above)

## Files

`transcription.txt`, `decode.txt`, `ct.txt`, `key/`, `tools/`, `WORKLOG.md`, `profile.json`. Images are fetched, not stored: `curl -L "https://central.bac-lac.gc.ca/.item?id=<id>&op=img&app=nf"`.
Image credit: Library and Archives Canada (LAC) / Archives nationales d'outre-mer (ANOM), via New France Archives.
