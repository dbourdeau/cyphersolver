# Pré-enregistrement — relecture IA lieu par lieu des figures « g » de R4936 (transylvania1645), 24/11/2026

Partie A, écrite et hachée AVANT de regarder un seul lieu non vu (seuls vus à ce stade : les 4 exemples d'alphabet de la planche,
L02 s8, L03 s4 « boucle longue », L05 s7, L06 s12 « crochet court », recadrés à 400 % dans le scratchpad).
Lecteur : agent IA (Claude), sur délégation de Brice, qui ne relit pas un par un. Cible de Daniel Bourdeau : rien n'est écrit
chez lui ; copie locale planche-2411/integration-ai/. 🔴 Images DECODE R4936 : découpes dans le scratchpad seulement, jamais
copiées dans un dépôt ni publiées.

## Lieux
- 106 « g lu t » non vus = les 114 g=t de R4936_align.tsv (dont [?mint] L15) moins les 8 tranchés par Brice (T1-T8).
- 36 « g lu u » (figure g, valeur propre u) non testés.
- Index sN = rang de la figure dans la ligne (alignement de Daniel), comme la planche.

## Critère de forme (provisoire, d'après les exemples d'alphabet ; précisé en partie B par les 9 prototypes de Brice)
- **crochet** (= q du scripteur, valeur t) : panse ronde de hauteur d'x ; la queue descend PEU sous la ligne de base (environ
  la hauteur de la panse ou moins) et se termine par un petit crochet ou une goutte tournée à gauche ; pas de trait qui remonte,
  pas de boucle inférieure.
- **boucle** (= g, valeur u) : la queue descend nettement plus bas (environ 1,5 à 2 hauteurs de panse sous la ligne), tourne à
  gauche et REMONTE en formant une boucle inférieure, ouverte ou fermée (allure de « 8 » ou de « g » d'écriture).
- **douteux** : forme intermédiaire (queue longue sans remontée, ou courte avec amorce de boucle), tache, chevauchement d'une
  ligne voisine, figure coupée, ou boîte dont on ne peut pas affirmer qu'elle contient la bonne figure du mot (segmentation).
- Confiance notée 1 (faible) / 2 / 3 (nette). Un « crochet » ou une « boucle » de confiance 1 est traité comme douteux.

## Étalonnage aveugle (avant toute relecture des 142 lieux)
- 21 vignettes anonymes mêlées (graine 20261124) : les 9 lieux de Brice (T1-T9), les 3 contrôles (K1-K3, à classer x / z),
  9 lieux non vus tirés au hasard (graine 4936) parmi les 142. La table de correspondance est écrite par script et n'est lue
  qu'APRÈS que la classification a été notée et hachée (etalonnage-classification.tsv + sha256).
- Arrêt : si plus d'1 désaccord avec Brice sur T1-T9 (un « douteux » compte comme désaccord) ou un contrôle faux →
  ARRÊT, rapport : la relecture IA ne serait pas fiable ; rien n'est recompté.
- Les 9 lieux non vus de l'étalonnage gardent la classification notée à l'aveugle.

## Application (copie locale integration-ai/ ; aucune valeur nouvelle dans la clé, clé gelée a-v b-f c-p d-o e-y g-u h-r i-n
k-l m-z q-t s-x, 7 = m)
- g lu t + crochet sûr → relabel g→q (t soutenu par la forme). g lu t + boucle sûre → t NON soutenu à ce lieu : signalé, mot
  inchangé ({probable}), aucune autre lecture proposée.
- g lu u + boucle sûre → u confirmé (aucun changement). g lu u + crochet sûr → conflit signalé (u non soutenu), mot rétrogradé
  {probable} s'il était sûr.
- douteux → aucun changement.
- Un mot n'est « sûr » (#728) que si, après relabel, toutes ses figures se lisent par la clé gelée et donnent le mot entier
  (aucune lettre restante sur un look-alike non vérifié : q=u, c=y, g=g, h, a, n restent comme avant sauf vérifiés par la planche).
- Ces changements sont marqués « relecture IA lieu par lieu, prototypes validés par un humain », distincts de ceux de la planche.
- Part de R4936 = mots sûrs / 341. Si > 0,85 : préparer (sans pousser) une mise à jour pour Daniel ; sinon dire ce qui manque.

---
## Partie B (24/11, après l'étalonnage aveugle, AVANT les 133 lieux restants) — critère précisé sur les 9 prototypes de Brice
Partie A gelée : RELECTURE-AI-PREREG.partA.md, sha256 927b4cbb… (ligne 1 de RELECTURE-AI-PREREG.sha256).

### Étalonnage (fait) — integration-ai/etalonnage/
Classification notée et hachée avant lecture de la table (etalonnage-classification.tsv, sha256 d1889951…). Accord avec Brice
**9/9** (T1-T8 crochet, T9 boucle) ; contrôles **3/3** (K1 x, K2 z, K3 z). Règle d'arrêt non déclenchée.
Limites dites : Brice ayant déjà répondu, ses réponses (8 crochets, 1 boucle) étaient connues de l'agent avant l'étalonnage ;
l'aveugle porte sur l'identité des vignettes (mêlées, anonymes), pas sur la proportion attendue. Les vignettes p. 2 se
reconnaissent à la couleur du papier (aucune cible de Brice n'est en p. 2).
9 lieux non vus de l'étalonnage (classes gardées telles quelles) : L08 s2 crochet 2 ; L28 s3 crochet 3 ; L45 s13 crochet 2 ;
L07 s27 crochet 2 ; L04 s21 crochet 2 ; L08 s16 crochet 3 ; L35 s17 douteux (queue longue en J sans boucle) ;
L34 s12 douteux (boîte mal placée : un y) ; **L09 s27 (g lu u) crochet 2 → conflit** (u non soutenu par la forme à ce lieu).

### Prototypes (découpes 400 %, proto/ du scratchpad ; image native, panse ≈ 16-18 px de haut)
- **crochet** (T1-T8, Brice) : panse ronde fermée à hauteur d'x ; la haste droite descend sous la ligne de base de 1 à 1,4
  hauteur de panse (≈ 18-25 px), puis tourne à GAUCHE en un crochet ouvert (en « c » ou « J » court) qui finit par une goutte
  épaissie ; l'extrémité reste sous la panse ou à peine au-delà de son bord gauche ; AUCUN trait ne remonte ; le contre-poinçon
  du crochet reste ouvert. Variante T1/T5/T6 : queue un peu plus longue (≈ 1,4), toujours ouverte et sans remontée.
- **boucle** (T9, Brice ; exemples d'alphabet L02 s8, L03 s4) : la queue descend ≈ 2 hauteurs de panse ou plus (≈ 35 px et
  au-delà), passe nettement sous le crochet type, tourne à gauche et REMONTE vers la haste en formant une boucle inférieure
  fermée ou presque (allure de « 8 » / « ℓ ») ; elle entre souvent dans la zone des hampes de la ligne suivante.
- **douteux** : queue longue (> 1,5 panse) en J sans remontée, ou courte avec amorce de remontée ; boucle confondue avec une
  hampe de la ligne suivante sans continuité visible ; tache ; figure coupée ; boîte qui ne tombe pas sur le g attendu.
- Contrôle de position obligatoire pour chaque lieu : la vignette montre le mot ; les voisins visibles doivent correspondre
  aux figures attendues (sinon nouvelle localisation, ou douteux si impossible).
