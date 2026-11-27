# Blind second reading of the 23 Jan 1643 letter (NA 1.04.02 inv. 1141 copy 2, scans 0901, 0902, 0905, 0906): alignment with the frozen transcription

## Who and how
- Reader 3: an isolated Claude subagent (Fable model; exact model id not recorded in its folder), working in its own folder with the four
  NA IIIF page images and its own enlargements only. It never saw our transcription, KEY_v2, KEY_B_v1, the decode, the glossed copy 1
  (scans 0886, 0890) or any result. It did no web search.
- It froze `reader3/T1643_reader3.txt` (md5 d5dd27fe36c8e9440a5a94263d514970) and `reader3/NOTES.md` (md5 2e1dd3d2b324bb5f8638f7062a444985)
  at 2026-11-25T21:44:49Z (`reader3/FREEZE_reader3.txt`), stamped at once: Sectigo 21:44:49 and FreeTSA 21:44:51 GMT, OpenTimestamps
  submitted; manifest sha256 03a8221387f9faacc1a3d79bb3ff1dca4184d83d63ebdf64fa44fbe1848eaa49 (`reader3/stamps/`).
  `COUNT_reader3.txt` was written by script after the freeze and is in the same stamped manifest.
- The reader's images (page images and enlargements from the NA IIIF server) are kept locally and not filed here (archive images).

## Alignment (script, not by eye)
`python3 -I scripts/align_readers.py letters/1643/T1643_transcription.txt letters/1643/readers/reader3/T1643_reader3.txt "1643 scans 901-906"`
(difflib on number groups only; clear words, `<letter words>` of the frozen file and `[LC: ..]` of the reader dropped). Output: `align_reader3_output.txt`.

- Frozen groups 86; reader 3 groups 89 (three marked doubtful).
- Matched 85 of 86 frozen groups: 85/86 = 98.84%.
- 1 disagreement: 902.4 group 3, frozen `10` against reader 3 `16`. This is already a listed doubt in NOTES.md ("could be 16"); copy 1
  writes 16, and the KEY_B_v1 reading of the run (2 = t, 12 = o, 16 = n: 'ton..', see the NOTES.md doubts) also favours 16. The frozen 10 stays in the figure of record.
- 3 extra numbers in reader 3, all its own doubtful signs inside letter-cipher words that the frozen transcription, by its convention
  set before the decode, writes as part of the letter word: `[LC: m]8?` = frozen `<m8>` (901.2); `[LC: mtddbi]6?` = frozen `<mtddbi6>` (901.9);
  `[LC: m]6?` = frozen `<m6>` (906.9). Reader 3 itself gives letter alternatives for all three ('o', 'b', 'b').
- Count check: 86 frozen = 85 matched + 1 replaced; 89 reader = 85 matched + 1 replaced + 3 inserted.

## Effect
- None on the figure of record: 59/86 groups = 68.60% stands (first pass, frozen transcription).
- The second reading supports the frozen transcription. It is not a human check: no person has compared the transcription with the image.
- Exposure: our 1643 transcriber had KEY_v2 in context (disclosed in METHOD_1643.md); reader 3 did not, so this alignment is the
  control on that exposure for the number groups.
