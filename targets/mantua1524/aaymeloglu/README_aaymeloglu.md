# Mantuan cipher extracts of 1524 (BAV Vat. lat. 8214)

**Status: partial, 15 November 2026.** Three leaves of a volume of letters and extracts sent to Federico II Gonzaga, marquis of Mantua, in 1523-24 share one homophonic cipher. Large parts read as Italian under a key reconstructed from the text alone (all values grade S; no key sheet, gloss or contemporary decipherment is known). The best passages are nearly all strict; names, rare signs and code signs remain open.

| Leaf | Content | Segments | strict | forced | lenient | doubt | unread |
|---|---|---|---|---|---|---|---|
| f. 298r | "Ex litteris Suardini": G.B. Suardino at the Imperial court, heading and 23 lines | 49 | 21 | 8 | 10 | 4 | 6 |
| f. 298v | the same extract, 8 lines | 20 | 15 | 1 | 3 | 0 | 1 |
| f. 68r, lines 1-19 | a letter almost all in cipher, first person plural | 114 | 72 | 8 | 17 | 6 | 11 |
| f. 68r, lines 20-23 | the same letter; reserved control lines (see Controls) | 31 | 23 | 3 | 4 | 1 | 0 |
| f. 198r | "Ex litteris D. Cappini dat. in Robio 8 Aprilis 1524", two cipher lines | 13 | 10 | 2 | 1 | 0 | 0 |
| **all** | | 227 | 141 | 22 | 35 | 11 | 18 |

A segment is one run of cipher between clear words or gaps, as transcribed: it can be part of a word (`scr-`, `-sar`) or several words (`la investitura`). Strict counts include short function words. The read fractions are coverage, not accuracy: there is no blind calibration on this hand.

Files: [reading.md](reading.md) (Italian, English and notes per leaf), [reading-words.tsv](reading-words.tsv) (units, key output, reading, tier and note per segment), [key.json](key.json), the transcriptions [transcription-298.tsv](transcription-298.tsv), [transcription-68r.tsv](transcription-68r.tsv), [transcription-198r.tsv](transcription-198r.tsv), the sign inventory [signs.md](signs.md), [images.tsv](images.tsv) (IIIF URLs and hashes; the images are not redistributed), and [audit/](audit/) (decisions log, reserved-line protocol, the Codex review, control outputs). `python3 mantua-1524/verify.py` recomputes every key output from the transcriptions and the key, enforces the tier rules and prints the counts above.

## What the letters say

**f. 298r-v, Suardino at the Imperial court.** Heading: Ex litteris **Suardini** datis **Victorie?** 26 **Februarii** ("from the letter of Suardino, dated at Vitoria (?), 26 February"). Charles V's court was at Vitoria from 5 January to 6 March 1524, so the date fits; the place itself is doubt (below). The subject is Carpi, confiscated from Alberto Pio and promised to Prospero Colonna, who died at Milan in late December 1523:

> ...essendosi in-[..] **la morte del S. Prosper(o)** ... me fu detto **[BOX] haver donato al S. Prospero Carpi per lui et per li heredi: ma che non li dava [..] fatto la investitura** ... **volendosene prevaler** di qualche **summa di denari in questo bisogno di Italia, et recompensar poi li heredi del S. Prospe(r)o** in quel che **altra cosa**.

"...the death of Signor Prospero having become known ... I was told that [BOX] had given Carpi to Signor Prospero for him and his heirs, but had not [yet] made the investiture ... wishing to draw some sum of money from it in this need in Italy, and then to compensate Signor Prospero's heirs with something else."

> Dal predicto .S. **Canceller** me fu resposto ... che **[BOX] havea donato Carpi al S. Prospero** et per suoi **heredi**: et così non se mutarebbe questo **per la morte**, ancora che non fosse **fatto la investitura**. Vero era che anchora non era stato cognoscuto se **di ragione Carpi** era stato **tolto** o no ...

"The said lord Chancellor answered me that [BOX] had given Carpi to Signor Prospero and his heirs, and this would not change because of his death, even though the investiture had not been made. True, it had not yet been determined whether Carpi had been taken away by right or not..."

The grant to Colonna without investiture is already reported in Petrucci's life of Prospero Colonna (DBI 27, 1982); the letter gives the state of the question at the Imperial court in February 1524. BOX is a code sign: the Emperor where he is the grantor, the Marquis more naturally in "che [BOX] fosse preposto ad ogni altro".

**f. 68r, a feigned illness.** A "we" told not to ride out pretends to be ill:

> **havemo questa matina mandato fori alli medici** in sala? **orine fatte tingere a posta con sangue** [..] **facendo uscire voce che havemo** [..] **orinato sangue** ... **da poter mostrare al [..] Duca di Sessa et a chi ve parirà, ma per la verità siamo sano et gagliardo como mai fossimo.**

"This morning we sent out to the physicians urine dyed on purpose with blood, letting the word go round that we have passed blood ... so that it can be shown to the Duke of Sessa and to whomever you see fit; but in truth we are as sound and vigorous as we ever were."

Earlier lines: "[salve] would wish that we should not ride out, even though, as far as the illness goes, we could ride, but that it should not be known in Milan"; "we rode a horse the day before yesterday, showing in the evening that it had tired us, and yesterday we schooled a jennet and made a show of having hurt our back". Benzoni's life of Federico II (DBI 45, 1995) describes this episode: Federico showed physicians blood-dyed urine and admitted the deception to Baldassarre Castiglione, "sano et gagliardo". So 68r is plausibly Federico writing to Castiglione, his ambassador at Rome; that is an inference from the match, as the leaf names neither. Benzoni cites Vat. lat. 8214, so the episode is known to scholarship. The Duke of Sessa was Charles V's ambassador at Rome in 1524.

**f. 198r, Capino de Capo, Robbio, 8 April 1524.**

> ...prima la tregua di Spagna per il maneggio del Arcivescovo di Capua **se retirerà questo exercito de fiume in fiume, et poi in Pavia, Cremona et Milano**, secondo dice **Barbon**.

"...[if] the Spanish truce [has not come] first through the negotiation of the Archbishop of Capua, this army will withdraw from river to river, and then into Pavia, Cremona and Milan, according to what Bourbon says."

A conditional, prospective retreat, not a report of an itinerary followed; "questo exercito" most naturally means the writer's own (imperial) force. The cipher reads Cremona sign for sign.

## The key

[key.json](key.json) gives each unit's value, its supporting words and a confidence class. Units are the transcribed signs with these pairs joined: `m i`, `o o`, `c c`, `d d`, `b b`, `l o`, `n o`, `p a`, `l a`, `b o`, `m o`, `g r`, `g 1`, `b u`. It is a homophonic substitution over Latin letters and digits: for example 9 = a, 2 = e, 9+ (crossed 9) = o, `m i` = i, 8 = r, `p#` (doubly crossed p) = u/v, `ss#` (crossed double s) = l, x = n, 7 = c, `o o` and `l o` = t, s = d, `e+` = m, 4 = h, i = f, 3 = g, I and I= = p, a and `l a` = s, 6 = b, `b o` and d = q.

| Confidence | Meaning | Units |
|---|---|---|
| A | several independent words agree | 9, 2, 9+, mi, 8, p#, ss#, x, 7, oo, lo, s, e+, no, 4, i, 3, I, I=, a, la, cc, dd, pa |
| B | two independently secure words | 6 (Februarii, bisogno), bo (questa, alquanto, quanto), d (questo, qualche uno) |
| W | two words, one resting on an uncertain transcription or unit | mo = m (summa; mandato with `m{n}?`), gr = a (sangue; cavalcato with `r{c}?`), bu = r (desideraria; altra with `u{n}?`) |
| C | one word | q = a (Suardini), g1 = a (Carpi), o = b (bene), bb = o (havemo), c = e (exercito), S = d (denari), b = b (Barbon), p+ = u |

No value: H, the code signs BOX, IZ, CROSS and C@ (the looped che-shaped sign; q in 198r *questo* is a conjecture), `p@`, `b+`, `8+`, the two tall strokes `) )`, and lone `n`, `r`, `p`, `u`, `l`.

Exceptions to a single substitution remain visible in the reading as `raw → read`: `lo` gives t securely, but five readings want l (canceltere twice, lattro, caualto, alti) with no graphic rule found to separate them; `p+` and `p#` must read per in *per lui* and *per la morte*; x must stay x in *exercito*; i must read e in *denari*; H would need incompatible values. Some may be copying or transcription errors; that is not established case by case.

## How the segments are graded

- **strict**: the reading spells the key output (ignoring case, spacing, apostrophes, hyphens, accents and u/v); the row has no transcriber alternative `x{y}?`; no code sign; every unit's value has confidence A or B. `verify.py` enforces this.
- **forced**: one unit is a one-word or weak value, a code sign is present, or a transcriber alternative exists, but only one reading gives a word.
- **lenient**: the reading departs from the key output (a substituted or supplied letter) or the choice was made by sense.
- **doubt**, **unread**: no secure reading; an unread segment has no reading outside brackets.

Every value is grade S (CONVENTIONS.md section 1).

## Method

Transcribed from the BAV images ([images.tsv](images.tsv)) sign by sign with alternatives; 68r is second-checked on 5 of 23 lines plus targeted image checks of disputed signs. A homophonic simulated annealing with a 4-gram character model (`cipherkit` `it` corpus: Venetian dispatches of 1589, Albèri's Relazioni, Machiavelli; j/v/k/y folded) gave a first key with the frequent letters and several sinks. Values were then fixed by hand only where several independent words agree (Prospero, Carpi, heredi, investitura, Cremona, fatto, fiume, Februarii), and units were joined where repeated words required it. The decisions log with every value and its supporting words is [audit/decisions.md](audit/decisions.md).

## Controls

- **Key shuffle on the text used for fitting** (`cipherkit.controls.permutation_z_key`, 200 shuffles, lines 68r 20-23 excluded): 4-gram score z = 14.5; segments that are corpus or clear-text lexicon strings, 81 of 191 against 19.0 ± 5.9. These are circular for a hand-tuned key: they show the key is far from a relabelling of the same values, not that each word is right.
- **Reserved lines 68r 20-23**, set aside before the hand refinement and scored by rules written before the count ([audit/reserved-lines.md](audit/reserved-lines.md)): 19 of 31 segments are lexicon strings against 4.8 ± 1.6 for 200 shuffled keys; 10 of the 20 fully keyed segments of 4+ letters (10 of 22 counting unread ones) against 0.06. This is a **fit-consistency check with leakage, not a held-out test**: the annealed key the refinement started from was fitted on all lines including these, its decode of them had been seen, and a shuffled-key null does not model the trying of many keys and merges. With the later `b u` unit and two image corrections on line 23 the counts are 22 of 31 and 13 of 20; these are reported separately and do not replace the first count. The score counts strings, not correct words (`perla` = per la hits; `littera`, `a chi`, `fareti`, `ve parirà` miss; the hit `l` at 21.3 is an overwritten sign). A genuinely unseen passage transcribed and frozen before decoding would be the missing predictive test.
- **Leave-one-out**: freeing one unit and choosing its value by the 4-gram model returns the key value for most units but not for I (model t), i (u), 6 (r), b (c), pa (o), bu (s), bb, g1, o, S. Those values rest on words and names, not on the model.
- **Merges tested both ways** (A values fixed, re-annealed, scored per letter and by lexicon hits): splitting `l o` or `n o` loses hits (79 to 68 and 74); splitting `p a` or `b u` is inconclusive.
- **Matched synthetic control**: an unaided anneal on 1,200 units of homophonic Italian of this shape and 38 symbols recovered 94% of the text in one run of three and 45% in two, on an earlier unit scheme. An unaided anneal is unreliable at this length, which is why the frequent values were checked against words.
- **Independent review**: a second model (Codex) checked 174 signs in 19 key groups on the images, reproduced every key output and the control arithmetic, and checked the historical claims ([audit/codex-review.md](audit/codex-review.md)). Its transcription corrections at 298v 04/6 and 68r 23/4, 23/5, its reading "ve parirà" and its historical corrections are applied. It could not locate the segment 68r 19/2; two loop-and-descender signs are visible there between `b b` and `9+ 8 m i x`, and the segment is kept, unread.

## Open points

- **Heading place**: the key gives `uf[n]fctorie`. Victorie needs the minim cluster after the crossed p to be one i, and the image shows three minims, not the four of `m i`. The court's presence at Vitoria makes it plausible; the signs do not settle it.
- The `lo` t/l question; the minim clusters (`i n i`, `n i`, `r n i`) behind Victorie and *Italia*.
- Unread: H, BOX's referent, IZ, CROSS, `p@`, `b+`, `8+`, `) )`; the names at 68r 07-08 (key output `cchilte`, `borronei`); the clear word "salve" (68r 02, 10), possibly a code name; 68r 01-02, blotted and partly clear text.
- One-word values (q, o, bb, c, S, b, g1, p+) and the weak units mo, gr, bu.
- The ASMn originals (Archivio Gonzaga, Carteggio estero: Spagna for Suardino, Milano for Capino, and Federico's minutes to Castiglione) may carry chancery decipherments, which would give the first C-grade values.
- Whether the heirs and the proposed sale of Carpi are already in print was not checked.

## Sources

- Biblioteca Apostolica Vaticana, Vat. lat. 8214, ff. 68r, 198r, 298r-v ([DigiVatLib](https://digi.vatlib.it/view/MSS_Vat.lat.8214); [BAV OPAC record](https://opac.vatlib.it/mss/detail/25568)). Catalogued as a cipher in [dbourdeau/cyphersolver](https://github.com/dbourdeau/cyphersolver) entry 2368.
- G. Benzoni, "Federico II Gonzaga", *Dizionario Biografico degli Italiani* 45 (1995) ([Treccani](https://www.treccani.it/enciclopedia/federico-ii-gonzaga-duca-di-mantova-e-marchese-del-monferrato_%28Dizionario-Biografico%29/)).
- F. Petrucci, "Colonna, Prospero", *DBI* 27 (1982) ([Treccani](https://www.treccani.it/enciclopedia/prospero-colonna_%28Dizionario-Biografico%29/)).
- F. Forner, "Pio, Alberto", *DBI* 84 (2015) ([Treccani](https://www.treccani.it/enciclopedia/alberto-pio_%28Dizionario-Biografico%29/)).
- Charles V at Vitoria, 5 January to 6 March 1524: [EFE, 30 Dec 2023](https://efe.com/pais-vasco/2023-12-30/carlos-v-vitoria/).
- Sessa as imperial ambassador at Rome: [Real Academia de la Historia](https://historia-hispanica.rah.es/biografias/15460-luis-fernandez-de-cordoba); [Calendar of State Papers, Spain, July 1524](https://www.british-history.ac.uk/cal-state-papers/spain/vol2/pp647-650).
- Schönberg's truce mission, April 1524: [Calendar of State Papers, Venice](https://www.british-history.ac.uk/cal-state-papers/venice/vol3/pp359-364).
- No edition, decipherment or key for these leaves was found. DECODE R7860 (a Mantuan key of 1524-25, ASMn AG b. 423 f. 8) and R7865 (d'Atri, c. 1510) were compared and do not fit.

Read 15 November 2026 with Claude Code; reviewed by Codex the same day.
