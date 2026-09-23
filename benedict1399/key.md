# Benedict XIII – Climent cipher, 1399–1400: key rebuilt from the p. 475 facsimile

Rebuilt 23 Sept 2026 from the only image of the ciphertext, Puig y Puig, *Pedro de Luna* (1920), p. 475: a halftone
of the last page of app. XXXV (Benedict XIII to Climent, Avignon 22 June 1400, ACB doc. 1068), read against
Puig's own printed text of the same page (italics = deciphered). Known-plaintext rebuild, not a ciphertext-only
break: the reading is Puig's. Puig never printed his key; this is the first printed form of it.

Image: Google Books `CuOlkxWnk-EC`, PA475, 1826 × 2500 px (the largest served), cropped, rotated 90°, deskewed
−0.7°, lines found from the ink profile (26 lines, about 38 px apart), each cipher run zoomed 3–5× with
autocontrast. Word-by-word check: `src/plate475_check.tsv`.

## System

Simple substitution, one sign per letter, no homophones seen, no word division (signs joined by hair-lines),
mixed into clear Latin, with one name sign and groups of separator signs. Many signs are letter-shaped
(o, n, T, b, δ), so a run looks like scrambled minuscule.

| plain | sign (as it looks on the plate) | seen in, e.g. |
|---|---|---|
| a | open δ-like hook (ɣ) | atentis, quam, Catalonia, factas, alias |
| b | T with a bar (Ƭ) | sibi (×6), debet, deberet, nobis, dubitamus, tribulacione |
| c | small o (as i) | cum, duce, dices, hic, contenti |
| d | double cross ‡ | duce, de, ideo, diceres, deficere, quod |
| e | δ | et (×6), deberet, remanere, necessitatem |
| f | Ϭ (σ with a flag) | factus, facto, futurum (×2), deficere, suficere |
| g | 4-like sign (ɕ) | negocium, negociis, cogitare, congedio |
| h | 2-like / ʒ-like sign | hoc, habet, habere, hic |
| i | small o (as c) | ideo, sibi, modis, qui, detinent |
| l | ϑ (looped d) | velit, alias, tribulacione, Catalonia, cancellarius |
| m | ɛ with a foot (t-like) | cum, sumus, mentem, remanere, modis |
| n | n | in, nobis, contenti, detinent, remanere |
| o | double loop ꝏ | modis, nostrorum, nos, contenti, con- |
| p | ⊥ (inverted T with a stroke) | placet, recipiat, expensis, respectum, prout, potes, poterimus |
| q | ⊧ (double-barred upright) | quod (×9), quam, quia, qui, quasi |
| r | single upright (ı) | diceres, atribueret, remanere, istorum, adversariorum |
| s | T | sibi, est, sed, suam, statu, nostris |
| t | c with a superscript stroke (c′) | et, tu, statu, atentis, contenti, detinent |
| u / v | cb (a joined pair, one sign) | cum, duce, sumus, vero, velit, voluntatem |
| x | ɑ-like sign | expensis, ex, Ambaxiatis |
| Rex / Regis Aragonum | dotted V (V̇) | lines 1, 6, 9, 10 |

The letter o is a double loop (ꝏ), c and i a single small o: *modis* is ɛ ꝏ ‡ o T, *contenti* o ꝏ n c′ δ n c′ o,
*hic* ʓ o o. Found on a 5× re-read of line 24 (the first pass had merged ꝏ into two o's). c and i still look alike
on the 1920 halftone; the original may separate them by a tick or dot. d and p look alike at this resolution (both barred uprights); where they could be
separated, p is ⊥ and d is ‡.

**Separators.** Groups of λ-, ʒ- and ɑ-like signs (λʒ … λʒ) stand at four places: line 4 (Puig ";"), line 8
between *nostris* and *De facto* (Puig "—"), line 17 after *necessaria* before the clear *De collectore* (Puig
"—"), and line 23 before *quasi territus*, the last with a dotted V and a barred p inside the group. Puig prints
nothing for them. They read as null punctuation marking a sentence break; the dotted V inside two of them is not
the King of Aragon, since the text does not name him there.

## Corrections to Puig's print (p. 475–476)

- *te sicudum* (line 4) → **tenendum**: the run is c′ δ n δ n ‡ cb ɛ, and line 3 ends *…sic negocium*.
  So the sentence is *et ideo est sic negocium tenendum in suspenso*, echoing the clear text
  just before it (*in suspenso tenendum*).
- *abique congerio* (lines 24–25) → **absque congedio** ("without leave"): ɣ Ƭ T ⊧ cb δ, then o o n | ɕ δ ‡ o o.
- *necesaria* → **necessaria** (TT on the plate).

## Measure

Plate cipher runs: 148 words, 826 letters of Puig's plaintext (name signs counted once, separators not counted).
125 words are confirmed sign by sign against the key, 16 have one to three signs too blurred to confirm, 7 are
in line 4's overwritten and underlined stretch and cannot be read on the halftone. That is 755 of 826 letters
confirmed (91.4%), and 96.3% of the legible runs. No sign on the plate contradicts the key.
