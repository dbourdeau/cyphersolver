# duben1764, system A: key_c02 (324 groups, 306 with a value), frozen 17 Nov 2026

SHA-256 of `key_c02.json`: `1813621c87e836f3b20610b544239e892726b419ea5a02fc9ff71fa768b87285` (frozen in `../aug1764/PREREG.md`).
Format as key_c01: group -> [value]; an empty value is a null.

## How it was built (from key_c01, 217 groups)
1. **Training alignment** (`scripts/align_learn.py`, `scripts/learn_iter.py`): a monotone dynamic-programming alignment of
   each system A letter that has a contemporary clear (letter 96 + 100R / L096; 6 Mar 1764 101R-102L / 102R-103L.08;
   15 June 1764 108R-109L / 109R-110L; 15 Nov 1765 / gloss) with that clear, using the current key; a known value must
   match exactly or pays an error cost; an unknown group may take 0-8 letters. A value is added when the same string is
   emitted at >= 2 occurrences flanked by matching groups (or 1 such occurrence and >= 2 in all); a known value is
   corrected when its errors outnumber its matches two to one with an agreeing majority. Iterated to a fixed point.
2. **90R-93L by sense** (`additions_from_90R-93L_sense.json`, 48 values): read in the decode of the undeciphered letter,
   each checked against the alphabetical place of the group in this one-part code (e.g. 275 f, 304 ga, 405 leursma,
   477 ob, 508 pour, 400 la, 109 ac). Each was re-checked on the four training letters: the alignment cost fell on all
   four; one ("558 ret") was withdrawn because the training alignment emits nothing for it.
3. **16 single-occurrence values** set by hand from the training alignment where the alphabetical place agrees.
Every change against key_c01 with its source: `key_c02_changes.json` (107 new groups, 30 values corrected).

## Checks
- In-sample CA (decoded letters in matching blocks of >= 4 letters): 0.966 (L096), 0.892 (6 Mar), 0.828 (15 June),
  0.919 (15 Nov 1765); permuted-key controls about 0.08-0.10.
- Held-out, pre-registered, 20/31 Aug 1764 (`../aug1764/`): CA 0.831 vs controls max 0.078: FAIL at the 0.85 bar.
- 90R-93L: key_c02 knows 1,492 of 1,585 groups (94 %, key_c01 80 %). Strict reading 698 sure words of about 895 (0.78),
  `../letter90/reading_90R-93L_key_c02_tagged.txt`: still "read in part" under the 95 % rule.

## Limits
Values from step 2 are read by sense in a letter with no clear; some may be wrong (e.g. 405 "leursma" rests on the
gloss "L: L: M: M:" of 1765 and on 90R-93L). Some groups have alternative cuts (213 d / de, 448 n / on).
