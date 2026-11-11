# legation1788 — residual groups in Jefferson's legation codes Nos. 10, 13 and 16 (Short 1792, Carmichael 1788, T. Pinckney 1793)

Catalogue no. 484 (Founders Online sweep, `research/founders_emlo/`). Worked 26-27 Oct 2026 from the solve-page brief.
Sibling target: `jefferson1787` (Code No. 11, catalogue 483).

## What it is

Three letters to Thomas Jefferson as Secretary of State (or minister in Paris), each partly in a numerical code, each
printed in *The Papers of Thomas Jefferson* with a few groups left unread or read by conjecture:

| Letter | Code | Original | What was open |
|---|---|---|---|
| William Short → TJ, The Hague, 26 Jul 1792 ("Private") | No. 10 | LoC Jefferson Papers ser. 1, mtj1 016_0998-1009 (RC, TJ interlinear); extract re-enciphered in Short → TJ 27 Jul 1792, 016_1010-1012 | 401, 1083, 401 (note 21); 359, 199, 34, 724 (note 23) |
| William Carmichael → TJ, Madrid, 14 Apr 1788 | No. 13 (the code David Franks left with him, Nov 1786) | LoC mtj1 009_0223-0230 | five groups read by conjecture: [Maryland] x2, [Massachusetts], [majority], [you?] |
| Thomas Pinckney → TJ, London, 28 Aug 1793 | No. 16 | NARA RG 59, Despatches from US Ministers to Great Britain, M30 roll 2 frame 0140 | three sentences "deciphered in part"; "Undeciphered code 497"; [time?], [secret?], [Dunda]s |

The codes are two-part numerical codes of about 1,700-1,850 groups (words, syllables, letters), groups separated by
dots, numbers in no alphabetical order (checked for No. 10 on 016_1007-1008: 7 s, 12 pleny, 68 president, 153 al, 218 my,
224 the, 294 I, 426 to ... no run is ordered), so a group cannot be bracketed between its neighbours.

## Sources and files

- `transcription/short_17920726.tsv`: the open groups of Short's letter and their neighbours, both copies.
- `transcription/short_17920726_full.tsv`: every code group of the 26 Jul letter with TJ's interlinear (subagent).
- `transcription/code10_hunt.tsv`, `code10_checked.md`: the search of the other Code No. 10 letters for the six groups.
- `transcription/carmichael_17880414.tsv`: Carmichael's five code items.
- `transcription/pinckney_m30.tsv`, `pinckney_m30_frames.md`: every code group on M30 roll 2 frames 0101-0330 (15 coded
  frames, ~2,660 rows), with the interlinear decodings of 20 Jun, 25 Sep, 27 Nov, 17 Dec 1793, 28 Jan and Feb 1794 and
  the "Explication of the Cyphers" (0179) aligned to 25 Nov 1793.
- `reading_pinckney_17930828.tsv`: the 28 Aug 1793 passage group by group, graded against the attested values.
- `key.tsv` (`make_key.py`): values decoded at the time, per code. `make_profile.py` → `profile.json`, `ct/`, `texts/`.
- `dl_m30.py`: downloads M30 roll 2 frames from the NARA catalog media server (images git-ignored).

## Findings

### Pinckney, 28 Aug 1793 (Code No. 16)

The coded passage is on M30 roll 2 frame 0140 (right page; TJ's pencil "copy so far only" above it), 58 groups in five
lines; the leading digits of lines 2-5 are lost in the binding gutter. Values from Pinckney's decoded letters on the
same roll confirm the editors' frame word by word: 753 = i (reg-i-ments), 1490 1517 = to be, 709 = with, 323+ =
general-s, 856 = and, 800 = s, 513 525 = under him, 1228 ... 1181 = des-tin-ation, 885 = is, 323 675 175 = general-ly
thought, 1226 = for. On 27 Oct 2026, of 58 groups, 30 carried a value attested in another Pinckney letter (H), 23
rested on the editors' reading (E), 4 were the editors' bracketed conjectures (C) and 1 was open. Since 11 Nov 2026
(the other letters of the code, below): H 39, E 17, C 0, O 2 (447 and ?55).

- **The open group is 447, not 497.** The image shows two matching open 4s (same form as the 4 of 1465 on the page).
  447 occurs nowhere else in the 15 coded Pinckney frames. Context: "447 regiments are to embark in a short [time] on a
  [secret] expedition"; a number or "several" is expected, but the code's number words seen elsewhere are 1244 = 6,
  531 = 8, 383 or 6?4 = nine, 1491 = six (approximate); none is 447.
- 234 [time?] and 501 [secret?] also occur only here among Pinckney's letters on M30 roll 2 (for the other letters of the code, see the next point).
- The 15 Aug 1793 letter (frames 0135-0136, ~1,020 groups, no interlinear) has an en clair State Department copy
  (Bankson's Tr, printed in PTJ 26), so it is not open; it does not contain 447, 234 or 501.
- **Other letters in the same code (contributed by Andrew Beling, Nov 2026; [`beling/`](beling/README.md)).** Code No. 16
  is the code Weber (1979, p. 155) calls the "663" code; it was also used by Pinckney from Madrid and Paris in 1795, by
  William Eaton at Tunis in 1801-02 and by Tobias Lear in 1813. Read in those letters: 234 = time (Lear 1813, twice;
  Tunis 1802), 501 = secret (Lear 1813), "Sir" = 1328 1374 (si-r), so Charles is 672 alone; 668 = at (Eaton 1801,
  Pinckney 1795, Tunis), which does not spell [Dunda]s; 675 = ly; 1010 = tin (des-tin-ation). 447 is in none of them.
  The grades in `reading_pinckney_17930828.tsv` follow that (H 39, E 17, C 0, O 2: 447 and ?55). The bundle also has a
  537-group key, the held-out tests and a decode of Pinckney's undecoded frames on M30 roll 2 (decoded, not read).

### Short, 26 Jul 1792 (Code No. 10)

- The passage: "if I had not counted enough on the justice of government to have **401** sure. There **1083** have
  **401** no of it if my conduct was satisfactory" and "say that the salary should not **359 199 34 724** allowing the
  president to fix each at what rate he pleases".
- Short's private letter of 27 Jul 1792 repeats the whole paragraph in cypher with the same groups and no decoding
  (and a struck 1312 687 after 757: he first wrote "salaries", then 757.427 "salary"). It confirms the digits only.
- "Been" is 1700 in this code (TJ's interlinear, this letter and three others), so 401 = been would need a homophone.
  401 carries a caret below it in both copies; the same caret marks 985 (= less), so the mark is not specific to 401.
- None of the six groups occurs in any other Code No. 10 letter checked (Founders notes of all 39 documents; page
  images of Short 26 Sep 1790, 27 Oct 1790, 11 and 13 Nov 1793, TJ to Carmichael & Short 31 May 1793, ~1,100 groups).
- Readings by context only, kept as conjectures: 401 [been?], 1083 [would?] ("to have [been] sure. There [would] have
  [been] no[ne?] of it"), 359 199 34 724 [four groups, e.g. "exceed a fixed sum"; not filled].

### Carmichael, 14 Apr 1788 (Code No. 13)

- Five items: 108 ("Had I been in 108 I should ... have been of the sentiment of Paca"), 108 again (blotted: "108 has not
  acceded to the Constitution"), 223 ("223 has"), 273 ("the 273 seem pleased with it"), 597 ("what says 597").
- Code No. 13 is not Code No. 11 read through a faulty copy: in the rebuilt Code No. 11 table (`jefferson1787/key.tsv`,
  `reading.tsv`) 597 = freedom and 223 = trouble. Founders "Code No. 13" returns this letter only, so there is no
  sibling text.
- The context fixes 108 = Maryland (Carmichael's state; Paca was Maryland's leading Antifederalist; Maryland ratified
  on 28 Apr 1788) and 223 = Massachusetts (ratified 6 Feb 1788) with high confidence, 273 = majority as likely.
  597 [you?]: "what says Virginia" fits the sentence as well as "you" (Virginia had not ratified; TJ was a Virginian);
  both are context guesses and 597 stays open.

## Reading

`make_reading.py` → `reading.tsv` (one row per counted code group; Short's one struck group excluded). Grades: T = TJ's
interlinear over the group; H = value attested by a decoding in another letter of the same code; E = the PTJ editors'
reading, not attested elsewhere; C = conjecture (editors' brackets or context only); O = open.

| Letter | Groups | T | H | E | C | O |
|---|---|---|---|---|---|---|
| Short 26 Jul 1792 | 674 | 511 | — | 156 | 0 | 7 (401 x2, 1083, 359, 199, 34, 724) |
| Pinckney 28 Aug 1793 | 58 | — | 39 | 17 | 0 | 2 (447, ?55) |
| Carmichael 14 Apr 1788 | 5 | — | — | — | 4 | 1 (597) |
| **All** | **737** | 511 | 39 | 173 | 4 | 10 |

727 of 737 groups (98.6%) carry a reading; 723 (98.1%) without the conjectures (figures of 11 Nov 2026, after the
regrading of the Pinckney passage; on 27 Oct they were 728 and 720). Every letter is covered; what stays open is ten
groups in three letters (nine distinct), each without a decoded occurrence anywhere in its code. The six other Code
No. 16 letters (next section) are not in this table: they carry decipherments of the time and have their own texts.
Short's full code: 7 coded frames (016_0999, 1001, 1005-1009), 32 groups with a doubtful digit (read through TJ's
interlinear and the editors).

## Outcome

Method: existing decipherment (TJ's interlinear decoding of Short's letter, the PTJ editors' printed decodings of all
three, conjectures in brackets); the work was transcription, checking every group against the attested values of the
same code, and searching every sibling letter for the open groups. Extent: complete by the read bar (98.1% without
conjectures, measured; only scattered single-occurrence groups open, each externally blocked). Key: partial (none of
the three codes has a key; `key.tsv` collects 171 Code No. 10 values from TJ's interlinear and 262 Code No. 16 values from
Taylor's decodings and the Explication). Profile class: already solved (as erving1807); grades in profile.json: H = T+H
(550), M = E (173), I = C (4). Provenance: mixed since PR #399. Prior solution: the editors'
readings (PTJ 13, 1956; 24, 1990; 26, 1995), found before the work and used. What this adds: 447 for the editors' 497
(Pinckney); the confirmation of 30 of the 58 Pinckney groups from Taylor's decodings (39 with the other letters of the code, PR #399); the proof that the open Short
groups and Carmichael's code occur nowhere else (Code No. 13 ≠ Code No. 11; "been" = 1700); a full transcription of
Short's 674 groups and of Pinckney's 15 coded frames on M30 roll 2.

## Other letters in Code No. 16 (PR #399, Andrew Beling, 11 Nov 2026)

Contributed by Andrew Beling, with AI agents; everything is in [`beling/`](beling/README.md). Code No. 16 is the code
Weber (1979, p. 155) calls the "663" code and lists as not located. The same code is used in six further letters, all
with a decipherment of the time on the page except Eaton's copy of the Bey's letter, which has a printed translation:

| Document (profile id) | Where | Groups | Words from | State |
|---|---|---|---|---|
| Pinckney, coded parts of 21 Jul and 11 Aug 1795 re-enciphered in "Cypher 2d" (enclosed 27 Aug), and of 1 Oct 1795 (`pinckney_179508`) | NARA M31 roll 7 frames 0018-0021 | 295 | George Taylor Jr.'s interlinear | read (phrases; read_share 0.963) |
| Pinckney, San Lorenzo 28 Oct 1795 with notes on the treaty, Paris 18 Dec 1795 (`pinckney_179510`) | M31 roll 7 frames 0020, 0111, 0134-0135, 0177 | 224 | a clerk's interlinear and margin | read in part (0.941; gutter, fragments) |
| Eaton to the Secretary of State, Tunis, 25 May 1801 (`eaton_18010525`) | NARA T303 roll 2 frames 0048-0049 | 196 | Jacob Wagner's interlinear | read (0.980) |
| Hammuda Bey to Jefferson, 8 Sep 1802, Eaton's coded copy, with Eaton's postscript, enclosed 9 Oct 1802 (`eaton_18021009`) | T303 roll 2 frames 0299-0303 | 468 + 94 | 1802 printed translation (body); Madison Papers editors (postscript) | read (0.959) |
| Eaton to Madison, 22 Oct 1802 (`eaton_18021022`) | T303 roll 2 frame 0320 | 92 | interlinear on the page; repeats the postscript | read in part (0.921; blots) |
| Lear to Madison, [Jan] 1813 (`lear_181301`) | LoC James Monroe Papers reel 5, images 981-982 | 354 | John Graham's interlinear | read (0.992) |

- Transcriptions and decryptions: `ct/<id>.txt`, `texts/<id>_decryption.txt` (built by `make_code16_texts.py` from the
  bundle's witness files), readings `texts/<id>_reading.txt` (written by hand from them in the integration check).
- Key: `beling/key/code16_key_v4.tsv`, 537 groups: D 158 (one group under one word), S2 81 and S1 111 (the only element
  of Weber's 1,600-element word list that fits), A 125 (aligned from the bare Pinckney frames to the printed editions),
  B 62 (taken from `key.tsv`). `key.tsv` stays as it is; the comparison is in `beling/comparison/` (D agree 64, differ 0;
  20 unmarked whole-word entries of `key.tsv` are syllables in the other letters, e.g. 541 an, 982 ar, 1453 sa, 523 ful;
  13 differ outright). Those 33 entries of `key.tsv` are not corrected here: none of them changes the 28 Aug 1793 reading.
- Tests with a key frozen beforehand (311 groups): Pinckney 1795 0.886 (93 of 105), pass; Eaton 1801 0.80 (48 of 60),
  below the 0.85 bar; Eaton 22 Oct 1802 0.898 (44 of 49) on a passage that repeats the 9 Oct postscript, so not new text.
- Prior work, as the contributor found it: the Madison Papers editors read Eaton's 1802 postscript and Lear's letter
  with an unprinted key from the Lear family papers; the Jefferson Papers editors used an unpublished partial
  reconstruction. Nobody was found to have said that Pinckney's London code and the Eaton/Lear code are one code.
- Pinckney's frames on M30 roll 2 without a decoding of the time (0106-0107, 0135-0136, foot of 0148, 0178, 0196 ll. 5-10,
  0305, 0317; 1,982 groups) are decoded with the key in `beling/decodes/`: 81.0% of groups covered, 62.1% without the A
  and B values. Decoded, not read; the editions print most of them. Not listed in `outcome.texts`.

## Integration check (11 Nov 2026)

- Scripts in `beling/tests`, `comparison`, `corrections`, `decodes` read first (they read the bundle and `../`, write only
  inside the bundle, no network), then run. `rescore_frozen_key.py`: 0.879 (94 of 107, shuffled best 0.065) and 0.797
  (51 of 64, shuffled best 0.125), as the README says; verdicts as recorded (pass; below the bar). The original scoring
  runs (0.886, 0.80) were not kept as scripts, so those two exact figures are the contributor's record.
- The Eaton 22 Oct 1802 score (0.898) could not be re-run: the edition text is not in the bundle and Founders Online
  answered with a bot check. An interlinear on the page gives the same words; 21 of 28 single-group words equal `key.tsv`.
- Held out: `tests/frozen_key_v1.tsv` has 311 groups and the sha256 stated in the preregistration (e88b2c7f...). The
  preregistration and the key arrive in one commit, so the order of events rests on the contributor's timestamps.
- Key count: `code16_key_v4.tsv` has 537 rows (D 158, S1 111, S2 81, A 125, B 62), sha256 e18775d8... as stated.
- One key, one entry: checked apart from the contributor's key. Single-group interlinear words of each new letter
  against `key.tsv` (values from Pinckney's 1793-94 letters only): Lear 61 of 70 equal, Tunis 177 of 178, Eaton 1801 29 of
  36, Pinckney 1795 66 of 70 and 42 of 44, Eaton 22 Oct 21 of 28; the best of 200 shuffled keys gives 2 to 20. The misses
  are syllables (541 an) and inflections. All six are Code No. 16 and belong in this folder with Pinckney's 1793 letter.
  The folder still holds three codes (10, 13, 16), as it did before; splitting Code No. 16 into its own entry is left
  to the maintainer.
- Corrections to the 28 Aug 1793 reading checked in the witness files: 234 time (Lear 981-L4, 982-L2; Tunis body), 501
  secret (Lear 981-L25), 923 are (Eaton 1801 L10; Pinckney 1795 0019L-L01), Sir = 1328-1374 (Tunis, twice) and Mr = 1018-1374 (twice), 668 at (Eaton 1801 three times, Pinckney 1795, Tunis), 1010 tin (distinguishable,
  distinction, distinguished), 675 ly (generally, particularly, successively ...). 447 and 672 are in no witness.
  `proposed_changes.patch` applied; `make_reading.py` gives H 39, E 17, C 0, O 2.
- Corrected here: `beling/corrections/pinckney_17930828_points.tsv` was stale in two cells (1374 and 1258 showed "-"
  from before the key correction of 11 Nov); regenerated, and its line in `SHA256SUMS.txt` updated. The README's last
  paragraph says the comparison and decodes "were not regenerated"; sections 5 and 6 say they were, and re-running
  them reproduces the committed files, so they were.
- Readings: the six texts were read as sentences. In Eaton 1801 four interlinear words were doubtfully transcribed;
  the reading marks them: 855 [?is] (transcribed "professd"; 855 is "is" in cru-is-ing), 828 1506 1559 [?Barbary],
  1506 886 658 [?Bashaw] (transcribed "Barbary", blotted on the image; Bashaw three times in the Bey's letter),
  586 918 134 [?going] (transcribed "& my gains"). The printed editions were not opened in this check.
- `make_profile.py` was not re-run (it would drop hand edits); `profile.json` was edited directly.

Claims review by a second reader (11 Nov 2026): the first coded line of Pinckney's 1 October 1795 letter (frame
0020, ten groups) is in both `ct/pinckney_179508.txt` and `ct/pinckney_179510.txt`, so the 295 and 224 group counts
overlap by ten (509 distinct, and about 1,710 rather than 1,720 in all); the two transcriptions differ on its first
group (1521 against 1321), not settled. The Escalation line's "31 of 58" is 30, as everywhere else.

## Remaining gaps

- Pinckney 28 Aug 1793, group 447 (first word of the passage, before "regiments") - blocker: too-short; single occurrence in all 15 coded Pinckney frames on M30 roll 2 and in none of the six other Code No. 16 letters, no decoding; Pinckney's own copy (PrC, Pinckney Family Papers, South Carolina Historical Society) not online
- Pinckney 28 Aug 1793, ?55 668 800 (a general's name ending -at-s; the editors' [Dunda]s) - blocker: illegible; the first digits of ?55 are in the binding gutter, and 668 = at in Eaton 1801, Pinckney 1795 and the Bey's letter of 1802, so the groups do not spell Dundas (234 time and 501 secret are closed: attested in Lear 1813)
- Short 26 Jul 1792, groups 401 (x2), 1083, 359, 199, 34, 724 - blocker: too-short; they occur only in this passage and its re-encipherment of 27 Jul; no decoding in any Code No. 10 letter checked; 401 is not the attested "been" (1700)
- Carmichael 14 Apr 1788, group 597 (and the context-only values of 108, 223, 273) - blocker: no-key-material; Code No. 13 survives in this letter only, no key and no other text
- Pinckney 28 Oct and 18 Dec 1795 (M31 roll 7 frames 0111, 0177), line ends and several groups - blocker: illegible; binding gutter and a shadowed last line, the NARA JPEG is the only image
- Eaton 22 Oct 1802 (T303 roll 2 frame 0320), six interlinear words - blocker: illegible; blotted on the film; the passage repeats the 9 Oct postscript, which reads
- Code No. 16 groups without a value (about 1,600 elements; 537 in the key) - blocker: no-key-material; the original key (Lear family papers) is unprinted and was sold in 2010 to an unnamed buyer (contributor's notes)

## Escalation

- [x] siblings: Short's re-enciphered extract of 27 Jul 1792 (016_1010-1012); 39 Code No. 10 documents (Founders notes) and six of them on the images; all 15 coded Pinckney frames of M30 roll 2 (1793-1795) transcribed, seven with decodings; Founders "Code No. 13" = this letter only
- [x] clear-pages: TJ's "copy so far only" Tr omits the coded section; the 15 Aug 1793 clear Tr and the 25 Nov 1793 "Explication of the Cyphers" (frame 0179) used as cribs for Code No. 16 values; no clear copy of 28 Aug exists in RG 59
- [x] known-keys: Code No. 11 table (jefferson1787) tried on Carmichael's Code No. 13: does not fit (597 freedom, 223 trouble)
- [x] print: Founders Online (PTJ 13, 24, 26), Founders search for each number, web search for the size of Grey's force (Aug 1793): no number found
- [x] key-rebuild: Code No. 16 values collected from seven decoded Pinckney letters and applied (30 of 58 groups of 28 Aug attested); Code No. 10 checked for alphabetical bracketing (none: two-part code)
- [x] retry: 447/497 re-read at 2x on frame 0140; Carmichael's blotted 108 re-read at 2x; every open group searched in all transcribed frames; 11 Nov 2026: the 28 Aug 1793 passage regraded with the six other Code No. 16 letters (PR #399), 447 and 672 searched in them (absent)
