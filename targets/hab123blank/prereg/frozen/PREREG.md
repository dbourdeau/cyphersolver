# PREREG — HAB Cod. Guelf. 123 Blank., f. 59v (scan 00120), cat. Bourdeau 3807 — 27/11/2026
Gel AVANT toute mesure. Mesure UNIQUE, à lancer seulement après publication du manifeste de gel (convention holdout de Daniel, PR #1014).

## Antériorité (vérifiée le 27/11)
Catalogue cyphersolver (origin/main 401e355) : fiche 3807 = vetting Codex 23/11 seulement (« No decipherment of the last leaf was located »,
« No mapping was tested »), aucune réservation ni travail. leads.json, git grep du dépôt, PR et issues (gh, « 3807 », « 123 Blank », « Foremberger ») : rien.
Nos dossiers : rien. Butzmann (p. 131) signale le chiffre sans lecture.

## Transcription
Deux passes aveugles indépendantes (agents A et B, sans hypothèse de clé), puis arbitrage aveugle des 38 discordances sur agrandissements
par un 3ᵉ agent qui n'a pas vu la clé → transcription/ARBITREE.txt (principale). Passe B rapportée à titre secondaire.
Accord A/B brut (groupes identiques, notations +/t et 2/z rapprochées) : 0,654 en lettres.

## Portions
Règle fixée avant la clé (REGLE-PORTION-RESERVEE.md, sha256 f4ef9527…) : réserve = de « Cognitum » (L30) à la fin, étendue vers le haut jusqu'à ≥ 300 lettres.
Comptée sur ARBITREE : réserve = L19–L46, 56 groupes, 315 lettres (PORTION-RESERVEE-L19-L46.tsv). Portion de clé = L01–L18 + marges.
ÉCART DÉCLARÉ : un essai de déchiffrement a affiché L18 (hors réserve, 63 lettres) pendant la construction de la clé ; la réserve L19–L46 n'a jamais été déchiffrée.
Le transcripteur-arbitre ne connaissait pas la clé ; l'auteur de la clé a vu la transcription (non déchiffrée) de la réserve.

## Clé gelée K1 (CLE-K1.json)
Substitution simple : voyelles décalées d'un rang (a→b, e→f, i→k, o→p, u→x) ; consonnes b–m numérotées (b=1/j, c=2, d=3, f=4, g=5, h=6, l=8, m=9) ;
n→o, p→+ (t en croix), r→t (tau) ou r, s→d, t→c (ou e), q→q. z et les signes absents de la portion de clé = inconnus.
Texte de la portion de clé : latin alchimique et pharmaceutique mêlé d'allemand (lune, saturno, ueneri(s), martis, anthimonio, litargir, sigillum,
capellam/capellarum, treibscherben, sinter, inbiberem, additione, sedecimam, quantitate, libenter, lauatura…).

## Mesure (scripts/measure.py, une seule exécution)
Pour chaque groupe éligible de la réserve (scripts/groups.py ; exclus : groupes « clair? », sigles fh/p~k/kt…, groupes à majuscule ou abréviation, barrés, < 2 lettres) :
déchiffrement par K1 ; le groupe compte comme lu (toutes ses lettres justes) si le mot obtenu (u=v, i=j=y) est dans scripts/lexique.txt (lexique générique gelé,
écrit avant tout déchiffrement de la réserve), ou en est une abréviation (préfixe ≥ 4 lettres), ou radical lexical ≥ 4 + désinence latine de la liste, ou 2 mots du lexique accolés ;
tout signe inconnu (?) = faux. Accord = lettres lues / lettres totales.
Témoins : 200 clés obtenues en permutant les valeurs claires de K1 entre ses signes (graine 3807), même transcription, même lexique.
Étalonnage (fait le 27/11 sur la portion de clé L01–L17, ARBITREE, même lexique) : 0,592 ; témoins ≤ 0,039.
CRITÈRE fixé : accord(ARBITREE, L19–L46) ≥ 0,503 (= 0,85 × 0,592, SEUIL.txt) ET ≥ meilleur témoin + 0,30.
Écart déclaré au seuil générique de 0,85 : il suppose une glose de référence ; ici la référence est un lexique, d'où le seuil étalonné.
Rapportés sans être décisifs : accord sur la passe B ; lecture par le sens (règle de Daniel, sûrs/{probables}/[restitués]/‹irrésolus›) faite APRÈS la mesure.
Après la mesure, la réserve est grillée ; aucun changement rétroactif de clé, lexique ou transcription.
