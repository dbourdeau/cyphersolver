# Règle de sélection — planche « Transylvanie 1645, R4936 p. 1 » du 23/11/2026 (nuit ; dossier planche-2411) (cible cyphersolver transylvania1645), écrite AVANT toute construction de vignettes

Pièce : DECODE R4936 (Keresdi Bethlen / Rákóczi, points pour la mission de Varsovie 1645), image IMG_R4936_I28640_P1.jpg
(1704 × 2272 px, seule résolution disponible), dans src/ = lien symbolique vers SPOF_2 …/DECODE-planches-2411/ (SHA256SUMS
de ce dossier). 🔴 Image DECODE : planche privée seulement, jamais publiée ni copiée dans un dépôt ; citer « DECODE R4936 ».
🔴 Cible d'un tiers : transylvania1645 est un dossier de Daniel Bourdeau (dépôt principal, lecture b15 du 23/10, « decoded,
not read »). Étape 0 (23/11 nuit) : `gh pr list --search transylvania1645 --state all` → aucune PR propre (seule #237 rakoczi1632,
sans rapport) ; profil/NOTES = origin/main 31295a96a3. Le résultat sera PROPOSÉ à Daniel (issue/PR, crédit Daniel + relecteur
Brice) ; rien n'est écrit chez lui sans accord.
Base : targets/transylvania1645/R4936-transcription-b15.txt, R4936_align.tsv (colonne class_resolved : 114 « g=t »,
6 « q=u », 4 « c=y »), NOTES.md (« 130 letters on look-alike alternates, mostly t on g-shaped figures »).
Coordonnées = pixels de l'image native ; index de figure à partir de 0 dans la ligne chiffrée (texte clair entre accolades exclu),
lignes numérotées comme R4936_align.tsv.

## Critère
Examen à l'œil (23/11 nuit, crops 2,5-3×) : la figure « g » se présente sous deux formes — **boucle longue** (queue descendante qui
revient largement à gauche, ex. succumbalna L02, respublicanak L03 : valeur u sans conteste) et **crochet court** (queue courte
terminée en crochet, comme les « q » lus t de fegyvert L05 et eytenek L06). Question : les « g » lus t portent-ils la forme
crochet ? Pour chaque famille, les EXEMPLES sont pris sur des lieux non ciblés ; toutes les cibles sont sur la page 1
(écriture plus grande que p. 2), lignes 1-13 seulement, lettres nettes (lieux tachés ou chevauchés écartés : L01 s41 « e »
sous tache, L09 s25 entre deux lignes).
Paires h/r, i/n, a/v : hors planche (aucun lieu signalé hors des [?mots] ; h=h, n=n, a=a seulement dans des mots douteux).
Paire c/e : 2 lieux seulement (signe de hauteur d'x ≈ 22 px, agrandi ≈ 7× : à écarter à la vérification si flou).

## Cibles retenues (11)
g lu t (options : g boucle longue / g crochet court) : **T1** L01 s33 (holtig) ; **T2** L01 s47 (gyalazattyara) ; **T3** L04 s13
(mellett) ; **T4** L05 s14 (eroesitenek) ; **T5** L07 s6 (temnaltatnak) ; **T6** L08 s15 (gyalazattyokra) ; **T7** L12 s31
(ertette) ; **T8** L13 s7 (beczuleteket).
q lu u (mêmes options) : **T9** L09 s8 (beczuletek).
c lu y (options : c / e) : **C1** L05 s3 (fegyvert) ; **C2** L13 s31 (kyralyoknak).

## Contrôles nets (3), signes sans ambiguïté de forme (options : x / z)
**K1** L05 s12 x, attendu x ; **K2** L04 s8 z, attendu z ; **K3** L07 s12 z, attendu z.

## Alphabet (exemples ; jamais une cible ni un contrôle)
g boucle longue (lu u) : L02 s8, L03 s4 ; g crochet court (q lu t) : L05 s7, L06 s12 ; c (lu p) : L01 s0, L03 s3 ;
e (lu y) : L03 s19, L08 s17 ; x : L02 s7, L03 s2 ; z : L02 s12, L04 s17.
Boîtes vérifiées sur planches-contact de travail (scratchpad, 23/11 nuit) puis crops/_contact.jpg.
Page : un seul signe encadré ; aucune glose ; « forme n » ; titre « Planche T ». Options texte habituelles. Ordre : planche_core v2
(copie P2, vignettes agrandies), graines 20261124 / 4936. Export : reponses-2411-transylvania.json.

## Intégration (après réponses, sur une copie locale ; rien n'est écrit chez Daniel sans son accord)
1. Un contrôle raté (y compris « impossible à distinguer ») → rien intégré ; noté dans HANDOFF.
2. T1-T8 : chaque cible qui reçoit « crochet court » → la lecture t y est soutenue par la FORME (le « g » est la figure t du
   scripteur) ; proposer le relabel g→q à ce lieu. Si ≥ 6 des 8 reçoivent « crochet court » → proposer à Daniel la règle de forme
   (crochet = t, boucle = u) pour l'ensemble des 114 « g=t », à vérifier lieu par lieu avant tout recompte. « Boucle longue »
   → la lecture t n'est pas soutenue à ce lieu (noté, signalé) ; « impossible à distinguer » → rien.
3. T9 : « boucle longue » → u soutenu. C1-C2 : « e » → lecture y soutenue ; « c » → non soutenue.
4. Aucune valeur nouvelle n'entre par la planche ; recompte (règle #728) seulement sur copie, entrée HANDOFF datée ;
   proposition à Daniel avec crédit.
