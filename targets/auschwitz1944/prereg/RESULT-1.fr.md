# RÉSULTAT — message clandestin d'Auschwitz du 4/9/1944

**Mesure préenregistrée : ÉCHEC (résultat négatif).**

On a testé 6 clés (PREREG.md, SHA-256 88f909c8…). Sur la mise au point (G1–G19), aucune ne dépasse les témoins : chacune ne trouve qu'un seul mot du lexique, quand les témoins en trouvent jusqu'à 4. La clé retenue sur la mise au point, F1-c (texte cité par Kłodziński), ne trouve aucun mot sur la validation (G20–G39) : 0 mot sur 18 groupes de longueur ≥ 2, et ses 200 témoins font au moins aussi bien. La sortie complète est dans essais/mesure_sortie.txt.

Comme prévu au PREREG, on n'ajuste rien après coup. On ne fait donc pas de lecture par le sens.

## Observations (hors mesure, non probantes, à préenregistrer avant tout nouvel essai)
- **Un seul groupe commence de façon plausible.** Avec les clés F1, G2 (7-5-6-1-4-18-27-5-28) commence par « w-i-ę-k-s ». Ce début vient seulement des 7 valeurs attestées par Kłodziński (k=1 … w=7). C'est un indice que la famille de clés est la bonne au moins pour les premiers numéros. La table au-delà de la position 13 resterait à trouver.
- **Indices d'une table non purement positionnelle.** La citation (« … i=10, e=11 … cały alfabet, bez szcz, cz, rz ») évoque une table construite pour couvrir « tout l'alphabet », avec des homophones. Ce ne serait pas une simple lecture du chant position par position. Cette table complète est décrite dans Paczyńska 2013, pp. 33-36, ouvrage non consulté.
- **Groupes répétés.** G7 = G17 et G22 = G34. Ce sont des mots répétés, ce qui est utile pour une prochaine tentative.

## Antériorité (non tranchée, présomption forte)
Je n'ai trouvé aucune lecture publiée de CE message en ligne. En revanche :
- Paczyńska 2013 édite et décode les grypsy de Cyrankiewicz et Kłodziński (« odkodowane grypsy », Paszek p. 127). Le message du 4/9/1944, écrit en polonais avec des mots chiffrés par ce système et venant du même réseau, y figure très probablement, décodé.
- La thèse de Paszek, §5.4 p. 170, présente un message décodé ; cette page n'est pas dans le PDF public.

**Il n'y a donc rien à publier.** Avant toute nouvelle tentative, il faudrait consulter Paczyńska 2013 (pp. 33-36 pour la table, et l'édition du message daté du 4/9/1944).
