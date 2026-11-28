# PREREG — ljs51-22r1-61r3 : un solveur par mots pour les chaînes longues avec séparateurs

Rédigé le 28/11/2026 (UTC) avant toute mesure sur les chaînes fraîches. Agent : piste « hard strings » de la campagne
LJS 51 (Claude Opus 5.5 pour Brice Dudout). Base : dbourdeau/cyphersolver `d8ac608093e1149f9456eaa2c99bb456ca0abc92`
(même base que la piste 2, ljs51-aveugle, PR #1055).

## Diagnostic (fait avant, sur des chaînes grillées ; `diag/DIAGNOSTIC.md`)
22r.1 et 61r.3 échouent par **échec de modèle**, pas de recherche : sous l'objectif du solveur de caractères, le
décodage aveugle bat le vrai clair (log P −52 et −131). La clé de Daniel est cohérente (99,4 % et 99,1 %), le clair est
le bon, il n'y a ni nulle, ni transposition, ni seconde plume. Causes : homophones lourds et vocabulaire rare (22r.1) ;
clair d'un genre atypique, une liste d'impératifs (61r.3).

## Hypothèse unique H
Un objectif **par mots** — chaque groupe noté par sa fréquence dans un lexique de formes attestées, avec repli sur les
4-grammes et une pénalité ρ hors lexique — casse plus de chaînes longues avec séparateurs que l'objectif de caractères
de la piste 2, à réglages de recherche égaux.
**H soutenue si, sur les 10 chaînes fraîches, (validées par MOTS) − (validées par CARACTÈRES) ≥ 2.** Sinon, H non
soutenue. Aucune autre lecture du résultat n'est décisive.

Prédiction déclarée (non décisive) : le gain portera sur les chaînes à homophones (classes − lettres ≥ 4) ; un clair
du genre de 61r.3 (liste d'impératifs) resterait au hasard avec les deux solveurs.

## Chaînes de mesure (fraîches, jamais mesurées ; `transcriptions/SELECTION.tsv`, `scripts/selection2.py`)
Règle fixée avant tout résultat : `keys_eye` présent, séparateurs présents, clair du compilateur présent
(`chains_all.json` → `plaintext.text`, `answered == "yes"`). Hors : les 18 chaînes de la piste 2 ; les exclusions de la
piste 2 ; les folios des autres pistes en cours (12v, 106v, 63v, 21r, 37v-38v, 3v-4r, 98v, 30v.7, 22v.9, 14v.7, 48r.8).
On prend toutes les éligibles ≥ 90 signes, puis on complète par longueur décroissante jusqu'à 10 chaînes. Une chaîne
dont plus de 5 % des 12-grammes du clair figurent dans le corpus du modèle OU du lexique est remplacée par la suivante
(écartées : 87r.3 5,7 %, 37r.11, 9v.3, 89v.4, 91v.10).
Résultat : **87v.8 (130), 96r.2 (128), 83r.13 (100), 77v.9 (94), 84r.12 (93), 104v.2 (90), 1v.3 (90), 43v.11 (89),
86r.9 (89), 94r.3 (89)**. Le clair de ces chaînes n'a été lu que par script (éligibilité, fuite) et n'a jamais été
affiché.
22r.1 et 61r.3 ne sont pas dans la mesure : elles ont servi au diagnostic et au réglage.

## Entrée
`transcriptions/<chaîne>.sig` = `cipher_lines` de `keys_eye/<chaîne>.json` seul. `|` = séparateur ; fin de ligne =
pas de séparateur (même lecteur `sigparse.py` que la piste 2).

## Modèles
- 4-grammes de caractères : celui de la piste 2, inchangé (`ljs51-aveugle/modele/lm4_sp.bin`, sha256 dans le
  MANIFEST).
- Lexique : `modele/lex.bin`, 124 376 formes (compte ≥ 2, 1-12 lettres), tirées de 9 textes OpenITI
  (`modele/CORPUS-LM2.txt`) : les 4 textes du modèle de la piste 2 + Yatīmat al-dahr, al-Wāfī, Aʿyān al-ʿaṣr,
  al-Durar al-kāmina, al-Nujūm al-zāhira. Exclus : Ibn Nubāta (calibration de la piste 2) et Ṣubḥ al-aʿshā
  (chapitre de cryptographie qui cite Ibn al-Durayhim).

## Solveurs (mêmes réglages de recherche pour les deux)
- MOTS : `scripts/salex` (`salex.c`), mode 0 : groupe dans le lexique → log((c+0,5)/N) ; sinon log P 4-grammes
  (« ␣mot␣ ») + ρ, avec **ρ = −5**. Objectif = somme − λ·(classes − lettres distinctes), **λ = 8**.
- CARACTÈRES : `ljs51-aveugle/scripts/sa` (inchangé), λ = 8.
- Les deux : 20 relances × 500 000 itérations, température 4 → 0,05, 70 % réaffectation / 30 % échange, sens direct et
  inverse (le meilleur objectif décide, sans regarder le clair), graine 2811 (chiffre réel), 2811+i (témoin i).
- ρ et λ choisis sur les 16 chaînes déjà mesurées, avec séparateurs (`diag/devgrid1.txt`), déclarées grillées.

## Mesure unique (`scripts/mesure2.py`)
- Refuse de tourner sans `--hash-poste=<URL>` ou si `mesure/RESULTATS.tsv` existe ; vérifie le MANIFEST.
- Référence : `chains_all.json` → `plaintext.text`, normalisé (`common.norm`), comme dans la piste 2.
- Accord en caractères = lettres appariées (difflib, autojunk=False) / la plus longue des deux chaînes (lettres seules).
- Témoins : 200 par chaîne **et par solveur**, signes mélangés (séparateurs conservés, `random.Random(2811·100003+i)`),
  passés au même solveur, comparés au même clair.
- Critère par chaîne et par solveur : accord ≥ 0,85 ET ≥ meilleur témoin + 0,30. Accord en mots rapporté, non décisif.
- Sorties : `mesure/RESULTATS.tsv`, `mesure/BILAN.md`, `mesure/HEURE.txt`, `mesure/DEBUT.txt`.
- Pas de seconde mesure ; aucun paramètre changé après le résultat.

## Biais et écarts déclarés
1. Les classes de signes de Daniel ont été faites en connaissant le clair (comme dans la piste 2).
2. Le lexique vient de textes où des vers du recueil peuvent figurer : on contrôle la fuite par 12-grammes (≤ 5 %),
   mais un mot rare d'un vers peut être dans le lexique sans que le vers y soit.
3. Les chaînes fraîches font 89-130 signes : elles sont un peu plus courtes que 22r.1 (167) et 61r.3 (113).
4. Gel par MANIFEST sha256 posté sur #1023, et non `freeze.py` (#1014), pour la même raison que la piste 2.
5. Le chemin du solveur de caractères pointe vers `ljs51-aveugle/` (fichiers figés par son propre MANIFEST) : leurs
   sha256 sont repris dans ce MANIFEST.
