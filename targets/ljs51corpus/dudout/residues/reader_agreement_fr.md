# Accord lecteur A / lecteur B aveugle — planches ljs51-residus (28/11/2026)

- Lecteur A : Claude Opus 5.5, auteur des planches. Il connaissait l'alignement de Daniel, donc sa lecture n'est PAS aveugle.
- Lecteur B : Claude Opus, lecture aveugle sur les images seules (`planches/LECTEUR-B-aveugle.md`).
- Règle appliquée : une correction n'est comptée que si les deux lectures concordent. Sinon, elle passe en {probable} et n'est pas comptée : on garde la lecture de Daniel.

| Planche | Q | A | B | Verdict | Effet |
|---|---|---|---|---|---|
| 24v6_LA | Q1-Q9 | A A B A A B B A C | A A B A A B B A C | accord 9/9 | lam-alif en 3 formes : **compté** |
| 24v6_Al-St-W-Sr | Q10-Q12 | trait vertical (A≈B) | A A B? (A/B même trait) | accord : même classe | aucun changement |
| | Q13-Q14 | D D | D D | accord | « سا » = un seul signe ق : **compté** |
| | Q15-Q19 | E ×5 | E ×5 | accord | aucun changement (rupture W conservée) |
| | Q20-Q22 | F ×3 | F ×3 | accord | aucun changement |
| | Q23 | autre (≠ F) | G probable / autre (hybride, ≠ F) | accord : ce n'est pas F ; identité indécise | sortie de Sr **comptée** ; valeur غ = {probable} |
| 33r4_coupes | Q1-Q5, Q7-Q9, Q11, Q12, Q14 | A | A | accord | — |
| | Q15 | B | B | accord | — |
| | Q6 | B | B? (indécis) | indécis | déjà S11 chez Daniel : aucun changement |
| | Q10 | B | B? (indécis) | **désaccord / indécis** | correction S12→S11 **retirée** → {probable} |
| | Q13 | B | B? (indécis) | **désaccord / indécis** | correction S12→S11 (ي) **retirée** → {probable} |
| 33r4_divers | Q16 / Q17 | A / B (formes distinctes) | A / B | accord | — |
| | Q18 | C (sablier) | C | accord | sablier inséré dans الحاجري : **compté** |
| | Q19 | ya-barree (D) | E ou D (D=E) | accord : ya-barree | ya-barree inséré (منكور) : **compté** |
| | Q20 | autre | autre | accord | boîte longue non résolue |
| 33r4_triangle-yabarree | Q21 | A | A | accord | ت de كنت = S18 : **compté** |
| | Q22-Q26 | C (S23 ≈ S1) | C (même tracé) | accord | séparation S1/S23 de Daniel maintenue (non tranché) |
| 101r2_S9 | Q1-Q6 | A A B A B B | A A B A B B | accord 6/6 | ه/ح séparés : **compté** |
| 103v2_S19 | Q1 | A | A | accord | — |
| | Q2 | illisible | indécis / autre | accord : non classable | retiré de la classe I : **compté** |
| | Q3 | illisible | A probable | **désaccord** | neutralisation **retirée** → Daniel gardé |
| 59r2_S15 | Q1 | autre (sommet coupé) | autre | accord | ▱ reste une forme à part, non lue |
| 81r5_S20 | Q1-Q2 | A A | A A | accord | aucun changement |

Au total, 61 questions : 56 accords complets. Désaccords ou indécision : 33r Q10 et Q13 (corrections retirées), 103v Q3 (neutralisation retirée), 33r Q6 (indécis, sans effet). Accord partiel : 24v Q23, sur l'exclusion de F seulement.

## Cohérence recalculée (règle des deux lecteurs)
Comptage sur les formes répétées, en partant de l'état de Daniel :

| Chaîne | Avant | Après |
|---|---|---|
| 24v.6 | 88,2 % | 97,3 % (71/73) |
| 33r.4 | 96,3 % | 97,6 % (80/82) |
| 101r.2 | 95,4 % | 100 % (65/65) |
| 103v.2 | 96,0 % | 98,0 % (48/49) |
| **Total** | 461/479 = 96,2 % | **471/477 = 98,7 %** |

Le total de la lecture A seule était de 99,4 % (`resultats_lecteurA.txt`). Le détail des corrections retirées est dans `probables_non_comptes.json`.
