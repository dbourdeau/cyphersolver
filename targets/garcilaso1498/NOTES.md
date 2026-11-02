# Ferdinand II to Garcilaso de la Vega, 31 August 1498: the passages in Garcilaso's cipher (catalogue no. 349)

Status: attempted, open. The two passages in the second cipher are located, transcribed and attacked; every key
reachable online was tested and excluded. The likely key is in RAH Colección Salazar y Castro A-11, which is not
digitised.

## The target

Barcelona, ACA, Diversos, Sástago 193 (Lío B), nº 79/83 = DECODE R10180 (7 images, "Authentication required";
DECODE status Non-decrypted). Parisi 2004 doc. 83 (ff. [134–137]): Ferdinand to Garcilaso de la Vega, his ambassador
in Rome, enclosing a copy of what he wrote to Joan Ram Escrivà at Naples on the general peace with France. Endorsed
"A Garcilasso", "Cifra d'Espanya de ses alteses 31 d'agost 98", "N. 83".

The letter is in two hands and two systems (Parisi n. 13, n. 71, n. 89):

| part | where | cipher | state |
|---|---|---|---|
| head, 1 line + 4 signs | image P5, above "Copia" | Garcilaso's cipher (the "fourth variant") | unread |
| "Copia" (the Escrivà letter) | P5–P7, P1–P4 | Escrivà cipher no. 2 | printed by Parisi 2004, pp. 105–109 |
| ten lines before the date | foot of P4, then "xxxi de agosto de xcviij" in clear and two rubricas | Garcilaso's cipher | unread |

Parisi printed the body and left both Garcilaso passages as "[...]": "este sistema no ha sido todavía descifrado"
(n. 13). The DECODE image order is not the folio order: P5 (with "N 83" and "Copia") is the first page.

## What was checked first (26 Oct 2026)

- Prior solutions: Parisi 2004 (UB mirror `revistes.ub.edu/index.php/pedralbes/article/view/35612`, the RACO copy
  is behind a Cloudflare check; `lit/parisi2004.pdf`), Tomokiyo's `unsolved.htm` and `spanish.htm` and his 2019 blog
  post (no comments, no solution), Cryptoole IT1498-1 (open), the DECODE record and siblings R10172–R10179 (all
  Escrivà letters of the Parisi corpus, none in this system). No reading exists anywhere.
- Parisi n. 13 names the probable key: RAH Salazar A-11 doc. 1067, a cipher letter of Garcilaso to Ferdinand of
  3 Oct 1496, whose decipherment is doc. 1076 (Galende 1994 gives it as RAH 9/11 ff. 109–111). Villanueva Morte's
  Claver monograph (Zaragoza 2025, `lit/claver2025.pdf`, n. 152) cites a second one: Garcilaso to the Catholic Monarchs,
  31 Dec 1496, A-11 ff. 121r–125v, "descifrado en ff. 125rv". Neither is on DECODE; the RAH Biblioteca Digital
  catalogues Salazar items but has none of the A-11 letters (searched for Garcilaso, Garci Lasso, Lasso de la Vega,
  embajador en Roma, Alejandro VI, Claver, A-11). D. W. McPheeters, "Una carta desconocida de los Reyes Católicos a
  su embajador en Roma, Garcilaso de la Vega" (1989), not seen.

## Keys tested and excluded

**BRAH 9/15 (Galende's "Cifras de los Reyes Católicos") is on DECODE**, as key records R9815–R9832 and R9486
(all "N/A", 1600–1699 dates are wrong): the esp318 NOTES say 9/15 "is not online"; it is. Images fetched to `key/`
(git-ignored). Compared sign by sign with the postscript:

| key | DECODE | why excluded |
|---|---|---|
| ff. 11–14v, Alonso de Silva ↔ Garcilaso | R9822 | alphabet has 9 = m, ʒ = v, ∝ = d, < = q, ⊤ = o, but no Λ, π, To, ⧺o, β-forms; 9 occurs 17× in 315 tokens, too often for m. Its code groups (VC for A-words, CVC b-/c-/d-/e-/f-/g-) look like the superscripted pairs (aᵠ, eᵗ, aᶠ), but the frequent signs are not in the alphabet |
| f. 16, a Rome cipher of c. 1495–96 (pope, College, S. Pietro in Vincoli, vice-chancellor, cardinals of Naples, Cartagena, San Giorgio) | R9823 p2 / R9824 | name capitals coincide (B, M, T, R, H, π), but the alphabet (Latin-letter substitutes with ^ marks) has none of Λ, ∠, To, zh, β. Galende calls f. 16 "fray Juan de Mauleón"; the name list is a Rome list |
| ff. 7–10, Cifra general | R9821 (Galende app. 1, `../esp318/keys/`) | different alphabet |
| ff. 1–6 Cifra del visorrey, f. 15 (Muros, Latin cover names), f. 17 (Latin-letter substitution with syllable names), f. 18 (Don Juan Manuel), ff. 19–25 | R9815–R9820, R9823 p1, R9825–R9832, R9486 | different sign sets |
| Escrivà ciphers no. 1 and no. 2 | Parisi 2004 pp. 70–73 | shares π, Λ, ∝, ∞, ⧺ as shapes, but read with alphabet 2 the postscript gives nonsense (z would be the commonest letter); Parisi tried both |
| RAH 9/7–9/8 letters (Ferriz 1475, Leonor 1476, Carrillo, Claver 1500) | R9483–R9485, R9591 | different systems |

## Transcription

`ct.txt`: both passages, one row per written line (H0, H0b, L1–L10), 315 tokens, 79 types (57 when superscript
variants are folded into their base sign). Read by eye from 2× crops of the DECODE images (`img/`, git-ignored).
Sign names are explained in the file header. The ten lines have two water-stain lacunae (L1 mid-line, L3–L4 middle).
Confidence is moderate: several base signs (β with ring, β with z-tail, tall ß, the stacked ʃ/4) are close in shape, and
superscript letters are often uncertain.

What the transcription shows about the system:

- Most signs are symbols (Λ with a dot, ∠ with a dot, π, ⧺o, T with o, 9, ʒ, β-forms, ꝏ, zh), each frequent:
  the seven commonest cover 40% of tokens, so this is homophonic.
- Lower-case Latin letters with a superscript and a point (aᵠ·, eᵗ, aᶠ, aˢ, aᵈ, bⁿ·, hⁿ·, gᵉ·, kᵉ:) are frequent
  (about 40 tokens). They look like code groups written as letter + superscript, the style of the Silva–Garcilaso
  code (ab, eb, … bag, beg …).
- Capitals B, M, R, T, H occur as single signs: name codes.
- Repeats: "π bong zh" (L1, L6), "ꝑ π" ×5 (also in the head line), "aꝛaꝛ" ×4, "eꝛeꝛ".
- Ferdinand was at Zaragoza on 31 Aug 1498 (Cortes; princess Isabel died there on 24 Aug, prince Miguel was born on
  23 Aug), so the cipher before the clear date may close with the place. The crib "çaragoça a" fits the last tokens
  only if Λ = g, which its frequency rules out.

## Ciphertext-only attack

`solve.py`: homophonic annealer, one letter per sign type, 5-gram Spanish model without spaces built from
es-golden-age plus Parisi's printed Ferdinand–Escrivà texts of 1495–98 (×5), with a unigram (KL) penalty
against collapse onto vowels. `control.py`: the same annealer on 315 letters of Spanish from es-gutenberg (not in the
model) under a 57-symbol homophonic key.

Results (26 Oct 2026, `run_merge.log`, `run_control.log`):

- On the postscript (57 folded types, 315 tokens), restarts give different, non-Spanish strings at -2.7 to -3.0
  nats/char ("saitiocastiaeldesleaneracerea…", "qeicareniraelesabererrendo…"); no two agree. Without the KL penalty
  the annealer collapses to "iiieeaa". The campaign was stopped after seven restarts once the control had failed.
- Control: on clean synthetic ciphertext of the same length and homophony, six restarts of 250,000 steps recovered
  0–29% of letters (best -2.46 nats/char, "seyendoaencandeador…" for "resentoaestostiologos…"). So 315 tokens under 57
  homophones are below what this method can break even with a perfect transcription and no nomenclator. The real text
  also has code groups, name signs and transcription doubt.

Conclusion: the passages cannot be read ciphertext-only at this length. They need the key, or more text in the same
cipher.

## Remaining gaps

- Head line (H0, H0b; about 35 signs) - blocker: no-key-material; Garcilaso's own cipher, whose deciphered specimens
  are in RAH Salazar A-11 (ff. 109–111 and 121–125), not digitised
- Ten-line postscript (L1–L10; about 280 signs) - blocker: no-key-material; same key; ciphertext-only fails at this
  length (see control)

## Escalation

- [x] siblings: DECODE R10172–R10179 (Sástago 193) are Escrivà letters; no other letter in this system on DECODE
- [x] clear pages: the letter's clear endorsement and date only; the body is the Escrivà copy, already printed
- [x] known-keys: all of BRAH 9/15 (R9815–R9832, R9486), Escrivà 1 and 2, the Cifra general, RAH 9/7–9/8 records; none fits
- [x] print: Parisi 2004, Galende 1994, Villanueva Morte 2025, Tomokiyo; McPheeters 1989 not seen
- [x] key rebuild: ciphertext-only homophonic annealing with an in-domain model; failed (control below the bar)
- [ ] print/archive (next): AGS Patronato Real on PARES may hold Garcilaso's own Rome despatches of 1494-99 with their decipherments; the PARES search returned HTTP 429 (rate limit) on 26 Oct 2026, both scripted and in the browser, so it is untried. Search `catalogo/find?texto=Garcilaso de la Vega&anio1=1494&anio2=1500` first
- [x] print (later, 26 Oct): BNE holds five Garcilaso letters (datos.bne.es XX1338429: to the Monarchs 8 Nov [1496], to Cisneros, to Ferdinand 25 Aug 1500, to Almazán [1493]), none described as ciphered. Usoz printed his clear letter to the Monarchs of April 1498 (San Sebastián 1842, IA `cartalosreyesdf00spaigoog`): Cesare Borgia's Neapolitan marriage, the Calahorra bishop's trial, the infanta María and the duke of Calabria. Topics only, no crib that aligns with the postscript signs
- [ ] retry: needs images of RAH Salazar A-11 ff. 109–111 and 121–125 (Garcilaso's cipher letters with their
  decipherments); request from the RAH, then rebuild the alphabet and code from the 1496 letters and apply it here

## Files

- `ct.txt` transcription; `solve.py`, `control.py`, `run_*.log` solver runs
- `lit/parisi2004.txt` (the model corpus); the Parisi and Villanueva Morte PDFs and the Tomokiyo pages are kept locally, git-ignored
- `img/`, `key/` DECODE images (git-ignored; not public domain)

## Dudout corrections, 29 Oct 2026
- ct.txt checked sign by sign on the full-resolution R10180 P4/P5 images: about 310 of 315 tokens agree. Suggested: H0 token 28 g^n is the same sign as L6 y^n (so y^n); L1 has a superscript 'oto' over S8 b (not noted); L5 ends with an extra division mark after BB; L7 has a three-dot mark between B and BB; L2 opening '? i' is more likely '- TA'. No key found: the Gran Capitan keys cover only 45% / 37% of tokens by shape.
(Brice Dudout, research/dudout_2026-10-29/; his findings, not re-checked here.)
