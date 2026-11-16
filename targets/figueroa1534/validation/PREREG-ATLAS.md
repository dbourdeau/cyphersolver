# PRÉREGISTREMENT P-ATLAS — n° 744 figueroa-1534 — transcription guidée par l'atlas Estense (14/11/2026)
Gelé par SHA-256 (PREREG-ATLAS.sha256) AVANT tout regard sur 1547 img04 / img06 (PARES 3615615). Reprend PREREG-ATLAS-PROPOSITION.md tel que rédigé, avec UNE addition (témoins intra-classe, § Mesure).

## Clé
- K4 inchangée : `working/ags1545/K4.tsv` (SHA a456e5bba6ee788371827d73ffa263ae034c98615bfb1f91dfdac3de90632ed6). Aucune valeur changée.
- Étiquettes de FORME : `working/p-atlas/LABELS-FORMES.md` (gelé ici). Constat à l'étalonnage : les 76 familles de l'atlas correspondent toutes à des étiquettes K4 existantes ; aucune nouvelle étiquette n'est donc ajoutée à K4 (« K4A » = K4, même SHA). Une étiquette absente de K4 compte « hors clé ».
- Atlas : `working/atlas-estense/atlas.tsv` (SHA 4ba643ea…65eb) + planches A-D (ATLAS.sha256).

## Étalonnage (fait AVANT gel, entraînement seulement)
- 1547 img02 l. 1-4 ↔ clair img11 (fin) ; règles 1-6 de LABELS-FORMES.md § C. Aucun regard sur img04 / img06.

## Écart déclaré avant gel (contamination possible du lecteur principal)
- En lisant le dossier, le lecteur principal (agent orchestrateur P-ATLAS) a vu passer à l'écran la fin de `working/c05/clear_1547_full.txt` : la copie en clair img13 (depuis « Yo desseo ») – img14 – DÉBUT img15 (« como havia hecho … que le fuessen pagados de sus bienes », ≈ 400 car.). Ce début d'img15 correspond très probablement aux premières lignes du chiffré img06 ; la fin d'img13 correspond à la fin d'img04.
- Parade, fixée ici : le lecteur principal NE transcrit PAS la portion tenue à l'écart. Passe 1 = sous-agent A ; passe 2 = sous-agent B, sans accès à la passe 1 ; arbitrage = sous-agent C, sur l'image, avec les deux passes mais sans valeurs ni clair. A, B, C : interdiction de lire le clair (img11-17, `clear_*.txt`), K4 (valeurs), les transcriptions antérieures et les mesures ; ils ne reçoivent que : bandes de lignes de la portion, planches A-D, `LABELS-FORMES.md`. Le lecteur principal ne fait que des opérations mécaniques (découpe des bandes, fusion, calcul).

## Portion tenue à l'écart (une seule)
- 1547 chiffré **img06 entier** (toutes les lignes chiffrées). Si < 300 jetons après arbitrage : ajouter les DERNIÈRES lignes de img04, de la dernière vers le haut, ligne entière par ligne entière, jusqu'à ≥ 300 jetons, décidé sur le seul compte des jetons.
- Référence : `working/c05/clear_1547_full.txt` complété par la transcription de la copie en clair img15-16 (et img13 si img04 est ajouté), faite APRÈS l'arbitrage gelé ; fenêtre choisie mécaniquement par le script (Smith-Waterman, ± 40 car.).

## Transcription
- Étiquettes de forme (LABELS-FORMES.md) ; signe non identifié = `?…` ; choix d'étiquette jamais guidé par un décodage ; cachets/taches = `?tache`.
- Transcription arbitrée gelée par SHA AVANT la lecture du clair img15-16 et avant le calcul.

## Mesure (une seule)
- `cryptanalysis/p-atlas/score_atlas.py` (gelé ici) : reproduit `cryptanalysis/c05/score_k4.py` à l'identique (précision LCS caractères, normalisation C04, fenêtre SW, 200 témoins clé entière, graine 744 — vérifié : il redonne 0,795 / max 0,472 sur img05 grillé) et ajoute **200 témoins intra-classe** (graine 744) : permutation des valeurs à l'intérieur de chaque classe — LETTRE (valeur d'une lettre), SYLLABE (2-3 lettres : syllabes, groupes cr/pr/tr…, doubles), CODE (nomenclateur : étiquette `{…}` ou valeur ≥ 4 lettres), NUL (inerte). Raison (leçon Fuensalida 14/11) : la permutation sur la clé entière envoie des valeurs longues sur des signes fréquents, gonfle la longueur décodée et change la base du rappel ; la permutation intra-classe garde la structure de longueur et constitue le témoin le plus dur.
- Les deux plans sont rapportés ; `score_k4.py` est aussi lancé tel quel sur la même transcription.
- **Seuils (sur le plan intra-classe)** : score ≥ 0,85 ET score ≥ max(témoins intra-classe) + 0,30 ET hors clé ≤ 20 %. Sinon : NON VALIDÉ. La portion est grillée dans tous les cas.
- Rétro-information (sur img05 grillé, pas une mesure) : témoins intra-classe médiane 0,473, max 0,510 (contre 0,432 / 0,472 clé entière).

## Ensuite
- Si VALIDÉ : fiches strictes 1547 puis lot 1553 dans l'ordre 312, 242, 364, 296, 351-353 ; livrable PR dans `lots-classement-1411/relance/figueroa-1534/`. La planche de Brice (planche-312) peut servir pour le lot 1553 seulement.
- Si NON VALIDÉ : chiffres rapportés tels quels ; pas de PR de lecture.
