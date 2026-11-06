# Work log, smolensk1633 (catalogue 1588)

All steps 5 Nov 2026, Claude Opus 5.5 in Claude Code, one session, at Daniel Bourdeau's request.

- 2026-11-05 access: catalogue entry and vetting read; szukajwarchiwach returns an Imperva shell to curl, so the unit page was opened in the user's Chrome; seven frames found, frames 4-5 hold the cipher; full-size `_max` images reached from the viewer iframe.
- 2026-11-05 access: localhost upload of the images stalled on a Chrome network prompt and the browser tool blocks base64 output; frame 4 downloaded with the user's permission, frame 5 read in the browser.
- 2026-11-05 literature: Nagielski, Miscellanea Historico-Archivistica XI (2000), fetched from AGAD and read: five Sokoliński letters printed, not this one, no key.
- 2026-11-05 transcription: first pass of f. 1r lines 1-15 from 2.5x screenshots (`draft_f1.txt`), crossed digits as one class; 22 sign types.
- 2026-11-05 statistics: sign frequencies and word lengths (mean about 6) fit a Polish simple substitution of about 20 signs.
- 2026-11-05 solver: free annealing on pl-1790 with homophones allowed: collapses onto a few letters (noise).
- 2026-11-05 hypothesis: glyph pairs (parity test): 47 of 116 words odd, ruled out.
- 2026-11-05 hypothesis: crossed digit = 10-19 (teen numbers): 19 types but too flat a frequency curve; solver noise; ruled out.
- 2026-11-05 solver: one letter per sign (maxdup 1): fragments wiadomosli, niemriialiez, niemami; key c=6, i=4, w=10 in place.
- 2026-11-05 crib: clear close has W.X.Mci; cipher group t0,D,7,6,4 occurs four times: w, X, M, c, i.
- 2026-11-05 hypothesis: б and the free cross are two letters (r, z): the repeated 12-sign word becomes nieprzyiaciel.
- 2026-11-05 transcription: 4.4x zoom shows two crossed 7s (z-shaped = p, top cross = m) and two free crosses (footed = z, plain = s).
- 2026-11-05 reading: line 1 reads Za gwałtownym i potężnym a barzo ścisłym opasaniem straża murów; key extended from lines 1-7 (g, ł, t, n, ę, b, h, k, u, f).
- 2026-11-05 transcription: frame 4 cut into 42 overlapping strips at 2.5x; all 35 lines of f. 1r re-transcribed in the finer classes (`transcription.txt`), reading each line as the work went.
- 2026-11-05 transcription: f. 2r cipher lines 1-2 read in the browser: prozbami, łzami oblewaiąc się ... odratowanie prosząc.
- 2026-11-05 verification: doubtful spots re-read at 3.5-5x; corrected przemysłów (f1r.06), przy uniżonych prozbach (f1r.12), iż on po rożnych (f1r.25), z uniżonemi (f1r.35).
- 2026-11-05 reading: key applied mechanically (`decipher.py`); per-word status in `reading.tsv`; 95.0% of 1,856 signs read as written, 99.4% with doubtful signs, 11 signs unread (one word, f1r.13).
- 2026-11-05 verification: docs/_validate.py on pl-1790: reading -2.521, random keys -5.747 (z 7.6), shuffled refit -4.171 (z 86.1): pass.
- 2026-11-05 literature: web search on phrases of the reading: no print or decipherment found.
- 2026-11-05 translation: English translation written (`translation_en.md`).
