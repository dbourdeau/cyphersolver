# ARBITRAGE v5a / v5b → CLE_v6 — pandolfini-francia-1514-15 — 09/11/2026 ≈ 03:45 CET (agent arbitrage, Opus)

## Objet
Deux clés dérivées déclarées de CLE_v4 (1848f692…) divergent :
- cle/CLE_v5a.json (16a6d2de…, agent 307/309) : α = et ; 4# = gg (hérité de v4) ; G# = gg ; 0 = c partout.
- cle/CLE_v5b.json (9d5cf3d5…, agent 311/333) : α = per ; 4# = ll ; règle « 0 devant 8 = t ».
- Accord : 2^5 = ca (ba dans « bande ») ; signe 2 polyphone b/c ; 2^1 = cu.
Décision consignée dans cle/CLE_v6.json (a2f1c942…, cle/CLE_v6.sha256, construite par scripts/build_cle_v6.py qui vérifie les
empreintes de v4/v5a/v5b et n'admet que les deux conflits α et 4#). v3, v4, v5a, v5b NON modifiées (empreintes revérifiées).
Relevés faits par script (scripts/contextes.py, contexte décodé par scripts/decode_v6.py) sur TOUTES les transcriptions hachées :
H_346, H2_340, H4_342, N322, N307, N309, N311, N333 (310 pas encore transcrite au moment de l'arbitrage).

## 1. α : « per » (v5b) contre « et » (v5a) → **α = per. Sûr. Pas d'homophonie.**

### 1.1 α est le signe déjà noté « P » (= per depuis T)
- Les premiers transcripteurs ont noté ce signe « P » : T (318, glose d'époque « P D^n 8^2 » = « per conto »), H_346, H2_340, H4_342,
  N322. La note de forme de H4_342 (gelée 36df3d6a…) le dit en toutes lettres : « α (signe « per ») = P comme en 340 ».
- Vérifié sur l'image 346 c. 441r (pos. 883, SPOF_2, découpe privée) : le signe transcrit « P » en L1 (« … 8^4 P 3 L# O … », « .20. P B M … »)
  a exactement la forme α (a fermé à queue, ∝) de 307/309/311 ; même forme vue en 342 L4 (« t^4 α 2^4 G 8^2 »).
- Les agents 307/309 et 311/333 l'ont transcrit « α » (signe « hors légende ») : c'est le même signe, pas un signe nouveau.

### 1.2 Clairs d'époque (paires) : 13 occurrences, toutes « per »
| Pièce | Jetons (contexte) | Clair d'époque |
|---|---|---|
| 346 L1 | … di-se-r-na-te **P** a-ll-o i-n-con-t-ro de Svizeri | 345 « disegnate **per** lo incontro de Svizeri » |
| 346 L1 | Svizeri **P** ancora non si ti-ro-no più | 345 « **per** ancora non si tirono più avanti » |
| 346 L2 | c-re-do i-o **P** a-pe-s-t-ta-re | 345 « sia **per** aspettare » |
| 346 L4 | di-se-r-na-to **P** vo-le-r-si secondo | 345 « **per** volersi secondo » |
| 346 L5 | **P** (po)-te-re più fa-ci-l-me-n-te | 345 « **per** potere più facilmente » |
| 346 L6 | fino alli [xv] **P** | 345 « fino alli xx **per** alla volta » |
| 346 L8 | al quale **P** su-a pa-r-te | 345 « al quale **per** sua parte » |
| 340 L1 | con Inghilterra con **P** la u-l-ti-ma | 341 « come **per** le ultime » |
| 340 L4 | a h **P** … | 341 « et **per** fino al presente » (alignement approximatif) |
| 340 L6 | … si **P** gi-o-r-n … | 341 « ogni dì » (« per giorno » ; alignement approximatif) |
| 342 L4 | qui si tiene **P** ce-g-to (certo) | 343 « qui si tiene **per** certo » |
| 342 L6 | se ne ha qui **P** i-n-te-n-de-re | 343 « se ne ha qui **per** intendere » |
| 342 L7 | non erano **P** su-cc-e-de-re | 343 « non erano **per** succedere » |

### 1.3 Lettres nues : les 25 occurrences de α (relevé exhaustif), lecture en contexte
Légende : ✔ = « per » donne la tournure attendue ; ✘et = « et » est exclu (agrammatical ou impossible) ; = = les deux se lisent.
| Pièce | Contexte (décodé v6) | per | et | Verdict |
|---|---|---|---|---|
| 307 L4 | sendo cosa … secreta **α** il periculo che ne potresse succedere | ✔ (« à cause du danger ») | possible | = , per meilleur |
| 307 L10 | monstrando **α** questi vol-t … | ? | ? | non lu (ni l'un ni l'autre) |
| 307 L12 | volere il Cristianissimo **α** co-no di … commodo | ✔ « per conto di » ? | faible | per probable |
| 307 L16 | accerto … vostre Signorie **α** t-ra-g-lo di bon loco che | elliptique | meilleur | **seul cas pro-« et »** |
| 307 L22 | la ragione non vole **α** nulla | ✔ « per nulla » (locution) | ✘et | per |
| 307 L23 | della tregua con Spagna **α** ancora non s'intende | ✔ « per ancora » = 345 « per ancora non si tirono » | ✘et (« et ancora » sans verbe coordonné) | per |
| 309 A3 | parentado della figlia del duca Valentino **α** vostra Magnificentia | ✔ (« pour Votre Magnificence ») | possible | = |
| 311 A4 | il duca di Suffolc dovessi pigliare **α** moglie la regina | ✔ « per moglie » | ✘et | per |
| 311 A7 | senza qualche fondamento da **α** ‹F^n…› | ? | ? | non lu |
| 311 B2 | un gran **α**-(c)-so-na-gg-io | ✔ per-sonaggio (dans le mot) | ✘et | per |
| 311 B5 | qualche bono **α**-so-na-gg-io | ✔ per-sonaggio | ✘et | per |
| 311 B7 | qualchuno s-pa-r-ge-va **α** la corte | ✔ « per la corte » | ✘et | per |
| 311 B10 | non era **α** c-re-de-r-lo | ✔ « non era per crederlo » (= 343 « non erano per succedere ») | ✘et | per |
| 311 B11 | da posserlo sa-**α**-e | ✔ sa-per-e (dans le mot) | ✘et | per |
| 311 B11 | et **α** via ‹E› del papa | ✔ « et per via » | ✘et (« et et ») | per |
| 311 B12 | né manco **α** via delli oratori | ✔ « per via » | ✘et | per |
| 311 B12 | et **α** re-la-t-o-ne di chi | ✔ « et per relatione » | ✘et (« et et ») | per |
| 311 B14 | tenessi la cosa **α** ce-r-ta | ✔ « per certa » (= 343 « per certo ») | ✘et | per |
| 311 C1 | [Siamo ad notte et di nuovo] **α** via d'uno particulare | ✔ « per via » | ✘et | per |
| 311 C2 | intendere al Cristianissimo **α** via di … | ✔ « per via » | ✘et | per |
| 311 C5 | sono pagati **α** e-qua-l parte | ✔ « per equal parte » | ✘et | per |
| 311 C7 | che il papa sia **α** havere | ✔ « sia per havere » | ✘et | per |
| 311 C9 | **α** natura | ✔ « per natura » | ✘et | per |
| 311 C9 | et **α** a-cc-i-de-n-te | ✔ « et per accidente » | ✘et (« et et ») | per |
| 311 C16 | che si mostra **α** le cose venute | ✔ « per le cose » | ✘et | per |

Bilan : 25 occurrences ; 19 où « per » est la seule lecture possible (dont 3 « et α » et 3 à l'intérieur d'un mot : per-sonaggio ×2,
sa-per-e) ; 2 neutres (307 L4, 309 A3) ; 2 non lues ; **1 seule** (307 L16) où « et » se lirait mieux, sans être exigé (« per [quel che]
traggo » reste possible). Les 4 attestations de v5a (309 A3, 307 L23, L4, L10) se lisent toutes avec « per », et 307 L23 devient la
formule même de 345.
Homophonie (α = per ET et) : rejetée. Aucune occurrence n'exige « et » ; « et » a déjà son signe (F barré, des dizaines d'emplois, y
compris juste devant α : « F α ») ; un signe-mot à deux valeurs serait inutilisable par le déchiffreur. 307 L16 est classé ‹α› irrésolu
dans la relecture (ou erreur de chiffrement du secrétaire), pas comme preuve d'une seconde valeur.

## 2. 4# : « ll » (v5b) contre « gg » (v4 → v5a) ; G# = gg (v5a) → **4# = ll (sûr) ; G# = gg (probable). Deux signes distincts.**
- Il n'y a pas de conflit d'observation : 4# n'apparaît NI en 307 NI en 309 (v5a n'a fait qu'hériter de « 4# = gg » de v4, posé par
  « analogie seulement », sans attestation) ; G# n'apparaît NI en 311 NI en 333.
- Formes (images privées, SPOF_2) : 4# = « 4 » anguleux ouvert + double barre (333 c. 417r L1, vu) ; G# = δ à boucle fermée, rond, +
  double barre (309 c. 378r B1, vu). Formes différentes.
- 4# (21 occurrences, relevé exhaustif) :
  - clair d'époque : 333 L1 « da-4#-e ba-n-de a qua » ↔ 332 (copie claire aux Otto du même jour) « dalle bande di qua » ; 333 L2
    « da-4#-e re-so-lu-ti-o-ni », L3 « de-4#-e qua-li » (même phrase que 332 « aspectando la resolutione ») ; 342 L2 « … 4? Q 2^5 y^4 »
    ↔ 343 « dalle bande di costà » (# non vu par le transcripteur : appui faible) ;
  - lettres nues : 322 L8 « da-4#-e ba-n-di » ; 311 A1 de-4#-o (dello) appuntamento, A3 de-4#-a (della) opinione, A7 della ragione,
    B3/B8/C3 ne-4#-a (nella) legha ×3, B7 que-4#-o (quello), B12 de-4#-i (delli) oratori, C7 da-4#-e (dalle) bande, C8 a-4#-e (alle)
    spese, C15 nella capitulatione, C12 de-4#-a (della) cosa : « ll » partout ; « gg » ne donne aucun mot (« dagge », « degge »,
    « negga ») ;
  - 3 cas où « ll » ne donne pas non plus le mot : 311 C9 « a-4#-i-de-n-te » (accidente : cc), C12 « a-4#-e-r-ta-ta-si », C13
    « … h-4#-i-a » (gl ?), et C10 « a-4#-i-o » : confusion de forme ou valeur « gl » à vérifier en HD ; ne remettent pas en cause ll.
- G# (1 occurrence) : 309 B1 « non ve-G#-i-a » = « non veggia » (forme toscane de « vegga ») : gg, comme g# (340 L7, 346 L9, 311
  « personaggio ») ; « ll » donnerait « vellia » (pas un mot). Probable (1 attestation).

## 3. Signe 2 (b ou c) ; 2^5 → accord, rien à trancher
- Défaut c (2^1 cu, 2^2 co, 2^3 ci, 2^4 ce, 2^5 ca) : v5a et v5b. Règle machine : 2^5 devant « y 3^x » (bande) = ba.
- b par le sens, dans la lecture seulement (alternative déclarée, non appliquée au décodage) : bona, bono (311), buon, bon, dubio (307),
  bianca (311 A4 : 2^3 = bi, que v5b décodait « bi » par défaut et que v6 décode « ci »).

## 4. « 0 devant 8 = t » (v5b) contre 0 = c (v5a) → **0 = c ; règle v5b non reprise (orthographe seulement)**
- Les exemples de v5b (tutto, detto, mattina, lettera, lettere) se lisent avec 0 = c : tucto, decto, mactina, lectera, lectere, graphies
  latinisantes courantes de la chancellerie florentine (cf. les clairs d'époque 343 « effecti », « predecte », 341 « satisfactione »,
  et 307 « intractengono », « salvocondocto »). La règle ne change aucun mot, seulement la graphie du décodé ; la clé la plus simple
  (v5a) est gardée. Changement visible dans les décodés v6 de 311 et 333 (« tu c to » au lieu de « tu t to », etc.).
- Gardées de v5b : O devant r nu = c (ch : richiesta, chi, chiaro, qualchuno) ; .4. = maestà après « questa » abrégé (S^4 6 8).

## 5. Contenu de CLE_v6 (a2f1c942…)
Union v5a ∪ v5b, avec : α = per ; 4# = ll ; G# = gg ; m# = mm ; T^2 = senza ; 2^1 cu, 2^2 co, 2^3 ci, 2^4 ce, 2^5 ca ; règles machine
« O + r nu » et « 2^5 y 3… » et .4. ; alternatives non appliquées listées dans _alternatives_non_appliquees (2 = b ; O + 8 = ct ;
9^4 = ze ; 5 nu = h ; A nu = a ; α = et REJETÉE ; 4# = gg REJETÉE ; 0 + 8 = tt non reprise). Aucune valeur nouvelle hors arbitrage.
Statut : clé PARTIELLE (P03bis), dérivée déclarée, NON mesurée.
