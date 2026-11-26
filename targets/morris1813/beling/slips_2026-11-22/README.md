# The three one-digit places, checked on the film (22 Nov 2026)

This answers the "workable next step" in `../../NOTES.md` (claims review, 14 Nov 2026). That step asked whether three groups are really on the page before the one-digit rule (README Conventions, 14 Nov 2026) is applied to them:
- No. 13: 510 where *sour-ce* wants 516 ce;
- No. 13: 146 where *vis-it* wants 140 it;
- No. 24: 593 where *Sir* wants 598 si before 813 R.

Andrew Beling did this with AI agents. The frames are NARA RG 59, M31 roll 14 (Despatches from U.S. Ministers to Spain). The crops were cut from the catalog's images; they are not committed, and each can be cut again from its pixel box (`readings.tsv` and below):
- [0084](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-014/M31-014-0084.jpg)
- [0088](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-014/M31-014-0088.jpg)
- [0196](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-014/M31-014-0196.jpg)
- [0205](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-014/M31-014-0205.jpg)
- [0220](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-014/M31-014-0220.jpg)

## How

1. **First reading.** The coordinating agent located each group and cropped it. It compared the doubtful figure with the same figures elsewhere on the same line.
2. **Second reading, blind.** A separate helper agent got only the seven tight crops (A to G) and the question "what number is written". It was not given the candidates.
3. **Third reading, for 510 only.** The helper's answer for 510 differed from the first reading. So a second helper, also given no candidates, transcribed every number on two strips of the line (H and J). The strips keep the comparison figures.

`readings.tsv` gives each reading with its crop box. The tight crops are enlarged 3.5 to 5 times. The strips and the 0196 view are not in the TSV. Their boxes in pixels of the catalog image (x0, y0, x1, y1) are:
- H, frame 0084: 1560,1950,2300,2075 (enlarged 2 times);
- J, frame 0088: 1290,1270,1900,1360 (enlarged 2 times);
- K, frame 0196: 2700,180,3500,450 (actual size).

## Result

| Group | Frame, place | First reading | Blind readings | Manuscript has |
|---|---|---|---|---|
| 510 (No. 13) | 0084, coded line 1, after 1349.1190 | 510 | tight crop: 576; line strip: 510 (high) | 510 |
| 510 (No. 13) | 0088 left leaf, coded line 1 | 510 | tight crop: 570; line strip: 510 (high) | 510 |
| 146 (No. 13) | 0084, coded line 2, after 1176 | 146 | 146 | 146 |
| 146 (No. 13) | 0088 left leaf, coded line 2 | 146 | 146 | 146 |
| 593 (No. 24) | 0220, first group of the text | 593 | 593 (high) | 593 |
| 593 (No. 24) | 0205, right page, first group | 593 | 593 | 593 |
| 593 (No. 24) | 0196, right page, first group (very dark) | 593 | 593 (2 possible for the last figure) | 593 |

**510.** In this hand a 6 has a tall stem rising above the other figures, as in 76, 766, 1060 and 126 on the same line. A 0 is a small oval. The last figure of 510 is a small oval at the height of the 0s of 1190 and 1060.

On the tight crops the blind reader took the middle stroke for a 7 and the last figure for a 6 (576) or a 0 (570). Those crops cut off the figures beside the group. On the line strips the second blind reader read 510 on both copies. It noted that the 0 matches the 0s of 1190 and 1060 and that the 1 does not descend like the 7 of 76.

We take 510. This rests on the first reading and one blind reading of the strips, not on two agreeing tight-crop readings.

**146.** The last figure has the 6's tall stem on both copies.

**593.** The last figure is an open two-lobed 3, like the 3 of 813 next to it. It is not the closed 8 of 813.

**The clerk on 0196.** The clerk's decipherment begins "I am inform[ed]" over 101. Nothing is written over 593.813.367 (view K), so the clerk did not decode the opening either.

## Consequence

The three groups are the writer's slips on every copy, not misreadings here. The one-digit rule applies:
- the key is the surviving sheet;
- one digit changes;
- the other groups of the word are read from the key;
- the corrected groups spell the whole word: so-ur-ce, vis-it, si-R.

The readings now have `sour{+ce}`, `vis{+it}` (No. 13) and `{+Si}r` (No. 24).

Recounted with `../../word_share.py`:
- No. 13: 72 of 72 (1.000; was 0.972).
- No. 24: 128 of 130 (0.985; was 0.977).
- The thirteen texts: 2,609 coded words, 62 holes, 0.976 (was 65 holes, 0.975). The twelve letters have 2,259 words and 52 holes. Frame 0039, counted by hand, is unchanged at 350 words and 10 holes.

The class does not change. No. 17 stays at 0.941, so the target stays read in part.

`../scripts/read_share.py` is the group count of the catalogue 650 letters from 11 Nov 2026, superseded by `word_share.py`. It still lists 593.813 as inferred and was not changed.

The frames are NARA microfilm images, public domain as US federal records; the crops are kept out of git.
