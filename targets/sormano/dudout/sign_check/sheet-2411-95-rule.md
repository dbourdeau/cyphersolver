# Règle de sélection — planche « Sormano no 63, 95 % » 2411-95 du 24/11/2026 (cible cyphersolver sormano), écrite AVANT toute construction de vignettes

Demande de Brice (24/11) : « prépare des planches s'il manque quelques mots des lectures précédentes pour passer 95 % ».
Pièce : BnF fr. 3096 no 63 (Gallica btv1b9060015d, vues 119-121, public ; sources/gallica/ = liens vers SPOF_2).
Base : planche-2411/integration/ (réponses 2411 + fusion « n italique = n à queue = ϰ = e », π seul = n) :
841 mots, sûrs 748 + probables 48 = 796 = 94,6 %. Seuil 95 % = 799 : **il manque 3 mots**.
Coordonnées = pixels natifs des vues Gallica (f120 : 8664 × 5878). Lignes = étiquettes de no63_signs_2411_fusion.txt.

## Pourquoi cette planche
Après la fusion du 24/11 (ALPHABET-CORRIGE.md), un signe « n » de la transcription peut être π (n) ou ϰ (n italique à
queue, e). Trois groupes [?] ne donnent pas de mot avec n mais en donnent un avec e, et à l'œil (agrandi 4×, par moi
seul) leur signe a le tracé cursif de ϰ, sans la barre débordante de π. Un humain qui tranche la FORME fait passer le
groupe en mot. Ce sont les seuls [?] décidables par un seul signe ; les autres [?] (Q6 « pa », v116_00 4n9kSwetp,
r116_00 « al n i nta », c3ZYcw…) demandent plusieurs signes ou un sens non établi : écartés.

## Formes (2) — exemples réels de cette main, un signe par vignette, vérifiés à l'œil (planche-contact 3-4×)
- **π (n)** : v116_00 2ᵉ signe de « 4n9kSwetp » (f121 : 1897-1970 × 683-742) ; v115_08 « zkn… » (f120 : 1812-1878 × 1770-1830).
- **ϰ (n à queue = n italique, e)** : s115_07 « 9ez7rc4t1 » l'esercito (f119 : 6455-6500 × 4110-4185) ; v116_00 7ᵉ signe de
  « 4n9kSwetp » (f121 : 1740-1778 × 668-732). (Les quatre ont été montrés à Brice comme exemples le 24/11 : exemples
  seulement, jamais contrôles.)

## Cibles (3) — options π / ϰ ; boîtes élargies (marge ≥ 5 px), voisin exclu, vérifiées à 4×
- **S1** r116_16 « zoryz615nd7zn **n**t bgn » : le n de « nt » (f120 : 5662-5722 × 2694-2752 ; voisins : n à 5610-5655, x à 5727).
  ϰ → « et » : « si rispondese, **et** ben che con buone… » (le [?] devient un mot).
- **S2** r116_16 « rwSp9p5n **n** zpz F1r » : le n isolé (f120 : 7328-7402 × 2672-2738 ; voisins : π à 7316, ⊡ à 7412).
  ϰ → « e » : « con buone et vive ragion **e** si sforsasi ».
- **S3** r116_31 « **n**S9pgruo 9 mvrch7zk » : 1ᵉʳ signe (f120 : 5387-5448 × 4594-4658 ; voisins : ʒ à 5381, S à 5456).
  ϰ → « egli era il » : « del qual si parla **egli era** il marchese di Mantoa ».

## Contrôles (3), signes de mots lus, jamais montrés à Brice ni cibles ni exemples
- K1 r116_16 « bgn » (ben) : π (f120 : 5917-5980 × 2689-2743), attendu π.
- K2 r116_15 « dkte » (dete) : ϰ final (f120 : 5404-5457 × 2586-2648), attendu ϰ.
- K3 r116_14 « H19ezkr7 » (vol essere) : ϰ (f120 : 5240-5313 × 2463-2533), attendu ϰ.

Page : un seul signe encadré ; aucune glose ; « forme n » ; titre « Planche S (95 %) ». Options texte habituelles (aucune /
autre forme, impossible à distinguer, illisible, pas un signe) + remarque. planche_core v2 (copie planche-2411), cadre
rouge = boîte ci-dessus (déjà élargie ; le noyau ajoute 2 px). Graines 20261124 / 6395. Export : reponses-2411-95-sormano.json.
Taille visée ≤ 1,6 Mo.

## Intégration (après réponses, sur une copie de planche-2411/integration/cible ; PR #440 mergée : correction = nouvelle PR, rien poussé sans accord)
1. Un contrôle raté (y compris « impossible à distinguer ») → rien intégré ; noté dans HANDOFF.
2. Cible répondue ϰ → signe réétiqueté e dans la copie ; le [?] devient le mot (S1 et, S2 e, S3 egli era) ; classe
   {probable} (°) : valeur ϰ = e établie par la fusion du 24/11 mais le mot n'est lu qu'avec ce signe tranché par la forme.
   (Mot sûr si la règle de comptage du dossier compte « forme vue par Brice » comme sûre, comme meter/lega le 24/11.)
3. Cible répondue π → [?] inchangé. « aucune / autre forme » avec remarque → forme propre (sans valeur), [?] inchangé.
4. Recompte (compter.py, base 841 mots) ; seuil 799. Entrée HANDOFF datée ; PR de correction proposée, pas poussée.

## Avenant 1 (24/11, après la 1ʳᵉ planche-contact, AVANT toute présentation à Brice) — hash initial 638de718f8f97da9ca2eaf616a806c09a2c3dadd8629e94e13b30c7bc76f2bdb
- Exemples ϰ recadrés sans changer de signe : v116_00 (f121 1730-1789 × 674-740 : le jambage droit sortait du cadre) ;
  s115_07 (f119 6445-6506 × 4118-4176 : marge homogène, ϙ et Ŧ voisins exclus).
Aucune cible, aucun contrôle, aucune option ni règle d'intégration changé.
