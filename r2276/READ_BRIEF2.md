# Reading brief, round 2, for R2276 (BnF fr. 20974 pp. 1-3)

Work dir: guise1556/ (Windows, Bash tool, POSIX syntax, always `export PYTHONUTF8=1`).

## What is now known

The letter is written from **Reims, 19 June [1590]**, in the Nevers-Piles cipher (Jean de Piles, abbé d'Orbais, League
agent, Cardinal Pellevé's man). It reports on the Reims chapter's **election or postulation** of a new archbishop:
"une election ou postulation de deux personnes et deux chanoines, l'ung le grand archidiacre Brulart … l'aultre esleu
… le doien Frison qui est maintenant a Rome … porteurs de l'acte de postulation a Rome"; the abbey of Saint-Remi;
the vidame; a Mr Robilard; "sa Saincteté"; "Mr de Maine" (Mayenne) and his delays; 18,000 lansquenets and 8,000
reiters; one army to go to the Low Countries or hinder the Duke of Parma; the duc d'Elbeuf's ransom of 50,000 écus;
150,000 écus that the town excuses itself from contributing. 16th-c. spelling (i=j, u=v, scauoir, faict, mesmes).

## THE KEY IS STRICT: one value per glyph

Tomokiyo's table (`key_ref_header.png` gives the column letters; `key_ref1.png` = columns a..o, `key_ref2.png` =
columns o..z + nulls; `key_ref3.png` = code signs). Read these images first. Values per label in `key_strict.json`:

a = ꝺ (d), − (-), plain v (v) · b = ƨ (2) · c = W (w), 8 (8) · d = ↄ (7), ʒ (3) · e = curly ꭗ (X), θ (o), ꝝ (z)
f = Ꜩ-like f (F) · g = ꞑ (u) and one form of uq · h = 4 · i = ∞ (Q), k-shape (h), y-shape (9) · l = + (t), crossed ꝏ
m = ⱴ, v with a hook/tail on top (V) · n = closed box ⊏ (R) · o = tt ligature (T), ce/ee (e) · p = small o (0), uq (P)
q = Ɫ (L) · r = open box ⊐ with foot (H), m (m) · s = g with short stroke (g), ≠ with v below (S), ÷ (%)
t = ava (A), long ʃ (J) · u = ɔ (c), φ (f), b (b) · x = a ꝺ with a curl (NOT the a-sigma; give it label `j`)
NULLS: e with a lead-in tail, the cursive x, ẋ (Y).
Codes: 1 = de, n = et, Mr (M), g with long looping swash = que (G), ε-with-loops = qui (E), ℛ = quil (K),
y = luy (y), plain × = les (x), Ɪ = des (D).

So when the machine decode of a sign disagrees with the sense, the likely cause is a **mislabelled glyph**:
v (a) vs ⱴ (m, label V); x (null/les) vs ∞ (i, Q); T (o) vs crossed ꝏ (l, give label `l`); d (a) vs ꝺ-with-curl (x, `j`);
u (g) vs n; H (r) vs R (n); g (s) vs G (que); F vs other; c/f/b (u). Look at the image and relabel.
A sign that really is written against the key (writer's slip) stays, and is read through.

## Files and tools

- `t1.txt`, `t2.txt`, `t3.txt`: transcriptions, "N: tokens". Your job includes correcting them.
- `python tok.py key_strict.json t2.5` shows each token with its strict value (edit tok.py's file list if needed; it loads t1-t3).
- `python wdec.py key_strict.json t2.txt` machine word segmentation (guide only).
- `python check.py t1.txt,t2.txt,t3.txt <reading>` measures agreement: per line, signs read / signs, and each
  disagreement (`X=e`: sign X read as e against the key; `+q`: letter with no sign; `X=null`: sign skipped).
  Always run it with the strict key: `KEY=key_strict.json python check.py t1.txt,t2.txt,t3.txt <reading>`.
- Images: `cd img && python zl.py <page> <line>` -> img/zl.png (1.5x zoom, parts stacked); page 1 also `python z2.py <line>` -> img/z2.png.

## Task

For your assigned lines, produce a reading that is **French sense throughout**, in `tN.L: text` format, into your
reading file. Rules:
1. Never write key-value letter strings that are not words. If a stretch does not make sense, look at the image and
   fix the labels; if it still does not, write `?` for each unread word. An honest `?` is better than a fake word.
2. Every correction to the transcription is made in the t-file (only your lines).
3. Target: every line reads as sense with >= 95% of its signs agreeing with the strict key after relabelling.
4. Words run across line ends; the text is continuous from p.1 l.1 to p.3 l.13.
At the end report: per-line check.py counts, number of relabels, the lines or words still `?`, and any glyph that
you think genuinely has a value outside the table (with 3+ occurrences as evidence).

## Addendum (key v3)

Reading the letter showed that its key has more signs than Tomokiyo's partial table. `key_v3.json` holds the value
sets estimated from the readings so far (EM over the word decoder). Extra values found: ʒ + Ձ (labels `3 Z`) =
"cardinal"; ꝺ with superscript t (`s`) = "il" or i; n = et or x; ⱴ (`V`) and Ɫ (`L`) sometimes "ie"; hooked b (`b`)
= a or u; d = a (sometimes t, p); H = n (more often than r); g = s or i; G = s or que; Y (ẋ) = i.
`wd_v3.txt` is the machine word decode with key_v3 (a guide: good in long stretches, wrong in many words).
Measure with `KEY=key_v3.json python check.py t1.txt,t2.txt,t3.txt <reading>`.

## Addendum 2 (key v4)

From page 3: the ce/ee ligature (`e`) is also the code for **"pour"** (and o); ʒ (`3`) is also **"du"** (and d; with Z,
"car-dinal"); Z also r; F also u (uille, pouoir); x also e. `key_v4.json` has these. Page 3 reading: read3_r2.txt.
Measure with `KEY=key_v4.json python check.py t1.txt,t2.txt,t3.txt <reading>`.

## Addendum 3 (key v5, two-sign codes)

`decode.py` now merges two-sign codes into one token: `b b` -> `bb` = **leur**; `3 Z` -> `3Z` = **cardinal**. ʒ (`3`)
alone is d, du or **le**; the ce-ligature (`C` or `e`) is **pour**; Ƨ (`D`) is des or t. `key_v5.json` has these.
Measure with `KEY=key_v5.json python check.py t1.txt,t2.txt,t3.txt <reading>`. Current readings: read1_r2.txt (p. 1,
82.8%, 76 `?` words), read3_r2.txt (p. 3, ~84%), read2.txt / read2_r3.txt (p. 2).
Page 1 right ends of lines 1-4 and 16-31 are torn away (physically lost: mark [...], not `?`).

## Addendum 4 (key v7, the '?' round)

Current whole-letter reading: `reading.txt` (93 lines). Measure with `KEY=key_v7.json python measure.py reading.txt`
(strict = sign agrees with key; sense = sign aligned to a letter of a real word or a declared null). Now: strict 88.3%,
sense 91.2%, 119 `?` words. key_v7 adds: page-1 dotted M relabelled `Ml` = lettre; `_` (e with lead-in tail) = null;
`^` = s. Tools: `seg.py "<signs>"` best dictionary splits of a sign string; `cand.py` one/two-word candidates;
`al.py`, `al2.py` alignment views; `dv.py` line decode; `img/zx.py <page> <line> x0 x1 [scale]` zoom crops.
Rule for this round: a '?' word may be read when (a) the word is required by the sentence and (b) at least half of its
signs agree with the key and the rest are visible look-alike glyphs (writer's slip or transcription doubt). Mark such
words with a trailing `*` in the reading (e.g. `pratiques*`) so they can be graded C. Never invent words to fill a tear.
