# Pre-registration, round 2: a key rebuilt from round 1, tested on the cipher lines nobody has transcribed

Written 11 Nov 2026, after round 1 (`PREREG.md`, one run: 0.818, a fail) and before any sign of the round-2 lines was
transcribed. The round-2 lines have not been read by anyone in this work; their copy text has (the Brienne pages
were transcribed after round 1's run), but the round-2 cipher readers do not see it.

## Question
Round 1 showed that Tomokiyo's key reads these leaves but that sign naming kept the score under the bar. Does a key
rebuilt mechanically from the round-1 lines (key v2), with the sign names fixed in one catalogue, give the copy text
on cipher lines that played no part in building it?

## Steps, in this order
1. **Sign catalogue** (`catalogue/`). A reader who has not seen the copies, the decryptions or any alignment fixes one
   name per shape and re-examines on the leaves every confusable round-1 token, writing renamed copies of the
   round-1 files to `transcription/round1_catalogue/`. No values go in the catalogue.
2. **Key v2** (`scripts/build_key_v2.py`, `key/key_v2.tsv`), built from the renamed round-1 files and the round-1
   part of the copy only (f. 406: to "laq.lle", fol. 173v l. 2; f. 410: to the end of fol. 194r). Rule, fixed here:
   - Each round-1 token is aligned to the copy (difflib, as in round 1) and given the copy string it lines up with.
   - A sign in Tomokiyo's key keeps his value unless it occurs at least 5 times, one copy string takes at least half
     of its occurrences, and his value takes under 0.3; then it takes that string.
   - A sign not in his key takes its commonest copy string if it occurs at least 3 times and that string takes at
     least 0.6 of its occurrences (an empty string makes it a null). Otherwise it stays unknown (`?`).
   - Repeat with the new key until nothing changes (at most 6 rounds).
   Token rule: `x?` → x; `a|b` → a; `#x`, `^x`, `m:x` → x; `-x` (struck) → dropped; `[?]` → unknown.
   Key v2 and the script are hashed into `results/frozen_inputs_round2.sha256` before any round-2 transcription
   comes back.
3. **Round-2 transcription**, three blind readers, one per part:
   (d) f. 406v from l. 21 to the last cipher line, and the cipher lines of f. 411v;
   (e) f. 410v, every cipher line;
   (f) f. 411r, every cipher line.
   They see the leaves, the catalogue with its exemplars, and the round-1 renamed files with their line crops (names
   only) for calibration. They do not see the copies, the keys' values, the decryptions, the alignment or any result.
   A shape not in the catalogue gets a new name and decodes as `?`. Files hashed on arrival.
4. **Copy text**: f. 406, fol. 173v from after "laq.lle" to "priant Dieu"; f. 410, fol. 194v "m'a faictes de sa part"
   to "bien disposees" (fol. 196r). From the first readings (`brienne_173r_173v.txt`, `brienne_194v_196r.txt`) with
   the second reader's settled readings applied where the collation (`transcription/second_reading/collation.tsv`)
   settles a disagreement on the image. Built into `transcription/copy_round2_406.txt` and `copy_round2_410.txt` and
   hashed before the run. Neither copy reading has seen the round-2 cipher or key v2, so this choice cannot favour
   the key.
5. **One run** of `scripts/test_key_v2.py`.

## Scoring (as round 1)
Normalise to a-z, merge i/j and u/v. For each letter, join the decrypted round-2 lines in order (d) and align to the
copy text (T) with `difflib.SequenceMatcher(None, d, T, autojunk=False)`. Score = matched characters / len(d), both
letters together; unknown signs count as one unmatched character; nulls decode as nothing.

## Control
200 keys made by shuffling key v2's values among its signs (seed 15932), scored the same way.

## Pass
Score ≥ 0.85 and score minus the best shuffled score ≥ 0.30. One run, reported whatever it gives.

Also reported, not pass/fail: the score per reader, the share of tokens decoding as `?`, and Tomokiyo's key as frozen
in round 1 (`key/tomokiyo_maisse2.tsv`) on the same tokens; signs not in his key decode as unknown.

## After the test (exploratory)
The full construction: rebuild the key from all lines (round 1 and round 2) by the same rule, list each sign with its
value, count and agreement, decrypt both letters in full, align them with the copies, and list where cipher and copy
differ in wording. The short run on f. 406r l. 13 is decrypted with that key and matched against the clear copy of
fol. 172r above "Le surplus".
