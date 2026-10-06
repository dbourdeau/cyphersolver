# Nicolas Raince, Rome, 1526 and 1529 (BnF fr. 2984, fr. 3040, fr. 3091)

Catalogue item 5 (the "gamble" of the five-item goal list). Two sessions, 17 September 2026.
Everything below is unvalidated until Daniel reviews it; the evidence for each claim is named.

## Outcome in one paragraph

The item was never a blind-solving problem. Tomokiyo published the 1526 key in 2020 and the 1529
key with it; DECODE holds two Raince letters as decrypted; the one letter "entirely in cipher"
(9 June 1526) has its contemporary clear duplicate eight leaves earlier in the same volume, as
Mignet noted in 1886; and Bourrilly printed the cipher passages of the 17 June and 20 August
letters in 1901. What has never been read anywhere found is most of the **13 May 1526** letter
(pp. 29-31) and the lower part of the **20 November 1526** letter (p. 105), about 106 lines.
**Session 2 (17 Sept 2026) found that the first session had misread Tomokiyo's key by one
column** - l, m and n were shifted - and re-measured the whole table off the key image; see
CALIBRATION.md. With the corrected table the control line resolves glyph for glyph, and a
rebuilt machine draft (`draft5.txt`, and `draft5_seg.txt` with word breaks) reads in long
stretches. Two lines have since been read glyph by glyph against the numbered-token images and
agree with the draft to about 86 % of letters, which is where the reading now stands: the key
and the page structure are settled, the residual gap is transcription accuracy on a microfilm,
not cryptanalysis.

## Prior art (checked 17 Sept 2026)

* **Tomokiyo, "French Ciphers during the Reign of Francis I"**
  (cryptiana.web.fc2.com/code/francis.htm, first posted 2 Nov 2020, last modified 7 Dec 2023),
  section "BnF fr.2984 (1526)": key published as `francisRaince.png` (copy in `img/`).
  Monoalphabetic substitution with homophones for a (4), e (3), i (4), o (2), r (3), u/v (4);
  three nulls (λ, "ny", K); three word-signs: *con*, *l'empereur*, *le pape*. The same key
  serves fr. 3040 f. 21 (Raince to Montmorency, 7 Nov 1526). Section "Raince's Cipher (1529)":
  a second key for fr. 3091 f. 19 (12 Aug 1529), `francis_Raince1529.png`, with 16 word-signs
  (aux, bien, des, dit, de, en, et, il/je, la, le, les, leur, luy, pour, par, que). Tomokiyo
  credits Desenclos (HistoCrypt 2018) with locating the letters. He gives no plaintext.
* **DECODE** (de-crypt.org): records 4228 (fr. 3040 f. 21, 1526, "Decrypted", plaintext
  attached) and 3696 (fr. 3091 f. 19, 1529, "Decrypted", transcription and plaintext attached),
  both uploaded by user lehoanna 2022–23. Nothing from fr. 2984 is in DECODE.
* **Mignet, *Rivalité de François Ier et de Charles-Quint*, 2nd ed. 1886, t. II p. 211 n. 1**
  (archive.org `rivalitdefranois02mign`): "Lettre de Nicolas Raince à François Ier, écrite de
  Rome le 9 juin 1526 ... Mss. Béthune, vol. 8509 [= fr. 2984], l'original en chiffres f. 33,
  **le déchiffrement f. 17**." So no. 8 (ff. 33–37, wholly in cipher) has its contemporary clear
  duplicate at no. 5 (f. 17 ff., "Double de lettres ... des neufme et XIe juin"). Verified on
  the image: f. 17r begins "Sire, depuis les depesches envoyées du ... et une de moy ... adressée
  à monseigneur le grant maistre ... le comte de Venise ... le pape a depesché messire Francisque
  Guichardin, president de la Romaigne, qui partit vendredy matin pour commissaire general sur le
  faict de la guerre", and the same words are glossed above the first lines of f. 33r.
  Mignet also quotes the 12 June and 30 Jan 1527 letters (pp. 213–214, 272).
* **Bourrilly, "La première défection de Clément VII à la ligue de Cognac (août–septembre
  1526)", *Bulletin italien* 1 (1901) pp. 213–229** (archive.org `bulletinitalien01borduoft`):
  appendix II prints "simplement les parties chiffrées et qui n'avaient pas été déchiffrées
  encore" of the **17 June 1526** letter to the King (ff. 41–43, no. 10) and of the **20 August
  1526** letter to Montmorency (ff. 47–50, no. 11). He read them himself in 1901 (the
  interlinear decipherment on f. 41 is contemporary and partial). He also cites the 1, 20 and 27
  Aug letters and the Carpi letters of the volume.
* **Grethen, *Die politischen Beziehungen Clemens VII. zu Karl V.* (1887) pp. 108–115** used the
  9 and 17 June reports (per Pastor, *History of the Popes* IX pp. 308–311, notes). Not online
  in full text; not checked.
* **Pastor IX appendix XXXVIII** prints one Raince letter to Montmorency (1526). Not seen.
* Friedmann's cipher keys (NAF 4206) do not include Raince (Tomokiyo, "Further sources").

## The ciphered letters on the image

Gallica ark btv1b90598430 is a black-and-white microfilm of fr. 2984, 85 openings, all canvases
labelled "NP". Canvas n shows the opening whose recto is foliated 2n−3 (checked on ff. 17, 23,
25, 27, 29, 31, 33, 35, 37, 39, 41, 103, 105, 119, 121, 123); each canvas is 7,984 × 5,525 px
via `/full/full/0/native.jpg`.

| no. | folio | date 1526 | to | cipher on the leaf | read where |
|---|---|---|---|---|---|
| 6 | 25 | 1 Aug | Montmorency | last 7 lines of f. 25r | contemporary interlinear decipherment on the leaf |
| 7 | 29–31 | 13 May | Montmorency | f. 29r whole (36 lines), f. 30v whole (35), f. 31r upper half (25); clear close | later gloss on lines 1–c. 13 of f. 29r only; **rest unread anywhere found** |
| 8 | 33–37 | 9 June | the King | whole letter, 9 pages | clear duplicate f. 17 ff. (Mignet 1886); gloss on f. 33r top |
| 10 | 41–46 | 17 June | the King | most of the letter | interlinear decipherment; cipher parts printed by Bourrilly 1901 |
| 11 | 47–50 | 20 Aug | Montmorency | parts | cipher parts printed by Bourrilly 1901 |
| 24 | 105 | 20 Nov | Montmorency | 40 lines after 4 clear lines | gloss on the first c. 12 lines; **lower 21–28 lines unread anywhere found** |
| 28 | 121–123 | 7 Dec | Montmorency | c. 18 lines on f. 123r | dense interlinear decipherment on the leaf |
| fr. 3091 no. 11 | 19 | 12 Aug 1529 | Montmorency | — | DECODE 3696 decrypted; Tomokiyo's 1529 key |

Token count of the unread residue: 106 lines of about 50 glyphs, 5,629 segmented tokens.

**Note on the foliation.** The "folio" numbers in the table above are in fact **page numbers**,
written on odd pages only; see the session-2 section. Read f. 29r as p. 29, f. 30v as p. 30,
f. 31r as p. 31, f. 105r as p. 105, and so on. Gallica view n shows pages 2n-4 and 2n-3.

## Session 2 (17 Sept 2026): the key re-measured, and what changed

### The key had been misread by one column

`img/key3x.png` is Tomokiyo's table: a header row of plaintext letters over up to four rows of
cipher glyphs, columns about 78 px apart. Reading it by eye slipped a column. Locating the white
header letters and the ink blobs programmatically and assigning each blob to the nearest column
(every blob falls within 15 px of a column centre) gives the measured table in CALIBRATION.md.
The corrections that matter:

* **l** is the `9`, not the round `s`; **m** is the round `s`, not the long `f`; **n** is the
  long `f`. The first session had these one place to the left.
* **H is s**, not an r variant.
* p has two glyphs (`T`, and a circle with a dash to its right) and r has two (`4`, and a dash
  then a circle) — the two are near mirror images and are the easiest pair to confuse.
* The most frequent single glyph, a circle at the foot of a barred stem, is an e, as the first
  session said.
* g is a circle with a long bar driven through it; the *l'empereur* word sign is two small
  circles joined by a curve underneath; the *le pape* sign is a cursive y, while the letter y is
  `E`.

`img/key_labelled.png` is a contact sheet of every glyph cut out of the key and labelled.
`handmap.json`, `hand_decode2.txt`, `draft3.txt`, `greedy70map.json` and the readings in
`trans/f29r.txt` all rest on the shifted table and are not trustworthy as letter readings;
`trans/f29r.txt` is kept only as a record of what the first pass produced. The shift is exactly
what produced "dongUeaent" for *longuement*, "egsembde" for *ensemble* and "SonseigEur" for
*monseigneur* in that draft.

### The page structure: nothing is missing from Gallica

The leaf numbers on successive Gallica views run 29, 31, 33, 35, 37 — **+2 per view** — which
at first looked as if half the openings had not been filmed. They are page numbers written on
odd (recto) pages only: view n shows pages 2n−4 and 2n−3, 85 views cover about 167 pages, and
the digitisation is complete. So what these notes call ff. 29r / 30v / 31r are **pp. 29, 30,
31**, three consecutive pages of one letter, and "f. 105r" is p. 105. The text confirms it:
p. 29 ends "… ne se peut monstrer plus affe-" and p. 30 opens "-ction".

### The clear close of the 13 May letter (new)

`trans/p31_clear_close.txt`. Below its 25 ciphered lines, p. 31 carries ten lines of clear
French, signed and dated, which had not been transcribed here. It dates the letter "De Rome,
ce xiij jour de may 15c xxvj", signs it *Nicolas Rainse*, and reports that Rome expects
**Andrea Doria at Civitavecchia today or tomorrow with six galleys and two brigantines** —
nine days before the League of Cognac was signed at Cognac on 22 May 1526.

### The rebuilt draft

* `lmns.py` trains a space-free period-French character 6-gram on the Du Bellay (Legrand),
  Nevers 1593 and BnF French texts already in the repo.
* `solve3.py` (70 clusters) and `solve140.py` (140 clusters) hill-climb the cluster-to-letter
  map with **each cluster restricted to the letters its glyph shape allows**, read off the
  tight-cropped cluster sheets `img/z70_sheet_*.png` against the measured key. Restricting the
  moves is what stops the collapse into a degenerate map that defeated the first session's
  blind solver.
* `render140.py` writes `draft5.txt`; `seg_words.py` writes `draft5_seg.txt`, which segments it
  with a period lexicon and upper-cases whatever will not segment — a map of where the reading
  still fails.
* `htr.py` (per-token classifier plus LM beam) and `worddec.py` (joint letter choice and word
  segmentation over a lexicon trie) were tried and do **not** beat `draft5.txt`: both train on
  the map's own output, so they reproduce its errors. `qual.py` scores any draft by lexicon
  coverage and by distance to the control line.

Readable stretches in `draft5.txt`, all consistent with the letters' subject matter:
"pour perdre la belle occasion qu'il avoit", "de ce que l'on n'a escript autrement", "en son
royaume", "ce qu'il a envoye d'icy et de **Venise**", "trois fois qui avoit deu venir a
**Rome**", "prendre tout pour le mieulx", "qu'il avoit faict si soudainement", "un jour en
pleine place pres du palais", "qu'il avoit envoye de … **Naples**", and on p. 105, the
20 November letter, "seroit la cause de la totale ruine de sa maison" — Clement VII and the
Medici, two months after the Colonna raid on the Vatican.

### The reading

`trans/reading_edited.txt` is the reading: the ciphered residue of pp. 29-31 and p. 105 set out
as running French, with editorial word division, `[ ]` for letters supplied, `(?)` for readings
that fit but are not secure, and `...` for what did not resolve. **Nothing is supplied by
conjecture**: a gap is left as a gap. 86 of the 106 lines were read glyph by glyph; the other 20
are lines where the hand reading added nothing over the machine decode and are left out of the
edited text rather than dressed up. `trans/reading.txt` is the same material line by line with
each line marked `H` (hand) or `M` (machine) so the two are never confused, and
`trans/p31_clear_close.txt` holds the clear close of the 13 May letter.

### Lines read glyph by glyph

`bandsi.py PAGE LINE` writes `img/idx/<page>_<NN>.png`: the line at 2x with every token boxed
and numbered, so a hand reading is aligned to `raince_tokens.json` with no guesswork. The
readings so made are in `trans/verified_lines.txt` (p. 29 line 20; p. 30 lines 1, 2 and 8;
p. 31 line 21; p. 105 line 4). New content from them:

* p. 30 line 8: "… respondu a ce que ce qu'on a envoyé d'icy et de Venise par devers …"
* p. 31 line 21: "… un jour en plaine place pres du palais, un nommé **Pietro Anthonio** …",
  running on into line 22 "secretaire ou serviteur dudict, qui estoit icy pour …" — a named
  person in the ciphered part of the letter, surname not yet resolved.
* p. 105 line 4: "… [pontif]icat seroit la cause de la totale(?) ruine de sa maison …"

Measured against those lines, `draft5.txt` is right on about **86 % of letters**, which is why
only about a quarter of it segments into real words: a six-letter word survives at 0.86⁶.

### Where the ceiling is, measured

`gold/labels.txt` holds the hand labels as one character per token. `htr2.py` trains a
per-token letter classifier (PCA to 55 dimensions, Gaussian class-conditionals) on the
shape-constrained map's confident tokens plus the hand labels, and reports **leave-one-line-out**
accuracy on the hand-labelled lines - the only honest figure, since training on the map's own
output otherwise scores itself:

| training data | LOO per-token accuracy |
|---|---|
| map's confident tokens only | 0.840 |
| + hand labels, weight 1 | 0.856 |
| + hand labels, weight 8 | **0.868** |
| + hand labels, weight 30 | 0.860 |

PCA dimension 55 is the optimum (35 -> 0.856, 80 -> 0.860, 110 -> 0.860). `decode2.py` adds the
6-gram LM beam on top and writes `draft9.txt`, which is marginally better than `draft5.txt`
(lexicon coverage 24.2 % against 23.1 %, control-line distance 3 against 4).

The shape of that table matters: **hand labels buy about 3 points and then saturate.** So the
limit is not the key (settled), not the map (shape-constrained), and not the amount of training
data - it is the microfilm resolution and the connected-component segmentation. The confusions
that remain are between glyphs that really are similar at this resolution: `ψ` (e) against `4` (r),
`ℓ` (t) against `9` (l) against `ϙ` (d), and `∧` (s) against `v` (u) against `×` (a). Building a much
larger labelled set out of the clear/cipher pairs elsewhere in the volume would therefore help
less than it first appears; better images, or a sliding-window recogniser that does not commit to
a connected-component segmentation, or simply reading the lines by hand, are what would move it.

## Session 3 (5 Oct 2026): full re-transcription pass, sense measured

**The old measure did not count sense.** `fraction_read` 0.66 counted every resolved character on
an H line, whether or not it formed a word ("eav", "tcduesn" all counted). `measure_sense.py`
now counts a letter only when its whole word is a period-French word (lexicon from the
`fr-1530-despatches` corpus sources, u/v i/j y/i folded, plus a hand-checked list of period forms
and names in the script), and words broken at a line end are credited when the join is a word.
`?`, `(?)`, bracketed word signs and M lines count unread. Denominator = the line's non-null
machine token count. On the old `trans/reading.txt` it gives **0.476**, not 0.66.

**Re-transcription.** Page images re-fetched from Gallica (views 16, 17, 54); `img/idx/` rebuilt
for all 106 lines; `show.py PAGE LINE` prints the machine label per numbered token. Every line
was then read off its image and written to `trans/reading_v3.txt` (marked R) with `setline.py`.
All 20 former machine-only lines are now hand-read. New content, e.g.: p. 29 "fai[cte] entre eulx
mais qu il luy fera tant de guerre ... les aragonoys, bourguignoms, haynoyers et fla[mens] contre
ceulx de castile ... les castiliens disent au contraire que les dessusdictz sont veillacos et
borachos"; "ledict Herrera doit partir dans deux ou troys iours ... et Lopes Hortado"; p. 31 "donne
aduis au conte de Sainct Severin et conseil ... par la poste et ont despesche ung courier a toute
diligence"; "l ambassadeur dudict a faict entendre de semblable au duc de Sesse"; "ie ne scay pas
ou ilz les forgent"; p. 105 (Clement VII after the Colonna raid) "abandonner Rome et s enfuir ...
desirant la mort et parlant de sorte en souspirant si profondement qu il n y a si dur cueur qui ne
n eust eu la plus gran compasion du monde, et m a dict en la presence du ... que j escripvise le tout
au roy".

| page | old reading.txt (sense) | v3 (sense) |
|---|---|---|
| p. 29 | 0.538 | 0.923 |
| p. 30 | 0.606 | 0.857 |
| p. 31 | 0.363 | 0.845 |
| p. 105 | 0.313 | 0.748 |
| **all** | **0.476** | **0.850** |

What still fails: single glyphs inside words that will not resolve on the B/W film at any zoom
(the e/r/n, t/l/d, s/u/a sets), clustered on p. 105 ll. 15-17, 20-21, p. 30 ll. 30, 32-34 and
p. 31 ll. 1-2, 17, 23-24; and two non-key signs: the bold two-crossbar stem ([X], ~4 places,
clause boundaries, probably a name sign) and a circled four-armed cross ([X2], 4 places). Word
signs ([roy], [pape], [l empereur]) are read but counted unread by the measure, so 0.850 is a
floor.

### Session 3b (5 Oct 2026): enhanced zoom pass and printed cribs

`zoomx.py PAGE LINE F0 F1 [Z]` crops half a line at 2.5x with autocontrast, unsharp mask and a
soft threshold, with the token numbers ticked. Every worst line was re-read this way (p. 105 ll.
15-17, 20-21; p. 30 ll. 30, 32-34; p. 31 ll. 1-2, 17, 23-24). The enhancement resolved most of the
faint strokes. What it gave:
* **⊕ (circled cross, formerly [X2]) is a homophone of i.** It fits "bien" on p. 105 l. 20 ("θ ⊕ ψ f" =
  b-i-e-n) and "il avoit" on p. 31 l. 24, so it is no longer an open code.
* **The -| sign is o** ("du coste de dela" p. 105 l. 15, "mon seigneur" p. 30 l. 32), and the
  C-with-a-circle sign is the l homophone ("seulement" p. 105 l. 15).
* **ℓ° (a cursive ell with a small circle, [Y]) is a word sign** that is not in the key. It stands
  where a name or title fits: "contre [Y] comme l on devoit", "ledict [Y] il auroit tousiours le
  moyen" (p. 105), "de [Y] icy" (p. 30 l. 33) and "les dictz de [Y]" (p. 31 l. 2). It is open: 4 occurrences.
* The two-crossbar stem [X] follows "son maistre" on p. 31 l. 23, and so is a person's sign.
* New readings: p. 105 "ouoit procedoit seulement de ce que du coste de dela", "ne s estoit
  rompo(?) contre [Y] comme l on devoit"; p. 30 l. 32 "[X] mon seigneur, i ay sceu hyer soir de bon
  lieu que de Mantoue"; p. 31 l. 1 "traicte entre [le pape] ... et [l empereur]"; l. 2 "c est ceste
  nuyt passee les dictz de [Y] en ont donne aduis"; l. 23 "tout le mal de son maistre [X] et que
  deux ou troys foys"; l. 24 "il avoit este en voye d estre destruict pour luy".

**Printed cribs.** *Grethen 1887* is not on archive.org, HathiTrust or Google Books under any
search tried, so it is still not seen. Grethen pp. 108-131 quotes the reports of 9, 11 and 17
June, 20 Aug and 30 Nov 1526. Pastor cites none for 13 May or 20 Nov. *Pastor IX* (English, archive.org
`historyofpopesfr09past`) has been checked. Its appendix no. 38 prints **Raince to Montmorency, 26
Nov 1526, fr. 2984 f. 109**, six days after the p. 105 letter, and not the same text. It is a
strong parallel: "de tout habandonner et s'enfuyr", "ne voyant mesmement venir du coste de dela",
"n'a moyen d'obvyer". These are the phrases read independently on p. 105 ("abandonner rome et
s enfuir", "du coste de dela", "le moyen"), so it supports the reading but supplies no letter
values. The "1522 despatches" Pastor cites (9-10 Jan 1522, Béthune) are other letters, outside this target.

Sense measure after 3b: p. 29 0.923, p. 30 0.877, p. 31 0.872, p. 105 0.781; **all 0.870**
(0.850 before 3b).

## What would finish it

1. **Better images.** The Gallica item is a black-and-white microfilm; a reader's photographs
   of pp. 29–31 and 105 at reasonable resolution would let the segmentation run clean and would
   probably be worth more than any further modelling, given the saturation measured above.
2. **Continue the numbered-token hand reading with `bandsi.py`, line by line.** This is the sure
   route: `bandsi.py PAGE LINE` boxes and numbers every token, the reading is written as one
   character per token in `gold/labels.txt`, `htr2.py` checks it against the token count, and
   each line both adds to the reading and slightly improves the model. About 100 lines remain.
3. A recogniser that does not commit to a connected-component segmentation (a sliding window
   over the line with the LM doing the segmentation) would address the part of the error that
   more labels cannot. The aligned cipher/plaintext pairs elsewhere in the volume - the 9 June
   letter at pp. 33–37 with its clear duplicate at p. 17 ff., the interlinear decipherments on
   pp. 41 ff. and p. 123, and Bourrilly's 1901 printing of the 17 June and 20 August cipher
   passages - would give it the training data.
4. One glyph is still unidentified: a bold stem with two crossbars, standing as a one-glyph word
   (p. 30 line 1, between "plaisirs" and "qu'il"). It matches nothing in Tomokiyo's table.
5. Registration in DECODE of the eight fr. 2984 letters (none is there) is Daniel's step, with
   the key image credited to Tomokiyo.

## Files

`NOTES.md`; `CALIBRATION.md` (the measured key and the reading method).

Images: `bands3.py` (one 2x image per line, four overlapping quarters, into `img/lines/`),
`bandsi.py` (the same with tokens boxed and numbered, into `img/idx/`), `zoom.py` (any fraction
of a line at higher magnification), `sheets2.py` (tight-cropped cluster sheets), and the
first-session `bands.py`, `bands_gloss.py`.

Segmentation: `seg2.py` (regions hard-coded; writes `raince_tokens.json` / `raince_cipher.txt`
at 70 clusters and `raince140_*` at 140), `feats.py` (saves the per-token feature vectors),
`lineinfo.py` (token count and cluster ids per line).

Decoding: `lmns.py`, `lm.py` (language models; the `.pkl` files are not tracked — rerun
`python lmns.py`), `solve.py`, `solve2.py`, `solve3.py`, `solve140.py`, `render4.py`,
`render140.py`, `beam.py`, `htr.py`, `worddec.py`, `seg_words.py`, `qual.py`, `score_trans.py`.

Results: `map_lm.json`, `map140.json`, `draft4.txt`, `draft5.txt`, `draft5_seg.txt`,
`draft6.txt`, `draft7.txt`, `draft8.txt`; `trans/verified_lines.txt`,
`trans/p31_clear_close.txt`, and the first-session `trans/f29r.txt` and `trans/*_gloss_*.txt`.
Superseded by the key correction: `handmap.json`, `hand_decode2.txt`, `draft3.txt`,
`greedy70map.json`, `blind140_render.txt`, `hinit140.txt`.

`img/` holds Tomokiyo's two key images, `key_labelled.png`, `keyglyphs/`, `key_words.png` and
the cluster sheets `z70_sheet_*.png`. The page images (`../f2984/c*.jpg`, views 16, 17, 54) are
not tracked; re-fetch with
`https://gallica.bnf.fr/iiif/ark:/12148/btv1b90598430/f<n>/full/full/0/native.jpg`.

## Remaining gaps
- residual unresolved glyphs, ~13 % of letters, worst on p. 105 ll. 15-17, 20-21, p. 30 ll. 30, 32-34, p. 31 ll. 1-2, 17, 23-24 - blocker: illegible; every line was re-read from the image in session 3 (trans/reading_v3.txt); the remaining glyphs do not resolve on the B/W Gallica microfilm; colour photographs of pp. 29-31 and 105 needed
- two word signs absent from Tomokiyo's key: bold two-crossbar stem [X] (a person, follows 'son maistre') and ℓ° [Y] (name or title), ~4 occurrences each - blocker: open-codes; too few occurrences, no clear copy; the circled cross is now identified as i
## Escalation
- [x] siblings: clear duplicate of the 9 June letter (p. 17 ff.) and glossed leaves pp. 25, 41, 121-123 checked; no clear copy of 13 May or 20 Nov found
- [x] clear-pages: clear close of the 13 May letter on p. 31 transcribed (trans/p31_clear_close.txt); glosses on p. 29 ll. 1-13 and p. 105 top used
- [x] known-keys: Tomokiyo 1526 key re-measured (CALIBRATION.md); 1529 key noted as a different system
- [x] print: Mignet 1886, Bourrilly 1901, Tomokiyo, DECODE, Pastor IX (app. 38 = 26 Nov 1526 f.109, parallel wording, not this text) checked; Grethen 1887 not digitised anywhere found
- [x] key-rebuild: shape-constrained hill climb (solve140.py), per-token classifier htr2.py, 6-gram LM beam decode2.py
- [x] retry: session 3 re-read all 106 lines off the images (trans/reading_v3.txt); sense measure 0.476 -> 0.850
