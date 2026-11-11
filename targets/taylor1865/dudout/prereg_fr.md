# PREREG — catalogue 681, fr. 0030 et 0031/0032 du vol. 196 (21 février 1865)
Écrit le 2026-11-12 vers 00:50 CET, APRÈS le gel de la transcription aveugle
(TRANSCRIPTION-AVEUGLE.txt, sha256 10984ebe1ae35be8f67185555b3a02d195881a4c65df1fb6a0b770e2cd330efb)
et AVANT tout essai de clé sur ces deux télégrammes.

## Corpus
- T1 = fr. 0030 (à Maury), 29 mots chiffrés, 156 lettres.
- T2 = fr. 0031–0032 (à D. W. Adams), 44 mots chiffrés, 206 lettres.
- Lettres prises dans la lecture principale de la transcription gelée (première option des [X|Y]), sans aucune correction.
- Total 362 lettres. Les clés essayées sont des phrases fixées d'avance (rien n'est ajusté sur ce corpus) :
  les 362 lettres sont donc toutes « tenues à l'écart » (held-out), ≥ 300.

## Clés (liste close)
1. COMERETRIBUTION   2. COMPLETEVICTORY   3. MANCHESTERBLUFF
4. THENAVYOURPRIDE (targets/taylor1865/continuation_key.md)   5. OURNAVYOURPRIDE (variante notée dans le même dossier)

## Chiffre et convention (fixés d'avance)
Vigenère tabula recta, P = C − K (mod 26), la clé court sur les lettres chiffrées seules, et repart à la position 0
à la première lettre chiffrée de chaque télégramme (convention établie par WAINUT et B. Payne dans targets/taylor1865).

## Mesure unique
S = moyenne, par lettre, de log10 p(lettre) sous la table de fréquences de l'anglais (table standard ci-dessous,
codée en dur dans scripts/prereg_measure.py), calculée sur le clair obtenu.
Contrôles : 200 clés aléatoires de 15 lettres (graine 681), même convention (décalage 0).
Décision, par télégramme ET sur le total de 362 lettres :
- une clé « convient » si son S dépasse les 200 contrôles (rang 1/201, p < 0,005) ;
- s'il y a plusieurs clés au-dessus des 200 contrôles, on retient celle de S maximal.
Rapporté à titre descriptif (ne change pas la décision) : S de la même clé aux 14 autres décalages.

## Lecture et règle des 95 % (Daniel)
Après la décision seulement : lecture mot à mot, corrections de glyphe permises seulement d'une lettre par place et
documentées (E/F, I/J, C/G, L/I, P/D… comme dans targets/taylor1865/NOTES.md). Un mot compte « lu » s'il donne un mot
anglais qui fait sens dans la phrase ; compte = mots chiffrés lus / mots chiffrés (unités = mots chiffrés du clerc).
Lu ≥ 95 % = read ; sinon read in part.

## Ce qui serait un échec
Aucune clé au-dessus des 200 contrôles → rien de lu, on le dit.
