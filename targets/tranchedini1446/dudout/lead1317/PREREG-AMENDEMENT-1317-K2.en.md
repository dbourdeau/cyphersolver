# PREREG amendment no. 3: key K2 and one measurement on ital. 1584 f. 353r (14 Nov 2026, evening)

English translation of the frozen French original `PREREG-AMENDEMENT-1317-K2.md` (sha256 9bea6a6a..., in `HASHES-1317-K2.txt`).
The French file is the one that was frozen; this translation was made afterwards for the pull request and changes nothing.

Written and frozen (SHA-256 in `HASHES-1317-K2.txt`) BEFORE any sign-by-sign transcription of f. 353 and BEFORE any reading of the
copy f. 352. Brice Dudout's instruction (14 Nov, evening): complete the R5318 key, freeze it, make ONE measurement on the intact letter
ital. 1584 f. 353, keep f. 71 in reserve. Seen of ff. 352-353 so far: the whole 1000 px thumbnails of views 346-348 (layout only;
unreadable at that size), no crop.

## Frozen key K2
- `K2_key.tsv` (shape label -> value; x|y -> first value; '' = null) and `sign_legend_K2.md` (shapes only, no values).
- Built only on: the R5318 sheet, f. 28 + clear f. 27, f. 30 + clear f. 29, f. 35r + clear ff. 34r-v (burnt), the f. 134 glosses;
  scripts `k2/common.py`, `k2/explore.py` (alignment -> counts); image checks on training crops.
- Changes against R5318_crosswalk (04c8ae96...): 21 new shapes valued (`LTL` = Re de Ragona, `MINL` = ambassadore, `lolli` c,
  `ribbon` le, `heart` lu, `tribar` me, `hookl` pu, `rstem` se, `bslash` t, `pix` x, `rc` a, `rcb`/`baro` f, `zz` z, `fa3` fa,
  `CLOVER` milan, `MEANDER` denaro, `OBLOOP` facto, `DIAMDOT` pace, `RCAP` fiorini, `UDOT` italia, ...); nulls: `DEL`, `otee`, `o3`,
  `rho`; corrected: `tt` cc (not sa), `dd` sa, `ri` ri (not bi), `rb` ra, `ne` ne, `VEN` li Venetiani (1448 use; duca as second
  value, not used), `COSIMO` cosimo, `oc` d. In-sample check (not evidence, training material): f. 35 0.840, f. 30 0.860.

## Portion (one only)
- **BnF ital. 1584 f. 353 recto** (Gallica btv1b100373864, view 347, right-hand page), Tranchedini, Florence, 14 Oct 1447:
  **all cipher runs of the page, in order**, first line to last. The verso (view 348) carries only the address.
- Never transcribed or decoded by us. After the measurement f. 353 is burnt. **ital. 1585 f. 71 stays intact (reserve).**

## Differences of date / key period (recorded before the measurement)
- f. 353 = 14 Oct 1447: after the death of Filippo Maria (13 Aug 1447), Ambrosian Republic; between R5318 (1446 key,
  bar-o-bar-o = Duca) and the letters of Feb 1448 (VEN = Venetiani). The key may have changed in between (nomenclator reassigned).
- VEN = "li Venetiani" is kept (first value); "Milanesi" will probably be frequent (CLOVER = milan + e + si).
- Image: black-and-white microfilm (ff. 28/30/35: colour), so the transcription is harder.

## Reference
Copy f. 352 r-v (view 346 right-hand page + view 347 left-hand page), read only AFTER the transcription is frozen.
For each run, the words of the copy between the clear words that frame it on f. 353, written to `texts/f352_reference.txt`
(format `Rn: words`) BEFORE any decoding; blank / dash of the copyist = `[—]`. If a run is not found in the copy (copyist's skip),
it is removed from the portion BEFORE decoding, and noted.

## Transcription
Labels of `sign_legend_K2.md`; shapes not in it -> `@Nxx` (no value, no attachment afterwards).
Pass B and pass C by blind subagents (no key, no values, no copy, no left-hand page); each pass may be made by two subagents on two
halves of the page separated by a line fixed in advance. Settling on the image by a third blind subagent -> `texts/f353_signs.txt`.
I do not transcribe (I know the key). Working image: the right-hand page only, cropped.

## Measurement (one only): `measure_f353.py`
- Metric identical to f. 35: first value; normalisation (lower case, letters only, v->u, y->i, j->i, h dropped, doubles simplified);
  score = 1 - sum Levenshtein / sum of reference lengths.
- Controls: 200 keys shuffled inside classes (word signs = UPPER-CASE labels; nulls; letters/syllables), seed 1447.
- Thresholds: **read** if score >= 0.85 AND >= best control + 0.30; **partial** if only >= best + 0.30; otherwise **failed**. z reported.

## After the measurement
Only if "read": reading of the letter, strict word count (sure / {probable} / [supplied] / <unresolved>); >= 95% = read;
pull-request folder. Otherwise: the figures are reported, no reading is claimed, f. 71 not touched.
