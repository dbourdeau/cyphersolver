# Shape pass on `^`, `C` and the dotted rare codes (full-resolution crops)

Method: I segmented img/p1, p2, p3 and p6 into ink components at full resolution and drew numbered bands. I matched every token to its component by reading each line against its token list, and cut contact sheets from the original pixels without downscaling. This file's line references are `line#token-index`, counted on the v7 token list, bracketed items included.

## 1. `^`: two shapes, two values

69 of the 71 `^` tokens were located. The other two turned out not to exist (see below).

| shape | description | value |
|---|---|---|
| **upright Δ** | a closed triangle with a vertical or slightly slanted left side and a flat base | **n** (firm) |
| **arched Δ** | the left side is a long arc that starts left of and above the apex and sweeps down to the right corner. It is the same glyph as the `>` tokens (p1.24#21, p1.28#19, p2.01#25, p2.02#27, p2.05#18, p2.15#4, p2.22#8/#15, p3.02#28, p3.04#10, p3.09#22, p6.18#26) | **o** (= `>`) |

The two shapes separate cleanly: none of the 69 is in between. The shape predicts every place v7 had to read o "where n fails": "retourne" p2.28, "money" p2.32, the 1st Δ of "Cornwel" p6.05 (#20 is arched, #25 upright = n), "took" p3.07, "no gentleman" p6.07, "wold" p6.08, "toke" p6.10, "canone" p6.20, "on(e)" p6.03 and "how" p1.15. In "crownes" p1.06 the o is arched (#14) and the n is upright (#17). The n/o rule for `^` is therefore replaced by shape.

**Relabelled `^` to `>` (arched, o):** p1.04#28, p1.06#14, p1.15#15, p1.20#26, p2.08#30, p2.28#8, p2.32#16, p3.07#6, p6.03#36, p6.05#20, p6.07#29, p6.08#1, p6.10#17, p6.20#18 (14 in all).

**All other 55 `^` are upright = n.** They are p1.04#24/#32, p1.06#17, p1.08#3/#15, p1.10, p1.11, p1.12, p1.18, p1.20#16, p1.23-p1.30, p2.01-p2.05, p2.15 ×2, p2.19 ×2, p2.22, p2.25, p2.30, p2.32#29, p3.02, p3.05, p3.11, p3.16, p3.22, p3.24, p3.26, p3.27, p3.29 ×2, p3.30, p6.03#16, p6.04, p6.05#25, p6.07#21, p6.09, p6.16, p6.17, p6.20#12, p6.22 ×2, p6.23 and p6.27.

**Spurious tokens deleted.** On p1.16 "E > ^ mu" and on p2.24 "-8 > ^ J", the image has only one Δ-like glyph between the neighbours, and it is arched. The `^` token was a double transcription of the `>`. Both are removed: "{concludid}" now counts 9 signs and "{Compiegne}" 9.

## 2. `C`: two shapes, two values

18 of the 20 were located, and p1.11#13 and p1.12#13 were checked on separate crops, so all 20 are covered.

| new label | shape | value | occurrences |
|---|---|---|---|
| `C_X` | ꞓ with a **horizontal bar through the stem** | **s** | p1.11#13 (wyse), p1.13#7, p1.16#12 (advertisith), p1.17#21, p1.18#8 (some), p1.20#32 (occasion), p1.25#19 (Farnese) |
| `C_U` | the same looped c with **no bar** | **u/v** | p1.05#13, p1.10#27, p1.12#13 (retourne), p1.27#9, p2.31#0, p3.03#19 (untrew), p3.05#0 (-vertsmentes), p3.08#28 (much), p3.11#19, p3.17#24, p3.24#0 (countrey), p6.02#8 (rover/over), p6.11#6 (usid) |

Every place v7 read s has the bar, and every place it read u has none. The one exception is p1.17 "{use:3}". That C is barred, so it reads s. The word stays tentative ("(u)se"): the u would then have to come from elsewhere.

New readings that follow:
- **p1.10/11:** "the m**u**-steries" (C_U = u; was m{s}).
- **p1.27:** "hath none two **hund(red)** [?3] crownes". The run is `pt C_U ^ OMEGA` = h-u-n-d(ω). It parallels "fowre hundrid" on p1.28 and replaces "(tho)usand".

Also noted: `C_DOTBEFORE` p3.17 and `E_DOTBEFORE` (Monsieur de) are a small **plain c with a dot before**. `C_CEDILLA` (p3.09#5, p3.17#26) is the same plain small c with a **dot below**. Neither is the looped ꞓ.

## 3. Arched Δ: changes in reading

- **p1.04#28:** the run after "he" is b-o-(CD)-t-i-n (l o t i n). It is still unread ([?5]). "Lot(h)in(g)" does not fit the count.
- **p1.20#26:** `EE . > -8 E v C_X XX o/ xe mu` now reads "to {a} {o-c-(E)(v)-s-i-o-n = occasion}" (count unchanged).
- **p2.08#30:** the sign before `+. Y_ o/ b.` is o, not n, so "Plymtown" loses its n. It now reads "Pl{y}m{to}w [?5]".

## 4. Dotted rare codes compared with R354 (enlarged)

| label | image | R354 candidate | proposal |
|---|---|---|---|
| `.I` (p1.12, p2.15#31, p6.11#2, p6.13#0, p6.18#4) | capital I with top and bottom serifs, dot before | **Parma = Ī** (I with a bar); Mirandola = i̲ | Parma is the only I-shaped cell. It is tentative and **not applied**: "of [Parma] eny" p6.18 and "[Parma] undiscreetly" p6.11 do not read better than [?]. |
| `.M` (p2.14#1, p2.28 `. M .`) | dotted M with splayed legs | Trent (M4), already rejected in v7 | no other M cell; stays unread |
| `.d` (p6.02#21, p6.05#11, p6.13#24) | dot + a small closed loop with an arched stroke, like the arched Δ with a loop | none | no sheet match. It may be the arched-Δ o with a dot (compare `·>`), but that is untested |
| `N_DOT` (p6.05#4, p6.11#17, p6.26#7) | capital N + dot after | none (the sheet's capital-letter codes are G Council, M Trent, K clergy, Γ noblemen) | likely a name code missing from this copy of the key |
| `R_DOT*` (p6.12#15, p6.13#7, p6.24#10, p6.26#29) | capital R with a dot before or after (both forms) | none | as N: probably a name code not on R354 |
| `CIRC_BIG` (p3.24#23, p3.25#35) | large circle with a small loop inside at the top | **the queen's highness / her highness / your highness** (circle with inner top loop). This is the same cell as CIRC_LOOP | **"your highness('s) apointment"**, tentative, not applied (context "Monsieur de [CB] apointment") |
| `C_CEDILLA` (p3.09#5, p3.17#26) | plain c with a dot below | none; the nearest cells are "the said" (C) and "that they" (C with a dot inside) | no match |
| `Q_TAIL` (p3.04#25) | dot + small o with a long horizontal tail | none (the nearest is "It may like your L. to be advertised", a large curl, which does not match) | no match |
| `TALL_F_LOOP` (p3.17#4) | tall ſ with a loop at the foot | **Metz** (looped-foot f-like sign), weak | tentative only: "were him [Metz?] he" gives no sentence; not applied |

## 5. Re-read of p1.13-15, p1.18, p1.24

At full resolution the token lists match the image. No sign is missing, and none is mis-split, apart from the relabels above. What changes:
- **p1.13:** the C is `C_X` = s, so the run reads s-i/s-t-e-(3)-s-s-(y)-u/y-e-?-i before "the Constable". It is still no word, and it stays [?9].
- **p1.15:** `^` #15 is arched = o, which confirms "how". The opening run `ll CURL_D ? v g+ x= -2 P 7 xi e=` stays [?6].
- **p1.14, p1.18, p1.24:** no shape change. The p1.24 Δ (#23) is upright = n, and the `>` beside it (#21) is arched. The runs stay unread.

## Measure (final_v8.txt)

Same counting as v7: nulls per key_v6 plus E_DOT and r.; ':' '.' and bracketed clear text are not counted. My script puts p2 at 677 non-null signs for v7, against the 683 v7 reported. The comparison below is like for like.

| page | non-null | unread | tentative | firm % | incl. tentative % |
|---|---|---|---|---|---|
| p1 | 733 | 102 | 142 | 66.7 | 86.1 |
| p2 | 676 | 69 | 101 | 74.9 | 89.8 |
| p3 | 709 | 67 | 62 | 81.8 | 90.6 |
| p6 | 683 | 59 | 99 | 76.9 | 91.4 |
| all | 2801 | 297 | 404 | 75.0 | 89.4 |

(The same script on v7 gives 2803 / 296 / 406 = 75.0 / 89.4.) The percentages barely move. What the pass gains is certainty: 55 `^` and 20 `C` now carry their value by shape rather than by context.
