# Blind re-readings by sign shapes, 11 Nov 2026 (sheets K1, K2, K3)

Three sheets were pre-registered; K1 and K3 were answered by Brice Dudout and integrated, K2 was abandoned before it was shown.
No image, crop or thumbnail of any sheet is reproduced here.

| sheet | bears on | questions | controls | status | effect |
|---|---|---|---|---|---|
| K1 | held-out portion, image 031 | 26 + 2 controls | 2/2 | integrated | held-out portion 96.1% -> 94.41% (B, retained; A 94.97%) |
| K2 | rest of the book | 36 drawn at random + 2 controls | - | **abandoned before it was shown** | none |
| K3 | rest of the book, targeted | 9 + 2 controls | 2/2 | integrated | whole book 95.16% -> 95.13% (B, retained; A 95.12%); held-out portion untouched |

## Sheet K1 - held-out portion (image 031)
One blind sheet of sign shapes, answered by Brice Dudout on 11 Nov 2026 (export 17:08 UTC), integrated once by a Claude Opus 5.5
agent at 18:14 CET. It bears only on image 031 (both pages), read at full resolution after the single measurement of the key.
No image, crop or thumbnail of the sheet is reproduced here.

### Rules, written and hashed before the sheet was built

`PREREG-PLANCHE-K1.md`, SHA-256 **ecdd74a70fa8eb58a0e4b7b83a39202a6e1092202956a34efdd0750cd148a505** (re-checked at integration).
- One question = one doubtful sign of image 031 (or its immediate neighbour), boxed on its line; the options are 2 to 4 reference
  shapes cut from certain words of the same leaf, plus "none / illegible" and a free remark. No value, gloss or letter is shown.
  Order of questions and options drawn at random, seed 2525111.
- Two control questions on certain signs (the second b of "Stabben"; the e of "Hjørne"). If either control fails, nothing is
  integrated and a different sheet is made later.
- Integration, applied once and mechanically:
  1. shape chosen = class of our reading: the word keeps our reading; if it was probable and this sign was its only doubt, it
     becomes certain;
  2. shape chosen differs: the word becomes unresolved, unless the letter of the chosen shape gives a Danish word attested in the
     Gutenberg word list (frequency >= 2) or a declared 19th-century spelling (t/f, o/ø, i/j, e/æ, aa/å): then it is probable
     with the new reading;
  3. "none / illegible" or no answer: a probable word becomes unresolved, a certain word stays certain;
  4. the share read is recomputed and recorded as it comes out, even under 95%;
  5. no second sheet on the same signs to recover a result.

### Sheet and answers

- Sheet `planche_kloge_K1.html`, SHA-256 76fdabe2dc34caee2471cd00bdfde2ef49e3c7398d94278db97feec05330e3ba (28 questions = 26 points
  + 2 controls; shapes only, images embedded, no external resource; tested under jsdom before it was sent). Builder `build.py`
  dab19930f6b28e025b2279f4da0b66793ae033ec03151774b438d47fb012b3c8. The private map question -> sign -> reading
  (1a1aaae9342d397bf5b6cd97a455a0bfec9e1d1d5f1efcec1d77a7ba676656f2) was never loaded by the page.
- Answers `reponses-brice-2026-11-11.json`, SHA-256 **bdefcb9359da707fa87f4071cab58dbd64066cb058e7ebffd78d6c0b88518a28**
  (equal to the value in its .sha256 file, checked before integration).
- **Controls 2/2**: q26 (b of "Stabben") answered b; q22 (e of "Hjørne") answered e. The sheet is integrated.

### Two results

- **A, the hashed rule as written** (clauses 1-3; the answer is the shape ticked; remarks ignored): held-out portion
  133/37/1/8 of 179 words = **94.97%** (95.5% with the restored word).
- **B, retained at Brice Dudout's request, a declared deviation from the rule**: where Brice wrote a remark ("shape 1 with a dot
  above", "shape 2 without the dot", "the two dots on the side are missing, the shape should be wider"), the remark is turned
  into a sign of the key table, then into a letter, before clauses 1-3 are applied. Held-out portion 133/36/1/9 of 179 words =
  **94.41%**. B is the figure we declare; A is given beside it.
Both are under 95%: the held-out portion is **read in part**. Clause 5 applied: no second sheet on these signs.

| q | place (031) | word (our reading) | shape answered / remark | effect A / B |
|---|---|---|---|---|
| q01 | right l. 23 | [karlegravet] a | shape 1 (a) / "with a dot above" | already unresolved; B would give "kerlegravet", not a word: unresolved |
| q02 | right l. 20 | Kirkegaard: k | shape 2 (dotted stroke, s) / "without the dot" | k not chosen; "Sirkegaard" not a word: certain -> **unresolved** (A and B) |
| q03-q05, q07 | right l. 17, 24-25 | ligger, Solens, foretages | as read | confirmed |
| q06, q10 | right l. 22 | øver ste: ø, e | as read | confirmed; stays probable (wrong word space) |
| q08, q11, q12 | left l. 5 | Kabbe: b, b, e | as read | confirmed (see q15) |
| q09 | right l. 22 | nord: o | as read | only doubt removed: probable -> **certain** |
| q13 | right l. 20 | Aand: a | as read | stays probable (one chevron for "Aa") |
| q14, q16 | right l. 24 | [søn]: s, ø | as read | signs confirmed, word still unresolved by sense |
| q15 | left l. 5 | Kabbe: a | shape 1 (a) / "with 2 dots" | A: stays probable. B: the key has no chevron with two dots; either the dots of the k before it fell in this box (a stays a) or the chevron is dotted (e: "Sebbe", "Kebbe", not words): probable -> **unresolved** in B |
| q17, q19-q21, q23, q25 | right l. 16-17, 25 | Solens, høire, Saugspaaner, som | as read | confirmed |
| q18 | right l. 23 | [karlegravet] a | as read | still unresolved |
| q22, q26 | right | Hjørne e, Stabben b | as read | **controls passed** |
| q24 | right l. 20 | en: e | as read | only doubt removed: probable -> **certain** |
| q27 | left l. 7-8 | Jomfru: o | as read | confirmed (see q28) |
| q28 | left l. 7-8 | Jomfru: capital J (stroke-and-dot + hook) | shape 2 (stroke + 2 dots, h) / "the 2 dots on the side are missing, the shape should be wider" | J not chosen; "Hjomfru" / "Somfru" not words: probable -> **unresolved** (A and B) |

"Jomfru" (031 left l. 7-8) was counted probable before the sheet: the full-resolution re-reading of 031 left gives only a page
total, with no class per word, so this is our assumption; the share read does not depend on it (the word ends unresolved either
way).

### Counts of the held-out portion (restored and unresolved words are holes)

| state | 030 | 031 left | 031 right | held-out portion | read |
|---|---|---|---|---|---|
| after the measurement, before the sheet (re-reading after the measurement, not blind) | 47/15/1/3 | 38/13/0/1 | 47/12/0/2 | 132/40/1/6 of 179 | 96.1% |
| A, rule as written | 47/15/1/3 | 38/12/0/2 | 48/10/0/3 | 133/37/1/8 of 179 | 94.97% |
| **B, retained (declared deviation)** | 47/15/1/3 | 38/11/0/3 | 48/10/0/3 | **133/36/1/9 of 179** | **94.41%** |
| first reading by sense, right after the measurement | | | | 95/62/2/24 of 183 | 85.8% |

The sheet took the held-out portion down by 1.7 points (96.1% -> 94.41%).

### Defect of the sheet: frames too tight

Three of the five losses (q02, q15, q28) come from the segmentation, not from the reading: the floating dots of a sign (the two
dots of k, or of the capital J) fell into the frame of the neighbouring sign, or outside the frame. Brice's remarks describe exactly
what each frame contained. This hand shifts the two dots of k to the right, onto the next sign (q01, q15 confirm it). A later sheet,
on other signs, must widen its frames to take in the floating dots.

## Sheet K2 - abandoned before it was shown

K2 was pre-registered (`PREREG-PLANCHE-K2.md`, SHA-256 c0bc50a7a4758f0806282c7a2a71160eb6271de3e79ac24b82148d51ddf43488, seed
2525222): 36 points drawn **at random** from the 1,122 doubtful shapes of the working fiches, plus 2 controls (38 questions). It was
**abandoned on 11 Nov 2026 before it was shown to Brice Dudout**: no answer exists, no rule was applied, no class or figure was
changed from it. Reason: Brice Dudout asked for one or two sheets only, on useful signs (doubtful characters whose answer changes
a reading); a random draw does not pick useful signs, the sheet was too long, and at least one question was not informative (two
options of the same shape). The abandonment is recorded and hashed: `ABANDON-2026-11-11.md`, SHA-256
f57b26f87209fbccf49488244c4f2b29cdf49c0335b37345c57b2a06ee28085b. Since K2 received no answer, its clause "no second sheet on the
same signs" does not bind; it was replaced by the targeted sheet K3.

## Sheet K3 - targeted re-reading of the rest of the book

Integrated once by a Claude Opus 5.5 agent on 11 Nov 2026 at 21:32 CET, from Brice Dudout's export, by the rule below.

### Rules, written and hashed before the sheet was built

`PREREG-PLANCHE-K3.md`, SHA-256 **0400d3cf7094f5e9d03766b23c68262219ad2711b6c040f3e90391548b72c622** (re-checked at integration).
- Choice of signs, made on the fiches before any cropping: the doubtful signs ranked by the number of words whose class (certain,
  probable / restored, unresolved) depends on the answer; one question per kind of confusion; no sign of the held-out images 030-031
  (already in K1); no question whose options have the same shape. Nine signs kept; the signs ranked at zero are listed in the
  pre-registration with the reason.
- Two controls on certain signs of page 025 R (read 100%): the dotted chevron (e) of "Amen", l. 13, and the bar with two dots (n)
  of "Navnet", l. 4.
- Frames widened (lesson of K1): each frame holds every dot that may belong to the sign, margin up to 40 px while no neighbouring
  ink enters. Options are reference shapes cut from certain words (page 042 L, read 100%; 022 R for one shape), plus "none / other
  shape", "illegible", "not a sign" and a free remark. No value, gloss or letter shown. Seeds 2525333 (order), 2525334 (options).
- Integration, once and mechanically: 0. if a control fails, nothing is integrated; 1. shape chosen = our reading: the word keeps
  it, and a probable word whose only doubt was this sign becomes certain; 2. another shape: the word becomes unresolved, unless the
  new letter gives a Danish word attested in the Gutenberg word list (frequency >= 2) or a declared 19th-century spelling (t/f, o/ø,
  i/j, e/æ, aa/å), then probable with the new reading; 3. "none / other", "illegible", "not a sign" or no answer: a probable word
  becomes unresolved; 4. remarks about dots are turned into the dotted variant of the key table, declared, with the strict result
  beside it; 5. other occurrences of the same shapes are not changed mechanically (the answers are hints for a declared re-reading);
  6. the whole-book share is recomputed and recorded as it comes out, even lower; 7. no further sheet on these 11 signs.

### Sheet and answers

- Sheet `planche_kloge_K3.html`, SHA-256 c39f77e537d8b44f3574697032a5305b0627d76c16176e9032a7f282e47f563f (11 questions = 9 + 2
  controls; tested under jsdom before it was sent); builder `make_planche.py` 94d6e0bed71f711222293c6e34ae8044517764fb1c824ace0d82a5297bfcfa33,
  shared sheet core `planche_core.py` 0c605bc9c282f7c317fe4603b8950425cbe842e12289bf22bba934caa2d75e80; the private map question -> sign
  -> reading (96c37e2d98f5558f13c73b7fe8e83839224e3183e0f2ef9e9cb8e15dffb3cdff) was never loaded by the page. All four re-checked at
  integration.
- Answers `reponses-brice-2026-11-11.json` (K3), SHA-256 **4fbf5ec1f3674b68d8e1bf96126d1913c75fcfc2cb3620ed3631738d490c2e12**
  (equal to its .sha256 file, checked before integration); 11 answers, general remark empty.
- **Controls 2/2**: q01 (n of "Navnet", 025 R l. 4) and q06 (e of "Amen", 025 R l. 13) answered with their own shapes. The sheet is
  integrated.

### Two results

- **A, the hashed rule as written** (clauses 1-3; "none / other shape" makes a probable word unresolved).
- **B, retained, a declared deviation (as for K1)**: Brice Dudout's remarks are turned into a sign of the key table, then a letter,
  and clauses 1-3 are applied. Clause 4 covered remarks about dots only; here two remarks point to the shape of another question
  (q04, q09: "shape 1 of question 6", which is the dotted chevron of the control, the letter e) and one describes a shape (q03: "an x
  crossed by a bar"). This extension is declared.
A and B differ on one word only (q09).

| q | place, word (our reading), sign | answer / remark | effect A / B |
|---|---|---|---|
| q01 | 025 R l. 4 "Navnet", sign 1 | own shape | **control passed** |
| q02 | 039 R l. 3 "før [for]", sign 2 (two dots) | as read (ø) | shape confirmed; the word stays probable (ø written for o, a spelling, not its only doubt) |
| q03 | 064 L l. 2 "før", sign 1 (star-like sign read f) | none / other shape; "an x crossed by a bar" | the key table has no barred x worth f (the nearest, X on a bar, is read n once: "nør", not a word); probable -> **unresolved** (A and B) |
| q04 | 019 R l. 1 "Ankerne", sign 1 (chevron with a foot, read a) | none / other shape; "an incomplete triangle (shape 1 of question 6)" | A: unresolved. B: dotted chevron = e, "Enkerne", not in the word list (nor "Ænkerne"), e for a not a declared spelling, and the sense (casks) does not fit: probable -> **unresolved** (A and B) |
| q05 | 035 L l. 12 "som", sign 2 | as read (o) | only doubt removed: probable -> **certain** |
| q06 | 025 R l. 13 "Amen", sign 3 | own shape | **control passed** |
| q07 | 036 L l. 6 "lider [lyder]", sign 2 | as read (i) | shape confirmed; stays probable (i written for y) |
| q08 | 016 R l. 8 "son [som]", sign 3 | the other shape (m, three dots) | clause 2: "som" attested, probable with the new reading **"som"**, written correctly (was read "son") |
| q09 | 033 L l. 11 "før", sign 2 (closed loop, read ø) | none / other shape; "shape 1 of question 6" | A: probable -> unresolved. B: dotted chevron = e, "fer", which is in the word list with frequency 2 (the threshold): clause 2 gives **probable, new reading "fer"**. See below |
| q10 | 052 L l. 2 "jag [jeg]", sign 2 | as read (e: the wider frame holds the dot) | the word is written "jeg"; only doubt removed: probable -> **certain** |
| q11 | 027 L l. 9 "have", sign 1 | as read (h: the wider frame holds the second dot) | only doubt removed: probable -> **certain** |

**The "fer / før" case (q09), flagged.** The rule, applied mechanically to B, gives "fer"; the sense requires "før" ("at før Solens
Nedgang", before sunset), and e for ø is not a declared spelling. "fer" at frequency 2 is very likely noise in the word list. We keep
B as computed (the word stays probable) but do not adopt "fer" in the reading: `reading.md` keeps "[?før]" marked doubtful, with a
note. If "fer" is set aside (B'), the word is unresolved and B' = A. To be settled in the declared re-reading that follows.

### Words changed

| word (page, line) | before | A | B |
|---|---|---|---|
| som (035 L l. 12) | probable | certain | certain |
| jeg (052 L l. 2) | probable | certain | certain |
| have (027 L l. 9) | probable | certain | certain |
| før (064 L l. 2) | probable | unresolved | unresolved |
| Ankerne (019 R l. 1) | probable | unresolved | unresolved |
| før (033 L l. 11) | probable | unresolved | probable ("fer" by the rule; "før" by sense) |

No change of class: før [for] 039 R, lider [lyder] 036 L, som 016 R (reading changed from "son [som]"). `decryption.txt` keeps the
per-line counts and readings made before K3 (generated from the working fiches, which were not edited); the six words above are the
only changes, and `reading.md` and the counts in `NOTES.md` include them.

### Counts (restored and unresolved words are holes)

| page | before | A | B |
|---|---|---|---|
| 035 L | 58/8/1/4 (93.0%) | 59/7/1/4 (93.0%) | = A |
| 052 L | 33/3/0/0 (100%) | 34/2/0/0 (100%) | = A |
| 027 L | 57/6/1/0 (98.4%) | 58/5/1/0 (98.4%) | = A |
| 064 L | 37/7/1/25 (62.9%) | 37/6/1/26 (61.4%) | = A |
| 019 R | 28/6/0/6 (85.0%) | 28/5/0/7 (82.5%) | = A |
| 033 L | 63/9/1/0 (98.6%) | 63/8/1/1 (97.3%) | 63/9/1/0 (98.6%) |
| **whole book, 8,055 words** | 6,863/802/77/313 = 95.16% | 6,866/796/77/316 = 95.12% | **6,866/797/77/315 = 95.13%** |

- Rounded, **95.1%** in every case (was 95.2%): recorded as it came out, lower. Still **indicative only**: it rests on readings by
  sense, and only nine doubtful signs of the rest of the book have been checked blind.
- **Held-out portion 030-031 untouched** (no K3 frame on 030 or 031): **94.41%**, under 95%; the status stays **read in part**.

### What follows (clause 5)

The answers are hints, not proofs, for other occurrences of the same shapes (the chevron with a foot on 034 R, the closed loop on
073 R, 074 L, 075 L, the star-like sign of 064 L, and the dot confusions, best re-read with wider frames as in K3). A declared
re-reading will first write and hash the list of occurrences, then re-read each on the full-resolution image, and record the new
total as it comes out. No further sheet on the 11 signs of K3, and none to "recover" q03, q04 or q09.
