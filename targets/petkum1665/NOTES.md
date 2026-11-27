# Petkum 1665-66 and Paulmyer 1664: unglossed letters in the Danish chancery's French syllabary, read with a key rebuilt from the chancery's own glosses (catalogue 2530; issues #443, #444)

Status: in progress (17 Nov 2026, PR #776: key v7 tested by Brice Dudout's side on fresh glossed leaves 505/501, 0.8808 against a best shuffled key of 0.3241, see the last section; 16 Nov 2026: key v7 = #646's key v6 + values read from Sehested's glosses on the rest of unit 261294, see Key v7; 14 Nov 2026, PR #622: Brice Dudout's independent key T2 verified and nine of its values taken into `key_v6.tsv`, see the last section; 13 Nov 2026, round 6: key v5 from Sehested's glosses and the twelve bare letters filed per letter, see `NOTES_addition_2026-11-13.md` and Integration check, round 6; 13 Nov 2026 session: key v4 added from four unused glossed leaves, see Key v4 below; integration check, 12 Nov 2026: every letter is read in part, none reaches 95%; not written up yet because the gaps below that are not-attempted can still be worked, see Integration check). Key rebuilt from the interlinear decipherments of sister leaves (no key sheet). Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic); issues #443 and #444 and the comments on them. Folder prepared 12 Nov 2026 in answer to the maintainer's note on both issues ("held, not rejected: the issue gives the results but not the files").

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

- Code numbers with no value: 16 after key v7 (40, 108, 135, 197, 198, 235, 330, 344, 351, 370, 374, 376, 388, 390, 394, 399; the 21 left by key v5 less 134 = Stockholm of key v6 and 151, 181, 248, 346 of key v7: 21 - 1 - 4 = 16, `counts_v7.txt`), and 2 more whose v7 value is doubtful (181 bruit, 248 hommes: 18 without a settled value) - blocker: not-attempted: Sehested's glossed relations in unit 261294 are now read on every image 5-141 except the right pages of 30, 33, 50 and 71 (`gloss/KEY_v5_coverage_261294.tsv`, `gloss/KEY_v7_coverage_261294.tsv`), but images 29-141 only as 1560 px spreads after contact-sheet triage, so a small number may have been missed; 235 and 399 occur there only as clerk's slips corrected in the margin and 40 only inside a gloss with no word for it alone (`gloss/KEY_v7_DIFF.md`). The 164 conflict is settled in v7 (amitie, 21 glosses; 574R's single 'alliance' kept in the source note). Workable: 248 against 181 for 'bruit' (541 left by Brice Dudout's reading has 'bruit' over 248; three Sehested glosses give 248 = hommes and one gloss over a clerk's slip gives 181 = bruit; both rows doubtful, `gloss/KEY_v7_DIFF.md`): look at 541 left again at full resolution. Over all first-reader transcriptions, 26 numbers in use have no value under v7 and 2 more are doubtful (`counts_v7.txt` section 2; 54, 70, 73, 127, 136, 154, 292 and others).
- Values of key T2 not taken into `key_v6.tsv` (PR #622, last section): 207 don, 225 fomenter, 376 traffic and 395 Sund are glossed by Brice Dudout's record and were not seen again here; 151 françois (key v7 now has 151 = François from a Sehested gloss, found without T2), 197 conduite, 344 raison and 351 rupture are placed by alphabetical rank only and give sense in all ten places where the folder's letters have them, which is context and not a gloss - blocker: not-attempted (the four glosses are on images 338, 421, 429 of unit 261267; a gloss for the rank values may be in the unread images of unit 261294).
- Signs not in `key.tsv` (v3): plain q, crossed d, PF, FF (Q = b and PF = f are in key v4, crossed d = g in key v7 from four glosses; FF has no value); in Paulmyer's hand also plain m (= h) and an 8-like sign (= m) - blocker: open-codes.
- The four letters of #444 and the four Paulmyer letters have no blind second reading (the twelve of the 13 Nov filing have one, with exposure disclosed) - blocker: not-attempted.
- The twelve filed letters (13 pages) have no French reading or English translation, so they stay decoded, not read - blocker: not-attempted (workable).
- The other bare pages: the 12 letters (13 pages) are now filed per letter (13 Nov, PR #500); two bare pages (337L, 376L) of letters glossed on their first page are not among them; and 7 bare Paulmyer passages (18 Apr, 23 May, 26 Jun 1664, leaf 150 right, three of 1665; 6 of them tried only with the unadopted KEY_v4); of these, 18 Apr 1664, 26 Jun 1664 and 14 Apr 1665 are filed blind on 16 Nov 2026 as decoded, not read, and 31 Mar 1665 is recorded as failed (below); 23 May 1664, leaf 150 right and one of 1665 remain - blocker: not-attempted as far as this folder goes.
- The pair 'T T' in three Paulmyer passages of 16 Nov 2026 (tryyis, _ambryytius, giyye): settled after the decode as a transcription error, not a key fault. It is one sign, the cursive # (HSH), which looks like two crossed t's on one bar (image 144R, line 2); the chancery glosses it o (unit 261294, 113R "ou", 111L "obtenir") and `key_v5.tsv` already has HSH = o, so tryyis = trois; row T = y stands (a single small T is glossed y at least 11 times in unit 261294). The gloss rows are filed with the key v7 work (separate pull request). The blind files of 16 Nov stay frozen and their first-pass figures stand; a corrected transcription has not been made or decoded - blocker: not-attempted (a second, declared transcription of the three passages).
- 14 Apr 1665, image 191: our crop of 191 right left out the part of the letter page that lies left of it, so the frozen transcription lacks 10 tokens (Dan Bourdeau, review of PR #689; not re-checked here): LAM 299 355 TH 277 before 301 (line 1); 364 Y m 18 after ct QX (line 2); 157 after "qu'un". The 80 tokens and 58/80 of the table below cover only what was transcribed; the frozen BLIND, decode and judge files are not re-scored or edited - blocker: not-attempted (a declared second transcription of image 191 from the full image).
- The three Paulmyer passages of 16 Nov 2026 are cipher runs only: the clear French around them was not transcribed, so they cannot read as sentences yet - blocker: not-attempted.
- A contemporary decipherment of these very letters may exist unfilmed (the chancery read the code) - blocker: needs-physical-access.

## Escalation

- [x] siblings: the glossed Petkum leaves 377, 401, 574 right are the key source (v5: 23 of 137 images of unit 261294 read, 114 not: not complete); Paulmyer's glossed leaves (unit 261294) checked against the key; other bare letters listed above
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

## Key v4 (13 Nov 2026): values read from the glosses on four unused sibling leaves

Done in a follow-up session (an AI reader, working from Rigsarkivet images fetched with `api.rigsarkivet.dk/ao/v1/images/<id>`, id = 48872547 + image number in unit 261267: 477, 561, 565 left, 581). The chancery wrote its decipherment between the lines; a value is taken only where the gloss word sits over a cipher number whose neighbouring tokens all have values and read as the gloss. `key_v4.tsv` = `key.tsv` + these rows (tier G = code word, counts E, never S; tier A3 = spelled value), each with the gloss quoted in its source column. md5 of key_v4.tsv is not fixed by any stamp.

| value | gloss and place |
|---|---|
| 313 = on | 561 left "auquel on pouvoit parler" (x.313.319.u.383.b.q); 561 right "la mediation de tout autre" (366.313.201 = ti-on-de) |
| 180 = bon | 561 right "bon Traitte" over x.335.180.373 |
| 373 = traitte | 561 left "un traitte" (...conclu un 373, mais je); 561 right "bon Traitte"; 477 "dans le Traitte", "traitte de paix" |
| 321 = paix | 561 right "faire la paix laquelle se fera"; 477 "de paix" (373.201.321.337.n = traitte de paix quo-n) |
| 118 = Espagne | 561 left "que l'Espagne et" (335.118.100); "Amb. d'Espagne" (x.165.u.30.17.118) |
| 348 = Roy | 561 right "Roy disant que" (348.202.352.n.32.335) |
| 117 = l'Empire, 329 = Princesse, 285 = mariage, 328 = Prince | 561 left "l'Empire"; 581 "Princesse Douairiere d'Orange" (266.329.203.u.a.341.18.340); 581 "ces mariages" (183.285.31); 561 right "tout autre Prince" (one gloss each) |
| PF = f | 561 left "la Flandre" (266.PF.266.n.17.340), 581 "la flotte" (266.PF.269.32.365) |
| Q (plain q, straight tail) = b | 477 "veritable" twice (381.341.364.Q.267); the looped G stays p ("pretexte") |
| 242 = he (was tier C) | 565 left "cher" (y.242.beta) |

Hold-out discipline: these values were found after every count of record above (by the record of this folder; no stamp). They are not part of the held-out tests and are not used to claim the earlier shares. The context guesses of `holes.md` 2 for 313 (on), 180 (bon), 373 (traite), 348 (Roy), PF (f) and Q (b) agree with the glosses; 310 (nous), 390 (vous), 369, 370, 281, 248, 181 were not found glossed on these leaves and stay open. 285 = mariage agrees with the context reading of Paulmyer 25 Apr (the "[match] of Savoy"), guessed before. Open after v4: 29 of the 35 code numbers (list in `profile.json` gaps).

Recount (`python3 -I scripts/count_v4.py`, `counts_v4.txt`): code words stay E, so only words with PF, Q or 242 turn N into S. First reader: 24 Mar 1665 68.97% to 72.41%, 23 Nov 70.83% to 71.88%, 10 Dec 68.00% to 72.00%, 6 Apr 1666 53.85% to 57.69% (blind copy the same), the other five unchanged (28 Apr 73.08%, 23 Jun 62.07%, 17 Sep 61.54%, 18 Jan 72.00%, 13 Apr 62.77%). No letter is near 95%. The 30 Nov letter and the Paulmyer letters carry the reader's own unit labels and were not relabelled; their figures stay as filed (a floor).

Still not done, and why the status stays "in progress": (1) Sehested's glossed Paris relations in unit 261294 (images 5-141) were not read, so values for 310, 390, 369, 370, 281, 248, 181 and the rest of the 29 were not looked for there; (2) the twelve unfiled bare Petkum letters exist in this folder only as a pooled figure (121/190), with no transcriptions or per-letter labels, so they cannot be filed per letter without transcribing the 13 pages again from the images; (3) no blind second reading was made of the four letters of #444 or the Paulmyer letters. All three are doable, none has an outside blocker.

## Integration check, round 6 (13 Nov 2026): PR #500 (key v5, the twelve letters per letter, blind second readings)

Verified by the integrator; nothing in the contributor's files was changed. Figures re-run: `python3 -I scripts/count_twelve.py` and `scripts/agreement_twelve.py` write byte-identical files (first reader KEY_v3 121/190 = 63.68%, v5 124/190 = 65.26%; blind v3 121/190, v5 126/190 = 66.32%; agreement 393/403 = 97.52%); an own labeller and an own decoder (from `key.tsv`, `key_v5.tsv` and the transcriptions, not importing the contributor's code) reproduce S and unit counts of all twelve letters and all 48 decryptions. `key_v5.tsv` md5 4a57336c...; against `key_v4.tsv` it adds exactly the 8 rows.

Gloss rows checked by the integrator on the Rigsarkivet images of unit 261294 (id = 48879349 + image number): 309 nostre and 307 negociation (image 6 left), 310 nous (images 6 left and 17 right), 163 alliance and 82 l'Electeur de Brandebourg (image 17 right) all stand over the cipher groups the contributor names. 82 has one attestation and the gloss covers several groups. Not checked on the images: 369, 281, 338, and the twelve transcriptions. The shuffle controls per letter were not re-run (decode_v2.py and the corpus are not in the folder).

What this changes: per letter, no letter reaches 95% (best 16 Mar 1666, 16/17 = 94.12% on 17 units with 0 code words; its shuffle control fails, 197 of 5,000). Under the repository's rule the twelve are decoded, not read (no reading file). The figures per letter are the evidence; the pool of twelve is information only and is not a headline (the filing was selective: these twelve were first held back because they fell under the 65% line). The blind second readings are "second readings with exposure": the blind reader had read the first reader's log (pooled tally, file names, one token string) before transcribing, so 97.52% is not an independent-reader figure. Order of events (v5 frozen 21:25:25 UTC, blind frozen 21:31:08 UTC) is by the contributor's record: no external timestamp covers this addition. The v5 figures are not held out and their gain over v3 comes from the v4 rows PF, Q and 242, not from the v5 rows (which only turn N into E).

Status decision: the gaps are not all outside-blocked (114 images of unit 261294, the 164 conflict, blind readings of the other eight letters, readings of the twelve are all workable), so the target stays `Status: in progress` and gets no page, README row or SOLVED rows. Profile: four solution steps, the twelve letters as documents (decoded, not read), outcome gaps and `codes_open` updated.

## Issue #607 (14 Nov 2026): an independent key T2, as first reported (the files came with PR #622: next section)

Brice Dudout reports in issue #607 a key of his own for this code, called T2. No file came with the issue (no key table, no transcription, no hash, no script), so nothing below is verified here; the figures are the issue's.

What the issue reports:
- T2 was learned from the chancery glosses of images 338, 377, 401, 421, 429 and 461, then of 561; frozen by SHA-256; measured once on glossed portions not looked at before (553 left, 541 left, 638 right; 554 glossed groups): character agreement 0.885, best of 200 shuffled keys 0.295.
- The system as T2 has it: 14-36 single letters; 170-399 consonant and vowel syllables in blocks of five with whole words filed in the gaps; 38-169 names, titles and words; signs as letter homophones. This is the system of the section "The system" above.
- With T2 the letter of 30 Nov 1665, pp. 2-3 (image 573): 247 enciphered words, 232 sure, 10 probable, 5 unresolved (399, 40 twice, 338, 370), "about 98% by sense". The count of record here for the same pages is 169 of 238 units strict (71.0%, `counts.txt`); the two counts do not use the same unit (words there, units here) or the same rule, and are not comparable as they stand.

What could be checked here without the files, against `key.tsv`, `key_v4.tsv` and `key_v5.tsv`:
- Of the 37 nomenclator and word values the issue gives as attested by glosses, 29 have a value in `key_v5.tsv`. 28 are the same (38 and 100 et, 51, 61, 74, 92, 96, 107, 116, 118, 119, 120, 152, 153, 157, 196, 209, 222, 227, 236, 240, 288, 321, 328, 350, 373, 386, 389). One differs: 88 is "Roy d'Espagne" in T2 and "l'Espagne" here (tier A2, from 574 right), where 118 = Espagne too (v4, from 561 left); T2's value would end that doubling and puts 88 among the sovereigns (61, 74, 92). Not settled here: 574 right has to be read again.
- Eight attested values of T2 are not in any key here: 114 Dannemarck, 130 Hollande, 133 Copenhague, 134 Stockholm, 150 danois, 192 commerce, 212 ennemi, 358 satisfaction; nor are four of its probables, placed by rank only: 151 françois, 197 conduite, 344 raison, 351 rupture. Of these, 134, 151, 197, 344 and 351 are among the 21 numbers with no value (Remaining gaps); 134 also stands in the letter of 18 Jan 1666.
- The other T2 probables are in `key_v5.tsv` already from glosses: 163 alliance, 281 maistre, 310 nous. T2 arrives at them by rank, v5 by Sehested's glosses: two routes, same values. (The 164 conflict, amitie against alliance, is not touched by the issue.)
- T2 lists 338 as unresolved; `key_v5.tsv` has 338 = qu'u (unit 261294, image 5 right, "qu'un traitte"). 399, 40 and 370 are open in both.
- The issue names no value for 313, 180 and 390 or for the signs q and crossed d, which stand in image 573 too; the files would show what T2 reads there.
- The issue's correction to catalogue entry 2530 is right by this folder's own key: on image 377 the example "222.100.215 = 'faire'" is three groups, faire (222), et (100), executer (215), glossed "a faire et executer" (`key.tsv` rows 100, 215, 222). The entry text in `catalogue.json` (and in `research/sweep_2026-11-11_tkua_paging_2/candidates.json`) still has the short form; not edited here.

Not checked: the Rigsarkivet images (none fetched for this issue), the T2 table, its hash, the held-out portions, the 0.885 and 0.295, the reading of image 573. What is asked of the contributor: a pull request with the key table and its hash, the transcriptions of the training and held-out glosses, the script that gives 0.885 and the controls, and the reading of image 573 with its units, under `targets/petkum1665/` (for example a `dudout/` subfolder, as in other shared targets). The new values can then be tested as a held-out prediction on the twelve letters filed on 13 Nov and counted by this folder's rule. Until then nothing of T2 enters the key or the counts.

## Integration check, PR #622 (14 Nov 2026): key T2 verified; what this folder takes from it

Brice Dudout (with AI agents) sent the files asked for under issue #607: `dudout/` (its `README.md` lists them). His commit is unchanged; what follows was checked at integration and is in separate commits.

| claim | his figure | here | how |
|---|---|---|---|
| hashes of the protocol, keys T and T2, held-out transcriptions | 10 SHA-256 | 10 of 10 match; json and TSV regenerate byte for byte | `python3 -I dudout/scripts/verify_hashes.py` |
| measure 2: T2 on H2 (553 left, 541 left, 638 right; 554 groups, 200 glossed passages) | 0.8848 | 0.8848 | his `measure.py`; and a decoder written here from `key_T2.tsv` (own edit distance): 0.8848, 158 of 200 passages exact, 12 groups without a value |
| controls for measure 2 | best 0.2946, mean 0.2704, 0 of 200 | the same; 100 further shuffles with other seeds: best 0.2841, mean 0.2696 | `controls.py` output identical to his file; own shuffles |
| measure 1: T on 561 (654 groups) | 0.7976, failed | 0.7976 | `measure.py` |
| image 573, strict by this folder's rule | S 173 of 238 = 72.69% (E 43, N 22) | 173 / 43 / 22 | `units_573.py` |
| image 573, by sense | 233 of 238 = 97.90% (220 sure, 13 probable) | his rule, his figure | not this folder's rule: probable words count there |

**The first test failed and is recorded as failed.** The protocol declared one measure on image 561 with the bar at 0.85 and at 0.30 above the best shuffled key. Key T scored 0.7976: under the bar. A second measure was then added (addendum 2): the 561 glosses went into the key (T2) and a new portion was measured, 0.8848, over the bar. That second measure is a rule added after the result. What makes the key credible beyond it: the margin over shuffled keys (0.59), and the checks below.

**What "held out" rests on.** The hashes show that the key files and the held-out transcriptions are the ones measured. The times are from the contributor's log: there is no outside stamp, and everything came in one commit on 14 Nov. The training glosses were not written down on 11 Nov; `training_A_posthoc.txt` was transcribed on 14 Nov, after both measures, by a reader who by then knew the key and the held-out leaves. So the files cannot show that the key was built before the held-out leaves were seen; that is by the contributor's record. What the files do show: every value T marks as seen stands under a gloss in the training file, every value added for T2 stands in the 561 file, and T2 has no value for 12 groups, 11 numbers, that H2 glosses in full (124, 127, 153, 164, 167, 199, 209, 289, 348, 350, 375), which a key built with H2 in view would have had.

**Images.** Rigsarkivet's image API served the leaves (api.rigsarkivet.dk, id = 48872547 + image number). Compared with his transcriptions: 553 left (H2), 561 right (H_561), the head of 541 left (H2), 461 right (training): about 440 groups. One misreading: on 561 right the number under "Roy disant que" is 348, his file has 248. That put 248 = roy into T2; the folder's 348 = Roy (v4, from the same gloss) is right. On 553 left a ct before 389.288 is not in his file. Everything else agrees.

**Two transcriptions of image 573.** His token transcription (`dudout/reading/573_transcription.txt`) and the folder's (`transcriptions/petkum_1665-11-30_p2-3_R1.txt`), made apart, agree on 552 of 558 tokens (98.9%; sign names mapped). The differences: 270 against 220 twice (his 270, p-lu-s, is the one that spells), d against FF, 4 against #, one syllable written in clear.

**T2 against `key_v5.tsv`.** 139 numbers have a value in both. 130 are the same letter for letter; seven differ in wording or spelling only (51, 61, 96, 107, 118, 161, 236); two differ in value: 23 (j in T2, k here, both by the row rule and neither met under a gloss) and 88, below. T2 only: 2, 4, 6, 9 (signs named by figures), 101, 114, 130, 133, 134, 150, 192, 207, 212, 225, 248, 358, 376, 395.

**88 is le Roy d'Espagne.** Seen here on 561 right: "entre le Roy son Maitre et V. M." over ll.4.9.340.88.100.389.288, and "l'Empereur et du Roy d'Espagne et croy que l'Espagne" over 74.100.88.38.y.342.T.335.118, with 88 and 118 in one line. `key_v6.tsv` corrects 88 (v2 had l'Espagne from the short gloss "d'Espagne" on 574 right).

**The new values tested on the folder's letters** (decoded before T2 was known here, so this is a prediction): 114 once, 130 once, 133 four times, 134 four times, 192 three times, 376 once, 88 three times: 17 places. 16 give sense ("qu'elle s'accorde a Coppenhague", "ce que Dannemarck et la Suede voudra faire", "negocie a Stockholm", "touchant le commerce de nostre sel", "le Roy T.C. et le Roy d'Espagne"). One does not: Paulmyer, 16 May 1664, "Conseiller en la Cour des aydes a 134" (Paris is expected; that number has to be looked at on the image). 248 = roy fails in its three places ("cinq ou six mille 248s"), as the misreading above explains. The four rank values (151 françois five times, 197 conduite three times, 344 raison, 351 rupture) give sense in all ten places; they stay out of the key, since sense is not a gloss.

**`key_v6.tsv`** = `key_v5.tsv` with 88 corrected and nine T2 values seen again on the image here: 101 la Suede, 114 Dannemarck, 130 Hollande, 133 Coppenhague, 134 Stockholm, 150 danois, 192 commerce, 212 ennemi, 358 satisfaction (tier D, sources in the file).

**Counts, by this folder's rule** (`counts_v6.txt`, `python3 -I scripts/count_v6.py`): code words count E, never S, so no strict share changes. On the twelve letters of 13 Nov two units move from N to E, for both readers: 133 in the letter of 13 Jan 1665 and 114 in that of 27 Jan 1665. In the other letters 134 moves one unit in each of 23 Jun 1665 and 18 Jan 1666. The counts of record (`counts.txt`, `counts_twelve.txt`) stand; the decryptions and readings were not rewritten with v6. For image 573 the count of record stays 169 of 238 (71.0%); Brice Dudout's 173 of 238 uses the same rule with his own word division and list of accepted spellings.

**The reading of image 573** (`dudout/reading/573_reading.md`) was read here as French against its translation: it builds sentences throughout, with 13 probable words and 5 unresolved marked. It is a second reading of pages the folder already reads in part and is not an entry of `outcome.texts`; no `reading_review` is recorded for it. The eleven readings of `outcome.texts` had no `reading_review`, which is why the reading check was red on PR #622 (Brice Dudout's comment there). They were read through here as French against their English, by a session that did not write them: all build sentences with their holes marked, all are graded B, and the notes are in `profile.json`. The weakest is 6 Apr 1666, whose matter rests on three open numbers (346, 235, 373).

**Catalogue 2530.** The example in the entry is corrected as issue #607 asked: on image 377 the groups 222.100.215 are glossed "faire et executer", not "faire".

Credit: shared. Malcolm McBratney's key and readings; Brice Dudout's independent key T2, which agrees with this folder's key on 137 of the 139 numbers they share, corrects 88 and adds nine values.

14 Nov 2026, second maintainer's review of PR #646 (Brice Dudout's side): petkum_1666-04-06 is set to "decoded, not read" and carries no reading review: its two sentences rest on the open numbers 346 (twice), 235 and 373. Ten readings keep grade B.

## Addition of 16 Nov 2026 (Malcolm McBratney, with Claude): four bare Paulmyer passages, blind

Four of the seven bare Paulmyer passages listed in Remaining gaps, unit 261294 (Rigsarkivet image API, no bot check;
`blind16/<doc>/FETCH_LOG.txt`). Everything is in `blind16/`, one folder per letter, frozen before the decode:
- Keys frozen first: `blind16/_key_frozen/` holds byte copies of `key.tsv` and `key_v5.tsv` of upstream 89e25ef (sha256 in
  `FREEZE.txt`); decode key = `key_v5.tsv`, unchanged.
- Blind transcription: one AI reader (Claude) per letter, given only the image crop and the label sheet
  (`<doc>/blind_packet/`: sign names, no values), no earlier transcription, no web. `BLIND.tsv` hashed before the decode
  (`<doc>/FREEZE_blind.txt`). An earlier, unfiled decode of most of these passages with the unadopted KEY_v4 exists in our
  working files (pooled 51/95), so this is not the project's first sight of them.
- One decode (`blind16/decode_once.py`, upstream `decode.py` dec_run marks unchanged): `<doc>/decode_once.txt`; copies in
  `transcriptions/*_blind16.tsv`, `decryptions/*_blind16.txt`.
- Strict one-pass judge per sign unit, no edits (`blind16/JUDGE_NOTES_paulmyer.txt`, `<doc>/judge.tsv`).
- Shuffled-key control (`blind16/shuffle.py`, `blind16/shuffle_out.txt`): the values of the 1-3-letter key rows permuted
  among the signs, spelled runs scored with `lang` model fr-1600-letters, 5,000 per seed. Bar fixed before the run:
  fewer than 5 of 5,000 at or above the real score at both seeds.
- Readings (`readings/paulmyer_<date>.md`): the judge's segmented text of each run unchanged, holes marked, each run after
  the clear word before it; English by Claude, unchecked.

| letter | tokens | strict judge | shuffle, seed 20261112 / 7: >= real of 5,000 (real; max) | _check_reading | filed as |
|---|---|---|---|---|---|
| 18 Apr 1664, Paris, image 144R | 71 | 61/71 = 85.9% | 0 / 0 (-3.4411; -4.0497, -4.0876) | 0.614 marginal | decoded, not read |
| 26 Jun 1664, Fontainebleau, image 162 | 54 | 36/54 = 66.7% | 0 / 0 (-3.2243; -4.0095, -4.1741) | 0.476 marginal | decoded, not read |
| 14 Apr 1665, images 191R-192 | 80 | 58/80 = 72.5% | 0 / 0 (-3.0540; -4.0675, -4.2740) | 0.481 marginal (0.444 after the image-191 note was added to the reading file) | decoded, not read; 10 tokens of image 191 not transcribed |
| 31 Mar 1665, images 189R-190L | 17 | 11/17 = 64.7% | 0 / 0 (-2.1851; -3.2812, -2.6398) | not run | failed our 65% line: recorded only |

Token counts are from `DECODE_RUN.txt` (script-written). These entries are kept apart from the Paulmyer pool above and
from every Petkum figure; they do not change any count of record. By cipher word (the judge's segments in
`<doc>/judge.tsv`, a word counted read only when every unit is S): 18 Apr 1664 19/28, 26 Jun 1664 15/22, 14 Apr 1665
16/28, 31 Mar 1665 2/5. `profile.json` carries the word share as `read_share` and the unit figure in the note.

What they touch (Claude's gist, unchecked): 18 Apr 1664, a maritime union of three powers and the Rhine alliance, with
Austria, the Dutch, France and its navy, Louis XIV and the King of Denmark named; 26 Jun 1664, a new subsidy to the
Swedes; 14 Apr 1665, a notable sum of money, engaging Louis XIV, Chancellor Séguier and a man named des Fargues.

The recurring 'yy' (the pair 'T T') in three passages was first taken for a suspected key fault. That is withdrawn: it
is one cursive # sign (HSH = o) misread as two T's, a transcription error found after the decode (Remaining gaps).
Nothing was changed in any key.

Key v6 (`key_v6.tsv`, PR #622 integration, now on main) gives values to numbers in these passages that the frozen v5
decode leaves open: 114 = Dannemarck (18 Apr and 26 Jun 1664) and 134 = Stockholm (26 Jun 1664). Nothing was decoded
again with v6: the decodes, judge counts and readings above are the frozen v5 pass.

14 Apr 1665 is incomplete: image 191 shows more of the letter page left of our crop, and 10 tokens are missing from the
transcription (LAM 299 355 TH 277 before 301 (line 1); 364 Y m 18 after ct QX (line 2); 157 after "qu'un"; Dan Bourdeau's review of PR #689, not re-checked here). The 58/80 above is the first pass on
the 80 tokens transcribed, not a figure for the passage; nothing frozen was edited or re-scored.

Prior art: the folder's search (above) found printed Paulmyer letters of Sept-Nov 1666 only; DECODE, Cryptiana,
Fridericia's Aktstykker and the Aarsberetninger in full were not reached for Paulmyer, and a web search of 16 Nov 2026
found nothing. No content is claimed first.

## 14 Nov 2026: reading review of the eleven letters read in part (audit section J)

Done by Claude (session of 14 Nov 2026). Nothing in the contributor's transcriptions, decryptions or counts was changed.

- Each of the eleven reading files (30 Nov, 24 Mar, 23 Nov, 10 Dec 1665, 13 Apr 1666; 28 Apr, 23 Jun, 17 Sep 1665, 18 Jan, 6 Apr 1666; Paulmyer 25 Apr 1664) was read as sentences against its decryption, line by line. All eleven build sentences with scattered holes: the cipher passages sit in the letter's clear French, and the reading adds no word the decryption does not carry except the marked `[?guesses]`. `reading_review` (grade A, with what each rests on and what is open) is recorded per entry in `profile.json`. The weakest is 6 Apr 1666 (three open codes, 346 twice and 235, in its main sentence). States stay `read in part`; no count of record, `fraction_read` or class changed.
- The eleven frozen transcriptions were decoded again with `key_v5.tsv` (`python3 -I scripts/decode.py key_v5.tsv transcriptions/<doc>.txt`; the 30 Nov letter from `petkum_1665-11-30_R2_blind_keynames.txt`). The key v3 decode of each was reproduced byte for byte first. New files: `decryptions/<doc>_v5.txt` for the ten, `decryptions/petkum_1665-11-30_R2_blind_v5.txt`. 55 tokens gain a glossed value (on, nous, traitté, Roy, tant, bon, maistre, nostre, paix, alliance, Espagne, mariage, negociation, 82 = l'Electeur de Brandebourg, f, b, qu'u); 28 Apr 1665 is unchanged. Each reading file has a dated addendum listing the changed tokens line by line and the tokens still without a value; the text above the addendum is the contributor's, unchanged.
- What the v5 decode changes in the sense: 18 Jan 1666, "le rapel de Cliffort n'aye este qu'une fainte" (338 = qu'u): the recall of Clifford was only a feint; the English of the reading file ("was not [338] nor feigned") is wrong there. 17 Sep 1665: "si grands amis du Roy nostre maistre". 13 Apr 1666: the list of allies includes 82, l'Electeur de Brandebourg (one attestation in the key), which the English omits. 23 Jun 1665: under key v3 every sentence had a hole; under v5 only 390 and 134 are open.
- Not done: the reading files were not rewritten with the v5 values (they are the contributor's filed text; the addenda carry the changes), and the counts were not re-run for 30 Nov and Paulmyer (their unit labels are the reader's own; `counts_v4.txt` covers the nine others under v4).

## Key v7 (16 Nov 2026, Malcolm McBratney, with Claude): Sehested's glosses read to the end of unit 261294

First filed with PR #689 as a key_v6.tsv built on key v5; renamed v7 and rebuilt on #646's key_v6.tsv after the
maintainer's review, because the two files shared a name with different content.

An AI reader (Claude) read the chancery's interlinear glosses on the 119 images of unit 261294 not read for v5 (11-16, 22,
26-141 except 30, 33, 50, 71) and the unread halves of 17, 23, 24 and 25, and re-read 574R (unit 261267); every fetch is in
`gloss/KEY_v7_FETCH_LOG_261294.txt` (Rigsarkivet image API, all HTTP 200, no bot check). Each gloss used is a row of
`gloss/KEY_v7_glosses_261294.tsv`; the diff, the basis of each row and the dispute with #646 are in `gloss/KEY_v7_DIFF.md`.

- `key_v7.tsv` (md5 d1ee7e3094e1643bfb0f58b39e9d0052) = `key_v6.tsv` of #646 + 151 = François (G2, single gloss, 1560 px
  spread), 181 = bruit (G2?, single gloss over a clerk's slip for 185 contre; doubtful), 248 = hommes (G?, 3 glosses;
  doubtful), 346 = ratification (G, 2), crossed d (DB) = g (A, 4); and 164 changed from alliance to amitie (21 glosses).
- Disputed, not picked: #646 records 'bruit' over 248 on 541 left (Brice Dudout's reading, "un bruit sujet a caution");
  our glosses give 248 = hommes three times and 181 = bruit once. Both rows are marked doubtful (tier ending '?') and
  count N in `scripts/count_v7.py`; the evidence on both sides is set out in `gloss/KEY_v7_DIFF.md`.
- Agreements: 88 = le Roy d'Espagne, corrected by #646 from 561R, is also glossed three times in unit 261294 (86R, 117R
  twice); row T = y is confirmed by at least 11 glosses.
- Not adopted: 40 (inside the gloss "plus", no word of its own), 235 and 399 (clerk's slips corrected in the margin).
  Proposed only: three C -> A2 tier upgrades (245, 252, 256).
- Open (`scripts/count_v7.py`, `counts_v7.txt`): 21 - 1 - 4 = 16 of the 21 numbers, plus 2 doubtful. Per letter, not a
  count of record: 14 word units would move, 11 N to E (151, 346) and 3 N to S (DB = g).
- Nothing was decoded with key v7 and no count of record changes.
- Brice Dudout's T2 was not used to find or choose any value. Remark only: T2 had 151 = françois as a rank probable. The
  context guesses of `holes.md` (248 homme, 181 bruit, DB = g), never applied, agree with the glosses.
- **No person has checked the gloss readings.** Every gloss in `gloss/KEY_v7_glosses_261294.tsv` was read by an AI
  reader (Claude) only; the maintainer checked images 27, 113 and 141 for 181, 248 and 346 in review of #699.
- Maintainer's review of #699 (16 Nov 2026): on 541 left the figure under 'bruit' is a clear 248, so explanation (b) of
  `gloss/KEY_v7_DIFF.md` is ruled out. For our values: Petkum, 23 Nov 1665 (`readings/petkum_1665-11-23.md`), "courir
  un faux 181 d'une levee de cinq ou six mille 248s", and "mille 248s" twice in the bare letters. Both rows stay doubtful.
- Limit: images 29-141 were triaged on contact sheets and read at 1560 px, lower than v5's 2400 px copies; 151 rests on
  one such reading.

## Key v7 tested on fresh glossed leaves (Brice Dudout, 17 Nov 2026; depends on PR #699)

Files: `dudout_v7heldout/` (its `README.md` gives the order of events, the hashes and how to reproduce). Key v7 is Malcolm McBratney's (`key_v7.tsv` of PR #699, md5 d1ee7e3094e1643bfb0f58b39e9d0052), used unchanged and copied byte for byte into the folder.

- Portion: the glossed relations to the king on images 505 left, 505 right and 501 right of unit 261267, never used by anyone for a key, a check or a measure (505 and 501 were the reserves of our protocol of 11 Nov). Chosen and frozen with the key, the script and the bar before any crop was made: 315 cipher tokens, 57 glossed runs.
- Two blind transcriptions by separate AI readers with the label sheet only: 310 of 315 tokens agree (first given as 311; on 505R line 21 A has "MT 269" and B "PM 169", two tokens, maintainers' count at integration); 4 token rows (5 token positions) and 4 gloss differences adjudicated on the image (by an agent who knew v7, disclosed) and frozen before the decode.
- One measure, decode against the chancery gloss: **0.8808** (1 - Levenshtein / length, a-z); 200 shuffled keys best 0.3241, mean 0.2778, 0 of 200 at or above. Bar fixed before: >= 0.85 and >= best + 0.30. **Passed.** Pass A alone 0.8637, pass B alone 0.8719 (not decisive). Strict: 26 of 57 runs decode the gloss letter for letter.
- Seen in the misses, not changed: both readers wrote the i-sign as `6` (v7 names it `B`), which the frozen rule leaves without a value; on 505 right the gloss over `100 335 88` reads "et que l'Euesque de Munster", against 88 = le Roy d'Espagne in v6/v7; we misread one gloss ("emulitez", where the key gives civilitez). 151 = François (v7, single gloss) is glossed twice more here (505R, 501R). Glossed numbers with no value: 53 (S.A.R.), 94 (Duc d'York), 262, 347, 349 (observations, burned with the portion, not added).
- Recount of our reading of image 573 (`dudout_v7heldout/573_recount_v7.md`): six rank-only probables now stand under a gloss in v5 or v7 (151 three times, 163, 281, 310): 226 of 238 units sure = 94.96%, under 95%, so it stays read in part. By this folder's rule the six move N to E (S 173, E 49, N 16); no count of record changes. No frozen transcription was touched.
- 18 Nov 2026, blind sign-form check on image 573 (Brice Dudout; 3 of 3 controls right): unit 114 ends in the sign HB of 574R (z in v7), so "persuadez" is sure; the middle sign of the catchword unit 238 looks like X (l), so "tous" stays probable (decoded "tols"). Our count: **227 of 238 units sure = 95.38%**, a unit figure. The class of the 30 Nov 1665 entry stays read in part (maintainer, 19 Nov 2026) until a recount by cipher words is at or above 95% and a reader other than the author has reviewed the reading; the counts of record are not changed.
- Integration check of PR #776 (27 Nov 2026, AI agent for the maintainers; linear copy of Brice Dudout's two commits): the 13 hashes match, `build_final.py` regenerates FINAL.tsv and the two single-pass files, and `measure_v7.py` gives 0.8808 against a best control of 0.3241 (mean 0.2778, 0 of 200), 26 of 57 runs strict; pass A 0.8637, pass B 0.8719. `key/key_v7.tsv` is byte-identical to `key_v7.tsv`. A/B agreement recounted as 310 of 315 tokens (lines 8, 12, 21 twice and 25 of 505R); it does not touch the measure. Rests on Brice Dudout's record only: the order of the freeze (all files are in one commit, so the hashes show only that the committed files are the frozen ones), the isolation of the two blind readers, and that 437R and 481L were transcribed but not decoded. Not checked: the images of 505 and 501 (505R was checked in part on 18 Nov).
