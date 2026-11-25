# PREREG — test indépendant de la clé breant1673 sur la lettre chiffrée du carton 170.1

Rédigé le 19/11/2026 par 🔓 (agent Opus), AVANT toute transcription et tout décodage. Gelé par SHA-256 (empreinte notée dans HANDOFF.md et dans PREREG.sha256).

## Pièce
- Médiathèque Georges-Delaw, Sedan, fonds Gourjault, carton 170.1, pièce f. 3-4 : Louvois → M. de Réveillon, « A Versailles le 19e Mars 1674 », mention « Duplicata ». Vues IMG_3234 (f. 3) et IMG_3235 (f. 4, haut). Images privées, jamais publiées.
- Système vu sur la vignette : nombres de 2 ou 3 chiffres séparés par des points, plage visiblement 6…316, comme la clé de Bréant ; glose interlinéaire d'époque **groupe par groupe** ; quelques passages en clair dans le texte.

## Exposition déclarée (écart à l'aveugle)
- L'agent qui rédige connaît la clé breant1673 (lue dans le dossier) et a vu les vignettes de 3234/3235 à 1500 px (glose comprise) pour l'inventaire, avant ce PREREG. Il n'a transcrit aucun groupe.
- En conséquence, **l'agent rédacteur ne transcrit pas** et **n'arbitre pas** : la transcription (groupes + glose alignée) est faite par deux sous-agents indépendants qui ne reçoivent ni la clé ni aucune valeur ; les désaccords sont arbitrés par un troisième sous-agent aveugle à la clé, sur l'image. L'agent rédacteur se limite à fusionner mécaniquement et à lancer le calcul.

## Clé (gelée, sans retouche)
- `key-pr798-1abb47a.tsv` = targets/breant1673/key.tsv de la PR #798, commit 1abb47a51, SHA-256 25052e57967ab1a66e1c37a9eae8c13d846aeba58e79b8546bcc1f792cf42221 (90 groupes, dont 208 = o, 293 = vo, 74 = ca inférés). Aucune valeur ajoutée ni corrigée avant la mesure.

## Mesure unique M
- Unité : un groupe chiffré de la transcription arbitrée.
- Ensemble mesuré E : groupes dont (a) la lecture du nombre est sûre après arbitrage, (b) le nombre est dans la clé gelée, (c) la glose d'époque au-dessus est lisible et attribuée à ce groupe seul.
- Accord(g) = 1 si la valeur de la clé, normalisée, est égale à la glose normalisée ; sinon 0. Normalisation : minuscules, sans accents, u=v, i=j=y, s=z, sans ponctuation ni espaces. Valeur à alternatives (« x / y ») : accord si l'une convient. Un nom propre de la clé (Roi, M. de Cologne…) s'accorde si la glose donne ce nom (abréviations admises : « R », « M. de C. »).
- M = Σ accord / |E|.
- Témoins : 200 tables obtenues en permutant au hasard les valeurs de la clé entre ses 90 groupes (graine 20261119, `random.Random`), même calcul sur E. Rapporter le meilleur témoin et la moyenne.
- **Critère : M ≥ 0,85 ET M ≥ meilleur témoin + 0,30.** Succès = la clé breant1673 est validée sur une lettre neuve (autre scripteur, même table).
- Taille minimale : la glose de E doit compter ≥ 300 signes (lettres après normalisation). Sinon la mesure est déclarée **non mesurable** (on rapporte M à titre descriptif seulement).
- Une seule exécution. Portion grillée après mesure.

## Rapporté, non décisif
- Couverture : part des groupes de la lettre absents de la clé (nouvelles valeurs), et leur place par rapport à l'ordre « à peu près alphabétique » (la valeur glosée tombe-t-elle entre ses voisins de la clé ?).
- Valeurs inférées : accord ou non de 208, 293, 74 s'ils apparaissent (chaque cas listé).
- Liste de chaque désaccord avec la cause probable (lecture du nombre, faute du chiffreur, homophone, faute du déchiffreur).

## Comptage #728 (après la mesure)
- Sur les mots chiffrés seulement (les passages en clair ne comptent pas).
- **Compte A (clé seule)** : sûr = tous les groupes du mot sont dans la clé gelée, lus sûrement, et le mot obtenu a le sens et concorde avec la glose ; un mot qui demande une valeur hors clé, une correction, une restitution ou une inférence = trou.
- **Compte B (clé + glose d'époque)** : en plus, un mot dont un groupe hors clé est donné par la glose et a le sens = sûr seulement si cette valeur est attestée au moins deux fois de façon cohérente dans la lettre ; sinon probable {x} = trou.
- Probables, restitués, inférés, irrésolus = trous. « read » si ≥ 95 % ; si moins de 40 mots chiffrés, au plus 2 trous.

## Si le système n'était pas celui de Bréant
- Décrire le système, chercher un crib dans les lettres en clair du carton 170.1, rédiger un PREREG distinct avant toute reconstruction. (Non attendu d'après la vignette.)
