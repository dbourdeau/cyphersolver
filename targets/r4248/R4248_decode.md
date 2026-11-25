# R4248, f. 85r-v: the cipher decoded sign by sign (14 Nov 2026)

Made from `R4248_transcription.txt` (the signs as written, read on the Gallica scans of BnF fr. 3053, views 157-158)
with one value per sign label. The values are those of S. Tomokiyo's second fr. 3053 table (`img/francisMacon2.png`)
where a sign could be matched to it, fixed on the contemporary decipherment of f. 86 where it could not. A single AI
transcription and decode (Claude, session of 14 Nov 2026), not checked by a person.

Word division, apostrophes and i/j, u/v are added; no letter is changed. `[..]` in roman = clear words of the letter
standing between the cipher runs (read at a glance on the scan, not a transcription). `[CL]` = one sign with no letter
value, standing where the f. 86 decipherment names the cardinal de Lorraine. `[?..]` = letters as decoded that make no
word. `{x}` = a letter the decode lacks or doubles, shown so the word can be read. Nulls (30, 22, 19, the
three-barred cross, the 3 in a curve) are dropped.

## f. 85r

que toutes ch{o}ses et particulierement celles de la guerre avoient a passer par voz mains [et partant] je le
conseillois de s'adreser et faire fondement dessus vous, qu'est et le scavoir et le pouvoir [et que toute aultre
chose estoit fumee et vent. Je luy dys davantaige] qu'il debveroient totallement se remettr{r}e en vostre jugement
tant de la maniere de faire la guerre [Comme] du lieu et du temps [Parce que en fin il falloit] tout home {f}ist son
mestier et ceulx qui le {f}ont le mieul{x} sont les plus pratic[?i]

## f. 85v

[... Que] le [CL] par les capitulations faictes avec le [?i] avoit acorde choses ausquelles [au paravant] ilz
n'avoient jamais pense, comme de [?aaiette] [et daultres quil me nomma. Adjoustant par apres ces mesmes parolles]
qu'ilz estoie{n}t deliberez par vostre moien reordonner les conditions passe{e}s par ledict seigneur [CL] [par ce
quilz] congnoisoient qu'il leur avoit plus concede que n'estoit le debvoir [et que] eulx mesmes ne vouloient [Mais
que] a vous seroit remise toute capitulation de qui ilz vouloie{n}t entierement dependre, congnoisant ung seur
fondement aux choses qui passe{n}t par voz mains [Il me dist aussi quil]

## Raw decode, line by line

`_` = null, `I` = the ringed x (i or j; it also stands where x and the word "pape" are expected), `R` = the barred
oval (r in lines 2-3, h in line 15: two look-alike signs not told apart), `/` = a struck sign.

```
L01 __quetouteschcsesetpartIculi
L02 eRement_cellesdelaguerre_auoient
L03 apasserpaRuozmains [et partant] Ie__le
L04 conseilloisdesadreseretfairefo
L05 ndementdessusuousquest_etlescauo
L06 iretlepouoir [et que toute aultre chose estoit fumee]
L07 [et vent Je luy dys davantaige] __quildebueroie
L08 nttotallementseremettrreenuostreiu
L09 gementtantdelamanieredefairelaguer
L10 re [Comme] __dulieuetdutemps [Parce que en fin]
L11 [Il falloit] _touthome/istsonmestieretceul
L12 xquilecontlemieulIsontlespluspraticI
L13 le<CL>parlesca
L14 pitulationsfaictesauecleIauoitacorde
L15 cRosesausquelles [au paravant] _ilznauoientia
L16 maispensecommedeaaiette [et daultres quil me]
L17 [nomma. Adjoustant par apres ces mesmes parolles] ___quilz
L18 estoietdeliberezparuostremoienreor
L19 donnerlesconditIonspassesparledic
L20 tseigneur<CL> [par ce quilz] _congnoisoientquil
L21 leurauoitplusconcedequenestoitledeb
L22 uoir [et que] _eulxmesmesneuouloient [Mais que]
L23 auousseroitremisetoutecapitulationde
L24 quiIlzuouloietentierementdependre
L25 congnoisantungseurfondementauxchos
L26 equipassetparuozmains [Il me dist aussi quil]
```

## Values used (label = value)

e, m = e · # x oo = a · b- = b · o- 8 c) = c (c) also stands for o in line 1) · z to o-o = d · X X# df = f · p = g ·
bh = h · ~ L = i · k oHo C = q · 7 11 5 = l · mz M2 = m · a 4 = n · 3 = o · S8 H = p · Lp W = r · y Y qq = s ·
b ph St = t · al d = u/v · f = x · zt = z · nulls 30, 22, 19, N3, G3.

## Where the cipher differs from the f. 86 decipherment as transcribed in R4248.md

| R4248.md (f. 86, about 85 % of words secure) | the cipher |
|---|---|
| de s'adresser a faire fondement de vous seul, car c'est a scavoir le premier [pouvoir?] | de s'adreser et faire fondement dessus vous, qu'est et le scavoir et le pouvoir |
| qu'il cognoistroit totallement le [Roy?] en ce jugement | qu'il debveroient totallement se remettre en vostre jugement |
| comme au lieu et du temps | comme du lieu et du temps |
| que tout homme feist son mestier | tout home [f]ist son mestier |
| par la cappitulacion faicte | par les capitulations faictes |
| comme de partir [?] | comme de [?aaiette] (not read) |
| par leurs moyens [de] rompre [?] les conditions | par vostre moien reordonner les conditions |
| toute l'application de qui vouldroient entierement se rendre | toute capitulation de qui ilz vouloient entierement dependre |
| ung seul fondement aux choses qui passeroient | ung seur fondement aux choses qui passent |

The f. 86 scan (view 159) was not re-read in this session, so these are differences between the cipher and the
September transcription of f. 86, not shown differences between the cipher and f. 86 itself.
