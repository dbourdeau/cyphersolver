# Heidelberg, Cod. Pal. germ. 597 — "Alchymey teuczsch" (East Bavaria, 1426)

Status: found already read. Written up 18 Sept 2026: https://dbourdeau.github.io/cyphersolver/heidelberg597.html

## Outcome
The ciphers in this book were broken and described by Wilhelm Wattenbach in 1869, with facsimiles
and plaintexts of f. 1r, f. 5v and f. 6v (*Anzeiger für Kunde der deutschen Vorzeit* NF 16,
cols. 264–268). Gerhard Eis printed extracts (1957; *Medizinische Fachprosa*, 1982, pp. 307–315).
The 2014 Heidelberg catalogue (Kalning, Miller, Zimmermann, *Cod. Pal. germ. 496–670*, pp. 257–260)
says its quotations from the cipher passages are given resolved, and it reads f. 93r. DECODE R2876
"Non-decrypted" is stale. Not a candidate for the oldest-unread-solve record (`research/oldest/CANDIDATES.md` A4).

Wattenbach: "es ist nun nicht schwer, den Anfang zu errathen … wie alle einfache Chiffren, leicht zu
enträthseln."

Correction to the memo: "ff. 70–71" came from the Handschriftencensus citation of Bischoff 1954,
"S. 12 (Nr. 70–71)". Those are Bischoff's item numbers, not folios. ff. 61v–82v are blank.

What this project added: the two struck alphabets recovered from the images and checked against the
printed plaintexts; a third sign set identified and partly fixed from the catalogue's crib; a survey
of every cipher run in the book; the correction above.

Three alphabets, three results (one-key review, 14 Oct 2026): the profile gives the outcome per sign alphabet in
`outcome.parts` and README has one row per part, as soria1523 does. Key A (f. 1r, the recipe names): read from
Wattenbach's decipherment, partial (the recipe cipher is not transcribed). Key B (ff. 6v, 91v): read from
Wattenbach's decipherment, complete. Set C (ff. 1r ll. 1-2, 5v-6r, 44v, 93r): key recovered from the 2014
catalogue's reading of f. 93r (external plaintext), partial; f. 44v and the f. 6r glossary unread. Wattenbach is
credited for keys A and B and f. 1r l. 1, the catalogue (Kalning et al.) for set C only.

## The book
Free images: https://digi.ub.uni-heidelberg.de/diglit/cpg597 (Public Domain Mark). Only the 85
written leaves are imaged. The IIIF manifest `/diglit/iiif/cpg597/manifest.json` fetches with a
browser User-Agent; `/diglit/cpg597/...` pages are behind the Anubis bot wall. Local copies
(git-ignored): `img/`, catalogue pp. 256–261 `cat_*.jpg`, Bischoff 1954 `bischoff1954.pdf`,
Wattenbach's pages `watt_015*.jpg`, OCR `wattenbach_ocr.txt`.

Contents (catalogue): cisioianus 2r–v; alchemical and medical recipes 5v–47r, 54r–58v, most headed
Niklas Jankowitz; unlucky days (Michael von Pirpach) 47v–48r; charms (Michel Wulfing) 48r–49v;
astrological text 83r–84v (struck); calendar 86r–v; address to Bishop Leonhard of Passau 91r;
notes 93r–94v, among them the gold-multiplication weighing of Easter week [14]23. Wrapper: an
unexecuted 1413 Leuchtenberg charter for the Jew Salman Teublin. Dated 1426 on f. 9r:
*Das puch ist angehaben ym [tauro] xiiii und xxvj*.

## Where the cipher is (survey of all 85 leaves, three agents, 18 Sept 2026)
- f. 1r: four struck lines, the first sign alphabet (key A).
- ff. 5v–6r: preface and glossary of cover-names, in a third set (set C) mixed with key A.
- f. 6v: three lines, the invocation, in key B.
- f. 7r: ruled box of four sign lines; ff. 7r–22r, 46r–v, 54r–61r: substance names and quantities
  inline in the German recipes (key A with admixtures). Densest on 20v–22r and 57r–58r.
- f. 9r: after the invocation in clear, lines 7–12 largely in cipher (*Nu nym des …*).
- f. 44v: two notes almost wholly in cipher (set C variant). f. 93r: two lines, set C.
- f. 79ar: struck table of sign groups over pairs of signs. f. 91v: struck line, key B in abc order.
Per-line boxes and glyph counts are in the session log; enlarged strips in `crops/` (git-ignored).

## Key A — f. 1r (the compiler's "new abc")
Wattenbach's reading of f. 1r: *Das ist ein abc vnd das haben wir selbs neus gemacht /
abcdefghiklmnopqrſstuwschch vnd ich / hab es darum gar an ein ander gesetzt das man /
nicht sul versten das es ein alfabet sei.* The alphabet is one unbroken run of 24 signs, heavily
struck. Read after removing the strike line (`seg2.py`, `crops/1r_abc_*.png`):

| a | b | c | d | e | f | g | h | i | k | l | m |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ▪ | o | 2 | ∴ | ⊡ | 8 | Y | ˥ | : | ɓ | 4 | ꝝ |

| n | o | p | q | r | ſ | s | t | u | w | sch | ch |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ϙ | 88 | ꝗ | ꝁ | × | F | ● | ◒ | • | T | ⊙ | ♣ |

Grades: a–l high (clear on the image and checked). m–ch lower: the strike is heaviest there and
several of those signs are read from their shape, not checked in running text.
Checks:
- f. 1r line 2 continues after the clear *vnd ich* with ˥ ▪ o ⊡ ● = **hab es** (h a b e s).
- The recipe heading on f. 11r line 4 (and 10v heading): ϙ : ɓ 4 ▪ ● | Y ▪ ϙ ɓ ⊚ : 2 =
  **niklas gank?icz**, one sign unread (⊚, o or w). A modern pencil gloss on 11r reads
  "= Niklas Gankwiz". The clear headings elsewhere spell him Niklas Janowitz / Jankowitz.

## Key B — f. 6v and f. 91v (stroke and figure signs)
Aligned glyph by glyph (`seg.py`, `crops/6v_*`) against Wattenbach's plaintext of f. 6v:
*In dem namen des faters vnd des suns vnd des heiligen geistes so fach ich schuldiger man dises buch an.*

| sign | letter | sign | letter |
|---|---|---|---|
| : | i | ⊙ ring with dot | h |
| Y hooked top | n | T | l |
| 3 | d | ꝑ-like with dot | g |
| trefoil on stem | e | two loops on stem | t |
| Ω with inner triangle | m | ring with 3-tail | sch |
| ● blob, no stem | s (final) | 8 with inner loop | b |
| tall stroke | s (medial) | c with 2 | ch |
| short stroke | a | 9 | o |
| ring with tail | f | T with wavy top | r |
| cup + 3 | u (in *vnd*) | | |

f. 91v is the same set written in abc order and struck; its first signs agree with a, d, e, g, h, i, l.

## Set C — f. 1r lines 1–2, ff. 5v–6r, 44v, 93r
This is Wattenbach's second system on f. 1r: lines 1–2 are in set C, lines 3–4 (the alphabet) in key A.
- f. 93r, catalogue's reading *Nota wir haben versucht das [in dem caichen] der [iuncfrawn]*:
  ✱ i, T n, ∴ d, ⊡ (one dot) e, filled box m, 2 c, ▪ a, ⊏ h.
- f. 1r line 1 (`crops/1r_line1_setC.png`), Wattenbach's *Das ist ein abc*: Das [✱ 中 ⊡̈] [⊡ ✱ T]
  [▪ o 2]. Independently confirms i, n, e and the shared a b c, and gives s = 中 (box on a stem),
  t = ⊡̈ (box with two dots). Grade C for s and t (one word each).
It shares a, b, c, d, e with key A and differs for i, n (T is w in key A). The f. 6r glossary uses
these signs and a few dotted-box variants not yet assigned; it has not been read.

## Open
- A continuous transcription of the recipe cipher (ff. 7r–22r, 46r–v, 54r–61r), f. 9r lines 7–12,
  the f. 6r glossary and f. 44v has never been printed. Keys A and C need their doubtful signs
  settled on running text first. Philological value only; no bearing on the record hunt.
- Key A positions m–ch are graded lower until checked on running text.

## Tools
`lines.py <fol> x0 x1 y0 y1 [scale]` — ink-profile line detection, enlarged strips.
`seg.py <fol> x0 y0 x1 y1 out.png` — connected-component glyph boxes, numbered.
`seg2.py <fol> x0 y0 x1 y1 out.png` — same after removing long horizontal strike lines.
