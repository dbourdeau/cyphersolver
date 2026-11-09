# PROTOCOLE P01 — pandolfini-francia-1514-15 (cat. Bourdeau 2389 ; puis 2393, 2388)
Écrit le 06/11/2026 (après-midi), AVANT tout calcul : aucune clé écrite, aucun décodage par script, aucun comptage.
Agent Opus (vague 23, cible pandolfini-francia-1514-15).

## Regards déclarés avant ce protocole
- Images ASF MAP LXXII récoltées à la taille native du serveur (1272 px de large ; full/full) sur SPOF_2 (PROVENANCE.md).
- Vus à l'œil : 287 c.343r (pos. 687) entier + zoom des lignes chiffrées 1-3 ; 288 c.344r (pos. 689) entier ;
  308 c.370v (pos. 752) entier + zoom de la 1re ligne glosée ; 215 (pos. 515) entier ; 306 c.368r (pos. 745) ;
  316 c.388r (pos. 783) ; 307 c.369r (pos. 747) entier, sans aucun essai de décodage.
- Essais de tête (non notés comme valeurs, à refaire proprement sur T) : sur la 1re ligne glosée de 308 et la 1re ligne
  chiffrée de 287, j'ai reconnu la STRUCTURE du système : signes de consonnes (avec homophones) portant un chiffre en
  exposant qui note la voyelle suivante (hypothèse a=5, e=4, i=3, o=2, u=1), signes de voyelles seules, groupes
  numériques entre points (« .5. », « .6. », « .26. » = nomenclateur : Cath., Inghilterra, Arciduca), F = « et »,
  D^n = « con/col ». Quelques valeurs de tête : 3 = d, t = n, y = n, 2 = b, 4 = l, 7 = r, r = s, 6 = s.
- 215 n'est PAS de ce système (code à barres obliques, autres signes) : écarté comme texte-clé.
- 306 = clair du 18 janv. 1515 (aucune des six pièces) ; 316 = clair sans titre (mars 1515), déjà apparié à 315 par le catalogue.
- AUCUN regard sur 345 ni 346 (pos. 879-884) : ils forment la portion tenue à l'écart.

## Pièces et partition (fixée maintenant)
- APPRENTISSAGE T (clé) : paires et gloses du même système, au choix, sauf 345/346 : 308 (glosé)/313, 287/288,
  318, 319 (glosés), 290/291-292, 293/335, 320/321, 330/331, 334/332, 338/339, 340/341, 342/343, 349/348, 315/316, 317.
- TENUE À L'ÉCART H : 346 c.441r, PREMIER bloc chiffré continu de la page (du premier signe chiffré jusqu'au premier
  passage en clair d'au moins trois mots), avec sa référence = le passage correspondant de la copie claire 345.
  Les bornes de la référence dans 345 sont fixées par les mots en clair qui encadrent le bloc dans 346 (et non par
  un décodage). Si 346 c.441r commence par un bloc de moins de 4 lignes, H = ce bloc + le suivant (même règle).
  Si 345 n'est pas une copie claire suivie de 346 (passage absent), H passe à 340 c.430r / 341 selon la même règle,
  et l'écart est consigné.
- Rien ne sera décodé dans H avant la mesure unique.

## Transcription
- Jetons ASCII, un jeton par signe : base[^exposant]. Base = forme du signe (légende transcription/LEGENDE.md) ;
  exposant = chiffre(s) ou lettre écrits au-dessus (« 3^4 », « D^n »). Groupes de nomenclateur entre points : « .26. ».
  « ? » suffixe = jeton douteux. Mots en clair entre crochets droits : [et con].
- H est transcrite en entier puis gelée (SHA-256 dans TRANSCRIPTION_H.sha256) AVANT le gel de la clé et avant tout
  décodage ; la référence R (345) est transcrite en clair (abréviations développées) et gelée (REF_H.sha256) — elle peut
  être transcrite avant ou après la clé, mais jamais regardée en même temps qu'un décodage de H.

## Clé
- Format CLE.json : {"vowels": chiffre → voyelle, "base": signe → valeur (consonne(s), voyelle, ou "" = nulle),
  "codes": nombre → mot, "tokens": jeton complet → valeur (exceptions)}. Règle de décodage d'un jeton :
  tokens[jeton] sinon base[signe] + (vowels[chiffre] pour chaque chiffre de l'exposant) + (lettre d'exposant n/m
  ajoutée telle quelle) ; signe inconnu → « ? » (compté comme 1 caractère faux).
- Construite UNIQUEMENT sur T (gloses lues + alignements chiffré/clair), gelée par SHA-256 (CLE.sha256) avant la mesure.

## Mesure unique (sur H)
- D = décodage de H par la clé gelée (script mesure/measure.py, testé d'abord sur données synthétiques).
- Normalisation de D et R : minuscules, lettres seules, h supprimé, j→i, y→i, v→u, k→c, x→s, ph→f, doubles consonnes
  réduites à une (graphie flottante des copistes).
- Accord en caractères = 1 − distance de Levenshtein(D, R) / longueur(R).
- 200 témoins : clés obtenues en permutant au hasard (graine 20261106) les valeurs de "base" entre signes ET les valeurs
  de "vowels" entre chiffres ; codes et tokens gardés. Même normalisation, même formule.
- CRITÈRE (décisif, fixé avant) : accord ≥ 0,85 ET accord ≥ meilleur témoin + 0,30. Sinon NON VALIDÉE, H grillée,
  pas de rattrapage rétroactif (une nouvelle mesure exigerait une nouvelle portion et un nouveau protocole).
- Accord en mots (difflib sur les listes de mots normalisés, part des mots de R retrouvés) : calculé, rapporté, non décisif.

## Après la mesure
- Lettres nues (307, 309, 310, 311, 322, 333 ; puis CXXXVII 666 ; puis LXXII 130/140) : d'abord comparaison avec les
  copies claires sans titre (284, 306, 316, 332, 337, 344, 347, 350, 365-366, 368, 419) par les mots en clair et la date ;
  une pièce couverte par un clair d'époque = EXISTING (pas de lecture à publier).
- Si clé validée : décodage, fiche de lecture (sûrs / probables {x} / restitués [x] / irrésolus ‹…›), règle des 95 %.
- Si non validée : rien n'est présenté comme lu.

## Antériorité (vu avant ce protocole, sans incidence sur la mesure)
- Desjardins/Canestrini, Négociations diplomatiques de la France avec la Toscane, t. II (1861), OCR archive.org
  gri_33125010469852 : imprime Pandolfini aux Huit 1514 jusqu'au 16 août 1514, puis du 25 mai 1515 ; rien entre
  le 16 août 1514 et le 25 mai 1515 ; Vercelli 9 sept. 1515 = Raffaello Girolami (pas Pandolfini 6/8 sept.).
