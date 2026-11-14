# barbavara1447: "Cologna" is in the cipher; key-only decoder of the f. 135/143 runs (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Image check: f. 68 "Monsignore da Cologna"
NOTES listed this as a gap: "the cipher at that word was not compared; a copying slip by the evidence". The cipher
f. 69 was checked on Gallica btv1b100373864, canvas 65 (lower slip, l. 2, full size). After `ꝗ fto o-` (papa),
`Є p7 fo ꝺ7 ⊃ per ÷` (m-on-s-ig-n-or-e) and `♀ o-` (d-a), the word is written **`ott p+ p- ⊃ o-`**: c-ol-og-n-a.
`ott` is the key's c (spot-checked on f. 40), not one of the b signs (B-barred, o+). So *Cologna* is in the cipher.
The late copyist copied it faithfully, and the slip goes back to the encipherer or the writer. The gap is removed from
NOTES. The notes in `texts/decipherments_18c.md` and `_en.md` now say "so in the copy and in the cipher".

## Decoder
`verify_dudout_20261114.py targets/barbavara1447` reads the sign values listed at the head of `texts/glossed_letters.md`
("read off R1857 P11") and the code and spot signs of `key_R1857_codes.tsv`. It deliberately leaves out the values the
notes infer from the glosses (t-o = i, h = l, fto = ap, ϵg = s, ꝕ = n). It then aligns each run of `glossed_runs.tsv`
with the "deciphered" column (dynamic programming; a sign fits when one of its key values spells the next letters).

| runs (label in the table) | runs | signs that fit a key value |
|---|---|---|
| f. 135 (4 runs) | 4 | 63 / 79 |
| f. 143, K ("every sign read with the key and agreeing with the gloss") | 9 | 56 / 84 |
| f. 143, K+G | 25 | 90 / 243 |
| f. 143, "K for …" (143.4, .12, .41) | 3 | 19 / 38 |
| f. 143, G and "-" | 8 | 13 / 51 |
| all deciphered runs | 49 | **241 / 495 (0.49)** |

Only 143.8 (*al dinaro*), 143.25 (*accordato a*) and the code sign 135.2 (*Re*) fit sign for sign. The other "K" runs
also use signs that are not on the key list: 143.24 (11/21: t-o, ʒ=, ꝺ-o, fto), 143.26 (4/8: 9#, h=, t-o), 143.48
(12/17: fto, ho-, t-o). So the f. 143 count "9 from the key with the gloss agreeing" overstates what the key copy gives
alone. Most of the text rests on the glosses. That is fine for a reading, but the table's K/K+G split should not be
quoted as key confirmation. Signs most often outside the key list: t-o (30x), h (19), h= (15), ϵg (10), ꝺ (9),
fto (7), ꝕ (7), d- (4), ʒ= (4).

Two internal inconsistencies:
- ʒ= is given *an* in 143.4 (*mandato*) and *am* in 143.24 (*etiamdio*), both under K. On the key list an = ꝁ and
  am = Ŧ.
- 9# is read *ag* (143.26, .30), but the key list gives ag = ꝺ# / 9÷o.

## Read bar (README)
`v10_relabel.measure` uses the one file `glossed_letters.md` for both entries, so it gives f. 135 and f. 143 the same
figure, 0.976. Measured per letter (the Text sections only), the shares are:
- f. 135: 1.0 (89 words), the same as recorded;
- f. 143: **0.9496** (641 words, 34 holes), against read_share 0.9 recorded. The 0.9 is a run count (46 of 51), not
  a word share. The word share is just under the 0.95 bar (it rounds to 0.950 at three decimals). *read in part*
  stands on the strict figure; left to the maintainer.

The clear copies (`decipherments_18c.md` 0.996, `pusterla_copies_a.md` 0.984, `_b.md` 0.991) have no read_share
recorded. All are above the bar.

## Key correction
None to R1857 values. The K labels and ʒ= / 9# above are labelling points.

## Not done
The f. 143 signs were not re-read on the image (canvas 136), and the R1857 key image (DECODE, not public) was not
seen. The second sign-by-sign pass that NOTES asks for is still open. No human palaeographer.
