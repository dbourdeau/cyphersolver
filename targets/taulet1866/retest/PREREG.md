# PREREG — re-test unique de la clé taulet-1866 (catalogue Bourdeau 2444) sur portion NEUVE
Écrit le 2026-11-10 13:18 CET, AVANT toute transcription des nombres de N.94 et tout décodage.
Règle : [consigne interne du contributeur, avenant du 10/11/2026].

## Clé gelée (aucun changement)
- KEY.tsv SHA-256 0f174dd7fb30fde05ba82ba56277e4f8d2be6244a71553ea9347f4fcb7db8b18 (identique au gel du 09/11 et à la PR #376).
- scripts/measure.py SHA-256 cc27e1cf5c7ba0370909d1b569cf00fe50dd457ed84b9bd5a3261d60044628eb (inchangé, témoins graine 2444).
- Lexique es.json.gz SHA-256 0c49f0d49d93f8531fef0ea5f32419e302a3a1fecb196735f108588c3d1368df.
- Ancienne portion H (N.99 S33) grillée : jamais recalculée.

## Matériel neuf (jamais vu pendant la construction de la clé)
AHN, DIVERSOS-COLECCIONES,193,N.94, PARES 5855640 (oficios reçus par le colonel Taulet, janv. 1866), images [stockage privé, non publié]. Contrôle de système (étape 1, recadrages seulement) : vues 43 et 87 = nombres à 2 chiffres
reliés par tirets/« = », valeurs 10-92 (11, 29, 88, 21, 61, 64, 92, 81…), même système homophonique que N.99, en partie
entremêlés de mots clairs (le clair inséré fait partie du message, il ne le double pas). Aucune version claire ni brouillon
du même texte à côté (vues voisines 42, 44, 77, 79, 86, 88 vues en vignette : autres lettres / adresses / verso).
Noms vus en passant (fuite déclarée, sans effet : la clé est gelée) : quelques mots clairs des vues 43 et 87.

## Portion tenue à l'écart H (fixée maintenant)
- H = TOUTES les suites de nombres des vues 43, 87 et 78 de N.94, dans cet ordre, puis, si le total est < 300 nombres,
  aussi celles de la vue 26. Une suite = nombres consécutifs entre deux passages clairs (protocole P01).
  - 5855640/43.jpg 9b06ec440a4e2b461800bbb02bc57dc3b2c9330c34f66dedd4cf79f5d921eabf
  - 5855640/87.jpg e57e2b71ed3f8205d680feeb78c7881e68752a61e20f4d934e9f09bbff9933dd
  - 5855640/78.jpg 3580af49429e2430441d02046c2af7d6f816e3bbae6e03c65db4fd442f91a791
  - 5855640/26.jpg aacecba084c123c8beca5539f30166d498702cba61dc28f5f91dbcb82262ac56 (seulement si < 300)
- Taille exigée : ≥ 300 caractères chiffrés (= nombres). Si même avec la vue 26 H < 300 : mesure NON jouée, H reste vierge.
- Nombre absent de la clé → « ? » non couvert (pénalise, comme en P01).

## Ordre des opérations
1. transcription.txt (format P01, toutes lignes partie H, une passe, sans lecture) → SHA-256.
2. decode.txt = décodage par la clé gelée → SHA-256.
3. clair.txt = clair établi par le sens (fiche sûrs / probables / irrésolus) → SHA-256.
4. UNE mesure : python3 measure.py retest-1011/transcription.txt KEY.tsv es.json.gz --part H → MESURE.txt, SHA-256.
   (Mesure automatique indépendante du clair établi ; le clair sert à la fiche de lecture.)

## Critère (inchangé)
VALIDÉE si car ≥ 0,85 ET car ≥ meilleur des 200 témoins + 0,30 (ET H ≥ 300 nombres). Sinon PARTIELLE.
Une seule mesure ; portion grillée ensuite, jamais remesurée.
