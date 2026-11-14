# Anthony Morris to James Monroe, Cadiz/Madrid 1813-15: the State Department code with its blocks reversed

Status: written up 12 Nov 2026 (`docs/morris1813.html`).

Thirteen coded texts of 1814-15 on NARA M31 roll 14 are read here with the State Department code (Weber's WE028,
the = 1385), which Morris's copy numbers with its sixteen blocks of 100 in reverse order. Class: read in part.
Method: read after matching with key from external sources. Provenance: contributed (WAINUT, PR #114: the block
reversal and frame 0039; Andrew Beling, PR #200 and PR #415: the key sheet and ten letters). Two short pieces were
added at the integration of 12 Nov 2026. The state of each text, the counts and the corrections are in
"Integration check (12 Nov 2026)" below; that section is the latest word where it differs from the older ones.
The word counts and the state of each text were changed once more on 14 Nov 2026, when the sign 370 was taken as
punctuation: the figures in force are in "The sign 370 on the image (14 Nov 2026)".
Sections 1 to 6 are the record of the first contribution (27 Oct 2026), which used the table rebuilt in
[`../jqa`](../jqa/NOTES.md) and read frame 0039 at 0.678; the reading of frame 0039 was replaced on 31 Oct 2026
(PR #200, 0.965 of the words).

Since 14 Nov 2026 this folder also holds three letters of Governor William C. C. Claiborne to James Madison of 1805-06
(NARA T260 rolls 7-8), written in a copy of the same code with the same reversed blocks, in `claiborne/` (Brice Dudout,
PR #564 and PR #581; folded in under one key, one entry). Their texts are Jacob Wagner's decipherments of the time; that
part is still in progress and is not counted in the figures above. See "Claiborne's letters of 1805-06" at the end.

Catalogue 650. Contributed by WAINUT (https://github.com/WAINUTAI), a Dutch AI company. The work was done with AI
language-model agents. The transcription of frame 0039 was made from the NARA image; a second agent re-read a quarter
of the groups blind against the image and re-tested the block order with its own code.

## 1. The document

- **Source.** NARA RG 59, Despatches from US Ministers to Spain vol. 12 (28 May 1813 - 13 Apr 1816), microfilm M31
  roll 14 ([naId 188606645](https://catalog.archives.gov/id/188606645)). Anthony Morris was the US agent at Cadiz and
  Madrid in 1813-15. Per the catalogue, code runs on frames 0036-0039 (a triplicate, Cadiz), 0050, 0052-0057,
  0124-0125 and 0191-0192, about 3,000 groups in all.
- **The page worked here.** [Frame 0039](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-014/M31-014-0039.jpg),
  headed "4": 26 written lines, all code except a few phrases written in clear in lines 1-6 ("would induce them to",
  "an offer was made by them", "the intention of holding it", "take place"). It begins and ends in mid-sentence.
  It carries no date itself: the dateline, Cadiz 4 January 1814, is on frame 0038, and the page runs on from it. L1-8 are the end of that cover letter (in clear on M37 roll 2 frames 395-396) and L9-26 the start of the proposal it enclosed (in clear on frames 0059-0060); see `beling/`.
- **No contemporary decipherment** is on the frame, and the catalogue found none in the OCR of the neighbouring
  frames.

## 2. The code and the key

The groups run 1-1600 with marks under some of them, as in the JQA-type syllable codes. The catalogue found that the
signature groups do not match the JQA table (the = 1385) read directly; 285 and 76 are Morris's commonest groups.

**Morris's copy is the JQA table with its blocks of 100 in reverse order.** Each block keeps its inner order:

    Morris 100*i + r  (i = 0..15, r = 1..100)   =   JQA 100*(15 - i) + r

So Morris 1-100 = JQA 1501-1600 (76 of, 1 a, 92 on), 101-200 = 1401-1500 (126 in, 140 it), 201-300 = 1301-1400
(285 the, 284 that, 299 this), ... 1501-1600 = 1-100 (1590 should, 1549 United States, 1521 Minister).

This folder has no code table of its own. `profile.json` names `../jqa/code_table.tsv` as its key file, used unchanged,
together with `block_map.tsv`, the sixteen rows of Morris's block order. `decode.py` reads both. Nothing in `../jqa` is
changed.

**How it was found.**

1. 220 number-to-value tables in the repository (main and the open WAINUT pull requests) were applied directly.
   None fits (best function-word share 0.11). This was done with the solver's working script `score_all.py`, which
   parses every number-to-value mapping in the key, code and pairs files and scores coverage and function words; it
   is not included in this pull request, so this step cannot be rerun from the PR alone. `decode.py --controls`
   reproduces the result that matters: the JQA fit under `block_map.tsv` against random block orders.
2. Constant shifts against the US tables: the JQA table at +1100 stood out (function-word share 0.25 against 0.03
   for the next tables), because one block of 100 lines up.
3. Best offset per Morris block: the busy blocks (Morris 1-300) gave +1500, +1300, +1100, which suggests the full
   reversal.

**What supports each block (corrected by the verification).** The first round said that the per-block best offsets
follow the reversal on their own. That was overstated. On function words alone, the reversed block is the best one
for only **8 of 16** Morris blocks (1-300, 401-500, 601-700, 801-1100). The sparse blocks prefer other offsets. The
other eight rest on the pattern and on context. A context test supports them: for each Morris block, every JQA block
is tried with the other blocks kept as in `block_map.tsv`, and the decoded word pairs touching the block are counted
as word bigrams of Ford, *Writings of J. Q. Adams* vols 3-4 (in `../jqa`). The reversed block ranks first in **15 of
16** blocks (once tied). Morris 701-800 and 1201-1300 rest on only 2 bigrams each. Morris 1501-1600 ranks second (3
bigrams against 4), but reads in context: 1590 should ("should a change in the [Regency] take place"), 1549 United
States, 1521 Minister (ad-Minister-ation). The `basis` column of `block_map.tsv` records this per block.

## 3. Transcription and decryption

- **Transcription** (`morris1813_transcription.txt`): 554 groups in 26 lines, read by eye from the full frame and
  enlarged crops (lines 1-6 and 10-12 in a first pass, the rest in a second). Groups of one word are joined by dots,
  as Morris writes them.
- **Blind re-reading.** A second agent re-read 144 groups (lines 3, 7, 9, 13, 18, 24 in full, parts of 12 and 17)
  without looking at the first transcription: 140 agree (97.2%). The three clear disagreements are applied here:
  L9 **721** (first read 724), L9 **13** (first read 131), L24 **608** (first read 108). Each turns a broken syllable
  into the expected one: dem-o-cre-at-ic (democratic), ad-Minister-ation (administration), am-bass-ad-or
  (ambassador). The second agent read 721 before it looked up the value. This is a blind check on the key. L24 518 may
  be 548; it is left as 518[?]. About 74% of the groups were read once only.
- **Decryption** (`morris1813_decryption.txt`, output of `python decode.py`): each group as morris>jqa=value/grade,
  then the words with their syllables. **506 of 554 groups have a value** in the table. The 48 without one are 36
  distinct groups: open slots of `../jqa/code_table.tsv`, one group out of range (5127) and one cut by the frame edge.

## 4. The reading

`morris1813_reading.md` gives the page as sentences, with every hole marked. It is English, so no translation is
needed. A sample (L9-L10):

> The democratic government of the United States, under the administration of the Frenchified Señor Jefferson [908]
> Ma[d]ison, not only [385] the [?European] war, but also before that England ...

Lines 3-5 (with the clear phrases): "... to counteract any [1577] of the British in that quarter. An offer was made
by them last year to send [1579.401] there under the [1311.1246] of preserving the territory to Spa[in], but probably
with the intention of holding it ..."

**Read in part, and only just.** The page builds sentences in stretches, but there are holes in most sentences.
read_share is **0.678** (`research/reading_audit/v2_score.py`, hole rate 0.322, every open group, context reading and
supplied letter counted). Of the 32 sentence units of the `## Reading` section, 4 are clean (v2_score.py);
`docs/_check_reading.py` over the whole file, notes included, gives a clean share of 0.467 ("marginal"). The main
context readings, all marked `[?word]`: 670 = Floridas (5x, no value in the table; it fits each occurrence: "an integral part
of", "the provinces of both"), force (the table has france), Regency, colonies, Peninsula, overwhelm, importunities,
treason, revolutionary, effect, threatened.

**What the page says.** It deals with Spain's Floridas: a British offer "last year" to send [troops] there under
cover of preserving the territory to Spain, "but probably with the intention of holding it"; a change in the Regency
once the Cortes are organized; the "democratic government of the United States under the administration of the
Frenchified Señor Jefferson [and] Madison"; the separation of Spain's colonies from the mother country; the
insurrection of [West?] Florida and Baton Rouge; the claim that the territory belongs to Spain and was "an integral
part of" the Floridas; something "conceded" concerning "both Floridas" under certain conditions; the treason of a
governor; the ambassador of a revolutionary government. The tone ("Frenchified") suggests Morris is reporting
Spanish charges against the United States. Whose words they are cannot be told from this page alone.

## 5. Controls (`python decode.py --controls`)

On the 552 groups 1-1600 of the frame:

- `block_map.tsv`: coverage 0.917, function-word share 0.353. Identity (no block change): 0.630 and 0.058.
- 20,000 random orders of the 16 blocks: function-word share median 0.062, 99.9th percentile 0.250, max 0.297. The
  reversal beats them all. Most of this signal comes from the three busy blocks, Morris 1-300.
- Per block: function words alone 8 of 16; Ford bigrams 15 of 16 (section 2).
- Repeats: 76 285 (of the) 15 times as adjacent groups (285 occurs 46 times, 76 occurs 28 times); 329.937
  govern-ment 3x; 279.140.608.953 ter-it-or-ty and 126.1295.1018.133 in-sur-rect-ion 2x each as identical group
  strings. (The first round said 25x, and 3x each for territory and insurrection; the third instances need L19 479
  read as 279 and L17 132 as 133, which are plausible but not checked.)
- 364 = JQA 1264: in the Ellis 1839 alignment (open PR #107, `targets/ellis1839/ellis1839_pairs.tsv` there) 1264 is
  the full stop. Here 364 stands where a sentence ends in lines 12, 17, 21 and 24 (once, in line 8, inside an
  unread word). 364.370 occurs 3 times, so 370 (= JQA 1270) may be part of the stop sign.

## 6. Prior work

- The catalogue calls the code unidentified ("a code no table here matches"). The block reversal is not recorded in
  the repository, and we found no publication of it.
- **Not checked, so the content cannot yet be called new:** W. R. Manning, *Diplomatic Correspondence of the United
  States concerning the Independence of the Latin-American Nations* (1925), vol. 3, part XIII "Communications from
  Spain". This page is about the separation of Spain's colonies and an insurrection, Manning's subject; if the
  Department deciphered the despatch on receipt, Manning may print it in clear.
- **Woolfley prints two of the coded passages.** H. L. Dufour Woolfley, *A Quaker Goes to Spain* (2013), read in part
  (pp. 64-66, 74-80, 97-98, 180 and notes on pp. 187-198; Ebook Central page numbers, printed pages not checked), quotes
  4 April and 11 April 1814 on p. 78, citing Dispatches 12 and 13 (notes 30, 32-33). So neither is unpublished.
  Differences from the decode in `beling/`:
  - 4 April: Woolfley "paid in articles", decode "paid in the articles"; "$10,000", "ten thousand dollars";
    "great hope", "great hopes".
  - 11 April: Woolfley "in short time", decode "in a short time"; "Not having the satisfaction", "Not having had the
    satisfaction"; "my discretion", "a discretion"; "in the present circumstances", "under present circumstances".

  The decode's groups at the 11 April places read directly on the image (1 a, 344 had, 1180 under), so he may have
  worked from another text or edited. He also gives the = 285 and last = 157 (p. 65), which fit the reversed key.
  11 May 1814, the coded part of 27 January 1815 and 24 March 1815 were not found in what was read.
- **Dispatch 26.** Woolfley's note 50 (p. 191) calls Dispatch 26 of 27 January 1815 the one dispatch missing from State
  Department files. It is at M31 roll 14 frame 0075, headed "No 26 Triplicate", and its plain text fits his description.
- Three web searches found neither the passage nor a decipherment.

## Catalogue 650: five more letters (Beling, 11 Nov 2026)

Andrew Beling, with AI agents. Five more of Morris's letters to Monroe on M31 roll 14, from frames catalogue 650 left
open, read with the State Department code (WE028, the = 1385) under the block reversal. The key is
`beling/key/codebook_M97_13_transcription.csv`, unchanged since PR #200. Files are in `beling/letters/`, one folder per
letter; the method, scripts and tests are described in `beling/README.md`.

**What the frames are.**
- **No. 18, Seville, 20 September 1814**: 0112-0113 (Duplicate, the base text), 0117-0118 (Triplicate, with the date
  in clear under the coded heading), 0129 (a copy wrongly headed "No 19"; its continuation, 0130, is too dark to read).
- **No. 19, Madrid, 27 October 1814**: page 1 in clear on 0137 (filmed again on 0138; copies on 0146, 0148). The coded
  passage is on 0139, which the catalogue groups with No. 18, with copies on 0147 and 0149.
- **No. 24, Madrid, 30 December 1814**: top of 0220, wholly in code (number and date in the coded heading). Copies on
  0205 and 0196; 0196 has a clerk's decipherment between the lines.
- **No. 25, Madrid, 6 January 1815**: coded paragraph at the foot of 0220 and the top of 0221. Another copy on 0174 is
  deciphered in full by a clerk.
- **No. 28, Madrid, 12 May 1815**: 0209 (Duplicate) and 0210 (Triplicate).

**What they say.**
- **No. 18.** The Inquisition was restored by a decree of July, against the wishes of all the ministers, through the
  king's confessor and the papal nuncio. The Cortes' decrees on the tobacco and other monopolies were repealed. There
  were arrests and discontent, and disturbances at Cadiz. The treasury was being refilled by "benevolences" and forced
  loans. The king had "thrown himself entirely into the arms" of the nobility and clergy. Nothing had changed on Florida
  and Louisiana. A report had the Marquis de Casa Yrujo as the next secretary of state.
- **No. 19.** Page 1, in clear, says Morris came to Madrid on the 9th, after reports of British troops landing in
  Florida, and called on the Duke de San Carlos on the 13th. In code: the duke received him without cordiality and has
  not answered; the press is guarded against anything unfavourable to the government or to the British government,
  and the post office against the introduction of foreign papers.
- **No. 24.** Morris reports, from a source he trusts, that the Council of State is preparing a report to the king
  recommending a declaration of war on the United States over its proceedings on Louisiana and Florida (a report in
  preparation, as he was told; not a decision). 47,000 soldiers and 5,000 officers have
  come back from France as prisoners of war; Spain has at least 160,000 men under arms; two expeditions of ten thousand
  each are fitting out at Cadiz, under Field Marshal "Linan" for Mexico and General "Murillo" for Buenos Aires, to sail
  early in January. Manning vol. 3, p. 1604, names a Field Marshal Linan as commander-in-chief in Mexico at the time of
  Iturbide; "Murillo" is not identified here.
- **No. 25.** In clear, Morris forwards Erving's letter of that day with congratulations "on this happy occasion".
  Woolfley (Ebook Central p. 106) says it was the first report of the peace signed at Ghent to reach Madrid. In code: the
  news, received with great surprise, may change the "intended measures" of his last letter (No. 24); new powers are to
  be sent to Onis; on Erving's instructions Morris has had no communication with the Spanish authorities on it.
- **No. 28.** Things stand as in his letter of 24 March. There has been no communication with the government since
  Erving's letters, but "the glorious result of the expedition against N. Orleans" must have changed the court's views.
  In clear he encloses the government's only public document on the return of the "Ex-emperor".

**Read share.** `beling/scripts/read_share.py` counts coded groups (heading, body and signature), less those unread or
read only by inference: No. 18 0.981 (486 groups), No. 19 0.955 (156), No. 24 0.980 (205), No. 25 1.000 (98), No. 28
1.000 (90). This is a count over groups, set from hand lists of the unread and inferred places, not the
`research/reading_audit/v2_score.py` figure. `v2_score.py` on the text of each `reading.txt` (notes and headers left
out) gives hole rates of 0.029, 0.050, 0.046, 0.015 and 0.012. `docs/_check_reading.py --file` on the same text gives
clean shares of 0.842, 0.917, 0.818, 0.923 and 0.929. On the whole files, notes and headers included, it gives 0.689,
0.610, 0.652, 0.718 and 0.778, because those parts are full of frame numbers, groups and names.

**Tests against the clerks' decipherments.** Share of the clerk's letters matched in order by the decode with key values
only (no mark rules, no context), against 200 shuffled keys:

| Letter | Clerk's copy | Real key | Shuffled best | Shuffled median |
|---|---|---|---|---|
| No. 24 | frame 0196 | 0.904 | 0.342 | 0.215 |
| No. 25 | frame 0174 | 0.945 | 0.343 | 0.201 |

Neither test is fully blind. For No. 24, the 0196 decipherment was not read before transcribing, but the frame was seen
at low resolution while frames were being identified and a few words were glimpsed; the clerk's text, on very dark film,
was read after the decode was made, so that reading may lean toward the decode. For No. 25, the 0174 decipherment had
been viewed before the numerals on 0220-0221 were transcribed; the digits were read from 0220-0221 only, and none was
changed for sense.

**Single readings worth a look.**
- 145 with a stroke (key "June") stands for "relative" in Nos. 18 and 24; the 0196 clerk writes "relative" at the No. 24
  places. 131 (key "into") must be "re" in No. 18.
- 1569 is "December" in the No. 24 heading and "United States" in its body (the clerk: "U States"), the misfit already
  noted on 27 January 1815. Morris's usual United States is 1549.
- No. 18 has 1351 (code 251, "son") with the doubling hook for "soon". This is one more place where Morris 1351 reads
  as son. It bears on the code 251/257 question still open from PR #200 (Daniel Bourdeau's merge comment) and does not
  settle it. `../jqa/code_table.tsv` is not changed here.
- Unexplained: 1457 ("mou") and 1040 ("embass") in No. 18; 572.1101 and 575.1060 in No. 19 (the second left unread);
  1150 in No. 19. The opening 593.813 of No. 24 (shall, R) is unread, perhaps "Sir". [370], the sign after full
  stops, is still unidentified.
- No. 18 113.06: the Duplicate has 1303, the Triplicate 1363; 1363 gives "understanding" and is adopted, a choice between
  copies guided by sense.

**Prior print.**
- *Woolfley.* First searched through Google Books snippets, then on 11 Nov 2026 in the Ebook Central full text (UMD),
  whose page numbers are used here and in section 6. Google's page numbers are 16 lower (Ebook Central 99 = Google 83).
  - **No. 18, pp. 98-99.** Woolfley calls it a "heavily encoded" dispatch. He quotes three of the coded passages and
    paraphrases the Inquisition one (confessor, papal nuncio):
    - "Numerous arrests ... daily becoming more universal": his "more" confirms our [?more].
    - "The king has indeed thrown himself entirely into the arms of those two classes ... previous to the Revolution in
      1808" (his note 71). Our decode has "these" (292) where he has "those".
    - "there does not, I think, subsist a sufficient understanding between the Spanish and the English cabinets to
      render a cordial union between them on this ... very probable" (note 72). Our decode has "sufficiently good" and
      "these or any other subjects". At 113.06 the copies differ (1303/1363), and our choice there was guided by sense.
  - **No. 19, p. 100.** He quotes the sentence on the duke's reception (note 74), word for word as decoded.
  - **No. 24, p. 106.** He quotes the Council of State sentence (note 93), word for word as decoded, apart from an
    ellipsis and "[in preparation]" for "preparing". It has "United States" and "relative", where our reading has
    [?United States] and [?relative]. He also summarizes the 160,000 men and the two expeditions.
  - **No. 25.** On p. 106 he gives the arrival of Erving's news on 6 January, but the coded sentences were not found. Full-text
    searches for "intended measures", "new powers" and "great surprise" found nothing.
  - **No. 28.** Not found ("glorious result": no hit).
  - Yrujo: no hit.

  Woolfley evidently worked from clear copies, probably the HSP Morris papers he cites, so his quotations are an
  independent check on the decode wherever they overlap: they agree, apart from the differences listed under
  No. 18. Parts of Nos. 18, 19 and 24 are therefore in
  print. The searches were by phrase, so a miss does not show that a passage is absent.
- *Manning* (1925) vol. 3: the five passages were not found. Two web searches found nothing more; a Google Books search
  for the No. 24 Council of State sentence found only Woolfley.
- Not checked: *American State Papers*, Foreign Relations; *Papers of James Monroe* vol. 7; the HSP Morris papers.
  None of these passages should be called unpublished or new.

**Limits.**
- One reader for all five letters; no second reading of the numerals or of the readings.
- No `reading_review` when the pull request came in; one was recorded at integration (12 Nov 2026), a model reading, not a person's.
- The two tests are not blind (above), and the other three letters have no contemporary decipherment to test against.
- The unread and inferred lists behind the read shares are a judgment.
- Left unread by the pull request: a wholly coded document on 0115-0116 (deciphered copy on 0169-0170; a further copy on 0201) and three coded lines on 0111. Both were read at integration (see "Integration check").

## Integration check (12 Nov 2026)

PR #415 was verified independently before integration, then integrated; this section records both.

**What reproduced.** The three scripts were read (standard library, no network, no writes) and run. The five
line-by-line decodes are byte-identical; the key hash and `beling/SHA256SUMS.txt` match. A decoder written from the key
CSV alone agrees on all 1,035 groups. The 1,600 rows of the reversal column agree with the block formula. The two
clerk tests reproduce: No. 24 against frame 0196 0.904 (shuffled best 0.342, median 0.215), No. 25 against frame 0174
0.945 (0.343, 0.201). Group counts 486, 156, 205, 98, 90. On the images: all 205 groups of No. 24 agree with frame 0220
at full resolution (the last is 1551 or 1557, as flagged); 13 of 13 on the first line of No. 25; about 110 groups of
No. 18 on frame 0112 and two lines of No. 19 on frame 0139 with no difference. Frames 0113, 0221, 0209, 0210 and the
other copies were not viewed. The statement that the numerals were frozen before decoding is by the contributor's
record: the pull request is a single commit.

**Corrections made.**
- *Unflagged inferences.* In No. 18, "liberal" and "liberality" are decoded li-er-al (780.400.35); in No. 19,
  "approbation" is decoded ap-pro-bat-ad (975.1319.209.13). They are now marked `[?...]` in the readings, like the
  supplied "delay[ed]" and "[going]" already were. `beling/SHA256SUMS.txt` carries the new hashes of the three reading
  files changed (Nos. 18, 19, 24).
- *One counting rule.* `word_share.py` (new, in this folder) counts the coded words of each letter reading and the
  holes among them: an unread group, a guessed `[?word]` or a word with supplied letters is a hole. Output in
  `word_share.txt`:

  | Text | Coded words | Holes | Share | State |
  |---|---|---|---|---|
  | No. 12, 4 April 1814 | 181 | 5 | 0.972 | read |
  | No. 13, 11 April 1814 | 74 | 4 | 0.946 | read in part |
  | No. 14, 11 May 1814 | 157 | 6 | 0.962 | read |
  | No. 17, 21 June 1814 (three lines) | 35 | 3 | 0.914 | read in part |
  | No. 18, 20 September 1814 | 312 | 13 | 0.958 | read |
  | No. 19, 27 October 1814 | 106 | 6 | 0.943 | read in part |
  | Cevallos to Morris, 20 November 1814 | 312 | 12 | 0.962 | read |
  | No. 24, 30 December 1814 | 131 | 4 | 0.969 | read |
  | No. 25, 6 January 1815 | 74 | 0 | 1.000 | read |
  | No. 26, 27 January 1815 | 46 | 2 | 0.957 | read |
  | 24 March 1815 | 779 | 18 | 0.977 | read |
  | No. 28, 12 May 1815 | 71 | 1 | 0.986 | read |

  Frame 0039 stays at 0.965 (Andrew Beling's count by the same rule, PR #200; a recount here gives 353 words, 13
  holes, 0.963). All thirteen texts: 2,631 coded words, 87 holes, 0.967. The contributor's figures for the five
  PR #415 letters, 0.981, 0.955, 0.980, 1.000 and 1.000, are shares of groups (`beling/scripts/read_share.py`), not of
  words. The verifier's word count before the three inferences were marked was 0.965, 0.953, 0.978, 1.000, 1.000.
  The target as a whole is read in part: three texts are under 0.95 and the open places are listed under Remaining gaps.
- *Which readings are new.* Nos. 24 and 25 have a clerk's decipherment on another copy, so there the reading confirms
  an existing decipherment. Nos. 18, 19 and 28 have none on the frames. Woolfley (2013) quotes parts of Nos. 18, 19
  and 24, so nothing is called unpublished.
- *No. 24.* The decode gives: "a report is pre-par-ing by the council of state to H . M . re-com-end-ing a
  dec-lar-ation of war against the [1569] four-nd upon the ground general-ly of our proceed-ing relat-[145] to
  [lo]-is-i-an-a and Florida". Group 1569 is "December" in the key and in this letter's own heading; "United States"
  rests on "our proceedings", on the clerk's words on frame 0196 ("against the U States", read by the verifier after a
  contrast stretch) and on Woolfley's quotation. Morris reports, from a source he trusts, that a report recommending
  war was being prepared: hearsay about a recommendation, not a decision.
- *No. 24, opening.* 593.813 (shall, R) is what frame 0220 has. The letter of 24 March 1815 opens 598.813 (si, R),
  "Sir", so 593 is probably a slip for 598. It stays `[?Sir]`.
- *Profile.* The five PR #200 letters were missing from `documents` and `outcome.texts` and are added; a
  `reading_review` is recorded on every letter text (a model reading at integration, not a person; frame 0039 keeps
  Andrew Beling's); `fraction_read` and `codes_open`, which still described frame 0039 alone, are recomputed.

**Two pieces added at integration** (one reader, the integrating agent; same key and decoder, unchanged):
- *Frames 0115-0116* (`beling/letters/1814-11-20_Cevallos/`, 621 groups) are a copy, headed "Copia", of a note in
  Spanish from Pedro de Cevallos to Morris, dated Palacio, 20 November 1814, spelled out with the syllables of the
  English code. It answers Morris's paper of the 17th: the king resents the conduct of the United States; the
  appointment of Erving does not repair the refusal to recognise the minister Spain sent in 1809; satisfaction must
  begin with that recognition; Morris may still deal with Cevallos on matters between the two states. A clerk wrote
  the Spanish between the lines of the copy on frames 0169-0170, and that copy was seen at reduced size before the
  numerals were transcribed, so the transcription is not blind and the reading confirms a contemporary decipherment.
  One group was corrected after decoding with 0169 in view (1301, particular, first read 1307). The clerk writes
  "elev son" and "ep for" where the sense wants "elevado" and "época": those are slips in the coding. The copy on
  0169 leaves out ten groups that 0115 has ("hecho ahora en ... con igual"). Word share 0.962, with a translation
  (`translation.txt`).
- *Frame 0111* (`beling/letters/1814-06-21_No17/`, 53 groups) is the end of No. 17, Seville, 21 June 1814, nine pages
  in clear: "In the [?present] most unexpected state of things, therefore, I have thought it most [?prudent] to remain
  quiet until I shall have the satisfaction of hearing from you." The coded heading on frame 0107 was read at reduced
  size.

**Print, 12 Nov 2026.** Two web searches found no printed text of the Cevallos note or of the No. 24 sentence. One
result summarises an annotation in the *Papers of James Madison* (Founders Online, Madison/03-08-02-0355): Erving's
letter to Monroe of 4 December 1814 enclosed a copy and translation of Cevallos's note of 20 November to Morris. The
page could not be opened here, so this is not checked.

**Related targets.** [`../jqa`](../jqa/NOTES.md) and `../ellis1839` use the same code in its usual numbering.
[`../poinsett1813`](../poinsett1813/NOTES.md) and [`../king1797`](../king1797/NOTES.md) are other State Department
codes; king1797 tested the WE028 sheet of this folder against its own code in both block orders: no value in common.

**Catalogue.** Entry 650 had been narrowed on 3 Nov 2026 to No. 18, No. 28 and the despatch on frames 0220-0221. All
three are read here, so the entry leaves the catalogue.

## Proposed table changes (for `../jqa/code_table.tsv`, not applied)

None is proposed from this page alone. Candidates to test on more Morris text: 670 Florida(s) (JQA 970), 1566
colonies (JQA 66), 361 comma (JQA 1261, as in Ellis 1839), 652 the figure 1 (JQA 952). 721 (JQA 821) dem is grade I
in the table (a slot inference); it fits here (democratic).

### Claims review by a second reader (12 Nov 2026)

- "relative" in No. 24 (145 with a stroke; the key value is "June") is now marked [?relative] and counted as a hole,
  as the same group is in No. 18: No. 24 is 131 words, 4 holes, 0.969; all thirteen texts 2,631 words, 87 holes, 0.967.
- Frame 0039: the recount used in the total is 353 words, 13 holes, 0.963; 0.965 is the contributor's count.
- The mechanical decode of frame 0039 shown on the page is the first one, of 27 October, made with the rebuilt Adams
  table; the letter decodes use the code sheet file.
- The mark example on the page corrected: dispose with one stroke, then -it-ion (140 = it).

## Independent verification by Brice Dudout (PR #570, 14 Nov 2026)

Brice Dudout (`VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) decoded the letters from
`beling/key/codebook_M97_13_transcription.csv` and the transcriptions alone: 1,707 of 1,712 groups equal
`line_by_line_decode.txt` (the five others are marks kept inside a value and the three catchwords of 24 March 1815), and
No. 13 from copy A gives its reading word for word. His count reproduces the twelve `word_share.py` figures exactly.
Re-run here: the same. `research/reading_audit/v10_relabel.py` gives higher figures for Nos. 13, 17 and 19 (0.966 to
0.971) only because it counts the heading, summary and notes in clear; the `word_share.py` figures stand.

**370.** He points out that `word_share.py` counts each `[370]` as an unread word, while on the key sheet 370 closes
the run of punctuation signs 361 to 370 (`, ; : . ! ? — ( ) "`; the first reading of the numerical sheet has "[PARAGRAPH
SIGN?]") and in the letters it stands after a full stop. Checked here in the key file and the transcriptions: the run is
as he says, and of the 21 places his script finds 19 follow 364 directly; the other two stand at the head of a line
(Cevallos 115.12, where the line before ends with 364, and No. 12 L10, before the coded signature). So 370 behaves as a
sentence or paragraph mark, not as a word. Leaving it out of the count gives No. 13 0.972 (72 words, 2 holes), No. 19 0.962 (104, 4) and
No. 17 0.941 (34, 2): Nos. 13 and 19 would cross the 95% bar, No. 17 would not.

**Not applied.** The counting rule of 12 Nov 2026 (an unread group is a hole) is kept, and with it every `read_share`,
the three texts under the bar and the totals. Changing it moves two letters up a class on a sign nobody has identified
on the image (the cell on M97 roll 13 frame 1057 was not viewed by him or here), so it is left to the repository owner.
370 itself stays in the gaps below either way.

## The sign 370 on the image (14 Nov 2026)

The repository owner asked for the check that the section above left open: look at the cell on the image and, if the
evidence holds, adopt Brice Dudout's point in one pass. Done here by the project; the observation is his (PR #570).

**The sheet.** Both frames of the code sheet were fetched from the National Archives Catalog, the way the M31 frames
are fetched (direct download, no bot check):
`https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M97/M97-013/M97-013-1057.jpg` (numerical sheet, 4304 x
3744) and `...-1056.jpg` (alphabetical sheet, 4288 x 3728). Both are bitonal film scans.

- *Numerical sheet (1057).* In the column 1201-1300 the cells 1261 to 1270 (Morris 361 to 370) hold no word or
  syllable. They hold, in order: a comma, a semicolon, a colon, a full stop, an exclamation mark, a question mark, a
  dash, a pair of round brackets, a double quotation mark, and in 1270 a small upright sign: an S-like stroke with a
  loop in the middle and a hooked foot, like a section sign (§). The d of "down" in the cell below (1271) runs into
  its foot, which is probably why it was first described as "z-like". 1260 is "having" and 1271 "down": the ten cells
  are a closed run between two words.
- *Alphabetical sheet (1056).* The last column, after X, Y and Z, lists the figures 0 to 9 and then the same marks,
  printed, in the same order, each with its number written beside it in ink: , 1261 ; 1262 : 1263 . 1264 ! 1265
  ? 1266 - 1267 ( ) 1268 " 1269, and an eleventh printed sign of the same shape as on the other sheet (a curl like a 2
  over a second curl), with a faint number beside it that fits 1270. The printed instructions for the marks under the
  figures begin directly below it.

So on both halves 370 is the last entry of the sheet's list of punctuation marks. Beling's transcription has it right
("[z-like glyph; unidentified]", first reading "[PARAGRAPH SIGN?]"); nothing in the key file is changed. Which mark it
is cannot be said for certain on this film: the shape fits a section sign better than a pilcrow, and the use (below)
fits either. Weber's print of WE028 was not seen.

**Where it stands.** One count, from the transcription files, one line per place (a place that stands in two copies
is counted once). 22 places in the thirteen texts; every one comes directly after the full stop 364.

| Text | Line | Position | Before | After |
|---|---|---|---|---|
| Frame 0039 | L12 | mid-line | ... mother country . | In summer of the year 1810 |
| Frame 0039 | L21 | mid-line (364 and 370 both marked doubtful) | ... insurrection mentioned . | In the month of June 1811 |
| Frame 0039 | L24 | mid-line | ... the said Floridas . | The ambassadors |
| No. 12 | L06 (second copy D07) | mid-line | ... means of this description . | I have waited |
| No. 12 | L10 | line head; L09 ends with 364 | ... yet appeared . | the coded signature |
| No. 13 | copy A, L5 | line end | ... to proceed . | (end of the text; copy B stops at 364 and has no 370) |
| No. 13 | copy A, signature line | after a second 364 | . | the coded signature |
| No. 17 | 111.03 | line end | ... hearing from you . | (end of the coded lines) |
| No. 18 | 112.08 | mid-line | ... the pope's nuncio . | Numerous arrests |
| No. 18 | 112.11 | mid-line | ... suppressed . | The government is |
| No. 18 | 113.04 | mid-line | ... revolution in 1808 . | No facts have |
| No. 18 | 113.09 | line end | ... secretary of state . | (words in clear), I have |
| No. 19 | 139.04 | mid-line; the line begins 364.370 | ... complied with . | It is very difficult |
| No. 19 | 139.08 | line end | ... foreign papers . | (end of the coded text) |
| Cevallos | 115.06 | mid-line | ... su real nombre . | El desaire |
| Cevallos | 115.12 | line head; 115.11 ends S . M . | ... S. M. | Por otra parte |
| Cevallos | 115.16 | mid-line | ... de Erving . | S. M. tiene |
| Cevallos | 115.21 | mid-line | ... Estados Unidos . | No obstante |
| Cevallos | 116.04 | mid-line | ... para ello . | Aprovecho esta ocasion |
| Cevallos | 116.06 | mid-line | ... muchos años . | Palacio a 20 de |
| No. 24 | 220.04 | line end | ... Louisiana and Florida . | The number of |
| 24 March 1815 | 124.25 (copy B 192.03) | line end | ... impropriety in it . | I have |

Per text: frame 0039 3, No. 12 2, No. 13 2, No. 17 1, No. 18 4, No. 19 2, Cevallos note 6, No. 24 1, 24 March 1815 1;
none in Nos. 14, 25, 26 and 28. That is 19 in the twelve letters and 3 on frame 0039. The earlier figures: 21 was
Dudout's script, which reads the `transcription.txt` files only and so counts 24 March 1815 twice (both copies), frame
0039 not at all and Nos. 12 and 13 not at all; 20 "in the letters" was a miscount of the 19 in `word_share.txt`; 22
was right. "19 of 21 follow 364" understated it: the two line heads also follow a 364, across the line break. With the
second copies there are 24 written instances (No. 12 second copy and 24 March 1815 copy B repeat theirs); copy B of
No. 13 drops the final one, which a copyist could do with a paragraph mark and not with a word.

**Verdict: punctuation.** A mark of the sheet's punctuation list, used after a full stop where a new sentence or
paragraph begins, before the signature and at the end of a coded passage. It is not a word.

**Applied.** `word_share.py` now leaves `[370]` out of the words and of the holes (the readings themselves are not
changed, and the contributors' files keep their own wording, "unread group"). This amends the counting rule of 12 Nov
2026 in one point only: an unread group is still a hole, but 370 is not a group that stands for a word. Output in
`word_share.txt`:

| Text | Coded words | Holes | Share | State | Before (370 as a hole) |
|---|---|---|---|---|---|
| Frame 0039, 4 January 1814 (by hand) | 350 | 10 | 0.971 | read in part | 353, 13, 0.963 |
| No. 12, 4 April 1814 | 179 | 3 | 0.983 | read | 0.972 |
| No. 13, 11 April 1814 | 72 | 2 | 0.972 | **read** | 0.946, read in part |
| No. 14, 11 May 1814 | 157 | 6 | 0.962 | read | same |
| No. 17, 21 June 1814 (three lines) | 34 | 2 | 0.941 | read in part | 0.914 |
| No. 18, 20 September 1814 | 308 | 9 | 0.971 | read | 0.958 |
| No. 19, 27 October 1814 | 104 | 4 | 0.962 | **read** | 0.943, read in part |
| Cevallos to Morris, 20 November 1814 | 306 | 6 | 0.980 | read | 0.962 |
| No. 24, 30 December 1814 | 130 | 3 | 0.977 | read | 0.969 |
| No. 25, 6 January 1815 | 74 | 0 | 1.000 | read | same |
| No. 26, 27 January 1815 | 46 | 2 | 0.957 | read | same |
| 24 March 1815 | 778 | 17 | 0.978 | read | 0.977 |
| No. 28, 12 May 1815 | 71 | 1 | 0.986 | read | same |

All thirteen texts: 2,609 coded words, 65 holes, **0.975** (was 2,631, 87, 0.967). The 65 holes are 5 unread or
unsettled groups (575.1060 in No. 19; 1520, 572.1001, 1466 and 1407 in the letter of 24 March 1815) and 60 words
guessed or with letters supplied (26 in the PR #200 letters, 24 in the other seven, 10 on frame 0039); the page and
README had said 58 and 59. In the profile, frame 0039's `read_share` is now this recount (0.971), with Andrew Beling's
0.965 named once as his; its state is not changed (it is a fragment reread with the clear copies in view).
`codes_open` goes from 3 open groups and 16 tokens to 2 and 2 (575 and 1060).

**The class does not change.** Nos. 13 and 19 are now read. No. 17 has two inferred words in 34 (0.941) and stays
read in part; one sure word more would not be enough either (33 of 34 is 0.971, so it needs one of [?present] and
[?prudent] settled: the blotted group on frame 0111 or another occurrence of 1159). The target stays read in part.

**One-digit rule not applied; a workable next step (claims review, 14 Nov 2026).** Three of the 65 holes are one
digit away from the sheet value the word wants: No. 13 `sour[?ce]` (510 cape for 516 ce) and `vis[?it]` (146 jur for
140 it), No. 24 `[?Sir]` (593 shall for 598 si before 813 R). The one-digit rule (README Conventions, 14 Nov 2026) asks
that the slip be seen on the image, so that it is the writer's slip and not a misreading here. The contributors'
transcriptions give 510 and 146 as written in both copies of No. 13
(`beling/letters/1814-04-11_No13/first_reader_line_by_line_both_short_letters.md`) and 593 on frame 0220, but the
project has not looked at the three places on the frames for this rule, so the rule is not applied and they are
counted as holes. Next step: look at the three places on the frames. If they are confirmed: No. 13 72 of 72, No. 24
128 of 130 (0.985), 62 holes in 2,609 words (0.976); the class does not change (No. 17 stays at 0.941).

**Credit.** The observation is Brice Dudout's (PR #570). The image check, the count and the change are the
project's. Andrew Beling's transcription of the sheet and WAINUT's block reversal are as before.

## Remaining gaps

- The exact mark that 370 stands for (22 places, each directly after the full stop 364) - blocker: illegible; its
  meaning is settled: it is the last entry of the punctuation list on both halves of the code sheet (seen 14 Nov
  2026) and is not counted as a word. The mark itself, a small S-like sign with a second curl, like a section sign,
  cannot be named with certainty on the bitonal film; Weber's print of WE028 was not seen.
- 575.1060 in No. 19, an adverb before "guards" - blocker: open-codes; se with two strokes + ti gives no word, and the
  three copies agree.
- Words read from context where Morris's group does not give the word (counted as holes) - blocker: open-codes;
  1569 for United States (No. 24, No. 26), 593.813 for Sir (No. 24), 145 with a stroke for relative and
  131 for re (No. 18), 1457, 1040 and 780.400.35 (No. 18), 209.13, 1150 and 572.1101 (No. 19), 1351, 681, 1450, 1037,
  1167 and 1060.1046 (Cevallos note), 1159 (No. 17), and the inferred words of the PR #200 letters and frame 0039. The
  key sheet is complete for these numbers: they are slips or private usages of the writer, and each needs another
  occurrence or a clear copy to settle.
- Despatch number of the letter of 24 March 1815; one blotted group on frame 0111 - blocker: illegible; the group is
  1310 or 1320. Copy A's coded number reads seventeen, Copy B's is overwritten. The catalogue's vetting reports a copy on
  frames 0206-0207 headed No. 27, not compared here.
- Anthony Morris Family Papers, Historical Society of Pennsylvania, Collection 2018-A - blocker: needs-physical-access;
  HSP's catalogue lists a copybook of letters, 1813-1816, to Monroe and with Erving, and Woolfley cites the collection
  for nearly every dispatch. It may hold clear copies, which would test the readings of Nos. 18, 19 and 28 line by
  line. Not seen, and whether the letters are in clear is unknown.
- Claiborne's letter of 24 Oct 1805 (`claiborne/`): troops written 1077 603 three times - blocker: open-codes; 1077 is
  tra on both halves of the code sheet, which has no tro: a substitution by Claiborne's clerk, which no key entry settles.
- Claiborne's letter of 24 Oct 1805: "arrival" (980 1?0 35) and "leather" (1?37), image 0224 - blocker: illegible; in
  both the digit is a blot under Wagner's gloss (179 riv and 1087 lea would fit).

## Escalation

- [x] siblings: the code is the JQA table (`../jqa`), also used by Crawford 1813, Appleton 1823, Everett 1825 and
  Ellis 1839, with the blocks reversed in Morris's copy; the copies of each letter on the roll were collated where
  they exist
- [x] clear-pages: frame 0039 has clear copies (M37 roll 2 frames 395-396; M31 roll 14 frames 0059-0060), used in the
  reading; clerks' decipherments on other copies of Nos. 24 and 25 and of the Cevallos note were compared
- [x] known-keys: 220 repository tables tried directly (none fits); the JQA table fits under the block reversal; from
  PR #200 the surviving code sheet (M97 roll 13, WE028) is the key
- [x] print: Manning (1925) vol. 3 searched (nothing); Woolfley (2013) searched in full text on Ebook Central (parts
  of 4 and 11 April 1814 and of Nos. 18, 19 and 24 quoted); *Papers of James Monroe* vol. 7 by Google Books snippets
  (nothing); two web searches on 12 Nov 2026 (one result reports an annotation in the *Papers of James Madison* that
  Erving's letter of 4 December 1814 enclosed a copy and translation of the Cevallos note; the page could not be
  opened). *American State Papers* not read
- [n/a] key-rebuild: the key is a complete surviving sheet of the code, not a rebuilt table; the open places are
  slips and private usages in the letters, which a rebuild from these texts cannot settle
- [x] retry: 12 Nov 2026: the two pieces left unread (frames 0115-0116 and 0111) transcribed and decoded; every
  doubtful word of Nos. 18 and 19 regraded against the key values (three more marked as inferred); 593.813 in No. 24
  compared with 598.813 = Sir in the letter of 24 March 1815

## Checks not made

These are not gaps in the reading (12 Nov 2026):

- Frames 0036-0038 and 0050-0057 are further coded copies of the letter of 4 January 1814 and its proposal, whose text
  is known from the clear copies (section 1). Their numerals are not in the repository (working numerals for 0050 and
  0052-0057 still have misreads; 0051 is not transcribed), so the proposal has not been decoded from the code beyond
  frame 0039.
- Other coded frames of the roll carry a clerk's words above the groups (the catalogue's vetting lists 0028, 0033,
  0066, 0069-0070, 0077-0079, 0206-0207, 0293 and 0316). They were not worked here.
- The digit rereads on frame 0039 were made with the clear text in view (`beling/frame39/frame0039_rereads.md`); no
  blind reread has been made.
- One reader only for Nos. 18, 19, 24, 25 and 28, for the letter of 24 March 1815, and for the two pieces added at
  integration. Frames 0113, 0221, 0209 and 0210 and the second copies were not viewed by the verifier.
- The order of the contributor's work on PR #415 (numerals frozen before decoding) is by the contributor's record:
  the pull request is a single commit.
- Print: Woolfley's page references (Ebook Central) were not checked at integration. *American State Papers*,
  Foreign Relations, was not searched beyond two web searches. *Papers of James Monroe* vol. 7 was searched by Google
  Books snippets only (catalogue vetting, 3 Nov 2026). So no passage here is called unpublished.
- Claiborne's letters (14 Nov 2026), none of them a gap in a reading here:
  - The letters of 18 and 19 Nov 1806, which the Madison editors list under the same code, are in the Library of
    Congress (Burr Conspiracy Collection; T260 roll 8 image 0408 is the slip that says so). loc.gov answers a script
    with a Cloudflare challenge (HTTP 403, the contributor's attempt), so whether they are online is not known: to be
    looked at in a browser. No image seen, nothing decoded. Their clear texts are in print by the contributor's record
    (PJM-SS 13; Rowland, *Official Letter Books* 4:36-37).
  - The editors' note "State Department code; key not found" and the printed texts of Wagner's decipherments were read
    through search snippets only (Founders Online answers a script with an AWS WAF challenge); the volume and page
    numbers are by the contributor's record. Wagner's words were seen between the lines on images 0045, 0409 and 0226.
  - The code sheet image (M97 roll 13) was not re-read at 577 (Morris and Claiborne 1077); the value tra is Beling's
    transcription, on which the two halves of the sheet agree.
  - The rest of T260 rolls 7-8 was not paged for further coded despatches of Claiborne (the contributor scanned roll 9
    in contact sheets: none).

## Files

- `morris1813_transcription.txt`: frame 0039, 26 lines, with the three corrections of the blind re-reading
- `block_map.tsv`: Morris's block order against the JQA table, with the basis for each block
- `decode.py`: decodes with `../jqa/code_table.tsv` under `block_map.tsv`; `--controls` runs the tests of section 5
  (Python standard library)
- `morris1813_decryption.txt`: output of `python decode.py`
- `morris1813_controls.txt`: output of `python decode.py --controls`
- `morris1813_reading.md`: the page as sentences, with notes on single readings
- `beling/letters/<date>_No<n>/` (catalogue 650 letters Nos. 18, 19, 24, 25, 28): `transcription.txt`,
  `line_by_line_decode.txt` (output of `beling/scripts/decode650.py`), `reading.txt`; for Nos. 24 and 25 the clerk's
  decipherment and the test against it
- `beling/scripts/`: `decode650.py`, `score_interlinear.py`, `read_share.py` (Python standard library)
- `beling/letters/1814-11-20_Cevallos/` and `beling/letters/1814-06-21_No17/` (added at integration, 12 Nov 2026):
  `transcription.txt`, `line_by_line_decode.txt`, `reading.txt`; the first also `translation.txt`
- `word_share.py`, `word_share.txt`: the share of coded words read in each letter reading, by one rule
- `claiborne/` (folded in on 14 Nov 2026 from `targets/claiborne1806`, PR #564 and PR #581, Brice Dudout): `transcription.txt`
  (the groups of the three letters lined up with Wagner's words), `transcription_corrections.tsv` (three corrections seen on
  the images), `we028_check.py` (the code sheet under the block reversal, unchanged, against Wagner's words), `key.tsv` (the
  contributor's own partial key, 261 values, built from Wagner's words before the match), `decryption.txt`, `reading.md`,
  `validation.txt`, `frozen/`, and the former folder's `NOTES_PR564.md` and `profile_PR564.json`

## Follow-up commit of the contributor (12 Nov 2026, c84e484c of PR 415)

After the integration above Andrew Beling pushed one more commit: reading reviews (grade A, with two independent
AI-agent readings) of Nos. 18, 19, 24, 25 and 28, recorded in `profile.json` next to the integration reader's review
(the profile holds one review per text, so his is added to the note of ours), and three changes in the readings:

- **No. 28, "actu[al]".** 10.1151.1255 is act + UV + non; nothing gives "-al", so the contributor marks it supplied.
  Under the strict rule it is a hole: No. 28 has 1 hole in 71 coded words, **0.986** (was 1.000; `word_share.py`, output
  in `word_share.txt`). All thirteen texts: 2,631 coded words, **87 holes**, 0.967 (the share does not move to three
  places). The profile figure of 85 holes and the 96.8% in README, SOLVED_CATALOGUE and the site blurb did not agree with
  the 86 holes counted here before this commit (frame 0039 at its recount of 13 holes); all now say 87 holes, 96.7%.
  His own group figure for No. 28 stays 1.000 (90 groups) and is his, not ours. The same word in No. 19 was already
  marked `[?actual]` here.
- **No. 24, 593.813.** He now writes the opening groups as numbers, `[593.813]`, where our reading has `[?Sir]`
  (the letter of 24 March 1815 opens 598.813, si-R, so 593 is probably a slip for 598). Both count as one hole; the
  integration's `[?Sir]` is kept because it says what the sense wants; his version of that line is not taken.
- **No. 19, "post office".** A note: 458 post, 367 dash, 76 of, 1231 "ficent" with strokes, "office" read by the stroke
  rule used in the other letters; no clerk's check. The word is not marked; it counts as read by the mark rule, and the
  stroke rule is itself inferred from use, not from an instruction.

His reviews: No. 18 and No. 19 as above in the profile notes; the clerk's decipherment on frames 0196 and 0174 was read
before the figures were transcribed (No. 25) or after the decode (No. 24), so the agreement with it supports the
reading and is not an independent test. `beling/SHA256SUMS.txt` carries the new hashes (No. 19 reading changed by his
note and the integration's mark, No. 28).

## Claiborne's letters of 1805-06 (folded in 14 Nov 2026; PR #564 and PR #581, Brice Dudout)

**Status of this part: in progress.** Three letters of William C. C. Claiborne, governor of the Orleans Territory, to
James Madison: New Orleans, 24 Oct 1805 (NARA RG 59, Territorial Papers, Orleans, microfilm T260 roll 7 images
0224-0226), 13 Jan 1806 (roll 8 image 0045) and 25 Nov 1806 (roll 8 image 0409). Each carries Jacob Wagner's decipherment
between the lines, and the *Papers of James Madison* print the texts with the note "State Department code; key not
found" (by the contributor's record and search snippets). Brice Dudout, with an AI agent, transcribed the groups, lined
them up with Wagner's words (328 words) and rebuilt 261 values and the block structure from them (27 Oct 2026, PR #564).
At the integration of PR #564 the project found that his values are the State Department code with its blocks of 100 in
reverse order, the numbering of Morris's copy. The owner decided on 14 Nov 2026 that the folder `targets/claiborne1806`
joins this target (one key, one entry), provided the same-map claim held when checked again. It does.

### The same map (checked again, 14 Nov 2026)

Own script, written for this check, on `claiborne/key.tsv` (the contributor's values, which were built from Wagner's
words and not from any code sheet) against `beling/key/codebook_M97_13_transcription.csv`:

- Every one of the 1,600 rows of the sheet's column `morris_number_after_reversal` is 100*(15-i) + r: the column is the
  pure reversal and nothing else.
- Under that reversal the sheet gives the contributor's value for 223 of his 261 numbers (I/J and U/V merged); of his 89
  sure values 86 by this script (85 at the earlier check; the difference is how "I.J." is normalised). Read directly,
  the sheet gives 0 of 261.
- 2,000 random orders of the sixteen blocks give at most 102 agreements.
- Block by block: for each of Claiborne's sixteen blocks the best-matching block of the sheet is the reversed one, with
  3 to 21 agreements, and no other block of the sheet scores a single agreement for any of them.

So Claiborne's copy (sent by Wagner on 8 July 1805, by the contributor's record of Rowland 3:165) and Morris's copy of
1813-15 number the code the same way. The map is one; what differs is the clerk's usage (below).

### PR #581 (second pass by the contributor), verified

| claim | contributor | ours | how |
|---|---|---|---|
| image 0226 (end of 24 Oct 1805) | 57 live groups agree with `transcription.txt` except the second Lakes, 153 1482L -> 153 148L | image fetched from the NARA catalogue; 57 groups counted and compared: the same, with 148 followed by the final hook | NARA medialz, T260-07-0226 |
| "the collecting" | the clerk wrote 362 285, struck 153 148L 1 12, then 76; "collecting" has no group | seen: four groups struck through after 285, "collecting" written by Wagner over them, 76 at the end of the line | image |
| Philip ends 401 | yes | the group reads 401 with the clerk's open 4 (it can be taken for 1101 at low size) | image crop |
| `we028_check.py` | 295 of 328 words mechanically (was 294) | 295/328: 228/250, 40/51, 27/27 | script re-run, before and after the move |
| by hand | 319 of 328 (was 317) | the list recounted: 13 of the 22 mechanical misfits of 24 Oct 1805 and all 11 of 13 Jan 1806 fit by hand; 9 do not | from the script's misfit list |
| 1077 = tra | both halves of the sheet read tra; the run is tol ... town, tra, trac, tract, traction; no tro entry | sheet rows 570-580 read as stated; the only "tro" on the sheet is trouble (19 = Morris 1519) | grep of the sheet transcription |
| the LoC letters | not seen, no figure | nothing to verify; kept as a check not made | - |

### Figures, per letter

The texts are Wagner's, so the question is not whether the letters are read but how far the code sheet, used unchanged
under the reversal, gives his words. Strict count = the mechanical rule of `claiborne/we028_check.py` (the values of a
word's groups, joined, spell Wagner's word; overlaps of one or two letters and I/J, U/V allowed; nothing else):

| letter | coded words | reproduced mechanically (strict) | with the hand classification |
|---|---|---|---|
| 24 Oct 1805 (T260 r7 0224-0226) | 250 | 228 = 91.2% | 241 = 96.4% |
| 13 Jan 1806 (r8 0045) | 51 | 40 = 78.4% | 51 = 100% |
| 25 Nov 1806 (r8 0409) | 27 | 27 = 100% | 27 = 100% |
| all three | 328 | 295 = 89.9% | 319 = 97.3% |

The hand classification is the contributor's and the earlier integration's, given once: it accepts the clerk's spellings
(mo-bil-e, missisipi, sp-e-dy, ben), his near syllables (at-tact-k, cant-non), the numerals of 13 Jan 1806 written as
digits (653 659 651 = 2 8 0), 364 as a full stop, and a different split of "General Wilkinson" and "General binding".
The nine words that no rule gives: four slips of the encoder (611 order in "information", 235 bil for "the", "John"
written 101 51, "collecting" with no group), troops three times (1077 tra), and "arrival" and "leather", unreadable on
the image. The letter of 13 Jan 1806 is low on the strict count only because of its numerals and the two re-splits.

The contributor's own key, sure values only, covers 326 of the 550 groups (59.3%); it is kept as `claiborne/key.tsv`
and is not the key of this target.

### What is and is not claimed

- Outcome for these three letters: read from Wagner's decipherments of the time (existing), and matched with a key from
  external sources (the code sheet under the reversal). The editors' "key not found" is explained. No new text.
- Credit: Brice Dudout for the transcription, the alignment and the rebuild of 261 values and of the block structure
  from Wagner's words, made before the match by the contributor's record (one commit); and for the second pass (image
  0226, the 1077 argument, the search for the letters at the Library of Congress). The identification of his table with
  the reversed code sheet was made at the integration of PR #564. The code sheet is Beling's transcription; the
  reversal was found by WAINUT for Morris.
- The held-out test in `claiborne/validation.txt` (22 of 23 new groups of 25 Nov 1806 at their alphabetical place)
  tests the structure of the contributor's rebuild; the letter was held out by the contributor's record. It is superseded
  by the external key.
- Two corrections to the printed text that the code confirms: 489 before "measures" is "wise" (Wagner does not gloss it),
  and "information" and "the" on 24 Oct 1805 carry encoder slips (611, 235).
- The share of 96.7% and the count of thirteen texts in this file are for Morris's letters only. The Claiborne letters
  have their own figures above and are not pooled with them.
- `../graham1806` (Graham, 1806) is a different code: it does not fit the reversed table.

### Open for this part

Blocked from outside: 1077 for tro- (open-codes), "arrival" and "leather" (illegible); both are under Remaining gaps.
Workable, listed under Checks not made: the two letters at the Library of Congress, the editors' notes and printed texts
in a browser, the sheet image at 577, the rest of T260 rolls 7-8. Until those are done this part stays in progress.
