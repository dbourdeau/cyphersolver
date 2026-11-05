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
- [ ] print: catalogue vetting (NY Colonial Documents vol. 10, web searches) found nothing; Brice Dudout found the 7 June 1759 abstract of despatches (NY Col. Docs X 974-975, a summary of the 10 and 16 April letters only); Casgrain, the RAPQ and ANOM F3 16 not yet searched
- [x] key-rebuild: table cells corrected from context across the four letters (key/overrides.json)
- [x] retry: the unread groups were re-run against the images and the alphabetical key (cells 656, 505, 9, 289 and the 5/3 slips settled); 9 places remain (listed above)

## Second reading: Brice Dudout (PR #268)

Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents, read this letter separately from the same images with the same 1757 table, and sent it as PR #268 (opened 4 Nov 2026, 22:52 UTC) with 1389, 1390 and a reading of 1391. His 1391 is not merged: `targets/vaudreuil1760/` keeps its own reading of 1391. His files are in `dudout/`: `transcription_1388.txt`, `decryption_1388.txt`, `reading_1388.md` (French), `translation_1388.md` (English); for the three letters `key.tsv` (his table, v2), `validation.txt` and `compare.txt` (the comparison made when merging, with the key-table differences). They are kept as a second reading beside this folder's, not merged into it.
- Order: the PR was public about 14 hours before this folder's reading was committed (5 Nov 2026, 06:54-07:25 CST). Whether this session saw it is not recorded, so the two readings are a cross-check, not independent verifications of each other.
- His count (certain + probable words, restored words not counted as read): 2,012 words, 99.6% (1,965 certain, 38 probable, 6 restored, 3 unresolved). This folder counts cipher groups: 23 groups unread of 3,633 (99.4%). The two measures differ in unit and are not compared.
- Transcriptions (`dudout/compare.txt`, aligned digit sequences): 3,633 groups here, 3,631 there; 99.2% of ours sit in matching runs; 29 places differ, nearly all by one digit (the hand's 5 against 3, 2 or 4: 235/255, 341/541, 312/512 ...). Not reconciled; neither file was changed.
- Key: his table is a separate transcription of the same sheet (deciphering table e001295274 checked against the enciphering table e001295269, frozen as v1, then 20 corrections in context = v2). Against `key/key274.json` with its overrides, 653 of 700 values agree after dropping accents, case and '?'; 47 differ (listed in `dudout/compare.txt`). His validation: one pre-registered measurement of v1 on the 8 May 1759 letter (ANOM C11A 104 ff.79-83), whose LAC transcript copies the cipher with its contemporary interlinear decipherment: agreement 0.972 against 0.185 for the best of 200 permuted keys (`dudout/validation.txt`). Run by him on his table; not re-run here.
- Where his reading differs from the gaps listed above (candidate fills, not applied here; check them on the image first):
  - f.64r "toutes les s u tu r es des s u l in s" (10 groups): he reads "j'ai pris d'autorité toutes les moutures des moulins".
  - f.59v "la sur co de cette capitale" (2 groups): he reads "la sûreté de cette capitale".
  - f.66r "il n'est point d i que" (2 groups): he reads "il n'est point d'obstacle que je ne surmonte" (his cell 161 is "obstacle", here "i").
  - f.60v "le transport des ap se e ment de leur armée": open in his reading too. His other two open places, f.58 "j'‹équivale›" and f.63v "munitions ‹ta›", are read here.
- Print: he found the "Abstract of despatches" of 7 June 1759 (New York Colonial Documents X, pp. 974-975), which summarises the letters of 10 and 16 April in a sentence or two (not this one); not re-checked here. Not checked by anyone: Casgrain (Lévis collection), the RAPQ, ANOM F3 16 (calames row "Vaudreuil à Berryer lui annonçant en chiffres la perte de la colonie", probably a cipher copy of the 13 Aug 1760 letter, cat. 1391). The print step below stays unticked until they are searched.

## Files

`transcription.txt`, `decode.txt`, `ct.txt`, `key/`, `tools/`, `WORKLOG.md`, `profile.json`, `dudout/` (second reading, see above). Images are fetched, not stored: `curl -L "https://central.bac-lac.gc.ca/.item?id=<id>&op=img&app=nf"`.
Image credit: Library and Archives Canada (LAC) / Archives nationales d'outre-mer (ANOM), via New France Archives.
