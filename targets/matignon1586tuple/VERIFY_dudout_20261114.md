# matignon1586tuple: independent decoder, image check of f. 234r and f. 235r (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/matignon1586tuple` reads only `key.json` and `transcription/f*.txt`, and compares
with `decryption/`, `glosses_multivalued.tsv` and `texts/f*_reading.md` (no decoding script used).

- 2,152 groups, 225 of them on multi-valued labels. Every value in `decryption/` is one of the key's values for its
  label, except notation: nulls written `[NR]`, `[NUL]` ... (10), *u* for *v* in three gloss labels (RECOUVRER,
  SILVENOIT, V7) and G_LEREVENU (4). Labels `L` (6 groups, decoded c, d, e, l, l, l) and `M` (1, s) are not in
  `key.json`, as `legend.md` says. Every decrypted line equals the join of its group values.
- All 216 rows of `glosses_multivalued.tsv` point at the right group, label and decoder value.
- Decoded letters against the readings (supplied letters removed): 0.982 (234r), 0.986 (235r), 0.982 (235v),
  1.000 (237r), 0.992 (237v); lower on 234v, 236r, 236v, 238r, 238v, where unread groups are `[?]`. Outside the
  holes and doubtful words, the only differences are the gloss contradictions below.

## decryption/ not synced with the glosses (corrected)
NOTES says the readings follow the gloss where it contradicts the decoder (issues #95, #99), but the ten groups were
never changed in `decryption/`. Corrected here (each new value is one of the key's values for the label):
234r l. 7 g. 5 QUI que -> qui; 236r l. 22 g. 9 M30 n -> m; 236r l. 25 g. 1 SSL s -> ss; 236v l. 4 g. 9 M30 n -> m;
236v l. 7 g. 6 CN e -> que; 236v l. 11 g. 2 CNPOUR e -> pour; 237r l. 1 g. 1 DA d -> de; 237v l. 3 g. 4 and l. 4 g. 6
SR sieur -> monsieur; 238r l. 20 g. 7 M30 n -> m. The decrypted line strings are updated with them. Not changed:
238r l. 16 g. 6 M30, decoded *n* with no gloss, read *[?ma]* (inside a doubtful word).

## Image check (Gallica btv1b9061879d, canvases 241-242, full size)
- **234r l. 3 g. 11 (CN, recorded "q[?ue] (looped q, unclear)")**: the gloss is the 8-shaped *que* sign, the same mark
  recorded as *que* ("8, the que sign", agrees) on 236r l. 1. It agrees with the decoder (*que*). The group itself
  is a C-shaped sign followed by *n* (the CN shape is not recorded in `legend.md`). Suggest "yes": 234r unconfirmed
  2 of 251 groups (0.8%) instead of 3.
- **234r l. 12 g. 1 (DAN, decoded nn)**: not settled. The group is a straight stroke with a ʒ at its top, unlike the
  ß of DA four groups later; the gloss is a small mark followed by *da*, close to the gloss over that DA. *tira|nnie*
  needs *nn*.
- **234r l. 12 g. 9 (BQ, decoded de)**: the gloss is a d with a flourish; whether an *e* follows cannot be seen.
  Not settled.
- 234r l. 1 g. 1 (E2, the doubtful *[?ca]*): the gloss *c* is clear; the doubt is in the sense, not the image.
- **235r ll. 5-8, a blind sample**: read sign by sign before opening the transcription, 4 lines (36 groups): 35
  agree with `transcription/f235r.txt`; the 36th (l. 6 g. 3, DA) I had left unread, and it is the ß of DA. No gloss
  stands over lines 6-9, as recorded ("none").

## Read bar (README)
`v10_relabel.measure` on the ten readings equals the recorded `read_share` (0.974 ... 0.431). Without the known
artefact (in-word expansions such as *[e]xtreme* counted as holes) 237r is 0.960 and 237v 0.946; no class changes,
since on 237r 10 of 190 groups (5.3%) remain unconfirmed, over the 3% look-alike limit.

Key correction: none.

## Not done
Only 234r's three unclear groups and four lines of 235r were read on the image. ff. 236-238 (show-through) were
not re-read.
