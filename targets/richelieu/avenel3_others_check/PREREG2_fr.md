# PREREG2 — autres pièces chiffrées d'Avenel t. III (système 1629-1630), clé de la PR #813

Rédigé et gelé le 20/11/2026 (fil 🔓), **avant tout décodage** des pièces ci-dessous avec la clé. Les gloses d'Avenel ont été lues pendant la transcription (imprimées sur les mêmes pages) : limite déjà déclarée dans le PREREG de #813.

## 1. Matériel gelé

| Objet | Fichier | sha256 |
|---|---|---|
| Transcription (passe V2, images archive.org `lettresinstructi03richuoft`, chaque nombre lu sur recadrage) | `transcription/avenel_figures_V2.txt` | `7c848ec8e516fe771252f8215140ecf44ee708b2c36cd2da9ee849f7cde6c650` |
| Clé de la PR #813, `targets/richelieu/texts/key.md` @ `fbc611f8e9c4deb3363587d570a308193d9514d7` | `cle-813/key813.md` | `6a47387b839cb45fe39a2e77b1d5f51f661846c66d9ed6f9354a555c8975c591` |
| Même commit, `targets/richelieu/final.py` (KEY, 41 = que, NOMEN étendu) | `cle-813/final813.py` | `79003b84ccc972a39660c0367e14fde1930b9ca9d30bc474a5964ba30ca015a0` |
| Outil (écrit avant exécution, non exécuté) | `outils/describe.py` | `15bdc3343d79784402c913bab0db1aa89f94cd176cbdd72c1da4b532fbd77125` |

## 2. Pièces et statut (constaté sur les images avant décodage)

Toutes les pièces candidates du rapport 🔎 portent un déchiffrement imprimé par Avenel :
- **CLVI** (Béthune 9331 fol. 44, 1er mai 1629, à Bouthillier ; doublet de CLV) : 15 notes-gloses, tout glosé → EXISTING.
- **CLXXIV** (Béthune 9331 fol. **46**, mai 1629) : 3 suites glosées + codes glosés → EXISTING.
- **CCCXII** (Turin XI fol. 136, 5 mars 1630) : 4 suites glosées ; code 63 non expliqué (« Nous ne trouvons pas le sens de 63 ») → EXISTING, 1 code ouvert.
- **CCCXIV** (Turin XI fol. 187/298, 8 mars 1630 ; « déchiffrement interlinéaire de la main de Bouthillier ») : 21 suites, toutes glosées → EXISTING.
- **CCCXVI** (Turin XI fol. 300/317) : imprimé en clair d'après Bouthillier ; une suite citée en note avec sa lecture (« de Saint-Luc ») → EXISTING.
- **CCCXVII** (Turin XI fol. 323, 10 mars 1630) : « n'a pas été déchiffrée » **par le secrétaire**, mais Avenel l'a déchiffrée et l'imprime en clair ; il ne donne les figures qu'en deux endroits : la Morane (n. 1 p. 581, lecture donnée) et la suite finale de 14 signes, dont il **imprime la valeur de chaque lettre** sans lecture en mots → EXISTING au niveau des lettres ; la segmentation en mots est ouverte.
- **CCCXXXII** (Turin XI fol. **359**, 31 mars 1630) : 9 suites/codes, tous glosés → EXISTING.
- **CCXLV** (9 oct. 1629) et **CCLIII** (8 nov. 1629 ; le rapport disait CCLII, qui n'a pas de chiffre), à Châteauneuf : **autre table** (chiffre de l'ambassade de Londres : 60 ≠ Mme de Longueville ; « 10 25 12 11 » = *Scot* d'après la minute, ce que la clé de Rancé ne donne pas). Codes seuls, hors protocole.

## 3. Mesure

- **Portion sans déchiffrement imprimé** : segments sans glose, plus la suite finale de CCCXVII (lettres données, mots non). Comptage avant décodage : **14 signes** (CCCXVII n. 4) ; aucun autre segment n'est sans glose.
- Règle (consigne du fil) : **< 300 signes → « non mesurable »**, description seulement. Le seuil (≥ 0,85 ET ≥ meilleur contrôle + 0,30) n'est donc **pas appliqué** ; aucune mesure n'est faite.
- **Description** (une seule exécution de `describe.py`) : accord en caractères entre la clé #813 (gelée, sans aucune extension nouvelle) et les gloses d'Avenel, même score que #813 (distance d'édition contre la meilleure sous-chaîne de la glose normalisée), par pièce et pour l'ensemble EXISTING ; 200 tables mélangées (permutation des valeurs 10–38, codes de mots conservés ; graine 20261120) **à titre de repère**, sans valeur de test.
- 42 reste « la » dans la clé ; ses emplois « le / les » (1630) apparaissent comme écarts, ils ne sont pas corrigés.

## 4. Comptage #728 (règle stricte de Daniel, PR #813, 19/11)

- Mots chiffrés seulement ; mêmes unités que #813.
- **Sûr** : toutes les lettres viennent de la clé sans correction et le mot fait sens ; ou code de la **table de Daniel @ 9736c436** (51, 52, 54, 58, 59, 60, 66, 83, 84, 92) employé avec sa valeur ; codes de mots 39, 40, 41, 42.
- **Trou** : code dont la valeur vient de la glose locale ou du contexte (règle stricte de Daniel) ; code de l'extension #813 (55, 61, 62…) s'il apparaît : compté à part (variante), car sa valeur vient d'Avenel ; correction d'un nombre (probable {x}) ; 59 lu « duc de Mantoue » contre la table ; code inexpliqué (63).
- Seuil « lu » : ≥ 95 % ; plancher < 40 mots : trous ≤ 2 ou ≤ 5 %.

## 5. Extensions de clé

Seulement depuis des pièces EXISTING, au sens E2 de #813 (code glosé par Avenel à l'endroit, suites voisines en accord). Toute valeur nouvelle est **déclarée** et reste « d'après Avenel » ; elle ne rend aucun mot sûr selon la règle stricte.
