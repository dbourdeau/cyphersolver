# Proposal for `targets/sanchez1522` (R9614), sign plate of 25 Nov 2026

For Daniel Bourdeau. Prepared with Brice Dudout's agreement; not yet sent.

## Credit

This folder is ours (Brice Dudout, PR #479). The key is Daniel's (`../key_codes.tsv`, Tomokiyo 2025 + Daniel's
additions) and is not changed. No file outside `dudout/` is touched, and no other person's work is used.

## What this changes

R9614 (Alonso Sánchez to Charles V, Venice, 18 June 1522; DECODE R9614, RAH Salazar 9/24 ff. 208-210) gains 78 words.
On the README rule (sure words only) it goes from **62.4 % to 67.2 %** (sure + probable: 77.3 % -> 83.4 %). It stays
**read in part**. Details in `RECOMPTE-2511.md`.

## Why

The 12 Nov reading had 131 words marked † (they read only if one transcribed sign is taken as another). Most of them
came from one label slip: the transcriber wrote `9` for the conjunction "y" (40 times), while Daniel's table reads `9` as
l, and wrote `q` (s|t) for an l in "les", "le" and some other words. Looking at f. 208r, the hand seems to have:
a looped g-like sign (r: *republica*, *parecia*), a small g-like sign with a short tail (y: *fuy*, the 2nd g of
*instruydo*, and every "y" written `9`), and two stem signs: a round head on a straight stem (l: *ellos*) and the q of
*escritura* (s|t).

## How

1. **Sign plate 2511 (25 Nov 2026), f. 208r only.** Twelve questions: nine target signs and three hidden controls of
   known answer (the looped g of *parecia*, the small 2nd g of *instruydo*, the q of *diputar*). Each question showed the
   line, the boxed sign and real examples of each candidate shape, cut from words of the same page; no value, word or
   place was shown. The selection rule was written and hashed before any thumbnail was cut
   (`sign_check_2511/REGLE-SELECTION.md`, SHA-256 6aa5b7cb…faeb4c); one amendment, made before any answer, only
   re-cropped six boxes (`AVENANT-CADRES.md`). The plate was built and scored by AI agents (Claude Opus 5.5). The
   checker, Brice Dudout, is the contributor of the reading, not an independent reader. Answers:
   `sign_check_2511/answers-2511-sanchez1522.json` (SHA-256 6daf3e85…79c1); decoded in `sign_check_2511/results.tsv`.
   - **Controls: 3/3 right.**
   - Five "y" signs written `9`: **5/5 the small g-like sign** (the threshold set in advance was 3/5).
   - Four l places written `q`: **4/4 the stem sign of *ellos***, never the q of *escritura*.
2. **What the rule then says** (written before the answers): split the g label by shape; a new label `gp` (the small
   sign) takes the value y, which is the y of the `(r|y)` pair the sign table already gives to `g` (your `alpha.py`
   has a separate y sign too). The l places are relabelled `9`. One line is added to the sign table of
   `scripts/decode_lot3.py` (`'gp':'y'`); no code group changes. R9607, R9610, R9640, R9647 decode exactly as before.
3. **Extension to the whole letter.** The places to relabel were found by aligning each † word of the classes 9->y and
   q->l with its line, then **every one of the 78 signs was looked at on the image** (zoomed line strips, the plate's
   thumbnails as models): 46 small signs (y), 32 round heads on a stem (l); none contradicted the alignment. Nine of the
   78 were seen by Brice on the plate; the other 69 were seen by the AI agent alone. The list, with the context and who
   saw each sign: `sign_check_2511/places.tsv`. The `9` of *ellos* is a stem sign everywhere and stays l.
4. **Re-tagging.** `scripts/autotag.py` (unchanged) tags the new reading; by hand: *infie-les* and *de-clararan*, split
   over two lines, are probable (they go through P = (f|s) and g = (r|y)); nine "y" and two short words were put back on
   their own signs (autotag's alignment does not see the tokens of words already in braces and had put them on a
   neighbouring g). No sure word of the old reading became probable or unresolved. No value is taken from the sense.
5. **Two words counted twice** in the 12 Nov reading are dropped (see `RECOMPTE-2511.md`).

## Words that move (78)

- `9` -> `gp` (y), 46: "y" ×40, *danyo* ×2, *seydo* ×2, *anyo*, *creydo*.
- `q` -> `9` (l), 32: *les* ×13, *le* ×3, *replicaron* ×2, *dixeles*, *razonables*, *establecer*, *infieles*, *ello*,
  *sale*, *replique*, *bolver*, *totalmente*, *salir*, *declararan*, *escrevirles*, *licencia*, *valientemente*.

The doubt left by this first plate (208v.27: the key spelled *danyo*, R9613 has *engaño*) is settled by part B below.

## Not done

The other g signs of R9614 (looped or small) are not reclassified one by one, so the words that hang on them stay
probable, as before. R9640 and R9647 have the same slip and are not relabelled yet. `R9614_text_es.md` and
`R9614_en.md` are not updated in this patch. The † classes Lo/s, "tt #", z/d and mo/i remain (45 words after part B).

## Part B — second sign plate (2511b, 25 Nov 2026): `oo` and bold `OO`

**Why.** The 12 Nov transcription noted no bold OO ("every ∞ is oo"), so the key read all 24 `oo` of R9614 as d. Looked at
one by one, the hand has two shapes there: two separate open ovals (once, 208r.07, *dispuesta* = d) and a closed
figure-eight (22 times; R9613 has a g at every one of them: *tregua* ×6, *engaño*, *gana*, *postigo*, *algunas*, ...).
A third, crossed sign (208v.07, written `oo?`) looks like the sign written `xo`.

**Plate.** Twelve questions: nine figure-eight places (208v.27 and eight others) and three hidden controls of known
answer (the figure-eight of *tregua* 209r.18; the `xo` of 209r.22 and of 210v.06). Options: three shapes only, cut from
R9614 (open ovals, 208r.07; figure-eight, 208v.02 and 209r.13; crossed `xo`, 208v.26 and 208v.13), plus "none / other
shape", "cannot tell", "illegible", "not a sign" and a remark field; no value, word or place was shown. The rule was
written and hashed before any thumbnail (`sign_check_2511b/REGLE-SELECTION.md`, SHA-256 21883723…bc5f06b). Declared
limit: the open-oval shape has a single example in the letter, so no control could test it. Answers:
`sign_check_2511b/answers-2511b-sanchez1522.json` (SHA-256 844ce91e…9680); decoded in `sign_check_2511b/results.tsv`
with the plate's key `sign_check_2511b/key-2511b-sanchez1522.json` (one internal note field removed; the original key
file had SHA-256 3cc911d10282c7c871dad92ee725f5d2ae9d724ae33e6f087cdf2e43950c8695).
- **Controls: 3/3 right.**
- **Targets: 9/9 the closed figure-eight**, 208v.27 included; never the open ovals.

**What the rule then says.** 208v.27 is `OO` (g): "en danyo" becomes *enganyo* = *engaño*, as in R9613. The threshold set
in advance for the whole letter (6 of the 8 other targets) is met, so the 22 figure-eight signs are relabelled `OO`;
the 12 not answered on the plate were each looked at on the image by the AI agent against the plate's thumbnails, and
none contradicted. 208r.07 stays `oo` (d); 208v.07 is not touched. `OO` = g is already in your `alpha.py` and in
`scripts/decode_lot3.py`: no script or code group changes. Words: `sign_check_2511b/places.tsv`; recount:
`RECOMPTE-2511b.md` (67.2 % -> **67.4 %** sure, 83.4 % -> **84.4 %** sure + probable, 1,256 -> 1,254 words; still read in part).
Patch: `sanchez1522-planche-2511b.patch`, to apply after the first one; it touches `R9614_signs.txt`, `R9614_decode.txt`,
`R9614_reading.txt`, `R9614_vs_R9613.txt` and `README.md` only. The R9614 figure in `NOTES.md` would become 845 of
1,254 = 67.4 %. Sign-check entry, if kept: 9 signs checked, 3 controls, 3 right.

## Applying it

From the repository root: `git apply targets/sanchez1522/dudout/sanchez1522-planche-2511.patch`, then
`git apply targets/sanchez1522/dudout/sanchez1522-planche-2511b.patch` (checked: both apply in that order to `main`).
It applies cleanly to `main` (2134221795). It touches only `dudout/`: `R9614_signs.txt` (the frozen 12 Nov file
335600be… with the 78 labels changed and a comment), `R9614_decode.txt` (regenerated by `scripts/decode_lot3.py`),
`R9614_reading.txt`, `R9614_vs_R9613.txt` (regenerated by `scripts/cmp9613.py`), `README.md` (R9614 figures) and
`scripts/decode_lot3.py` (one entry). `profile.json` and `NOTES.md` are yours and are not touched. The R9614 entry of
`profile.json` stays right: "read in part" does not change, and the relabelling is one label for one label, so the
measured length of `dudout/R9614_signs.txt` (2,965 tokens) is the same. If you keep sign-check entries, this plate would
be: 9 signs checked, 3 controls, 3 right. The R9614 figure in `NOTES.md` (785 of 1,258 = 62.4 %) would become 844 of
1,256 = 67.2 %.

No image is reproduced here; cite DECODE R9614.
