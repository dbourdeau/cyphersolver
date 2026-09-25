# TNA SP 106/10 ff. 241-243 — undeciphered letter in the "masonic alphabet" (DECODE R927)

Lasry review (25 Sept 2026): the letter was decoded by Sheila Richards in *Secret Writings* (1973). The book was not seen here and a web search found no record of it; it was not used. This reading is an independent re-solution (outcome.first_break = false), left out of the ciphertext-only list for Klaus Schmeh.

Outcome: read in part (2026-09-19). Cipher broken: French, homophonic pigpen. Last page (f.243) read almost in full; first page (f.241) read in fragments.

## Source

- DECODE record 927, `TNA_SP106/10_UND_(0241-0243)`, 3 images (auth-only; fetched with the bordeaux cookie):
  `IMG_R927_I4921_P1.png`, `I4922_P2.png`, `I4923_P3.png` (kept in `img/`, git-ignored).
- DECODE: "Undeciphered letter in the masonic alphabet, say 800 codegroups in sum total." No sender, recipient, date.
- Web search (Sept 2026): no published decipherment found.

## What the pages show

- Pigpen-type glyphs (the nine tic-tac-toe cell shapes), each followed by 1-3 dots (occasionally 0 or 4).
  Some glyphs carry an inner stroke or inner dot; a few are stacked composites (e.g. ⊔ over ⌟); two special
  "9/6"-like signs; "=" marks at line ends (word carried over).
- Writer's frame: turn the images 90° counter-clockwise (the "67" on p.1 is then upright). Text then runs in
  horizontal rows, dots above the glyphs. In the archive's image orientation the rows appear as vertical columns.
- P.2 carries a paper flap with a **pencil key** (later hand, probably a reader's attempt):
  `akt | blu | cmw / dnx | eoy | fpz / gq | hr | is` — i.e. the 1-2-3-dot pigpen (a-i one dot, k-s two, t-z three).

## Tests so far (p.3, ~470 glyphs, automatic segmentation + hand checks of cols 0-11)

- The flap key applied literally gives nonsense ("oeaeydakdorsefekdoi..."). Under it g/q would be ~16% of text, t ~0,
  k ~9%: the key is not right as written.
- All 8 rotations/reflections of the grid × all dot-order permutations × both reading directions × dot-shift ±1,2:
  best quadgram score -6.3/char (real text ≈ -4.0). Languages: en, fr, de, nl, es, it, la.
- Cell-constrained solve (letter free within the key cell), any orientation: no language fits.
- All 9! shape→cell assignments (dots = position): no fit.
- Free homophonic hill-climb over (shape, dot-count) symbols, IoC of that stream 1.64 (×26, i.e. language-like):
  en/fr/de/nl/it/es/la/sv/da/pt/cy/pl/hu all -4.5..-5.0 with no readable text; column, row, reversed and
  boustrophedon orders tried. Synthetic English with 10% symbol noise still reaches -4.6 and reads in part,
  so either transcription error is much higher than 10% or the symbol set is wrong (inner-mark variants,
  composites and the special signs not yet separated).

## Next

Full hand transcription with inner-mark variants and composites as separate symbols (p.3 cols 0-11 partly done
in this session's notes below), then pp.1-2; rerun the free solver.

### Hand transcription p.3 (archive orientation, columns right→left, top→bottom; `*` = inner mark; `@` = 9/6 sign)

    c0: E2 E1 A1 E1 E3 D1 A1 A2 D*1 E2 H*2 I2 E*1 F1 E1 A2 D1 E*2 I1
    c1: A2 A1 E1 A1 A1 A2 G2 E*3 F3 A2 I*2 H2 E1 A1 H2 E2 H1 F2 E*1
    c2: B1 G2 B1 A1 D2 [blot] B1 E*3 E*2 I1 E2 H*2 C2 A2 E*1 I1 A2 A1 D*2 E2
    c3: B1 B*2 E1 I1 E*1 F1 E1 B2 E1 A1 D2 E2 F*3 F2 D1 G1 G1 E1
    c4: F3 E1 C2 A2 E1 F*2 H2 B1 F*3 A2 B*1 I1 E1 I2 A*1 E2 E1 I1 E1 G1 E1 A1 D2
    c5: @ A? I1 E1 F2 B1 E3 B1 I2 D2 I1 E0 @ G1 D1 A1 G1 B1 E2 D1 ?
    c6: [blot] A2 H2 B1 A2 E*2 E1 H2 F*1 I2 E1 A2 C2 A2 E*1 F3 C1 A2

### Session 1 close (2026-09-19)

- Auto labels (`v3_glyphs2.json`, from `segv.py` + `segv2.py`) checked against hand reading for cols 0-6:
  133 glyphs, 16 shape errors, 20 dot errors (~25% symbol error). Cols 7-23 eyeballed in montages: same error profile,
  plus inner-stroke variants (◻ with inner bar, ⊓ with inner stroke) that the classifier merges with plain shapes.
- The free solver fails at this noise level. Next step: finish the hand transcription (cols 7-23, then pp.1-2),
  keep inner-mark variants as separate symbols, then rerun `hc3.py` (en, la, fr first).
- Tools here: `seg2.py`/`segv.py` (glyphs), `segv2.py` (dots → nearest glyph), `hc2.py`/`hc3.py` (homophonic
  annealing with quadgrams `q_<lang>.json`, built by `mkq.py`), `cons.py`/`cellperm.py` (key-constrained tests).

## Broken (session 1, later)

Full hand transcription of p.3 in `hand_p3.txt` (450 signs). With it the free solver lands on **French**
(quadgram -4.39 vs -4.8/-5 elsewhere); anchors then fixed by hand ("monsieur", "de vostre", "vous supplie",
"croire que je vous honnor"). The system is a **homophonic pigpen**: sign = cell shape (+ optional inner stroke)
+ 1-3 dots; common letters have several signs. The pencil key on the flap is NOT the key.

Working key (`key_fr3.json`; `*` = inner stroke; some values still provisional):
a=B1  b=H1  c=F1  d=I1  e=E1,E*1,K3?  i=E2,E*2,B*1  l=F2,F3,F*3  m=G1  n=A1,D*1?,K1  o=D1  p=E3,E*3
q=C1,C2  r=I2,I3,D*2  s=H2,H*2,I*2,F*2  t=D2,B2,F*1  u/v=A2,A*1  y=G2  h=K2  nn/ss?=X2  g=B*2

Reading of p.3 (end of the letter; brackets = my regularisation, ? = unsure):
  je ne pouvois recevoir d'un ennuy plus sensible [qu'] ayant appris que du [ma]riage de cet[te] ... l'homme
  lequel ... de vie ... [&] de la part de [&] mon ... vous avez esté ... quelque ... closes, prejudice
  de l'entiere affection ... a vostre service ... je puisse prendre confiance ... nous eussions ...
  jusque je ne te dis rien tant que les occasions de ... des effets ... ce que cet entier homme ...
  et vous supplie tres humblem[ent], monsieur, [de] me continuer l'honneur de vostre bienveuillance
  et croire que je vous honnor[e] ...
Language and formulae point to a French letter of the 17th century. Sender and recipient are not yet identified.

Next: hand-transcribe pp.1-2 (the start of the letter, which should name people), finish the key, then /writeup.

## Reading of the last page (f. 243; `hand_p3.txt` → `p3_plain.txt`, key `key.json`)

Raw decipherment, one line per written line:

    ieneponunisreceuoid / unennuyplussensible / ayantapidisquedunri / agedecegentillomme /
    lequessaluiderviedement / &ndelapartde&monmaio / usauiestreuquelfu / closespreiudice /
    dehentiereaffectionse / iayuoueauostreseruice / utesteiersnenei / ipeusseprendreconfia /
    nuouseussiescouguupr / luyqueienecledisrien / tantfuetesoccasionsdeutub / entesmoingnerdeseffets /
    iescrisa&cequecegentil / lommealloetfaircpardela / etuoussupplietreshunblem / monsieurmecontinuerlloseur /
    deuostrebienueuheanceet / croirefueieuoushonnor

Regularised: "... je ne pouvois recevoir d'un ennuy plus sensible, ayant appris que du mariage de ce gentilhomme,
lequel ... de la part de mon ma[istre] ... vous a esté ... prejudice de l'entiere affection [que] j'ay vouée
a vostre service ... je puisse prendre confiance ... Je ne te dis rien tant que les occasions ... en tesmoigner
des effets. J'escris a[u] ... ce que ce gentilhomme alloit faire par dela, et vous supplie tres humblement,
monsieur, me continuer l'honneur de vostre bienveuillance et croire que je vous honnor[e] ..."

Key notes: C1 serves both f (affection, effets) and q (que): either a true polyphone or an inner-mark variant
not separated in transcription. K1=c, K2=h, B2/B*2=g, G2=y. The two circle/"9" signs (@) and the stacked
composites are unresolved; they sit where names or abbreviations are expected (e.g. before "de la part de").

## First page (f. 241)

Auto-segmented (`v1_glyphs2.json`); the classifier often reads ⊔ as ◻ on this page. Hand-checked columns give
"... disposer ... envoier le ...", "... la santé ... la longue maladie qu'il a eue, je m'asseure ...",
"... que les personnes ...", "vous aimés, n'en seroint ...", "... mon costé ...", "... mon coeur ...",
"... faveur ...". Full hand transcription of f. 241 is still open.

Sender, recipient and date are not named in the parts read. The formulae ("monsieur", "tres humblement",
"vostre bienveuillance") and spelling point to a French letter of the 17th century, from a client or
servant to a patron.

## Remaining gaps
- f. 241 (p. 1), all but hand-checked fragments - blocker: not-attempted; auto-segmentation too noisy, full hand transcription not done
- f. 242 (p. 2) - blocker: not-attempted; never transcribed
- the two circle/"9" signs and stacked composites on f. 243 - blocker: open-codes; they sit where names or abbreviations are expected, too few to value
- sender, recipient and date - blocker: not-attempted; expected in the unread start of the letter

## Escalation
- [ ] siblings: not done — the neighbouring SP 106/10 records around ff. 241-243 were not opened for this letter (sp106box10 covers ff. 125-205 only)
- [ ] clear-pages: not done — check those neighbouring records for a decipherment or clear copy
- [x] known-keys: the pencil flap key tested in all orientations and rejected
- [ ] print: not done — only a web search; no calendar (CSP Domestic/Foreign) searched, needs the sender from p. 1 first
- [x] key-rebuild: homophonic key built by annealing (hc3.py) on the p. 3 hand transcription plus hand anchors (key.json)
- [ ] retry: not done — hand-transcribe pp. 1-2 with inner-mark variants separate and decode with key.json, then rerun the annealer on all three pages
