# William H. Crawford to James Monroe, Paris, 5 Nov 1814 ("Despatch No 33-2, Private"): a coded letter in WE025

Contributed by Andrew Beling, with AI agents, 15 November 2026. Status: read, with eleven groups supplied from the
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
full as WE025 (pp. 470-480): 1355 = the, 1397 = of, 1554 = to. It is the code of Poinsett's letters
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

## 3. Reading

`crawford1814_reading.md` gives the coded passages as sentences with the clear words around them;
`crawford1814_decryption.txt` gives every group (`python decode.py`). 281 of the 292 groups read straight from the
table. Eleven are supplied from the sense and bracketed in the reading:

| Group(s) | Line | Table | Reading | Why (inference) |
|---|---|---|---|---|
| 1512 (4x) | 64R14, 65R02, 65R07, 66L09 | our | [a] | 1215 = a: the digits written in another order |
| 1276 | 64R12 | fish | [say] (sa-y) | 1275 = y, one higher; the image shows 1276 |
| 556 | 66L09 | late | Rom[e] | 1556 = e, the first digit left out |
| 361 | 66L12 | run | [these] | 561 = these |
| 1474 | 66L15 | cy | [any] | 1472 = any |
| 812 (r-stroke) | 65R02 | june | decis[ive] | dec-is-? ; not settled |
| 1244, 1116 (marked) | 64R06-07 | tre, op | [troops] | British [troops] and others in British pay; the marks are not understood |

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
- **`docs/_validate.py`** on `validation.tsv` (the eleven supplied groups left unread): 281 tokens over 155 types
  (1.8 per type); reading -1.845 against random keys -2.748 (z 6.3) but a key refitted to shuffled text scores the
  same, so the verdict is "underdetermined": with so few tokens per type the letter model cannot separate a code
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

## Remaining gaps

- The eleven supplied groups (section 3); the meaning of the y-tail under 1244. Blocker: none outside; the slips are
  inferred from the sense, and 812 and the [troops] pair are not settled.
- A period decipherment or clear copy: the clerk's fair copy (last page on 0067R), the Crawford papers (Library of
  Congress), the Monroe papers (New York Public Library) and Green (1965) not seen. Blocker: needs access.

## Escalation

- Siblings: frame 0031 of the same roll carries a short WE025 passage of September 1814 with an interlinear
  decipherment, a check of the table on Crawford's own use; not done.
- Print: the sources in section 5 checked; Green (1965) and the Crawford papers remain.
- Retry: the 16 Dec 1814 private letter (roll 18 frames 0129-0131, same code) has a period decipherment on the
  Library of Congress duplicate (Monroe Papers reel 5, images 938-941) and can test Crawford's slips; not done here.
