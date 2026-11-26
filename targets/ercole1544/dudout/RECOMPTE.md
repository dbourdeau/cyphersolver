# RECOMPTE mot par mot — ercole1544 (cc. 78r-79r et 174r-175v), planche ercole1544-2511, 25/11/2026

Base : `targets/ercole1544` de LcCompany/WAINUT, identique sur `main` (b13dd55072 et db211162a9) → avant/. Copie modifiée → après/
(= le patch `ercole1544-planche-2511.patch`). Contrôles K1-K3 : 3/3.
Compteur : `scripts/count_words.py` de LcCompany/WAINUT (inchangé). Décodage : `scripts/decode.py` + `key.tsv` (inchangée) ;
les deux décryptions régénérées sont identiques aux fichiers du patch (aux fins de ligne CRLF près). `scripts/check_repairs.py` :
0 écart non marqué ; `--table` redonne les deux `editorial_*.md` du patch.

## Totaux (inchangés)

| | plain | no hole | clean | verbatim | repairs |
|---|---|---|---|---|---|
| cc. 78r-79r avant | 718 | 385 | 184 | 148 | 3 |
| cc. 78r-79r après | 718 | 385 | 184 | 148 | 3 |
| cc. 174r-175v avant | 1240 | 697 | 260 | 216 | 15 |
| cc. 174r-175v après | 1240 | 697 | 260 | 216 | 15 |

Seuls bougent : l'estimation `est` (78r 348 → 349, 175r 332 → 334 : les nouveaux codes ouverts [#3] et [#2] comptent comme
signes) et la répartition des réparations par feuillet (174v 2 → 1, 175r 6 → 7 ; « without 175r » 9 → 8).

## Mots qui changent dans la lecture (tous les autres : texte et classe identiques)

| lieu | avant | après | effet |
|---|---|---|---|
| E21 | `intertener°` (réparé, les signes donnaient `inter[m]ener`) | `intertener` | réparé → sûr (verbatim) |
| F03 | `gratissime` (sûr) | `gratissime°` (les signes donnent `gratissi[d]e`) | sûr → réparé, valeur tirée du sens seul {probable} |

Correction des signes, pas de gain de lecture : un mot gagne, un mot perd.

## Décryptions (lignes qui changent)

| ligne | avant | après |
|---|---|---|
| A05 | `…pericolosaftriglia…` | `…pericolosaf[#3]riglia…` (lecture : `[...]` gardé) |
| B02 | `…dallaltrose[IO]fussi…` | `…dallaltrosa[IO]fussi…` (`[?Se]` gardé) |
| B21 | `…fradoidouino` | `…fradoidou?ao` (lecture : `[...]` gardé) |
| E21 | `…intermenera` | `…intertenera` |
| F03 | `…gratissimealre…` | `…gratissidealre…` |
| F08 | `…farire.rito…` | `…farire[#2]drito…` (lecture : `[...]` gardé) |

## Sortie brute de count_words.py

Avant :
```
c. 78r         est   348  plain 335 (96%)   no hole 226 (65%)  blocks 7/11  clean 113 (32%) blocks 4  verbatim 113 (32%)  repairs 1  doubtful 11  holes 6  codes 5
c. 78v         est   296  plain 275 (93%)   no hole 126 (43%)  blocks 5/10  clean 51 (17%)  blocks 2  verbatim 15 (5%)    repairs 1  doubtful 10  holes 6  codes 0
c. 79r         est   142  plain 108 (76%)   no hole 33 (23%)   blocks 2/5  clean 20 (14%)  blocks 1  verbatim 20 (14%)   repairs 1  doubtful 1  holes 4  codes 1
c. 174r        est   321  plain 315 (98%)   no hole 149 (46%)  blocks 5/10  clean 80 (25%)  blocks 4  verbatim 80 (25%)   repairs 3  doubtful 7  holes 5  codes 0
c. 174v        est   358  plain 341 (95%)   no hole 296 (83%)  blocks 8/9  clean 42 (12%)  blocks 2  verbatim 42 (12%)   repairs 2  doubtful 17  holes 2  codes 4
c. 175r        est   332  plain 297 (89%)   no hole 61 (18%)   blocks 2/9  clean 61 (18%)  blocks 2  verbatim 17 (5%)    repairs 6  doubtful 11  holes 11  codes 2
c. 175v        est   344  plain 287 (83%)   no hole 191 (56%)  blocks 6/9  clean 77 (22%)  blocks 3  verbatim 77 (22%)   repairs 4  doubtful 8  holes 5  codes 4
cc. 78r-79r    est   786  plain 718 (91%)   no hole 385 (49%)  blocks 14/26  clean 184 (23%) blocks 7  verbatim 148 (19%)  repairs 3  doubtful 22  holes 16  codes 6
cc. 174r-175v  est  1355  plain 1240 (92%)  no hole 697 (51%)  blocks 21/37  clean 260 (19%) blocks 11  verbatim 216 (16%)  repairs 15  doubtful 43  holes 23  codes 10
without 175r   est  1023  plain 943 (92%)   no hole 636 (62%)  blocks 19/28  clean 199 (19%) blocks 9  verbatim 199 (19%)  repairs 9  doubtful 32  holes 12  codes 8
```

Après :
```
c. 78r         est   349  plain 335 (96%)   no hole 226 (65%)  blocks 7/11  clean 113 (32%) blocks 4  verbatim 113 (32%)  repairs 1  doubtful 11  holes 6  codes 5
c. 78v         est   296  plain 275 (93%)   no hole 126 (43%)  blocks 5/10  clean 51 (17%)  blocks 2  verbatim 15 (5%)    repairs 1  doubtful 10  holes 6  codes 0
c. 79r         est   142  plain 108 (76%)   no hole 33 (23%)   blocks 2/5  clean 20 (14%)  blocks 1  verbatim 20 (14%)   repairs 1  doubtful 1  holes 4  codes 1
c. 174r        est   321  plain 315 (98%)   no hole 149 (46%)  blocks 5/10  clean 80 (25%)  blocks 4  verbatim 80 (25%)   repairs 3  doubtful 7  holes 5  codes 0
c. 174v        est   358  plain 341 (95%)   no hole 296 (83%)  blocks 8/9  clean 42 (12%)  blocks 2  verbatim 42 (12%)   repairs 1  doubtful 17  holes 2  codes 4
c. 175r        est   334  plain 297 (89%)   no hole 61 (18%)   blocks 2/9  clean 61 (18%)  blocks 2  verbatim 17 (5%)    repairs 7  doubtful 11  holes 11  codes 2
c. 175v        est   344  plain 287 (83%)   no hole 191 (56%)  blocks 6/9  clean 77 (22%)  blocks 3  verbatim 77 (22%)   repairs 4  doubtful 8  holes 5  codes 4
cc. 78r-79r    est   787  plain 718 (91%)   no hole 385 (49%)  blocks 14/26  clean 184 (23%) blocks 7  verbatim 148 (19%)  repairs 3  doubtful 22  holes 16  codes 6
cc. 174r-175v  est  1356  plain 1240 (91%)  no hole 697 (51%)  blocks 21/37  clean 260 (19%) blocks 11  verbatim 216 (16%)  repairs 15  doubtful 43  holes 23  codes 10
without 175r   est  1023  plain 943 (92%)   no hole 636 (62%)  blocks 19/28  clean 199 (19%) blocks 9  verbatim 199 (19%)  repairs 8  doubtful 32  holes 12  codes 8
```
