# PREREG — one measure, re-read of no. 63 ff. 115r l.28 - 116v (BnF fr. 3096), 12 Nov 2026

Frozen by SHA-256 BEFORE the measure. The sign transcription and DOUTES.md were frozen first
(GEL-transcription.sha256: no63_signs_reread.txt 395d8021…c5d5, DOUTES.md 926d00b4…8b0b).
Declared limit: the signs were identified line by line on the image with the key in mind (as in Daniel's no. 66
re-read); the look-alike choices (T/b, pi/e, Y/y) are listed in DOUTES.md and are the weak point of the measure.

- **Portion**: every cipher sign of no63_signs_reread.txt (f. 115r from "-solverse" to the foot of f. 116v, about
  2,000 signs, far above 300), decoded with Lasry's key + no. 66's values (crossbarred long-s and looped h = null,
  looped b-shaped sign = z here), first option of each doubtful sign. Code signs and unidentified signs are context
  tokens (never read). Clear-hand text closes a run.
- **Statistic M**: share of cipher-sign tokens READ by Daniel's rule (targets/matignon1586c3/f276/scripts/measure.py:
  run of >= 3 lexicon words totalling >= 10 letters), lexicon `it-cinquecento` (lang/, mincount 20).
- **Controls (400)**: 200 permuted letter keys (seeds 1-200) + 200 shuffles of the token order (seeds 1001-1200).
- **Comparison**: Daniel's `n63_transcription.md`, same stretch (old L23-L35 of f. 115r and all of ff. 115v-116v),
  same rule.
- **Criteria, fixed in advance**:
  1. M(re-read) > max of the 400 controls (p < 1/401);
  2. M(re-read) > M(old transcription).
  Both held -> the re-read is proposed to Daniel. 1 without 2 -> reported as neutral. 1 not held -> nothing proposed.
- One run only (scripts/measure63.py). The output is copied unchanged into MESURE-resultat.txt and HANDOFF.md.
