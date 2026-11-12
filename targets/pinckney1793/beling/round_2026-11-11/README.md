# Follow-up of 11 Nov 2026: Pinckney's letters of 1794, key v5, and a test on frame 0178

Andrew Beling, with AI agents. This folder adds to the bundle and changes no other file in it. `code16_key_v4.tsv` in
`../key/` is still the key behind the readings in `../../texts/`. Paths inside the scripts and the transcription READMEs
point to our working folders (`output/...`, `sources/raw/...`), as in the rest of the bundle. They show the method and do
not run from here.

## Letters (NARA M30 roll 2)

- **28 Jan 1794**, coded: frame 0196, with a clerk's interlinear on lines 1-4, 11 and 12 and the clerk's "Explication" on
  frame 0195. The other letter of 28 Jan, printed in ASP Foreign Relations 1:448, is in clear on frame 0194.
- **26 Feb 1794**: the postscript on frame 0208, in Code No. 16, with a clerk's interlinear.
- **1 Oct 1795**: the alignment to its printing in ASP Foreign Relations 1:536 is in `alignment_17951001_a.tsv` and `_b.tsv`.
- Frames 0196 (247 groups), 0208 (55) and 0178 (353) were transcribed blind by agents that had no key
  (`transcriptions/`). Each README lists its doubtful digits.

## Key v5 (`code16_key_v5.tsv`, 549 groups, sha256 in `code16_key_v5.sha256`)

Built from v4 by `scripts/build_key_v5.py` and frozen by hash before the test below. Every change, with its evidence, is in
`key_v5_changes.tsv`.

- **Added, 13 values.**
  - 1160 = comma, grade D. The Lear clerk wrote a comma stroke over it, and both printed commas on 0196 fall on it. This
    replaces the "ry" that v4 had already dropped as suspect.
  - Grade A: 1501 di, 1435 ent, 941 pre, 481 fine, 679 mine, 1235 past, 69 because, 1336 pres, 415 ume, 586 move,
    490 cure, 950 ia.
- **Changed, 3 values.**
  - 1366 ge → g ("insurgents", "sending").
  - 631 th → sixth (the clerk's "6th" over 631 alone on 0196).
  - 598 fourth → es ("acquiesce" at 0019L, Tunis ti-es).
- **Dropped:** 640 = es. Three words want "iv" there, which is not on Weber's element list, so no value is entered.
- **Grade B → D:** 1494 no, 779 plan, 144 place, 885 is, 1252 try (the clerk's whole word over a single group).
- **Still in conflict:**
  - 1162 = va does not fit "fluctuation".
  - 1368 is "stead" in one letter but falls inside "avoided" in another.
  - 1064 fits "Toulon" on 0196 as u, not ou. That weakens the St-ou-rt flag in `../README.md` section 5.
  - Pairs that claim the same element: 1501/1496 di, 1435/1438 ent, 380/38, 1524/1521. A 5/8 misreading in one member of
    a pair is likely.
- **Known slip in the file:** the `n` for 1160 is 16, but `key_v5_changes.tsv` says it should be 14. The two files also
  disagree on how many Lear strokes there are (14 against 12). The key file is left as it was frozen.

## Test on frame 0178: Pinckney, 25 Nov 1793 (`tests/`)

Written down first in `PREREGISTRATION_0178.md`, before any text of the letter was opened.

- **Key and groups.** The key was the frozen key v1 minus the 35 values Bourdeau had read partly from 0178. It was scored on
  the 290 groups where the blind transcription and Bourdeau's transcription agree (97% agreement), against the text printed
  in ASP Foreign Relations 1:328.
- **Result:** 0.724 (126 of 174 covered groups). The mean of 200 shuffled keys was 0.155 and the best was 0.264. **The test
  fails the 0.85 bar.** This result is in `0178_result_asp.json`.
- **A cause found afterwards.** The ASP text leaves out the last paragraph of the Explication, about a third of the coded
  text, so part of what the key decodes has nothing to match. This was found after the run and does not change the verdict.
- **Post hoc, not the declared test:** the same key against the clerk's full Explication on frame 0179, transcribed for this
  (`explication_0179_transcribed.txt`), scores 0.948 against a shuffled best of 0.287 (`0178_result_0179_posthoc.json`).
  0179 had already been used as a crib for some of Bourdeau's values, which is why they were removed from the test key.

## Group 447

It does not occur in 0178, 0196 or 0208, so it is still open.
