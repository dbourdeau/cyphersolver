# LECTURE — DECODE R8495 (BL Harley MS 287 ff. 92-93) — Cobham à Walsingham, « Belgia », 27 mai 1588

2026-11-13, agent Opus, fil Déchiffrement (relance 13/11). **Au compte de Daniel Bourdeau** (`targets/cobham1588`, catalogue n° 131). 🔴 Aucune image ni découpe DECODE publiée ; citer « DECODE R8495 ».

## Statut (exact)

**Lu en partie : 12 mots chiffrés sur 38 lus par le sens = 32 %** (7 sûrs, 5 probables, 5 restitués, 21 irrésolus). Aucun code (nombre, ◻, ·x·) dans le chiffre de cette lettre. **Seuil de 95 % très loin → « read in part ».**

## Méthode

1. Deux passes aveugles (R8495-pass1/pass2), arbitrage sur l'image → `R8495_chiffre.tsv` (16 passages, 212 signes) **haché avant tout décodage** : SHA256 `66e8bb5a7c0b84ee33b16350c24801c10da6b914eacc47899eaa5531b74267d3` (addendum `PREREG-B.addendum-B1-R8495.md`).
2. Décodage brut à la clé gelée (script et clés inchangés) → `R8495_decodage_cle_gelee.txt`. **Artefact du script** : il coupe les mots sur « | » avant de lire les hésitations {a|b}, donc R01 « {L|h} » et R08/R09/R14 « {+|X} » y apparaissent scindés (« ? | ? ») ; traités ici à la main (L = l/p, h = h ; + = b, X = x/c/i).
3. Valeurs nouvelles seulement dans `R8495_cle_derivee.tsv` (attestations, force A/B/C) ; clés gelées intactes.
4. Unités de lecture = mots anglais. Écart déclaré au découpage du fichier haché : R02 « I R N | A R N » lu comme un seul mot (blanc faible noté à l'arbitrage) ; R10 « A h 7 V E A R 8 » = deux mots + un signe (there / to / c…) ; R10 « 7 N d I 7 N A R F N E · Y L R V A » = ancient / of / Newport ; R11 « F d V W · V T N G R F » = forwarding / of ; R11 « … A h 7 7 » séparé ; R12 = captein + ‹…›.
5. Classement (strict, comme R8490) : *sûr* = chaque signe pris dans son ensemble de clé (gelée ou dérivée R8490), sens net ; *probable* {x} = un seul signe hors clé / hors ensemble / à statut de transcription douteux ; *restitué* [x] = ≥ 2 signes changés, mot donné par le sens ; *irrésolu* ‹…› = pas de mot.

## Choix entre valeurs d'ensemble (justifiés)
- **A = s / t** : *captein* (t), *inprisoned* (s), *Bridgis* (s), *Bridges* (s), *there* (t), *to* (t), *Ionson* (s, R02 « A R N »), *at*/R13 n'emploie pas A.
- **L = l / p** : p dans *captein*, *inprisoned*, *preist*, *Newport* (Daniel note ϕ = p sur ces lettres) ; l nulle part de sûr.
- **d = o** (R8490) : *inprisoned* ; contre-proposition d = c dans *ancient* (restitué).
- **c = o / a / e** : a dans *captein*.
- **X = x / c / i** : non tranché (R05, R06, R12 irrésolus).
- **Y = r / y** : r dans *Newport* (si « · Y » n'est pas W, voir plus bas).

## Tableau des mots chiffrés

| n° | id | signes | brut (clé gelée) | lecture | statut | justification |
|---|---|---|---|---|---|---|
| 1 | R01 | I 7 Y I A | ieris/ieyit | ‹…› | irrésolu | nom de personne probable (sujet de « are imprisoned ») ; pas de mot |
| 2 | R01 | L I G {L\|h} Y 7 N | lig(l/h)ren | ‹…› | irrésolu | idem (nom ?) |
| 3 | R02 | v 8 B W v V O | acbward | ‹…ward› | irrésolu | fin « -ward » nette (W v V O = w a r d, v = a C) ; début a-c-b sans mot |
| 4 | R02 | I R N \| A R N | ion son | {Ionson} | probable | Johnson (I = J) ; tout dans la clé mais lu par-dessus un blanc et comme nom propre |
| 5 | R03 | G L c A | g-l/p-o/a/e-s/t | ‹…› | irrésolu | après « sent by yor· » (« your … ») ; « glos/gpas » sans mot |
| 6 | R04 | 7 n | e-? | [at] | restitué | « are imprisoned at Bridges » ; 7 = a (hors ensemble) et n = t (signe hors clé) |
| 7 | R04 | B V + O G 7 A | b r b d g e s | {Bridges} | probable | Bruges (« Bridges » élisabéthain) ; un seul signe hors ensemble (+ = i), forme proche de ⊥ = i (cf. n° 35) |
| 8 | R05 | 8 h c V X | c h o/a/e r x/c/i | ‹…› | irrésolu | « they have char… » ? (charged demanderait X = g et T = e) |
| 9 | R06 | T O A n P N L 7 X A | t d t ? p n l e x t | ‹…› | irrésolu | — |
| 10 | R06 | L + F A T N U N A | l b f t t n a n t | [leftenant] | restitué | « …-tenant of [Vereke] » ; + = e et T = e (deux signes changés) ; « leftenant » graphie du XVIe s. |
| 11 | R07 | L 7 A n · E B V A | l/p e s/t ? · e b r s/t | ‹…› | irrésolu | lieu après « of vereke (?) of » ? |
| 12 | R08 | R N Y | o n r/y | ‹…› | irrésolu | — |
| 13 | R08 | d N v 7 | o n a e | ‹…› | irrésolu | — |
| 14 | R08 | {+\|X} L c A n | b/x l o s/t ? | ‹…lost ?› | irrésolu | — |
| 15 | R09 | 7 A h R A | e t h o t | ‹…› | irrésolu | — |
| 16 | R09 | N 7 V | n e r | ‹…› | irrésolu | — |
| 17 | R09 | D + A Y u {+\|X} O E | d b s r u ? d e | ‹…› | irrésolu | « dis… » si + = i ; pas de mot |
| 18 | R10 | A h 7 V E | there | there | sûr | clé gelée (+ E = e, A) ; « that daye was there… » |
| 19 | R10 | A R | to | to | sûr | R = o (A) |
| 20 | R10 | 8 \| u A + O | c \| u s b d | ‹…› | irrésolu | « c[…] » puis « usid » (+ = i) ? ; « : · » après 8 peut être une ponctuation |
| 21 | R10 | 7 N | e n | {an} | probable | « an ancient of Newport » ; 7 = a (hors ensemble, 7 à tête ronde) |
| 22 | R10 | 7 N d I 7 N A | e n o i e n t | [ancient] | restitué | ancient = enseigne (porte-drapeau) ; 7 = a et d = c (deux changements) |
| 23 | R10 | R F | o f | of | sûr | clé |
| 24 | R10 | N E · Y L R V A | n e ? r p o r t | {Newport} | probable | Nieuport (crib de la liste) ; « · Y » relu comme W (point + trait oblique), correction de transcription en addendum ; L = p |
| 25 | R11 | F d V W · V T N G | f o r w ? r t n g | [forwarding] | restitué | f-o-r-w-·-r-t-n-g : point = a, T = d, i manquant (≥ 2 retouches) ; cf. R8490 « forwarde » |
| 26 | R11 | R F | o f | of | sûr | clé |
| 27 | R11 | u | u/v | ‹…› | irrésolu | deux points espacés, peut-être ponctuation |
| 28 | R11 | 7 V A I A n d | e r s i s ? o | ‹…› | irrésolu | « -sist- » net ; ni resisted ni assisted sans ≥ 2 changements |
| 29 | R11 | A h 7 7 | t h e e | ‹…› | irrésolu | « the » + 7 (ou « thee ») ; non tranché |
| 30 | R11 | L V 7 + n T | p r e b ? t | [preist] | restitué | « priest » (graphie preist) ; + = i et n = s (signe hors clé) |
| 31 | R12 | 8 c L A 7 I N | c a p t e i n | captein | sûr | c = a, L = p, A = t (ensembles) |
| 32 | R12 | B R X 8 E | b o x/c/i c e | ‹…› | irrésolu | nom du capitaine ? (« Boice » si X = i, non retenu) |
| 33 | R13 | I N L V I A d N E O | i n p r i s o n e d | inprisoned | sûr | L = p, A = s, d = o, E = e, O = d : ensembles ; répète le clair « imprisoned » |
| 34 | R13 | U n | a ? | {at} | probable | U = a (gelée) ; n = t (signe hors clé) ; « inprisoned at Bridgis » |
| 35 | R13 | B V I O G I A | b r i d g i s | Bridgis | sûr | tout dans la clé (B = b, O = d : A) ; = Bruges |
| 36 | R14 | d O A n N L I {+\|X} | o d s/t ? n l/p i ? | ‹…› | irrésolu | « of late there are too ‹…› from » |
| 37 | R15 | I V · E A h N R B P 7 | i r ? e t h n o b p e | ‹…› | irrésolu | lieu d'origine ? |
| 38 | R16 | Y T N | r t n | ‹…› | irrésolu | — |

Décompte : 38 mots chiffrés = 7 sûrs + 5 probables + 5 restitués + 21 irrésolus ; **(7 + 5) / 38 = 31,6 %**. Codes : aucun.

## Codes et signes hors alphabet
- Aucun nombre, aucun ◻, aucun ·x· dans le chiffre de R8495.
- Points isolés « · » (non valués) : R03 avant G (« sent by yor· ·G L c A are imprisoned » ; brut ‹g-l-o-s› ; NON compté comme signe) ; R07 « L 7 A n · E B V A » (« of vereke of ‹letn·ebrt› whereupon … ») ; R10 « N E · Y L R V A » (lu W, Newport) ; R11 « F d V W · V … » (« forw·rting ») ; R15 « I V · E A h … » (« from ‹ir·ethnobpe› Y T N 4 Italians »). Aucune valeur de code attribuée ; pour l'orchestrateur : aucun candidat à la mesure de codes (PREREG-B §Valeurs de codes) dans cette lettre.

## Texte continu (anglais, clair de notre relecture rapide, chiffre en *italique*)

> … that 300 mariners of Hamborough that were at Sluys are returned to Dunkergh: *‹…› ‹…›* and *‹…ward› {Ionson}* sent by yor *‹…›* are imprisoned *[at] {Bridges}*. It ys reported that they have *‹…› ‹…› [leftenant]* of Vereke (?) of *‹…›*, whereupon (?) he hath byn condemned and appointed (?) *‹…› ‹…› ‹…›*.
> – *‹…› ‹…› ‹…›* – that daye was *there to ‹c…› {an} [ancient] of {Newport}*, *[forwarding] of ‹…› ‹…› ‹the…› [preist] captein ‹…›* ys also *inprisoned {at} Bridgis* (the rest ?) ys not knowen.
> Of late there are too *‹…›* from *‹…› ‹…›*. 4 Italians that were …

## Résumé (FR)
Le 27 mai 1588, Lord Cobham écrit à Walsingham (dossier « Belgia »). Le clair rapporte que 300 marins de Hambourg qui étaient à L'Écluse sont revenus à Dunkerque. En chiffre, on lit seulement des bribes : deux hommes, dont un « … Johnson », envoyés par Walsingham, sont emprisonnés à Bruges ; un « lieutenant » de [Vereke] a été condamné ; ce jour-là un enseigne de Nieuport […] ; un prêtre (?) et un capitaine sont aussi emprisonnés à Bruges. Lecture très partielle : 32 % des mots chiffrés lus par le sens.

## Summary (EN)
On 27 May 1588 Lord Cobham writes to Walsingham ("Belgia"). The clear reports that 300 mariners of Hamburg who were at Sluys have returned to Dunkirk. The cipher yields only fragments: two men, one a "… Johnson", sent by Walsingham, are imprisoned at Bruges ("Bridges"); a "lieutenant" of [Vereke] was condemned; that day an ensign ("ancient") of Nieuport […]; a priest (?) and a captain are also imprisoned at Bruges ("Bridgis"). Very partial reading: 32 % of the cipher words read by sense — read in part.

## Fichiers
`R8495_chiffre.tsv` (+ .sha256), `R8495_arbitrage.md`, `PREREG-B.addendum-B1-R8495.md` (+ .sha256), `R8495_decodage_cle_gelee.txt`, `R8495_cle_derivee.tsv`, ce fichier.

---
## Écarts avec Daniel (ajouté le 2026-11-13 22:55 CET, APRÈS hachage de cette fiche : version hachée = LECTURE-R8495.v1-hachee.md, SHA256 85d7e7c3…fdca ; la lecture ci-dessus n'est pas modifiée)

Comparé à `targets/cobham1588/texts/R8495_reading.md` (Daniel, relu le 22/10).
- **Accords** : *ancient of Newport* (il lit « nL·\pcVA » n-e-w-p-o-r-t : confirme notre correction « · Y » = W, addendum B1-corr) ; *Captain* ; *Bruges* deux fois (lui [?Bruges] ; nous {Bridges} R04 et **Bridgis** R13, lu en entier, sûr) ; *forward* (lui [?forward] ; nous [forwarding]).
- **Nous en plus** : **inprisoned** en entier (lui « in [?prison] ») ; {at} Bridgis ; {Ionson} (Johnson) dans « … and ‹…ward› Ionson sent by yor … » ; [leftenant] ; [preist] avant *captein* (Daniel note ailleurs « priests ») ; *there to*, *of* (×2), {an}.
- **Lui en plus / divergences** : R05 « 8 h c V X » = [?charge] (X = g ; nous irrésolu, X = g hors ensemble) ; R07 = [?letters] chez lui (« l7AAALVA », l-e-t-t-t-e-r-s) — nous transcrivons « L 7 A n · E B V A » (n arrondi, point, E, B) et ne lisons pas : écart de transcription à revoir ; R15 [?Irish] (« IVILAϸ ») — nous « I V · E A h N R B P 7 », point + E au lieu de I L : écart de transcription.
- **Clair** (non décisif pour le %) : il lit « 4 sent by […] are […] » et « sent by […] imprisoned in [?Bruges] » ; nous voyons « yor· » (pas « 4 ») et, la ligne montant, l'ordre « … and … sent by yor· ·GLcA are imprisoned [at] Bridges » ; « of words of » (nous « of vereke ? of ») ; « determined and appointed » (nous « condemned and appointed ») ; « the cause whereof ys not knowen » (nous « the residue ? ») ; « Of late ther are come to » (nous « there are too »). Son run 92a « pcc:GlcA » (Portugals ?) = notre R03 « ·G L c A » précédé de signes que nous lisons comme le clair « yor· ».
- Bilan : aucun mot de Daniel ne contredit une lecture « sûre » de notre fiche ; ses trois lectures en plus (charge, letters, Irish) reposent sur des transcriptions différentes des nôtres à ces endroits.
