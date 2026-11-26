# Règle de sélection — planche « Wąsowicz 1663, R7508 » du 23/11/2026 (cible cyphersolver wasowicz1662), écrite AVANT toute construction de vignettes

Pièce : ANK AKPot 3227 p. 235, Wąsowicz à Lubomirski, 5 mai 1663 (DECODE R7508, image IMG_R7508_I33935_P4.jpg, page de
droite, bloc chiffré). Image DECODE de Daniel (dudout_decode_2026-10-27, SPOF_2), 🔴 jamais publiée : planche PRIVÉE.
Cible : la nôtre (PR #135 mergée, Brice crédité « solution ») ; étape 0 (23/11) : `gh pr list --search wasowicz1662` → #135,
#174, #728 (règle de compte), #789 (notre page méthode, ouverte, sans rapport) ; aucune PR de tiers sur la cible.
Base : targets/wasowicz1662 (texts/R7508_transcription.txt gelée, decryption, profile gaps : « 12 of 48 cipher words carry a
blotted or ambiguous number (a flat-topped 3 read as 5, overwritten digits) »), key.tsv (table R7501).

## Critère
Chiffres douteux de R7508 notés [a/b] dans la transcription, regardés à l'image (×2-3) le 23/11, lisibles agrandis ; un chiffre
par question. Dans cette main le 3 (ʒ à tête plate), le 5 (ſ à drapeau) et le 1 (trait court) se ressemblent : les trois formes
sont proposées à chaque question.

## Cibles retenues (9) — ligne de la transcription, groupe
- **W1** l3 « 35 » (cho·d·ził), 2e chiffre (trait fin) ; **W2** l3 « 1[3/5] », 2e chiffre ;
- **W3** l6 « 3[5/1] » 1er groupe (rozumienia), 2e chiffre ; **W4** l6 « 3[5/1] » 2e groupe, 2e chiffre ;
- **W5** l7 « 2[3/5] » (marszałka), 2e chiffre ; **W6** l8 « 2[5/1] » (iesli), 2e chiffre ; **W7** l8 « [3/5]0 », 1er chiffre ;
- **W9** l8 « 3[5] » (fin de ligne), 2e chiffre ; **W10** l5 « 3[3/5] » (fin de ligne), 2e chiffre.
Options : 3 / 5 / 1.

## Contrôles nets (3) — chiffres de mots SÛRS
- **K1** l7 *marszałka* 2e « 53 », chiffre 3 (attendu 3) ; **K2** même groupe, chiffre 5 (attendu 5) ; **K3** l1 « 13 » (z de
  la 1re ligne), chiffre 1 (attendu 1).

## Écartés
- l2 « 5? » (zeby) : sous une grosse tache, illisible agrandi. l8 « 2[8/3] » (iak) : non retrouvé avec certitude à l'image.
- R7507, R7510 : bords déchirés / taches ; hors lot (une planche suffit, ≤ 12 questions).

## Alphabet (exemples ; jamais une cible ni un contrôle)
3 : l7 *marszałka* 1er « 53 » (le 3), « 13 » (le 3) ; 5 : l7 1er « 53 » (le 5), « 35 » (le 5) ; 1 : l7 « 13 » (le 1), l1 « 41 » (le 1).
Page : un seul chiffre encadré ; aucune glose ; « forme n » ; titre « Planche W ». Options texte habituelles. Ordre :
planche_core v2 (copie P2, vignettes agrandies), graines 20261123 / 1663. Export : reponses-2311-wasowicz.json.

## Intégration (après réponses, sur une copie locale)
1. Un contrôle raté (y compris « impossible à distinguer ») → rien intégré ; noté dans HANDOFF.
2. Chaque cible : le chiffre choisi remplace la notation [a/b] ; le groupe est relu par la table R7501 SANS valeur nouvelle ;
   un mot devient sûr seulement s'il se lit en entier par la table (#728). Réponse « impossible » ou « illisible » → inchangé.
3. Recompte de R7508 (36/48 au départ) et de la part lue (251/281) ; entrée HANDOFF datée ; mise à jour proposée à Daniel
   seulement si la règle des 95 % est franchie (≥ 267/281), sinon notée.
Gain maximal : W1-W10 portent 8 des 12 mots douteux → ≤ +8 mots → 259/281 (92,2 %).
