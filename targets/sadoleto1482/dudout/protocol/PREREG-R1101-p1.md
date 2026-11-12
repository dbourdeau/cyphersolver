# PREREG — sadoleto-1482, R1101 contre 7a — gelé AVANT tout regard sur 7a (Vestigia 1283)

Date : 2026-11-12 ~02:15 CET. Entrée : TRANSCRIPTION-AVEUGLE-R1101-p1.md, SHA-256
0cbd43020c26e935ae709f77a8f07f3a191079d0d0a1bbad94c7a00b07f1bd65 (gelée, jamais modifiée).
Clé testée : key_working.md de Daniel (cyphersolver origin/main 08f07fb79), sans ajout.

## Portion tenue à l'écart
Original R1101 = Vestigia 1284 photo (103) = page 1 de la lettre, **lignes 2 à 8** (ligne 1 exclue : incipit de 7a vu
dans la fiche Vestigia). 79 mots, 306 lettres chiffrées (≥ 300, avenant du 10/11).
Hors des passages déjà alignés par Daniel : alignment_r1101.md / r1101_final_parallel.md (page finale, photo 105),
r1101_queen_parallel.md (page 2, I5654 gauche), z_control / ff_control / k (pages 2 et finale). La page 1 n'a servi
qu'à une recherche d'images par gabarit (emperor_expression_audit.md, aucun mot lu). Portion neuve, jamais mesurée.
Transparence : la portion a été choisie après avoir regardé la page 1 pour la transcrire, mais avant toute lecture de 7a.

## Référence
R = mots de 7a (copie claire contemporaine) correspondant à la portion : de l'équivalent du premier mot chiffré de
l. 2 jusqu'à celui du dernier mot de l. 8, bornes fixées par le sens et écrites dans COLLATION-R1101-p1.md avant le
calcul. 7a transcrit sans retouche, abréviations développées entre ( ) puis comptées comme lettres.

## Mesure unique
Normalisation des deux côtés : minuscules, lettres seules, j/y→i, v→u, « & »→et.
Alignement global mot à mot (Needleman–Wunsch), coût de substitution = Levenshtein(h,r)/max(|h|,|r|), coût d'un trou = 1.
S_car = Σ_{paires alignées} max(0, |r| − Lev(h,r)) / Σ_{r∈R} |r|.  S_mot = #paires h = r / |R| (rapporté, non décisif).
Témoins (500 ≥ 200) :
 C1 : 250 clés aléatoires = permutation aléatoire de l'alphabet appliquée à la chaîne aveugle (graines 1..250) ;
 C2 : 250 permutations aléatoires de l'ORDRE des mots de R (graines 1001..1250), chaîne aveugle inchangée.
Critère (BRIEF-VAGUE23 points 9-10) : S_car ≥ 0,85 ET S_car ≥ max(C1 ∪ C2) + 0,30. Une seule mesure, script
`mesure_r1101.py`, résultat consigné tel quel ; la portion est ensuite grillée.

## Comptage (règle de Daniel, ≥ 95 % des mots lus par le sens)
Unité : mot chiffré de la portion. Classes :
 - sûr : lecture = mot de 7a (normalisé), lu sur les signes ;
 - probable {x} : un seul signe diffère, sur une confusion de forme documentée (4/Δ, б/6, ω/u, ſ/7, ϑ/δ) ou une
   graphie (ct/tt, double/simple) ;
 - restitué [x] : signes partiellement lisibles, mot donné par 7a sans contredire aucune lettre sûre ;
 - irrésolu ‹…› : ni lu ni restitué, ou 7a diverge.
Trois états rapportés : (0) état de Daniel avant ce travail ; (1) lecture aveugle seule (classes jugées contre 7a,
sans relire l'image) ; (2) après collation (relecture des signes face à 7a, mot par mot, justification écrite).
« Lu » si sûrs + probables + restitués ≥ 95 % (règle de Daniel) ; sûrs + probables rapportés à part.

## Ce qui invalide
S_car < 0,85 ou marge < 0,30 → la clé n'est PAS revalidée sur portion neuve ; la collation (état 2) reste une
lecture appuyée sur un clair d'époque, à présenter comme telle (« collated with 7a »), pas comme un test de clé.
