# Code No. 16 beyond Pinckney's London letters: attachment bundle

Contributed by Andrew Beling, with AI agents (Claude Fable 5.2, with Claude Opus 5.5 subagents), November 2026.
It adds to `targets/legation1788/` (Code No. 16, Thomas Pinckney's London code of 1793) and does not change any file
outside this folder. The small edits it proposes to the target's own files are in `proposed_changes.patch`, to apply
or not.

Moved on 11 Nov 2026: when Code No. 16 was split out of `targets/legation1788/` into its own target, this bundle went
with it to `targets/pinckney1793/beling/`. `../` in this file and in the scripts now means `targets/pinckney1793/`, which
holds `key.tsv` (the 262 Code No. 16 rows only; the Code No. 10 rows stayed in `targets/legation1788/key.tsv`),
`reading_pinckney_17930828.tsv` and `transcription/pinckney_m30.tsv`. File names with `legation1788` in them, `CHECKS.txt`
and `proposed_changes.patch` (applied on 11 Nov 2026, against the old paths) are kept as they were; `reading.tsv`, `NOTES.md`,
`profile.json` and `make_profile.py` named below are the files of the folder as it then was.

Paths such as `output/...`, `sources/raw/...` or `scripts/...` inside the copied READMEs and the scripts in `key/scripts/`
refer to our working folders, not to this bundle. Those scripts are included to show the method and do not run here.
The scripts in `tests/`, `comparison/`, `corrections/` and `decodes/` read only this bundle and `../` and do run
(`python3 <script>` from this folder; outputs are in `CHECKS.txt`). No images are included; links are below.

## 1. What the code is

Code No. 16 is the code Weber (1979, p. 155) calls the "663" code (663 = the) and lists as "not located": used by
Pinckney in London and sent by Rufus King to Robert R. Livingston in January 1802. We find the same code in:

| Letter | Where | How the words were obtained |
|---|---|---|
| Pinckney, Madrid and San Ildefonso, 21 Jul and 11 Aug 1795, re-enciphered in "Cypher 2d" and enclosed on 27 Aug 1795 | NARA M31 roll 7, frames 0018-0019 | George Taylor Jr.'s interlinear |
| Pinckney, San Ildefonso 1 Oct, San Lorenzo 28 Oct, Paris 18 Dec 1795 | M31 roll 7, frames 0020-0021, 0111, 0134-0135, 0177 | clerk's interlinear; marginal decipherment on 0134-0135 |
| William Eaton to the Secretary of State, Tunis, 25 May 1801 | NARA T303 roll 2, frames 0048-0049 | Wagner's interlinear (copy A, frame 0049) |
| Eaton's coded copy of the Bey of Tunis to Jefferson, 8 Sep 1802, enclosed in Eaton to Madison 9 Oct 1802, with Eaton's postscript | T303 roll 2, frames 0299-0303 | body aligned by hand to the 1802 English translation (American State Papers, Claims, p. 331; Naval Documents, Barbary Powers II:269); postscript from the Madison editors' decipherment |
| Eaton to Madison, 22 Oct 1802 | T303 roll 2, frame 0320 | two blind transcriptions of the numerals; a contemporary interlinear on the page |
| Tobias Lear to Madison, [Jan] 1813 | Library of Congress, James Monroe Papers, reel 5 (mss33217.005), images 981-982 | Graham's interlinear |

What was known before, as far as we could find:

- Weber links Pinckney's London code to King and Livingston (1802). Tomokiyo (Cryptiana) identifies it by 663 = the only.
- The Madison Papers editors read Eaton's 1802 postscript and Lear's 1813 letter "using a key from the Lear family papers"
  (Founders: Madison/02-04-02-0007 and 03-05-02-0448). So the Eaton-Lear identity is implicit in their edition; the key
  itself was never printed. Cipher papers from that family were sold at auction in 2010 to an unnamed buyer.
- The Jefferson Papers editors verified Pinckney's 1793 letters with "partially reconstructed Code No. 16" (unpublished;
  size not stated).
- This repository's `key.tsv` (262 Code No. 16 values, 27 Oct 2026) was the first public table of the code.

What we have not found anywhere: a statement that the London code, the Madrid 1795 use and the Eaton/Lear code are one
code. We claim no more than that. The code was not lost (an original key existed in private hands), and we are not
the first to reconstruct part of it.

## 2. Witnesses (`witnesses/`)

Each folder has the transcription as made, with its own README (method, doubtful digits, conventions). Numerals were read
from the images; nothing in a transcription was filled from a key.

- `tunis_1802-09-08_enclosure/`: `tunis_word_spans.tsv` (468 groups aligned to 322 words; flag `x` where the print
  differs from the cipher, `u` uncertain, `d` date line), `tunis_postscript_spans_v2.tsv` (Eaton's postscript, 56 words,
  re-read with his punctuation), the comparison with keys built by others (`tunis_external_comparison.tsv`,
  `summary.json`: of 44 direct values also in `../key.tsv`, 43 agree and 1 is good/goods), the held-out check on Lear
  (`heldout_lear.json`: 48 of 50, shuffled best 0.44), and the 1802 printed translation used as the crib
  (`crib_printed_translation_1802.txt`, a 1940 US Government printing, with `crib_acquisition.json`). The alignment was
  made with the crib in view, so it is not a blind test. Eaton's marks: a period ends a word, a dash joins the groups
  of one word, a caret under a group doubles its last letter, + inflects.
- `eaton_1802-10-22/`: two blind transcriptions (A and B) of the coded passage of 22 Oct 1802. The interlinear words on
  the page are kept in the two `*_SPOILER` files.
- `eaton_1801-05-25/`: both copies, 196 groups, with Wagner's interlinear on copy A.
- `lear_1813-01/`: a fresh transcription (354 groups) from the Library of Congress master TIFFs, and the differences from
  an earlier transcription of ours (`diff_vs_6nov.tsv`, 36 numerals corrected).
- `pinckney_1795_madrid/`: the "Cypher 2d" enclosures (283 groups with Taylor's words), and Pinckney's covering letter of
  27 Aug 1795, which explains the re-encipherment.
- `pinckney_1795_oct-dec/`: 224 further groups of 1795 and a survey of M31 roll 7 and M30 roll 3 (`frame_survey.tsv`).

Images (public, NARA catalog media server and Library of Congress):

- T303 roll 2: `https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T303/T303-02/T303-02-NNNN.jpg` with NNNN = 0048, 0049, 0299-0303, 0320
- M31 roll 7: `https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-007/M31-007-NNNN.jpg` with NNNN = 0017-0021, 0111, 0134, 0135, 0177
- M30 roll 2 (this target's frames): `https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M30/M30-002/M30-002-NNNN.jpg`
- Lear: `https://www.loc.gov/resource/mss33217.005/?sp=981` and `?sp=982` (masters: `https://tile.loc.gov/storage-services/master/mss/mss33217/005/0900/0981.tif`, `.../0982.tif`)

Editions (cited, not copied): Eaton 25 May 1801, Madison/02-01-02-0296; 9 Oct 1802, Madison/02-04-02-0007; 22 Oct 1802,
Madison/02-91-02-0526; Hammuda Bey to Jefferson, 8 Sep 1802, Jefferson/01-38-02-0321; Lear [Jan 1813], Madison/03-05-02-0448;
Pinckney 21 Jul 1795, Washington/05-19-02-0013-0001 (all at `https://founders.archives.gov/documents/`). Pinckney Statesmen
(Rotunda): PNKY-01-02-02-0004-0125 (23-27 Feb 1795), -0004-0243-0001 (3 Apr 1795), -0002-0976 (17-23 Dec 1793), -0003-0076 (28 Jan 1794).

## 3. The key (`key/code16_key_v4.tsv`)

537 groups (sha256 `e18775d8...`), after the corrections at the end of this README (536 before them). Columns: group, value,
grade, n, sources, on_element_list.

| Grade | Groups | Meaning |
|---|---|---|
| D | 158 | one unmarked group under one word, in a contemporary interlinear or the Tunis crib (n = times seen) |
| S2 / S1 | 81 / 111 | the only element of Weber's word list that fits every word the group occurs in (S2: two or more words; S1: one word, weaker) |
| A | 125 | read off by aligning bare Pinckney frames of this target's `transcription/pinckney_m30.tsv` (0106-0107, 0135-0136, 0183, 0196, 0305, 0317) to the printed editions |
| B | 62 | from this repository's `key.tsv` (commit c14c822, unchanged at ebb365f): a list element that no other group owns. These are Bourdeau's values, not ours |

- Word list: `key/weber_1600_family_vocab.txt`, the union of the elements of WE023-WE028 as printed by Weber (1979),
  from the text layer of the book. The premise, tested and not proven, is that Code No. 16 was made on the same printed
  form of about 1,600 elements; 158 of 158 direct values are on the list.
- Build: `key/scripts/code16_merge_v3_2026_11_10.py` (D, S, B; uses `code16_frame_solver_2026_11_10.py`), then
  `code16_align_cribs_2026_11_10.py` (A). Summaries: `code16_key_v3_summary.json`, `code16_alignment_summary.json`,
  `code16_aligned_values.tsv`; words that would not segment: `code16_v3_unsegmentable.tsv`.
- Calibration of A: with a tenth of the known key hidden, ten times, the aligner proposed values for 147 of 260 hidden
  groups and 144 were right (0.98; an earlier run gave 0.976). The hidden groups are commoner than the ones actually
  solved, so the real error rate of the A values is likely higher.
- Known weak values, found while preparing this bundle: 1505 = ceive (S1) was wrong; `key.tsv`'s 1505 = "." (full stop)
  is right: in the decodes it falls at sentence ends again and again. 1160 = ry (A) sits in the same places and is
  suspect (11 Nov follow-up: 1160 is the comma; `round_2026-11-11/`). 1258 = y and 1374 = r are attested (see section 5) but were missing. All four are corrected in v4 (last section).

## 4. Tests (`tests/`)

The key was frozen before testing: `frozen_key_v1.tsv` (311 groups, sha256 `e88b2c7f...`, as stated in
`PREREGISTRATION_eaton_1802-10-22.md`). Rule (Dudout's): pass at 0.85 or more and 0.30 above the best of 200 shuffled keys.

| Text | New text? | Score | Shuffled best | Result file |
|---|---|---|---|---|
| Eaton, 22 Oct 1802 | no: the passage repeats the 9 Oct postscript | 0.898 (44 of 49 covered groups); blind readers agreed on 85 of 92 | 0.224 | `eaton1802-10-22_frozen_key_v1_result.json` |
| Pinckney 1795, M31/7 frames 0018-0021 | yes | 0.886 (93 of 105) | 0.105 | `pinckney1795_frozen_key_v1_result.json`: pass |
| Eaton, 25 May 1801 | yes | 0.80 (48 of 60) | 0.10 | `eaton1801_frozen_key_v1_result.json`: below 0.85 |

- Eaton 22 Oct: the first run gave 0 for the real and the shuffled keys alike, because the edition passage was taken from
  the file's header instead of the coded passage. The extraction was fixed and the same measure run again; both are
  recorded in the result file. The edition text itself is not copied (the field gives the URL).
- Eaton 1801: of the 12 misses, four are right syllables whose word runs on under the clerk's dashes (ad in Morad, ro in
  squadron, ni in Tunis, ti in chastised), which the declared rule does not credit; four are whole-word values from
  `key.tsv` (541 another, 1453 said, 312 sense, 1015 spend). It was not re-scored.
- Pinckney 1795: 11 of the 12 misses are values the frozen key took from `key.tsv` (541 another and 1122 we, where Taylor
  wrote "anxious" over 541 1122 753 698, an-x-i-ous; 411 compliance under "complied"; 982 arrangements inside "guarantee"). Three of those
  (936 "accede") are our doing: the frozen key dropped the brackets of `ac[cede]`.
- `rescore_frozen_key.py` re-implements the 1795 and 1801 scoring from this bundle's files (the original runs were not
  kept as a script). It gives 0.879 (94 of 107, shuffled best 0.065) and 0.797 (51 of 64, shuffled best 0.125): the
  same verdicts, slightly different counts, because the units are rebuilt from the span files.

## 5. Against `../key.tsv` and the 28 Aug 1793 reading

`comparison/compare_with_legation1788_key.py` compares key v4 with the 262 Code No. 16 rows of `../key.tsv` at ebb365f (last changed 27 Oct 2026)
(`v4_vs_legation1788_key.tsv`, `.json`; the earlier comparison at c14c822 is `key_v2_vs_legation1788_c14c822.json`).

- Independent values (D, S1, S2) against his: D agree 64, D a syllable of his word 4, D differ 0; S agree 20, syllable of
  his word 23, differ 10. A values were only sought for groups that key v3 did not hold, and v3 already held his
  list values as grade B, so A never simply agrees with him.
- 34 groups carry a whole word in `key.tsv` where our value is a syllable of it. 14 of them he already marked as
  pieces ([..] or a group span). 20 are unmarked, e.g. 541 another (an), 982 arrangements (ar), 1571 structions (struct),
  1453 said (sa), 523 full (ful, Eaton's caret doubles the l); for 6 of these his `other_readings` column already lists
  our value. 13 more differ outright, e.g. 675 information (ly), 1005 is (te), 1075 part (ant), 1122 we (x: an-x-i-ous in Taylor's 1795 interlinear). Our earlier count of "62" such entries does not reproduce and should not be used.
- 329 of the 537 groups are not in `key.tsv` at all.
- The counts above and `v4_vs_legation1788_key.*` are from the corrected v4 (537 groups), regenerated on 11 Nov 2026.
  Against v4 before the corrections (536 groups) 1505 was a difference and 1374 was missing; the 329 are unchanged.

`corrections/pinckney_17930828_points.tsv` takes the 58 groups of `../reading_pinckney_17930828.tsv` one by one (the
script stops if a row no longer says what the proposal assumes):

- 234 = time (Lear 1813, twice; Tunis 1802) and 501 = secret (Lear 1813, once): direct values in other letters of the code.
- "Sir" is 1328 1374 (si-r: Tunis "Mr" = 1018-1374, "Sir" = 1328-1374; Lear re-si-dent; 1795 si-tu-ation), so
  "Charles" is 672 alone, not 1374 672.
- 668 = at (Eaton 1801 three times, Pinckney 1795, Tunis). ?55 668 800 cannot spell [Dunda]s; the name stays open.
  `key.tsv`'s 668+ = ted (0183) fits at + inflection.
- 675 = ly (seven words in Tunis and Lear); 1010 = tin (dis-tin-guish..., three words), so destination is des-tin-ation
  (1228 1010 1181).
- 447 is in none of the witnesses and stays open.
- Flagged only: 1064 = ou in Tunis (w-ou-nd, one word), which would make 1565 1064 942 St-ou-rt, not St-ua-rt.
  (Weakened 11 Nov: 1064 fits "Toulon" on M30 frame 0196 as u; `round_2026-11-11/`.)

## 6. Pinckney frames without a decoding (`decodes/`)

`decode_undecoded_frames.py` applies key v4 to the groups of `../transcription/pinckney_m30.tsv` that have no
contemporary decoding: 0106-0107 (5 Jul 1793), 0135-0136 (15 Aug 1793), the line below the signature on 0148, 0178
(25 Nov 1793), 0196 ll. 5-10, 0305 (Feb 1795), 0317 (3 Apr 1795). This repository reads none of them; the editions print
plaintexts for most (Bankson's clear copies, the 0179 Explication, the Pinckney Statesmen staff).
**Decoded, not read**: `m30_undecoded_v4.txt` is a stream of key values with no word division and no editing.

| | groups | any v4 value | without A | without A and B |
|---|---|---|---|---|
| all nine frames | 1,982 | 0.810 | 0.685 | 0.621 |

These figures, `coverage.tsv` and `m30_undecoded_v4.txt` are from the corrected v4 (regenerated 11 Nov 2026; before the
corrections they were 0.806, 0.674 and 0.618).

Per frame in `coverage.tsv`. The A values came from aligning these same frames to the editions, so only the last column
is independent of them. Sample, 0317 as decoded: "a [988] [592] alliance between russia AUSTRIA and GREATBRITAIN is [258] conclude"
(upper case = grade A).

## 7. The proposed edits (`proposed_changes.patch`)

Made with `git diff` against origin/main 6897c12b. `targets/legation1788` is unchanged at ebb365f, where `git apply --check`
passes and the profile stays valid with the patch applied (`CHECKS.txt`, re-run). Daniel's files in this worktree were
reverted after the diff. It changes:

- `reading_pinckney_17930828.tsv`: 12 rows (234, 501, 923 twice, 1328, 1374, 672, ?55, 668, 1010, 1181, 675) with the
  evidence above, and the header's definition of H extended to "another letter of the same code". Counts go from
  H 30, E 23, C 4, O 1 to H 39, E 17, C 0, O 2.
- `reading.tsv`: regenerated by `make_reading.py` from it (no other change).
- `NOTES.md`: one pointer bullet under the Pinckney findings, and the line "They stay conjectures" qualified.
- `profile.json` and `make_profile.py`: two credit entries for `ajbeling` (identification; key corrected), added to both
  so that a re-run of `make_profile.py` keeps them.

Not in the patch, for the maintainer: re-running `make_profile.py` after it would move the Pinckney letter to read_share
0.966 and state "read", but it would also revert the Carmichael summary added to `profile.json` in 44eeed68, which
`make_profile.py` does not carry. The Pinckney summary, `texts/pinckney_17930828_reading.txt` ("[Dunda]s", "Generals
Stuart and Dundas"), the "Remaining gaps" bullets and `outcome.gaps` would also need a hand edit. Whether
`outcome.provenance` should become "mixed" is the maintainer's call.

## Checks

`CHECKS.txt`: `docs/_check_profile.py legation1788`, `docs/_check_reading.py legation1788` and the reading-check
workflow step, before and after the patch (after: in the worktree and in a separate scratch copy), plus the output
of the bundle's scripts. `SHA256SUMS.txt` covers every file of the bundle except itself.

## Corrections made 11 Nov 2026, after the comparison with the current key.tsv

In `key/code16_key_v4.tsv` (now 537 groups): 1505 = "." (your value; our "ceive" was wrong) kept as grade B; 1160 = "ry" removed
(suspect); 1258 = y and 1374 = r restored (both attested in the Tunis letter: Bey = 1517-1258, Sir = 1328-1374, Mr = 1018-1374).
The frozen test key (`tests/frozen_key_v1.tsv`) and the test results are unchanged. The comparison (section 5) and the
decodes (section 6) were made before these corrections and were not regenerated.

## Follow-up of 11 Nov 2026 (after PR #399 was merged)

`round_2026-11-11/` (its README gives the detail) adds:
- blind transcriptions and alignments of Pinckney's coded letter of 28 Jan 1794 (M30 frame 0196) and postscript of 26 Feb
  1794 (frame 0208);
- key v5, 549 groups: 13 values added, among them 1160 = comma; 3 changed (1366 g, 631 sixth, 598 es); 640 dropped.
  This corrects four values of v4 above: 598, 640, 1366 and 631. v4 stays as it is, because the readings were made with it;
- a declared test on frame 0178 (25 Nov 1793) that **failed**: 0.724, against a shuffled best of 0.264. A post hoc check
  against the clerk's full Explication on 0179 gives 0.948.

