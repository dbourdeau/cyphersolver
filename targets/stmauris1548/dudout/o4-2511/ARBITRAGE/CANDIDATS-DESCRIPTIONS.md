# Candidate names and shape descriptions for arbitration (shapes only, NO values)
## Reference list 1 — input/SIGNS.md (WAINUT)
One token per sign, separated by spaces. A raised mark is written straight after its base sign, with no space.

Raised marks: `o` small raised ring (as in 3°, 4°), `2` raised 2-like mark, `3` raised 3-like mark, `s` raised
s-like mark. So `3o`, `4o`, `12`, `x3`, `mx2`, `4s`. A dot after a sign on the line: `.` as its own token.

Base signs (descriptions; reference crops are in scans/, e.g. c3r_L08-11.jpg):

| name | shape |
|---|---|
| `O` | two small rings joined by a horizontal bar (dumbbell), the most frequent sign |
| `d` | small loop with a tail rising to the right, like a reversed e with an upstroke |
| `dd` | two such loops joined |
| `D/` | the same loop crossed by a long oblique stroke |
| `vt` | a v joined to a small cross, like the letters "vt" |
| `a` | alpha-like loop with a tail (α) |
| `w` | small cursive w with loops |
| `W` | capital W, often with a crossing stroke |
| `x` | plain x |
| `x:` | oblique stroke with a dot above and a dot below (like ÷ tilted) |
| `+` | small cross (usually with a raised o: `+o`) |
| `#` | double-barred cross, like H with crossbars |
| `sq` | small square |
| `n` | n shape, sometimes with a tail |
| `@` | large curl: ring with a long tail down |
| `mx` | m joined to an x-like stroke with a long descending tail ("my") |
| `eee` | chain of small loops, like "eeo" |
| `Le` | looped l followed by a small c or e |
| `R` | R-like sign |
| `q` | 9-like: ring with a descending stem |
| `&` | ampersand-like |
| `fs` | f-like stem with a loop on the right |
| `4` | figure four |
| `b` | b-like looped stem |
| `y` | r-like or gamma-like sign with a descending loop |
| `z` | z |
| `u` | u |
| `1 2 3 5 6 8` | digits |

Unknown shape: `N1`, `N2`, ... and describe it once at the end of the file. Doubtful reading: add `?` (`4o?`).
Struck or cancelled: add `_`. Page punctuation: `/` and `(` as written. Clear words inside a line: in quotes.
Ignore small letters written above or between the lines in another ink (later glosses): do not transcribe them.

## Reference list 2 — input/SHAPES-KEY-NAMES.md (WAINUT)
For the blind transcribers of PREREG-O4. Use these names ONLY when the shape matches the description. Any other shape not in
SIGNS.md or below gets YOUR OWN name `t1`, `t2`, ... (never `N...`), described once at the end of your file.
Compiled on 25 Nov 2026 from WAINUT's public files of `targets/stmauris1548` (cyphersolver origin/main b81c613843): the
"N-signs" section of `transcription_l2_passA.txt`, the N-list of `transcription_l4_blind.txt`, the header lines of
`transcription_l2.txt` / `transcription_l4.txt` and NOTES.md "fixes of 3 Nov". Wording shortened; reading contexts and
values removed. Names of the key that have no usable description here (`N1b`, and the value-less `N19`, `L1`) are left out:
such shapes get a `t` name.

Composite names follow the SIGNS.md rule (base + raised mark glued): `xo`, `5o`, `6o`, `2o`, `4s`, `vto`, `N7o`.

| name | shape |
|---|---|
| `N1` | q-like ring at the top of an upright stem, the stem crossed by one or two horizontal bars (a 9 standing on a double cross) |
| `N2` | small t-like cross joined to a following u/n/i minim (looks like "tu", "ti", "fu"); often lighter ink |
| `N3` | downward-pointing triangle (a v closed by a bar on top) |
| `N4` | small free-standing closed ring or D-shaped loop at line height, no tail (not `d` with its long upstroke, not a raised o) |
| `N5` | figure 4 whose stem ends at the foot in a closed loop (4 over a b-bowl), sometimes a dot at upper right |
| `N6` | small loop at the bottom with a stroke rising to a horizontal top bar hooked to the left (a 7 over an o, a capped delta) |
| `N7o` | m-shape (humps, no x, no descending tail) with a raised o |
| `N8` | t-like cross joined to a 3 (looks like "t3" / "tz"), short stem |
| `N9` | small ring joined on the left of a `#` (like "o#") |
| `N10` | large fs-like sign (cross-stroke, loop, long descender) with an extra looped stroke rising on top (fs and b run together) |
| `N11` | upright cross with a small ring at the top of the stem and a closed loop at its foot |
| `N12` | cross whose upright has a tall ascender curving up and right, joined at right to a 3-like bowl (a tall "t3", like B/13 with a cross) |
| `N13` | the same tall bent-stem cross with a small loop at its right on the line, the stem stopping at the line (a tall "to") |
| `N14` | two-loop chain: small open loop, long U-swing, closed (often inked-in) loop at right ("u-o"); `eee` has three loops |
| `N15` | 8-like sign with a horizontal stroke or hook across / over its top, top loop open (like a sharp s); plain `8` has none |
| `N16` | small loop joined to two uprights crossed by one bar ("o#", like a vt with a double cross); close to `N9`, which is a ring on the left of a full `#` |
| `N17` | A-like: long oblique stroke rising from lower left, short upright, small ring at top right, no crossbar |
| `N18` | long f-stem with a foot curling to the lower left, crossed by a bar, with a small n/r at the right ("fn") |
| `N20` | 8-like loop with a raised ring (not the R-like `R`) |
| `Le` | looped l followed by a small c (SIGNS.md: "c or e"; here c only) |
| `Lo` | looped l followed by a small o |
| `eo` | open e-loop followed by a small ring, written as one sign ("eo"), without the looped l ascender |
| `fz` | f-like stem with a y-like descending tail (sometimes a dot above), as opposed to `fs` (loop on the right) |
| `phi` | phi-like curl: open c-curve run into a p-like loop, often light ink |
| `yg` | the gamma-like crossed loop (often with a dot above); `y` is kept for the r-like / n-like sign with a descending loop |

## Pass A — its own t-shapes (renamed tA-...) and naming conventions, as written in its header
  tA-t1  3-like sign whose lower bowl is closed flat (3 standing on a closed flat loop), no raised mark (5r L06 start)
  tA-t2  cursive n/m-like: arching first leg with long descending stroke, small hooked second hump ("n" with a long left leg)
  tA-t3  a 6 whose top curls over in a high arch down into a small closed ring at right ("6" and "o" joined by an arch)
  tA-t4  p/y-like: small loop on the line with a long stem descending and curling to the lower left (an inverted "p" with swash)
  tA-t5  small closed loop with a thick hook/flag rising at its upper left ("ɒ"/"x"-like small loop, like a d with a short hook)
  tA-t6  dumbbell O with a dot above the bar
  tA-t7  looped tall l (like L of Le) followed by a short separate vertical stroke (l + i), not c/e/o
  tA-t8  dumbbell whose left ring is crossed by an oblique stroke
  tA-t9  long f-stem with foot curl, crossed by a bar, followed by a small ring and a c ("for"-like)
  tA-t10 open ring enclosing a 2 (circled 2)
  tA-t11 d-loop with its tail, with a dot above
  tA-t12 (not used)
  tA-t13 figure 4 whose top closes into a loop/flag, with an extra short stroke on the left (no separate raised o)
  tA-t14 x with raised 3 and a b-like closed loop joined to its right arm (5v L18)
 Conventions: @2 = large curl/ring with a 2-like mark inside or raised (5r); N-names from SHAPES-KEY-NAMES.md
 6r L24 'D/?' (b-like loop crossed obliquely) and 'O?' (dumbbell with inked right ring) ; tA-t5 vs d, tA-t2 vs y/n, tA-t4 vs y

## Pass B — its own t-shapes (renamed tB-...) and naming conventions, as written in its header
   names from SIGNS.md and SHAPES-KEY-NAMES.md only when the description matched; other shapes = tB-t1..tB-t14 (below).
 Conventions used: `+o` = plain small cross with a small ring at its right (not the tall bent-stem N13); `@2` = large curl @ with a 2 inside;
   `12`/`13` = upright 1 with flat foot and raised 2/3; `mx2`/`mx3` = mx with raised 2/3; `phi` used for the c-curve + p-loop sign
   (also the larger hump variants); `b` = upright stem with small upper loop and lower bowl; `N15` = 8 with stroke/hook across top.
   tB-t1  = a 3 standing on a horizontal foot stroke (closed flat base), followed in 5r L06 by a dot
   tB-t2  = long stroke rising from lower left (often curled foot) to a short top bar ending in a loop at upper right; slanted p-like, no second diagonal (not xo)
   tB-t3  = dumbbell O with a dot above its left ring
   tB-t4  = small x whose right arm runs into a closed loop on the line (x+o at line height, no raised ring)
   tB-t5  = small closed ring / small down-pointing triangle with a dot above
   tB-t6  = vt with a dot above
   tB-t7  = "fo": long f-stem (top bent right, foot turned to lower left) crossed by a bar, small ring at right on the line
   tB-t8  = looped l ascender followed by a short separate upright stroke ("Li"), no c or o
   tB-t9  = a 3 whose top stroke runs into a crossing stroke and an open loop at upper right (3 with attached x-like raised loop)
   tB-t10 = tall stem bent up-right at top, crossed, running down into a large closed bowl at the foot with a loop to the right (6-like, no descender; cf. fz)
   tB-t11 = dumbbell O whose left ring is crossed by a short oblique stroke
   tB-t12 = "for": long f (foot curling to lower left, crossbar) + small o + small r/c, written as one group
   tB-t13 = 3 with raised o, crossed by a short vertical stroke through its middle (correction?)
   tB-t14 = d (loop with stroke) with a dot above
   5v L12 first sign eee? (messy, possibly corrected) and Lo? (l + small loop, could be Le); 5v L17 z? (2-shaped z) and .? after fz;
   5v L18 x3? (x with loop on right arm + raised 3, maybe tB-t4+3); 5v L30 4o? (small, crowded after &); 6r L24 tB-t4? (light x with open curl);
   dots above signs (tB-t3, tB-t5, tB-t6, tB-t14) may be stray ink; small dots ignored: 6r L03 dot above mx2, 6r L07 dot above z, 6r L10 dot after phi,
   6r L19 high dot above first O, 6r L27 dot above w; 5v L02 small mark above O ignored (gloss-like); 5v L04 tick after 6 ignored.
