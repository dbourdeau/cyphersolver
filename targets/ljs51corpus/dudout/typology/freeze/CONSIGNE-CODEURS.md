# Consigne des codeurs A et B (double codage aveugle, grille v1)

Tu es codeur indépendant. Tu codes 30 chiffres du manuscrit Penn LJS 51 d'après des fiches texte, selon la grille
`gel/GRILLE.md`, section B (dimensions B1 à B7). Lis la grille en entier d'abord : ses règles et son ordre de priorité font foi.

- Chemins relatifs au dossier `ljs51-typologie/gel/`.
- Fichiers à lire : `gel/GRILLE.md` ; `data/echantillon_30.json` (la liste des 30 unités) ; pour chaque unité, `data/fiches/<unité>.txt` et RIEN d'autre (pas d'autre fiche, pas de dossier `../mesure/`, pas d'internet, pas d'image, pas de clone git).
- Code chaque unité séparément, sans comparer aux autres unités, et sans deviner : si la fiche ne dit rien, c'est `ND` / `AUCUNE` / `INCONNU` / `NON` selon la dimension.
- Écris un TSV UTF-8, une ligne d'en-tête puis 30 lignes, colonnes séparées par une tabulation :
  `unite	B1	B2	B3	B4	B5	B6	B7	justification`
  (justification : 1 phrase courte, citant le mot de la fiche qui décide les codes non triviaux).
- Codes autorisés seulement : B1 {MUSHAJJAR, TASHIFI, MAQLUB, NONCLE, SQUELETTE, HOMOPHONE, SIMPLE} ; B2 {UN, DEUX, ND} ;
  B3 {NONECRITE, ECRITE, ND} ; B4 {FACILE, DIFFICILE, MIXTE, AUCUNE} ; B5 {COMPILATEUR, ALAI, MUTARJIM, JAWLANI, AUTRE, INCONNU} ;
  B6 {OUI, NON} ; B7 {OUI, NON, NA}.
- Ne modifie aucun autre fichier.
