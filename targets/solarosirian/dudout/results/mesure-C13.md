# C13 — mesure unique de la table v5 sur la portion neuve (2026-11-16 19:13 CET)

Protocole : `PREREG-C13.md` (SHA f1aedecd…) + `AVENANT-1-C13.md` (zone F ajoutée avant lecture). Table `table-v5.json` (f3ad6282…). Script `measure_c13.py` (95c9d862…). Transcription arbitrée (98308750…). Lecture aveugle gelée (cd2cab3c…) avant toute ouverture des publications. Référence `reference.json` produite APRÈS ce gel par Opus 5.5 (API, run 2), sans la table. Résultat brut : `mesure.json`.

## Résultat (mesure faite une seule fois)
| | valeur |
|---|---|
| Signes de la portion (A–F) | 428 (A 42, B 47, C 21, D 159, F 159) |
| Couverture de la table (signes ayant une valeur) | 70,3 % |
| Signes notés par la référence (valeur phonétique ou PL) | **65** (351 « ? », 12 DET) |
| **M = justes / notés** | **27 / 65 = 0,415** |
| Témoins (200 tables permutées) | moyenne 0,018 ; **maximum 0,154** |
| Seuil | M ≥ 0,70 **et** M ≥ max + 0,30 |
| **Verdict pré-enregistré** | **ÉCHEC** : M < 0,70, et M − max = 0,26 < 0,30 |

Le signal est réel (27 justes contre 1,2 en moyenne pour les témoins, aucun témoin au-dessus de 10/65). Mais il n'atteint pas le seuil fixé d'avance : **la table v5 ne « lit » pas la portion neuve.**

## Indicateurs secondaires (sans décision)
- **Substitutions de la table** (S28 = s, 3 points = PL, M17x2 = y, etc.) : 18/26 = 0,69. **Valeurs ordinaires** : 9/39 = 0,23.
- **Par zone** : A 11/19 ; B 5/11 ; C 1/1 ; F 10/27 ; D (chapelle) 0/7.
- **Écart de normalisation, découvert après la mesure et non corrigé** : la référence écrit ꜥ (U+A725) là où la table écrit ʿ (U+02BF). Ces deux caractères ne figuraient pas dans les équivalences gelées. En les rapprochant, on obtiendrait 29/65 = 0,446, toujours sous le seuil. Le chiffre de décision reste 0,415.

## Pourquoi l'échec (analyse après la mesure)
1. **La référence est trop pauvre.** 85 % des signes y sont « ? » : Darnell & Darnell 2018 donne une traduction anglaise sans translittération, et Darnell 2004 (édition signe à signe) n'est pas accessible. Le dénominateur (65) est donc petit et biaisé vers les étiquettes courtes.
2. **La référence a mal placé la zone F.** Elle a aligné les colonnes F sur l'annotation du registre 3 (« They exist in this fashion in the Place of Destruction… »). Or F est l'**annotation cryptographique de la Section droite, scène 1** (« This god is in this fashion, his arm in the Upper Region, his feet in the Place of Destruction… »). Les valeurs qu'elle donne pour F sont donc en partie fausses. Je ne pouvais pas lancer de troisième run (plafond de 2), et la mesure n'est pas refaite.
3. **Il manque des valeurs dans la table** (classes de forme nouvelles, sans valeur) :
   - BOUTON = *p* (5 cas, dans *pn*) ;
   - OBLNOIR = *nṯr* (mât-drapeau R8 tracé en oblique) ;
   - BOLCORNES = *ḏw* (montagne N26 renversée ?) ;
   - V6 = *š* (acrophonie de *šs*, et non le bilitère).
4. **La chapelle (D) est illisible à 15 px par signe.** Aucune des deux passes ne vaut mieux qu'une devinette, et la référence n'a rien aligné (7 signes, 0 juste).

## Ce que la mesure établit quand même
- La partie « substitution » de la convention, apprise sur la chapelle et sur Ramsès IX (C03–C12), se transfère à un passage jamais lu avec environ 70 % de justes.
- La partie « valeurs ordinaires » est faible. Elle est aussi sous-estimée, à cause des classes de forme créées pour ce passage, qui n'ont pas de valeur.
- **La portion N13 est grillée** pour toute nouvelle mesure de la table v5 ou d'une table v6.
