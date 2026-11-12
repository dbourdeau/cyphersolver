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
- **No. 65 gap**: done in a second pass, below.

# no. 65 — foot of f. 119r, foot of f. 119v, f. 120r re-read (second pass, 12 Nov 2026)

The cipher runs that `n65_reading.md` leaves as «…», (?) or "only partly legible": f. 119r L32-36, f. 119v from the end
of L23 to L37, f. 120r L01-L11, L13-L20, L22-L23 (your line numbers).

## Method
- Same as for no. 63: Gallica views 123-124, IIIF full resolution, every cipher sign transcribed line by line
  (`no65_signs_reread.txt`, same alias alphabet, plus `D` = the DUCA circle). Doubts in `DOUTES65.md`.
- Key: Lasry's with no. 66's values; the looped b-shaped sign is decoded **z**, as in the no. 63 pass, and declared.
- `no65_signs_reread.txt` (SHA-256 `98b4099f190b6f75e76d5113e47c4b0154c3aa194d7484bdccd1d65909827234`) and
  `DOUTES65.md` (`ae73d6f7cdb4930cdd3a8ed4f283eb1f7f6d253bc5adb570a58028b97924043c`) frozen before decoding (02:43 CET).
- `PREREG65.md` (`a828cd9663d613479b22cc78b75f53558a288d78f65eb900e34788e17ebeb476`), `scripts/measure65.py`
  (`9fd5d034…e5a4`) and `scripts/decode65.py` (`619fd85a…f08f0d`) frozen before the measure (02:44 CET). One run.

## Measure (one run, output copied unchanged: `measure65_result.txt`)
```
portion: 1904 cipher-sign tokens, 1902 with a letter value
M re-read = 1885/1904 = 0.990
M old     = 1716/1964 = 0.874  (n65_transcription.md, same lines)
key: n=200 median 0.156 p99 0.603 max 0.685
shuf: n=200 median 0.842 p99 0.884 max 0.901
controls >= M re-read: 0/400 ; p = 0.0025
```
Same rule and lexicon as the no. 63 measure. Both pre-registered criteria are held. As before, the honest margin is
against the shuffled text (0.990 vs 0.901).

Run it with `python3 scripts/measure65.py <worktree> no65_signs_reread.txt ../n65_transcription.md`.

## Reading with the 95% rule (`no65_reading_reread.md`)
- **Before** (`n65_reading.md`, same passages): 315 deciphered words, one marked (?) (*concedeva*), 33 gaps "…" and
  3 unread stretches «…» (f. 119r L32-36, f. 119v L35-37).
- **After, by words** (422): 397 sure, 22 probable, 2 restored (*c[o]sì*, *sign[o]r*), 0 unresolved, 1 code sign
  (DUCA). Sure + probable = **99.3 %**.
- **After, by letters** (1904 cipher-sign tokens): 1880 sure, 22 probable (19 doubtful signs and the 2 looped
  b-signs read rr, below), 1 unidentified, 1 code sign. Sure + probable = **99.9 %** of the letter signs.

## Points for you
- **Looped b-shaped sign**: here it is **rr** by sense in *Fe-rr-ara* (f. 119r L33-34) and *a-rr-ivò* (f. 120r L03),
  and **z** in *contente-z-a* (f. 119v L26). Together with no. 63 (z) and no. 66 (rr), the sign seems to carry both
  values, or two close forms are merged. Decoded z here by protocol.
- Gaps filled, among others: f. 119r *in cosa d'honor, d'utile, stabilimento et esaltation del nome, casa et stato
  di Ferrara, che da mo' suo si poseva dire* and *ci habi prestato ogni sua opera et uficio. Non contenti di questa
  opera*; f. 119v *si per stabilire il suo stato, esaltar con suo poco et picolo pericolo et minor spesa la sua casa
  et sucesione, come per liberar Italia* and *io Sormano una altra volta mi trovase, come mi trovai, solo con il Duca
  per avertirlo di novo*; f. 120r *poco apreso noi arrivò eso signor don Hercole, che ci confirmò come el signor Duca
  in alcun modo intendere non voleva al regno per sé*.
- Corrections: f. 119v L26 *cedeva* (not *concedeva(?)*); L29 *operando* (not *sperando*); L23 *la sua* (not
  *questa sua*); f. 120r L23 *causa* (not *cosa*). *Duca* and *Papa* are spelled out in cipher on f. 120r.

Based on Lasry's key, Arya Patel's identification of f. 123, and your no. 66 re-read and transcriptions.
