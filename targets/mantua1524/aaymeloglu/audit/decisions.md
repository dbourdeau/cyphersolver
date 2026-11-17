# Decisions log (round 6, 2026-11-15)

Start: anneal5.json seed 2 (4=h, 7=c fixed). Units changed, then values set by hand where several independent words agree. Reserved lines 68r 20-23 were never used as support (RESERVED.md). "LOO" = best single value for the sign by the 4-gram LM with all other values held (controls6.json); a disagreement means the value comes from words/names, not from the model.

## Unit (merge) decisions

| change | evidence | effect |
|---|---|---|
| drop `io` merge | it swallowed the `i` of `i o o` (fatto: `i 9 o o lo 9+`, Italia `r n i o o 9 ...`) | fatto x2, Italia read |
| add `l a` = one unit | havesse `4 9 p# 2 [l a] a 2`, Grossino `3 8 9+ a [l a] mi x 9+`, potessimo, mostrassimo, se (`l a 2`), sia | lone `l` almost vanishes (5 left, all in doubtful 68r 01-02) |
| add `b o` = one unit (q) | questa `b o p# 2 a lo 9` (68r 16), quan-to (68r 03-04), alquanto | |
| add `m o` = one unit (m) | somma `a p# e+ m o 9` (r15), mandato `m o 9 no s 9 oo 9+` (68r 16) | m is no longer a sink; giam-netto reads n (lenient) |
| add `g r`, `g 1` = one unit (a) | cavalcato `7 9 p# cc ss# 7 g r oo 9+`, sangue `a g r no 3 p# dd`, Carpi `7 g 1 8 I mi` | g is a two-stroke a |
| keep `m i` = i | in x5, Carpi, heredi, matina ... | |
| `l o` kept = t, with an anomaly | t in fatto, investitura, potessimo, tanto, matina, questa, tolto, haveti, sinistrato; but **l** in cancel-l-ere (r01, v01), l'al-t-ro (68r 11), caval-l-o (68r 11), al-l-i (68r 17) - 4 of 5 right after `ss#` = l | words with lo=l graded forced; looped vs plain l not separable on the images |
| `b u` merged = r (**post-hoc**, after the reserved count) | first left split (altra wants r, "Borbone" 68r 08 wants b). Retested: bu = r gives altra (r18) and desi-deraria (68r 03, conditional of desiderare); 68r 08 then reads Borron(e)? after "M. [..]chille", so the Bourbon reading of 68r was dropped | 198r Barbon (b alone) unaffected; b now rests on Barbon alone (conf C) |
| `n i`, `r n i`, heading `i n i` not merged | `n i` stands alone at r05 = "in"; r16 `r n i` + talia; heading `p# i n i 7...` gives Victorie only if `i n i` = i | treated as minim-cluster transcription questions; those words lenient |

## Value decisions

| sign | value | supporting words | from | LOO |
|---|---|---|---|---|
| 9 | a | fatto, donato, Carpi, havea, matina, mandato, Milano, Pavia, Cremona | anneal + hand | a |
| 2 | e | heredi, che, havesse, Cremona, morte, retirera, fiume | anneal + hand | e |
| 9+ | o | donato, fatto, altro, Prospero, bisogno, potessimo, Cremona | anneal + hand | o |
| mi | i | heredi, Carpi, investitura, matina, Milano, Pavia, fiume | anneal + hand | i |
| 8 | r | heredi, morte, Prospero, Carpi, Cremona, retirera, Februarii | anneal + hand | r |
| p# | u/v | Suardini, havea, havendo, investitura, Pavia, volendo, questa; = per in "per la morte" (v04) | anneal + hand | u |
| ss# | l | la investitura (r13, v04), la morte x3, Milano (198r), del S. Prospero x3, volendo, altro | **hand** (anneal: n) | l |
| x | n | investitura, donato, bisogno, Milano, Cremona, havendo, tanto | anneal + hand | n |
| 7 | c | Carpi x5, che x4, Cremona, cancellere, cavalcato, cosa | anneal (fixed) | c |
| oo, lo | t | see merges | anneal + hand | t |
| s | d | di x4, heredi x3, donato x2, Suardini, volendo, mandato; `s .` = S[ignor] at r12 | anneal + hand | d |
| e+ | m | morte x3, matina, mandato, Milano, Cremona, potessimo | anneal + hand | m |
| no | n | Suardini, ragione, non x2, quanto, havendo, sangue | anneal + hand | n |
| 4 | h | heredi x3, havea, haver, havendo, havemo, che | anneal (fixed) | h |
| i | f | fatto (r13, v04), fiume x2 (198r), Februarii, infirmita, satisfare | **hand** (anneal: r) | u |
| 3 | g | bisogno, ragione, sangue x2, Grossino | anneal + hand | g |
| I | p | Prospero x3 (r08, r12, r17), Carpi x4, per lo | **hand** (anneal: t) | t |
| I= | p | Prospero x3, potessimo, recompensar, poi, Pavia | anneal + hand | p |
| a | s | Suardini, sua, bisogno, questo, investitura, Prospero, summa; `. a .` = .s. = S[ignor] | anneal + hand | s |
| la | s | havesse, Grossino, potessimo, mostrassimo, se, sia | hand (new unit) | s |
| 6 | b | Februarii, bisogno | **hand** (anneal: a) | r |
| cc | a | Italia (r05), sua (r11), al S. Prospero (v03), a volonta, cavalcato | anneal + hand | a |
| dd | e | heredi x2, Februarii, bene, cavalcare, sangue | anneal + hand | e |
| b | b | Barbon (198r) only, after the bu merge | **hand** (anneal: t) | c |
| bo | q | questa (68r 16), quan-to (68r 03-04), alquanto (68r 13) | hand (new unit) | q |
| d | q | questo (r16), qualche uno (v08) | anneal + hand | q |
| mo | m | summa, mandato | hand (new unit) | m |
| pa | i | Suardini, Februarii, Carpi (v02), heredi (v03), orine | **hand** (anneal: e) | o |
| gr, g1 | a | cavalcato, sangue; Carpi | hand (new unit) | a/o |
| q | a | Suardini only | hand | - |
| o | b | bene servita (r04) only | hand | o |
| p+ | u | Sua (r09), un (68r 11), qualche uno; = per in per lui (r12) | hand | - |
| bb | o | havemo (68r 19) only | hand | e |
| c | e | exercito (198r) only | anneal | - |
| S | d | denari (r15) only | hand | t |
| bu | r | altra (r18), desideraria (68r 03) | hand, post-hoc | s |
| u | none | alone only in 68r 02 (u r a, p u m i s a 8 9), probably clear text | - | - |
| C@ | q | questo (198r) only; kept as code sign in the decoder | hand | - |
| H | none | se ben / indebilita want H i = b; maneggiassimo wants H = g | unread | - |

Values with one supporting word (q, o, bb, c, S, b, C@, g1) make their words forced or lenient, never strict.

## Code signs
BOX (r11, r14, r20, r22, v02): "me fu detto [BOX] haver donato Carpi al S. Prospero", "che [BOX] havea donato Carpi ... et per suoi heredi", "appresso [BOX]", "alla volta [BOX]" fit the Emperor (the grantor of Carpi); "serebbe ragionevole che [BOX] fosse preposto ad ogni altro" fits the Marquis better. Not resolved; possibly two signs. IZ (r03), CROSS (68r 18): unread.

## Image re-reads (round 6, non-reserved lines only)
- H1 run 2 (`p# i n i 7 ...`), 5x crop: after p# there are three minims (dotted i + a two-minim u/n), plus a second dot further right; not four minims. So `m i` = i is not established and **Victorie is doubt**, not forced.
- 68r 17/2: the fifth sign has the flat angular top of 7, not 9: `e+ 2 s m i 7 m i` = **medici** (transcription corrected).
- 68r 18/6: only one 7 after `a`: `p# a 7 m i 8 2` = **uscire** (transcription corrected).
- 68r 18/5 facendo (`i 7 7 2 ...`) and 68r 19/3 orinato (`... x 7 oo 9+`): tops ambiguous at this resolution; words stay lenient.

## Tier guard
build_words.py demotes any "strict" word whose row has a transcriber alternative `{..}?` (cavalcato 68r 11, mandato 68r 16, haveti 68r 01, -ra r18), a code sign ([BOX] haver), a one-word sign value (et ve lo, Barbon, reserved fatto with bb), or a reading that differs from the key output. So gr = a and mo = m rest partly on forced words (sangue, summa are clean).

## Changes after the Codex review (codex-review.md, 2026-11-15)

| item | change |
|---|---|
| 298v 04/6 | transcription `m i x p# a` -> `m i x p# 2` (checked on the image at 1650,640,1840,755): reads inve-\|stitura, both segments strict |
| 68r 23/4, 23/5 (reserved) | `i 9+ a l a m i e+ s 9+` -> no s; `o o p# l o o 9+` -> `l o o o`: fossimo, tutto strict. Checked on the image. Not folded into the frozen score |
| 68r 21/9-22/1 (reserved) | reading "et a chi ve parirà" (review) replaces "ve(r)rà"; keeps every decoded sign; strict |
| 68r 19/2 `9 9` | review could not find it; **kept**: two loop-and-descender signs are visible between `b b` and `9+ 8 m i x` (crop 300,1950,900,2040). Still unread |
| decoder | `lib6.load_key` skips `_` metadata and null values (dec6.py crashed on null entries) |
| strict guard | now requires independent support: a unit with confidence C (one word) or W (mo, gr, bu: two words, one with an uncertain transcription or unit) demotes the segment to forced. Demoted: summa, sangue, -deraria, mai (reserved), mostrare (reserved) |
| `lo` | readings that want l (canceltere x2, lattro, caualto, alti) shown as `raw -> read` substitutions and graded lenient (were forced); no graphic t/l rule claimed |
| names on 68r 07-08 | Achille / Borrone withdrawn to unread |
| Victorie | doubt in the TSV too; the four-minim note withdrawn |
| 68r 10.1 | `douecuenire` doubt; English no longer supplies "[find]" |
| reserved-line result | reframed in controls.md as a fit-consistency check with leakage, not a held-out test; 4+ denominators stated (20 fully keyed, 22 with unread); z for 4+ not quoted; frozen, post-hoc and post-review rows kept separate |
| history | Prospero: late December 1523 (28/30/31 in sources); Carpi grant without investiture already in Petrucci's DBI life (no novelty claim); Carpi chronology after Forner (expulsion 3 Jan 1523, recovery Aug 1523, forfeiture 9 Mar 1525); 198r is a conditional, prospective retreat; 68r matches Benzoni's DBI account (urine deception, admission to Castiglione) and is plausibly Federico to Castiglione, as inference |

Counts after these changes (segments): non-reserved 118 strict, 19 forced, 31 lenient, 10 doubt, 18 unread (196); reserved 23 strict, 3 forced, 4 lenient, 1 doubt (31).

## Response to the Codex review
- Accepted: all transcription corrections except 68r 19/2 (see above); the decoder fix; the independent-support rule for strict; the reframing of the reserved-line control; the `lo` presentation; "ve parirà"; the historical corrections and the Benzoni identification.
- Not accepted: removal of 68r 19/2, because the signs are on the image. The review's own caution (only remove it if the position cannot be shown) is met by the crop.
- Noted, unchanged: `bb` = o, `p+` = u and `S` = d stay as provisional values with forced or lenient words; `pa` stays merged despite the inconclusive split test, for its repeated function (Suardini, Februarii, Carpi, heredi, orine).
