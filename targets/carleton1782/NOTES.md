# British headquarters at New York to Haldimand at Quebec, 1782: Clinton (22 February) and Carleton (6 and 25 September), word code plus Army List spelling — BL Add MS 21808 and 21806 (LAC B.148, B.146)

Status: in progress. Read in part, 510 of 559 cipher units read strictly (0.912), the three letters together (13 Nov 2026, Andrew Beling, with AI agents). Method: key recovered from external plaintext (the clear copies kept at Quebec), then tested: a code table frozen from the 22 February letter predicted the 25 September letter before its clear copy was opened, and **55 of 58 unqualified word predictions agreed** (failures kept: 22-19 thence where the clear copy has there, 43-19 hundred where it has thousand, 9-8 has where it has have). A shuffled table averages 0.44 of 58. The order of events rests on our own agents' files only (see Freeze disclosure). The word list behind the codes is not identified, so the key is partial. A fourth letter, Haldimand to Clinton, 16 March 1782, intercepted by the Americans and filed in the Papers of the Continental Congress as "from J. R.", decodes in full on the unchanged Army List key (a second held-out check of the key; section below). Folder only, no page.

**What the letters say and why they matter.** Clinton, writing from New York on 22 February 1782, passes on intelligence that the Americans and French plan an attack on Canada (Lafayette, it is said, went to France to propose it) and that George Rogers Clark, the Virginian commander in Kentucky, will lead two state regiments and about one thousand French and Spaniards down the Ohio and up the Wabash against Detroit in the spring. Carleton, his successor, writes on 25 September 1782 that Congress and the Pennsylvania assembly plan two raids into the Indian country: James Potter of the Pennsylvania militia ("Major Genl Potter" in the letter) from Fort Muncy on the West Branch of the Susquehanna into the Seneca country, and the Continental general William Irvine ("Irwin") from Fort Pitt towards Lake Erie; a later Carleton letter in cipher reported Potter's expedition laid aside (Brymner's 1885 calendar of B.146). These are the warnings the commander-in-chief sent the governor of Quebec about threats to Canada and its western posts in the last year of the war.

## What the letters are

Three letters from the British commander-in-chief at New York to General Frederick Haldimand, governor of Quebec, in one hybrid cipher. All three survive here as the nineteenth-century transcripts made for the Canadian Archives (Library and Archives Canada, MG21, the "B" volumes of the Haldimand Papers), photographed on reel H-1649 and viewable on Canadiana; the originals are British Library Add MS 21808 and 21806 and were not seen.

| document | cipher witness | clear text kept with it | units |
|---|---|---|---|
| Clinton, New York, 22 Feb 1782 | B.148 pp. 11, 11A, 11B (frames 1080-1082) | B.148 pp. 8-9, "Quadruplicate of Letter sent in Cypher overland" (frames 1077-1078); p. 12 a further clear postscript | 320 units: 223 word codes, 44 spelled words, 52 clear words, 1 unread |
| Carleton, New York, 6 Sep 1782 (duplicate sent with the 9 Sep dispatch) | B.148 pp. 93-94 (frames 1174-1175) | B.146 p. 50, "(in Cypher)", No. 6 (frame 612) | 117 units: 94 word codes, 15 spelled words, 8 clear |
| Carleton, New York, 25 Sep 1782 | B.148 pp. 123-125, duplicate arrangement pp. 126-128 (frames 1205-1210) | B.148 p. 102 (frame 1183), signature and docket p. 103; B.146 p. 54 (frame 616) | 200 units: 139 word codes, 43 spelled groups, 18 clear |

Full archive references and image links: `SOURCES.md`.

## The cipher

Two parts in one message (`KEY.md`):

- **Spelled words**, marked x or underlined: pairs line-letter on the title page of the annual Army List ("A List of the General and Field Officers ...", London, J. Millan), lines 1-29, letters counted from the left. This is the Haldimand-Clinton cipher of 1778-1781, which Haldimand describes in his own key sheet (B.147 pp. 402-405); our agents identified the page on 12 Nov 2026 (151 of 155 of his worked examples, 232 of 249 letters of his 16 Dec 1778 letter). `key/armylist_titlepage_1778.txt` is that key, unchanged throughout this folder.
- **Word codes**: plain pairs, first number up to 58, second up to 34, one pair for one word (a few take a written suffix: communicat+ed, honoura+ble, Vermont+eers, who+se). The printed list they come from is **not identified**. `key/word_codes.tsv` holds all 174 codes seen in the three letters, with every reading in every letter and where each value came from.

## What was done, in order

1. **Carleton, 6 Sep 1782** (12 Nov): cipher transcribed before the clear copy was read beyond its opening lines; aligned word for word with B.146 p. 50. 94 word codes (66 distinct), 15 spelled words: 95 of 96 letters agree on the Army List key (the miss: did spelled d-i-t). `carleton_1782-09-06/`.
2. **Clinton, 22 Feb 1782** (12 Nov): the whole cipher body transcribed and aligned with the clear quadruplicate. 100 distinct codes; 26 also occur in the 6 Sep letter (their 6 Sep readings are recorded beside them); 39 of 44 spelled words agree exactly on the unchanged key, five do not and are kept (intllligent, newyhrk, storis, wabache, hggreed). Numerals were re-read on enlarged crops after mechanical mismatches, so this is source-assisted transcription, not blind. `clinton_1782-02-22/`.
3. **Freeze** (12 Nov, 23:44 UTC): the Clinton code table (100 codes, with a qualified status on 21 of them) and the key, byte for byte, plus a full transcription of the 25 Sep cipher and the mechanical predictions it gives. The 6 Sep alignment was not added to the table beyond what the Clinton table already carried. Our own AI coordinator hashed the freeze before either agent opened the 25 Sep clear copy: `carleton_1782-09-25/CHECKPOINT.md`, `preclear/`. This is not an outside check; see Freeze disclosure.
4. **Test** (12 Nov, scored again 13 Nov): then the clear copies were opened and every frozen unit compared. The 12 Nov scorer (`postclear/score.py`) filled in the clear word from the prediction wherever it had no hand alignment, and so missed one failure; the figures below are from the 13 Nov hand alignment of every unit (`posttest/clear_alignment_25sep.tsv`, `posttest/rescore.py`, `posttest/SCORE.json`). The 12 Nov `postclear/` files are kept as they were.

   | prediction class | units | result |
   |---|---:|---|
   | unqualified word codes from the Clinton table | 58 | **55 agree, 3 fail** (22-19 thence, clear there; 43-19 hundred, clear thousand; 9-8 has, clear have) |
   | qualified word codes (a set of readings) | 25 | 21 in the set, 3 fail (13-14 in/on, clear near; 5-22 who, clear whom; 11-1 an, clear any), 1 extra |
   | spelled groups on the Army List key | 43 | 36 exact (i/j allowed), 6 differ, 1 extra |
   | word codes not in the table | 56 | no prediction; not counted as successes |
   | clear words in the cipher | 18 | not predictions |

   Shuffled-table control: the readings of the 100 codes permuted among the codes 200 times (seed 1782) give a mean of 0.44 agreements on the same 58 units, a maximum of 15, none near 55.

   On the failures. 22-19: both clear copies read "and to march from there", while the same hand writes "from thence" two lines on; it counts as a failure, though a debatable one, since a clerk may have written *there* for the cipher's *thence* (the code's reading in Clinton's letter twice and at unit 131 here). 43-19: the frozen *hundred* was our misreading of Clinton's clear copy, which reads "One thousand French and Spaniards" (frame 1077); 43-19 is *thousand* in both letters, so this failure is our error in building the table, not a conflict in the code. 9-8 *has*/*have* is a genuine difference.

   The spelled-group differences: incuosions, susnuehannah, escapedo, reuuire, and two groups whose last letter turned out to be the next pair (assembl+y, repairin+g). *escapedo* was our transcription slip: the cipher has seven pairs and spells *escaped* (`posttest/corrections.tsv`). The imprint line 29 of the key, inferred before, gave principal (twice), Irwin, plan and new exactly. The cipher's repeated "to Pines Creek" is in neither clear copy.
5. **After the test** (12 Nov): 39 new code associations from the 25 Sep letter (`postclear/new_associations.tsv`), marked as post-clear and untested. Five codes of the 6 Sep alignment that the frozen table did not carry (1-18, 6-6, 18-1, 29-9, 41-9) all agree with their 25 Sep readings; that is an observation after the fact, not part of the test.
6. **Second check and corrections** (13 Nov): a second AI agent of ours, not shown our conclusions, reran the predictions byte for byte, rechecked 26 groups on the images (24 confirmed, 2 wrong: Clinton 43-19 *thousand* and 25 Sep *escaped*, both now corrected) and found the scoring error above. Each point was then rechecked on the images, and the corrections went into `posttest/` (`CORRECTIONS.md`), leaving the frozen table and predictions as they were.
7. **Packaging** (13 Nov): this folder; `verify.py` re-checks the freeze hashes, regenerates all 200 predictions from the key and table, and runs `posttest/rescore.py` and checks the corrected score, the control and the corrections; `measure_strict.py` gives the strict read figures below. `docs/_validate.py` on `validation.tsv` (word codes and spelled letters of all three letters, 1088 read tokens): reading -2.031 against random keys -3.151 (z 13.9) and the shuffled refit best -2.148: verdict pass. The code values were fitted to these same letters, so this shows that the aligned values read as English, not that they are held out; the held-out evidence is the 25 Sep test. The package scripts `preclear/check.py`, `predict.py`, `transcribe.py` and `postclear/score.py` are kept as run on 12 Nov; they expect the workspace paths and the page images, so `verify.py` is the check to run in the repository.

## Reading

- Clinton 22 Feb: Chief Justice William Smith's intelligence that the Americans plan to invade Canada, Lafayette gone to France to propose it; George Rogers Clark to go down the Ohio and up the Wabash against Detroit in the spring; a report that Congress has agreed to give Canada to France. Cipher-order reading `clinton_1782-02-22/CIPHER_READING.md`; clear text `CLEAR_COPY.md`.
- Carleton 6 Sep: approves Haldimand's handling of the Vermonters, regrets the Indian raids, will not go to Quebec; Pigot's fleet arriving. `carleton_1782-09-06/reading.md`.
- Carleton 25 Sep: two expeditions planned into the Indian country, Potter from Fort Muncy towards the Seneca country and Irwin from Fort Pitt towards Lake Erie; Paterson in Nova Scotia ordered to assist Quebec; Washington's army at Verplanck's Point; L'Aigle taken in the Delaware. `carleton_1782-09-25/reading.md`; clear text `posttest/CLEAR_COPY_25sep.md` (the 12 Nov `postclear/CLEAR_COPY.md` misread "from there" as "from thence").

The texts are English, so there is no translation. Strict figures (`measure_strict.py`: a unit counts only when the key and table give the clear-copy word unchanged; spelled mismatches, the unread unit, units under glare and every occurrence of a code with conflicting readings are not counted): Clinton 236 of 268 (0.881), 6 Sep 103 of 109 (0.945), 25 Sep 171 of 182 (0.940), with the post-test corrections.

## A fourth letter: Haldimand to Clinton, 16 March 1782, intercepted

`haldimand_1782-03-16/` (13 Nov 2026). Two cipher copies of one short letter lie among the American intercepts in the Papers of the Continental Congress (National Archives RG 360, M247 roll 65), item 51: vol. 2 p. 227 ("Duplicate"; docket on p. 228 "Letter in Cypher from J. R.", catalogued by Fold3 as "Unknown. To unknown") and vol. 1 p. 737 ("dupl.", catalogued as "Sorel. To unknown ... with translation"), with an American translation on vol. 1 p. 738. Upstream's `balfour1781/NOTES.md` lists both items, found in the same pass, without linking them. The letter is all spelled: line-letter on the Army List title page, a number with only a dot repeating the last line, Q as a circled dot, a few words in the clear; 296 numbers on p. 227.

- **Who and when.** The cipher signature 6.11 11.1 spells F H; "J. R." is a misattribution. Haldimand's letterbook copy is B.148 p. 21 (BL Add MS 21808 fo. 17; reel H-1649 frame 1096), endorsed "1782 Copy. Cypher to Sir H. Clinton from St Johns March 16th". The letter it cites is Clinton's of 2 August 1781 (received 21 September), and "a few days ago I wrote more fully" is Haldimand's of 5-6 March 1782 (B.148 p. 16; Brymner's 1887 calendar). The cipher copies say Sorel where the letterbook says St Johns.
- **How it was read here.** The p. 227 copy was transcribed twice, then 56 cell values were solved from the clear words and word patterns alone before the key file was opened (`test/key_work.json`). A test was written down first (`test/TEST_PLAN.md`), and the key file of this folder, frozen for the 1782 letters on 12 Nov, before this letter was looked at, was then applied unchanged:

  | key | agreement with the 56 crib cells | decoded words found in a dictionary (65) |
  |---|---:|---:|
  | Army List title page, as in `key/` | **1.00** | **0.89** |
  | line number + 1 | 0.07 | 0.12 |
  | place + 1 | 0.02 | 0.12 |
  | letters shuffled within each line, 200 seeds | max 0.25 | max 0.31 |
  | lines in reverse order | 0.11 | 0.09 |

  Read on the letterbook copy afterwards (`CLEAR_COPY.md`), the decode is the same word for word, apart from St Johns for Sorel and the transcript's "Robinson" for Robertson. The one impossible group, 14.21 (line 14 has 17 letters), stands where the letterbook has "will". This is a second held-out confirmation of the title-page key, on a letter that is six months earlier than the Carleton letters and comes from the other correspondent. The key was not tuned, and its line 6 and 11 values give the signature. It also shows the Army List spelling in use by Haldimand in March 1782, after the "simpler cypher" he sent late in 1781 (B.147 p. 402).
- **The two copies** (`alignment.tsv`). Each has slips the other does not: p. 737 has *drectly*, *dince* (18.3 for 18.13, marked x on the page), *Sorl*; p. 227 has *rtports* (16.16 for 16.10). An ink blot on p. 227 covers three numbers of *sixteenth*, which p. 737 gives. Both copies share 14.21.
- **Who read it before us.** Clinton's office, if a copy arrived; Haldimand's clerk wrote the clear letterbook copy. An American decipherer read it during the war: the translation on vol. 1 p. 738 is right except for "any other" for "the least" (lines 12-13, used only there), "would" for "will", a dropped "the" and the signature guessed as "(perhaps) A. F.". Errors of that kind suggest that the decipherer worked from the cipher without the key. The hand is not identified; whether it is James Lovell's was not checked. Fold3's description says "with translation"; no printed text was found (two Founders Online searches found nothing; the 27 May 1781 intercept in James Clinton to Washington, 30 May 1781, is a different letter, to Haldimand).

## Freeze disclosure

- The order of events rests only on our own AI agents' files and file times: freeze 23:44 UTC on 12 Nov 2026 (`preclear/FREEZE.json`), the 25 Sep clear-copy images saved two to three minutes later. Nothing outside the machine dates it.
- The pre-opening checkpoint was done by our own AI coordinator.
- Before the freeze, another of our agents had already downloaded an 800-pixel copy of the second clear copy (B.146 p. 54, frame 616) and the OCR of Brymner's 1887 calendar, whose summaries name Potter, Irwin, Fort Munsey, Fort Pitt, Paterson and Verplanck and give "Irwin, of 1,000 men". The freezing agent's input manifest (`preclear/input_provenance.json`) lists only the key and the Clinton table, and its protocol says no clear transcript was opened; we can show what it declared, not that it never looked at those files. The predictions are table lookups, so such knowledge could affect only grouping and digit reading; *hundred* was kept for 43-19 against the calendar's 1,000.
- Whether a code counted as qualified (and so outside the 58) partly comes from the 6 Sep clear text (`prior_carleton_readings` in the table); none comes from 25 Sep.
- All three letters are one system from one headquarters, with clear copies: a held-out test inside a corpus fitted on the same system, not a blind decipherment. Details: `posttest/CORRECTIONS.md`.

## Who read these before us

- **At the time**: the clear texts are period copies kept with the ciphers at Quebec. Clinton's is the sender's own clear quadruplicate ("sent in Cypher overland"); the Carleton clear texts are entered in Haldimand's letter register B.146 ("(in Cypher)") and as a "Copy" in B.148 p. 102 whose margin points to the cipher transcriptions. Whether Haldimand's secretaries deciphered the Carleton letters or received clear duplicates is not established here. Either way the messages were read in 1782, and everything we read rests on those copies.
- **The Canadian Archives copyists** of the 1880s transcribed the cipher figures and the clear texts and cross-referenced them; all our readings are of their copies.
- **In print**:
  - **Clinton, 22 Feb 1782, is printed in full** (the clear text, not the cipher) in Michigan Pioneer and Historical Collections vol. 20 (1892), pp. 2-4, "Sir Henry Clinton to Gen. Haldimand", from B.148 p. 8, with the endorsement and "one thousand French and Spaniards". Our clear copy was read from the manuscript transcript; this printed text was found on 13 Nov, after the work.
  - Carleton, 6 and 25 Sep 1782: not found in Michigan Pioneer and Historical Collections vols. 9, 10, 11, 19 and 20 (Internet Archive OCR, searched for names and phrases of both letters; vol. 20 prints only B.148 pp. 8, 24, 109, 130 and B.146 pp. 7, 22 from these volumes).
  - Historical Manuscripts Commission, Report on American Manuscripts in the Royal Institution of Great Britain, vol. III (1907), calendars Carleton's own copies (Royal Institution American MSS vol. 47 no. 9 for 6 Sep, about p. 111; nos. 13 and 14 for 25 Sep, p. 132) with a heading and the locations of the other copies only (for 6 Sep it lists a cipher in Add MS 21705 fos. 73-74), no text.
  - Douglas Brymner's calendars print English summaries: Report on Canadian Archives 1887, calendar of B.148 (Clinton 22 Feb, with "The cypher of this letter. 11"; Carleton 25 Sep at p. 102), and Report on Canadian Archives 1885, calendar of B.146 (the 6 Sep letter, "Approves of his course with the Vermonters").
  - Not checked: the Colonial Office copies (CO 5/107; Q series 20) or any edition of them.
  - So the full text of Clinton's letter has been in print since 1892; the two Carleton letters only as summaries. None of these prints a cipher figure.
- **Modern**: Brice Dudout pointed in issue #359 (9 Nov 2026) to Clinton's line-column cipher of 22 Oct 1779 in B.147 with its clear copy and a partial key; that is the earlier, all-spelled stage of the same correspondence. We found no earlier identification of the Army List page or reconstruction of the 1782 word codes.

What we add: the reconstructed code table and Army List spelling over all three letters, and the frozen prediction of the 25 Sep letter (55 of 58).

## Catalogue and leads

Not in `catalogue.json` (items 781 and 783 are Clinton-Cornwallis photostats in the Clements Library, different letters). It attaches to waiting lead **1137** (Carleton Papers, TNA PRO 30/55: Clinton, Haldimand, Cornwallis and Leslie letters in cypher, 1779-1782), whose Carleton side this is, and whose 1779 Clinton-Haldimand item Brice Dudout pointed to (#359). Lead 1136 (Cornwallis Papers, PRO 30/11) is the southern Common cipher of 1780-81, a different system.

## Remaining gaps

- Clinton 22 Feb, the glare strip on p. 11B column 4 (to [?]duce it that engagement by) and the prefix of reduce - blocker: illegible (photographic defect on the LAC film; original needed)
- spelled groups that differ from the clear copies (Clinton intllligent, newyhrk, storis, hggreed; 6 Sep dit; 25 Sep incuosions, susnuehannah, reuuire) - blocker: needs-physical-access (digits or the special q mark in the originals)
- codes with more than one reading across the letters (9-8 has/have, 22-19 thence/there, 13-14 in/on/near, 2-5 engagement/French, 46-9 just/been, 9-19 this/the, 11-1 an/any, 5-22 who/whose/whom) and the provisional 23-6, 49-9, 2-2 - blocker: open-codes (the printed word list is not identified; a headword list would settle inflection and digit slips)
- the printed word list behind the codes - blocker: no-key-material (no candidate book found; `clinton_1782-02-22/DIFFERENCES.md` lists the coordinates any candidate must fit)

## Escalation

- [x] siblings: the 6 Sep, 22 Feb and 25 Sep letters worked together; Haldimand's 1778-81 Army List letters in B.147 used to identify the spelling key (12 Nov 2026)
- [x] clear-pages: clear copies located for all three (B.148 pp. 8-9, 12, 102-103; B.146 pp. 50, 54)
- [x] known-keys: Army List title page key (Haldimand's key sheet, B.147 pp. 402-405) applied unchanged
- [x] print: Brymner's 1885 and 1887 calendars (summaries), Michigan Pioneer and Historical Collections vols. 9-11, 19-20 (Clinton 22 Feb printed in full in vol. 20; the Carleton letters not found) and the HMC Royal Institution calendar vol. III (headings only) checked, 13 Nov 2026; CO 5/107 not checked
- [x] key-rebuild: code table rebuilt from the clear copies and tested on a held-out letter (55 of 58)
- [n/a] retry: the open pieces need the British Library originals or the printed word list, not another pass over the same copies

## Log

- 2026-11-12: Army List key identified on Haldimand's 1778-81 letters; 6 Sep 1782 aligned; Clinton 22 Feb collated in full; freeze; 25 Sep test (Andrew Beling, with AI agents).
- 2026-11-13: Haldimand to Clinton 16 Mar 1782 (PCC item 51 intercepts) identified, decoded with the unchanged key against a pre-written test, collated with both copies, the letterbook copy B.148 p. 21 and the 1781 American translation (Andrew Beling, with AI agents).
- 2026-11-13: folder assembled from those packages, strict figures measured, profile and validation; second AI check, scoring error and two misreadings corrected in `posttest/`, print search (Andrew Beling, with AI agents).
