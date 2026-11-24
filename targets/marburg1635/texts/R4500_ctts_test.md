# R4500: does a sign-level re-transcription in CTTS change the key or the reading? (20 Nov 2026)

Claude Opus 5.5, for the CTTS gold-standard pipeline (`research/ctts/README.md`). The transcription (`cipher_tokens.txt`)
and the key (NOTES.md) were both rebuilt here from the ciphertext, so either may hold errors. Lines 1-7 decoded but did
not build sentences.

## What was done

1. **Bands.** The page image (`img/R4500.jpg`, 2628 x 3778, git-ignored) was cut into 14 bands, one per cipher line,
   with `research/ctts/segment_lines.py`: line centres given by hand (the interlinear gloss over lines 1-4 defeats both
   automatic line finders), each band straightened by a column shear. 633 candidate boxes from ink blobs.
2. **Blind first pass.** A fresh Fable 5.2 agent saw only the bands, the numbered overlays and a notation sheet (not
   `cipher_tokens.txt`, the reading, the key, the decode or the gloss transcription). It labelled 633 boxes: 571 signs
   in boxes, 15 missed, 40 split, 41 part, 51 clear text, 14 junk, with notes on every doubt
   (`research/ctts/projects/marburg1635/labels_fable.json`).
3. **CTTS.** Its own split/part/missed notes were applied mechanically (`research/ctts/apply_flags.py`) and the project
   written with `to_ctts.py` (640 boxes, 36 types). Claude read every line on enlarged, overlay-free strips and the
   doubtful places on 3x crops, then made the corrections in CTTS 3.7.0 by computer use while the user watched
   (17:32-17:45 and 17:46-17:49; reading and crops 17:17-17:31): about 30 type moves, 3 renames, 7 deleted duplicate or
   punctuation boxes, 1 merge, 2 boxes redrawn. Saved with F10/ESC. Result: **582 signs** in 14 bands.
4. **Comparison** with `cipher_tokens.txt` only after that (step 5c of the README).

## Error rates (sequence alignment per line; error = (S+D+I)/N)

| transcription | against | N | match | S | D | I | error |
|---|---|---|---|---|---|---|---|
| first pass, raw box labels | final CTTS | 582 | 516 | 15 | 51 | 37 | 17.7% |
| first pass with its own notes applied | final CTTS | 582 | 558 | 22 | 2 | 9 | 5.7% |
| same, `?x` read as x | final CTTS | 582 | 572 | 9 | 1 | 8 | 3.1% |
| first pass with notes applied | `cipher_tokens.txt` | 576 | 560 | 15 | 1 | 14 | 5.2% |
| **final CTTS** (marks folded into the target notation) | `cipher_tokens.txt` | 576 | 565 | 11 | 0 | 6 | **3.0%** |

Marks are not counted in the last two rows: CTTS records marks the target transcription has none of (0¨ x1, 0~ x1,
9~ x6, D‾ x3, F- x2). Box geometry was left largely as segmented and split; only boxes that put signs out of order were
redrawn, so the boxes are not yet a gold standard of geometry.

## The 17 differences from `cipher_tokens.txt`, and what the image shows

| line | cipher_tokens | CTTS | evidence (3x crop, no overlay) | decode effect |
|---|---|---|---|---|
| 1 | 7 (first sign) | ?1 | short stroke with a dot above-left, like the dotted 1s of the hand | "iie" -> "die" (gloss: "die") |
| 1 | ? | ?9 | loop with a long descender to the left (rho-shaped) | "ta?" -> "tau"; open |
| 2 | T (after 6 0 0 8) | ?F | oval with a loop rising to the left; the first pass read the d-shaped s | "ennoch" -> "ennosh"; LM prefers T |
| 2 | X (blotted) | F | tall stroke with cross stroke at top, under a blot | "nur b eit" -> "nur seit" |
| 2 | F (after 6 0 1) | T | clear theta: oval with a stroke through it | "endss" -> "endcs"; LM prefers F |
| 2 | 1 ? | 7 4 1 2 | four signs written joined, same forms as "7 4 1 2" earlier in the line | "halberd ?" -> "halber ihr" |
| 4 | (none) | 1 | a tall 1 between "1 2" and "6 0" | "weren" -> "werden" (gloss: "werden") |
| 6 | q | 9~ | 9 with a bow above, no cross stroke | "derm" -> "der b/w" |
| 6 | q | [hook] | a hook trailing from the 2, not a crossed q; the real q follows | "serm mait" -> "ser' mait" |
| 7 | X | T | theta with a pointed top (the crossed t is small, foot to the right) | "boni" -> "coni": "conjuncturn" |
| 9 | (none) x2 | [hook] | the same hook after 3 and after "1 2" | none (not a key sign) |
| 10 | ? | ?7 ?6 | burn hole: the top of a 7 and the looped ascender of a 6 survive | "ua?rn" -> "uaiern": "Baiern" |
| 12 | X | F | large long s, smudged while wet | "bein" -> "sein" |

Lines 3, 8, 11, 13 and 14 agree sign for sign. The three signs NOTES listed as blotted in line 7 (`6 F 6`) are clear.

## Decode with the target key on the CTTS tokens

Key unchanged, marks ignored (`decode_ctts.py` in the project folder):

    l01 dieaandtstaudinhae
    l02 rirennoshnurseitihrendcshaluerihruracst
    l03 enueschwerungenichagudiesesortshaluersastueg
    l04 rissendagegendenseluenetwastentiertwerden
    l05 soltenuhahlnnichtunueuandtwusundobengebuhrend
    l06 ermanutenirungderueiser'maitunddehreichwie
    l07 auchueidiesenconiuncturngelegen
    l08 daheroichnichanunderlabensolendienotturstdie
    ...

With the marked signs given their own values (9~ = b/w, 0¨ = 0~ = z, D‾ = ll, F- = ss):

    l04 rissendagegendenseluenetwastentiertwerden
    l05 soltezuhahlnnichtunbebandtwusundossengebuhrend
    l06 ermanutenirungderbeiser'maitunddehreichwie
    l07 auchbeidiesenconiuncturngelegen
    l08 daheroichnichanunderlassensollendienotturstdie
    l11 nochmalsallerunderthenigstundunderthenigst
    l12 anzudeutendomitichausallenaslentschuldigtsein
    l13 undesanmeinemgebuhrendenberichtangehossigenort

## Key test (lang `de-1500s`, order 5, no spaces; per-character log score of the whole decode)

Each value tried in turn with the rest fixed (`keytest.py`, scratch):

| sign | n | target value | best values (score) |
|---|---|---|---|
| 9~ | 6 | (u) | w -2.368, b -2.377 ; u -2.437 |
| 0~ | 1 | (n) | z -2.424 ; n -2.437 |
| 0¨ | 1 | (n) | z -2.431 ; n -2.437 |
| D‾ | 3 | (l) | ll -2.402 ; l -2.437 |
| F- | 2 | b | ss -2.429 ; b -2.437 |
| 9, T, F, q, M‾, j | 36, 21, 31, 9, 6, 1 | u, c, s, m, w, d | unchanged: each is already the best value |
| s | 2 | u | e -2.414, a -2.416 ; u -2.437 (two signs, not settled) |
| A | 2 | a | t -2.394 (two signs; noise) |

All five marked values together: -2.316 (from -2.437). By part: lines 8-14 -2.130 -> -1.979, lines 4-7 -2.382 -> -2.248,
lines 1-3 -3.115 -> -3.115 (no marked sign there). The target tokens with the target key score -2.691 on lines 1-3:
the CTTS readings at the two doubtful theta/s places of line 2 cost most of the difference (-2.861 with T restored).

## Answer

- **Key.** No value of the target key changes: 9 = u, T = c, F = s, q = m and the rest stay the best fit. What changes is
  that the marks are part of the key: a bow on 9 marks b/w (bei, bericht, unbewandt), two dots or a bow on 0 mark z
  (zu-, anzudeuten), the bar on the triangle doubles it (allen, aller-, sollen), and the doubly crossed long s is ss
  (unterlassen). The old transcription dropped all marks, and the old key covered the gaps with "9 also b once" and
  conjectured readings. Plain 9 still stands for b once (in Baiern).
- **Reading.** Lines 4-7 now build a clause with fewer supplied letters: "dagegen denselben etwas tentiert werden solte,
  zumahl nicht unbewandt, w[a]s und o[b] en gebührender manutenirung der [K]eiser[l.] Mait. und de[m] Reich, wie auch
  [K. Churf.] bei diesen conjuncturn gelegen". New from the signs: "werden", "bei diesen conjuncturn gelegen", "die" at
  the start of line 1, "ihr" in line 2, "Baiern" in the burn hole, "sein" in line 12. Lines 1-3 still do not build
  sentences, and the two places in line 2 where CTTS departs from `cipher_tokens.txt` make the decode slightly worse,
  so they stay marked as doubtful.
- **Not settled.** "zumahl" has an angular 4 where m is needed (a writer's slip or a q that lacks its cross stroke);
  "Keiser" begins with a bowed 9 (b/w) where K is needed; the two s-signs of "was und" decode u u.
