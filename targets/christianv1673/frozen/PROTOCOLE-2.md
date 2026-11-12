# PROTOCOLE-2 — christianv-1673 : validation de la clé par vérité terrain (glose d'époque), écrit et figé AVANT la mesure

Date : 2026-11-11. Auteur : agent Opus (fil 🔓). Remplace, pour la validation, le critère « danois / lexique » du PROTOCOLE (1) :
le bloc final de 1673 est lu et brûlé ; un code est validé quand son décodage **reproduit la glose d'époque** d'une pièce tenue à l'écart,
même si des permutations syllabiques produisent aussi du danois.

## Pièce tenue à l'écart
- Volume (62 images vérifiées sur planches-contacts) : pièces chiffrées seulement aux images 8-11 (ordre du 25 mai 1673, sans glose sauf la feuille volante 9 d.)
  et 32-43 (ordres de 1674, glosés entre les lignes). Trois ordres de 1674 :
  **A** = images 32-37 (« … Kiøbenhafn den 21 July Anno 1674 », signé) ; **B** = images 39-41 d. (3 oct. 1674, signé, + Post Scriptum) ;
  **C** = images 42-43 (« Datum 6 octobris loco et anno ut supra », signé Christian / Griffenfeld).
- **Pièce tenue à l'écart : C (images 42-43)**, relevé `working/pairs/1674_img42.tsv` + `1674_img43.tsv` (≈ 1 250 lignes, ≫ 300 groupes),
  figés le 11/11 à 15:07 (FREEZE.sha256, contrôle OK avant cette mesure), **non corrigés** depuis.
- Clé v2 (`working/KEY-v2.json`) construite SANS aucune paire de C : `scripts/mesure2.py buildkey` = TSV 32-41 (ordres A et B) avec les
  corrections `working/groupes-retrouves/CORRECTIONS-RELEVES.tsv` (toutes sur 33-41) + groupes de 3 chiffres de la feuille 1673 absents des TSV 32-41.
  Valeur = glose majoritaire pondérée (s = 2, p = 1, ? = 0,5) ; seules les unités d'un seul jeton (pas de glose « + » à la suite) donnent une paire.
- Notation : signes ramenés à un identifiant canonique par `working/notation/TABLE-SIGNES.tsv` (planche faite par un sous-agent sans ouvrir 42-43) ;
  étiquettes à deux canons : à l'entraînement, règle par la glose (RULE dans mesure2.py) ; **dans la pièce C, premier canon listé** (A4 « 4 » → SIG_4ouvert, A4 « 9 » → SIG_9) ;
  étiquette SIG_? ou absente de la table → non décodée (comptée fausse).

## Ce qui a déjà été vu de la pièce C (déclaration)
1. Le relevé 42-43 a été fait ce jour par le sous-agent A4 (gloses lues sur l'image) ; ses paires sont entrées dans `key_1674_v0.json`, `KEY-v1.json` et
   `agg_1674.txt`, que l'agent principal et des sous-agents ont lus (agrégats par groupe, toutes images confondues).
2. L'agent principal a affiché, avant le choix de la pièce, l'inventaire des étiquettes de signes **par relevé** incluant 42-43 (ex. A4 « 3 » glosé i ×21, A4 « m » glosé u ×6,
   A4 « Z » = n ×80). Ces observations n'ont servi ni à la table de notation ni aux règles ci-dessus (la table vient de la planche faite sur 32-41 et 8-11).
3. L'agent principal a vu l'image 43 entière (réduite, gloses visibles) et une bande du haut de 42 g., pour établir les limites des pièces.
4. Les sous-agents « planche » et « groupes absents » n'ont ouvert ni les images 42-43 ni leurs TSV.
5. Étalonnage fait AVANT, sans C (`mesure2.py calib`) : clé A → test B : exact 0,769 (536/697), max 50 clés permutées 0,109, max décalages 0,032 ;
   clé B → test A : exact 0,706 (1224/1734), max permutées 0,141, max décalages 0,032.

## Mesure unique (`python3 scripts/mesure2.py mesure`)
- Unité = segment de glose : jeton chiffré dont la glose n'est pas « + » + les jetons « + » qui le suivent ; mots en clair exclus.
  Unités exclues du calcul : glose vide, « - », « [… », contenant « ? », conf « ? », ou vide après normalisation.
- Décodage déterministe (concaténation des valeurs de KEY-v2 ; jeton numérique douteux « 8?60 » lu sans « ? ») ; **exact** si norm(décodage) = norm(glose)
  (normalisation de mesure.py : w→v, ø/ö→o, æ→e, ck/c/q→k, ff→f, y/j→i, ß→s, lettres doublées réduites).
- Contrôles : 200 clés permutées (valeurs mélangées entre groupes de 3 chiffres et, séparément, entre autres signes ; graine 20261111) ;
  20 décalages de la glose (unité i comparée à la glose de l'unité i+d, d = 1…20).
- Critères (tous requis) :
  - C0 : ≥ 300 unités notées dans C ;
  - **C1 (principal) : exact ≥ 0,65** ;
  - C2 : exact ≥ max(200 clés permutées) + 0,40 ;
  - C3 : exact ≥ max(20 décalages) + 0,40.
- Verdict : C0-C3 tenus → clé v2 VALIDÉE (le code de 1674 reconstruit par les gloses se transporte à une autre pièce), puis relecture de la cible 1673 ;
  sinon → résultat négatif consigné, pas de relecture présentée comme validée.
- Une seule exécution. Après la mesure, aucune modification de la clé ni du relevé C ne refait la mesure ; toute correction est consignée en v3.

## Portée
- La mesure valide la clé reconstruite sur les ordres de 1674 (mains M74a/M74b). Le transport à 1673 (main M73) repose en plus sur la feuille volante
  (bloc 1 lu presque mot à mot avec la même clé) et sur la table des signes (canons par main, ex. m barré = k en 1673, u en 1674).
