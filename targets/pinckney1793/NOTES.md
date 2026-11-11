# pinckney1793 — Jefferson's Code No. 16 (Thomas Pinckney's London code, Weber's "663" code), 1793-1813

One code, seven documents: Thomas Pinckney to Jefferson, London, 28 Aug 1793 (part of catalogue no. 484, Founders Online
sweep, `research/founders_emlo/`); Pinckney from Spain and Paris, 1795 (two files); William Eaton at Tunis, 25 May 1801;
Hammuda Bey to Jefferson, 8 Sep 1802, in Eaton's coded copy with Eaton's postscript; Eaton, 22 Oct 1802; Tobias Lear,
[Jan] 1813. The 1793 passage was worked on 26-27 Oct 2026 inside `targets/legation1788/`; the six later letters, the
537-group key and its tests were contributed by Andrew Beling (PR #399, merged 11 Nov 2026; [`beling/`](beling/README.md)).
Split out of `legation1788` on 11 Nov 2026 (see "Split", below): Short's Code No. 10 and Carmichael's Code No. 13 are
different codes, with their own page, `targets/legation1788/`.

## What it is

Jefferson's Code No. 16 is a two-part numerical code (words, syllables, letters; about 1,600 elements by Weber's word
list), numbers in no alphabetical order. Pinckney used Code No. 15 to 27 Apr 1793 and Code No. 16 from 20 Jun 1793
(Founders note on Pinckney's letter of 20 Jun 1793). It is the code Weber (1979, p. 155) calls the "663" code (663 =
the) and lists as not located.

| Document (profile id) | Where | Groups | Words from |
|---|---|---|---|
| Pinckney → TJ, London, 28 Aug 1793 (`pinckney_17930828`) | NARA RG 59, Despatches from US Ministers to Great Britain, M30 roll 2 frame 0140 | 58 | the PTJ editors' partial decipherment (vol. 26); no decoding of the time |
| Pinckney, coded parts of 21 Jul and 11 Aug 1795 re-enciphered in "Cypher 2d" (enclosed 27 Aug), and of 1 Oct 1795 (`pinckney_179508`) | NARA M31 roll 7 frames 0018-0021 | 295 | George Taylor Jr.'s interlinear |
| Pinckney, San Lorenzo 28 Oct 1795 with notes on the treaty, Paris 18 Dec 1795 (`pinckney_179510`) | M31 roll 7 frames 0020, 0111, 0134-0135, 0177 | 224 | a clerk's interlinear and margin |
| Eaton to the Secretary of State, Tunis, 25 May 1801 (`eaton_18010525`) | NARA T303 roll 2 frames 0048-0049 | 196 | Jacob Wagner's interlinear |
| Hammuda Bey to Jefferson, 8 Sep 1802, Eaton's coded copy, with Eaton's postscript, enclosed 9 Oct 1802 (`eaton_18021009`) | T303 roll 2 frames 0299-0303 | 468 + 94 | 1802 printed translation (body); Madison Papers editors (postscript) |
| Eaton to Madison, 22 Oct 1802 (`eaton_18021022`) | T303 roll 2 frame 0320 | 92 | interlinear on the page; repeats the postscript |
| Lear to Madison, [Jan] 1813 (`lear_181301`) | LoC James Monroe Papers reel 5, images 981-982 | 354 | John Graham's interlinear |

## Sources and files

- `transcription/pinckney_m30.tsv`, `pinckney_m30_frames.md`: every code group on M30 roll 2 frames 0101-0330 (15 coded
  frames, ~2,660 rows), with the interlinear decodings of 20 Jun, 25 Sep, 27 Nov, 17 Dec 1793, 28 Jan and Feb 1794 and
  the "Explication of the Cyphers" (0179) aligned to 25 Nov 1793.
- `reading_pinckney_17930828.tsv`: the 28 Aug 1793 passage group by group, graded against the attested values.
- `key.tsv` (`make_key.py`): the 262 Code No. 16 values decoded at the time in Pinckney's letters of 1793-94.
- `beling/`: Andrew Beling's bundle (witness transcriptions of the six later letters, `key/code16_key_v4.tsv`, the tests
  with a frozen key, the comparison with `key.tsv`, decodes of Pinckney's undecoded frames).
- `ct/<id>.txt`, `texts/<id>_decryption.txt`: built by `make_code16_texts.py` from the bundle's witness files for the six
  later letters; `texts/<id>_reading.txt` written by hand from them. The three files of `pinckney_17930828` were made by
  `../legation1788/make_profile.py` in October and edited by hand on 11 Nov.
- `dl_m30.py`: downloads M30 roll 2 frames from the NARA catalog media server (images git-ignored).
- `WORKLOG.md`: the Code No. 16 lines of the log of 26-27 Oct 2026, copied from `../legation1788/WORKLOG.md`.

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

## Reading of 28 Aug 1793

`reading_pinckney_17930828.tsv` (one row per code group). Grades: H = value attested by a decoding in another letter of
the same code; E = the PTJ editors' reading, not attested elsewhere; C = conjecture (editors' brackets or context only);
O = open.

| Date of the count | Groups | H | E | C | O |
|---|---|---|---|---|---|
| 27 Oct 2026 (Pinckney's letters of 1793-94 only) | 58 | 30 | 23 | 4 | 1 (447) |
| 11 Nov 2026 (with the six later letters, PR #399) | 58 | 39 | 17 | 0 | 2 (447, ?55) |

56 of 58 groups (96.6%) carry a reading (recounted from the file on 11 Nov 2026 after the split). Until the split these
58 groups were counted with Short's and Carmichael's in `../legation1788/reading.tsv` (737 groups).

## The six later letters in Code No. 16 (PR #399, Andrew Beling, 11 Nov 2026)

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
  B 62 (taken from `key.tsv`). `key.tsv` (this folder's 262 values) stays as it is; the comparison is in `beling/comparison/` (D agree 64, differ 0;
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

## Measure (recounted 11 Nov 2026, after the split)

Groups, counted in the `ct/` files: 58 (28 Aug 1793), 295, 224, 196, 562 (468 + 94), 92, 354; the six later letters make
1,723, or 1,713 with the first coded line of 1 Oct 1795 (ten groups, in both Pinckney 1795 files) counted once; 1,771 with
the 1793 passage. `python docs/_check_profile.py --measure <file> --drop-first` gives 295, 224 and 196 for the three files
it can count; Lear's file has 355 tokens because the catchword 478 at the foot of image 981 is written again at the head
of 982; the Bey's letter (groups joined by dashes) and Eaton's 22 Oct passage (two transcriptions) were counted by
splitting the lines on spaces, dashes and stops.

Words, counted in the reading files with `research/reading_audit/v10_relabel.py` `share()` (holes = bracketed doubtful or
supplied words and marked gaps):

| Reading file | Words read | Holes | Share |
|---|---|---|---|
| `pinckney_17930828` | 38 | 1 | 0.974 (by groups, 56 of 58: 0.966, the figure used) |
| `pinckney_179508` | 224 | 9 | 0.961 |
| `pinckney_179510` | 185 | 12 | 0.939 |
| `eaton_18010525` | 244 | 5 | 0.980 |
| `eaton_18021009` | 378 | 16 | 0.959 |
| `eaton_18021022` | 67 | 6 | 0.918 |
| `lear_181301` | 248 | 2 | 0.992 |
| **All seven** | **1,384** | **51** | **0.964** |

The profile carried 0.963, 0.941 and 0.921 for `pinckney_179508`, `pinckney_179510` and `eaton_18021022` before the split;
the files as they stand give 0.961, 0.939 and 0.918, and the profile now has those. The two under 0.95 are "read in part".

## Outcome

Method: read from existing decipherment. Six of the seven documents carry a decipherment of the time (or, for the Bey's
letter, a translation printed in 1802), and the 1793 passage was printed deciphered in part by the PTJ editors (vol. 26,
1995); the work was transcription, rebuilding values of the code from those decipherments and checking the editors'
reading of 1793 against them. No text shown was first obtained with the rebuilt key, so the method is not "key recovered
based on adjacent plaintext", although the key was rebuilt that way: the one text the key alone produces, the decode of
Pinckney's undecoded London frames, is decoded, not read, and is not counted. Extent: complete by the read bar (0.964 of
the words of the seven readings, measured; every document covered; what is open is blocked from outside: binding,
blots, one group that occurs once). Profile class: already solved, as the combined entry was. Key: partial (537 of about
1,600 groups; no key sheet is public). Grades in profile.json, for the 1793 passage only: H 39, M = E 17. Provenance:
mixed (the project's October work on the 1793 passage, then PR #399). Prior solutions: the PTJ editors (1793 passage);
the clerks' interlinears; the Madison Papers editors for Eaton's postscript and Lear's letter (per the contributor's
notes). What this adds: 447 for the editors' 497; 39 of the 58 groups of 1793 confirmed from decodings of the time and
[Dunda]s shown not to be what the groups spell; the identification of Pinckney's London code with the code of Eaton and
Lear; transcriptions of the six later letters and of Pinckney's 15 coded frames on M30 roll 2; a graded key of 537
groups with tests on a key frozen beforehand.

## Integration check (11 Nov 2026, made in `targets/legation1788/` before the split)

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
  are syllables (541 an) and inflections. All six are Code No. 16 and belong with Pinckney's 1793 letter.
  The folder (then `targets/legation1788/`) still held three codes (10, 13, 16), as it did before; splitting Code No. 16
  into its own entry was left to the maintainer, and was done the same day ("Split", below).
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
- `make_profile.py` (in `../legation1788/`) was not re-run (it would drop hand edits); `profile.json` was edited directly.

Claims review by a second reader (11 Nov 2026): the first coded line of Pinckney's 1 October 1795 letter (frame
0020, ten groups) is in both `ct/pinckney_179508.txt` and `ct/pinckney_179510.txt`, so the 295 and 224 group counts
overlap by ten (509 distinct, and about 1,710 rather than 1,720 in all); the two transcriptions differ on its first
group (1521 against 1321), not settled. The Escalation line's "31 of 58" is 30, as everywhere else.

## Split (11 Nov 2026)

Until 11 Nov 2026 these documents were part of `targets/legation1788/`, which held three codes (Short's No. 10,
Carmichael's No. 13, Pinckney's No. 16). The repository's rule is one key, one entry, so Code No. 16 was moved here at
the maintainer's request. Short's and Carmichael's letters stay in `legation1788`: a different code each, with its own
page (`docs/legation1788.html`).

- Moved here with `git mv`: `beling/`, `reading_pinckney_17930828.tsv`, `make_code16_texts.py`, `dl_m30.py`,
  `transcription/pinckney_m30.tsv` and `pinckney_m30_frames.md`, and the `ct/` and `texts/` files of the seven documents.
- Divided: `key.tsv` (the 262 Code No. 16 rows are here; the 171 Code No. 10 rows stayed) and `make_key.py` (this
  folder's half reproduces `key.tsv` byte for byte).
- In `beling/`: the four scripts that say where to run them now say `targets/pinckney1793/beling`; they find `../key.tsv`,
  `../reading_pinckney_17930828.tsv` and `../transcription/pinckney_m30.tsv` here. Re-run after the move: the comparison
  gives the same table (its header line names the new path), the decode of the undecoded frames and the coverage table
  are unchanged, `rescore_frozen_key.py` prints 0.879 and 0.797 as before, and `corrections/pinckney_17930828_points.py`
  stops as it is meant to once the patch is applied (row 1.5 is already H). `README.md` has a note on the move and
  `SHA256SUMS.txt` has the six changed hashes. `CHECKS.txt`, `proposed_changes.patch` and the file names with
  `legation1788` in them are unchanged.
- Pointers fixed elsewhere: `targets/king1797/` (the Weber list is `../pinckney1793/beling/key/weber_1600_family_vocab.txt`),
  `targets/poinsett1813/shift_test.py` (reads both halves of the old `key.tsv`).
- Site: `docs/pinckney1793.html` (new), `docs/legation1788.html` cut down to Short and Carmichael; the images
  `legation1788_lead.jpg` and `legation1788_eaton1801.jpg` became `pinckney1793_lead.jpg` and `pinckney1793_eaton1801.jpg`;
  the key-web node `k-legation-code16` now links to this target.
- Catalogue no. 484 named Short, Carmichael and Pinckney 1793 together and was removed on 27 Oct 2026; it stays listed
  under `legation1788`, and this target's ledger rows refer to it.

## Claims review of the new page (11 Nov 2026)

No separate reviewer agent was available in the session that made the split, so `docs/pinckney1793.html` was re-read line
by line against this file, `profile.json`, the reading files and the bundle, with the checklist of
`.claude/skills/writeup/claims-review.md`. Fixed: the hero said all seven documents carry decipherments of the time (the
1793 passage has none); "No key sheet has been found" became "has been printed" (a key exists in the Lear family papers,
unprinted); the hands of two interlinears are not named in the sources, so they are no longer called State Department
clerks; "one group undeciphered" reworded. Not checkable here: the images, and the printed editions (not opened).

## Remaining gaps

- Pinckney 28 Aug 1793, group 447 (first word of the passage, before "regiments") - blocker: too-short; single occurrence in all 15 coded Pinckney frames on M30 roll 2 and in none of the six other Code No. 16 letters, no decoding; Pinckney's own copy (PrC, Pinckney Family Papers, South Carolina Historical Society) not online
- Pinckney 28 Aug 1793, ?55 668 800 (a general's name ending -at-s; the editors' [Dunda]s) - blocker: illegible; the first digits of ?55 are in the binding gutter, and 668 = at in Eaton 1801, Pinckney 1795 and the Bey's letter of 1802, so the groups do not spell Dundas (234 time and 501 secret are closed: attested in Lear 1813)
- Pinckney 28 Oct and 18 Dec 1795 (M31 roll 7 frames 0111, 0177), line ends and several groups - blocker: illegible; binding gutter and a shadowed last line, the NARA JPEG is the only image
- Eaton 22 Oct 1802 (T303 roll 2 frame 0320), six interlinear words - blocker: illegible; blotted on the film; the passage repeats the 9 Oct postscript, which reads
- Code No. 16 groups without a value (about 1,600 elements; 537 in the key) - blocker: no-key-material; the original key (Lear family papers) is unprinted and was sold in 2010 to an unnamed buyer (contributor's notes)

## Escalation

- [x] siblings: all 15 coded Pinckney frames of M30 roll 2 (1793-1795) transcribed, seven with decodings; the six later letters of the code (Pinckney 1795 on M31 roll 7, Eaton 1801-02 on T303 roll 2, Lear 1813) transcribed with their decipherments (PR #399)
- [x] clear-pages: TJ's "copy so far only" Tr omits the coded section; the 15 Aug 1793 clear Tr and the 25 Nov 1793 "Explication of the Cyphers" (frame 0179) used as cribs for Code No. 16 values; no clear copy of 28 Aug exists in RG 59
- [x] known-keys: no key sheet of Code No. 16 is public (Weber: not located; the Lear family key is unprinted); King's code (king1797) compared number by number: no value the same
- [x] print: Founders Online (PTJ 26), Founders search for each number, web search for the size of Grey's force (Aug 1793): no number found; the 1802 printed translation of the Bey's letter used for its body
- [x] key-rebuild: Code No. 16 values collected from seven decoded Pinckney letters and applied (30 of 58 groups of 28 Aug attested); then Beling's key of 537 groups from the six later letters (39 of 58 attested)
- [x] retry: 447/497 re-read at 2x on frame 0140; every open group searched in all transcribed frames; 11 Nov 2026: the 28 Aug 1793 passage regraded with the six other Code No. 16 letters (PR #399), 447 and 672 searched in them (absent)
