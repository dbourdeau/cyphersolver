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

### Where each base code comes from (20 Nov 2026, question on #813)

The ten base codes above were entered on 14 Sept 2026 (commit 2787a883, "this work + Avenel's footnotes across
vol. III") and left unchanged on 23 Oct 2026, when only 39 was corrected. No source letter or note was recorded for
them then; `avenel.py` searched the OCR of the whole volume. What the printed volume gives (page images checked for
`ff87-89_avenel_figures.txt`, `fr3828_avenel_figures.txt` and `avenel3_others_figures.txt`):

| Code | Occurs in ff. 87, 89 | Avenel's glosses |
|---|---|---|
| 51, 52, 58, 66, 83, 84, 92 | yes | his notes to ff. 87, 89 themselves (CXCIX pp. 368-369, CCV pp. 381-383) |
| 54 Monsieur | no | notes to the nine letters: CXXXV p. 263 n. 2; CXLVI p. 275 nn. 4, 6; CXLVII p. 277 n. 8; CLIV p. 294 n. 3; CLVIII p. 301 n. 5; CLXVII p. 321 nn. 6, 9. Outside them: CCCXIV p. 570 n. 9 (March 1630) |
| 59 princesse Marie | no | notes to the nine letters only: CXXXV p. 263 n. 1 ("La Longueville et Marie de Mantoue"); CLXVII p. 321 nn. 8, 9. CLVIII p. 300 nn. 5, 6 and CCCXIV p. 570 n. 6 gloss it "M. de Mantoue" / "duc de Mantoue" |
| 60 Mme de Longueville | no | notes to the nine letters only: CXXXV p. 262 n. 4 ("Dans ce chiffre, 60 signifie toujours Mme de Longueville"), p. 263 nn. 1, 3; CLXVII p. 321 n. 8. (60 in CCXLV belongs to Châteauneuf's cipher, another table.) |

So 59 and 60 can only have come from Avenel's notes to these nine letters, and 54 most probably did (eight
glosses there, one elsewhere, in 1630). Under the owner's rule on #813 (a value taken from Avenel's note to one of
these nine letters is a hole where it is counted) all three are counted as holes in the nine letters
(`fr3828_measure/word_count.tsv`: 337/375). They do not occur in ff. 87, 89; in the 1630 pieces a value fixed from
the 1629 letters is a value from another letter and stays sure.

## Extension from fr. 3828, 3825, 3835 (Nov 2026)

Added by Brice Dudout (with Claude Opus 5.5), 19 Nov 2026, when the key above was applied unchanged to the nine
sibling letters that Avenel prints with their figures (t. III, nos. CXIX, CXXXV, CXLVI, CXLVII, CLIII, CLIV, CLV,
CLVIII, CLXVII; `fr3828_reading.md`, `fr3828_method.md`). The letter values 10–38 and the word codes 39, 40, 42 are
unchanged. The entries below are **taken from Avenel's footnotes**, each at a place where his note glosses the figure
and the decoded runs next to it agree with the note; none comes from the two letters held out for the test (CLIV,
CLV). Like the earlier nomenclator entries, they rest on Avenel, not on the ciphertext alone. Under the strict count (owner's decision on
#813, 19 Nov 2026) a value fixed from the printed decipherment of the same letters, or from context, is a hole where
it is read: writing it here does not make the word sure (`fr3828_method.md`).

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
