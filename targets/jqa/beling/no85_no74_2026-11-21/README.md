# No. 85 (27 May 1812) and No. 74 (2 Nov 1811): working records, 21 Nov 2026

Contributed by Andrew Beling, with AI agents. Everything here was made by AI agents on 21 November 2026 between 03:10 and 04:10 US Eastern; no person has checked it. The result is written up in `../../NOTES.md` (section "No. 85 and No. 74, 21 Nov 2026") and in `../../texts/no85_*`.

Images: National Archives Catalog, record 188725601 (microfilm M35 roll 3), frames 0168, 0170, 0171, 0196, 0197; public domain, not committed.

| File | What it is |
|---|---|
| `trans_A/`, `trans_B/` | Two blind transcriptions of every code group on frames 0196 left, 0197 left, 0168 left and right, and of the clerk's decyphered sheet of No. 74 (frames 0170-0171). The two agents saw neither each other's work, nor a table, nor this repository's transcriptions, nor any print. Their notes list every doubtful digit. |
| `TRANSCRIPTION_merged.txt` | The two merged token by token, every difference shown. 796 tokens; same number read by both at 717; doubted by neither at 600. |
| `TEST_PLAN.md` | The test, written before any number was looked up in the code sheet (repository copy: three local paths replaced; the sha256 of the frozen file is in its first line). |
| `run_test.py` | The test script (repository copy: paths and table loader changed so that it runs here against `../../../morris1813/beling/key/codebook_M97_13_transcription.csv`; the sha256 of the frozen script is in its docstring). `python run_test.py run` rewrites `TEST_RESULT.txt` and the four detail files. |
| `TEST_RESULT_frozen_run.txt` | Output of the one frozen run (03:49). |
| `TEST_RESULT.txt`, `TEST_DETAIL_part*.tsv` | Output of the repository copy, run in this folder: the same figures line for line (the detail files differ from the frozen ones only in the spelling and capitals of the sheet values). |
| `pilot_control.txt` | Control calibration on 200 synthetic tables before the run (no real sheet value used). |
| `ERROR_GROUP_candidates.txt` | For 387, 1431, 1101: the sheet value of every number one step away, as the plan required. None was needed. |
| `verify/blind_0197.txt`, `verify/VERIFY.md` | A third agent's blind reading of frame 0197 and of the first eight groups of frame 0168, written before it opened the code sheet or the files above, and its comparison afterwards. |

## Test result

The code sheet against the Department clerk's own decipherment, number by number; a number is scored only where both transcribers read it the same and neither doubted it; pass mark 0.85 on both transcribers' readings; control: the sheet's values shuffled among its numbers 1,000 times.

| Part | Scored | Base A | Base B | Largest control |
|---|---|---|---|---|
| No. 85, frame 0196 left, the clerk's words over the groups | 112 of 139 numbers | 0.929 | 0.911 | 0.062 |
| No. 74, frame 0168, aligned with the clerk's separate sheet | 367 of 535 | 0.935 | 0.932 | 0.131 |

Both parts pass. The misses were not all gone through; those of part 1 are discussed in `../../NOTES.md`.

## Not included

The crops and the frames (public domain, about 35 MB); the file of sha256 sums taken before the run (it names local paths); the frozen plan and script themselves (their sha256 sums are given in the two repository copies).
