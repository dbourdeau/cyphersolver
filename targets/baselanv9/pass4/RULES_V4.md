# Key v4 and transcription v4 (pass 4): written before the freeze, 27 Nov 2026

Pass 4 answers Dan Bourdeau's re-review of PR #957 (25 Nov 2026, on head 57aae52, pass 2). Pass 1 stays the figure of record. Passes 2 and 3 stay as they were filed. Pass 4 is a new version with its own figures. No decoded word is emended.

The checks were done with AI tools and no person checked each record by hand.

## Declared changes

1. **K1, key: `Tk@` = ru** (was re in `keyleaf/KEY_LEAF.tsv` and `pass3/KEY_V3.tsv`). Ground: on f. 99r the label over the tack with a big loop reads "ru", in the same letter forms as "rum" over the same sign with a dot (`crops/f099r_ru_rum.jpg`). The first-pass alignment also gave ru 9 of 9 times (Dan's point 1). [measured: `KEY_V4.tsv` differs from `KEY_V3.tsv` in this row only.]
   - Effect on the texts: no transcription in pass 4 has a bare `Tk@`. The 11 words Dan counted are written `Tk^@` (f. 4r 5, f. 4v 4, f. 15r in pass 2's transcription 2) [measured: grep of the transcriptions]. Pass 2 decoded them re + m. Pass 3's rule C1 already reads `Tk^@` and `Tk@^` as the one sign rum, and pass 4 keeps C1. So pass 4 gives rum in those words. The key row is corrected so the key file matches the leaf.
2. **C2, nasal dot on a two-letter sign (Dan's point 2): kept from pass 3, unchanged.** A dot below (n) or above (m) on a vowel + consonant group sign (ar er ir or ur, as es is os us, at et it ot ut) puts the nasal after the vowel: et_ = ent, so obedient, ueniant, ruebant, surgens. Pass 3 declared this rule (`pass3/RULES_V3.md` C2) and applied it to H1r, H4 and the S2 rims. Pass 4 applies it, unchanged, to every text decoded here. That includes the 62 first-series rims and the training leaves, which pass 3 did not decode.
3. **T1, transcription: 16 rim words changed from `Dl@` to `X@`** (Dan's point 3). Every rim word that passes 2-3 wrote with `Dl@` was looked at again on the image (`DL_CHECK.tsv`):
   - 16 show the leaf's "is" form (an x whose right arm sweeps up into a big loop) and are now `X@`. Where `X Dl@` had been written, the x and the loop are one sign.
   - 16 show the leaf's "us" form (a delta whose ascender curls into a small loop) and stay `Dl@`.
   - 2 are unresolved and stay as written: S1-012 (a big loop round a delta-like sign) and S1-079 (an ink blot).
   - The value of `Dl@` stays us, as on the leaf. The 12 `Dl@` words of H1r and H4 and the 39 of the training leaves, H2 and H3 were not looked at again; they stay as written (Remaining gaps).
4. **Decoder: `pass3/scripts/decode_p3.py` unchanged** (rules C1-C5 of `pass3/RULES_V3.md`), copied as `scripts/decode_p4.py` with one switch, `NO_C45`. The switch turns off C4 (`Cl Tq` = rte) and C5 (x = ch in the chi-rho-iota abbreviation), the two rules that are not on the leaf. The decode is run once with the rules on (figure of pass 4) and once with them off (variant), both after the freeze.

## Texts decoded (all frozen in `FREEZE_P4.txt` before the decode)

| text | file | source | held out? |
|---|---|---|---|
| TRAIN f4r | `tx/f004r.txt` | pass 2 `keyleaf/tx2/`, unchanged | no (training leaf of pass 1) |
| TRAIN f4v | `tx/f004v.txt` | pass 2, unchanged | no (training leaf of pass 1) |
| H1r f. 15r l. 1-12 | `tx/f015r_H1r.txt` | pass 3 re-read, unchanged | no (decoded in passes 1-3) |
| H2 f. 159r | `tx/f159r.txt` | pass 2, unchanged | decoded in passes 1-2 |
| H3 f. 34r rims 3-4 | `tx/f034r_p34.txt` | pass 2, unchanged | decoded in passes 1-2 |
| H4 f. 25r l. 1-12 | `tx/f025r_H4.txt` | pass 3, unchanged | decoded once, in pass 3 |
| S1 rims, 62 | `tx/PENT_S1_v4.txt` | pass 2 + T1 (13 words) | decoded once, in pass 2 |
| S2 rims, 11 | `tx/PENT_S2_v4.txt` | pass 3 + T1 (3 words) | decoded once, in pass 3 |

None of these texts is held out in pass 4. Each was decoded before, and the reader had seen the earlier decodes. The figures below measure the corrected key and transcription, not a blind test.

## Count (Dan's point 5): sure words per text, cipher words only

- Unit: the word between separators, as decoded. A word broken with "=" at a line end is one word.
- A word is **sure** when it is the Latin word (or a divine or magical name of the passage) that the sentence needs, with no letter wrong, missing or added and no `[?]`. A bar `~` on a full word or a standard contraction (dni~, ch~ri) does not make a hole.
- Every other word is a **hole**: a slip, a transposition, a `[?]`, a word with no sense, a lone `[?]`.
- `read_share` = sure / cipher words. Short-text floor (README Conventions, 19 Nov 2026): a text of fewer than 40 cipher words may have at most 2 holes or 5%, whichever allows more. Our own 65% line binds each text and each rim.
- The tags are this agent's own (Claude Opus 5.5), made after the decode, one tagger and no separate judge. Where a pass-4 word is the same as the pass-2 decode at the same place, the pass-2 separate judge's tag (`keyleaf/judge/JUDGE_OUT.tsv`) is used: S = sure, E or N = hole. Every other word is tagged by this agent, and each hole is listed with a reason in `SCORE_P4.tsv`.
