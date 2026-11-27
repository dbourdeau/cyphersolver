# Consigne de transcription aveugle (C09, lead 1561) — FORMES SEULEMENT

Tu transcris des lignes de chiffre (lettres de 1546-1555, chiffre à signes) **par la forme seule**.
Tu n'as ni clé, ni valeurs, ni déchiffrement. N'essaie JAMAIS de décoder ni de deviner du texte.

## Interdits (lecture aveugle)
- Ne lis AUCUN fichier hors de ceux listés dans ta mission (images de lignes, planches d'atlas, cette consigne).
- En particulier : rien dans `cyphersolver-pr/`, aucun `key*.tsv`, `K4.tsv`, `atlas.tsv`, `sign_*.tsv`, aucun fichier WAINUT,
  aucun autre dossier de `dechiffrements-europe/`, aucun fichier `blind/` d'un autre lecteur. Pas de web.

## Jeu de signes nommé
Référence visuelle : `atlas/planche_A_sans_valeurs.png` … `planche_D_sans_valeurs.png` (exemples découpés dans une autre
lettre du même chiffre, autre main ; chaque rangée porte son NOM à gauche, à utiliser tel quel, sans le « fig. »).
Noms de l'atlas (75) :
X-bar star-x x-stroke-o xo x-curl x-curl-1dot x-curl-2dots x-p sideloop sideloop-o nine eight-1dot eight-2dots eight-bar
eight-o eight-oo eight-p g-1dot g-2dots g-bar g-o ring-1dot ring-inf ring-stem op openj-1dot openj-2dots j-1dot j-2dots loopg
seven seven-1dot seven-2dots seven-bar y-1dot y-2dots y-bar y-o ys-1dot ys-2dots ys-bar n a ap aplus S theta theta-bar
cslash cw-2dots six-1dot six-o six-bar e-1dot e-oo L-o L-1dot L-2dots L-bar invT-1dot Lambda-o Lambda-1dot Lambda-side
Lambda-bar tri-1dot tri-2dots tri-bar tri-o d dash-o crossV-bar ap-dots-below Gamma dash L-tick

Grammaire des noms (pour une forme de base connue avec une autre marque) : `<base>-1dot` (un point au-dessus),
`-2dots` (deux points), `-bar` (trait/barre), `-o` (petit o/anneau attaché), `-p` (queue en boucle vers le bas, « p »),
`-dots-below` (points SOUS le signe). Bases : x-stroke-o, x-curl, eight, g (anneau + queue ouverte), ring, openj, j, seven,
y, ys, n, a, ap, S, theta, six, e, L, invT, Lambda, tri, sideloop, nine, d, dash.
Autres noms admis (formes absentes des planches) : `u` (u/v ouvert nu), `m` (m en lettre), `six` (6 nu), `L` (L nu),
`eight` (8 nu), `tri-cross` (triangle/T à croix), `tt-cross` (croix seule type « + » ou « t » croisé), `theta-tick`
(theta avec petite coche), `Lambda-p`, `tri-p`, `L-p`, `n-1dot`, `n-2dots`, `n-o`, `n-p`, `cw-1dot` (ω ouvert à 1 point),
`cw` (ω nu), `ring-inf` (deux anneaux couchés « oo »), `N` (N majuscule), `R-1dot`, `crescent` (trait oblique / barre de
séparation, écrire aussi `/` si c'est une simple barre oblique), `star` (étoile), `plus` (+ isolé).
Tout autre signe : `?` + courte description ASCII sans espace (ex. `?pi-barred`, `?cross-loop`, `?8-hook`).
Mots écrits en lettres latines dans le chiffre (ex. groupes comme « dide », « mus ») : `{lettres lues}`.
Doute entre deux noms : `nom1|nom2` (le plus probable d'abord). Signe illisible (tache, déchirure) : `#`.

## Format de sortie
Une ligne de fichier = une ligne de chiffre du manuscrit, dans l'ordre : `P<page>-L<nn> tok tok tok …` (séparés par des espaces).
Ne transcris pas l'écriture ordinaire (clair) : si une ligne commence ou finit en clair, écris `[clair]` à cet endroit.
En tête du fichier : `# lecteur <A|B>, lettre <id>, date/heure, images utilisées`.
Compte : un jeton par signe. Les points comptent : regarde-les à l'agrandissement (tu peux recadrer/agrandir avec Python/PIL
dans le dossier scratch indiqué) ; si 1 point net + 1 tache, suis le point net.
À la fin : calcule `shasum -a 256` de ton fichier et donne-le dans ton rapport ; n'édite plus le fichier ensuite.
