# PREREG — catalogue 1213, AD24 2 E 1841/18 (photos SHAP), lettre du 17 août 1651 (« 2 E 1841/18-3 »)
Gelé le 23/11/2026 AVANT toute transcription du chiffré et tout décodage. Une seule exécution de score.py.

- **Portion tenue à l'écart (held-out)** : tous les passages chiffrés de P1370688 (deux pages) situés après le premier passage clair (« Je suis bien fasché … entr'eux ») et avant le dernier passage chiffré de la page (« au Parlement K 30 74 … », qui continue sur la page suivante, non photographiée lisiblement : P1370689 est grise). La première ligne chiffrée de la page (fin de la phrase de P1370687) est exclue aussi (avant le premier clair).
- **Transcription** : deux passes aveugles indépendantes (sous-agents Opus, sans clé, sans dactylographie Brianson, sans les feuilles P1370715–727) + arbitre aveugle ; format `nombre|marque` (none, tilde, acute, diaeresis, caron, macron, dot, grave, other) ou `SYM:nom` ; le fichier arbitré est haché (SHA-256) avant la mesure.
- **Référence** : `reference_brianson_688.txt` (passages en capitales de la dactylographie de Brianson, P1370721), codes ?/n retirés.
- **Clés testées, dans la même et unique exécution** : K1 = clé Condé–Barrière 1655 (`K1_key1655.json`, notre transcription C05 ; correspondance de marques déclarée : none→'' ; acute→′ ; diaeresis→¨ ; caron→ˇ ; macron→¯ ; dot→· ; tilde→^ ; grave→` ; symboles non mappés). K2 = clé de Brianson laissée dans le dossier (`K2_brianson.json`, P1370718–719). Écart déclaré au « une seule mesure » : deux clés, une seule exécution, aucune re-mesure.
- **Décodage** : première valeur de chaque signe ; signe inconnu = rien ; signes `|macron` (classe des noms propres chez Brianson) exclus des deux côtés (comme les ?/n de la référence).
- **Normalisation** : minuscules, lettres seules, sans accents, j→i, v→u, y→i.
- **Mesure** : accord caractères = 1 − Levenshtein(décodage, référence) / max(longueurs). Témoins : 200 clés où les valeurs sont permutées entre signes (graine 20261123).
- **Critère** : VALIDE si accord ≥ 0,85 ET ≥ meilleur témoin + 0,30. Moins de 300 signes mesurés = non mesurable. Accord en mots : non calculable (décodage sans séparateurs), déclaré non calculé.
- Jamais rétroactif : P1370688 est grillée après la mesure.
