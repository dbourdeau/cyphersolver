# Communist Party of America book code: letters seized at 170 Bleecker St., New York, 1920-21

Status: in progress. Contributed by WAINUT (27 Oct 2026). Key grid rebuilt from the Bureau of Investigation's own
decodes; read in part. The book is not identified; the known-keys, print and handwritten-page steps below are open.
The site page and the ledger rows are left to the maintainer.

Catalogue 678. Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents;
the transcription was made with a vision-capable language model. Every run was read from the NARA scans. Most runs
were read a second time, independently, by another agent; A0014, A0706 and A887 run 2 were checked in a later pass
against the page images. The faint runs of A0887 and the torn run of A0886 were re-read on enlarged crops.

## 1. The documents

- **Source.** NARA RG 65, Investigative Case Files of the Bureau of Investigation 1908-1922, Old German Files
  (M1085), roll 940, case 202600, "202600-1775 THRU 202600-1949-1 (4 of 4)",
  [naId 369272950](https://catalog.archives.gov/id/369272950). The roll is served as three large PDFs, M1085-940A,
  -940B and -940C (`https://catalog.archives.gov/medialz/dc-metro/rg-065/833671/M1085/M1085-940/M1085-940A.pdf`, and
  the same with B and C). They are stamped "Copies of Letters & Documents Found at 170 Bleecker St.".
- **What they are.** Typed copies, made by the Bureau, of letters between district organizers ("D.O.") of the
  Communist Party of America and the Executive Secretary ("Exsec"), 1920-21. The letters are in clear English.
  Names, addresses, dates and a few other words are in a book code. Under many runs the Bureau typed its own
  decode ("Decode: ...").
- **Pages with runs.** Page numbers are PDF pages (A0015 = 940A p. 15). A text-layer scan of all 3,222 pages,
  and a look at every page it flagged, found **28 runs on 14 typed pages, 439 tokens**: A0011-A0015, A0493,
  A0527, A0706, A0880, A0886-A0888, A0939 and B0494. 940C has no runs. The catalogue's "77 runs, about 2,400
  tokens" was not reproduced: the text layer also counts dates and ratios, and handwritten letters have no text layer
  and were not searched page by page. So 77 is neither confirmed nor refuted. The catalogue row should give 28 runs
  and 439 tokens on typed pages until the handwritten pages are searched (the next step).
- **The Bureau's decodes.** 16 of the 28 runs carry a Bureau decode: 15 in the new code (A0011, A0012, A0013, the
  four runs of A0015, three on A0886, three on A0887, two on A0939) and the one old-code run (A0014). They are
  transcribed and aligned token by token in `bureau_decodes.tsv`.

## 2. The system

- A token **a/b** is line *a*, letter *b* of one page of a book, with letters counted **without spaces**. On line 2,
  the Bureau's words give letters 3-9 as E N O C H A R, contiguous, and the struck typed word "arden" after 2/8-2/12
  on A0880 fits the rest (ENOCH ARDEN). A dash separates words.
- Any cell that holds a letter can be used for it, so the code is homophonic. Doubled letters take two different
  cells (HARR = 2/7 2/8 2/9 3/4).
- **Two key pages.** The circular of 24 Jan 1921 (A0880) says that telegrams from the National Office will be signed
  in the "Old code page 14" and in the "New code last page". A0014 is the only old-code run with a decode. On that
  page numbers are spelt out (2600 = TWENTY SIX HUNDRED). All other runs are in the new code.
- **Digits (new code).** A digit token points to a digit character printed at the start of a key line. All 40 digit
  tokens in the Bureau-decoded runs sit at letter position 1 or 2 of their line; only 1 of 297 letter tokens does,
  and that one is a slip (see A11 below). No cell is ever used for two different digits. The lines seem to start
  with a two-figure number and a title: **37** IDYLLS OF THE KING, **7?** ENOCH ARDEN, **?8** FRIENDSHIP,
  **40** O?GO..., **42** M?M?RI..., **56** ..., **?8** POE...
  An earlier working rule, "a digit is the first letter of its English name" (1 = O, 4/5 = F ...), fits the Bureau's
  numbers but not the cells: under it 4 and 5, 6 and 7, 2 and 3 would share cells, and they never do. We call the
  digit-character model strongly supported, not proven: no key page has been found.
- **The book.** Not identified. The page looks like a numbered list of titles, perhaps the advertisement page at the
  back of a pocket series. No search of book lists was made.

## 3. The key grid and its test

`decode.py` builds the grid from the Bureau's decodes **only** (`bureau_decodes.tsv`): 112 cells in the new code,
27 in the old (`key_new.tsv`, `key_old_p14.tsv`, with the runs that attest each cell). The grid rows are printed in
`decryption.txt`.

**Leave one run out.** For each of the 15 Bureau-decoded new-code runs, the grid is rebuilt from the other 14 runs
and predicts that run.

| | right | wrong | no value in the other runs |
|---|---|---|---|
| letters | 251 | 4 | 42 |
| digits | 34 | 1 | 5 |

All five misses are clashes inside the Bureau's own decodes, not failures of the grid:

1. **5/14, U or Y.** The Bureau typed "SOVRYS" on A0939. 5/14 is U in six other Bureau words, so the run reads
   SOV. RUS., the magazine *Soviet Russia*.
2. **1/2, I or 7.** It is 7 in 773 (A887.1) and I in OHIO (A11). 1/2 is a digit position; the writer of A11 most
   likely typed 1/2 for 1/3, which is I. The decoding uses 7.
3. **26/30, Z or L.** Z in "Speizman" (A887.1), L in "K-ldas" (A15.2), once each. Unresolved; shown as [L|Z].

**Controls.** A shuffled grid (500 repetitions) gets 4.7% right, chance level. The grid shifted one line down gets
3 right and 178 wrong; shifted one letter along, 13 right and 160 wrong.

An independent check, with its own script, earlier on the same day gave the same picture on 11 runs (216 right,
1 wrong, 31 unseen; shuffled grid 6.1%).

## 4. The readings

Line by line in `decryption.txt` (output of `python decode.py`). Coded words inside clear sentences are read as
sentences in `reading.md` and `reading_a0706.md`. The plaintext is English. Most runs are names and addresses, not
prose, and are marked so in `profile.json`.

**Runs the Bureau decoded (checked, 16 runs).** Hugo S---l, 148 Jackson St., Sandusky, Ohio (A11); Paul Stockman,
a district organizer's official name (A12); Frank Thomas, 446 E. Washington St., Phoenix (A13); Wm. Burns,
2600 Oakdale St. (A14, old code); S. KRGA, 1615 St. Clair St., Racine; Chas. K?LDAS or K?ZDAS, 23?8 Julia Str.,
Milwaukee; Joe Rasheta, 504 Park Ave., Racine; Peter Barry, 48? Milwaukee St., Milwaukee (A15); S. Minski,
1320 18th St.; Emil Smi[th], 1 R 11 Curtis; [..]ERIC Sahlin, 808 Montana Av. (A886); Harr[y] Speizman, 773 8th St.,
Milwaukee; Joe Poltn, 1208 Winter St., Superior; W. J. Schnetrum, 1624 Oake Ave., Superior (A887); I. W. and
SOV. RUS. (A939). Where the grid differs from the Bureau:

- A939: SOV. RUS., not the Bureau's SOVRYS.
- A11: the Bureau's "S---l" stays open (no other run uses 3/17, 3/13, 3/18).
- A15.1: the Bureau wrote "S. Ki?ga" and struck "S. K". The grid gives KRGA (3/4 = R in 8 Bureau words; G only from
  HUGO). The name stays doubtful.
- A15.2: the Bureau's "23-8" has a digit token (14/2) with no attested value; 2308 if 14/2 is 0 [?].
- A886.3: the Bureau's decode is torn ("[..]hlin"). The grid gives the first name as [..]ERIC, very likely Eric
  Sahlin. The page is torn before it, so a token may be lost.

**Runs the Bureau did not decode (12 runs).**

| run | clear context | reading | note |
|---|---|---|---|
| B494 | "I shall see to day Comrade [run] (this is his right name)" | **S. RUBIN** | B = 10/15 from Barry; every other cell in 2 or more Bureau words |
| A493 | "the application by this district for [run]" | **MINOR** | who is meant is not known; Robert Minor is a guess |
| A527 | "delegates to the unity convention elected by [run]" | **MAY 12** | 2 = 6/2, as in 1624 and 1208 |
| A888 | "Mr. Louis De Philips Address [run] Phila. Pa." | **1148 S. 8[th] ST.** | |
| A706.1 | "[run] Delegate of P A C arrived here Monday" | **AT[?]OOD** | very likely ATWOOD; W is not attested |
| A706.2-6 | "two members of [U?P] ... three members of [?P]" | **U[?]P** and **[?]P** | if 5/12 is C: UCP and CP; C is not attested |
| A880.1 | old-code telegram signature | UR[?][?][?] | the page-14 grid has one decode only |
| A880.2 | new-code telegram signature | AR[?][?][?] = **ARDEN** | D E N rest on the struck typed word "arden" alone |

On A706 the sentences make the three-token group the writer's own side ("two members of U[?]P ... Grey and Conner
from our side") and the two-token group the other side. If Grey wrote as a CPA organizer, his own side would be
expected to be the CP, the reverse of what 5/12 = C gives; one more reason to leave 5/12 open. What "P A C" is, and
where Grey wrote from, are not established; the report mentions "the S.P. of the C." and "Finns". These are leads
only, not checked.

**B0494's date.** The copy is typed "January 24, 1920". The letter says the man "left the S.P." after "January
raids" and joined a group "organized about three months ago", which fits January 1921 better. The year may be a
typing slip. Not settled.

## 5. Prior work

- The Bureau's own "Decode:" lines and pencil glosses on the copies (1920-21) are the contemporary decipherment of 16
  runs. They are credited here as `contemporary`, roles "prior solution" and "key or decipherment used": the grid
  comes from them alone.
- The catalogue's prior-art check (27 Oct 2026: the repository's lists and the NARA READMEs) found no published
  reading. Not checked: Theodore Draper, *The Roots of American Communism* (1957), Harvey Klehr and John Earl Haynes
  on the underground party, the Early American Marxism archive on marxists.org (Tim Davenport; many Bureau documents
  on the 1920-21 underground CPA, among them a 1921 New York Times piece on the Bleecker St. raid), and the other
  three parts of case 202600 on roll 940. Any of these could print the Bureau decodes or name S. Rubin and Atwood.
  **No printed decipherment was found, but the search was not done; no "no published reading" claim is made.**

## Remaining gaps

- The key book (new code, last page) and the old code page 14 - blocker: no-key-material. The grid rows suggest a
  numbered list of titles; not identified.
- Cells with no value - blocker: no-key-material; no Bureau decode uses them: 3/17 3/13 3/18 (A11), 18/6 (A15.2),
  3/1 (A15.4), 14/2 (A15.2), 5/29 (A706.1), 5/12 and 5/13 (A706), three cells of the old-code signature (A880.1).
- 26/30, Z or L, a clash inside the Bureau's decodes - blocker: no-key-material.
- Two cut tokens and possibly lost tokens at the torn edge of A0886; the last token of A887.3 - blocker: illegible.
  The originals of the copies were not traced.
- The struck typed word after the old-code signature on A0880 - blocker: illegible; about 8 letters, starting with s.
- Runs in handwritten letters (the catalogue's 77 runs against 28 found here) - blocker: not-attempted; the
  handwritten pages have no text layer and must be looked at page by page (next step).

## Escalation

- [x] siblings: all three PDFs of roll 940 scanned by text layer; 940C has no runs. The other three parts of case
  202600 were not opened (next step).
- [x] clear-pages: the clear text around every run is used as context; A0880 gives the two key pages.
- [ ] known-keys: the book is not identified (next step). Lead from the maintainer's review: the grid lines read as a
  numbered list of titles (37 Idylls of the King, 7? Enoch Arden, ?8 Friendship, Socialis[m]?, 42 Memories?), which
  fits the back-page list of a numbered pocket series of 1919-21; Haldeman-Julius's *Appeal's Pocket Series*
  (Girard, Kansas, 1919 onward) is the first to check. Its title list would fill the open cells (3/13 3/17 3/18,
  5/12, 5/29 ...) and settle ATWOOD, U?P/?P and S---L. Not yet checked.
- [ ] print: Draper (1957), Klehr and Haynes, and the Early American Marxism archive on marxists.org were not checked.
- [x] key-rebuild: the grid is rebuilt from the Bureau decodes and tested by leave-one-run-out and three controls.
- [ ] retry: handwritten pages could hold more runs; a page-by-page look is needed. Open runs to be retried once the
  book's title list is found.

## Files

- `transcription.txt`: the 28 runs, page by page, with their clear context
- `bureau_decodes.tsv`: the Bureau's decodes as written, aligned token by token
- `decode.py`: grid, leave-one-out test, controls, digit test and decoding (standard library). `python decode.py`
  prints `decryption.txt`; `python decode.py --key` writes the two key files
- `decryption.txt`: output of `python decode.py`
- `key_new.tsv`, `key_old_p14.tsv`: the grids, with the runs that attest each cell and the clashes
- `validation.tsv`: each token with its grid value, for `docs/_validate.py` (`python decode.py --pairs`). The test
  is underdetermined: 3 tokens per cell on names and addresses are too few for the letter model to tell the grid
  from a key fitted to shuffled text. The leave-one-run-out test in `decryption.txt` is the stronger check.
- `reading.md`, `reading_a0706.md`: the coded words inside their clear sentences

## 14 Nov 2026: reading review recorded

`reading.md` and `reading_a0706.md` were read as sentences against `decryption.txt` (Claude, session of 14 Nov 2026). Both
are clear typed English with single coded words; the sentences are coherent. `reading_review` grade A recorded on both
entries in `profile.json`; states unchanged (A0706 read in part: the cells 5/29, 5/12 and 5/13 have no value). Pages not
re-opened.
