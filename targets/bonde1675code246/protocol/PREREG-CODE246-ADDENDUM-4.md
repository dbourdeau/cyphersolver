# ADDENDUM 4 au PREREG code 1-246 — figé AVANT le run Fable « clé passe 4 » et avant tout appel API — 15/11/2026
Base : PREREG-CODE246.md (06ffce5f…), ADDENDUM-1 (e0873adf…), ADDENDUM-2 (edd81f4a…), ADDENDUM-3 (01e35ac8…),
METHODE-CLE.md (2b83cbf0…), FABLE-BRIEF.md (f3ec33fb…), passe4/ (S1_passe4 b096bffc…, S2_passe4 fb40c6d2…,
key_passe4_candidate.json 7b06a131…, build_key4.py 089c44e6…). Référence de H : verif-lot13/REFERENCE-G05-G20.txt (96e9e271…)
et REFERENCE-G05-G20-lignes.tsv (bcb06431…). H = H-secret/H_final.tsv (d428dfd3…e391), colonne 2 jamais ouverte.

## Accord et plafond
- Accord explicite de Brice dans le chat le 15/11 : « Oui, 5 USD ». Il couvre UN run payant de Fable 5.2 (API) pour la clé du
  code 246 (Bonde), plafond dur **5,00 USD pour ce run**. Cumul Fable avant le run : 177,32 USD sur le plafond global de 200 USD.
- Plafond appliqué dans le runner (wrapper fable_run_cap5.py, fonctions de fable_run.py) : AVANT chaque requête, estimation
  du pire cas = jetons d'entrée comptés avant l'appel (messages.count_tokens, historique compris) × prix d'écriture en cache
  + (budget de tâche + max_tokens) × prix d'écriture en cache + max_tokens × prix de sortie + 10 relectures du contexte au prix
  de lecture en cache ; la requête n'est PAS envoyée si dépense réelle du run (usage renvoyé par l'API) + pire cas > 5,00 USD.
  Après chaque requête, le coût réel (usage) est ajouté au run et au ledger.json. Aucune autre requête au-delà.

## Ce que Fable reçoit et ne reçoit pas
- Reçoit : S1/S2 passe 4 (colonnes 1-2 seulement : identifiant de ligne + nombres) ; T-train.txt (référence d'apprentissage,
  mots normalisés par l'ADDENDUM-3 (b)1, produite par le code de build_key4.py) ; la clé de départ (key_passe4_candidate.json) ;
  METHODE-CLE.md ; metric.py (align et cost3 de build_key4.py, inchangés) ; build_key4.out.
- Ne reçoit JAMAIS : H-secret/ (ni colonne 2 ni colonne 3 en fichier séparé ; les gloses G21-G33 n'existent que fondues dans
  T-train.txt), REFERENCE-G05-G20*, aucune image, aucun crop.

## Règles (inchangées sauf mention)
1. La clé de Fable (fichier KEY-PROPOSAL.tsv/.json produit dans le conteneur) est copiée et figée par SHA-256 dès réception,
   AVANT tout calcul sur H. Interprétation fixée maintenant : une valeur = une seule lettre a-z å ä ö après normalisation
   (minuscules, w=v, j=i) ; toute autre valeur (nulle, multilettre, vide, « ? ») = « ? » au décodage. Les nombres absents
   = « ? ». Nous n'ajustons PAS la clé de Fable (pas de revote, pas de correction).
2. Préalable : resubstitution A_train calculée par NOUS (métrique ADDENDUM-3 (b), cost3 de build_key4.py inchangé), sur S1+S2
   passe 4 contre T (le même T que build_key4.py), avec la clé de Fable telle quelle. Si A_train < 0,85 : AUCUNE mesure,
   H reste intacte, non décodée, non grillée.
3. Seulement si A_train ≥ 0,85 : clé gelée KEY_code246.tsv + KEY.sha256, puis UNE mesure sur H selon l'ADDENDUM-3 (c),
   seuils INCHANGÉS : SUCCÈS si A ≥ 0,85 ET A ≥ max(200 témoins) + 0,30 (témoins : permutation des lettres entre les nombres
   de la clé, graines 1676000-1676199, même métrique) ; longueur décodée ≥ 0,8 × 301. H grillée ensuite.
4. Contrôle indépendant de la clé de Fable par nous, sans valeur de décision supplémentaire : resubstitution S1 et S2 séparées,
   ancienne métrique, nombre de valeurs changées par rapport à la clé de départ, et plausibilité des suites alphabétiques
   (blocs de nombres consécutifs donnant des lettres consécutives) que Fable invoque.
5. Aucun autre seuil, aucune autre portion, aucun deuxième run sans nouvel accord de Brice.
