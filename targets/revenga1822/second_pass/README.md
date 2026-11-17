# Revenga 1822: second transcription pass (Andrew Beling, with AI agents; work of 12 November 2026, added 17 November 2026)

The second pass that NOTES.md names as the next step: a second transcription of the cipher on frames
T33-03-0055 to -0058, every difference from the first pass settled on the frames, and a test of the z sign. Nothing
in the folder above this one is changed; where this pass disagrees with `../transcription.txt`, `../reading.md` or
`../corrections.md`, the difference is stated here and in the dated section of `../NOTES.md`.

## What is blind and what is not

- **The second transcription was blind.** It was made from the four NARA frames (300 dpi, checksums in the project's
  local copy) by an AI agent that saw no key, decryption or earlier transcription. Its files were hashed when it
  finished (`blind/SHA256SUMS_blind.txt`) and are copied here unchanged.
- **The settling of the differences was not blind.** One AI agent compared the two transcriptions, looked at every
  difference on the frames and chose a reading, knowing both readings and the key. Where the shape could not decide,
  it chose from the sense, and says so (`method` = sense).
- No person has checked any of it.

## Files

- `blind/transcription_blind.tsv`: the blind transcription, 56 groups (B01-B56), with frame, line and the clear
  words before and after each group.
- `blind/clear_text.txt`: the blind transcription of the clear text, line by line, including the clear passages the
  first pass did not transcribe (0055 right lines 1-9, the cut last line of 0056 right, and the separate
  clear fragment on 0057 left).
- `blind/legend_signs.md`: the blind transcriber's conventions (how groups were cut, how ambiguous letter shapes were
  written) and its list of doubtful places. It is the frozen `legend.md` less one paragraph: the frozen legend also
  held a working note unrelated to the readings (a helper-script name clash in a shared scratch folder, which wrote
  two small error files into another target's working folder; no file of this letter was involved). The frozen
  `legend.md` (sha256 6319c71f9ee539bacd12801981dda4caae4841370d3629e7896275f2bf76fdec) is held by the project and
  can be supplied.
- `blind/SHA256SUMS_blind.txt`: the hashes written when the blind transcription was finished (unchanged; its
  `legend.md` line refers to the frozen file just described).
- `collation.tsv`: the 231 places where the two transcriptions differ (200) or agree only on a doubtful or
  alternative reading (31), and 5 places where both read alike but the frame shows otherwise; for each, frame and
  line, both readings, the settled reading, how it was settled (shape / sense / open) and what the frame shows.
- `transcription_settled.tsv`: the 56 groups as settled (B-numbering, with the first-pass C-id).
- `decryption_settled.tsv`: the settled groups decrypted mechanically with the key of `../key.txt`.
- `corrections_check.tsv`: the 108 corrections of `../corrections.md`, each checked against the settled text.
- `z_sign_test.md`: the z sign, the j sign, final z and k as stops, and the doubled g before -ción.
- `open_places.tsv`: the 15 places left open.

## Group alignment with the first pass

B01-B09 = C01-C09; B10 + B11 = C10 (the blind pass cut the run at a full stop: B11 = `zrph`); B12-B17 = C11-C16;
B18 = C17 + C18 (one run from the last line of 0057 right onto the first line of 0058 left); B19-B54 = C19-C54;
B55 + B56 = C55 + C56 (cut at a different place). The two transcriptions agree on 2,293 of 2,532 signs (0.906),
counted with ll as two letters.
