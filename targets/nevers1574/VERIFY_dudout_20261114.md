# nevers1574: independent check of f. 15-16 against the signs, image check of f. 15r (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/nevers1574 [-v]` reads only `f15_key.md` and `f15_signs.tsv`, and compares with
`f15_reading.md` (`research/reading_audit/verify2_nevers_*.py` not used). Since two signs carry two letters
(9 = q/s, + = f/m), the reading is enciphered back into sign classes with the key and aligned with the transcribed
signs. Normalised on both sides: doubling signs dropped and runs of one sign collapsed; name and number signs
(SS, [RM], [-d-], XX…) and unread marks dropped; y = i and final -ct = -t (the cipher writes *luy* as *lui*, *dict*
as *dit*).

| page | signs (collapsed) | agree with the reading |
|---|---|---|
| f. 15r | 978 | 942 (0.963) |
| f. 15v | 781 | 637 (0.816; ll. 2-5 unread) |
| f. 16r ll. 1-19 | 620 | 587 (0.947) |

So "gloss and decode agree word for word on f. 15r and f. 16r" (`reading_review`) holds for the words, not for
every sign: on f. 15r and f. 16r about fifty places differ by a letter or two. Most are letters the transcription
does not show (*veu[l]x*, *fai[l]lir*, *advertir* without its last r, *vou[s]*), a few are gaps in the transcription
(16r l. 6, where the line `… h …` stands for *que je vous ay bien voulu faire*), and two are regular usages that
`f15_key.md` does not list:

- **"gouvernement" is written `0 8 2 …` in all five occurrences** (15r ll. 8, 10-11, 15; 15v l. 23; 16r l. 12): the
  sign for n (2) stands where the gloss has u. Elsewhere u is 6 (*vous* 686, *pour* G86T, *jourd'huy* 786Tb6y).
- **the d-sign (b) stands for u/v three times**: 15r l. 2 `9bE` *que*, l. 8 `082bFT…` *gouvernement* (the v),
  l. 26 `9b1PTF9` *qu'apres*.

On the image (Gallica btv1b90600800, f17, full size) 15r l. 2 `9bE` and l. 8 `082bET2F+F24` are as transcribed: the
second sign of *que* is the small b-shape of *jourd'huy*'s d, and *gou-* has the same 2 as *son* (`982`) just
before it. These are the encipherer's usage (or slips), not transcription errors. Suggest a line in
`f15_key.md` ("u: 6; also 2 in *gou-* of gouvernement, 5×; b for u/v 3×"). Left to the maintainer.

## Image check of f. 15v ll. 2-5
Read at full size: the gloss over l. 2 is legible as *ayant tant d'affection*, as in the reading; over ll. 3-4 only
isolated words (*la*, *elle*) are sure. Nothing new is recovered; the gap stays.

## Read bar (README)
`v10_relabel.measure`: f15_reading.md 0.941 (= recorded), f. 21 1.0. Read in part stands.

Key correction: none to the letter values; the two usages above are additions.

## Not done
f. 16r and f. 21 were not re-read on the image; the ~50 one-letter differences were not checked one by one.
