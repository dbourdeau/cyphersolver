# kanawha1863: Union route-cipher telegrams of the Kanawha district, West Virginia, 1-3 July 1863 (Gilder Lehrman GLC02414)

Status: in progress (read in part, folder only, no page). Four of the five cipher telegrams were deciphered at the time
by General Scammon's headquarters; our part is the route, the code-word values, a held-out test of them, and a partial
reading of the fifth telegram, GLC02414.339, which has no decipherment of the time in the collection.

Contributed by Andrew Beling, with AI agents (Claude Opus 5.5), 13 November 2026. Lead 2051 in `research/leads.json`.

## Who read what, and when

| Telegram | Read first by | What this folder adds |
|---|---|---|
| GLC02414.341, White to Scammon, Fayette, 2 July 1863 | Scammon's headquarters, 1863: decipherment grid GLC02414.114 (catalogue: "possibly a copy in General Scammon's hand") | The route, recovered from this pair; six code words, two of them on uncertain readings (Venus/Agnes, Italy/truly) |
| GLC02414.229, White to Scammon, Fayette, 2 July 1863 | Scammon's headquarters, 1863: clear copy GLC02414.137 ("Recd telegram") | Route confirmed on a 10-row and a 2-row section; six more code words |
| GLC02414.344, White to Scammon, Fayette, 3 July 1863, 9.35 p.m. | Scammon's headquarters, 1863: clear copy GLC02414.138, marked "Cipher" | Four more code words |
| GLC02414.185, Toland to [Scammon], undated | Its own decipherer, on the same sheet (grid below the cipher) | Held-out test: the frozen key predicted 60 of 66 cells |
| GLC02414.339, Camp Piatt to "Operator", 1 July 1863, signed by code as Toland | No decipherment of the time found | Partial reading: 35 of 42 cells with a word or value under our readings (32 without three later additions in other ink or another hand), 7 holes |

The readings of .341, .229 and .344 are therefore not independent solutions: the key was built from those pairs. Only
.185 (as a test) and .339 (as a reading) go beyond what the 1863 decipherers left.

The transcriptions, the grids and the readings in this folder are the project's, made by AI agents on 13 November 2026
from the images described under Sources. No person has checked them against the images. A second AI agent of ours
checked them independently on 13 Nov 2026 (see Independent check below); its corrections are applied.

## Sources and terms

- **Originals.** The Gilder Lehrman Institute of American History, New York, Gilder Lehrman Collection GLC02414 (papers of
  Eliakim P. Scammon). Free item pages give the catalogue record and, when the Cloudflare check passes, a small
  public preview (about 400 pixels wide, too small to read the words): for example
  https://www.gilderlehrman.org/collection/glc02414341, .../glc02414229, .../glc02414344, .../glc02414339,
  .../glc02414185, .../glc02414114, .../glc02414137, .../glc02414138.
- **Edition used for reading.** "American History, 1493-1945" (Adam Matthew Digital), which reproduces the Gilder
  Lehrman Collection, opened through the University of Maryland's library subscription. The transcriptions were made
  from that edition's viewer and its per-document PDFs. The images are licensed; none is included here or anywhere in
  the repository.
- **Terms, Gilder Lehrman** (read 13 Nov 2026). The item pages say images are available to Collection subscribers and
  carry the standard notice on title 17 of the United States Code. The Rights and Reproductions page
  (https://www.gilderlehrman.org/collection/rights-and-reproductions) covers images only: publishing an image needs a
  publication-rights request and fee, and "Research copies cannot be used for any print or publication purposes." The
  site has no general terms-of-use page that we could find (/terms-use and /terms-and-conditions give "page not
  found"; the footer links only a privacy policy). Nothing we found on the Gilder Lehrman site restricts publishing a
  transcription of an item's text.
- **Terms, Adam Matthew** (the edition we read; "Terms of Use" page of "American History, 1493-1945", read 13 Nov 2026).
  It grants research and non-commercial use and says: "Authorised Users have the right to use, with appropriate credit
  and copyright permission from the original source archive in the case of re-publication, figures, tables and brief
  excerpts from the Licensed Materials in the Authorised User's own scientific, scholarly and educational works." It
  also says "The Licensee shall not modify or create a derivative work of the Licensed Materials without the prior
  written permission of Licensor", and forbids commercial use and "bulk reproduction or distribution". It does not
  mention transcriptions. Whether a full transcription of a short 1863 manuscript counts as a "brief excerpt" of the
  licensed materials, or needs Gilder Lehrman's permission, is not settled by these words: this is a decision for
  Andrew before posting. The manuscripts themselves are 1863 United States Army messages, out of copyright; the
  transcriptions are ours; no image is included.
- **Catalogue notes used.** .341 docket "Col. C.B. White / Statement of Mrs. Miller / about 22nd & 45th Va."; .344 docket
  "Enemy's scouts seen"; .339 "In code addressed to Operator. Written in Camp Piatt" (place written: Belle, West
  Virginia); .114 and .117 "possibly a copy in General Scammon's hand of a decoded cypher telegram".

## The system

A Union military-telegraph route cipher with local code words.

- The message is written six words to a row. In four telegrams row 1 is a heading; what it holds:
  - .341 (.114): Fayette, July, second, Scammon, Charleston, then the first text word "Just".
  - .229: Fayette, July, second, Scammon, Charleston, then "we" (= Lew, the first text word).
  - .344: Fayette, July, third, Scammon, then the text begins ("enemy's cavalry"): no Charleston.
  - .339: sherry (inferred: Camp Piatt), July, first, Scammon, Charleston, then [Virginia].
  - .185 has no heading row: its grid begins with the text ("after making a thorough search of").
  The sender's name is the last cell in .341, .229, .344, .185 and .339.
- The columns are taken off in this order: **up the 5th, down the 1st, up the 4th, down the 2nd, up the 6th, down the
  3rd.** No blind (check) words are added at the column ends.
- A **commencement word** stands in front of each section (`COMMENCEMENT.tsv`). Observed, not tested: the number of rows
  goes with the word in every case seen. Florida 6 rows (1 example, .341), Ocean 10 (1 example, .229), Dacotah 7 (1
  example, .339, and only if the later additions in .339 are counted as words, so this one is circular), Wilderness 9
  (2 examples, .344 and .185), Turkey 2 (2 examples, the second sections of .229 and .185). Only Wilderness and Turkey
  repeat. In every case the rows also equal the word count divided by six, which is how our key computes them, so
  nothing here shows that the word sets the rows; the held-out test held the grid sizes fixed and does not test it.
  Plum (1882, vol. 1, p. 47) describes Stager's cipher No. 7 as having commencement words that "indicated the number of
  lines", which fits. The route is the same for every row count seen; no telegram shows another route.
- **Code words** replace places, names and military words: `codewords.tsv` lists every one, with the pair it was valued
  from and how often it occurs in the valued pairs. Sixteen word forms were frozen in the key. Two of them rest on
  uncertain readings of .341 and are not counted: word 2, "Venus" or "Agnes" (= yours), and word 14, "Italy" or "truly"
  (= Truly; if "truly", it is a plain word, not a code word). That leaves **14 code words valued** in the frozen key:
  sycamore, rye, amazon, mississippi, apricot(s), apple, cedar, whistle, cotton, currants, vermillion, gild, gilding,
  coat. Of these, **rye, apple, cedar, cotton, gild, gilding and coat rest on a single occurrence** in a valued pair
  (cedar and cotton are also corrected in the decipherment .110). plated = retreated and nile = Toland were learned
  from .185 after the test, one occurrence each. sherry = Camp Piatt is inferred from the heading slot, not valued.
- Telegraph slips are common and are not code: ffine = from, rain = run, "laying road" = hanging around, "the" for They,
  "of" for if, "air" for are, "we" for Lew, "these" for them, "might" for night. An ink blot in .229 marks a deleted
  word; words struck through in .229 (twenty, fortifying, would, say) are needed in the grid and count as text.
- Word counts: .344 has "55" written at its foot, which is the commencement word plus the 54 grid words once the two
  struck words are left out and the interlined "at" counted, as in the grid used here.
- The telegraph names on the forms, "Graham" (White) and "Thomas" (Scammon), stand outside the cipher.

## How the route was found (round 1, 13 Nov 2026)

GLC02414.114 is a period decipherment of .341 written into a 6 x 6 grid. Putting the .114 grid through the route gives
the .341 cipher word for word (`verify.py`, part 3): 23 positions are the same word, 6 are code words (two of them,
Venus/Agnes and Italy/truly, uncertain readings), 5 are spelling variants (va, thirteenth, forty, twenty, ms), and 2
are hidden under a paper repair patch on the .341 form, so they are not seen. The round 1 notes said "all 36 positions
agree"; 34 of 36 is the seen count. The key was built from this same pair, so this shows consistency, not a test.
("had" in our first transcription is "head" on the image, as in .114.)

## Tests

### Round 1 (written before scoring): FAILED

`freeze/round1/` holds the key, the protocol and their sha256. The measure was the share of adjacent row-reading word
pairs attested in the Huntington Eckert telegram ledgers, against 200 random routes; to pass, a telegram had to beat
every control and reach 0.30. All four failed, the known crib .341 included (`freeze/round1/test_results.json`):

| Telegram | Read share | Controls: median / max | Controls at or above |
|---|---|---|---|
| .341 (the crib) | 0.114 | 0.057 / 0.200 | 47 of 200 |
| .229 | 0.211 | 0.141 / 0.225 | 2 of 200 |
| .339 | 0.175 | 0.100 / 0.275 | 17 of 200 |
| .344 | 0.226 | 0.113 / 0.245 | 3 of 200 |

The measure cannot tell the right route from a random one: every route keeps the same bag of words, and code words and
names starve the pair counts. The protocol was not blind either (the telegrams had been transcribed and explored
first). After the failure, a check devised afterwards and labelled as such: of 10,000 random routes only 1 to 4 put
the heading words into their row-1 slots as the frozen route does (`freeze/round1/heading_control_posthoc.txt`).

### Round 2 (written before scoring, held-out pair): PASSED

`freeze/round2/` holds `key_v2.json`, `TEST_PROTOCOL_v2.md`, their sha256 (`key_v2.sha256`) and the result. The key was
fixed from three pairs (.341/.114, .229/.137, .344/.138) and the corrections in .110, then used to predict the .185
decipherment grid cell by cell from its cipher alone. Control: 200 random six-column routes (seed 1863) with the same
code values.

| | Cells matching the decipherment of the time |
|---|---|
| Frozen key | **60 of 66 (0.91)** |
| Random routes | median 1, maximum 40 |
| Random routes at or above 60 | 0 of 200 |

The six misses: "through" for thorough, "the" for that, "start" for started, "suspects" for suspect (clerks' variants),
and two code words not in the key, plated (retreated) and nile (Toland).

Limits, stated as they are:
- **Disclosure.** The agent had glanced at the .185 sheet during triage, before writing the protocol: it saw that the
  sheet holds a cipher and a grid and read its opening words. No value in the key comes from .185.
- The order of events rests on our own file times only: key, protocol and hash list were written at 22:41:37 local
  time on 13 Nov 2026 and the scored output at 22:41:48. Nothing outside our machine dates the freeze.
- The test checks the route and the code values the key holds. .185 shares only one valued code word with the key
  (whistle, twice); the other 13 code-word values are not tested by it.
- `verify.py` re-runs the test and reproduces the frozen figures.

## Independent check (13 Nov 2026)

A second AI agent of ours, working from the images before it opened this folder, derived the route from .341 and .114
and got the same route (up 5, down 1, up 4, down 2, up 6, down 3, commencement word outside the grid) and the same
code-word values. Its agreement counts match ours: 70 of 70 checkable cells on .229 (row 1 columns 4-5 are not in
.137), 54 of 54 on .344, and 60 of 66 on .185 by our script. Its record is outside this folder. Its corrections are
applied here: the heading row and commencement-word statements, the sources of rye and amazon, the single-occurrence
marks, "head" for "had", the uncertain readings Venus/Agnes and Italy/truly (now outside the count of code words),
the alternative readings in .339 (gave, will, as, way) and the .339 counts with and without the later additions.
It also noted that the .185 control randomises the route only, with grid sizes and code values fixed.

## Integration check (14 Nov 2026, PR #585)

Verified from the files by the integrating reader (an AI reader, not a person).

- **Reproduced.** `verify.py` passes; the four sha256 values in `freeze/` match the files. A second decoder written from
  `key_v2.json` without the contributor's code gives the same grids for all five telegrams and the same held-out score
  on .185: 60 of 66 cells. Our own control, 2,000 random six-column routes: median 1, maximum 41, none at or above 60.
- **The held-out test** is judged on what the files show: no value of `key_v2.json` is needed from .185, and the six
  misses are the ones listed above. That the key was frozen before scoring is by the contributor's record (file times
  11 seconds apart, no outside stamp), and the agent had seen the opening words of the .185 sheet. The test covers the
  route; of the 14 valued code words it touches one (whistle).
- **Strict read share per telegram** (README read bar: supplied, inferred and unsettled words are holes), in grid cells:
  .341 32 of 36 (0.889; two words under the patch supplied from .114, words 2 and 14 uncertain); .229 71 of 72 (0.986;
  the word read as Coat is not legible); .344 54 of 54; .185 66 of 66 (the decipherment is on the sheet); .339 **33 of
  42 (0.786)**: the seven unvalued words, sherry (Camp Piatt is inferred from the heading slot, no pair) and the
  unsettled at/as. The contributor's count for .339 is 35 of 42 (0.833). Four of the five telegrams were deciphered in
  1863; the only reading that is ours is .339, so the pooled 256 of 270 (0.948) is not a headline.
- **Outcome method:** key recovered based on plaintext from external sources (the 1863 decipherments, separate items of
  the same collection). Key state: partial.
- **Not checked:** the transcriptions against the images. gilderlehrman.org answered 403 (bot check) on 14 Nov 2026 and
  its free preview is too small to read; the readable images are in the licensed Adam Matthew edition. No person has
  compared any word with an image. The Official Records and Plum page references were not re-opened.
- **Duplicates.** No other target holds GLC02414 or this route; `eckert1862`, `civilwar1862`, `union1864`, `army1865`
  and `ammen1864` use the War Department books (No. 1, 2, 9 ...), whose six-column routes differ. Lead 2051 in
  `research/leads.json` is this folder.
- **Why it stays in progress.** The gaps can still be worked: the rest of GLC02414 .100-.350 has not been opened (the
  cipher forms of the decipherments .110, .116-.118, .184 and the autumn grids would value more code words and could
  give a second message with the open words of .339), and Books No. 10 and No. 12 were not seen. Whether the
  transcriptions may be published in full under the edition's terms is for the owner and Andrew Beling to settle
  before a page is written.

## Readings

Sentences in `reading/`, grids in `decryption/` (written by `verify.py`). Holes are marked [ ].

- **.341** (crib; read in 1863, .114): Mrs. Miller, wife of a soldier of the 13th Virginia, has come in from the head of
  Paint Creek and says the 45th and 22nd Virginia were to leave Lewisburg yesterday.
- **.229** (read in 1863, .137): a path from the Soak road is open for infantry, not cavalry; the enemy is fortifying at
  the ford of Piney and holds the forks of Beaver; the 45th Virginia is at Pack's Ferry, the 22nd reported advancing to
  reinforce Raleigh; officers say they will attack with six thousand, take Fayette and clear the valley; White thinks
  this very doubtful. 72 of 72 cells.
- **.344** (read in 1863, .138): enemy cavalry came in sight of the outpost; White has sent all his cavalry to drive the
  enemy pickets into Raleigh, attacking at two in the morning. 54 of 54 cells.
- **.185** (read at the time on the sheet; our held-out test): Toland reports that the powder and fuse are not in the
  army wagon, that he started at three in the morning, and that it will be a close race if the enemy has retreated.
- **.339** (no decipherment of the time): "[Camp Piatt], July first. Scammon, Charleston. [Virginia] I saw [Missouri]
  last night before answering, & [gaol, or the plain word gave] our united opinion. If the movement is important,
  please direct when at/as shall start [bent]. [nile, or the plain word will] not this interfere with the proposed
  [amore] on [away]? Signed Toland."
  - **Filling the grid.** The 42 cells fill exactly only if the darker-ink "&", the margin "when", the interlined
    "not", the overwritten word ("amore") and the struck word ("bent") each count as one word. Three of the cells
    counted as read (&, when, not) are later additions in other ink or another hand.
  - **Counts.** Under our readings: 35 of 42 cells carry a word or a value (0.833); without the three later additions,
    32 of 42 (0.762). Under the second reader's "gave" and "will": 37 of 42 (0.881), or 34 of 42 (0.810) without the
    additions. In every count Camp Piatt (sherry) is inferred from the heading slot and nile = Toland in the signature
    was learned after the test.
  - **Readings re-examined on the image** after the independent check (13 Nov 2026): "gaol" (the letters look like
    o-l, not v-e, but "gave" reads well: both given, kept as a hole); the first "nile" (n or w, not settled: both given,
    kept as a hole); "at" or "as" (a plain word either way; the earlier emendation to "it" is dropped); "away" or
    "way" (a hole either way); the struck word "bent", "bout" or "best" (illegible).
  - **Arrangement.** The round 2 arrangement left the "&" out and an empty cell at row 7 column 2 ("if when movement is
    important please direct not at shall start"). Arrangement B was chosen at packaging by sense; the independent
    check reached the same arrangement. Both are in `decryption/GLC02414.339.txt`. The darker ink may be the receiving
    operator's or the decipherer's.

### The six (now seven) unvalued code words in .339, tried against the context

Tried on 13 Nov 2026 after the test; none is given a value.
- On 4 July Halleck told Kelley to "push forward the expedition planned for General Scammon", and Kelley ordered
  Scammon to send a force to cut the Virginia and Tennessee Railroad (Official Records, Series I, vol. 27, part 3, p.
  528); on 5 July Scammon would "start the expedition without delay" (p. 550). On 8 July Scammon formed the 34th Ohio
  (mounted), the 2nd West Virginia Cavalry and two companies of the 1st West Virginia Cavalry into a brigade under
  Toland (p. 614). A telegram of 23 July reports "Colonel Toland killed and Colonel Powell mortally wounded" (p. 750);
  the index lists the expedition from Fayetteville to Wytheville, 13-25 July 1863.
- So the last sentence may ask whether "the movement" would interfere with the proposed raid ([amore]?) on the
  railroad or Wytheville ([away]?), and "our united opinion" may be Toland's and Powell's ([Missouri]?). These are
  guesses from context; no second message tests them.
- [Virginia] stands in the first text slot (where .114 has "Just" and .344 "enemy's"). [gaol] may be the plain word
  "gave"; [bent] is illegible. The first nile (row 6) does not read as Toland; read "will" it gives "Will not this
  interfere with the proposed [amore] on [away]?".

## Period decipherments whose ciphers were not found

In the same collection (`contemporary/INVENTORY.md`): .110 (3 July; the decoder strikes the code words cedar and cotton
and writes "force" and "scouts" above them), .117 and .184 (4 July: Major Cadot reports two killed and five wounded at
the front; White sends the rest of the 91st Ohio under Col. Turley; `contemporary/GLC02414.117.txt`), .116, .118, and
the October-December 1863 grids .108, .109, .111, .112, .113 and .115. Their cipher forms, if they survive, would value
more code words. The search of the folder (447 items) was by catalogue terms and by opening the neighbours of each
hit; not every number from .100 to .350 was opened. One item of the inventory was corrected at packaging: .136 is
dated "Piatt July 6" on the form, not 1 July (Powell asks leave to send White's report of the losses of "Saturday
morning", 4 July, to the families at Ironton, Ohio).

## The cipher book: not identified

Compared:
- **Cipher for Telegraphic Correspondence, Book No. 1** (Huntington Library, Eckert Papers, mssEC 43 and the printed
  1861-62 copies, items 351, 388, 428, 467, 507, 547): its six-column route is up 6, down 3, up 1, down 5, up 4, down 2.
  Venus = Position and Italy = Halleck there.
- **Book No. 2** (mssEC 47, Huntington Digital Library item 596), route pages 1-8, viewed 13 Nov 2026: the six-column
  page (p. 5) has the route down 6, up 3, down 1, up 5, down 4, up 2, and the printed commencement words Driver, Dupont,
  Dunn, Enemy, Enlist, Engage, Forward, Foote, Forts with written row counts. The commencement words of every page
  are the printed series (Army, Anson, Action ... Volunteers, Wise, War).
- **Book No. 9** (mssEC 67, item 1750; printed in full in W. R. Plum, *The Military Telegraph during the Civil War in the
  United States* (Chicago, 1882), vol. 1, appendix "Cipher Number Nine Complete", pp. 370 ff.): its six-column routes
  are 4u3d2u1d5u6d, 5u4d6u3d2u1d, 6u5d4u3d2u1d, 3d4u2d5u1d6u, 4d3u5d2u1d6u, 6u1d5u4d2u3d and 3u2d4u5d1u6d; none is ours.
- **Book No. 12**: no copy in the Huntington's Eckert Papers (a catalogue query of 13 Nov 2026 lists Books 1, 2, 5 and 9,
  mssEC 37 and 38, and Stager's memoranda mssEC 36 of 1865-67). Plum (vol. 1, pp. 48-49) says Nos. 12, 9 and 10 shared
  the printed key and arbitrary words with different meanings, and that the commencement words gave the number of
  lines and the route. Since our commencement words (Florida, Dacotah, Wilderness, Ocean, Turkey) are not among the
  printed ones of that series, No. 12 is unlikely to be the book, but it was not seen.
- **Overlap of words, not meanings.** Venus, Italy, Apple, Cedar, Whistle, Nile and Florida are printed code words in
  Books No. 1 and No. 9, with other meanings. Sycamore, amazon, apricot, cotton, currants, vermillion, gild, coat,
  plated, rye and the commencement words are not in those lists.
- **Plum on department ciphers.** Plum (vol. 1, pp. 46-48) describes the early ciphers Nos. 6 and 7, held among others by
  W. G. Fuller in West Virginia, No. 7 having commencement words that "indicated the number of lines", and says that in
  the East "department ciphers were used which were modeled after the general plan of these, but differed mainly in
  routes and arbitraries". Our telegrams fit that description; that they are a Department of West Virginia key is a
  reading of the evidence, not a proof.

Not compared: Book No. 10, the 1861 Stager ciphers Nos. 6 and 7 themselves (no copy seen), Book No. 5 (a different
system, date tables), the Fairchild book mssEC 38 (Department of the Gulf), and Stager's memoranda mssEC 36 page by page.

## Context

On 30 June 1863 Brig. Gen. Eliakim P. Scammon's division of the Department of West Virginia (the "3d Div., 8th Army
Corps" of his order of 8 July) held the Kanawha valley; its Second Brigade under Col. Carr B. White had the 12th, 34th
(Col. John T. Toland) and 91st Ohio, two companies of the 2nd West Virginia Cavalry and a battery (Official Records,
Series I, vol. 27, part 3, pp. 449, 614). The telegrams themselves place White at Fayette(ville) and Scammon at
Charleston. Facing them, Confederate Maj. Gen. Sam Jones wrote to Lee on 27 June that he was "on my way to Piney, near
Raleigh Court-House", where he had a small brigade, and would attack the Kanawha posts if he could (p. 942); on 2 July
he told Jefferson Davis that the Union side was "strongly intrenched at Fayetteville, Gauley Bridge, and Charleston",
with mounted regiments meant for raids on the Virginia and Tennessee Railroad (p. 958). White's telegrams of 2-3 July
report the same front from the other side: the 45th Virginia at Pack's Ferry on the New River, the 22nd moving toward
Raleigh, talk of an attack with six thousand, and his own night strike at the pickets before Raleigh on 3-4 July. By
mid-July McCausland had left Piney (p. 1008) and Patton was holding Pack's Ferry (pp. 1008, 1032), while Toland's
mounted brigade rode for the railroad at Wytheville (pp. 614, 750).

Page references were checked on 13 Nov 2026 in the archive.org text of the volume (Cornell copy, cu31924077700262).
The round 1 notes gave Pack's Ferry as p. 1031; the mention is on p. 1032 (and p. 1008).

## Files

- `transcription/`: the cipher telegrams as written (.341, .229, .344, .339, .185).
- `contemporary/`: the decipherments of the time (.114 grid, .137 and .138 clear copies, .185 grid, .117) and the inventory.
- `codewords.tsv`, `COMMENCEMENT.tsv`: code words with their sources; commencement words and row counts.
- `freeze/round1/`, `freeze/round2/`: the two frozen keys, protocols, hashes and results (copied byte for byte).
- `decryption/`: grids written by `verify.py`. `reading/`: the readings as sentences.
- `verify.py`: checks the hashes, the crib, re-runs the held-out test and writes `decryption/`.

## Transcriptions and the edition's terms (owner decision, 14 Nov 2026)

The transcriptions in this folder were made by the contributor from the licensed Adam Matthew edition of the Gilder Lehrman
Collection, whose terms mention only "brief excerpts". Decision: they stay in the repository. The telegrams are of 1863 and in
the public domain, the transcriptions are the contributor's own work, and no image of the edition is included or shown. If the
rights holder objects, they are to be replaced by the group counts and the readings alone.

## Remaining gaps

- .339: code words Virginia, Missouri, gaol, bent, amore, away and the first nile have no value - blocker: open-codes;
  no second message with these words and no decipherment of the time has been found; the cipher book is not identified.
- .339: arrangement of the "&", the margin "when" and the interlined "not" chosen by sense, and the readings gaol/gave,
  nile/will, at/as, away/way - blocker: illegible; not settled on the image; whose hand added the words, and when,
  cannot be settled either.
- .341: word 2 Venus/Agnes and word 14 Italy/truly - blocker: illegible; both readings kept, neither counted as a code word.
- The cipher book behind the route, commencement words and code words - blocker: no-key-material; Books 1, 2 and 9 do
  not fit, No. 12 and No. 10 were not seen.
- .341: two words under the paper repair patch - blocker: needs-physical-access; supplied from .114.

## Escalation

- [ ] siblings: the GLC02414 neighbours .108-.118, .136-.139, .183-.186, .228-.230, .338-.345 were opened; the rest of .100-.350 was not
- [x] clear-pages: the decipherments of the time in the collection (.110, .114, .116, .117, .118, .137, .138, .184, .185 and the autumn grids) checked and used
- [ ] known-keys: Books No. 1, 2 and 9 compared (routes, commencement words, code words); No. 10 and No. 12 not seen
- [x] print: Official Records, Series I, vol. 27, part 3 searched (none of the telegrams printed); Plum 1882 vol. 1 read on the ciphers
- [ ] key-rebuild: unvalued .339 words tried against the Official Records context only; no value assigned
- [ ] retry: waits on more pairs from the unopened GLC02414 items
