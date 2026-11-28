# PREREG-3b — complément de taille (27/11/2026, AVANT toute exécution de scripts/mesure3.py ou de mesure3b.py)
Constat (avant toute mesure) : la portion 3 (blocs marginaux 318r/318v, ARBITRE-P3.tsv, gelé 2b3c8d3c…) ne compte que 237 nombres < 300 ;
les pages d'extension (319r, 300v, 301r, 161v, 162r, 314v) n'ont aucun bloc. mesure3.py N'EST PAS exécuté.
Complément : la portion PREREG-2 (336r + 321r), jamais mesurée, jamais utilisée pour K (vérifié : absente de T1–T4), arbitrée A2/B2 →
transcriptions/ARBITRE-336-321.tsv ; seuls les groupes à glose sûre (colonne 5 = 1) comptent ; le choix « sûre / incertaine » a été fait
avant toute application de K' à ces groupes. Biais possible : l'arbitre (agent 🔓) connaît K ; il n'a appliqué ni K ni K' aux groupes.
## Mesure unique (scripts/mesure3b.py)
Clé K' = table mod 24 de PREREG-3 (+ codes de K). Deux sous-portions, même règle de comptage (« ? » = faux) :
- S1 blocs 318r/318v : Smith-Waterman de chaque bloc contre le concept 318r+318v+319r (P3-C) — renvois a–h non reliables avec sûreté ;
- S2 groupes glosés 336r/321r : Needleman-Wunsch du déchiffrement contre la glose du même groupe (codes : mot entier).
Accord global = Σ justes ÷ Σ caractères déchiffrés (S1+S2). Seuil = moyenne pondérée par caractères déchiffrés de 0,555 (S1, cf. ρ = 0,653
de PREREG-3) et 0,85 (S2, glose verbatim) ; ET accord ≥ meilleur de 200 témoins (permutations des 24 cases, graine 24683) + 0,30.
Taille totale ≥ 300 nombres exigée. Accords par sous-portion rapportés. Une seule exécution ; portions grillées ensuite.
