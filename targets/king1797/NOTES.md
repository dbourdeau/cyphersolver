# Rufus King (London) to the Secretary of State, 1797-1803: King's State Department code (the = 769) rebuilt from the Department's interlinear decipherments; No. 29 of 13 April 1797 read in part

Status: written up 11 Nov 2026 (`docs/king1797.html`). Contributed by Andrew Beling, with AI agents (pull request #398, 11 Nov 2026);
checked on integration the same day (section "Integration check" below). The key is partial: 764 of about 1,600
groups. It was tested once, on a held-out despatch, before any value was added from clear texts. Of the one coded passage with no
decipherment on the film and no text found in print (No. 29, on Sweden), every sentence reads, and 10 words rest on context alone.

Related: [`../king1801`](../king1801/NOTES.md) (King's despatches of 25 Apr and 8 Jun 1801, closed 26 Oct 2026 as already
in print). This target identifies and rebuilds the code that king1801 records as "not identified or rebuilt". The coded
duplicates king1801 could not see are on M30 roll 7, not roll 9 (see "For king1801" below). The two targets are kept apart
because their documents and methods differ: king1801 is a text read from the 1896 print, and this one is a key recovered from
adjacent plaintext plus a passage that has no print.

## 1. The documents

| Document | Frames (NARA M30) | Role here | State |
|---|---|---|---|
| No. 29, London, 13 Apr 1797 | roll 4, 0092 R (code); 0093-0096 clear | **read here**: the coded paragraph on Sweden (119 groups on 13 lines, mixed with clear) | read in part |
| No. 59, London, 23 Dec 1797 | roll 4, 0272 R, 0273 L (code); 0273 R (Department's clear text, "No. 59. Trip.") | **held-out test** of the key; text known from the clerk's clear copy | decoded, not read (test document) |
| No. 30, 19 Apr 1797, triplicate | roll 4, 0117 R, 0118 R | check against print (C. R. King, *Life* 2:172-75), not declared in advance | not claimed |
| No. 14, 25 Apr 1801, duplicate | roll 7, 0142 R | check against print (*Life* 3:436-38); it is king1801's first document | not claimed |
| No. 21, c. 8 Jun 1801, a run of 12 groups | roll 7, 0162 R | check against print (*Life* 3:472-73); king1801's second document | not claimed |
| 72 interlined frames, 1797-1803 | rolls 4-8 | source of the key (`corpus/interlined_spans.tsv`) | not read as texts |

**No. 29.** The despatch is a clerk's copy received by the Department of State, with "No. 29." and "London Apr. 13th 1797." in
clear. After a clear opening, King writes in code about Sweden. His words: the late regency; the Duke Regent's partiality for
France; the King since his majority; French influence less at Stockholm; the answer the President instructed him to give to
the Swedish government's overtures; the President's decision "for the present to decline the overture". The despatch then turns
in clear to the Maryland Bank Stock, Captain Home, and seamen, and runs in clear to King's signature on frame 0096; the whole
despatch is transcribed in `reading_no29.md` (frames 0094-0104 were checked: no further code). The left page of
0092 carries the docket of No. 28. Nothing is written over the code groups. No separate decipherment was found on 0092-0096.
The frame survey found none for No. 29 elsewhere on the film. Reading and context: `reading_no29.md`.

## 2. Sources and images

NARA RG 59, Despatches from U.S. Ministers to Great Britain, microfilm M30. The rolls used are roll 4 (vol. 5, 10 Aug 1796 - 28 Dec
1797, NAID 188512917), roll 5 (vol. 7, 1798, NAID 188513207), roll 6 (vol. 8, 1799-1800, NAID 188513469), roll 7 (vol. 9,
1801, NAID 188513785) and roll 8 (vol. 10, 1802-03, NAID 188514061). Frame images are public on the NARA catalogue:

    https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M30/M30-00N/M30-00N-FFFF.jpg   (N = roll, FFFF = frame)

for example [No. 29](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M30/M30-004/M30-004-0092.jpg). A frame that
does not exist still returns HTTP 200 with an HTML body. Each frame is a two-page opening (L, R). No images are in this folder.
106 frames were downloaded for the work (628 MB). The NARA OCR text of rolls 4-8 was used only to find frames with runs of code
groups (170 frames with three or more).

## 3. The system

A one-part numerical code: groups 1-1599 written with full stops between them. One plain 1600 was read ("according"), and
nothing above 1600 was read with confidence. The size of the range fits a printed 1600-number form. Whole words, syllables and
single letters each have a number. Words are built from several groups (pre-par-ed, S-wed-ish, St-…-m). A caret after a group
marks a plural or inflection, and a small v or + allows a suffix. The commonest groups are 769 the, 644 to, 1410 of, 321 in,
710 and, 147 that, 107 I, 10 a and 29 s. The code is used for chosen passages inside clear despatches, and now and then for a
whole despatch (No. 59).

The same code runs from King's first coded despatch (14 Jan 1797) to his last (No. 89, 2 Apr 1803). For example, "Mr Addington"
is 128.1234.712.694.678 in No. 58 (13 Mar 1802), in No. 89 and in the June 1801 run. This agrees with Weber's statement that King
"continued to use the same code he began with in January 1797" (Weber 1979, p. 153). It is **not** the 663 code ("the" = 663)
that King sent Livingston in January 1802. 663, 1518, 1490 and 1513 are rare or absent in King's despatches, and no value is
shared with that code's key.

The elements fit the printed 1600-element word list behind Weber's WE023-WE028: 382 of the 411 single-group values read directly
from the clerks are on it. But the numbering is none of Weber's nine 1600/1700 tables. 40 values from frame 004-0249 were tested
against WE016, WE018 and WE022-WE028 and against constant offsets, and none matched. So this is a further code on the same
printed form, and Weber does not print its sheet. That the code is built on this list is the working assumption of the frame
solver. It is consistent with the evidence but not confirmed by any outside source (Prior work).

## 4. The key (`key.tsv`, `key_method.md`)

The key comes from the Department's own interlinear decipherments. Seven AI agents transcribed 72 interlined frames of rolls 4-8
from the images, with no key in view: 13,603 groups, of which 6,535 were usable as word-to-group equations. The usable set
excludes rows with an ambiguous placement, a doubtful digit or no word above.

| grade | groups | how |
|---|---|---|
| D | 405 | one group under one word, majority reading |
| S1 / S2 | 129 / 183 | the only element of the printed list that fits every multi-group word the group occurs in (frame solver) |
| A | 24 | aligned to clear text after the test (No. 59 clear copy; King's print of No. 30 and the 1801 items); calibrated 92 of 94 right |
| R | 15 | read on 11 Nov 2026 from the clerks' multi-group words while reading No. 29, every occurrence listed. Six correct D values, as below |
| I | 8 | from No. 29's context only, doubtful |

`scripts/king_code.py` rebuilds `build/key_v1.tsv` (the tested key) and `build/key_v2.tsv` byte for byte from the corpus,
given Weber's list. The list is not repeated here: it is in the Code 16 folder, `../pinckney1793/beling/key/weber_1600_family_vocab.txt`
(pass it as `--elements`). With the WE028 sheet already in this repository instead (`../morris1813/beling/key/`), 715 of the
723 v1 values come out the same.

**Conflicts.** 107 groups have two different words written over them as single groups on different pages
(`build/key_v1_conflicts.tsv`). The majority value was taken and ties left out. The `source` column of `key.tsv` names every
minority reading. Reading No. 29 exposed a systematic error in the D grade. When a clerk wrote a whole word over the first group
of a word and left the rest bare, the D value took the whole word. 1097 "prepared" is pre, 926 "mer" is er, 246 "prove" is pro,
1338 "change" is dec, and 287 "line" is li. 128 "Mr" is the letter m: the clerks expanded King's "M." to Mr, and the group is m
inside words, as in Mr. Fox = m-r-f-o-x in No. 30. Those six are corrected. 550 "case" (probably ca) is suspected and was not
corrected. Others of the kind may remain.

## 5. The declared test (`test_no59/`)

The test was written at 2026-11-10 19:43 -0500, before any transcription batch came back (`test_no59/PREREGISTRATION.md`). It
used No. 59 of 23 Dec 1797: wholly in bare code, 297 groups, transcribed without a key and in no batch. The truth was the
Department's clear text on 0273. The key was hashed before scoring (sha256 `6a9a1d8c...9f064`, 723 groups). The measure is the
share of covered groups whose values fall in order on the clear text, under a 12 x (k+1) letter gap rule. The pass rule was
score >= 0.85 and margin over the best of 200 shuffled keys >= 0.30. There was one run.

**Result: 0.946** (212 of 224 covered groups; coverage 0.742). Shuffled keys gave a mean of 0.108 and a best of 0.165.
**Pass.** The decode of the frozen key opens "this ca bi[net] last [night] after … consider ation ga[ve] a [de] ci ded
[negative] to a propos al [of] peace made by the di rec[tory]". The clear text reads "This Cabinet last night after several days
consideration, gave a decided negative to a proposal of peace made by the Directory". (`test_no59/no59_decryption.txt`, line
by line.)

## 6. Checks against print (not declared in advance)

The key frozen for the test (v1) was applied to three bare items transcribed blind on 11 Nov 2026 (`checks/bare_items.tsv`,
`checks/checks_decode_keyv1.txt`). The truth was C. R. King, *The Life and Correspondence of Rufus King* (1894-1900), printed
from King's press copies with the coded words in italics. The italic runs are in `checks/print_italics.tsv`.
`scripts/check_against_print.py` (standard library, fixed seed) writes `checks/check_against_print.json` and the
group-by-group alignment `checks/check_against_print_alignment.tsv`.

The measure. Every code group of the item, in manuscript order, is laid in order on the letters of the print's italic runs. A
group agrees when it takes exactly its key value (after a marked group a suffix such as s or ed may follow). A group that does not
agree, or has no value, may take 0 to 14 letters. The alignment with the most agreeing groups is taken, and the score is
agreeing groups over covered groups. As a control, the key's values were permuted over its groups 1,000 times.

| Item | Groups | Covered | Agree | Score | Permuted keys: mean / best |
|---|---|---|---|---|---|
| No. 30, 19 Apr 1797 (triplicate) | 286 | 227 (0.794) | 201 | 0.885 | 0.094 / 0.181 |
| No. 14, 25 Apr 1801 (duplicate) | 124 | 100 (0.806) | 85 | 0.85 | 0.083 / 0.21 |
| No. 21, c. 8 Jun 1801 | 12 | 9 (0.75) | 9 | 1.0: "Lord Hawkesbury and Mr Addington" | 0.043 / 0.222 |

No permuted key reached the key's score on any item.

Earlier figures. This section first gave 0.833, 0.81 and 9 of 9 (permuted best 0.348, 0.42, 0.556) from a script that was not
kept. They are reproduced exactly (189 of 227, 81 of 100, 9 of 9) by the held-out test's scorer run on each run of code groups
between clear words separately, with the whole saved print file as truth: heading, notes and roman text included. Each run could
then start anywhere in the letter, so permuted keys averaged 0.27-0.30. The figures above replace them.

Caveats. These checks were not declared in advance. The prints come from King's press copies, not from the copy the Department
received, and the No. 30 triplicate is faint (8 groups with an unreadable digit). Where the copy has a word in clear that the
print italicises, or codes words the print has in roman ("the Ministry have been" in No. 30), the neighbouring groups count as
not agreeing. `print_pairs.json`, made for the v2 alignment, pairs the 1801 runs with the wrong parts of the print (for No. 14 the
roman text, for No. 21 the letter without its italic words). The three grade-A values touched (561 y, 1152 de, 534 bury) also
occur in the No. 59 pair, and with key.tsv they agree with the italics in the new alignment. None of them is used in No. 29. In the 1801 decode (with the later
key.tsv values 29 = s and 561 = y), the king-s rec-over-y has not been … de-li-r… sub-side … rel-ap-se … de-bi-li-ty … the k-ing-s … la-dy correspond to the print's
"the King's recovery … delirium having subsided … a relapse … extreme debility … the King's malady".

## 7. Reading of No. 29 (`reading_no29.md`, `no29_decryption.txt`)

The coded paragraph reads as English sentences. 119 groups (82 distinct). 108 have a value from the clerks' decipherments, the
print checks or the alignments, and 107 of those fit. 11 tokens rest on eight grade-I values: indulged (717), predilection (389),
majority (1279), Stockholm twice (1074, 1490), Swedish twice (507), esteem (1440) and "the" (269, a slip or a second number). The
group 769 (the) stands where "and" is needed (line 15), and an encoder's slip is supposed. Read share over the page's reading
(clear and decoded words, the project's rule, `research/reading_audit/v10_relabel.py`) is **0.994** over the whole despatch,
now transcribed to frame 0096; on the decoded words alone it is 0.855 (65 of 76). The document is marked **read in part**
because the coded part on its own is under the bar. Andrew Beling read it as sentences against frame 0092 on 11 Nov 2026 and
signed it off, including the context-only words (`reading_review`).

In the reading, King reports that under the late regency Swedish policy favoured France. That was the guardianship of Duke Karl,
which ended when Gustav IV Adolf took over the government on 1 Nov 1796 (*Svenskt biografiskt lexikon*, "Gustav IV Adolf",
sok.riksarkivet.se/sbl/artikel/13318). The young King is more national
in outlook, and French influence at Stockholm is less. King expects the President's answer to the Swedish overtures, which declines
them "for the present", to be well received there. He has tried to show American esteem for Sweden while explaining the
President's motives. Pickering names the overture himself (to John Adams, 24 Sept 1798, Founders Online, Adams Papers
99-02-02-3023). It was the "propositions made by the Swedish minister, Baron d'Engerstrom ... to Mr. Pinckney", answered by
Pickering's letter to King of 17 Sept 1796 and by "Mr. King's communications on the subject, extracted from his letters of April
13th 1797, & June 5th following". Engeström's note of 1794 invited the United States to accede to the Danish-Swedish neutrality
convention of 27 March 1794 (*Papers of Alexander Hamilton* 16:548-50, notes; Pickering dates the propositions "1793"). Pickering's
instruction of 17 Sept 1796 was not read.

## 8. Prior work

- **The key.** None found. Weber (1979) gives no table for King's despatch code and none of his tables has the = 769. Tomokiyo's
  Cryptiana (all 293 pages linked from its code index, searched 10-11 Nov 2026) never has 769 = the. The Madison Papers editors print "key not found" for King's 1801-03
  despatches. `../king1801` (26 Oct 2026) says the code "was not identified or rebuilt". DECODE has no King record. Searches
  of this repository (catalogue.json, research/leads.json, issues and pull requests, 11 Nov 2026) found no entry for King's code
  or for No. 29. The only King item is catalogue 649, a French code he enclosed.
- **The texts.** Most of King's coded despatches are printed in his *Life and Correspondence*, vols. 2-4, deciphered from his
  press copies ("Italics in cipher"). So the key is new but most of the plaintext is not. **No. 29 was not found in print.** It is
  not in *Life* vol. 2, whose sequence runs from the 2 Apr 1797 letter to Hamilton to No. 30 of 19 Apr, with no letter of 13 Apr.
  It is not in American State Papers, Foreign Relations 1-2, and not on Founders Online. Not checked: the Pickering Papers at the
  Massachusetts Historical Society and their printed index, the Rufus King Papers at the New-York Historical Society (King's
  letterbooks, which would hold his own clear copy), and the Adams Papers (see 9).
- What may be claimed: a first published key of King's 769 code, tested on a held-out despatch, and a reading of No. 29's coded
  paragraph, which was not found in print. What may not be claimed: that King's despatches in general are newly read, or that
  No. 29 is unpublished. Say "not found in print".

## 9. The Weber WE025 attribution conflict

Weber (p. 143) lists among the early uses of WE025 (1592 elements, Adams Papers) "King to Pickering, 13 Apr 1797", citing Adams
Papers reel 392. The Department's copy of King's No. 29 of that date is in the 769 code, not WE025. 769 is its commonest group,
and it shares 762.409 (government) and other groups with the interlined pages. Either Weber's letter is a different one of the
same date, perhaps a copy King sent by way of John Quincy Adams, or the attribution is wrong. The Adams Papers copy was not seen.
If it is a copy of No. 29 in another code, or carries a decipherment, it would check this reading. It is the first item to look
for (Remaining gaps). One explanation fits: on 24 Sept 1798 Pickering sent John Adams extracts of King's letter of 13 Apr 1797
and said he would send copies to John Quincy Adams at Berlin, "putting some parts of them in cypher" (Founders Online, Adams
Papers 99-02-02-3023). Such a copy would be in a code Pickering shared with the Adamses, not in King's code. Not checked.

## For king1801 (proposed change, not made here)

king1801's NOTES and profile are left unchanged. Suggested changes for the maintainer:
- "NARA M30 roll 9 is not online": Despatches vol. 9 (1801) is **M30 roll 7** (NAID 188513785), and it is online. The duplicate
  of 25 Apr 1801 is frame 007-0142 R, with 124 groups in 16 lines among clear. The 8 Jun 1801 run is frame 007-0162 R, lines 2-3,
  12 groups. Roll 9 is vol. 12 (Monroe, 1803-07).
- "the code was not identified or rebuilt": it is King's 769 code. The code groups of both duplicates are now transcribed
  (`../king1797/checks/bare_items.tsv`) and decode with the key in `../king1797` in agreement with the print (section 6).
- The two remaining gaps (code groups; key) and the archive request seeded from them ("the code groups of both duplicates (NARA
  RG 59 M30 roll 9)", blocker needs-physical-access) can be closed with a pointer to `../king1797`.
- The Madison Papers abstract of No. 21 says "Swedes and Danes" where King's print and the coded run have "Lord Hawkesbury and
  Mr Addington". That suggests the editors did not have the coded words read.

## Integration check (11 Nov 2026)

Done by the project when pull request #398 was integrated. Nothing in the key, the transcriptions or the reading was changed.

- **Rebuild.** `scripts/king_code.py build` with Weber's union list gives `build/key_v1.tsv` byte for byte (723 groups, sha256
  `6a9a1d8c...9f064`, the hash recorded for the test); `score` gives `test_no59/heldout_result.json` exactly (212 of 224 covered
  groups, 0.946, coverage 0.742, shuffled mean 0.108 and best 0.165, pass); `align` gives `build/key_v2.tsv` byte for byte (747
  groups, calibration 92 of 94). With the WE028 sheet of `../morris1813/beling/key/` instead: 736 groups, 0.948 at coverage 0.772,
  as section 4 says. `scripts/check_against_print.py` rewrites `checks/check_against_print.json` and the alignment table byte for
  byte (201 of 227, 85 of 100, 9 of 9). `decode --key key.tsv no29_transcription.txt` gives the D lines of `no29_decryption.txt`.
- **The Weber list is not in this folder.** `../pinckney1793/beling/key/weber_1600_family_vocab.txt` arrives with pull request #399
  (Code No. 16); until that is merged the byte-for-byte rebuild needs that file from the pull request. The check above used it.
- **Was the key frozen before the test?** What can be checked: the v1 build reads only `corpus/interlined_spans.tsv` and the element
  list, never `test_no59/`; frames 0272 and 0273 are not among the 72 corpus frames; no run of four consecutive groups of No. 59
  recurs in the corpus more than three times on any frame (common phrases only), so no other copy of No. 59 is in the corpus; the
  same holds for No. 29, No. 30 and the 25 Apr 1801 duplicate (the 8 Jun 1801 run is two ministers' names, which recur). What
  cannot be checked from the repository: the time of the declaration (`test_no59/PREREGISTRATION.md`, 10 Nov 2026 19:43 -0500) and
  that there was one run. The folder arrived in a single commit of 11 Nov 2026 02:46 -0500, so these rest on the contributor's statement.
- **Counts.** `no29_transcription.txt`: 119 code groups, 82 distinct. By key grade: 69 D, 18 S (15 S2, 3 S1), 2 A, 19 R, 11 I.
  The frozen key v1 covers 94 of the 119, and 87 of those have the value they have in `key.tsv` (the other 7 are the corrected D
  values). No. 59: 297 groups plus five dashes on the code lines (302 tokens in the score).
- **Second reading of frame 0092.** The frame was fetched from the NARA catalogue and all 119 groups of lines 7-21 were read again
  on crops at full resolution, with the transcription in view (so not blind). Every group stands as transcribed, including 1051
  (twice), 269 (line 14) and 769 (line 15). The marks stand too: the caret after 1556, 529 and 709, the small v after 1494 and 406.
- **Retry of the open values.** Each of the eight grade-I groups (717, 389, 1279, 1074, 1490, 507, 1440, 269) was searched in
  the 13,603 groups of the corpus, in No. 59 and in the bare items. None occurs under a clerk's word. 1074 occurs once more, in the
  faint No. 30 triplicate (0118 R11), where the print has "immediate" and 1075 = im is likely meant (already noted in `key.tsv`).
  So nothing in the folder confirms or refutes them, and they stay doubtful.
- **One key, one entry.** `key.tsv` was compared number by number with the other United States code tables here: Codes No. 10 and
  No. 16 (`../legation1788/key.tsv` and, since the split of 11 Nov 2026, `../pinckney1793/key.tsv`; 83 and 128 numbers in common, no value the same), the WE028 sheet of `../morris1813` in both block
  orders (757 and 752 in common, none the same, no constant offset), and the commonest groups of the others (the = 972 Armstrong,
  1385 `../jqa`, 1651 Pinckney, 536 `../murray1801`, 798 Sumter). It is a different code from all of them. The two despatches of
  `../king1801` are in this code; that folder is closed with no page (texts already in print) and now points here.
- **The reading** was read as sentences against `no29_decryption.txt` and the frame: it holds as English throughout, with the ten
  marked words and the supplied letter as its only holes.
- **Gaps list.** The four items the contributor marked "not attempted" were sorted: the second reading of the digits was done
  (above); the others are not unread pieces of No. 29 and moved to "Further work".

## Remaining gaps

- No. 29: the eight grade-I values (717, 389, 1279, 1074, 1490, 507, 1440, 269), behind nine words, and the 769 written where "and" is needed (ten marked words in all) - blocker: open-codes; none occurs under a clerk's word in the 72 transcribed frames, No. 59 or the print checks (retry, 11 Nov 2026); a clear copy (King's letterbook at N-YHS, the Pickering Papers) or an occurrence in the coded frames not yet transcribed would settle them
- Adams Papers reel 392, King to Pickering 13 Apr 1797 (Weber's WE025 attribution) - blocker: needs-physical-access; MHS microfilm, would show whether it is a copy of No. 29

## Further work (not gaps in the reading of No. 29)

- The key: about 830 of 1,600 groups have no value. D values may still carry the error of section 4 (550 suspected). 48 OCR code
  frames on rolls 5-6 and about eight small coded items on roll 6 were not opened. `outcome.key` is "partial" for this reason.
- Pickering's instruction to King of 17 Sept 1796 on Engeström's propositions (the overture is identified, section 7) and King's
  letter of 5 June 1797 were not read: NARA RG 59 M77 roll 1 (instructions) and M30 roll 4.
- No blind second transcription of frame 0092 and no human palaeographic check of any transcription. The integration reading
  above had the transcription in view.

## Escalation

- [x] siblings: the 48 interlined despatch copies on rolls 4-8 are the key source (72 frames transcribed)
- [x] clear-pages: No. 59's clear triplicate is used as the test truth; No. 29 has no clear copy on 0092-0104; its clear pages (0093-0096) are transcribed in `reading_no29.md`
- [x] print: King, *Life* vols. 2-3 (No. 30, 1801 items) used as checks; No. 29 not found in *Life* 2, ASP FR 1-2 or Founders Online
- [x] key-rebuild: done (key.tsv), tested once on a held-out despatch
- [x] known-keys: Weber's nine 1600/1700 tables tested on 40 values from 004-0249, none fits (not this code); on integration, Codes 10 and 16 and the WE028 sheet compared number by number, no value shared
- [x] retry: 11 Nov 2026, on integration: the eight context-only groups searched in the corpus, No. 59 and the bare items (no occurrence under a clear word); frame 0092 read a second time against the transcription (all 119 groups stand)

## Method and tools

The work was done by AI agents (Claude Fable 5.2, with Claude Opus 5.5 subagents), run by Andrew Beling, on 10-11 Nov 2026.
Agents surveyed the film through the NARA OCR, downloaded and classed 106 frames, and transcribed 72 interlined frames without a key.
They declared the test before the batches came back, built and tested the key, transcribed the bare items blind, aligned clear
texts, read No. 29 and checked the prior art. Images were cropped with `sips`. Scripts: `scripts/king_code.py` (build, score,
align, decode) and `scripts/check_against_print.py` (section 6), both standard-library Python 3. Batch notes: `corpus/batch_notes/` (batch 1 kept no notes). Mixed line-numbering
conventions: some batches count only code lines, others every line; the `note` column gives the physical line where it matters.

## Files

- `key.tsv`, `key_method.md`: the key and how it was built
- `no29_transcription.txt`, `no29_decryption.txt`, `reading_no29.md`: No. 29
- `test_no59/`: the declaration (`PREREGISTRATION.md`), transcription (`no59_transcription.tsv`), the Department's clear text
  (`no59_department_clear.txt`), decryption (`no59_decryption.txt`) and result (`heldout_result.json`)
- `checks/`: blind transcription of No. 29, No. 30 and the 1801 items (`bare_items.tsv`), their decode with key v1, the
  print's italic runs (`print_italics.tsv`), the print-check figures and alignment (`check_against_print.json`,
  `check_against_print_alignment.tsv`), and the clear-text pairs used for the v2 alignment (`print_pairs.json`)
- `corpus/interlined_spans.tsv`, `corpus/batch_notes/`: the 72-frame interlined corpus
- `build/`: key v1 (tested) and v2 as the script writes them, with summaries and the conflict list
- `scripts/king_code.py`, `scripts/check_against_print.py`; `CHECKS.txt` (checker output)
- `viewer/`: a static page (open `viewer/index.html`) showing frames 0092-0096, loaded from the National Archives catalog,
  beside the reading of No. 29, with each code group and its value; `viewer/reveal_king1797.json` is a draft for the site's
  "watch it decipher" widget, offered for the write-up
