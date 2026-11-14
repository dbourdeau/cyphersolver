# morris1813: decoder re-run; read shares explained; the sign 370 is punctuation (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

`verify_dudout_20261114.py` (run from `targets/morris1813/`; part 3 imports `v10_relabel`, which needs numpy).

## Decoder

The script reads only `beling/key/codebook_M97_13_transcription.csv`, mapping each Morris number to its reading, and
each letter's `transcription.txt`. Compared group by group with `line_by_line_decode.txt`, 1,707 of 1,712 groups
agree. The 5 that differ are marks kept inside the published value (`smal[c]?`, `stru[c/t?]`) and the catchwords of
24 March 1815, whose layout the script does not parse. The decodes of Nos. 17 and 19 agree in full (53/53, 156/156).
No. 13 has no line-by-line file. Decoded from the second reader's copy A (frame 0084), it gives the reading word for
word ("so ur cape" for sour[?ce], "vis jur" for vis[?it], 1450 with its mark for Morris).

## Why v10 measures more than is recorded

The recorded `read_share` values come from `word_share.py`, which counts only the coded words of each letter. v10
(`v10_relabel.share`) counts every word of `reading.txt`, including the heading, the summary, the conventions and the
notes, all in clear. For No. 17 that is 231 words against 35 coded words, which is why v10 gives 0.971 against 0.914.
v10's figures for Nos. 13, 17 and 19 (0.966, 0.971, 0.966) are an artefact of this larger denominator; the recorded
figures are the right count by `word_share.py`'s rule. My own count reproduces all twelve of them exactly.

## The sign 370 is punctuation, not an unread word

`word_share.py` counts each `[370]` as a hole, that is, as an unread coded word. On the key sheet, 370 closes the
punctuation run 361 `,` 362 `;` 363 `:` 364 `.` 365 `!` 366 `?` 367 `—` 368 `( )` 369 `"` 370, and the numerical
sheet's reading of 370 is "[PARAGRAPH SIGN?]" (column `numerical_sheet_1057_first_reading`). In the letters, 19 of the
21 places transcribed have it right after 364 (`.`). Whatever its exact name, it is a punctuation mark, so the read bar
(words read as sense) should not count it.

| text | recorded (word_share.py) | 370 left out | effect |
|---|---|---|---|
| No. 13, 11 Apr 1814 | 0.946 (74 words, 4 holes) | **0.972** (72, 2) | crosses 0.95 |
| No. 17, 21 Jun 1814 | 0.914 (35, 3) | 0.941 (34, 2) | stays under |
| No. 19, 27 Oct 1814 | 0.943 (106, 6) | **0.962** (104, 4) | crosses 0.95 |
| No. 12 | 0.972 | 0.983 | |
| No. 18 | 0.958 | 0.971 | |
| Cevallos note | 0.962 | 0.980 | |
| No. 24 | 0.969 | 0.977 | |
| 24 Mar 1815 | 0.977 | 0.978 | |

Nos. 14, 25, 26 and 28 have no 370. With 370 left out, Nos. 13 and 19 would read; No. 17 stays read in part on
[?present] and [?prudent]. The class is not changed here; that is the maintainer's decision. Frame 0039
(`morris1813_reading.md`) was not recounted.

## Not done

- No image viewed. The cell of 370 on the M97 roll 13 numerical sheet (frame 1057) would show the glyph itself.
- hintze1903 was not done in this session.
