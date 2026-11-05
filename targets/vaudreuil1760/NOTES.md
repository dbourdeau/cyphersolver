# Vaudreuil to the minister (Berryer), cipher letter, Montréal, 13 Aug 1760

Catalogue 1391. ANOM COL C11A 105 ff.147-152 (CABAC_PIAF_61062), 6 images
(LAC e000875753-e000875758, [record](https://nouvelle-france.org/eng/item/details?id=27665)).
Pierre de Rigaud de Vaudreuil de Cavagnial, governor of New France, to the minister of the Marine, written weeks before the
capitulation of Montréal (8 Sept 1760). French. 2424 number groups, 35 words in clear.

## What the document is

A whole letter in number groups, with names, titles and the closing formula in clear. Spread over f.147r-152r; f.152r ends with
the clear formula "Je suis avec un très profond respect, Monsieur, votre très humble et très obéissant serviteur, Vaudreuil".
It is a war report: the British fleet and Amherst's army converging on Montréal, the three French ships bound for Ristigouche
under M. Danjac, the frigate Machault (Sr Lagirauday), the goélette l'Extravagante in the baie des Chaleurs, the loss of the lake
Champlain flotilla, no powder, no food, Murray's circular letter to the militia captains (copy enclosed) against the paper money, the
Intendant and Lévis following Vaudreuil's example, and the request that the minister assure the King that the colony will
fall only at the last extremity. Full French reading in [reading.md](reading.md).

## System and key

A syllabary-nomenclator of 700 numbered entries (1-700): whole words, names of places and ships, syllables, single letters;
homophones for the commonest items (de 309/642, t 51, i 661, te 107, s 235). Words not in the table (names, titles, "Monseigneur")
are written in clear. Spelling is phonetic.

The key is the 1757 table of Vaudreuil, in the same volume the vetting named: ANOM COL C11E 10 ff.285-290v,
"Chiffre ou code de Montcalm et de Vaudreuil ... 1757 et 1758" (nouvelle-france.org 15213, LAC e001295267-76). The 10 images hold two
tables for Vaudreuil/the Marine (1757, two sheets) and the Montcalm table (1758), each as an alphabetical list and a
numerical list. The numerical sheet that decodes this letter is e001295274 (the second numerical sheet; the first, e001295272, does
not fit). Transcribed here in full: `key/key274.json` (700 entries; `?` marks doubtful cells) and `key/overrides.json` (32 cells
corrected from the letter, each with its reason). The table was not previously connected with this letter.

## The reading

`reading.md` (French), `transcription.txt` (groups), `tools/decode.py` (decode), `tools/stats.py` (measure), `gaps.json` (legible groups
not read), `restored.json` (gutter-cut groups restored from the visible first digits and the sense).
Outcome method: **external key matched** (a key from the same collection, filed for the same correspondent three years earlier, not
connected with this letter, found to fit and applied; the table cells were read from the images and corrected from the letter).
Measured (`tools/stats.py`, 5 Nov 2026, third pass): of 2424 groups, 2328 (96.0%) are read from the image as written; 25 more (1.0%, total 97.1%)
are groups cut by the binding that the visible leading digit(s) and the sense fix; 24 (1.0%) are legible and unread, in 9 places; 47 (1.9%) are lost in the gutter.
That clears the read bar (95% as sense, measured; every folio read; every legible gap tried; what stays open is scattered groups and the binding).
Third pass: an interlinear line on f.150v belongs at a caret after "de" ("ces derniers se lassent de notre extrême indigence, il ne faut rien moins
que mes soins ..."); the duplicate group 51 that had been read there is removed; "qui[n]ze", "[Lou]isbourg" and "aie [don]né" settle three more places;
cell 2 of the table is "campagne" (the alphabetical sheet e001295269 has compagnie = 102), not "compagnie".
The historical frame is confirmed by the clear letters next to it in C11A 105 (7 and 13 Aug 1760: the Machault, the Bienfaisant and the Marquis
de Malauze with the troops, François-Gabriel d'Angeac = "M. Danjac", La Giraudais, Villemont carrying the despatches, the goélette
l'Extravagante, Bigot, Amherst).

## Remaining gaps
- groups cut by the binding at the right edge of ff.147v-151v (20 partly visible and not restored, 27 wholly lost) - blocker: illegible; microfilm image, a clear copy would restore them
- f.147v.4 "et i" after "tiennent ce poste" and f.147v.9 "mais son se le pour-ra-t" (6 groups) - blocker: open-codes; cells confirmed on the alphabetical sheet, the words are not identified
- f.147v.24-25 "au pre[..] / i si un instant favorable" (3 groups) - blocker: open-codes; the order given for the Machault, words not identified
- f.148r.13-14 "fin-i-ra bateau campagne" (5 groups) - blocker: open-codes; the officer Villemont, "fin i ra" and "bateau" confirmed, the phrase is not
- f.148v.17 "de b l[..]" (2 groups) after "quinze diverses charges du" - blocker: open-codes; the word is not identified
- f.149v.17-18 "ceux un | ton" (2 groups) - blocker: open-codes; cells 494 and 152 (ton) confirmed on the alphabetical sheet, the sense is not
- f.150v.24 "de moyen" (2 groups) and f.151v.6 "nt s" (2 groups) and f.151v.19-20 "je vous ent[..] e" (2 groups) - blocker: open-codes; cell 473 = moyen confirmed, the words are not identified

## Escalation
- [x] siblings: neighbouring records of C11A 105 (ff.136-146, 153-155: clear letters of 7 and 13 Aug 1760) opened, they confirm the names and facts; the four cipher letters of the same hand and office (cat. 1388, 1389, 1390 of April 1759 and 1392 of Nov 1759, C11A 104) fetched and tested with the same table: 1390 (354 groups) decodes as French in full with it, 1389 and 1388 use the same groups (1389 sample f.68v-69v reads: "j'ai l'honneur de vous envoyer ci-joint copie de la lettre que M. le marquis de Montcalm m'écrivit ... février dernier"); 1392 (Trémais, 6 Nov 1759) does not: its numbers are a different, smaller code mixed with clear French
- [x] clear-pages: ff.142-146 (lake Champlain, movements of the enemy, 7 Aug) and the cover letters ff.153-154 (13 Aug) checked; none is a decipherment
- [x] known-keys: both numerical sheets 272 and 274 of C11E 10 tried; 274 fits and reads the letter (the third numerical sheet, e001295276, not tried)
- [x] print: web searches (FR/EN, 5 Nov) for the letter, the cipher and the correspondents, and NY Colonial Documents vol. 10 (vetting): nothing; Tomokiyo's and Lasry's pages were searched, not opened; Casgrain's Lévis collection not read for this date
- [x] key-rebuild: 33 table cells corrected from the letter and the images (key/overrides.json); the alphabetical sheet e001295269 (rotated 90 degrees, readable at 5x) used to confirm cells 473 moyen, 152 ton, 671 bateau and to correct cell 2 (campagne)
- [x] retry: the unread groups were re-run with the corrected key and the alphabetical sheet; 9 places remain (listed above)

## Sibling letters (C11A 104, 1759) decoded with the same table

The 1757 table is Vaudreuil's working key from at least April 1759 to August 1760, not only a 1757-58 key. Transcribed in full here and decoded
with the same table and overrides (`tools/sib.py`); each reads as French. They now have targets of their own (cat. 1388 = `targets/vaudreuil1759a/`, 1389 = `vaudreuil1759b/`, 1390 = `vaudreuil1759c/`; class "read" for all three, 99.4% / 99.2% / 99.4%, model readings with no outside reader); they are
listed as evidence that the table fits and as extra text for cell checks (5 cells settled on them: 452 fret, 301 trou, 133 oit, 367 crai, 195 vrai, 613 cas).
- cat. 1388 (8 Apr 1759, ff.54-66, LAC e000874955-67, 13 images, 3637 groups): `sibs/1388.txt`, decode `sibs/1388_decode.txt`. Reports on the winter and the defence plan:
  famine and loss of draught animals, 20-25 000 men against Niagara, Fort Duquesne evacuated, Montcalm's absence, numbered requests (1o battalions, 2o munitions, 3o provisions).
- cat. 1389 (10 Apr 1759, ff.68-72, e000874969-73, 1225 groups, 32 partly cut at the gutter): `sibs/1389.txt`, decode `sibs/1389_decode.txt`. Encloses Montcalm's letter and
  reflections ("la façon de penser de M. le marquis de Montcalm a été publique ..."); Vaudreuil asks that the officers who spread such talk be sent to France.
- cat. 1390 (16 Apr 1759, ff.75-76, e000874976-77, 354 groups): `sibs/1390.txt`, decode `sibs/1390_decode.txt`. Freight of the supply ships, munitionnaire.
- cat. 1392 (Trémais, 6 Nov 1759): not this table; a different code with clear French between the groups; separate target.
The records' image lists end one short for 1388 (the 13th image, e000874967, holds ff.65v-66). The three letters have profiles and reading files of their own; they carry the same hand's 3/5 confusion, which was corrected line by line on the images in cats. 1388-1390 (see their `reading_notes.md`). The 1391 transcription has not had that line-by-line image comparison.

## Files

`transcription.txt`, `reading.md`, `gaps.json`, `key/key274.json`, `key/overrides.json`, `key/t274_part*.txt`, `tools/` (cell crops,
decode, stats), `WORKLOG.md`, `profile.json`. Images are fetched, not stored (`img/`, `key/*.jpg`, `crops/` are git-ignored); fetch with
`curl -L "https://central.bac-lac.gc.ca/.item?id=e000875753&op=img&app=nf"` (ids e000875753-58 and e001295267-76).
Image credit: Library and Archives Canada (LAC) / Archives nationales d'outre-mer (ANOM), via New France Archives.
