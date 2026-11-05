# Gallica volume sweeps for unlisted cipher leaves, 1570–1620 (started 16 Sept 2026)

Goal: find cipher leaves in digitised BnF volumes that none of the standard lists (Tomokiyo, Schmeh, Dunin) carries,
and read them with the tools built for Ségur (mod-5 test, structured annealer) or with keys recovered from
contemporary decipherments in the same volume. Method as for 500 Colbert 401 (`../../targets/segur/`): IIIF canvases at 1400 px
(`fetch_vol.py`), 4-up contact sheets at 1000 px (`mksheets_vol.py`), read by eye.

## Volume selection

Gallica SRU (`sru_results.json`, queries on Colbert, Dupuy, Ségur, Navarre, chiffre, Villeroy, Bellièvre, Nevers,
ambassadeur 1575–1620; 1,097 + … records, 159 in range). Checked against Tomokiyo's pages (`src/*.txt`: bnf4715,
nevers, league, henryiii, henryiv, mayenne) so as not to redo his ground:

| Volume | ark | canvases | Tomokiyo? | decision |
|---|---|---|---|---|
| fr. 4715 "pièces originales, la plupart en chiffre, affaires de la Ligue" | btv1b52509819x | 202 | yes, `bnf4715.htm`, most items with decipherments; ff. 82, 84 solved by Lasry; f. 61 open | fetched for f. 61 (`f4715_full/`); not the sweep target |
| fr. 3995 "Recueil de chiffres avec leurs clefs 1580–95 (Nevers)" | btv1b525085665 | 285 | yes, `nevers.htm` catalogue | fetched as a key reference |
| **fr. 16127** ambassadors in the Low Countries 1571–94 (Mondoucet, Refuges, Blatier; Court minutes) | btv1b90609766 | 427 | **no** | **swept, see below** |
| fr. 15906 Bellièvre XVII, letters to Bellièvre 1581–82 | btv1b90643237 (1), btv1b9064322t (2) | 478 + 377 | ff. 759–781 only (Lasry) | swept 5 Nov 2026, see below |
| fr. 15900 (1) Bellièvre XI, letters from foreign sovereigns and their agents | btv1b525217736 | 900 | no | swept 5 Nov 2026: no cipher |
| fr. 15891 Bellièvre II 1578–85 | btv1b525218150 | 888 | no | swept 5 Nov 2026: no cipher |
| 500 Colbert 402 | – | – | – | not on Gallica (checked 16 Sept, `../../targets/segur/NOTES.md`) |
| Dupuy 407 | btv1b10035037p | 320 | – | read to canvas 46 in the Ségur session, chronological, clear; not resumed |

Gallica began refusing connections (WinError 10061) after five parallel fetchers ran for ~20 minutes; the fetchers
were killed. Resume one at a time with a pause.

## fr. 16127 (Harlay 228) — Mondoucet's cipher, 1571

Microfilm digitisation (black and white). Canvases 1–102 read on sheets (`sheets_btv1b90609766_1000/`).

* **ff. 7–8 (canvases 19–21): Mondoucet to Charles IX, Brussels, 29 August 1571.** Clear opening ("Sire, Vostre
  Majesté aura entendu par mon homme que j'ay depesché il y a deux jours toutes les particularitez des affaires de
  deça…"), then two and a half pages entirely in cipher: a mixed alphabet of letters, Arabic figures (4, 10, 16, 17,
  24, 25, 30…) and signs (crosses, barred letters, ∞-like loops), written continuously without word breaks. Signed
  "De Mondoucet".
* **f. 9 (canvases 23–24): "deschiffré de la précédente"**, headed "Chiffre", the contemporary clerk's decipherment in
  clear: "Hier matin Mons[eigneur] le duc d'Alve, qui est demeuré gouverneur, me vint trouver … la nouvelle qu'il
  avoit eue de l'exécution de [la] Sainte Ligue [?] … faire chanter un Te Deum solemnel … le duc d'Alve au camp …".
  (The Lepanto news? No: August 1571 precedes Lepanto; the "execution" is to be read.)
* Canvases 25–102: Refuges to the Queen and Anjou (27 Oct 1571, long, clear), Mondoucet to the King, Queen and Anjou
  (Nov 1571 – Apr 1572), the state of the Spanish garrisons (23 Nov 1571), copy of Philip II to Alba (Dec 1571,
  French and Spanish), all in clear. The Court minutes (canvases 15–17) are in a heavily abbreviated secretary hand,
  not cipher.

So the volume yields at least one cipher letter *with* its decipherment, which gives the key; whether it also holds
Mondoucet cipher passages *without* decipherment (the target) depends on canvases 103–427, not yet fetched.

Not on any list: Tomokiyo's pages mention Mondoucet only in a 1577 quotation from Catherine de Médicis about "le
déchiffrement de la lettre de Mondoucet"; fr. 16127 is not cited anywhere in them.

## Next (superseded, see below)

1. When Gallica answers: full-resolution IIIF of canvases 19–21 and 23–24; then canvases 103–427 sequentially.
2. Transcribe the decipherment (f. 9), align it to the cipher (ff. 7–8), recover the key (letters, homophones,
   figures for names and words).
3. Read any undeciphered Mondoucet cipher in the rest of the volume; controls as usual.

## fr. 16127 — full inventory of the cipher (17 Sept 2026)

The whole volume was read from the Gallica PDF export (1024 px pages, `pdf16127/`, `pdfsheets/`) after the direct
IIIF fetch was throttled; PDF page = canvas + 2. The volume is a Court file of the correspondence with Claude de
Mondoucet, agent in the Low Countries: his letters arrived in cipher and were deciphered on receipt, the decipherment
being filed on a following leaf ("deschiffré de la précédente") or, from 1573, written in the margin beside each
cipher block. Cipher letters and their decipherments:

| letter (Mondoucet → the King unless noted) | cipher | decipherment |
|---|---|---|
| Brussels, 29 Aug **1572** (archivist's "1571" is wrong: the letter is dated "ce xxix.me jour d'aoust 1572") | ff. 7–8, c. 2,700 glyphs | f. 9r–v, separate leaf. Alva's Te Deum for the "executions" of Paris; Aerschot left as governor |
| Brussels, 6 July 1572 | ff. 55–56, half the letter | marginal readings beside each block |
| Brussels, 13 July 1572 | ff. 60–61, c. 35 lines, entirely in cipher after the opening | **none** |
| Brussels, 16 July 1572 | ff. 62–63 | f. 64 |
| 17 Aug 1572 | ff. 65–67 | ff. 69–70 |
| camp before Mons, 4 Sept 1572 | (decipherment only) | ff. 72–73 |
| 6 Sept 1572 | ff. 74–75 | ff. 76–77 |
| 9 Sept 1572 | ff. 78–79 | ff. 82–84 |
| 11 Sept 1572 and the September–October 1572 series from the camp | ff. 85–…, several letters | each followed by its decipherment |
| Antwerp, 4 Jan 1573 | ff. 126v–127v, 39 lines | **none** (read in part 18 Sept 2026, `mondoucet/f1573/reading.md`) |
| Amsterdam, 9 Sept 1573 (not 5 Sept) | ff. 135r–137v | ff. 139r–141r, verbatim (aligned 18 Sept 2026) |
| 9 Sept 1573 (second letter, f. 142) | one page | f. 144 |
| 12 Sept 1573 | ff. 145–146 | f. 147 |
| 18, 19, 24, 29 Sept 1573; 1, 6, 13, 25 Sept 1574 | blocks of cipher inside clear text | readings in the margin beside each block |

The 1576 minutes of the King to Mondoucet (ff. 187–194) and Blatier's 1584 letters are in clear. So the volume holds
about twenty cipher letters in one system (letters, Arabic figures 4 10 11 16 17 24 25 30, and some twenty signs:
crossed x, triple bar, barred o, tall phi, dagger, looped l, lambda, double long s …), of which one long letter,
**13 July 1572**, has no decipherment anywhere in the volume, and two or three others need checking. None of this is
in Tomokiyo's, Schmeh's or Dunin's lists; Tomokiyo cites Mondoucet only in a 1577 quotation.

### Key recovery from the 29 Aug 1572 pair: negative so far

Full-resolution IIIF images of ff. 7–9 (`mondoucet/full_c019-024.jpg`, saved by Daniel when the fetch was throttled).
Two transcriptions of f. 7r: by hand at glyph level (`mondoucet/ct_c019.txt`, 1,227 tokens, 54 codes) and by
automatic segmentation and k-means shape clustering of all three cipher pages (`glyph_cluster.py`,
`all_clusters.txt`, 2,681 glyphs, 80 clusters, cluster sheets in `clusters/`). The decipherment f. 9r typed
(`pt_f9r.txt`, 1,215 letters). Alignment methods, each validated on a synthetic control built from the same
plaintext (homophones, 12–15 % nulls, 8–10 % token noise, word-codes): hard-EM Viterbi (`align_key.py`), consistency
beam search (`beam_key.py`), soft-EM HMM with banded initialisation and sharpening (`hmm_align.py`, control 44/44
symbols), and the same with word-signs consuming 2–10 letters (`hmm_align2.py`, control 56/58 letters, 7/10 codes).
On the real pages every method scores exactly at the shuffled-plaintext baseline (aligned fraction 0.51–0.56 vs
0.52). A blind French homophonic anneal of the hand tokens (`../../sp53/fasthomo.py`) gives no words.

What that excludes: a homophonic letter substitution with word-signs whose decipherment on f. 9 is verbatim, given
these tokenisations. What remains open: (a) the Court's decipherment is a paraphrase, as the 1819 Catinat
"traductions" were; (b) the cipher is syllabic or otherwise structured so that one glyph is not one letter; (c) the
glyph classes are noisier than the controls tolerate (the hand transcription lumps d-forms that the clusters split
three ways; the clusters fragment shapes so far that the sequence's index of coincidence, 0.016, falls below uniform).
The 1573–74 letters, where the reading stands in the margin beside each short block, are the cheaper test of (a) and
(b): a block of thirty glyphs against thirty letters of margin.

### 13 July 1572 (ff. 60–61), the target

Full-resolution images `full16127/c125.jpg`, `c127.jpg`; line strips `mondoucet/strips/c125_s*.png`. About 35 lines
of cipher after a clear opening ("Sire, encores que je vous aye faict une depesche de l'unziesme de ce moys assez
ample ... des propos que ces jours j'euz avec Monsieur le duc d'Alve, que ceux qui estoyent ... en ceste ville ..."),
and a clear close about the skirmish before Mons. Same glyph repertoire as the 29 Aug letter. Not attacked until a
key exists.

### The 16 July 1572 pair (ff. 62–64): verbatim, glossed, and still not aligned

f. 62r (canvas 129) carries the Court decipherer's own interlinear glosses above several cipher words ("pouvez", "leur
délivrance", "la bruslation", "nous maintenant", "au 30"), and f. 64 (canvas 133, "16 juillet 1572, déchiffré de la
précédente") gives the reading of the block in 17 lines, 863 letters (`mondoucet/pt_f64.txt`). The block is c. 26 lines,
1,149–1,191 glyph segments by the automatic segmenter (`joint_clusters.txt`, `joint2_clusters.txt`; the second run
attaches dots, apostrophes and bars to their letters, which removed only 6 % of segments). So the ratio is 1.3–1.4
glyph segments per plaintext letter on a pair that is verbatim where it can be checked, which means either a quarter
of the glyphs are nulls or letters are regularly written with more than one separable stroke. The validated aligner
(`hmm_align2.py`, one global null rate) scores this pair at the shuffled baseline (0.58 vs 0.57 aligned). A variant
with a learned per-symbol null rate, meant to absorb a dedicated null glyph, collapsed to all-null on its own control
(0/58) even with the plaintext forced to be consumed, and was discarded; the file on disk is the validated version.

### Where this stands (17 Sept 2026)

Found and inventoried: an uncatalogued cipher corpus, Mondoucet's despatches from the Low Countries 1571–74 in
BnF fr. 16127, about twenty letters in one system, most with the Court's decipherment, one long letter of 13 July 1572
(ff. 60–61) and possibly two others without. Not read: the key. Three transcriptions (hand, two automatic) and four
alignment methods, each proved on synthetic controls, all sit at baseline against two decipherments that are
demonstrably of the right letters and, for 16 July, glossed word by word by the decipherer. The remaining explanations
are (a) the cipher writes many letters with two or more separable glyphs (the 1.3–1.4 ratio), so that the unit of
substitution is not the connected component; (b) the decipherments abridge, as the 1573 marginal readings visibly do
(f. 161: 15 lines of cipher against 12 short marginal lines); (c) both. The way through is the one that worked for
Feuquières: hand-anchoring, starting from the glossed words on f. 62r (the glyphs under "pouvez", "leur délivrance",
"la bruslation" give a dozen letters at once), then carrying letters into the 16 July block and from there to 13 July.
That is a day of careful work at the strips already cut (`mondoucet/strips/c129_s*.png`, `c125_s*.png`), not a
computation, and it was not started.

Other volumes from the selection (fr. 15906, fr. 15900, fr. 15891) were not swept: their downloads were killed with
the throttling and not resumed.

### SOLVED, 17 Sept 2026 — 13 July 1572 (ff. 60–61)

The key was recovered by the hand-anchor route the NOTES above prescribed, and it reads the target. Steps:
(1) hand-transcribe the 16 July block at glyph level (`hand/ct_f62.txt`, `hand/ct_f62v.txt`); (2) anchor on
the f. 62r interlinear glosses ("pouvez", "leur délivrance", "au 30") and the verbatim f. 64 reading; (3)
anchored HMM alignment → homophone counts (`hand/anchor_align2.py`, `hand/key2.json`, `hand/key_counts.json`);
(4) beam decode with a 16th-c. French 5-gram model (`hand/lm_decode.py`, width 300).

The 1.3–1.4 glyph/letter ratio was a **segmenter artefact**, not nulls or multi-stroke letters: at glyph level
one glyph = one letter. Nulls are a small set {*, C, mq, j} plus low-rate per-symbol nulls. This is why every
automatic aligner sat at baseline — the segmentation, not the model, was wrong. Transcription by hand, budgeted
not automated, was the way through, exactly as the goal directed.

**Control (decisive):** decoding the 16 July block with this key reproduces the decipherer's own gloss verbatim,
line 22 = "...leur delivrance des espagnols a ce moyen...", matching the f. 62r gloss and the f. 64 reading.

**The 13 July despatch is partly enciphered**: clear-text bands carry the narrative (f. 60v C3–C7: Spanish troop
counts "troys mil hommes de pied & cinq cens chevaux" at Mons, German regiments at Maastricht "nouvellement leuez";
f. 61r sign-off "De Bruxelles ce [Ve] jour de Juillet 1572 / de Mondoucet"), and 22 + 1 + 6 cipher lines
(J1–J22, K1, M1–M6) decode in stretches: religieuse, Espaigne, saint père, Escosse, troupes de terre, le pape,
Angleterre, catholique, ministres, liberté, "le prince... service du roi", "parenté entre les autres cour[s]",
"avaient esté capitulé". Full reading in `reading.md`; consolidated output `hand/decode_all.txt`.

Catalogue entry 1 moved from open to resolved (**read**). Remaining: `\todo` fills and DECODE registration are
Daniel's steps; HistoCrypt 2027 draft to write in `papers/histocrypt/`.

### 1573 leaves, catalogue entry 2 (18 Sept 2026)

Which passages lack a reading, fixed by transcribing and aligning rather than by eye: **9 Sept 1573** (cipher ff.
135r–137v, not ff. 138–140) has a complete, literal decipherment on ff. 139r–141r: 4,735 glyphs aligned letter for
letter (ratio 0.91, only word signs unaligned). **4 Jan 1573** (ff. 126v–127v) has none; ff. 124–125 decipher the 5 Dec
1572 letters. With the 1573 key from the 9 Sept alignment the 4 Jan cipher reads in stretches (about two-thirds; held-out
control 77 % letters; the Court's gloss "hambourg" decoded in place). Full account `mondoucet/f1573/reading.md`.

## Bellièvre volumes fr. 15906, 15900 (1), 15891: swept 5 Nov 2026

All canvases fetched through openapi.bnf.fr at 800 px (`fetch_openapi.py`; gallica.bnf.fr/iiif 403s scripts): four
arks, 2,643 canvases. fr. 15906 is split in two arks, **btv1b90643237 = fr. 15906 (1)** (478 canvases, ff. 1-434) and
**btv1b9064322t = fr. 15906 (2)** (377 canvases, ff. ~322-782); both are microfilm shot as two-page openings.
fr. 15900 (1) is btv1b525217736 (900 canvases); **fr. 15900 (2)** (letters to Bellièvre 1599-1607, chronological) has
no Gallica ark (archivesetmanuscrits notice cd0e3981) and was not swept. fr. 15891 is btv1b525218150 (888 canvases).
Contact sheets (`sheetN.py`: 3x3 at 420 px for single pages, 2x3 at 640 px for openings) were read by screening
agents to the brief in `SCREEN_BRIEF.md`, each flag checked on the 800-px canvas; results per batch in
`screen_<vol>_<a-f>.txt`. An ink-fraction filter (`ink.py`) was tried to skip blank pages and dropped: it skipped
faint-ink letters. The BnF item-level inventories are saved in `bellievre_inventory.txt`; none flags cipher except
Entragues.

Yield: one new cipher item, and the known Entragues letters.

* **fr. 15891** (Bellièvre's own minutes and letters 1578-85, Low Countries, Guyenne, Navarre): no cipher. Minutes
  are written in clear; the only figures are article numbers and sums.
* **fr. 15900 (1)** (letters from sovereigns and agents 1596-1605: Clement VIII, cardinals, Tuscany, Malta, Spain,
  England, German princes, Netherlands, Swiss cantons): no cipher.
* **fr. 15906 (1)** (letters to Bellièvre 1581): no cipher. The Henri III / Catherine / Anjou letters were opened at
  800 px; at that size one page of an opening is ~300 px wide, so a block of signs shows but a single cipher word
  inside a line may not. Pages too faint to read at 800 px are listed in `screen_15906_d.txt`.
* **fr. 15906 (2)**: ff. 759-761 and 780-782, d'Entragues to Saint-Aignan with the "Copie d'une cifra trouvée" key on
  f. 761 and the summary slip on f. 782, all glossed: George Lasry's item (`targets/entragues1581/`), excluded.
  **ff. 520r-522v: Henri III to Bellièvre and Villeroy, Ollainville, Friday 21 Oct 1580**, countersigned Pinart, the
  new item (below).

### Henri III to Bellièvre and Villeroy, 21 Oct 1580 (fr. 15906 (2), ff. 520r-522v)

Canvases 92-95 of btv1b9064322t; full-resolution openings saved as `bellievre_hi/a_c092.jpg`-`a_c095.jpg` (9,700 x
6,460 px). The letter, written while the two were going to assist Anjou in the peace negotiation with Navarre (the
peace of Fleix, 26 Nov 1580), has four cipher passages in one system of invented signs (Greek-like and barred
letters, phi/psi/sigma shapes, '#'-like crossed strokes, a few figures such as 14 and 18):

| place | extent | decipherment |
|---|---|---|
| f. 521r, lines 2-8 | 7 lines, ~330 signs | complete, in the left margin ("que je ne pesseray pas que le sr de la Rochepot se puisse loger avec ses troupes du costé de Cambray ... bien pourrez dire") |
| f. 521v, upper | 2 lines | in the margin ("je croy qu'ilz n'y ont ny l'un ny l'autre aucune volunté", on Anjou's marriage) |
| f. 521v, middle | 13 lines | in the margin (Portugal, Labadie, Elizabeth's forces, Strozzi, the English ambassador's audience), breaking off at "pour elle et pour moy d'aultant" |
| f. 522v, postscript after the signature | **17 lines, ~750 signs** | **none on the leaf** |

The postscript ends in clear "... a Dolinville ..." and is signed Henry / Pinart. The glossed blocks, about 900
letters of known plaintext, give the key for it. The sibling Godefroy 260 f. 52 (Henri III to the same two,
Ollainville, 30 Oct 1580, partly ciphered, catalogue #1185, not online) is probably in the same key.

Edition. *Lettres de Henri III*, t. V (ed. J. Boucher, Société de l'histoire de France, 2000), **no. 4006, p. 110**,
prints this letter as an analysis with quotations, source "ms. fr. 15906/2, fol. 520-523: orig.", and a note that
the original has "passages chiffrés. Le résultat du déchiffrement y a été porté en regard". Read through Google Books
snippets only (gdata feed `gb_feed.py` and the new Books interface in Chrome; books.google.fr shows a CAPTCHA). The
analysis quotes the marginal decipherments, then a phrase not in any margin seen ("... guerre sur les bras a quoy je
veulx bien penser avant que d'entrer en aucune chose qui me puisse nuire"), and ends: "Enfin le maréchal de Biron veut
se mêler du rétablissement de la paix en France. Des consignes sont données ici à Villeroy pour qu'il écrive au
maréchal. (Pinart.)" The edition says "post-scriptum" where a letter has one (four hits in the volume) and does not say
it for no. 4006, and the clear text of ff. 522r-v speaks of Biron only as sending news. So the last sentence may
summarise the cipher postscript, which would mean its content was known to the editors.

**Key test (5 Nov 2026), and the lead closed.** A substitution key was rebuilt from the glossed f. 521r block (the
decipherer wrote "escripte" over its signs; the rest aligned to the margin) and the postscript read in part
(`bellievre_hi/ps1580/report.md`, `key.json`, `ct_ps.txt`). The system is a homophonic letter substitution with word
signs and number codes. The postscript tells of Marchaumont and Anjou's wish to send troops toward Cambrai and seize
Le Catelet, the king's "je veulz y penser avant que d'entrer en aucune choze", and then the peace, with Villeroy to
write to the man "que j'ay employé aulx aultres paix" (code 10) to learn whether he wants to take part or to
obstruct. That is the end of the edition's analysis of no. 4006, quotation included, so the editors had the
postscript deciphered: the item is closed as read (edition), lead in `candidates.json`. The partial key fits the
sibling Godefroy 260 f. 52 (catalogue #1185), which the same volume prints as "31 octobre, Ollainville" (Portugal,
don Antonio; "en partie chiffrée"); noted on #1185.

Result of the sweep: no open cipher in fr. 15906, 15900 (1) or 15891. Still unswept: fr. 15900 (2) (no ark), and the
other Bellièvre volumes fr. 15890, 15892-15905, 15907-15911 (fr. 15905 holds Catherine's 1580 letters to Bellièvre).
