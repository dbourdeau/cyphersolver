# RESULTAT-O3 — stmauris1548 (cible WAINUT), lettre de 1547, cc. 1v + 2r — 25/11/2026, Claude Opus 5.5 (fil 🔓)

**Verdict : FAIL** (M 0,784 < 0,85). Mesure unique, faite une seule fois, selon PREREG-O3 (SHA fd80c823…, vérifié avant toute action).

## Chaîne (horodatée)
| étape | fichier | SHA-256 |
|---|---|---|
| préenregistrement (vérifié) | PREREG-O3.md | fd80c8234ba34c04c35a7752982475af690a250fb2be2919257b4af9dbf330cc |
| consigne des passes | input/BRIEF-PASSE.md | 66c569947eaa0d38ea2e6c689677d0dc3fdc584f3a5dd3234c0ddee0a5be8762 |
| passe A (agent Opus neuf, aveugle) | passe-A/transcription_passA.txt | 691d2051b2591f3844a737474d6c153596d026c6377c2765ba959e944a39b287 |
| passe B (agent Opus neuf, aveugle, sans accès à A) | passe-B/transcription_passB.txt | e3b9ae6f45b6a8092fae6992696e5f03fcb16eb654633130c32e1389c721a0f1 |
| comparaison A/B | COMPARAISON-AB.txt | — |
| arbitrage aveugle (3ᵉ agent Opus) | ARBITRAGE/ARBITRAGE.tsv | — |
| transcription fusionnée, gelée 09:22:36 | transcription_1547_c1v2r_merged.txt | 1ebb74d67b44c3606ad02cd04917fb3f5d3297e6fbccaa8952d0616cb7700866 |
| mesure unique, 09:22:47 | MESURE-O3.txt / MESURE-O3.json | 4718e4f0… / 8ec8b4d2… |

Entrées gelées revérifiées (identiques au PREREG) : c01v.jpg, c02r.jpg, wainut-key.tsv, wainut-SIGNS.md, transcription c. 1r (bloc de conventions seulement), measure_o2.py, compare.py, corpus fr-1520s-diplomatic.

## Chiffres
- Portion : 35 lignes (1v L01-L22 bloc principal + L23-L26 bloc inférieur ; 2r L01-L09 jusqu'à « ( »). 791 jetons (hors ponctuation).
- **Accord A/B : 0,961** (760/791 positions alignées, 31 désaccords) ≥ 0,80 → on continue.
- Arbitrage : A 18, B 12, « ni l'un ni l'autre » 1. Désaccords surtout u/d (13 → u ×12), carré à pattes (B:N12 ×5), crochets N9/N13/fs/q.
- **Mesure** (graine 1548, clé WAINUT inchangée) : 746 jetons avec valeur (94,3 %), 750 lettres décodées ;
  **M = 0,7840** ; témoins (200 permutations) max **0,3914**, moyenne 0,2195 ; marge 0,3926 ; z non disponible (l'outil ne sort pas
  l'écart-type ; voir ci-dessous).
- Critères : lettres ≥ 300 OUI ; M ≥ 0,85 **NON** ; M ≥ max témoins + 0,30 OUI. → **FAIL**.

## Conséquence (PREREG-O3 §5, appliqué tel quel)
Rien sur cc. 1v-2r n'est un texte validé ; le décodage reste une donnée (MESURE-O3.txt). cc. 1v et 2r sont **grillées**. La
lettre de 1547 n'a plus de portion neuve pour cette clé : arrêt. Une nouvelle tentative demanderait une autre lettre du même
chiffre (p. ex. 12 mars 1548, cc. 5r-8v) et un nouveau PREREG. Aucune PR ; rien posté, envoyé ni publié.

Observation (non validée, ne change pas le verdict) : le décodage donne du français suivi sur de longs passages (ex.
« le roi c'est plainct », « le connestable », « Turin en leurs garnisons », « espaignols », « pour le trop grand service »).
L'échec tient au seuil absolu M ≥ 0,85, pas aux témoins (marge 0,39). 45 jetons sans valeur (formes N du transcripteur, NIL)
coupent les mots ; l'orthographe du XVIᵉ s. et le lexique limitent aussi M.

## Points d'exécution déclarés (aucun ne touche la clé, l'outil, la graine ni les seuils)
1. Comptage A/B : `compare.load` et la boucle ligne à ligne de WAINUT (tools/compare_o3.py), SANS le `BMAP` de WAINUT
   (table propre à leurs passes l2) : noms comparés tels qu'écrits (strict).
2. Arbitrage : l'agent C a lui-même localisé et encadré chaque position (ARBITRAGE/boxes/, sur SPOF_2) à partir du rang du
   signe et du contexte, puis choisi sur les seules descriptions de formes (ARBITRAGE/CANDIDATS-DESCRIPTIONS.md).
3. « ni l'un ni l'autre » écrit `NIL` (nom absent de la clé) et non `?` : `compare.load` supprime un `?` isolé, ce qui aurait
   collé les lettres voisines ; `NIL` donne bien « pas de lettre » et coupe la couverture.
4. Formes N des transcripteurs renommées `tN…` / `tA-N…` / `tB-N…` dans la fusion, pour appliquer §3 (« N-shapes … give no
   letter ») : la clé de WAINUT contient ses propres N1-N20, qui auraient sinon donné des valeurs par homonymie.
   **À signaler sur O2** : la transcription c. 1r (O2) contient 22 jetons N1-N8 ; ceux dont le nom existe dans key.tsv
   (N1-N6, N8) ont reçu en O2 les valeurs WAINUT de même nom, contrairement à la limite déclarée d'O2. O2 n'est pas recalculée.
5. Lignes : 1v compte 22 + 4 lignes (PREREG : « ≈ 24 » + 4). Recadrages (tools/make_crops.py) et cases d'arbitrage sur SPOF_2
   uniquement (liens symboliques `crops`, `ARBITRAGE/boxes`) ; aucune copie d'image ailleurs ; zooms temporaires effacés.
6. z des témoins : non produit par measure_o2.py (inchangé) ; seuls max et moyenne existent.
