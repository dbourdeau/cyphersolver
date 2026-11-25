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
- **Signs:** angular, mostly an upright stem with a foot to the right (L) or a hook to the left (J), cups (U), arches, closed boxes with a flag, zigzags, stems
  with side bars, thick-ended bars, small curls; one large ring with a cross. Groups are divided by dashes (short or long) and by dots. 8 lines, 166 tokens
  (152 classifiable) in 15 classes, per line 21, 15, 27, 24, 22, 21, 20, 16.
- Condition: lines 1, 6 and 7 are firm; lines 2-5 and 8 are rubbed, stained or on the frame rule (counts +-20%).

## Moves (all recorded in `profile.json`)

1. Prior art: PGP record, both sweeps, web search, DECODE harvest grep: nothing. Not in Bohak 2010's list.
2. Native images; flattened crops of each line, two per line.
3. **Transcription (`transcription.txt`, `cipher_tokens.txt`, `legend.txt`)**: a shape-class first pass (14 classes plus `?`, letters not assigned). It merges
   look-alike signs, so it is a layout and repertoire record, not a text a solver can use. A second reading at 2-3x was done for lines 1, 6 and 7 only; doubtful
   classes: J/c (hook against small curl), H/Z (stem with bars against zigzag), C/U (bracket against cup), b/- (thick bar against dash).
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

- lines 2, 3, 4, 5 and 8: rubbed, stained or on the rule, counts +-20% - blocker: illegible; only a better image (multispectral or raking light) or a reader of Geniza hands can recover them
- sign-level transcription of all 8 lines (the classes merge look-alikes) - blocker: illegible; shapes that a flattened JPEG does not separate reliably
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

1. A sign-level transcription (each class split, doubtful signs flagged), starting with lines 1, 6, 7; try raking-light or multispectral images if CUDL
   has them (not checked).
2. Mirrored-Hebrew and Hebrew-square-letter candidate sets per class, then a constrained solver with the registered models.
3. Contact the Princeton Geniza Project / Cambridge Genizah Research Unit (Elbaum entered the record) before any publication; nothing sent.
