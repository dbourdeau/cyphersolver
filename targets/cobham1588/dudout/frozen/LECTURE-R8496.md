# LECTURE — DECODE R8496 (BL Harley MS 287 ff. 96-97) — Cobham à Walsingham, Bourbourg (« Binborow »), 9 juin 1588

2026-11-13, agent Opus, fil Déchiffrement. **Au compte de Daniel Bourdeau** (`targets/cobham1588`, catalogue n° 131). 🔴 Aucune image ni découpe DECODE publiée ; citer « DECODE R8496 ».

## Statut (exact)
**Lu en partie : 18 mots chiffrés sur 30 lus par le sens = 60 %** → **read in part** (seuil 95 % non atteint). Détail : 7 sûrs, 11 probables, 1 restitué, 11 irrésolus. **Codes : aucun** (ni nombre, ni ◻, ni signe-code ; les « ·I· » de la passe 1 sont des W).
Le clair autour n'a été relu que par les deux passes de transcription (lectures incertaines, marquées « ? ») : pas de pourcentage pour la lettre entière.

## Méthode
1. Transcription arbitrée `R8496_chiffre.tsv` (SHA256 dad10ca5…dbce), hachée avant décodage (addendum `PREREG-B.addendum-B1-R8496.md`, SHA b171405d…820c). Désaccords : `R8496_arbitrage.md`.
2. Décodage brut : `R8496_decodage_cle_gelee.txt` (script `decode_cle_gelee.py` non modifié). **Défaut du script** : il coupe les mots sur « | » avant de lire les accolades, donc chaque {a|b} est cassé (sortie fautive aux passages qui en ont). Copie corrigée de cette seule ligne (scratchpad `decode_r8496_accolades.py`, même clé, même logique) → `R8496_decodage_cle_gelee_accolades.txt` ; c'est elle qui sert à la lecture.
3. Valeurs nouvelles seulement dans `R8496_cle_derivee.tsv` : r (Γ) = a (B), T = e (B), S = h (C).
4. Classement comme LECTURE-R8490 : *sûr* = clé gelée ou dérivée de force A, mot qui fait sens ; *probable* {x} = une valeur B/C ou nouvelle, ou une lettre manquante, sens net ; *restitué* [x] = ≥ 2 signes changés ; *irrésolu* ‹…›.

## Choix dans les ensembles
- Λ (A) : t dans *the*, *letters* (t t), *written*, *forth*, *treater* (1er, 5e) ; s dans *servant*, *preist* (s), *letters* (s final), *passed* (s s) ; a (dérivée C, Λ large soudé) dans *treater* (4e). Autres valeurs ne donnent pas de mot.
- {Q|7} (forme ambiguë) : 7 = e dans *servant* (2e), *treater* ; Q = a dans *servant* (5e), *England*, *Westmorland*, *captan*.
- Y = r dans *treater* (pas y) ; L (ϕ) = p dans *passed*, *preist*, *captan* (dérivée C, Daniel « ϕ for p ») et = l dans *letters*, *England*, *Earle*.
- c = o dans *forth* (gelée), = a dans *captan* (dérivée A).

## Tableau des mots chiffrés
| id | signes | brut (clé) | lecture | statut | justification |
|---|---|---|---|---|---|
| C01a | A h 7 | the | the | sûr | clé gelée |
| C01b | r V L L E | ?rlle | {Earle} (« Arlle ») | probable | r = a (nouvelle, B, cf. France) ; graphie *Arlle* pour Earl, l doublé ; suivi de « of » |
| C01c | R F | of | of | sûr | R = o (A) |
| C01d | W 7 A A Y u V L {Q|7} I O | westrurlaid | [Westmorland] | restitué | 11 signes = 11 lettres ; w e s t … r l a … d tombent de la clé, mais Y = m, u = o, I = n changés (3 signes) ; le comte de Westmorland, rebelle de 1569, exilé aux Pays-Bas espagnols |
| C01e | L U A A T D | latttd | {passed} | probable | L = p (C), A A = s s, T = e (nouvelle, B, cf. written) |
| C01f | B | X | b x | ‹…› | irrésolu | « by » (X = i, « bi ») possible mais non établi ; X peut appartenir au clair |
| C02a | W I A h | with | with | sûr | clé gelée |
| C02b | R N | on | ‹on› | irrésolu | décode « on » sans retouche, mais « with on France » ne fait pas phrase (*within* exigerait R = i) |
| C02c | F V r N 8 E | fr?nce | {France} | probable | r = a (nouvelle) ; tout le reste gelé |
| C02d | A {Q|7} V u | c A | taru ot | ‹serves ?› | irrésolu | « s e r v e s » possible (Q lu 7, c = e C) mais le sens avec le clair voisin n'est pas établi |
| C03 | V c L 7 V | roler | ‹roler / roper› | irrésolu | « of ‹…› and of his » : nom propre possible (Roper ?), non vérifiable |
| C04a | A {Q|7} V u {Q|7} N A | taruant | {servant} | probable | s e r v a n t : chaque signe dans son ensemble, mais forme {Q|7} lue une fois 7 (e), une fois Q (a, B) ; « of his servant » |
| C04b | I S R N | i?on | {Ihon} | probable | S = h (nouvelle, C) ; *Ihon* = John (graphie du temps) |
| C04c | L V 7 X A A | lrextt | {preist} | probable | L = p (C), X = i (C) ; *preist* = priest (Daniel signale « priests » ici) |
| C05 | A V 7 A A {Q|7} Y | trettar | {treater} | probable | 4e Λ = a (C, Λ soudé), {Q|7} lu 7 = e, Y = r ; *treater* = négociateur |
| C06a | R F | of | of | sûr | |
| C06b | L E A A E V A | lettert | letters | sûr | E = e (A) ; dernier Λ = s |
| C06c | F c V A h | forth | forth | sûr | clé gelée (*for th[e]* possible si le groupe suivant commence par r = e) |
| C06d | r L {Q|7} O I W {U|v} u 8 R | aladiwauco | ‹…› | irrésolu | aucune coupe ne donne un sens |
| C07a | W V I A A T N | writttn | {written} | probable | T = e (nouvelle, B) ; « that he hath written … » |
| C07b | N A R | nto | {into} | probable | i manquant (ou absorbé par le N précédent) ; sens net |
| C07c | {7|T} N G L {Q|7} N O | england | {England} | probable | {7|T} = 7 (e), Q = a (B), O = d (A) ; « written into England » |
| C08a-b | {8|P} V {Q|7} F A I A V r A {7|T} V {P|Y} | craftitr?terp | ‹…› ‹…› | irrésolu (2) | « craft… », « …trater… » : pas de mot sûr |
| C09 | W I A A E | witte | ‹witte› | irrésolu | *wit* possible, sens non établi |
| C10a | F L {Q|7} 8 E | flace | ‹…› | irrésolu | « flace/flece » |
| C10b | A R | to | to | sûr | clé gelée + R = o (A) |
| C10c | {7|T} u V | evr | ‹evr› | irrésolu | « ever » manquerait un e ; sens non établi |
| C11a | {8|P} {Q|7} L A c N | caltan / captan | {captan} | probable | 8 = c, Q = a, L = p (C), A = t, c = a (A) ; *captan* = captain (i manquant ; Daniel signale « captain » ici) |
| C11b | B {Q|7} V V {I|W} N r X | barrin?x | ‹B…› | irrésolu | « Barrin… » : nom propre ? (après *captan*) |

Comptes : 30 mots ; sûrs 7 (the, of, with, of, letters, forth, to) ; probables 11 ; restitué 1 ; irrésolus 11. (18/30 = 60 %.)

## Texte anglais (chiffre en gras ; clair des passes, incertain, en italique)
*… the Bastill, and the Arsenal, in their hands.* **the {Earle} of [Westmorland] {passed} ‹b x›** *ys himself … arryved(?)* **with ‹on› {France} ‹serves?›** *o^r they … hath informed yow, of* **‹roler›** *and of his* **{servant} {Ihon} {preist}** *a doller(?) …* **{treater}** *, and a tarrie(?)* **of letters forth ‹…›** *and that sondely(?) …* … *that he hath* **{written} {into} {England}** *the … : P and he … and rather* **‹…› ‹…›** *thys* **‹witte›** *, ther may sent a good fare(?) … how* **‹flace› to ‹evr›** *y^t ys / I pray let me knowe by yow … what order you take for* **{captan} ‹B…›** *I pray let me here from yow.*

## Résumé
- FR : après les nouvelles de Paris (la Bastille et l'Arsenal aux mains des ligueurs), Cobham signale, en chiffre, un comte (« the Earle of [Westmorland ?] ») qui serait passé, un serviteur prêtre nommé Ihon (John), un « treater » (négociateur), des lettres, et quelqu'un qui a écrit en Angleterre ; il demande à Walsingham quel ordre il prend pour un capitaine (« captan B… »). Beaucoup de mots restent irrésolus ; le sens précis n'est pas établi.
- EN: after the news from Paris (the Bastille and the Arsenal in the Leaguers' hands), Cobham reports in cipher an earl ("the Earle of [Westmorland?]") who has passed, a servant priest called Ihon (John), a "treater" (negotiator), letters, and someone who has written into England; he asks what order Walsingham takes for a captain ("captan B…"). Many words remain unresolved: read in part (60 %).

## Codes
Aucun dans cette lettre (pas de nombre, pas de ◻, pas de signe-code). Rien pour la mesure de codes (PREREG-B §Valeurs de codes).

## Écarts avec Daniel (ajouté après hachage, 2026-11-13)
La lecture ci-dessus a été hachée AVANT ouverture de `texts/R8496_reading.md` de Daniel : SHA256 7e04d0f1c4b136e055139ebf6112c508083a4bd3fbcd1a3b010c1ab410053c30, copie inchangée `LECTURE-R8496.hachee.md`. Cette section n'en fait pas partie ; aucune correction de la lecture hachée.
- **Accords** (mots que Daniel donne aussi, au moins en « ? ») : *the* (l. 1), *passed* (ŧ = e, comme notre T = e), *within/with on* + *France* (son ŧ = notre r Γ ; il lit Γ = a dans France, comme nous), *Roper* (chez lui « a guess », chez nous irrésolu), *servant(s)*, *Iohn* (chez lui « a guess », chez nous {Ihon} probable avec S = h), *priests/preist*, *of letters*, *written*. Notre Γ = a / T = e rejoint ses valeurs ŧ = a/e.
- **Nouveaux chez nous, non lus chez Daniel** : {Earle} + [Westmorland] (l. 1 ; restitution à 3 signes, faible), {treater} (l. 3, `AV7AA7ϑ` chez lui non lu), {into} {England} (l. 8 ; il transcrit `AnAAT7nӾ ϕ7nc`, nous `N A R {7|T} N G L {Q|7} N O` : écart de transcription — son « n » / notre N « tH », son ϕ = notre L), {captan} (l. 12 ; il voit un Λ de plus, comme notre passe 1, que nous avons écarté comme jambage de « cypher »).
- **Lus chez lui, non chez nous** : *for the [?people]* (l. 4) : il lit `AϸT` = *the* avec ŧ = e et `ϕ7cϕl` = people ; notre transcription arbitrée du même groupe est `r L {Q|7} O I W …` (O et I là où il voit c et ϕ) → notre C06d reste irrésolu ; à revoir sur l'image (écart de transcription, pas de clé). S'il a raison, notre *forth* devient *for the* (r = e), ce qui ferait de Γ un signe a/e.
- **Transcription** : Daniel note `ǂǂ` pour notre F (H à barre doublée) et `n` pour notre N (tH) — même distinction que la nôtre. Il compte un Λ en plus en l. 12 (et sans doute en l. 8), cf. arbitrage C07/C11.
- **Clair** : ses lectures du clair diffèrent beaucoup de celles des passes (« works overthrown », « a doctor in », « caried », « shortly », « what order yow have given for » …) ; le clair n'est pas notre objet ici.
- Bilan : Daniel ne donne aucun pourcentage (« partial reading ») ; notre 60 % reste « read in part ». Ajouts proposables : *treater*, *into England*, *captain*, et l'alignement Γ = a / T = e.
