# Verification of catalogue 2346 (Griffoli to Cosimo I, figure cipher), 6 Nov 2026

> Published copy: unchanged except that one line of section 6 (a hygiene grep that named AI vendors) was removed.
> The figures below predate the fixes made after this check (see NOTES.md, "Changes after the independent check").

Independent, adversarial check by WAINUT. The verifier is a separate AI language-model agent. It read only NOTES.md and
SIGN_CONVENTIONS.md, then transcribed a sample from the scans and wrote that text into this file before it opened any
transcription, decryption, reading or key file. Section 1 is that blind text, unchanged.

Verdict: **confirm**. The statuses in NOTES.md hold: k316 (2 Feb) is a transcription job, and 443 c. 315 and
451 c. 25r are **read in part**. Neither is "read". The digit transcription is very good. In the held-out lines the
verifier's blind text matches the solver's digit for digit. The key holds and the held-out test is real. `check_marks.py`
passes and catches unmarked departures. There are three caveats (section 4). About half the "marked repairs" fill
odd-length digit groups from context, so they are closer to guesses. The verbatim share is 86-87%, not the 93% "read as
sense" figure. Some NOTES details are slightly off.

## 1. Blind transcription (written before opening the solver's files)

Crops came from the local full-size scans (2000 px) as 3x strips of about 230 px, with 4-7x zooms on doubtful spots.
Units are written as split on 0, and the 0s are kept. `[a|b]` means the verifier could not decide between two digits.

| id | page / line | blind digits |
|---|---|---|
| H1 | 443 c. 318r line 1 (held-out block c) | `34 0 44 0 74 0 7538 0 23 0 7572 0 11 0 7274 0 4745 0 39 0 22 0 76 0 72 0 12 0 7572 0 3273 0` |
| H3 | 443 c. 318r line 3 (held-out block c) | `11 0 4572 0 24 0 3472 0 7572 0 532274 0 43 0 4745 0 5272 0 74 0 4375 0 4524 0 18 0` |
| A01 | 443 c. 315r line 1 | `47 0 4932 0 4738 0 44 0 47 0 43 0 3245 0 75 0 7623 0 39[2|7]6 0 43 0 34 0 4374 0 5272 0 3345 0 7545 0 723943 0` |
| A10 | 443 c. 315r line 10 | `3245 0 55 0 72 0 3345 0 3946 0 11 0 2332 0 3345 0 32 0 22 0 3947 0 74 0 72 0 3943 0 43 0 7576 0 237672 0` |
| A18 | 443 c. 315r line 18 | `7445 0 5272 0 3972 0 7552 0 43 0 74 0 [8|0]43 0 9839 0 23 0 3423 0 74[2|7]6 0 43 0 4745 0 33 0 38 0 74 0 23 0 12 0` |
| B02 | 451 c. 25r line 2 (blotted) | `13 0 25 0 22275 0 34443 0 76222 0 [3|8]523 0 4[8|9]32274 0 457672 0 7439 0 7247 0 4332 0` |
| B12 | 451 c. 25r line 12 | `74 0 3245 0 4532 0 5223 0 74 0 455272 0 4743 0 32 0 2274 0 3343 0 1112 0` |
| B21 | 451 c. 25r line 21 | `45 0 5276 0 387673 0 11 0 4722 0 7545 0 32 0 4652 0 72 0 397674 0 22 0` |

Notes made blind: on 315r a "Z"-shaped sign with a flat foot occurs at A01 (`39?6`) and A18 (`74?6`). It is not the
plain 7 of this hand and not the looped 2, and it could not be settled. B02 is overwritten and blotted in its middle
third, and `34443` and `4?32274` are odd stretches as read. A18 `[8|0]43`: the sign after `74 0` is a small closed
loop, 8 or 0.

## 2. Comparison with the solver's transcription

The sample is 8 lines: 492 digits and 185 units. Two lines are in the held-out block (c. 318r c01, c03), three are
on the bare 443 c. 315r and three on the bare 451 c. 25r. c. 315v was left out because its bleed-through is too heavy
for a fair blind read.

- **Raw disagreement: 13 of 492 digits (2.6%), touching 12 of 185 units (6.5%).**
- Five lines agree digit for digit: H1, H3 (the held-out lines, 117 digits), A10, B12 and B21.

Each disagreement was settled on 5-8x crops of the full-size scan:

| line | verifier | solver | settled |
|---|---|---|---|
| A01 pos 4 | `4932` | `4332` | unresolved (3/9 shape). No effect: 43 and 49 are both e |
| A01 `39?6` | Z-sign | `3976` | **solver right.** The flat foot is the lead-in stroke into the 6 (it occurs only before 6). 76 = t |
| A01 line end | `3943 0` | `394304` | **verifier probably right**: the last mark is a line-end flourish. The solver reads it as 4 and deletes it in the reading (`comisione{[?4]/}`), which costs one verbatim word |
| A18 `[8|0]43` | extra sign | `74 0 43` | **solver right.** The verifier counted the one oval twice (as 0 and 8) |
| A18 `9839` | 9 | `3839` | **solver right** by context: `38 39 23` = "una" in "una parte di mura". The shape leans 9 |
| A18 `74?6` | Z-sign | `7476` | **solver right** (same ligature as A01) |
| B02 `25` | 5 | `28` | **solver right**: S-shaped 8 with no 5-flag |
| B02 `22275` | three 2s | `2275` | **solver right** at 7x: two 2s. The verifier over-counted long-based 2s |
| B02 `76222` | three 2s | `7622` | **solver right** (same cause) |
| B02 `[3|8]523` | 5 | `3823` | **solver right**: same S-shaped 8 as above |
| B02 `4[8|9]32274 0` | one overwritten sign | `4932 2 0 74 0` | **unresolved.** One overwritten sign (2 over 0, or 0 over 2) sits between `32` and `74`. The solver gives it two digits (`2 0`). By SIGN_CONVENTIONS it should be one, the top ink. If it is 0, the decryption gives "el ritorno" with no repair, and the mark `{[?49322]/ il}` falls away |

After settling, the solver is wrong at 1 place probably (A01 flourish) and 1 is unresolved (B02 overwritten sign). A
third (A01 3/9) has no effect. **Sign level: 1-2 of 185 units (0.5-1.1%); 0 in the held-out lines.** Most of the
verifier's own errors came from over-counting the long-based joined 2s. The solver handles that form consistently.

## 3. Key and held-out test

- **Key values hold.** `key_frozen.tsv` has 35 rows and `key.tsv` adds 15, 28 and 46. Unit counts across the three
  documents (k316 / c315 / c25) for values that hold at every occurrence with no repair are:
  11 et (8/9/7), 12 che (8/6/3), 24 non (5/4/2), 25 si (7/11/2), 32 l (22/32/25), 39 n (34/38/27), 43 e (31/68/43),
  45 i (48/65/56), 47 d (22/29/19), 52 c (19/22/18), 74 r (24/47/34), 75 s (22/31/22) and 76 t (25/44/26). That is
  **13 values, well over 10**, each with dozens of occurrences that make clean Italian in both bare letters. There are
  single departures, all marked: 73 o read t (c315 r04, an overwritten digit), 33/93 m read n (c25 r19), 38 u read n
  (c25 r23), and one 22 a deleted (c25 r02).
- **The pairs are real and aligned.** The verifier read c. 317r from the scan. It is a contemporary decipherment in a
  different hand: "Acapi il tutto et venga co destrezza et che non si parti di Montalcino senza resolutione ... Si è
  imposto al Collonello ... persuaso et ordinato et solo voglino la protezzione di V. Ecc. et io nò posso far di quore
  se nò quato è servitio di V. Ecc." The mechanical decryption of 316v a/b follows it line by line. NOTES lists only
  three a/b differences, but there are more small ones: a01 `acapiqtut[?722]` against "Acapi il tutto",
  `connresteza` against "con destrezza", b02-b03 `subto come ti` against "subito commetti", b12 `pa quale` against
  "la quale", and b10 `cse[?4744912]` against "crede". The claim that "in each the cipher reads cleanly" is too strong.
  This does not affect the key: these are key-source lines, and the pattern looks like clerk slips.
- **The held-out test is genuine.** `python scripts/decrypt.py transcription_k316.txt key_frozen.tsv` reproduces c01-c04
  exactly as quoted in NOTES. Against c. 317r's 24 words, 22 agree (spelling apart), "che" stands for c. 317's "et",
  and `[?83223]` stands where c. 317 has "la". No held-out unit is missing from the frozen key. The verifier's own blind
  transcription of c01 and c03 matches the solver's digit for digit, so the held-out input is confirmed independently.
  File times: `work/b3_p1.txt` (the pass-1 digits of block c) was written at 13:34, before the freeze at 13:50:18. No
  pre-freeze file aligns block c with c. 317 (`work/b1_units.txt` covers block a only). No leak was found.
  Caveats: the test is small (24 words) and has no shuffled-key baseline. NOTES says "70 units", but `decrypt.py` splits
  block c into 77.
- `46 i` comes from a pair (a03 "aduisi") but is not in the frozen key. That is conservative and has no effect on the
  held-out block.

## 4. Mark check, counts and status

- `python scripts/check_marks.py` gives **exit 0**. It rebuilt the three decryption files identical and printed
  "c315: words 187: verbatim 161, marked repair 12, guess 0, decoded but not read 14; holes 11" and "c25: words 131:
  verbatim 114, marked repair 7, guess 0, decoded but not read 10; holes 8".
- Tamper tests on a scratch copy:
  - Removing the mark in `le {o/t}rombe` makes it FAIL at c315 r04.
  - Changing "homini" to "uomini" makes it FAIL at c315 r10.
  - Changing one transcription digit that alters a letter (r10 `55` to `75`) makes it FAIL with a stale decryption.
  - Changing `43` to `49` (both e) passes, which is correct.
  - So every departure in the readings is marked, and the check enforces it.
- **Caveat on the counts.** About 9 of the 19 "marked repairs" restore text from odd-length digit groups the signs do
  not give: `{[?34774]/pr}`, `{[?222]/a}`, `{[?74843]/re}`, `{[?1182543]/ et si è}`, `{[?722]/o}`, `{[?34443]/pet}`,
  `{[?49322]/ il}`, `{[?447]/d}` and `{[?477]/festa}`. The last one turns three digits into five letters. Two more fill
  unknown units from context (`{[84]/v}`, `{[78]/r}`). These are context guesses in a repair mark. `reading.py` counts
  them as "repair", not "guess". Two more "repairs" only delete a stray group (`{[?4]/}`, `{[?72423]/}`).
- **Honest headline.**
  - 443 c. 315: 161 of 187 words (86.1%) verbatim from the signs; 14 decoded but not parsed; 11 holes.
  - 451 c. 25r: 114 of 131 (87.0%) verbatim; 10 decoded but not parsed; 8 holes. c. 25v is not transcribed.
  - The "93% / 92% read as sense" figures include context fills and should not be the headline.
- **Status rules.** "Read" needs 95% of words verbatim from the signs, and neither bare piece reaches it. So **read in
  part** is right for both, and NOTES does not claim more. The 2 Feb letter (k316) is covered by c. 317r, so it is a
  transcription job, as NOTES says.

## 5. Reading files

- `reading_c315.md`: **B**. It is coherent over most lines: Poggio Imperiale, the ladders and fire-trumpets, Milandrone,
  the feigned "trattato", and the ten men in Montalcino. Unparsed stretches are honestly bracketed. The English adds
  "[che]" and "[è]" in the running text only, which is acceptable. "Milandrone" reads letter by letter from
  `33 45 32 22 39 47 74 72 39 43`, as stated.
- `reading_c25.md`: **B**. It is coherent from r06 to r16 and r20 to r23. r17-r21 are bracketed as not read. The note on
  84 (p at r13, not at r06) is candid. r02 "per aspettava il ritorno" rests on two context fills. The verifier's
  settled reading of the overwritten sign may remove one of them (section 2).
- `decryption_*.txt`: **A** as mechanical output, rebuilt identical.

## 6. Names and sources

- NOTES says "AI language-model agents" with no vendor name.
- The sources named are ASF (Florence), the ASF inventories, DECODE, Cryptiana, Lasry's list and Cantagalli. These are
  fine.

## 7. Recommended status

| doc | status | reason |
|---|---|---|
| k316 (443 cc. 316v, 318r; 2 Feb) | transcription job | c. 317r is the contemporary decipherment; it also serves as the key source and the held-out test (22/24) |
| c315 (443 c. 315r-v; 1 Feb) | read in part | 86.1% verbatim, under 95%; key confirmed; transcription confirmed on a blind sample |
| c25 (451 c. 25r; 3 Jan) | read in part (25r only) | 87.0% verbatim; c. 25v about 19 lines not transcribed |

Suggested fixes (for the solver; not made here):
- Reclassify the context fills of odd digit groups as guesses, or report them separately.
- Re-check the overwritten sign in 451 r02 (one sign, not `2 0`) and the line-end flourish in 443 r01.
- Correct "three places" and "70 units" in NOTES.
