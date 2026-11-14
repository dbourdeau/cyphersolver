# gerlach1252: decoder re-run, and the doubtful signs of p.7 re-read on the Wellcome image (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder

`verify_dudout_20261114.py` reads only `key.tsv` and `transcription.txt`. It decodes all 348 lines, and all 348 have
the same letters as `decryption.txt`; pictograms and damage marks are left out of the comparison. It gives the same
result on the corrected files below.

## Image check: p.7 (scan b19695561_0012)

Source: `https://iiif.wellcomecollection.org/image/b19695561_0012.jp2/full/full/0/default.jpg` (3078 x 5250,
Public Domain Mark), fetched once by curl. It was read in bands of 2-3 lines at full resolution. No image is in the
repository.

The three figure-4 shapes are told apart easily on this page. The open "ч" form (4L, l) has no closed top. The closed
form with the stem through it, ending in a point (4R, r), is a kite on a cross. The modern closed form with a flat foot
(4U, u) is used in "ruret" and "thue". The page carried 45 of the target's 4-shapes marked doubtful. Every one was
looked at, and each agrees with its shape. Their "?" are removed in `transcription.txt` and `decryption.txt`.

Three readings change. They are on the image, and they bring the decode into line with what the reading already
proposed:

| line | was | image | decode now |
|---|---|---|---|
| L07 word 2 | `PI LEO OL? PHI DOT 4R?` "sol?uir?" | π, δ with its curl (LEO, one sign), ⊕, ⊙, open 4; there is no o+ sign | `PI LEO PHI DOT 4L` "souil" (reading.md: "souil") |
| L07 word 4 | `SQ? LEO 4L? ST LAM` "a?olet" | the first sign is the rhombus, the same as the first sign of "wefel" in the line | `RH LEO 4L ST LAM` "wolet" (reading.md: "wolet?") |
| L13 word 1 | `EUR 4U? PLUS? ST TRI` "ru?h?et" | €, a closed flat-foot 4, then a pale figure 4 (not a plain cross), st, ▽ | `EUR 4U 4R? ST TRI` "rur?et" = ruret, rühret (reading.md: "ruhet? [ruret?]"; "ruret es tzu weilen umb" in L17) |

After these changes, p.7 has 7 doubtful signs instead of 54. The 7 are LAM? (L01), X? (L13, L18), CC? (L14),
EUR? (L17), PST? (L21) and the pale 4R? (L13).

**Suggested for `reading.md` p.7 (not changed here; the maintainer's count):** "souil ir wolet" without "?"; "ruret in
wol umb" in place of "ruhet? [ruret?]". The end of L24, left untranscribed, shows LEO, a d-sign, st and a 4 crowded
against the frame rule. That fits "o[der]", but only as a probable reading.

## Not done

- The other pages were not re-read. The figure-4 shapes still marked doubtful are: p.8 2, p.9 3, p.10 5, p.13 3,
  p.16 1, p.107 1, p.112 6, p.115 1, p.177 1. The s-signs and the stained foot of p.9 were not re-read either.
- The read share was not recounted. `reading.md` is unchanged, so the 90.3% stands until the maintainer applies the
  suggestions above.
