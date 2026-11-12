# PREREG — catalogue 1554, c. 114r (letter 2), known key applied unchanged — 12/11/2026, Opus 5.5

Frozen BEFORE the key is applied by program to the transcription. Honest limit: the transcriber knew the table
(key_frozen.tsv, WAINUT/LcCompany, PR #221) while reading shapes, as WAINUT's own transcribers did.

- Key: targets/ercole1544/key_frozen.tsv (origin/main), UNCHANGED. Built by WAINUT from c. 103r / c. 104r only.
  Nothing of c. 114r was ever used to build or adjust it -> the whole page is held out (about 420 signs >= 300).
- Text: transcriptions/t0114r_pass1.txt, SHA-256 89ed7126...64fa (frozen 18:45 CET), decoded mechanically:
  letters by the table, numbers by the table's code list, nulls 24 25 27 dropped, ? and m and undecided [a/b]
  take their first option, unknown codes become '#'.
- ONE measure M: share of decoded plain letters covered by Italian words of length >= 3 in the lexicon
  (words with frequency >= 3 in lm/it_nunz_clean.txt), by dynamic programming maximising coverage.
- Controls: 200 random permutations of the 20 letter values of the table (same seed list 0..199, codes kept),
  applied to the same transcription.
- Thresholds fixed now: PASS if M > max(controls) AND M >= 0.50. Otherwise the key is not confirmed on this page
  and no reading is claimed.
- Reading (only if PASS): sense-based resolution of look-alike signs (c/e, g/q/z, n/r/u, f/s, x/r) is logged per word
  as "probable"; count by Daniel's rule: sure + probable = read; < 95 % of words = read in part.
