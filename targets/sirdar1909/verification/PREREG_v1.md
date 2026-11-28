# PREREG v1 — Sirdar → Herbert, 9 janv. 1909 (cat. 2907), 27/11/2026
- Hypothèse : l'alphabet de substitution (lettre à lettre, groupé par 5, nulles en tête/fin de série) bâti sur HIL/64/402=403 et HIL/64/239=118 est celui des dépêches de 1908-1909 du même dossier.
- Construction : build_v1.txt seulement. Portion réservée : HIL/64/240=119 (même dépêche, feuillet 2, jamais lue par le constructeur) + HIL/64/214=62 (26 sept. 1908), transcrites en double aveugle (passes A et B), arbitrage mécanique arbitrate_v1.py.
- Mesure unique : tools/holdout/measure.py (Daniel, commit ff4a515bda), métrique char, 200 témoins (valeurs mélangées), graine 2907. Réussite = score ≥ 0,85 ET ≥ meilleur témoin + 0,30. Accord par série rapporté, non décisif.
- Écarts déclarés d'avance : 301 signes dont 28 « ? » (273 comptés) ; fin de la série 214 hors feuillet (référence = 235 premières lettres du clair à partir de « Two of these ») ; 214 peut relever d'un autre alphabet ; la clé ne porte pas i, n, z (valeurs inconnues) ; w→h isolé dans « railway » non retenu ; g/q confondables selon les mains.
- Passage nu (HIL/64/400) : hors test ; lecture par le sens fixée dans passage_2907_v1.txt + NOTES.
