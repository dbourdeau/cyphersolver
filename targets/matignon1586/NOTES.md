# Forget / Mayenne, BnF fr. 15572 (+ fr. 15571 f. 177), 1585–86 — Mayenne–Forget Cipher-1

Status: read in part. Written up 22 Oct 2026 ([`docs/matignon1586.html`](../../docs/matignon1586.html)); page and
ledgers brought up to date the same evening. ff. 123r and 124r stay decoded, not read after three passes each; what remains needs a clear copy or another letter in the same hand (Remaining gaps).

**22 Oct 2026, the day in short.** George Lasry reviewed the page: "The decryptions are not useful. They seem to have
many errors, making it impossible to assemble coherent French sentences." The nine pages without a clear copy were
first relabelled *decoded, not read* (commit 021b4de9f). Then, following his method, each leaf was built into
sentences against the full-resolution images: every break cropped and looked at, Brackx's figure labels corrected
where the image disagrees (about 400 changes, `brackx2026/corrections/`), letter values added per leaf
(`key_cipher1_<leaf>.json`), the leaf re-decoded and read again, and an English translation written. Clean sentences
(`docs/_check_reading.py`, cipher part; a sentence is clean with at most one hole in ten words), before -> after:

| leaf | before | after | state | reading / log |
|---|---|---|---|---|
| f. 173 | 0.16 | 0.71 | read | `texts/reading_f173.md`, `_log.md` |
| ff. 196 / 201 (two fair copies of one enciphered draft) | 0.14 / 0.44 | 0.79 | read | `texts/reading_f196_201.md` |
| f. 196v (found untranscribed; Monségur, May 1586; 1,236 figures) | - | 0.71 | read | `texts/reading_f196v.md` |
| fr. 15571 f. 177r-v (clear copy found on f. 176r-v and transcribed) | 0.24 | 0.69 | read | `texts/reading_f177.md`, `reading_f177_vs_copy.md` |
| f. 110 (three passes; dateline Villeneuve-d'Agenais, not Bellebourg) | 0.23 | 0.70 | read | `texts/reading_f110.md` |
| f. 123v | 0.19 | 0.66 | read | `texts/reading_f123.md` |
| f. 124v | 0.12 | 0.72 | read | `texts/reading_f124.md` |
| f. 143v ll. 26-35 (after the copy's break; the copy continues on f. 155v) | 0.14 | 1.0 | read | `texts/reading_f143v_tail.md` |
| f. 123r (two passes) | 0.05 | 0.41 | decoded, not read | `texts/reading_f123.md` |
| f. 124r (two passes) | 0.28 | 0.56 | decoded, not read | `texts/reading_f124.md` |

* **Read and translated: 14 of 16 documents, 15,395 of 17,913 tokens (85.9%, measured on `documents[].length`).**
  Seven leaves read with the Cipher-1 key on the images (ff. 110, 123v, 124v, 173, 196, 196v, 201); ff. 143r-v,
  149v-150v and 154r-v read from their contemporary clear copies ff. 155-157 (Brackx, #70), and fr. 15571 f. 177r-v
  from its copy on f. 176r-v (found 22 Oct 2026), which the key's decode matches. The method is now *read with known
  key* (the copies are the second part, *read from existing decipherment*).
* **Decoded, not read: ff. 123r (0.41) and 124r (0.56).** Figures legible; the breaks are letter values the merged
  key lacks or writer's slips. Not counted.
* **Open inside the leaves that read:** f. 110 ll. 1-4, 8, 10, 14-16, 24-25, 36; code groups 16, 19, 23, 45, 47, 60,
  65, 67, 99, 101, 102, 103, 9 and the name code 98 (Remaining gaps). Settled today: 73 = *le Roy* and 64 = *quelque*
  on f. 177 (its copy), 63 = *après* (f. 201's clear tail), 59 = *argent* (f. 157r copy).
* **Not a second reader yet:** the label corrections were made and checked by one reader (Claude) on the images.
* Withdrawn as reading figures: 0.637 of tokens in runs of French (`measure.py`, before the review) and 0.315 (copies
  only, after it).
* **Next**: a hand-mapped atlas of the f. 123r and f. 124r hands (exemplars per figure, as for f. 110 pass 2) to test
  the remaining letter values, then the open codes; a second reader of the corrections.

The sections below are the history of the target, kept as written.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). This folder keeps **Mayenne–Forget's
Cipher-1** only. Matignon's **Cipher-3** leaves (fr. 15572 f. 276 and fr. 15571 f. 179, read by alejandrozarco in
PR #25) are a different cipher with their own entry and page: [`targets/matignon1586c3/`](../matignon1586c3/NOTES.md)
(`f276/` and `f179/` moved there). f. 79r is Cipher-1 (see below). The genuine Cipher-2 leaves, fr. 15572 ff. 218–219,
were not attempted here; Harumi-Matsuba read them (issue #49) and they are now the entry
[`targets/mayenne1586c2/`](../mayenne1586c2/NOTES.md), with two more Cipher-2 letters of fr. 15573 (ff. 120, 385).
fr. 15572 f. 43, solved by George
Lasry in 2022, is not a document of this entry and carries no credit here. Matignon's despatch to the King in his
**tuple cipher**, fr. 15572 ff. 234r–238v (May 1586; Michael Brackx, issue #86, taken in 24 Oct 2026), is another
different cipher with its own entry: [`targets/matignon1586tuple/`](../matignon1586tuple/NOTES.md).
Two more ciphers of fr. 15572, taken in 24 Oct 2026 from Michael Brackx (issues #91, #92), each have their own entry:
Camus de Pontcarré's blocks to Villeroy, ff. 111v–272v ([`targets/camus1586/`](../camus1586/NOTES.md)), and
Malicorne's letter from Niort, ff. 162–164 ([`targets/malicorne1586/`](../malicorne1586/NOTES.md)).

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
  (margin); undeciphered **f. 276**, and **f. 179 of fr. 15571** (both now read; the entry `matignon1586c3`).
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
| **110** | **116 right** | one leaf wholly in cipher, c. 48 lines, ending "De Villeneufve Dagenoys … jour de Mars 1586" (read "De Bellebourg" until 22 Oct 2026; checked on the image) |
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
| **total** | | **12,994 (+1,088 est.)** | **4,325** | **0.33** | | **0.26** |

Of the whole target (~14,082 tokens) **0.31 is read (0.24 chance-corrected)**. (Until 14 Oct 2026 the denominator
also carried ~1,560 estimated tokens for the two Cipher-3 leaves, giving 0.28 / 0.22; those leaves are now
`matignon1586c3`, measured there: f. 276 706/734, fr. 15571 f. 179 473/509.) 90% of transcribed
tokens are keyed; the gap between "keyed" and "read" is the transcription noise the notes describe.
The prose estimates were high on f. 143r ("two thirds": 0.59), f. 173 ("half": 0.28), f. 201 ("two
thirds": 0.46) and f. 177 ("a third": 0.24), and gave no figure for ff. 123-124 (0.19-0.32). f. 110
scores at its scrambled floor: unread, as `f110_status.md` says. Line counts checked on the images:
f. 196 has 31 cipher lines (26 transcribed; untranscribed are the part-line after *auquel*, the first
three full lines and the 13th, "mo£7om…"), fr. 15571 f. 177 has 29 (24 transcribed).

## Contributions of 21 Oct 2026 (Michael Brackx, issues #64, #68-#71)

Michael Brackx (@brackxm), working with Claude Code (Opus 5.5), posted five issues on 21 Oct 2026. They are folded
in here as contributed work, with credit in `profile.json` (provenance `mixed`). He gave no licence and no
repository, so his readings are summarised here, not copied; the issues hold his full text and figure tables.
None of it was checked by a second person against the images; what was checked here is listed at the end.

| issue | leaves | what he did | adopted here |
|---|---|---|---|
| #64 | ff. 196, 201 | joint figure-by-figure alignment of the two encipherments (914 columns, 487 identical), beam decode, f. 201 re-read on the image | all four names: **Sainct-Chamarand, la Barge, Montberault, la Binault**; content (Mayenne's fever, Matignon pressed to come, two trenches, battery of fifteen cannon); q = s (our own f. 196 head crib already implies it), f = h, ss = h; the clear phrase *Le regard dud. siege il s'advance fort* inside the f. 201 cipher block (checked) |
| #68 | f. 143r-v | decode with the corrected key; verso ll. 1-7 checked on the image | the treaty with the captain of **Castets** (12,000 écus in three months, leave to sell his property, a pardon to be registered by the Parlement); T= = r, a = a/m, c = p/l; 62 *peut*, 33 *vostre*, 40 *bien*, 54 *aussi*. **Not adopted:** 44 = *Sire* (he withdrew it himself); code 54's first value was inconsistent until the copy fixed it |
| #69 | f. 173 | decode; nine lines checked on the image | the credit crisis: no means to pay two musters, the town refuses to contribute on the strength of letters from the King, no one will stand surety, only merchants of Paris lend on the writer's word; 4+ = m/n, 8 = g/e. **Not adopted:** 79 = *pour* (one context). His notation block is pasted twice in the issue |
| #70 | ff. 154r-v, 155-157 | **found that ff. 155-157 are contemporary clear copies** of f. 143r-v (f. 155r-v), the ff. 149v-150 cipher (ff. 155v-156r) and f. 154r-v (f. 157r); read the copies by eye and aligned them with the decodes; found the f. 154v cipher (two blocks of about 11 lines) | the copies as the text of those leaves; codes 33 *vostre*, 36 *toutesfois* (not *avant*), 40 *bien*, 49 *comme* (not a null), 53 *affin*, 54 *aussi*, 62 *peut*, 76 *roi de Navarre*, 88 *Monsieur du Mayne*, 104 *mil*, `hash` *coustume* |
| #71 | ff. 123-124 | U = u/e/a, d = s/c, q = s/o/a (merged figure classes in our transcription); canvases 128-139 checked, no clear copy | the letter sets and the outline (no contributions without garrisons, the troops cannot be kept, the bearer sent for the King's intention, relief of places); partial, as he says: f. 123r still does not read |

**Key.** `key_contrib.json` (built by `mk_key_contrib.py`) is `key.json` plus his letter sets and the copy codes.
Not taken: `BOX` = u (in this transcription `BOX` also marks figures that could not be read), 44 = *Sire*,
79 = *pour*, and his figure names that have no token in our transcription (δ, ω, λ, ʒ as he names them).

**Re-measured (21 Oct 2026).** `measure.py --key key_contrib.json --control`, same rule as 22 Sept:

| leaf | read / transcribed, key.json | with key_contrib.json | scrambled floor | corrected |
|---|---|---|---|---|
| f. 110 | 0.10 | 0.09 | 0.09 | 0.01 |
| f. 123r | 0.21 | 0.27 | 0.15 | 0.14 |
| f. 123v | 0.32 | 0.39 | 0.15 | 0.28 |
| f. 124r | 0.26 | 0.35 | 0.10 | 0.28 |
| f. 124v | 0.19 | 0.38 | 0.12 | 0.29 |
| f. 143r | 0.59 | 0.63 | 0.09 | 0.59 |
| f. 143v | 0.55 | 0.66 | 0.07 | 0.64 |
| f. 150 | 0.42 | 0.48 | 0.08 | 0.43 |
| f. 154 | 0.47 | 0.56 | 0.08 | 0.53 |
| f. 173 | 0.28 | 0.49 | 0.09 | 0.44 |
| f. 196 | 0.45 | 0.54 | 0.07 | 0.50 |
| f. 201 | 0.46 | 0.62 | 0.10 | 0.58 |
| fr. 15571 f. 177 | 0.24 | 0.30 | 0.17 | 0.16 |
| **total** | 4,325 (0.333) | **5,480 (0.422)** | | 0.351 |

Of the whole target (~14,082 tokens) 0.389 (0.324 corrected). The floors rose by up to 3 points: part of the gain is the
wider letter sets, the rest is the code values and the corrected letters. The measure counts what the key decodes;
it does not credit ff. 143, 150 and 154 with their clear copies.

**Checked here on the images (21 Oct 2026, openapi.bnf.fr IIIF; gallica.bnf.fr/iiif answers 403).**
- Canvas 162 right (f. 155r): a clear page in a secretary's hand, opening *S'estant laissé entendre comme il se
  vouloit départir du Roy de Nav[arre] duquel je sçay qu'il est tres mal contant*; *soubz vostre bon plaisir
  toutesfois que je ne me fusse pas tant advancé* and *Et aussi qu'il n'y avoit plus de hasard* are legible. That is
  the f. 143 cipher, with 49 = *comme*, 33 = *vostre*, 36 = *toutesfois*, 54 = *aussi*.
- Canvas 163: f. 155v ends with the endorsement *Mr du Mayne de ... avril 1586*, then *Comme il estoit bien besoing
  ... Castetz*; f. 156r ends *Mr Forget de ... avril 1586*.
- Canvas 164 right (f. 157r): *En quelle peine nous estions lors pour le payement des deux monstres ...*, *quarante
  mil escus*: the f. 154 cipher. The left page (f. 156v) is blank but for an endorsement.
- Canvas 162 left (f. 154v): two cipher blocks with clear text between and after, signed Forget at Bordeaux.
- Canvas 208 (f. 201): the clear words *Le regard dud. siege il s'advance fort* followed by the code 36 inside the
  cipher block, as #64 reports.
- Not checked here: the names in ff. 196/201 figure by figure, the f. 173 and ff. 123-124 decodes, and Brackx's
  transcription of the copies beyond the lines quoted above.

## Contributions of 22 Oct 2026 (Michael Brackx, issues #73, #77, #78, #79, #83)

Brackx re-transcribed every Cipher-1 leaf from full-size, deskewed line crops (openapi.bnf.fr IIIF) in a new label set
that keeps apart figures Tomokiyo's table separates and our transcriptions had merged, and decoded each with a per-leaf
key (beam search under his own French 5-gram from Montaigne). His figures and keys are in `brackx2026/` (copied from the
issues; his readings are summarised here). Credit in `profile.json` (provenance `mixed`).

| issue | leaves | what it adds |
|---|---|---|
| #73 | fr. 15571 f. 177r (29 lines) and **f. 177v (11 lines, new)** | the Pons–Taillebourg plan (Taillebourg's toll on the Charente, *trente mil escus* from the country) given up when **[84] = le vicomte de Turenne** took the field with guns; matches the archivist's summary on the leaf; 24 = *mais*, 27 = *nostre* |
| #77 | **f. 154v, two blocks of 10 and 11 lines (new)** | the first figure-by-figure test of the key against a contemporary copy (f. 157r); figure splits δ = c / ∂ = s, θ = m / ɟ = s, ꝭ = x, ⊔ = q; 51 = *pas*, 47 = *tous/tout* |
| #78 | the f. 18/19 crib completed: ff. 18r (22 lines), **18v (34), 20r (17)**; ff. 123-124 re-transcribed (36/41/41/38 lines, f. 124r-v completed) | codes **15 = quoy, 73 = oi** (syllable), **78 = le roy de Navarre**, **82 = le gouverneur de Coul[…]**, 84 = le viconte de Turenne, 44 = a stop or null (not *Sire*); code groups split into two figures in the old files (`4 9` = 49, `t 8` = 48, `8 t` = 84); ff. 123-124: Mayenne at Marmande, March 1586, no money, contributions only by garrisons, Turenne back over the Garonne |
| #79 | f. 110 (38 lines, all) | the leaf has 38 cipher lines, not 54 (checked on canvas 116 here); it reads: Mayenne to Villeroy, [Villeneuve-d'Agenais], March 1586, on war without money and his reputation |
| #83 | ff. 143r-v, **150r (32 lines, new)**, 150v, 154r, 173, 196 (31/31), 201 | the repo's `f150_cipher.txt` is the **verso**, f. 150v; f. 150r (canvas 157 right, checked here) was never transcribed; splits θ = m / ϑ = s, ꝺ̄ = u, ɛ = i; codes **46 = rien, 61 = beaucoup**, 34 = *ainsi*; eleven code groups the old files had split into two figures; five misreadings of the copies f. 155r and f. 157r and seven of f. 156r corrected |

**Validated here (22 Oct 2026), `brackx_validate.py` -> `brackx_validate.json`.** His transcriptions and keys, decoded
with this project's beam and period-French 6-gram (`lm.pkl`), not his decoder. Control: each key's letter sets
permuted among its figures, set sizes kept (so the decoder keeps its freedom), 3 seeds.

| leaf | tokens | read as sense (floor) | clear copy, letters matched (floor) | his figure |
|---|---|---|---|---|
| fr. 15571 f. 177r / 177v | 863 / 301 | 0.60 (0.11) / 0.62 (0.18) | none | — |
| f. 154v block A / B | 360 / 350 | 0.61 (0.15) / 0.74 (0.12) | f. 157r: 0.90 (0.37) / 0.94 (0.38) | 95.7 / 96.4% |
| f. 18r / 18v | 722 / 1,163 | 0.50 (0.06) / 0.61 (0.06) | f. 19 (his reading): 0.86 (0.27) / 0.74 (0.23) | 85.9 / 80.8% |
| f. 20r | 575 | 0.60 (0.07) | its copy (end of f. 19v), posted as written in #87 (23 Oct): `texts/f19v_copy.md`; recomputed against it by Brackx (#95): 593 letters matched, 85.7% of copy letters, 86.7% of decoded letters | 86.7% (86.0% against the normalised crib; unchanged within a point against the as-written copy, #95) |
| ff. 123r / 123v / 124r / 124v | 1,113 / 1,374 / 1,405 / 1,183 | 0.47 / 0.56 / 0.61 / 0.68 (0.06-0.11) | none | — |
| f. 110 | 2,164 | 0.61 (0.14) | none | — |
| f. 143r | 704 | 0.70 (0.14) | f. 155r: 0.94 (0.31); with his corrections 0.95 | 94.4% |
| f. 143v | 1,212 | 0.71 (0.08) | f. 155r, the 25 lines it covers: 0.88 (0.31); corrected 0.90 | 88.8% |
| f. 150r | 1,132 | 0.66 (0.06) | f. 155v: 0.84 (0.25) | 87.0% |
| f. 150v | 441 | 0.63 (0.10) | f. 156r as read in #70: 0.83 (0.36); corrected 0.91 | 90.2% |
| f. 154r | 1,056 | 0.63 (0.04) | f. 157r: 0.90 (0.28); corrected 0.91 | 89.8% |
| f. 173 | 1,072 | 0.50 (0.14) | none | — |
| ff. 196 / 201 | 975 / 972 | 0.59 (0.10) / 0.71 (0.07) | each other: 0.78 (0.50-0.52) | 79.5% |

His copy percentages reproduce within 1-5 points with a different decoder and language model; the f. 18v gap (74 against
81%) is the largest. The copy readings marked "corrected" were re-read by him with the cipher beside them, so they are
not independent; the uncorrected readings (#70) give 0.83-0.94 on their own. Every leaf stands far above its control.
Image checks here: canvas 157 right is f. 150 (159 struck), a clear opening then about 32 cipher lines; canvas 116 right
(f. 110) has about 38 lines. Not checked here: his figure labels line by line (no second reader has done so) and his
reading of the copies of f. 19 and f. 19v.

**Taken in:** the transcriptions (`brackx2026/*_cipher.txt`; for measuring they supersede `f110_cipher.txt`, `f123*`,
`f124*`, `cipher_f143.txt`, `f143v_cipher.txt`, `f150_cipher.txt` (= f. 150v), `f154_cipher.txt`, `f173_cipher.txt`,
`f196_cipher.txt`, `f201_cipher.txt` and `f177_cipher.txt`, which are kept), the per-leaf keys, the code values above
and the figure separations. **Not taken:** 64 = *un* and `me` = *mesme* (open, as he says); the f. 20r copy agreement,
which cannot be checked without its copy text. The keys differ from leaf to leaf (θ = m on ff. 143, 150, 154r but m/s on
ff. 173, 196, 201): a merged key for the whole target is still to be made.

## One key, 22 Oct 2026

`merge_keys.py` -> `key_merged_union.json`, `merge_keys.json`. Brackx's eleven per-leaf keys were merged by union: each
figure takes every letter any leaf gives it, each code every value (a word in one leaf beats `+` in another). Decoded
with this project's beam and 6-gram and scored as `brackx_validate.py`, the union key reads **every leaf as well as or
better than its own key**: 9,855 of 15,705 document tokens against 9,609, copy agreement unchanged within a point
(f. 143r 0.93, f. 154r 0.89, f. 154v 0.89/0.93, f. 150r 0.85, f. 150v 0.90 on the corrected copy), scrambled floor 0.121
against 0.100. So the differences between the per-leaf keys (θ = m or m/s, e/ɛ) are differences of hand and reading,
not of key, and the target has one key. Pruning the union (dropping letters a figure took in under 5% of its
occurrences) lowered the score (0.628 -> 0.610; f. 110 0.62 -> 0.57) and was dropped.

Open codes, retried (`code_lm_test.py`, `code_lm_test.json`, and the copies):
- **59 = argent**, adopted: f. 154r "nous prester icy de l'[59] a rendre a Paris" is "de l'argent à rendre à Paris" in the
  copy f. 157r; the other four contexts fit (f. 124r "pour faire [59] pour l'employer", f. 154r "leur [59] leur seroit
  rendu a Paris", f. 173 "recouvrer de l'[59] soubs ses obligations", "qui avoient de l'[59]").
- 44: at a sentence end both times it meets the f. 156r copy (f. 150v); a stop, as Brackx said (already read as nothing).
- 9: "Comme il estoit" in one copy context (f. 150r), "Mais s'il y avoit" in the other: not one word; open.
- 103 (f. 18v): the f. 19 copy itself has an unread word there, before "chevaulx légers"; open.
- me = *mesme* ("a eu mesme advis de Bourdeaux") and 64 = *un* ("avec un peu de forces") fit, no copy covers them; not adopted.
- Ranking candidate words by the 6-gram over 30-letter contexts does not work: the model picks two-letter function
  words everywhere (it would make 59 *es*). Recorded as a failed step.

`final_texts.py` -> `key_cipher1.json` (union + 59), `final_texts.json`, `texts/<doc>.txt` (per line: figures, then the
decode cut into words, upper case inside a sense run, `|...|` outside one, `[nn]` open codes; the clear copy appended
where there is one). Per document 0.51 (f. 123r) to 0.77 (f. 201).

## Verification 3, 23 Oct 2026: ff. 173, 196v, 124v rescored

The v3 sweep (`research/reading_audit/v3_below_b.txt`) flagged ff. 173 (0.535), 196v (0.547) and 124v (0.533) as below
0.60 on the explicit-hole measure. The flag was the scoring, not the readings: `v2_score.py` counts every `[l. n]` line
marker as a hole and scored the English headers with the text, and for f. 124v it scored the whole of
`reading_f124.md`, f. 124r (decoded, not read) included. Cut to the running text (`v3b_body.py`, markers and the stop
code 44 removed):

| leaf | explicit holes | plain | hole rate | stays |
|---|---|---|---|---|
| f. 173 (clear opening + cipher) | 0.72 | 0.68 | 0.085 | read, grade B |
| f. 196v (cipher ll. 1-36) | 0.885 | 0.73 | 0.049 | read, grade B |
| f. 124v (section) | 0.667 | 0.63 | 0.086 | read, grade B (close to the bar) |

What each rests on, plainly: **none of the three has a clear copy, a contemporary decipherment or a printed text.**
Each is the key (`key_cipher1.json`, merged Cipher-1) applied to a figure transcription corrected on full-resolution
images by one reader, with a few letter values added for that leaf only, and the reading chosen by hand from the
figures' letter sets. f. 173: Brackx's figures, 14 labels corrected, leaf values oob = ff, fe = r/rr, zu = u/uu.
f. 196v: figures transcribed here for the first time (1,236), four new labels; 63 = *après* carried by f. 201's clear
tail. f. 124v: Brackx's figures, 65 labels corrected across ff. 124r-v, seven leaf values. No second reader.

Because the key gives many figures two to four letters, the question George's review raises is how much the sets let
a reader make any French he likes. `v3b_matignon_sets.py` aligns each reading with its figures and leaf key and
compares it with two controls on the same figures (the reading's own words shuffled; f. 154's text):

| leaf | letters carried | controls (shuffled / f. 154) | carried letters on a non-first value |
|---|---|---|---|
| f. 173 | 0.962 | 0.470 / 0.476 | 0.131 |
| f. 196v | 0.974 | 0.473 / 0.448 | 0.165 |
| f. 124v | 0.968 | 0.489 / 0.485 | 0.153 |
| f. 143v ll. 26-35 (clear copy fixes it) | 0.843 | 0.464 / 0.440 | 0.122 |

The sets are wide (wrong French still lands on half the letters), but the readings sit far above that, and they use
the second or third value of a set about as often as f. 143v does where the clear copy decides. The readings keep
`read`; the grade drops from A to B on all three because no outside text checks them.

## Read share over cipher words only (16 Nov 2026)

README Conventions now measure the read bar over the words written in cipher only. Each reading was counted section
by section with the v2_score rules (holes by words). Left out of the count: the clear text, which is in italics or in
the files' "clear opening / close / end" sections; f. 201's variant wording in braces in `reading_f196_201.md`; headers
and notes. Line markers (`[l. n]`, `[v. l. n]`, `[f. 201 l. n]`) were not scored as holes. The earlier figures were
taken over each whole file, header, clear text and notes included.

| leaf | recorded | cipher words only | holes / words read | state |
|---|---|---|---|---|
| ff. 196 / 201 (joint reading) | 0.954 | 0.957 | 12 / 267 | stays read |
| f. 196v | 0.963 | 0.952 | 16 / 316 | stays read |
| fr. 15571 f. 177 | 0.946 | 0.956 | 14 / 304 | read in part -> read |
| f. 173 | 0.949 | 0.919 | 26 / 296 | stays read in part |
| f. 123v | 0.942 | 0.935 | 23 / 330 | stays read in part |
| f. 124v | 0.941 | 0.914 | 27 / 287 | stays read in part |
| f. 110 (no clear text) | 0.944 | 0.919 | 46 / 519 | stays read in part |

f. 177 goes up because the old whole-file figure counted its holes twice: once in the reading and again in the list
under "What stays open". It also scored the eleven verso line markers `[v. l. n]` as two holes each. ff. 143r-v,
149v-150v, 154r-v and f. 20r are read from clear copies of the cipher and hold no clear text, so their figures are
unchanged.

Code 47: #77 (22 Oct) reads it *tous/tout* from the clear copy of f. 154v; Remaining gaps list it as open
on f. 110 only, and the page now says so (16 Nov 2026, claims review).

The class stays read in part (ff. 123r and 124r are decoded, not read; f. 173, 123v, 124v and 110 are
under the bar). Remaining gaps are unchanged.

## Remaining gaps

- ff. 123r (0.41) and 124r (0.56) decoded, not read - blocker: no-key-material; three passes each on the images (labels re-cut figure by figure, a per-label atlas of the hand's 5,111 figures with cross-leaf classifiers, code values from other leaves tried): the remaining breaks fall on legible figures of their ordinary shapes, so they are the writer's omissions or slips and codes 16, 60, 66, 67, 101, 102 with no value anywhere; only a clear copy of the Marmande despatch or another letter in this hand using the same codes would settle them (none found on canvases 126-139)
- f. 110: ll. 1-4, 8, 10, 14-16, 24-25, 36 and codes 45, 47 inside a leaf that reads at 0.70 - blocker: no-key-material; three passes; legible figures that no key value consistent with the leaf fits, and codes with no gloss; l. 1 corner illegible
- code groups 16, 19, 23, 45, 47 (f. 110), 60, 67 (f. 124), 65, 99 (f. 196v), 101, 102, 103, 9, and the name code 98 - blocker: no-key-material; one to three contexts each, none in a clear copy (9 is two different words against the copies). Settled 22 Oct 2026: 64 = *quelque*, 62 = *peu*, 73 = *le Roy* on fr. 15571 f. 177 (its clear copy f. 176), 63 = *après* (f. 201's clear tail), `me` a null on f. 177

Not a gap of this target (crib material): the clear copy of f. 20r (end of f. 19v, 13 lines and the endorsement) was posted as written by Brackx in #87 (reply of 23 Oct 2026) and is `texts/f19v_copy.md`, with his English in `texts/reading_f20r_en.md`. f. 20r is now in `outcome.texts` as read in part from that contemporary copy (read_share 0.856 under v10: the in-word bracket expansions count as holes; grade B). His corrections to the normalised text of #87: l. 5 is *q[ue] [?ce] fust honte*, not *car ce fust honte*, which confirms code 14 = *que* there and removes the one wording difference claimed between copy and cipher; l. 1 names four regiments (*[?Sacremore]*, *[?Vic]* and two unread), not two; ll. 6-7 *me voudroient ... je voy q[ue] cela me feroit consommer*; the day in l. 3 is *[?vj]me*, the same numeral as the endorsement (6 January), not *xe*. Still open in the copy: two regiment names; his crib agreement (86.0%) was computed against the normalised crib; recomputed against this as-written text (#95: expansions kept as letters, `&` as *et*, the span *Et celuy des Suisses* … *Roy de Nau[ar]re*) it is 85.7% of copy letters and 86.7% of decoded letters, so the normalisation did not inflate it.

## Escalation

- [x] siblings: ff. 14/15 and 18/19 cribs used to re-derive and verify the key; f. 78v margin decipherment used as a control (`cribem.py`); ff. 196/201 aligned (57% identical figures; Brackx's joint alignment, #64); f. 125r clear letter read for context; canvases 128-139 round ff. 123-124 checked for a copy, none (Brackx, #71). The f. 18/19 crib completed through f. 20r (Brackx, #78). Not yet: ff. 91-92
- [x] clear-pages: **ff. 155-157 are the contemporary clear copies of ff. 143, 149v-150 and 154r-v** (Brackx, #70; checked here). f. 144 is a separate letter; f. 19 is the decipherment of f. 18; f. 125r is a clear letter
- [x] known-keys: Cipher-1 done (Tomokiyo's table, re-derived and verified on every Cipher-1 leaf); the Cipher-3 leaves and their key are matignon1586c3; the Cipher-2 leaves (ff. 218-219, fr. 15573 ff. 120, 385) are mayenne1586c2
- [x] print: BnF catalogue and literature searched 17 Sept 2026, no printed decipherment; Tomokiyo's cryptiana openings for ff. 143, 150, 154, "111" used as checks
- [x] key-rebuild: key re-derived from the ff. 14/15 and 18/19 cribs, confusable figures modelled as letter sets, code values such as 17 *car*, 25 *nous* and 52 *plustost* added from context and the crib; Brackx's letter sets and eleven code values from the clear copies (`key_contrib.json`); his per-leaf keys and codes 15, 34, 46, 51, 61, 73, 78, 82, 84 (`brackx2026/`, 22 Oct), merged here into one key (`key_cipher1.json`, union; pruning tried and dropped); 59 = argent from the f. 157r copy
- [x] retry: every Cipher-1 leaf re-transcribed in full and re-decoded by Brackx (issues #73, #77-#79, #83, 22 Oct 2026) and re-scored here with this project's decoder and a control (`brackx_validate.py`); every open code retried against the copies and by LM ranking (`code_lm_test.py`), 59 recovered

## Assumptions for George's review

- Your 2022 solution of fr. 15572 f. 43, which stood on this entry as a "prior solution" credit, is removed: f. 43 is
  not one of this entry's documents and its cipher was not identified here as Cipher-1. It is credited nowhere until
  its key is shown.
- f. 79r is treated as Cipher-1 (the solved key reads it); the earlier "Cipher-2 crib" values from it stay withdrawn.
- ff. 143r-v, 149v-150 and 154r-v now count as read from an existing decipherment (the clear copies ff. 155-157, outcome.parts), while the key decode of the same leaves stays in the measure. Is that the right split, or should those leaves leave the key-read part altogether?
