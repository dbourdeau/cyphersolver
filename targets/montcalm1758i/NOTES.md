# Montcalm's 1758 court code ("code I"): the Marine ministry's deciphering table, sheet e001295272

Status: in progress (contribution folder only, no site page yet; Daniel is free to write, edit or replace one).

Contributed by Andrew Beling, with AI agents, 13-14 November 2026. All transcription and testing below was done by
our own AI agents; it has **not** been rechecked by a second, uninvolved agent.

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
  in figures, with a period decipherment between the lines. Not seen: the F3 reels on Héritage Canadiana (C-10523 to
  C-10533) film only the volumes LAC did not transcribe (vol. 50 onward); ANOM's own search sits behind a bot check;
  the LAC transcript of vol. 15 is not online as far as we found.
- **New York Colonial Documents vol. 10** (archive.org `documentsrelativ10brod`): Montcalm to Belle-Isle, Montréal,
  12 Apr 1759, "This despatch was in cipher" (from the War archives, now Service historique de la Défense, A1). Given
  I4, it may be in code I; the original is not online.
- **Trémais to the minister, 22 Sep 1759** (C11A 104 f.342, LAC e000875266): written with stacked, fraction-like
  groups, a different system; the five groups quoted in `vaudreuil1760/WORKLOG.md` give "prompt escorte France qu'il
  tion" on this table. Not code I. (Brice Dudout is working this lead.)
- **Casgrain**: vols. I-XII were searched on 12 Nov 2026 for figure groups; only the six letters of vol. III print
  them. The Rapport de l'Archiviste de la Province de Québec was not searched.
- Upstream targets from Canada 1757-60 other than the Vaudreuil letters: none in the repository holds open groups.

## Remaining gaps

- Cells 1-20 of the table: off the LAC photograph. blocker: needs-physical-access (ANOM COL C11E 10 f.288).
- 138 doubtful cells, chiefly short syllables, at 775 pixels. blocker: needs-physical-access (a better image).
- No second text in the code read: the F3 15 f.194 and 12 Apr 1759 cipher pieces are not online. blocker:
  needs-physical-access.

## Sources

See `sources.md`.
