# PREREG-C14 — 1549-05-27, Charles Quint → Ferrante Gonzaga, Bruxelles (Estense, Autografoteca Campori, Lettera K, Karl V, sfasc. III, chiffre cc. 31-36 ; déchiffrement d'époque cc. 12-15) — 17/11/2026, agent Opus 5.5

Écrit et haché AVANT toute transcription de la portion (c. 31v et suite), AVANT toute ouverture des images du déchiffrement
d'époque (cc. 12-15) et AVANT toute ouverture des fichiers de McBratney qui portent du clair ou des valeurs au-delà de c. 31r.

## Antériorité et état de connaissance déclarés (honnêteté du test)
- PR #684 (mmcbratney, fusionnée 16/11) : c. 31r seule transcrite et décodée avec sign_table (64,1 % des unités, « decoded, not read ») ;
  déchiffrement d'époque transcrit pour c. 12r seulement ; « une passe séparée sur cc. 31v-36v avec une clé reconstruite mécaniquement
  a fait 38,71 %, non déposée » ; NOTES : 31v-36r « not transcribed or decoded … not attempted this session ». Rien de lu ni réservé
  sur 31v-36v (aucun « reserved », aucune PR/issue ouverte ; recherche gh 17/11).
- NON ouverts avant le gel de T14-arb : KEY_NOTES.md (liste des valeurs manquantes tirée de la passe 31v-36v), 27may1549_decipherment_12r.txt,
  _en.md, _reading.txt, _decryption.txt, _ledger.tsv, _analysis.txt, _score.txt, _31r.tsv. Lus : corps de PR, FREEZE.txt, PRIOR_ART.md (lignes
  repérées), NOTES_mcbratney.md (lignes repérées : liste des pages chiffrées 31r, 31v, 32r, 32v, 33r, 33v, 34r, 35v, 36r ; clair 34v-35v).
- Notre propre passé : C01 (29/10) a « vu » les pages cc. 12-15 à l'échelle de la page (aucune transcription, aucune valeur apprise ;
  aucune des clés KB1-KB5 n'apprend sur le 27/5). C12 a recopié la table key_cv1549.tsv (valeurs = sign_table de Daniel, tirées de 31r et de
  l'image Masiá/Tomokiyo, pas du clair de 31v) ; seules 3 valeurs créditées sont dans KB4/KB5.
- Main : 31r (vu à 1900 px pour cette question seulement) est l'ORIGINAL de chancellerie avec phrases en clair intercalées ; le 4/7 (41v)
  est une COPIE chiffrée. Identité de main NON établie ; on teste donc KB5 telle quelle, sans ajustement.

## Clé gelée : KB5.tsv (sha256 dans SHA-C14.txt)
KB5 = KB4 (fe2552a8…) avec exactement deux changements, tirés de la portion grillée du 4/7 : `g` = y (KB4 : re), `4` = o (KB4 : que).
Rien d'autre. Aucune valeur de la passe 38,71 % de McBratney.

## Portion neuve
- c. 31v depuis la l. 1, tout le chiffre, lignes entières, dans l'ordre ; si 31v donne < 300 jetons, on continue sur 32r par lignes
  entières jusqu'à ≥ 300 jetons (ligne entamée finie). Mots en clair notés `[...]`, hors jetons (servent d'ancres).
- Notation : GLYPHES.md / GLYPHES-C02 / GLYPHES-C03 + formes de T41v-arb / T13-arb ; forme inconnue → libellé nouveau (décodé `#`) ; illisible → `?`.
- Images : recadrages IIIF natifs (curl, recette NOTES gonzaga1549 « Access »), sur SPOF_2 seulement, étude seulement, jamais publiés.

## Transcription (2 passes aveugles)
- Passe A : SECOND sous-agent aveugle (Opus), mêmes recadrages, étalonnage = recadrages 41v grillés + T41v-arb / T13-arb ; ni clé, ni référence,
  ni décodage. Échec → passe A par moi, déclarée.
- Passe B : moi, sans ouvrir A avant que B soit écrite et hachée. Arbitrage sur l'image, sans clair ni décodage. T14-arb gelé (sha256) AVANT
  toute ouverture de cc. 12-15 et des fichiers McBratney non ouverts ci-dessus. Accord A/B rapporté.

## Référence (déchiffrement d'époque cc. 12-15, autre main), transcrite par moi APRÈS le gel de T14-arb
- Segments = suites de jetons entre deux ancres en clair de l'original (ou bord de portion). Pour chaque segment :
  1. si le déchiffrement porte les mêmes ancres (mots en clair), la référence est le texte entre elles ;
  2. sinon, début : après le texte correspondant à la fin du chiffre de 31r (repéré par la dernière ancre commune de 31r et par la
     longueur r × n, n = jetons de 31r après cette ancre, comptés dans notre notation ; McBratney 31r peut servir de contrôle, pas d'ajustement) ;
     fin : r × n (jetons du dernier segment) ; r = 488/322 (taux C12) ; coupe à la frontière de mot la plus proche (égalité → la plus courte).
- Bloc sans correspondant dans le déchiffrement : exclu des deux côtés (déclaré). Abréviations développées comme C12/C13.

## Mesure unique
`python3 score_c14.py T14-jetons.txt REF-C14.txt KB5.tsv 527 <segments>` (= score_c13.py, métrique C02 ; car. = 1 − distance d'édition
normalisée ; 200 témoins = permutations des valeurs de KB5, graine 527).
- **VALIDÉE** si M_car ≥ 0,85 ET M_car ≥ témoin max + 0,30. Mots : rapportés, non décisifs.
- **PARTIELLE** si rang 1/201 mais sous un seuil. Sinon NON VALIDÉE. Une seule mesure ; portion grillée ensuite.
- Contrôle d'information (déclaré, non décisif) : la même mesure avec KB4 est calculée APRÈS, pour isoler l'effet de g = y et 4 = o.

## Ensuite
Compte strict (règle de Daniel) : « read » seulement si ≥ 95 % des mots sont SÛRS ; sûrs + probables à part. Livraison : mise à jour PR #763
ou PR neuve (dossier targets/gonzaga1549/dudout_27may1549/), sans images, catalogue.json non touché, en anglais ; crédits McBratney
(localisation du passage et du déchiffrement d'époque, table de comparaison).
