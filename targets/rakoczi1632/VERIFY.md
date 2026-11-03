# VERIFY rakoczi1632 (independent adversarial check, 3 Nov 2026)

Verdict: **fix**. Status class **read in part** stands, but the headline figure needs restating, and five items must
be fixed before a PR. Nothing here was pushed; no solver file was edited.

## 1. Blind transcription (before opening transcription, words, key or reading)

Sample: fol. 491r (scan 1199) lines 1-28, all cipher groups (433 signs by the solver's own token count), plus the
first five lines of fol. 491v (scan 1200, held-out area, about 75 signs). About 508 signs. Read from 1.4x bands of the
full-size microfilm scan, then 2-3x crops. The interlinear gloss over the sample was read by me as well.

Raw disagreements with `transcription_f491r.txt` / `heldout_f491v.tsv`: 14 numeric groups + 3 sign-class labels =
17 / ~508 = **3.3%**.

Settled on full-size crops:

| place | mine | solver | settled |
|---|---|---|---|
| l.2 word 1, group 1 | 25 | 28 | solver (28) |
| l.4 perveniens, group 7 | 25 | 28 | mine, weakly (looks 25 on the crop; both = i, no effect on reading; but this is one of the four sources of 28 = i in key.tsv) |
| l.13 coniungamus, group 7 | 68 | 65 | unresolved (5/8 ambiguous) |
| l.15 obligent, group 3 | 57 | 51 | solver (51) |
| l.15 iuramenti, group 3 | 32 (pass 1) | 82 | solver (82) |
| l.17 adversa, group 2 | 28 | 23 | solver (23) |
| l.17 adversa, group 5 | 82 (on zoom) | 32 | solver (32) |
| l.18 end, first group of substantiarumque | 86 | 80 | **mine (86)**: clearly 86 on the 2x crop; the solver's own pass 1 also had 86 |
| l.22 personis, group 5 | 46 | 40 | unresolved (0/6) |
| l.22 nobis 40.?.{mu} | 57 | 32 | solver (32 or 52, not 57) |
| l.23 voluntatem, line-end group | 86 | 66 | unresolved |
| l.24 pernicie, group 6 | 48 | 45 | unresolved (5/8) |
| l.26 inibunt, group 3 | 25 | 28 | unresolved |
| 491v nemini, group 4 | 49 | 19 | unresolved (1/4) |
| l.18 vitae sign; l.22 auxilio sign; l.23 voluntatem sign | {z}, a, a | {b}, {z}, {z} | sign-class labels; unresolved |

Settled: solver wrong in 2 places (0.4%), I was wrong in 6, 9 stay ambiguous on the microfilm (at most 2.2% against
the solver). None of these changes the sense; the ambiguities are the 5/8, 0/6, 1/4, 25/28 confusions the NOTES already
name. The transcription is sound.

Gloss check: my reading of the glosses agrees with the solver's for every glossed word in the sample except one:
**word 44 is glossed**. Above 28.32.32.62.56.58.80.66|19 the gloss "deserent." is plainly written (crop at 3x). The
solver lists it as unglossed ("-") and leaves it [?deserent]. Under the solver's own rules this word is a gloss
reading over a cipher departure (key gives d-e-e-s-e-r-e-n-t), i.e. `<deserent>`. The gloss over 80.18.25.32.66.19
reads "adveniant" or "advenient" (ambiguous); the cipher itself spells -ent, so `<adveniant>` should say the cipher
has advenient.

## 2. Rebuild

Scratch copy (f491r/, key.tsv, heldout_f491v.tsv, scripts/). `python scripts/check_marks.py f491r` -> exit 0, same
counts as NOTES; rebuilt `decryption_f491r.txt` is **byte-identical** to the folder copy.

Negative tests in the scratch copy:
- `<personis>` changed to plain `personis` -> `FAIL 46: reading "personis" not given by the key`, exit 1. Good.
- group 22 changed to 23 in "nobis" (transcription and table) -> `FAIL 60: reading "nobis" not given by the key
  (nubis)`, exit 1. Good.
- Loophole (minor, conservative direction): a needless `[?nobis]` passes when the note merely contains the word
  "sign" or "doubt". It can only lower the count, so not a must-fix.

## 3. Held-out test

`scripts/heldout.py` rerun: 79/87 = 90.8%, shuffled tables mean 5.5, max 25; identical to NOTES. It is graded against
the **contemporary gloss on fol. 491v**, i.e. an independent text, not the solver's own reading. Caveat: the
"expected" strings were aligned by the solver after seeing the cipher (hae- for "hereditatum", e dropped from
"omnes" and "impetitores", "nemini" started at the second letter). These choices are disclosed in the TSV notes but
each one can only help the score; the PR should say the alignment was hand-made. The test covers 12 words.

## 4. Counts and honest headline

Page fol. 491r: 147 words = **78 clear Latin + 69 cipher**. The 93.9% (138/147) counts the 78 words that were never
enciphered. On the cipher words alone:

- read by the frozen key: 53 / 69 = **76.8%**
- read from the gloss where the cipher departs from the key (marked `<..>`): 10 (11 if word 44 is fixed)
- not read / doubtful: 6 (5 if word 44 is fixed)
- key + gloss: 63 / 69 = 91.3% (64 / 69 = 92.8% after the word-44 fix)

And this is one of four cipher pages (fol. 491r-492v); 491v-492v are not transcribed beyond 12 held-out words. So the
document is under 95% by any count: **read in part** is right. Honest headline: "fol. 491r (1 of 4 cipher pages): 53
of 69 cipher words read by the key, 10 more from the contemporary gloss where the cipher departs from the key; 6 not
read; fol. 491v-492v not done." The 147-word figure may be given as well, but not alone.

It is a transcription job: the key was built only from Camerarius's glosses on the same page, so "read by the key"
on 491r means "consistent with the gloss"; only the 491v held-out test is independent evidence for the key.

## 5. Reading (`f491r/reading_f491r.md`)

Grade **B**. The Latin reads as continuous, coherent sense: travel orders, then the alliance conditions (oath not to
desert in good or bad fortune, aid in person, no separate peace, care of the heirs). English matches the Latin.
Weak places: [?Itinere] [?a] se (word boundary), [?agat] (41 = g from context only), [?substantiarumque] (first group
86 on my crop, which gives a key-read *substantiasque*), [?deserent] (glossed, see above), [?de]fensionem (decodes
"ie"), the final [...] (decodes a-?-e-l-a-t-u-n-t; with 44 = b as on 491v the cipher is a-?-e-l-a-b-u-n-t, perhaps
not "habebunt"), *coniungamus* where the cipher spells constr-g-amus, and ten gloss-only words. The page ends
mid-sentence.

## 6. Vendor / path grep

No hits for vendor or model names, local paths or the other terms on the contributor's exclusion list in NOTES, TSV, TXT, MD, PY.
"Transcription and reading were done by AI language-model agents" is the only AI mention, in the allowed form.
No __pycache__. scans/ holds JPGs, a 1.2 MB IIIF manifest and R639_table.txt: none of these may go into the PR.
NOTES names an internal WAINUT folder (`new_camerarius1621`); harmless, but better reworded for the repo.

## 7. Prior art

One web search (Rákóczi 1632 memoriale, adhaereamus / iuramenti sacramento, Camerarius, Clm 10401): no edition or
decipherment found. The solver's OCR check of Szilágyi 1882 found nothing. **Not checked**: Szilágyi, *Okmánytár
I. Rákóczy György svéd és franczia szövetkezéseinek történetéhez* (1873), which the NOTES themselves name and which
is the most likely place for Rákóczi's 1631-32 conditions to Gustavus Adolphus. Also the clear Latin "Bericht" on
fol. 493 discusses the same conditions. Until the 1873 volume is checked, do not call this a first reading.

## Must fix before PR

1. Restate the headline on cipher words (53/69 by key, 10 gloss-only, 6 not read; one of four pages), not 93.9% alone.
2. Word 44: gloss "deserent" is present; set gloss and mark `<deserent>`, update NOTES ("unglossed") and counts.
3. Word 41 (l.18): first group is 86 on the full-size crop (the solver's own pass 1); recheck and, if kept as 80,
   say why.
4. Check Szilágyi 1873 (Okmánytár I. Rákóczy György svéd ... szövetkezéseinek) before the PR.
5. In the held-out section say that the expected letters were aligned by hand (hae-, omnes, impetitores, nemini).
6. Keep scans/ (images, manifest, R639_table.txt) out of the commit.

---
Submitter's note: this report is as written by the checker except for one phrase in section 6, where the list of
private search terms was shortened to "the other terms on the contributor's exclusion list". Nothing else was changed.
The fixes it asks for are listed at the end of NOTES.md.
