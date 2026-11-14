# British headquarters at New York to Haldimand at Quebec, 1782: Clinton (22 February) and Carleton (6 and 25 September), word code plus Army List spelling — BL Add MS 21808 and 21806 (LAC B.148, B.146)

Status: in progress. Read in part, 511 of 559 cipher units read strictly (0.914), the three letters together (13 Nov 2026, Andrew Beling, with AI agents). Method: key recovered from external plaintext (the clear copies kept at Quebec), then tested: a code table frozen from the 22 February letter predicted the 25 September letter before its clear copy was opened, and **56 of 58 unqualified word predictions agreed** (the two failures, 43-19 hundred/thousand and 9-8 has/have, are kept). The word list behind the codes is not identified, so the key is partial. Folder only, no page.

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
3. **Freeze** (12 Nov, 23:44 UTC): the Clinton code table (100 codes, with a qualified status on 21 of them) and the key, byte for byte, plus a full transcription of the 25 Sep cipher and the mechanical predictions it gives. The 6 Sep alignment was not added to the table beyond what the Clinton table already carried. A second agent (the coordinator) hashed the freeze before either agent opened the 25 Sep clear copy: `carleton_1782-09-25/CHECKPOINT.md`, `preclear/`.
4. **Test** (12 Nov): then the clear copies were opened and every frozen unit compared (`postclear/comparison.tsv`, `SCORE.json`):

   | prediction class | units | result |
   |---|---:|---|
   | unqualified word codes from the Clinton table | 58 | **56 agree, 2 fail** (43-19 hundred, clear thousand; 9-8 has, clear have) |
   | qualified word codes (a set of readings) | 25 | 21 in the set, 3 fail (13-14 in/on, clear near; 5-22 who, clear whom; 11-1 an, clear any), 1 extra |
   | spelled groups on the Army List key | 43 | 36 exact (i/j allowed), 6 differ, 1 extra |
   | word codes not in the table | 56 | no prediction; not counted as successes |
   | clear words in the cipher | 18 | not predictions |

   The spelled-group differences: incuosions, susnuehannah, escapedo, reuuire, and two groups whose last letter turned out to be the next pair (assembl+y, repairin+g). The imprint line 29 of the key, inferred before, gave principal (twice), Irwin, plan and new exactly. The cipher's repeated "to Pines Creek" is in neither clear copy.
5. **After the test** (12 Nov): 39 new code associations from the 25 Sep letter (`postclear/new_associations.tsv`), marked as post-clear and untested. Five codes of the 6 Sep alignment that the frozen table did not carry (1-18, 6-6, 18-1, 29-9, 41-9) all agree with their 25 Sep readings; that is an observation after the fact, not part of the test.
6. **Packaging** (13 Nov): this folder; `verify.py` re-checks the freeze hashes, regenerates all 200 predictions from the key and table, and recounts the score and the spelling figures; `measure_strict.py` gives the strict read figures below. `docs/_validate.py` on `validation.tsv` (word codes and spelled letters of all three letters, 1089 read tokens): reading -2.037 against random keys -3.163 (z 16.0) and the shuffled refit best -2.155: verdict pass. The code values were fitted to these same letters, so this shows that the aligned values read as English, not that they are held out; the held-out evidence is the 25 Sep test. The package scripts `preclear/check.py`, `predict.py`, `transcribe.py` and `postclear/score.py` are kept as run on 12 Nov; they expect the workspace paths and the page images, so `verify.py` is the check to run in the repository.

## Reading

- Clinton 22 Feb: Chief Justice William Smith's intelligence that the Americans plan to invade Canada, Lafayette gone to France to propose it; George Rogers Clark to go down the Ohio and up the Wabash against Detroit in the spring; a report that Congress has agreed to give Canada to France. Cipher-order reading `clinton_1782-02-22/CIPHER_READING.md`; clear text `CLEAR_COPY.md`.
- Carleton 6 Sep: approves Haldimand's handling of the Vermonters, regrets the Indian raids, will not go to Quebec; Pigot's fleet arriving. `carleton_1782-09-06/reading.md`.
- Carleton 25 Sep: two expeditions planned into the Indian country, Potter from Fort Muncy towards the Seneca country and Irwin from Fort Pitt towards Lake Erie; Paterson in Nova Scotia ordered to assist Quebec; Washington's army at Verplanck's Point; L'Aigle taken in the Delaware. `carleton_1782-09-25/reading.md`; clear text `postclear/CLEAR_COPY.md`.

The texts are English, so there is no translation. Strict figures (`measure_strict.py`: a unit counts only when the key and table give the clear-copy word unchanged; spelled mismatches, the unread unit, units under glare and every occurrence of a code with conflicting readings are not counted): Clinton 237 of 268 (0.884), 6 Sep 103 of 109 (0.945), 25 Sep 171 of 182 (0.940).

## Who read these before us

- **At the time**: the clear texts are period copies kept with the ciphers at Quebec. Clinton's is the sender's own clear quadruplicate ("sent in Cypher overland"); the Carleton clear texts are entered in Haldimand's letter register B.146 ("(in Cypher)") and as a "Copy" in B.148 p. 102 whose margin points to the cipher transcriptions. Whether Haldimand's secretaries deciphered the Carleton letters or received clear duplicates is not established here. Either way the messages were read in 1782, and everything we read rests on those copies.
- **The Canadian Archives copyists** of the 1880s transcribed the cipher figures and the clear texts and cross-referenced them; all our readings are of their copies.
- **In print**: Douglas Brymner's calendar of the Haldimand Collection prints English summaries, not full texts: Report on Canadian Archives 1887, calendar of B.148 (the Clinton letter of 22 Feb with "The cypher of this letter. 11"; the Carleton letter of 25 Sep at p. 102), and Report on Canadian Archives 1885, calendar of B.146 (the 6 Sep letter, "Approves of his course with the Vermonters"). We found no full printed text of any of the three in the sources checked (both calendars in OCR). Not checked: the Historical Manuscripts Commission's Report on American Manuscripts in the Royal Institution (the Carleton Papers, now TNA PRO 30/55, which hold another copy of the 6 Sep letter, Am. MSS vol. 47 no. 9) and the Colonial Office copy (CO 5/107 p. 113) or any edition of it.
- **Modern**: Brice Dudout pointed in issue #359 (9 Nov 2026) to Clinton's line-column cipher of 22 Oct 1779 in B.147 with its clear copy and a partial key; that is the earlier, all-spelled stage of the same correspondence. We found no earlier identification of the Army List page or reconstruction of the 1782 word codes.

What we add: the reconstructed code table and Army List spelling over all three letters, and the pre-registered prediction of the 25 Sep letter.

## Catalogue and leads

Not in `catalogue.json` (items 781 and 783 are Clinton-Cornwallis photostats in the Clements Library, different letters). It attaches to waiting lead **1137** (Carleton Papers, TNA PRO 30/55: Clinton, Haldimand, Cornwallis and Leslie letters in cypher, 1779-1782), whose Carleton side this is, and whose 1779 Clinton-Haldimand item Brice Dudout pointed to (#359). Lead 1136 (Cornwallis Papers, PRO 30/11) is the southern Common cipher of 1780-81, a different system.

## Remaining gaps

- 43-19 read hundred in Clinton's letter and thousand in Carleton's 25 Sep letter; the two copies agree on the figures - blocker: needs-physical-access (British Library Add MS 21808 originals, to tell a copying slip from a code conflict)
- Clinton 22 Feb, the glare strip on p. 11B column 4 (to [?]duce it that engagement by) and the prefix of reduce - blocker: illegible (photographic defect on the LAC film; original needed)
- spelled groups that differ from the clear copies (Clinton intllligent, newyhrk, storis, hggreed; 6 Sep dit; 25 Sep incuosions, susnuehannah, escapedo, reuuire) - blocker: needs-physical-access (digits or the special q mark in the originals)
- codes with more than one reading across the letters (9-8 has/have, 13-14 in/on/near, 2-5 engagement/French, 46-9 just/been, 9-19 this/the, 11-1 an/any, 5-22 who/whose/whom) and the provisional 23-6, 49-9, 2-2 - blocker: open-codes (the printed word list is not identified; a headword list would settle inflection and digit slips)
- the printed word list behind the codes - blocker: no-key-material (no candidate book found; `clinton_1782-02-22/DIFFERENCES.md` lists the coordinates any candidate must fit)

## Escalation

- [x] siblings: the 6 Sep, 22 Feb and 25 Sep letters worked together; Haldimand's 1778-81 Army List letters in B.147 used to identify the spelling key (12 Nov 2026)
- [x] clear-pages: clear copies located for all three (B.148 pp. 8-9, 12, 102-103; B.146 pp. 50, 54)
- [x] known-keys: Army List title page key (Haldimand's key sheet, B.147 pp. 402-405) applied unchanged
- [x] print: Brymner's 1885 and 1887 calendars checked (summaries only); HMC Royal Institution calendar and CO 5/107 not checked, listed above
- [x] key-rebuild: code table rebuilt from the clear copies and tested on a held-out letter (56 of 58)
- [n/a] retry: the open pieces need the British Library originals or the printed word list, not another pass over the same copies

## Log

- 2026-11-12: Army List key identified on Haldimand's 1778-81 letters; 6 Sep 1782 aligned; Clinton 22 Feb collated in full; freeze; 25 Sep test (Andrew Beling, with AI agents).
- 2026-11-13: folder assembled from those packages, strict figures measured, profile and validation (Andrew Beling, with AI agents).
