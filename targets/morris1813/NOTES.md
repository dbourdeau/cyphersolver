# Anthony Morris to James Monroe, Cadiz/Madrid 1813-15: the State Department code with its blocks reversed

Status: in progress. Next step: transcribe the other coded frames, then the rest of the print search (Manning vol. 3 searched, Woolfley read in part, *Papers of James Monroe* vols. 6-7 not read).
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

## Proposed table changes (for `../jqa/code_table.tsv`, not applied)

None is proposed from this page alone. Candidates to test on more Morris text: 670 Florida(s) (JQA 970), 1566
colonies (JQA 66), 361 comma (JQA 1261, as in Ellis 1839), 652 the figure 1 (JQA 952). 721 (JQA 821) dem is grade I
in the table (a slot inference); it fits here (democratic).

## Remaining gaps

- Frames 0036-0038, 0050, 0052-0057, 0124-0125 and 0191-0192 (about 2,500 groups) - blocker: not-attempted; not
  transcribed. This is workable, so "read in part" is not a stopping point. 0191-0192 are two copies of one despatch
  and would check readings and transcription together.
- 36 distinct groups (48 tokens) on frame 0039 without a table value - blocker: open-codes; among them 670 (5x), 904,
  1149, 1311, 163 and the figure groups 655, 657 and 659. More Morris text would test the context readings.
- Frame 0039's reading of 31 Oct uses rereads made with the clear text in view (`beling/frame39/frame0039_rereads.md`), so a blind reread of those digits is still open - blocker: not-attempted.

- Anthony Morris Family Papers, Historical Society of Pennsylvania, Collection 2018-A - blocker: needs-physical-access;
  HSP's catalogue lists a copybook of letters, 1813-1816, to Monroe and with Erving, and Woolfley cites the collection
  for nearly every dispatch. It may hold clear copies, which would test the readings line by line. Not seen, and whether
  the letters are in clear is unknown.

## Escalation

- [x] siblings: the code is the JQA table (`../jqa`), also used by Crawford 1813, Appleton 1823, Everett 1825 and
  Ellis 1839 (open PR #107), with the blocks reversed in Morris's copy
- [x] clear-pages: frame 0039 has clear copies (M37 roll 2 frames 395-396; M31 roll 14 frames 0059-0060), used in the reading
- [x] known-keys: 220 repository tables tried directly (none fits); the JQA table fits under the block reversal
- [ ] print: Manning (1925) vol. 3 searched; Woolfley read in part (section 6); *Papers of James Monroe* vols. 6-7 not read
- [ ] key-rebuild: open slots (670, 1566 and others) need more Morris text
- [ ] retry: the other coded frames are not transcribed

## Files

- `morris1813_transcription.txt`: frame 0039, 26 lines, with the three corrections of the blind re-reading
- `block_map.tsv`: Morris's block order against the JQA table, with the basis for each block
- `decode.py`: decodes with `../jqa/code_table.tsv` under `block_map.tsv`; `--controls` runs the tests of section 5
  (Python standard library)
- `morris1813_decryption.txt`: output of `python decode.py`
- `morris1813_controls.txt`: output of `python decode.py --controls`
- `morris1813_reading.md`: the page as sentences, with notes on single readings
