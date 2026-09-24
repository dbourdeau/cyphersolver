# Charles III of Lorraine to the comte de Vaudémont, Nancy, 18 June 1592 (BnF fr. 3621 no. 97)

**Status: read in part — 71.5% of cipher tokens read as sense, measured (22 Sept 2026).** The
system is broken: a reciprocal letter-pair substitution (a/i b/p c/f d/q e/t g/u l/y m/z n/s o/r h/x),
dots for doubled letters, a null, a few special signs and syllable/word figures (31 = ma, 139 = vous,
145 = me). 790 of 1,105 cipher tokens read (`python measure_reread.py`); the 18 Sept key and
transcription gave the same words for 40.6%. Open: most special signs, 11 of 14 figures, four garbled
runs. See §9 (the re-read), `## Remaining gaps`, `## Escalation`. The 18 Sept head read "SOLVED"; that
overstated it — the key was a 44-symbol fit that hid the pair system, and the reading was an estimate.
Catalogue item 15. Reading of record: `ct/no97_reading2.md` and `ct/no97_reread.txt`; the 18 Sept
account (`ct/no97_reading.md`, `ct/no97_solution.txt`) is kept for the record.

The document was catalogued as unsolved: **DECODE record 9449** is this exact piece and gives its
status as `Non-decrypted` (<https://de-crypt.org/decrypt-web/RecordsView/9449>). No key for it has
ever been published. **But it was not unread** (found 24 Sept 2026, see §4a): Tomokiyo's cryptiana
`unsolved.htm` already marked it "Solved" before this project began, reporting that he broke it in 2025.

## 1. The verification step, answered

The catalogue set this task first: *"Look for the ciphered originals of the January intercepts in
fr. 3621."* They are not there. **No. 22 (fol. 31) is a plaintext decipherment only** — a fair copy of the
French of three intercepted Vaudémont letters, with no cipher anywhere on the sheet, headed "Dechiffrement
des lettres de Monsieur de Vaudemont à Monsieur de Lorraine [son] pere, interceptées et apportées à
Monsieur de Dinteville, le XX[e] Janvier 1592". Nothing else in the volume is described as intercepted;
"intercept" occurs once in the whole BnF notice, in that entry. So the hoped-for crib — decipherment
against its own ciphertext — does not exist in this volume, and the catalogue's own scoring note ("if
no. 22's decipherment corresponds to a cipher copy elsewhere in the volume the key falls; otherwise a
single copy") resolves to the second branch.

## 2. What the documents are

Gallica `btv1b52524472n`, 286 canvases, single pages about 4266 × 5883 — good images, not microfilm.
**Canvas = 2 × folio + 9**, fixed on fol. 30 (canvas 69, the Nevers letter of 14 January that the notice
assigns to no. 21). In this notice the folio printed *before* a piece number belongs to that piece.

| piece | leaf | canvas | content |
|---|---|---|---|
| 22 | fol. 31 | 71 | decipherment of three intercepted Vaudémont letters, plaintext only |
| **97** | **fol. 109** | **227** | **"Coppie d'une lettre … de Charles de Lorraine à monsieur de Vaudemont", Nancy, 18 June 1592, with cipher** |

The volume is Nevers's own intercept and correspondence file for 1591–92, and it holds several letters
"avec chiffre et déchiffrement" from his own correspondents — Lodovico Birago (nos. 31, 35), Nicolas
Potier de Blancmesnil (no. 79), Dinteville (no. 114). Those are the Nevers side's own keys, not this one.

## 3. The cipher of no. 97

Twenty-one written lines, with clear French and cipher **alternating inline on the same lines** — not a
wholly ciphered despatch. Lines 9 and 20 are entirely clear, line 21 is cipher then clear, and the whole
postscript after the signature is clear. The baselines slope; the shear that sharpens the histogram of
glyph y-centres is **−0.031**, and deskewing at that value resolves the block into 21 bands at about
87 px spacing.

The system is an alphabet of **ordinary cursive letterforms** — plain minuscules, the same letters
carrying a crossbar, an overbar or dots, and a few special signs (a lambda, a dotted circle, an alpha, a
crossed E) — together with **figures for names and words**: 13, 31, 57, 88, 98, 103, 121, 122, 123, 137,
139, 141, 145, 146, of which 139 occurs ten times and 145 seven. The letter frequencies match French rank
for rank through fourteen places, the commonest symbol standing at 14.4%, and the coincidence statistics
put the cipher between a monoalphabetic and a fully homophonic system: a letter substitution with modest
homophony, plus the nomenclator.

The flanking clear text is the same business as the cipher: munitions promised and undelivered, the
inhabitants of Chaumont, the sieur de Buzonville, and the attempt on **Chasteauvillain**. Transcriptions
in `ct/clear_texts.md`; the cipher transcription in `ct/no97_eye.txt`.

## 4. The key is not published, and is not in fr. 3995

Confirmed against the DECODE database, Tomokiyo's Cryptiana, the HistoCrypt proceedings, the BnF
notices and the printed editions. DECODE holds 8 records for fr. 3621; only nos. 97 and 116 are
`Non-decrypted`. Record **9444** is no. 22, marked `Decrypted`, 2 pages — which is the catalogue
entry for the plaintext decipherment described in §1, and confirms that finding independently.
No key record anywhere in DECODE is attributed to Charles III de Lorraine or to Vaudémont.

Keys for *other* Lorraine ciphers are published and are **not** this system: Bréval to Henri II,
ca. 1620 (Tomokiyo, `lorraine.htm`; DECODE 7952), and Bassompierre to Charles III, 1 Aug 1593
(Tomokiyo, `nevers.htm`, BnF fr. 4715 no. 15). Desenclos and Lasry's HistoCrypt 2024 paper publishes
the Henri IV–Nevers digit ciphers of fr. 3995 fols. 141 and 67; fr. 3621 is never mentioned. Lepage's
1864 edition of Charles III's League correspondence stops in 1591 and prints no cipher table.

## 4a. A prior reading existed: Tomokiyo, 2025 (found 24 Sept 2026, after this reading)

The §4 search looked for a published *key* and found none, which still holds. It missed a published
*claim of reading*. Tomokiyo's *Unsolved Historical Ciphers* (`cryptiana.web.fc2.com/code/unsolved.htm`)
has an entry "Duke of Lorraine (1592)", marked **Solved**, citing BnF fr. 3621 "f.125" (DECODE R9449),
Charles II/III to Vaudémont, 18 June 1592: *"I solved this in 2025: 'J'ay este infiniment mal satisfait du
peu d'execution ....'"*, adding that the alphabet uses letters and other symbols, that historians' help is
needed for the numerical symbols, and that many low-frequency symbols seem to be nulls. The entry is
already in the 6 Sept 2026 snapshot saved in this repo (`napoleon/unsolved.htm`), so it predates the
18 Sept attempt. He published only that opening, no key and no text.

What this changes: the contamination answer (profile `conditions.prior_solution`: exists online, found
after reading, not used), and any claim that this was a first reading. What it does not change: the key
was recovered here ciphertext-only without it, and our reading opens with the same words he quotes
(`ct/no97_reading2.md` L00: "j'ay esté infiniment mal satisfait du peu d'execution"), an independent
confirmation of the first line. His "f.125" does not match the stamped f. 109 used here; the DECODE
number, parties and date make it the same piece.

Four 1592 key sheets in fr. 3995 whose DECODE profile matched this cipher were fetched and examined.
All four are eliminated on documentary grounds:

* **fol. 32** — a jargon dictionary of covert equivalents (*Nouvelles* = "Draps de soye"), geometric
  signs and figures 2–40, not a letter cipher.
* **fol. 83–84** — an all-digit cipher with a *Nulles* row (24 33 52 61 70 80 96); "Duc de Lorraine"
  appears in it as nomenclator entry 46, so it is somebody else's key that mentions Lorraine.
* **fol. 98** — endorsed in its own hand "1592 / Chifre d'entre le Duc de Parme et le Roy Cath[olique]
  en l'an 1592 / lequel sert aussi p[our] le Duc de Sessa et don Diego de Ybarra".
* **fol. 103** — a Nevers-circle nomenclator, its flap listing Gondi, Nemours, Guise and Montpensier.
  It gives **three homophones for every letter**, which is incompatible with this cipher's single
  symbol at 14.4%. Its own structure is worth recording: a 22-letter alphabet in three rows, syllable
  figures 1–72 (ba be bi bo bu, ca ce ci co cu …), double-letter figures 73–98 (cc dd ff mm nn pp …),
  word figures 99–353, and overbarred province and city lists in which Lorraine is 30 and Metz 68.

So the cipher had to be broken cold, from the one copy.

## 5. Breaking it

**The glyphs are ordinary cursive letterforms.** That is the fact the earlier attempt missed. They are
not the geometric signs of the Nevers keys; they can be read straight off the page, so the unsupervised
shape clustering that had been failing is unnecessary. Per-line crops at about 1.5× native — 21 lines,
each in two halves, in `lc/` — are legible enough to transcribe by eye.

The transcription is `ct/no97_eye.txt`: 1,109 tokens, **1,071 letter symbols in 44 distinct forms and
38 nomenclator figures**. Three long internal repeats confirm it is self-consistent, including a
twelve-symbol group recurring on lines 15 and 19.

The search had to be rebuilt. The random-move annealer used earlier cannot solve a cipher of this size
at all: on a **control with a known key**, same symbol count and same segmentation, it recovered only
37–56% of letters at −2.64 per character while the true key scored −1.62. The optimum was therefore
well separated by score and the failure was in the search. Replacing the random move with a
steepest-ascent sweep over every symbol, run to convergence and then kicked out of the local optimum,
recovers known keys at **98.7–99.6%** in about fifteen seconds (`search.py`).

Two further traps had to be closed. Allowing nulls freely lets the search delete every hard position
and map the rest onto e/t/n/r/s, scoring −1.70 — better than French — which is an artefact of
normalising per surviving character. And selecting on the unpenalised score picks a degenerate key
that reads "etenete…". Nulls are capped and degenerate keys rejected by an explicit test on the
induced letter frequency.

With that, the cipher breaks. Key, evidence and reading: **`ct/no97_reading.md`**.

## 5b. Tested against nulls

The search maximises a French 4-gram score over 44 free parameters on ~1050 characters, so it
could in principle manufacture French from nothing; and words picked out by eye prove little
when the chooser knows the subject. Run unchanged on nulls with no plaintext — same symbols,
same frequencies, same segment lengths, order shuffled — and scored blind on dictionary
coverage and distinct French words of six letters or more:

| | 4-gram | coverage | distinct 6+ letter words |
|---|---|---|---|
| **manuscript** | **−2.10** | **83.0%** | **33** |
| null mean of 5 | −2.73 | 74.6% | 1.2 (range 0–3) |

Thirty-three against nought to three. There is real French under this transcription and the key
exposes a substantial part of it. Coverage barely separates the two and is a weak statistic
here. Full output in `ct/control_null.txt`, script `nulltest.py`.

One correction the blind list forces: it returns *uilains*, i.e. *vilains* under u/v folding,
immediately after *chasteau* and sharing its final u. The decode gives **chasteauilains** where
the name wants **chasteauuilains** — one symbol short. A transcription slip, not a key fault,
but it means the crib is eight letters secure and six more probable, not fifteen proved.

## 6. How good the reading is, measured

The solution scores −2.10 per character, against −1.93 for real 16th-century French, −1.63 for the
true key of a clean control, and −2.15 to −2.23 for controls in which six to twelve pairs of distinct
glyphs have been transcribed as the same form (`ct/control_merge.txt`). At that level the controls
recover 65–75% of letters, which is what the decode looks like. Random transcription noise was also
calibrated (`ct/control_noise.txt`) and does not explain it; the error is systematic, as by-eye
reading of barred and dotted variants would be.

So: the cryptanalysis is finished and the key is stable across independent runs and under a locked
crib. **What limits the reading now is the transcription.** Re-reading the 42 crops in `lc/` with the
key in hand, correcting the barred, dotted and capital variants, would read the letter through.

## 7. What the letters say, from the clear text

In `ct/clear_texts.md`. The June letter's clear portions have the Duke urging his son to press the attempt
on **Chasteauvillain**, complaining of munitions promised and undelivered, and naming Chaumont and
Buzonville. No. 22's decipherment carries the January business: the Spanish army's march on Rouen, the duc
de Mayenne finding the Spaniards resolved on a battle, Parma's judgement, the cavalry; and then the
political matter — the papal legate, the Spanish pretensions, Villeroy at Pontoise, the house of Bourbon,
Bellievre, and the peace which nobody could support the war's length without. That is the double game the
catalogue points at: the Duke of Lorraine's son inside the League army reporting home on Parma and on
feelers toward Henri IV, and the King's side reading his letters.

## 8. Files

`fetch.sh`, `zoom.sh`, `zoom71.sh` (page and region fetches), `fetch3995.sh` (the Nevers key book),
`deskew.py` (shear deskew and line segmentation — the reusable piece), `lines.py`, `stitch.py`, `pipe.py`
(earlier, superseded line finders kept for the record), `cluster.py`, `cluster2.py` (shape clustering),
`solve.py` (the earlier homophonic solver, superseded), `buildlm.py` (the French n-gram model),
`solve97.py`, `solve97b.py` (scoring, nulls, merge variants), `search.py` (the iterated local search
that works), `run97b.py`, `final97.py` (the solve), `polish97.py` (word-level refinement),
`control.py`, `control2.py`, `control3.py`, `control4.py`, `stats.py` (the calibrations),
`lc/` (42 per-line crops), `key3995/` (crops of the fr. 3995 candidate keys),
`ct/no97_eye.txt` (the transcription), `ct/no97_reading.md` (the result), `ct/no97_solution.txt`,
`ct/control_*.txt`, `ct/clear_texts.md`, `src/` (manifests, notices, corpus and models).

Checked: the folio-to-canvas mapping on a foliated leaf; that no. 22 carries no cipher; the piece list
against the notice; the absence of fr. 3621 from Tomokiyo's League survey and from the Desenclos–Lasry
HistoCrypt 2024 paper; DECODE records 9444 and 9449 field by field; seven candidate key sheets in
fr. 3995, including all four whose DECODE profile matched; the deskew and line segmentation; the search
against controls with known keys, against random transcription noise and against systematic glyph
merging; the recovered key against the page's own clear text, which writes Chasteauvillain twice.
Not checked: the remaining key sheets in fr. 3995 one by one; the Archives départementales de
Meurthe-et-Moselle, where a duplicate or a key would most plausibly survive; the values of the fourteen
nomenclator figures, which no surviving key supplies. User must verify: the DECODE query results through
the site's own interface; the identification of DECODE's "Charles II, Duke of Lorraine" with Charles III;
and every transcription here, clear and ciphered, as my reading of a secretary hand — about a quarter of
the cipher glyph identifications are still wrong, which is why the reading is partial.

## 9. The re-read with the key in hand (22 Sept 2026)

Done as §6 proposed, from the native IIIF image of canvas f227 (4046 × 5762), sheared −0.031 and cut into
21 line bands, each viewed in five crops at 2.3× (`img/g/`, git-ignored; `img/mkcrops.py` makes the
sheared page). Full account in `ct/no97_reading2.md`.

* **The key is a reciprocal pair cipher**, not 44 free symbols. The 18 Sept values already paired
  (a↔i, o↔r, d↔q, n↔s); read as pairs the whole alphabet falls into eleven: a/i b/p c/f d/q e/t g/u
  l/y m/z n/s o/r h/x. Two dots under a letter double it (ṇ = ss, c̤ = ff, c̈ = tt); the looped æ is a
  null word-divider; Θ = s.
* **Two transcription merges** caused most of the 18 Sept errors: `c` was both the secretary e (→ t)
  and c (→ f), so every f was lost; `B` was both b (→ p) and the looped secretary h (→ x).
* **Figures**: 31 = *ma* (*com-31-nder*, *de-31-nde*, *31 resolution*), 139 = *vous* (*chemins, 139
  tiendrés*), 145 = *me* (*affin que 141 ne 145 delaissent*) — so at least part of the nomenclator is
  syllabic. Graded C.
* **Measured** (`measure_reread.py`; rule in its docstring: a token is read if its word is graded H/C):
  790/1,105 = **0.715** (letter signs 0.721; figures 21/38). Before: the 18 Sept key and tokens give the
  same words for 449/1,105 = 0.406. Four emendations, listed by the script.
* The *chasteauilains* slip of §5b is confirmed twice (L14, L18): the scribe omitted the *v* both times.
* Siblings: the fr. 3621 notice lists no other Lorraine or Vaudémont piece in cipher (the ciphered
  pieces are Birago nos. 31/36, Potier no. 79, Dinteville nos. 114/116 — Nevers's own correspondents).

## Remaining gaps

- Special signs λ, m̄, U, E, π, γ, ꝗ, low-barred t, figure-4 (about 60 tokens, and the words they sit in) - blocker: open-codes; no key survives and each sign occurs 1-11 times, too few for context to fix most of them.
- Figures 57, 98, 141, 122, 123, 13, 137, 88, 146, 121, 103 (17 tokens) - blocker: open-codes; one letter, no key, no sibling in the same cipher.
- Garbled runs L12 (after *passer*), L13 (*des … apres*), L18 (*pour … Chasteauvilain*), L20 (*m'a d…te*) (about 45 tokens) - blocker: illegible; at IIIF 1:1 the glyph sequence does not decode under the pair key; needs the original or a higher-resolution scan to tell e/c, b/h and dotted forms apart.

## Escalation

- [x] siblings: fr. 3621 notice read for other Lorraine/Vaudémont cipher pieces — none; no. 22 is plaintext only (§1).
- [x] clear-pages: the clear text of no. 97 and the postscript transcribed (`ct/clear_texts.md`) and used as context; no decipherment on the page.
- [x] known-keys: fr. 3995 ff. 32, 83-84, 98, 103 eliminated (§4); Tomokiyo's Lorraine keys (Bréval c. 1620, Bassompierre 1593) are other systems.
- [x] print: Lepage 1864 stops in 1591; no print of this letter found (§4).
- [x] key-rebuild: 18 Sept search key re-derived as the eleven-pair reciprocal key with doubling dots and a null (§9).
- [x] retry: every line re-read from the page with the key in hand (§9, `ct/no97_reread.txt`); the Archives de Meurthe-et-Moselle (possible duplicate or key) not consulted — needs physical access or their catalogue.
