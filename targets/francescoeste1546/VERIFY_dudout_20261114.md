# francescoeste1546: independent decode, read-bar recount and one image check (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/francescoeste1546` reads only `key.tsv`, `key_c42r.tsv` and
`transcription_c42r.txt` (not `scripts/`). Two-sign units are taken when the key has them, else single signs; top value
only. Letters of the interlinear decipherment (`clear_c42r.txt`, 381 letters) found in order in the decode:

| key | match |
|---|---|
| `key_c42r.tsv` (c. 42r key) | 320 / 381 (0.840) |
| `key.tsv`, pass A values | 313 / 381 (0.822) |
| `key.tsv`, pass B values | 302 / 381 (0.793) |

The rest is the homophone choice (`x` i/p, `a` u/v, `L` a/r/e) and the marked units of `reading_marked_c42r.txt`; the
key supports the gloss, it does not replace it, as NOTES says. No key correction.

## Read bar (README) and where the 0.969 comes from
`research/reading_audit/v10_relabel.measure` gives 0.969 (441 words) on `reading_c42r.md`. That figure is an artefact:
the file has no `## Reading` heading, so `v2_score.body_of` takes the whole file, with the preamble, the list of marks,
the notes and the clear text of the letter, and the `°` marks are not counted. Measured on the parts:

| text measured | words | holes | share |
|---|---|---|---|
| whole file (v10 as run) | 441 | 14 | 0.969 |
| `## Italian` section | 139 | 13 | 0.914 |
| the cipher passages only (bold) | 90 | 12 | 0.882 |

The recorded 0.885 (85 of 96 word slots) is the right kind of count. The class *read in part* stands.

## Image check: 12 unread groups, not 11
The reading has 12 `[?]` in the cipher passages; NOTES, profile and `check_marks.py` count 11 groups. On the Estense
IIIF image of c. 42r (canvas 1, full-size crop of L11), L11 begins with `e T` under the digits 6 4, then the clear words
"me ne allegro però, perchè fra tanto", then `n o q` under 6 and 4, then the cipher of "venendo". These are two
groups, which `check_marks.py` merges because it counts runs per line (`validation/unglossed_c42r.tsv` lists them as one,
"c0L11 0-4"). The reading is right to give two `[?]`. With 12 groups the share is 85/97 = **0.876** (not 0.885).
Class unchanged.

## Not done
cc. 42v-43r not transcribed or checked; no other sign re-read on the image.
