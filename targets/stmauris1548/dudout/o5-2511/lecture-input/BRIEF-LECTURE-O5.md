# Brief — lecture par le sens du décodage, portion Q de PREREG-O5 (§7)

Vous êtes un lecteur indépendant. Vous lisez un décodage mécanique et vous dites, mot par mot, ce qui se lit par le sens et ce
qui ne se lit pas. Vous ne voyez ni les images, ni les signes, ni la clé : seulement les lettres que la clé a produites.

## Ce que vous savez du texte (et rien de plus)
Un texte supposé en français du milieu du XVIᵉ siècle (correspondance diplomatique), graphie d'époque, chiffré par
substitution puis décodé avec une clé figée. Le décodage n'a pas d'espaces ni de ponctuation ; i/j et u/v y sont confondus ;
il n'a pas d'accents ; `?` marque un signe auquel la clé ne donne pas de valeur. Il peut y avoir des nulles (signes sans valeur
glissés dans le texte), des lettres doublées ou omises par le chiffreur, des noms propres. La clé n'est pas forcément juste :
votre lecture sert justement à le mesurer. Ne forcez rien : un passage qui ne se lit pas doit être déclaré irrésolu.

## Fichiers que vous pouvez ouvrir (et RIEN d'autre)
- `lecture-input/DECODE-O5.txt` — le décodage, une ligne par ligne chiffrée (`6v L01: …`) ; le texte est continu d'une ligne
  et d'une page à l'autre.
- `lecture-input/BRIEF-LECTURE-O5.md` (ce fichier) et `lecture-input/check_lecture_o5.py` (contrôle de forme).
- Votre dossier de sortie `lecture-L<n>/`.
N'ouvrez AUCUN autre fichier ni dossier (ni images, ni `scans/`, `crops/`, transcriptions, `passe-*`, `ARBITRAGE/`, clé,
`MESURE-*`, autre dossier `lecture-*`, `o2-2311/` à `o4-2511/`, `wainut/`, HANDOFF, notes, cyphersolver). Pas de recherche
sur le web. Vos connaissances du français ancien sont votre seul outil.

## La règle (Daniel Bourdeau, CONTRIBUTING de cyphersolver)
Un document compte comme lu quand **95 % de ses mots se lisent par le sens**. On rapporte séparément les mots **sûrs**,
**{probables}**, **[restitués par le sens]** et **‹irrésolus›**, et chaque mot non sûr a sa justification. Une valeur tirée
du seul sens reste au mieux {probable}. Une restitution [x] ne contredit jamais des lettres sûres du chiffre. On garde la
graphie du chiffre telle quelle : on ne modernise pas (« auoit » reste « auoit », « faict » reste « faict »).

## Format de votre lecture : `lecture-L<n>/LECTURE.txt`
Lignes commençant par `#` = vos commentaires (ignorés). Le reste est un texte continu, en minuscules, qui reprend **toutes
les lettres du décodage, dans l'ordre, sans en changer, en sauter ni en ajouter une** — sauf les lettres que vous donnez par
le sens, écrites en MAJUSCULES. Vous coupez en mots par des espaces ; l'apostrophe et le trait d'union séparent aussi les mots.
- `mot` — **sûr** : toutes ses lettres viennent du décodage, aucune majuscule, aucun `?`, et le mot se lit sans doute.
- `{mot}` — **probable** : lettres du décodage, mais un doute (forme rare, coupure discutable, nom propre), ou bien **une seule**
  lettre donnée par le sens (en MAJUSCULE, par ex. pour un `?`), le mot gardant au moins 2 lettres du décodage.
- `[mot]` — **restitué** : plus d'une lettre donnée par le sens, ou un mot entier ajouté parce que le sens l'exige (omission
  du chiffreur). Une MAJUSCULE remplit un `?` du décodage ou s'insère entre deux lettres ; elle ne remplace jamais une lettre
  du décodage (si une lettre vous semble fausse, le mot est ‹irrésolu›, ou {probable} si la coupure seule est en doute).
- `‹lettres›` — **irrésolu** : les lettres du décodage telles quelles (`?` permis), aucune majuscule ; compte pour 1 mot ;
  `‹lettres|3›` si vous estimez que ces lettres couvrent 3 mots.
- `(xy)` — **nulle** : 1 à 3 caractères du décodage (`?` permis) que vous jugez sans valeur (nulle, lettre doublée) ; ce n'est
  pas un mot. À utiliser avec retenue et à justifier.
- `§6v-L01` — repère facultatif, placé exactement là où commence la ligne 6v L01 (le contrôle le vérifie). Conseillé.
Une marque enserre des mots entiers (`{l'on}` = 2 mots probables ; pas `aut{r}e`). Pas d'accents, pas d'autre ponctuation.
Exemple inventé (décodage `commelonenau?itfaitgrant`) : `comme l'on en {auOit} faict…` est FAUX (« c » ajouté sans
majuscule) ; juste : `comme l'on en {auOit} fait {grant}`.

## Fiche de justifications : `lecture-L<n>/JUSTIFICATIONS.tsv`
Une ligne par mot non sûr (probable, restitué, irrésolu, nulle), dans l'ordre : `J001<TAB>{auOit}<TAB>justification`.
Obtenez la liste des identifiants avec
`python3 -I lecture-input/check_lecture_o5.py lecture-input/DECODE-O5.txt lecture-L<n>/LECTURE.txt --modele`.
Justification = pourquoi ce mot, pourquoi cette classe (forme attestée, accord, construction, contexte ; pour une restitution :
quelles lettres sont données par le sens et pourquoi ; pour une nulle : pourquoi elle n'a pas de valeur). Au moins une phrase.

## Contrôle avant remise
`python3 -I lecture-input/check_lecture_o5.py lecture-input/DECODE-O5.txt lecture-L<n>/LECTURE.txt lecture-L<n>/JUSTIFICATIONS.tsv`
doit afficher `FORME OK`. Corrigez la FORME autant qu'il le faut ; ne changez pas une classe pour atteindre un chiffre : le
contrôle ne juge pas votre lecture, un second lecteur indépendant lira le même décodage et les deux lectures seront comparées.
Vous pouvez aussi écrire `lecture-L<n>/TEXTE.txt` : le texte en clair lisible (graphie du chiffre, mêmes marques), non compté.

## Réponse finale
Nombre de mots sûrs / probables / restitués / irrésolus, nulles, vos principaux doutes, et une phrase sur ce que dit le texte.
Ne modifiez plus rien après votre réponse : vos fichiers sont gelés par SHA-256.
