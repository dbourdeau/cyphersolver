# Blind second reading of the 1640 postscript (NA 1.04.02 inv. 1134 scan 583): alignment with the frozen transcription

## Who and how
- Reader 2: an isolated Claude subagent (Fable model; exact model id not recorded in its folder), working in its own folder with
  crops of scan 583 only. It never saw our transcription, KEY_v2, the decode, the glossed copy (scan 617) or any result.
- It froze `reader2/T1640_reader2.txt` (md5 d31ecd94971ef97870e952224d41b179) and `reader2/NOTES.md` (md5 98253589a4942134bbf0d589788c1d5e)
  at 2026-11-25T21:30:51Z (`reader2/FREEZE_reader2.txt`), stamped at once: Sectigo and FreeTSA 21:30:52 GMT, OpenTimestamps submitted;
  manifest sha256 3ab07449b3b23753eac26bfcbbc1b596447047822d2cdc9f966cec43b0e2b20c (`reader2/stamps/`).
- The reader's working crops (17 JPEGs cut from the NA IIIF image of scan 583) are kept locally and not filed here (archive images).

## Alignment (script, not by eye)
`python3 -I scripts/align_readers.py letters/1640/transcriptions/T1640_transcription.txt letters/1640/readers/reader2/T1640_reader2.txt "1640 scan 583"`
(difflib on number groups only; clear words `[..]` and letter-cipher words dropped from both). Output: `align_reader2_output.txt`.

- Frozen groups 57; reader 2 groups 57 (one marked doubtful).
- Matched 56 of 57 frozen groups: 56/57 = 98.25%.
- The only difference: token 13 group 2, frozen `0` (illegible, under an ink blot) against reader 2 `57?` (5 clear, 7 under the blot).
  Reader 2's 57 agrees with the contemporary interlinear gloss in the other copy (scan 617, letter m = 57 in KEY_v2), which it never saw.
- Word division: reader 2 marks two words split over a line end with no slash (L2/L3, L3/L4); the frozen transcription joins them the same way.

## Effect
- None on the figure of record: 9/11 tokens = 81.82% stands (first pass, frozen transcription). The blotted group stays a hole in the figure.
- The second reading supports the frozen transcription. It is not a human check: no person has compared the transcription with the image.
