# Pass 5: key, decoder and transcriptions (written before the freeze, 27 Nov 2026)

Pass 5 answers Dan Bourdeau's point 4 on PR #957 (review of 25 Nov 2026): the second-series figures not yet transcribed (inside the circles of ff. 52r-53r, the four figures of f. 54r, f. 97r and f. 97v) and the looped-sign words of the other texts. Pass 1 stays the figure of record. Passes 2-4 stay as filed. No decoded word is emended.

The checks were done with AI tools and no person checked each record by hand.

## Declared changes
1. **Key: none.** `KEY_V5.tsv` is a byte copy of `pass4/KEY_V4.tsv` [checked: diff empty].
2. **Decoder: none.** `scripts/decode_p5.py` is a byte copy of `pass4/scripts/decode_p4.py` (rules C1-C5 of `pass3/RULES_V3.md`, C2 from pass 4). Run once with C4/C5 on (figure of pass 5) and once off (variant).
3. **T2, transcription: 15 words changed from `Dl@` (us) to `X@` (is)** in the training leaves (3 on f. 4r, 6 on f. 4v), H2 (5) and H3 (1), after the 51 `Dl@` words that pass 4 had not re-looked at were looked at on the image (`DL_CHECK_P5.tsv`: 30 kept, 15 changed, 6 unresolved and kept). Where the transcription had `X Dl@` and the image shows one sign, the pair becomes `X@`. H1r and H4: no change.
4. **New transcriptions** (never decoded before): `tx/S2_INNER_v5.txt` (ff. 52r-53r inside the circles, 9 figure parts), `tx/F054R_v5.txt` (f. 54r, 7 parts), `tx/F097_v5.txt` (f. 97r-v, 7 parts). Doubts: `DOUBTS_P5.md`.

## Held out?
The new texts were never decoded, but the reader knew the key and recognised words while transcribing, so they are **not blind**. The changed old texts were decoded before. Nothing in pass 5 is a blind test.

## Count (Dan's point 5, house rule as in pass 4)
Unit: the word between separators, as decoded. Sure = the Latin word, or a divine or magical name, that the place needs, no letter wrong, missing or added, no `[?]`; a bar `~` on a full word or a standard contraction does not make a hole. Every other word is a hole. read_share = sure / cipher words. Short-text floor (README Conventions): under 40 cipher words, at most 2 holes or 5%, whichever allows more. Our own 65% line binds each text.
For magical names with no fixed spelling (for example the names in the f. 97r inner ring) a word is sure only if the same name is attested in that form in the volume's own clear text or in the standard divine names (tetragrammaton, adonai, sabaoth, agla, alpha, omega, messias, the four evangelists and the four archangels); otherwise it is a hole.
Tags: for a word identical to the pass-4 decode at the same place, the pass-4 tag (`pass4/WORDS_P4.tsv`) is kept; every other word is tagged by this agent after the decode, one tagger, no separate judge, each hole with a reason in `TAGS_P5.tsv`.

## Controls
`scripts/control_p5.py` = `pass4/scripts/control_p4.py` with the pass-5 text list: (a) 5,000 key shuffles (the 73 single-sign values permuted) at seeds 20261112 and 7; (b) 5,000 ciphertext shuffles per seed (signs of each text permuted across its word slots, real key), real text ranked. Statistic: mean log10 p per character under the same Latin 4-gram model.
