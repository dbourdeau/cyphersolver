# balfour1781: independent decoder without a language model, read bar, one image check (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/balfour1781` reads only the key constants of the key file `decode.py` (`RING`
and `TABLES['C']`, parsed as literals; the script is not run or imported) and `transcription/p7xx.txt` (L lines;
N lines only for the decipherer's "should be 13" on p. 718). Its rules are written from NOTES.md and use **no
language model**:
- A, B: dash groups run across line ends; numbers >= 30 are fillers; a group of fillers holding exactly one number
  below 30 (at least two fillers, at most one illegible) is an indicator; a line end is a group break only next to
  an indicator group of five numbers or more; a lone number is a numeral in clear unless it reads *a*; the setting
  simply carries from sheet to sheet (no `START` table).
- C: the fixed table, fillers from 40.

| | letters | agree with decryption_X.txt | indicators |
|---|---|---|---|
| A (Nos. 1-3) | 2,742 | **2,742 (100%)** | 31: 13 + 15 + 3, the settings listed in NOTES.md |
| B | 1,539 | **1,539 (100%)** | 4: 23 18 6 5 |
| C | 850 | **850 (100%)** | none |

So the indicators that `decode.py` decides with `en-modern` (a one-letter word padded with two fillers or an
indicator) are decided the same way by the dash rule alone, and Nos. 2 and 3 open on No. 1's and No. 2's last
setting (a=9, a=14) without being told: the two `START` values are confirmed, not assumed.

## Read bar (README)
`v10_relabel.measure` on the reading files: A 668 words, 8 holes, **0.988**; B 406 / 4, **0.990**; C 226 / 7,
**0.970**. The recorded `read_share` values are 1.0, 0.994 and 1.0. All three stay above 0.95: the class (read) does
not change. The holes are [?] and conjectures ([Hightown?], [Pedee?], [the next?]); B's *Feb[ruary]* is an
abbreviation counted as a hole by v10 (known artefact).

## Image check (NARA, M247 roll 65, image 570 = p. 725, Fold3 file 407653)
The one real disagreement in NOTES.md: No. 3 has the numeral 18 for the men lost, the interlinear "fifteen".
On the image, L09 opens `15 — 18 — 2, 14, …`. Over 15 the interlinear has a single letter, an **f** (the mark the
transcription takes as a "4" in the margin): 15 is the *f* that ends "loss o|f" (a=16), not a numeral, as the
decoder has it. The word over 18 is small, faint and partly struck through; it ends in "-teen", its first letters
are not clear on this microfilm scan ("fifteen" or "eighteen"). So the disagreement rests on a faint, struck word;
the cipher's 18 stands.

Key correction: none.

## Not done
The 12 illegible tokens of A and B and the open values of C (2, 3, 19, 30) were not re-read: the microfilm scan
is the only image online.
