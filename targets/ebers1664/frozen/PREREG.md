# PREREG — ebers-lilienthal-moscou-1664 (leads Daniel 2315 + 2316), écrit le 10/11/2026 (agent Opus 5.5)
Écrit APRÈS lecture de quelques paires sur R0003225 image 106 (et un coup d'œil à 108), AVANT toute transcription des portions H.

## Antériorité (10/11/2026, gh api dbourdeau/cyphersolver)
Rien sur Ebers / Lilienthal / Muscovitica / R0003225 / R0000814 dans targets/, branches, PR ouvertes (#380, #381) ni commits
depuis le 05/11 (ceux du 10/11 = hopken1739/1740, Höpken, Constantinople). Seules mentions : research/sweep_2026-11_riksarkivet_west,
research/vetting_2026-11 (n09 : verdict « read », glose d'époque partout). Pas de doublon en cours.

## Systèmes
- E = code d'Ebers (R0003225, Diplomatica Muscovitica 3/b/602) : substitution littérale à 2 chiffres (15-95), homophones probables.
- L = code de Lilienthal (R0000814, Diplomatica Muscovitica 1/36/82) : 2-3 chiffres (jusqu'à ~390), nomenclateur probable.

## Clés (tirées des paires chiffré/glose)
- K_E : pages de clé R0003225 images 106 et 108 seulement. Gelée (KEY-EBERS.tsv + sha256) avant transcription de H_E.
- K_L : pages de clé R0000814 images 38 et 47 seulement. Gelée (KEY-LILIENTHAL.tsv + sha256) avant transcription de H_L.

## Portions tenues à l'écart (choisies ici, avant de les regarder de près)
- H_E = R0003225 image 138 : les 160 premiers groupes chiffrés en ordre de lecture (page gauche puis droite, lignes de haut en bas),
  clair mêlé exclu. Si moins de 160 groupes, compléter avec image 140.
- H_L = R0000814 image 42 : les 160 premiers groupes chiffrés en ordre de lecture ; si moins, compléter avec image 43.
- Transcription des groupes seuls (codes), gel H_*-CHIFFRE.txt + sha256 ; ENSUITE lecture de la glose d'époque au-dessus de ces
  groupes (G_*-GLOSE.txt + sha256), sans décodage par script entre les deux ; ensuite décodage par script.
- Limite : la glose est sur la même image ; je la vois en transcrivant les chiffres. Biais possible, signalé.

## Mesure (une par système, une seule fois)
car = égalités alignées Smith-Waterman (+1/-1/-1) entre décodage de H (lettres normalisées : minuscules, j→i, v→u, w→u, y→i,
ß→ss, umlauts → voyelle + e retiré : ä→a ö→o ü→u ; groupes hors clé = « ? » non concordant) et la glose normalisée,
divisé par le nombre de positions décodées de H (lettres produites + « ? »).
Témoins : 200 permutations des valeurs de K entre les codes présents dans H (graine 1664 / 1666). Marge = car − max témoins.
car ≥ 0,85 ET marge ≥ 0,30 → VALIDÉ ; marge ≥ 0,30 seule → PARTIEL ; sinon ÉCHEC. H grillée après mesure.

## Ensuite
Inventaire des pages chiffrées (glosées / non glosées). Partie sans glose = vraie lecture nouvelle (au compte de Daniel).
Aucune PR ni issue : PR-PREP.md si publiable. Riksarkivet = PDM (crédit « Riksarkivet, SE/RA/… , bildid »).
