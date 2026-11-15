# David Humphreys to Pickering, Madrid, 1799: the coded parts of despatches Nos. 188 and 214

Status: in progress (folder only, no site page in this commit; target files and checks only)

Class: read in part (key recovered based on adjacent plaintext). The key is a table of Humphreys's code rebuilt from
the State Department clerks' decipherments of his other despatches and from printed decoded texts, frozen and tested
on a held-out despatch, then applied to two despatches of 1799 that carry no decipherment.

## Who read this code before us

- **The State Department's clerks**, at the time, deciphered many of Humphreys's despatches in this code between the
  lines (in 1801 the hand is Jacob Wagner's, according to the Papers of James Madison) or on a separate sheet (No. 73
  of 1793). Those decipherments are our source of pairs and the reference of our test.
- **The editors of the Papers of Thomas Jefferson** (Princeton) printed Humphreys's letters of 3 and 15 January 1791
  decoded (vol. 18, pp. 472-75 and 497-98), and say they decoded or verified them "employing Code No. 8", Julian
  Boyd's name for the code Jefferson made in 1785 for his correspondence with John Adams (Humphreys was then secretary
  of the commission in Paris). By the 1990s the editors describe it as a "partially reconstructed" Code No. 8 (vol. 26,
  note to No. 73), built from Jefferson's reuse of the same elements in later codes. The Papers of John Adams (vol. 17,
  note to Jefferson to Adams, 2 June 1785) say the original key "has not been found" and cite "Code No. 8 partial key,
  communication from James P. McClure, 20 April 2012". That partial key is a working file of the Jefferson Papers; it
  is not printed in Boyd, and Ralph E. Weber's United States Diplomatic Codes and Ciphers (1979) lists the code as
  "not located" (994 = "the"). We have not seen it.
  The identification of this code with Code No. 8 rests on the editors' saying they decoded these 994-code letters
  "employing Code No. 8"; an early line in `print/founders_index.tsv` ("NOT shown to be the 994=the code") was written
  before those notes were read and is superseded.
- **Frank Landon Humphreys**, Life and Times of David Humphreys (New York 1917), says the Department "has lost the
  cypher", that some despatches "were decyphered when received" and others by "Dr. Lowndes"; he prints the two 1791
  letters decoded and the coded part of the despatch of 24 February 1801 (No. 262) in italics. He does not print
  Nos. 188 or 214.
- **The Papers of James Madison, Secretary of State Series 1** (pp. 36, 43, 50-53) print Wagner's decodings of the
  coded sentence of 23 March 1801 and of the postscript of 30 March 1801, and say "key not found".
- **Nos. 188 and 214.** Whether the Department read them in 1799 is not established. No decipherment is on or after
  either copy on the film (frames 0295-0302 after No. 188; 0410-0429 around No. 214, of which 0418-0429 are its
  enclosures), and no second copy of either is on M31 rolls 5-7. The copies sent by other ships are not on this film,
  and Pickering's instructions to Humphreys of 1799 (microfilm M28, vol. 5) were searched through the catalog text
  layer only. Neither coded part was found in print (see "Prior print").

**What this folder adds:** a table of the code tied frame by frame and line by line to the clerks' decipherments
(`key/pairs.tsv`, every pair labelled by source); a held-out test written down before it was run; and readings of the
coded parts of Nos. 188 and 214 and of a 16-group sentence of April 1799, with every word marked as table value,
context value or guess. This is a reading made with a key rebuilt from period decipherments of other letters, not an
independent ciphertext-only solution.

## Documents and coverage

National Archives Catalog records (free images; federal records in the public domain):
- M43 roll 2, Despatches from U.S. Ministers to Portugal, 19 Nov 1790 - 17 Sep 1793: https://catalog.archives.gov/id/188790777
- M31 roll 5, Despatches from U.S. Ministers to Spain, vol. 4, 27 Oct 1797 - 29 Oct 1799: https://catalog.archives.gov/id/188602965
- M31 roll 6, same series, vol. 5, 1 Nov 1799 - 26 Apr 1806: https://catalog.archives.gov/id/188603515

Frame numbers are the catalog image numbers (M31-005-0294 = roll 5, image 0294).

| document | frames | groups | state on the film | here |
|---|---|---|---|---|
| No. 214, Madrid, 6 Aug 1799, to Pickering | M31 roll 5, 0414-0417 | 352 in ten passages | bare | read in part |
| No. 188, Madrid, 19 Mar 1799, to Pickering | M31 roll 5, 0294 | 56 | bare | read in part |
| despatch of April 1799, number not read | M31 roll 5, 0364 left | 16 | bare | read |

`inventory.tsv` lists every despatch found in this code (16), with roll, frame, date, groups and whether it is
interlined or bare. How the film was searched: every frame of M31 rolls 4, 5 and 6, M43 rolls 2 and 3, and M31 roll 7
frames 0003-0214 was downloaded and searched with our own OCR and the catalog text layer, and every flagged frame was
looked at; M31 roll 3, the rest of M31 roll 7 and M43 roll 4 were searched through the catalog text layer only. Short
passages of one or two lines can be missed by both readers.

Correction made while packaging: the first session's inventory listed the 1793-94 letters on M43 roll 2 as all in
Barclay's "Algerine" cipher. No. 73 (Lisbon, 29 May 1793; coded sentence on frame 0285, clerk's decipherment on 0286)
is in this code: 16 of its 17 groups decode with the frozen table to the clerk's text (`test/no73_check_after_test.txt`;
made after the test, not pre-registered). The Gibraltar letter on 0343-0345 is in the other cipher (a separate lead,
not worked). The April 1799 sentence has 16 groups, not the 19 estimated at overview size.

Images: none are committed in this folder, as in the other State Department targets here (`king1797`, `king1801`,
`morris1813`) and in `kerlerec1759`; the frames are cited above and in every transcription.

## System

One-part code (numbers in scrambled order: Spearman correlation between number and alphabetical rank of its value
0.04) of about 1,600 elements, numbers 2-1590 seen: about 46% whole words, 49% syllables, 5% single letters, and
punctuation groups 1436 (full stop), 1235 (comma), 1312 (semicolon), 1527 (stop, often closing a coded passage).
Some homophones (of = 240 and 24; be = 641 and 108; ing = 1122 and 1583 ...); i and j are one element (502). Proper
names are spelled out (Lo-u-i-si-a-n-a = 649.543.436.1466.925.892.925). The same values run from 1791 to 1801.
Compared at the same numbers and at every offset with the codes of Weber's appendix (WE016-WE028), Code No. 16, King's
769 code, Carmichael's 1196 code, Code No. 10 and Pinckney's 1651 code: none is a relative (`key/relatives_test.tsv`;
the independent check's `check/key_spotcheck.tsv`, 0 of 30).

## The pairs and the table

- `key/pairs.tsv`: 3,460 pairs, each with roll, frame, line and position, labelled by source:
  - `clerk_word_over_one_group` (579): the 1791 letters, where the clerk wrote the word over the group;
  - `clerk_words_over_several_groups_split_by_us` (620): the running decipherments of 1800-01, where the clerk's words
    run over several groups and the split into elements is ours;
  - `printed_edition` (2,261): groups aligned by us to a printed decoded text (Papers of Thomas Jefferson 18 for the
    1791 groups without a legible gloss; Madison Papers SS 1:50-53 for frame 0284).
  The 1791 "over one group" marks are the transcriber's; the independent check found 26 of 40 sampled pairs directly
  glossed, 10 running splits and 4 printed only. 3,368 pairs went into the table build (`in_table_build` = y); 92
  were added by the second pass after the test.
- `key/pairs_build_v1.tsv`: the pairs exactly as frozen; `scripts/build_table.py` rebuilds `key/table_frozen_v1.tsv`
  from it byte for byte (sha256 `2c2358a47ccca4e7ad266db3e4f6c158a8149a7271a246b1a7aae371c3a98cd1`, checked again on
  14 Nov 2026 while packaging). 686 groups; two groups with tied incompatible values left out (351 bil/men, 903 how/put).
- `key/corrections_after_test.tsv`: corrections and additions made after the test (second-pass readings of crib
  groups, values from the held-out despatch and from later glosses, conflicts). The frozen table is not changed.
- `key/context_values.tsv`: values for groups the table lacks or gives wrongly, chosen from the sense; not part of the
  table. Basis H = also the clerk's value in the held-out despatch; P = a group with hidden digits, fixed by the
  visible digits and the sense; S = sense only.

## Held-out test

`test/TEST_PLAN.md` was written before the run; the table was frozen; No. 262 (24 Feb 1801, M31 roll 6 frame 0235,
interlined, and printed in italics by F. L. Humphreys 1917) was kept out of the build and transcribed after the freeze.

| | result |
|---|---|
| frozen table on 135 scored groups (29 excluded under the plan) | **129 of 135 = 95.6%** decode to the clerk's element; precision 99.2% |
| 200 shuffled tables | at most 3.0% (mean 0.1%) |
| stricter count by the independent check: groups whose reference is a whole word carried by one group | **74 of 78** (94.9%), precision 1.000; shuffled at most 3 of 78 |

Rerun while packaging: `python scripts/holdout_test.py key/table_frozen_v1.tsv test/no262_transcription.txt` and
`python scripts/strict_holdout.py` give the same figures (`test/TEST_RUN_v1.txt`, `test/strict_result.txt`). Caveat
from the plan: the split of the clerk's words into elements was written by an agent that knew many table values; the
whole-word count is the version of the test that involves no split. The misses are five groups absent from the table
(foreign, never, carried, true, establish) and one partial (1292 pe/pel).

Statistical validation (`docs/_validate.py`, en-modern): **underdetermined**. The reading scores -1.842 per letter
against -2.665 for random keys (z 9.6), but a key annealed onto shuffled ciphertext reaches -1.850 (z 0.4): with about
two tokens per code number, a letter model cannot tell this reading from a fitted key. The held-out test is the
evidence for the table.

## Transcriptions

- `transcriptions/no214_pass1.txt` (reconciled text, clear context in braces), `no214_pass2_and_reconciliation.txt`
  (second pass from the end backwards: no group differs; the points re-examined); `no214_groups.txt` (groups only).
- `transcriptions/no188_pass1.txt`, `no188_pass2_and_reconciliation.txt`, `no188_groups.txt`.
- `transcriptions/april1799_0364.txt` (one transcription, checked twice on one crop).
- Both passes of each target despatch are by the same agent; the second pass is recorded as a reconciliation note,
  not as a separate group list. The independent check transcribed No. 188 and No. 214 passages a and e itself and
  checked f-j group by group on the image (`check/verifier_transcription_no188_no214.txt`,
  `check/transcription_no214_f_to_j_checked.txt`): one misread corrected (0415 line 1, 1393 "should", not 1392),
  one left open (0415 line 7, 827 or 927), No. 188 line 3 [?]405 (not 105).
- `transcriptions/crib/`: the crib pages (1791 Nos. 10 and 11; 1800-01 frames 0127, 0130, 0253, 0254, 0284);
  `transcriptions/crib_pass2/`: second passes of six of them (1,533 of 1,541 groups agree). No. 10 frames 0042-0045
  (about 1,050 groups) have one pass only.
- `transcriptions/short_passages_after_freeze.txt`: frame 0364, 0271 (interlined) and No. 271 (0290, bare; decoded in
  part, a five-group place name not read).

## Readings

`readings/reading_214.txt`, `reading_188.txt`, `reading_0364.txt`, made by `scripts/mark_reading.py` from
`readings/words_*.txt`. Plain = frozen table; {..} = context value of basis H or P; [..?] = sense-only guess; [n] =
group left unread, shown by its number; (..) = Humphreys's clear text. `readings/marked_*.tsv` give every word with its
groups, pieces and mark (T table, C supported context value, G guess, U unread).

| | words | table | context | guess | unread | groups read by the frozen table |
|---|---|---|---|---|---|---|
| No. 214 | 224 | 173 | 17 | 24 | 10 | 293 of 352 (83.2%) |
| No. 188 | 43 | 35 | 1 | 4 | 3 | 50 of 56 (89.3%) |
| April 1799 | 14 | 12 | 2 | 0 | 0 | 14 of 16 |

The first session counted 295 of 352 groups (84%) for No. 214; the recount here is two lower because 349 ("lay"),
1587 ("child") and the uncertain 827 are not counted as table readings where the reading uses another value.

### What No. 214 says (wording set by the independent check)

- **Yrujo.** Humphreys explains Spain's "strange fluctuating conduct" over the recall of the Spanish minister Carlos
  Martínez de Yrujo by supposing that Yrujo is "connected with certain lea[d?][ing?] [men?] here in the profits of an
  exclusive [trade?] from the United States to the Spanish colonies", which needs his presence in America ("leading
  men" and "trade" are guesses; "trade" could be "commerce").
- **Orders.** "If the President should [646] to send him [away?] ..." the reasons should be explained in a letter to
  the King of Spain; he asks "to be honoured [with?] the orders of the President whether {to} remain at Lisbon or
  [proceed?] to the United States in case of my being obliged to leave this country".
- **Louisiana**, as it stands, with its holes. This is Humphreys's own belief, which he says he told Urquijo ("I had
  good reason to believe", in clear), not a fact the despatch establishes: "that the design of {re}covering Louisiana had {never} been
  re[197][1355]ished … the {ces}sion was [in?]serted in the [origin?]al project of the {trea}y of [Basl?]e … Truguet had
  re[22]d the negociation with Saave[dra?] … he had [314]ed against the ratification of the treaty for want of that
  cession, which he said would have been made but for treachery … so long as he remained in office I might rest
  assured France {should} {never} get possession of Louisiana."
  Strength of each named detail: "Basle" weak (a guess for one group plus a final e); "Truguet" fairly strong (spelled
  Tru-gue-t; "Tru" is a single row); "Saavedra" medium (the last syllable is a guess); "treachery" medium
  (tre-a-[ch]-e-ry is the only English word that fits, but three of its pieces rest on single entries and 1587 is
  "child" in the table); "voted" for [314] is a guess and is not printed in the reading; "never" rests on the clerk's
  value in the held-out despatch; "relinquished" is three-quarters guessed. The man who "had [314]ed against the
  ratification" is Guillemardet, French ambassador at Madrid (named in the clear text before the passage). Urquijo
  said Humphreys "might rest assured"; he did not swear.
- Passages b and c (the person of Nos. 203 and 204, a name [713][983]-is-he-f-er-na-n, not read; a letter "from
  Ur-u-i-[jo?]" to "Ur-que-[426]-[jo?]", names not resolved) and d (friendship "of the latter for the former") are
  short and partly unread.

### What No. 188 says

In substance (a paraphrase, not the reading): the government of [Sweden?] was now less inclined to humour France, and
the Baron [935] sta[ël?] would probably soon leave Paris. Word for word the decode runs: "[ga?]ve me in confidence reason to
believe that the government of [Sweden?] now less [inclin?]d to use management with that of France than [126] [?405]
of that letter and that it is even probable the Baron [935] sta[ël?] would soon retire from Paris". The chargé d'affaires who gave Humphreys this in confidence ("This Gentleman", in clear) is identified from
the enclosures on the film (M31 roll 5 frames 0296-0297: letters of Carl Gustaf Adlerberg, Swedish chargé d'affaires
at Madrid, quoting the Swedish chancellor Ehrenheim) as the Swedish chargé Adlerberg, which makes Sweden likely but
not settled: group 1097 occurs nowhere else, and the clear sentence before it is about Danish convoys. The group
between "Baron" and "Sta" (935) is "rise" in the table and possibly "hand" in No. 10, so "de Staël" is weak. The
passage fills the asterisks in Naval Documents Related to the Quasi-War between the United States and France, vol. 2
(1935), p. 437, which prints "... it must be by the approbation of their Government. * * *" and goes on with
"Calepio ..."; the film has "This Gentleman" and the 56 groups at that place (`print/navaldocs_v2_p436_humphreys_17990319.txt`).

### The April 1799 sentence

"I have seen a letter from the {Dutch} minister at {Paris} which reports that" (clear text follows on the clamour
against Scherer's peculations and Rewbell leaving the Directory with thirty millions).

## Prior print

Not found in: Naval Documents, Quasi-War vol. 2 (No. 188, code left out) and vol. 4 (No. 214, text search only);
American State Papers, Foreign Relations vol. 2 (no Humphreys despatch of 1799); the calendar of the Pickering Papers
(Massachusetts Historical Society Collections, 6th series, vol. 8, 1896: no entry for 19 March or 6 August 1799);
F. L. Humphreys 1917. Not searched: Naval Documents vols. 1 and 5-7; Humphreys's own papers (the
Humphreys-Marvin-Olmstead collection at Yale, and the David Humphreys papers at the New Haven Museum, known from SNAC
records only); the books by Whitaker, Lyon and DeConde (below).

## History and significance

Three things are kept apart below: what the despatches say (from our reading); established history (with the source
consulted); and inference (ours).

**Sources consulted.** Frederick J. Turner, "The Policy of France toward the Mississippi Valley in the Period of
Washington and Adams", American Historical Review 10 (1905), 249-279 (read in full, Penelope copy, saved locally);
Founders Online editorial notes (Papers of Thomas Jefferson, Papers of James Madison); the film itself. **Not
consulted:** Arthur P. Whitaker, The Mississippi Question 1795-1803 (1934); E. Wilson Lyon, Louisiana in French
Diplomacy 1759-1804 (1934); Alexander DeConde, This Affair of Louisiana (1976). The archive.org copies are lending-only
and were not reached. These are the standard accounts, so the comparison below is incomplete.

**Yrujo and his recall.** *Established* (Founders Online, Jefferson Papers editorial note): the Adams administration
(Pickering was Secretary of State) asked Spain to recall its minister Carlos Martínez de Yrujo; in 1800 Spain named
Nicolás Blasco de Orozco minister to the United States and appointed Yrujo elsewhere, but under Jefferson the recall
was dropped and Yrujo stayed. The film has (M31 roll 6 frame 0068, an enclosure of
early 1800, read from our OCR only) Humphreys arguing that Saavedra's illness might excuse the delay but that American
patience "would not be interminable". *The despatch says* that Humphreys could account for Spain's wavering only by supposing
that Yrujo shares, with certain lea[d?][ing?] [men?] at Madrid, in an exclusive [trade?] from the United States to the Spanish colonies: a supposition of Humphreys's, not a fact the despatch reports.
*Inference:* this is a contemporary allegation, possibly connected with the flour licences for Havana and Caracas
reported in clear in the same despatch; it was not found in the sources consulted.

**France and Louisiana, 1795-1800.** *Established* (Turner 1905): Barthélemy was instructed on 10 May 1795 to demand
Louisiana from Spain as the price of peace; at Basel (July 1795) Godoy made peace but refused Louisiana, giving up the
Spanish part of Santo Domingo instead; France pressed for it again in the alliance talks of 1796 (Perignon), sent his
successor to offer a joint conquest of Portugal, and in 1797 offered the papal legations; in 1798 Talleyrand
instructed Guillemardet at Madrid to make Spain see the danger of the United States, and reported Spain's "yielding
spirit" (memoir of 10 July 1798); "Napoleon found Louisiana ripe for the picking in 1800". The retrocession was agreed
in the secret Treaty of San Ildefonso of 1 October 1800 (general reference; the date is not taken from Turner, who
does not give it). *The despatch says* that the cession was in the original project of the Treaty of [Basle?], that
Truguet had re[newed?] the negotiation with Saave[dra?], that Guillemardet told Humphreys he had [voted?] against the
ratification of the treaty for want of the cession, which would have been made but for "treachery", and that Urquijo
assured Humphreys that France {should} {never} get Louisiana while he remained in office. *Inference:* Humphreys's account
of the treaty (if [Basl?]e is right) and of the later French approaches agrees with Turner's; Turner does not name Perignon's successor, and the
identification of that successor with Truguet rests on the despatch. The identification of Urquijo as the Spanish
minister who signed at San Ildefonso is from memory and was not checked here.

**Why a report of August 1799 matters.** *Inference:* an American minister at Madrid told his government, fourteen
months before the retrocession, of his own belief (told to Urquijo) that France had never given up its design on Louisiana ("relinquished" is mostly guessed), with the French side of the
story from the French ambassador himself, and with the Spanish minister's personal assurance to the contrary. Because
the passage was in code and no decipherment is on the film, it is not clear that Pickering ever read it; if he did,
it is a warning given in 1799. Whether historians have used it is not known: it was **not found in the literature
consulted**, and Whitaker, Lyon and DeConde, who cite the State Department's Spain despatches, were not checked.

**No. 188.** *Established from the film:* the Swedish chargé at Madrid in March 1799 was Carl Gustaf Adlerberg
(enclosures, frames 0296-0297). Erik Magnus Staël von Holstein was the Swedish minister in Paris; a list of Swedish
envoys gives the end of his mission as 13 July 1799, and another secondary source differs (not checked). *Inference:*
if the reading is right, Adlerberg foresaw in March 1799 a departure that came that summer; this rests on
"Bar-on [?] Sta-".

## Reading review

Preliminary. `CONTRIBUTING.md` (14 Nov 2026): a reading merges only with a `reading_review` graded A or B,
"recorded by the reviewer, not by the author of the reading". The grades in `profile.json` (3 entries) were
written by Andrew Beling's own AI agents and are kept as preliminary grades: `by` is "Author's agents (Andrew
Beling, with AI agents)" and each note begins "PRELIMINARY: author's self-check, not a reviewer's grade. For a
maintainer to confirm or replace.", followed by the agents' own reading note. No grade letter was changed.

## Limits

- 12 groups of No. 214 have digits hidden in the binding (frames 0415 and 0417); frame 0416 adds nothing, and there is
  no second copy on the film.
- Context values (`key/context_values.tsv`) are unconfirmed by a second occurrence, except those of basis H; every one
  was searched for in all transcriptions and in both machine readings of every code page found.
- M31 roll 3, M31 roll 7 after frame 0214 and M43 roll 4 were searched through the catalog text layer only.
- Humphreys's own papers (Yale; New Haven Museum) were not checked for letterbooks or clear drafts of 1799.
- The 1791 crib pages 0042-0045 have one transcription pass; the "over one group" labels of the 1791 pairs are the
  transcriber's.
- Nothing has been checked by a person: the transcriptions, the pairs, the test and the readings are AI agents' work,
  checked by a second AI agent of ours.

## Remaining gaps

- No. 214: 12 groups with digits hidden in the binding on frames 0415 and 0417 - blocker: needs-physical-access; no second copy on M31 rolls 5-7; the volume itself or another copy of the despatch would restore them.
- Nos. 188 and 214: 36 code numbers with no value in the frozen table (37 with group 1290 of the April 1799 passage, frame 0364; recounted 15 Nov 2026 from `readings/marked_*.tsv`; partly legible groups not counted) (1097, 864, 126, 314, 22, 197, 1355, 646, 766, 713, 983, 426 and others) - blocker: open-codes; none occurs a second time with a decipherment in any page found; context values are given where the sense allows and marked.

## Escalation

- [x] clear-pages: the clerks' interlined decipherments and the decipherment sheet of No. 73 used; no decipherment follows Nos. 188 or 214 (frames 0295-0302, 0410-0429).
- [x] siblings: M31 rolls 4-6 and M43 rolls 2-3 paged by image and OCR for other copies and coded passages; no second copy of Nos. 188 or 214.
- [x] known-keys: Weber's appendix codes, Code No. 16, King's 769, Carmichael's 1196, Code No. 10 and Pinckney's 1651 compared: none is a relative; the Jefferson Papers' partial Code No. 8 is unpublished and was not seen.
- [ ] print: Naval Documents vols. 2 and 4, American State Papers, the Pickering calendar, F. L. Humphreys 1917 and Tomokiyo's Cryptiana (describes the 994 code, gives no key) checked; Lasry's GL.htm not checked; Naval Documents vols. 1 and 5-7, Humphreys's papers at Yale and the books by Whitaker, Lyon and DeConde not checked.
- [x] key-rebuild: 3,368 pairs, 686 groups; held-out test passed; second pass of six crib pages after the test.
- [x] retry: every open group searched in all transcriptions and both machine readings of every code page; corrections after the test applied; no reading of No. 214 changed, No. 188 gained "now".

## Files

- `inventory.tsv`; `profile.json`; `validation.tsv`
- `key/`: `pairs.tsv`, `pairs_build_v1.tsv`, `table_frozen_v1.tsv` and `.sha256`, `corrections_after_test.tsv`,
  `context_values.tsv`, `relatives_test.tsv`
- `test/`: `TEST_PLAN.md`, `TEST_RESULT.md`, `TEST_RUN_v1.txt`, `no262_transcription.txt`, `strict_result.txt`,
  `no73_check_after_test.txt`
- `transcriptions/`, `readings/`, `check/` (the independent check's own transcriptions and samples), `print/`
  (the Naval Documents text of No. 188 and an index of the Founders Online items used)
- `scripts/`: `build_table.py`, `holdout_test.py`, `strict_holdout.py`, `targets.py`, `mark_reading.py`,
  `cite_pairs.py`, `pairs.py`, `label_pairs.py`, `compare_passes.py`, `relatives.py`, `detect.py`, `pick_pairs.py`.
  The last six were run in the working folder and read files not copied here (OCR output, the downloaded frames);
  they are kept as a record.

Credit: Andrew Beling, with AI agents (Claude Opus 5.5), 14 November 2026.
