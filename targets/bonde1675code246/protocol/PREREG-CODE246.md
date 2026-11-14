# PREREG — code 1-246 (vues 113 d. + 114 g., R0003797) — figé AVANT toute transcription — 14/11/2026
Agent Opus 5.5 (fil 🔓). Rien de 113 d. n'a été transcrit à ce stade (seulement vu : vue d'ensemble réduite, ligne 1 zoomée,
crayon tardif « h e r … » au-dessus de la ligne 1, et 114 g. dernière ligne crayon « N o v e m b r i s » sous
50.77.34.42.22.16.112.55.149 → hypothèse : une lettre par nombre, homophones ; des nombres-mots possibles).

## Unités
- Ligne chiffrée k de 113 d. : k = 1 … dernière (≈ 33), numérotées de haut en bas, la ligne 1 commence « 4?.13.27 ».
- Glose Gk = la ligne d'encre écrite immédiatement AU-DESSUS de la ligne chiffrée k (G1 = « Herr Cantzlirådet … »).
- 114 g. : lignes glosées 1-5 (fin de la même lettre), puis lignes nues (autre message, daté « 18/28 Novembris »).

## Partage
- APPRENTISSAGE : 113 d. lignes 1-18 (nombres + G1-G18 + crayon tardif de ces lignes) ; 114 g. lignes glosées 1-5 ;
  112 d. P.S. (4 lignes, crayon) si ses valeurs relèvent du même code ; 114 g. dernière ligne (« Novembris », crayon).
- TENUE À L'ÉCART (H) : 113 d. lignes 19 → dernière, nombres + gloses G19 → dernière. Transcrites UNIQUEMENT par des
  sous-agents (deux passes indépendantes + arbitrage sur l'image par un troisième), sans que l'agent principal regarde
  les crops ni le texte de H avant le gel de la clé. Crayon tardif éventuel sur H : non transcrit, non utilisé.
- Si la glose concaténée de H a < 300 lettres : mesure déclarée IMPOSSIBLE (pas de repli).

## Clé
- Construite sur l'apprentissage seulement : nombre → lettre(s) ou mot ; nulles explicites ; valeurs non vues = « ? ».
- Gelée par SHA-256 (fichier KEY_code246.tsv + KEY.sha256) AVANT la lecture de H par l'agent principal.

## Métrique (UNE mesure)
- Décodage des nombres de H avec la clé gelée (nulles supprimées, « ? » compte faux) ; normalisation : minuscules,
  w=v, j=i, lettres a-z å ä ö seulement (comme mesure-1411/metric.py).
- Référence = G18 + G19 … Gdernière + glose de 114 g. ligne 1, concaténées et normalisées (marges pour la dérive).
- A = 1 − distance d'édition semi-globale (extrémités de la référence libres) / longueur décodée.
- Contrainte : longueur décodée ≥ 0,8 × nombre de groupes de H (sinon ÉCHEC).
- Témoins : 200 clés mélangées (permutation des valeurs entre les nombres de la clé, nulles conservées),
  graines 1676000 … 1676199.
- SUCCÈS si A ≥ 0,85 ET A ≥ max(témoins) + 0,30. Sinon ÉCHEC, et H est grillée.
