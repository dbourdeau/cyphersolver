# Montcalm's 1758 court code ("code I"): the Marine ministry's deciphering table, sheet e001295272

Status: in progress (contribution folder only, no site page yet; Daniel is free to write, edit or replace one).

Contributed by Andrew Beling, with AI agents, 13-14 November 2026. All transcription and testing below was done by
our own AI agents. The follow-up of 14 Nov (settled cells) was checked in part: on 15 Nov 2026 a second AI agent of ours, not shown the conclusions, re-ran the figures (identical) and compared ten settled cells with the LAC image: five agree, five cannot be told apart at the image's 775 px (all five are cells the table marks only "image permits"); none disagrees.

## What this is, in one paragraph

Library and Archives Canada (LAC) image e001295272 is a copy of Archives nationales d'outre-mer (ANOM), COL C11E
volume 10, folio 288: a 700-cell numerical table. Its covering sheet, e001295271, reads "Canada 1758 / Chiffre avec
M. le Mis de Montcalm ... Déchiffrant". It is the French Marine ministry's **deciphering table for its 1758 cipher
with the marquis de Montcalm**. We call that cipher "code I" because Casgrain (Collection des manuscrits du maréchal
de Lévis, vol. III, 1890) prints four letters to Montcalm in it, marked "chiffre I". Decoded with this table alone,
the four letters give back 92-94% of Casgrain's printed clear text, against 13-30% for shuffled tables.

## What we add, and what we do not

- **Not new text.** The four letters were enciphered and deciphered at the time by the ministry's and Montcalm's
  clerks, and Casgrain printed them in figures with their clear text in 1890. We read nothing that was not read before.
- **What we add:** the identification of sheet e001295272 as the Montcalm 1758 table (the volume was known to hold a
  Montcalm table, but upstream had not said which sheet; see Prior work), a transcription of the table by two blind
  passes, and a blind test of it against the printed letters with a shuffled control. Against the code I values
  we had earlier aligned from Casgrain, the table supplies 407 entries we lacked (327 clear) and shows most of our
  64 "conflicts" to be faults of our aligner.
- **No other letter in this code was found** (see Search for more text). So the table opens no new plaintext yet.
- **Cells 1 to 20 are off the photograph.** The top edge of the sheet is cut on the LAC image (cells 1-10 absent,
  11-20 show only the feet of letters), and LAC serves nothing larger than 775 pixels wide.

## The table (key/)

- `table_e001295272.tsv`: the frozen table, 700 rows: cell, reading, status (clear 542 / doubtful 138 / illegible 20),
  alternatives, pass A, pass B, note. Frozen 13 Nov 2026 22:11 EST; sha256 in `FREEZE.txt` (begins d13fcfac).
- `passA.tsv`, `passB.tsv`: the two blind passes. Pass A read from cell 1 forward, pass B (a separate agent) from cell
  700 backward; each saw only its own crops of the image and none of our code files. They agree on 609 of 680 legible
  cells (89.6%); the 71 differences were settled on 6x crops and marked doubtful where they stayed uncertain.
- `corrections_post_freeze.tsv`: seven readings that the letters show to be wrong (428 va, 479 ces, 474 t, 210 vraie,
  604 croi, 621 si, 591 po), and a note on cell 623 (sheet "bau", where I4 has "Bougainville"). Listed after the
  comparison; **the frozen table was not altered** and no decode in this folder applies them.
- The system: a two-part ("hatched") code, numbers 1-700 in no order against the values; single letters, syllables,
  common words and a few names (le Canada, Sa Majesté, colonie, monsieur); proper names are mostly spelled out
  (Vaudreuil = va-u-d-re-u-il).

## Test plan and results

`TEST_PLAN.md` was written and frozen with the table (sha256 in `key/FREEZE.txt`) before any of our code files, the
letters or any Montcalm or Vaudreuil target was opened. It fixes the normalisation, five classes of agreement, a
control of 200 shuffled tables (`random.Random(1758 + k)`) and a decision rule.

| Compared with | Agreement | 200 shuffled tables | File |
|---|---|---|---|
| Our earlier code I table (aligned from Casgrain, 12 Nov) | 188 of 273 cells exact; 209 lenient | exact mean 0.49, max 3; p = 0.005 | `results/compare_codeI.tsv` |
| Bougainville's code B (our table) | 0 of 292 | mean 0.42, max 3 | `results/compare_codeB.tsv` |
| Montcalm's War code W (our `montcalm1757w`) | 0 of 238 | mean 0.35, max 3 | `results/compare_codeW.tsv` |
| Montcalm to Bougainville, 21 Nov 1758, code B (112 groups) | 0 exact, 1 near | mean 0.08 exact | `results/letter1758_with_sheet.txt` |

By the pre-set rule (exact agreement on at least half the cells and above every shuffle) the sheet is code I, and it
is neither code B nor code W.

**Casgrain's four letters, decoded with the table alone** (`decode_letters.py`, `results/letters_test.json`). This
measure (difflib similarity of the decode to Casgrain's clear text, letters only) was chosen **after** the test plan
was frozen, so it is not pre-registered; the shuffle control is the plan's.

| Letter | Groups | Not on the sheet | Similarity to Casgrain | Shuffled mean / max |
|---|---|---|---|---|
| I1 Massiac to Montcalm, Versailles, 26 Aug 1758 (Casgrain III no. LIV, pp. 122-123) | 230 | 2 | 0.938 | 0.155 / 0.257 |
| I2 Massiac to Montcalm, 23 Sep 1758, cipher end of a clear letter (LV, pp. 124-125) | 47 | 0 | 0.921 | 0.181 / 0.315 |
| I3 Massiac to Montcalm, 23 Sep 1758 (LVI, pp. 125-127) | 370 | 1 | 0.939 | 0.303 / 0.352 |
| I4 Belle-Isle to Montcalm, Versailles, 10 Feb 1759 (LXXII, pp. 161-164) | 660 | 12 | 0.935 | 0.127 / 0.219 |

No shuffled table reached the real score for any letter. I3's shuffled baseline is higher because Casgrain prints
some words in clear among its figures ("Le Canada", "jamais", "maréchal" ...), which count on both sides.
The statistical check of the repository (`docs/_validate.py`, `validation.tsv` = each group with its frozen-table
reading, 1292 read groups, model fr-1750-nospace) gives **pass**: the table's decode scores -2.130 per letter against
-3.164 for 200 random keys (z 11.4) and -2.212 for keys refitted to shuffled text (z 8.4); recorded in `profile.json`.

Files per letter in `letters/`: `<L>.tr` (Casgrain's figure lines F and clear lines C, checked on the page images,
12 Nov 2026), `<L>_groups.txt` (the figures), `<L>_casgrain_fr.txt` (his clear text), `<L>_decode.txt` (our
table-only decode: `x?` = doubtful cell, `[N?]` = group off the photograph or illegible, `{...}` = word printed in
clear), `<L>_en.txt` (our English translation of Casgrain's French).

Note on I4: it is from the War minister (Belle-Isle), not the Marine, yet it is in the same code. Casgrain's note gives
its key as "volume ... No. I". So the 1758 code was used by both ministries with Montcalm, at least by February 1759.

## Prior work and credits

- The letters: enciphered and deciphered by the clerks of the Marine and War ministries and of Montcalm (1758-59);
  printed with their clear text by H.-R. Casgrain, 1890.
- The volume: ANOM COL C11E 10 ff.285-290v, "Chiffre ou code de Montcalm et de Vaudreuil au cours des deux années 1757
  et 1758" (New France Archives record 15213), was pointed to as a key lead by the repository's own sweep
  (`research/canada_lac/README.md`, "Key leads"). Brice Dudout transcribed and validated the Vaudreuil table on sheet
  e001295274 (pull request #268, files in `targets/vaudreuil1759a/dudout/`), as did the repository's `vaudreuil1760`.
- Sheet 272 upstream, quoted exactly. `targets/vaudreuil1760/NOTES.md`: "The 10 images hold two tables for
  Vaudreuil/the Marine (1757, two sheets) and the Montcalm table (1758), each as an alphabetical list and a numerical
  list. The numerical sheet that decodes this letter is e001295274 (the second numerical sheet; the first, e001295272,
  does not fit)." `targets/vaudreuil1760/WORKLOG.md`: "Hypothesis 1: numerical table on sheet e001295272 (top of
  volume order). Looked up 235/661/642/653/674/471/309/51/107/163: nonsense ("question", "usage", "celle").
  Rejected." and "second sheet pair of C11E 10 (the 1758 Montcalm table) not compared with this letter."
  Its Escalation list: "both numerical sheets 272 and 274 of C11E 10 tried; 274 fits and reads the letter".
  Nobody upstream had said that 272 is the Montcalm table or transcribed it; this folder does not touch the Vaudreuil
  targets. A search of the repository's targets, research files, issues and pull requests (14 Nov 2026) for
  e001295272, "Déchiffrant", folio 288 and Montcalm's 1758 code found nothing else.
- Our own earlier work: the code I values aligned from Casgrain (12 Nov 2026, not in this repository) and our
  pull request #574 (`montcalm1757w`, the War code W).

## Search for more text in this code (13-14 Nov 2026, about two agent-hours)

Paged or searched, with result:

- **New France Archives** (nouvelle-france.org, LAC/ANOM item records with images) searched for Montcalm, Massiac,
  Berryer, Moras and "chiffr"; ANOM COL C11A 103-104 records listed by folio. The only cipher letters of 1758-59 are
  Vaudreuil's (catalogue 1388-1391) and Trémais's (1392). Montcalm to the minister, Carillon, 3 Aug 1758 (C11A 103
  ff.142-143, LAC e000874148-49) is in clear.
- **C11A 104 ff.157-166** (LAC e000875059-68): copies of Montcalm to Belle-Isle and to Le Normant de Mézy (first
  clerk of the Marine), Montréal, 12 Apr 1759. The second ends: "S.S. J'ay l'honneur Monsieur de joindre a cette
  lettre un état exact des troupes que les Anglois ont dans cette partie, et une observation particulière que j'ay
  cru devoir vous mettre en chiffre en me servant de celuy que Mons. de Moras m'a envoyé l'année dernière." That is a
  Montcalm letter in **this** code (the Marine cipher of 1758). The cipher sheet is not in the copy, and no image
  follows f.166 (LAC has no record e000875069; ff.167 and 215-260 have no item description). Not found.
- **ANOM COL F3 15, folio 194** (Moreau de Saint-Méry collection), described in Édouard Richard's inventory
  (Supplément du rapport ... sur les Archives canadiennes, 1899, archive.org `cihm_97295`): "M. de Montcalm au
  ministre. La situation de la colonie est des plus critiques. Paix nécessaire, ou Canada perdu ... La France devrait
  envoyer 2,000 hommes ... (Dépêche chiffrée traduite entre lignes.) Folio 194, 2 pages", dated in the margin, as far
  as the OCR layout shows, Camp de Carillon, 1 September 1758. ANOM's finding aid calls it "Lettre chiffrée de Montcalm
  au ministre réclamant deux mille hommes ou la paix". **This is the best candidate**: Montcalm to the Marine minister
  in figures, with a period decipherment between the lines. (Corrected 14 Nov 2026: the F3 reels on Héritage
  Canadiana, C-10523 to C-10533, are LAC's handwritten transcripts of F3 in volume order, and the clear text of this
  letter is on reel C-10528; see "Known plaintext of a second letter" below. The figures are not in the transcript.)
- **New York Colonial Documents vol. 10** (archive.org `documentsrelativ10brod`): Montcalm to Belle-Isle, Montréal,
  12 Apr 1759, "This despatch was in cipher" (from the War archives, now Service historique de la Défense, A1). Given
  I4, it may be in code I; the original is not online.
- **Trémais to the minister, 22 Sep 1759** (C11A 104 f.342, LAC e000875266): written with stacked, fraction-like
  groups, a different system; the five groups quoted in `vaudreuil1760/WORKLOG.md` give "prompt escorte France qu'il
  tion" on this table. Not code I. (Brice Dudout is working this lead.)
- **Casgrain**: vols. I-XII were searched on 12 Nov 2026 for figure groups; only the six letters of vol. III print
  them. The Rapport de l'Archiviste de la Province de Québec was not searched.
- Upstream targets from Canada 1757-60 other than the Vaudreuil letters: none in the repository holds open groups.

## Integration check (14 Nov 2026)

Checked when pull request #583 was integrated (round 13).

- Freeze: the four sha256 values in `key/FREEZE.txt` match the files in the folder. That the table and plan were frozen
  before any comparison is by the contributor's record (one commit, no outside timestamp).
- `decode_letters.py` re-run: the four similarities (0.938, 0.921, 0.939, 0.935) and every shuffle figure come out the
  same. An own decoder written from the frozen table gives the same four `_decode.txt` files.
- Strict word count, table alone. A word of Casgrain's clear text counts only when every letter of it comes out of cells
  the table marks clear: I1 82 of 122 words (67.2%), I2 23 of 31 (74.2%), I3 169 of 233 (72.5%), I4 265 of 371 (71.4%).
  With the doubtful cells counted too: 79.5%, 83.9%, 82.0%, 82.7%. The contributor's 92 to 94% is a letter-level
  similarity, a different and looser measure. So the table alone does not read a letter; the text is Casgrain's.
- Image: the LAC file of e001295272 has the recorded sha256. 80 cells (301-394 and 401-494, first four columns) were
  read on it at five times enlargement: 71 agree with the table. Of the 9 differences, 8 fall on cells the table already
  marks doubtful (474 read "t", which is the contributor's own post-freeze correction), 1 on a cell marked clear
  (492, "contraire" in the table, "connoitre" possible). At 775 pixels neither reading of 492 is safe.
- Outcome method set to "read from existing decipherment": all four letters were printed in clear by Casgrain in 1890
  and nothing is read here that was not in print. Matching the archive table to them is kept as a part of the outcome
  (`outcome.parts`, "read after matching with key from external sources", partial).
- One key, one entry: code I is not code W (`results/compare_codeW.tsv`, 0 of 238) and not the Vaudreuil table of
  `targets/vaudreuil1760` (sheet 274; that target tried sheet 272 on its letter and rejected it). Three codes, three
  folders. This folder and `targets/montcalm1757w` point to each other.
- Not rechecked: the comparisons with the contributor's earlier code I and code B tables (those tables are not in the
  folder, only the result files), Casgrain's figures against the page images, the searches for more text.

The gaps are workable from here only in part: the doubtful cells can be settled from the four letters (the seven
post-freeze corrections show how), so the folder stays `Status: in progress` and has no page.

## Cells settled from Casgrain's text (14 Nov 2026, follow-up to #583)

Done as Daniel suggested on #583: a separate, labelled table, `key/table_settled_from_casgrain.tsv`. **The frozen
table is not changed** (its sha256 still matches `key/FREEZE.txt`), and the settled values are read from the same four
letters they are then measured on, so the "after" figures below are circular: they show how far the sheet plus
Casgrain's clear text account for his figures, not an independent test of the sheet. Work by our own AI agent;
on 15 Nov 2026 a second AI agent of ours, not shown the conclusions, re-ran the figures (identical) and compared ten settled cells with the LAC image: five agree, five cannot be told apart at the image's 775 px (all five are cells the table marks only "image permits"); none disagrees.

How. `settle_from_casgrain.py` aligns, letter by letter, Casgrain's printed figures (`letters/*.tr`) with his printed
clear text by dynamic programming (a clear cell must match its reading or pay per edit; a doubtful, illegible or
off-photograph cell may take any 1-10 letter stretch at a cost; skipped text letters cost). Every occurrence of every
cell that is doubtful, illegible, off the photograph, in `key/corrections_post_freeze.tsv`, or clear but aligned with
other text is listed in `results/casgrain_implied_values.tsv` (336 occurrences, with context). Each value was then
checked by hand against the context, and each cell was looked at again on the LAC image (sha256 ac16ca78...,
775 px, enlarged crops of the passes' band images).

Result: 69 cells.

| Status | Cells | Which |
|---|---|---|
| confirmed on image | 34 | the doubtful reading is what the letters need and the image shows it (35 em, 42 nu, 55 ro, 73 at, 75 voi, 82 peine, 147 che, 196 eux, 234 etre, 247 y, 261 sou, 281 nt, 284 ex, 313 p, 329 n, 361 isle, 381 l, 410 tre, 442 r, 448 lui, 489 deffen, 494 ont, 495 ite, 512 ti, 558 hi, 592 trou, 618 tout, 645 ne, 652 ve, 674 oc, 681 ils, 687 suite, 690 te), and 604 croi (frozen "envi") |
| image permits | 23 | the letters need another value and the image allows it: 102 oit, 210 vrai, 220 su, 290 gi, 312 sen, 352 tant, 388 i, 407 tien, 428 va, 430 sa, 444 aussi, 452 lettre, 474 t, 479 ces, 536 ha, 621 si, 623 bou, 638 oient, 663 ri, 672 si→fi, 695 ressource; and two cells marked clear that the letters show misread: 564 er→cr (2 occurrences), 688 eu→cu (6) |
| image contradicts | 4 | 355 (image honteuse/honte; letters need homme), 437 (image a six-letter word read combie; letters need comm, four times), 591 (image lors; letters need po; 571 = po, so Casgrain's or the clerk's 591 may be a slip), 151 (clear "penible"; letters need possib in "impossibilité") |
| off the photograph | 8 | values for cells 1-20 from the letters only: 2 necessaire, 10 operation, 11 go, 12 facheux, 16 na, 17 vie, 18 ac, 19 avi |

Of the seven post-freeze corrections, six are settled as listed there (428 va, 479 ces, 474 t, 604 croi, 621 si, 591
po, the last contradicted by the image); for 210 the letters give "vrai" (cell 160 = e follows), not "vraie".

Not counted as misread cells: spelling conventions of the code (133 v and 617 v used for u, 414 j for i, 457 s for z,
589 Roy for roi, 507 envoy, 489 deffen) and clear cells the encipherer used for part of their value (99 circonstance,
68 jour, 293 volonte, 440 prompt, 483 rempli, 580 vers, 631 terre, 646 effet: "al-terre-ca-tion", "rempli-or-te-r").
Figure slips, where a neighbouring number on the sheet has the needed value: 677 loi for 678 ennemi (I1 "ses
ennemis"), 548 négociant for 584 je (I2), 352 for 252 tant, 591 for 571 po, 320 coup for 220 su (I1 "de suite"; I4
uses 320 as "cou" in "recouvrer"). Whether the slip is Casgrain's printer's or the 1758 clerk's cannot be told
without the originals.

Measures, before and after (`results/settled_measures.json`). The whole-word measure is Daniel's: a word of
Casgrain's clear text (split on spaces) counts only when every letter of it is matched, in the alignment of decode and
text, by letters from cells counted as clear. Our re-implementation gives exactly his frozen figures. "After" puts in
the settled values with status confirmed or permits, counted as clear; cells the image contradicts stay as frozen.

| Letter | Words | Whole words, frozen clear cells | with doubtful cells | Whole words, after settling | Letter similarity before / after |
|---|---|---|---|---|---|
| I1 | 122 | 82 (67.2%) | 97 (79.5%) | 112 (91.8%) | 0.938 / 0.973 |
| I2 | 31 | 23 (74.2%) | 26 (83.9%) | 28 (90.3%) | 0.921 / 0.937 |
| I3 | 233 | 169 (72.5%) | 191 (82.0%) | 213 (91.4%) | 0.939 / 0.974 |
| I4 | 371 | 265 (71.4%) | 307 (82.7%) | 334 (90.0%) | 0.935 / 0.961 |

With the four contradicted cells also put in: 93.4, 90.3, 91.8 and 94.1% of words. The letter similarity is the
difflib ratio of `decode_letters.py`, a looser measure, labelled as such. The remaining word losses are mostly the
slips above, the loose uses of clear cells, and words Casgrain prints in modern spelling (étoit for estoit).

## Known plaintext of a second letter in this code (cipher unseen)

Montcalm to the minister (Marine), Camp de Carillon, 1 September 1758: ANOM, Colonies F3 (Moreau de Saint-Méry
collection) volume 15, folio 194 (duplicate), marked "Lettre chiffrée". The original, in figures with the decipherment
between the lines (Richard 1899: "Dépêche chiffrée traduite entre lignes"), is at ANOM and not digitised. The clear
text survives in Library and Archives Canada's handwritten transcript of F3 15, pages 224-225, on Héritage Canadiana
reel C-10528, frames 1188-1189 (frame 1190 is a second exposure of page 225; frame 1191, page 226, is folio 204, a
different document): https://heritage.canadiana.ca/view/oocihm.lac_reel_c10528/1188 . The transcriber copied only the
decipherment; there are no figures. Transcribed by our AI agent from the frame images (1600 px), 14 Nov 2026,
keeping the transcript's spelling:

> [margin: Duplicata 194. B/que(?) Canada] Au Camp de Carillon le prem[ie]r 7bre [septembre struck through] 1758.
> M. De Montcalm. Monseigneur, [margin: Lettre chiffrée]
> La situation de la Colonie des plus critiques: La paix nécessaire. Les anglois ont eu, indépendament de leur armée
> pour Louisbourg, trente mille hommes pour agir en Canada.
> Nous n'avons que huit bataillons, douze cent soldats de la Colonie, le surplus dans les forts ou la Belle Rivière.
> Les Canadiens pourroient fournir trois mille hommes toute la campagne, cependant nous n'en avons eu cette année que
> douze cent en campagne. On en a mis un plus grand nombre, mais seulement pour un mois. Les Canadiens bons pour des
> courses ne sçavent pas rester cinq mois en campagne, les Sauvages encore plus.
> J'écris la verité comme citoyen, sans être découragé, résolu de m'ensevelir sous les ruines de la Colonie. Il
> faudroit que la France put envoyer deux mille hommes de recrüe et six bataillons.
> Peut-elle les envoyer et des recrües de la bonne espece.
> [margin: 194v] Donc la paix nécessaire ou le Canada perdu; nos forces trop inférieures à celles des Anglois pour
> resister à trois attaques. J'aprends dans le moment qu'ils sont à Frontenac. Il y a longtems que je le craignois.
> La Colonie sera coupée en deux.
> Je suis avec respect, Monseigneur, Votre très humble et très obeissant serviteur. Montcalm.
> [note: Signature autographe. 195 en blanc. 196-203 copiés au Supplément pp. 119-127.]

English (ours): "The situation of the colony most critical: peace necessary. The English have had, besides their army
for Louisbourg, thirty thousand men to act in Canada. We have only eight battalions and twelve hundred colonial
soldiers, the rest in the forts or on the Belle Rivière [the Ohio]. The Canadians could provide three thousand men for
the whole campaign, yet this year we have had only twelve hundred in the field. A larger number was called out, but
only for a month. The Canadians, good for raids, cannot stay five months in the field; the Indians still less. I write
the truth as a citizen, not discouraged, resolved to bury myself under the ruins of the colony. France would have to
send two thousand recruits and six battalions. Can she send them, and recruits of the right sort? So: peace necessary,
or Canada lost; our forces are too inferior to the English to resist three attacks. I learn at this moment that they
are at Frontenac. I have long feared it. The colony will be cut in two. I am with respect ... Montcalm."

The enciphered body is 186 words, 874 letters; at the rate of Casgrain's letters (about 2.7 letters a group) that is
some 320 groups. Nothing here is encoded or decoded: the cipher is unseen. Whether this letter is in code I is not
known; it is likely (Montcalm writes on 12 Apr 1759 that he enciphers to the Marine "en me servant de celuy que Mons. de
Moras m'a envoyé l'année dernière"), but not shown. What a scan of the original (ANOM reading room or reproduction
service) would allow: (1) whether the figures are code I at all, by decoding them with the frozen table and comparing
with this text, a test on a text the table has never seen, unlike Casgrain's four; (2) settling more of the 138
doubtful cells and cells 1-20 from a second, independent text; (3) a check on the period decipherment between the
lines against this later transcript.

ANOM checked again, 14 Nov 2026, in the built-in browser (its bot check passed by itself): the free search of the
finding aids returns 4 records for "Montcalm" (none in F3) and nothing for "COL F3 15"; F3 is not in its online
inventories or its "Autres fonds numérisés". FranceArchives (record 03740afc...) still describes F3 15 as not
digitised. So the cipher of f.194 is not online.

## Remaining gaps

- Cells 1-20 of the table: off the LAC photograph. blocker: needs-physical-access (ANOM COL C11E 10 f.288).
- 138 doubtful cells, chiefly short syllables, at 775 pixels. The 57 doubtful cells the four letters use are settled in
  `key/table_settled_from_casgrain.tsv` (14 Nov 2026); four values the letters need are contradicted by the image
  (151, 355, 437, 591). blocker: needs-physical-access (a better image) for the doubtful cells the letters never use.
- No second text in the code read: the clear text of F3 15 f.194 (1 Sep 1758) is now transcribed above, but its
  figures, and the 12 Apr 1759 cipher piece, are not online. blocker: needs-physical-access (ANOM scan of COL F3 15
  f.194).

## Sources

See `sources.md`.
