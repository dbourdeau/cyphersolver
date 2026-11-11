# Anthony Morris to James Monroe, Cadiz/Madrid 1813-15: the State Department code with its blocks reversed

Status: in progress. Next step: a reading review and a second reader for the catalogue 650 letters of 11 Nov 2026; transcribe the coded frames still open (0111, 0115-0116, and the copies on 0036-0038 and 0050-0057); then the rest of the print search (Manning vol. 3 searched, Woolfley read in part and searched in full text, *Papers of James Monroe* vols. 6-7 and *American State Papers* not read).
Contributed by WAINUT (27 Oct 2026). The code is identified: it is the State Department code already rebuilt
in [`../jqa`](../jqa/NOTES.md) (the = 1385), and Morris's copy numbers its sixteen blocks of 100 in reverse order.
One page (frame 0039, 554 of about 3,000 groups, some 18%) is transcribed and read in part (0.678 of its words read
as sense); the other coded frames are not transcribed, so the catalogue item as a whole is about 12% read. In short:
code identified, complete; text of frame 0039, partial; text of the other frames, not attempted (`outcome.parts`).
The site page and the ledger rows are left to the maintainer.

Merge order: the 364 = full stop argument (section 2) rests on the Ellis 1839 alignment of PR #107, so #107 goes in
first. On merge, catalogue 650 (which says the signature groups do not match the JQA table) and `../jqa/NOTES.md`
should record the reversed-block copy; a one-line pointer is added to `../jqa/NOTES.md` in this pull request.

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
- **No. 24.** From a source he trusts: the Council of State is preparing a report to the king recommending a declaration
  of war on the United States over its proceedings on Louisiana and Florida. 47,000 soldiers and 5,000 officers have
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
- No `reading_review` yet: a person still has to read each `reading.txt` as sentences.
- The two tests are not blind (above), and the other three letters have no contemporary decipherment to test against.
- The unread and inferred lists behind the read shares are a judgment.
- Not read: a wholly coded document on 0115-0116 (deciphered copies on 0169-0170 and 0201) and three coded lines on 0111.

## Proposed table changes (for `../jqa/code_table.tsv`, not applied)

None is proposed from this page alone. Candidates to test on more Morris text: 670 Florida(s) (JQA 970), 1566
colonies (JQA 66), 361 comma (JQA 1261, as in Ellis 1839), 652 the figure 1 (JQA 952). 721 (JQA 821) dem is grade I
in the table (a slot inference); it fits here (democratic).

## Remaining gaps

- Frames 0036-0038 and 0050-0057 - blocker: not-attempted. A survey of the coded frames on 11 Nov 2026 found them to be
  further copies of the 4 January 1814 letter and its proposal, which have clear copies (section 1). Their numerals are
  not in the repository: working numerals for 0050 and 0052-0057 still have misreads, and 0051 is not transcribed. The
  other frames of this gap as first listed, 0124-0125 and 0191-0192, are the letter of 24 March 1815, read in part in
  `beling/letters/1815-03-24/` (PR #200).
- Frames 0115-0116 (a wholly coded document, with deciphered copies on 0169-0170 and 0201) and three coded lines on
  0111 - blocker: not-attempted; not transcribed or read.
- Catalogue 650 letters Nos. 18, 19, 24, 25 and 28 (`beling/letters/`) - blocker: open-codes; [370] after full stops
  is unidentified; 593.813 opening No. 24 and 575.1060 in No. 19 are unread; 1457, 1040, 572.1101 and 1150 misfit their
  key values and are read from context; 1569 is both December and United States. One reader only, and no
  `reading_review` yet.
- 36 distinct groups (48 tokens) on frame 0039 without a table value - blocker: open-codes; among them 670 (5x), 904,
  1149, 1311, 163 and the figure groups 655, 657 and 659. More Morris text would test the context readings.
- Frame 0039's reading of 31 Oct uses rereads made with the clear text in view (`beling/frame39/frame0039_rereads.md`), so a blind reread of those digits is still open - blocker: not-attempted.

- Anthony Morris Family Papers, Historical Society of Pennsylvania, Collection 2018-A - blocker: needs-physical-access;
  HSP's catalogue lists a copybook of letters, 1813-1816, to Monroe and with Erving, and Woolfley cites the collection
  for nearly every dispatch. It may hold clear copies, which would test the readings line by line. Not seen, and whether
  the letters are in clear is unknown.
- Print not checked for the catalogue 650 letters: *American State Papers*, Foreign Relations, and *Papers of James
  Monroe* vol. 7 - blocker: not-attempted. (Woolfley was searched in full text on 11 Nov 2026; see the
  catalogue 650 section.)

## Escalation

- [x] siblings: the code is the JQA table (`../jqa`), also used by Crawford 1813, Appleton 1823, Everett 1825 and
  Ellis 1839 (open PR #107), with the blocks reversed in Morris's copy
- [x] clear-pages: frame 0039 has clear copies (M37 roll 2 frames 395-396; M31 roll 14 frames 0059-0060), used in the reading
- [x] known-keys: 220 repository tables tried directly (none fits); the JQA table fits under the block reversal
- [ ] print: Manning (1925) vol. 3 searched; Woolfley read in part (section 6) and searched in full text for the catalogue 650 letters (parts of Nos. 18, 19 and 24 found); *Papers of James Monroe* vols. 6-7 and *American State Papers* not read
- [ ] key-rebuild: open slots (670, 1566 and others) need more Morris text
- [ ] retry: Nos. 18, 19, 24, 25 and 28 read (11 Nov 2026, `beling/letters/`); not transcribed: 0036-0038 and 0050-0057 (copies with clear texts), 0111, 0115-0116

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
