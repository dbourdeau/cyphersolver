# LJS 51 line finder and sign segmenter

`segment.py` finds the text lines on a master TIFF of Penn LJS 51 (`output/ljs51/master/0084_NNNN.tif`, about
2340 x 2960; a missing or truncated file is fetched with curl from openn.library.upenn.edu), says which lines are cipher
and which are Arabic naskh, and cuts every cipher line into signs, right to left, with word dividers and red
glosses flagged. This is version 2; version 1 is kept as `segment_v1.py` (its crops are in `output/ljs51/signs/`).
`evaluate.py` scores a segmenter against the by-eye counts of the transcription agents (`eval_set.json`, built by
`build_evalset.py` from `chains_0006_0029.jsonl` ... `chains_0078_0101.jsonl`).

    python segment.py 35                 # one image: output/ljs51/signs_v2/0035/ and the counts
    python segment.py 33-37 22 131       # a list and ranges (image numbers; image = 6 + 2*(folio-1), +1 for verso)
    python segment.py --all --jobs 8     # every master TIFF (212), 8 processes: the signs_v2 export
    python segment.py 35 --overlay       # also output/ljs51/crops/s2_0035_overlay.png (boxes on the page)
    python build_evalset.py              # rebuild eval_set.json from the chain records
    python evaluate.py                   # tuning and test scores per tier
    python evaluate.py --split test -v   # per chain and per line
    python evaluate.py --seg segment_v1  # the old segmenter on the same set
    python evaluate.py --set fix5=0      # a switch or parameter of P overridden (ablation)
    python evaluate.py --ref             # the old reference pages (tashifi counts)

From Python: `from segment import segment_page; lines = segment_page(35)`.

## Output

Per line: `index` (top to bottom, counting every text line, so on f. 14v the cipher starts at index 7 as in the folio;
v2 keeps v1's numbering, also for a line whose pieces all lie outside the text block), `kind` (`cipher` or `arabic`),
`y0 y1 x0 x1`, `features`, and for cipher lines `items`, ordered right to left:
`{'kind': 'sign' | 'divider', 'box': [x0, y0, x1, y1], 'red': [boxes of the red letters over this sign],
'merged': True if cut from a touching group, 'wide': True if wider than 1.7 median signs, 'joined': ['stack' | 'flag' |
'slash', ...] for a sign put together from several pieces, 'how': 'dots' | 'stemless' for a divider (stroke with dots,
or dots whose stem is pale or lost), 'stemless': True}`, and `red_letters`.
`export_signs(n)` writes, in `output/ljs51/signs_v2/<image>/`: `<line>_<k>.png` (k-th sign of the line, right to left,
64 x 64, dark ink on white, aspect kept), `<line>_<k>d.png` (the divider after sign k), `index.json` (one record per
crop: file, image, line, pos, kind, box, red, merged, joined, how) and `lines.json` (the whole page record).
Dividers are not signs: `k` counts signs only.

## How it works

1. Ink = pixels well below the local paper grey (paper estimated by a large closing; depth rescaled so a stained patch
   counts like clean paper). A piece is kept only if its darkest pixel and its mean are dark enough (drops show-through
   and pale smudges). Red ink (R - (G+B)/2 > 45) is a separate mask. Ink within 30 px of the page edge is ignored.
   Pale pages (median ink depth < 112: ff. 1r, 1v) use looser thresholds (fix 8).
2. Connected pieces. No dilation: a sign, a stem and a dot stay separate pieces and are put together by rule.
3. Text block columns = densest run of occupied x bins; then (fix 4) the block found from the lines themselves.
4. Lines: page skew by maximising the row-profile energy; row profile in sheared coordinates; lines are the peaks,
   cut at the valleys; then each line gets its own fitted slope and pieces are re-assigned to the nearest fitted line.
5. Cipher or Arabic: the v1 rule (cipher signs are single glyphs, so a cipher line has at most 2 pieces wider than
   100 px; red gloss and dotted-divider overrides), then the v2 corrections of fixes 3 and 5.
6. Signs and dividers (fixes 1, 2, 6), red letters attached to the sign below them.

## Changes in v2

Each fix is a switch in `P` (`fix1` ... `fix8`), so its effect can be measured (`evaluate.py --set fixN=0`). The rules
were set on the tuning set only (see Evaluation).

1. **Dotted divider = one item.** Dot candidates are compact pieces (no hole bigger than 1.5% of unit^2: pale dot
   centres leave pin-holes) at most 0.55 unit. A divider is a single stroke (thin: median row width <= 0.26 unit,
   2.2 x taller than thick, one run per row after a 3 x 3 closing that heals pale stroke centres, slant allowed) with
   two or more dots above it (no higher than 0.95 unit over its top, centre within 0.4 unit of its box); dots that ran
   together into one blob count as two when the blob is 2 x the line's single-dot area or 0.38 unit tall. A stroke with
   one dot is one sign (the zay of 40v, the stroke-and-dot sign of 28v l.3). Two or more separate true dots with no
   stroke under them are a divider whose stem is pale or lost (`how: 'stemless'`; the bare three-dot dividers of
   ff. 42r-44v come out this way).
2. **Two-part signs = one sign.** Pieces stacked over each other (x-ranges overlapping by half the narrower, at most
   0.4 unit apart, at most 1.7 units tall together: '8', '=', '//' drawn as two strokes, a dash over a body); two
   slanted strokes side by side leaning the same way; a small flag or dash (under 0.4 of its neighbour's ink) within
   0.15 unit of a body's top or foot. Checked on tiles of the joined signs of ff. 25r-36v: almost all are '//', '8',
   bar-and-stem and dotted signs; a few joins are Arabic words on lines that are not cipher.
3. **Arabic words on cipher lines.** (a) A line classed cipher whose pieces overlap like naskh (median gap < 0.12 unit;
   the lowest cipher line of the tuning pages is 0.21) and has no red gloss is Arabic: the headings written on a line
   of their own (wa-l-thani minhuma on 28r, basata llahu zilalahu on 30r, wa-l-awwal on 12v, overflow words, verse
   lines such as 31v l.6). (b) A line next to a line of the other kind is cut at a gap of 0.3 unit into a naskh part and
   a cipher part, the cipher part on the side the reading direction requires (a heading stands right of the first
   signs, the compiler's words left of the last ones): heading + 6 signs on 26r l.1, 4r l.9 after basata llahu
   zilalahu, the end of 4r l.13. Lines of the cipher kind are only cut where the other part is plain naskh (3+
   overlapping pieces, one a joined word).
4. **Gutter and fore-edge.** The text block is found from the lines: for every column the number of lines with a body
   piece over it; a corridor of at least 0.6 unit covered by fewer than 2 lines separates the block from the facing
   page, the fore-edge and margin stains; pieces beyond it are dropped (the facing page's letters at the left of every
   line of 27v, 29v, 4v). With the block known, the old per-line stray rules only cut pieces 4.5 sign widths away.
5. **Cipher lines classed Arabic.** An Arabic verdict is overturned when the pieces are small, separated and regularly
   spaced: median gap between neighbouring pieces >= 0.24 unit (naskh: 90% of lines below 0.24; cipher: 90% above
   0.34), under 30% of the ink in pieces wider than 2 units, at most one piece wider than 1.8 units, 5+ pieces (28 of
   the 46 misclassed cipher lines of the tuning pages, none of the 553 other lines). In context, a line between two
   cipher lines needs gap >= 0.3 and < 45% wide ink, a line next to one cipher line gap >= 0.4 and < 30%.
6. **A plain stroke is a sign.** The v1 'fused' test (a stem with a head up to 1.7 x wider, taken for dots fused to the
   stem) is off: on 28v, 35r and 40v it took the numeral-1 sign with its serif, the plain stroke and the m-on-stem
   sign for dividers. Dividers need separate dots (fix 1).
7. **Touching pairs** (off by default). A piece wider than 1.8 median sign widths is cut at a neck (one crossing, at
   most 1.5 stroke widths, both sides sign-sized). It cuts some real pairs (a double triangle on 6v, ع+8 on 2v) but
   also naskh on lines that are not cipher, and it is neutral to slightly worse on the tuning set, so `fix7=False`.
8. **Pale pages.** Pages whose median ink depth is below 112 (only ff. 1r-1v) use the looser `faint_*` thresholds;
   a 'cipher' line whose unit is under half the page's, or with at most 6 pieces spread more than 1.5 units apart, is
   texture. The six rows of 1r and of 1v are now boxed; see the failure list for the rest.

## Evaluation

`build_evalset.py` turns the chain records into `eval_set.json` (89 chains, 526 lines with per-line counts). The
records were counted in different ways, so each chain has a tier:

- `eye`: counted by eye on the master (chains_0054_0077, chains_0078_0101, 22v.9). In chains_0054_0077 the per-line
  list mixes segmenter and eye counts; it is used per line only where it adds up to the by-eye total, otherwise the
  chain total only. 27v.3 is moved to `checked` (its counts are v1's overlay, gutter boxes included).
- `checked`: v1 overlay counts corrected by eye, +-2..6 per chain (chains_0006_0029). They inherit v1's errors where
  the agent did not catch them (on 12r the dotted dividers v1 counted as signs are in the counts), so this tier
  favours v1.
- `segmenter`: v1 counts as they came (chains_0030_0053 except 22v.9): agreement with v1, not truth; not in the scores.
- `rough`: ff. 1r and 1v, +-8, totals only (scored on all cipher lines of the page, since the line finder renumbers a
  pale page).

Scores: per line, the share of lines within one sign and exact, and sum |found - expected| / sum expected (a line
classed Arabic counts 0 signs); per chain, the total error % of signs and of dividers, and divider accuracy = share
of chains whose divider count is within 10 % (at least +-1). Per-line divider counts exist only for the two blocks
without dividers. Test set = chains_0078_0101 (24 chains, 169 lines), held out; tuning set = the other three files
(eye+checked: 52 chains, 204 lines). Two test pages (images 85, 89) were looked at while the divider rules were being
debugged (the decision to drop the fused test and the single-blob dot count came from them), so the test set is not
perfectly clean for fixes 1 and 6.

| set (tiers) | version | within 1 | exact | line error | chain total error | divider error | divider accuracy |
|---|---|---|---|---|---|---|---|
| tune (eye+checked, 204 lines, 52 chains) | v1 | 77.0 % | 56.4 % | 13.3 % | 8.7 % | 14.7 % | 55.8 % |
| | v2 | 78.9 % | 44.6 % | 9.5 % | 6.3 % | 9.5 % | 71.2 % |
| tune (eye only, 61 lines, 25 chains) | v1 | 63.9 % | 37.7 % | 26.5 % | 12.1 % | 19.1 % | 44.0 % |
| | v2 | 85.2 % | 62.3 % | 7.0 % | 4.8 % | 7.6 % | 80.0 % |
| test (eye, 169 lines, 24 chains) | v1 | 69.2 % | 36.7 % | 15.5 % | 12.5 % | 18.0 % | 58.3 % |
| | v2 | 85.8 % | 61.5 % | 6.2 % | 5.0 % | 12.8 % | 58.3 % |

Lines classed cipher on the scored pages that belong to no chain (headings, verse, the compiler's lines): tuning
42 lines / 382 signs (v1) -> 18 / 174 (v2); test 13 / 104 -> 7 / 50. The `checked` tier alone falls from 82.5 % to
76.2 % within one, because its counts carry v1's divider and gutter errors (see above).

Cumulative effect, fixes added in order (tune eye+checked / test; within 1, chain total error, divider error):

| step | tune within1 | tune total | tune div | test within1 | test total | test div |
|---|---|---|---|---|---|---|
| v1 | 77.0 | 8.7 | 14.7 | 69.2 | 12.5 | 18.0 |
| + fix 1 dividers | 76.0 | 9.3 | 13.4 | 69.2 | 12.1 | 20.0 |
| + fix 2 two-part signs | 73.0 | 9.4 | 13.4 | 74.0 | 11.2 | 20.0 |
| + fix 3 Arabic words | 73.0 | 9.6 | 13.4 | 74.6 | 10.6 | 19.8 |
| + fix 4 gutter | 73.5 | 11.1 | 14.0 | 78.7 | 10.2 | 19.8 |
| + fix 5 line class | 78.4 | 6.6 | 10.4 | 85.2 | 5.6 | 15.7 |
| + fix 6 no fused dividers | 78.9 | 6.3 | 9.5 | 85.8 | 5.0 | 12.8 |
| + fix 8 pale pages (= v2) | 78.9 | 6.3 | 9.5 | 85.8 | 5.0 | 12.8 |
| v2 + fix 7 | 78.9 | 6.2 | 9.5 | 85.2 | 5.3 | 12.8 |

Fix 3 mostly removes false cipher lines (42 -> 27 on the tuning pages) rather than changing scored counts; fix 8
changes only ff. 1r-1v (rough tier, not in the table). Overlays checked by eye: images 7, 19, 28, 56, 59, 61, 63, 70,
74 (styles: pale red-glossed 1v, round 7v, dotted-alif 12r, letter-like 26r, gutter 27v, angular 28v, 29v, 33r, 35r);
`output/ljs51/crops/s2_*_overlay.png` holds the v2 overlays of 6, 24, 41, 56, 59, 63, 70, 74.

## Known failure modes (v2)

- **Mixed and letter-like lines.** A cipher line that looks like naskh stays Arabic: 31v l.1 (repeated loops), 33r
  l.11, the overflow sign 31r l.14, 41v l.10-11, the heading-plus-signs line 28r l.1-3 (28r ll.2-3 hold long 'aS'
  signs and are still Arabic); 16v l.6 (one sign, divider, text) is still missed. 22v-23r (letter-shaped signs, no
  dividers): the cut of 23r l.1 drops signs.
- **Line finding.** 35r l.11 is merged with the Arabic of l.12 and is now classed Arabic (11 signs lost); lines are
  not re-found in v2.
- **Dividers.** A divider whose dots are faint (below the ink threshold) and whose stroke is alone is a sign; three
  dots fused into a ring with a big hole beside a stroke still count. On 37v-38r (bold angular hand) and 42v, 44r the
  divider counts are still off by 4-8 per chain. 'Divider accuracy' on the test set did not move (58 %), although the
  divider count error fell from 18 % to 13 %.
- **Over-merging.** The stacked rule can join two separate small signs written one over the other (seen once in the
  tiles checked, a pair like ع over 3) and joins pieces of Arabic words on lines wrongly classed cipher.
- **Touching signs** stay one box (fix 7 is off).
- **Pale pages ff. 1r-1v.** The rows are found, but show-through and texture add boxes (1r rows 18, 18, 20, 10, 15, 15
  against about 15, 15, 14, 13, 14, 14 by eye), and texture or faint Arabic below the block on 1v (lines 9-10) is
  classed cipher: the page-level total error of the rough tier is 29 % (v1 13 %, with its rows half missing).
- **Text block.** A single long line running past a crack (10r l.3) loses its end (`block_cov=1` would keep it but
  scores slightly worse on the tuning set).
- **Figure rows** with red letters on f. 63v are still classed cipher (red override).
