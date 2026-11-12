# Reader d, round 2: f. 406v ll. 21-33 and f. 411v ll. 1-3, legend

Blind reader (d), Andrew Beling's agent (Claude), 11 Nov 2026. Shapes only, named from `beling/catalogue/catalogue.md`. Nothing was decoded, and no copy, decryption, reading, key or other round-2 file was opened. Companion to `f406v_411v_cipher.tsv`.

## Pages and extent

- **f458.jpg, left page = f. 406v.** The folio number "406" is written at the top left, and the right page is "407". Line 20 is at y 2897-2921, which matches b's 2900. Line 21 is the next line below (y ~3037). The cipher block runs to **l. 33** (y ~4556). L. 33 ends with a gap and then clear writing in thinner ink ("Qui", into the gutter). L. 34 ("Je ferois fin ...") and the lines after it are clear and are not transcribed.
- **f463.jpg, left page = f. 411v.** The right page is numbered "412". There is nothing above the first line of text. **Ll. 1-3 are cipher.** L. 3 ends in cipher with `w`, then a comma and clear text ("Je vous" and a word that runs into the gutter). Ll. 4 ff. are clear.

## Counts

| page | lines | tokens | doubtful (`?` or `\|`) |
|---|---|---|---|
| 406v | 13 (ll. 21-33) | 494 | 34 |
| 411v | 3 (ll. 1-3) | 113 | 8 |
| total | 16 | 607 | 42 |

Per line, 406v ll. 21-33: 38 41 41 40 37 37 39 35 38 39 37 37 35. 411v ll. 1-3: 42 39 32.

Commonest names: `26` 52, `k` 45, `27` 42, `uy` 34, `d` 32, `E~` 31, `23` 30, `10` 30, `pi` 28, `19` 27, `q~` 27, `8` 27.

There are also two marked tokens, which are not counted as doubtful: `#23` (406v l. 33, the 2 is under an ink blot) and `-d` (406v l. 28).

## New names

None. Every shape fitted a catalogue name or a plain figure. Three names are uncommon in b's ll. 1-20:
- `3` standing alone (406v l. 28, twice), written `3|Z3`. The first has a round top and the second a flat top.
- `9` without a stroke before it (l. 31).
- `5` (l. 22, `5?`).

## Recurrent doubts

1. **`k` vs `z`.** Most small signs of this kind have the heavy left upright of `k`, often with a dot. Two (406v l. 21, l. 30) have a flat top stroke, a diagonal and a long foot, but are heavy at the upper left. They are written `k|z`. The small sign after 24 at the start of 411v l. 1 is `k?`. The "ck" form (406v l. 24) is written `k`, as the catalogue says.
2. **`uy` vs `y` / `s5`.** `uy` is usually a dot plus a 3-loop sweeping left. Two signs have only a dot-head and one arc (ll. 24, 31) and are written `uy|y`. One has a hooked top rising above x-height (l. 28) and is written `uy|s5`.
3. **`x` vs `alpha`.** The bold cursive x in this hand has a heavy lower-left blob, like exemplar `x_1`, and I wrote it `x`. Only the sign with a closed, pointed a-bowl is written `alpha` (l. 26). L. 28 is undecided: `x|alpha`.
4. **`D~` vs `tri`.** The A-shape crossed by a bar that runs out to the sides is `D~` (compare exemplar `D~_1`): 406v l. 25 (`D~?`), 411v ll. 1-3. The solid triangle with no bar is `tri` (l. 31).
5. **`Dot?`.** Reversed-C loops with an inner curl or stroke instead of a clear dot: 406v ll. 26 and 29, and 411v l. 1. The clear ones (dot inside) are written `Dot`.
6. **`19|9`.** A dot followed by a swash 9 (ll. 21, 23, 27), written as b wrote it in l. 19.
7. **`q~` with an open head.** Some crossed-descender signs have a 4-like open head instead of a 9-loop. I wrote them `q~`, with `q~?` where the stem barely descends (l. 22).
8. **Minim groups.** `mm` is used for three separate small minims (l. 28). The groups in l. 25 (three or four minims after a faint hairline) and at the gutter in l. 27 are `mm?`. The group in l. 25 that follows a long slash from below is `III`, joined to a small a-shape (`a~?`).

## Odd features

- **406v l. 22, insertion.** A long slanting stroke with a dot at its foot stands between `10` and `23`, and four signs are written above `23 22`: `^k ^x+ ^2+? ^7`. These may be an insertion. They are placed after `10` in the row.
- **406v l. 24.** There is a small arch between ll. 23 and 24 above a `19`, written `^arch`. A `6` there runs into the hooked foot of the l. 23 `q~` (`6?`, perhaps `6~`).
- **406v l. 28.** A `d` is crossed by a heavy horizontal stroke (`-d`).
- **406v l. 33.** A large loop under the second `23` reaches into l. 34. I take it as a flourish of the clear line and did not tokenise it.
- **Vertical ruling.** A vertical ruling (hairline) crosses or touches signs in ll. 26 (from `H`), 27 (`d`) and 32 (`8`).
- **Figures with dots.** Some figures are written with a dot between or under their parts (`2.7`, `2.9`, `2.6`). They are noted, not tokenised. Separate dots or strokes standing clearly before a sign are tokenised as `1?`; there is one case, l. 23 before `k`.
- **Gutter.** Every line runs into the gutter. The last sign is often cut, and signs hidden there are not recorded.

## Method

- **Crops.** Each line was cut at native resolution into four overlapping pieces: x 620-1520, 1460-2360, 2300-3200 and 3140-3920 on f. 406v, and 1000-1760, 1720-2480, 2440-3200 and 3160-3840 on f. 411v. Each piece was 260 px high, centred on the line, with y interpolated along the line because of its slope, and enlarged 2x with `sips`. The files are `work/d_round2/lNN_k.jpg` and `vN_k.jpg`.
- **Overlaps.** The overlaps were matched by native x, so that each sign is counted once.
- **Close-ups.** Doubtful signs were zoomed 4x (`z*.jpg`, `y*.jpg`) and compared with the catalogue exemplars and with b's crops of l. 20.
- **Line centres.** They come from row ink profiles in three x-bands, computed with standard-library Python from a BMP made by `sips`.
