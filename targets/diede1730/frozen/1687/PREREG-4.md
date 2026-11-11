# PREREG-4 — précision du 11/11/2026, écrite APRÈS gel de KEY.tsv (sha256 4d83b4f7…) et AVANT toute ouverture de H (033-036)
Constat sur les sources de clé (056, 027) : la glose d'époque est écrite SOUS la ligne de chiffres qu'elle traduit (au-dessus de la
suivante), et en texte continu, pas groupe par groupe. Le système est une substitution homophonique de LETTRES (≈ 1 groupe / lettre)
avec quelques codes-mots (Chur Mayntz, Chur Cölln…).
- H-CHIFFRE.txt : inchangé (160 premiers groupes, 033→036, page G puis D, des séries marquées G par le transcripteur).
- G-GLOSE.txt : TOUTE la glose interlinéaire des passages chiffrés (entre deux textes clairs) qui contiennent ces 160 groupes, dans
  l'ordre de lecture, plus la glose écrite immédiatement sous la dernière ligne retenue. Aucune autre glose.
- Mesure : scripts/measure.py (sha256 dans KEY.sha256), inchangée sur le fond : codes « douteux » = « ? », « · » = vide,
  Smith-Waterman, car = égalités / positions décodées, 200 témoins graine 1730, critère car ≥ 0,85 et marge ≥ 0,30.
- Hann. 92 Nr. 1149/1 (copies de Londres) : hors de H et hors de la clé.
