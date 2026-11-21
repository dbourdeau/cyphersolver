# Sforza chancery letters in cipher, ASMi cart. 1598 and 1591 (catalogue 1311; DECODE R5297-R5298, R5476-R5587)

Status: in progress. Triage done and catalogue 1311 split into sign families, ids 2628-2645 (14 Nov 2026); nothing read yet. Sibling of catalogue 1310 (`targets/sforza1597`).

## Fetched (14 Nov 2026, DECODE cookie, `fetch_all.py`)
203 records in `list1598.json`: 110 letters (record_type 1) and 93 key sheets (record_type 2). PDFs in `pdf/`, renders in
`png/`, contact sheets in `sheets/` (`sheets.py`); all git-ignored.

## What the letters are
Not one cipher. The 133 letter pages show many hands and sign families, as in cart. 1597:
- Geometric/cursive sign alphabets without word division (R5488, R5509, R5519, R5524, R5529 ...), the R5464-type homophonic letters.
- Clear letters with cipher passages (R5485 "Capo de Cremona", R5492, R5510, R5522, R5534 ...): these clear contexts are cribs.
- R5482: a code. Capital letter + superscript number (L^2, H^30, A^13, M^2, e^39, Z^19, N^17 ...) mixed with single signs and
  ligatures; signed "Idem". Needs a codebook; repetitions (H^26, A^11, A^13, M^2, L^3) are frequent.
- Several leaves are nearly all clear (R5481, R5489, R5494, R5530) or wrappers (R5490 p.2, R5512 p.2).

## 14 Nov 2026: split into sign families (`split1311.py`)
Top 3-4 lines of every letter rendered at 110 dpi (`strips.py`, sheets `strips/f00-f10.jpg`, git-ignored) and grouped by sign shapes by eye. Catalogue 1311 retired; 18 entries promoted:

| id | fam | DECODE records | hand |
|---|---|---|---|
| 2628 | A | 5488, 5528, 5579, 5581 | geometric T, III, infinity, U |
| 2629 | B | 5562, 5572, 5573, 5575-5577, 5586 | x, double-cross, 3, barred m, pp, k |
| 2630 | C | 5502-5506, 5514, 5515, 5517, 5518 | numerals 4/6/8 + crosses; clear phrases between runs |
| 2631 | D | 5495-5499, 5507 | lambda, 3, bz, L-dot, ooo |
| 2632 | E | 5520, 5523, 5535, 5537, 5541 | m-divide, infinity, pi, barred P |
| 2633 | F | 5555, 5556, 5559, 5563 | v, divide, infinity, plus |
| 2634 | G | 5516, 5519, 5522 | x, 4, 3, theta, lambda; clear passages |
| 2635 | H | 5551, 5561 | cursive ml, z3o, // |
| 2636 | I | 5500, 5553 | pseudo-Latin a b f |
| 2637 | J | 5490, 5493 | pseudo-Latin bz, rb, Z |
| 2638 | K | 5511-5513 | numeral-like 7, 5, 3, 9 |
| 2639 | L | 5564, 5565, 5582-5584 | ta, delta, square, Afk |
| 2640 | M | 5486, 5487, 5530 | bz, inverted T, infinity, lambda |
| 2641 | N | 5568, 5574 | hash, 8, inverted T |
| 2642 | O | 5524, 5529 | V, hash, 8, barred p |
| 2643 | P | 5521, 5542 | to, delta, 3n, qo |
| 2644 | Q | 5482, 5485 | code: capital + superscript number |
| 2645 | Z | 38 singletons | unmatched hands, many with clear context |

Clear or nearly clear leaves, left out: R5481, R5483, R5494, R5525, R5552, R5557, R5566, R5569, R5578. Families are by eye on strips, a proxy for keys; they may merge or split once key sheets are compared. The first split attempt was written into the stale shared checkout (ids 2464-2481) and reverted before commit; the committed ids come from origin/main (a second clash on push moved them from 2575-2592 to 2628-2645).

## Next steps
1. Largest family first: C (9 letters, clear phrases as cribs), then B and A.
2. Match families against the 93 key sheets of this box and the 115 of cart. 1597 (`keycols.py` in sforza1597).
3. Run the sforza1597 chain (signreader + CTTS + keyrefine) on the largest clean family.

## Remaining gaps
All letters unread; no key matched yet. Blocker: none external; work not yet done.

## Escalation
Not started beyond triage (siblings: cart. 1597 keys; clear passages as cribs).

## 14 Nov 2026: family C (id 2630), first solver pass, no signal
Nine letters (R5502-R5506, R5514, R5515, R5517, R5518; 12 pages) extracted from the PDFs at native resolution (about 1,750 px wide) to `famC/`
(git-ignored). Sign reader copied from sforza1597 (`signreader.py lines` + `extract2`, SR_SENSITIVE, block 41, C 12, big area 100): 16,055 glyphs on
374 lines. `f2tokens2.py` Ward clustering, CTTS headless (period Italian corpus `lm_qc`, n-gram 5):
- 60 clusters, 4 homophones, 300 s: 7.31 M against 6.48 M shuffled (ratio 1.13).
- 35 clusters, 3 homophones, 240 s: 7.45 M against 6.86 M shuffled (ratio 1.09).
Decryptions are letter salad. R5464 in cart. 1597 gave 1.67 with the same chain, so this is a failure of the reader, not evidence against Italian.
Why: the letters interleave clear Italian/Latin (salutation "Illustrissime princeps", "quando", "sempre quella"), which the reader cuts into
glyphs too; the signs are 12-18 px tall; and dotted signs (p with a raised o, o-dot-o, x with a dot) split into pieces.
Seen by eye on R5518 at 2x: the alphabet is small and legible (o, inverted T, +, 6, 8, 1, 9, 2, z, 3, p, raised-o p, x, crossed stroke, f, v, T, t, d,
long s, o-dot-o, / ), with some word spacing. A hand transcription is workable: R5518 (15 lines, about 500 signs) first, clear words marked
as cribs, then extend to R5514/R5517.

## 14 Nov 2026: R5518 transcribed by hand, family C key partly recovered (ciphertext only)
`famC/hand/r5518_hand_v2.txt`: R5518 (cart. 1598 no. 44, 11 lines of cipher after the clear opening "Illustrissime princeps et ex.me domine";
a clear phrase "quando ... la V.ra Ill.ma Sig.ria" in line 2), 563 signs, about 36 sign types, read from 3x crops of each line.
v1 (`r5518_hand.txt`) merged three signs as one q and lost the line beginning with the crossed stroke (a comment filter); v2 splits
q / h (hooked, like a turned y) / y (open reversed 9) and restores the line.
CTTS headless (period Italian corpus, n-gram 5, up to 4 homophones, 300 s), shuffled-token control each time:
- v1 (506 signs): 16.90 M vs 11.75 M shuffled (1.44).
- v2 without the lost line (506): 19.02 M vs 12.72 M (1.50).
- v2 full (563): 18.60 M vs 11.97 M (1.55); two seeds give the same key (`famC/hand/v3a.txt`).
Key (homophonic, about 2 signs per vowel): + T = a; z w = a; 1 = c; v = d; 2 d f = e; e = f; 3 = g; h = m; u = m; q = n; S = n; 6 = o; l t = o;
# = p; 7 = q; L = r; 8 R = s; P m = s; b = t; c = t; r = b; - 4 X Q = i; o y = u/v; p = l. The ct sign is a cipher sign here (t), not the clear "et".
Readable stretches in the decryption (spelling of the chancery, u/v merged):
- l. 9 "mente adoperarme in bene[f]icio del vostra stato ... subito"
- l. 10 "de cio avisarme"
- l. 8 "in ordine ... fornire de le cose necesvrae (necessarie) e acio ..."
- l. 6 "... pericvla ... come poria ..."
- l. 5 "... in qviesto paese per cvrestia (carestia?) ... de ogni [a]ltra cosa sia"
- l. 3 "... la cosa ... conclusione ... aspecto"; l. 7 "... electione del ..."
Lines 1, 2, 4 and 11 do not read yet. Known problems: the o sign takes u in "qviesto" but a in "ogni altra" and "carestia", so it is
probably two signs (plain o and o with a top stroke, written "o -" in places) merged; + and t may be confused; e is f in "beneficio" and
"fornire" but the solver flips it to d. Status: R5518 read in part (estimate: about half the text in words; not yet measured), key from the
ciphertext alone. Next: re-check o / o-with-stroke and + / t on the image, fix the key by hand from the cribs above, then decrypt R5514
and R5517 (same family) with this key as the check.

## 14 Nov 2026 (later): R5514 transcribed, joint solve with R5518 reads in long stretches
`famC/hand/r5514_hand.txt`: R5514 (cart. 1598 no. 40), 26 lines, 1,853 cipher signs, with long clear passages left out ("che merita
possuto io fare cosa alcuna che fosse grata a la V.ra Ill.ma Sig.ria ...", "a qual cosa prego cum ogni instantia ...", "a qual cosa
racordo", "prego La V.ra Ill.ma S.ria voglia"). New sign O (o with a top stroke) kept apart from o here (R5518 v2 still merges them).
Joint CTTS run on R5518 + R5514 (`tj.txt`, 2,416 signs, 400 s, two seeds agree): 17.46 M against 8.67 M shuffled, **ratio 2.01**.
Decryption with the solver key and r = b: `famC/hand/dec_joint.txt`. Share of letters in dictionary words of 4-12 letters (greedy, period
corpus): R5518 0.39, R5514 0.51, shuffled-token control 0.23 (so roughly 15-30 points of real words; far from the read bar).
R5514 stretches that read (u/v merged, chancery spelling): "la qual cosa grandemente me sto ... per adoperar ben del vostro stato",
"... a roma ... castro ... el quale a posto", "la civita di ... a cremona", "... in questa ... nel paese ... per persone inteligenti",
"... secreti ... ", "risposta ... scrito", "secreto ... seguire", "per le ... scrito ... scrivere", "a la cosa", "lo vostro stato".
Key changes from R5518 alone: r = b (was c), the theta sign reads f in "beneficio"/"fornire" but t in "scrito"/"secreto": probably two
signs (barred o and theta) that the transcription merges; same for o / O in R5518.
Status: family C read in part (R5514 and R5518), key recovered from the ciphertext alone; not yet at the read bar.
Next: (1) split theta and o/O on the images of both letters; (2) hand-fix the key from the word stretches; (3) transcribe R5517 and
R5515 and decrypt them with the fixed key as an out-of-sample check; (4) then R5502-R5506 (two-page letters).

## 14 Nov 2026 (later still): R5517 transcribed; the key reads it out of sample
`famC/hand/r5517_hand.txt`: R5517 (cart. 1598 no. 43), 33 lines, 1,698 cipher signs, clear passages left out ("Spero pure che sera
tanta la benignita et clementia de la V.ra Ill.ma Sig.ria", "questo sia cusi ma non se retrovera mai ...").
**Out-of-sample test**: R5517 decrypted with the key solved on R5518 + R5514 only (`ja.txt`, r = b), no re-solve: dictionary-word share
0.40 (shuffled control 0.23), and it reads: "la impresa de urbino" (twice), "lo mio cancelliero" (three times), "conte Iacomo",
"risposta", "delibero", "regimenti", "pratica", "provisionata", "Francesco", "la vostra signoria". The key generalises to a letter it
was not fitted on, so it is a real key, not an artefact of the solver.
Joint solve of all three (`t3.txt`, 4,114 signs, 480 s, two seeds agree): 16.70 M vs 8.04 M shuffled (2.08). Word share R5518 0.42,
R5514 0.48, R5517 0.42 (`dec3.txt`); the joint key changes a few rare signs (w, q, c, u) without raising the share.
Context from the text: Conte Iacomo (Jacopo Piccinino?) and an "impresa de Urbino", with the writer's cancelliere going back and forth:
the 1460s Sforza-Piccinino-Montefeltro politics are a candidate setting; not checked against dated letters.
Remaining: theta and o/O splits, + / t, the rare signs; R5515 and R5502-R5506 not transcribed; no clear-text decipherment checked.

## 15 Nov 2026: key corrected by hand, with R5517 held out
Objective: word-segmentation log-probability of the decryption (period Italian corpus, unknown letter -14), fitted on R5518 + R5514,
checked on R5517, which no change was chosen on (`famC/hand/refine.py`, `try1.py`).
- Blind coordinate ascent (`refine.py`) raised both scores but broke real words ("pigliato" -> "pidliato", "qvale" -> "ivale"): the
  model penalises rare letters, so it pushes b, g, q signs to common letters. Rejected; every change below was checked in context.
- Kept against the model: 7 = q (questo, quale, quanto), r = b (beneficio, subito, urbino), 3 = g (grandemente, pigliato).
- Changed: o = a (was o; "la qual cosa", "ogni altra", "carestia", "impresa"; in R5518 the o-with-stroke sign O = u was merged into o),
  - = e, w (o-dot-o) = i, t = o, c (ct sign) = i. theta stays t: e = f lowers both scores, so "beneficio" / "fornire" show a second,
  not yet separated sign.
Scores (train / holdout): solver key -8020 / -6760; hand key (`key_h2.json`) -7704 / -6335. Word share (4-12 letters): R5518 0.43,
R5514 0.50, R5517 0.43 (was 0.40; shuffled 0.23). Decryption: `famC/hand/dec_h2.txt`.
R5517 under the hand key, examples: "la impresa de urbino", "deliberato ... la vostro signoria", "lo mio cancelliero ... conte Iacomo",
"per la via de ... pratica", "regimenti", "rispondermi", "mandato a dire", "provisionata". R5514: "la qual cosa grandemente me ...
per adoperar ben del vostro stato", "in questa ... nel paese ... per persone inteligenti", "a roma", "castro", "a cremona".
Limits: the gain is small (holdout share +3 points); what remains is in the transcription (theta / barred o, + / t, rare signs, merged
o / O in R5518), which needs another pass on the images, not more key search.

## 15 Nov 2026 (later): sign re-check, ligature signs
In the 3x crops, two things typed as two tokens are one sign: "- T" (a bracket sign with a lead stroke, 18 times) and "- e" / "e -"
(a barred o whose bar runs out both sides, 8 times). `t4.txt` writes them as D1 and E.
- Joint CTTS on t4 (480 s): 16.82 M vs 7.97 M shuffled (2.11; t3 gave 2.08). The solver gives D1 = x (a rare-letter slot, i.e. unplaced).
- Hand test with the segmentation score (train / holdout; t3 hand key -7704 / -6335): D1 = a -7683 / -6275, D1 = la -7685 / -6314,
  D1 = e -7679 / -6303; E = t, e or s about equal, E = f worse by about 30 on the holdout. Kept D1 = a, E = t (`key_h3.json`, `dec_h3.txt`).
  Contexts favour a word sign ("per esser [D1] piu debile", "altra cosa sia [D1]"), so "la" stays possible.
- The f in "beneficio" (R5518 l. 9) is, on the crop, the long-barred o; the plain theta reads t in "scrito", "secreto". The hand
  transcription did not mark the two shapes consistently, so the split cannot be scored from it. Word share unchanged (0.43 / 0.50 / 0.43).
What it needs: a box-level transcription (each sign with its position, CTTS-style) so the theta shapes, + / t and o / O can be
relabelled from the image and re-scored; a by-eye re-read of whole letters is not precise enough for these look-alikes.

## 15 Nov 2026 (later): box-level transcription by alignment, failed
`famC/hand/align.py`: the hand tokens of R5518, R5514 and R5517 aligned line by line (DP, costs re-estimated from token-cluster
co-occurrence over four rounds, line correspondences fixed by hand from the crop positions) to the signreader v2 boxes (60 shape
clusters). 3,063 of 4,114 tokens get a box. Checked with montages of the box masks (`montage.py`): of 52 barred-o tokens about 4 boxes
show a barred o; of 60 sampled "6" tokens about 6 show a 6. The detector splits and merges signs (12-18 px tall, ligatures, dots) too
often for a token sequence to align to it, so the boxes cannot be used to relabel look-alikes. Not repeated with other settings: the
detector itself is the limit, as on R5464 (sforza1597).
Routes left for the theta / + vs t / o vs O splits: (a) a second by-eye pass over the 3x crops with a strict legend for these shapes
only; (b) a human CTTS session drawing boxes; (c) higher-resolution images from ASMi (`../sforza1597/asmi_request_draft.md`, unsent).

## 15 Nov 2026 (later): second pass by eye on the look-alikes
Note: R5514 has 27 transcription lines (its l. 15 is split around a clear passage), so the train / holdout cut is after line 38 of
t3-t7, not 37 as in the earlier scores; scores below use the corrected cut and are not comparable with the earlier ones.
- o with a right tail: on 4x crops of R5518 the "o -" pairs are one sign, the O of R5514/R5517 (o with a tail). Merged 7 times (`t5.txt`).
  O = v stays best (-7920 / -6000 against -7954 / -6004 unmerged).
- Barred o: two shapes, plain (bar inside the o, e) and long-barred (bar out both sides, E). Re-read R5514 ll. 4, 10, 15, 24, 25 on the
  crops (`t6.txt`) and R5518 l. 9 ("beneficio": long-barred, `t7.txt`). E = f by context ("a haver fare", "spero ne faro seguire",
  "beneficio") although the segmentation score prefers t or e by 20-30 (it under-rates f); plain e = t ("scrito", "aspetto", "civita").
  "fornire" (R5518 l. 8) and "Francesco" (R5517) also need f; their shapes were not re-checked. Key `key_h4.json`, decryption `dec_h4.txt`.
- Word share (4-12 letters): R5518 0.439, R5514 0.498, R5517 0.425; before this pass 0.430 / 0.501 / 0.427. Flat.
Reading of the result: the look-alikes were not what holds the share near 45 %. The decryptions read in phrases but most lines still
have unread stretches between them; the likelier causes now are word signs and syllable signs in a nomenclator part (the "-T" sign looks
like one), misread rare signs, and the 1-in-10 transcription errors a by-eye reading leaves. Next options: list the frequent unread
cipher strings and test them as nomenclator entries; or get the ASMi images and re-transcribe.

## 15 Nov 2026 (later): nomenclator test, no signal
`famC/hand/nom2.py`: decryption (`key_h4`, `t7`) masked by a maximal cover with dictionary words of 4-12 letters; per-sign unread rates
and recurring unread cipher n-grams. Worst signs: c (ct sign) 70/80 unread, q 67/77, P 51/62, u 19/21, l 25/28, w 41/55, Q 23/30,
D1 16/18, m 25/29. Recurring unread pairs are mostly doubled or vowel pairs ("2 o" 17/18, "o o" 14/16, "6 6" 11/14, "c X" 12/15).
`nomtest.py`: each bad sign set to null or to each single letter, scored on train (R5518 + R5514) and holdout (R5517): null never helps;
best single-letter moves are small (c = t +53 letters in words, r = t +33, of about 4,100).
`nomtest2.py`: each sign set to word or syllable values (che, et, per, con, non, de, la ...): every sign gains with "non" / "con" (+50
to +210), including r, which is b on sure words (beneficio, subito, urbino). The cover metric rewards any value that makes 4-letter
words, so it cannot tell a code sign from a letter sign; no sign stands out above that baseline. Not adopted.
So the nomenclator question stays open: it needs a test that compares against a frequency-matched control sign, or cribs from the
clear text and the history (names: Iacomo, Urbino, Francesco, Roma, Cremona, Castro), or a contemporary key sheet. The 93 key
sheets of cart. 1598 are still uncompared with family C; that is now the strongest lead: a sheet whose signs match family C would
give the nomenclator directly.

## 15 Nov 2026 (later): key sheets compared with family C, no match
Family C test values (key_h4): + T = a, 2 = e, 6 = o, 4 X = i, L = r, S q = n, 8 = s, b = t, # = p, 1 = c, v = d, p = l, h = m, 7 = q, r = b, 3 = g.
- cart. 1598, all 93 key records (`keysheets.py`, contact sheets `sheets/k00-k04.jpg`, top strips `sheets/kt00-kt07.jpg`): most are
  16th-18th-century numeric or syllabic codes. Sign alphabets close in style, checked at full size: R5245 (a = +, but o = 4, i = e-hook),
  R5255 (+ = e, crossed stroke = a), R5475 "Vincentius / Nicola Guarna" (a = +, but b = 6, o = q), R5265, R5266, R5240, R5243. None fits.
- cart. 1597, all 115 key sheets (sforza1597 `sheets/k00-k22.png`): none has a = +, e = 2, o = 6, i = 4. Close in style: R5346
  (a = +, but m = 6, o = m), whose "nichil importans" list includes the ct sign, which fits family C's ct sign hardly ever sitting
  inside a word (70/80); Antonius M., Lancelotus de Figine, Petrus de Monteferrato and Ottone del Carretto keys are different alphabets.
Conclusion: the family C key is not among the 208 key sheets of cart. 1597/1598. Many keys of the period start a = + (the chancery
habit), so the style is shared, not the key. The reading rests on the key recovered from the ciphertext alone.

## 15 Nov 2026 (later): R5503 transcribed; the key reads it out of sample
R5515 (the next shortest) is too faint on the DECODE scan to read sign by sign; R5503 is sharp and was taken instead.
`famC/hand/r5503_hand.txt`: R5503 (cart. 1598 no. 29), 34 lines, 1,551 cipher signs, clear passages left out ("bon cavalero ...",
"Lo cardinal mio ...", "in verita me sforzaro", "cum ... certamente ...", "Como mio ...", "lo cardo ... la V.ra Ill.ma Signoria",
"non mora ...", "Como commandamento lo dicto ...", "per bona informatione"). Lower confidence than R5514/R5517 (lighter ink).
Decrypted with `key_h4.json` as fitted on R5518 + R5514, no re-solve (`dec03.txt`): **word share 0.471 against 0.143 for the same
signs shuffled**: the best letter so far, and out of sample. Phrases: "grandisime", "bene", "a darlo", "quattrocento", "potese",
"altri non veritate", "grandisima ingratitudine", "la mia compagnia", "per merito di boni servitori", "bisogna me dormire a provedere",
"certamente", "servicio", "fortificarse de altre gente", "a fine de fare", "la vostra illustrissima signoria", "per lo diavolo",
"terminato di pigliare bataglia", "lo tempo", "per servire", "pare se me bastaria l'animo de fare", "la risposta",
"conte Iacomo", "sempre", "acampo a Castiglione", "cinque milia persone utile", "questi designi", "facendo", "la impresa",
"debilitar", "bastie seria facilisima obtenere", "grandi benefici", "destruttione", "de ognia pensero", "sigillate le mie litere del
mio sigillo", "maravigliate". The setting (conte Iacomo, an army camped at Castiglione, bastie, 5,000 men) fits Jacopo Piccinino's
campaigns of the 1450s-60s; not checked against dated sources.
Status: family C read in part on four letters (R5518, R5514, R5517, R5503), one key recovered from the ciphertext alone and
confirmed on two letters it was not fitted on. Next: R5502, R5504-R5506 (two-page letters, sharp scans).

## 15 Nov 2026 (later): R5502 transcribed; out of sample again
`famC/hand/r5502_hand.txt`: R5502 (cart. 1598 no. 28), 42 lines, 2,011 cipher signs, clear passages left out ("Spero ...", "recordo a la
V.ra Ill.ma S. Signoria", "senza fallo la V.ra Ill.ma Signoria ... deve rendere certissima", "non ... forsi la cosa como mi e stata
porta ...", "Et sia como se voglia ...", "sinceramente a la V.ra Illustrissima Signoria"). Decrypted with `key_h4.json` (fitted on
R5518 + R5514), no re-solve (`dec02.txt`): **word share 0.461 against 0.140 shuffled**. Phrases: "li vostri ... lo ... questo ...
mandato", "a persuadermi", "lo mio ... certo", "per esser ... voluntade", "la compagnia ... la mostra", "quante volte e per quante vie
... ho pensato", "e cercato ... tutto lo stato", "per la quale", "certo sera vincitore", "rispondendome presto", "questa intencione",
"lo conte Iacomo pigliando ... sentendo", "risposta", "disputacione ... argumenti me pare", "mandare", "per la copia ... conclusa",
"parlare ... Lodovico", "el quale ... la Mirandola ... a cercare", "proveditori", "questa impresa li fratelli", "la questione",
"per la ritornata de ser Cristoforo", "el quale per intendere tutto fo mandato", "lo vostro", "de tutta Italia", "subito", "la spada",
"el quale ... de corte", "a dare ... adaptare la trama", "mandando copie".
Family C now: five letters (R5518, R5514, R5517, R5503, R5502; 7,676 cipher signs), one key recovered from the ciphertext alone and
confirmed out of sample on three letters (0.42, 0.47, 0.46 word share; shuffled 0.14). Read in part, not at the read bar.
Remaining in family C: R5504-R5506 (two-page letters), R5515 (scan too faint).

## 15 Nov 2026 (later): R5506 page 1 transcribed; out of sample again
`famC/hand/r5506_hand.txt`: R5506 (cart. 1598 no. 32) page 1, 23 cipher lines, 1,034 signs (page 2 not transcribed). Clear passages
left out ("Lo signor Cavalero a Bersana la Sig.a del duca de Modena voglia ...", "Questa matina ... risposta ... mandato", "Spero
pure ...", "che sempre quella porta ... et copiosamente"). Decrypted with `key_h4.json` (fitted on R5518 + R5514), no re-solve
(`dec06.txt`): **word share 0.470 against 0.164 shuffled**. Phrases: "per la mia ... per lo ... del conte Iacomo", "cerca fornirse de
gente", "in questo ... de la ... far", "per esser possente a farlo", "star paciente a ogni ... voluntate", "esser fornito de gente
per poterlo meglio", "fare stare", "soldati ... la Marca ... trova", "Baglione ... cerca de desviarme ... quatrocento cavalli ...
potese desviare", "Baglione ... oltra lo pensero", "per la parentela ... esser piu forte de gente", "lo conte Carlo", "per derisione",
"conte Iacomo questo ser Cristoforo suo cancellero", "altre ... poco importano". Names now across the family: conte Iacomo, ser
Cristoforo (his cancelliere), conte Carlo, Baglione, the duke of Modena, la Marca, Urbino, Castiglione, la Mirandola, Lodovico.
Family C: six letters, 8,710 cipher signs, one key from the ciphertext alone, out of sample on four (0.42, 0.47, 0.46, 0.47).
Remaining: R5506 page 2, R5504, R5505 (two pages each), R5515 (faint).

## 15 Nov 2026 (later): R5504 sample transcribed; out of sample again
`famC/hand/r5504_hand.txt`: R5504 (cart. 1598 no. 30) page 1, lines 1-16 only, 393 cipher signs (rest of the page and page 2 not
transcribed). Decrypted with `key_h4.json`, no re-solve (`dec04.txt`): **word share 0.417 against 0.102 shuffled**. Phrases: "per
vostro cavallaro", "lo fatto de tutta ... stato bene informato", "per maggior", "litera ... secretamente", "ogni altra cosa ... in modo
... strattamente", "piaseria", "pare ... bono", "dubio", "conoscere questa vostra litera", "oltra questo ... intendeva".
Family C: seven letters (9,103 cipher signs), one key from the ciphertext alone, read out of sample on five (0.42, 0.47, 0.46, 0.47,
0.42; shuffled 0.10-0.16). Remaining: the rest of R5504, R5505, R5506 page 2, R5515 (faint).

## 15 Nov 2026 (later): R5505 sample transcribed; out of sample again
`famC/hand/r5505_hand.txt`: R5505 (cart. 1598 no. 31) page 1, lines 1-16, 439 cipher signs. Decrypted with `key_h4.json`, no re-solve
(`dec05.txt`): **word share 0.417 against 0.171 shuffled**. Phrases: "la vostra signoria sia de tutto", "de la Mirandola dove ero trovato
ser Cristoforo cancellero del mio [?] conte Iacomo", "el quale", "molte ... per modo alcuno", "facendo ... a mario", "per la ... altra
trovara meglio", "farà per la via", "dicendome ... me pare ... la impresa de questi". Clear opening "quando ... senza fallo me pare
impossibile a l'altro".
Family C: eight letters (9,542 cipher signs), out of sample on six (0.42-0.47). Each new letter confirms the key and the setting
(conte Iacomo, ser Cristoforo his cancelliere, the Mirandola) but none raises the share above about 0.47: the remaining gap is in the
transcription and in signs the key does not yet place, not in missing text. Not transcribed: rest of R5504 and R5505, R5506 p.2, R5515.

## 15 Nov 2026 (later): re-solve on all eight letters
`famC/hand/tall.txt`: all transcribed family C text (9,509 signs). CTTS (period Italian, n-gram 5, 4 homophones, 540 s), two seeds
agree: 17.13 M against 7.18 M shuffled, **ratio 2.39** (best so far; 2.08 on three letters). Solver key `key_s.json` vs hand key
`key_h4.json`: word share over all text 0.476 vs 0.460, higher on every letter (R5518 0.47, R5514 0.50, R5517 0.44, R5503 0.48,
R5502 0.48, R5506 0.48, R5504 0.47, R5505 0.46).
The 12 differences tested one at a time against the hand key (letters inside words, of about 9,500): P v->i +46, E f->t +40,
c i->d +25, q i->m +23, u c->s +21, D1 a->v +8, others within +-5, w i->v -12. Checked in context: q = m breaks "ordine in modo",
E = t breaks "beneficio" (long-barred o read f on the crop), c = d contradicts the ct sign's place in the nulls; these come from the
model's taste for common letters. Adopted only P = i (fits "regoai[i]", "per[i]", "racosi[i]"): `key_h5.json`.
Conclusion: more text sharpens the solver signal but does not move the reading past about 0.47-0.48; the key is stable. The rest needs
cleaner signs (ASMi images) or a contemporary key; family C is left read in part.

## 15 Nov 2026: family B (id 2629), R5562 deciphered on the first pass, key from the ciphertext alone
`famB/r5562_hand.txt`: R5562 (cart. 1598 no. 88, stamped 134), 14 lines, 686 signs, all cipher (no clear text), read from a 2/3-scale
render and line crops; about 35 sign types (letters, digits, crossed tt/ff/pp/n/m ligatures, o with a cross, q with a cross).
CTTS (period Italian, n-gram 5, 4 homophones, 240 s), two seeds agree: 24.09 M against 10.73 M shuffled (ratio 2.24). Dictionary
cover of the decryption: 0.99 with words of 2+ letters (shuffled 0.93), 0.65 with 4+ letters (shuffled 0.26). The text reads as
continuous Italian (`famB/oa.txt`), word division added here, spelling as decrypted:
"Firensa de presimo et t'avisai Nicodemo de tutto quello che intesi per tenire al signore. Trovai Iovan Galeasmo in quela cita,
venuto a cercare partiti cum Fiorentini facendo soldati, o cum lo signore; le dimande sue sono grande, e cum lui era uno [famiglio?]
di l'arcivescovo mandato per sentire di qua ... desiderio et espectatione di cose nove. Ma se pur al signor parese di prendere
alcun partito cum meser Ludovico, ma advertite che sua signoria el facio obligare per Tomasino, el quale intende temperare le cose de
Corsica in li primi movimenti de importantia ... A Firensa trovai le cose molto in [?]; non ne scrivo altro ... Nicodemo como ... el
quale ancho avisai de uno ambasiatore venitiano ... Iovan Galeasmo dove va venir a far pratiche a Firanse e poi andare a Roma.
... die quinto decembris etcetera."
Key (solver, `oa.txt`): a = 8 X p; c = D; d = 4; e = P m x; f = N; g = Q; i = F v; l = c; m = R; n = O; o = 7 k; p = H; r = 3; s = T;
t = 9; u/v = 5 a; b = +; h = S; q = y; s = d g. Simple homophonic substitution, no code words seen.
Context: Nicodemo (Tranchedini, Sforza agent in Florence?), Giovanni Galeazzo, messer Ludovico (il Moro?), Tomasino (Campofregoso?)
and Corsica point to the 1470s-80s; not checked against dated sources. Status: R5562 read as sentences on a first-pass
transcription; a few words open. Next: re-check the doubtful spots on the image, measure the read share, and decrypt the other six
family B slips (R5572, R5573, R5575-R5577, R5586) with this key.

## 15 Nov 2026 (later): family B, five more slips decrypted with the R5562 key unchanged
Key `famB/keyB.json` (solved on R5562 only), applied without any re-solve. Dictionary cover with words of 4+ letters (same signs
shuffled in brackets): R5562 0.65 (0.15), R5576 0.67 (0.15), R5572 0.64 (0.17), R5577 0.65 (0.10), R5575 0.60 (0.16), R5586 0.64 (0.16).
Decryptions `famB/dec*.txt`; each reads as continuous Italian (cover below 1.0 because the measure skips short words and names):
- R5576 (452 signs, complete): "Non vi ho scripto de la venuta de Iohan Galeasmo in questa terra perche non era al fine ... meser
  Ludovico ha avuto da Firense ... del consiglio ducale ... uno doctore mio parente venuto ieri da Firense mi diceva aver inteso da uno
  residente in quela cita per il duca di Modena che el conte Guido Rangone per venir presto di qua mandato dal suo duca ... Sarsane
  die septe iunii etcetera."
- R5572 (407 signs, complete): "Meser Ludovico ha mandato a Sena uno Bartolomeo Borella ... per intendere e praticare ... madona
  duchessa gubernatore ... retenendo in lei castelleto ... per via de Piero de Cosmo ... Tomasino manda uno Marcelino in Corsica per
  sulevare li Corsi ... cum madona qualche composicione honesta ... Sarsane tredese martii etcetera."
- R5577 (577 signs, complete): "De qua non accade altro al presente se non che meser Ludovico e Tomasino sono in molte diferentie e
  ogni volta piu cresce l'odio e la difidentia fra loro. El podesta de Ponsano ... io andero questo septembre a Volterra per observare
  la fede ... finito lo oficio tornero ... io bisogno de ducati quaranta per espedire certi mei strecti bisogni ... pregare madona et el
  signore ... bon servidore de le vostre illustrissime signorie. Sarsane die decimoseptimo iulii etcetera." (two digit-signs 6, 10 left
  as written.)
- R5575 (first 12 lines, 592 signs): "Respondo a la vostra ricevuta heri; Nicodemo va sempre confortato meser Ludovico circa la
  specialita del signore ... la electione di la cancelaria di Volterra la quale acceptai non per voglia ... ogni sinistro ... el tempo
  non comincia fino a octobre ... seguiro l'ordine nostro cum Nicodemo."
- R5586 (first 6 lines, 348 signs): "... cum Fiorentini non e stata alcuna ... per parte de meser Ludovico ... dato al signore tale
  aviso ... suspecto ... certi ... dato aviso a Nicodemo ... meser Ludovico a uscire."
Setting: the writer is at Sarzana (dated "Sarsane", 5 Dec, 7 June, 13 March, 17 July), reports to the duchess and duke (madona e el
signore) on messer Ludovico, Tomasino (Fregoso) and Corsica, Florence, Siena and Volterra; Nicodemo is his correspondent or channel.
That fits the regency of Bona of Savoy and Gian Galeazzo (1476-80) with Ludovico in exile, but the dating is not checked.
Status: family B read on a first-pass transcription (six letters, key from the ciphertext alone, confirmed on five letters it was not
fitted on). Not yet done: R5573 (full page), the rest of R5575 and R5586, word-level review against the images, measured read share.

## 15 Nov 2026 (later): family B complete, all seven letters decrypted
Rest of R5575 (now complete, 1,004 signs) and R5586 (now complete, 974 signs) transcribed, and R5573 (a 7-line slip, 261 signs,
not a full page as the triage thought). All decrypted with `keyB.json` unchanged. Total 4,363 cipher signs.
4+ letter word cover (no shuffle in brackets this time; shuffles were 0.10-0.17 above): R5562 0.65, R5576 0.67, R5572 0.64,
R5577 0.65, R5575 0.60, R5586 0.54, R5573 0.62; all 0.61.
- R5575 end: "... me pare habiate a fare altra provisione, perche me pare haver tolta via ogni rasone et a meser Ludovico, e mi incresce
  ch'io habia acceptato dicto oficio, nondimeno fate como vi pare meglio. Iovan Galeaso mi disse questi di a Firense haver havuto
  letera da Iovan Coscia che volese mandare uno de li soi al duca Iovani per bona casone, e che gli voleva mandare uno Piero del
  Cerreto, famiglio di l'arcivescovo ... intrinsico e pratico di la lingua e del paese. Sarsane die vigesimo februarii etcetera."
- R5586 rest (rougher transcription): "... per la restitutione de ... [Fiorentini?] non entrerano in tel facende sensa consenso del signore;
  il simil credo del duca de Modena ... meser Ludovico, el quale per le morte de meser Ieronimo ... in terre de Firentini ... Iovan
  Galeaso cerca per mio meso havere le licentia da meser Ludovico ... sconforterò la cosa ... se pur meser Ludovico inclinase al denaro
  infra quatro di ... Firentia die octavo febrarii."
- R5573 (complete): "El messo de Tomasino e tornato de Corsica; diceva aver trovato e lasato quele cose in pacifico, ma che Tomasino era
  in pensiero de moversi per sua specialita. Le cose ocorse di qua mi sono parute simile a quele di sè vala ... credo sero a Milano de poi
  Pasqua e satisfaro piu a pieno. Sarsane die vinti tre marcii etcetera."
Family B status: all seven letters decrypted with one key recovered from the ciphertext alone (outcome: key recovered from
ciphertext-only), confirmed on six letters it was not fitted on, each reading as dated Italian sentences. Not yet at the read bar as
measured: first-pass transcriptions, R5586 second half rough, two digit-like signs (6, 10) and a few words open; no word-by-word
review against the images and no reader review yet. Remaining gaps are workable, not blocked.

## 15 Nov 2026 (later): family B review
- `flag.py`: every sign position re-scored with a 5-gram letter model (period Italian); 130 positions where one other sign would read
  much better. Two systematic look-alike merges in the transcription explain most of them:
  1. `R` covers two shapes, a plain "r4" ligature (= m) and a longer underlined "rr4" (seen on R5572 l.1); in "lvdovic[R]",
     "bartol[R]meo", "servid[R]re", "tenend[R]", "molt[R]" the sign must be o.
  2. `5` and `S` (5-like v sign and 5-like h sign) were merged: "c[5]e" must be "che" (S = h): 13 places.
  Also c / D (l vs c) in a few places.
- 43 emendations applied for these look-alike pairs only, with a model gain of 10+ (`emend.json`, emended tokens `e*.txt`). They are
  editorial: each fits a known look-alike and the context, but they have not each been checked on the image.
- Read share, strict segmenter (dictionary words of 4+ letters seen 5+ times in the corpus, a closed list of short function words, the
  names; chancery spellings and u/v count against it), first pass / emended: R5562 0.897 / 0.915, R5576 0.921 / 0.932,
  R5572 0.882 / 0.902, R5577 0.899 / 0.910, R5575 0.872 / 0.894, R5586 0.830 / 0.836, R5573 0.916 / 0.916; **all 0.893 emended**.
  Segmented readings with unread pieces in brackets: `famB/read*.txt`.
- What the unread 11 % is, read by eye: mostly words the segmenter cannot place but that read (spellings like "tvto", "cvi", "vebi",
  "facio", "sarvane"; split words such as "lvdo vi cma"), a few names (Iovan Coscia, Piero del Cerreto, Marcelino), the two digit-like
  signs (6, 10), and R5586's second half where the transcription is rough. Genuinely unread stretches by eye are a handful of words per
  letter.
Status: family B read in part, measured 0.89 (below the 95 % bar); the gap is the R/rr4 and 5/S splits (need a token-by-token pass on
the images to replace the emendations with readings), R5586's second half, and the two digit signs. All workable from the scans.

## 15 Nov 2026 (later): family B emendations checked on the images
Each of the 43 flagged signs was cropped from the DECODE image at its estimated position (line from an ink profile, x from the token's
place in the line; `lines.json`) and judged by eye on contact sheets (`chk0-3.png`, git-ignored):
- `R` -> o (16 places): the image shows the long underlined "rr4" sign, distinct from the plain "r4" (= m) standing nearby; confirmed.
  Now its own sign `W` = o in `keyB2.json`. (Other `R` tokens not flagged were not re-checked; some may also be W.)
- `5`/`8` -> S (h) in "che" (22 places): the image shows "ɔ S" (c + h-sign), not the digit 5; confirmed as transcription errors.
- c->D, N->5, 9->5, Q->5 (5 places): not confirmed on the crops; dropped.
38 corrections accepted (`v*.txt`). Strict-segmenter read share: R5562 0.905, R5576 0.932, R5572 0.897, R5577 0.910, R5575 0.882,
R5586 0.828, R5573 0.916; all 0.886. (Lower than the 0.893 with the unconfirmed emendations; the measure under-counts chancery
spellings, so these figures are a floor; by eye the letters read in sentences with a handful of open words each.)
Remaining gaps (workable): R5586 second half (rough transcription), the two digit-like signs, unflagged `R`/`W` and other look-alike
tokens, a reader review of the seven texts, and a proper read-share count by a reader rather than the segmenter.

## 15 Nov 2026 (later): R5586 lines 7-18 re-read on the image
Lines 7-18 re-viewed at 2.5x (`h0-h5.png`, git-ignored). The earlier transcription was close: four corrections (three underlined
"rr4" = W = o in ll. 7, 15, 16; l. 7 "H M G +" and l. 17 end). R5586 read share 0.828 -> 0.833; family B 0.887.
What keeps R5586 low is not the transcription but the text: damaged and creased edges (end of ll. 9, 11, 12 lost in folds and
holes), an erased word in l. 13, and the date line "dd o+ T o+ bb 6" in signs outside the letter key (numerals?). The decryption
reads in sentences where the paper is whole (`famB/read86.txt`).
Family B gaps now: physical damage in R5586 (outside blocker for those few words), the numeral-like signs (6, 10, dd, bb, o+), and
the reader review. Measured 0.887 with a strict segmenter that counts chancery spellings as unread.

## 15 Nov 2026 (later): reader review draft for family B
`famB/READER_REVIEW.md`: all seven letters with word division, punctuation, open words marked ([?], [...], { }), and a close English
translation, for a second reader (the reading gate asks for a reader review and English). Not yet reviewed by anyone.

## 15 Nov 2026 (later): more family B analysis
- Five open words resolved with the look-alike pairs already confirmed on the images (5/S, M/N barred m/n, c/D): R5562 "fhia" ->
  "Fui a [Firensa]", "vebi da" -> "hebi da", "a iar pratiche" -> "a far pratiche", "invicvpate" -> "inviluppate"; R5575 "vaslripto" ->
  "ha scripto" (`v62.txt`, `v75.txt`). Same classes as the confirmed fixes; these five were not cropped individually.
- Historical check (web, 15 Nov; sources in `famB/READER_REVIEW.md`): Ludovico Sforza's exile at Pisa (May 1477 - Sept 1479) under the
  regency of Bona of Savoy ("Madona", "el Signore"), Tommasino Campofregoso lord of Sarzana (governor of Corsica later), Milanese
  Corsica 1464-1481, Nicodemo Tranchedini writing from Genoa in 1478 (DBI), and "meser Ieronimo" (Girolamo Olgiati, d. Jan 1477?) all
  fit. Working date: June 1477 - March 1479; an informer at Sarzana near Ludovico. Not checked in archival registers.

## 15 Nov 2026 (later): open words, doubling marks found
- The sign o-with-cross (`o +`, 10 uses) and the digit-like 6 and 10 are **nulls between doubled letters** ("dupple" marks): "el
  mes[o+]so", "Volter[6 10]ra", "Volter[o+]ra", "dis[o+]se", "podes[10 6]se". Removed (`w*.txt`). Resolves R5573 "messo", R5577
  "Volterra"/"podesse", R5575 "disse", "Volterra". Read share: R5577 0.923, R5575 0.896, R5586 0.850, R5573 0.930; **all 0.897**.
- Tried and not settled: "{mamiglio}", "si s'gain", "sarvane", "{mas}sano", "canteera", "sevala", "promqso", "Miser Andremto". A
  look-alike search gives no strong single fix, and the image crops for these spots missed (position estimates from token counts are
  too rough on these lines). They need a person, or a sign-by-sign box transcription, to read the exact shapes. R5586's 'dd', 'bb', 'e'
  cluster (the date line and two spots) is also still unread.

## 15 Nov 2026 (later): open words, whole-line image pass
Whole lines holding the open words cropped and read by eye (`L0-L6.png`, git-ignored). Result:
- R5577 l. 7 "tornermche" -> "tornero, che" (an underlined rr4 = o read as plain R); fixed in `w77.txt`.
- R5562 l. 5 "si s'gain": the image shows a plain q-shaped sign with an ink blot where `Q` (g) was written; no candidate reads.
- R5577 "promqso": the image gives "pp ɔ 7 tt m S k" around it, which does not yield "promesso" under the key; left open.
- R5562 "sarvane": the date line is torn at the left edge; the sign before "rvane" is lost (outside blocker; probably Sarsane).
- "mamiglio", "mas…sano", "canteera", "sevala", "Miser Andremto": the line crops are legible but my token sequence for these spots
  does not align closely enough with the image to say which sign is wrong; a box-level transcription of these lines is the fix.

## 20 Nov 2026: PR #825 integrated (36 pages of 30 records, keys and decodes; prabal-rje)
Files: `outside_prabal-rje_2026-11-19/` (rows, key tables, decodes, frozen reads, record pages, `check.md`), the contributor's files unchanged. His nested `profile.json` is folded into `profile.json` here and removed from the folder (no checker reads a nested profile; git history keeps his, commit 5b535700b6): 30 documents, 11 parts (one per catalogue entry), 30 texts, his two credits (transcription, solution), his three steps and one step for our review; provenance "mixed".
Everything is decoded, not read: no word division, no reading in sentences, cipher words not counted. Family A (2628) is decoded with the archive's key sheet R5347 (cart. 1597 no. 47), which he matched to it; families Z (2645), C (2630), K (2638), G (2634), E (2632), P (2643), O (2642), F (2633), L (2639) and N (2641) with keys he recovered from the ciphertext alone. R5504 p. 1 and R5505 p. 2 are his own key for family C, made independently of ours: a second key for 2630.
Checked here with own scripts: each key table applied to its rows gives his decode on every line of the 36 pages; the "Agree" figures of his `check.md` recount exactly (24,483 of 27,152); the cartella numbers equal `list1598.json`; the document lengths are `_check_profile.py --measure --drop-first` on his rows (37,077 signs, 835 of which he does not read). Family C: 245 of the 392 letters (62%) of `famC/hand/dec04.txt` (R5504 p. 1, lines 1-16) fall in blocks common with his decode; 100 shuffles of his key values give at most 45% (median 19% against his rows 1-16, 27% against the whole page); the first review reported 16% for one shuffle.
Key not confirmed: R5516 p. 1, R5564 p. 1, R5583 p. 1 (first review: his key scores below a hill-climb on the shuffled signs; not run again here). Agreement by construction, so no test of the key: R5297 p. 1, R5521 p. 2 and p. 3, R5542 p. 1 (key table taken from his frozen read). By his statement the key of R5516, R5519 and R5522 also decodes R5445 p. 1 of cart. 1597 (`targets/sforza1597`); not confirmed.
Not checked: the rows against the DECODE images; the language, clear-text and plaintext fields of the 30 documents and the year leads, which are his; the frozen reads against his repository (github.com/prabal-rje/branicki-1757, `sforza-160-records`). His conditions, as his profile gave them: images and his own transcription, ciphertext-only, language models not named at his request, own Python scripts, 16-19 Nov 2026; our decryption of R5504 p. 1 lines 1-16 (15 Nov) existed before his attempt and, by his record, was not used.
