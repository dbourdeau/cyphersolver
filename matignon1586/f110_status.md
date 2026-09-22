# fr. 15572 f. 110 — the one leaf I could not read, and the six things I tried

Canvas 116 right; foliation confirmed on the leaf (117 struck, **110** valid). Fifty-four lines,
**wholly in cipher from the first line** — no clear opening, no marginal decipherment, nothing on the
page to crib from. It ends "De Bellebourg … jour de Mars 1586". The hand is far smaller and denser
than any other leaf in the target.

## It is the same cipher as the other nine

Decode a sample with the solved key and score it; then do the same with scrambled versions of that
key — same symbols, same letters, values shuffled. Chance would put the two together.

| leaf | true key | scrambled | gap |
|---|---|---|---|
| f. 154 (reads) | −2.22 | −6.02 | **+3.80** |
| f. 124r (reads) | −2.31 | −5.36 | **+3.06** |
| **f. 110** | −3.31 | −5.38 | **+2.07** |

Far better than a wrong key, much worse than a leaf whose figures I have read correctly. The cipher
is not the problem.

## What was tried, and what each attempt measured

1. **Hand transcription at three columns a row** — 37 rows, 1,699 figures (`f110_cipher.txt`).
2. **Hand transcription at five columns** on sample rows: same figures, no improvement — so the
   magnification is not the limit.
3. **Automated glyph segmentation and clustering** (`glyphseg.py`, `glyphclust.py`), to bypass my
   eye entirely and solve on cluster ids. **Control: the same pipeline on f. 154, a leaf I can
   read, also fails** (−2.90 per figure, no language). The segmenter cuts cursive figures into
   strokes; calibrated against f. 154's known count it gets the count right but the clusters stay
   too impure (mean cosine 0.79). The pipeline is at fault, not this leaf.
4. **Crib fitting** (`cribfit.py`, `cribem.py`) — no crib exists for f. 110: the page has no clear
   text and no margin decipherment.
5. **Seeding the solver with the solved key**: on f. 110 it **moves 23 of 27 shared labels away**
   from the key, while leaving them alone on leaves that read. My names for this scribe's shapes do
   not correspond to the figures the key is keyed on.
6. **A cold solve on all 1,699 transcribed figures** (42 symbols, 40 figures per symbol): reaches
   **−2.27 per figure**, *better* than the −2.40 that a known-correct solution scores elsewhere —
   and still produces no continuous French, only fragments (*la venue de*, *que rien*, *les*,
   *et ne s'est*). A solve that hits the right score without producing language is fitting noise.

## The diagnosis, stated plainly

Taken together, (5) and (6) say the same thing: **my transcription of this hand is not internally
consistent** — I am giving the same shape different names in different places and different shapes
the same name. No amount of search fixes an inconsistent figure stream, and the automated route that
would sidestep my eye does not work on this script.

## What would finish it

An exemplar set built on this leaf itself: cut its glyphs, sort them by hand into classes, and label
the classes by matching against figures whose values the key already fixes — the work done for the
other hands, which is why they read. That is focused manual work on one page. I could not do it
reliably at this figure size in this session.

**This leaf is not read, and I would rather say so than publish a reading I cannot stand behind.**

**Correction (22 Sept 2026).** An earlier version of this line said "Nine of the ten leaves are read".
That was wrong. The other leaves are *read in part*, and measured (`measure.py`: a figure counts as read
only if the key gives it a value and it falls inside a run of real French words) the transcribed
leaves read between 19% (f. 124v) and 59% (f. 143r); overall 33% of the 12,994 transcribed figures,
28% of the whole target once the untranscribed lines and the two Cipher-3 leaves are counted. f. 110
itself scores 10%, against a scrambled-key floor of 9%, i.e. nothing. See `NOTES.md`, "Coverage,
measured".
