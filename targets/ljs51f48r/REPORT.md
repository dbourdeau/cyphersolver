# LJS 51 ff. 48r l.8 - 48v l.13: deciphered (27 Nov 2026)

Status: key recovered from ciphertext only, then confirmed against a plaintext elsewhere in the volume.

## Result

The block (229 signs by eye, 52 groups) enciphers the first two thirds of the rhymed-prose riddle that the compiler
gives in clear on f. 21r l.7 - 21v l.2 (the answer to chain 20r.8, the third of al-Jawlani's test pieces):

ولينه الاعطاف واسعه الاكناف وطيبها مباح على انها تجافاها اهل الصلاح تزور اذا جن الليل وترحل عند الصباح ترميها العسي
وتطعنها الاسنه وهي معدوده من نعيم اهل الجنه وجمعها يستر بالظهور وافتراشها بعقد جايز غير محذور يحمد منها ما يذم في
المذاهب وظهرها اوطا ظهر للراكبان جمالها ربها جملته

It stops at جملته; the rest of the clear text (وازدها نعمته فاذكر اسم ربك ...) is not enciphered here.

## How it was found

1. The 47r key does not fit (`keys_eye/47r.1.json`; the earlier attempt below): same sign shapes, different key.
2. Simulated annealing over one-to-one keys, word dividers kept as spaces, scored with `lang` model `ar-mamluk`
   (`anneal_sp.py`, 6 restarts x 40,000 steps; no plaintext given). Restart 1 reached -2.51 per character and read
   "... اهل اصلاح تثور اذا ب ن الليل وترحل عند الصفاح ترميها ... وهي معدوده من نعيم اهل الجنه ...", which is the
   f. 21r riddle. Other restarts scored -2.64 to -3.24 with partial words.
3. `verify.py`: alignment of the 229 signs to the f. 21r text (DP, key re-learned from the alignment, 6 rounds):
   - 218 of 229 signs take their key letter (95.2%); 5 surplus signs, 8 dropped letters; the block covers 232 of the
     riddle's 293 letters.
   - The key is one-to-one: 27 sign shapes, 24 of them a single letter; the commonest sign (W, 44) is ا, the
     triangle-over-bars (TB, 24) is ه, X is ل. Key in `key_48r.json`.
   - The annealer reached the text blind, so the reading is not an artefact of the alignment; the alignment figure
     itself is self-consistency.

## What the cipher settles in the clear text (record of 20r.8, read from the master)

- ترميها where the record reads توهمها; يحمد منها where it reads وخمد منها; العسي confirmed (the record has العسى[?]);
  اوطا ظهر confirmed. The cipher writes تجافاها with an extra ت (تتجافاها) and drops the ل of الصلاح (اصلاح).
- Remaining mismatches (11 signs) are mostly look-alike shapes in this transcription (HK, OM, AY, XN, K) and need a
  check at 2x.

## Why it looked unanswered

The plaintext stands 28 leaves earlier (f. 21r), under another block (20r.8). The compiler's remark on 49r (solved
"only after much toil") may refer to this block or to the short one on 49r l.1-4 (not examined). Chain 20r.8 was
found at chance in `keys_fork/` (its record notes a change of sign style at 21r l.1): 20r.8 and 48r.8 are two
encipherments of the same riddle; 20r.8 should now be re-keyed with this text.

## Earlier attempt (same day, sub-agent): 47r key; riddle verses 1-5; 49r verses; answer verses: all ruled out
(see the files align_*.py, control_align.py, lm47.py).

## 2x re-read on the master (27 Nov 2026; `recheck_2x.md`, `transcription_v2.txt`, `verify_v2.py`)

Every flagged position was re-read at 2-3x. Five were transcription errors (an extra W on 48v l.2, a missed SW on
48v l.10, HK for SW on 48v l.12, a phantom W on 48v l.13, and the SW over a divider on 48v l.10); six dividers were
misplaced. With v2: **220 of 228 signs (96.5%)** take a one-to-one key (`key_48r_v2.json`). The rest are the scribe's
slips (الاكانف with letters swapped, وطيها, تتجافاها, وجهها, جملها, منه ما) and places where the cipher corrects the
clear text of 20r.8: ترميها (record توهمها), يحمد (record وخمد), and القسي "the bows" (record العسي[?]; the three-pronged
OM sign is ق in both its places). Rule-out (`ruleout.txt`): the decoded block against all 206 plaintexts in the book:
20r.8 95.2%, next best 22%, median 9%.
