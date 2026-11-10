# PROTOCOLE P01 — taulet-1866 (catalogue Bourdeau n° 2444 ; AHN, DIVERSOS-COLECCIONES,193,N.99, PARES 5928106)
Écrit le 09/11/2026 ≈ 22:20 CET par l'agent Opus K2, AVANT toute transcription des nombres et tout calcul (aucune valeur
de nombre essayée). Critère de validation : BRIEF-VAGUE23.md point 9 (Brice, 30/10/2026).

## Constat préalable (vu seulement, planches réduites 560 px + vues 25-26 en pleine taille)
- Vues 2-13, 44-50 : ordres reçus (Gobierno militar de Tarragona) en clair. Vues 14-45 : copiador des rapports numérotés
  (1 → 67) du lieutenant-colonel Bernardo Taulet, colonne/cantón de Jalet (Falset), 14/1 → 2/3/1866. Rapport 13 (24/1, vue 21) :
  Taulet ne peut lire une communication « por carecer de la clave para descifrar » et demande la clé ; rapport 14 (vue 22) la
  redemande. Les nombres apparaissent à partir du rapport 18 (27/1, vue 25).
- Nombres à 2 chiffres reliés par des tirets, insérés dans le clair : longue suite vue 26 (≈ 100 nombres, coupée de mots
  clairs : « que », « de V.S. », « de ayer », « quedando », « y espero », « para ») ; suite vue 27 ; courtes suites de 5-9 nombres
  en fin de rapport, juste avant « Dios gue. » (vues 25, 27, 28, 30, 31, 32, 34, 35, 39, 41…), certaines répétées
  (61-64-38-92-29-60-64 deux fois vue 25). Vues 51-52 : télégramme reçu (Reus, 7 mars 1866) en nombres séparés par des virgules,
  ≈ 100 nombres, avec « Traslado a V.S. … por parejas de Guardia Civil, lo siguiente = … V.S. … ».
- Fuites déclarées : j'ai vu les répétitions des suites de fin de rapport et formé à l'œil l'idée (non testée) qu'elles
  pourraient coder l'heure ou une formule ; j'ai vu les formes du télégramme sur planche réduite sans essayer de valeur.

## Unités et partition (fixées maintenant)
- « Suite » = séquence continue de nombres entre deux passages clairs ; une suite coupée par une fin de ligne reste une seule
  suite. Numérotation S1, S2… dans l'ordre des vues. Un mot clair inséré (p. ex. « que ») coupe la suite.
- **TENUE À L'ÉCART H** = dans le télégramme (vues 51-52), la (les) suite(s) qui suivent le DERNIER « V.S. » clair du télégramme
  jusqu'à la fin des nombres (vue 52, avant « Dios gue. »). **APPRENTISSAGE T** = toutes les autres suites (rapports vues 25-45,
  et les deux premières suites du télégramme : avant « por parejas » et entre « lo siguiente = » et « V.S. »).
- Seuil de puissance : si H compte moins de 30 nombres, la mesure est « non probante » et la clé ne peut être que PARTIELLE.
- Risque déclaré : le télégramme vient d'un autre expéditeur (Reus) ; si sa clé diffère de celle des rapports, la mesure
  échouera ; T contient ses deux premières suites pour le détecter.

## Transcription
- Toutes les suites (T et H) transcrites dans `transcription.txt` (format : `Sk<TAB>T|H<TAB>n.n.n` ; douteux `n?`, illisible `?`,
  variante `a|b`) et gelées par SHA-256 AVANT toute construction de clé. Pas de correction après gel (une passe 2 serait un
  nouveau fichier déclaré, sans effet sur la mesure). Le clair voisin (cribs) va dans `clair.txt` (non haché).
- Les suites de H sont transcrites en une passe, sans tentative de lecture.

## Clé K_T
- Construite sur T seul : cribs du clair voisin (lieux, colonnes, formules « sin novedad », heures), fréquences, répétitions ;
  substitution simple, homophonique, syllabique ou code (un nombre → lettres, syllabe, mot, nulle « - », séparateur « _ »).
- Aucune valeur tirée de H ; H ni décodé ni regardé « pour voir » avant le gel de K_T (`KEY.tsv`, SHA-256 dans HANDOFF).
- Nombre de H absent de K_T → « ? » (non couvert).

## Mesure UNIQUE (`scripts/measure.py`, haché avec ce protocole avant toute exécution sur H)
- `python3 -I scripts/measure.py transcription.txt KEY.tsv <lexique es.json.gz> --part H`
- Décodage de chaque suite de H par K_T ; normalisation minuscules a–z (accents ôtés, ñ→n) ; concaténation par suite.
- **car** = part des lettres décodées couvertes par une segmentation à couverture maximale en mots du lexique
  `_shared/cyphersolver/lang/lexicons/es.json.gz` (effectif ≥ 2, longueur ≥ 2) ∪ {a, y, o, e} ∪ NOMS (liste dans measure.py) ;
  « ? » jamais couvert.
- **Témoins** : 200 clés = K_T dont les valeurs (hors « _ » et « - ») sont permutées entre les nombres, graine 2444 ; max = meilleur.
- **VALIDÉE** si car ≥ 0,85 ET car ≥ meilleur témoin + 0,30 ET H ≥ 30 nombres. Sinon PARTIELLE (si la clé lit T) ou échec.
  Accord en mots rapporté, non décisif.
- Une seule mesure ; H grillée ensuite ; rien de rétroactif.
- Si la clé n'est pas trouvée sur T (pas de lecture convaincante), AUCUNE mesure n'est jouée et H reste vierge.

## Lecture et publication
- Fiche : sûrs / probables {x} / restitués [x] / irrésolus ‹…›, justifiés ; règle de Daniel ≥ 95 % des mots.
- Publication seulement si VALIDÉE ET ≥ 95 % ; images PARES seulement après vérification de la licence.
- Aucune PR ni issue ; `NOTE-DANIEL.md` (anglais).
