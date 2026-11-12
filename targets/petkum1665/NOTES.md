# Petkum 1665-66 and Paulmyer 1664: unglossed letters in the Danish chancery's French syllabary, read with a key rebuilt from the chancery's own glosses (catalogue 2530; issues #443, #444)

Status: in progress (integration check, 12 Nov 2026: every letter is read in part, none reaches 95%; not written up yet because the gaps below that are not-attempted can still be worked, see Integration check). Key rebuilt from the interlinear decipherments of sister leaves (no key sheet). Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic); issues #443 and #444 and the comments on them. Folder prepared 12 Nov 2026 in answer to the maintainer's note on both issues ("held, not rejected: the issue gives the results but not the files").

## What this folder is, and why one folder

Simon de Petkum, Danish resident in England, wrote to the German Chancery secretary Conrad Biermann (and twice to Frederik III) in French, with passages in a number-and-sign code. The chancery deciphered most of these letters between the lines when they arrived; the letters here are the ones the film shows bare. Jean de Paulmyer, Hannibal Sehested's correspondent in Paris, wrote in 1664 in the same code (his glossed leaves in the same unit agree with it, `gloss/paulmyer_gloss_checks.tsv`). One key was built from the Petkum glosses and frozen; it was then applied unchanged to every letter below. The Petkum and Paulmyer letters are in one folder because they rest on that one key file and one set of scripts and controls; a second folder would duplicate them. They are kept apart in every table, count and pool, and the Paulmyer letters have their own part in `profile.json` (`outcome.parts`), so that either can be judged alone.

## The documents

Rigsarkivet (Copenhagen), Tyske Kancelli, Udenrigske Afdeling (TKUA), Speciel del. Images: Arkivalieronline, `https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=<epid>#<unit>,<image id>`.

| id | letter | archive reference and images | in |
|---|---|---|---|
| petkum_1665-11-30 | Petkum to Biermann, Oxford, 30 Nov 1665 | England A III 52 (Gesandtskabsrelationer fra Simon de Petkum 1653-66), epid 19852633, unit 261267, images 572 right (p.1, image id 48873119), 573 (pp.2-3, 48873120), 574 left (p.4, 48873121) | #443 |
| petkum_1665-03-24 | Petkum to Biermann, London, 24 Mar 1665 | same unit, image 416 right (48872963) | #444 |
| petkum_1665-11-23 | Petkum to Biermann, Oxford, 23 Nov 1665 | images 568 right, 569 right (48873115-16) | #444 |
| petkum_1665-12-10 | Petkum to Biermann, Oxford, 10 Dec 1665 | images 576 right, 577 right (48873123-24) | #444 |
| petkum_1666-04-13 | Petkum to Biermann, London, 13 Apr 1666 | images 641 left, 642 (48873188-89) | #444 |
| petkum_1665-04-28 | Petkum, London, 28 Apr 1665 | image 435 right | comment on #444 |
| petkum_1665-06-23 | Petkum, London, 23 Jun 1665 | image 473 right | comment on #444 |
| petkum_1665-09-17 | Petkum, Salisbury, 17 Sep 1665 | image 528 right (third page) | comment on #444 |
| petkum_1666-01-18 | Petkum, Oxford, 18 Jan 1666 | image 597 right | comment on #444 |
| petkum_1666-04-06 | Petkum to Frederik III ("Sire"), London, 6 Apr 1666 | image 634 right | comment on #444 |
| paulmyer_1664-04-25 | Paulmyer to Hannibal Sehested ("Vostre Excellence"), Paris, 25 Apr 1664 | Frankrig, Gesandtskabsrelationer: Hannibal Sehested og Jean de Paulmyer 1662-65, epid 19852643, unit 261294, image 147 left (48879496) | comment on #444 |
| paulmyer_1664-05-02 | Paulmyer, Paris, 2 May 1664 | same unit, images 148 right, 149 (48879497-98) | comment on #444 (key support only) |
| paulmyer_1664-05-16 | Paulmyer, Paris, 16 May 1664 | images 151 right, 152 | comment on #444 (key support only) |
| paulmyer_1664-06-19 | Paulmyer, Fontainebleau, 19 Jun 1664 | images 159 right, 160 | comment on #444 (key support only) |

The leaf survey that pointed to these units is the repository's TKUA sweep of 11 Nov 2026 (credit in `profile.json`).

## The system

French. Three layers inside one word, with clear French around them:

1. Letters by number, in alphabetical order: a 14, b 15, c 16, d 17, e 18 ... z 37 (with k, without j and w); 38 and 100 = et.
2. A second set of letter signs: ct = a, looped ll = e, b = i, x = l, psi = n, beta = r, m-with-tail = s, crossed q = t, lambda = u, small T = y, y = c, g = p, theta = m, # = o, p-like = f, u4-like = x, barred h = z. Sign names as used in the files: `key.tsv` and the head of each transcription.
3. Syllables in rows of five (a e i o u) on consecutive numbers: b 170-174, c 182-186, d 200-204, f 217-221, g 229-233, l 266-270, m 276-280, n 298-302, p 316-320, qu 334-337, r 339-343, s 352-356, t 364-368, v 380-384 (h and j rows have one glossed value each).
4. Code numbers for names, titles and frequent words (51 le Roy de Danemark, 61 le Roy T.C., 92 le Roy d'Angleterre, 107 Mrs les Estats, 116 la France, 119 l'Angleterre, 120 la Suede, 152 Suedois, 153 Anglois, 165 Ambassade(ur), 222 faire, 288 majeste ...). 35 code numbers met in these letters have no value (`holes.md` 2).

## The key and how it was obtained (`gloss/README.md`)

- v1 (`gloss/KEY_v1_gloss_377_401.tsv`): values read under the chancery's glosses on images 377 (27 Jan 1665) and 401 of the Petkum unit; the row rule fixed from them. Frozen 01:29:32 UTC, before the first bare page (573) was decoded.
- v2: v1 plus 17 values from the glosses on image 574 right (U4 = x, HB = z and code words); frozen 01:35:14 UTC, before pages 1 and 4 of the 30 Nov letter were transcribed (they are the held-out test).
- Check of the row rule: 17 values that the rule had predicted before 574 right was read were then met under its glosses; 17 agree, 0 contradict (`gloss/rowrule_check_574R.tsv`).
- v3 = `key.tsv` (md5 ddc02e4a9408e8ead7d51b5135a1ae82): v2 with one correction made after decoding: code 51 is le Roy de Danemark (V. M.), not la France (our misreading of the 401 gloss). Code words count as not read, so no count changed. Every letter in this folder except the first decode of 30 Nov was decoded once with this file, unchanged; each transcription was frozen (md5 in our log) before its decode.
- Tiers in `key.tsv`: 84 A (gloss), 17 A2 (glosses on 574 right), 46 B (row rule), 8 C (row with one anchor; counted N). The decoder prints A2 values as `(x?)`: a display quirk of the contributor's script, kept so that the decryptions stay byte-identical to the stamped ones.

## The counting rule and the counts of record (`counts.txt`, `scripts/count.py`)

One rule for every letter: a unit is a word of the plaintext as the reader divided it. S = every token of the word has a spelled value (letter or syllable, tier A or B) and the word reads as French as written. E = the word is or contains a code word, even when the chancery glossed it. N = any token without a value, marked unsure (~), of tier C, or a spelling that does not read. Strict share = S / (S + E + N). S+E is shown for information and is not a share read. Code words are thus never counted as read; the strict share is a floor for what the decryptions say.

Where the labels come from: for the 30 Nov letter (first transcription) and the four Paulmyer letters, the reader's labels made at the first decode (`units/*.units.tsv`), counted as they stand; for the other nine Petkum letters, labels computed by `scripts/count.py` from the reader's word division (`units/*.seg`) and `key.tsv`, with the flattened tokens asserted equal to the frozen transcription. The blind reader's five letters use the first reader's word division mapped onto the blind tokens. The 30 Nov R2 count is the R1 labels with 23 listed relabels (blind reading adjudicated on crops, and the values KEY_v3 has that key v1 lacked), applied and asserted by the script.

Every figure below was produced by running `scripts/count.py` on the files of this folder (`python3 -I`, 12 Nov 2026) and is the same as the figure we filed. Arithmetic: `counts.txt`.

| letters | filed | reproduced here | S + E + N |
|---|---|---|---|
| 30 Nov 1665, R1 p.2-3 (key v1) | 162/238 = 68.07% | 162/238 = 68.07% | 162 + 26 + 50 = 238 |
| 30 Nov 1665, R1 pp.1, 4 held out (key v2) | 50/74 = 67.57% | 50/74 = 67.57% | 50 + 11 + 13 = 74 |
| 30 Nov 1665, R1 pooled (#443) | 212/312 = 67.95% | 212/312 = 67.95% | 212 + 37 + 63 = 312 |
| 30 Nov 1665, blind R2 adjudicated, KEY_v3 (comment on #443) | 220/312 = 70.51% | 220/312 = 70.51% | 220 + 51 + 41 = 312 |
| 24 Mar 1665 | 40/58 | 40/58 = 68.97% | 40 + 5 + 13 |
| 23 Nov 1665 | 68/96 | 68/96 = 70.83% | 68 + 15 + 13 |
| 10 Dec 1665 | 51/75 | 51/75 = 68.00% | 51 + 13 + 11 |
| 13 Apr 1666 | 59/94 | 59/94 = 62.77% | 59 + 16 + 19 |
| four letters pooled (#444) | 218/323 = 67.49% | 218/323 = 67.49% | 218 + 49 + 56 = 323 |
| five letters, first reader, pooled (comment) | 103/157 = 65.61% | 103/157 = 65.61% | 103 + 21 + 33 = 157 |
| the same five, blind reader, ~ as N (comment) | 100/157 = 63.69% | 100/157 = 63.69% | 100 + 21 + 36 = 157 |
| the same five, blind reader, ~ ignored (comment) | 104/157 = 66.24% | 104/157 = 66.24% | 104 + 21 + 32 = 157 |
| Paulmyer 25 Apr 1664 (comment) | 21/27 = 77.78% | 21/27 = 77.78% | 21 + 2 + 4 = 27 |
| Paulmyer 2 May, 16 May, 19 Jun 1664 | 23/36, 25/44, 25/44 | 23/36 = 63.89%, 25/44 = 56.82%, 25/44 = 56.82% | 73 + 20 + 31 = 124 (58.87%) |
| Paulmyer, all four pooled | 94/151 = 62.25% | 94/151 = 62.25% | 94 + 22 + 35 = 151 |

Per letter for the five: 28 Apr 19/26 = 73.08%, 23 Jun 18/29 = 62.07%, 17 Sep 16/26 = 61.54%, 18 Jan 36/50 = 72.00%, 6 Apr 14/26 = 53.85% (first reader); blind 18/26, 18/29, 17/26, 33/50, 14/26.

Not filed before, computed here from the same files: the eleven letters filed as read in part, each at its count of record (30 Nov R2, the four, the five by the first reader, Paulmyer 25 Apr), pool 562/819 = 68.62% (220 + 218 + 103 + 21 = 562; 312 + 323 + 157 + 27 = 819); with the blind reader's five, 559/819 = 68.25%. No letter reaches the 95% read bar.

## Controls

**Shuffled keys** (`controls.txt`, `scripts/shuffle_control.py`): the spelled values used in a text are shuffled among their tokens 5,000 times per seed and each decode is scored with a French character 4-gram model (Project Gutenberg 4650, 13951, 17489, 5097; the script refuses a corpus file whose header does not say French, or that is short). Code words and unknown tokens are never scored. Seeds 20261112 and 7, every letter and every pool above: 0 of 5,000 at or above the true score in 41 of 42 runs. **The exception is new and is ours to report: 28 Apr 1665 alone, seed 7: 1 of 5,000 (true -3.6403, best shuffle -3.6087).** With seed 20261112, as filed, it is 0 of 5,000 (best -3.6524). It has 36 scored tokens, and with seed 20261112 its best shuffle was already close to the true score; the pool of five that holds it is 0 of 5,000 on both seeds (true -3.6209; best -4.0960 and -4.1557). Every filed seed-20261112 figure is reproduced to four decimals, true and best, e.g. 30 Nov p.2-3 true -3.4264, best -4.1016 (seed 7 best -4.1421, as filed); R2 all pages true -3.3907, best -4.1776; Paulmyer 25 Apr true -2.5705, best -3.4029 and -3.4811. A first scoring of 30 Nov, which let code-word values count as text, gave 1 of 5,000 and was replaced before filing; it is recorded in our log, not used.

**Blind second transcriptions** (`agreement.txt`, `scripts/compare_blind.py`): 30 Nov 1665, R2 made from the images before R1 was opened: 721/726 tokens = 99.31% agree (5 substitutions, 0 insertions or deletions). The five letters of the comment: 383/387 = 98.97% (4 substitutions). The blind reader of the five had seen the first reader's tallies and one token string by accident before starting (not the transcriptions); this was disclosed on #444. The four letters of #444 and all four Paulmyer letters have one reader only.

**Key from elsewhere**: the row rule predicted 17 values before the 574 right glosses were read; 17 agree. Paulmyer's glossed leaves agree with KEY_v3 wherever it has a value (11 values on leaf 179 and the names on 164R, 167R, 168L).

## What the letters say (`readings/`, French with holes and English)

- 30 Nov 1665: with the French ambassadors recalled, Petkum expects a [break] between France and England; England has no friend but the Bishop of Munster; one defeat could raise the malcontents, chiefly the Scots; he asks to be withdrawn in good time if Denmark binds itself to France against England.
- 24 Mar 1665: no need to rush; England's malcontents have no leader; the [king] is armed.
- 23 Nov 1665: spread a false [rumour] of a levy of five or six thousand [men] to get better terms: "Mundus vult decipi".
- 10 Dec 1665: Frederik III has resolved to break with the States General by arresting their ships in Norway; Sweden will pass the treaty of Clifford to the Dutch and the French.
- 13 Apr 1666: Louis XIV wishes to see Petkum; Coventry and the Swedes are feeding Juel false reports.
- 28 Apr, 23 Jun, 17 Sep 1665, 18 Jan, 6 Apr 1666: the English treaty terms; a Swedish-English [treaty]; the Swedes' design on Bremen; the recall of Clifford and Talbot; the States' [346] and leave-taking of the King of England.
- Paulmyer, 25 Apr 1664: Mademoiselle de Montpensier despairs of the [match] of Savoy because the King refuses consent. The sister letters (Terlon and Courtin, the Thudesquin affair, Turin) are excerpts only.

## Corrections to our issues and comments

1. Paulmyer's passage on image 147 left was filed as of 2 May 1664. It ends the letter of 25 Apr 1664 (147 right opens the 2 May letter, whose first line refers to his letter of the 25th). Corrected on #444 the same day; this folder uses 25 Apr. The frozen transcription keeps its first header line.
2. The 30 Nov letter: #443 gave 212/312 (R1, keys v1/v2). The count with the blind R2 adjudicated and KEY_v3 is 220/312; both are given, and the reading file is the one written at the first decode (values that the later glosses supplied stand there as [?guesses]; `units/petkum_1665-11-30_R2.units.tsv` lists each change).
3. The five letters of the comment: the filed pool, 103/157 = 65.61%, rests on one reader and stands one unit above our 65% filing line. The blind reader gives 100/157 = 63.69% (unsure marks as N). Our own reopening condition for that comment was a blind count below 65%; it is met. We do not rely on the margin, and the five are offered as read in part on the readings, not as a pool above a threshold.
4. New here: the shuffled-key control for 28 Apr 1665 alone is 1 of 5,000 at seed 7 (above). The filed "0/5,000 each" was true for the one seed then run.
5. The Paulmyer 25 Apr count depends on counting period spellings as S. A later automatic check of ours with a modern-spelling word list scored the same passage 16/27 = 59.26%; the gap is the rule, not the reading. 21/27 is the figure under the rule of this folder.

## What is not claimed

- No letter here is read in the README's sense (95%). All are read in part; the three Paulmyer sister letters are decoded, not read, and are offered only as evidence that the key is the code Paulmyer used.
- No value proposed from context (`holes.md` 2) is in the key or any count.
- A later key built from Paulmyer's own glosses (our KEY_v4) was tried on six more bare Paulmyer passages: 51/95 = 53.68%. It was not adopted; nothing here uses it.
- Twelve further bare Petkum letters (13 pages) were decoded once with KEY_v3 on 12 Nov 2026: pooled 121/190 = 63.68% in our log, below our filing line. They were not filed and are not in this folder; two of the pages belong to letters glossed on their first page.
- Priority: not established (below).

## Remaining gaps

- Code numbers with no value: 35 in the Petkum letters (`holes.md` 2), mostly names and titles seen one to four times - blocker: not-attempted; the glossed Petkum leaves 477, 561, 565L, 581 and Sehested's glossed relations in unit 261294 (images 5-141) would settle most of them.
- Signs not in the key: plain q, crossed d, PF, FF; in Paulmyer's hand also plain m (= h) and an 8-like sign (= m) - blocker: open-codes.
- The four letters of #444 and the four Paulmyer letters have no blind second reading - blocker: not-attempted.
- The other bare Petkum pages of the unit (12 letters, 13 pages, decoded once with KEY_v3, pooled below our filing line, not filed) and 7 bare Paulmyer passages (18 Apr, 23 May, 26 Jun 1664, leaf 150 right, three of 1665; 6 of them tried only with the unadopted KEY_v4) - blocker: not-attempted as far as this folder goes.
- A contemporary decipherment of these very letters may exist unfilmed (the chancery read the code) - blocker: needs-physical-access.

## Escalation

- [x] siblings: the glossed Petkum leaves 377, 401, 574 right are the key source; Paulmyer's glossed leaves (unit 261294) checked against the key; other bare letters listed above
- [x] clear-pages: no clear copy of any of these letters found; the clear French around each passage is used for context only
- [x] known-keys: no key sheet for this code found in the units opened; a printed reference to a contemporary Galt key of the 1620s (Kong Christian IV's Breve I p.186) was noted, not seen and not used
- [x] print: printed Petkum letters are of other dates (1654; June-July 1663; Paris Sept 1666 to Apr 1667); printed Paulmyer letters are of Sept-Nov 1666 only (below)
- [x] key-rebuild: v1 to v3 from the glosses only, each frozen before the text it was tested on; v4 (Paulmyer glosses) tried and not adopted
- [x] retry: every unit not read is in `units/` with its reason; values suggested by the readings listed in `holes.md`, not applied

## Prior art (checked 12 Nov 2026): priority not established

Searched for these letters and their clear phrases: Danske Magazin, all 56 volumes (OCR); 155 archive.org volumes (Danske Samlinger, Nye danske Magazin, Historisk Tidsskrift, Kong Christian IV's Breve, Handlingar rorande Skandinaviens historia, Historiska handlingar); Thyra Sehested, Hannibal Sehested I-II; Schoolcraft, EHR 1910; DECODE (Petkum: 0 records); the Cryptiana index; 140 saved texts scanned for the dates and distinctive phrases; archive.org full-text searches. Found: Petkum letters printed are of other dates; Paulmyer letters printed are of Sept-Nov 1666. Not reached: Becker, Samlinger til Danmarks Historie under Kong Frederik den Tredies Regiering (archive.org and Google Books refused or had no text); Bøggild-Andersen, Hannibal Sehested (in copyright); Danmark-Norges Traktater 6 in full; for Paulmyer, DECODE, Cryptiana, Fridericia's Aktstykker and the Aarsberetninger in full. The Danish chancery read this code at the time; the Montpensier-Savoy match is known history (the claim is this passage). Nothing here claims a first.

## How to reproduce (standard-library Python, no network)

From any directory: `python3 -I scripts/decode.py key.tsv transcriptions/<id>.txt` (each file in `decryptions/` is byte-identical to this output; the 30 Nov R1 pages use `gloss/KEY_v1_gloss_377_401.tsv` and `gloss/KEY_v2.tsv`, the R2 file is first mapped by `scripts/signnames.py` to `transcriptions/petkum_1665-11-30_R2_blind_keynames.txt`); `python3 -I scripts/count.py` (writes `counts.txt` and two files in `units/`); `python3 -I scripts/compare_blind.py`; `python3 -I scripts/shuffle_control.py <pg4650.txt> <pg13951.txt> <pg17489.txt> <pg5097.txt>` (about two minutes; the corpus is not in the folder). The repository's own checkers were not run by us.

## Files

`key.tsv` (KEY_v3); `gloss/` (key history and the gloss evidence); `transcriptions/` (frozen, as decoded; `_blind` = second reader; the 30 Nov R1 is in two files, p2-3 and the held-out pp.1, 4); `decryptions/` (one per transcription); `units/` (`*.seg` word division, `*.units.tsv` labels, two files written by `count.py`); `readings/` (French reading with holes and English, one per letter, copied from our working files); `counts.txt`, `controls.txt`, `agreement.txt` (script outputs); `holes.md`; `scripts/`; `timestamps/` (six RFC 3161 and OpenTimestamps stamps, `timestamps/README.md` maps the files of this folder to them).

## Integration check (12 Nov 2026)

Verified from the files by the integrating reader (an AI reader, not a person); the full report is the coordinator's `R4_petkum.md`.

- Reproduced: `python3 -I scripts/count.py` and `scripts/compare_blind.py` give every figure in the table above to the unit; key md5 ddc02e4a9408e8ead7d51b5135a1ae82; 21 of 21 decryptions are byte-identical to `scripts/decode.py` (the 30 Nov R2 file through its keynames file). A second decoder written from `key.tsv` without importing the contributor's code gives the same letters for all 22 transcriptions. `docs/_check_profile.py petkum1665`: valid; `docs/_check_catalogue.py`: valid; `docs/_check_terms.py petkum1665`: 0 hits.
- Images (Rigsarkivet, `api.rigsarkivet.dk/ao/v1/images/<id>`, no bot check): 435R all 70 tokens, 573 right page lines R01-R12 (about 150 tokens), 641L lines 09-21 (about 100), Paulmyer 147L all 76: about 390 tokens compared by eye, 0 disagreements. Not compared: the other nine Petkum letters and the three Paulmyer sister letters.
- Control of ours: 300 key-level shuffles (the values of all tier A and B rows shuffled among the signs, French 4-gram, `lang` model fr-1600-letters) on the eight letters other than 30 Nov, the blind copies and Paulmyer: true -3.80, best shuffle -5.33, 0 of 300 at or above.
- Held-out test: pp.1 and 4 of 30 Nov (67.57%) against the pages the key was tried on first (68.07%), no drop. The order (key v2 frozen 01:35:14 before pp.1 and 4 were transcribed) is by the contributor's record: the only external stamp (RFC 3161, 01:36:39 GMT, imprint checked) is of one manifest that holds keys v1 and v2, the held-out transcription and its decode together, so it shows they existed by then, not in what order. No pass bar was declared for the held-out pages; the 65% filing line applies to pools. The 574R glosses are on the page next to p.4, and 574R is the relation to the king of 10 Dec 1665, the same affair as the bare letter of 10 Dec 1665 (arrest of ships in Norway): the code words 115, 386, 289, 314, 350 read in that letter come from its glossed twin. They are E, so the strict share is unaffected.
- Selection: twelve more bare Petkum letters (13 pages) were decoded with KEY_v3 and left out because they fell under the 65% line, which was applied after the results were seen. The pool of the eleven filed letters (562/819 = 68.62%) therefore leaves out the worse ones; with those 121/190 = 63.68% (the contributor's log figure, not in this folder) the pool of every decoded bare passage would be 683/1009 = 67.69% [derived]. Use the per-letter figures, not the pool, as the headline.
- Own line: on the blind reading the five-letter pool is 63.69%, under the contributor's own 65% line; that test is published as failed. Single letters at 53.85% (6 Apr 1666), 61.54%, 62.07% and 62.77% are below the three Paulmyer sister letters' best (63.89%) in some cases, so no threshold separates "read in part" from "decoded, not read" for the Petkum letters. Under the project's rule (strict share, under 95% = read in part) they are read in part, each at its own figure; the Paulmyer sisters stay decoded, not read and key support only.
- Not checked: the certificate chains of the stamps, the OpenTimestamps proofs, `scripts/shuffle_control.py` (needs four Gutenberg files), the images of the other ten letters.

Why the status is "in progress": the repository allows "read in part" as a stopping point only when each unread piece has an outside blocker. These do not: (1) the glossed Petkum leaves 477, 561, 565 left and 581, and Sehested's own Paris relations in unit 261294 (images 5-141, same code, glossed between the lines throughout, per the 11 Nov TKUA sweep) were not used to extend the key, and would settle most of the 35 open code numbers; (2) the twelve unfiled letters, and the blind second readings of the four letters of #444 and the four Paulmyer letters, were not made. When these are done, or each has a real blocker, the status line goes and `/writeup petkum1665` is run (page, ledgers, catalogue 2530 narrowed to the unread leaves, key web entry for the Petkum/Paulmyer key, atlas places, portraits of Petkum and Biermann if any exist).
