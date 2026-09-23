# Nevers to Villeroy, Saint-Quentin, 16 August 1595 — BnF fr. 3993 no. 102, ff. 148r–149r

Catalogue entry 277 ("new 22 Sept", class C, solve candidate with no known key). Session of 22 September 2026.

Status: attempted, closed from the evidence (not read). The key is not among the Nevers keys that survive, and
the runs are not a plain homophonic cipher: the solver that breaks a matched control of the same size fails on them.

## The document

* BnF fr. 3993 = Gallica `btv1b9059229n` (279 canvases, each a two-page spread; *Collection Mémoires de la Ligue*).
  f. 148r = canvas 161 (right half); ff. 148v and 149r = canvas 162. IIIF `full/full` gives 7640 × 6089 px spreads.
  Images in `img/` (git-ignored); `fetch.py` takes canvas numbers.
* BnF OAI record (`src/oai_3993.xml`): no. 102, *"Lettre, avec chiffre, de LOUIS DE GONZAGUE, duc DE NEVERS, à
  monseigneur de Villeroy,... De St Quentin, ce 16 aoust 1595". Copie.* It is Nevers's file copy in a secretary's hand,
  dated at the head "16 d'aoust 1595" and at the foot "De St Quentin ce 16 aoust 1595".
* The letter is in clear French with 17 inserted cipher runs (753 signs, first pass): one on f. 148r l. 7, a block of
  seven lines at the foot of f. 148r, four runs on f. 148v, four on f. 149r. The subject is the relief of Cambrai
  (besieged by Fuentes from mid-August), the loss of Doullens (31 July) and the council to be held.
* The opening explains why cipher is used: Villeroy writes "assez intelligiblement", but "ce qui est de plus pregnant
  seroit bon d'estre en chiffre ... affin que 72 ne puissent prendre cognoissance de noz affaires". The figure 72 stands
  in the clear text as a code for a plural party (the enemy).
* Tomokiyo (cryptiana, *League* page, 2018–19): "Portions in cipher. Undeciphered. The cipher uses figures and other
  symbols ... It seems none of the Nevers collection decodes these." No later publication found.

## Transcription

`ct_f148r.txt` (301 signs) and `ct_f148v_149r.txt` (452 signs), one token per sign, codes listed at the head of each
file. First pass from native-resolution line crops. Known weaknesses: the small circle `o` and the zero of `20` are not
distinguished; dots over figures (the `i` and `:` tokens) are not all recorded; `d` covers both the italic d and the
looped ∂.

Counts: `1` 112, `2` 92, `o` 74, `3` 35, `7` 32, `4` 30, `9` 28, then about 45 non-figure signs (ↄ, T, λ, π, θ, ∞, ‡,
ϖ, Δ, ∩, Ⱡ ...). `1` is followed by a figure 87% of the time; `2o` occurs 33 times, `41` 14 times. Read as two-digit
numbers wherever a figure is followed by a figure or o, only about 45 figures are left single.

## Keys tried (all ruled out)

| key | where | result |
|---|---|---|
| Balagny–Nevers alphabet | Tomokiyo's reconstruction from fr. 3993 f. 130 (`src/league12.png`) | different sign set |
| no. 76 | fr. 3995 ff. 142v–143r (canvas 274), read in full here | same sign family (λ, π, θ, Δ, #, ϖ, figures as letters), two-cycle word list (dotted 12–99 A–L, barred 1–100 M–V), names 59–90, towns 101–181; the assignments give no French and 72 is not a party |
| no. 75 "Chiffre commun entre messieurs les secretaires d'estat et messieurs du conseil" | fr. 3995 f. 140v (canvas 270) | figures only (A 90–99, E 70–79, I 50–59, O 30–39, U 20–29 ...); no fit |
| no. 66 | fr. 3995 ff. 122v–123r (canvas 235) | λ = n, π = o, θ = l; no French |
| no. 65 (Lesdiguières) | fr. 3995 ff. 120v–121r (canvas 232) | symbol + two numbers per letter, nulls 10, 20 ... 100; λ = B, π = O; no French |
| nos. 68–74 | fr. 3995 ff. 126–139 | Italian or figures only |

## Solver runs and controls

The first annealer (`anneal.py`, full rescoring, 40k moves) failed on everything, including its own control, so its
results say nothing. `hsolve.py` replaces it: one letter per unit, incremental 5-gram scoring (fr-1600-letters), a
letter-frequency penalty (all three French models rate "iiii..." above real French because of Roman numerals in the
corpora), 600k moves, 4 restarts.

**Control** (`control.py`): 753 letters of Henri IV's letters in the letter's 17 run lengths, enciphered with a random
homophonic key of 49 signs (e seven homophones) plus 3 nulls at 5%. `hsolve.py glyph` reads it letter for letter
(−1.84 per window, all three restarts identical).

**Target**, same solver, every unit model (per-window score; the control's is −1.84):

| unit model | units | best | restarts agree? | result |
|---|---|---|---|---|
| every sign a unit (`glyph`) | 753 | −3.13 | no | no French |
| 1x/2x figure pairs (`pair`) | | −2.80 | no | no French |
| every figure pair (`pairall`) | | −2.56 | no | no French |
| 1 + next sign (`prefix1`) | 643 | −2.91 | no | no French |
| figure pairs collapsed to their decade (`decade`) | 575 | −2.97 | no | no French |
| no. 65 design: pairs 11–64 letters, 10/20/... nulls, ≥65 codes (`n65`) | 526 | −2.54 | no | no French |

**Syllabic model** (`hsyl.py`: a unit is a letter or a consonant+vowel syllable, as in fr. 3995 no. 57 where figures
1–72 are syllables): the matched control (`control_syl.py`, the same plaintext with 70% of CV syllables as two-digit
figures) is not solved either (−2.14/char, gibberish), so this design cannot be tested at this length with this
solver; the target gives nothing (−2.16).

So the runs are not a one-sign-one-letter homophonic cipher under any of the six cuts. What is left is a mixed
nomenclator (syllables and word codes with marks the copyist dropped), which 753 signs cannot break without the key.

## Other letters checked

* fr. 3993 no. 133, Nevers to Villeroy, Saint-Quentin 18 August 1595 (ff. 173–174, canvases 186–187): all clear; it
  opens "Comme je vous escrivis devant hier", i.e. it follows this letter, but carries no cipher.
* Mémoires de Nevers (1665) t. 2, Gallica full text: the clear phrases of this letter are not found.

## Remaining gaps
- all 17 runs (753 signs) - blocker: no-key-material; the key is not among fr. 3995 nos. 1-76 (Tomokiyo; nos. 65, 66, 68-76 re-checked here), the as-sent letter to Villeroy is not located, and a syllabic nomenclator of this size is beyond ciphertext-only attack (its matched control fails)

## Escalation
- [x] siblings: fr. 3993 no. 133 (18 Aug, ff. 173-174, next letter to Villeroy) is all clear; nos. 22 and 46 are listed as plain copies; the Balagny and Charles de Gonzague ciphers of the same weeks are different systems
- [x] clear-pages: none; the copy has no decipherment and no gloss
- [x] known-keys: fr. 3995 nos. 65, 66, 68-76 read or checked on the image (no. 76 read in full: same sign family, different assignments); Balagny alphabet (Tomokiyo)
- [x] print: Memoires de Nevers (1665) t. 2 full text searched (exact phrases), not printed; Tomokiyo's League page lists it undeciphered; web search found no edition
- [x] key-rebuild: ciphertext-only anneals under six unit models, validated on a matched homophonic control that solves; the syllabic model's control fails
- [n/a] retry: nothing was read, so there is nothing to regrade
