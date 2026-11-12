# Holes: every word unit of the nine held-out pages that is not counted read

Written by scripts/build.py from units.tsv. A unit is a hole when its class is E or N (rule in scripts/build.py), after overrides.tsv.
The reason column is the script's reading of the decoded form, not a hand classification.

## 1. Totals by page

| page | units | S | E | N | gutter cut | no value (code or sign) | weak value | flagged by reader or overrides.tsv |
|---|---|---|---|---|---|---|---|---|
| f306r_321R | 47 | 33 | 12 | 2 | 0 | 10 | 1 | 2 |
| f306v_322L | 120 | 73 | 39 | 8 | 23 | 16 | 4 | 8 |
| f307r_322R | 111 | 94 | 13 | 4 | 0 | 7 | 4 | 5 |
| f307v_323L | 100 | 71 | 26 | 3 | 20 | 6 | 1 | 4 |
| f308r_323R | 104 | 83 | 18 | 3 | 1 | 14 | 5 | 3 |
| f309v_325L | 82 | 50 | 30 | 2 | 16 | 10 | 5 | 5 |
| f310r_325R | 83 | 62 | 16 | 5 | 0 | 10 | 7 | 5 |
| f310v_326L | 72 | 47 | 20 | 5 | 8 | 6 | 4 | 7 |
| f311r_326R | 45 | 33 | 9 | 3 | 0 | 5 | 5 | 3 |
| all | 764 | 546 | 183 | 35 | 68 | 84 | 36 | 42 |

A unit can fall in more than one of the last four columns.

## 2. Numbers with no value in key v3, as they occur in the nine pages

| number | occurrences | pages | key row | sense from context (not read) |
|---|---|---|---|---|
| 99 | 19 | f306r_321R x4, f306v_322L x9, f307v_323L x1, f308r_323R x3, f309v_325L x1, f310r_325R x1 | not in key | st (proposed after the test; not counted) |
| 44 | 6 | f306v_322L x2, f308r_323R x1, f309v_325L x1, f310r_325R x1, f310v_326L x1 | not in key | x (proposed after the test; not counted) |
| 173 | 5 | f306r_321R x1, f306v_322L x1, f307r_322R x2, f309v_325L x1 | not in key | null? |
| 109 | 4 | f308r_323R x3, f309v_325L x1 | not in key | ff (proposed after the test; not counted) |
| 120 | 4 | f308r_323R x1, f309v_325L x2, f310v_326L x1 | not in key | q (proposed after the test; not counted) |
| 129 | 4 | f308r_323R x1, f310r_325R x2, f310v_326L x1 | not in key | y (proposed after the test; not counted) |
| 176 | 4 | f306v_322L x1, f307r_322R x2, f308r_323R x1 | (null?) U | null? |
| 3 | 3 | f311r_326R x3 | not in key | null? |
| 76 | 3 | f306r_321R x1, f307v_323L x1, f310v_326L x1 | not in key | g (proposed after the test; not counted) |
| 124 | 3 | f306r_321R x2, f308r_323R x1 | not in key | st (proposed after the test; not counted) |
| 145 | 3 | f308r_323R x2, f310r_325R x1 | not in key | l (proposed after the test; not counted) |
| 162 | 3 | f307v_323L x1, f309v_325L x1, f310r_325R x1 | not in key | o (proposed after the test; not counted) |
| 111 | 2 | f306v_322L x1, f310r_325R x1 | not in key | h (proposed after the test; not counted) |
| 175 | 2 | f306v_322L x1, f310r_325R x1 | not in key | null? |
| 178 | 2 | f306r_321R x1, f310r_325R x1 | not in key | null? |
| 314 | 2 | f307v_323L x1, f308r_323R x1 | Danmarck W | Danmarck (1675 gloss; counted not read by rule) |
| 4 | 1 | f310v_326L x1 | not in key | null? |
| 8 | 1 | f310v_326L x1 | not in key | null? |
| 115 | 1 | f310r_325R x1 | not in key | ll (proposed after the test; not counted) |
| 123 | 1 | f307v_323L x1 | not in key | ss (proposed after the test; not counted) |
| 130 | 1 | f311r_326R x1 | not in key | p (proposed after the test; not counted) |
| 134 | 1 | f311r_326R x1 | not in key | h (proposed after the test; not counted) |
| 139 | 1 | f309v_325L x1 | not in key | ll (proposed after the test; not counted) |
| 155 | 1 | f307v_323L x1 | not in key | x (proposed after the test; not counted) |
| 157 | 1 | f309v_325L x1 | not in key | st (proposed after the test; not counted) |
| 174 | 1 | f307r_322R x1 | not in key | null? |
| 177 | 1 | f309v_325L x1 | not in key | null? |
| 240 | 1 | f306v_322L x1 | not in key |  |
| 245 | 1 | f306r_321R x1 | not in key |  |
| 267 | 1 | f307r_322R x1 | not in key | alliance |
| 324 | 1 | f307r_322R x1 | not in key | discours |
| 463 | 1 | f306v_322L x1 | not in key | reputation? |

## 3. Every hole

| page | unit | decoded | class | reading | not read because |
|---|---|---|---|---|---|
| f306r_321R | 2 | `besoin<76>` | E | besoing | no value for 76 |
| f306r_321R | 3 | `de<99>re` | E | d'estre | no value for 99 |
| f306r_321R | 9 | `e<124>re` | E | estre | no value for 124 |
| f306r_321R | 14 | `<245>` | E |  | no value for 245 |
| f306r_321R | 16 | `uiltoire` | N | victoire | flagged N by the reader (key gives a wrong letter, or no reading) |
| f306r_321R | 17 | `<173>` | E |  | no value for 173 |
| f306r_321R | 20 | `maie<99>e` | E | maiesté | no value for 99 |
| f306r_321R | 22 | `biento<99>` | E | bientost | no value for 99 |
| f306r_321R | 24 | `e<124>at` | E | estat | no value for 124 |
| f306r_321R | 27 | `moåen` | N | moyen | flagged N by the reader (key gives a wrong letter, or no reading) |
| f306r_321R | 37 | `re<99>ablir` | E | restablir | no value for 99 |
| f306r_321R | 42 | `aÅaires` | E | affaires |  |
| f306r_321R | 44 | `<178>` | E |  | no value for 178 |
| f306r_321R | 47 | `malemLgne` | E | d'alemagne? | weak C-tier value |
| f306v_322L | 1 | `lo<99>re` | E | vostre | no value for 99 |
| f306v_322L | 2 | `maiest[~]` | E | maiesté | numeral cut at the gutter or edge |
| f306v_322L | 4 | `<240>` | E |  | no value for 240 |
| f306v_322L | 5 | `uoudroet` | N | voudroit | flagged N by the reader (key gives a wrong letter, or no reading) |
| f306v_322L | 7 | `fai` | N | fait | flagged N by the reader (key gives a wrong letter, or no reading) |
| f306v_322L | 10 | `declara[~]ons` | E | declarations | numeral cut at the gutter or edge |
| f306v_322L | 12 | `<173>` | E |  | no value for 173 |
| f306v_322L | 17 | `itere<99>` | E | interest | no value for 99 |
| f306v_322L | 24 | `efec[~]` | E | effects | numeral cut at the gutter or edge |
| f306v_322L | 25 | `que<99>ion` | E | question | no value for 99 |
| f306v_322L | 26 | `de<44>[~]cuter` | E | d'executer | numeral cut at the gutter or edge; no value for 44 |
| f306v_322L | 29 | `u[~]loir` | E | valoir | numeral cut at the gutter or edge |
| f306v_322L | 31 | `iu<99>ice` | E | iustice | no value for 99 |
| f306v_322L | 33 | `[~]L` | E | la | numeral cut at the gutter or edge; weak C-tier value |
| f306v_322L | 37 | `<175>` | E |  | no value for 175 |
| f306v_322L | 39 | `Lmis` | E | amis | weak C-tier value |
| f306v_322L | 40 | `secouri[~]` | E | secourir | numeral cut at the gutter or edge |
| f306v_322L | 43 | `mal<111>eureu<44>` | E | malheureux | no value for 111; no value for 44 |
| f306v_322L | 45 | `de<99>ruction` | E | destruction | no value for 99 |
| f306v_322L | 48 | `e<99>L[~]` | E | estats | numeral cut at the gutter or edge; no value for 99; weak C-tier value |
| f306v_322L | 52 | `le[~]` | E | les | numeral cut at the gutter or edge |
| f306v_322L | 55 | `uo<99>re` | E | vostre | no value for 99 |
| f306v_322L | 56 | `maie[~]` | E | maiesté | numeral cut at the gutter or edge |
| f306v_322L | 60 | `[~]` | E |  | numeral cut at the gutter or edge |
| f306v_322L | 63 | `<176>` | E |  | no value for 176 |
| f306v_322L | 65 | `da[~]urer` | E | d'assurer | numeral cut at the gutter or edge |
| f306v_322L | 67 | `conque<99>es` | E | conquestes | no value for 99 |
| f306v_322L | 68 | `ee` | N | et | flagged N by the reader (key gives a wrong letter, or no reading) |
| f306v_322L | 69 | `d[~]fermir` | E | d'affermir | numeral cut at the gutter or edge |
| f306v_322L | 72 | `g[~]oire` | E | gloire | numeral cut at the gutter or edge |
| f306v_322L | 73 | `ee` | N | et | flagged N by the reader (key gives a wrong letter, or no reading) |
| f306v_322L | 75 | `<463>` | E |  | no value for 463 |
| f306v_322L | 82 | `uoler` | N | violer | flagged N by the reader (key gives a wrong letter, or no reading) |
| f306v_322L | 85 | `tr[~]ittes` | E | traittes | numeral cut at the gutter or edge |
| f306v_322L | 86 | `e<99>es` | E | estes | no value for 99 |
| f306v_322L | 88 | `garan[~]` | E | garant | numeral cut at the gutter or edge |
| f306v_322L | 92 | `preu[~]nir` | E | prevenir | numeral cut at the gutter or edge |
| f306v_322L | 96 | `prep[~]rä` | E | prepare | numeral cut at the gutter or edge |
| f306v_322L | 100 | `ge[~]rosite` | E | generosité | numeral cut at the gutter or edge |
| f306v_322L | 104 | `lonne` | N | bonne | flagged N by the reader (key gives a wrong letter, or no reading) |
| f306v_322L | 105 | `fo[~]` | E | foy | numeral cut at the gutter or edge |
| f306v_322L | 108 | `laisse[~]` | E | laisser | numeral cut at the gutter or edge |
| f306v_322L | 111 | `Llies` | E | allies | weak C-tier value |
| f306v_322L | 112 | `bandonner` | N | abandonner | flagged N by the reader (key gives a wrong letter, or no reading) |
| f306v_322L | 115 | `uo[~]lu` | E | voulu | numeral cut at the gutter or edge |
| f306v_322L | 116 | `sacricier` | N | sacrifier | flagged N by the reader (key gives a wrong letter, or no reading) |
| f306v_322L | 120 | `regnen[~]` | E | regnent | numeral cut at the gutter or edge |
| f307r_322R | 18 | `<173>` | E |  | no value for 173 |
| f307r_322R | 20 | `Lmås` | E | amys | weak C-tier value |
| f307r_322R | 21 | `enes` | N | eles | flagged N by the reader (key gives a wrong letter, or no reading) |
| f307r_322R | 26 | `<176>` | E |  | no value for 176 |
| f307r_322R | 32 | `l<267>` | E | l'alliance | no value for 267 |
| f307r_322R | 38 | `rLssureront` | E | rassureront | weak C-tier value |
| f307r_322R | 45 | `<176>` | E |  | no value for 176 |
| f307r_322R | 51 | `<324>` | E |  | no value for 324 |
| f307r_322R | 53 | `iuil` | N | quil | flagged N by the reader (key gives a wrong letter, or no reading) |
| f307r_322R | 67 | `<174>` | E |  | no value for 174 |
| f307r_322R | 77 | `scauroet` | N | scauroit | flagged N by the reader (key gives a wrong letter, or no reading) |
| f307r_322R | 83 | `tLnt` | E | tant | weak C-tier value |
| f307r_322R | 90 | `reconuuerir` | N | reconquerir | flagged N by the reader (key gives a wrong letter, or no reading) |
| f307r_322R | 99 | `<173>` | E |  | no value for 173 |
| f307r_322R | 106 | `eÅorts` | E | efforts |  |
| f307r_322R | 108 | `lL` | E | la | weak C-tier value |
| f307r_322R | 111 | `d` | E | (catchword) | flagged E by the reader (emended) |
| f307v_323L | 2 | `rassLmbl[~]nt` | E | rassamblent | numeral cut at the gutter or edge; weak C-tier value |
| f307v_323L | 5 | `emp[~]oåer` | E | employer | numeral cut at the gutter or edge |
| f307v_323L | 8 | `uostr[~]` | E | vostre | numeral cut at the gutter or edge |
| f307v_323L | 11 | `[~]ux` | E | aux | numeral cut at the gutter or edge |
| f307v_323L | 16 | `rehau<123>ent` | E | rehaussent | no value for 123 |
| f307v_323L | 20 | `maintenan[~]` | E | maintenant | numeral cut at the gutter or edge |
| f307v_323L | 32 | `prendr[~]` | E | prendre | numeral cut at the gutter or edge |
| f307v_323L | 35 | `i[~]certain` | E | incertain | numeral cut at the gutter or edge |
| f307v_323L | 38 | `fortun[~]` | E | fortune | numeral cut at the gutter or edge |
| f307v_323L | 43 | `[~]econdes` | E | secondes | numeral cut at the gutter or edge |
| f307v_323L | 48 | `iusque[~]` | E | iusques | numeral cut at the gutter or edge |
| f307v_323L | 52 | `pa[~]` | E | par | numeral cut at the gutter or edge |
| f307v_323L | 53 | `leles` | N | belles | flagged N by the reader (key gives a wrong letter, or no reading) |
| f307v_323L | 55 | `glorieuse[~]` | E | glorieuses | numeral cut at the gutter or edge |
| f307v_323L | 56 | `acti<162>ns` | E | actions | no value for 162 |
| f307v_323L | 64 | `roå` | N | roy | 66 = å in key v3; word needs y (roy) |
| f307v_323L | 66 | `<314>` | E | Danemarc | no value for 314 |
| f307v_323L | 68 | `nu[~]åer` | E | envoyer | numeral cut at the gutter or edge |
| f307v_323L | 72 | `d` | E | de | flagged E by the reader (emended) |
| f307v_323L | 76 | `troupp[~]` | E | trouppes | numeral cut at the gutter or edge |
| f307v_323L | 79 | `uaisseau<155>` | E | vaisseaux | no value for 155 |
| f307v_323L | 80 | `prop[~]tionne` | E | proportionne | numeral cut at the gutter or edge |
| f307v_323L | 84 | `[~]` | E | du | numeral cut at the gutter or edge |
| f307v_323L | 85 | `dan<76>er` | E | danger | no value for 76 |
| f307v_323L | 87 | `moåen` | N | moyen | 66 = å in key v3; word needs y (moyen) |
| f307v_323L | 90 | `no[~]` | E | nous | numeral cut at the gutter or edge |
| f307v_323L | 92 | `re<99>ab[~]r` | E | restablir | numeral cut at the gutter or edge; no value for 99 |
| f307v_323L | 97 | `cau[~]` | E | cause | numeral cut at the gutter or edge |
| f307v_323L | 100 | `l[~]` | E | le | numeral cut at the gutter or edge |
| f308r_323R | 7 | `<176>` | E | (sign) | no value for 176 |
| f308r_323R | 11 | `Lu` | E | au | weak C-tier value |
| f308r_323R | 14 | `<314>` | E | Danemarc | no value for 314 |
| f308r_323R | 17 | `L` | E | a | weak C-tier value |
| f308r_323R | 18 | `l[~]` | E | la | numeral cut at the gutter or edge |
| f308r_323R | 22 | `aåant` | N | ayant | 66 = å in key v3; word needs y (ayant) |
| f308r_323R | 23 | `<145>Lisse` | E | laisse | no value for 145; weak C-tier value |
| f308r_323R | 29 | `nå` | N | ny | 66 = å in key v3; word needs y (ny) |
| f308r_323R | 39 | `au<44>` | E | aux | no value for 44 |
| f308r_323R | 42 | `ro<129>aume` | E | royaume | no value for 129 |
| f308r_323R | 43 | `a<109>lige` | E | afflige | no value for 109 |
| f308r_323R | 51 | `<120>ue` | E | que | no value for 120 |
| f308r_323R | 54 | `<145>a` | E | la | no value for 145 |
| f308r_323R | 67 | `in<99>Lnces` | E | instances | no value for 99; weak C-tier value |
| f308r_323R | 73 | `humllement` | N | humblement | flagged N by the reader (key gives a wrong letter, or no reading) |
| f308r_323R | 75 | `uo<99>re` | E | vostre | no value for 99 |
| f308r_323R | 76 | `maie<99>e` | E | maieste | no value for 99 |
| f308r_323R | 78 | `maie<124>e` | E | maieste | no value for 124 |
| f308r_323R | 82 | `Lmitie` | E | amitie | weak C-tier value |
| f308r_323R | 96 | `di<109>iculte` | E | difficulte | no value for 109 |
| f308r_323R | 101 | `e<109>ort` | E | effort | no value for 109 |
| f309v_325L | 2 | `<173>` | E | (sign) | no value for 173 |
| f309v_325L | 3 | `ene` | N | elle | flagged N by the reader (key gives a wrong letter, or no reading) |
| f309v_325L | 4 | `se<99>` | E | sest | no value for 99 |
| f309v_325L | 5 | `gl[~]rieusement` | E | glorieusement | numeral cut at the gutter or edge |
| f309v_325L | 6 | `ac<120>uis` | E | acquis | no value for 120 |
| f309v_325L | 8 | `di<109>erentes` | E | differentes | no value for 109 |
| f309v_325L | 9 | `uictoirs` | E | victoires | flagged E by the reader (emended) |
| f309v_325L | 12 | `e<139>e` | E | elle | no value for 139 |
| f309v_325L | 13 | `d[~]` | E | de | numeral cut at the gutter or edge |
| f309v_325L | 16 | `mesure[~]` | E | mesures | numeral cut at the gutter or edge |
| f309v_325L | 18 | `de[~]` | E | des | numeral cut at the gutter or edge |
| f309v_325L | 22 | `soi[~]` | E | soit | numeral cut at the gutter or edge |
| f309v_325L | 26 | `decLration` | E | declaration | weak C-tier value |
| f309v_325L | 28 | `lL` | E | la | weak C-tier value |
| f309v_325L | 29 | `pai<44>[~]` | E | paix | numeral cut at the gutter or edge; no value for 44 |
| f309v_325L | 33 | `resolut[~]on` | E | resolution | numeral cut at the gutter or edge |
| f309v_325L | 34 | `Lpres` | E | apres | weak C-tier value |
| f309v_325L | 37 | `l` | E | le | flagged E by the reader (emended) |
| f309v_325L | 42 | `[~]acrifiLnt` | E | sacrifiant | numeral cut at the gutter or edge; weak C-tier value |
| f309v_325L | 44 | `con<120>uest[~]` | E | conquestes | numeral cut at the gutter or edge; no value for 120 |
| f309v_325L | 48 | `quene` | N | quelle | flagged N by the reader (key gives a wrong letter, or no reading) |
| f309v_325L | 50 | `uoudr[~]it` | E | voudroit | numeral cut at the gutter or edge |
| f309v_325L | 58 | `rmettre` | E | remettre | flagged E by the reader (emended) |
| f309v_325L | 60 | `possessi<162>n` | E | possession | no value for 162 |
| f309v_325L | 62 | `[~]places` | E | places | numeral cut at the gutter or edge |
| f309v_325L | 67 | `intere[~]` | E | interest | numeral cut at the gutter or edge |
| f309v_325L | 70 | `tou[~]` | E | toute | numeral cut at the gutter or edge |
| f309v_325L | 73 | `gen[~]rosite` | E | generosite | numeral cut at the gutter or edge |
| f309v_325L | 74 | `Luroit` | E | auroit | weak C-tier value |
| f309v_325L | 76 | `traitt[~]` | E | traittes | numeral cut at the gutter or edge |
| f309v_325L | 80 | `<177>` | E | (sign) | no value for 177 |
| f309v_325L | 82 | `uo<157>r[~]` | E | vostre | numeral cut at the gutter or edge; no value for 157 |
| f310r_325R | 1 | `maie<99>e` | E | maieste | no value for 99 |
| f310r_325R | 7 | `lL` | E | la | weak C-tier value |
| f310r_325R | 11 | `a<115>ies` | E | allies | no value for 115 |
| f310r_325R | 15 | `fLsse` | E | fasse | weak C-tier value |
| f310r_325R | 18 | `<145>Lrticle` | E | larticle | no value for 145; weak C-tier value |
| f310r_325R | 33 | `luå` | N | luy | 66 = å in key v3; word needs y (luy) |
| f310r_325R | 35 | `a<129>e` | E | aye | no value for 129 |
| f310r_325R | 37 | `satisfLction` | E | satisfaction | weak C-tier value |
| f310r_325R | 43 | `lL` | E | la | weak C-tier value |
| f310r_325R | 47 | `anies` | N | alies | flagged N by the reader (key gives a wrong letter, or no reading) |
| f310r_325R | 49 | `så` | N | sy | 66 = å in key v3; word needs y (sy) |
| f310r_325R | 51 | `n<129>` | E | ny | no value for 129 |
| f310r_325R | 53 | `<111>olandois` | E | hollandois | no value for 111 |
| f310r_325R | 56 | `lapplLudir` | E | lapplaudir | weak C-tier value |
| f310r_325R | 58 | `<178>` | E | (sign) | no value for 178 |
| f310r_325R | 61 | `<175>` | E | (sign) | no value for 175 |
| f310r_325R | 64 | `pai<44>` | E | paix | no value for 44 |
| f310r_325R | 65 | `<162>u` | E | ou | no value for 162 |
| f310r_325R | 70 | `anies` | N | alies | flagged N by the reader (key gives a wrong letter, or no reading) |
| f310r_325R | 77 | `då` | N | dy | 66 = å in key v3; word needs y (dy) |
| f310r_325R | 82 | `abLndonnes` | E | abandonnes | weak C-tier value |
| f310v_326L | 4 | `setimens` | E | sentimens | flagged E by the reader (emended) |
| f310v_326L | 8 | `m[~]lheureuse` | E | malheureuse | numeral cut at the gutter or edge |
| f310v_326L | 11 | `nå` | N | ny | 66 = å in key v3; word needs y (ny) |
| f310v_326L | 13 | `bie[~]` | E | bien | numeral cut at the gutter or edge |
| f310v_326L | 14 | `nå` | N | ny | 66 = å in key v3; word needs y (ny) |
| f310v_326L | 18 | `lL` | E | la | weak C-tier value |
| f310v_326L | 24 | `commi[~]ce` | N | commerce | flagged N by the reader (key gives a wrong letter, or no reading); numeral cut at the gutter or edge |
| f310v_326L | 25 | `prouinc[~]s` | E | prouinces | numeral cut at the gutter or edge |
| f310v_326L | 26 | `estLnt` | E | estant | weak C-tier value |
| f310v_326L | 32 | `n<129>` | E | ny | no value for 129 |
| f310v_326L | 41 | `dun` | E | dune | flagged E by the reader (emended) |
| f310v_326L | 42 | `louan<76>e` | E | louange | no value for 76 |
| f310v_326L | 43 | `suÅire` | E | suffire |  |
| f310v_326L | 45 | `<8>` | E | (sign) | no value for 8 |
| f310v_326L | 46 | `le<44>cessiue` | E | lexcessive | no value for 44 |
| f310v_326L | 49 | `fair[~]` | E | faire | numeral cut at the gutter or edge |
| f310v_326L | 51 | `<120>ue` | E | que | no value for 120 |
| f310v_326L | 52 | `uo[~]re` | E | vostre | numeral cut at the gutter or edge |
| f310v_326L | 54 | `suppleer[~]` | E | suppleera | numeral cut at the gutter or edge |
| f310v_326L | 60 | `extrLordinaire` | E | extraordinaire | weak C-tier value |
| f310v_326L | 64 | `luå` | N | luy | 66 = å in key v3; word needs y (luy) |
| f310v_326L | 68 | `ser[~]it` | E | seroit | numeral cut at the gutter or edge |
| f310v_326L | 69 | `amploåee` | N | amployee | 66 = å in key v3; word needs y (amployee) |
| f310v_326L | 71 | `<4>` | E | (sign) | no value for 4 |
| f310v_326L | 72 | `Lchete` | E | acheter | weak C-tier value |
| f311r_326R | 4 | `bouchs` | N | bouche | flagged N by the reader (key gives a wrong letter, or no reading) |
| f311r_326R | 11 | `än` | N | en | flagged N by the reader (key gives a wrong letter, or no reading) |
| f311r_326R | 12 | `<134>olande` | E | hollande | no value for 134 |
| f311r_326R | 15 | `<3>` | E | (sign) | no value for 3 |
| f311r_326R | 18 | `L` | E | a | weak C-tier value |
| f311r_326R | 19 | `<3>` | E | (sign) | no value for 3 |
| f311r_326R | 24 | `<130>omerLnie` | E | pomeranie | no value for 130; weak C-tier value |
| f311r_326R | 26 | `lL` | E | la | weak C-tier value |
| f311r_326R | 27 | `conseruLtion` | E | conservation | weak C-tier value |
| f311r_326R | 35 | `L` | E | a | weak C-tier value |
| f311r_326R | 36 | `<3>` | E | (sign) | no value for 3 |
| f311r_326R | 40 | `luå` | N | luy | 66 = å in key v3; word needs y (luy) |
