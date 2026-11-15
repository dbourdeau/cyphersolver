# Harford Jones's Baghdad code, 1798-1802 (IOR/L/PS/9/76/49, 51, 212, 217)

Status: in progress

British Library India Office Records, Political and Secret, IOR/L/PS/9/76: papers of Harford Jones, East India
Company Resident at Baghdad. Free IIIF images on the Qatar Digital Library (found by the QDL sweep,
`research/qdl/`). Viewed and transcribed 29 Oct 2026.

| item | QDL record | what |
|---|---|---|
| /49 | vdc_100109378677.0x000001 | Jones to Henry Dundas, Bagdad 17 Dec 1798, "true Copy" in code (2 pp.) |
| /51 | vdc_100109378680.0x000001 | "Copy - Original in Cypher. Secret." The same letter in clear |
| /212 | vdc_100109378870.0x000001 | "Translation ad Sensum" of a letter from KARAP[ET] dated Erzeroum 20 Nov, received 6 Jan; docketed "Enclosed in Sir Har[ford Jones's letter] to the Chairman ... 20 Jany 1802" (6 pp.) |
| /217 | vdc_100109378875.0x000001 | "Translation ad Sensum" of a letter from KARAPET dated Erzeroum 19 Dec, received 12 Feb (2 pp.) |

## The system

An English one-part code. Each group is `page,word`, and the pages run roughly in alphabetical order. A group
stands for a whole word, or for a letter when a word is spelled out. Letter groups sit at the start of their letter
in the book: A 1,1; B 28,1; C 29,10; D 93,66; E 123,1; F 141,67; G 161,70; I 187,63; K 213,8; L 215,23; M 228,45;
N 229,28; O 256,12; P 266,63; R 305,25; S 327,1; T 376,56; U/V 398,16; Y 439,66; Z 440,72. Second codes: C 49,10;
N 249,48 / 249,45; O 256,10; A 56,11; L 215,3; H 147,7 and 174,7; P 265,63. Pages 442-443 hold personal names,
past Z.

- Clear words are left in the text ("he had", "on the", "into"). The code is applied to the sensitive words only.
- Inflections are suffixes after the group (`230,1 ing` making, `373,52 ed` astonished, `129,70 es` enemies), or a
  third number (`177,12` have, `177,12,2` had; `13,71,7` is, `13,71,5` are).
- Function words (the, of, to, a) take groups ending `,2` on many different pages. These may be homophones, or
  "word 2 of any page" may be a rule. The pairs do not settle which.
- The alphabetical order is only rough between M and W: me 235, measure 235, would 238, with 236, while N is at 229.

## 1798 key from the pair 49/51

`ct_49.txt` holds /49 (326 groups by `align.py`'s tokens) and `pt_51.txt` holds /51 (308 words). `align.py` aligns
them by dynamic programming over (group, word, letter-in-word):
- 221 groups line up with one word each, and 104 are letters of spelled names (Constantinople ×4, Russians ×2,
  Russian, England, India).
- 74 clear words match. 4 moves are skips: "would", "if" and "Government" are not in the code copy, and one group
  `230,1` falls out where `230,1,2,2` stands for "make a".
- Output: `table_1798.tsv` (group to word) and `align_1798.tsv`.
- Nine groups get two words. The `,2` function-word groups cause most of these, plus two places where the clear copy
  paraphrases ("this Question, and a" against `302,19. 15,65. 15,65 a`).

## Test: do the 1798 values read the 1802 letters? Yes, same code book

`apply.py` applies the 1798 table to `ct_212.txt` and `ct_217.txt` and writes `decode_212.txt` and `decode_217.txt`.

| letter | groups | 1798 word value | 1798 letter value | letter fixed by a 1802 name | no value |
|---|---|---|---|---|---|
| 217 | 128 | 3 (2%) | 62 (48%) | 22 (17%) | 41 (32%), 32 distinct |
| 212 | 580 | 16 (3%) | 315 (54%) | 119 (21%) | 130 (22%), 85 distinct |

- Every 1798 group that recurs in 1802 gives sense in place:
  - `309,26` received (both headings)
  - `31,7` Bacha
  - `169,25` Government ("belonging partly to the Government of SEFLIS")
  - `271,10` party ("depart in small parties")
  - `302,31` put ("will soon put an `129,40` [end]")
  - `382,28` then
  - `353,5` some
- The spelled names read with the 1798 letters plus the new ones:
  - KARAPET; ERZEROUM; ABDULLAH × AGA; MERDIN; BAGDAD; CONSTAN(tinople); DEARBEKIR; MOOSHA; BAYEZEED; MADAN
  - PHILIPOOS × AMEREK; ARMENIANS; ASTRACHAN; EECH × MIASIN (Etchmiadzin); ERIUAN (Erivan)
  - PUMBEC (Pambak); SEFLIS (Teflis, spelled with S); KARS; ALCALZIKEH (Akhaltsikhe); TOMANS; RUSSIA(N); PERSIA
  - DAMAR × CAPI (Demir Kapı), i.e. DERBEND
- Few 1798 *word* groups recur (2-3% of the 1802 groups), because the 1802 letters are about other things. Most
  open groups are content words. The page alone places them in the alphabet:
  - `95,32` D-E, the heading formula: "dated"
  - `96,75` D-E: "December"
  - `145,56` E-I: "February"
  - `188,31` I-L: "January"
  - `255,4` N-O: "November"
  - `221,15`/`221,25` L-N: "letter"
  - `378,44` T-U: "Tartar"
  - `164,30` E-I: "General", after RUSSIAN
  - `272,17` P-R: "Patriarch"
  - `128,21` E-I: "Emperor"
  - `149,56` E-I: "Firman"
  - `262,35` O-P: "Ottoman"
  - `169,74 404,67` G / V: "Grand Vizier"
  - `394,37/38` T-U: "troops"
  - `95,50` D-E: "days"
  - `205,70` I-L: "intelligence"

  These readings are proposals from context and alphabet position. None is in `table_1798.tsv`.

## Content (proposed, not a reading yet)

The informant, an Armenian (KARAPET), writes to Jones from Erzeroum in Nov-Dec [1801]. He went in the suite of
Abdullah Aga to Merdin, then Dearbekir and Madan, and reached Erzeroum.

He reports the disputed succession to the Armenian Patriarchate (Catholicos) at Etchmiadzin:
- The Armenians at Astrachan back `442,56`. The Khan of Erivan backs `442,55`, who pays him 400 tomans and holds
  the convent.
- A Russian firman and an Ottoman firman favour `442,56`.
- A Russian General is at Teflis, with troops at Pambak, 12,000 according to /212.

He also reports:
- The Pasha of Akhaltsikhe has fled to Teflis.
- The Grand Vizier has given Madan and Erzeroum to `443,48` Pasha, who served in Egypt.
- The Russians threaten Erivan.

`442,55`/`442,56` are presumably David and Daniel, the rival Catholicoi of 1801. That is not yet checked.

## Siblings and retry (29 Oct 2026, second pass)

- **Siblings opened.**
  - /214 (Rickards/Manesty, 1801-02) uses a different system, a homophonic two-digit alphabet only for dates and a
    few words, with the body in clear: A 9/37, E 8/40, N 70, I/J 75, S 39, R 23, H 5, D 30, O 36, V 33, M 4. It
    gives "dated R-E-S-H-E-D", "the 12th N-O-V", "received the 12th J-A-N" and "made public to all the
    A-R-M-E-N-I-A-N-S".
  - /243 and /244 (May 1802) are in clear.
  - /274 (Erzeroum, 7 Aug 1802, same informant?) is in clear and names Pumbec, the Khan of Erivan, the Pasha of
    Kars and the Russian commander "Shebkatoor at Teflis".
  - /211 (interrogation of the Armenian Stephan, 8 Jan 1802) confirms the Pasha who fled Akhaltsikhe to Teflis.
  - /213 (Jones to Wellesley, 13 Jan 1802) does not paraphrase the code.
  - None is a clear copy of a coded letter, so the siblings add context, not values.
- **Key rebuild.** `proposals.tsv` gives values for 98 of the open groups, from their page position in the
  alphabet plus context, graded H/M/L. Examples:
  - ALTOON IAAK = Turkish *altun ayak*, "golden leg": "so called from having lost a leg in war and wears a golden
    or gilt [one] in the place of it".
  - "the convent of the three churches" = Uch Kilise, Etchmiadzin.
  - "not in command of the troops who are commanded by a Russian General".
  - Three misreadings resolve to 1798 values: `148,76` = 128,76 find; `160,30` = 164,30; `87,63` = 187,63.
  - DE-A-RBEND has a second A, `1,45`.
- **1798 table correction.** The DP had shifted "Government (said he emphatically)", giving `169,25` = said. It is
  now Government, with `327,66` = said (`align.py` OVERRIDES).
- **Retry** (`apply.py --retry`, `reading_212.txt`, `reading_217.txt`): 645 of 708 code groups (91%) read from the
  1798 key, the 1802 letters or a grade-H proposal. Another 32 are grade M, 25 grade L, and 6 are open.
- **Statistical test** (`docs/_validate.py`, en-modern, H values only): underdetermined. Most read stretches are
  spelled foreign names or single code words between clear words, which a letter model cannot separate from a
  fitted key.
- **Names.** `442,55`/`442,56` are presumably the rival Catholicoi David and Daniel. The two letters disagree on
  which one arrives at Erzeroum to be escorted, so both are graded L.
- Work stopped here at the user's request (29 Oct 2026): the session turned to logging the sweep.

## Remaining gaps

- 212/217 groups with only an M or L value (57 tokens) and 6 open tokens (443,48 x3, 48,75,3, 239,69, 53,36) - blocker: open-codes; workable from context, set aside on 29 Oct 2026 when the session turned to logging the QDL sweep
- The `,2` function-word groups (homophones or a rule) - blocker: open-codes; untested
- Name groups 442,55 / 442,56 (which Catholicos) - blocker: open-codes; the two letters conflict, needs a history of the 1801-02 succession
- Transcription doubts (/49 superscript over `187,3`, blotted `179,7`; /217 `213,7` vs `213,8`; /212 SGUSGEG after DERBEND) - blocker: open-codes; re-read at higher zoom

## Escalation

- [x] siblings: /214, /243, /244, /274, /211, /213 opened 29 Oct 2026 (see above). None is a clear copy of a coded letter; /214 uses another system.
- [x] clear-pages: /51 is the clear copy of /49 and gave the 1798 table. /212 and /217 are themselves English "translations ad sensum" with no clear version of the coded words on their leaves (all six and two pages viewed 29 Oct 2026).
- [x] known-keys: the 1798 table from 49/51 applied to 212/217 (apply.py). The code book itself is not identified; it may be a printed vocabulary of about 445 pages with names after Z.
- [x] print: web search 29 Oct 2026 found no edition or study of these letters or of Jones's cipher.
- [x] key-rebuild: proposals.tsv, 98 groups bracketed by page and context, graded H/M/L.
- [x] retry: apply.py --retry, 91% at grade H or better; validation underdetermined.

## Files

- `ct_49.txt`, `pt_51.txt`, `ct_212.txt`, `ct_217.txt`: transcriptions from QDL IIIF crops.
- `align.py`: builds the 1798 key and writes `table_1798.tsv` and `align_1798.tsv`.
- `apply.py`: applies the 1798 key to 1802 and writes `decode_212.txt` and `decode_217.txt`. `--retry` adds
  `proposals.tsv` and writes `reading_212.txt` and `reading_217.txt`.
- `proposals.tsv`: graded values for the groups with no 1798 value. `validation.tsv`: pairs for `docs/_validate.py`.

## Dudout corrections, 29 Oct 2026
- Held-out check of the 1798 table (ct_49/pt_51/align_1798.tsv): table from /49 f. 1r only (129 rows), tested on f. 1v: letters 0.959 (70/73, 0 wrong) against witnesses max 0.329. Groups x,2 are not fixed values. New sibling leads: IOR/L/PS/9/76/134 (Malcolm to Jones, Shiraz Aug 1800, partly in cypher) and BL Add MS 41767-41768 (Jones papers).
(Brice Dudout, research/dudout_2026-10-29/; his findings, not re-checked here.)

## The code book is Entick's New Spelling Dictionary (Andrew Beling, with AI agents, 15 Nov 2026)

All of this section was done by AI agents (Opus) on 15 Nov 2026 for Andrew Beling. No person has checked any reading
in it. It adds files, appends this dated section to NOTES.md, and appends seven solution steps, one credit and
`outcome.provenance` to profile.json; no earlier line of any file is altered or removed. Where it corrects this
folder's values, the old value, the new value and the evidence are in the added files.

### The book and the rule

- **Book.** John Entick, *New Spelling Dictionary* (revised by William Crakelt), in the setting of the Internet
  Archive copy `bim_eighteenth-century_enticks-new-spelling-di_entick-john_1795_0` (title page dated 1795). The
  Internet Archive copy dated 1796 seems, from its machine-read text only, to be in the same setting. It was not
  compared page by page, and no 1796 page image was looked at. Which of 1795 and 1796 Jones had is not settled. The
  1787-1791 settings do not fit.
- **Opening a page.** Printed page p is image p + 35 of the item: file
  `..._1795_0_jp2/..._1795_0_{p+35, four digits}.jp2` in its `_jp2.zip` (page 217 is image 0252). In the viewer this
  is normally `https://archive.org/details/bim_eighteenth-century_enticks-new-spelling-di_entick-john_1795_0/page/n{p+35}`
  (the viewer link was not opened in this work; the image numbers were).
- **Rule.** A group `p,n` is printed page p, printed line n. Column a is lines 1 to 39, column b lines 40 to 78
  (k + 1 onwards when column a has k lines; page 366 has 40). Continuation lines of an entry are counted. A third
  number k is the k-th word of that line, part-of-speech abbreviations not counted (`13,71,5` are, `13,71,7` is,
  `177,14,2` had, `285,35,2` Political).
- **Name pages 442-443: a separate rule, found after the fact.** These two pages are the list "The most usual
  Christian names of men and women", set in five columns, with letter headings and blank rows between the letters.
  The rule above does not apply there: a blind reader who applied it (an independent package check, below) read
  Benjamin, Bennet and Jeffry. The numbers fit another count: the n-th name on the page, running down the five
  columns in turn, letter headings and blank rows not counted. On page 442 column 1 ends at Anselm (18), column 2 at
  Blase (35), column 3 at Cuthbert (52); then Cyprian 53, Cyril 54, **Daniel 55, David 56**. On page 443 column 1
  ends at Hubert (32); then Hugh 33 ... Joscelin 47, **Joseph 48**. This count was found by the package checker and
  confirmed by the packaging agent on the page images (both AI, neither blind); it was not set before any test. In
  `entick_lines.tsv` these rows have column `n1`-`n5` (column of the names list) and the place of the name in that
  column.
- The letter codes are the first entry of each letter (`249,48` NAB for N, `213,8` KAlendar for K, `49,10` CAB for C),
  with exceptions listed under "Not explained".

### Files added

| file | what |
|---|---|
| `entick_lines.tsv` | the Entick lines the three letters use (page, line, column, line in column, entry or continuation, first word), each with the line before and after; whole-line text where a group has a third number. From blind counts of the page images: two AI counters per page, 186 pages, 0 disagreements in line count or line type. On pages 442-443 the "line" is the name count above. Public domain text; no page image is committed. |
| `ct_49_reread.txt`, `reread_49.tsv` | /49 re-read blind (see below); the table lists every group that differs or stays doubtful, with each reader's figures. |
| `ct_212_reread.txt`, `reread_212.tsv` | the same for /212. |
| `entick.py` | applies the rule to `ct_49_reread.txt`, `ct_212_reread.txt` and `ct_217.txt` (as it stands); writes `entick_49.tsv`, `entick_212.tsv`, `entick_217.tsv` (group by group: dictionary line, value, this folder's value and grade, status), `reading_49_entick.txt`, `reading_212_entick.txt`, `reading_217_entick.txt` and `entick_217_suggest.tsv`. Standard library only; two runs give identical bytes. |

The `folder_grade` column of `entick_*.tsv` names where this folder's value comes from: `H`, `M`, `L` are the grades
of `proposals.tsv`; `1798w` a word value of `table_1798.tsv`; `1798l` a letter value of `table_1798.tsv`; `1802l` a
letter fixed by the 1802 names (`apply.py`'s `LETTERS_1802`); `open` no value. For /49 the grade is the clear copy
/51 (`clear copy /51` for a word, `letter (clear copy)` for a letter of a spelled name), and `skipc` is the one group
(`230,1`) that `align.py` skipped. In `reread_*.tsv`, R1, R2 and R3 are the three AI readers of the digits (below).

`python targets/jones1802/entick.py` rebuilds every output above from the committed files.

### How it was found and tested, misses included

1. **Letter starts.** The page where each letter begins in Jones's code (A 1, B 28, C 49, ... Z 440, using the
   second codes for C and N) fits the 1787-1795 settings of Entick with no rescaling (21 of 21 letters within 3 pages).
2. **Word test, pre-set: MISSED.** 25 words by a fixed rule, headword on Jones's page: 18 of 25 for the 1787
   setting against a mark of 20 (1791: 13, 1795: 14, 1798: 13).
3. **Page test, pre-set: MISSED.** 122 fresh groups from `table_1798.tsv`: 51 of 122 (42%) on the page for 1787,
   against a mark of 80%; 1795_0 61 (50%). Controls (other editions rescaled, Bentick 1786) 10-29%.
4. **Position test, pre-set: MISSED.** The printed-line rule was chosen among four counting rules on 15 training
   groups (8 of 15 exact) and frozen. Held-out image subset: 14 of 36 at the exact line against a mark of 60% within one line; shuffled 0 of 36.
   17 of the 36 words were not on their page at all; of the 19 that were, 14 sat on the exact line.
5. **After the fact:** reading a figure 2 in `table_1798.tsv` as 4 put 22 more groups on their exact line; reading
   4 as 2 put none.
6. **Blind digit test, pre-set: PASSED.** The 22 disputed groups were cut from the Qatar Digital Library scan of /49
   and read by two AI readers told nothing of the question: 20 and 22 of 22 read as 4 (mark 16 of 22); control
   groups read right 92-100%.
7. **Blind re-reading of all of /49** (below), then the **confirmation test, pre-set: PASSED.** With the re-read
   digits and the frozen rule, 101 of 137 test groups have their clear-copy word on the exact Entick line (73.7%;
   mark 60%). Shuffled control (1000 shuffles): 0.66% (mark under 10%), 95th percentile 3, max 5. Secondary figures,
   set beforehand and not used for the verdict: with the bare `p,2` groups 102 of 150 (68.0%); without the 22 groups
   of step 6, 83 of 117 (70.9%). The test was run once.
8. **Independent check of this package, pre-set** (a further AI checker, 15 Nov 2026, blind readers): the dictionary
   line table, 21 of 24 sampled rows read the same from the page images, against a mark of 22: MISSED, the three
   misses being the name rows `442,55`, `442,56`, `443,48`, where the column rule does not apply (see the name-page
   rule above); the re-read /49 digits, 20 of 20 sampled changed groups read the same, against a mark of 16: PASSED.
   The script and the counts reproduce.

Each plan was written and hashed before its test was run. The plans, the test items and the scoring scripts are in
the contributor's files, not in this folder; what this folder rebuilds is the full look-up (`entick.py`).

### Re-reading of the digits

**/49.** Three AI readers read the Qatar Digital Library scan of /49 line by line (38 line crops in shuffled order,
nothing else given): the first and second readers (R1, R2) read every crop, a third (R3) read every crop with a
disagreement and decided it. R1 and R2 agreed on 520 of 660 number fields; R3 sided with R2 135 times and with R1 4 times; 1 field stayed doubtful.
**98 of 326 groups differ from `ct_49.txt`, and 4 are doubtful** (137,1,5 perhaps 13,71,5; 20,2; 32,1; 187,3).
The figure changes are 2 to 4 ×125, 5 to 6 ×2, 0 to 9, 1 to 4 and 2 to 8, plus three structural changes: 122,33 to
22,33, 179,7 to 179,70 (an ink blot) and 220,50 to 240,5 (which holds a further 2 to 4). Most are a figure 4 typed as 2: the copyist's 4 is an open L-shaped figure. With the
re-reading the letter codes in /49 become C `49,10` and N `249,48`, the codes /212 uses.

**/212.** Two AI readers read all 141 line crops; they disagreed on 3 of 1176 fields, and a third reader settled
them. 9 of 580 groups differ from `ct_212.txt` (29,10 to 49,10 ×2; 236,23 to 436,23; 188,31 to 180,31; 265,63 to
266,63; 205,2 to 295,2; 250,48 to 258,48; 113,50 to 115,50; 106,71 to 166,71 at its second place), 2 are doubtful.
The 2-for-4 slip is a /49 problem. Two of the nine re-readings, `188,31` to `180,31` and `106,71` to `166,71`, turn
this folder's sensible value (January, difficulty) into a word with no sense in place (Heresy, Glaver). They are
doubtful re-readings, not corrections, and are flagged in `reread_212.tsv` for a person to look at; the blind
readers' figures are kept as recorded.

**/217 was not re-read**: its scan is not among the files used.

### Against this folder's values

From `entick_212.tsv` (status per group; the grades are this folder's):

| this folder's value | agrees | corrected | other |
|---|---|---|---|
| H (word) | 57 | 18 | 1 does not fit (`87,63`, a proposal for the letter I, as `187,63`; line Cradle) |
| M | 13 | 10 | 1 does not fit (bare 295,2) |
| L | 2 | 16 | |
| 1798 word value | 7 | 9 | |
| open | | | 6 filled |
| letters (1798 and 1802) | 370 of 441 | | 71 do not start their line |

Not all "corrected" values are corrections of sense:
- the 9 corrected 1798 values are all `31,7`, which Entick spells Bashaw (this folder: bacha);
- 6 of the 18 corrected H values are `50,66`, whose line is Can ("v. n. to be able" / "s. a vessel"): Khan by sound
  only; it is marked doubtful in the readings;
- 10 corrections give words that make no sense in place (5 at grade H, 5 at grade M; listed under "Not explained").
  Two of them come from doubtful re-readings (`180,31`, `166,71`).

The corrections that give sense: `371,76` steward to Superintendent; `345,13` Shah to Silver; `239,69` (open) Mine,
"superintendent of the silver mine"; `37,36` clergy to Bishop (×2); `40,20` corps to Body ("a body of 12000
troops"); `162,9` get to Gain ("gaining intelligence"); `156,48` form to Fortify ("fortifying all the frontier");
`159,42` forces to Frontier (×3); `436,23` war to Winter ("the winter in these parts will soon put an end to all
intercourse"); `224,24` more to Little ("some little time"); `245,34` not to More ("more serviceable"); `339,23` seem
to Serviceable; `254,66` news to Notice ("we have notice that"); `295,8` progress to Proceeding; `21,55` appointment
to Arrangement; `23,63` assistance to Assignment; `442,55` = Daniel and `442,56` = David (this folder has them the
other way round; 10 places). Gaps filled: `443,48` Joseph (×3, "Joseph Bashaw", i.e. Yusuf Pasha), `239,69` Mine,
`53,36` Carry, `48,75,3` the third word of the By line.

**/49** (the test letter, `entick_49.tsv`): of 221 coded words, 151 are on the exact line, 8 within one line, 62 do
not fit; of 104 letter groups, 91 start their line with that letter.

### The third letter, /217 (after the fact)

The confirmation work did not treat /217. `entick.py` applies the frozen rule to `ct_217.txt` as transcribed here,
digits not re-read. Of its 128 groups:
- 15 word groups are on pages that were not counted (`96,75`, `145,56`, `337,65`, `257,44` ×2, `320,8`, `210,10`,
  `361,65`, `226,22`, `219,78`, `165,76`, `168,42`, `44,38`, `78,19`, `27,22`): no value from the book;
- of the 28 word groups on counted pages, 18 agree with this folder's decode and 10 do not: `31,7` Bashaw (same
  word); `50,66` Can ×2 (Khan by sound); `442,56` David ×2 and `442,55` Daniel (the same swap as in /212); and 4
  words that make no sense in place: `221,15` Level (for letter; Letter is 221,5), `249,61` Nameless (Name is the next
  line), `138,31` Exhorter (for expelled), `139,13` Expence (for express);
- of the 85 letter groups, 66 start their line with their letter; 19 do not (the I and U codes, `249,45` for N, and
  `213,7`, whose line is Ivy while `213,8` is KAlendar: this supports reading `213,8`, the doubt already listed).
- No group that fails as written fits with one figure 2 read as 4 (`entick_217_suggest.tsv` is empty), so there is
  no 2-for-4 suggestion to check on the manuscript.

### Readings

`reading_49_entick.txt`, `reading_212_entick.txt`, `reading_217_entick.txt`: each code word is the word of its
Entick line. `[p,n]` is a group that does not fit (one unread word); `[?word]` is a word the line gives but that is
doubtful (within one line of the clear word in /49, no sense in place, `50,66` Can, or doubtful digits). A lowercase
letter inside a capitalised name is a letter code whose line does not start with that letter.

Read shares, sure words only (`research/reading_audit/v10_relabel.py`'s count, every `[...]` and `[?word]` a hole):
- /212: 0.984 (1014 words, 17 holes). Counting every name with a letter not explained by the book as a hole: 0.937.
- /217: 0.923 (264 words, 22 holes); 0.888 the strict way.
- /49: 0.769 (250 words, 75 holes); 0.742 the strict way. /49 stays read from its clear copy /51; this is the test.

`docs/_check_reading.py`'s sentence score (share of clean sentences): 0.60 (/212), 0.48 (/217), 0.20 (/49). The
running texts carry no punctuation, so its sentences are long.

These readings are preliminary. They are not entered in `profile.json` `outcome.texts` and carry no
`reading_review`: that is for a reviewer other than their author. `reading_212.txt` and `reading_217.txt` are left
as they were.

### Not explained

- The bare `,2` groups: 19 in /49, 1 in /212 (`295,2`). Of the 13 different bare `,2` groups in /49, only one has its clear-copy word on line 2 of its page.
- 12 function words in /49 coded with a small second number (`7,8` am, `8,5` of, `19,5` in, `24,4` of, `29,3` by,
  `30,4` of, `35,6` with, `41,4` of, `49,3` that, `49,6` of, `56,6` the, `67,5` the).
- The letter codes for I and U: `187,63` is Hypothetically (the I entries start at line 68) and `398,16` is Tyro (one
  line before Vacancy); also `249,45` for N (three lines before NAB). They are used consistently (I 41 times in /212).
- 10 dictionary words in /212 and 4 in /217 that make no sense in place: `180,31` Heresy (January?), `166,71`
  Glaver, `160,30` Fugitive (General?), `394,33` Trode, `387,24` Toad, `156,57` Fortunateness, `237,18` Mercifully,
  `221,25` Levigate, `433,25` Where, `160,73` Fun (Function is the next line); /217 as above. A figure or count
  problem is likely; not resolved.
- 23 of the 137 test groups of /49 have their word nowhere on the page (`75,28` conversation on the Conference line,
  `138,32` French on Exigence, `154,12` force, `204,72` instant, `254,57` not, `433,62` which, `440,49` you, `127,86`
  embarrassed, whose line number is beyond the 78 lines of the page, and others in `entick_49.tsv`).
- After the fact, not tested: the name-page count of pages 442-443 (above), which gives Daniel, David and Joseph.
- After the fact, not tested: the four-number group `13,70,7,8` reads "I am" as words 7 and 8 of line 70 of page 13
  ("see. The present tense runs thus; I am,"); this folder's tokens split it in two.
- Which claimant comes through Erzeroum: /212 has David (`442,56`) arriving at Erzeroum and Daniel paying the Khan;
  /217 has `442,55` Daniel arriving and the Khan taking 400 tomans from David. The swap of the two names does not remove
  the conflict between the letters.

### Not done

- The 1796 copy was not compared page by page with 1795_0 (the planned machine comparison was swamped by OCR noise);
  no 1796 page image was looked at.
- /217's digits were not re-read, and 15 of its word groups are on dictionary pages not yet counted.
- No person has checked any re-read digit, any line count or any reading. Places for a person's look first:
  /212 `180,31` (read 188,31 before; January becomes Heresy) and `166,71` (106,71 before; difficulty becomes Glaver);
  /49 `154,42` (f. 1r line 7), where the package checker's reader read 154,22 as `ct_49.txt` has it; the second
  `249,48` on f. 1v line 18 (that reader gave 249,28 first); and `382,25`, `432,14`, `321,13`, where that reader saw
  a 4 and the re-reading keeps a 2.
- Prior identification: Tomokiyo's Cryptiana (code index, the Wellington dictionary-code page, the Drake-Nelson page,
  the book-code page; its blog searched for "Entick" and "Harford Jones") and three web searches found no earlier
  identification of Jones's book. Cryptiana's book-code page describes Entick used as a code book by John Jay, Arthur
  Lee, Francis Dana, Aaron Burr (page and line, a mark for the second column) and the British army; nothing for Jones.
  Other Cryptiana pages and the Qatar Digital Library catalogue notes were not searched.
