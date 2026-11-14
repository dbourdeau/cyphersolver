# Méthode de clé (lot 13) — figée AVANT construction — 14/11/2026 ≈ 17:25 (référence G05-G20 déjà figée : 96e9e271…)
- Données d'apprentissage (ADDENDUM-1) : S1 = nombres 113 d. L01-L18 (passA/passA_113L.tsv, 1ʳᵉ option) ;
  S2 = nombres 114 g. G01-G32 (passA/passA_114g.tsv, 1ʳᵉ option). Jamais H-secret/ colonne 2.
- Texte clair d'apprentissage T = glose Fable G01-G20 (1ʳᵉ option de chaque {…}, ‹…› supprimés) + gloses G21-G33
  (H_final.tsv colonne 3 SEULE, H21-H33) + gloses 114 g. l. 1-5 (passA_114g colonne 3), normalisé (minuscules, w=v, j=i,
  a-z å ä ö).
- Départ : travail/KEY_code246_brouillon.tsv. Itérations (≤ 12) : décoder S1 et S2, alignement semi-global (S1 sur T, S2 sur T),
  vote majoritaire par nombre (≥ 2 votes, ou 1 vote si nombre vu une fois) ; classes : lettres seulement (pas de nulles, pas
  de mots-codes) ; valeurs non vues → « ? ».
- Préalable (ADDENDUM-2) : resubstitution A_train = 1 − (d1 + d2)/(|dec S1| + |dec S2|) ≥ 0,85, sinon pas de mesure.
- Si OK : clé gelée KEY_code246.tsv + KEY.sha256 ; puis seulement, décodage de H (H_final.tsv colonne 2, 1ʳᵉ option, « ? »
  et « [?] » ignorés comme dans outils/data.py) et mesure contre REFERENCE-G05-G20.txt (« # » ne s'apparie à rien) ;
  200 témoins = permutation des lettres entre les nombres de la clé (seule classe), graines 1676000-1676199.
