# French cipher in Canada, 1756-60: LAC copies and Montcalm's War code (code W)

> Exploratory record of 12 November 2026, kept as written. Paths under `sources/raw/` are the contributor's local download folders and are not in this repository; `reading_W_1756-1759.md` is `research_readings.md` here. Where this record differs from `../NOTES.md`, `../DIGIT_AUDIT.md` or `../KEY_SCOPE.md`, those files are current.

Built 12 Nov 2026 for Andrew Beling's Historical Ciphers project. Local only. I used curl only: no browser, no login,
nothing posted.
[V] = checked on a frame image, in a file or in tool output. [I] = inference.
Downloads are in `sources/raw/deep_2026-11-12/montcalm/` (see `SOURCES.txt`; 11,864 files hashed in `SHA256SUMS`,
about 1.4 GB).

## Main findings

1. **Library and Archives Canada's copies of the War archives are free on Canadiana Héritage, and they copy the
   cipher figures.**
   - MG4 B1 série A1 (SHD GR A1) is on reels C-12576 to C-12580. The MIKAN record is
     https://heritage.canadiana.ca/view/oocihm.lac_reel_c12576 ... c12580; the collection page is
     https://heritage.canadiana.ca/view/oocihm.lac_mikan_113037 [V].
   - These are handwritten copies. Where the original is in cipher, the copyist reproduced the figure groups together
     with the 18th-century interlinear decipherment, and added "sic pro NNN = ..." notes in the margin [V].
   - Frames download by curl through IIIF (`https://image-uab.canadiana.ca/iiif/2/69429%2F<id>/full/max/0/default.jpg`;
     the ids are in the reel page HTML) [V].
   - Volume map, read from the target slips:

     | reel | A1 volumes | covers |
     |---|---|---|
     | C-12577 | 3408-3417 | 1756 |
     | C-12578 | 3457 (frames 12-670), 3471-3494, then 3498 (frames 852 to the end) | 1757; Jan-May 1758 |
     | C-12579 | 3499 (frames 7-569), 3500-3539, 3540 (frames 785-1345), 3542 onward | 1758; 1759 |
     | C-12580 | starts at 3574 | 1760 |

     [V by slip OCR and by eye on samples]
   - MG1 F3 (Moreau de Saint-Méry) is on reels C-10523 to C-10533 (https://heritage.canadiana.ca/view/oocihm.lac_mikan_100163).
     Reel C-10523 holds "extraits des volumes 2, 14, 15 et 16" [V].

2. **Montcalm's War code ("code W") is the third code, and it can be rebuilt.**
   - It is a two-part (hatched) code. The values have no alphabetical order: 168 of 318 adjacent pairs are in order,
     against a shuffled median of 167 [V, inline Python test on `w_table_tokens_1757.tsv`, 2,000 shuffles]. It has many homophones (a = 257/641/832/880,
     de = 397/586, le = 509/697, s = 13?/83/301). Groups go up to at least 900.
   - Montcalm used it to the War minister in 1756 (d'Argenson), 1757 (Paulmy) and 1758 (Belle-Isle). Lévis used it
     in Nov 1759 [V].
   - The table built from the token-aligned 4 Nov 1757 copy has 320 groups: `w_table_tokens_1757.tsv` (reliable,
     1 group = 1 decipherer token). Adding the word-level pieces through a DP aligner gives about 430 groups:
     `w_table_all_aligned.tsv` and `w_alignments.txt`. The added values are less reliable, because neighbouring
     unknown groups can merge.
   - It is not code B and not code I (CMNF figures decode to nonsense with both, as found before) [V].

3. **CMNF IV p. 153.**
   - The 5 "unread" groups `583 878 110 103 83` read **peu-p-l-e-s = "peuples"**: the last word of the paragraph
     before the footnote ("...forts chez ces peuples"). Every value is attested at least twice in the 1757 copy.
     Confidence: high [V].
   - The 31-group footnote reads in part: "ma-l-[gré] nos succez la paix à [dési-rer] pour [?] qui do-it [être] pri-s
     ... la difficile[-té] ... fer pa-se-r de-s vivres & secours". 20 of 31 groups are attested. The cipher is shorter
     than the printed clear text. Details in `reading_W_1756-1759.md` §6.

4. **New text: the cipher paragraphs NYCD X omitted from Montcalm to Paulmy, 4 Nov 1757, and the annexed cipher
   sheet** (A1 3457 pièces 179-180).
   - The sheet is Montcalm's plan for defending Québec between the Montmorency falls and the St-Charles ("cet espace
     est de trois mille six cents toises").
   - The paragraphs cover the 1757-58 food crisis (horse meat "comme à Prague", the quarter-pound bread ration,
     Vaudreuil and Bigot asking him to write to the King) and Pontleroy's report on Louisbourg.
   - None of these phrases occurs in the OCR of NYCD X, Casgrain I-XII, Chapais or RAPQ 1920-42 [V]. The French text
     and an English translation are in `reading_W_1756-1759.md`.
   - These are the 18th-century decipherer's words as copied, not my decryption. I re-checked them against the
     groups: 89 C/F line pairs, all with matching counts once a "?" written without a group is dropped.

5. **Other cipher pieces found in the LAC copies** (each listed with frames in the table below), plus a fourth code
   (code D, Doreil's: de = 214/888, la = 121, l = 27) on two pieces. Code D is not analysed beyond the transcription.

6. **ANOM F3 15 f.194** (Montcalm to the Marine minister, "Camp de Carillon, 1er septembre 1758").
   - The LAC 1899 inventory (archive.org `cihm_97295`, p. 168) summarises it: "Paix nécessaire, ou Canada perdu ...
     La France devrait envoyer 2,000 hommes et 6 bataillons de recrues ... (Dépêche chiffrée traduite entre lignes.)
     Folio 194, 2 pages" [V, OCR]. So the original carries an interlinear decipherment.
   - LAC did not copy it. That entry has no "Soit N pp.", and reel C-10523's extracts from that volume cover only its
     pp. 338-343 (Bigot, 15 Oct 1759) and pp. 370-375 (Lévis, 10 Nov 1759) [V on the title frames 0315 and 0336;
     LAC labels it "Volume XIII (1757-1759)" in the old numbering].
   - The image is not reachable without ANOM.

7. **AN 155AP/2, images 1021 to the end:** no cipher. The Canada papers end at image 1959 (1960 onward is a 1767
   ship's journal). Pièce 25 (0816) remains the only cipher piece. A sub-agent did this survey; details in
   `an155ap2/notes.md`, sheets in `an155ap2/sheets/` [V there].

## Cipher pieces located (all free on Héritage)

| # | piece | code | reel, frames | decipherment in copy | transcribed |
|---|---|---|---|---|---|
| 1 | Montcalm to Paulmy, Québec 4 Nov 1757, A1 3457 p.179 + annexed sheet p.180 | W | C-12578, 0525-0526, 0530-0533, 0537-0538 | yes, syllable by syllable over each group | all, `transcriptions/W1757-11-04_...` |
| 2 | Montcalm to [Belle-Isle], Montréal 9 May 1758, A1 3498 p.80, and p.80bis "Quadriplicata" (cipher note on peace) | W | C-12578, 1022-1027 | yes, word by word | all, `W1758-05-09_...` |
| 3 | Montcalm to [Belle-Isle], Montréal 9 Sept 1758, A1 3499 p.65, cipher end | W | C-12579, 0172 | yes | all, `W1758-09-09_...` |
| 4 | Montcalm to [d'Argenson], Montréal 3 Nov 1756 (duplicata), A1 3417, cipher P.S. | W | C-12577, 0934 | yes (under the figures) | all, `W1756-11-03_...` |
| 5 | Lévis to the Marine minister, "Canada 10 9bre 1759", F3 [15] | W | C-10523, 0345-0359 (pp. 307-318; pp. 305/306, 313 and 318 filmed twice) | yes, word by word under the figures, drifting | p. 307 only, `W1759-11-10_Levis_F3_sample_p307.txt` |
| 6 | [Doreil] to [d'Argenson], 1756, A1 3417 copy pp. 715-716 | D | C-12577, 0869-0870 | yes (under) | all, `D1756_Doreil_...` |
| 7 | Doreil to [Crémille?], [late July] 1758, A1 3498 copy p. 472: one line; copyist says the cipher equals pièce 191 | D | C-12578, 1330 | yes | all, same file |
| 8 | Vaudreuil, 1760, F3 [16] extract pp. 331-332 | Vaudreuil's (not W) [I] | C-10523, 0372-0373 | not checked | no |

How I searched: Apple Vision OCR of every frame of C-12577, -12578, -12579, -12580 and C-10523 at 1200 px, then a
scan for lines made mostly of 1-3-digit groups (`scripts/figline_scan.py`). The hits were checked by eye; tables and
accounts were rejected [V]. Limits:
- A single short figure line can still be missed.
- No figure lines were found in the copies of A1 3540 (1759). The 12 Apr 1759 Montcalm letters (to Crémille,
  Belle-Isle, Le Normand) were not looked at individually. Their copies probably give the clear text only [I].
- Doreil's pièce 191 (31 July 1758) shows no figures in the copy [I, from the OCR scan only].
- I did not find the Feb 1758 memoir on the limits in the vol 3498 copy by OCR. This is not proof.
- C-12576 (A1 up to 1755) and C-10524 to C-10533 (other F3 volumes) were not surveyed.
- Neither nouvelle-france.org nor the C11A images were checked (time).

## What remains, ranked, and what would unblock it

1. **Transcribe the Lévis 10 Nov 1759 cipher** (C-10523 frames 0345-0359; full-size frames already in
   `sources/.../lac/full_c10523/`). It has about 1,400 groups with the decipherment, and would take code W to about
   600-700 groups. Unblocked; it only needs time. Align page by page (`scripts/walign.py`).
2. **Second-reader check** of the digits I marked "?":
   - 1757 p.506 "670"; p.511 "13"; p.517 "886?/486", "63?"; p.518 "215"
   - 1758 p.167 "13", "670"
   - 1756 "159"

   They should be checked on the IIIF max frames.
3. **ANOM COL F3 15 f.194-195** (Montcalm au ministre de la Marine, camp de Carillon, 1er septembre 1758, "dépêche
   chiffrée traduite entre lignes", 2 pages). Andrew's call:
   - in a browser, https://recherche-anom.culture.gouv.fr/ark:/61561/3072288 (Anubis bot check); or
   - an ANOM reproduction request for "FR ANOM COL F3 15, folios 194-195".

   It is probably code I (Marine) or code W [I]. Either way it carries its own decipherment, so it is a crib.
4. **SHD GR A1 3498: Montcalm to Paulmy, Montréal 23 Feb 1758, and the annexed "Mémoire ... sur les limites ... (en
   chiffre)"**. This would give the full figures of the memoir that CMNF IV printed only as leftovers. Two steps:
   - First page through C-12578 frames about 852-1021 by eye (unblocked).
   - If the copy gives the clear text only, Andrew could ask the SHD for: GR A1 3498, Montcalm's letters of 19 and
     23 Feb 1758 with the annexed memoir (the pièce numbers are not yet known).
5. **SHD GR A1 3540, Montcalm's letters of 12 Apr 1759** (to Belle-Isle, Crémille and Le Normand). Check the
   C-12579 copies (frames 785-1345) by eye first. If they give clear only, the originals need an SHD request for
   GR A1 3540, those pièces.
6. **Code D (Doreil, d'Argenson's code).** Doreil to Belle-Isle, 31 July 1758, is GR A1 3498 pièce 191 (NYCD X
   pp. 767-769 in clear). With the figures it would be a long crib. The copy (C-12578) is to be checked by eye. The
   original would need an SHD request.
7. **Verify the copies against the originals** (optional): GR A1 3457 pièces 179-180. The copyist's "sic" notes
   suggest he copied faithfully.

## Judgement calls

- The French readings in `reading_W_1756-1759.md` are the 18th-century decipherments as copied by LAC, re-read by
  me. They are not independent decryptions. I checked them group by group only for the 4 Nov 1757 letter, where the
  decipherer split the text per group.
- "Code W" is my label. It is the code of the "petit chiffre" Paulmy sent in 1757 (Casgrain III p.64) [I]. The 3 Nov
  1756 letter shows it was already in use in 1756 [V], so it may be the cipher Montcalm took to Canada from
  d'Argenson's office [I].
- On the CMNF footnote I did not force readings for the unattested groups (533, 314, 480, 108, 131, 611, 536, 655).
  The guesses shown in brackets are mine [I].
- The AN 155AP/2 survey (item 7 above) was done by a sub-agent. I have not re-viewed its sheets.

## Files

- `reading_W_1756-1759.md`: the readings (French and English) and the CMNF IV decoding.
- `transcriptions/`: transcriptions made by eye from the frames before any decoding, hashed in
  `transcriptions/SHA256SUMS` (written right after each file).
- `w_table_tokens_1757.tsv`, `w_table_all_aligned.tsv`, `w_alignments.txt`: the code W tables.
- `lac/`:
  - `ocr/` (Vision OCR of every frame)
  - `scan_*.tsv`, `figlines_*.tsv` (triage)
  - `sheets/`, `crops/`
- `an155ap2/`: the AN 155AP/2 survey.
- `scripts/` (run with `python3 -I`; Swift tools compiled into the scratchpad):
  - `reel_ids.py`, `fetch_frames.sh`, `fetch_reel.sh`, `retry_missing.sh`, `fetch_region.sh`
  - `lac_ocr.swift`, `ocr_worker.sh`, `ocr_scan.py`, `figline_scan.py`
  - `lac_sheet.sh`, `zoom.sh`
  - `wcode.py` (token table), `walign.py` (word-level aligner)
  - the sub-agent's `an_*` scripts
