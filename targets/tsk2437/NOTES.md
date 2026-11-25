# T-S K24.37: Geniza leaf in an invented angular dash-divided script (Cambridge University Library)

Status: in progress

Cambridge University Library, Taylor-Schechter K24.37 (Princeton Geniza Project id 32699). Undated paper leaf, eight lines of angular signs on the
recto (CUDL image 1), the verso (image 2) blank except for a faint mirrored ink offset. PGP: "Fragment with mysterious writing on it. It might be
mirror-image Hebrew script. Needs examination." No tags, no transcription, no bibliography, no related documents; entered by Alan Elbaum in 2021.
Found as a new lead by the 25 Nov 2026 thorough Geniza sweep (`research/sweep_2026-11-25_geniza_thorough/`), which first filed it as a probable mirror
imprint and, on a second look, as an invented angular alphabet. Partner target: `targets/tsk2424/`. Session of 24 Nov 2026
(claude-sonnet-5-5), ciphertext-only.

## Access

CUDL IIIF by plain curl: `https://images.lib.cam.ac.uk/iiif/MS-TS-K-00024-00037-000-0000N.jp2/<region>/full/0/default.jpg`, N = 1 (recto, 5673 x 6438 px) and
N = 2 (verso, 5757 x 6413 px; N = 3 not tried). `full` is capped at 2000 px; `../tsk2424/fetch_images.py <id> <out.jpg>` stitches 1800-px region tiles to native
size. `crop.py` writes a background-flattened crop for reading. Images stay in the git-ignored `img/`. Reproduction on the public web needs permission
from genizah@lib.cam.ac.uk (CUDL statement on the PGP page), so nothing is committed.

## What the leaf shows

- **Layout (recto):** line 1 across the top of the sheet; lines 2 (isolated, short); lines 3, 4, 5 stacked tightly below; lines 6, 7 and 8 inside a ruled
  frame (a dashed left rule and a solid right rule, the last line sitting on the bottom rule); the sheet is torn, patched, and has a fold or join across the middle. The
  verso shows a mirrored ghost of the lines (ink offset), which is probably what PGP's "mirror-image" refers to.
- **Signs:** angular, stem-based: an upright stem with a foot to the left (J, 31 examples, with Jd 2) or to the right (L, 8), plain stems (I), brackets
  (R), boxes (B), cups (U, u), solid blobs (o, c), long bars with a heavy head at the right (b), short bars (d), long diagonals (D), and a tail of
  rare shapes (K, W, X, Z, G, C, O, P, M, Y ...). Groups are divided by thin dashes and dots. 8 lines, 209 signs (190 classified, 19 `?`) in 36 shape
  classes, 15 dash and 8 dot dividers (second reading, 24 Nov 2026; the first pass had 166 tokens in 15 classes). Per line 26, 18, 29, 35, 28, 27, 21, 25.
- Condition: lines 5, 6, 7 and the right half of 8 are firm; lines 1 and 3 are firm on the left and rubbed in the middle and right; line 2 fades out after
  x 3900; line 4 is stained at the left (1700-2150); line 8 is traces only left of x 2150; holes cost 3-4 signs in line 6 (2555-2830) and a gap of
  about 260 px in lines 3 and 7. Positions below are pixel x in the native recto image.

## Moves (all recorded in `profile.json`)

1. Prior art: PGP record, both sweeps, web search, DECODE harvest grep: nothing. Not in Bohak 2010's list.
2. Native images; flattened crops of each line, two per line.
3. **Transcription, first pass** (now `transcription_first_attempt.txt`): 14 shape classes plus `?`, 166 tokens. It merged look-alike signs
   (see the comparison under "Sign-level transcription").
4. Statistics (`../tsk2424/analysis.py transcription.txt --drop ?,c`): 125 tokens of 12 used classes; IC 0.118 (uniform 0.077); entropy 3.26 of 3.70 bits;
   repeated 2/3/4-grams 28/7/0 against shuffle means 27.8/7.6/0.9; H(next|prev) 2.35 vs 2.53 (z -2.8), the only departure from chance. 31 dash groups,
   none repeated; group lengths 1-5 mostly, a few 9-15 where dividers were missed. The class inventory (about 14-15 shapes) is in the range of an alphabet, but
   the classes merge signs, so the real inventory could be 20-28; not decidable from this transcription.
5. Comparison (see table): not Bohak's ring-letter family (K24.19 viewed), not NS J479, not K24.24.
6. Attacks (`../tsk2424/attack.py`): many-to-one monoalphabetic annealing of the 14 classes, dividers as word breaks, both directions:

   | model | real forward | real reversed | shuffled nulls (12) | z fwd / rev | control (12) | control vs nulls |
   |---|---|---|---|---|---|---|
   | he-tanakh | -3.645 | -3.637 | -3.685 (sd 0.111) | +0.4 / +0.4 | -2.641 | z 9.5 |
   | ja-from-arabic | -3.044 | -3.127 | -3.150 (sd 0.076) | +1.4 / +0.3 | -2.369 | z 10.2 |

   The real class stream scores like its shuffle. The control (model-language text of the same length, random many-to-one map to 14 classes, same
   word-break rate) separates by z 9.5-10.2, so a clean monoalphabetic text at this length would have shown; the leaf's transcription does not.
   The Arabic-model "decrypt" degenerates to alif-lam runs (overfit). Control text overlaps the model corpus, so detectability is an upper bound.
   Read together: either the leaf is not a monoalphabetic cipher of Hebrew or Arabic letters, or the class transcription is too coarse and noisy; this
   run cannot tell which.
7. Crib and pattern: no repeated dash group, no repeated 5-sign run; the longest repeated class run is 4 signs (`c J b b`). A formula test (basmala, greeting) is
   impossible at class level.

## Sign-level transcription (second attempt, 24 Nov 2026)

Method: native recto (5673 x 6438, CUDL IIIF region tiles; CUDL holds only the two pages 1r and 1v, no raking-light or multispectral image, and ids
-00003 and -00004 do not exist), background-flattened windows of 700-950 px cut along each line (`mkwin.py`, `win.py`; pixel ruler on every window),
read at 1.8-2.5x. **Pass 1** (flattened, 2.1-2.5x, `pass1.txt`) read every sign with its x position, a grade and a note. **Pass 2** (CLAHE, 1.6-1.8x,
window edges offset, `pass2.txt`) re-read lines 1-4 afresh and lines 5-8 as a confirming reading (these four lines were copied over after
re-viewing, so their agreement is partly anchored by memory of pass 1; the pass was made by the same model within one session, not an independent
reader). `diff.py`: 222 signs agree, 6 differ in class, 1 is in pass 1 only and 4 in pass 2 only. Each difference was resolved on 3.2x tiles
(`changes_from_pass2.txt`). Class contact sheets (`contact.py`, git-ignored images) drove the merges and splits: `e` merged into `o`; the old `c` split
into `o` (solid blobs of 40-55 px) and `c`; the old `b` split into `b` (long bars with a head at the right) and `d` (short bars); the old `V` split
into wedges `V` and thin short diagonals `Ds`; `v` and a faint dash merged into `W`; the J class was kept whole after 31 examples showed a continuum of
foot shapes (flat, hooked, long thin). Output: `final.txt` (positioned, graded), `transcription.txt`, `cipher_tokens.txt`, `legend.txt` (counts per
class and grade), `doubts.txt` (every likely and doubtful sign). **Grades: 98 firm, 72 likely, 39 doubtful** (of 209 signs incl. 19 `?`).

Against the first attempt (`align.py`, an alignment per line with a merged-class compatibility table): of its 166 tokens, 108 (65%) correspond to
a compatible new class, 31 (19%) to a different class (mostly the catch-all `H`, `Z`, `C` and `c`), 23 (14%) involve a `?`, 4 have no counterpart;
47 of the new 209 signs (22%) are not in the first attempt. The first attempt's `H` (15), `Z` (12) and `C` (9) were catch-alls for K, G, W, X, A, M, Y,
Z, R, C, U and I. The same shape recurs identically across lines, e.g. K three times (L1 4510, L6 2135, L7 3130), B four times with a rising flag
(L5 2955, L6 3190, L7 2525, L8 3360), the ring with a cross once (L5 2325).

### Reading direction (evidence, not a conclusion)

Right-to-left is probable and not established. For: (1) the right ends of lines 3-8 sit at x 4770-4975 (sd about 55 px) against the ruled right-hand
frame line at x 4960-5000, and line 7 ends with its last foot touching the rule, while the left ends scatter between x 1520 and 1835 (sd about
125 px) with 850 px of empty paper between them and the left rule: the lines hug the right rule and stop ragged at the left; (2) long bars carry
their heavy head or ring at the right and thin out to the left (14 of 16 long bars with a head; the 4 short bars with a ball at the left are the
exception), which is the pooling expected when a reed or pen starts a leftward stroke loaded with ink; (3) the leftward foot dominates the stem
signs (J and Jd 33 against L 8). Against or neutral: the same pooling can come from a rightward stroke that ends in a blot; no smeared or overlapping
ink shows stroke order; the lines rise to the right at about 2 degrees, but so does the frame rule (sheet skew); CUDL's `textDirection: L` is a
viewer default. Line-initial in page order (left end): I in lines 1, 2, 4 and 5 (rubbed in three), which would be a line-final stem read right to left.

### Quick statistics on the new transcription (`../tsk2424/analysis.py`, `?` dropped)

| | first attempt (`?` and `c` dropped) | second attempt |
|---|---|---|
| signs, classes | 125, 13 | 190, 36 |
| IC (uniform) | 0.118 (0.077) | 0.065 (0.028) |
| entropy | 3.26 of 3.70 bits | 4.40 of 5.17 bits |
| repeated 2-/3-/4-grams (shuffle mean) | 28/7/0 (27.8/7.6/0.9) | 33/7/1 (27.3/3.4/0.2) |
| H(next / prev), shuffle mean | 2.35 (2.53), z -2.8 | 2.49 (2.56), z -1.2 |

The one repeated 4-gram is `c J L R` twice in line 5 (x 1870-2195 and 3440-3760, followed by O and by X), also `J L R`, `b o I`, `b o b`, `c b B`,
`b c U` (7 repeated 3-grams, two each); no dash group repeats except the single stem `I` and `?`. Annealing (`../tsk2424/attack.py`, the 36 classes onto
22 letters, dividers as word breaks, 6 restarts x 3000 steps, 12 nulls and 12 controls): he-tanakh real -3.551 forward / -3.502 reversed against
shuffled nulls -3.715 (sd 0.095, max -3.575), z 1.7 / 2.3; ja-from-arabic -3.142 / -3.084 against -3.250 (sd 0.081), z 1.3 / 2.1; controls separate
from the nulls by z 16.9 and 13.5. With firm and likely signs only (doubtful set to `?`) he-tanakh reversed reaches z 2.8, forward 1.3 (one test of
two directions, not corrected). A quick first run with 3 restarts x 1500 steps gave z 5.4 / 4.0; the nulls were under-converged, and the value is
not used. **Nothing reads as language**: the class stream scores inside the range of its shuffles, as before; with 36 classes (14 of them with one or
two examples) a many-to-one fit is cheap, and a clean monoalphabetic text of this length would have shown (controls). The weak signals are the
line-5 repeat and the reversed score.

## Is it mirror-image Hebrew?

PGP's note is likely prompted by the verso ghost. Test done: horizontal flip of crops of lines 6 and 7: the signs do not turn into recognisable square
Hebrew letters by eye (the stems with feet and the boxes are suggestive of gimel/vav/zayin and mem/samekh forms, but that is a resemblance, not an identification).
Open: a shape-by-shape comparison with Hebrew square-script letters, normal and mirrored, giving each class at most two candidate letters, then a
constrained solver with `he-tanakh` / `ja-from-arabic`. That is the cheapest next test and needs the sign-level transcription first.

## Sign comparison with published and neighbouring systems

| system | look | K24.37 |
|---|---|---|
| Bohak ring-letter cipher (K24.19 viewed) | upright, rings, x, 9, H, plain Hebrew words interspersed | no rings (one ring-with-cross), no x/9 forms; no plain words |
| T-S NS J479 (viewed; Elbaum's table not seen) | rings with a dot, P- and D-like signs | no match |
| T-S K24.24 | slanted brush cursive, rings, zigzags, long slashes | different hand, shapes, ink and layout; shared: dot dividers, a zigzag shape |
| T-S AS 187.240 glyph block | goblet, 8, C, L, n, 3, U | L, U and C classes look similar in name only; not compared closely |
| Hebrew square script, mirrored | suggested by PGP | not excluded; not tested sign by sign |

## One text or two?

Two separate leaves with separate hands and shapes, so two folders. (Conclusion from the visible differences, not proof; the shared box number K24 only shows
that the leaves were shelved together.)

## Remaining gaps

- 39 doubtful and 72 likely signs and the 19 `?` (`doubts.txt`): rubbed or stained, mostly in lines 1, 3, 4, 8 - blocker: illegible; a better image (multispectral or raking light, not held by CUDL) or a reader of Geniza hands
- lost zones: line 6 hole 2555-2830, lines 3 and 7 about 260 px each, line 8 left of x 2150, line 2 right of x 3900 - blocker: illegible, physically lost
- the class inventory rests on one reader: pass 2 re-viewed lines 5-8 with memory of pass 1 - blocker: needs a second human or model reader working blind
- any key or plaintext: none known - blocker: no-key-material; no matching published key
- the script's identity (invented, or mirrored/stylised Hebrew) - blocker: no-key-material; needs a letter-by-letter comparison and, if possible, the editors' opinion

## Escalation

- [ ] siblings: K24.19 viewed; K24.23, ENA 3211.1-2, Misc.10.60/11.91/22.218 not viewed; PGP lists no related documents for K24.37
- [n/a] clear-pages: the verso carries only a mirror ghost of the recto
- [ ] known-keys: Bohak's key not available to this session (the 2010 PDF returned 403); no key applied
- [x] print: PGP, both sweeps, web search, DECODE grep: no reading
- [x] key-rebuild: monoalphabetic annealing on the class stream with Hebrew and Arabic models: null result (controls above)
- [n/a] retry: nothing read, nothing to retry

## Next steps

1. A blind third reading of lines 1-8 by a second reader, then re-grade `doubts.txt`.
2. Mirrored-Hebrew and Hebrew-square-letter candidate sets per class (the class stream is now sign-level: K, B, ring-with-cross, G, R, X and the
   cups are the most distinctive shapes), then a constrained solver with the registered models; try right-to-left first.
3. Contact the Princeton Geniza Project / Cambridge Genizah Research Unit (Elbaum entered the record) before any publication; nothing sent.

## 25 Nov 2026: remaining routes tried (claude-sonnet-5-5)

Blind reading 3 (`blind3/`, pass 1 only, 57 unmerged labels) disagrees with the 36-class inventory, so the inventory is unstable between readers. The 31 dash
groups run 1-24 signs and none repeats (besides the single stems), so dashes are not word breaks; an annealer run without word breaks (ja-from-arabic, z 1.4 / 1.9,
controls only z 3.0) found nothing. A flip of line 7 gives no square-Hebrew forms. Siblings viewed (K5.7, K24.19, K24.23, K24.24, Misc.10.60, 11.91, 22.218, ENA 3207.17,
CUL Or.1080 J277) share no sign set and carry no sign table; box K24 has no other cipher leaf. Bohak 2010/2011 not accessed. Reading the leaf as a decorative or
magical pseudo-script (no text to read) fits the evidence at least as well as a cipher. Details: `WORKLOG.md`, `profile.json`. Contacting the PGP editor was deliberately not done.
