# PREREG — key_c01 on the 15 June 1764 letter (Chiffer n:o 1, system A)

Written 14 Nov 2026, BEFORE any transcription of this letter and before any decoding of it. Brice Dudout's session (Claude Opus 5.5).
Frozen by SHA-256 (see `SHA256SUMS-PREREG`). Any change after this point goes into a dated amendment below, never into this text.

## Material (never seen by the key or by any previous decode)
- Cipher: Riksarkivet K 259 (IIIF A0073297), image 108 right ("N:o 4[?]", "St Petersbourg ce 15. Juin 1764"): the numeric lines
  that follow the clear opening ("En reponse de Votre chere Lettre du 11 de May ... de mes nouvelles"), and image 109 left
  (all numeric lines). Expected about 500 groups (≥ 150 required). The clear opening on 108R is plain text and is not used.
- Clear: images 109 right ("Till chifferbrevet av den 15 juni 1764", archivist) and 110 left, to "je suis un homme ruiné".
  This is the contemporary decipherment filed with the cipher.
- key_c01 has 217 groups, all taken from image 96 + 97 left (PR #566). No group or value comes from 108-110.

## Key
`../key_c01.json`, unchanged, SHA-256 3fcecea8afc3f0e8649c1d38ccca799bcd3ca1a5155552db0fb7b972da8fb0eb.
No value is added, removed or corrected before the measure.

## Transcription (before decoding)
Two passes of the cipher and of the clear: pass 1 by this session, pass 2 by a blind sub-agent that does not see pass 1 or
the key; differences arbitrated on the full-resolution image; the result frozen by SHA-256 in an amendment BEFORE the
decode is run. Doubtful groups are kept with "?" and counted as written (first reading).

## The one measure
`scripts/measure_june.py` = the metric of `scripts/check2.py` (PR #566, accepted by the maintainer), unchanged except the seed
and the parser (dot- or space-separated groups):
- decode every group ≥ 100 with the first value of key_c01 (empty for unknown groups and nulls);
- M = share of the letters of the normalised clear (a-z, accents stripped) covered by difflib matching blocks of ≥ 4 letters
  between the decode and the clear;
- controls: 200 random permutations of the key's values over its groups, `random.seed(1764)`.

## Thresholds (fixed now)
PROTOCOLE.md (27 Oct 2026) sets no bar for this kind of check (the maintainer noted it), and the project default
(characters ≥ 0.85 and ≥ best control + 0.30) cannot apply: key_c01 is partial (197 groups with a value, perhaps a third of the
repertory) and some values are mis-cut, so even the training letter 96 scores only 0.363 on this metric.
Reference values on this metric, all known before this prereg: 15 Nov 1765 0.545 (controls max 0.061), 6 Mar 1764 0.261 with
a clear 2.6 times too long (max 0.043), 101R held-out 0.325 (max 0.062), 96 training 0.363.

**PASS** if M ≥ 0.15 AND M ≥ (max of the 200 controls) + 0.10.
- 0.15 is below the lowest real value seen (0.261, diluted by an over-long clear) with margin for a different scribe and
  topic; 0.10 above the best control is more than 1.5 times the largest control ever seen (0.062).
**FAIL** otherwise. A fail is reported as such; the portion is then burnt for this key.

## After the measure (not part of the test)
Reading is from the contemporary clear (existing decipherment); strict count by the README rule (≥ 95 % of words read by sense =
"read"); English translation. Key values suggested by the alignment are a separate, unvalidated addition.

## Amendment 1 — 14 Nov 2026, before the decode is run
- Transcriptions frozen (hashes in `SHA256SUMS-AMEND1`): `transcr/c1764-06-15.txt` (32 lines, 108R.01-15 + 109L.01-17;
  478 groups read alike by both passes, 74 differing groups kept as first reading with "?"), `clears/p1764-06-15_clear_contemporary.txt`
  (109R + 110L, two passes nearly identical; arbitrated). Passes in `transcr/passes/`.
- Clear normalisation fixed now: [del:...] dropped, [ins:...] kept, [?] dropped, then a-z as in check2.py. The meaningless
  string "ritedriibsdoucle" on 110L.03 is kept as written.
- Parser: groups split on spaces or dots; for "a/b" alternatives the first is used; "???" and groups < 100 are skipped (as check2.py).
- `scripts/measure_june.py` is the measure; it is run ONCE, after this amendment is hashed.
