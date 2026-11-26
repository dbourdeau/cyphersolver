# PREREG-2 — message clandestin d'Auschwitz du 4/9/1944

Rédigé le 27/11/2026 avec l'accord de Brice, transmis par le coordinateur. Il est haché (PREREG-2.sha256) AVANT d'exécuter `essais/mesure2.py`. La mesure est unique.

## Ce qui a été fait avant ce PREREG (déclaration)
1. **Mesure 1** (PREREG.md) : ÉCHEC. Les groupes G20–G39 y servaient de validation ; ils sont désormais **grillés**.
2. **Exploration sur les groupes grillés G20–G39 seulement** (lecture et calcul de fréquences, sans chercher de mots dans G1–G19). Plusieurs mots apparaissent :
   - G22 = G34 = 1-3-12-2-11-1-2, donc « kontakt » (n=12, a=11) ;
   - G38 « materjały » (orthographe d'avant 1936) et G39 « wybuchowe » ;
   - G26 « przez », G30 « ogrodnika », G37 « prasę ».
   On en tire l'ordre suivant : k1 t2 o3 s4 i5 ę6 w7 p8 e9 d10 a11 n12 u13 m14 c15 ł16 r17 z18 j20 l22? ż23 g26 y27 h28 ó30.
   C'est exactement l'ordre de **première apparition des lettres distinctes** dans le chant, si on lit « A cał**e**m sercem ». Avec la graphie « całym », le y tombe à 17 : c'est la clé F2 de la mesure 1, qui a échoué. La suite du texte place f19 (ufa), j20 (jemu), ś21 l22 (Śmiele), ż23 (może), b24 ń25 (obrońcę), g26 (Boga) et y27 (przypadnie). Les valeurs h28 et ó30 ne viennent pas du chant : on les tire des groupes grillés (« wybuchowe », « Józka »).
3. **Contamination partielle de G1–G19, à déclarer.**
   - Pendant la mesure 1, j'ai vu leurs déchiffrements avec 6 clés fausses. F2 est la plus proche : elle coïncide avec la nouvelle clé de 1 à 16.
   - Pendant l'exploration, j'ai aussi fait quelques conjectures mentales sur G10 (4-4 « SS »), G15, G8, G13, G9, G4 et G1, avec des valeurs différentes de la clé ci-dessous. Aucune de ces conjectures n'a servi à fixer la clé : elle vient du chant et des groupes grillés.

## Portion neuve
- Elle comprend **G1–G19** : 19 groupes et 88 nombres, dont 16 groupes de longueur ≥ 2.
- **Elle est trop petite pour la règle de Daniel** (au moins 300 caractères). Le texte chiffré ENTIER (183 nombres) ne fait pas 300 caractères non plus. La validation statistique ci-dessous reste possible sur 88 nombres. Pour la lecture finale, on comptera donc les 95 % sur le message entier, clair compris (plus de 300 caractères), en séparant les parties chiffrées. Si le coordinateur refuse ce mode de calcul, la lecture sera publiable seulement comme « lecture partielle expliquée ».

## Famille de clés (liste close, 5 variantes)
**Règle de construction.** On parcourt le chant (Kochanowski, Ps. 91, première strophe). Chaque lettre distincte reçoit, à sa première apparition, le numéro suivant. Les digrammes ne forment pas de signe à part. Les valeurs k1 t2 o3 s4 i5 ę6 w7 sont fixes, car attestées.

Textes de la strophe :
- **K1** : « Kto się w opiekę poda Panu swemu, A całem sercem szczerze ufa jemu, Śmiele rzec może: mam obrońcę Boga, Nie przypadnie na mię żadna trwoga. »
- **K2** : la même strophe avec « całym ». Cette clé a déjà été testée (F2).
- **K3** : version chantée avec « całem », « odda » et « zaufa ».
- **K4** : « poddał Panu swemu, A całem… ». Le ł apparaît alors avant n.
- **K5** : K1 avec la numérotation de la citation de Kłodziński (p=9 au lieu de 8). Toutes les valeurs à partir de p sont décalées de +1.

Dans toutes les variantes, h28 et ó30 sont ajoutés quand le numéro est libre ; ils viennent des groupes grillés.

**Choix de la clé.** Il se fait sur les groupes grillés G20–G39, avec la métrique principale. La mesure unique se fait ensuite sur G1–G19, avec la clé choisie seule.

## Métrique (sur G1–G19)
- **Principale** : log-vraisemblance moyenne par lettre, avec le modèle de bigrammes polonais de la mesure 1 (texte de la thèse Paszek, déjà haché dans PREREG.md). Les numéros sans lettre sont exclus.
- **Secondaire**, informative seulement : nombre de groupes de longueur ≥ 2 qui sont des mots du lexique de la mesure 1 (lexique_pl.txt, SHA-256 9ea97c09…). Ce lexique ignore l'orthographe d'avant 1936.
- **Témoins** : 200 permutations aléatoires (graine 19440904) de la table numéro→lettre de la clé choisie.

## Seuil de succès
- Le score principal sur G1–G19 doit être strictement supérieur à celui des 200 témoins (p < 0,005).
- **ET** au moins 50 % des groupes de longueur ≥ 2 de G1–G19 doivent être lisibles comme des mots polonais (orthographe d'époque admise). Je fais ce contrôle à la main, juste après la mesure, et je justifie chaque mot dans RESULTAT-2.md.

**En cas d'échec** : arrêt et rapport. On ne fait pas de PREREG-3 sans accord.
