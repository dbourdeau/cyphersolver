# PREREG B — mesure unique sur la portion tenue à l'écart (gelé AVANT décodage de la portion), 16/11/2026

Portion (PREREG-A, d17c48e5…f2b7) : f. 152r entier (H1-H7) + dernière ligne de f. 151v (HV), 302 signes.
Transcription arbitrée : transcription/holdout_final.txt (ece481a5aca9abde8d4a1c9013c4cf21f0c72fb2e2d6c1d9d7deeded68c8acde),
deux passes (holdout_pass1.txt a3b82a95…83e6, holdout_pass2.txt 170d12d7…343a), 4 désaccords tranchés sur l'image.
Aucune valeur de clé n'a été appliquée à la portion avant ce gel.

Clé figée : key_frozen.tsv (913f766dcd5c42c6852410b6569028c8356f094c04bb31c3c7de123c4e17461b) = table de Tomokiyo
(« Matignon's Cipher-1 ») + valeurs établies sur le DEV f. 151r (ſſ = t, 6^ = m, ꝭ = b, ℊʒ = z, ꝺ à queue = « que »,
4 à hampe = q, θ barré = « le roy »). Signe sans valeur : Pr (ſ à boucle pleine) → « ? ». Nuls : ≋, //.

Scripts : scripts/decode.py (9206a6a0…97f0), scripts/run_measure.sh (9ee2e816…20b0),
mesure de Daniel targets/matignon1586c3/f276/scripts/measure.py (94078041…4d15, origin/main du 16/11, lang/lm.py e97a9483…62b5,
lang/corpora.py 8c9fb1da…062c), modèle fr-1600-letters, mincount 20.

- Statistique M : part des signes de la portion LUS selon la règle de Daniel (suite de ≥ 3 mots du lexique totalisant
  ≥ 10 lettres ; un « ? » est un signe de contexte jamais compté lu). Dénominateur = signes non nuls décodés.
- Témoins : 200 clés permutées (permutation des valeurs de lettres, graine 2, celles de measure.py, argument n = 200).
- Seuils fixés d'avance : RÉUSSITE si M ≥ 0,85 ET M ≥ (max des 200 témoins) + 0,30. Sinon ÉCHEC.
- Une seule exécution (scripts/run_measure.sh). Le résultat est copié tel quel dans HANDOFF.md. La portion est ensuite
  grillée. Aucune correction de clé ni de transcription après la mesure ne change le résultat déclaré.
