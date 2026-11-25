# Règle de sélection — planche « rossi1537-2511 » (lettre B, c. 33r), écrite AVANT toute vignette (25/11/2026)

Cible : `rossi1537` chez Daniel (Rossi di San Secondo → Ferrante Gonzaga, 8 nov. 1537 ; BEU Modena, Campori R, Rossi c. 33r).
Données gelées : `origin/main:targets/rossi1537/` (units.tsv, dt_ledger.tsv, holes.md, transcription_B.txt), lues le 25/11.
Images : IIIF Estense (édl-jarvis), régions 1709×600 à pleine résolution, **étude privée** : blocs, recadrages, vignettes et
`cle-PRIVEE.json` sous `/Volumes/SPOF_2/Archives-Veille-cyber/planches-pistes-2511/rossi1537/` ; jamais dans un dépôt ni publiés.

## Pourquoi la lettre B
Portion = lettre B entière (755 unités, ≥ 300 car.). Mesures actuelles : unités, d/t par le test aveugle 717/755 = 94,97 %
(il manque 1 unité pour 95 %) ; mots (règle de Daniel) 154/166 = 0,928 (il manque 4 mots). La lettre A (1 613 u.) demande
+ 10 unités sur le seul verso et aucun de ses trous de mots ne dépend d'une forme décidable : pas dans cette planche.

## Cibles (13) — unité = n° d'unité de units.tsv ; options = formes
| code | lieu | signe transcrit | options | ce que change la réponse |
|---|---|---|---|---|
| T1 | B10 u29 | z | z / D(l) | D → « [?valli] » lu (clé « uarli ») : +1 mot, +1 unité |
| T2 | B10 u35 | P | d / t / l | l → « [?meglio] » lu (« megtio ») : +1 mot, +1 unité |
| T3 | B12 u43 | P | d / t / l | d → avec T4 = t, « [?vedeti] » lu : +1 mot, +6 unités N |
| T4 | B12 u45 | P | d / t / l | t → (avec T3) idem |
| T5 | B16 u38 | S | S / 8 | 8 → « [?viver] » lu sans émender S : +1 mot |
| T6 | B16 u41 | P | d / t / l | d → « [?di] » lu ; T5+T6 conformes : +7 unités N (B16 u36-42) |
| T7 | B03 u1 | P | d / t / l | d (lecture) → +1 unité (aveugle B = t aujourd'hui) |
| T8 | B05 u37 | P | d / t / l | d → +1 unité |
| T9 | B06 u14 | P | d / t / l | t → +1 unité (aveugle A = d) |
| T10 | B12 u24 | P | d / t / l | d → +1 unité |
| T11 | B12 u29 | P | d / t / l | t → +1 unité |
| T12 | B13 u24 | P | d / t / l | d → +1 unité |
| T13 | B16 u4 | P | d / t / l | t → +1 unité |
T7-T13 = toutes les unités P de la lettre B où la classe aveugle contredit la lecture (class_blind = E, lecture d ou t).
T1-T6 = les trous de holes.md de la lettre B qui ne dépendent que d'une forme de signe (B10, B12 vedeti, B16 viver di).
Exclus : comodità (sens, pas forme), Castel[...] (nom non identifié), com[...]gie (signe perdu au bord), B07 T (sans valeur).

## Contrôles (2, jamais cible ni exemple ; options sans sosie)
K1 B05 u33 « 8 » (lecture u) : options 8 / S, attendu 8. K2 B06 u6 « z » (lecture r) : options z / D(l), attendu z.
Pas de contrôle d/t (paire jumelle, interdite en contrôle).

## Exemples de formes (lettre B, verdicts aveugle et non aveugle concordants « high », jamais cible ni contrôle)
d : B03 u26 (P, A high, lu d) ; t : B03 u28 (P, B high, lu t) ; l : B04 u29 (D, C high, lu l) ;
z : B03 u10 (lu r) ; 8 : B03 u36 (lu u) ; S : B03 u3 (lu p). Si un exemple est illisible ou mal localisé sur l'image,
remplaçant : d B09 u20, t B04 u10, l B06 u20, z B03 u17, 8 B06 u11, S B03 u44 (remplacement noté dans cle-PRIVEE.json).

## Page
15 questions (13 + 2 contrôles), ordre tiré (graine 20261125), places des options équilibrées (logique planche_core v2),
contrôles à des places différentes. Un seul signe encadré en rouge, ligne de contexte + agrandissement, aucune glose ;
options « forme n » (vignettes) + « aucune / autre forme », « impossible à distinguer », « illisible », « pas un signe » +
remarque. Export `reponses-rossi1537-2511.json` : téléchargement + copie + zone de texte (téléphone).

## Intégration (future)
Un contrôle raté → rien intégré. Sinon chaque forme choisie remplace la classe aveugle de l'unité (classe « relu Brice, aveugle ») ;
« aucune / impossible / illisible » → inchangé. Recompte units (S/E/N) et mots de la lettre B ; succès = lettre B ≥ 95 % en unités
avec les classes aveugles + Brice, et ≥ 158/166 mots. Gain maximal si tout tombe : unités 717 → 739/755 (97,9 %) ; mots 154 → 159/166 (95,8 %).
Limite : valli / meglio restent de sens douteux même lettres confirmées (à dire).
