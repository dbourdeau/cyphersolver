# RÉSULTAT LOT4 — vanhalen-1840 — mesure unique sur H (S7, S8), 11/11/2026 14:18 CET — agent Opus 5.5
Cadre : `PROTOCOLE.md` (P01) + `PROTOCOLE-AVENANT-LOT4.md` (SHA 41a8ea9a…, gel `AVENANT-LOT4.sha256` vérifié par le script et après).
Clé gelée : `KEY.tsv` = clé étendue de Fable (SHA d4ee3937…). Une seule exécution de `scripts/mesure_lot4.py` ; essai à blanc `--dry-T`
fait avant, sur T, sans panne, sans correction du script. Sortie brute : `RESULTAT-LOT4-sortie-brute.txt` (SHA 8883e352…), écrite par
le script lui-même, recopiée ci-dessous sans retouche.

## Verdict
- **P01 d'origine : NON VALIDÉE** (car 0,880 ≥ 0,85, mais marge 0,120 < 0,30 ; puissance de ce critère calibrée à 4 %).
- **Mesure LOT4 (décisive) : NON VALIDÉE.** C1 réussi (car 0,880 ≥ 0,75) ; C2 réussi (lm −1,048 ≥ −1,139, soit 0,31 au-dessus du
  meilleur des 200 clés mélangées) ; **C3 échoué** (lm −1,048 < −1,021 = meilleure permutation de groupes −1,101 + 0,08 ; il manque 0,027).
- **Clé : PARTIELLE** (avenant §5 : mesure non validée → partielle, quel que soit le sens). **H est brûlée** : aucune nouvelle mesure
  n'est possible sur cette lettre ; rien n'est rejoué, ni clé, ni seuil, ni transcription.

Pourquoi C3 échoue (constat, sans effet sur le verdict) : H est très répétitive (le même mot de 8 lettres deux fois ; 6 « a », 4 « r »,
4 « e » sur 25 lettres) ; ses nombres, mélangés, redonnent des suites de lettres espagnoles plausibles (meilleure permutation à −1,101).
La clé bat toutes ces permutations, mais de 0,053 seulement, sous la marge de 0,08 fixée d'avance (calibrée au 10ᵉ centile sur T).
Tous les nombres de H figurent déjà parmi les 24 observés dans T : la clé stricte aurait donné le même décodage, et aucune valeur
extrapolée n'a joué.

## Contrôle de sens (jugé une fois sur la sortie brute ; il ne peut plus changer le verdict)
- **Sens-S7 : conforme.** `lacaretera` = « la caretera » (carretera avec un seul r, sans aucune correction) : un complément de « sobre »
  qui ferme la phrase avant « .— Sirvase V.S. … » → « …antes de dicha fecha sobre **la caretera**. »
- **Sens-S8 : non conforme au sens strict de l'avenant.** `dicbosacaretera` (passe 1) / `dicgosacaretera` (passe 2) se lit
  « dic{h}osa caretera » (« sobre la **dichosa carretera** », cette maudite route), accord féminin avec « la » et fin de phrase avant
  « Dios guarde » ; mais il faut relire S8 n°4 (transcrit 13 en passe 1, 18 en passe 2) en **19** (= h, valeur observée dans T,
  « dichos » S2). Une confusion 13/18 → 19 n'est **pas** dans les classes déclarées (3/5, 13/18, 13/3, 8/3, 1/7, nombre omis). C'est
  justement le signe dont la lecture était déjà douteuse (planche 09/11). À revoir sur l'image ; sans effet sur le verdict.

## Lecture de toute la lettre (sous la clé PARTIELLE, non validée)
> Como en ese caso deve **ve[n]ir a Montblanc fuerza** Suficiente para **{custodiar} dichos caudales**. Seria de desear que V.S. **se
> abocase conmigo en** dicha Ciudad el **once, dado caso de que la** marcha por Cervera **del comboi de Barcelona no** nos deviera poner
> personalmente **en contacto antes de** dicha fecha sobre **la caretera**. — … tendremos … de lejos … sobre la **dic{h}osa caretera**.

## Décompte façon Daniel (S1-S8, 30 mots chiffrés ; clé PARTIELLE)
- **Sûrs : 27.** Les 24 de T (voir `fable-lot4-2026-11-11/LECTURE-PROPOSEE.md`) + la, caretera (S7) + caretera (S8).
  « caretera » : lu lettre à lettre sans correction, graphie à un r (r pour rr), à noter comme graphie.
- **Probables {x} : 2.** {custodiar} (S2 n°5, 13 lu 3) ; {dichosa} (S8 n°4, 13|18 lu 19).
- **Restitués [x] : 1.** ve[n]ir (S1 : un 2 manquant entre 16 et 20).
- **Irrésolus ‹…› : 0.**
- Sûrs 27/30 = 90 % ; avec probables et restitués 30/30. La règle de Daniel (≥ 95 %) et P01 (publication seulement si clé VALIDÉE)
  ne sont pas remplies : **pas de publication**. Lecture : 90 % des mots sûrs, 100 % lisibles par le sens, clé non validée.

## Ce qui pourrait encore départager (sans H, désormais brûlée)
- La relecture sur image de S8 n°4 (13/18/19), S2 n°5 (13/3) et du « 2 » manquant de S1 : ce sont des lectures, pas une validation.
- Une validation ne peut plus venir que d'une pièce extérieure : table de chiffre de l'Ejército de Cataluña / Brigada de Reserva
  1839-1840, ou une autre lettre chiffrée du même réseau (voisins N.13/N.15 du fonds 195, Segovia, fonds Espartero).

## Sortie brute (copie exacte de RESULTAT-LOT4-sortie-brute.txt)
```
# sortie brute de scripts/mesure_lot4.py (execution unique)
gel verifie (AVENANT-LOT4.sha256)
--- P01 (scripts/measure.py, inchange) sur H, passe 1 ---
part H nombres hors 70 : 22
decode : lacaretera / dicbosacaretera
car = 0.880 ; mots = 0.000 ; meilleur temoin = 0.760 ; marge = 0.120
VERDICT : NON VALIDEE -> PARTIELLE au mieux
--- LOT4 : decodage brut H, passe 1 (cle gelee KEY.tsv, aucune correction) ---
S7	34=l 70=a 14=c 12=a 6=r 16=e 8=t 28=e 6=r 70=a
S7	lacaretera
S8	15=d 20=i 14=c 13=b 3=o 7=s 12=a 14=c 24=a 6=r 28=e 8=t 16=e 6=r 70=a
S8	dicbosacaretera
H : 25 nombres (22 hors 70)
car = 0.880 ; lm/lettre = -1.048
200 cles melangees : max car 0.760 ; max lm -1.359
200 permutations de groupes : max car 0.920 ; max lm -1.101
C1 car>=0.75 : True ; C2 lm>=-1.139 : True ; C3 lm>=-1.021 : False
MESURE LOT4 : NON VALIDEE
--- information : H passe 2 (non decisive) ---
S7	34=l 70=a 14=c 12=a 6=r 16=e 8=t 28=e 6=r 70=a
S7	lacaretera
S8	15=d 20=i 14=c 18=g 3=o 7=s 12=a 14=c 24=a 6=r 28=e 8=t 16=e 6=r 70=a
S8	dicgosacaretera
passe 2 : car = 0.840 ; lm/lettre = -1.033
```
Rien publié, aucun mail, aucune PR/issue. HANDOFF.md non modifié (à compléter par le fil principal).
