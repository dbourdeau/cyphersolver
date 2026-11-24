# No. 85, 27 May 1812: the "three lines of cypher not decyphered" (no85_three_lines.txt), decryption

NARA M35 reel 3 frame 0197, left leaf: one group at the end of the line "...the English meaning of neutrality," and the three lines after it, 35 groups, two of them cut by the binding gutter (116x has its last figure blotted, 9x is cut); Ford 4:339 "[here three lines of cypher not decyphered]". Transcription: two blind readings merged, 21 Nov 2026 (`beling/no85_no74_2026-11-21/`). First block: the State Department code sheet (NARA M97 roll 13 frames 1056-1057, Weber WE028; `key_we028_no85.tsv`) applied group by group, unedited: one value per group in the order of the transcription, `{n}` = no value (a number not on the sheet, or digits lost). Second block, for comparison: `python render.py no85_three_lines.txt`, the rebuilt `code_table.tsv` (? = grade M or I value, CAPS X = digit lost). Status and note for every group: `we028_no85.tsv`. The reading follows the sheet.

## Group by group (code sheet)

```
and
the sw ed ish mean ing of it is to be ex {116x} ed
by the hope of be ing is dem ni fied {1626} nor way {9x}
the lose of fin la nd
```

## Group by group (render.py, code_table.tsv)

```
and
the sw ed ish mean ing of it is to be ex 116X ed
by the hope of be ing is dem? ni fied? {1626} nor without? 9X
the sum of Fin la nd?
32 of 33   by grade: H=25 C=3 M=3 I=1
```
