# Règle de sélection — planche « delacroix1797-2511 », écrite AVANT les vignettes de la planche (25/11/2026)

Cible : `delacroix1797` chez Daniel (Delacroix → Létombe, dépêche n° 5, 25 messidor an V / 13 juil. 1797 ; NARA RG 59,
M30 roll 4, vues 0244 droite – 0245 gauche). Notre dossier : `../delacroix-1797/` (n° 649).
Données gelées lues le 25/11 : `origin/main:targets/delacroix1797/` (ciphertext.txt de Brackx, NOTES.md, profile.json,
beling2026/proposals/transcription_corrections.tsv). Aucune PR/issue ouverte sur la cible le 25/11.
Images : NARA (domaine public), `/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/delacroix-1797/dl/M30-004-0244.jpg`
(SHA 13cef462…) et `M30-004-0245.jpg` (SHA 75389957…). Recadrages et clé sous
`/Volumes/SPOF_2/Archives-Veille-cyber/planches-pistes-2511/delacroix1797/` (des recadrages de repérage, sans options ni
ordre, ont servi à localiser les groupes avant cette règle).

## Portion et seuil
Portion = la dépêche entière (653 groupes, bien plus de 300 caractères de clair). Lecture actuelle (NOTES.md de Daniel) :
415/442 mots = 0,939 ; 27 mots-trous. 95 % = 420/442 : il faut **5 mots** de plus. Le profil bloque les 8 corrections de
chiffres « tant qu'une personne n'a pas regardé les vues 0244-0245 » : cette planche est ce regard humain.

## Cibles (9 questions sur 8 groupes) — une question = un chiffre encadré ; options = formes de chiffres de la même main
| code | lieu (Brackx) | groupe transcrit | chiffre encadré | options | ce que change la réponse |
|---|---|---|---|---|---|
| T1 | 0244 dr. l. 11, 9e | 257 | 3e | 7 / 1 / 4 | 1 → 251 = « ai » (« je n'[ai] rien ») : +1 mot ; 7 → reste 257, trou maintenu ; 4 → 254, à examiner |
| T2 | 0244 dr. l. 17, 6e | 257 | 3e | 1 / 4 / 7 | 1 → 251 (« n'[ay]iez rien ») : +1 mot ; sinon trou maintenu |
| T3 | 0245 g. l. 15, 4e | 257 | 3e | 4 / 7 / 1 | 1 → 251 (« consul[ai]res ») : +1 mot ; sinon trou maintenu |
| T4a | 0244 dr. l. 19, 1er | 108 | 3e | 0 / 6 / 8 | 0 (avec T4b = 0) → 100 = « sur » (« détaillés [sur] tout ») : +1 mot ; 8 → 108/128, trou maintenu |
| T4b | idem | 108 | 2e (taché) | 2 / 0 | 0 → 108 ou 100 selon T4a ; 2 → 128, trou maintenu |
| T5 | 0245 g. l. 12, 8e | 808 | 2e (avec « 80 » écrit au-dessus) | 9 / 0 / 8 | 9 → 898 = « con » (« le[çon] ») : +1 mot ; 0 → reste 808 |
| T6 | 0245 g. l. 13, 1er | 1024 | 3e (taché) | 8 / 2 / 3 | 3 → 1034 = « e » (« pri[e] ») : +1 mot ; 2 → reste 1024 ; 8 → 1084, inconnu |
| T7 | 0245 g. l. 25, 8e | 327 | 1er | 5 / 3 | 5 → 527 = « d » (« [d]'envoyer ») : +1 mot ; 3 → reste 327 |
| T8 | 0245 g. l. 25, 11e | 381 | 2e (taché) | 6 / 8 / 0 | 6 → 361 (« sans [dél]ai ») : +1 mot ; 8 → reste 381 |

Gain maximal : 8 mots → ≈ 423/442 = 0,957 (contre 0,939). Seuil 95 % atteint si ≥ 5 des 8 groupes tombent du côté
« corrigé ». Si les « 257 » restent des 7 (cas probable, 3 lecteurs IA), il faut les 5 autres : T4 (100), T5, T6, T7, T8.

## Contrôles cachés (3), sans option jumelle
| code | lieu | réponse attendue | options |
|---|---|---|---|
| K1 | 0245 g. l. 13, « 474 », 1er chiffre | 4 | 6 / 4 / 3 |
| K2 | 0245 g. l. 12, « 266 », 3e chiffre | 6 | 2 / 6 / 7 |
| K3 | 0245 g. l. 13, « 972 », 1er chiffre | 9 | 3 / 2 / 9 |
Règle : si un contrôle échoue, les réponses sur la même forme sont tenues pour faibles (pas d'application sans second regard).

## Application
Une réponse « corrigée » ne s'applique qu'avec le décodage de la table de Beling (valeur attendue confirmée ailleurs) ;
elle est proposée à Daniel comme « regard humain sur les vues 0244-0245 », jamais comme une lecture nouvelle.
Réponses « aucune / impossible / illisible » = rien ne change. Exemples des formes : chiffres nets de la même main,
vue 0245 gauche lignes 1-6 (806, 694, 800, 799, 350, 972, 1031).
