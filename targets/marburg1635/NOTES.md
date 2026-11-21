# Marburg 1635: cipher passage in a Thirty Years' War letter (DECODE R4500)

Status: in progress (was: read, ≈97% of tokens; nine signs at the end of line 1 open)

20 Nov 2026, CTTS re-transcription (gold-standard pipeline, `research/ctts/README.md`; full record
`texts/R4500_ctts_test.md`, tokens `texts/R4500_ctts_tokens.txt`). The page was cut into 14 line bands, a blind Fable
5.2 first pass labelled the candidate boxes from the image alone, and Claude Opus 5.5 corrected it in CTTS by computer
use, with every doubt checked on 3x overlay-free crops before `cipher_tokens.txt` was compared. **582 signs.** First
pass: 17.7% sign error raw, 5.7% with its own notes applied, against the final CTTS project; final CTTS against
`cipher_tokens.txt`: 3.0% (565 of 576 match; S11 I6, marks not counted). The old transcription dropped every mark;
CTTS records them, and they belong to the key: **9 with a bow = b/w** (bei, bericht, unbewandt), **0 with two dots or a
bow = z** (zu-, anzudeuten), **triangle with a bar = ll** (allen, aller-, sollen), **long s with two cross strokes = ss**
(unterlassen). No base value changes (an LM test keeps 9 = u, T = c, F = s, q = m as the best fit). Transcription
errors fixed: l. 4 a missing 1 ("werden", as the gloss), l. 7 `X 8 0 7` is theta ("bei diesen conjuncturn gelegen";
the three "blotted" signs are clear), l. 12 X is F ("sein"), l. 2 the "?" is four signs `7 4 1 2` ("ihr"), l. 6 the
second q is a hook (abbreviation mark), l. 10 the burn hole keeps the tops of 7 6 ("Baiern"), l. 1 the first sign is a
dotted 1 ("die"). Lines 4-7 now build a clause; lines 1-3 still do not, and two CTTS readings in l. 2 (theta/s) make
that decode slightly worse, so they stay doubtful. The CTTS project is model-made until a person checks it.

23 Oct 2026, re-reading (REREAD_BRIEF, batch b30): lines 1-7 re-examined. Record and image re-opened (no attachment);
gloss of ll. 1-4 re-read on native crops and aligned with the decode; no label or key value changed. Partial reading
`texts/R4500_l01-07_reading.md` ("... dagegen denselben etwas tentiert weren solte, zumahl nicht unbewandt, was und ob
en gebührender manutenirung der [?Keiserm.] Mait. und [?des] Reich[s] ..."); ll. 1-3 do not build. Score 0.00 (0/5),
explicit holes 0.20: stays decoded, not read; blocker illegible. Log `texts/R4500_l01-07_reread_log.md`.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read**: cipher lines 8-14,
the closing sentence (280 of 538 signs). **Decoded, not read**: lines 1-7 (258 signs): the decode of ll. 2-4 is
garbled and the normalised reading fills it with bracketed conjecture; ll. 5-7 give a clause with slips. Split into
two `outcome.texts` entries; class read -> read in part; 97.4% (signs with a value) withdrawn as a reading figure, 52%
of the signs read.

- **Record.** DECODE R4500, Hessisches Staatsarchiv Marburg, HStAM 4 d Nr. 1218 no. 49 (arcinsys v1923393). One page,
  image `IMG_R4500_I26572_P.jpg` (git-ignored in `img/`). DECODE: "Partially decrypted", date span 1635–1652 (the
  volume's span, not the letter's date), sender/recipient not given.
- **What it is.** A German letter in clear text reporting troop movements (Rostock, companies marching, "Marche").
  From "noch nicht zu vernehmen," the rest (14 lines) is in cipher; the letter closes in clear with "... beygefügter
  Extract". A contemporary hand wrote a decipherment between cipher lines 1–4. That is why DECODE has it as partly
  decrypted. Lines 5–14 have no gloss.
- **Series.** R4452–R4577 are the same volume: about 120 key sheets (claves of Hesse-Kassel with officers and civil
  servants, 1635–52) and four ciphertexts (R4452–R4454, R4536 decrypted, R4546). None of the single-row alphabets checked
  (R4467, R4491, R4520, R4525) is this key. The key was rebuilt here from the text instead.

## Method

1. Token transcription `cipher_tokens.txt` (577 signs, word gaps kept).
2. Homophonic annealing against `lang` `de-1500s` (spaces, order 5). A free run gave near-German; seeding a few
   letters from "und"/"under" repeats (`9 0 1`, `6 1 2`) produced readable words: "entschuldigt", "damit ich",
   "underthenigst", "ermangelen möchte". These fixed the rest by hand.
3. The interlinear gloss is the control: "(zu)mahl nicht", "etwas tentiret werden", "dieses orths halber", "dagegen"
   come out of lines 3–5 with the rebuilt key unchanged, except that it fixes M = w and 8 = o.

## Key (signs → letters)

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| 5, 8(o), A | a / o | 6 | e | 0 | n |
| 1 | d | 1 2 (joined, "iz") | r | 2 | s |
| 3 | g | 4 | h | 7 | i |
| 9 | u (also b once in "halber") | F (d-shaped) | s | W (w-sign) | t |
| T (theta) | c (`T4` = ch) | D (triangle) | l | q (4 with cross) | m |
| X (crossed t) | b | M (superscript w/m) | w | j | d |

So the table is a letter-for-letter substitution with a few homophones (a: 5, 8, A; s: 2, F), written mostly in digits.

Marked signs (CTTS re-transcription, 20 Nov 2026; the earlier transcription dropped the marks): 9 with a bow = b or w
(6x; plain 9 = b once more, in "Baiern"); 0 with two dots or with a bow = z (2x); triangle with a bar = ll (3x); long s
with two cross strokes = ss (2x; in l. 5 "o?en" it is unsettled). A hook after `1 2` (3x) is an abbreviation mark.

## Reading (normalised; [..] = conjectural)

> ... noch nicht zu vernehmen, [die Landtschaft ...] ... [unleserlich] ..., das kann dieses orths halber observiren,
> dagegen den selben etwas tentiret werden solte, zumahl nicht unbewandt [was und ob] gebührend zur manutenirung dero
> Kays. Maj(estät) und des Reichs wie auch [bey diesen] ... [ungelegen]; dahero ich nicht unterlassen sollen, die
> notturft dieser Vestung so wol allerhöchst ihrer Kays. Maiestet als auch ihrer Churf. Durchl. in Bayern ohnlängst
> nochmals allerunderthenigst und underthenigst anzudeuten, damit ich aus allen fall entschuldigt sein und dessen,
> meinem gebührenden bericht an gehörigen ort, nicht ermangeln möchte.

The writer reports to Kassel that he has set out the needs of "this fortress" (dieser Vestung) to the Emperor and the
Elector of Bavaria, and asks to be held excused ("damit ich aus allen fall entschuldigt sein"), so he writes as an officer
or agent on the imperial side, from a fortress.

## Measurement

Second pass on lines 1–2 (22 Sept): line 2 `12 7 12 / 6 0 0 8 T 4 / 0 9 / 12 F / 6 7 W / 7 4 12 / 6 0 1 F F / 4 5 D 9 6 12`
= "(w)ir (d)ennoch nur seit ihr endes halber ... ursach" (an initial sign dropped in transcription on two words);
line 1 `1 7 6 / A 5 0 1 W F` = "die landts..." (first sign is 1 = d, not 7; A = l here). Unread: the last ~9 signs of
line 1 and ~6 blotted signs in lines 7 and 9, about 15 of 590 signs. 96.8% measured in `reading_tokens.txt` (538 signs, 17 unread). Class:
read; key recovered. After the line 9 correction of 30 Sept (below): 97.4% (538 signs, 14 unread: nine in line 1, one in
line 2, three in line 7, one in line 10).

## Transcription doubts

From the CTTS re-transcription of 20 Nov 2026 (`texts/R4500_ctts_tokens.txt`, `?x` there); each checked on a 3x
overlay-free crop of the line band, against the decode, and against `cipher_tokens.txt` afterwards.

- ?1 (l. 1, first sign) - read: 1; checked: image, decode, transcription; dotted short stroke (old: 7); gives "die" as the gloss
- ?9 (l. 1, seventh sign from the end) - read: 9; checked: image, decode, transcription; rho-shaped loop with a long left descender (old: ?); "ta?d inhae-" does not build either way
- ?F (l. 2, after 6 0 0 8) - read: F, alternative T; checked: image, decode, transcription; oval with a loop rising left (old: T); LM and "ennoch" favour T
- T (l. 2, after 6 0 1) - read: T; checked: image, decode, transcription; clear theta (old: F); LM favours F ("endss"), neither builds
- ?F (l. 2 blot, l. 3 blot, l. 11 stain) - read: F; checked: image, decode, transcription; tall cross-stroked long s under ink (old: X, F, F)
- ?A (l. 3, before 3 9 1 7) - read: A; checked: image, decode, transcription; pointed sign overrun by the gloss (old: A)
- ?7 ?6 (l. 10, burn hole) - read: 7 6; checked: image, decode, transcription; top of a 7 and a looped ascender survive (old: one ?); gives "Baiern"
- 4 (l. 5 "zu?ahl", l. 6 "de? Reich") - read: 4; checked: image, decode, transcription; angular 4 with a long bar, the form that is h in l. 11; the sense wants m
- 9~ (l. 6 and l. 9, "?eiser") - read: 9 with bow; checked: image, decode, transcription; the bow is b/w elsewhere, the sense wants K

## Remaining gaps
- cipher lines 2-3 decoded, not read - blocker: illegible; re-read 23 Oct 2026 (b30, `texts/R4500_l01-07_reread_log.md`): the gloss is faded and cramped and departs from the signs at "insonderheit" and "observiren"; ll. 4-7 now build a clause (`texts/R4500_l01-07_reading.md`), score 0.00 / holes 0.20, so lines 1-7 stay decoded, not read

- End of line 1 (~9 signs, `W 5 ? 1 7 0 4 5 6`) - blocker: illegible; cramped under the faded gloss on the only scan.
  CTTS (20 Nov 2026) reads every sign, `W 5 ?9 1 7 0 4 5 6`, with the seventh rho-shaped and doubtful; the decode
  "ta?d inhae-" still does not build.
- Two signs of line 2 (after `6 0 0 8`, after `6 0 1`) - blocker: illegible; theta and the d-shaped s are written alike
  in this hand, CTTS and `cipher_tokens.txt` disagree at both, and the LM prefers the older readings; recorded as
  doubtful in `texts/R4500_ctts_tokens.txt`.

## Escalation
- [x] siblings: all 126 records R4452-R4577 of the volume downloaded; no clear copy of this letter
- [x] clear-pages: the interlinear gloss on lines 1-4 used as crib and control
- [x] known-keys: sign alphabets R4467, R4491, R4520, R4525 compared; none is this key
- [x] print: no edition of HStAM 4 d Nr. 1218 found; DECODE has no transcription
- [x] key-rebuild: homophonic anneal on de-1500s plus hand fixes; key recovered
- [x] retry: lines 1-2 and the doubtful signs re-viewed at 3-4x zoom; still open
- [x] retry (23 Oct 2026): gloss of ll. 1-4 re-read and aligned word by word; ll. 4-7 rebuilt as a clause; ll. 1-3 still open
- [x] retry (20 Nov 2026): sign-level re-transcription in CTTS from the image (blind first pass, overlay-free crops of
  every doubt): 17 transcription differences, marks recorded and valued (9~ = b/w, 0¨/0~ = z, D‾ = ll, F- = ss); ll. 4-7
  now build a clause, ll. 1-3 still open (`texts/R4500_ctts_test.md`)
- [ ] reader review of the corrected ll. 4-7 clause (reading gate) before the class or fraction read is raised

## Corrections

- **20 Nov 2026 (CTTS re-transcription, `texts/R4500_ctts_test.md`).** Line 7 "ueidiesen boni", listed under Remaining
  gaps since September: the signs are clear on the CTTS crops, and `X 8 0 7` was a misread theta, so the line reads "bei
  diesen conjuncturn gelegen". Line 4 lacked a 1 ("werden"), line 12 X is F ("sein"), line 2 "?" is `7 4 1 2` ("ihr").

- **30 Sept 2026 (reported while quotations were pulled for Lasry's list; checked on the scan).** Line 9: its first
  three signs `F 6 12`, marked unread as blotted, are clear on `IMG_R4500_I26572_P.jpg` (main checkout
  `marburg1635/img/R4500.jpg`, zoomed 3x) and give `s e r` with the key unchanged. With the end of line 8 (`1 7 6` die)
  and the rest of the run (`9 6 / F W / 9 0 3`) the text is "die|ser ue st ung" = "dieser Vestung" (9 = u/v), so the
  conjecture "dieser [sachen]" is withdrawn: "die notturft dieser Vestung", the needs of this fortress. Line 11: the
  "..." after "nochmals" hid `F 5 / D 6 12` = "s a / l er", and on the scan the triangle carries a doubling bar (ll), so
  the text is "nochmals allerunderthenigst und underthenigst" (allerunterthänigst for the Emperor, unterthänigst for
  the Elector); nothing is supplied. `reading_tokens.txt` updated (L09 signs read, L11 D = ll): 14 of 538 signs unread,
  97.4%. Changed: `docs/marburg1635.html` (reading, English, summary, uncertainty list), `docs/reveal/marburg1635.json`
  (caption, D = ll), this file, `profile.json`. Not changed (outside this folder): `papers/lasry/excerpts.json` still
  quotes both places with "...". Not re-checked: line 7, where the scan shows a clear-text insertion after "auch"
  (abbreviated "K. Chur...", then a struck-through group) that `cipher_tokens.txt` does not record.
