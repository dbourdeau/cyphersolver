# Règle de sélection — planche « Guarna 21/5/1447 » du 23/11/2026 (cible guarna1447, notre travail), écrite AVANT toute construction de vignettes

Pièce : BnF, italien 1584, f. 153r (Gallica btv1b100373864, vue 146 ; SPOF_2 …/sforza-envoyes-1447/gallica-ital1584/f146.jpg,
7746 × 5348, déjà récoltée le 05/11 ; « Source gallica.bnf.fr / BnF »). Aucun téléchargement fait.
Base : clone de lecture _shared/cyphersolver (main f280c87b99) targets/guarna1447 : transcription.txt (jetons de forme),
reading.md (852 mots : 583 sûrs, 33 probables, 236 irrésolus estimés), clé K3 (c03-2026-11-05/cle-K3-guarna.json, sha 8a16f1de…).
Aucune PR ouverte sur guarna1447 au 23/11 (gh search). K3, transcription.txt et reading.md ne sont pas modifiés par la planche.

## But (reprise prévue au HANDOFF du 05/11)
Les signes voisins de cette main, que la transcription du 05/11 sépare « au jugé » (TRANSCRIPTION-163v-suite.md, tokens-Hprime.txt) :
- **ɧ** (crochet à droite) : étiqueté « hk » (valeur r) ou « 4 » (i/h/f) ; tokens-Hprime : « pas séparable à coup sûr » ;
- **σ / ơ** : « ot » (t, boucle fermée à barre/queue haute) contre « oe » (e, boucle ouverte à appendice).
La question est de FORME : un humain voit-il deux formes distinctes, et laquelle à chaque lieu ? Ce n'est pas une question de
valeur ; la valeur suit l'étiquette par K3 inchangée.

## Critère
Lieux du bloc H (f. 153r l. 2–7, image nette) où l'étiquette d'un de ces signes est douteuse ou tombe dans un passage
irrésolu ou probable ; regardés à l'image le 23/11 (×1,7–1,8).

## Cibles retenues (5)
- **G1** H04 jeton 17 (« hk », passage « {parere} [?3] ») : ɧ-r / ɧ-i. Le décodage de ce passage (par q hk 4 ff 4 t) est
  incohérent avec le nombre de signes vus : à l'image on ne voit qu'UN ɧ entre « q » et « ff » (transcription : « hk 4 »).
- **G2** H04 jeton 20 (« 4 », même passage) : ɧ-r / ɧ-i.
- **G3** H05 jeton 1 (« oe », passage « [?2] che ») : σ / ơ.
- **G4** H05 jeton 13 (« oe », mot probable {vostra} = pi b hs oe ot hk q) : σ / ơ. À l'image le signe ressemble au σ.
- **G5** H05 jeton 15 (« hk », même mot) : ɧ-r / ɧ-i.

## Contrôles nets (2), signes de mots SÛRS
- **K1** H02 « questi » (gp pc **ot** pi) : σ attendu (options σ / ơ).
- **K2** H02 « benedetti » (6 **oe** qn 7 a) : ơ attendu (options σ / ơ).
Pas de contrôle ɧ : si ɧ-r et ɧ-i sont une seule forme, aucun contrôle ɧ ne peut avoir de réponse sûre (voir Écartés).

## Écartés
- ꞇ (t / T / z) et Ъ (hs / h) : à l'image du bloc H, les ꞇ vus (H02 « a », H04 jeton 21) ont la même forme ; pas d'exemple
  sûr de T et z repéré dans les lignes nettes ; à poser sur une planche suivante (163r–163v, paire avec la copie).
- Les autres irrésolus : questions de VALEUR (polyphonie de K3), hors planche de forme.

## Alphabet
- ɧ-r : exemples H02 « remediare » 1er signe (hk = r), H04 « servi{re} » (hk = r, partie sûre) ;
- ɧ-i : exemples H02 « remediare » 6e signe (4 = i), H04 « servi{re} » (4 = i) ;
- σ : exemple H07 « questo » (ot) ; ơ : exemples H02 « remediare » (oe), H07 « questo » (oe).
Exemples = signes de mots SÛRS, même main, jamais une cible ni un contrôle ; vérifiés sur crops/_contact.jpg.
Page : un seul signe encadré en rouge ; aucune glose ; « forme n » ; titre « Planche G ». Options texte habituelles (dont
« impossible à distinguer », réponse attendue et UTILE pour ɧ). Ordre : planche_core v2 (copie lot P1, clé dans prive/),
graines 20261123 / 1447. Export : reponses-2311-guarna.json.

## Intégration (après réponses, sur une copie ; transcription.txt, K3 et reading.md inchangés)
1. Un contrôle raté (y compris « impossible à distinguer ») → rien intégré ; noté dans HANDOFF.
2. σ / ơ (G3, G4) : réponse = l'autre forme → étiquette corrigée (oe ↔ ot), passage redécodé avec K3 inchangée ; un mot n'est
   compté SÛR que s'il se lit en entier par K3 (#728) ; sinon il reste {probable} / irrésolu. Réponse = forme transcrite →
   étiquette « ! » (lue à la planche), compte inchangé. G4 : si σ, « vostra » perd son « e » parasite (vos·t·tra → à redécoder).
3. ɧ (G1, G2, G5) : si Brice choisit une forme distincte à chaque lieu ET que les exemples r/i ne lui paraissent pas
   « impossibles à distinguer », l'étiquette suit sa réponse et le passage est redécodé (même règle de compte). Si la réponse est
   « impossible à distinguer » : on note que ɧ est UNE forme (homographe r/i de la main) ; la transcription garde les deux
   étiquettes mais K3 doit fusionner « hk » et « 4 » en un seul signe polyphone (avenant à écrire AVANT toute nouvelle mesure).
4. Aucune valeur n'entre dans K3 par la planche. Recompte (sûrs ; sûrs + probables) et entrée HANDOFF datée.
Gain maximal attendu : faible et non prévisible mot par mot (≤ 3 mots du bloc H, déjà consommé comme réserve : aucune mesure
nouvelle sur H). Le but principal est la règle de transcription ɧ / σ-ơ pour la retranscription fine de 153–154.
