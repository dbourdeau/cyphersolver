# Anthony Morris's coded despatches: attachment bundle

Accompanies a contribution to catalogue 650 of dbourdeau/cyphersolver. Methods are in the issue text. Paths such as `sources/raw/...` inside the JSON files and scripts refer to our working folders, not to this bundle; image names there are our crops of the NARA frames (M31 roll 14: https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-014/M31-014-NNNN.jpg).

## Contents

- `key/codebook_M97_13_transcription.csv`: the surviving copy of the State Department code at NARA M97 roll 13, frames 1056 (alphabetical sheet, with printed instructions) and 1057 (numerical sheet), printed by Weber (1979) as WE028. It gives all 1,600 entries with the number each has in Morris's reversed copy. The numerical sheet was read for all entries; the alphabetical sheet for 1-800 and about 90 others. A modern museum table was compared after a frozen first pass. Seven entries are blank; eleven have readings that disagree. It is a working transcription, not a critical edition. 1570 was corrected to "occur" on 30 October 2026.
- `letters/<date>/reading.txt`: the reading as sentences, with a short summary. `[?word]` is an inference; `[370]` is an unread group. These readings are reconciled across readers, so they can differ in small ways from either reader's own file, which predate the 1570 correction. One reader's file has "doubloons" at 899 in the 4 April letter; the other and the second copy have 894 (dollars).
- `letters/<date>/first_reader_*`, `second_reader_*`: numerals, line-by-line decode and digit checks. The two short letters share files.
- `letters/1814-04-04_No12/second_copy_*`, `collation_two_copies.txt`: the second copy of the 4 April cipher.
- `letters/1815-03-24/`: one reader. `transcription.txt`, `line_by_line_decode.txt`, and `reading.md` with the collation of its two copies.
- `frame39/`: working clear texts of the 4 January 1814 cover and the Louisiana proposal (frames 59-64). They normalize some spelling and are not diplomatic editions.
- `tests/`: the clerk-word test (`reversal_test_226_spans.csv`, `reversal_test.py`), the stroke test, and the blind test. The scripts expect our working folders and are included to show the method. The blind test's clear text (M31 roll 14 frames 40-45) and numerals (`literal_reviewed_v4`) are not bundled.

The 1,679-row alignment of the proposal is left out because it still has misread numbers.
