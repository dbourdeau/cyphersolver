# Règle de sélection — planche « Meyerfeldt k/m » 2411 du 24/11/2026, écrite AVANT toute construction de vignettes

Pièces : Riksarkivet, Pommeranica vol. 149, lettres chiffrées de Meyerfeldt (1712–1714). Vues redressées sur SPOF_2
(src/ = lien symbolique vers …/riksarkivet-echantillons-2411/pommeranica-149-redresse ; aucune copie ici) :
143535 (lettre lue, blocs 1–2), 143510 (22/02/1713, non lue), 143523 (10/05/1712 ou 1713, ligne 1 seulement),
143346 (clé d'époque, page tournée pour que la clé soit horizontale).
🔴 Images Riksarkivet : planche PRIVÉE (Brice seulement), jamais publiée, jamais copiée dans un dépôt ni envoyée.

## Pourquoi
La clé d'époque (CLE.md, gelée CLE.sha 8d682769…) écrit k, l et m par des boucles doubles sur hampe. Dans les
lettres, la boucle double (code DL) se lit m dans « moskowitsche », « Regimenter », « lamentiret » et k dans
« moskowitsche », « wegkrigen », « können » : la transcription ne départage pas k et m (decode donne (k|m)). C'est
le premier doute de la lecture. Les autres doutes (traits pleins et boucles g / h / s / t / r) viennent ensuite.

## Famille 1 (en premier) : k / m / l — options = formes de la CLÉ (143346, ligne liée), + un l des lettres
Options : forme « k » (clé), forme « m » (clé), forme « l » (clé + 2ᵉ l de « letzlich », 143535 L2).
Cibles (8) : 143535 L1 m de « moskowitsche » ; L1 k de « moskowitsche » ; L5 k de « wegkrigen » ; L5 k de « können » ;
L7 m de « Regimenter » ; bloc 2 L10 m de « lamentiret » ; 143523 L1 boucle double (« …(k|m)iches ») ;
143510 L1 boucle + tache pleine (1ʳᵉ ligne).
Contrôles (2), lettres de mots lus, jamais prises comme exemples : C1 1ᵉʳ l de « letzlich » (L2) ; C2 l de « lamentiret »
(bloc 2 L10). Réponse attendue : l.

## Famille 2 : g / h / s / t / r — options = formes de mots lus de 143535
Exemples : g (2ᵉ g de « wegkrigen », L5), h (h de « letzlich », L2), s (s de « moskowitsche », L1),
t (t de « letzlich », L2), r (r de « wegkrigen », L5).
Cibles (3) : L2 1ᵉʳ signe (trait plein « \ ») ; L7 trait plein montant entre « ei » et « l » ; L6 fin, boucle penchée.
Contrôle (1) : C3 s de « sie », L9 (attendu s).

Ordre : la famille 1 forme les questions 1 à 10, la famille 2 les questions 11 à 14 (ordre tiré au sort DANS chaque
famille ; seule modification du noyau planche_core.py copié de planche-2411a : tri stable par q['groupe'] après
le tirage). Places des options : équilibrées par le noyau v2.
Boîtes : scripts/boites.py, mesurées sur crops quadrillés (scratchpad 24/11), vérifiées à l'œil sur crops/_contact.jpg.

## Intégration (après réponses ; rien n'est écrit ailleurs)
1. Un contrôle raté (y compris « impossible à distinguer ») → rien intégré de sa famille ; noté dans HANDOFF.
2. Forme choisie = forme d'une option → le lieu est retranscrit avec CE code (k ou m : nouveau code DK / DM à créer
   dans une nouvelle version de TRANSCRIPTION, la clé gelée n'est pas touchée) ; redécodage avec un nouveau PREREG.
3. Si les k et les m sont choisis de façon cohérente avec le sens (k dans wegkrigen/können, m dans Regimenter/…),
   la distinction est déclarée RÈGLE de lecture de la main ; sinon « impossible à distinguer » → double lecture (k|m)
   maintenue, k/m tranché au sens seulement et compté {probable}.
4. « aucune / autre forme » + remarque → nouvelle étiquette de signe SANS valeur.
5. Rien publié, rien envoyé, pas de PR.
