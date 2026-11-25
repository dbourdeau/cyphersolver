# Test plans, audit of 17 Nov 2026 (written and hashed before any helper was started)

## Test L: second, independent look-up of the William Lee (15 Oct 1778) groups in Entick 1776
- Input: 14 column jobs (helper_lookup/jobs.tsv): the 12 distinct William Lee coordinates (169b21, 115b38, 92b27,
  259b32, 140a28, 426b28, 177a16, 415a10, 39b2, 305b30, 373a34, 253b21), 110a28 (the typed notes' reading of the
  fifth group) and the seed 80a16 (expected Cavalier, from the Arthur Lee key). The helper is given only page,
  column and a count_to 2-3 entries past the target line; it sees no letter, gloss, key or earlier look-up.
- Counting rule: the same as the 15 Nov listers (entries = new headwords at the left margin; run-over lines, running
  head and letter headings not counted; a line with two headwords is one entry).
- Score: for each of the 12 coordinates, the helper's Nth headword compared with the frozen look-up
  (output/lee_letters_1778_2026-11-15/work/lookup/lookup.tsv). Same headword (ignoring part of speech, case,
  long s, and spelling variants printed on the same line) = agree.
- Rule: seed must be Cavalier, else the run is reported as failed and not repeated. PASS if 12 of 12 agree. Each
  disagreement is reported as a miss, with both headwords; no second run.
- 110a28 is reported as information only.

## Test M: second blind reading of the figures in Montcalm to Bougainville, 21 Nov 1758 (AN 155AP/2 piece 25)
- Input: the page image only (helper_montcalm/image/page.jpg, sha256 29c04a3f...fbcff, = FRAN_0093_0816_L-medium).
  The helper makes its own crops at 3x in its folder, sees no transcription, code table or reading.
- Score: its groups aligned (difflib on the group sequence, per paragraph) with
  output/research_2026-11-12/montcalm_codes/transcriptions/T1758_AN155AP2_p25_figures_v2.txt (112 groups). A group
  agrees if digits and the "+" mark both match.
- Rule: PASS if at least 106 of 112 groups (95%) agree exactly. Every disagreement listed; for each, whether it
  changes a word of the reading in reading_1758-11-21.md. Specially reported: line 1.2 group 2 (674 vs 634) and line
  1.1 group 2 (666 vs 668). One run; misses reported as misses.
