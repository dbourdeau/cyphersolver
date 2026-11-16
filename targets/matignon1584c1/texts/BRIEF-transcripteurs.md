# Brief transcripteurs — BnF fr. 15568 f. 151r / f. 151v (chiffre de Matignon, 1584) — 16/11/2026

Travail : transcription de FORMES de signes, ligne par ligne, en étiquettes ASCII. AUCUNE valeur, AUCUNE clé.

## Interdits
- Ne lire AUCUN de ces fichiers : key_*.tsv, lecture/, mesure/, pr-matignon1584c1/, src/, daniel_tools/, HANDOFF.md,
  transcription/v_pass1.txt, transcription/dev_f151r_*.txt, ni les fichiers des autres transcripteurs (*_pass*.txt
  sauf le tien). Pas de navigateur, mail, compte, push, PR, rm. Pas d'API Anthropic.
- Écriture : UNIQUEMENT le fichier de sortie indiqué dans ta mission, sous
  /Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/matignon-1584-f151/transcription/.
- Ne rien écrire sur le disque interne (il est plein) ; ne pas créer d'images.

## Étalonnage (OBLIGATOIRE avant de commencer)
Le fichier transcription/holdout_final.txt donne, avec les étiquettes à utiliser, les lignes H1-H7 de f. 152r
et HV. Les images correspondantes : crops/P2L1a.jpg … P2L1d.jpg (= H1), P2L2a-d (= H2) … P2L7a-d (= H7),
P2HVa-d (= HV). Compare 3 ou 4 lignes signe à signe pour apprendre quelle forme porte quelle étiquette.

## Étiquettes (formes)
e ε (3 retourné) ; 3 ʒ simple ; 3h ʒ à longue queue/hampe ; s petit s/σ ; oo o-o lié ; o petit o isolé ;
n ∴ (3 points) ; X ; 4 ; 4| 4 à longue hampe barrée ; 6 ; 6^ 6 à boucle haute ; 7 ; 8 ; c ; f ; y ; z ; a ;
M m souligné ; PP ſſ ; ft ſ/ſt à boucle ; Pr ſ à grande boucle ; D losange ◊ ; Dp losange à queue ;
W Ω (oméga) ; w ω petit ; tt ; R ; Q ; P ; Y ; g3 ʒ en g ; th ⊖ (thêta barré) ; + ; ± (croix/ꝯ) ; rho ρ/ꝭ ;
T τ ; A ; L ; Lx ; Z ƶ gras ; sq □ ; ast ✱ ; tri Δ ; circ signe cerclé ; zz ≋ ; // double barre ; # ;
? illisible (un signe). Signe nouveau : invente une étiquette courte et décris-la en commentaire (# …).
Les « : » et points séparateurs ne se transcrivent PAS (sauf les 3 points ∴ = n). Groupe biffé : [entre crochets].

## Format de sortie
Une ligne d'en-tête « # … » (qui, quelle passe, quels crops), puis une ligne par ligne de cipher :
`V07: tok tok tok …` (f. 151v) ou `R07: tok …` (f. 151r). Numéro = rang de la ligne dans le fichier
crops/PV_lines.txt ou crops/PR_lines.txt (les crops sont nommés _Lnn). Doute entre deux formes :
écris la plus probable puis, en fin de ligne, `# signe k : A ou B`. Ligne ou zone sans chiffre (adresse, clair,
signature) : `# Lnn : clair/…` et ne la transcris pas.
