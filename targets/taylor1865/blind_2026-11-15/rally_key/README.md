# A new key, RALLY TO THE FRONT: the second 11 April 1865 telegram on vol. 11 frame 0046

15 November 2026, Andrew Beling, with AI agents (Claude, Opus). All image readings are by AI readers; no person has
checked them. Telegram files: `../../v11-0046b-maury_{transcription,decryption}.txt`, `../../v11-0046b-maury_reading.md`.

## Result

The telegram that failed every known key in this folder's blind test (`../TEST_PLAN.md`, T11) reads under a 15-letter
key not found in any source we could open: **RALLYTOTHEFRONT**, ordinary Vigenère (plain = cipher - key), key letter 1
on the first cipher letter, advancing over cipher letters only - the same rule as the telegrams around it.

> Meridian, April 11th 1865. Maj. Genl. D. H. Maury, Mobile. Let me know EXACTLY HOW LONG YOU WI[L]L HOLD THE CITY as
> the RUNNING OF THE TRAINS DEPENDS on that. If you can HOLD ON UNTIL NINE O CLOCK TOMORROW Can have four or five
> ADDITIONAL TRAINS THERE. E. Surget, A.A.G.

One letter is a correction against the image (cipher letter 20: the clerk's T where WILL needs J; a hole). The other
letters the reading needs are readings the strokes allow (`../../v11-0046b-maury_decryption.txt` lists each).

## How it was found (`key_search/`)

A key-search worker, after a test plan frozen at 15:24:52 UTC (`key_search/TEST_PLAN.md`, `PLAN_FROZEN.sha256`):
(a) period: 15 ranks first of 1-20 for both readers, weakly (`a_period.txt`); (b) the known keys used other ways
(Beaufort, reversed, restarted, tableau slip): **miss**; (c) a list of literature keys: **miss**; (d) crib dragging:
**miss / not informative**; (f) an unconstrained hill-climb over all 15-letter keys: on reader B1's text it returned
RALLYTOTHEFRONT (score -4.857 against 100 hill-climbed shuffles, best -5.915); on B2's it stopped at GQHAYTOTHEFRONT
(11 of 15 letters). **Its calibration missed its own mark**: it was to recover at least 12 of 15 key letters on 5 of 7
telegrams of known key; it did so on both readers for 3 of 7, on either reader for 5 of 7 (`f_calibration.txt`). The
key is an English phrase although the search did not ask for one. (e) with the fixed key: 20 of 25 groups give words on
B1's letters and 18 on B2's (mark 17), beating every control (`e_candidate.txt`). Scripts as run; paths edited.

## Verification (`verification/`)

By a second agent that had not taken part.

1. Two new blind transcriptions from the image (helpers A and B, told nothing of key or plaintext; frozen before any
   decryption, `helperA/`, `helperB/`). Both 107 letters, 22 dash-separated groups (25 if three line-end joins split).
   A and B agree on 104 of 107 letters; with the earlier readers B1 and B2 on 98-101 (`agreement.txt`).
2. Frozen test (`TEST_PLAN_verify.md`, run once, `results_verify.txt`): groups giving dictionary words on each
   helper's first choices, mark 15 of 22 and 17 of 25 on both, every control below. **Miss**: 11 of 22 and 12 of 25 on
   both helpers. Controls: 400 random English-like keys at most 5 of 22 (8 of 25); the four known keys at all offsets at
   most 5. The helpers read Y for V (letter 1), D for the gutter M (letter 7) and E for all six of the clerk's F; the
   dictionary also lacks DEPENDS and TRAINS (inflected forms).
3. Blind letter-shape check (`TEST_PLAN_verify_addendum_tick.md`, written before the run; `tick_check/`): this clerk's
   E carries a separate tick at the lower right. Fourteen E/F tiles, shuffled, classified by a third agent told nothing:
   12 of 14 as the key predicts (mark 12). The six letters the key needs as F (12, 16, 34, 64, 76, 81) were all called
   F; letter 64 and the final E (107) were "unclear".
4. Letters compared on the image by the verifier: letter 1 is this clerk's V (no descender; his Y in YYS has one);
   letter 20 is his T (same form as letter 19 and the T of TYQ), not his hooked J; letter 77 is a light open C with a
   heavy blot at the foot, not his looped Q.
5. The key on every other cipher stream of this folder (all `*_cipher.txt`, the provisional runs of fr. 0044 and 0045,
   the first 11 April telegram including its nine unread words, on three readers' letters), all phases, against 400
   random keys: no hits (`other_telegrams_results.txt`).

## Pencil marks

Both blind helpers, separately, found faint pencil numerals ("15", some read "13" or "5") over cipher letters 30, 45
(very faint), 60, 75, 90 and 105, none over letter 15, and an unclear small mark over letter 20 - the one letter that
the reading cannot take from the image. The verifier saw the same. Every fifteenth letter from 30 on is marked: someone
counted a 15-letter key from the first cipher letter. Who, and when, is not known; there is no interlinear plaintext.

## Is the key documented?

Not in anything we could open: this folder and the rest of the repository; Official Records ser. I vol. 49 pts. 1-2;
W. F. Friedman, *Lecture No. 4, Codes and Ciphers of the Civil War*, and *Introduction to Cryptology IV* (both list
COMPLETE VICTORY, MANCHESTER BLUFF, COME RETRIBUTION and, from one example, IN GOD WE TRUST); W. R. Plum, *The Military
Telegraph during the Civil War* (1882), vols. 1-2; D. H. Bates, *Lincoln in the Telegraph Office* (1907); Internet
Archive full-text search for the phrase with "cipher", "Vigenere", "Meridian", "Maury" (only ordinary uses of the
phrase). Not opened: D. W. Gaddy's chapter in *Masked Dispatches* (the site refused the download), Kahn's *The
Codebreakers*, Gaddy's *Cryptologia* articles, *The Signal and Secret Service of the Confederate States* (lending only).

## Fit with the day

Official Records ser. I vol. 49 pt. 2: p. 1225, Gibson at Mobile on 11 April withdraws infantry and artillery "during
the night" and tells the cavalry to "cover the troops and trains"; p. 1226, Bullock at Meridian asks Maury in clear the
same day "Why remove all your troops if enemy have made no demonstration?"; p. 1226, Surget signs as Assistant
Adjutant General at Meridian on 11 April; p. 1255, Taylor on 20 April: "Mobile was evacuated by General Maury on night
of 11th". The telegram is not printed there.
