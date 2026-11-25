# Plan, written before any transcription or decoding: lead 892, the four remaining items

Written by an AI agent (Claude Opus 5.5), 23 Nov 2026, about 10:25 Eastern. Not checked by a person.
Hashed (SHA-256) into `PLAN_malvezzi_rest.md.sha256` before any transcription is decoded and before any witness is
transcribed.

## Pieces (line crops in `lines/`, cut by `work/cut.py` from raw images in `sources/raw/malvezzi_rest_2026-11-23/`)

| Item | Lines | What |
|---|---|---|
| 8-2-24 (Ferdinand to Malvezzi, Vienna, 25 Mar 1550, Latin) | P01-P20 (image 1), Q01-Q06 (image 2) | the whole cipher, 26 lines, between "Nobilis fidelis nobis dilecte." and "Nostram benegratam ..." |
| 9-1-2 (Ferdinand to Malvezzi, Augsburg, 3 Oct 1550, Latin) | N01-N03 (image 2) | the whole cipher, 3 lines, after "uteris." |
| 8-3-10 (Malvezzi to Ferdinand, 22 Apr 1550, Italian) | M01-M10 (image 1, fol. 160r) | the two cipher passages on the first page (10 lines). The about 40 cipher lines on fol. 160v-161r (image 2) are left out by choice, for time; they are not scored. |
| 8-2-22 (Malvezzi to Ferdinand, 24 Mar 1550, Italian), original | S01-S04 (image 3, left page), E01-E06 (image 4) | two of the four cipher passages of the original (10 lines). The two long passages on image 3, right page (about 36 lines), and the duplicate (images 5-8, cipher without gloss) are left out by choice. |

Disclosures, before any test: (1) I have looked at all images at reading size while cutting lines. 8-2-24 lines 1-3
carry a modern pencil decipherment between the lines (I read "quamvis tibi per proximas litteras nostras
commisimus ..."). Every cipher line of 8-3-10 and 8-2-22 (original) carries a 16th-century decipherment between the
lines in Italian. (2) I read the whole 19th-century decipherment of 9-1-2 (image 3, one sentence) before writing this
plan. (3) I have seen the draft 8-2-10 fol. 74 only as an 800 px survey image (not read). The transcribers see none
of these witnesses as text; the interlinear glosses are partly visible in their line crops but they transcribe sign
shapes into codes and are given no values.

## Frozen key

The same as the 8-3-12 test (`output/malvezzi1550_2026-11-23/PLAN_malvezzi1550.md`): upstream
`targets/malvezzi1548/KEY_BRIEF.md` (SHA-256 66f98502...93fd), linked to sign codes by
`output/malvezzi1550_2026-11-23/sign_values_frozen_key.json` (SHA-256 50a3a583...f127), decoded by the same rules
(`value()` in `output/malvezzi1550_2026-11-23/work/decode.py`: candidate sets q = e|u, 8 = d|mm, b = n|null taken as n;
numerals 12-16 doubled letters; nulls n, z, and the clear words Cum, Porro, Spo, Dar, atque, etiam, idcirco, Dac, Der;
Ras = Imperator Turcorum; signs not in the key are holes). Unchanged.

- **Primary score**: this mapping, as frozen.
- **Secondary score, declared now**: the same mapping plus the three link corrections found on 8-3-12 (square u `U`
  = g, which is KEY_BRIEF's Sh-like g; `^` = h, KEY_BRIEF's turned y; the looped sign `??` = q, not in KEY_BRIEF).
  This tests on fresh text what 8-3-12 taught. Nothing else will be added after decoding.

Code words other than Ras keep the KEY_BRIEF values only if a transcriber writes them as clear words (ki = Rustanus,
ka/ke = Passa, Mis = Justus de Argento); others (for example Mus, Mes) are holes.

## Transcriptions

Two of every line, each by a separate helper agent (Claude Opus 5.5, medium effort) that sees only the line crops and
the blind sign sheet `output/malvezzi1550_2026-11-23/sign_sheet_blind.png` (codes, no values, no plaintext, no
witness). T1 and T2 do not see each other. Sign-by-sign agreement reported per item (aligned per line).

## Witnesses (transcribed by me after this file is hashed)

- 8-2-24: the clear draft (Reinkonzept), HHStA Türkei I 8-2-10 (AIS 7048141), fol. 74, images 9-10, the passage
  that corresponds to the cipher. Where the draft has words struck through or added, the final wording is used.
- 9-1-2: the 19th-century decipherment, image 3.
- 8-3-10 and 8-2-22: the 16th-century interlinear decipherment over the scored lines, transcribed letter for letter as
  written (abbreviations with a clear mark expanded; names as spelled).
- For the two Italian letters also: whether Austro-Turcica prints the cipher passages, tested by HathiTrust full-text
  phrase searches (mdp.39015038445451, search only) on phrases taken from the interlinear decipherment. This is
  reported, not scored.

## Test (per item, the same as the 8-3-12 test)

1. Decode each transcription mechanically (nulls dropped; holes `?`; candidate sets kept).
2. Letters only, lower case, u=v, i=j (and for Italian also y=i), ae=e. Global alignment of the decoded string to the
   witness string (match +1, mismatch -1, gap -1). Score = agreeing letters / letters of the witness.
3. **Pass marks**, primary score on T2: 8-2-24 **0.85**; 9-1-2 **0.85**; 8-3-10 and 8-2-22 (Italian, Malvezzi's own
   hand, a cursive gloss as witness) **0.80**. T1 reported too.
4. Controls: 200 keys made by shuffling the values among the sign codes (null and hole status kept), seed 1550, scored
   the same way. The key must beat the best control; for the 3-line 9-1-2 this is the main check.
5. Words read: a witness word counts only when every letter is matched. Say whether the decode builds sentences.
6. Where the draft or a gloss differs from the decode, list the places, and say from the image which is right only
   where the sign is clear.

A miss is reported as a miss. A draft that differs in wording from the sent letter lowers the score and stays in it.

## Not scored: 8-3-12 comparison

For 8-3-12 (already scored at 0.924), every place where the decode of T2 and the 19th-century decipherment differ is
listed from `key_gap_occurrences.json` and the alignment, and each is checked on the line image.
