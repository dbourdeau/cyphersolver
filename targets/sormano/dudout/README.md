Status: no. 63 f. 115r from line 28 to f. 116v re-read sign by sign and read in sentences, with one pre-registered measure (12 Nov 2026, Brice Dudout with Claude Opus 5.5). The state is left to the maintainer.

# sormano — no. 63 ff. 115r (line 28)-116v re-read

This closes the first gap in `NOTES.md` ("no. 63 f. 115r from line 28 to f. 116v, cipher runs not yet re-read sign by
sign"). It continues `no63_reading.md` (f. 115r lines 1-27, 23 Oct 2026) and stops where `n63_f123r_reading.md` takes
over.

## Method
- Images: Gallica `btv1b9060015d`, views 119-121, IIIF full resolution (8660×5876), regions from `pages.json`. No
  images are included here.
- Every cipher sign was transcribed line by line on the image (`no63_signs_reread.txt`). The alias alphabet is in its
  header: `!` = null, `P W R I` = code signs, `(a|b)` = doubtful sign (first option used), `?` = unidentified,
  `[..]` = clear hand. Doubtful signs and look-alike families are listed in `DOUTES.md`.
- Key: Lasry's (KEY.md) with no. 66's values (crossbarred long-s and looped h = nulls; looped Z = z), as in
  `no66_reread_log.md`.
- `no63_signs_reread.txt` (SHA-256 `395d8021c99dc4d6f50f8abd479068a874c713019adddb7957158224a1fcc5d5`) and `DOUTES.md`
  (`926d00b4c56c6887dd91530e74ec5d1a38c6d2da956b4f32fa6a10ae28868b0b`) were frozen before decoding (01:10 CET).
- `PREREG.md` (`26c773c6bf774740dd7b1e79e7b7d946363aa69bf14a98b0ab122e06e68cadae`) and the scripts were frozen before
  the measure (01:11 CET). The measure was run once.

## Measure (one run, output copied unchanged: `measure_result.txt`)
```
portion: 3787 cipher-sign tokens, 3768 with a letter value
M re-read = 3479/3787 = 0.919
M old     = 1966/2742 = 0.717  (n63_transcription.md, same stretch)
key: n=200 median 0.143 p99 0.531 max 0.593
shuf: n=200 median 0.808 p99 0.844 max 0.853
controls >= M re-read: 0/400 ; p = 0.0025
```
M is the share of cipher-sign tokens read by your rule (`matignon1586c3/f276/scripts/measure.py`: a run of ≥ 3
lexicon words totalling ≥ 10 letters), with lexicon `it-cinquecento` (mincount 20). Both pre-registered criteria are
held: M is above all 400 controls, and above the earlier transcription.

Caution: the shuffled-text controls are high (0.81-0.85), because the rule is lenient on long Italian letter
streams. The honest margin is 0.919 against 0.853, not against the permuted keys.

Run it with `python3 scripts/measure63.py <worktree> no63_signs_reread.txt ../n63_transcription.md`.

## Reading with the 95% rule (cipher part of the stretch)
Source: `no63_reading_reread.md`. Sure = word read as written. Probable = one doubtful sign or one look-alike choice
decides the word. Restored and unresolved letters count as holes.
- **Before** (`n63_reading.md`, same stretch): 442 deciphered words, partly carried with "…", and 49 unread
  stretches «…».
- **After, by letters** (3787, with each `[?]` group counted as 3 letters):
  - sure 3370 (89.0 %), probable 314, restored 16, unresolved 75, code signs 12;
  - sure + probable = **97.3 %**.
- **After, by words** (841):
  - sure 743, probable 52, restored 9, unresolved 25, code signs 12;
  - sure + probable = **94.5 %**, just under 95 % on words.

`_check_reading --file`: `dudout/no63_reading_reread.md` 0.642 clean (88/137 sentences, holes 0.118) vs
`n63_reading.md` 0.533 (57/107, holes 0.164; that file also holds f. 115r lines 1-27). Marginal: the `°` marks and
old spellings (dificulta, Firensa, ofendere) count as holes in the word list.

## Points for you
- **Б (looped b-shaped sign)**: here it reads **z** every time (Abruzzo ×2, excelenza, importanza, sicurezza,
  speranza). Your no. 66 gives it rr (ridure, Ferara, l'errore). Either these are two signs I have merged, or the
  sign has two values. Not settled.
- **Curled saltire = Venetiani.** The contemporary gloss "de Venetian[i]" sits above it on f. 116v l.10 (already
  noted in NOTES). It occurs 5 times here, and every context fits. No. 66's single [?Imperatore] reads as well with
  *Venetiani*.
- **⊬7 = Papa**, as in your no. 66.
- **Я (R)** is probably *Fiorentini* (Firensa, Toscana, "l'ambasator loro") and **Ф (I)** probably *Imperatore*
  ("trarlo delle man del ⟨I⟩"). Both are from sense only and are not added to the key.
- **Line order**: the earlier transcription has part of the line order wrong. "lei tanto più pesa" is the foot of
  f. 115v, not f. 116r L04.
- **Remaining**: 25 unresolved groups. The main ones:
  - f. 116r, the reason of the duke of Calabria's claim, "[?] [?] ragion di [?]";
  - f. 116r, "[?] il marchese di Mantoa";
  - f. 116v, "mantener gli [?] oficio".
- **Not attempted here**: the no. 65 gap.

Based on Lasry's key, Arya Patel's identification of f. 123, and your no. 66 re-read and transcriptions.
