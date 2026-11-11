# PROTOCOLE P01 — vanhalen-1840 (catalogue Bourdeau n° 2423 ; AHN, DIVERSOS-COLECCIONES,195,N.14, PARES 4151130)
Écrit le 09/11/2026 ≈ 15:25 CET, AVANT toute transcription et tout calcul (aucune valeur de nombre essayée).
Agent Opus 5.5. Critère de validation : BRIEF-VAGUE23.md point 9 (Brice, 30/10/2026).

## Constat préalable (vu seulement)
- Image 2 (zoom 10, 531×648 px) : lettre en clair, en espagnol, avec des suites de nombres 1-34 séparés par des points,
  introduites par « = » et souvent terminées par 70 ; contexte clair : Tarragona, Cervera, « dicha Ciudad », Llacuna, Llarch.
- Image 3 : une suite d'environ 16 nombres avant la signature (non regardée en détail).
- Fuite déclarée : en regardant l'image 2 à l'œil, j'ai vu la forme de la dernière suite de l'image 2 (après « dicha fecha
  sobre »), sans essayer aucune valeur.

## Unités et partition (fixées maintenant)
- « Suite » = séquence continue de nombres entre deux passages clairs (le « = » et le « .- » ou le clair qui suit la bornent).
  Une suite coupée par une fin de ligne reste une seule suite.
- Suites numérotées S1, S2, … dans l'ordre de lecture (image 2 puis image 3).
- **TENUE À L'ÉCART H** = (a) la DERNIÈRE suite de l'image 2 (celle qui suit « dicha fecha sobre ») ET (b) TOUTES les suites de
  l'image 3. **APPRENTISSAGE T** = toutes les autres suites (image 2).
- Seuil de puissance fixé : si H compte moins de 20 nombres hors 70, la mesure est déclarée « non probante » et la clé ne peut
  être que PARTIELLE, quel que soit le score.

## Transcription
- Toutes les suites (T et H) transcrites et gelées par SHA-256 (`transcription.txt`) AVANT toute construction de clé.
  Lecture douteuse notée `n?` ; illisible `?` ; variante `a|b`. Pas de correction après le gel (une passe 2 éventuelle
  serait un nouveau fichier déclaré, sans effet sur la mesure).
- Le clair entourant les suites (cribs) est transcrit dans `clair.txt` (non haché, contexte).

## Clé K_T
- Construite sur T seul : cribs tirés du clair voisin (lieux, formules), fréquences, répétitions ; substitution simple ou
  homophonique (un nombre → une lettre, une suite de lettres, une nulle, ou séparateur de mots) permise.
- Aucune valeur tirée de H ; H ni décodé ni regardé « pour voir » avant le gel de K_T (`KEY.tsv`, SHA-256 dans `KEY.sha256`).
- Nombre de H absent de K_T → « ? » (compté non couvert).

## Mesure UNIQUE (`scripts/measure.py`, haché avec ce protocole avant toute exécution sur H)
- Décodage de chaque suite de H par K_T ; normalisation : minuscules a–z, accents ôtés, ñ→n, séparateurs ôtés ; on concatène
  par suite (pas d'espace entre suites).
- **car** = part des lettres décodées de H couvertes par une segmentation à couverture maximale (programmation dynamique) en
  mots du lexique `_shared/cyphersolver/lang/lexicons/es.json.gz` (effectif ≥ 2, longueur ≥ 2) ∪ {a, y, o, e} ∪ NOMS, où
  NOMS = tarragona cervera solsona llacuna igualada barcelona manresa lerida berga cardona vich calaf urgel segarra llarch
  reus montblanc valls brigada division reserva auxiliar norte; « ? » jamais couvert.
- **Témoins** : 200 clés = K_T dont les valeurs (hors séparateur/nulle) sont permutées au hasard entre les nombres, graine 2423 ;
  même calcul ; meilleur témoin = max.
- **VALIDÉE** si car ≥ 0,85 ET car ≥ meilleur témoin + 0,30 (et H ≥ 20 nombres hors 70). **PARTIELLE** sinon si la clé lit T.
  Accord en mots (part des mots décodés de H, découpés par le séparateur s'il existe, présents dans le lexique) rapporté,
  non décisif.
- Une seule mesure ; H grillée ensuite ; aucune correction rétroactive. Les corrections ultérieures pour la lecture sont
  déclarées comme telles.

## Lecture et publication
- Fiche de lecture : sûrs / probables {x} / restitués [x] / irrésolus ‹…›, justifiés ; règle de Daniel ≥ 95 % des mots.
- Publication sur L'Europe chiffrée seulement si clé VALIDÉE ET ≥ 95 % ; crédit PARES / AHN ; images PARES : selon conditions
  d'usage notées dans PROVENANCE.md.
- Aucune PR ni issue : `NOTE-DANIEL.md` (anglais) dans ce dossier.
