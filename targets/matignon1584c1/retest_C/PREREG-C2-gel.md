# PREREG C2 — gel de la clé et de la transcription de la portion C, AVANT tout décodage de C (16/11/2026)

- Portion C : transcription/holdout_C_final.txt (f. 151v V01-V09, 377 signes ≥ 300, arbitrée sans clé)
  sha256 7606fff8edfc5fbf85528c8017ea54756ee464723709769b8b2abf24717f3023
- Clé figée : key_C.tsv = key_frozen.tsv + corrections/ajouts établis sur le DÉVELOPPEMENT seul (f. 151r p1/p2,
  f. 151v V10-V29 p1/p2) : 6^=p (et non m : « promptement », « s'y employeroient »), w (ω)=l (« le chasteau », « ilz »),
  lam (λ)=l, circ=o (« commande », « voyoient »), hs (#)=a (« au », « auez »), dx=s (« laisser », « aussi »),
  A=a, ast=a, tri=b, Z=i, T=d, o=o, sl et / = nuls. Y, 4|, Pr, +tt inchangés (valeurs non tranchées).
  sha256 ff5f12214ff0d2ad370fc6578b3c1ecdb2d4d05e8b239c29380ba234bae35b90
- Scripts : scripts/decode.py sha256 9206a6a0c7548b15cb2af759cb35d487b04b2b46355af5c8a0e76a73509097f0 ;
  scripts/run_measure_C.sh sha256 127ef30c0d69aa599540047b7082b4399f3516ba2bebc43ef391bbc60fe22cd6
- Statistique, témoins, seuils : ceux de PREREG-C (measure.py de Daniel, fr-1600-letters, mincount 20, 200 clés
  permutées, graine 2) ; RÉUSSITE si M ≥ 0,85 ET M ≥ max témoins + 0,30. Une seule exécution ; sortie brute
  mesure_C/RESULTAT.txt. La portion C est ensuite grillée.
