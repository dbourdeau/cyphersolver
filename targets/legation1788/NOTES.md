# legation1788 — residual groups in Jefferson's legation codes Nos. 10 and 13 (Short 1792, Carmichael 1788)

Catalogue no. 484 (Founders Online sweep, `research/founders_emlo/`). Worked 26-27 Oct 2026 from the solve-page brief.
Sibling target: `jefferson1787` (Code No. 11, catalogue 483). Until 11 Nov 2026 this folder also held Jefferson's Code
No. 16 (Thomas Pinckney, 28 Aug 1793, and six later letters): a different code, with its own page and folder,
`targets/pinckney1793/` (see "Split", below).

**This folder still holds two different codes**, Short's Code No. 10 and Carmichael's Code No. 13. They were not split
on 11 Nov 2026; by the one-key-one-entry rule they should be, and that is left for a later session.

## What it is

Two letters to Thomas Jefferson (as Secretary of State, and as minister in Paris), each partly in a numerical code, each
printed in *The Papers of Thomas Jefferson* with a few groups left unread or read by conjecture:

| Letter | Code | Original | What was open |
|---|---|---|---|
| William Short → TJ, The Hague, 26 Jul 1792 ("Private") | No. 10 | LoC Jefferson Papers ser. 1, mtj1 016_0998-1009 (RC, TJ interlinear); extract re-enciphered in Short → TJ 27 Jul 1792, 016_1010-1012 | 401, 1083, 401 (note 21); 359, 199, 34, 724 (note 23) |
| William Carmichael → TJ, Madrid, 14 Apr 1788 | No. 13 (the code David Franks left with him, Nov 1786) | LoC mtj1 009_0223-0230 | five groups read by conjecture: [Maryland] x2, [Massachusetts], [majority], [you?] |

The codes are two-part numerical codes of about 1,700-1,850 groups (words, syllables, letters), groups separated by
dots, numbers in no alphabetical order (checked for No. 10 on 016_1007-1008: 7 s, 12 pleny, 68 president, 153 al, 218 my,
224 the, 294 I, 426 to ... no run is ordered), so a group cannot be bracketed between its neighbours.

## Sources and files

- `transcription/short_17920726.tsv`: the open groups of Short's letter and their neighbours, both copies.
- `transcription/short_17920726_full.tsv`: every code group of the 26 Jul letter with TJ's interlinear (subagent).
- `transcription/code10_hunt.tsv`, `code10_checked.md`: the search of the other Code No. 10 letters for the six groups.
- `transcription/carmichael_17880414.tsv`: Carmichael's five code items.
- `key.tsv` (`make_key.py`): the 171 Code No. 10 values Jefferson wrote over Short's groups. `reading.tsv`
  (`make_reading.py`): the graded reading. `ct/`, `texts/`: the transcription, decryption and reading of each letter.
- `make_profile.py`: how the first profile (three letters) was made; not to be re-run since the split.
- `WORKLOG.md`: the dated log of 26-27 Oct 2026, all three letters, kept whole here.

## Findings

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
interlinear over the group; E = the PTJ editors' reading, not attested elsewhere; C = conjecture (editors' brackets or
context only); O = open.

| Letter | Groups | T | E | C | O |
|---|---|---|---|---|---|
| Short 26 Jul 1792 | 674 | 511 | 156 | 0 | 7 (401 x2, 1083, 359, 199, 34, 724) |
| Carmichael 14 Apr 1788 | 5 | — | — | 4 | 1 (597) |
| **Both** | **679** | 511 | 156 | 4 | 8 |

667 of 679 groups (98.2%) carry a reading without the conjectures, 671 (98.8%) with them (recounted 11 Nov 2026 from
`reading.tsv` after the split). Both letters are covered; what stays open is eight groups (seven distinct), each without
a decoded occurrence anywhere in its code. Short's full code: 7 coded frames (016_0999, 1001, 1005-1009), 32 groups with
a doubtful digit (read through TJ's interlinear and the editors).

History of the count: on 27 Oct 2026 the table had three letters, 737 groups, with Pinckney's 58 (728 with a reading, 720
without conjectures); after the regrading of the Pinckney passage on 11 Nov it read 727 and 723. Pinckney's 58 groups
are now counted in `targets/pinckney1793/`.

## Outcome

Method: read from existing decipherment (TJ's interlinear decoding of Short's letter, the PTJ editors' printed decodings
of both, conjectures in brackets); the work was transcription, checking Jefferson's values against the editors' text,
and searching every sibling letter for the open groups. Extent: complete by the read bar (98.2% without conjectures,
measured; only scattered single-occurrence groups open, each externally blocked). Key: partial (neither code has a key;
`key.tsv` collects 171 Code No. 10 values from TJ's interlinear). Profile class: already solved (as erving1807); grades
in profile.json: H = T (511), M = E (156), I = C (4). Provenance: project. Prior solution: the editors' readings (PTJ 13,
1956; 24, 1990), found before the work and used. What this adds: the proof that the open Short groups and Carmichael's
code occur nowhere else (Code No. 13 ≠ Code No. 11; "been" = 1700); a full transcription of Short's 674 groups.

## Split (11 Nov 2026)

Until 11 Nov 2026 this folder held three codes: Short's No. 10, Carmichael's No. 13 and Pinckney's No. 16, which after
PR #399 (Andrew Beling) was most of the entry. The repository's rule is one key, one entry, so Code No. 16 was moved
out, at the maintainer's request: it is a different code, with its own page (`docs/pinckney1793.html`) and folder
(`targets/pinckney1793/`).

- Moved there with `git mv`: `beling/` (the PR #399 bundle), `reading_pinckney_17930828.tsv`, `make_code16_texts.py`,
  `dl_m30.py`, `transcription/pinckney_m30.tsv` and `pinckney_m30_frames.md`, and the `ct/` and `texts/` files of the seven
  Code No. 16 documents (`pinckney_17930828`, `pinckney_179508`, `pinckney_179510`, `eaton_18010525`, `eaton_18021009`,
  `eaton_18021022`, `lear_181301`).
- Divided: `key.tsv` (the 171 Code No. 10 rows stay here, the 262 Code No. 16 rows are `../pinckney1793/key.tsv`),
  `make_key.py` (each folder has its half; both re-run and reproduce their file), `reading.tsv` and `make_reading.py`
  (Pinckney's 58 rows removed here; they are in `../pinckney1793/reading_pinckney_17930828.tsv`).
- Stays here: everything of Short and Carmichael, `WORKLOG.md` (the log of all three letters; the Pinckney lines are
  copied into the new folder's log), `make_profile.py` (marked not to be re-run).
- Credits: Andrew Beling's (identification, key corrected, transcription), the Madison Papers editors' and the
  provenance "mixed" went with Code No. 16; this entry is the project's own again.
- Catalogue no. 484 named all three letters; it stays listed under this entry and the new one refers to it.
- Not done: Codes No. 10 and No. 13 are still together here.

## Claims review of the cut-down page (11 Nov 2026)

No separate reviewer agent was available in the session that made the split, so `docs/legation1788.html` was re-read line
by line against this file, `profile.json` and `reading.tsv`, with the checklist of `.claude/skills/writeup/claims-review.md`.
Fixed: the head and hero said every group was set against Jefferson's decoding (he decoded Short's letter only, 511 of
674 groups); "the printed readings hold" cut (nothing here tests the editors' 156 groups); the glance box now says that
Carmichael's code has no other letter to search. Counts on the page are those of `reading.tsv` (679, 667, 4, 8).

## Independent verification by Brice Dudout (PR #570, 14 Nov 2026)

Brice Dudout (`VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) put `key.tsv` against `ct/short_17920726.txt`:
674 groups in the same order as the decryption, and all 471 groups that carry a value in `key.tsv` agree with it (99 more
are later parts of a word spread over several groups; 104 have no value in `key.tsv`). Re-run here: the same.

- **How to read `key.tsv`.** `make_key.py` credits a word that runs over several groups to its first group, so a
  syllable group can carry several words: 1101 accept / acquainted / account (probably ac-), 689 conspicuous /
  consolation / consider (con-), 562 forms / inform (form), 1259 re-. 494 (from, without) and 534 (circumstan-,
  honourable) do not resolve to one value. The file is a list of Jefferson's words by first group, not a table of code
  values. No reading changes and `key.tsv` is left as it is.
- **Carmichael, 14 Apr 1788.** `read_share` stays 0.0, the share of its five code items read from a key (none).
  `research/reading_audit/v10_relabel.py` would give 0.974 on the reading file, because it does not turn the capitalised
  conjectures *[Maryland]* and *[Massachusetts]* into holes and does not count 597; with the four conjectures and 597 as
  holes among the 40 words of the sentences the figure is 0.875. Either way the letter is read in part.

Not checked: the Library of Congress images (597, the blotted 108; 494 and 534 on frames 016_1006-1007).

## Remaining gaps

- Short 26 Jul 1792, groups 401 (x2), 1083, 359, 199, 34, 724 - blocker: too-short; they occur only in this passage and its re-encipherment of 27 Jul; no decoding in any Code No. 10 letter checked; 401 is not the attested "been" (1700)
- Carmichael 14 Apr 1788, group 597 (and the context-only values of 108, 223, 273) - blocker: no-key-material; Code No. 13 survives in this letter only, no key and no other text

## Escalation

- [x] siblings: Short's re-enciphered extract of 27 Jul 1792 (016_1010-1012); 39 Code No. 10 documents (Founders notes) and six of them on the images; Founders "Code No. 13" = this letter only
- [x] clear-pages: none; Short's copy of 27 Jul 1792 carries no decoding, and Carmichael's letter has no decoded copy
- [x] known-keys: Code No. 11 table (jefferson1787) tried on Carmichael's Code No. 13: does not fit (597 freedom, 223 trouble)
- [x] print: Founders Online (PTJ 13, 24), Founders search for each number: no value found
- [x] key-rebuild: Code No. 10 values collected from Jefferson's interlinear (171) and checked for alphabetical bracketing (none: two-part code); Code No. 13 has no attested value to build on
- [x] retry: Carmichael's blotted 108 re-read at 2x; every open Short group searched in all transcribed Code No. 10 frames
