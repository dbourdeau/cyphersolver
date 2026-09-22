# Forget / Matignon / Mayenne, BnF fr. 15572 (+ fr. 15571), 1586

Status: in progress. Read in part, measured 22 Sept 2026: 28% of the target's cipher tokens read as
sense (4,325 of 12,994 transcribed figures, 33%; 22% after a scrambled-key control), key for Cipher-1
recovered, Cipher-3 leaves untouched. Most gaps are workable (see "Remaining gaps"), so the target is
not closed. Per leaf: "Coverage, measured" below; `measure.py`, `measure.json`.

Catalogue item 12 (`CATALOGUE.md`), class B, solvability 5. Ten leaves that S. Tomokiyo
(`cryptiana`, *Henry III's Cipher with Ambassadors*) marks **undeciphered** although he publishes
partial tables for the two keys involved.

## What the target actually is

Tomokiyo's list, checked against the live page on 17 Sept 2026:

* **Mayenne–Forget's Cipher-1** (used among Mayenne, Forget de Fresnes, Villeroy and Henri III).
  Deciphered siblings in the same volume: **f. 14** (deciphered in f. 15), **ff. 18-21**
  (deciphered in f. 19), **ff. 78-79** and **ff. 91-92** (deciphered in the margin).
  Undeciphered: **ff. 110, 123-124, 143, 150, 154, 173, 196, 201**.
* **Matignon's Cipher-3**: deciphered f. 189 (in f. 190), ff. 277-278 (in ff. 279-280), f. 282
  (margin); undeciphered **f. 276**, and **f. 179 of fr. 15571**.
* fr. 15572 **f. 43** is in the catalogue line but is *not* open: George Lasry solved it in 2022.
* The catalogue's "fr. 15571 ff. 218-219" is a slip for **fr. 15572 ff. 218-219** (Matignon in
  Mayenne–Forget's Cipher-2).

Prior art checked: no printed decipherment of these despatches was found (searches on the BnF
catalogue and on the literature, 17 Sept 2026). Tomokiyo publishes short openings for ff. 143,
150, 154 and for "f. 111" (probably a slip for f. 110).

## Access: folio to Gallica canvas

fr. 15572 = ark `btv1b9061879d` (385 canvases); fr. 15571 = ark `btv1b90618802` (226).
**Each canvas is a double-page opening**, so the recto of folio *f* is the *right* page of a
canvas, and the verso of *f* is the *left* page of the next. The leaf carries two foliations,
the older one struck through; **the valid number is the lower of the two**. The offset from
folio to canvas drifts (about +2 at f. 14, +6 from f. 99 to f. 137, +7 by f. 142), so it has to
be read off the leaf. Fixed here:

| folio | canvas (page) | content |
|---|---|---|
| 14r / 14v | 16 right / 17 left | Forget to Villeroy, 24 Jan 1586; 4-line ciphered postscript on 14v |
| 15r | 17 right | the decipherment of that postscript, in clear, 3 lines |
| 78v, 79r | 85 left, 85 right | Mayenne to the King, camp de Tonneins(?), March 1586; cipher blocks with marginal decipherment |
| **110** | **116 right** | one leaf wholly in cipher, c. 48 lines, ending "De Bellebourg … jour de Mars 1586" |
| **123-124** | **129 right – 131 left** | despatch to the King: f. 123r opens in clear, then c. 140 lines of cipher over four pages |
| **143** | **150 right** | Mayenne to the King: clear first half (Marmande, Sainte-Bazeille, Castets, the capitulation), then 22 lines of cipher |
| **150** | **158 left** | a full page of cipher |
| **150** | **157 right – 158 left** | a page and a half wholly in cipher |
| **154** | **161 right** | clear opening, then c. 25 lines of cipher |
| **173** | **180 right** | "Sire" in clear, then c. 30 lines of cipher |
| **196** | **203 right** | clear to *auquel*, then the rest of that line and 30 full lines of cipher to the foot (31 in all; 26 transcribed) |
| **201** | **208 right** | the **same despatch**: clear a line and a half further, cipher, then clear again for the last three lines |

The clear openings identify the despatches: f. 123r "Sire, la dernière que j'ay eu l'honneur est
du huict[iesm]e de ce moys…"; f. 143 Marmande, Sainte-Bazeille, Castets and the capitulation;
f. 154 "Monseigneur, vous avez veu par la despesche du S.r Delorme … qui partit d'icy la veille de
Pasques" (Easter 1586 = 6 April), so f. 154 is to Villeroy, not to the King; f. 173 "Sire, Vostre
Majesté a esté suffisamment advertie par les deux dernières despesches de Monsieur du Mayne";
ff. 196 and 201 both "Sire, Depuis le partement du S.r de Bosseval…".

**ff. 196 and 201 are the same despatch** — see [`f196_f201.md`](f196_f201.md). That pair is now
the most tractable target in the item: it carries two cribs (f. 201 is in clear where f. 196 is in
cipher, at the head and again at the foot) and the two ciphered blocks are the same plaintext
enciphered twice, i.e. in depth.

All eight Mayenne–Forget leaves are now located on the image. f. 143 is the best conditioned:
a large, well-spaced hand, 21 lines. ff. 110 and 123–124 are the same cipher in a small, dense
hand — f. 123r alone runs to 38 lines — and are where the volume of text is.

## Method

1. `fetch.py` / `corners.py` / `folgrid.py` — IIIF fetch of the volume and of the folio-number
   corners, to build the index above.
2. `mklm.py` — a character 6-gram model of period French built from the 10 MB of Berger de
   Xivrey's *Recueil des lettres missives de Henri IV* already in `../bethune/xivrey/`
   (6.4 M characters after normalising: accents stripped, v→u, j→i, as the cipher does not
   distinguish them).
3. `flatten.py` — divides out a Gaussian background (flattens the parchment), then unsharp-masks.
   This is the single biggest gain in legibility of anything tried here and should be the first
   step on any new leaf. `tiles2.py` then cuts the block into per-line tiles for transcription by
   eye; `fitlines.py` + `recenter.py` place the lines.
4. `solve.py` / `dec.py` — a beam search over the token sequence where each glyph token carries a
   *set* of candidate letters, scored by the language model, then a dictionary word-segmenter.
   This is what makes the key usable: several glyphs of this cipher are genuinely confusable
   (Tomokiyo boxes three near-identical "6" shapes standing for **i, n, s**), so a
   one-glyph-one-letter transcription is not achievable by eye and the ambiguity has to be
   carried into the decoder.

## The key, as re-derived from the manuscript

Verified against the complete f. 14v/f. 15r crib ("Vous pouez juger que ceste ouverture n'est pas
toute nouvelle …") and against the cipher of f. 143. Values in **bold** are not in, or not
legible in, Tomokiyo's published table.

| glyph | letter | glyph | letter |
|---|---|---|---|
| ɑ (a with tail), Δ | a | ·v·, **ʄʄ (ff-ligature)** | n |
| ʠ | b, z | 7, H | o |
| ʃ (long s) | c | ᴄ, R | p |
| ϖ (m with overbar), ∞ | d | £, Ɛ, e | r |
| t, ʓ, Ƨ, ʋ | e | ∂, ɟ, **ɣɣ = ss** | s |
| M | f | m, **Ƶe** | t |
| 8, ▽, y | g | ʃ, s, Ɋ, ⊐ (box), **ꝉ (crossed t)** | u / v |
| f | h | θ, **₸ (crossed 4)** | m |
| o, 6, β, ε, 3, **ƀ** | i / j | n, A, **ʰe** | l |

Code groups seen so far: 12 *il*, 13 *qui*, 14 *que*, 47 *tous*, **49 (unidentified, frequent)**,
76 *le roi de Navarre*, 26 *vous/leur*.

## Result so far

**f. 143 (Mayenne to Henri III): 21 lines transcribed, about half read.** See
[`f143_reading.md`](f143_reading.md) for the text, `cipher_f143.txt` for the glyph transcription
and `reading_f143.txt` for the decoder's raw output. Tomokiyo printed
"s'estant laisse entendre 49 il se voulloit de partir du 76 duquel je scai quil est tres
malcontant et ayant considere que je lai tousjours ou y tenir pour le meilleur …". The reading
here agrees and runs on:

> … m'estant laissé entendre [49] il se vouloit départir du **roi de Navarre**, duquel je scai
> qu'il est très malcontant; et ayant considéré que je l'ay tousjours ou y tenir pour le meilleur,
> comme de [49] commandement qu'il ayt, et que ce ne seroit [une] petite faveur pour ses affaires
> que de …

Later stretches read "… le et service; il m'a promis de vous … faire pendant ce temps …",
"… ou à la vérité il s'est résolu … la composition de sa place, laquelle estoit encore …",
"… de séjour qui nous est très … parce qu'il m'eust fallu passer …". Lines 8-9, 14-15 and 19-21
still carry glyph errors and are not offered as a reading.

A practical note for whoever continues: **measure the line positions, do not assume they are
evenly spaced.** Cutting f. 143 on a uniform grid put the bands up to 60 px off by line 15 and
turned the second half of the page into noise; correlating a comb against the row-ink profile,
then refining each line on the local maximum, fixed it.

## Open / next

* Finish f. 143's weak lines (8-9, 14-15, 19-21). Everything there turns on telling apart the
  three "6" shapes (i / n / s) and the two round shapes (a / m); a labelled glyph atlas cut from
  the lines that already read would settle them.
* **ff. 196 / 201 first**: transcribe both blocks, align them, solve jointly against the two
  cribs. This is the one place in the item where the evidence is doubled.
* f. 110 is faded and dense (c. 48 lines); ff. 123-124 is the prize (four pages, c. 140 lines,
  opening in clear: "Sire, la dernière que j'ay eu l'honneur est du huict[iesm]e de ce moys …").
* A word-aware decoder (`wdec.py`, beam over letters *and* word boundaries, unigram word model
  swapped in for the character model over each closed word) was tried against the character
  decoder and does **not** help: on f. 143 the two agree on the lines that read and both fail on
  the same lines. That is the evidence that the residue is transcription, not decoding.
* The f. 18-21 / f. 19 crib has not been used yet and should settle the remaining homophones and
  the value of code 49.


## Where the work actually stops, measured

Two leaves have now been pushed hard enough to measure the cost of this cipher:

* **f. 143** (21 lines, the largest and cleanest hand of the eight) took *three* passes — three
  tiles a line, then five, then eight on the survivors — to reach about two thirds read. Lines
  1-7, 9-14 and 17 are continuous French; 8, 15-16 and 18-21 give clauses only. Line 8 resists
  even at eight tiles a line and flattened: it decodes to "a r o m e ? e [car] l m a l a i c t e
  d e n e p o r t e ..." and no reading of it is French, which most likely means a place or
  person name in it.
* **f. 196** (31 cipher lines counting the part-line after *auquel*; "36" was wrong; small hand) is not yet transcribed: the line fit alone needed a comb, a
  spacing-constrained DP, re-centring on glyph boxes and a manual offset, and still does not place
  every line well enough to tile. That is before a figure is read.

So the cost is roughly three tool-calls per line to get tiles the eye can settle, and about
fifteen per cent of figures resist anyway, to be recovered — or not — by the language model. The
eight Mayenne-Forget leaves are about 300 lines. This is a multi-session job, and the constraint
is the transcription of a 16th-century hand, not the cipher, which is solved.

### The order to do it in

1. **ff. 196 / 201** — the only place where the evidence is doubled (same plaintext twice) and
   where cribs at head and foot let segmented glyph boxes be *labelled*, which is the only thing
   that has actually broken a confusable pair so far.
2. **f. 143's** remaining eight lines.
3. **f. 154, 173** (clear openings, ~25-30 lines each).
4. **f. 110** (48 lines, faded) and **ff. 123-124** (140 lines) last: most text, worst conditions.


## Line placement is the unglamorous blocker

Worth writing down because it cost more than anything else here. Tiling a block into per-line
images needs the line centres to within about a fifth of the line pitch, or the tile clips and the
figures cannot be read. On these leaves the pitch is *not* constant — it wanders by 10-15 % from
line to line — so none of these alone is enough:

* a uniform grid from a comb fit (drifts; this is what silently corrupted the second half of the
  first f. 143 pass);
* local refinement on the ink profile (jumps to a neighbouring line);
* re-centring on the median glyph-box centre (`recenter.py` — returns almost no correction,
  because the boxes are already symmetric about the wrong centre);
* centre of mass of the x-height band (`center2.py` — best of the four, still leaves a systematic
  offset that varies per leaf and has to be found by eye on an overlay).

What works, and what the next pass should just do: draw the fitted lines on the flattened block,
look at the overlay, and set the per-leaf offset by hand — then tile with a band of about half the
pitch. f. 143 and f. 201 both fitted cleanly this way; f. 196 (the smallest hand) still does not,
and that is why its 31 lines were untranscribed at that point while f. 201's fit was ready to use.
(Later on 18 Sept, 26 of the 31 were transcribed: see "Coverage, measured".)


## The f. 18/f. 19 crib and the figures-to-French pipeline

The second half of the 17 Sept 2026 work turned on a crib Tomokiyo mentions in one clause and never
uses: **f. 18 is ciphered and f. 19 is its decipherment in clear**, about 1,650 figures with their
plaintext beside them. Full account in [`f18_f19_crib.md`](f18_f19_crib.md). In short:

* The pairing is verified twice on the leaf — f. 19r opens *"Que sa Majesté fust advertie"* against
  a cipher opening with `14` (*que*), and the cipher carries `52` where the clear reads *plustost*,
  the first check of Tomokiyo's nomenclature against a plaintext.
* It is **one key** across the leaves; an apparent contradiction with the ff. 196/201 crib was my
  own shorthand colliding on near-identical figures, not two ciphers.
* The confusable figures were **measured**: i/n, s/i and e/u sit at 0.91–0.93 correlation on the
  manuscript. They are not separable by shape at any resolution available, so **at the level of
  reading this cipher is polyphonic** — a figure is a small set of letters and only the language
  chooses. That explains every dead end: the shape classifier was always going to fail, and the
  early workaround `"6": ["i","n","s"]` in `key.json` was the right model all along.
* So the crib's output is stored as **labelled images**, not names: `exemplars/` with a manifest.
  103 figures over 18 of 22 letters at the time of writing; missing h, q, x, y, z.
* `readleaf.py` reads a line from figures alone — segment, match against exemplars, beam-decode
  with code groups — and recovers about **70 % of plaintext characters** on the crib leaf, with
  f. 18r line 3 read end to end: *"re et conseil des sembler de castille bour"*.
* Every free parameter is pinned by measurement against known plaintext, not by taste: segmenter
  gap 14, per-character bonus 1.6, code similarity floor 0.93.
* `baseline.py` scores the pipeline so a later pass can tell whether it helped — and its first job
  was to show that three lines is too small a test set to detect anything.

**The variable that remains is letter coverage.** Line 3 reads at 94 % because its letters are
covered; line 4 at 45 % because *instruction* wants p and q. Nothing else in the pipeline is
uncertain.

Two practical findings for whoever continues: **proper names are the densest exemplar source** (they
are spelled out rather than hidden in code groups — *Matignon* on f. 19r line 13 is nine consecutive
certain figures), and **exemplars do not transfer between scribal hands** — the same pipeline run on
f. 143 gives noise, because that is a different secretary.

## Session of 18 Sept 2026: six leaves read, and the target is not one cipher

**Read in substance or in stretches, all in the solved Cipher-1:** f. 143r+v (earlier), **f. 150**
(13 ciphered lines over a clear Forget letter to Villeroy, April 1586), **f. 154** (28 lines, the
army's pay crisis), **f. 173** (33 lines, to the King: no one will lend and no one will go surety),
**f. 196** (26 of its 31 lines transcribed) and **f. 201** (30 lines) — one despatch on two leaves, a siege report naming
**"le mareschal de Matignon"**, and **fr. 15571 f. 177** (28 lines, Mayenne's design for Gascony,
31 Dec 1585). See the `f*_reading.md` files.

**The ff. 196/201 check.** The two leaves were transcribed independently. Aligned figure by figure,
**57% of their figures are identical**, with 8 maximal runs of eight or more (longest 12); shuffling
one side gives 12% and no runs. That validates both transcriptions at once. (An earlier note said
"23 runs of eight" - that counted overlapping windows, not runs.) The 43% that differ are not noise:
a homophonic cipher offers several figures per letter, so f. 201 is a **re-encipherment** of the
same text, not a copy of f. 196.

~~**The target is at least three ciphers**~~ — **retracted** in `ciphers.md`: ff. 123–124, f. 110 and
ff. 78v/79r are all Cipher-1 (scrambled-key control and the f. 78v margin decipherment); the "three
ciphers" came from label drift between transcription sittings. The only other cipher in the item is
Matignon's Cipher-3 (ff. 276 and fr. 15571 f. 179). fr. 15571's ciphered page at canvas 187 left,
called "a fourth hand" here, **is fr. 15571 f. 179** (the slip is bound upside down; its foliation
reads 179 when turned), i.e. the Cipher-3 leaf, not a fourth cipher.

**A crib for the second cipher exists**: f. 79r (canvas 85 right), Mayenne's own letter from the
camp at Tonneins, 5 March 1586, carries a seven-line cipher block **with its decipherment down the
left margin**. "rouergue" matches the block's figures in exactly one place, giving `4+`=r, `6`=o,
`h`=u, `f`=e, `B`=g. **(Withdrawn: f. 79r is Cipher-1 and the solved key reads it; the single
"rouergue" hit was chance. See `ciphers.md`.)**

### Additions to the folio index

| folio | canvas (page) | content |
|---|---|---|
| **79r** | **85 right** | Mayenne to the King, camp de Tonneins 5 March 1586, signed Charles de Lorraine; 7 cipher lines **with marginal decipherment** — the crib for Cipher-2 |
| **125r** | **131 right** | clear letter: Castets besieged, the battery, M. d'Alincourt, Matignon, Mayenne |
| **fr. 15571 177** | **185 right** | Forget, 31 Dec 1585, 29 cipher lines in Cipher-1 (24 transcribed; foliated 190 struck / 177) |
| **fr. 15571 179** | **187 left** | the Cipher-3 slip, bound upside down (was listed here as "178v, fourth hand"); ~25 lines; `img/BnFfr15571f179.jpg` (cryptiana) carries an interlinear decipherment in magenta |
| **fr. 15572 276** | **285 right** | the other Cipher-3 leaf: a small slip, ~27 lines wholly in cipher; siblings ff. 277r-278r (canvases 286 right to 287 right, cipher) are deciphered in ff. 279-280 (clear from 288 right) |
| **fr. 15571 180** | **188 right** | (fixes the foliation: f. 180 recto is canvas 188 right) |

### Tools added

`rowcut.py` cuts rows with **alternate rows tinted**, so a row's left and right halves carry the
same wash and the join never depends on a line number — the fix for a full hour lost on f. 173 to
halves joined one row apart. `fitlines.py` fits and snaps a line grid. `hillclimb.py` is a cold
solver (annealing over figure→letter maps, `FIX=` to hold known values, `SEEDKEY=` to start from a
known key).

### A defect in the language model, found and fixed

Built with `v→u` and `j→i`, the corpus's Roman numerals became runs of `i`, and a page of `iiiiii`
scored **better** than French (−1.53 vs −1.51 per character) — so the cold solver collapsed every
figure onto `i`. Dropping Roman-numeral tokens and requiring a context to be attested 15 times gives
French −1.51, all-`i` −2.16, random −3.99. The old model is kept as `lm_v1.pkl`, the old scorer as
`solve_v1.py`.

## f. 110: identified, transcribed in part, not read

See `f110_status.md`. It is in the same key (decoded with the solved key it beats scrambled keys by
+2.07 per figure), but 18 of its 54 lines are transcribed and none of it reads continuously. The
diagnosis is transcription, not cryptanalysis: a solver seeded with the solved key moves 23 of 27
shared labels away from it, which means my names for this scribe's shapes do not match the figures
the key is keyed on. The fix is an exemplar set for this hand.

## Coverage, measured (22 Sept 2026)

The coverage figures in the `f*_reading.md` files ("about half", "two thirds") were estimates.
`measure.py` replaces them with a count (rule in its docstring; output `measure.json`): a cipher token
is **read** only if `key.json` gives it a value (tokens not in the key, `BOX`, `?` and unidentified
codes count unread) **and** its decoded letters fall inside a run of at least three corpus words
(count >= 20) totalling at least ten letters. Each leaf is decoded as `dec.py` does. Untranscribed
lines count as unread, estimated at the leaf's tokens per line (30 a line for untranscribed leaves).
Control: the same decoder and rule with the key's single-letter values shuffled (3 seeds).

| leaf | lines transcribed / on leaf | tokens | read | read / transcribed | scrambled floor | corrected |
|---|---|---|---|---|---|---|
| f. 110 | 37 / 54 | 1,699 (+781 est.) | 167 | 0.10 | 0.09 | 0.01 |
| f. 123r | 36 / 36 | 1,097 | 228 | 0.21 | 0.13 | 0.10 |
| f. 123v | 41 / 41 | 1,251 | 403 | 0.32 | 0.12 | 0.23 |
| f. 124r | 35 / 35 | 1,203 | 314 | 0.26 | 0.12 | 0.17 |
| f. 124v | 22 / 22 | 727 | 141 | 0.19 | 0.12 | 0.08 |
| f. 143r | 21 / 21 | 724 | 424 | 0.59 | 0.11 | 0.54 |
| f. 143v | 33 / 33 | 1,182 | 654 | 0.55 | 0.08 | 0.51 |
| f. 150 | 13 / 13 | 445 | 189 | 0.42 | 0.04 | 0.40 |
| f. 154 | 28 / 28 | 1,061 | 501 | 0.47 | 0.08 | 0.43 |
| f. 173 | 33 / 33 | 1,082 | 306 | 0.28 | 0.08 | 0.22 |
| f. 196 | 26 / 31 | 840 (+162 est.) | 376 | 0.45 | 0.07 | 0.41 |
| f. 201 | 30 / 30 | 987 | 455 | 0.46 | 0.07 | 0.42 |
| fr. 15571 f. 177 | 24 / 29 | 696 (+145 est.) | 167 | 0.24 | 0.14 | 0.12 |
| f. 276 (Cipher-3) | 0 / ~27 | (+810 est.) | 0 | – | – | – |
| fr. 15571 f. 179 (Cipher-3) | 0 / ~25 | (+750 est.) | 0 | – | – | – |
| **total** | | **12,994 (+2,648 est.)** | **4,325** | **0.33** | | **0.26** |

Of the whole target (~15,642 tokens) **0.28 is read (0.22 chance-corrected)**. 90% of transcribed
tokens are keyed; the gap between "keyed" and "read" is the transcription noise the notes describe.
The prose estimates were high on f. 143r ("two thirds": 0.59), f. 173 ("half": 0.28), f. 201 ("two
thirds": 0.46) and f. 177 ("a third": 0.24), and gave no figure for ff. 123-124 (0.19-0.32). f. 110
scores at its scrambled floor: unread, as `f110_status.md` says. Line counts checked on the images:
f. 196 has 31 cipher lines (26 transcribed; untranscribed are the part-line after *auquel*, the first
three full lines and the 13th, "mo£7om…"), fr. 15571 f. 177 has 29 (24 transcribed).

## Remaining gaps

- fr. 15572 f. 110 (54 lines, 37 transcribed; ~0% read) - blocker: not-attempted; same key, but the transcription is internally inconsistent and the exemplar set for this hand (cut glyphs, label against keyed figures) has not been built
- ff. 123r, 123v, 124r, 124v (4,278 figures; 21/32/26/19% read) - blocker: not-attempted; key verified on these leaves; re-transcription against the `key143_*.png` visual key not done (f. 123r was the first page transcribed in this hand)
- unread share of ff. 143r (41%), 143v (45%), 150 (58%), 154 (53%), 173 (72%), 201 (54%) - blocker: not-attempted; single-figure slips on confusable shapes; the higher-magnification second pass that closed f. 143r l. 7 has not been run on these lines
- f. 196: 5 of 31 lines untranscribed, 55% of transcribed tokens unread - blocker: not-attempted; part-line after *auquel*, full lines 1-3 and 13 never transcribed; f. 201 is the same despatch and a figure-by-figure crib
- fr. 15571 f. 177: 5 of 29 lines untranscribed, 76% of transcribed tokens unread - blocker: not-attempted; smaller hand, noisy transcription, no second pass
- Cipher-3, fr. 15572 f. 276 (canvas 285 right, ~27 lines) - blocker: not-attempted; not transcribed; key material exists (deciphered siblings f. 189/190, ff. 277-278/279-280, f. 282 margin; Tomokiyo's partial table)
- Cipher-3, fr. 15571 f. 179 (canvas 187 left, upside down, ~25 lines) - blocker: not-attempted; not transcribed; `img/BnFfr15571f179.jpg` (cryptiana) already carries an interlinear decipherment in magenta, not yet transcribed or checked
- names in ff. 196/201 (Sainct M-, la Bar-/la Garde, Montb-, la B-ault) - blocker: not-attempted; joint figure-by-figure reading of the two encipherments not done
- code 49 (frequent) and the other codes valued `+` in `key.json`; name codes 82, 84, 98 - blocker: open-codes; no context fixes them yet, and the siblings ff. 14/15, 18/19, 78-79, 91-92 have not been searched for each

## Escalation

- [x] siblings: ff. 14/15 and 18/19 cribs used to re-derive and verify the key; f. 78v margin decipherment used as a control (`cribem.py`); ff. 196/201 aligned (57% identical figures); f. 125r clear letter read for context. Not yet: ff. 91-92, and the Cipher-3 siblings ff. 189/190, 277-280, 282
- [x] clear-pages: f. 144 checked (a separate letter, not a clear copy of f. 143); f. 19 found to be the decipherment of f. 18; f. 125r is a clear letter, not a decipherment
- [ ] known-keys: Cipher-1 done (Tomokiyo's table, re-derived and verified on every Cipher-1 leaf); Cipher-3's key (Tomokiyo's partial table, deciphered siblings) not yet tried on ff. 276 / fr. 15571 f. 179
- [x] print: BnF catalogue and literature searched 17 Sept 2026, no printed decipherment; Tomokiyo's cryptiana openings for ff. 143, 150, 154, "111" used as checks. His f. 179 image with interlinear decipherment was saved but not transcribed
- [x] key-rebuild: key re-derived from the ff. 14/15 and 18/19 cribs, confusable figures modelled as letter sets, code values such as 17 *car*, 25 *nous* and 52 *plustost* added from context and the crib; cold and seeded solves on f. 110
- [ ] retry: done on f. 143r (three passes) and f. 110 (3 and 5 columns); not done on ff. 123-124, 143v, 150, 154, 173, 196, 201, 177, whose unread lines have had one transcription pass only
