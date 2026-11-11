# RESULTAT — fable-c05-validation — D.107 (Ridolfi, Rome 8/5/1646) — 11/11/2026, agent Opus
PREREG.md SHA-256 ce607b24705b4ed2b6106e5a77395f3832429bdcae8c2eae902a42a8f9c2691d (FREEZE.sha256, gel 10:54:20 CET, avant toute exécution de mesure.py).
Exécution UNIQUE de `python3 -I scripts/mesure.py` (sortie aussi dans scripts/mesure.out). Sortie brute, telle quelle :

```
gel verifie (FREEZE.sha256)
--- decodage brut p5 (cle gelee, aucune correction) ---
5.01	s·c·r·i·t·tu·r·a·r·i·chi·e·s·ta·. 
5.02	e·t·i·o·no·n·u·o·r·e·i·che·c·o·n
5.03	la·lu·n·g·h·e·[47?]·za·. ·di·s·p·e·r·a
5.04	to·bu·g·li·o·ne·s·i·a·c·o·r·da·s·e·c
5.05	o·n·li·[121]·. ·p·o·i·che·i·l·[108]·ma·za
5.06	r·i·no·s·e·n·p·r·e·g·li·fa·r·a·do
5.07	p·i·a·r·le·o·fe·r·b
p5 : 99 groupes, 120 lettres decodees
COV cle proposee = 0.817
200 cles melangees : max 0.487 moy 0.251
200 melanges des groupes : max 0.600 moy 0.415
C1 COV>=0.75 : True ; C2 COV>=maxcles+0.25 (0.737) : True ; C3 COV>=maxmelanges+0.08 (0.680) : True
MESURE : VALIDE
```

## Verdict de la mesure
C1 (0,817 ≥ 0,75), C2 (0,817 ≥ 0,737), C3 (0,817 ≥ 0,680) : **MESURE VALIDÉE**. Écarts : +0,330 sur le meilleur des 200 clés mélangées, +0,217 sur le meilleur des 200 mélanges de groupes (in-sample, fenêtres de 99 groupes : médianes 0,354 et 0,225 ; COV 0,817 ≈ p25 des fenêtres in-sample).

## Contrôle de sens (jugé une fois, sur la sortie brute)
- S1 — OK. Fin de p. 4 « ma con le medesime parole che mi sara data subito la » + début de p. 5 « scrittura richiesta . » → « …che mi sarà data subito la scrittura richiesta. » : complément nominal de « la », phrase fermée par X.
- S2 — OK. Lignes 5.01–5.06 lisibles sans aucune relecture : « et io non uorei che con la lunghe[47]za disperato Buglione si acordase con li [121] . poi che il [108] Mazarino senpre gli fara dopiar le ofer[b] ». Sens suivi avec la p. 4 (négociation avec Bouillon, « negotio di Buglione », Ugonotti) : Ridolfi craint que, avec le temps, Bouillon désespéré ne s'accorde avec les Français, Mazarin lui doublant toujours les offres.
- Seuls points hors clé : 47 (hors clé, non attesté p. 1–4 ; « lunghezza » impose z) et le dernier groupe 26 (b) pour 76 (te) — « oferte » ; aucun n'est nécessaire à S1/S2.
- Confirmation indépendante hors échantillon : les deux points suscrits de la p. 5 (41' dans uor'ei = vorrei, 42' dans acordas'e = accordasse) tombent sur une géminée écrite simple, comme la règle de Fable le prévoit.

## VERDICT FINAL : **VALIDÉ** (mesure VALIDÉE ET S1 ET S2).
Aucune modification de clé, décodeur, lexique ou transcription après la mesure. Lecture de p. 5 : LECTURE-p5.txt.

## Décompte façon Daniel, p. 1–5 (scripts/decompte.py → decompte.out ; classes de Fable pour p. 1–4, d'Opus pour p. 5)
```
p1 {'sur': 89, 'restitue': 7, 'probable': 7} 103
p2 {'sur': 96, 'probable': 7, 'restitue': 3, 'irresolu': 1} 107
p3 {'probable': 6, 'sur': 87, 'irresolu': 4, 'restitue': 3} 100
p4 {'sur': 83, 'restitue': 6, 'probable': 4} 93
p5 {'sur': 23, 'restitue': 2, 'probable': 3} 28
TOTAL {'sur': 378, 'restitue': 21, 'probable': 27, 'irresolu': 5} 431
lu par le sens (surs+probables+restitues) = 98.8 % ; surs seuls = 87.7 % ; surs+probables = 94.0 %
```
- Mots : 431 (dont 26 codes de nomenclateur). Sûrs 378 (87,7 %) ; probables 27 (6,3 % ; dont 21 valeurs de nomenclateur conjecturées par le sens : 107 Gran Duca ×6, 121 Francesi ×5, 126 V.E. ×3, 114 Duca ×3, 101 Sua Santità ×2, 100 Sua Maestà, 108 Cardinale) ; restitués 21 (4,9 % ; 19 émendations de EMENDATIONS.tsv p. 1–4 + 2 en p. 5) ; irrésolus 5 (1,2 % : codes 103, 110, 115, 116, 136).
- **Lu par le sens : 98,8 % (≥ 95 % → LU)**. Sûrs + probables seuls : 94,0 %.
- Réserves : les classes de p. 1–4 sont celles de Fable (sortie brute reproduite à l'identique par decode.py, mais classement non réaudité mot à mot) ; 47 et 28/30/35/58/69/79/84/92–95 restent des valeurs restituées (non attestées).
