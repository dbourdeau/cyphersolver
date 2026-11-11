# PREREG — fable-c05-validation — ronquillo-1646 (n° 748), D.107 (L. Ridolfi, Rome 8/5/1646) — 11/11/2026, agent Opus (validation)
Écrit et haché AVANT tout décodage de la page 5 (réserve H, 99 groupes). Modèle : godoi-paraguay-1878/fable-c03/PREREG-FABLE-C03.md.

## Antériorité de la réserve (vérifiée avant ce PREREG)
- HANDOFF : C01, C02, C03 et cribs-2026-11-05 tiennent la p. 5 à l'écart (« Réserve p. 5 intacte, aucune mesure ») ; c03/sn.txt, sd.txt = 1 313 jetons = p. 1–4 ; c01 (PAGES défaut 1234) ; c02/seg.py ne fait que segmenter les images (transcription), sans décodage.
- Fable (MANIFEST.json du run 20261111-103319) : D107_p1–p4 + atlas/diff p1–p4 seulement ; aucun fichier p5 envoyé. La p. 5 n'a été décodée par personne.

## Objet
Clé PROPOSÉE par Fable 5.2 (Anthropic), lot 2 API, run 20261111-103319 : chiffre italien numéroté — 20–24 = a e i o u ; 25–44 = alphabet a … u (28 d, 30 f, 35 m restitués) ; syllabaire par séries (49–53 b, 54–58 m, 59–63 l, 64 che, 65–69 n, 70–74 d, 75–79 t, 80–84 g, 85–90 f sans 88, 91–95 z), 97 che, 98 chi ; nomenclateur 100–243 ; X = ponctuation ; point suscrit = redoublement.

## Objets gelés (SHA-256 dans FREEZE.sha256)
- KEY-PROPOSAL.json, KEY-PROPOSAL.tsv (copies inchangées), ctrl.py et load.py de Fable (copies inchangées, pour mémoire).
- scripts/decode.py : décodeur déterministe écrit ici, n'appliquant QUE `lettres_et_syllabes` de KEY-PROPOSAL.json (aucune valeur nouvelle ; codes 3 chiffres = [nnn] inconnus, aucune conjecture du nomenclateur appliquée ; 2 chiffres hors clé = [nn?]). Testé sur p. 1–4 : sortie IDENTIQUE à DECODE-brut-p1-4.txt de Fable (86 lignes, au séparateur final près).
- scripts/cov.py (métrique et témoins), scripts/calib.py + calib.out (calibration p. 1–4), scripts/mesure.py (mesure unique, vérifie le gel).
- transcr/D107_p1–p5.txt : copies de working/transcr_v1 (transcription v1 gelée en C02, SHA identiques à working/transcr_v1/SHA256.txt ; p5 = 1f2ef733…).
- lexique-it-cyphersolver.json : copie inchangée de PISTES-AUTO/fable-api/lots/lot2/_communs/ (f4d2f270…), le lexique utilisé par Fable.

## Mesure unique (décisive)
COV = part des lettres décodées de la p. 5 couvertes par des mots ≥ 4 lettres du lexique italien cyphersolver (entrées de fréquence ≥ 3, v→u, j→i, accents ôtés), couverture maximale par segment ; X, codes 3 chiffres et codes hors clé = coupures ; points suscrits ignorés ; alternative « a/b » = première lecture. C'est exactement la métrique de ctrl.py de Fable (reproduite : p. 1–4 in-sample 0,876).
Pourquoi pas une mesure « caractères justes » : la p. 5 n'a ni déchiffrement d'époque ni clair parallèle ; aucune vérité terrain par caractère n'existe. COV est la mesure déjà employée (godoi fable-c03), complétée par le contrôle de sens.

## Témoins (calculés sur la p. 5 dans la même exécution)
- 200 clés mélangées (random.Random(5)) : permutation des valeurs entre codes, lettres entre lettres et syllabes entre syllabes (fonction shuffled() de ctrl.py) ;
- 200 mélanges des groupes décodables de la p. 5 entre leurs positions (random.Random(5)), coupures laissées en place, clé proposée.

## Seuil — calibré AVANT, sur p. 1–4 seulement (scripts/calib.out)
- In-sample p. 1–4 : clé 0,876 ; 200 clés mélangées max 0,388.
- 51 fenêtres de 99 groupes (taille de p5, pas 24) : COV clé min 0,783, p10 0,815, médiane 0,861 ; écart à max(clés mélangées) min 0,256, médiane 0,354 ; écart à max(mélanges de groupes) min 0,098, médiane 0,225 (le mélange de groupes est un témoin fort : les codes syllabiques donnent des syllabes italiennes quel que soit l'ordre).
- La règle maison (≥ 0,85 ET ≥ max témoin + 0,30) rejetterait 44/51 fenêtres in-sample (18/51 sur le seul seuil 0,85 ; seules 7/51 ont un écart ≥ 0,30 au meilleur des témoins) : elle n'est pas applicable à 99 groupes. Règle calibrée retenue :
  - C1 : COV ≥ 0,75 (marge sous le minimum in-sample 0,783, la p. 5 étant hors échantillon) ;
  - C2 : COV ≥ max(200 clés mélangées) + 0,25 (minimum in-sample 0,256) ;
  - C3 : COV ≥ max(200 mélanges de groupes) + 0,08 (minimum in-sample 0,098).
  - **Mesure VALIDÉE si C1 ET C2 ET C3** ; PARTIEL si C1 et une seule de C2/C3 ; ÉCHEC sinon.

## Contrôle de sens (pré-enregistré, décisif en second)
- S1 — La p. 4 se termine (lecture Fable) par « ma con le medesime parole che mi sara data subito la … » : le début de la p. 5 doit fournir un complément nominal italien de « la » (ex. risposta, risolutione…) qui ferme la phrase de façon grammaticale.
- S2 — La p. 5 doit se lire en italien suivi : au moins 3 lignes consécutives lisibles par le sens sur la sortie brute, avec au plus les classes de relecture déjà listées dans EMENDATIONS.tsv (confusions d'un chiffre 1/2, 2/3, 3/4, 3/7, 3/9, 6/8, 7/8, 0/6, 1/5, 1/8 ; groupe omis), chaque relecture justifiée et notée « restituée ». Une formule de fin de lettre est attendue mais n'est pas exigée.
- Jugement fait UNE fois sur la sortie brute de mesure.py.
- Verdict final : VALIDÉ = mesure VALIDÉE ET S1 ET S2. Mesure VALIDÉE mais sens non OK → « à revoir ».

## Règles
Une seule exécution de scripts/mesure.py ; sortie brute recopiée telle quelle dans RESULTAT.md ; aucune modification de clé, décodeur, lexique ou transcription après. Si validé : décompte façon Daniel (sûrs / probables / restitués / irrésolus ; ≥ 95 % = lu) sur p. 1–5. Images jamais republiées. Crédit : clé proposée par Fable 5.2 (Anthropic), validation Opus.
