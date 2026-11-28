# villeneuve1737maurepas — Villeneuve (Constantinople) to Maurepas, 18 Feb and 2 Apr 1737: the two undeciphered cipher letters of Archives nationales AE/B/I/414 (catalogue 538)

Source: Archives nationales, AE/B/I/414 (correspondance consulaire, Constantinople), reproduction ordered by Brice Dudout (26 JPEG, received 20 Nov 2026). Images are not distributed; cite « Archives nationales, AE/B/I/414 ».

## Pieces
- T1 — Villeneuve to Maurepas, Constantinople, 18 Feb 1737 (frames 0060-0062): inventory « Lettre chiffrée — lettre non déchiffrée ». 350 cipher groups, clear passages between them.
- T2 — Villeneuve to Maurepas, 2 Apr 1737 (frames 0092-0096 L): inventory « Lettre partiellement chiffrée, non transcrite ». 1,194 cipher groups. (Frames 0093-0097 also show the header strip of a sheet dated 10 Apr 1737 lying behind; it is not a separate cipher letter.)
- Key witnesses (same volume, period interlinear decipherment): 9 Jul 1737 (frames 0197-0202) and 29 Jul 1737 (frames 0230-0231).

## The code
A numeric nomenclator, groups 1-499: single letters with homophones (n = 78, 409, 182; e = 10; r = 164; t = 220, 400 ...), many syllables (co 26, so 469, pe 374, re 51, se 27, ro 292, la 203, de 441/495, que 117, ...) and some words (dans 189, nostre 461, commerce = 410 + ..., roy 447, bien 462). 318 is very frequent and behaves as a null, often between words. It is not the 1737 Villeneuve -> Otter key read by George Lasry (targets/villeneuve1737; e.g. there 283 = je, 78 = ce).

## Transcription
Two blind passes (A, B; AI agents without key; B in reverse page order) of targets and witnesses, a blind arbiter on the 62 disagreements (blind/), and a separate careful re-reading of the period glosses (key_source/gloss_careful.txt). Agreement before arbitration: 1,498/1,544 target groups, 1,712/1,781 witness groups. Main confusions: this hand's 3 and 5; groups lost in the binding at the end of left-page lines.

## Key and measure (pre-registered, prereg/)
- PREREG-0 (20 Nov, before any key): TRAIN = witness frames 0197-0199 + 0230-0231; HELD-OUT = 0200-0202 (598 groups); one measure; pass iff >= 0.85 and >= best of 200 controls + 0.30.
- K1 (prereg/KEY-K1-frozen.txt, 218 codes): fitted on TRAIN glosses only (coordinate ascent on edit distance + hard-EM majority + manual curation from repeated words; tools/solve.c, tools/align.py). In-sample 0.858.
- Measure (prereg/MEASURE-RESULT.json): **0.661 vs best control 0.263 (mean 0.120) — FAIL at the 0.85 bar**; margin over controls met. Held-out burnt. Causes: 31 held-out groups absent from TRAIN and 56 seen once; the gloss is often written a little ahead of or behind its number line.
- K2 (key.tsv, frozen before decoding the targets, PREREG-2): same fit on all glossed witness frames; each code marked S (supported) or W (weak). Not separately validated.

## Result
Read in part: T1 108 of 255 cipher words sure (0.424); T2 355 of 841 (0.422) (106/255 and 348/838 before the sign check of 23 Nov 2026, below); rule of #728, sure words only (reading.md, count728_detail.txt). 234 target groups use codes absent from the witnesses.

## Historical gist
The Porte intends to conclude a treaty of commerce with the King of the Two Sicilies (Charles of Bourbon); Villeneuve warns Maurepas that it must not harm French Levant trade, reports in April a conference where he was asked about it, the line he took, and the risk that the maritime powers would use the occasion to obtain advantages. The Ottoman-Neapolitan treaty was signed in 1740.

## Gaps
Codes absent from the witnesses (234 target groups); weak values; gutter losses on left pages (0061 L, 0062 L, 0093-0096 L). More glossed letters of 1737 in AE/B/I/414 (or the register copy at La Courneuve) would give a fresh held-out portion and close many holes.

## Sign check, 23 Nov 2026

Level sought: "AI decipherment, human-checked on a sample of signs" (`outcome.sign_check`, held in `sign_check_pending.json`
until the field is in profile.schema.json; files in `sign_check/`). It checks how nine doubtful digits are written, not the
key as a whole, and it changes neither the class nor the state (read in part).

**Sheet.** Twelve questions: nine targets and three controls. Each question boxes one digit and offers three shapes cut from
sure code groups of the same hand (same letters), plus "none / other shape", "cannot tell", "illegible" and "not a sign". No
gloss, reading, value, place or date was shown. The three controls are digits of sure groups with a known answer (8 of 238,
3 of 318, 5 of 495); **all three correct (3 of 3)**. The nine targets are digits of groups that the transcription had left
unsettled (two blind passes disagreeing, "?" in both, or an arbiter reading marked probable) and whose other digit forms
would give a different word: **all nine answered with the shape that makes the word** (V1 3, V2 9, V3 1, V4 2, V5 5, V6 3,
V7 3, V8 6, V9 0), i.e. confirmed in the expected direction; no target was corrected or left open.

**Who did what.** The checker is Brice Dudout (a member of the project, not an independent reader). An AI model (Claude Opus 5.5)
built the selection rule, cut the thumbnails, built the sheet, scored the answers and read the remarks. The answer key
(which option is which) stayed private until the answers were exported. No image, crop or thumbnail is committed: the
images are Archives nationales study images, not reproduced.

**Rule.** `sign_check/sheet-V-rule.md` (in French, as written), SHA-256
833589ddccc9c3e29834bfae32ef099fee6ba15fda96b043457e1d772e09a653, written and hashed before the thumbnails were cut and
before any answer. It has a written integration clause (section "Intégration"), applied as written, with no change.
Answers: `sign_check/sheet-V-answers.json`, exported 2026-11-23T19:36:44Z, SHA-256
3266f96cd9a331a2f78f2e7227434fa7d257562e2002f2dc62654add081edd77; results: `sign_check/sheet-V-results.tsv`.

**Effect (by the clause, on a copy; merged_cipher.json, key K2 and prereg/ were not touched).** The nine groups become
"planche-sure" (marked `!` in transcription.txt) and the #728 count was redone with tools/count728.py (one change: status
`planche-sure` is accepted like `agree`). New sure words: le (0094L L06, "que le traitt..."), port (0094L L06), le (0094L L13),
de (0093L L12), quel, de and la (0095L L06, "quel on fera au pr[ès] de la"), par (0061L L03), a (0062L L04); the null
318 of 0094L L11 stops being a hole. The nine groups fit the context we already had; the sign check settles the digit, it
does not add values to the key.
- T1: 106 -> **108** sure words of 255 (0.416 -> **0.424**).
- T2: 348 -> **355** sure words of 841 (0.415 -> **0.422**; the word segmentation of two lines changes the number of cipher words from 838 to 841).
- Both: 454 of 1,093 -> **463 of 1,096** (0.415 -> **0.422**). Still read in part; key still not validated at the 0.85 bar.

**Limits.** One checker inside the project; three controls; the digits were chosen because they were doubtful and the options
were built from the same hand: a diagnostic, not a sample of the text. No person has audited the model's part. This is not a
`human_check`. The check does not touch the 234 groups with codes absent from the key.
