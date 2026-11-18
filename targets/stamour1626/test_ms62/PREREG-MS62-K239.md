# PREREG — test de la table Ms 1580 f. 239 (K239) sur les passages chiffrés Saint-Amour → Cantecroy, Ms Granvelle 62 (img373–390)
Écrit le 18/11/2026 par le fil 🔓 (Opus) AVANT toute transcription des passages chiffrés du Ms 62 et AVANT tout décodage.
Seul vu jusqu'ici du Ms 62 : planche-contact à 330 px de large (repérage des pages chiffrées, formes ; rien lu ni décodé).

## 1. Objets gelés
- Clé : `f239/KEY-F239.json`, SHA-256 1f46773eb0f08227d4204857c856f648e2b65a5af28b1a5204bd2364ae1fe447 (table d'époque transcrite en 2 passes ; pas reconstruite).
- Lexique : `ms62-test/LEXIQUE-FR-EARLY.txt`, SHA-256 e97da1591797ed70d759406bb4250a1a7be185683a1f4ec44f8c8de9a6c38089 (Henri IV freq ≥ 2 + fr.json.gz freq ≥ 3, normalisation early).
- Transcription : faite par un agent Opus NEUF, aveugle à la clé (n'ouvre ni f. 239 ni ce dossier hors sa sortie), avec le vocabulaire neutre de signes de la consigne ; sortie `ms62-test/transcription/CHIFFRE-MS62.tsv` + `INTERLIGNE-MS62.tsv` (mots d'époque écrits au-dessus du chiffre, à part) ; gelée par SHA-256 (SHA256.txt) avant décodage.

## 2. Portion et décodage
- P = tous les signes chiffrés transcrits des img373–390 (toutes lettres), dans l'ordre de lecture, en excluant les signes marqués illisibles. Si |P| < 300 signes décodables → pas de mesure (rapport « portion insuffisante »).
- Décodage mécanique par `ms62-test/measure.py` (écrit et haché avant d'ouvrir la transcription) : signe → lettre selon `regle_decodage` de K239 ; signe absent de K239 → séparateur « | » (code/inconnu, compté à part). Les séparateurs de mots notés par le transcripteur (espace large, point, clair intercalé) → « | ».
- Rien n'est corrigé à la main avant la mesure ; aucune variante de clé essayée.

## 3. Mesure UNIQUE
- M = part des lettres décodées couvertes par une segmentation optimale de chaque segment (entre « | ») en mots du lexique de longueur ≥ 2 (programmation dynamique, maximise les lettres couvertes ; mots d'une lettre « a », « y », « e » (et), « o » non comptés).
- Témoins : 200 clés obtenues en permutant au hasard les valeurs (lettres) entre les signes de K239 (même ensemble de signes, même multiplicité de valeurs), graine 1626 ; même calcul.
- Critère fixé : **VALIDÉE si M ≥ 0,85 ET M ≥ max(témoins) + 0,30.** PARTIELLE si M ≥ max(témoins) + 0,30 sans 0,85. ÉCHEC sinon.
- Une seule exécution ; la portion est ensuite « grillée ». Rapporté aussi (non décisif) : part des signes hors clé ; accord lettres avec les mots interlinéaires d'époque s'il y en a (aligné par distance d'édition), et le relevé de Daniel (sûrs/probables/irrésolus) fait APRÈS la mesure.

## 4. Après
- Si VALIDÉE : identification = K239 est bien le chiffre des lettres Saint-Amour 1626–27 ; lecture des passages (règle de Daniel ≥ 95 % pour publier) ; si des mots d'époque interlinéaires existent, ces passages-là sont EXISTING.
- Si ÉCHEC : la table n'est pas celle de ces passages (ou un nomenclateur domine) ; on n'ajuste pas la clé sur cette portion.
