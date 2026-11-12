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

## Catalogue 650: five more letters (11 November 2026)

Nos. 18, 19, 24, 25 and 28 (Seville and Madrid, September 1814 to May 1815), from the frames catalogue 650 left open on M31 roll 14. The key is `key/codebook_M97_13_transcription.csv` under the block reversal, as above. One reader for all five; no second reader yet.

- `letters/1814-09-20_No18/`, `1814-10-27_No19/`, `1814-12-30_No24/`, `1815-01-06_No25/`, `1815-05-12_No28/`, each with:
  - `transcription.txt`: the numerals, made from full-resolution crops before decoding, with no key open. The hashes were frozen before decoding (11 Nov 2026, 10:43 UTC) and the files are unchanged since; `SHA256SUMS.txt` lists them. Notation is in each file's header: `[c]` hook, `[3]`/`[5]` strokes, `<` angle, `^` triangle, `|...|` words in clear, `{copy:reading}` variants. Headers that mention "REPORT.md" refer to our working notes, not to this bundle.
  - `line_by_line_decode.txt`: output of `scripts/decode650.py` on that transcription. Key values only: no mark rules, no context. No. 18 is decoded with one override, `112.10:69<[?]=69^`, the reading of two of its three copies.
  - `reading.txt`: the letter as sentences, with a summary. `*italic*` = Morris's words in clear, `[370]` = the unidentified sign after full stops, `[575.1060]` = groups left unread, `[?word]` = inference, `[word]` = supplied with no group for it. Notes on single readings follow the text.
  - No. 18 also has `collation_other_copies.txt` (Triplicate 0117-0118 and the copy on 0129 against the Duplicate, made before decoding).
  - No. 24 and No. 25 also have a clerk's decipherment from another copy (`clerk_decipherment_0196.txt`, `clerk_decipherment_0174.txt`) and the test against it (`test_vs_clerk_*.txt`).
- `scripts/` (Python standard library; run from any folder):
  - `decode650.py TRANSCRIPTION [LINE:OLD=NEW ...]` writes the line-by-line decode.
  - `score_interlinear.py TRANSCRIPTION CLERKTEXT PREFIXES` scores the key-only decode against a clerk's words, with 200 shuffled keys as the control. The commands for Nos. 24 and 25 are in its header.
  - `read_share.py` gives each letter's read share (`tests/catalogue650_read_share.txt`).

**Tests against the clerks' decipherments** (share of the clerk's letters matched in order by the key-only decode; 200 shuffled keys):

| Letter | Clerk's copy | Real key | Shuffled best | Shuffled median |
|---|---|---|---|---|
| No. 24, 30 Dec 1814 | frame 0196 | 0.904 | 0.342 | 0.215 |
| No. 25, 6 Jan 1815 | frame 0174 | 0.945 | 0.343 | 0.201 |

Neither test is fully blind:
- No. 24: the 0196 decipherment was not read before transcribing, but the frame was seen at low resolution while frames were being identified, and a few words were glimpsed. The clerk's text, on very dark film, was read after the decode was made, so its reading may lean toward the decode.
- No. 25: the 0174 decipherment had been viewed before the numerals on 0220-0221 were transcribed. The digits were read from 0220-0221 only, and none was changed for sense.

**Read share** (`scripts/read_share.py`: coded groups minus groups unread or read only by inference, over all coded groups): No. 18 0.981 (486 groups), No. 19 0.955 (156), No. 24 0.980 (205), No. 25 1.000 (98), No. 28 1.000 (90). The lists of unread and inferred groups are a judgment, set by hand from the readings.

**Reading review pending.** No `reading_review` is recorded for these five letters. A person has to read each `reading.txt` as sentences and record it in `profile.json`.

**Prior print.** Woolfley (2013) quotes or summarizes parts of Nos. 18, 19 and 24. What was searched, and with what result, is in `../NOTES.md`, section "Catalogue 650: five more letters".
