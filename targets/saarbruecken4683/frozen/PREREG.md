# PREREG — Saarbrücken 4683, système numérique A (rédigé le 26/11/2026 avant tout calcul de clé)

Source : Landesarchiv Saarland, Nassau-Saarbrücken II Nr. 4683 (1673/74), 47 doubles pages JPEG reçues le 26/11/2026.

## Hypothèse
Système A = substitution homophonique numérique, un nombre par lettre ; nombres 40–199 = lettres
(segmentation auto-délimitante : un groupe commençant par 1 a 3 chiffres, par 4–9 a 2 chiffres) ;
nombres ≥ 200 = nomenclateur (mots, noms). Passages chiffrés insérés dans un texte en clair.

## Données
- APPRENTISSAGE (clé K) : uniquement les alignements nombre → lettre tirés des résolutions
  interlinéaires d'époque (lettres reçues, fol. 160r, 161r, 235r–235v, 247r–247v, 254r, 265r–266v,
  279r–281r, 312r–316r, 331r–339r…) et des chiffrements marginaux des concepts (fol. 300r, 311r,
  312v, 318r–320v, 332r…). Un alignement n'est retenu que si le nombre de nombres du groupe = le
  nombre de lettres de la glose (normalisée), ou si la glose est lettre par lettre.
- PORTION TENUE À PART (test, jamais utilisée pour K, jamais regardée avec la clé avant la mesure) :
  la lettre chiffrée fol. 297r–297v (« Ab Schreiben vom 2. dieses … », Ottweiler 20 janv. 1674) ;
  référence = son concept en clair fol. 298r–298v. Exclus aussi de l'apprentissage : fol. 296r–298v.
- Transcription du test : 2 passes aveugles indépendantes (A, B ; sans le concept), arbitrage sur
  l'image, gel SHA-256 AVANT la mesure. Concept transcrit et gelé séparément.

## Clé
K = pour chaque nombre, la lettre majoritaire de ses alignements d'apprentissage (égalité → « ? ») ;
codes ≥ 200 : le mot de la glose s'il est attesté, sinon « ? ». K gelée (SHA-256) avant la mesure.

## Mesure (UNE seule)
Texte déchiffré = lettre du test où chaque nombre est remplacé par K (inconnu → « ? »), mots en clair
conservés. Normalisation : minuscules, lettres seules, u=v, i=j=y, ß=ss. Alignement global
(Needleman-Wunsch, +1 / −1 / −1) contre le concept normalisé. Accord caractères = caractères issus
des nombres alignés sur un caractère identique du concept ÷ nombre total de caractères issus des
nombres (« ? » compte comme faux). Taille minimale : ≥ 300 caractères chiffrés.
Témoins : 200 clés permutées (les lettres de K mélangées entre les nombres, graine 4683),
même calcul. Critère fixé d'avance : accord ≥ 0,85 ET ≥ meilleur témoin + 0,30.
Accord en mots (groupes chiffrés entièrement justes) rapporté, non décisif. La portion mesurée
est grillée ensuite. Aucune retouche rétroactive de K ni de la transcription.

## Lecture par le sens
Fiche séparée (sûrs / {probables} / [restitués] / ‹irrésolus›), règle de Daniel ≥ 95 %.
Note : les lettres reçues portent un déchiffrement d'époque → EXISTING ; la nouveauté possible =
la clé reconstituée et les passages sans résolution.
