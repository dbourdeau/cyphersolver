# Sign catalogue and round-1 renaming: README

Andrew Beling's agent (Claude), 11 Nov 2026. This was a blind pass by shape only: nothing was decoded, and no copy, decryption, reading or translation file was opened. Nothing has been posted or committed.

## Files

| file | contents |
|---|---|
| `catalogue.md` | **63 letter-like and composite signs + 26 figures.** Each has a shape description, its confusable neighbours, the round-1 names it absorbs, and exemplars. |
| `../../work/catalogue_exemplars/*.png` | 88 exemplar crops |
| `../transcription/round1_catalogue/f406r_cipher.tsv`, `f406v_cipher.tsv`, `f410r_cipher.tsv` | The round-1 files with names changed to catalogue names. Same rows, notes and conventions; one header line added. |
| `../transcription/round1_catalogue/changes.tsv` | One row per change: page, line, token position (in the round-1 file), old, new, reason |

## Method

1. **Key and legends.** I read the key TSV, Tomokiyo's key image and WAINUT's sign list, then the three round-1 legends. From these I listed every name per reader, with counts.
2. **Leaves.** I read each page in 4-5-line blocks cut from the full-size leaves at native resolution (f458: 15 blocks, f457: 15, f461: 18). Each line was compared with its round-1 row, sign by sign, for the names in the brief.
3. **Close-ups.** I zoomed 2.5-6x on doubtful cases. Side-by-side montages were used to compare shapes across readers:
   - `k` against `z`
   - `yy` against `Z2` against `gam`
   - `Cm` against `M`
   - `>o` against `20` (all 12 of b's `20`)
   - `x` against `alpha` against `xd`
   - `va` against `III` + a-shape
   - `s5` against `h`
   - `rho` against `rho2`
4. **Renaming.** Tokens were renamed only where the shape on the image supports it. A token kept its `?` where it had one, except where the zoom settled the reading (for example `yy?` → `yy`).
5. **What was checked.** Every token in the brief's list was looked at in the block views. Close-ups were made only for the doubtful ones.
   - Renames marked [V] in `changes.tsv` were seen either one by one or in a block view where the shape is clear at 1x.
   - The `ephi` → `E~` change was checked on the image as one shape class across all blocks of f. 406v. It was not zoomed token by token.
   - The `w|uu` → `w|mm` change is [I].

## Changes

**198 tokens changed: f. 406r 37, f. 406v 144, f. 410r 17.** One change merges two tokens: b l. 5 `1? alpha?` → `ct?`. Positions in `changes.tsv` refer to the round-1 files.

| old → new | 406r (a) | 406v (b) | 410r (c) |
|---|---|---|---|
| `ephi` / `ephi_lp` → `E~` | | 59 | |
| `x` → `k` | | 40 | 1 |
| `z` → `k` (ll. 40-43) | 12 | | |
| `ck` → `k` | 6 | | |
| `Rbar` → `k` | | | 8 |
| `xdots` → `k` | | 1 | |
| `gam` → `yy` | | | 7 |
| `Z2` → `yy` | 2 | | |
| `yy?` → `yy`, `z` → `yy` | | 3 | |
| `20` → `>o` | | 7 | |
| `6b` → `6~` | 4 | | |
| `6_lp` → `6~`, `6` → `6~` | | 4 | |
| `la` → `La` | 3 | | |
| `zA` → `La` | | 4 | |
| `alpha?` → `xd` | 4 | | |
| `h` → `s5` | | 4 | |
| `rho2` → `rho` | | 4 | |
| `phi?` → `desp?` | | 4 | |
| `z` → `L` | | 3 | |
| `M` → `Cm` | 2 | | |
| `gn?` → `Cm` | | 1 | |
| `Hl` → `H` | | 2 | |
| `MC?` → `H?` | | | 1 |
| `2_lp` → `2~` | | 2 | |
| `2` → `2~` | 1 | | |
| `0?`, `6?` → `a~?` (after `III`) | 2 | | |
| `la?` → `va` | 1 | | |
| `alpha?` → `x`, `pi|x` → `x` | | 2 | |
| `k?` → `Dc` | | 1 | |
| `1? alpha?` → `ct?` | | 1 | |
| `^cap` → `^arch` | | 1 | |
| `w|uu` → `w|mm` | | 1 | |

**Checked and left unchanged.** On the image these agree with the catalogue as they stand:
- `2+`, `24` and `4`
- `que`, `9` and `q~`
- `Dot`, `cdot` and `c`
- `a~` and `II`
- the `1` tokens before non-figure signs
- a's `20` (6 seen, 5 confirmed) and `>o`
- c's `z` (all flat Z), `6b` (all with a flat bar), `L`, `La` and `Cm`

## Shape pairs not separated (left as they stand)

1. **`va` vs `II` + `a~` vs `III` + `a~`.** On f. 406r, two minims plus a joined small a appear both after a long slash (a: `III 0?`, now `III a~?`) and without one. Reader a wrote the latter `II a~?` (l. 43) and also `la?` (l. 33, now `va`). Reader b writes it `va` throughout. Whether `va` is one sign or `II` + `a~` cannot be decided on shape. Both spellings remain.
2. **`III` vs `N`.** Reader c's single `N` (l. 26) has the same shape as a's `III`: a long slash rising from below, then minims. Which key drawing fits is open, so both names are kept.
3. **`x` vs `alpha`.** The thin cursive x (open arcs) and the α-fish (closed left loop) are close in quick hands. a l. 43 `x|alpha` remains.
4. **`z` vs `2`.** b keeps three `2|z` (ll. 3, 6, 16): the top is neither clearly flat nor clearly round.
5. **`6~` vs `6b` vs `6` + `^arch`.** I separate them by the length of the stroke over the 6: a short flat bar is `6b`; a long arch over the next sign is `6~`. a l. 35 is `6~?`, because its arc may be a separate mark.
6. **`uy` vs `1 y`.** These depend on whether the sign after the stroke has a v-head (`y`) or a 3-head (`uy`). a's `uy?` tokens are unresolved.
7. **`E~` vs `f_`.** b's tall, bold `E~?` signs (ll. 11, 17, 20) may be `f_`. b l. 19 `ff?` may be `E~ f~`.
8. **The `1?` stroke or dot before `k`.** In b ll. 4, 7, 16 and 18, a stroke or dot before `k` stays a separate `1?`. `k` often carries a dot, so these may belong to the sign.
9. **Single-reader shapes, not resolved.**
   - b `Sb?` (l. 10, perhaps `f_ rho`)
   - b `sigma?|0`
   - a `ae?` (may be `k` with a tail)
   - a `Sr` (may be `dots3 f_`)
   - c `II?` (two long strokes, perhaps `f_ f_`)
   - c `12?`
   - b `x?` (ll. 13, 16) and the final `x` of b l. 2 (too small to class)
   - c `Rbar?` → `k?` at l. 19 (in the stamp)

## Naming questions for Andrew (choices made by shape, not forced)

- **`z` / `k`.** Tomokiyo's drawing for TSV `z` is a short upright with an arm and a foot bar, which looks more like `k` than the flat Z. WAINUT and readers a and c used `z` for the flat Z, so that use is kept and the upright sign is called `k`.
- **`E~` / `Z3`.** The TSV files the flat-topped Ʒ drawing as `E~`, but WAINUT's `E~` is the looped long s. WAINUT's use is kept, and the Ʒ shape is `Z3`.
- **`yy` / `Z2`.** The ζ-shaped sign is called `yy` because its head is y-like. The key's `Z2` drawing (2/Z with a tail) may be the same sign.
- **`xd` and `H`.** These may be the key's `Sb` and `MC` drawings. Neither fit is close enough to adopt the key name.
- **`La`.** It matches the key drawing that the TSV mentions as "zA", but the TSV gives it no name of its own (column 2 reads `uu`, Tomokiyo's note below it).
