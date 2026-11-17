# PREREG — piste 2933, Sachau 218 f. 231r — écrit le 16/11/2026 AVANT tout décodage

Transcription gelée : transcription.txt (SHA-256 dans transcription.sha256), 59 signes, 26 types.

## Écart au protocole (à déclarer)
Le texte fait 59 signes (< 300 car., < 150 groupes) et aucun autre document du même système n'est connu (Sachau 221
f. 20b est une écriture « en arbres », autre système ; Sachau 93 et 116 portent des tables d'autres systèmes).
La portion tenue à l'écart réglementaire est donc IMPOSSIBLE. On s'appuie sur le témoin mélangé et sur le sens.

## Clé testée (unique), figée ici, SANS ajustement
K1 « abjad en chiffres arabes » : chaque lettre est remplacée par sa valeur abjad écrite en chiffres arabes-indiens,
le zéro étant le point (٠) — système suggéré par Sachau (« Ziffern ») et par l'alphabet « de Simon » (lettres notées
par des chiffres, Sachau 1899 p. 803). Valeurs des signes, attribuées par la seule forme du chiffre :
I=١→ا ; R=٢→ب ; W=٣→ج ; E=٤→د ; F=۴→د ; O=٥→ه ; L=٨→ح ; N9=٩→ط.
Le point rouge sous le premier F (L1) → ×10 : ٤٠ → م. Tous les autres signes : inconnus (non décodés).
Nombre de valeurs ajustées après coup : 0 (aucun ajustement permis).

## Mesure unique
Score = moyenne du log-probabilité des bigrammes de lettres adjacentes toutes deux décodées, à l'intérieur d'un même
groupe, sous un modèle de bigrammes arabes (corpus de référence : texte arabe du Coran, tanzil simple-clean, réduit à
l'alphabet karshuni de 22 lettres : ث→ت, خ→ك, ذ→د, ض→ص, ظ→ط, غ→ع, ة→ه, ى→ي, hamzas→ا ; lissage add-1).
Témoins : 200 clés aléatoires (graine 2933) qui donnent aux mêmes 8 classes de signes 8 lettres tirées au hasard dans
les 22 (sans remise ; le point rouge garde ×10 sur la valeur tirée si elle est une unité, sinon inchangée).
Seuils écrits avant : K1 est « soutenue » seulement si score(K1) ≥ meilleur témoin ET si au moins 3 groupes décodés
entièrement forment des mots arabes ou syriaques attestés, jugés par le sens. Sinon : K1 rejetée, texte « non lu ».
Une seule exécution de tools/measure.py. Le résultat est écrit tel quel dans MEASURE.txt.
