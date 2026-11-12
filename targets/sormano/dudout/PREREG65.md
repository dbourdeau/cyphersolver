# PREREG — one measure, re-read of no. 65 (foot of f. 119r, foot of f. 119v, f. 120r; BnF fr. 3096), 12 Nov 2026

Frozen by SHA-256 BEFORE the measure. The sign transcription and DOUTES65.md were frozen first
(GEL65-transcription.sha256, 02:43:47 CET: no65_signs_reread.txt 98b4099f…7234, DOUTES65.md ae73d6f7…043c).
Declared limit: the signs were identified line by line on the image with Lasry's key and Daniel's transcription in
mind (as in the no. 63 re-read); the look-alike choices are listed in DOUTES65.md and are the weak point.

- **Portion**: every cipher sign of no65_signs_reread.txt = f. 119r L32-36, f. 119v from the end of L23 to L37,
  f. 120r L01-L11 (with the short line under L11), L13-L20, L22-L23 (Daniel's line numbers). 1904 cipher signs
  (nulls excluded), far above 300. Decoded with Lasry's key + no. 66's values (crossbarred long-s and looped h = null),
  **looped b-shaped sign = z** (as in no. 63; DOUTES65 records that the sense gives rr twice and z once), first option
  of each doubtful sign. Code signs (D = DUCA) and unidentified signs are context tokens (never read). Clear-hand text
  closes a run.
- **Statistic M**: share of cipher-sign tokens READ by Daniel's rule (targets/matignon1586c3/f276/scripts/measure.py:
  run of >= 3 lexicon words totalling >= 10 letters), lexicon `it-cinquecento` (lang/, mincount 20). Same scoring as
  the no. 63 measure (scripts/measure65.py differs from measure63.py only by the portion, the code sign D and the
  parser of the old transcription).
- **Controls (400)**: 200 permuted letter keys (seeds 1-200) + 200 shuffles of the token order (seeds 1001-1200).
- **Comparison**: Daniel's `n65_transcription.md`, same lines, parsed as stated in measure65.py.
- **Criteria, fixed in advance**:
  1. M(re-read) > max of the 400 controls (p < 1/401);
  2. M(re-read) > M(old transcription).
  Both held -> the re-read is proposed to Daniel (commit on dudout/sormano-reread). 1 without 2 -> reported as
  neutral. 1 not held -> nothing proposed.
- One run only. The output is copied unchanged into MESURE65-resultat.txt and HANDOFF.md.
