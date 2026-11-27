# PREREG main 2 — Hautefort 1584, n° 2841 (BnF fr. 15568), clé Fable lot 15 — 16/11/2026

Gelé AVANT tout recadrage, agrandissement ou lecture de la portion H (CHOIX-PORTION.md, sha 7e5f386f… puis addendum 536383c2…) :
**H = fr. 15568 f. 207v** (Gallica btv1b9063927n, vue 216, moitié gauche, x < 0,42). H n'a jamais été envoyée à Fable (MANIFEST du
lot 15 : découpes de la vue 216 limitées à x ≥ 0,445 = f. 208r) ni regardée au-delà de la vignette 700 px des étiquettes.

## Clé (figée, telle que proposée par Fable, sans retouche)
key_main2_fable.json = KEY-PROPOSAL-MAIN2.json du run fable-api/lots/lot15/hautefort-main2/out/20261116-180543 (coût 3,46 USD).
Valeurs multi-lettres (que, vous, qui, par, sieur, roi, nauarre) = unités fixes ; « ? » = code de nomenclateur déclaré = coupure de
mot hors dénominateur. Les codes de contexte « +e » et « +m » de la clé ne seront jamais employés dans la transcription de H.

## Transcription de H (deux passes, par l'agent coordinateur, après ce gel seulement)
- Codes de formes et règles de GLYPHS-MAIN2.md (gelé ici). Toute croix = « + » (pas de « +e »/« +m », qui sont des codes de
  sens) ; 6 / b, q / Q, 8 / D, ^ / ^! / th distingués à l'œil selon GLYPHS-MAIN2.md, sans recours au sens ; illisible = « ? » ;
  forme hors inventaire = « ? » ; 1z = 12, 15, 17, 16, 14 = un signe ; signes sous glose d'époque retirés ; clair exclu.
- Portion mesurée : lignes entières de H depuis la première ligne chiffrée, jusqu'à la première ligne qui porte le total à
  ≥ 300 signes (choix par position, pas par contenu). Si la page entière a < 300 signes : page entière, mesure faite, et la
  sous-taille est signalée.
- Passe 1 sur bandes A, passe 2 sur bandes décalées sans regarder la passe 1 ; écarts tranchés sur l'image agrandie, en écrivant
  la règle de forme appliquée. Fichier mesuré : H_f207v_final.txt (lignes « Lnn: … »), SHA consigné avant la mesure.

## Mesure (une seule exécution)
`python3 tools/measure_main2.py key_main2_fable.json H_f207v_final.txt lex/lexique-fr-cyphersolver.json lex/fr-henri4.txt
lex/fr-1520s-diplomatic.txt` : measure_v4 généralisée (« x|y » tranché au lexique ; « ? » de clé = coupure hors dénominateur ;
signe absent de la clé ou « ? » transcrit = lettre non couverte). Lexique et métrique identiques à PREREG-v3/v4 (mots ≥ 4 lettres
lexique fréq ≥ 10 ∪ corpus fréq ≥ 3, liste fermée de mots outils ; normalisation accents, ſ→s, v→u, j/y→i).
Témoins : 200 permutations des valeurs entre signes à une lettre et signes « x|y », graine 20261116.
**Barre : score ≥ 0,85 ET score ≥ meilleur témoin + 0,30.**

## Calibrage (apprentissage seulement, transcription Fable de 207r, 208r, 208v, 209r, 2 996 signes)
Clé gelée : 0,9218 vs témoins max 0,4974 (moy. 0,3508) ; même transcription, croix toutes « + » (règle ci-dessus) : 0,9159 vs 0,4977.
Témoin négatif connu : clé dégénérée du recuit Opus sur 207r l. 1-18 : 0,865 vs 0,700 (échoue à la marge).

## Empreintes (PREREG-main2.sha256)
key_main2_fable.json 3d3186f3… ; GLYPHS-MAIN2.md c38dbc54… ; tools/measure_main2.py 2bff2f77… ; CHOIX-PORTION.md 536383c2… ;
lexiques : identiques à PREREG-v4.sha256.
