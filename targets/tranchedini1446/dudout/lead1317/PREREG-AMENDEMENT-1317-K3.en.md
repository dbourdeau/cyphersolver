# PREREG amendment no. 4: key K3 and one measurement on ital. 1585 f. 71 (14 Nov 2026, night)

English translation of the frozen French original `PREREG-AMENDEMENT-1317-K3.md` (sha256 4ec53a2b..., in `HASHES-1317-K3.txt`).
The French file is the one that was frozen; this translation was made afterwards for the pull request and changes nothing.

Written and frozen (SHA-256 in `HASHES-1317-K3.txt`) BEFORE any opening of the images of ital. 1585 f. 71 (view 137) and f. 70
(view 135), thumbnails included. Brice Dudout's instruction (14 Nov, evening): "K3 and one measurement on f. 71". Seen of ff. 70-71
so far: only the file dimensions (85_f137.jpg 3457x5063, 85_f135.jpg 3436x5083); and, from the lead, the date (18 June 1449) and the
title of the period decipherment f. 70 "Ex cifra Nicodemi". **f. 71 = the last intact letter of lead 1317.**

## Frozen key K3
- `K3_key.tsv` (shape label -> value; x|y -> first value; '' = null) and `sign_legend_K3.md` (shapes only, no values).
- Built only on burnt or training material: the R5318 sheet, ff. 28/30/35 + clears, f. 353r (burnt) + copy f. 352, the f. 134
  glosses (via the R5318 report); scripts `k3/`; Brice Dudout's blind review sheet (PREREG d553da37..., answers ea46acef...,
  controls 3/3, decisions `planche/DECISIONS-K3.md`).
- Changes against K2 (bfa0c266...): legend rewritten for `pe` (trefoil with nothing under it) / `CLOVER` (trefoil on a cross, milan);
  `re` (ꞔ⊣) / `rb` (ƅ, ra) / `hookl` (⅃ alone, pu) + `cbar` (ȼ, pu; "cbar hookl" = two signs, Brice's remark on q12);
  `oo+` (cross AFTER the loops = sig~sigismondo) / `FED` (cross ON the loops = sig~federico) / `MALA` (sig~malatesta);
  `SIGNORE` (♀ on a foot); `m8` -> i; new `n0` b, `ooo` be, `GDA` gente~darme, `o2L` null; `o2` with an inner dot = o2.
  Unchanged: `ss` s|p (first: s), `o3` null, `VEN` li~venetiani (1448 use). In-sample (not evidence): f. 353 with corrected labels 0.827.

## Differences of date (recorded before the measurement)
f. 71 = 18 June 1449, sixteen months after the letters of Feb 1448: the nomenclator may have been reassigned (oo+/FED, VEN). K3 is kept as it is.

## Portion (one only)
- **BnF ital. 1585 f. 71** (Gallica btv1b52525947w, view 137): **all cipher runs of the page, in order**, that have a counterpart
  in the period decipherment f. 70. If f. 71 also carries cipher on another view (verso), it is taken only if the image is already
  downloaded; otherwise noted and left out of the portion.
- Size bar: >= 300 cipher signs. If the covered portion has fewer than 300 signs, the measurement is still made and reported
  "below size bar" (not evidence for the repository).
- After the measurement, f. 71 is burnt.

## Transcription
Labels of `sign_legend_K3.md`; shapes not in it -> `@Nxx` (no value, no attachment afterwards). Margin marks excluded;
any interlinear glosses ignored. Pass B and pass C by blind subagents (no key, no values, no f. 70, no other image); a pass may be
shared by two subagents on two halves of the page, boundary fixed in advance. Settling on the image by a third blind subagent
-> `texts/f71_signs.txt`, hashed before any reading of f. 70. I do not transcribe (I know the key); I only crop the page (without
reading it beyond locating the lines) and merge mechanically.

## Reference
Period decipherment f. 70 (view 135), read only AFTER the transcription is frozen. For each run of f. 71, the words of f. 70 that
correspond to it (located by the clear words that frame it on f. 71), written to `texts/f70_reference.txt` (format `Rn: words`)
BEFORE any decoding; blank/illegible = `[—]`. A run with no counterpart is removed from the portion before decoding
(`texts/f71_signs_portion.txt`), and noted.

## Measurement (one only): `measure_f71.py` (runs `measure_f353.py` unchanged: key K3, seed 1449)
- Metric identical to f. 35 / f. 353: first value; normalisation (lower case, letters only, v->u, y->i, j->i, h dropped,
  doubles simplified); score = 1 - sum Levenshtein / sum of reference lengths.
- Controls: 200 keys shuffled inside classes (word signs = UPPER-CASE labels; nulls; letters/syllables), seed 1449.
- Thresholds: **read** if score >= 0.85 AND >= best control + 0.30; **partial** if only >= best + 0.30; otherwise **failed**. z reported.

## After the measurement
Only if "read": reading of the letter, word count (sure / {probable} / [supplied] / <unresolved>); >= 95% = read; pull-request
folder (target tranchedini1446 or the one of lead 1317) with an English PR body, no image. Otherwise: figures only, no reading claimed.
