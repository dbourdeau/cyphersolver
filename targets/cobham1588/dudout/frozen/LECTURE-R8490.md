# LECTURE — DECODE R8490 (BL Harley MS 287 ff. 80r-80v) — Cobham à Walsingham, Ostende, 5 mai 1588

2026-11-09, agent Opus, fil Déchiffrement. **Au compte de Daniel Bourdeau** (`targets/cobham1588`, catalogue n° 131) : contribution à son dossier, pas une lecture nouvelle à notre nom. 🔴 Aucune image ni découpe DECODE publiée ; citer « DECODE R8490 » (https://de-crypt.org/decrypt-web/RecordsView/8490).

## Statut (exact)

**Lu en partie : 35 mots chiffrés sur 43 lus par le sens = 81 %** (règle de Daniel : 95 % des mots lus par le sens). Avec les 6 codes de noms (tous glosés d'époque) : 41/49 = 84 %. **Seuil de 95 % NON atteint → pas de publication, pas de « read ».** Détail : 21 sûrs, 14 probables, 0 restitué, 8 irrésolus.

Le chiffre a été transcrit en entier (18 passages, 43 mots + 6 codes) ; le clair n'a **pas** été relu en entier par nous (voir « Clair » plus bas) : aucun pourcentage n'est donné pour la lettre entière.

## Méthode

1. **Transcription** de tout le chiffre de f. 80r et f. 80v sur découpes à 1:1 (scratchpad, jamais publiées) → `R8490_chiffre.tsv`, **hachée avant tout décodage** : SHA256 `01a80a432bc0423aac52825ec7d984d56c2fa1b2b7c541f4e122872e33d6a785`. P3 (f. 81r) est blanc ; P4 (f. 81v) porte l'adresse (« To the right honorable Sir Francis Walsingham, knight, principall Secretary to her Majesty and chancellor of the Duchy of Lancaster »), la mention de dos « Ostend 5 May 1588 from L. Cobham to Sir Francis Walsingham » et des notes au crayon sans rapport avec le chiffre (« Shippes … Groningen … No commission … Dunkirk … K. Sp. … »). Pas de chiffre ailleurs.
2. **Décodage brut avec la clé gelée** `cle_R8489_f78r.tsv` (SHA 2b3216e6…0566), sans retouche, valeur principale, signe inconnu = « ? » → `R8490_decodage_cle_gelee.txt`. Il donne déjà sans aide : *the*, *not*, *it*, *ther*, *retorn*, *to*, et presque *hostages*, *subiect*, *forwarde*, *openning*.
3. **Valeurs nouvelles** : uniquement dans la clé dérivée déclarée `cle_R8490_derivee.tsv` (SHA 8557ecf0…e37c), chaque valeur avec ses attestations ligne par ligne et une force A/B/C. La clé gelée n'est pas touchée.
4. **Codes** : 22 = Sir James Croft ; 27 = Dr Valentine Dale ; 26 = Dr John Rogers (absent ici) ; 15 = le duc de Parme ; 7 = la Reine ; ◻ = les États (gloses d'époque de R8489 f. 78r et de f. 79 ; 7 glosé chez Daniel).
5. **Classement** : *sûr* = chaque signe a une valeur de la clé gelée ou une valeur dérivée de force A, et le mot fait sens ; *probable* {x} = un signe de force B/C, non expliqué ou manquant, sens net ; *restitué* [x] = mot fourni par le sens (aucun ici) ; *irrésolu* ‹…› = pas de mot qui fasse sens.

## Signes polyvalents : choix au cas par cas

**Λ (A) = s ou t** (clé gelée : ensemble s,t). Chaque occurrence, tranchée par le mot :
- t : C02 *the* ; C03 *not*, *kept*, *the* ; C04 *hostages* (4e signe) ; C05 *to* (×2), *ther*, *surti* (4e), *these* (1er), *termes* (1er) ; C06 *treats* (1er) ; C07 *treat* (1er) ; C08 *subiect* (dernier) ; C10 *action* ; C11 *to* ; C12 *the* ; C14 *brother* ; C17 *to*, *retorn* ; C18 *restrain* (4e). Justification : seule la lecture t donne un mot anglais (the, not, to, ther, these…) ; *ther* = « their » dans la graphie de Cobham (clair : « ther preparation », « ther Mr »).
- s : C03 *is* ; C04 *hostages* (3e et dernier) ; C05 *surti* (1er), *these* (dernier), *termes* (dernier) ; C06 *treats* (dernier) ; C08 *subiect* (1er) ; C11 *send*, *Bruges* (dernier) ; C12 ‹bookes› (dernier) ; C17 *desire* ; C18 *restrain* (3e). Justification : pluriels en -s et mots en s- (send, subiect, surety) ; « tend/tubiect/turti » ne sont pas des mots.
- a (valeur dérivée C, caret large) : C06 *treats* (4e). Justification : « tretts » n'est pas un mot ; Daniel note le caret large = a.
- Non tranché : C02 ‹L U N 8 7 A›, C13 ‹A d N›, C15 ‹V Q I N A L c V A› (mots irrésolus).

**γ (Y) = r ou y** : C05 *ther* → r (« they surety » ne fait pas phrase ; « ther » est la graphie de Cobham pour *their*) ; C05 ‹D 7 Y N O E› → non tranché (ni « dernde » ni « deynde » n'est un mot).

**d = o** (valeur dérivée A ; f. 78r n'a pas ce signe) : C07 *of*, C11 *to*, C12 *openning* et *of*, C13 *of*, C14 *brother*. Justification : *to*, *of*, *open-* exigent o ; aucune occurrence de d ne demande la lettre d. La lettre d s'écrit ici ∞ ou un petit o fermé (O : *forwarde*, *send*, *Breda*), signe distinct de d et de c à 1:1.

## Tableau des mots chiffrés

| id | folio, ligne | signes | lecture | classe | justification |
|---|---|---|---|---|---|
| C01 | 80r l. 9 | c V N 8 S | ‹…› | irrésolu | « ornc? » ; aucun mot ; S (ʃ barré) inconnu, peut-être lettre du clair ; Daniel : non lu |
| C02a | 80r l. 10 | X # | {in} | probable | X = i et # = n (Daniel, valeurs C) ; sens « hoping theym in the… » |
| C02b | | A h 7 | the | sûr | clé gelée |
| C02c | | ◻ | [the States] | code | glose de f. 78r (« ye States », deux fois) |
| C02d | | L U N 8 7 A | ‹…ances› | irrésolu | « lances/pances » ; « [ex]pances » de Daniel suppose ◻ = ex-, contraire à la glose de f. 78r |
| C03a | 80r l. 12 | N c A | not | sûr | clé gelée |
| C03b | | B 7 | be | sûr | B = b (A, 5 attestations) |
| C03c | | w E L A | {kept} | probable | ω = k (gelée), E = e (A), ϕ = p (C, une attestation ici ; Daniel a ϕ = p ailleurs) ; « it will not be kept » |
| C03d | | A h 7 | the | sûr | clé gelée |
| C03e | | h c u 7 N | haven | sûr | c = a (A : 2 × haven, action) ; u = v |
| C03f | | I A | is | sûr | clé gelée |
| C03g | | X d + c u 8 7 | ‹…› | irrésolu | « ?obouce/?obauce » ; pas de mot |
| C04 | 80r l. 18 | h c A A U G E A | hostages | sûr | tout dans la clé gelée sauf E = e (A) ; « Touching hostages » |
| C05a | 80r l. 19 | 7 | [the Queen] | code | glose de f. 79 (Daniel) |
| C05b | | A R | to | sûr | R = o (A) |
| C05c | | D 7 Y N O E | ‹…› | irrésolu | d-e-r/y-n-d-e ; aucun mot |
| C05d | | A h 7 Y | ther | sûr | clé gelée ; = their |
| C05e | | A u V A I | surti | sûr | clé gelée ; = surety |
| C05f | | A R | to | sûr | R = o (A) |
| C05g | | A h 7 A | these | sûr | clé gelée |
| C05h | | A c V M 7 A | {termes} | probable | c = e (C, une attestation) ; « tormes » sans sens |
| C06 | 80r l. 20 | A V 7 A T A | {treats} | probable | A = a (C), T = t (B) ; = treaties |
| C07a | 80r l. 21 | A V 7 A T | {treat} | probable | idem |
| C07b | | d F | of | sûr | d = o (A) |
| C07c | | B V 7 O Q | {Breda} | probable | O = d (A), Q = a (B) ; lettre à lettre b-r-e-d-a (Daniel lisait b-r-e-d-d) |
| C08 | 80r l. 21 | A u B I 7 8 A | subiect | sûr | clé gelée + B = b ; singulier (Daniel : subiects) |
| C09 | 80r l. 31 | F c V W v V O 7 | {forwarde} | probable | v = a (C) ; O = d (A) |
| C10 | 80r l. 31 | c X A I R N | {action} | probable | X = c (C) ; c = a, R = o (A) |
| C11a | 80r l. 32 | A 7 N O | send | sûr | O = d (A) |
| C11b | | A d | to | sûr | d = o (A) |
| C11c | | B V u G E A | {Bruges} | probable | b-r-u-g-e-s ; seul doute : dernier signe, caret à boucle d'attaque ; **neuf** (Daniel : « b-u-i-e-s unread ») |
| C11d | | 27 | [Dr Dale] | code | glose f. 78r |
| C12a | 80r l. 32-33 | d P 7 N – N I N G | openning | sûr | d = o (A), le reste gelé ; coupé en fin de ligne |
| C12b | | d F | of | sûr | |
| C12c | | A h 7 | the | sûr | |
| C12d | | B R c w 7 A | ‹bookes› | irrésolu | signes b-o-o-k-e-s, mais « the openning of the bookes » ne fait pas un sens établi |
| C13a | 80r l. 33 | A d N | ‹…› | irrésolu | « ton/son » ; pas de sens |
| C13b | | d F | of | sûr | |
| C13c | | X c V I w 7 | ‹…› | irrésolu | « ?orike » ; nom de lieu ? non identifié |
| C14 | 80r l. 34 | B V d A 7 V | {brother} | probable | b-r-o-t-e-r, h non écrit |
| C14b | | 15 | [the Duke of Parma] | code | glose f. 78r |
| C15 | 80r l. 34 | V Q I N A L c V A | ‹…› | irrésolu | « rain-s-port » ; peut-être nom de lieu en -port ; non identifié |
| C16 | 80r l. 35 | h c u 7 N | {haven} | probable | 2e signe petit, lu c = a |
| C17a | 80v l. 1 | 22 | [Sir James Croft] | code | glose f. 78r |
| C17b | | v 7 A I v V | {desire} | probable | 1er et 5e signes (ʋ) non expliqués ; e-s-i-…-r sûrs ; « 22 hath a desire to retorne » |
| C17c | | A c | to | sûr | clé gelée |
| C17d | | V 7 A c V N | retorn | sûr | clé gelée (f. 78r : *retorne*) |
| C18 | 80v l. 2 | V j A A V Q I N B 8 | {restrain[ed]} | probable | r-e-s-t-r-a-i-n ; j = e (C), Q = a (B) ; finale « B 8 » non expliquée |

Décompte : 43 mots chiffrés (hors codes) = 21 sûrs + 14 probables + 8 irrésolus ; **35/43 = 81,4 %**. Codes : 6/6 (glosés). Total 41/49 = 83,7 %.

## Lecture (anglais du XVIe siècle)

Clair : transcription de Daniel du 22/10 (`texts/R8490_reading.md`), **non relue en entier par nous** ; vérifiée seulement aux lignes qui portent du chiffre (l. 9-12, 18-21, 31-35 ; f. 80v l. 1-2), d'où deux retouches : « the subiect » (singulier, chiffre) et l. 20 « in[somuch] » au lieu de « in [?numbers] » (lecture du clair incertaine). Chiffre en *italique* ; {x} probable ; ‹…› irrésolu ; [x] code ou mot fourni.

> Sir, I dowt not but that yow know what [?Pyne] hath to delyver from me to hys master, for he promised me to doo the same to yow. Ther ys not ony nation (and yf ther be mony) that [?sayeth] so of the D[uke]; but severally, and [?together], spoke that ther [?inbasied] unto Englande, saying that they wylle ether doo yt at the [?barkeday] or at the [?forder]. Therfor my poor opinion ys to strengthen our havens at home, boothe by lande and see, and to drawe our forces from *‹…›*, hoping theym *{in} the [States'] ‹…ances›*, for what chaunces so ever yow bestowe (and that muste be great) yt will *not be {kept}, the haven is ‹…›*; and moreover the wynde hath blown here these three wekes out [of the] north east, and ther hath not come owt of Holland and Zelande above three boottes, and yf the wynde [had been] good to doo hether. By that yow may see what help ther ys nor hope to be had from those parties.
>
> Touching *hostages*, yt ys honorable for *[the Queen] to ‹…› ther surti to these {termes}*, as usuall yn all *{treats}* in[?somuch] that at the *{treat} of {Breda}*, which was the 20, and the *subiect* ther were delivered Julio Romeo, Cristophero Mondragon, Mor Daussy, as they have bene done by a [?sovereign] prince to hys subiect: much rather to his [?royall] for the surety of her subiect and saufgarde.
>
> Mr Controller was sycke [?yesterday] … Doctor Dayll yowr [?] [?moved] to [?] […]. *(paragraphe tout en clair, transcription de Daniel inchangée)*
>
> I am informed that ther preparation doth dayly encrease; they chose the place of rendevous ys at Dunkergh. *[22: Sir James Croft]* is so *{forwarde}* yn the *{action}* that he promised Q[ueen] to *send to {Bruges} [27: Dr Dale]* to begyn the *openning of the ‹bookes?›*, which myght bee to the *‹…› of ‹…›*, that a *{brother}* about *[15: the Duke of Parma]*, who promised the mayor *‹…›* a *{haven}* to open.
>
> *[22: Sir James Croft] hath a {desire} to retorne* from theym, yf he be not more *{restrain[ed]}*. Ther ys great want of us to cumfort our […] and kepe them [?here], hoping that by yowr good meanes that we shall [be] [?relived] here. I commyt yow to the allmyghtye. From Ostende the 5 of May a 1588.
>
> Yowr very loving frend, W. Cobham

## Ce qui est neuf par rapport à la lecture de Daniel

- **22 = Sir James Croft, 27 = Dr Dale** (gloses de f. 78r) appliqués : « Croft is so forward in the action that he promised the Queen to **send to Bruges Dr Dale** to begin the opening of the … » et « Croft hath a desire to return from them, if he be not more restrained ». Cohérent avec l'histoire (Dale envoyé auprès de Parme en 1588 ; Croft négociant seul avec Parme), qui ne sert ici que de contrôle de sens, pas de preuve.
- **Bruges** (Daniel : b-u-i-e-s non lu), **kept** (« yt will not be kept », Daniel : non lu), **Breda** lu lettre à lettre (b-r-e-d-a, petit o fermé = d, ɔ = a), **subiect** au singulier, **termes** (c = e).
- Distinction de signes qu'il confond : O (petit o fermé = d) ≠ ∞ ; R (ꞇ = o) ≠ ŧ (= t) ; d (= o) partout.
- Restent irrésolus : l. 9 (lieu d'où retirer les forces), l. 10 « …ances », l. 12 état du port, l. 19 le verbe (« to ‹…› their surety »), l. 33 (deux mots, sans doute un lieu), l. 34 (le maire de ‹…›, peut-être un lieu en -port).

## Résumé (FR)

Le 5 mai 1588, depuis Ostende, Lord Cobham, l'un des commissaires anglais envoyés négocier avec le duc de Parme, écrit à Walsingham. En clair : les préparatifs ennemis grossissent, Dunkerque est le lieu de rassemblement, il faut fortifier les havres d'Angleterre et retirer nos forces ; le vent du nord-est bloque les secours de Hollande et de Zélande. En chiffre : la place « ne sera pas tenue », son havre est […] ; sur les otages, il est honorable pour la Reine de […] leur sûreté à ces conditions, comme dans tous les traités, ainsi au traité de Breda ; **Sir James Croft** (22) pousse tant l'affaire qu'il a promis à la Reine **d'envoyer à Bruges le Dr Dale** (27) pour ouvrir […] ; un « frère » proche de Parme (15) a promis au maire de […] un havre à ouvrir ; **Croft veut revenir** de chez eux s'il n'est pas retenu davantage. Lecture partielle : 81 % des mots chiffrés lus par le sens, sous le seuil de 95 %.

## Summary (EN)

On 5 May 1588, from Ostend, Lord Cobham, one of the English commissioners sent to treat with the Duke of Parma, writes to Walsingham. In clear: the enemy's preparations grow daily, Dunkirk is the rendezvous, England's havens should be strengthened and our forces withdrawn; the north-east wind keeps help from Holland and Zeeland away. In cipher: the place "will not be kept", its haven is […]; touching hostages, it is honourable for the Queen to […] their surety on these terms, as in all treaties, as at the treaty of Breda; **Sir James Croft** (22) is so forward in the action that he promised the Queen to **send Dr Dale (27) to Bruges** to begin the opening of the […]; a "brother" close to Parma (15) promised the mayor of […] a haven to open; **Croft wishes to return** from them unless he is further restrained. Partial reading: 81 % of the cipher words read by sense, below Daniel's 95 % rule.

## Fichiers

`R8490_chiffre.tsv` (+ `.sha256`, haché avant décodage) ; `R8490_decodage_cle_gelee.txt` (décodage brut) ; `cle_R8490_derivee.tsv` (valeurs nouvelles + attestations) ; ce fichier.
