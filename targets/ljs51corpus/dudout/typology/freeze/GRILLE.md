# Grille de codage — typologie des chiffres de Penn LJS 51 (v1, gelée avant tout codage)

Piste 3 de la campagne LJS 51 (brief `ljs51-revue/PISTES-LJS51-2811.md`, Brief 3). Rédigée le 28/11/2026 avant tout codage.
Chemins relatifs au dossier `gel/`. Base : clone cyphersolver `origin/main` = d8ac608093e1149f9456eaa2c99bb456ca0abc92 (fichiers de Daniel Bourdeau, non modifiés).

## Unités

Les 207 documents de Daniel (`targets/ljs51corpus/texts/stats.json`, `documents: 207`) : les 211 fiches de
`chains_all.json`, moins les deux fusions (20r.8 + 47r.1 → `20r.8+47r.1` ; 46v.11 + 13r.1 → `46v.11+13r.1`) et moins les
deux chiffres qui ont leur propre cible (48r.8 → `targets/ljs51f48r`, 106v.6 → cible qaysarani1350). Liste figée :
`data/units_207.json`. 63v compte pour deux unités (63v.1, chiffre de signes ; 63v.trees, écriture des arbres), comme chez Daniel.

## Sources autorisées pour coder (et seulement elles)

Pour chaque unité, la fiche `data/fiches/<unité>.txt`, extraite mécaniquement (script `scripts/fiches.py`) de :
`chains_all.json` (style, technique_note, notes, red_gloss, plaintext, fit_check, answered), la ligne de l'unité dans
`keys_eye/REPORT.md`, et `keys_eye/<unité>.json` (verdict, notes, fit_against_record_wording, measures, system, rule, status).
Si le style renvoie à une autre chaîne (« same family as … »), la fiche reproduit aussi le style de cette chaîne.
Aucune image, aucune lecture du manuscrit, aucune connaissance extérieure : on code ce que disent les fichiers.

## A. Dimensions automatiques (calculées par `scripts/auto.py`, déterministes, pas de kappa)

| code | dimension | règle |
|---|---|---|
| A1 | longueur | `signs` de keys_eye (sinon `signs_total` du record) ; classes `<40`, `40-79`, `80-119`, `>=120` |
| A2 | nombre de formes | nombre de formes distinctes (`measures.shapes`, sinon longueur de `shapes`, sinon clés de `key`) |
| A3 | homophones | lettres ayant ≥ 2 formes dans la clé (`measures.letters_with_two_or_more_shapes`, sinon calcul sur `key`) : nombre et liste |
| A4 | polyvalence | formes qui prennent ≥ 2 lettres différentes dans `key` : nombre (à part : même squelette / squelettes différents) |
| A5 | glose rouge | `red_gloss` du record (vrai / faux) |
| A6 | familles de formes | mots-clés dans `style` (renvoi résolu) : `letter`/`pseudo-Arabic`/`Hebrew` → L ; `numeral`/`digit` → N ; les deux → LN ; aucun → G (géométrique / inventé) ; `tree script`, `tashifi`, `ordinary Arabic letters` → S (système non substitutif ou à classes) |
| A7 | séparateurs | mots-clés dans `style` : `dotted-alif`, `dotted alif`, `dotted stem`, `dotted divider` → POINTE ; autre mention de `divider`/`separator` → AUTRE ; aucune → ND |
| A8 | auto-dérivation | parmi les formes dont la description (`shapes[].description`) contient une lettre arabe, part de celles dont la valeur majoritaire est cette lettre (forme tirée de la lettre claire) |

Descripteurs de contrôle (rapportés, pas des dimensions) : excédent signes − lettres ; état de la réponse du compilateur
(`answered`) ; cohérence lettre de Daniel.

## B. Dimensions codées à la main (soumises au double codage aveugle et au kappa)

Une seule valeur par dimension. En cas de doute réel entre deux codes : prendre `ND` (sauf mention contraire).

**B1 système** (lire d'abord le verdict de la ligne REPORT, puis le JSON) :
- `MUSHAJJAR` : écriture des arbres (comptes de branches) ;
- `TASHIFI` : un signe par classe de squelette non pointé, décrit comme tel ;
- `MAQLUB` : transposition en lettres arabes ordinaires ;
- `NONCLE` : aucune clé établie (pas de clair, « inventory only », « not keyed », « inconsistent ») ;
- `SQUELETTE` : substitution dont le verdict dit qu'elle n'est cohérente qu'au niveau du squelette, ou qu'une même forme sert systématiquement à des lettres de même squelette (« skeleton cipher », « consistent at skeleton level », « share a skeleton », « shared signs for ب/ي ») ;
- `HOMOPHONE` : substitution dont le verdict, les notes ou la technique_note signalent qu'au moins une lettre a deux formes ou plus (« two shapes », « homophones », « two different signs represent … ») ;
- `SIMPLE` : toute autre substitution avec clé (une forme par lettre, éventuelles ruptures isolées).
Ordre de priorité si plusieurs s'appliquent : MUSHAJJAR > TASHIFI > MAQLUB > NONCLE > SQUELETTE > HOMOPHONE > SIMPLE.

**B2 lām-alif** : `UN` si un fichier dit que lām-alif est écrit par un seul signe (ou qu'un signe « لا » vaut lām-alif) ;
`DEUX` s'il dit que lām et alif sont écrits par deux signes ; `ND` sinon.

**B3 hamza** : `NONECRITE` si un fichier dit que la hamza n'est pas écrite (« not written », « without hamza », « hamza
never written ») ; `ECRITE` s'il dit qu'elle a un signe (siège compris, « the ئ seat », « hamza other than the alif ») ; `ND` sinon.

**B4 difficulté déclarée par le compilateur** (technique_note seulement, paroles du compilateur) : `FACILE` (« quickly », « because of its ease », « at once », « from the head of the pen », سريعا, لسهولته, في الحال, من راس القلم) ;
`DIFFICILE` (« difficult », « hardest », « to make it harder », صعب, صعوبة, اصعب, تصعيبا) ; `MIXTE` si les deux ; `AUCUNE` sinon.

**B5 chiffreur** (qui a fait le chiffre, d'après technique_note et notes) : `COMPILATEUR` (« I wrote/enciphered », كتبت, ترجمت, « my answer ») ;
`ALAI` (le patron : al-Maqarr / al-Makhdūm al-ʿAlāʾī, المقر, المخدوم) ; `MUTARJIM` (Shihāb al-Dīn al-Mutarjim comme auteur du chiffre) ;
`JAWLANI` (Badr al-Dīn al-Jawlānī) ; `AUTRE` (une autre personne nommée ou décrite : « a man of Mosul », un qāḍī, Tāj al-Dīn…) ;
`INCONNU` (les fichiers ne disent pas qui a chiffré ; un simple porteur — « brought it » — ne compte pas comme chiffreur).

**B6 technique commentée par le compilateur** : `OUI` si la technique_note rapporte une remarque du compilateur sur la
fabrication du chiffre (formes de lettres, lām-alif, hamza, séparateurs, deux formes pour une lettre, erreur du chiffreur,
système nommé, plumes, nombre de lettres) ; `NON` s'il dit seulement qu'il l'a résolu (vite ou non) ou présente la pièce.

**B7 le chiffre s'écarte du clair écrit** : `OUI` si Daniel signale qu'au moins un mot du clair du compilateur doit être
corrigé ou que le chiffre a une autre forme (« as enciphered », « record X », « needs », « not … », « corrected », « read from the cipher ») ;
`NON` si le clair est confirmé ou si aucun écart n'est signalé ; `NA` pour `NONCLE`.

## C. Fiabilité (seule mesure, gelée)

- Échantillon : 30 unités tirées par `random.Random(3030).sample(units_207, 30)` sur la liste dans l'ordre de `chains_all.json` → `data/echantillon_30.json`.
- Deux codeurs indépendants (sous-agents Sonnet, A et B), même consigne (`gel/CONSIGNE-CODEURS.md`), mêmes fiches, sans voir le codage de l'autre ni le mien.
- Statistique : kappa de Cohen A–B par dimension B1-B7 (`scripts/kappa.py`). **Critère : κ ≥ 0,80 par dimension.**
  Une dimension sous 0,80 est déclarée non fiable : elle est rapportée comme telle (ou redéfinie en v2, déclarée et non
  re-mesurée sur le même échantillon). Si un codeur est constant sur une dimension (κ indéfini), on rapporte l'accord brut et on la déclare « non testable sur l'échantillon ».
- Rapportés en plus, non décisifs : accord brut, accord de mon codage avec A et avec B.
- Mesure unique : l'échantillon de 30 ne sert qu'une fois pour la grille v1.

## D. Ce que la grille ne fait pas

Pas de déchiffrement, pas de relecture d'images, pas de retranscription de 22v.9 ni de 37v.12 (cités depuis les fichiers
de Daniel seulement). Pas d'inférence sur l'identité du compilateur. Corrélations rapportées comme descriptives.
