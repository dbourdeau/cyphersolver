# PREREG — ljs51-aveugle : confirmation en aveugle des clés de LJS 51 et règle d'Ibn ʿAdlān

Rédigé le 28/11/2026 (UTC) avant toute mesure. Agent : piste 2 de la campagne LJS 51 (Claude Opus 5.5 pour Brice Dudout).
Base : dbourdeau/cyphersolver `origin/main` = d8ac608093e1149f9456eaa2c99bb456ca0abc92.

## Question
Les 199 clés de `targets/ljs51corpus/keys.tsv` / `keys_eye/` (D. Bourdeau) sont tirées du clair du compilateur
(« by-eye key from the compiler's plaintext, not independently confirmed »). Un solveur qui ne voit QUE le chiffre
retrouve-t-il ce clair ? Avec quel taux de réussite selon la longueur (règle d'environ 90 lettres d'Ibn ʿAdlān) ?

## Chaînes (fixées avant les résultats ; `transcriptions/SELECTION.tsv`)
- Lot L : 20r.8+47r.1, 22r.1, 19r.7, 105v.6, 18r.11, 23r.9, 61r.3, 30r.4, 42r.2, 39v.12.
- Lot E : 2 chaînes par tranche 30-45, 46-60, 61-75, 76-90 signes, tirées par `random.Random(5151).sample` sur les
  chaînes éligibles triées (clair présent, `answered == "yes"`, hors exclusions), en prenant dans l'ordre du tirage les
  2 premières dont la fuite 12-grammes est ≤ 5 %. Résultat : 56v.8, 6v.11 | 41r.3, 31r.11 | 35v.8, 69v.11 | 46r.11, 82r.9.
- Exclues : 14v.7, 22v.9, 37v.12, 48r.8 (et 21r), 106v.*, 3v.12, 98v.10, 1r.2, 12v.*, 30v.7, 63v.*, 47r.1 seul.

## Entrée
`transcriptions/<chaîne>.sig` = champ `cipher_lines` de `keys_eye/<chaîne>.json` SEUL (script `selection.py`) ; aucun
champ dérivé du clair n'est lu par le solveur. `|` = séparateur de mot ; fin de ligne = pas de séparateur.
Le clair n'a été lu que par script (éligibilité, fuite) et n'a pas été affiché.

## Modèle de langue (indépendant de `lang/` de Daniel)
4-grammes de lettres, 28 lettres + espace, interpolation fixe 0,70/0,20/0,07/0,03, add-0,01 (`build_lm.py`), sur 4 textes
OpenITI : al-ʿUmarī *al-Taʿrīf*, dīwān de Ṣafī al-Dīn al-Ḥillī, al-Ṣafadī *Alḥān al-sawājiʿ* et *Kashf al-ḥāl*.
Le dīwān d'Ibn Nubāta est tenu HORS du modèle et sert seulement à la calibration synthétique.
Variante sans espaces pour les chaînes sans séparateurs (69v.11, 6v.11).

## Contrôle de fuite (fait avant le gel)
Proportion des 12-grammes (lettres seules) de chaque clair présents dans le corpus du modèle : 0 % partout sauf 69v.11
(3,2 %). Aucune chaîne > 5 % : aucune exclusion.

## Solveur (`sa.c`, `solve.py`)
Recuit simulé, substitution simple avec homophones permis (plusieurs classes → une lettre ; aucune classe → espace),
séparateurs respectés. Objectif = log P(texte) − λ·(K − lettres distinctes), λ = 8. 20 relances, 500 000 itérations,
température 4 → 0,05 géométrique ; mouvements : 70 % réaffectation, 30 % échange. Les deux sens de lecture sont
essayés (direct, inverse) ; le meilleur objectif décide, sans regarder le clair. Graine 2811 (chiffre réel), 2811+i
(témoin i).

## Calibration (avant le gel, déclarée)
- Chiffres synthétiques tirés du dīwān d'Ibn Nubāta (hors modèle), homophones à 12 % : λ ∈ {0, 2, 5, 6, 10, 25},
  20 relances, 2×10⁵ puis 5×10⁵ itérations. λ = 8 retenu (entre 6 et 10, les meilleurs).
- Contrôle positif déclaré : 48r.8 (déjà publié en aveugle par Daniel et par nous ; clair connu) : le solveur retrouve
  l'énigme (« ولانه الاعطاف واسعه … »), −2,10 par symbole. 48r.8 n'est pas dans la mesure.

## Mesure unique (`mesure.py`)
- Référence : `chains_all.json` → `plaintext.text` (clair du compilateur), normalisé (`common.norm`). Pour
  20r.8+47r.1 seulement : champ `plaintext` de `keys_eye/20r.8+47r.1.json` (clair assemblé par Daniel pour la chaîne
  réunie), faute d'une entrée réunie dans `chains_all.json`.
- Accord en caractères = lettres appariées par `difflib.SequenceMatcher` (autojunk=False), divisées par la plus longue
  des deux chaînes (lettres seules), comme la métrique `char` de tools/holdout.
- Témoins : 200 par chaîne, signes mélangés (positions des séparateurs conservées, fréquences conservées,
  `random.Random(2811·100003+i)`), passés au MÊME solveur, comparés au MÊME clair.
- Critère par chaîne : accord ≥ 0,85 ET accord ≥ meilleur témoin + 0,30. Accord en mots rapporté, non décisif.
- Sorties : RESULTATS.tsv, COURBE.md (réussite × longueur en signes et en classes), DESACCORDS.md (chaînes validées :
  classes où la lettre aveugle diffère de la lettre majoritaire de Daniel ; aucun arbitrage automatique).
- Pas de seconde mesure ; aucun paramètre changé après résultat.

## Biais et écarts déclarés
1. Les classes de signes (S1, S2…) ont été faites par Daniel EN CONNAISSANT le clair : fusions/séparations de formes
   peuvent favoriser le cassage.
2. 30r.4 n'est pas aveugle pour le projet : sa clé et son clair ont servi dans ljs51-f30v7, et l'inspection de structure
   du JSON a affiché ici sa table de clé (28/11). Résultat rapporté, mais compté à part.
3. 20r.8+47r.1 chiffre l'énigme de 48r.8, dont le clair est connu du projet (relecture du 27/11). Résultat rapporté,
   compté à part.
4. Le contrôle positif 48r.8 a servi à vérifier le solveur avant le gel.
5. Gel par MANIFEST sha256 (et non `freeze.py` de la PR #1014 : le protocole de `measure.py`, clé fixe contre clés
   mélangées, ne correspond pas à un recassage aveugle avec témoins recassés).
