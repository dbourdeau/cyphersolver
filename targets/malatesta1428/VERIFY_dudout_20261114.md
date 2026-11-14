# malatesta1428: independent decoder; the repository's pre-key transcription matched against the corrected one (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/malatesta1428` applies `key.json` to `transcription_tomokiyo_corrected.txt` (not
`dec.py`) and aligns each run with `texts/p1_reading.md`. Run 1 (66 signs), run 2 (82) and run 3 (160) give the reading
letter for letter. The only differences are the unread sign 23 and the four letters the scribe left out, which
`p1_decryption.md` marks: cas(s)andis, dis(c)rimine, ef(f)ici, c(o)mitem.

## The two transcriptions, sign by sign
NOTES says: "We did not diff the two transcriptions beyond that." This check does that diff. `p1v2.txt` is this
project's own sign-by-sign pass of 22 Sept 2026. It was made from the DECODE image before any key was known, with its
own sign names. The script aligns it with the corrected Tomokiyo/Prizmic transcription. The alignment is seeded only
with the six name pairs that NOTES reads at the start of run 1. Each p1v2 name then takes the key value it meets most
often.

- With p1v2's colon `:` counted as a sign, and `|`, `/` and `.` dropped as separators, the two have the **same length,
  308 signs, with no insertion or deletion**. 293 positions have the same value.
- Every p1v2 name stands for one sign of the corrected transcription, except in three places:
  - `ss` (32×) covers both `ss` = e (11) and `ss2` = m (21). Our first pass did not separate the two long-s forms.
  - `oo` (11×) covers `48` = c (8) and `49` = x (3).
  - `v` (10×) is `V` = o nine times. Once it is the null `v`, in *serenis[ ]sima* (run 3). Our pass named that sign
    `v`, not `vb` as it did for the other null in run 1.
  All three are differences of naming. In none of them does a position disagree in shape.
- Besides the double slash = i and the three dots = a (NOTES), the **colon `:` is sign 10 (v)**, 10 times. Our first
  pass had set it aside as a separator. That is the rest of the "262 against 308" gap.
- Sign 23, the unread one, is p1v2's `g` ("flat-topped ʒ/g with descender, L05 only"). It is a separate shape in both
  passes, and the only one of its kind.

So a reader who had no key and did not know Tomokiyo's file saw the same 308 signs in the same order. This is an
independent check of the transcription that carries the reading, not only of the key.

## Read bar (README)
`v10_relabel.measure` on `texts/p1_reading.md` gives 1.0 (176 words). `read_share` recorded is 0.997 (307 of 308 signs).
The reading file does not mark the unread sign before *delliberet*, or the doubts of the clear text (*prepositum?*,
*fratrem?*, *sensu?*, *assi(?)*, *(?)dissere(?)*) that `p1_decryption.md` keeps. So v10 sees no hole. The class is
unchanged either way (above 0.95).

Key correction: none.

## Not done
No image check: the DECODE image is not public (account needed), and our rules forbid reusing it. The `ss`/`ss2` and
`48`/`49` splits were not checked on the image.
