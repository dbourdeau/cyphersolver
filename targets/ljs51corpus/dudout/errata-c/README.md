# LJS 51: second look at the "c" rows of errata.md (contribution)

Prior work: `targets/ljs51corpus/errata.md` and `errata.json` (Bourdeau, origin/main 43e3b1bcfd). That pass checked
131 suspected words on the master TIFFs. Results: a = 32, b = 56, c = 43 not settled. The cipher side used here is
Bourdeau's own `keys_eye/<chain>.json` alignment (sign → letter → word). Nothing in this folder is new transcription of
the cipher.

## What was done
The 43 c rows were frozen locally before any crop was looked at (no statistical measure, so no public freeze).
Fifteen rows got two readings:
- **Reader A** (Claude Opus 5.5, not blind) cropped the word from the Penn IIIF 2343 px JPEG (lower resolution than
  the masters). Reader A added one constraint: the cipher group aligned on the word in `keys_eye` has n signs, so the
  word has n letters. Each sign was valued only by its *other* occurrences in the same chain.
- **Reader B** (Claude Opus, blind) saw only the crop and 2 or 3 options worded as shapes (teeth, dots, loops,
  uprights). Reader B did not see the record, the errata or the cipher.

A row is settled only if A and B pick the same option and the cipher count does not contradict it. Three rows that
errata.md had already settled (7, 47, 48) were put to reader B as controls. All three were answered correctly.

## Result (`errata_c_recheck.tsv`)
- Settled **a** (the record misread the page), 8 rows: 4 (last word only), 8, 11, 28, 36, 85, 96, 102.
- Settled **b** (the page has the record's form), 6 rows: 19, 20, 45 (تطيف), 74 (علمت), 78 (مص), 113.
- Still **c**: row 75 (the two readers agree that the tooth has no dot of its own, which does not decide between ن and
  ي; the cipher has ن), and the other 28 rows, which were not re-read in this pass.
- Rows 4 and 78 are fragile: reader B gave a low-confidence answer.

Points that differ from errata.md's notes:
- Row 45: the page *does* show two dots over the first tooth of the interlinear word, i.e. تطيف, as in the cipher.
- Row 19: the cipher's sign for this letter is ك in لكل four times, so the corrected بكوه is the text.
- Row 20: the page has نخيل, but the cipher's first sign is the ب sign, so the cipher has بخيل.
- Row 80 (not re-read) is already answered by `keys_eye/62r.3.json`: the cipher opens with a 5-sign word (يخوتا) that
  the written text lacks. This is Bourdeau's finding, not ours.

## Limits
- The images are 2343 px JPEGs, not the masters.
- Reader A wrote the options and the crop coordinates, so reader B's independence is about what is seen, not about
  where to look.
- 28 rows were not re-read in the time available.

Images: University of Pennsylvania, LJS 51, OPenn (Public Domain Mark 1.0).
