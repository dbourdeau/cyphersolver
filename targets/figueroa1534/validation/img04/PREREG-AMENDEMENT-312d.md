# AVENANT au PREREG-ATLAS (6d666ab4…) — planche 312d de Brice → K5 + atlas v5 + étiquettes v5 — 15/11/2026
Gelé par SHA-256 (`PREREG-AMENDEMENT-312d.sha256`) AVANT toute transcription, tout regard et toute mesure sur 1547 img04 (PARES 3615615, `dl/img/3615615/04.jpg`, dernière portion intacte de ce chiffre).

## 1. Base
- Planche 312d (PREREG `atlas-estense/planche-312d-PREREG.md` ab9df790…, clé e40e2bc5…), réponses de Brice `atlas-estense/reponses-planche-312d.json` (ff02eb47…, 14/11 23:48Z). **Contrôles 11/11, formes 3/3 → réponses retenues** (`atlas-estense/score-312d.txt`, `cryptanalysis/r312d/score312d.py`).
- Regroupements appliqués sans valeur nouvelle (PREREG 312d § 4) → `working/p-atlas/lot/T_*_ARB8d.txt`, gelés `T-ARB8d-LOT1553.sha256` avant décodage (149 jetons : ʒ̇→ȣ̇ 57, ?4-open→ꝝ 88, c1→ė, c6→8̇, ʌ̇ de Bonifacio→?n-dot 2 ; c5 était déjà ȣ̶). ARB8c inchangés.
- Atlas v5 `working/atlas-estense/atlas-v5.tsv` (d1bd37c7…) = v4 + 54 exemplaires 312d.

## 2. Scissions → étiquettes nouvelles et valeurs CANDIDATES (K5)
`working/k5/K5.tsv` = K4 (a456e5bb…, aucune valeur changée) + 8 étiquettes :
| question | groupes de Brice | étiquette | valeur candidate | appuis antérieurs (lot 1553, fiches ARB8) |
|---|---|---|---|---|
| D3 | Xʰ « te » ≠ Xʰ « pre » ≠ ∇̶ | `Xᵗ` | te | ≈ 17 (alteza, parte, presente…) |
| D4 | ɏ « su » ≠ {ɏ se, ɏ ñ, 7̶} | `ɏᵘ` (= forme ?yr) | su | ≈ 30 (Su Majestad, su, sucedido…) |
| D5 | ꞓ « cre » ≠ ꞓ « fre » | `ꞓʳ` | cre | 2 + Tomokiyo (escrebí) |
| D6 | ʌ̇ de Bonifacio = ?n-dot ≠ ʌ̇ « para » | `ṅ` | fa | ≈ 20 (Bonifacio, favor…) |
| D7 | {« bo »} ≠ {« gu »} quelle que soit l'étiquette ?o7/oᵖ | `σ7` (oᵖ garde gu) | bo | ≈ 20 (Bonifacio, vuesa, favor) |
| D10 | + « ce » ≠ {+ « ne », ?t-cross} | `+ᶜ` / `+ⁿ` | ce / ne | hacer ×10 / manera, tienen… |
| D11 | Ꝉ° « mo » ≠ Ꝉ° « po » | `Ꝉ°ᵖ` | po | > 15 (por, podría, temporales) |
Non mis dans K5 : a+ « ge » (D1 : même forme → homophone, inutilisable par le score qui prend la 1ʳᵉ valeur) ; ɏ « ñ » (même forme que ɏ se) ; 7̶ = forme de ɏ (D4 : conflit be/se signalé, étiquettes inchangées) ; 8ᵒᵘᵛ̈ (D12 : classe propre ≠ ᘐ̈, sans valeur) ; ·8· (W1 : points latéraux, sans valeur) ; ȝ ≠ ∂ et ꝝ ≠ Ꝉ̶ (D8, D9 : classes existantes, règle de forme seulement). Ces formes, si elles apparaissent, comptent hors clé (sans valeur).
Équivalence `?yr` = `ɏᵘ` : jugée par l'orchestrateur sur la vignette D4c (y barré + crochet en r), déclarée ici.

## 3. Étiquettes et références (gelées)
- `working/p-atlas/LABELS-FORMES-v5.md` (d6841fa4…) = LABELS-FORMES (e0485fbc…) + § D (7/y, 8/g, paires 312d).
- `working/p-atlas/REF-312d.png` (SPOF_2, b882eaf3…), + `lot/REF-7y.png`, `lot/REF-8g.png` (déjà gelés) ; planches A-D de l'atlas.

## 4. Mesure unique (règle INCHANGÉE)
- Portion tenue à l'écart : **1547 img04 entier** (toutes les lignes chiffrées). Si < 300 jetons après arbitrage : pas de mesure (portion insuffisante), rien d'autre n'est ajouté (img05/06 grillés).
- Transcription : passe A (sous-agent), passe B (autre sous-agent, sans accès à A), arbitrage C (3ᵉ sous-agent, sur l'image, avec A et B, sans valeurs ni clair). A, B, C ne reçoivent que : bandes et page d'img04, planches A-D, REF-7y, REF-8g, REF-312d, LABELS-FORMES-v5.md ; interdiction de lire clairs, K*, transcriptions antérieures, mesures. Kit isolé SPOF_2 `working/p-atlas/heldout04/`. L'orchestrateur ne fait que des opérations mécaniques.
- Transcription arbitrée gelée par SHA (`working/p-atlas/T-IMG04.sha256`) AVANT toute lecture de la copie en clair correspondante.
- Référence : copie en clair d'époque correspondante (img12 fin – img13, PARES 3615615), transcrite APRÈS le gel → `working/p-atlas/clear_1547_ref_img04.txt`, réunie à `working/c05/clear_1547_full.txt` ; fenêtre choisie mécaniquement par le script (Smith-Waterman ± 40 car.).
- Score : `cryptanalysis/p-atlas/score_atlas.py` INCHANGÉ (21ed80a2…) avec K5 ; 200 témoins clé entière + 200 témoins intra-classe (graine 744). `score_k4.py` aussi lancé tel quel avec K5, et score_atlas avec K4 (rapporté, pour isoler l'apport de K5).
- **Seuils inchangés (plan intra-classe)** : score ≥ 0,85 ET ≥ max(témoins intra-classe) + 0,30 ET hors clé ≤ 20 %. Sinon NON VALIDÉ. img04 grillée dans tous les cas.
- Si VALIDÉ : les 8 valeurs K5 deviennent « validées par la mesure d'ensemble » (pas une à une) ; relabels aveugles du lot 1553 pour les classes scindées, puis fiches de lecture. Si NON VALIDÉ : K5 reste candidate ; chiffres rapportés tels quels.

## 5. Écarts déclarés
- L'orchestrateur de cet avenant a vu à l'écran la 1ʳᵉ ligne (≈ 200 car.) de `clear_1547_full.txt` (img13 depuis « Yo desseo ») en cherchant la couverture des clairs ; l'orchestrateur P-ATLAS avait déjà vu la fin d'img13. Parade : aucune transcription d'img04 par l'orchestrateur (§ 4).
- Les classes nouvelles ont été choisies sur le lot 1553 (sans clair) ; aucune n'a été réglée sur 1547.
