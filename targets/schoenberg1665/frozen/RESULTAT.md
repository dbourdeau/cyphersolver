# RÉSULTAT — schoenberg-1665 (mesure unique, 09/11/2026)

Chaîne de gels (SHA-256) : H-CHIFFRE.txt be650ff1… → PREREG.md e41effd7… → KEY.tsv 7239369c… → `scripts/measure.py`
(lexique cyphersolver `lang/lexicons/de.json.gz`, clone local HEAD 2d5b12ace3).

## Mesure (MESURE.json)
| H = L6–L9 | valeur |
|---|---|
| mots de H | 16 |
| **lis** (mots du lexique, fréq. ≥ 5) | **0,625** (10/16) |
| témoins (200 permutations, graine 1665) | max 0,3125 ; moyenne 0,061 |
| **marge** | **0,3125** |
| couverture des lettres de H par K | 0,96 (m, o absents de A) |
| **verdict** | **PARTIEL** (marge ≥ 0,30, mais lis < 0,70) |

Non lisibles dans la mesure : `neinen`, `eufed`, `gesch?ohren` (o absent de A), `?u` et `?eu` (m absent de A), `angerufen`
(absent du lexique ≥ 5). Deux « lisibles » le sont par hasard de coupure (`uen`, `een`, fins de mots au bord de la reliure).
Verdict conservé tel quel : aucun réglage après coup.

## Après la mesure (déclaré comme tel ; ne change pas le verdict)
- Clé complète : schéma régulier → KEY-COMPLET.tsv (m=z, o=w, e=k, h=q, l=x par le schéma ; m et o confirmés par « zu Zeu[g]en »,
  « geschwohren »).
- Corrections de transcription vues en relisant l'image : L1 capitale = A (→ B, « Boyneburg »), pas L ; L5 capitale = W (→ G, « Gott ») ;
  L4 `xqcgqbxsuiaki` (5ᵉ signe q, pas g) ; L7 dernier signe t (pas b) ; L9 1er signe probablement w (g). H-CHIFFRE.txt NON modifié
  (gelé) ; les corrections sont portées dans LECTURE.md.
- Avec la clé complète et ces corrections, le passage se lit entièrement (LECTURE.md : 31/32 mots lus par le sens).
