# PREREG — lead 1359 (NAI External Affairs, Sikkim (Political) 1930, File 5-P) — figé avant attaque

Date : 2026-11-11. Agent Claude (Opus) pour Brice Dudout.

## Données
- A. pp. 14-15 : deux télégrammes Nankin → « Dalai Buddha, Lhasa », 155 + 75 groupes de 4 chiffres (OCR du site vérifié sur captures ; douteux : p.14 « 6615 » (curseur), p.15 « 7308 » (curseur)).
- B. code-mots de 10 lettres (CVCVCVCVCV), Lhassa → Nankin etc. : p.11 (Chiang, 22/9/1930), p.12 (Ma Fuxiang, 22/9/1930), p.9 (Singchi c/o Thinyik Calcutta), pp.22-23 (13/10/1930).
- Crib p.18 (résumé britannique) : Chiang a reçu la lettre du Dalaï-Lama par Kun Kanpu ; se félicite de son soutien au gouvernement central ; la Chine n'a pas été « honest or considerate » ; souhaite l'unité complète ; salutations de Ma Fuxiang et Kun Kanpu.
- Table CTC : Unihan (unicode.org, SHA-256 4c93ea9c1f636451729a840978f1667a53886af37ba854fdcce109721c63d43e), kTaiwanTelegraph puis kMainlandTelegraph.

## Partie A (chiffres)
- H-A0 : CTC standard en clair, ordre de lecture en lignes (comme tapé). Pas de clé.
- Mots attendus (crib chinois fixé ici) : 達賴 / 喇嘛 / 蔣 / 中正 / 馬福祥 / 貢覺仲尼 (Kun Kanpu = 貢覺仲尼 / 貢覺 / 堪布) / 中央 / 誠意 / 統一 / 擁護 / 函 / 悉 / 電.
- Succès : texte chinois cohérent de bout en bout ; ≥ 3 mots du crib ; contrôles : 1000 permutations des groupes et 1000 additifs aléatoires 4 chiffres (score crib + part de bigrammes de mots attendus) ; p < 0,01.
- Si H-A0 échoue : H-A1 additif 4 chiffres constant ; H-A2 formule General Staff (±20…380 selon colonne, parité de page).

## Partie B (code-mots)
- Hypothèse principale H-B1 : un mot de 10 lettres = 2 × 5 lettres ; chaque demi-mot (CVCVC… en pratique CVCVC/VCVCV selon la position) code un nombre CTC de 4 chiffres par un alphabet de syllabes CV (une syllabe = un chiffre ou une paire de chiffres). Variantes : H-B2 table de code commerciale (non disponible → non testable, à documenter) ; H-B3 lettres → chiffres par position (C = chiffre parmi 20 consonnes ≡ mod 10, V = …).
- Apprentissage : p.11 et p.12 (+ pp.22-23 si lisibles) avec le crib.
- TENUE À L'ÉCART désignée maintenant : **p. 9 (Singchi c/o Thinyik)**, jamais regardée pendant l'ajustement. Mesure UNIQUE : part des demi-mots de p.9 donnant un code CTC valide et un caractère d'une liste fréquente (fixée par le script avant mesure), comparée à 1000 clés permutées ; succès si ≥ 0,80 et marge ≥ 0,30 au-dessus du max des contrôles, ET texte lisible.
- Si aucune clé : documenter l'échec, la structure observée et la sous-détermination.

## Règle 95 % (Daniel)
« Read » seulement si ≥ 95 % des caractères lus par le sens ; sinon « read in part ». Sûrs / probables / restitués / irrésolus comptés.
