# BnF Espagnol 318 no. 95: an unaddressed Spanish cipher letter, 8 Jan 1497 — George Lasry's alphabet

Status: in progress (f. 122v not decoded; the line-by-line correction walk of f. 122r and the retry are still to do)

Split on 14 Oct 2026 from `esp318` (the whole volume, catalogue no. 9) under the one-key rule (George Lasry,
14 Oct 2026). This letter is the only one in the volume in Lasry's 2022 alphabet; the other ciphered letters of
Espagnol 318 are different ciphers, each with its own entry and page: [`targets/esp318/`](../esp318/NOTES.md)
(no. 92, the *Cifra general*), [`targets/federico1497/`](../federico1497/NOTES.md) (no. 5, Escrivà's cipher),
[`targets/esp318no93/`](../esp318no93/NOTES.md) (nos. 93–94, key not identified).

**Outcome so far: read with known key, read in part** (about two thirds of f. 122r; f. 122v not yet decoded).
Sessions of 17 and 21 Sept 2026.

The segmentation pipeline built for this letter, its outputs and its git-ignored intermediates stay in
`targets/esp318/`, run from there (shared with no. 93, whose glyphs it also segmented): `seg.py`, `glyphs.py`,
`cluster.py`, `montage.py`, `assign95.py`, `localseg*.py`, `viterbi95.py`, `hybrid95.py`, `linedp95.py`, `band95.py`,
`reseg.py`, `solve95*.py`, `lm.py`, `f122r_*.txt`, `f122r_*.pkl`, `f122v_reseg.pkl`, the strips in `ov/` and the scans
`full/f122r.jpg`, `full/f122v.jpg`. The line-by-line reading `f122r_reading.md` moved here.

## The letter and the key

F. 122 is a single leaf of 31 dense lines (canvases 458–459 of ark `btv1b52503046q`), no address, no salutation, no
clear word anywhere, dated 8 January 1497, three days before Federico's no. 5 at the other end of the volume.

Solved "approximately" by George Lasry in May 2022; Tomokiyo prints the key as an image only
(on cryptiana's page of Lasry's solutions; the page is saved as `targets/esp318/lit/crypt/GL.htm`, the image was not
kept), and GL.htm says the letter "is solved"; no
plaintext has been published. The alphabet is homophonic, one to three signs per letter, plus unassigned signs and the
code groups `bac bnh bon dah daf dae oht bed dal boo del`.

## Lasry's key applied by machine and checked by eye

Reading the signs by eye alone was not reliable (÷ against ≐, plain 7 against ᵒ7 and crossed 7), so f. 122r was
segmented and clustered: adaptive-threshold binarisation (`seg.py`), connected components grouped into glyphs by
x-overlap with diacritics attached (`glyphs.py`: 963 glyphs on 31 lines), Ward clustering of 28×28 bitmaps
(`cluster.py`, `montage.py`), the clusters labelled from the montages against Lasry's key (`assign95.py`). The clean
clusters carry 64 % of the glyphs and their frequencies are Spanish to the letter (E 9 %, A 7 %, O 5 %, N 5 %, S, C,
U, R, D, M, T, I, Q ≈ 1 %). The rest — two signs touching, or a sign cut by a descender from the line above — is
re-explained by FFT correlation against the cluster templates (`localseg2.py`, `viterbi95.py`), and a beam search
over a 5-gram Spanish model (`lm.py`, Don Quijote) fills those boxes while the verified glyphs stay fixed
(`hybrid95.py` → `f122r_hybrid.txt`, where `~` marks model-filled positions). Annotated strips with the machine
letter under each glyph (`ov/A95_NNa|b.png`) are the instrument for checking it.

Checked by eye on the strips, with Lasry's key, the following read cleanly (line numbers of f. 122r):
3 *…r. Despues…*; 4 *…emos franceses…* (the y-with-crossbar is F, as in his key); 6 *[bac] que puedan merc[ed]…
[de] Francia…* (the dotted x is his *p*); 8 *…con esto…*; 11 *Señoría … que esta … por*; 12 *que me toca… mucho…
será… que [bnh]… haga* (the group `bnh` written in clear letters mid-line); 13 *con esto… acorde… lo bueno…*;
16 *…que go[u]ierna[n]… pero*; 17 *…muy grandes cosas … no creo que…*; 19 *que se … encubre … que … quieren*;
22 *por obra creo que … amigo*; 23 *escreuir a…*; 25 *dificultad … en los…*. The letter is Spanish, in a court hand
of the 1490s, about the French — *franceses*, *Francia* — and about what a *Señoría* (Venice?) can or cannot be made to
do; `bac` and `bon` are nomenclator groups. Two of Lasry's signs were corrected on the way (the n-with-cross-tail is
M, not Y). His two 7-forms — plain 7 = D, 7 with a small o = S — are confirmed by *puedan* and *franceses*, and the
clusters separate them where the eye at this resolution does not.

A word-segmentation pass over the hybrid decode with a Spanish lexicon (`f122r_words.txt`, non-words bracketed) is the
honest measure of where it stands: only the eye-checked stretches segment into words. The line-by-line result is
`f122r_reading.md` (here): every line has verified stretches, the nomenclator groups are located (`bac`, `bon` ×2,
`bnh` ×4, `dal`, `bed`?), and lines 19–20 give *…quieren go|uernar…* across the line break. It is a reading of
perhaps two thirds of the signs, not a text.

Two further mechanical attempts did not help: clipping every glyph to its line band (`band95.py`) cut the tall signs
in half; a segmentation-free DP tiling (`linedp95.py`) reads the same lines the eye did and no more, and its language
model writes Don Quijote over the uncertain tiles (*don quiiote que el que*). Three independent readings (eye,
cluster-hybrid, tiling) agree on the same two thirds and disagree on the same third. The limit is the sign shapes at
this resolution, not the method.

## Remaining gaps

- f. 122r, about a third of the glyphs - blocker: illegible; eye, cluster-hybrid and tiling readings agree on the same two thirds; touching signs at 4077 px full resolution; the line-by-line correction walk is still to do
- f. 122v (five lines) - blocker: not-attempted; segmented (targets/esp318/f122v_reseg.pkl) but not decoded with the f. 122r templates

## Escalation

- [x] siblings: all thirteen cipher folios of the volume opened; no other letter in this alphabet, no decipherment of f. 122 anywhere in the volume
- [x] clear-pages: none; the leaf has no clear word
- [x] known-keys: Lasry's 2022 alphabet is the key; two of its signs corrected here
- [x] print: Tomokiyo's cryptiana (GL.htm and the key image); no plaintext published anywhere
- [x] key-rebuild: cluster labelling against the key, FFT template re-explanation, beam search with a Spanish 5-gram, DP tiling (see above)
- [ ] retry: not done — correct f122r_local2_keyed.txt line by line against ov/R95_*.png, then run the templates over f. 122v

## Next step

Finish the reading by correcting `targets/esp318/f122r_local2_keyed.txt` line by line against `ov/R95_*.png`, then run
the same templates over f. 122v. This is transcription work, not cryptanalysis. Lasry's own plaintext (2022), if he
will share it, would settle the unresolved third.

## Assumptions for George's review

- Your 2022 alphabet is credited on this entry only, as the key used and as a prior solution (GL.htm: "is solved"),
  with first_break "unpublished prior". None of the other letters of Espagnol 318 carries your credit.
