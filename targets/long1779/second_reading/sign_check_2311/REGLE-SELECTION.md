# Règle de sélection — planche « Enoch Long 1779, alphabet B » du 23/11/2026 (cible cyphersolver long1779), écrite AVANT toute construction de vignettes

Pièce : NARA, M804 Revolutionary War Pension Application Files, dossier W. 16138 (Enoch Long), journal chiffré.
Images : 3 vues du National Archives Catalog (domaine public, NARA), téléchargées le 23/11 (curl, 3 × 200, 4 s d'écart) :
4160708_00399.jpg (image 16, pages 16L/16R), 4160708_00400.jpg (image 17, 17L), 4160708_00408.jpg (image 25, 25L) ;
stockées sur SPOF_2 …/dechiffrements-europe/long1779/img/ (PROVENANCE.md), lien symbolique long1779/img.
🔴 Cible d'un tiers : tout le travail long1779 est d'Andrew Beling (ajbeling) avec ses agents ; aucune PR ouverte sur la
cible au 23/11 (gh search). Le résultat lui sera PROPOSÉ (commentaire/PR, crédit Beling + relecteur Brice) ; ses fichiers ne
sont pas modifiés ici.
Base : clone de lecture _shared/cyphersolver (main f280c87b99) targets/long1779 : key_systemB_frozen.json (alphabet de Long,
16R l. 1–2), NOTES.md (jumeaux du système B), second_reading/second_reading.tsv (after_conf, after_word), linemap.tsv.
Départ (NOTES / profile, 15/11) : 1 041 mots chiffrés, 513 sûrs (49,3 %), 262 probables, 60 douteux, 206 non lus.

## Critère
Mots du système B classés M (probables) après la seconde lecture, dont le sens est donné et dont la seule incertitude est
UNE paire de formes jumelles nommée dans NOTES.md (m/w : creux ou bosses ; r/s : deux ʒ ; a/v), sur les trois vues
téléchargées, signe regardé à l'image le 23/11 (×3–5).

## Cibles retenues (7)
Formes (alphabet de Long, 16R l. 1–2) : « creux » = signe m (w cursif à creux) ; « bosses » = signe w (m cursif à bosses) ;
ʒ¹ = r (ʒ à crochet) ; ʒ² = s (ʒ à trois barres) ; 1 = a (trait court à drapeau) ; i = v.
- **L1** W0763 17L l03 mot 4 « my » (m/w y), 1er signe : creux / bosses. Creux → « my » sûr (+1).
- **L2** W0943 25L l03 mot 1 « which » (w/m h i c h), 1er signe : creux / bosses. Bosses → « which » sûr (+1).
- **L3** W0769 17L l05 mot 2 « me » (lu u u e par une équipe), 1er groupe : creux / bosses. Creux → « me » sûr (+1).
- **L4** W0966 25L l07 mot 1 « last », signe ʒ : ʒ¹ / ʒ². ʒ² → « last » sûr (+1).
- **L6** W0710 16R l12 mot 5 « more/wore », 1er signe (pâle) : creux / bosses. Creux → « more », bosses → « wore » (sûr si
  le sens du passage l'accepte, sinon noté seulement).
- **L7** W0720 16R l16 mot 3 « love », 3e signe (vu « en v renversé ») : 1 / i. i → « love » sûr (+1).
- **L8** W0961 25L l06 mot 1 « seeing », 1er signe : ʒ¹ / ʒ². ʒ² → « seeing » sûr (+1).

## Contrôles nets (3), signes de mots SÛRS (after_conf H), attendu connu
- **K1** W0690 16R l09 « thought », 1er signe : L (t) / « / » (l), attendu L.
- **K2** W0686 16R l08 « my », 2e signe : « : » (y) / « . » (i), attendu « : ».
- **K3** W0690 16R l09 « thought », 2e signe : « \ » (h) / ʃ (d), attendu « \ ».
Places différentes imposées par planche_core v2.

## Écartés
- W0748 16R l21 « down » (d/p) : à ×5, le 1er signe est un trait droit DÉTACHÉ du o suivant (d écrit en barre droite,
  habitude notée dans NOTES) ; l'effet « boucle ꞔ » vient de la jonction trait + o : question de segmentation, pas de forme.
- e / n / z (tirets identiques dans les rangs de Long) : pas de différence de forme à demander.
- d / l (barres droites toutes deux dans le texte) : idem.
- Pages non téléchargées (13R–15L, autres vues) : hors lot.

## Alphabet
Exemples = signes de l'alphabet écrit par Long lui-même (16R l. 1–2 : rangs a–s et t–z), plus un « my » sûr (16R l08, creux) ;
même main, jamais une cible ni un contrôle. Paires : creux 16R l1 (m) + 16R l08 « my » ; bosses 16R l2 (w) ; ʒ¹ 16R l1 (r) ;
ʒ² 16R l1 (s) ; 1 16R l1 (a) ; i 16R l2 (v) ; L 16R l2 (t) ; / 16R l1 (l) ; « : » 16R l2 (y) ; « . » 16R l1 (i) ; « \ » 16R l1
(h) ; ʃ 16R l1 (d). Vérifiés sur planches-contact de travail (scratchpad, 23/11) puis crops/_contact.jpg.
Page : un seul signe encadré en rouge ; aucune glose ; « forme n » ; titre « Planche L ». Options texte habituelles
(« aucune / autre forme », « impossible à distinguer », « illisible », « pas un signe (tache, trait) »). Ordre : planche_core v2
(copie lot P1, clé dans prive/), graines 20261123 / 1779. Export : reponses-2311-long1779.json.

## Intégration (après réponses, mécanique, sur une copie locale ; rien n'est écrit chez Beling sans son accord)
1. Un contrôle raté (y compris « impossible à distinguer ») → rien intégré ; noté dans HANDOFF.
2. Cible, réponse = forme qui donne le mot du sens : signe fixé (« ! » = lu à la planche), mot M → H (sûr) si le mot ENTIER se
   lit alors par la clé B gelée (#728 : aucune valeur ajoutée) ; sinon reste probable.
3. Réponse = l'autre forme : le mot reste M (ou passe douteux si l'autre forme ne donne aucun mot), remarque notée.
4. « impossible à distinguer » sur une paire (m/w ou r/s) : noté comme homographe de la main (renforce le constat de NOTES),
   mot inchangé.
5. Recompte (sûrs ; sûrs + probables) et entrée HANDOFF datée ; proposition à Beling.
Gain maximal : +7 sûrs (L6 seulement si le sens tranche) → 520 / 1 041 (50,0 %).
