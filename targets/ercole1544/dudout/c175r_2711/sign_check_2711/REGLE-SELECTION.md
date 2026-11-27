# Règle de sélection — planche « ercole1544 c. 175r » (95-ercole1544-c175r / ercole1544-c175r-2711), 27/11/2026, écrite AVANT toute vignette

Catalogue cyphersolver 1556 (cible ercole1544, LcCompany/WAINUT). Pièce : Biblioteca Estense, Autografoteca Campori, Lettera G,
Gonzaga Ercole, sfasc. III, cc. 174-175 ; c. 175r = `campori-estense/G_ErcoleGonzaga_Ferrante_sd_cc174-175/003.jpg` (IIIF 1900 px),
un exemple de 17 pris en 174v (`002.jpg`, boîte déjà vérifiée sur la planche du 25/11).
**Droits** : CC BY-NC-SA, usage d'étude, NE RIEN REPUBLIER (NOTICE.txt) → planche PRIVÉE, servie sur le LAN seulement
(:8831 avec clé ?k=), jamais publiée ; aucune vignette ni dérivé commité (ni dans le clone de Daniel, ni ailleurs) ;
vignettes et clé sur SPOF_2 (`ercole-1544/work/planche-c175r-2711/`).

Base : arbitrage du 27/11 (`work/c175r-2711/arb/transcription_arb.txt`, 1 263 signes, 30 {x|y}) et lecture
`reading_0175r.md` (branche locale dudout/ercole1544-close, 3f8ab3d170) : 340 mots, **293 sûrs (86,2 %)**, 36 probables,
3 restitués, 8 irrésolus.

## Gain maximal (calculé avant sélection)
Sur les 36 {probables}, seuls ceux qui sont à UN signe douteux {x|y} de la forme verbatim peuvent devenir sûrs par une planche :
| mot | signe(s) | réponse qui le rend verbatim |
|---|---|---|
| {Fiandra} F01 | {c\|e} x≈1066 | e |
| {parentado} F08 | {c\|e} x≈1037 | e |
| {qual} F09 | {b\|h} x≈715 | h |
| {regno} F12 | {f\|t} x≈440 (+ {e\|c} x≈403 gardé e) | t (et e) |
| {pratiche} F18 | {c\|e} x≈602 | e |
| {con} F18 | {n\|a} x≈786 | a |
| {genti} F26 | {h\|t} x≈958 | t |
**Max = +7 mots : 293 → 300 sûrs / 340 (86,2 → 88,2 %).** Les autres probables ne dépendent d'aucun des 30 signes douteux
(fautes du chiffreur hors {x|y} : dueste, notu, sentia, consentar, afettara, beatentara, libepo, fopsi, alla, lettpa, pocai,
dipa, ingailterra, mandala, presa… ; ou codes à valeur de contexte L^o, 55). La règle de Daniel (97,6 % par le sens) ne change pas.
F07 {L^r|L^o} : 0 mot gagné (L^o = imperatore « par le contexte » reste probable) mais corrige le signe ; F01 {S|14} et F07 {17|27} :
confirmations de mots sûrs (massimamente, doppiamente), 0 gain, demandées par l'agent précédent ; F12 {e|c} : même mot que {f|t}
(regno n'est sûr qu'avec e ET t).
Écartés (aucun mot ne bascule) : F02 g/q, F06 y/e, F07 g/f et x/k, F08 24/2+q (déjà posé le 25/11, Brice : 2 q), F08 b/h (‹fordarsi›
reste irrésolu), F11 h/r, F13 -/f, F20 f/h (pervenutami reste restitué), F21 p/f, F22 r/e (sapeer → ni l'un ni l'autre),
F23 f/x, F24 z/g, les 5 {d|y} et F03 {19|S} (la forme ne tranche pas).

## Cibles (11) — boîtes (x0, y0, x1, y1) dans 003.jpg ; cadres larges (exposant de L dans le cadre)
- T01 F07 « b {L^r|L^o} h n q » L + exposant en v : (1079,546,1125,585). Formes L^o / L^10 / r (r de cette main, en v). Réf. L^o.
- T02 F12 « del re{f|t}no » signe haut à crochet : (431,830,449,880). Formes f (ʃ) / t. Réf. t.
- T03 F12 « del {e|c} » : (395,848,412,872). Formes e / c. Réf. e.
- T04 F09 « q{b|h}al » : (706,660,726,700). Formes b / h. Réf. h.
- T05 F26 « L {h|t} r a g x » : (946,1644,972,1686). Formes h / t. Réf. t.
- T06 F01 « n {S|14} x » : (1139,234,1175,274). Formes S / 14. Réf. S.
- T07 F07 « b {17|27} x » : (1195,553,1236,586). Formes 17 / 27. Réf. 17.
- T08 F01 « q {c|e} n » : (1055,236,1077,262). Formes c / e. Réf. e.
- T09 F08 « c n {c|e} r a » : (1028,618,1047,644). Formes c / e. Réf. e.
- T10 F18 « r c {c|e} n g » : (593,1199,611,1223). Formes c / e. Réf. e.
- T11 F18 « p b {n|a} x » : (776,1196,797,1223). Formes n / a. Réf. a.
(Réf. = premier choix de l'arbitrage ou valeur qui rend le mot verbatim ; sert seulement à équilibrer les places, noyau v2.)

## Formes — exemples réels de cette main, lieux sûrs (A = B = W), 2 par forme ; boîtes dans `scripts/items.py`
c : F01 « 30 c b c » 1er c ; F18 « r c » 1er c. — e : F04 « b c e r f » ; F18 « g e r 20 ». — b : F01 « c b c » ; F04 « n a b g ».
h : F01 « x h t » ; F04 « b g h n ». — f (ʃ) : F12 « g b f p » (toscana) ; F12 « 30 f r s » (se). — t : F01 « n t a n e » ; F01 « h t h ».
n : F01 « h n q » ; F08 « c n c ». — a : F01 « t a n » ; F04 « n a b ». — S : F17 « x S r » (dissegni) ; F16 « r S r » (esser).
14 : F05 « n 14 n » ; F11 « n 14 r ». — 17 : F12 « n 17 h » (appuntar) ; 174v E21 « n 17 x ». — 27 : F21 « q 27 x 78 » ; F16 « p r 27 r ».
L^o : F14 ; F18. — L^10 : F07 x≈390 ; F09 x≈868. — r : F18 « 20 r c » ; F08 « c r a ».
Boîtes vérifiées AVANT cette règle sur feuilles de localisation (loc/chk_*.png, pas des vignettes) ; corrections faites : e F01 remplacé par
e F04, f F12 recadré, 14 F11 recadré, T02, K1, K3 recadrés.

## Contrôles (3), forme nette, lecture sûre, options SANS sosie (pas de c/e, b/h, f/t, 17/27), places différentes (noyau v2)
- K1 F12 « g b f » b (toscana) (206,838,224,876) : options b / c / a, attendu b.
- K2 F17 « p e r q » e (creder) (892,1136,912,1162) : options e / a / h, attendu e.
- K3 F21 « 24 27 q » 2ᵉ 27 (883,1366,928,1396) : options 27 / 14 / S, attendu 27.

## Planche
14 questions (11 + 3). Une valeur par option, un signe encadré par question, options texte « aucune / autre forme », « illisible »,
« pas un signe » + remarque. Noyau v2 copié de PLANCHES/_outils/planche_core.py (inchangé) ; post-traitement dans make_planche.py :
JPEG ≤ 560 px, CSS `.opt .v img{max-width:40vw}`, page ≤ 1,8 Mo. Graines 2711175 / 1556. Export `reponses-ercole1544-c175r-2711.json`.
Correspondance (cle-PRIVEE.json) dans `work/planche-c175r-2711/prive/`, jamais chargée par la page.
Copies : `_planches-tel/95-ercole1544-c175r.html`, `_planches-serve/ercole1544-c175r-2711/planche.html`.

## Intégration
1. Un contrôle raté → rien intégré.
2. Forme choisie = valeur → portée sur une COPIE de transcription_arb.txt ; {x|y} levé. Mot devenu verbatim → sûr.
   T02 sans T03 = e : regno reste probable. T01 = r → [L^r] gardé (« re », sens douteux, noté) ; = L^o → signe corrigé, mot reste probable.
3. « aucune / illisible / pas un signe » → doute gardé.
4. T06 = 14 ou T07 = 27 → le mot sûr redevient probable (compte baisse) ; signalé.
5. Crédit LcCompany/WAINUT ; rien poussé ni posté sans accord de Brice.

## Avenant 1 (27/11 ~07 h 45, après la planche-contact, AVANT livraison ; cibles, formes, options et contrôles inchangés, seules 4 boîtes recadrées)
Version initiale hachée 0f169b250a42fa49279c8dc37a0da61a59106e8cc85a44271eb03a130b37af86 (items.py f811c358…). Vérification vignette par vignette
de crops/_contact.jpg : 10 questions sur 14 bonnes du premier coup ; recadrés :
- T04 → (709,660,728,700) (le cadre prenait la panse du d voisin) ; T05 → (952,1644,974,1686) (le cadre prenait la haste du L voisin) ;
- exemple b F04 → (663,372,686,419) (coupait le a) ; exemple h F01 → (409,216,433,260) (coupait le x).
