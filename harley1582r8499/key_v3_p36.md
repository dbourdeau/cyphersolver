# Key v3 for pages 3 and 6 (regrade 3, 2026-09-22): label -> value, with evidence

Labels are the tokens of transcription_v2.txt (p3.*, p6.*). Checked against the key images kc0-kc4 (alphabet),
key_low0-2 (nomenclator) and the line crops img/L/p3_*, p6_*. The reading is in final_v3_p36.txt and the measure
in measure_v3_p36.py.

## Changes from key_merged_p36.md / pin9_1.json (the ones that move the reading)

| label | v3 value | evidence |
|---|---|---|
| `/` (ı·) | **he** | nomenclator key_low2: "he" = ı· (slanted stroke + dot). "that he answered him" p3.14, "declared to Carew what he was" p6.12, "if he must detect many gentlemen" p3.28 |
| `Ie` | **I** | "and I have oft spoken with" p6.02, "whom I talked with ... I" p6.01. It is not in the key excerpt, so the value comes from context |
| `A=` | **me** (not "my") | nomenclator row "we us but for hath had have there this either whom is it **me** none": Ā = me. "it is told me that" p6.20, "he giveth me" p3.04 |
| `Y_ETA` (ŋ) | **us** | nomenclator "us" = ƞ. "took us as spyes" p6.10. It does not fit everywhere (p3.02, p3.05, p3.19, p3.28), so those places stay unread |
| `SS` (plain ß) | **r** | "return" p3.15 (+ ct a. pt SS mu), "to return" p3.22, "Cornwel" p6.03, "gather" p6.15 |
| `SS_TAIL` (ß with z-tail) | **w** | kc3: first w sign in the key. "unknown" p3.30 (pt mu H_OVERBAR ^ ll SS_TAIL J+), "whether" p6.06, "was" p6.23, "twise" p6.09 |
| `sy` (ß8) | **th** | kc4: "th" column, row 2. "giveth" p3.04, "I think" p6.07, "th'other" p3.22 |
| `SLASH_O_UND` (ƅ̲) | **ch** | kc4: "ch" column (secretary c looks like r), row 3 = ƅ̲. "charges" p3.01, "this charge" p3.18, "lantzknechtes" p6.17 |
| `zo` (ʒ8) | **th** | "it is thought" p6.24; "he think(eth)" p3.15-16; "Smith" p6.03; "th'other" p3.22 |
| `F_OVERBAR` (F̄) | **a** | kc0: 5th a sign. "charges" p3.01, "commandment" p3.25-26, "Paris" p6.21 |
| `C` (ꞓ) | **u** (not s) | kc3: u column, ꞓ. "advertisements" p3.04-05 (a d **u** e r t i s e n t e s), "Carew he desired" p3.08. p6.04 "divers" also reads with C = s, so C may still merge two signs |
| `y=` (ꝫ̄) | **w** (not y) | kc3: w column, ꝫ̄. "know" p6.05, "towardes" p3.09, "the way towardes" p6.21, "Cornwel" p6.03, "wordes" p3.08, "fault" p3.28 |
| `d+` (∂ with dot) | **i** (not a null) | "longing" p6.06, "service" p3.01, "desired" p3.08, "Saint" p6.22. The null row's ǂ· is a different sign |
| `S_DOTBELOW` (Ş) | **f** (the key's ꝸ·) | "forget" p3.19 (Ş ll + e/ # g+). Elsewhere (p3.01, p3.22, p3.25, p6.24) it does not give a word, so those stay unread |
| `O_SLASH` (ø) | **i** | kc1: i column, ø. "Saint Quentin" p6.22, "passed" p6.19, "ensieged" p6.26 |
| `E_OVERBAR` | **i** | "the Emperor's sisters" p6.15 (s ē s t e r s) |
| `XUND` (x̲) | **i** per the key; **s** in "service" p3.01 and "Paris" p6.21 | the key has x̲ = i ("Smith" p6.03). It still merges two signs |
| `X_BAR` | **s** | "twise" p6.09, "he used" p6.11, "whose" p6.14, "sisters" p6.15 |
| `SLASH_O` (\o, no bar) | **i** | "gentleman's living" p3.23-24 (l y u **i** n g). Unread at p6.07 and p6.19 |
| `CROWNED_BOX` | **England** | nomenclator key_low0: England = a dome on a base. "he came not fynde in his herte to return into England" p3.15; "live in England" p3.21 |
| `E_DOTBEFORE` (·e) | **Monsieur de** before CIRC_BIG (p3.24, p3.25); otherwise not established | key_low2: "Monsieur de" = e |
| `C_OVERBAR_E` | **w** (a C= misread, as the legend suggested) | "new" p6.17 |
| `OMEGA_DOT` (ω̈) | **z** (key z column: ω̈) | "lantz-knechtes" p6.17 |
| `H_OVERBAR` | **k** | "unknown" p3.30 |
| `B_OVERBAR` | **l** | "told" p6.20 |
| `Y_LATIN` (y·) | **t** in "oft spoken" p6.02 only | it does not fit anywhere else (p3.14, p6.03, p6.05, p6.14, p6.26), so those stay unread. It is probably a word code, not a letter |
| `e` (ε) | **null** | the null row's ε; image p6.01 shows ε. Needed for "I think" p6.07 |
| `H` | **y** normally; **u/v** (the key's ʜ) in "trust" p6.06, "over" p6.03, "releeveth" p3.17, "live" p3.21 | token merges H (y) and ʜ (u) |
| `+` | **r**; **q** in "Quentin" p6.22 | key r: +. and q: +̇, so the token merges two signs |
| `U_HOOK` | u/v; **r** in "charge" p3.18, "wordes" p3.08, "entre" p3.01, "sisters" p6.15 | the ʉ is under u in the key; the r uses are from context |
| `-8` (δ̄) | c; in "towardes" p6.21 and "know" p6.28 it stands where o is needed | unexplained: a slip or a second sign |

## Values kept from key_merged_p36.md

Nulls: 3, -2, r (ꞅ), q, q=, 9, ft, xo, rho (⤳), 0 (o.), th, 3r (ε), tl (~+), XX (✱), NULL_LOOP (ɞ),
NULL_LOOP_BAR, CE_UNSEEN; plus `e` (ε).

Letters: a = S, S$, v, xh, S+, v~, F_OVERBAR · c = E, -8 · d = 8/, Z=, Z, OMEGA · e = 8, ct, #, x=, L_ ·
f = b (ƀ; b = l in "gentlemen" p6.04), f, k · g = <, .S., E_SLASH · h = q+ · i = z, d, d+, .I., O_SLASH ·
k = h, nj, H_OVERBAR · l = #/, or · m = 7, J · n = ^, mu, J+ · o = xi, xe, ll, > · p = x, Dx, p · r = +, SS ·
s = Y+, P, f-, X_BAR · t = a., g+, Y_ · u = pt, F, s, C, U_HOOK · w = C=, y=, SS_TAIL · y = H ·
ch = SLASH_O_UND · th = sy, zo.

Codes (key R354, confirmed on key_low1/2): AND and · -w the · B of · B= shall · B_ should · D to · D= what (also
"wh-" in "whether" p6.25) · D_ was · EE were · EE= where · EE_ will · A= me · Ap none · q) it · (q) is · o hath ·
o_ have · o= had · H_ with · H= in · p) this · -4 that · C: that they · C. the said · G= who · w= whereunto ·
.G. Council · Too the Constable · n Carew · n= the rebels · O / O_DOTABOVE the Emperor · CIRC_DOT the French king ·
CIRC_RING your highness · CROWNED_BOX England · E_DOTBEFORE Monsieur de.

## Still open (unread in final_v3_p36.txt)

- CIRC_BIG (p3.24, p3.25): a person code after "Monsieur de", not on the key sheet as imaged.
- L_DOTS (p3.17, p3.24, p6.14, p6.25), C_DOTIN, C_DOT, C_DOTBEFORE, C_CEDILLA, C_HASH, Q_TAIL, TALL_F_LOOP,
  F_PLAIN, E_DOT, E_CROSS, P_, N_DOT, N_DOTBEFORE, R_DOTBEFORE, R_DOTAFTER, Y_ZHOOK, Z_SMALL_DOT, the plain `I`
  token, and the dotted `.B` (p3.01, p3.16): single-use or dotted variants. Most are probably word codes from
  nomenclator rows that are not legible on the key images. N_DOT fits "them" (p6.11, p6.26) but is not proved.
- Y_LATIN (y·) outside p6.02, and Y_ETA where "us" does not fit.
- Tokens that still merge two key signs: n (Carew ɱ / we ɱ / ɳ k), C (u/s), XUND (i/s), H (y/u), + (r/q),
  U_HOOK (u/r), -8.
