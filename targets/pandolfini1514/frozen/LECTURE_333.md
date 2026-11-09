# Lecture — MAP LXXII 333 (c. 417r, pos. 837), lettre nue à Lorenzo de' Medici, Paris 27 déc. 1514 — 09/11/2026 ≈ 03:30 CET

## Statut
- Pièce : Pandolfini à Lorenzo (« Mag.ce vir et compater hon.de »), « Parisijs die xxvij decembris M.D.xiiij » ; 838 = 417v (sans texte),
  839 = c. 427 (blanc), 840 = adresse « Mag.co viro Laurentio de Medicis … Rome » + n° 333. UN bloc chiffré de 3 lignes.
- Clé : CLE_v3 (ae5f0b9f…, gelée, non modifiée) = P03bis PARTIEL ; CLE_v4 (1848f692…, non modifiée) ; valeurs nouvelles dans
  cle/CLE_v5b.json (9d5cf3d5…, dérivée déclarée, non mesurée, attestations dans _attestations).
- Transcription : transcription/N333_c417r.txt (a6118019… ; 1er haché 539bbe63… gelé à 03:28 CET AVANT le décodage machine v4,
  seule l'heure du commentaire d'en-tête corrigée ensuite ; N333.sha256). Avertissement : formes douteuses identifiées en lisant.
- Conventions de Daniel : sûr = nu ; {probable} ; [restitué] ; ‹irrésolu› (jetons).

## EXISTING / antériorité
1. Desjardins-Canestrini t. II : lacune 16/08/1514 – 25/05/1515 ; 27/12/1514 → non imprimée.
2. Clair d'époque : le chiffre de 333 n'a pas de déchiffrement propre, MAIS la même nouvelle est donnée en clair, avec des mots
   communs, dans **332** (c. 416, pos. 833-836 : « Copia d[ella lettera] dello imbasciadore di Franza Franc.o Pandolfini a' S. Otto
   di pratica de dì xxvij decembre 1514 », copie claire de la lettre aux Otto, la « allegata copia » dont parle 333) : « … dalle bande di
   qua … questa M.tà con desiderio et non senza grandissima suspitione aspectando la resolutione di Roma … ». La formulation diffère
   (ce n'est pas un déchiffrement de 333), mais **le contenu n'est pas nouveau** : 333 résume pour Lorenzo ce que 334/332 dit aux Otto.
3. Daniel (gh api, 09/11 ≈ 03:25) : 2389 toujours « open », aucune PR/issue/commit sur Pandolfini (derniers commits « Site: rebuild »,
   pigeongrammes1870) ; son vetting du 06/11 ne rattachait 333 à aucun clair (il ne cite pas 332 pour 333).
→ Lecture neuve du chiffre, contenu connu par 332 (à dire tel quel).

## Décodé brut, clé v4 (sans retouche)
    L1 da gg e ba n de a qua a l p re se n te si pu o di re po co
    L2 di mo me n to de pe n de n do i l tu c to da gg e re so lu ti o ni che si fa ra nn o co s ti
    L3 de gg e qua li qua si s ta con g ra n di s si ma su s pi ti o ne

## Décodé brut, clé v5b dérivée (sans retouche)
    L1 da ll e ba n de a qua a l p re se n te si pu o di re po co
    L2 di mo me n to de pe n de n do i l tu t to da ll e re so lu ti o ni che si fa ra nn o co s ti
    L3 de ll e qua li qua si s ta con g ra n di s si ma su s pi ti o ne

## Lecture par le sens
[clair : … la allegata copia qual scrivo ad Firenze alli S. Otto.] Dalle bande {di} qua al presente si può dire poco di momento,
dependendo il tutto dalle resolutioni che si faranno costì, delle quali qua si sta con grandissima suspitione. [clair : Altro per la
presente non mi occorre …]

## Justifications
- dalle / delle (×3) : 4# Q = « lle » (v5b 4# = ll ; v4 avait gg par simple analogie). « dalle bande di qua » est aussi la formule
  du clair 332 de même date, et le même groupe « 3^5 4# Q 2^5 y 3 3 S » figure en 322 L8 : sûr.
- bande : 2^5 = ba dans ce seul mot (ailleurs 2^5 = ca, cf. CLE_v5b) ; appuyé par 332 : sûr.
- {di} : exposant du « 3 » caché par une hampe de la ligne claire au-dessus ; d + qua → « di qua » par le sens : probable.
- poco : 6^2 2^2 (po-co) ; tutto : 8^1 0 8^2 avec 0 devant 8 = t (doublement, v5b, cf. 322 « detto ») : sûr.
- grandissima : G 7^5 y 3^3 6 r^3 5^5 ; suspitione : r^1 6 6^3 8^3 O t^4 ; « grandissima suspitione » est aussi dans 332 : sûr.
- Taux : 29 mots : 28 sûrs, 1 probable, 0 restitué, 0 irrésolu → lu 100 % (≥ 95 %).

## Résumé (FR)
Pandolfini à Lorenzo de' Medici, Paris, 27 décembre 1514 : il n'écrit que pour joindre la copie de sa lettre aux Otto. En chiffre :
de ce côté-ci (la cour de France), il n'y a pour l'instant rien d'important à dire ; tout dépend des décisions qui seront prises
« là-bas » (à Rome), et l'on attend ces décisions ici avec une très grande méfiance.

## Summary (EN)
Pandolfini to Lorenzo de' Medici, Paris, 27 December 1514: he writes only to send the copy of his letter to the Otto. In cipher: on
this side (the French court) there is little of weight to report for now; everything hangs on the decisions to be taken "there" (in
Rome), which are awaited here with very great suspicion.

## Publiable ?
OUI comme lecture complète (100 %, 29 mots) d'un passage court, clé PARTIELLE (P03bis) + v5b dérivée déclarée, sans aucune image ASF,
en disant que le contenu est déjà donné en clair par 332 (copie aux Otto du même jour) : lecture neuve du chiffre, pas nouvelle
historique.

## Relecture v6 (09/11/2026 ≈ 04:15 CET, agent arbitrage) — ce qui change
- Clé : cle/CLE_v6.json (a2f1c942…, fusion déclarée v5a + v5b + ARBITRAGE-v6.md). Transcription inchangée (a6118019…). Décodé brut v6 :
  lecture/_decode_v6_N333.txt :
    L1 da ll e ba n de a qua a l p re se n te si pu o di re po co
    L2 di mo me n to de pe n de n do i l tu c to da ll e re so lu ti o ni che si fa ra nn o co s ti
    L3 de ll e qua li qua si s ta con g ra n di s si ma su s pi ti o ne
- Seule différence avec v5b : « tu t to » → « tu c to » (0 = c ; graphie « tucto » = tutto, ARBITRAGE § 4). 4# = ll CONFIRMÉ par
  l'arbitrage (332 ↔ 333). Lecture inchangée : « … dependendo il tutto (tucto) dalle resolutioni … ».
- Taux : 29 mots, 28 sûrs, 1 probable → 100 % (inchangé). Contenu déjà donné en clair par 332 (inchangé).
