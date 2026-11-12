# Préenregistrement — planche W1 (relecture aveugle ciblée des CHIFFRES), lettre du camp devant Stralsund, 20/10/1715
Loc. 00712/05, scans 0380–0387 (ff. 307–314). Rédigé et haché le 2026-11-11 (nuit) par l'agent Opus 5.5 (fil 🔓), AVANT la
construction de la planche (aucun make_planche.py, aucune vignette, aucun HTML). Fichier PRIVÉ (contient des lectures) :
ne pas le montrer à Brice avant l'export de ses réponses. 🔴 Scans SächsHStA InC : usage local seulement, jamais publiés.
🔴 Découverte simultanée possible : A.-S. Rous (Tartu) — à nommer dans toute rédaction.

## Consigne
Demande de Brice (via l'agent principal, 11/11) : UNE planche aveugle ciblée (≤ 12 questions, formes de chiffres seulement,
aucune glose visible) sur les lectures fragiles qui changent la classe d'un mot : confusions 51/57, 25/28, 16/66 et « ch » = 72 ;
2 contrôles sûrs sur des pages différentes et à des places d'options différentes ; noyau v2 ; export `reponses-wackerbarth-W1.json`.
Une planche de FORMES tranche la LECTURE D'UN CHIFFRE, jamais une valeur de clé. KEY-1715.tsv (sha256 69bda731…268eb),
PREREG-1715.md, les relevés CIBLE-*/TRAIN-* et LECTURE-1715.md restent GELÉS : aucune réponse ne les modifie.

## Ce qui a été vu avant ce texte (déclaré)
- La lecture (LECTURE-1715.md, lecture/LECTURE-1715-10-20.txt, decodage-mecanique.txt) et les relevés gelés : je connais donc
  les lectures attendues. C'est pourquoi la réponse de référence de chaque cible est la lecture du relevé gelé (pas la mienne).
- Les scans 0380–0387 (et 0378–0379, 0388) en local, avec grilles de coordonnées, pour placer les cadres. En les regardant,
  j'ai une impression sur certaines cibles (notée ici pour être honnête, sans effet sur la règle) : 0386-d L03, le groupe lu
  « 96 » avant « 70/90 » ressemble à « 46 » (4 à hampe) ; non retenu (voir « Écartés »).

## Pas de double relevé : comment « désaccord » est traité
Les deux sous-agents ont relevé des pages DIFFÉRENTES (A : 0380–0383 ; B : 0384–0387, hachages CIBLE-A/B.sha256). Aucune page
n'a été relevée deux fois : il n'y a donc pas de désaccord A/B au sens strict. Retenu à la place : (1) les doutes notés par le
relecteur lui-même (`N/M?`) quand la lecture change le mot ; (2) les groupes nets mais dont le décodage donne un mot faux, corrigé
par le contexte (la confusion est alors celle du scribe ou du relecteur, la planche dit laquelle) ; (3) les deux mains de relecture
sont couvertes pour 25/28 (A : E ; B : A, C, D) et pour 72 (A : G ; B : B).

## Choix des signes
Question retenue seulement si la classe (sûr / probable / restitué, conventions de LECTURE-1715) d'au moins un mot dépend de la
réponse. Une question = un chiffre encadré ; options = formes de chiffres découpées dans des mots SÛRS de la même main de copiste,
de préférence sur la même page ou la page voisine, à hauteur de trait cohérente dans chaque forme.

| # | lieu (scan, page, ligne) | groupe relevé | chiffre encadré | options (formes) | mot (classe actuelle) | effet selon la réponse |
|---|---|---|---|---|---|---|
| A | 0387 g L12 (« Voilà, … ») | 25/28? | 2ᵉ | 5 / 8 | « ma » (s) | 5 → s inchangé ; 8 → 13·28 = « mt » → **r** [ma] |
| B | 0387 g L12 | 72 | 1er | 7 / 4 | « chère » (p : 72 = ch pris à S1/1717) | 7 → p inchangé ; 4 → 42 = l, « lere » → **r** [chère] |
| C | 0384 g L11 | 28/25? | 2ᵉ | 8 / 5 | « embrasser » (p) | 5 → e·m·b·r·a·s·s·e·r, toutes valeurs K1715 → **s** ; 8 → « embrtsser » → **r** |
| D | 0385 g L22 | 13.28.12 | 2ᵉ chiffre de 28 | 8 / 5 | « mal » (r : « mtl ») | 5 → 13·25·12 = mal → **s** ; 8 → r inchangé |
| E | 0383 g L04 | 28 (1er groupe) | 2ᵉ | 8 / 5 | « paix » (p : « ptix » corrigé) | 5 → p·a·i·x → **s** ; 8 → p inchangé |
| F | 0383 d L14 | 16/26? | 1er (surchargé) | 1 / 2 / 6 | « beaucoup » (p : « beoucoup ») | 6 → 66 = a → **s** ; 1 ou 2 → p inchangé |
| G | 0381 d L09 | 72 | 1er | 7 / 4 | « duché » (p) | 7 → p inchangé ; 4 → 42 = l, « dulé » → **r** |
| H | 0386 d L03 | 70/90? | 1er | 7 / 9 | « paix » (p : 70 = x déduit) | 7 → p inchangé ; 9 → 90 = ch → **r** |
| I | 0380 d L07 | 31/71? | 1er | 3 / 7 | « même » (s) | 3 → s inchangé ; 7 → 71 = i, « meie » → **r** |

Référence (forme dite « attendue » pour l'équilibrage du noyau, PAS une réponse attendue) = lecture du relevé gelé, première
lecture : A 5 ; B 7 ; C 8 ; D 8 ; E 8 ; F 1 ; G 7 ; H 7 ; I 3.

**Contrôles** (signes nets, mots sûrs, deux pages et deux mains de relecture différentes ; le noyau v2 les met à des places
différentes) :
- K1 = 0382 d L10, groupe 25 de « paix » (« le roi est fort disposé à la paix », sûr), 2ᵉ chiffre ; options 5 / 8 (confusion
  25/28) ; attendu 5.
- K2 = 0385 d L14, groupe 97 (« rendre la place », « la » sûr), 2ᵉ chiffre ; options 7 / 4 (confusion de 72) ; attendu 7.
Total : 9 questions + 2 contrôles = 11 (≤ 12).

## 51/57 : aucune question (déclaré)
Les 12 occurrences notées `51/57?` ou `57/51?` (0381 d L04 ; 0382 g L25 ; 0384 g L07, L11, L21 ; 0386 g L03, L05, L06, L07, L08 ;
0387 g L13 ; plus 0381 g L04 « 57 (51 non exclu) ») se lisent **s** dans les deux cas (K1715 : 51 = s, 57 = s) : aucun mot ne
change de classe → aucune question, conformément à la règle. La confusion graphique 1/7 de cette main (« 5 + trait court à
crochet ») est en revanche testée là où elle change un mot : 72 contre 12 n'étant pas plausible à l'œil, on teste 7 contre 4
(confusion « ч » = 7 déjà relevée en 1717) en B et G, et 7 contre 3 en I.

## « ch » = 72 : ce que la planche peut dire
La valeur ch de 72 vient de S1/1717 (KEY-W1717d : 5 contextes) ; elle n'est pas dans K1715 (seul 90 = ch, 1 occurrence). Dans la
lettre, 72 se lit ch dans 9 contextes cohérents (duché, chacun, retranchement, tâcher, fâcheuses, boucher, choses, échangée, chère).
La planche ne peut pas établir une VALEUR ; elle vérifie seulement que le groupe est bien écrit 72 (B, G). Une valeur reste une
question de clé.

## Écartés
- 0386 d L03, groupe lu 96 avant 70/90 : je crois y voir 46 (= i, ce qui donnerait « pa·i·x ») ; mais « paix » resterait probable
  (70 = x déduit) → 0 mot → non retenu ; noté pour une revue de clé de 96 (19 occurrences, valeur « le » déduite).
- 0385 g L20 28/25? (Stralsund) : le mot reste probable dans les deux cas (85 = st déduit).
- 0385 d L03 25/28? et 24/29? (« dans ») : deux doutes dans le même mot → la réponse ne suffit pas à fixer la classe.
- 0387 d L05 25/28? (« occupations », p : 34 = P vient de 1717) : 8 ferait passer le mot en r ; gardé en réserve, non posé
  pour rester ≤ 12 et parce que D et E testent déjà la même confusion dans la même main.
- 0384 g L08/L22 58/54? : ni l'une ni l'autre lecture ne donne le mot (« donc ») → clé.
- Groupes à 4 chiffres de 0383 g L20 (4008, 10009, 680) : pas de forme de référence ; irrésolus.

## Forme de la planche
Noyau v2 OBLIGATOIRE : copie inchangée de PLANCHES/_outils/planche_core.py, SHA-256 vérifié contre SHA256SUMS
(0c605bc9…5e80) ; place de la référence équilibrée ; contrôles à des places différentes ; refus d'une planche déséquilibrée ;
hauteur de trait renseignée pour chaque exemple (4 et 9 à hampe = « bas » ; 6 à boucle haute = « haut » ; autres = « moyen »).
Bande de ligne large (voisins et points de séparation visibles), signe agrandi, cadre rouge englobant tout le tracé.
Aucune valeur, glose, lettre ni numéro de scan visible ; correspondance seulement dans cle-PRIVEE.json (jamais chargé par la
page). Graines : ordre 1715201, options 1715202. Vérification de crops/_contact.jpg à l'œil ; test jsdom ; la planche n'est pas
ouverte dans un navigateur par l'agent. Fichiers : lettre-1715-10-20/planche-W1/ (local, privé).

## Règle d'intégration (une seule fois, mécaniquement, à l'export de Brice)
0. Contrôles : si K1 ou K2 reçoit une autre forme que la sienne (ou « aucune / illisible / pas un signe »), la planche n'est PAS
   intégrée ; l'échec est consigné dans ../HANDOFF.md.
1. Forme choisie → on lit le groupe avec ce chiffre, on applique K1715 GELÉE (complétée comme dans LECTURE-1715 par S1/1717) et
   les conventions de LECTURE-1715 : résultat = colonne « effet » ci-dessus. La clé n'est JAMAIS modifiée.
2. « aucune / autre », « illisible », « pas un signe » ou pas de réponse → un mot « s » qui dépendait de la question devient « p »
   (A, I) ; un « p » reste « p » ; un « r » reste « r ».
3. Remarques de Brice : notées telles quelles ; elles ne changent aucune classe mécaniquement. Une remarque qui propose un autre
   chiffre est notée comme piste, sans être appliquée.
4. Les autres occurrences des mêmes groupes ne sont PAS modifiées mécaniquement.
5. Le décompte (771 / 120 / 13 / 18 sur 922 → 96,6 %) est recalculé après intégration et noté tel quel dans ../HANDOFF.md, même
   en baisse (A, B, C, G, H, I peuvent faire passer un mot en restitué). Toute correction = nouveau fichier versionné
   (LECTURE-1715-v2…), jamais d'écrasement des fichiers gelés.
6. **Pas de seconde planche sur les mêmes signes** (les 9 chiffres ci-dessus et les 2 contrôles), quel que soit le résultat, ni
   pour « rattraper » une réponse.
7. La mesure de PREREG-1715 (S = 0,945 sur 0384 g) n'est pas recalculée : la question C porte sur la portion de contrôle, mais la
   planche ne touche que la lecture, pas la mesure.
