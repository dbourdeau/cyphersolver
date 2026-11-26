# Brief — transcription aveugle des formes, lettre du 12 mars 1548, portion Q de PREREG-O5 (§3)

Vous êtes un transcripteur aveugle. Vous transcrivez des FORMES seulement. Vous ne déchiffrez jamais.
(Brief d'O4, `o4-2511/input/BRIEF-PASSE-O4.md` a1c7b711…, repris tel quel sur le fond ; seuls changent les pages et les chemins.)

## Fichiers que vous pouvez ouvrir (et RIEN d'autre)
- `input/SIGNS.md` — noms des signes et description de leurs formes (WAINUT).
- `input/SHAPES-KEY-NAMES.md` — description des formes d'autres noms (WAINUT), formes seulement.
- `input/crops/` — recadrages des lignes chiffrées de la portion Q : `<page>_L01.jpg` … (page = 6v, 7r, 7v, 8r, 8v ; une page
  sans ligne chiffrée n'a pas de fichier), chacun avec la ligne entière (triangle rouge à gauche ; lignes voisines en partie
  visibles : ignorez-les), `_a` (moitié gauche, ×1,6) et `_b` (moitié droite, ×1,6 ; les moitiés se chevauchent : ne comptez pas
  deux fois les signes du chevauchement), et `<page>_overview.jpg` avec les numéros de ligne. Les zones blanches sont masquées
  exprès (texte en clair, notes) : n'essayez pas de deviner ce qu'elles cachent. Vous pouvez recadrer / agrandir ces fichiers
  avec Python PIL (fichiers temporaires dans votre dossier de sortie seulement, effacés à la fin).
N'ouvrez AUCUN autre fichier ni dossier : ni clé, ni décodage, ni autre transcription, ni `scans/`, `o2-2311/`, `o3-2511/`,
`o4-2511/`, `wainut/`, ni l'autre dossier `passe-*/`, ni `lecture-*`, ni HANDOFF, ni clone de cyphersolver. Pas de recherche sur
le web. Ne devinez aucun texte en clair : aucune valeur de lettre.

## Règles de nommage
- Un jeton par signe, séparés par des espaces ; marque haute collée à sa base (`3o`, `4o`, `12`, `x3`, `mx2`, `4s`, `N7o`) ;
  `.` en jeton propre ; `/` et `(` tels qu'écrits.
- N'utilisez un nom de SIGNS.md ou de SHAPES-KEY-NAMES.md que si la forme correspond à sa description.
- **Toute autre forme : VOTRE propre nom `t1`, `t2`, `t3`… — jamais `N1`, `N2`… (les noms `N` appartiennent à la liste de
  référence).** Décrivez chaque forme `t` une fois à la fin de votre fichier (forme seulement). Cela remplace la ligne de
  SIGNS.md qui dit « Unknown shape: `N1`, `N2`, … ».
- Douteux : suffixe `?` (`4o?`). Barré / annulé : suffixe `_`. Signe illisible : `t?` (un jeton).
- Ignorez les petites lettres écrites au-dessus ou entre les lignes d'une autre encre (gloses postérieures) et tout texte en
  clair : ils sont masqués autant que possible ; si un morceau reste visible, ne le transcrivez pas et ne vous en servez pas.

## Sortie
Un seul fichier `<votre dossier>/transcription_pass<X>.txt` :
```
# en-tête : qui/quand, méthode, formes t ajoutées (forme seulement), incertitudes
6v L01: tok tok tok ...
...
```
Exactement les lignes des recadrages, dans l'ordre des pages, préfixe exact `6v L01:` etc. Répondez ensuite avec : nombre de
lignes, nombre de jetons, formes t ajoutées, principaux doutes. Travaillez signe par signe ; vérifiez chaque ligne deux fois
(comptez les signes de la ligne entière contre les moitiés).
