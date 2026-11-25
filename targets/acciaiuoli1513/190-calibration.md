# Doc. 190 / 191 calibration of key_v6 on Ruberto Acciaiuoli's hand (Amiens, 23 [month] 1513)

Files: `190-transcription.txt` (signs, from the image alone), `191-clear.txt` (clear copy), `190-alignment.tsv` (457 rows).
Crops: `images/strips/c190_q_NN.png` (recto line NN), `c190_qv_NN.png` (verso), `c190_k_NN.png` (clear copy line NN).

## (a) Measured agreement

Protocol. The cipher was transcribed from the image before the clear was aligned (one token rename afterwards,
`L^-` to `L^.` at r12, a shape split, no value involved). The transcription was NOT blind to the key: I knew the system
and used sense to segment and name signs (as Dudout declares for 311). Decoding is mechanical (Dudout's
`frozen/decode_v6.py` logic; scorer `images/strips/align.py` + `dec190.py`, run from a directory holding both).
Unit = one sign; a sign agrees if its key value equals its piece of the clear word (u/v folded; Cristianissimo = Maestà = Re
one referent; the clear's "detto/tutto" scored as the chancery spelling "decto/tucto", so 0 = c counts as a hit).
Doubtful `{a/b}` signs: "strict" takes the first alternative, "tolerant" the best one.
Not scored: 116 of 1110 signs = 20 struck/stained/unidentifiable + 96 legible signs facing clear words I could not read
(56 in the fit lines, 40 held out). Corrections were fitted on 190r.03-11 only; 190r.12-190v.06 is held out.

| set | signs | key_v6 strict | tolerant | v6 + fitted corrections, strict | tolerant |
|---|---|---|---|---|---|
| fit lines r03-r11 | 333 | 282 = 84.7% | 287 = 86.2% | 307 = 92.2% | 312 = 93.7% |
| held out r12-v06, all scored | 661 | 560 = 84.7% | 580 = 87.7% | 607 = 91.8% | 627 = 94.9% |
| held out, lower bound (40 legible unscored signs counted as misses) | 701 | 560 = 79.9% | | 607 = 86.6% | |
| held out, clear words read before any decode | 93 | 74 = 79.6% | 83 = 89.2% | 78 = 83.9% | 87 = 93.5% |
| held out, + corrections first seen in held-out lines (not a test) | 661 | | | 620 = 93.8% | 640 = 96.8% |

If Γ and π are only this writer's forms of Dudout's bare `r` (= h) and `L` (= p) (see b), the unmodified key scores
571/661 = 86.4% held out, and the gain from real corrections is about 5 points, not 7.

Caveats that matter. Only 93 held-out signs face clear words in my pre-decode notes, and they are common words
(Marsilia, amico, non ho voluto andare più avanti, hiermattina mi fu detto da uno amico), which flatters the key. The
other 568 face words I recognised in the clear only once the cipher suggested them: that 92% is partly circular. It shows
the decode is coherent Italian that fits the clear's ink, not an independent test.
Word level (all rows): 287 y, 97 partial, 30 n, 43 unscored.

Fitted corrections (from r03-r11): ƀ = i, ȣ = o, Γ = h, π = p, ʃ# = ss, A = bene, L^r = vostra, L^- = quanto, D^1 = chi,
bare 4 = Maestà, .64. = S. Severino, r^4 y 9^5 = senza (9^5 = za), bare Z not before 7 = Papa.

What is left wrong after correction is almost all reading, not key: d/G (r for g and back), 2 standing for b
(bisogna, ubidientia, benefitio), one-sign superscript slips.

## (b) Signs and values differing from, or absent from, key_v6

| sign | value here | key_v6 | where, and the clear word that fixes it | status |
|---|---|---|---|---|
| ƀ (crossed 6) | i | absent (W = i) | r05 mane-gg-I-are, I-n-teramente; r10; r11 facess-I; r14, r19 I-o | sure; W also = i (r08 i-n, r16 lu-i) |
| ȣ (small open 8) | o | absent (O = o) | r06 su-O; r07 quell-O, mott-O; r08 stann-O; r15 mess-O | sure; O (ɔ) also = o |
| Γ (gallows) | h | absent by name; probably = Dudout's bare `r` (long r) = h, same value | r06 H-a detto, H-a la cifra; r10/r12 H-onore; r14 H-avendo; r15 H-o | sure for the value; naming open (in 307 Dudout writes ha/ho as `r 3`, `r O`) |
| π | p | absent by name; probably = Dudout's `L` (square) = p (307 `L 7^4` = pre) | r04 P-rocedere; r08 P-ratiche; r09 a-P-rir; r14 so-P-rastarvi; r18 P-rimo; v04 P-relati | sure for the value (always before r); naming open |
| ʃ# (long s, crossed foot) | ss | absent | r08 po-SS-ono; r11 conferi-SS-i, face-SS-i; r13 fu-SS-ino; r15 me-SS-o; r21 ne-SS-uno; v05 pa-SS-erano | sure |
| Ø (slashed 0) | t | absent (8, Z = t) | r16 ris-T-rignere, T-ractar | probable (2) |
| Φ (phi, long descender) | x (or ss) | absent | r12 di-X-e ("mi dixe"); r20 de-Φ-t-ri unread | probable (1) |
| Z (flat lying 2), bare, before 7 | t | Z = t | r06/r07 al-T-ri; r07/r08 mons-T-ro; r10 in-T-rometter; r14 po-T-ra | confirms v6 |
| Z / bare "2", elsewhere | Papa | .2. = papa; bare 2 = o | r06 volunta del [Papa]; v03 "che 'l [Papa] vuole"; v05 "haranno da [Papa]" | probable; never "o" here; no points written |
| 2 + vowel | b as often as c | c (b by sense) | b: r04 su-BI-to, r14 BI-sogna, r18 u-BI-dientia, v01 BE-nefitio; c: cose, costoro, secreti, facessi, magnificentia | confirms polyphony |
| 9 + vowel | z as well as v | v (9^4 = ze alt.) | r10, r12, v05 sen-ZA (9^5); v01, v03 forte-ZE (9^4) | sure |
| bare 4 (after "di", "et", "e") | Maestà / Sua Maestà | .4. = cristianissimo; 4 = g | r06 "et [S. M.] mi ha detto"; r08 "pratiche di [..]"; v04 "e [S. M.] mi [ha] detto"; with a point r10, r12 "honore di .4."; r20 "parlero a .4." = clear "al Re"; v02 "di [questa M.]" | sure for the referent (the French king); wording of the clear only partly read |
| "6 4" (no points) | S. Severino | .64. = santita | r11 "sendo amico di [64]" = clear "amico di S. Severino" | one occurrence, no points, other year: differs from v6, not a refutation (bare 6 + bare 4 = s + Maestà not excluded) |
| "5 1", "1 5" (no points) | Rubertet (Florimond Robertet) | .51. unresolved in v6 | r18 "opera con 51"; r19 "et 51 mi ha detto"; r15 "messo avanti da 15" = clear "Rubertet" written above a struck word | probable: my pre-decode notes already had "Ruberto.." twice in clear lines 19-20; answers Dudout's open .51.; r15 is clearly written 1-5, r18/r19 5-1 (crop c190_codes_15_51.png) |
| "9 7" (no superscripts) | ? (name after "lettere di") | absent | r04 "le lettere di [9 7] si dettono subito"; clear word not read | open |
| A | bene | A = m | r08 "non stanno BENE in man di tanti"; v04 "sarà BENE mandarl[o]" | sure for the crossbar capital A; the r07 sign is an arch/triangle, perhaps a different sign (Dudout's Δ), unread |
| L^r (L with small r) | Vostra | absent | r04, r20 "la Magnificentia [V.]" | sure |
| L^- (L with long bar) | quanto / quando | absent | r05 "et QUANTO al maneggiare"; r17 "et in QUANTO alla legatione"; r19 "QUANDO haro occasione"; r14 unread | probable |
| L^. (L/V with dot) | voi | absent | r12 "mi dixe VOI dite el vero" | 1 occurrence |
| V^0 / V^. | tempo | V^0 = null | r16 "lascero fare al TEMPO"; v01 "secondo che mi parra el TEMPO"; r03 as opening mark | probable; CONTRADICTS v6 null (except at r03) |
| D^1 | chi | absent | r07 comuni-CHI; r12 ri-CHI-amarlo; v04 "da CHI maneggia" | sure |
| D^c / D^m | come | absent | r13 "COME fussino terminate" | 1 occurrence |
| T^0 | secondo | = v6 | r05, v01 "SECONDO che mi parra" | confirms v6 |
| T^5 / T^s | Sua Santità | absent | r21 "servitore di [Sua S.]" | 1 occurrence |
| F^0 | essere | absent | v03 "doverrete ESSERE avisati" | 1 occurrence, clear word cipher-assisted |
| M + "o_" | Nostro (N. Signore) | absent | v01-02 "benefitio di N. S." | 1 occurrence |
| M ("2h"-like ligature) | non | = v6 M | r08, r09, r11 x2, r15, r19, v05 | confirms v6 |
| α, qu, D, D^n, F, t#, n#, r#, g#, c#, 4# | per, più, che, con, et, tt, nn, rr, gg, cc, ll | = v6 | throughout (4# = ll: quella, quello x4, alla, dell') | confirms v6 |
| f# (tall ft ligature) | ff | absent | r21 o-FF-icio | 1 occurrence |
| S^4, S^5 | que, qua | = v6 | queste, questa, quello, qualche, di qua | confirms |
| 6 bare / 6 + vowel | s / p + vowel | = v6 | costoro, questa / participi, puo, possono, opera | confirms |
| y bare / y + vowel | n / f + vowel | = v6 | confusione, fare, fussino, forteze | confirms |
| r + vowel | s + vowel | = v6 | si, subito, secreti, solieri, marsilia | confirms |

Not attested here: B (ancora), T bare (senza is spelled out r^4 y 9^5), Ł, ql, J, H, K, p-series beyond bare p = u.

## (c) Shape legend for this hand

| name | looks like | confusions | clean example |
|---|---|---|---|
| 7 | plain 7, flat top | r; the tail of a preceding sign | r03 "7^4" (lette-re) |
| r | 7 with a hooked/looped top, like ɤ or a small v on a stem | 7 (r = s+vowel, 7 = r+vowel: check the hook) | r04 r^1 (su-bito), r06 r^3 (monsi-) |
| d | small uncial d, ascender curling left, open bowl | G; the flourish of 6^x | r06 d in ma-R-silia |
| G | large closed delta/loop, taller than d | d: not separable at 1272 px; decide by word (g only before n, r, l) | r06 G in monsi-G-nore |
| 3 | 3, bare form often tall with a tail (= a) | 5, ʒ-like 2 | r04 3^4 (de) |
| 5 | s-shaped 5, small | S (S is twice as large, angular, hooked) | r04 5^5 (ma) |
| S | big angular S with top hook | 5; O^5 | r13 S^4 (que-ste) |
| 2 | z-like or flat lying 2, always with a superscript | Z when the superscript is shifted | r05 2^2 (co-se) |
| Z | same flat lying 2, bare, on the baseline | the superscript "~" (= o) of a neighbour; figure 2 = Papa | r10 Z (in-t-rometter) |
| ~ (superscript) | flat tilde above a sign = 2 = o | Z | r04 t^2 |
| 6 | bare: sigma-like, low; with vowel: tall with long right-swept ascender | the ascender read as an extra d; G | r05 6 (co-s-toro), r07 6^5 (pa-re) |
| ƀ | 6/b with a bar through the ascender | 6^x, t# | r05 (manegg-i-are) |
| 8 | closed 8 | ȣ (open top, smaller) | r04 8^2 |
| ȣ | small 8 with open/forked top, like ɣ | 8, O, 0 | r07 (quell-o) |
| O | ɔ / ">" open to the left | 7, 0 | r04 (dett-o-no) |
| 0 | small closed circle | O, ȣ | r06 (de-c-to) |
| Ø | circle with a slash | 0, Φ | r16 |
| Q | ß/β-like with stem (e) | qu, α | r03, r07 (soli-e-ri) |
| qu | Q-loop with a long flourish running right under the next sign | Q (no flourish), α | r15 "andar qu avanti" |
| α | a/Q-loop with an x-shaped crossing tail | qu | r10 "α marsilia", r15 |
| 9 | q-shape with straight descender | g# (9 + double bar) | r04 9^4 |
| 4 | open 4; 4# = large angular 4 with long tail + double bar | 9 | r05 4# (que-ll-a) |
| x / c | x cross / small c (both l) | y for x when tail long | r03 x^4; r04 c (de-l) |
| y | y with long left tail (n; f with vowel) | x | r04 y^3 (fi) |
| t | small barred t (n) | r | r04 t^2 |
| D / D^n / D^1 | square box D; small n or stroke above | each other (look above the box) | r07 |
| M | "2h"/"dn" ligature with tall right stroke | D^n | r09 "M 6^1 O" (non puo) |
| W | ϖ, omega with bar | t# | r08 (i-n) |
| Γ, π, ʃ#, L^r, L^-, V^0, A, T^0 | see (b) | Γ vs J/long s; L^r vs L^- (look inside the L) | r06, r04, r11, r20, r05, v01, r08, r05 |

Which sign is b: none of its own; b is 2 + vowel (same sign as c). Superscripts sit up to one sign right of their base.

## (d) What the clear copy does not cover

- 191 has two lines before "arrivò adì xx la sera" that correspond to 190's clear opening (not cipher).
- It ends "Nec plura" exactly where the cipher ends (190v.06), omitting 190's clear close; 79573 has no text.
- The six struck signs on r04 and the overwritten signs on r14/r18 have no counterpart.
- Not aligned (clear unread there, not shown to be absent): "9 7" (r04); r05 "la n-ra-ne da" (clear "lo andamento"?);
  r07 "con m-n-f-n-to-n-tt-o" (clear "Con ... ho hauto"); r08 end to r09 start; r10 start "te-n-g-a-i-no";
  r14 "che ma-l-l-h-u-n vo-ri-mi-n-ga [quanto]"; r20 "de-Φ-t-ri"; the nine stained signs of v01; v03 end "da v-r-o".
