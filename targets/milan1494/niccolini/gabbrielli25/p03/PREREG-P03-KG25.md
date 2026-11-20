# PREREG P03 — clé extérieure Gabbrielli n° 25 (K_G25, inchangée) sur les lettres glosées de Niccolini jamais utilisées pour K_T — 14/11/2026

Écrit et haché AVANT toute transcription de signes ou de gloses de la portion. Aucune séquence de la portion n'a été décodée par
personne. L'agent principal a seulement regardé les pages entières (vue d'ensemble 1272 px et une découpe de 161) pour compter
les lignes chiffrées et voir si une glose interlinéaire existe ; il n'a pas lu les gloses mot à mot ni aligné un signe.

## Objets gelés avant ce PREREG (SHA-256)
- Clé : kg25/K_G25.json = 3a81cd6d1c12e14a70530b9a251c28e5162a8a99200f9b22f9dc15f1c2c41611 (inchangée depuis P02).
- Formes neutres : kg25/MAP_F_vers_G.json = eb23f56e49f38193309403ac1b55587e171fe43a042ed843b5404a4a4ec1461e ;
  planche SPOF_2 …/kg25-work/CATALOGUE_F.jpg = 5cbd6f5e4a1320136c2064f3bed682d1380b0f890c7ae08bb593d5d8dc8fab0a.
- Script : p03/measure_p03.py = 4e91a79d05cb0bb01b59e1c8fb5479799cd0c70d54d175f202f2f9d8233f20da (testé à blanc sur texte
  factice : 0,95 ; témoins max 0,37 — voir « Témoins » plus bas).

## Contrôle de taille (fait avant ce PREREG, sans décodage)
Comptage visuel des lignes chiffrées et de la présence d'une glose au-dessus (estimations, ± 20 %) :
- doc. 7 pos. 23 : presque tout en clair, < 10 signes chiffrés → inutile.
- doc. 35 pos. 158 : ~15 rangées chiffrées, ~400 signes, glose au-dessus de presque toutes ; pos. 159 : ~9 rangées, ~275 signes, glosées.
- doc. 36 pos. 161 : ~9 rangées, ~300 signes, glosées (gloses parfois courtes ou abrégées).
- doc. 37 pos. 167 : ~6 rangées, ~150 signes, glosées. doc. 59 pos. 254 : ~4 séquences, ~60 signes, gloses courtes.
- doc. 72 pos. 299 : ~25 rangées glosées très serrées (~700 signes) ; 300 : ~3 rangées ; 301 : clair (souscription).
- doc. 81 c. 176r pos. 351 : ~6 rangées, ~200 signes, glosées.
Total ≈ 2 000 signes chiffrés, dont la grande majorité sous glose ; 158 + 159 + 161 seuls ≈ 950. Seuil 300 atteignable.

## Portion (fixée ici)
Portion de base : toutes les séquences chiffrées des pos. **158, 159 (doc. 35) et 161 (doc. 36)**.
Extension (seulement si, APRÈS transcription arbitrée et gel des gloses, Σ jetons F des séquences C < 300) : ajouter des
pages entières dans cet ordre, sur les seuls comptes, avant tout décodage : 167, 351, 254, 300, 299. Pos. 23 et 301 exclues.
Pos. 332 (H de P01) et 329-331 (P02) exclues. Une fois mesurée, la portion est grillée.

## Transcription (sous-agents aveugles : ne voient ni K_G25, ni les valeurs, ni K_T, ni CLE_KT.json, ni HANDOFF, ni RAPPORT g3,
ni l'issue #589 ; ne voient que les images de la portion et CATALOGUE_F.jpg avec les identifiants F01-F39)
1. Passe signes T2 (sous-agent A) : chaque séquence, jeton par jeton, en F01…F39 (doute = « ? » final, un seul choix) ;
   signe hors catalogue → `X:<description>` ; groupe-code (nombre à plusieurs chiffres, HH, ⊙, 22, 100…) → `K:<forme>`.
   Fichier P03_SIGNES_T2.tsv, haché AVANT la passe glose.
2. Passe glose (même sous-agent A, après le hachage) : glose d'époque au-dessus de chaque séquence ; marque C (couvre toute la
   séquence, lisible) / P ; mots portés par un jeton K: entre { } ; notes entre [ ] ; abréviations développées seulement si
   évidentes et notées. Fichier P03_GLOSE_T2.tsv, haché.
3. Seconde passe signes T3 (sous-agent B, ne voit pas T2), mêmes règles, sur toute la portion. P03_SIGNES_T3.tsv, haché.
4. Arbitrage jeton par jeton sur l'image par le sous-agent A (aveugle à la clé), qui reçoit T3 après le gel de T2/T3,
   journal d'arbitrage noté. Version arbitrée P03_SIGNES_FINAL.tsv hachée AVANT la mesure. Les gloses ne sont pas arbitrées
   (sauf C/P si l'arbitrage change le découpage d'une séquence, noté).
L'agent principal n'arbitre pas les signes (il connaît K_G25).

## Mesure (UNE seule, measure_p03.py tel que haché)
- Unités : séquences C. Seuil : Σ jetons F (hors X:, K:) ≥ 300, sinon NON MESURABLE (après extension éventuelle).
- Décodage : F → G → valeur K_G25 ; « ? » ignoré (le choix compte) ; X: → vide ; K: → vide et mots { } retirés de la glose.
- Normalisation des deux côtés (= P01/P02) : minuscules ; v→u, j/y→i, k→c, h supprimé ; tout sauf a-z supprimé ; lettres
  doublées réduites à une.
- **Métrique décisive : caractères** = 1 − Σ distance d'édition (décodage, glose) / Σ longueur(glose normalisée).
- Témoins : 200 clés = valeurs de K_G25 permutées entre les 39 formes (random.Random(2380)), même calcul.
- **Critère : accord ≥ 0,85 ET ≥ meilleur témoin + 0,30.** K_G25 inchangée ; jamais rétroactif.
- Rapporté, non décisif : accord en mots (mots de glose ≥ 3 lettres retrouvés tels quels dans le décodage normalisé ; et tous
  mots), mêmes chiffres pour les témoins ; part des jetons couverts par le catalogue F ; détail par séquence.

## Témoins — leçon Fuensalida (déclarée d'avance)
Les témoins par permutation peuvent être structurellement hauts : K_G25 donne 3 formes à a, e, i, o et 2 à c, h, l, m, n, r,
t, u ; une permutation garde donc beaucoup de voyelles, et l'édition sur des chaînes courtes favorise les accords fortuits
(test à blanc : meilleur témoin 0,37). Si les témoins sortent hauts, on le dit tel quel ; **on ne change ni le critère, ni la
métrique, ni les témoins après coup.** Plafond structurel connu : K_G25 n'a ni b, ni g, ni z (feuille Gabbrielli) ; chaque b/g/z
de la glose coûte une erreur (≈ 3-4 % du texte italien) ; il est accepté tel quel.

## Suite selon résultat
- Validée : lecture des nues 2380 (docs 42 c. 90r, 49 c. 104r, 81 c. 177r, 90 c. 200r) avec K_G25 ; fiche stricte (sûrs /
  {probables} / [restitués] / ‹irrésolus›), règle des 95 % ; livrable relance/niccolini-2380/. 2381 NON revendiqué (#589).
- Non validée : plafonné ; aucun décodage présenté.
