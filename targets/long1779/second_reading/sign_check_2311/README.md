# Blind sign-shape sheet of 23 Nov 2026 (system B), record

Status of the target is unchanged (decoded, not read). This folder records one check on the look-alike pairs of
system B, made by Brice Dudout (human reviewer) with Claude, at Andrew Beling's request on PR #670.

- Images: NARA National Archives Catalog 4160708_00399 (image 16), _00400 (image 17), _00408 (image 25); public
  domain. The crops shown to the reviewer are not included here.
- `REGLE-SELECTION.md` (in French): the selection and integration rule, written and hashed before any crop was made
  (`REGLE-SELECTION.sha256`, sha256 053f63a5...685d). Seven target signs and three controls taken from words already
  held as certain (t, y, h). Examples were taken from the alphabet Long wrote himself (16R lines 1-2).
- `answers-2311-long1779.json`: the reviewer's answers as exported by the sheet (2026-11-23T21:37:55Z). The reviewer
  saw one boxed sign per question, numbered shapes, no reading and no gloss.
- `results.tsv`: what each answer means and what was done.

Outcome: the three controls passed. Four words go from M to H in `second_reading.tsv` (W0720 love, W0763 my,
W0769 me, W0943 which): once the one doubtful sign is fixed by its shape, each whole word reads by
`key_systemB_frozen.json`, no value added. W0710 stays M: the sheet settles its first sign as m (so "more", not
"wore"), but its third sign is the r/s look-alike, read r only because "mose" is not a word. W0961 "seeing" and
W0966 "last" were answered "neither / other form" on the r/s pair: one form in Long's hand, as NOTES.md says.
W0748 "down": at x5 its first sign is a straight bar detached from the o; the loop seen at lower zoom is the junction
(segmentation, not shape).

Count of certain cipher words if the four rows are carried into `reconciled_transcription.tsv`: 513 -> 517 of 1,041
(49.3% -> 49.7%); certain + probable unchanged at 775. That file and the profile figures are not changed here.
