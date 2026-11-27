# Règle de sélection — planche « trezzo1464-2511 », écrite AVANT les vignettes de la planche (25/11/2026)

Cible : `trezzo1464` chez Daniel (catalogue 1320 ; Antonio da Trezzo → Fr. Sforza, 8 sept. 1464, BnF ital. 1590 f. 392,
Gallica btv1b10037390v vue 393). État : « decoded, not read » (#648, arya1515). Aucune PR/issue ouverte « trezzo » le 25/11.
Notre dossier : `../` (HANDOFF : H = f. 392 GRILLÉE le 25/11 pour la mesure ; cette planche ne revendique aucune lecture).
Images : Gallica (public), `../work/t392_full.jpg` (= vue 393, recadrage natif ; source « A ») et `../sources/f284.jpg`
(vue 284 = f. 283r, même main ; source « B »). Coordonnées des cadres (pixels de A ou B) : `scripts/items.json`
(gelé avec cette règle). Les cadres ont été vérifiés sur une planche-contact de repérage AVANT ce hachage (K1 recalé).

## Pourquoi
NOTES de Daniel : « les étiquettes regroupent des formes que la clé distingue ». Lecture par le sens de la sortie décodée
(decode392_refined de #648 + notre clé fusionnée) et comparaison des deux transcriptions indépendantes (c392 de #648 ↔ notre
H-final) : 10 signes où les deux lecteurs divergent (ou où une forme voisine donne un mot) et où la forme décide un mot.

## Questions (10) — une forme encadrée ; options = formes nettes prises ailleurs (lieux où les deux lecteurs concordent, ou f. 283r à clair connu)
| code | lieu (H-final) | H / #648 | options (formes) | ce que change la réponse |
|---|---|---|---|---|
| T1 | L06 #26 | pz / p7 | pz · p7 · r | p7 (= s) → « essere » (…desiderio essere) : +1 mot ; pz (= t) → trou maintenu ; r → à examiner |
| T2 | L07 #15 | pz / p7 | p7 · r · pz | p7 → « h p7 pz oo » = « questo » (comme f. 283r « h py pz » = quest- ×5) : +1 mot ; pz → « qutto », trou |
| T3 | L13 #20 | hz / hr | h · hr · ly | hr (= ell) → « h hr op » = « quella » : +1 mot ; h / ly → trou |
| T4 | L10 #27 | hz / hr | hr · ly · h | hr → « h hr o^n » = « quelle » : +1 mot ; sinon trou |
| T5 | L09 #14 | d^n / δ~ | d~ · d^n · d^o | d^n (= on) → « …ontent… » (contento/contenti) ; d~ (= or) → « …ortent », trou ; d^o → à examiner |
| T6 | L07 #10 | d^n / δ~ | d^n · d^o · d~ | d^n → « q^n q^a y oi d^n » = « electione » : +1 mot ; d~ → « electior », trou |
| T7 | L10 #20 | y / r | y · r · p7 | r → « r ec r et o » (decreto/secreto) : +1 mot ; y (= t) → « ctet o », trou ; p7 → à examiner |
| T8 | L04 #3 | qi / 4e | qe · q · qn | qe (= es) → « …restitucione » : +1 mot ; q / qn → trou ; « qi » = forme propre si « aucune » |
| T9 | L06 #20 | qi / 4e | q · qn · qe | qe → « desiderio » : +1 mot (avec T1) ; sinon trou |
| T10 | L10 #14 | l^n / L^a | l^n · L · l^a | l^n → « la S.V. che » ; l^a → « sua che » ; L → à examiner (les deux premiers lisibles : tranche la lecture) |

Exemples des formes (cadres dans items.json) : pz = L03 #23 (« onestamente ») ; p7 = f. 283r l. 1 « h py pz » (quest-) ;
r = L02 #6 ; y = L03 #26 ; h = L07 #14 ; hr = f. 283r l. 6 « h hr » ; ly = f. 283r l. 6 ; d^n = L03 #21 (« onestamente ») ;
d~ = f. 283r l. 2 #2 ; d^o = L06 #1 ; qe = L03 #22 ; q = L06 #17 ; qn = L06 #22 ; qa = L01 #24 ; l^a = L06 #6 ;
l^n = L11 #4 ; L = L10 #9 ; t = L06 #5 ; oto = L10 #25. Aucun exemple n'est pris sur un lieu de question.
Chaque paire d'options diffère par la forme ET par la valeur (vérifié sur la planche-contact ; pas de jumelle).

## Contrôles cachés (3), sans sosie parmi les options
| code | lieu | attendu | options |
|---|---|---|---|
| K1 | L11 #1 (t, les deux lecteurs) | t | qa · t · l^a |
| K2 | L11 #7 (oto, « sono ») | oto | oto · q · d^n |
| K3 | L13 #18 (qa, les deux lecteurs) | qa | y · l^a · qa |
Règle : un contrôle manqué → les réponses sur la même famille de formes sont tenues pour faibles (second regard avant usage).

## Gain possible et application
Si tout tombe du côté « mot » : ≈ 10 mots sur ≈ 120 (606 lettres décodées) ; f. 392 resterait « decoded, not read » (aucune
phrase ne tient), mais on saurait QUELLES étiquettes scinder (pz/p7, hz=hr, d^n/d~, qi=qe, y/r) pour une re-transcription à
formes fines puis un réalignement de 283r-284r (la seule voie restante, H étant grillée pour la mesure). Les réponses ne
s'appliquent qu'aux transcriptions (signes), jamais comme lecture ; proposées à Daniel/arya1515 comme « regard humain sur la
vue 393 ». Réponses « aucune / impossible / illisible » = rien ne change.
