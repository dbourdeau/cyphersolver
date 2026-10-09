# Reading guide for the Ottobon 1589 cipher (working file for the hand reading)

The key is the Council of Ten's **Zifra Prima** (DECODE R1789), transcribed in `keys/zifra_prima_R1789.tsv`
(code -> value; `_` = null; `#n` = numeral n; one-letter values are single letters; `lla`, `pro` etc. are syllables;
capitalised values are nomenclator words, often truncated stems: *Necess* = necess-, *Nostr* = nostr-, *Altr*, *Tutt*).
Plaintext is Italian chancery prose of the Venetian Senate (Doge and Senate to Giovanni Mocenigo, ambassador with
Henry III of France, 27 April 1589). Words are spelled out of syllables + letters, e.g. *soccorso* = h4 a49 c99 h4.

The first-pass transcription (`ct_f*.txt`) misreads digits **systematically**:
- the hand's **7** is a z/ʒ shape and was read as **2** (no 7 at all in the first pass: c2x is mostly c7x = lla lu lo
  li le la ma me mi mo; d20 = d70 *Del*; g20 = g70 *da*; d2 = d7 *pa*; g12 = g72 *de*);
- the **8** is a small closed loop read as **0** in the units (a20 = a28 *che*; f10 = f18 *ne*);
- **3 / 5 / 8** are confused in the tens (d83 = d53 *a*; d85 = d55 *n*; c86 = c56 *in*; h5x often h3x: h52 = h32 *ti*,
  h50 = h30 *ta* or h50 *va*; h2x often h3x: h22 = h32 *ti* where *Sua M.tà Christianissima* makes no sense);
- **1 / 7** sometimes (g12 -> g72, f15 -> f17 *na*);
- base letters are reliable but not perfect (c/a/d occasionally).
Plus ordinary random misreadings (~15 %).

Tools (run from targets/ottobon, `python -I`):
- `python -I ws.py ct_f37r.txt` — per line: each token with its Zifra Prima candidates under the confusions, and the
  machine draft (beam) line; then the whole page draft.
- `python -I cands.py <file>` — candidates only.
- line images: `img/dl/<page>_lNN_p0.png` (left half) and `_p1.png` (right half), from the full-size DECODE scans,
  cleaned. Line numbering of the crops can be off by one against the ct files; check the first tokens.
- full pages: `img/decode/IMG_R2252_I160NN_PN.png` (P2 right = f.35r; P3 = ff.35v|36r; P4 = ff.36v|37r; P5 = ff.37v|38r).

Method: for each line, choose for every token the code that (a) is compatible with the image and the confusion
classes and (b) makes Italian with its neighbours; look at the crop where the sense does not come. Do not force sense:
mark a token `?` when undecided.

Output, one file per page, `rd_<page>.txt` (e.g. `rd_f37r.txt`), appended line by line as you go:
```
# f.37r l.9
ct:  a28 a83 a51 c79 d70 c75 d7 c99 h32 a49 c75 c99 d23 h4 f18 g59?
rd:  che fa ce mo del la pa r ti co la r per so ne d?
it:  che facemo della particolar persone d[i]
conf: high
```
`ct:` the corrected codes (keep `?` on doubtful ones), `rd:` the unit values, `it:` the Italian as read with
word division ([...] for gaps, ... for unread), `conf:` high / medium / low.

**Update:** c86 reads as **o** in context (Serenissim-o, o-ltre, o-ttima), not *in*; d83 = **a**. See
`keys/ottobon_overrides.tsv`.

**Update (9 Oct 2026, later):** the reading is now driven by `dec.py` (calibrated decoder; `python -I dec.py calib`,
`decode`, `sim`) and `fit.py` (crib fit of a proposed Italian line onto the first-pass tokens). To add or change a
reading, edit the line's text in `texts_reread.txt`, check it with `python -I fitlines.py texts_reread.txt f35v:7`,
then `cp rd_hand1/rd_f3*.txt . && THR=-5 python -I refit.py --texts texts_reread.txt --write` and
`python -I measure_rd.py`. `lineview.py <page>` shows the hand reading, the decoder draft and each token's candidates.
Check every new text against `fitcontrol.py` (PERLINE=1): a line whose fit does not beat the wrong-line fits is low.
