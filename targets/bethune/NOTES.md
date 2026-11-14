# Henri IV to Philippe de Béthune (Rome), 9, 10 and 22 November 1601 — BnF fr. 3484 nos. 7, 8, 12 (catalogue item 22)

Status: in progress (23 Oct 2026, consistency pass: the Halphen 1889 edition is not yet opened, a gap marked not-attempted; the print, key-rebuild and retry escalation steps are not done)

**14 Nov 2026, verification pass (Claude Opus 5.5): three code groups fixed, letters still read in part.** The eight
cipher lines of f. 53r, block 1, were transcribed and aligned with their verbatim marginal gloss
(`f53r_alignment.md`): **72 = vous** (four aligned occurrences, which settles the proposal below and the D1
counter-indication), **6, standing as a word, = Sa Sainteté** (three), **66 = sa** (one); also `3:` = faire, `+.` = de,
`n,` = nous. A pre-registered check on glossed blocks not used for the derivation (f. 56r, f. 50r) found only one
locatable occurrence (72 under *que je vous*, agrees): not conclusive; the protocol measurement is not applicable to
groups this rare. Three 22 Nov runs give sense with the new values and the clear frames (*vostre negotiation*,
*…correspondance … discretion*, *le respect*), probable only. The 9 and 22 Nov letters stay decoded, not read;
Halphen 1889 is still behind HathiTrust's human check (403 on 14 Nov) and not elsewhere online.

**Status, 17 Sept 2026 (third pass): partly read; the 22 Nov letter (ff. 46r-47v) now transcribed in full.** The 10 November letter (f. 34) is read in full, because its minute survives in
clear four leaves on (f. 36, the notice's "copie du n° précédent"); that pair, six glossed passages of the 8 November
letter and a glossed passage of 10 December give the cipher's design and most of its letter values; the 9 November
letter (f. 33, one page entirely in cipher) decodes to about half of its words with that key and a French language
model; the 22 November letter (ff. 46–47, some forty lines) is transcribed in part and not decoded. The key is a
Villeroy-office cipher of the same design as the one Bazeries printed for Béthune's brother in 1599 (letters =
figures and letter-shaped symbols with homophones; letters with a comma, one dot or two dots = words in alphabetical
series; two-digit figures = names), with different values.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read in part**. The
10 November letter reads (from its clear minute). **The 9 and 22 November letters are decoded, not read**: the 9 Nov
decode gives about half the words, in lines that do not build sentences; the 22 Nov cipher runs are fragments inside
clear French. About a fifth of the cipher tokens read (estimated); "about six words in ten" below is withdrawn as a
reading figure.

**22-23 Oct 2026, re-read (REREAD_BRIEF, batch b17): 9 and 22 Nov stay decoded, not read.** Step 1 found the print
route the third pass could not reach: **Halphen's *Lettres inédites du roi Henri IV à monsieur de Béthune … du 18 octobre
au 24 décembre 1601* (1889) is in full view on HathiTrust**, item `iau.31858014633857` (record 100644113, public
domain). babel.hathitrust.org serves it only after a Cloudflare human-verification check (curl 403; the browser pane
shows the checkbox), which this session did not pass. Opening
https://babel.hathitrust.org/cgi/pt?id=iau.31858014633857 by hand and checking whether Halphen prints the ciphered
passages of 9 and 22 Nov in clear is the next step; it would read both letters and give the key by alignment. No new
image route (the transcription ceiling of the third pass stands). Not on the Internet Archive, Gallica or Google Books.

Working files: `corpus.txt` (known-plaintext pairs), `ct_f33.txt` (the 9 Nov cipher, 1.5× transcription),
`em_align.py` / `em_model.json` (EM alignment and the learned P(unit | symbol)), `decode.py` (character 5-gram
Viterbi) and `worddecode.py` (lexicon decoder, trie over the Xivrey volumes), `decode_f33.txt` (their output),
`key.tsv` (the key as recovered), `reading_10nov.md` (the 10 Nov letter). Third-pass files: `lm.py` (period-French LM), `decode2.py` (bigram word-lattice decoder), `eval.py` (control harness), `oracle.py` (ceiling), `crop.py` / `lines2.py` / `cut.py` / `sheet.py` (image pipeline), `seg.py` / `align.py` / `align2.py` (segmentation attempts, negative), `reading_22nov.md` and `ct_f46r.txt` (f. 46r). Images (`img/`, `full/`, crops, the
Xivrey and Bazeries downloads) are gitignored; `fetch.py` / `fetch_full.py` refetch them (Gallica IIIF, canvas =
2 × folio + 7 for a recto).

## Leaf map (from the images; the notice's folio guesses in the catalogue were wrong)

| item | date | folios | canvases | cipher | decipherment |
|---|---|---|---|---|---|
| 6 | Paris, 8 Nov 1601 | 30r–31v | 67–70 | six passages, 1–5 lines each | numbered marginal glosses in a smaller hand (paraphrase, near-verbatim) |
| 7 | Paris, 9 Nov 1601 | **33r** | 73 | 22 full lines, one passage after "il me mande qu'il est certain que" | **none** |
| 8 | Paris, 10 Nov 1601 | **34r–v** | 75–76 | 4 + 8 + 2 + 3 lines in four passages | **none on the leaf; the minute f. 36r–v (item 9) is in clear** |
| 9 | "Du Xe 9bre 1601" | 36r–v | 79–80 | none | the minute of no. 8, with corrections |
| 10 | Saint-Germain, 18 Nov | 43–44 | 93–95 | none | – |
| 12 | Saint-Germain, 22 Nov 1601 | **46r–47v** | 99–102 | c. 40 lines in several blocks | **none** (no clear copy found; f. 45 and f. 48 are address leaves) |
| 13 | Paris, 10 Dec 1601 | 49r–50v | 105–108 | 5 lines on 49v, c. 9 on 50r | footnote gloss on 49v (verbatim), marginal glosses on 50r |
| 14 | 24 Dec 1601 | 53 | 113 | 9 + 2 lines | marginal glosses |
| 16–17 | Jan 1602 | 56–57 | 119–121 | several blocks | marginal glosses |

Bazeries 1901, pp. 28–29 ("Chiffre baillé à M. de Béthune, 1599", Gallica bpt6k325768q, canvases 40–41) is the
elder brother's key of the same office: A = 3 + three symbols, B = 10 …; names = figures with two dots (Le Roy 4̈,
Le Pappe 3̈, Le Roy d'Espagne 2̈, Aldobrandin not present); words = a, ayant … z, nous; ä nostre … ÿ selon; 2, tout …
11, vivs; Δ doubles, y and $ cancel. The 1601 key uses the same conventions with other values.

## What is read

**10 November 1601 (f. 34).** The minute f. 36 gives the text of every enciphered passage; the sent original follows
it word for word except for small variants ("la somme de dix mil escus" written with the figures 6 7 1 for *a t i*
in "gratification"; "faites doncques valoir … et faites semblant que vous n'aiez receu la presente"). Reading in
`reading_10nov.md`. The passages: the King had "ce pretexte de gratifier led. Cardinal" [Aldobrandini] after the
Parlement's judgment in the Este–Aldobrandini debt, paid him 10,000 écus through Sillery at once, will pay 10,000
more in the first four months of 1602 through Sillery's brother "sans avoir esgard à l'arrest obtenu par lad.
duchesse de Nemours", wants Béthune to tell Cardinal Aldobrandini through Cardinal d'Ossat, "de facon qu'il recoive
et estime ceste grace comme elle merite", to pretend not to have received the letter, and to be "le premier qui en
avertira led. Cardinal Aldobrandin".

**Key.** `key.tsv`. Letters (confidence from the EM posterior and hand checks at 4× and 7×): e = Z ff EP 0;
a = 4 6 u; i = Cm(hooked m) v a 1; o = f + t; t = q 7 (p uncertain); s = g R2(2-shaped r) n; r = r d(∂-shaped);
l = h B S PH; m = x; f = m; u = y c; v = c; c = b e; p = o T; g = Cu(hooked u); x = f (in *veux*); y = a.
Word signs: f, = le; g, g' = la; x, = que; r, = par; s, = pro; q, q_ = pour; d, DL, = je; x: x^ = et; s: = dit;
t. t: = de; p: p. = ce; f: = au; J = bon; J, = mais; m, = men(t); y: = ent; r: = du; a, = faict; 61 = qui;
63 = re; 65 = si. Names: 48 = Cardinal, 17 = Aldobrandin, 7 = le Roy d'Espagne (P7, f. 56r). Open code groups
in the 9 and 22 Nov letters: 44, 45, 62, 66–72, 26–28, 5, 3, 8.

**9 November 1601 (f. 33).** `decode_f33.txt`. With the key and a lexicon decoder about half the words read; the
letter is about the Spanish news from La Rochepot's secretary and the cardinalate: "…et le [44] de la … cardinal …
de leurs places … le premier …", "…seront d'interest que [69] … partant vous en conférerez [avec] Aldobrandin…",
"…de vous dire … qu'il a de telles pratiques…", "…jamais il m'avoit … proposé de rechercher le cardinal…", "…comme
sera la promo[tion] [71] au cardinalat de … Alexandre communiqu…", "…les cardinaux de Joyeuse et d'Ossat … ensemble
ce que vous aurez…", "…Alexandre quelque instance que je ne face…", "…de partir de ce premier de [62] … des raisons
des dits car[dinaux]". Not a reading yet; a substance.

## Second pass, 17 Sept 2026 (evening): 4x re-transcription

`ct_f33_v2.txt` is the 9 Nov leaf re-read symbol by symbol from the 4x sixth-line crops (`q33_*.jpg`), and
`corpus_v2.txt` the f. 34 known-plaintext blocks re-read the same way (B3 from l. 26, B4, C, V1 l. 1 at 4x; the
rest and P1-P7, D1 at 1.5x). New from the 4x reading, all confirmed on several words of the minute:

* **φ is the doubling sign** of Bazeries' 1599 description ("Δ doublera son prochain précédent"): so-m-φ-e =
  somme, la-n-φ-e-φ = lannée, h-φ = ll in Sillery, o-c-φ = occ in occasions, u-φ = uv in retrouve (u/v one letter),
  mie-n-φ-e = mienne. `em_align.py` and both decoders now expand φ to the previous symbol.
* **Two-digit groups 61-73 are syllables and short words**, not names: 61 qui, 63 re, 65 si, 68 tout (toutes = 68
  Z g), 71 tion (affectionne, promotion), 73 vostre?, 70 car/tant?. Names are 48 Cardinal, 17 Aldobrandin, 7 le Roy
  d'Espagne, and the open 44, 45, 62, 66, 67, 69, 72, 26, 27, 28.
* Letters fixed on words of the minute: p (the ꝑ-like letter) = u/v (volonte = p t h f LS q Z; quatre = d p 4 q 63;
  luy = S p a); S = l (valoir = c 4 S + Cm r); Cm (hooked m) = i (merite = x Z R2 Cm q Z, mienne, valoir); R2 = r in
  merite/payer but s in fis/des; g = n in prochaine/mienne/occasions but s in les/escus/lors (two glyphs merged, an
  open-tailed and a looped g); plain m = g in grace/gratification, d in conduitte, f in fis (three glyphs merged);
  b = c; n = b (obtenu = + n q Z g); word signs S: = dit, R2, = par, q, = pour, l, = moi(s), m, = men(t), y: = ent,
  a, = faict, J = bon, + = o but also "de" in two places (two crosses?).
* [Third pass: `decode_f33_v3.txt` is the same transcription through `decode2.py`'s bigram LM. It adds
  "sur le revenu de Naples", "le nunce resident", "les cardinaux … enclins a la [26]", "aux prudens
  advis desdits card[inaux]", and keeps the v2 readings; the gain over v2 is small, as the oracle
  bound predicts.]
* Decoding `ct_f33_v2.txt` with `em_model_v2.json` (`decode_f33_v2.txt`) reads more of the 9 Nov letter but still
  about six words in ten: "...sera la promotion au cardinalat ... Alexandre ... ensemble ce que vous aurez ... jamais
  il m'avoit dit ... propos de rechercher le cardinal ... en telle occasion l'asseurant que ... de vous dire la
  res[olution] ... de telles pratiques ... je me remects de re[pr]endre ... des advis desdits car[dinaux]". The
  letter is about the Spanish pressure over the cardinalate of Don Alexandre and the cardinals' advice, not
  military news.

The remaining ambiguity is in three glyph families my eye does not separate reliably (g/ɠ, m/ɱ/ꞵ, r/ꝛ) and in the
two-digit names. Full-resolution copies of the glossed leaves ff. 53r, 56r-57r (c113, c119-121) are now on disk
(`full/`) and cut at 4x (`q53_*`, `q56_*`); their glosses are read (`f53r_margin.jpg`, `f56r_margin*.jpg`), their
cipher not yet transcribed. That is the next increment.

## Method, and where it stopped

1. Volume fetched (canvases 55–130 at 2000 px; 3996 px originals for the pages worked). Leaves mapped; the minute of
   the 10 Nov letter found by reading the sheets, not from the notice.
2. Known-plaintext corpus (`corpus.txt`): the 10 Nov cipher against the minute (four blocks, c. 480 symbols); the
   six glossed passages of 8 Nov; the footnote passage of 10 Dec. EM alignment (`em_align.py`: monotone, each symbol
   0–12 letters, proper string prior, seeded with hand-verified values, nulls allowed on PH HB $ Y LS) gives
   P(unit | symbol). Two decoders on the 9 Nov transcription: character 5-gram Viterbi over Xivrey's *Lettres
   missives* vols III–V, and a trie/lexicon decoder.
3. Hand checks at 4× and 7× on f. 34 fixed the glyph classes the 1.5× transcription had merged: hooked m (= i) vs
   plain m (= f), 2-shaped r (= s) vs r, u (= a) vs n, 6 (= a) vs b (= c), 671 = *a t i*. They also showed the
   transcription of the 9 Nov leaf carries the same merges, which is why the decoders plateau around half the words.
4. The 22 Nov letter (ff. 46–47) was cut into third-line crops; lines 1–7 read, the rest not. Gallica began
   refusing connections (HTTP 429, then closed connections) after the volume fetch, so the full-resolution copies of
   the glossed leaves ff. 53 and 56 (which would fix the remaining code groups) were not obtained in this session.

## Third pass, 17 Sept 2026: where the ceiling is, and the two routes past it

This pass set out to do what the second pass prescribed — re-transcribe f. 33 and ff. 46-47 at 4x and
rerun the decoders. It first built a control harness, and the harness changed the plan: the decoders
were already at their ceiling, and the ceiling is set by the transcription, not by the key or the
language model.

### Tooling added

* `lm.py` — period-French language model built from Berger de Xivrey, *Recueil des lettres missives de
  Henri IV*, t. I-V (Internet Archive `recueildeslettre0[1-5]henr`; 1.43 M words, 457 k bigrams,
  342 k character n-grams), normalised to the cipher's alphabet (lowercase, no accents, j->i, v->u).
  `targets/bethune/xivrey/` is gitignored and refetched from the identifiers above; so is `lm_cache.pkl`.
* `decode2.py` — word-lattice decoder. Beam search over word boundaries, each candidate word scored by
  a bigram LM with a character-6-gram backoff for names and rare spellings, replacing the unigram
  lexicon of `worddecode.py`. Code groups pass through as `[nn]`.
* `eval.py` — scores a decoder against every known-plaintext block of `corpus_v2.txt`: letter accuracy
  by Levenshtein alignment (so one misplaced word boundary is not punished twice) and words recovered
  in order by LCS.
* `oracle.py` — the upper bound. A monotone DP lets every token emit *any* unit in its model support
  and counts the true letters it could cover. This separates "the search is at fault" from "the
  transcription is at fault".
* `crop.py`, `lines2.py`, `cut.py`, `sheet.py` — image pipeline: page overview, line indexing by
  ink-profile peaks with the line pitch taken from the profile's autocorrelation, line cutting into
  thirds at 3x, and vertical stacking of strips. Stacking six thirds into one sheet reads two full
  lines per view at unchanged horizontal resolution.
* `seg.py`, `align.py`, `align2.py` — the segmentation experiments described below (all negative).

### What the ceiling is

Measured on the known-plaintext blocks of `corpus_v2.txt`, which are also what `em_model_v2.json` was
trained on — so these are best-case numbers, not held-out ones:

| measurement | letters | words in order |
|---|---|---|
| argmax of the key, no language model | 67.4 % | – |
| `decode2.py`, bigram LM (`eval.py`) | **74.5 %** | **51.8 %** |
| `oracle.py`: ceiling of the present transcription | **71.0 %** | – |
| same, at `--minp 0.005` | 72.1 % | – |
| oracle with confusion-widened emissions (`--wide`) | 80.6 % | – |
| `decode2.py` with the same widening, eps 0.15 | 71.9 % | 47.6 % |

Two things follow. First, the decoder already scores *above* the oracle bound of its own emission
model — it gets some letters right by accident — so **no further work on the search or the language
model can help**: about 29 % of the true letters cannot be produced by the tokens as transcribed.
Second, widening each token's emissions to those of its visually confusable partners raises the
ceiling by nearly ten points but *lowers* the real decode by 2.6 points; the extra ambiguity is more
than the language model can resolve. Widening is kept behind `decode2.py --wide` and is off by default.

Per block the oracle runs from 100 % on V3 to 52 % on D1, tracking exactly the zoom at which each block
was transcribed (D1 and P1-P7 at 1.5x, A/B/C/V1 at 4x). The transcription is the binding constraint.

### Why the glyphs cannot simply be re-read

The confusions are sub-glyph. Calibrating on f. 34v l. 1, whose token sequence is verified against the
minute, *conduitte* is written `b t g <m-like> r <m-like> q Z`: the same m-like shape stands for *d* in
one position and *i* in the next, the two differing only by a hook. The 4x re-reading of the second
pass hit this wall and so does a fresh eye. The three families recorded there (g / looped g, m / hooked
m, r / 2-shaped r) are real, and they are not resolvable at the ~450 dpi that Gallica's full resolution
gives for this folio — so a better scan would not help either.

### Why the machine cannot segment it either

* `seg.py` (connected components, small parts merged into the component they overlap): on f. 33 it
  gives 65 components per line against 47 hand-transcribed tokens, 1.38 per glyph; on f. 34r block A it
  both over-cuts (`4 a` split) and under-cuts (`g Z p f` swallowed into one box).
* `align.py` avoids cutting altogether: it concatenates a block's cipher spans into one strip and lets a
  DP give each token of the known sequence a variable-width slice scored against a per-class template,
  templates re-estimated from the alignment (hard EM). From a uniform start every template collapses to
  the average glyph, the DP then has no preference, and the alignment stays uniform — checked on the
  montage, where the labels drift steadily behind the ink.
* `align2.py` restricts the cuts to component boundaries and adds a per-class log-normal width model to
  break the symmetry. On block A the component pass yields 156 boundaries for 138 tokens — 1.13 per
  token — which leaves the DP almost no freedom, so it cannot recover where the components are wrong.

An automatic reader is reachable, but it needs a few hundred hand-drawn glyph boxes on one page to seed
the templates. That is the one piece of manual work that would pay for itself.

### The 22 November letter read (ff. 46r-47v)

All four pages of the 22 Nov 1601 letter are transcribed in `reading_22nov.md` - the first reading of
any part of it. It alternates clear French with short cipher runs inside the same lines, so the clear
text carries the sense, and it is countersigned by Villeroy ("DE NEUFVILLE"). It answers Béthune's
despatch of 29 October, received on the 18th.

What the clear text gives: a rebuke, in clear, of two persons named only by code groups - *"Il me
semble que [20] [S 12], qui sont douez de toute prudence, ont faict faulte de n'avoir rompu ce coup,
car ilz l'eussent faict facilement s'ilz y eussent pensé et operé d'heure, ainsi qu'ilz devoient"*;
the pension of the s.r Camaiano, to be paid, all to *"relever le party françois a Rome"*, with orders
not to give hopes or promises to others without express command, *"afin de n'abuser personne ne moy le
premier"*, and always *"après toutesfois en avoir conferé avec le Card.al d'Ossat"*; the Pope's *"bon
accueil … aux deux audiences"*; *"j'en diray autant au s.r Barbarino quand il sera arrivé"* (Maffeo
Barberini, the future Urban VIII, then on his way to France); the Jesuits deferred to an earlier
letter; an agent *"qui reside en Suisse, accompagné d'un certain Julio de la Torre y Travers[i]"* and
the reprimand Cardinal Aldobrandin gave him; and, in clear at the end of f. 47r, *"J'attends en bonne
devotion le retour du courrier que je vous ay envoié pour convier sa S.té au baptesme de mon filz,
lequel se faict tres bien nourrir et se fortifie a veue d'oeil"* - the dauphin, born 27 September 1601.
Dated *"Escrit a St Germain en Laye le xxij.e jour de 9bre 1601"*, signed HENRY, with a postscript,
signed again, that countermands part of the letter.

`ct_22nov.txt` holds all 80 ciphered runs. Decoded with `decode2.py` they give fragments only - "de le
resultat et sur", "leurs serviteurs", "le cardinal aldobrandin", "attenter a este toute", "suisses",
"octobre", "sainctete au" - which is exactly the ceiling measured above. `73` = *vostre* and `48 17` =
*Cardinal Aldobrandin* are confirmed by their clear frames.

Code groups seen in the letter, besides the known `48` Cardinal, `17` Aldobrandin, `61` qui, `63` re,
`65` si, `68` tout, `71` tion, `73` vostre: `2`, `5`, `6`, `8`, `9`, `12`, `20`, `28`, `31`, `44`, `66`,
`67`, `69`, `72`, `80`. Three have clear frames that constrain them: `S 12` and `20` are the two persons
"douez de toute prudence" (in Rome in Nov 1601, most likely the cardinals d'Ossat and Joyeuse, named in
clear on f. 33 - not proved); `28` is a place, from *"ce[luy] m'a escrit de [28]"*; `44` follows "et par
consequent". The glossed leaves ff. 49v-50r, 53r and 56r-57r (canvases 105-108, 113, 119-121, all in
`targets/bethune/full/`) carry marginal decipherments in the office hand and are the cheap route to fixing them.

### A proposal for one open code group: 72 = *vous*

Not proved, and flagged here the way this repo flags unconfirmed proposals - it must not be quoted as a
reading until the f. 53r alignment below confirms it.

The evidence is philological, not statistical:

* `x , 72` - *que* followed by `72` - occurs three times in the 22 Nov letter (f. 46r L07, f. 47r L06,
  f. 46v L22) and once in f. 33 (`p: x, 72`), i.e. four times as the collocation *que vous*.
* `72` opens a line three times on f. 46v (L01, L14, L27), which suits a pronoun.
* On f. 53r, whose marginal gloss is verbatim, the gloss reads *"…ie ne suis pas d'auis que vous
  pressiez sa Sain.té…"* and the cipher at the end of the block's second line runs
  `… x , 72 , T 63 , r S Z`. With the established values T = p, 63 = re, r = s, Z = e that is
  *que · vous · p-re-s-s-e*, i.e. *que vous pressiez*.
* `S 12 72 4 S` on f. 46r L09 then reads *"le [S 12] vous a l…"*, which fits its frame.

The full text of the f. 53r gloss, read at 2.8x from canvas 113 (the block it belongs to is marked with
a double cross, and the same mark stands over the cipher between *responce* and the first group):

> Je confesse, je ne suis pas d'auis que vous pressiez sa Sain.té de me faire scavoir sa volonté sur ce
> faict, ny que vous vous mettiez en peine de justifier davantage la mienne, encor que sur les discours
> d'autruy. Il fault, nous confians en la prudence et cognoissance de sa Sain.té, de la sincerité avec
> laquelle vous avez jusques icy procedé, attendre ce quil plaira a sa Sain.té vous en ordonner.

A decode-level test is not available: `[72]` as an opaque group and *vous* as a value segment their
neighbours identically, so the score barely moves (-6145.1 to -6138.2 over the whole 22 Nov letter).
What would settle it is the alignment of the eight lines against this gloss.

**And there is a counter-indication, recorded here so the proposal is not adopted on the strength of the
collocations alone.** The D1 block on f. 49v ends `… LS r y f p r 63 72`, and its footnote gloss ends
*"…il sera meilleur de differer a luy en parler"*. A final `72` is hard to reconcile with *vous* there.
Two readings survive: either the ciphered block runs on past the passage the footnote glosses (the
footnote is keyed to a marked passage, not necessarily to the whole block, and the letter continues on
f. 50r), or `72` is not *vous* and the four `que 72` collocations are something else. Re-reading f. 49v
at full resolution did not settle it - the 1.5x D1 transcription is the worst block in the corpus
(oracle 52 %), so its tail is exactly where its errors would be expected. **`72` stays unconfirmed.**

### Two more things tried on f. 33, both negative

**A re-reading at full resolution.** The second pass read f. 33 from the 2000-px Gallica image; the
3926-px original gives about 30 % more linear resolution, and `cut.py … 4 3.0` puts a quarter of a line
in one view at roughly 2.6x the original pixels, against about 2.0x for the sixth-line crops of the
second pass. The glyphs are visibly crisper. It does not settle them. An independent reading of the
first three lines disagrees with `ct_f33_v2.txt` at much the same rate as before, and there is no ground
truth on this leaf to say which reading is right - which is the clearest evidence yet that the ambiguity
is intrinsic to the hand and not an artefact of the earlier session's zoom. A third transcription of
unknown relative quality is worth less than the honest statement that two careful readings disagree.

**The figures as a lattice.** The re-reading did localise the disagreement: it clusters in the *figure
runs*, not in the letters. The cipher writes figures without separators and one- and two-figure groups
coexist (3, 5, 7, 8 beside 61, 63, 65, 68, 71, 73), so a run reads as `61|65` or `6|1|65` or `61|6|5`,
and a transcription that commits to one split bakes an error in that no decoder can undo. `decode2.py`
now has `SPLIT_FIGURES`, which merges adjacent figure tokens back into a run and expands it into every
legal split, weighted towards splits that use known groups, leaving the choice to the language model
(`run_emissions`, `merge_figures`).

It makes things worse, on both the control and the target:

| | letters | words in order |
|---|---|---|
| fixed splits (default) | **74.5 %** | **51.8 %** |
| figures re-split by the LM | 70.8 % | 48.7 % |

and on f. 33 it turns *partant* into "par [70]leroydespaigne[2]" and *de m…* into "[77][2]". The reason
is visible in the numbers: in the corpus blocks the second pass fixed its splits against known
plaintext, so they are already right and merging destroys good information. That makes the control
biased in favour of fixed splits, and the f. 33 result is therefore the more telling one - the merge is
too aggressive where figures are genuinely adjacent but genuinely separate. `SPLIT_FIGURES` is off by
default and kept for anyone who wants to restrict it to runs of four or more figures.

### Two independent readings, unioned: worth about three points

The last idea, and the only one that attacks the oracle bound directly. Blanket confusion widening
failed because it adds alternatives everywhere; but widening only at the positions where *two careful
readers of the same ink actually disagree* is targeted, and the union of two readings contains the true
glyph more often than either alone.

Tested for real, not assumed. Block V1 (f. 34v ll. 1-2, 102 letters of known plaintext) was read again
from scratch off the full-resolution leaf at quarter-line crops, without consulting `corpus_v2.txt`,
and the two readings were aligned token to token by edit distance (`union.py`).

| reading | tokens | oracle |
|---|---|---|
| reader A - the second pass, at 1.5-4x from the 2000-px image | 68 | **75.5 %** |
| reader B - this pass, at ~2.6x from the 3926-px original | 72 | **57.8 %** |
| the two aligned: agree on 50 of 72 positions (69 %) | | |
| **union** - both tokens' emissions offered wherever they differ | | **78.4 %** |

Three things follow, and they end the line of attack.

1. The union does help, and it is the only widening measured to help at all - but by **2.9 points**,
   nowhere near what turning f. 33 from partly read into read would need.
2. **Reader B is much worse than reader A** (57.8 % against 75.5 %), despite 30 % more resolution. A
   second full reading of f. 33 would therefore cost twenty-one careful views to produce a transcription
   below the one already on disk, for a union gain of about three points.
3. Two readers agreeing on only 69 % of tokens is itself the measurement that matters. It is not that
   one reading is careless; it is that this hand does not carry enough information at 450 dpi to fix its
   glyphs, exactly as the 71 % oracle bound says.

`union.py` is kept: it is the right tool the day a *third* party - a palaeographer, or a reading taken
from the original in Paris - supplies a second opinion worth unioning.

### f. 53r: the best crib left for the open code groups

f. 53r (24 Dec 1601, canvas 113) was fetched at full resolution and examined. Two things make it the
cheapest route to the open groups, and they are recorded here so the next pass does not have to find
them again.

* Its left margin carries a **near-verbatim decipherment in the office hand**, not a paraphrase. Read
  from the image: *"Je confesse, je ne suis pas d'advis que vous pressiez sa Saincteté de me faire
  sçavoir sa volonté sur ce faict, ny que vous vous mettiez en peine de justifier davantage la mienne,
  encore que sur le discours d'autruy. Il fault nous, confians en la prudence et cognoissance de sa
  Saincteté, de la sincerité avec laquelle vous avez procedé, attendre ce qu'il plaira a sa Saincteté
  vous en ordonner."*
* The ciphered block **interleaves clear words with the cipher**, so the gloss can be anchored to the
  cipher at several points without solving anything first. Read off the image: *justiffier davantage
  que* stands in clear in the middle of line 4, and line 5 runs `Z g x , g Z r f, x` **discours**
  d[e] **aultruy. Il fault** `n , b Z 4 …`. Those clear words are the gloss's own words in the gloss's
  own order, which settles that the decipherment is verbatim and that the alignment is tractable.

And **`66` and `72`, both open, occur in this block** (line 3 ends `… r 66`, line 4 opens `66 ff + S LS
LS q Z g Z r ff a ,` and later `g a x , 72 Z ff r x Z`; `72` also stands at the end of line 2). Since
the gloss holds no proper name, `66` and `72` are words or syllables, which matches their
sentence-medial positions in the 22 Nov letter.

What is *not* done: the eight cipher lines of the block are not transcribed, so the alignment that
would fix `66` and `72` has not been made. `targets/bethune/cut.py 113 0.30 0.138 0.99 0.345 <prefix> 3 3.0`
cuts them ready to read.

### f. 56r confirms the pattern of the glossed leaves

f. 56r (Jan 1602, canvas 119) carries three marginal glosses, and the second and third name in clear
exactly the groups the second pass hoped for - *"Le Roy d'Espaigne est mal pourveu…"* and *"…et la en
Flandres ou Archiduc Albert a tout besoin d'assistance"*. Examined at full resolution, it behaves like
f. 53r: the gloss is verbatim, and whole clear phrases sit inside the ciphered block - *"les Suedes
aussy destruisent"*, *"Mais je ne croy pas quil le face"*, *"si ce n'est pour"* - each of which is also
in the gloss, in the gloss's order. So the glossed leaves are not blocks of cipher with a paraphrase
beside them; they are clear and cipher interleaved with a verbatim decipherment, which is the handle
for an alignment.

Only `7` (= le Roy d'Espagne, already in the key) could be read off directly; the figures visible in the
block are `27`, `35`, `68`, `0`, `63`, `65`. The line detector fails on this leaf (it finds a 292-px
pitch where the true pitch is about 146, so it merges line pairs) and the block was not transcribed. A
fixed `nlines` argument to `cut.py`, or a narrower x-window that excludes the marginal hand, is the
first thing to try there.

### The two routes that would finish these letters

Both are archival, and both are the pattern that closed Du Bellay (Le Grand 1688) and read Hesse
(Rommel 1846): the clear text exists in a copy or in print.

1. **BnF, Cinq cents de Colbert 346** — *"Copies des despesches concernans l'ambassade de Messire
   Philippe de Bethune, conseiller du Roy en son Conseil d'Estat, à Rome, en 1601-[1605]"*, volume I,
   **23 août 1601 – 22 novembre 1602**, letters of Henri IV, Marie de Médicis, Villeroy and Béthune
   (notice `archivesetmanuscrits.bnf.fr/ark:/12148/cc917290`). The range covers both the 9 and the
   22 November 1601 letters, and a copy register of this kind is made from the minutes, i.e. in clear —
   which is exactly how the 10 November letter was read here, from its minute at f. 36. **Not
   digitised**: Gallica SRU returns no record for it. This is the most valuable next step, and it needs
   a reader in the Salle des manuscrits or a reproduction order.
2. **Eugène Halphen (ed.), *Lettres inédites du roi Henri IV à monsieur de Béthune, ambassadeur de
   France à Rome, du 18 octobre au 24 décembre 1601*** — an edition covering precisely this stretch.
   HathiTrust catalogue record 100644113. Not in Gallica, the Internet Archive or Open Library;
   HathiTrust refuses automated requests (403 on the catalogue, the Bib API and babel) and the Google
   Books API rate-limited every attempt from here. Whether Halphen printed the ciphered passages in
   clear — he would have needed the minutes — decides whether these letters count as already in print,
   as fr. 3077/3078 did.

Checked and excluded as sources of a clear text: Xivrey t. I–V (t. V prints a Béthune letter of
10 October 1601 but nothing for November, confirming the second pass); Mélanges de Colbert 17
(`btv1b10034921n`), whose part I is still running instructions at p. 179 and whose part II is
1602–1605; BnF fr. 3677 and fr. 3678, the "Registre des lettres que monseigneur de Bethune a escrites
en France durant son ambassade de Rome", which are 1624–1630, the second embassy.

### Next step, revised

1. Read or order **Cinq cents de Colbert 346** for 9 and 22 November 1601. That alone finishes both
   letters and hands over the whole key by alignment.
2. Failing that, get Halphen's volume through a HathiTrust member library.
3. Only then is more work at the keyboard worth doing: hand-box one page of glyphs to seed `align2.py`'s
   templates, and transcribe ff. 46v–47v with the sheet pipeline.

**Next step as the second pass left it (superseded by the section above):** re-transcribe f. 33 and ff. 46–47 at 4× with the refined glyph classes
(`q33_*.jpg` crops exist for f. 33), add the glosses of ff. 49v–50r, 53r, 56r–57r to the corpus from the
full-resolution pages, rerun `em_align.py` and `worddecode.py`. The design is known, the letter values are mostly
known, and the remaining unknowns are the two-digit names, which the later glosses name (Duc de Modène, Roy
d'Espaigne, Archiduc, Fuentes).

Not in Tomokiyo (his Béthune ciphers are fr. 15975 for 1602–05 and fr. 15972 for 1606–08), not in DECODE
(search "Bethune" returns only Charost 1673), not in Xivrey (t. V has no Béthune letter for Nov 1601).

## Remaining gaps

The 9 Nov 1601 (f. 33) and 22 Nov 1601 cipher runs are decoded, not read (2,849 tokens; reading audit 22 Oct 2026); the two letter lines below carry their blockers. The glyph transcription (~70% accurate) caps the decode; re-transcribe on full-resolution crops, using the glossed leaves ff. 49v-50r, 53r, 56r to fix the confusable glyphs.

- 9 Nov 1601 letter, f. 33 (about half the words) - blocker: illegible; third pass measured the ceiling as set by the glyph transcription (similar glyphs differ by a hook), not by the key
- 22 Nov 1601 letter, 80 ciphered runs (ff. 46-47) - blocker: illegible; decode2.py gives fragments only, the same transcription ceiling
- code groups 2, 5, 8, 9, 12, 20, 26-28, 31, 44, 45, 62, 67, 69, 80 - blocker: no-key-material; 6, 66 and 72 fixed on 14 Nov 2026 from the f. 53r gloss (`f53r_alignment.md`); the f. 56r blocks and the second f. 53r block (the Cordelier) are the next cribs
- Halphen 1889 (HathiTrust iau.31858014633857, full view): may print the 9 and 22 Nov letters in clear - blocker: not-attempted; behind a human-verification page, to be opened by a person
- clear copies in BnF Cinq cents de Colbert 346 - blocker: needs-physical-access; copy register 23 Aug 1601 - 22 Nov 1602, not digitised (Gallica SRU no record)

## Escalation

- [x] siblings: f. 36 minute read the 10 Nov letter; glossed leaves ff. 49v-50r, 53r, 56r-57r examined
- [x] clear-pages: f. 36 is the clear minute of f. 34; marginal glosses on ff. 53r, 56r found verbatim
- [x] known-keys: Bazeries 1901 key for Bethune 1599 compared: same design, different values
- [ ] print: Halphen, Lettres inedites ... 18 oct - 24 dec 1601 located 22 Oct 2026 in full view on HathiTrust (iau.31858014633857) but behind human verification, not opened; Xivrey, Colbert 17, fr. 3677/3678, Tomokiyo, DECODE checked
- [ ] key-rebuild: partly done 14 Nov 2026 - f. 53r block 1 aligned (72, 6, 66 fixed); the f. 56r blocks and f. 53r block 2 not yet aligned
- [ ] retry: not done - rerun em_align.py / decode2.py on f. 33 and ff. 46-47 after the gloss alignments
