# Richelieu-Rancé cipher, July 1629: the key

Copied verbatim from SOLUTION.md ("Cipher system"), 22 Oct 2026. The same key is in `final.py` (KEY, NOMEN).

## Cipher system

Homophonic substitution, two-digit figures, with a small nomenclature.

| Symbol | Letter | Symbol | Letter | Symbol | Letter |
|---|---|---|---|---|---|
| 10 | c | 17 | f | 24 | m |
| 11 | b | 18 | t | 25 | s |
| 12 | g | 19 | a | 26 | u/v |
| 13 | p | 20 | d | 27 | e |
| 14 | l | 21 | i/j | 28 | q |
| 15 | o | 22 | n | | |
| 16 | r | 23 | h | | |

- 10–28 = the 19 letters a b c d e f g h i l m n o p q r s t u in a scrambled order (no x y z observed).
- 29 30 31 32 33 = a e i o u and 34 35 36 37 38 = a e i o u — two extra homophone sets for the vowels
  (33 = u confirmed by Avenel's "ne piquer" = 22 37 13 21 28 33 30 16).
- **Tilde/diacritic = doubled letter**: ~14 = ll, ~22 = nn, ~25 = ss, ~30 = ee (d'e**ll**e, bo**nn**e, do**nn**er, Bra**ss**ac, amba**ss**ade, maitre**ss**e, men**ee**).
- 39 = "et" (23 Oct 2026, from Avenel's footnotes: *frontière et menée*, *Chevreuse et autres*, its only two occurrences; the 22 Oct key had 39 = a, from Tomokiyo's partial transcription read as *amenée*); 40 = "de", 42 = "la" (word codes).
- ≥41 = nomenclature. Identified (this work + Avenel's footnotes across vol. III):

| Code | Meaning | Code | Meaning |
|---|---|---|---|
| 51 | le Roi | 60 | Mme de Longueville |
| 52 | la Reine mère (Marie de Médicis) | 66 | le cardinal de La Valette |
| 54 | Monsieur (Gaston d'Orléans) | 83 | l'Espagne / le roi d'Espagne |
| 58 | la duchesse de Chevreuse | 84 | l'Angleterre |
| 59 | la princesse Marie (de Mantoue) | 92 | la Lorraine |

  Cleartext jargon also used: *Castor* = le Roi, *Lysandre* = la Reine mère (Avenel).

## Extension from fr. 3828, 3825, 3835 (Nov 2026)

Added by Brice Dudout (with Claude Opus 5.5), 19 Nov 2026, when the key above was applied unchanged to the nine
sibling letters that Avenel prints with their figures (t. III, nos. CXIX, CXXXV, CXLVI, CXLVII, CLIII, CLIV, CLV,
CLVIII, CLXVII; `fr3828_reading.md`, `fr3828_method.md`). The letter values 10–38 and the word codes 39, 40, 42 are
unchanged. The entries below are **taken from Avenel's footnotes**, each at a place where his note glosses the figure
and the decoded runs next to it agree with the note; none comes from the two letters held out for the test (CLIV,
CLV). Like the earlier nomenclator entries, they rest on Avenel, not on the ciphertext alone.

| Code | Meaning | Source (Avenel t. III) |
|---|---|---|
| 41 | *que* (word code) | CLXVII n. 9: 39 41 59 … = "et que la princesse de Mantoue s'en allast" |
| 55 | M. le Prince (Condé) | CLIII n. 5 |
| 61 | le duc d'Épernon | CLIII n. 7 |
| 62 | Montmorency | CLIII n. 10 (Avenel: the value is sure, though Ventadour made the *dégât* of Castres) |
| 67 | Calori | CLXVII n. 2 |
| 68 | le cardinal de Bérulle | CXIX n. 4; CLXVII n. 4 |
| 69 | le garde des sceaux (Michel de Marillac) | CXIX n. 13; CXLVI n. 12 |
| 95 | Nismes (Nîmes) | CLIII n. 9 |
| 96 | Castres | CLIII n. 8 |
| 97 | Montauban | CLIII n. 5 |

Usages noted, not new values:

- **40 = de** also stands for the syllable *de/dé* inside words: *bor-de-aus*, *ambassa-de*, *ambassa-de-eurs* (sic,
  40 followed by 30 = e), *s'acommo-de*, *se dé-portast*, *dé-livrer*, *d'Elbeuf* (40 + lbeuf).
- **20** (d) is used as the **number** in "le 20 mai" (CLIII, CLIV, CLV twice); Avenel, CLIII n. 12: "en traduisant
  dans cette phrase 20 par d, il n'y a pas de sens". The key is not changed; the reading marks these places.
- **59**: "princesse Marie" (Marie de Gonzague) in CXXXV and CLXVII, as in the table above; in CLVIII Avenel glosses
  it "M. de Mantoue" twice and calls it a slip of the secretary. Not settled: the table keeps "princesse Marie"; the
  reading of CLVIII follows the gloss and marks it.
- **84** "l'Angleterre" also gives "les Anglois" / "Angleterre" by context (CLIV nn. 4, 10–12, test letter; not added).
