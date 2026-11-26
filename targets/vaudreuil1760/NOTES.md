# Vaudreuil to the minister (Berryer), four cipher letters in his 1757 table, Montréal, Apr 1759 and Aug 1760

Catalogue 1388, 1389, 1390 and 1391. Class: **read in part** (24 Nov 2026), method: read after matching with a key from
external sources. The three April 1759 letters are each read (README word bar: 0.983, 0.983, 0.979); the 13 Aug 1760 letter is
read in part (0.933). Over the four letters 7499 of 7632 cipher groups are read as written (0.983).

## The merge (24 Nov 2026)

One key, one target: the maintainers decided on 24 Nov 2026 that the three April 1759 letters, which had targets of their own
(`vaudreuil1759a`, `vaudreuil1759b`, `vaudreuil1759c`; catalogue 1388-1390), belong here, since all four are in Vaudreuil's 1757
table. Their folders were moved whole with `git mv` (as for the Sabran and Mâcon merges) to `cat1388/`, `cat1389/` and `cat1390/`;
each keeps its transcription, decode, reading, translation, reading notes, tools, key copy, worklog and Brice Dudout's second
reading (`dudout/`). Their former NOTES are kept as `cat1388/notes_former_vaudreuil1759a.md`, `cat1389/notes_former_vaudreuil1759b.md`
and `cat1390/notes_former_vaudreuil1759c.md`; their profiles are merged into `profile.json` (documents B, C, D; their solution steps
prefixed with the catalogue number) and removed. The old folder names had no pages, so no stub page is needed.

| Doc | Cat. | Date | Shelfmark (ANOM COL) | LAC images | Groups | Unread groups | Words (README measure) | Holes | read_share | State |
|---|---|---|---|---|---|---|---|---|---|---|
| B | 1388 | 8 Apr 1759 | C11A 104 ff.54-66 | e000874955-67 (13) | 3633 | 23 | 2154 | 38 | 0.983 | read |
| C | 1389 | 10 Apr 1759 | C11A 104 ff.68-72 | e000874969-73 (5) | 1221 | 10 | 804 | 14 | 0.983 | read |
| D | 1390 | 16 Apr 1759 | C11A 104 ff.75-76 | e000874976-77 (2) | 354 | 2 | 325 | 7 | 0.979 | read |
| A | 1391 | 13 Aug 1760 | C11A 105 ff.147-152 | e000875753-58 (6) | 2424 | 26 legible + 47 gutter | 1383 (body) | 100 | 0.933 | read in part |

The word measures are `research/reading_audit/v10_relabel.measure_text` on each `reading.md` (24 Nov 2026 for the 1759 letters;
14 Nov 2026 for 1391, body only). The 1759 figures recorded on 5 Nov 2026 (99.4%, 99.2%, 99.4%) were shares of groups.
The three 1759 letters: 1388 reports on the winter and the defence plan (famine, the census of the three governments, the four
points to defend, the plan to fight at Québec, requests for battalions, munitions and provisions); 1389 sends Montcalm's letter of
27 February and complains that his opinions have gone round the colony; 1390 asks that the munitionnaire's correspondents replace
captured ships, that freight be paid in Canada, and for a supplement of provisions. Readings: `cat1388/reading.md`, `cat1389/reading.md`,
`cat1390/reading.md`, English in each `reading_en.md`, corrections, supplied and unread groups in each `reading_notes.md`.

## Reading reviews (24 Nov 2026)

The four reading reviews of 5 Nov 2026 were signed by the model that made the readings. They are replaced by the integration
review of 24 Nov 2026 (an AI agent, for the maintainers; not a person, and not the author): each reading read as French sentences
against its decode file; grade A for all four (coherent, holes scattered); cat. 1390 f.75r compared with its image. The notes in
`profile.json` say what was and was not done.

## Printed excerpts found (24 Nov 2026)

Francis Parkman, *Montcalm and Wolfe* (Boston 1884), vol. 2, ch. 23 "The Brink of Ruin" (archive.org `montcalmwolfe03park`),
translates passages of Vaudreuil's letters to the minister:
- "Vaudreuil au Ministre, 8 Avril, 1759": the census of a little more than 13,000 effective men (cat. 1388 gives 6356 + 5455 + 1313 =
  13,124), and a long translated passage ("If the English attack Quebec, I shall always hold myself free to go thither myself with
  most of the troops ... give battle ... again and again ... the slightest change in my arrangements would have the most unfortunate
  consequences") that is cat. 1388 f.62r-62v as read here. His other quotation under the same date ("infamous conduct and indecent
  talk ... ask for his recall") is not in cat. 1388 and must come from another letter of that day.
- "Vaudreuil au Ministre, 10 Avril, 1759": "the people are alarmed and would lose courage if my firmness did not rekindle their zeal
  to serve the King", the end of cat. 1389 f.69r as read here.
So a clear or deciphered text of 1388 and 1389 was read by Parkman in the Paris archives; only excerpts in English are in print.
Found after the readings, not used for them; recorded in `profile.json` as `prior_solution: partial`. The agreement is an outside
check of both readings at those places. Nothing was found for 16 Apr 1759 or 13 Aug 1760.

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
Measured (`tools/stats.py`, 5 Nov 2026, third pass): of 2424 groups, 2326 (96.0%) are read from the image as written; 25 more (1.0%, total 97.0%)
are groups cut by the binding that the visible leading digit(s) and the sense fix; 26 (1.1%) are legible and unread, in 9 places; 47 (1.9%) are lost in the gutter.
These are shares of groups. The README read bar is a share of words: by that measure the letter reads at 0.933, under 0.95, so it is **read in part** (recount of 14 Nov 2026, below); every folio reads and every legible gap was tried, and what stays open is scattered groups and the binding.
Third pass: an interlinear line on f.150v belongs at a caret after "de" ("ces derniers se lassent de notre extrême indigence, il ne faut rien moins
que mes soins ..."); the duplicate group 51 that had been read there is removed; "qui[n]ze", "[Lou]isbourg" and "aie [don]né" settle three more places;
cell 2 of the table is "campagne" (the alphabetical sheet e001295269 has compagnie = 102), not "compagnie".
The historical frame is confirmed by the clear letters next to it in C11A 105 (7 and 13 Aug 1760: the Machault, the Bienfaisant and the Marquis
de Malauze with the troops, François-Gabriel d'Angeac = "M. Danjac", La Giraudais, Villemont carrying the despatches, the goélette
l'Extravagante, Bigot, Amherst).

## Read bar recount and check of PR #565 (14 Nov 2026)

Brice Dudout's verification (PR #565, `VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) decodes `transcription.txt` from
`key/key274.json` + `key/overrides.json` alone: 2401 legible groups, none without a cell, 97.5% of the decoded letters aligned with
`reading.md`. Re-run here: same figures. He found no key correction, and one unmarked emendation: on f.152r, line 12 of the folio,
`672 672^ 51 51 | 494` decodes "me me t t / un", and the reading had "me mettroit" with no mark (494 = un is a confirmed cell). The reading
now has "me mett[roit]". The LAC image of f.152r (e000875758) was compared group by group with the transcription of the whole folio and
the first seven lines of f.151v (about 240 groups): all agree, and the inserted 672 written above the line is on the image.

He also pointed out that the recorded `read_share` 0.96 was the share of groups (2326 of 2424, `tools/stats.py`), not of words. Measured
on the reading body (ff.147r-152r) with the README rule (`research/reading_audit/v2_score.holes`: supplied, restored and unread words are
holes): 1383 words, 100 holes, **0.933**; his figure with `v10_relabel.measure` on the whole file was 0.937 (0.936 once the emendation is
marked; the whole file counts the preamble too). Under 0.95, so the class moves from read to **read in part** (profile, page and ledgers
changed the same day). The gaps below all keep an outside blocker; nothing in the reading changed except the mark.

## Remaining gaps
- groups cut by the binding at the right edge of ff.147v-151v (20 partly visible and not restored, 27 wholly lost) - blocker: illegible; microfilm image, a clear copy would restore them
- f.147v.4 "et i" after "tiennent ce poste" and f.147v.9 "mais son se le pour-ra-t" (8 groups: 2 at f.147v.4 and 6 at f.147v.9, as in gaps.json) - blocker: open-codes; cells confirmed on the alphabetical sheet, the words are not identified
- f.147v.24-25 "au pre[..] / i si un instant favorable" (3 groups) - blocker: open-codes; the order given for the Machault, words not identified
- f.148r.13-14 "fin-i-ra bateau campagne" (5 groups) - blocker: open-codes; the officer Villemont, "fin i ra" and "bateau" confirmed, the phrase is not
- f.148v.17 "de b l[..]" (2 groups) after "quinze diverses charges du" - blocker: open-codes; the word is not identified
- f.149v.17-18 "ceux un | ton" (2 groups) - blocker: open-codes; cells 494 and 152 (ton) confirmed on the alphabetical sheet, the sense is not
- f.150v.24 "de moyen" (2 groups) and f.151v.6 "nt s" (2 groups) and f.151v.19-20 "je vous ent[..] e" (2 groups) - blocker: open-codes; cell 473 = moyen confirmed, the words are not identified
- cat. 1388 f.64r "toutes les s u tu r es des s u l in s" (10 groups) - blocker: open-codes; the groups do not spell the word the sense wants (Dudout reads "toutes les moutures des moulins", not checked on the image); no sentence is lost
- cat. 1388 f.60v "des ap se e ment" (4), f.59v "la sur co" (2), f.66r "point d i que" (2) and 5 single groups (f.56v 389, f.58r 84, f.61r 235, f.63r 65, f.63v 686) - blocker: open-codes; scattered, none leaves a sentence unread
- cat. 1389 f.68v "de l diver m es re ment e c es" (8 groups) and f.70v "les [?] [?] de la douceur" (2) - blocker: open-codes; cells 139 and 431 do not give the words; Dudout's transcription of f.68v differs, a side-by-side look at the image is owed
- cat. 1390 f.75v "les [?] [?] sont trop grands" (2 groups, 323 + s) - blocker: open-codes; cell 323 reads "pu" on the table crop, neither "pu" nor "ju" gives the word

## Escalation
- [x] siblings: neighbouring records of C11A 105 (ff.136-146, 153-155: clear letters of 7 and 13 Aug 1760) opened, they confirm the names and facts; the four cipher letters of the same hand and office (cat. 1388, 1389, 1390 of April 1759 and 1392 of Nov 1759, C11A 104) fetched and tested with the same table: 1390 (354 groups) decodes as French in full with it, 1389 and 1388 use the same groups (1389 sample f.68v-69v reads: "j'ai l'honneur de vous envoyer ci-joint copie de la lettre que M. le marquis de Montcalm m'écrivit ... février dernier"); 1392 (Trémais, 6 Nov 1759) does not: its numbers are a different, smaller code mixed with clear French
- [x] clear-pages: ff.142-146 (lake Champlain, movements of the enemy, 7 Aug) and the cover letters ff.153-154 (13 Aug) checked; none is a decipherment
- [x] known-keys: both numerical sheets 272 and 274 of C11E 10 tried; 274 fits and reads the letter (the third numerical sheet, e001295276, not tried)
- [x] print: web searches (FR/EN, 5 Nov) for the letter, the cipher and the correspondents, and NY Colonial Documents vol. 10 (vetting): nothing; Tomokiyo's and Lasry's pages were searched, not opened. 24 Nov 2026, all four letters: archive.org full-text search (fts) on dates and phrases found Parkman, Montcalm and Wolfe (1884) ch. 23, with translated excerpts of the 8 and 10 Apr 1759 letters that agree with cat. 1388 and 1389 (above); nothing for 16 Apr 1759 or 13 Aug 1760; Canadiana phrase search: no results. Brice Dudout's NY Col. Docs X 974-975 abstract of 7 June 1759 (10 and 16 Apr letters summarised) not re-checked. Casgrain's Lévis collection (letters to Lévis, not to the minister), the RAPQ and ANOM F3 16 (calames "Vaudreuil à Berryer lui annonçant en chiffres la perte de la colonie", probably a copy of 1391) not reached as full text: a clear copy of 1391 in F3 16 would close the gutter gaps and is the one print/copy lead left (blocker: ANOM F3 16 not found online in this pass)
- [x] key-rebuild: 33 table cells corrected from the letter and the images (key/overrides.json); the alphabetical sheet e001295269 (rotated 90 degrees, readable at 5x) used to confirm cells 473 moyen, 152 ton, 671 bateau and to correct cell 2 (campagne)
- [x] retry: the unread groups were re-run with the corrected key and the alphabetical sheet; 9 places remain (listed above)

## Sibling letters (C11A 104, 1759) decoded with the same table

The 1757 table is Vaudreuil's working key from at least April 1759 to August 1760, not only a 1757-58 key. Transcribed in full here and decoded
with the same table and overrides (`tools/sib.py`); each reads as French. They had targets of their own from 5 to 24 Nov 2026 (`vaudreuil1759a/b/c`) and are now part of this target (`cat1388/`, `cat1389/`, `cat1390/`; see "The merge" above; `sibs/` keeps the first, uncorrected transcriptions of 5 Nov). They also served
as extra text for cell checks (5 cells settled on them: 452 fret, 301 trou, 133 oit, 367 crai, 195 vrai, 613 cas).
- cat. 1388 (8 Apr 1759, ff.54-66, LAC e000874955-67, 13 images, 3637 groups): `sibs/1388.txt`, decode `sibs/1388_decode.txt`. Reports on the winter and the defence plan:
  famine and loss of draught animals, 20-25 000 men against Niagara, Fort Duquesne evacuated, Montcalm's absence, numbered requests (1o battalions, 2o munitions, 3o provisions).
- cat. 1389 (10 Apr 1759, ff.68-72, e000874969-73, 1225 groups, 32 partly cut at the gutter): `sibs/1389.txt`, decode `sibs/1389_decode.txt`. Encloses Montcalm's letter and
  reflections ("la façon de penser de M. le marquis de Montcalm a été publique ..."); Vaudreuil asks that the officers who spread such talk be sent to France.
- cat. 1390 (16 Apr 1759, ff.75-76, e000874976-77, 354 groups): `sibs/1390.txt`, decode `sibs/1390_decode.txt`. Freight of the supply ships, munitionnaire.
- cat. 1392 (Trémais, 6 Nov 1759): not this table; a different code with clear French between the groups; separate target.
The records' image lists end one short for 1388 (the 13th image, e000874967, holds ff.65v-66). The three letters have profiles and reading files of their own; they carry the same hand's 3/5 confusion, which was corrected line by line on the images in cats. 1388-1390 (see their `reading_notes.md`). The 1391 transcription has not had that line-by-line image comparison.

## Transcription doubts

What the transcriptions and reading notes themselves mark as doubtful (24 Nov 2026 summary; details in each `reading_notes.md`). Format: sign (where) - read: reading; checked: what; evidence.
- 5 written like 3 (all four letters; 26 groups in 1388-1390, e.g. 301 -> 501 ois in seven places, 353 -> 553, 393 -> 593) - read: as corrected in each `transcription.txt`; checked: image, decode; every line of the 1759 letters compared with the images on 5 Nov 2026 (solver's pass), and f.75r of 1390 re-compared on LAC e000874976 on 24 Nov 2026 (the first eleven cipher lines agree). In 1391 only f.152r and seven lines of f.151v were compared (14 Nov 2026); other 3/5 slips may remain there.
- one-digit differences from Brice Dudout's transcriptions (1388: 29 places; 1389: 15; `cat1388/dudout/compare.txt`, `cat1389/dudout/compare.txt`) - read: ours kept; checked: decode, transcription; not settled on the images (open).
- gutter-cut groups (1391: 20 partly visible not restored, 27 lost, 25 restored; 1389: 32 partly cut, 7 supplied; 1390: 2 restored) - read: restored ones from the visible digits and the sense, marked `[...]` in the readings and counted as holes; checked: image, decode; the rest cannot be seen on the microfilm.
- three written signs that are not numbers (1388 f.62v after "boulets", f.63v after "munitions ta", f.63v after "j'en fais") - read: unread, `[signe ?]`; checked: image; not counted as groups.
- figures in clear (1388 and 1389 ordinals 1o-4o, 1389 date "27") - read: figures, bracketed in the transcriptions; checked: image, decode (as cipher they gave cells 1-4 and 27, nonsense).
- groups whose image value gives no sense (1390 f.76r 389 for "seront" and 488 for "elle"; 1388 f.58r 84 "fer" for "mettre") - read: kept as written, the sense supplied and counted as a hole; checked: image, decode; the digits read 389, 488 and 84 on the image.
- doubtful table cells (`?` in `key/key274.json`; 656 illegible, set to q from the letters; 323 "pu" or "ju" unsettled) - read: 656 = q, 323 unread; checked: image (table crop), decode; 32 cells corrected in `key/overrides.json`, each with its reason.

Images: the LAC server answered by curl on 24 Nov 2026 (e000874976 fetched); the ANOM viewer was not needed. The other images were not re-compared in this review.

## Files

`transcription.txt`, `reading.md`, `gaps.json`, `key/key274.json`, `key/overrides.json`, `key/t274_part*.txt`, `tools/` (cell crops,
decode, stats), `WORKLOG.md`, `profile.json`; `cat1388/`, `cat1389/`, `cat1390/` for the April 1759 letters, each with `dudout/`, Brice Dudout's separate reading of that letter (PR #268, transcription, decryption, French reading, English translation; his table `cat1388/dudout/key.tsv` and its validation 0.972 against 0.185 for permuted keys, kept beside ours, not merged). Images are fetched, not stored (`img/`, `key/*.jpg`, `crops/` are git-ignored); fetch with
`curl -L "https://central.bac-lac.gc.ca/.item?id=e000875753&op=img&app=nf"` (ids e000875753-58 and e001295267-76).
Image credit: Library and Archives Canada (LAC) / Archives nationales d'outre-mer (ANOM), via New France Archives.

Count check, 14 Nov 2026 (settled): gaps.json keyed the "de moyen" gap as f150v.24, but `tools/lines.py` numbers that line f150v.23 (the file's 24th row of the folio counts a comment line), so `tools/stats.py` skipped its 2 groups and reported 24. With the key corrected to f150v.23 the tool gives 26 legible unread groups (1.1%) in the same 9 places, 2326 groups read as written and 2351 (97.0%) with the 25 restored ones. The word measure (1383 words, 100 holes, 0.933) is not changed by this: "de moyen" was already among its holes or is to be rechecked there (not recounted today).
