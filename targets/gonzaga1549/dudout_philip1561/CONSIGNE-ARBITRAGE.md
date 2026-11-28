# Consigne d'arbitrage (C09) — FORMES SEULEMENT, sans clé

Entrées : `arb/<lettre>_PRE.txt` (lignes où A et B s'accordent ; chaque désaccord est écrit `{{lecture A||lecture B}}`),
`arb/<lettre>_DIFF.tsv` (liste des désaccords), la consigne `CONSIGNE-AVEUGLE.md` (noms admis) et les planches `atlas/`.
Images : les bandes de lignes indiquées dans ta mission.

Pour chaque `{{A||B}}` : regarde le signe sur l'image (agrandi) et écris UN choix : la lecture A, la lecture B, ou un autre
nom si les deux se trompent. Nombre de signes : si A et B diffèrent par le nombre de jetons, compte les signes sur l'image.
Formes hors atlas (`?…`) : HARMONISE-les. Fais une liste fermée de classes `?<nom>` (une classe = une forme), avec pour chacune
une description et 1-3 emplacements d'exemple, dans `arb/<lettre>_GLOSSAIRE.md`. Quand deux lecteurs ont donné deux noms à la même
forme (ex. `?pi` / `?pi-barred`), garde un seul nom de classe. Si une forme `?…` est en fait un signe de l'atlas, écris le nom de l'atlas.
Tu peux aussi corriger une place où A et B s'accordent si l'image montre clairement une erreur commune : note-le dans le glossaire (section « corrections communes »).
Garde `a|b` seulement si l'image ne permet vraiment pas de trancher (le premier choix compte).

Sortie : `arb/<lettre>_ARB.txt`, même format que les fichiers blind (une ligne = `P..-L.. tok tok …`), sans aucun `{{ }}`.
INTERDITS : aucune clé, aucune valeur, aucun texte clair, aucun fichier du dépôt cyphersolver ni d'autre dossier ; ne décode rien.
À la fin : SHA-256 de `_ARB.txt` et de `_GLOSSAIRE.md`, et ne les modifie plus.
