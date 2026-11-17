# William H. Crawford to James Monroe, Paris, 5 Nov 1814 ("Despatch No 33-2, Private"): a coded letter in WE025

Contributed by Andrew Beling, with AI agents, 15 November 2026. Status: read, with nine groups supplied from the
sense (section 3). No printed text or period decipherment of the coded part was found (section 5).
The site page and the ledger rows are left to the maintainer.

## 1. The document

- **Source.** NARA RG 59, Despatches from US Ministers to France vol. 15, microfilm M34 roll 18
  ([naId 188673229](https://catalog.archives.gov/id/188673229), "Sept. 10-Dec. 30, 1814"), frames 0063R to 0067L, e.g.
  [frame 0064](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M34/M34-018/M34-018-0064.jpg).
  Heading on 0063R: "(Despatch No 33-2) Paris 5th Novr 1814 / Private / My dear Sir". Crawford's own hand, signed
  "Wm H Crawford" on 0067L. The official Despatch No. 33 of the same day (clear, on the Decatur) begins on 0061R; the
  docket "Wm H. Crawford Paris 5 Nov 1814" is on 0069L.
- **Code.** About a third of the letter is in code, on 0064R, 0065R and 0066L: 292 groups in 39 lines, with words in
  clear written in among them. There is no interlinear decipherment on the film.
- **Neighbouring frames checked for a decipherment** (0059-0063, 0067-0070): 0059R-0060R the private letter No. 32-2
  of 21 Oct (clear); 0061R-0062L Despatch No. 33 (clear); 0067R the last page of a clerk's clear fair copy of this
  letter ("Seven millions of inhabitants ... Signed Wm H Crawford"), whose earlier pages are not on this roll; 0068-0070
  copies of notes to and from Jaucourt (3, 14 and 17 Nov). None carries a decipherment of the coded passages.

## 2. The code and the key

The groups are in the code Ralph E. Weber, *United States Diplomatic Codes and Ciphers, 1775-1938* (1979), prints in
full as WE025 (pp. 443-454; an earlier version of these notes gave 470-480, which are the page numbers of our scan,
not of the book): 1355 = the, 1397 = of, 1554 = to. It is the code of Poinsett's letters
([`../poinsett1813/beling`](../poinsett1813/beling/README.md)), and Weber found that Crawford used it in 1814
(foreword: a Crawford letter to the commissioners at Ghent in the Papers of Henry Clay).

- `key/we025_crawford1814.tsv`: the 156 WE025 rows for the numbers that occur here, cut by `key/extract_key.py` from
  our transcription of Weber's table, frozen by sha256 at 2026-11-11T10:37:23Z before any decoding (the same frozen
  table as `../poinsett1813/beling/key/`, sha256 `26dad03e...`; its one logged later correction, 668 = fect, does not
  occur here). Nothing in the table was changed for this letter. `key/SHA256.txt` holds the hash of the cut, which
  `decode.py` checks.
- Crawford's marks are read as in the Poinsett work: a small diamond above a group is plural -s; a caret is -ed; one to
  three r-strokes under a group drop that many final letters (1036 crisis with three = cri, 1048 ficent with two =
  fice: sa-cri-fice; 1046 spire with one = spir: con-spir-acy; 367 could with two = cou: dis-cou-er-ed); a small cross
  under a group doubles a letter (1115 al = all in rec-all-ing; 372 gle = ggle in stru-ggle).
- These marks are the code's own. After the table Weber prints its directions (p. 454, seen on the page image on
  15 Nov 2026, after the reading was made): a diamond makes a noun genitive or plural and a verb third person singular;
  a caret makes a verb a past participle or imperfect; a cross under a figure doubles the letter in the matching place
  (last figure, last letter; the one before, the letter before; and so on); a tick under a figure "withdraws the letter
  corresponding"; and u and v, i and j, are interchangeable (so cou-er-ed = covered). The Poinsett work and the first
  version of this reading inferred the marks from use and did not cite this page.

## 3. Reading

`crawford1814_reading.md` gives the coded passages as sentences with the clear words around them;
`crawford1814_decryption.txt` gives every group (`python decode.py`). 283 of the 292 groups read from the table, with
Crawford's marks applied. Nine are supplied from the sense and bracketed in the reading:

| Group(s) | Line | Table | Reading | Why (inference) |
|---|---|---|---|---|
| 1512 (4x) | 64R14, 65R02, 65R07, 66L09 | our | [a] | 1215 = a: the digits written in another order |
| 1276 | 64R12 | fish | [say] (sa-y) | 1275 = y, one higher; the image shows 1276 |
| 556 | 66L09 | late | Rom[e] | 1556 = e, the first digit left out |
| 361 | 66L12 | run | [these] | 561 = these |
| 1474 | 66L15 | cy | [any] | 1472 = any |
| 812 (r-stroke) | 65R02 | june | decis[ive] | dec-is-? ; not settled |

"British troops" (64R06-07) was among the supplied words in the first version (281 of 292, eleven supplied) because
the marks on its two groups were not understood. It is now read from the code: 1244 = tre with a hooked tail under the
last figure, which withdraws the last letter (tr); 1116 = op with a cross under its first figure, which doubles the o,
and a diamond above for the plural (oop-s). See section 7. The cross under 1116 was added to the transcription on
15 Nov (the group number is unchanged). One step in this is inference: by the printed direction a cross under the
first of four figures has no matching letter in a two-letter element, and it is read here as doubling the first letter.

Also: 66L02 "284 95" (that circumstance) is read as written, with [be brought by] supplied, as Crawford's sentence
lacks a verb there (285 951 would be "be brought"); 66L14 556 with one r-stroke is read la[s]t (lat[ter] is possible);
791 speci is read speci[fied]. 65R01 1025 thing is read "Things" (no mark seen).

**What it says (Crawford's report, in his words; none of it is established fact):** he believes the French government
has resolved to sacrifice everything for England's friendship; the King, far from being jealous of British troops in
Belgium, looks to them for protection against his own people; a conspiracy with Savary at its head is reported, which
opponents of the government call a police fabrication to justify about thirty arrests; a crisis is coming that will
decide the fate of the King, and many expect the royal family to be expelled again. If there is a struggle, three
parties: the army for recalling the Emperor; part of the new nobility for the King of Rome with a regency or for the
Duke of Orleans; the genuine republicans joining either of the last two.

## 4. Checks

- **Two blind transcriptions** (`tests/blind_comparison.tsv`). Two readers transcribed the 292 groups from the frames
  without sight of each other's work. They agree on 291 groups; the one difference (66L13, 307 or 317) was settled on
  the image as 307 (ge-nu-in-e, "genuine"). Decoded with the frozen table, the two give the same element for 291 of 292
  groups, and the second reader's reading (frozen before comparison) agrees with the first in every sentence; the
  bracketed words differ only in [a]/our and [these]/run, which both marked as uncertain.
- **Shuffle test** (`tests/shuffle_test_result.txt`), written down before the run: the real table's letter-trigram
  score -0.909 against 200 shuffled tables, mean -1.191, best -1.067, z = 5.7: pass. Re-run independently from the
  frozen inputs with the same result. The first run had a parsing bug (half the table unread); it was repaired and
  run once more, both outputs kept.
- **`docs/_validate.py`** on `validation.tsv` (the nine supplied groups left unread): 283 tokens over 157 types
  (1.8 per type); reading -1.850 against random keys -2.760 (z 6.6) but a key refitted to shuffled text scores the
  same (-1.855), so the verdict is "underdetermined": with so few tokens per type the letter model cannot separate a code
  reading from a fitted key on this text. The shuffle test above, which permutes the printed table rather than fitting
  one, is the test that bears on this reading.
- **Clear words**: "discussions at Vienna" (64R15) was misread by both readers at first and settled on a crop.

## 5. Print and earlier readings (checked 15 Nov 2026)

| Where | What was done | Result |
|---|---|---|
| Founders Online (Madison Papers) | searched Savary, "royal family will again", "King of Rome" with Crawford; Crawford's letters 1812-1815 listed | no hit. Crawford to Madison, 1 Nov 1814 ([Madison/03-08-02-0298](https://founders.archives.gov/documents/Madison/03-08-02-0298)) is clear and does not cover these matters. Crawford to Monroe 5 Nov 1814 is not in Founders. |
| *American State Papers, Foreign Relations* vol. 3 (Library of Congress text) | table of contents read | the France section has nothing on Crawford's despatches of late 1814 |
| Papers of James Monroe, Library of Congress | *Calendar of the Correspondence of James Monroe* (1902) read for Crawford | the Library's Crawford letters from Paris start 16 Dec 1814; none of 5 Nov |
| Crawford papers; Shipp, *Giant Days* (1909) | Shipp's full text searched | no hit (Savary, King of Rome, Orleans in this sense, royal family). The Crawford papers themselves not seen. |
| Mooney, *William H. Crawford* (1974) | search inside (Internet Archive) | no Savary, King of Rome, conspiracy. p. 67 n. 24 cites "Crawford to Monroe ... Nov. 5" on the Decatur; p. 66 says the French situation was explosive, with the Bourbons possibly replaced during the winter (source note not seen). |
| Green, *Life of William Harris Crawford* (1965) | not found online | not checked |
| Willson, *America's Ambassadors to France* (1928) | search inside | no Savary, conspiracy; the first reader found that p. 125 prints only the clear close of this letter |
| Tomokiyo, Cryptiana ("State Department Code: 1797-1866") | read | names Crawford's 1813 use of WE028; nothing on this letter |
| HathiTrust full text | phrases "royal family will again be expelled", "conspiracy is the creature of the police", "sacrifice every thing for the friendship of England", "King of Rome with a regency" | no hit for this letter |
| Google Books | the same phrases | no hit |
| Weber (1979) | text searched | counts about 1,000 coded lines from Crawford in 1814; no decipherment of this letter |
| This repository | targets, catalogue, triage notes | `crawford1813` is the 15 Aug 1813 letter in another code; the NARA triage lists roll 18 frame 0130 only; nothing on frames 0064-0066 |

## 6. History

Crawford, minister to France from 1813, wrote to Madison on 1 Nov 1814 that the American letter of marque *Decatur*
had lain fifty days below Nantes without leave to enter while British vessels came in, and that he meant to keep away
from the court ([Founders, Madison/03-08-02-0298](https://founders.archives.gov/documents/Madison/03-08-02-0298)).
In the clear part of his private letter of 21 Oct (frame 0060L) he had already expected "another civil commotion" in
France within six months. The coded part of this letter gives his private reading of the restored monarchy's weakness.

## 7. Check against Crawford's interlined letters of September 1814

Found on 15 Nov 2026, after the reading above was made and posted. It is therefore a check that happened to be
available afterwards, not a test fixed in advance, and no pass mark was set for it.

On the same roll two earlier private letters of Crawford's carry short coded passages with the State Department
clerk's decipherment written between the lines. `tests/crawford_sept1814_interlined_pairs.tsv` lists the 81 groups with
the clerk's word over each, by frame and line. The decipherment is the clerk's of 1814; reading with it is not an
independent solution, and it is used here only to check the table and the marks.

- **Frames 0031R and 0032L, Paris, 26 Sept 1814, in WE025** (68 groups: "[to expel the reigning family. Carnot ... and
  Barras] are said to be at work and that [an explosion] will certainly take place in the course of the winter [which
  will terminate in the expulsion of the Bourbons] ... to [bring them to the gallows for their past conduct]"). 66 of
  the 68 groups give the clerk's word from the table as we had transcribed it. The two that do not:
  - **1181.** The clerk's "explosion" (1168 1181 1573 765, ex-?-os-ion) needs "pl". Our transcription of Weber's table
    had "Pi". Weber's printed page (p. 451) has **1181 pl**: the error was in our machine-read copy, not in the code.
    1181 does not occur in the letter of 5 Nov, so `key/we025_crawford1814.tsv` (the 156 rows used here) has no such
    row and is unchanged, and `decode.py` gives the same elements as before. Against the printed table the agreement
    is 67 of 68.
  - **A group ending in 70** under the clerk's "Carnot" (with 1412 = not). Its first figure is written over and
    blotted: 570 = car fits, 870 = design does not, and the film does not show which stands.
- **Frame 0025R, mid-September 1814, in WE028** (a private letter on frames 0022-0028; the docket beside it reads
  10 or 16 Sept, and its first page was not opened for the date; 13 groups: "the discord which prevails [in the cabinet], especially
  between [yourself and the Secretary at war]"). All 13 agree with WE028, the code of `../crawford1813`. If the
  docket date is right, Crawford was still using the older code in mid-September and WE025 by the 26th.
- **The marks, as the clerk read them.** On 0031R the group 1359 = ult has a hooked tail under its last figure and
  the clerk reads 1298 1359 652 (exp-ult-sion) as "expulsion": the tail withdraws the last letter. On 0032L a small
  diamond stands over 1236 = it under the clerk's "its", and by 771 = low under "gallows" (176 771): the diamond adds
  s. Both agree with the code's printed directions (section 2).
- **The same marks on frame 0064R of this letter.** 1244 (line 6) has the same hooked tail under its last figure;
  1116 (line 7) has a diamond over its last figure and a small cross under its first; the next group, 783, has a
  diamond (others). Hence tr-oop-s, "British troops and others in British pay". The cross is not attested by the clerk
  in September; it rests on the printed directions and on its two other uses in this letter.
- **A slip of one number, attested.** On 0031R Crawford wrote 1480 248 1252 (tal-eck-en) in the list of names and the
  clerk copied it out literally as "Taleck en". The man meant is presumably Tallien (an inference; nothing on the page
  says so), which needs 249 = li, the next number. This is the kind of slip supposed for 1276 (for 1275) and 1474 (for
  1472) in section 3, and it shows that the clerk did not repair such slips.
- **What the check does not reach.** Neither 1512 nor 1215 occurs in the September passages, so the four groups
  written 1512 are no better explained; nothing bears on 812. No pair contradicts any of the nine supplied groups.

What was seen and by whom: the 81 pairs were transcribed from the film on 15 Nov 2026 by an AI agent with the clerk's
words in view. A second AI agent then looked at Weber's pages 451 and 454, at lines 1 and 6 to 9 of frame 0064R, at
lines 3, 4 and 6 of 0031R, lines 3 and 4 of 0032L and the two lines of 0025R, and saw the numbers, glosses and marks
described above; it did not re-read the other lines. No person has checked any of it.

## Remaining gaps

- The nine supplied groups (section 3). Blocker: none outside; the slips are inferred from the sense (one slip of
  the same kind is attested in September, section 7); the four groups written 1512 and 812 are not settled.
- A period decipherment or clear copy: the clerk's fair copy (last page on 0067R), the Crawford papers (Library of
  Congress), the Monroe papers (New York Public Library) and Green (1965) not seen. Blocker: needs access.

## Escalation

- Siblings: done on 15 Nov 2026 (section 7): frames 0025, 0031 and 0032 of the same roll, 81 groups with the clerk's
  decipherment. Not done: Crawford's other WE025 letters on this roll.
- Print: the sources in section 5 checked; Green (1965) and the Crawford papers remain.
- Retry: the 16 Dec 1814 private letter (roll 18 frames 0129-0131, same code) has a period decipherment on the
  Library of Congress duplicate (Monroe Papers reel 5, images 938-941) and can test Crawford's slips; not done here.
