# PREREG v1 — Penn LJS 51, f. 22v l.9-13 + 23r l.1 (catalogue ljs51corpus, chaîne 22v.9)

Agent piste 5 (campagne LJS 51, 28/11/2026). Écrit et gelé AVANT toute mesure sur les données réelles.
Images : University of Pennsylvania, LJS 51, OPenn (IIIF Penn, 2343 px ; f22v = canvas 50, f23r = canvas 51 ; sha256 dans SHA256SUMS.txt du dossier d'images).

## Antériorité (Daniel Bourdeau, dbourdeau/cyphersolver, origin/main d8ac608093)
`targets/ljs51corpus/keys_eye/22v.9.json` : 81 signes, clé à vue NON tenue (cohérence 0,40 lettre / 0,453 squelette) ; il note
que le nombre de signes et les répétitions (GH D Lo aux signes 1 et 41 ; W E8 A W aux signes 24 et 71) collent au clair, et
qu'une clé demande une passe signe à signe en classes de formes. Sondage de classement du 28/11 (non gelé) : décalages fixes,
mots inversés, texte inversé = niveau du hasard.

## Ce que l'agent a vu avant ce gel (déclaré)
- Le JSON de Daniel en entier (alignement positionnel compris) et le clair : l'arbitre n'est donc PAS aveugle au clair.
  En le lisant, il a remarqué que la forme notée E8 (Λ) tombe sur ذ à décalage variable (−2, −2, −1, −1, +1), ce qui
  suggère une substitution avec insertions/omissions mal alignée plutôt qu'un système exotique. C'est ce qui motive le
  choix d'un alignement avec écarts (H1/H4). Aucun calcul n'a été fait sur les données réelles avant ce gel.
- Les transcriptions A et B ont été faites par deux sous-agents Opus aveugles (ni clair ni JSON de Daniel). Accord strict
  74/81 (91,4 %), après correspondance des étiquettes 78/80 (97,5 %) : seuil de 85 % atteint. Arbitrage dans `arbitrage.txt`.
- La procédure a été mise au point sur des données SYNTHÉTIQUES seulement (`procedure.py selftest`).

## Données gelées
- `arbitrage.txt` : transcription arbitrée, 81 signes, 22 classes (étiquettes de A). `A.txt`, `B.txt` : transcriptions aveugles.
- `clair_23r.txt` : clair du compilateur (23r l.4-7), 21 mots, 80 lettres (lām-alif = 1 lettre) ; 2e colonne « hamza distincte ».
  Variantes déclarées : mot 1 لبني/بني ; mot 15 لشوق retenu (لشيق chez Daniel, non utilisé).

## Hypothèses (toutes traitées par UNE procédure, sélection sur la moitié d'apprentissage seulement)
- H1 : substitution de signes avec homophones (plusieurs classes pour une lettre), après redécoupage en classes de formes.
- H4 : H1 + « erreur » localisée : signes nuls / répétés et lettres omises (écarts de l'alignement) ; et le traitement
  propre de la hamza signalé par le compilateur (variante d'alphabet « hamza distincte » : أ ≠ ا, ﻷ ≠ ﻻ).
- Variante d'ordre : clair tel quel OU chaque mot écrit à l'envers (maqlūb par mot). Variante du mot 1 : لبني ou بني.
  8 variantes (2 alphabets × 2 ordres × 2 premiers mots) ; choix = meilleur score « laisser-un-dehors » (LOO) sur la seule
  moitié d'apprentissage ; égalités → ordre de la liste (merged<hamza, asis<wordrev, لبني<بني).
- H2 (ibdāl codifié : abjad ± n, ayqash, ordre ± n) et H3 (taṣḥīfī) NE SONT PAS MESURÉES : H2 exigerait de nommer les classes
  par des lettres (contraire à la transcription aveugle), H3 se mesure au niveau des squelettes, pas des caractères.
  Si H1/H4 échouent, elles restent des pistes, sans mesure sur la portion grillée.

## Procédure (`procedure.py`, gelée)
- Moitié A = signes 1-40 avec les mots 1-11 (لبني … اعتذر, 41 lettres) ; moitié B = signes 41-81 avec les mots 12-21 (39 lettres).
- Apprentissage : alignement global signe↔lettre (Needleman-Wunsch, score log P(lettre|classe) lissé α = 0,5, écart log 0,02),
  hard-EM multi-départs (13 diagonales décalées −6..+6 + 40 départs par morceaux, graine 1), solution de plus grande
  vraisemblance ; clé = lettre la plus fréquente par classe.
- Décodage de la moitié tenue à l'écart ; classe inconnue = « ? » (jamais juste).
- **Accord en caractères** = LCS(décodage, clair tenu à l'écart) / nombre de lettres du clair tenu à l'écart.
- **Témoins** : 200, graines 20261129…20261328 ; même procédure complète (y compris le choix de variante), les lettres du clair
  d'apprentissage étant permutées au hasard.
- **Critère (fixé avant)** : accord ≥ 0,85 ET ≥ meilleur témoin + 0,30.
- **Mesure primaire** : apprendre sur A, mesurer sur B. **Seconde mesure indépendante déclarée** (inversion unique permise) :
  apprendre sur B, mesurer sur A. Verdict « clé validée » si la primaire passe ; l'inverse est rapportée telle quelle
  (si l'une passe et l'autre non, le verdict est « plafonné »).
- Rapporté, non décisif : couverture (part des signes tenus à l'écart dont la classe a été vue), accord sur les seuls signes
  connus, accord en mots.

## Puissance (déclarée avant mesure)
Sur 10 jeux synthétiques de la taille de celui-ci (80 lettres, 22 lettres zipfiennes, vraie substitution simple, 1 nul, 1 omission),
la vraie clé donne 0,54-0,87 (3/10 ≥ 0,85) et les témoins 0,28-0,56 : avec 40 signes d'apprentissage, le critère de 0,85 est
souvent hors d'atteinte même pour une bonne clé (classes jamais vues). Un échec au seuil n'est donc pas une réfutation ;
un « plafonné » sera rapporté comme tel, jamais retouché a posteriori.

## Après la mesure
Fiche sûrs / {probables} / [restitués] / ‹irrésolus› ; localisation de « l'erreur » du chiffreur (écarts de l'alignement) ;
écarts avec la lecture de Daniel. Aucune nouvelle hypothèse testée sur une portion mesurée (grillée).

## Commande de mesure (à lancer seulement après confirmation que l'empreinte est postée sur #1023)
python3 -I gel/procedure.py measure mesure/
