# WORKLOG: burr1808 (Claude Opus 5.5, session of 5 Nov 2026; started from the catalogue 2049 contributor task)

- 2026-11-05 access: Hamilton Education Program page for GLC01523 gave three PNGs (Page_1 1160x1400, Page_2 1400x1138, Page_3 1200x1400) and the transcript PDF; downloaded to the scratchpad, not committed.
- 2026-11-05 statistics: transcribed section A of img1 (80 words, 341 numbers, values 1-26 in comma groups, one group per word); flat frequencies, all 26 values; same 6-number word three times running.
- 2026-11-05 hypothesis: mono-alphabetic ruled out (doubled numbers inside words that cannot be double letters; 3,22 and 23,12 as two-letter words).
- 2026-11-05 statistics: IoC 0.0435 overall; period 6 gives 0.0618, period 12 0.0583, word-position columns no lift.
- 2026-11-05 solver: column chi-square against English letter frequencies at periods 3, 6, 12; period 6 (= 12) gives shifts 6 18 22 7 24 8 and section A reads ("below the black line is copy of my last by the schooner wolf"); period 3 fails.
- 2026-11-05 transcription: rest of img1 (sections B, C) and img2 from 2.4x line crops; superscripts with a caret kept as insertions, superscripts without a caret (A.06, A.07) left out after they broke the decode.
- 2026-11-05 reading: the same key reads every section from the first key place; two phase slips.
- 2026-11-05 solver: resync.py (Viterbi over words, lang en-modern) locates the slips: B.06 Burr omitted the s of "best"; img2 a rubbed four-number group before "hourly".
- 2026-11-05 verification: torn numbers at the right edge of B.07 and B.08 completed from the key (2[5], 2[4]) giving "impracticable", "for".
- 2026-11-05 control: control.py, Davis's text of Burr's 18 July 1804 letter (341 letters) enciphered with 20 random 6-place keys; the same solver recovers the key 20/20.
- 2026-11-05 identification: docket on img2 "Balt[imore]" and "1808"; pencil "1523A" on img1; content (Baltimore incog., long voyage, The Oaks, mari) dates the sheets to Jan-Feb 1808 and makes Theodosia the recipient; split from the July 1804 letter (burr1804), which uses another cipher.
- 2026-11-05 literature search: Davis 1837 (Gutenberg #7851) has no letters Oct 1807 - June 1808; Kline 1983 table of contents (archive.org search-inside, in the built-in browser; scripts get 403) has no Jan-Feb 1808 letter, only the editorial note "The Road to Exile" (vol. 2 p. 1040), not read; cryptiana and DECODE: nothing.
- 2026-11-05 hypothesis: no keyword behind the shifts (26 offsets and the reversed form).
- 2026-11-05 retry: the rubbed group at all six phases, 3 and 4 numbers: no word fits before "hourly"; left open.
- 2026-11-05 measure: decrypt.py --measure: 973 numbers, 969 give sense (99.6%).
