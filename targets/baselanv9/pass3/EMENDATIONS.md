# Pass 3: emendations list

**Emendations made to the decode: 0.** `DECODE_P3.txt` is the output of the one decode of 25 Nov 2026 07:55:25 UTC, byte for byte (sha256 76f334c53450a421..., the same as `judge/decode.txt`) [measured]. No letter was changed, supplied or dropped afterwards, and no transcription file was edited after `FREEZE_P3.txt` (07:55:17 UTC; hashes re-checked on 25 Nov 2026 08:07 UTC, all nine match) [measured].

What follows is everything that could be mistaken for an emendation, so that it can be checked.

## 1. Readings the sense suggests that were NOT put into the frozen files

| unit | frozen label | what the sense suggests | effect of leaving it |
|---|---|---|---|
| S2-09 word 3 | `5` (g) | a hook-sign `Hk` (leaf: sc), giving inscribe | decodes ingribe, scored N by the judge (7 letters) |
| S2-11 word 1 | `5` (g) | `Hk`, giving scribe | decodes gribe, scored N by the judge (5 letters) |
| H4 L06 word 4 | `6^` (dot above the six) | an inner-dot reading | decodes emloo, scored N (5 letters) |

The reader saw the first two only after both rims were written down, and recorded them in `DOUBTS_P3.md` before the freeze; the files keep `5` because the change was prompted by sense.

## 2. Decoder rule changes against pass 2 (made before the freeze, not after the decode)

From `RULES_V3.md`. The 73 token values, 5 pairs and 2 word forms are those of pass 2's `keyleaf/KEY_LEAF.tsv`; 73 of 73 token values are the same (`checks/VERIFY_OUT.txt`) [measured].

| rule | change | ground | on the key leaf? |
|---|---|---|---|
| C1 | `Tk^@` and `Tk@^` are one sign, rum | pass-2 decoder fault | yes (rum) |
| C2 | a nasal dot on a vowel + consonant group sign goes after the vowel (et_ = ent) | the leaf's wording; training leaf f. 4r (ruebant, fiebant) | the leaf's wording, as we read the Danish [unverified] |
| C3 | two-dot fallback widened to the nearest earlier vowel sign | pass 1's training rule (34 of 43) | no: a declared fallback |
| C4 | `Cl Tq` = rte | analogy with the leaf's rt and te | **no** |
| C5 | x = ch in the chi-rho-iota abbreviation (`X Tk Cl`, `X~ Tk Cl`) | Latin usage | **no** |

C4 and C5 are the two rules with no entry on the leaf. The figures without them are in `variant/SCORE_VARIANT.tsv` and in NOTES.md, "Pass 3".

## 3. Transcription changes to H1 against passes 1 and 2

H1 (f. 15r lines 1-12) was re-read from the full-size image before the freeze. 30 of its 80 word groups (the line filler of L06 included) differ from pass 2's `keyleaf/tx2/f015r.txt`, per line: L01 2, L02 4, L03 2, L04 6, L05 4, L06 0, L07 2, L08 3, L09 1, L10 1, L11 2, L12 3 (2 + 4 + 2 + 6 + 4 + 0 + 2 + 3 + 1 + 1 + 2 + 3 = 30) [measured: `checks/VERIFY_OUT.txt`]. The reader had seen the clear copy f. 109v and both earlier decodes, so this re-read is not blind and H1 is not held out. The doubts are in `DOUBTS_P3.md`.

## 4. Known decoder weakness left in

Rule C3 gives a for i where the x's inner dot cannot be seen: ineffabale (H4 L07, S2-08), mirabala (S2-10). Left as decoded; the judge scored each E.
