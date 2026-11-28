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

**Pass 2** used the same protocol. The list was frozen first, then reader A's answers, then a *new* blind reader B.
- 8 more rows were posed: 42, 57, 63, 88, 110, 112, 127, and 123 (not found on the 2343 px image).
- Controls: rows 29 and 39, 2/2 correct.
- Answer to the objection that reader A set the options: for rows 4, 78 and 127, reader B got a wider crop *without
  coordinates*, had to find and describe the sign itself, and only then answered.

## Result (`errata_c_recheck.tsv`)
- Settled **a** (the record misread the page), 8 rows: 4 (last word only), 8, 11, 28, 36, 85, 96, 102.
- Settled **b** (the page has the record's form), 9 rows: 19, 20, 42 (ونظر), 45 (تطيف), 63 (مروت), 74 (علمت),
  110 (فيقتصك), 112 (درنحوا), 113.
- Still **c** after a re-read, 5 rows:
  - 57, 88 and 127: the two readers disagree.
  - 75: the tooth has no dot of its own (the cipher has ن).
  - 78: demoted in pass 2. On the wide crop neither reader could exclude a stroke before the loop.
- Not re-read, or word not found on the 2343 px image: 21 rows. They stay c.
- Row 4 is fragile. In pass 2 the blind reader found the word itself and saw the closed letter again, with low confidence.

Points that differ from errata.md's notes:
- Row 45: the page *does* show two dots over the first tooth of the interlinear word, i.e. تطيف, as in the cipher.
- Row 19: the cipher's sign for this letter is ك in لكل four times, so the corrected بكوه is the text.
- Row 20: the page has نخيل, but the cipher's first sign is the ب sign, so the cipher has بخيل.
- Row 80 (not re-read) is already answered by `keys_eye/62r.3.json`: the cipher opens with a 5-sign word (يخوتا) that
  the written text lacks. This is Bourdeau's finding, not ours.

## Limits
- The images are 2343 px JPEGs, not the masters.
- In pass 1 reader A wrote the options and the crop coordinates. Pass 2 tested free location on 3 rows: one row held
  (4), two did not (78, 127).
- 21 rows were not re-read, or their word was not found on the image.

Images: University of Pennsylvania, LJS 51, OPenn (Public Domain Mark 1.0).
