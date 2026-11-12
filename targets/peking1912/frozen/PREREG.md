# PREREG — lead 2465 (télégramme chinois, Pékin, oct. 1912) — figé avant toute attaque

Date : 2026-11-11. Auteur : agent Claude (Opus) pour Brice Dudout.

## Données
- Chiffré : 25 groupes de 5 chiffres (NAI Foreign Dept., Deposit Cypher 1912 Nos. 86-87, p. 6), transcription PROVENANCE vérifiée sur la capture p. 6 :
  col.1 71931 24834 09326 00170 11202 25080 60100
  col.2 88511 84203 67163 33604 97066 69466
  col.3 29492 36040 51068 51007 01032 39666
  col.4 04827 21788 25714 92706 71770 56643
- Crib (p. 9, traduction General Staff) : « Telegram understood (or for information). The President has already sanctioned the restoration of the Dalai Lama's title (B: the return) and has permitted him (B: also authorised the Dalai Lama) to proceed to the Capital. Extremely gratified at generous treatment. Quickly reply whether or not pass(ed) through. »
- Crib chinois attendu (mots probables, fixés ICI avant attaque) : 電悉 / 大總統 / 總統 / 已 / 准 / 恢復 / 達賴 / 喇嘛 / 名號 / 封號 / 回 / 來京 / 進京 / 赴京 / 感激 / 優待 / 厚待 / 速 / 覆 / 復 / 通過 / 與否 / 否.
- Table CTC : Unicode Unihan (Unihan.zip, unicode.org/Public/UCD/latest, SHA-256 4c93ea9c1f636451729a840978f1667a53886af37ba854fdcce109721c63d43e), champs kMainlandTelegraph et kTaiwanTelegraph (code télégraphique standard 4 chiffres).

## Hypothèses (dans cet ordre)
H0 lecture brute : chaîne de 125 chiffres lue en colonnes (col.1→col.4, de haut en bas) ou en lignes ; découpée en codes de 4 chiffres (décalage 0-3), ou chaque groupe 5 → 4 chiffres en retirant/ignorant une position (1-5).
H1 additif / soustraction modulo 10 (sans retenue) d'un nombre secret à 5 chiffres répété sur chaque groupe, puis un des découpages H0. Espace 10^5 × positions : sélection du nombre par score crib.
H2 relation « transparence » (Campbell 1908) : code réel = code chiffré décalé d'une relation de page (ex. 5391→5411 = +20 ; 0365→0025 = −340) — testée comme la formule de colonne H3 et comme décalage constant ±k.
H3 formule General Staff : chiffré = code ± (20,60,…,380 selon la colonne 1-10 du code), + page impaire, − page paire ; on teste l'inverse sur chaque code de 4 chiffres (page = 2 premiers chiffres, colonne = 3e chiffre, ligne = 4e), avec les deux conventions de parité.
H4 additif de longueur 4 (mod 10) sur les codes de 4 chiffres (10^4 clés).

## Score et critère de succès (fixés avant)
- Score = nombre de caractères décodés appartenant aux mots du crib (correspondance de mots ≥ 2 caractères, comptés une fois par occurrence) + bonus 0 ; on rapporte aussi la proportion de codes sans caractère.
- Contrôles : 1000 clés aléatoires (même famille d'hypothèse) et 1000 permutations aléatoires du chiffré ; p empirique = part des contrôles ≥ score du candidat.
- SUCCÈS seulement si : (a) le texte décodé est du chinois télégraphique cohérent ; (b) ≥ 3 mots du crib distincts dans l'ordre de la traduction ; (c) la clé ajustée sur la moitié du texte donne aussi des mots du crib sur l'autre moitié (validation tenue à part) ; (d) p < 0,01 contre les contrôles.
- Règle 95 % de Daniel : « sûr » = caractère contraint par le code et le sens ; « probable » sinon. Si < 95 % des caractères sont lus par le sens, publier comme lecture partielle seulement.
- Échec documenté sinon ; avec 25 groupes le problème peut être sous-déterminé (le dire).
