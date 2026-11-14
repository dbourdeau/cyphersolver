# f. 370: figures aligned with the Brienne 13 clear copy (r2f, 23 Oct 2026)

What was checked: every visible cipher group of f. 370r (31 lines, view 419 right page) and f. 370v (32 lines, view 420
left page) transcribed from the native openapi.bnf.fr images (`f370_figures.txt`, 2,298 groups, 42 marked uncertain),
decoded with Tomokiyo's key (`../key1.tsv`) and aligned letter by letter with the copy (`f370_brienne_copy.txt`) by
`research/reading_audit/r2f_align370.py`. The alignment runs from the first copy letter to the last: the copy is this
letter, from *Le Cardinal de Gondy* to *... conservation de cette Couronne*.

## Agreement

| | letters |
|---|---|
| copy letters carried by figures that agree | 2,255 |
| copy letters where the figure gives another letter | 45 |
| copy letters with no figure (omitted by the encipherer or misread) | 10 |
| extra figure letters not in the copy | 26 |
| copy letters under an abbreviation bar (v~re, occa~on, l~res, aud~, mesd~, s.r) | 65 |
| copy letters under a code group (23 pape x2, 24 Roy d'Espagne, 48 ambassadeur, 49 guerre) | 36 |
| copy letters at line ends hidden in the binding gutter of f. 370v | 147 |

**Letter agreement 97.6%** (2,255 of the 2,310 copy letters the figures cover, codes and abbreviations aside). By copy
word: 579 words; 491 agree (464 letter for letter, 20 abbreviated, 7 under code groups); 40 differ; 48 fall wholly or
partly in the gutter.

## The differences, and what the reading does with them

**Wording: the reading follows the figures.**
- *vous ne vouldrez deffaillir* (copy) / figures *uouldriez defaillir* (r14)
- *y adioustiez et retranchiez* / figures *y adioustiez ou restraigniez* (r25-26)
- *les choses qui concernent mon service* / figures *les choses concernans mon service* (v02)
- *d'y estre traictez* / figures *traictees* (v04; agrees with *les choses*)
- *desquelz ie sçay* / figures *lesquel[z]* (v11; the last group at the gutter)
- *que s'il estoit en ses propres pais* / figures *que si c'estoit ...* (v13)
- copy *[?vangez]* / figures *uengez* (v20); the copy's doubtful *[?convier]*, *[?veoir]*, *[?verrons]* are confirmed by
  the figures (v19, v20, v24).

**Spelling: the reading follows the figures.** besoin/besoing (r12: the group 2 after *besoin* is the g),
abandonnées/habandonnées (r12, h = 3), suiuy/suyuy (r05), addresse/adresse, afin/affin (twice), voiez/voyez,
propos/propoz, cognoissance/connoissance (68 = nn), presque/presques, desseins/desseings, deborde/desborde,
moiens/moyens (twice), peut/peult, amis/amiz, nuire/nuyre, eschauffer/eschaufer, deffaillir/defaillir, cette/ceste
(Couronne).

**Enciphering slips (or figures read doubtfully): the reading keeps the copy.** *sois parsz sisost* for *soit passé
sitost* (r18: 17 for 18 three times, 16 17 22 for s s e); *saruice* (r14, 7 for 11), *bian* (r13), *uoue* and *faics*
(r07), *seulerent* and *dextrerent* (v00, v23: 16 for 6 in *-ment*), *piecont* (v19, 9 for 6), *faicdes* (v26),
*apres apres* (v27, the word enciphered twice), *d'icelles* (v02, against the singular *depesche*), *laquell* (r03, final
e missing at the line end), *mesa affaires* (r11, a struck 7), *quelques* (r02, look-alike 7/17 before *iours*),
*anant* (r18, 12 read for 4), *aueci* (r23), *sIais* for *pais* (v14, 14 read as 4), *Pcontrainbt* (v29: a clear 8 written for 9, *contrainct*; read `9?` until the image check of 14 Nov 2026).

**Unidentified:** 90 at the end of r01 (between *ia* and *auoir*), probably a null.

**Key additions found here** (decoded consistently, grade C, from the copy): 71 = rr (*arriuer* v01, *pou[rr]ont*
v03, *angleter[rr]e* v06); 73 = tt (*a[tt]endant* v29; key1.tsv had 73 = uu from Tomokiyo's table, where 73 stands
unlabelled under u; 71 rr, 72 ss, 73 tt keep the alphabetical order of the doubles 66 ff, 67 mm, 68 nn); codes
23 = pape (r06 *le 23 au nom des Catholiques*, v25 *les resolutions du 23*), 24 = Roy d'Espagne (v12; Savasse's value
from Maisse's 1590 letters), 48 = ambassadeur (v06 *a l 48 d angleterre*), 49 = guerre (v18 *la 49 que le s.r
Desdiguieres a ouuerte*). Savasse's 23 = votre Majesté / le roi does not hold here: 23 is the Pope in both places.

**Not visible:** 147 copy letters at the right ends of verso lines v00-v30, which run into the binding gutter
(G in `f370_figures.txt`); blocker needs-physical-access. The copy is the only witness there.

## Line by line (figures decoded above, copy below; capitals = disagreement, ~ abbreviation, # code, _ gutter)

```
r00 fig : lecardinal
r00 copy: lecardinal
r01 fig : degondyaurapassepresdeuousilypeultia#
r01 copy: degondyaurapassepresdeuousilypeultia-
r02 fig : auoirquelqueSiourslequeluousaurafaictenten
r02 copy: auoirquelque-iourslequeluousaurafaictenten
r03 fig : dredemesnouuellesetladispositionenlaquell-
r03 copy: dredemesnouuellesetladispositionenlaquellE
r04 fig : ilauralaisseleschosespardecadestrebientost
r04 copy: ilauralaisseleschosespardecadestrebientost
r05 fig : suYuyparlemarquisdepisanypouralleruersle
r05 copy: suIuyparlemarquisdepisanypouralleruersle
r06 fig : ####aunomdescatholiquesdeceroyaumemesseruiteu
r06 copy: papeaunomdescatholiquesdeceroyaumemesseruiteu
r07 fig : rscequeiecroyuouEaurafaicSchangerladelibe
r07 copy: rscequeiecroyuouSaurafaicTchangerladelibe
r08 fig : ra~~ondeu~~~repa~rNementpouruousenreuenirain
r08 copy: rationdeuostrepa-rTementpouruousenreuenirain
r09 fig : syqueparu~~~rederniereuousmonstriezestre
r09 copy: syqueparuostrederniereuousmonstriezestre
r10 fig : enuolontedefairecaruousauezasseziugeque
r10 copy: enuolontedefairecaruousauezasseziugeque
r11 fig : surcetterencontremesAaffairesdedelanont
r11 copy: surcetterencontremes-affairesdedelanont
r12 fig : besoinGdestreHabandonneesdeu~~~~~~re-Pnce~~ESie
r12 copy: besoin-destre-abandonneesdeuostrepreSEnceetSIie
r13 fig : masseuretantdeu~~~reaffectionaubiAndemon
r13 copy: masseuretantdeuostreaffectionaubiEndemon
r14 fig : sAruicequeuousneuouldrIezde-faillirlors
r14 copy: sEruicequeuousneuouldr-ezdeFfaillirlors
r15 fig : queu~~~redemeureyestplusnecessaireetutille
r15 copy: queuostredemeureyestplusnecessaireetutille
r16 fig : lesincommoditezcontinuellesquiaccompagne
r16 copy: lesincommoditezcontinuellesquiaccompagne
r17 fig : ntmesd~~~~~affairesnontpermisqueled~~~marquis
r17 copy: ntmesdictesaffairesnontpermisqueledictmarquis
r18 fig : soiSpaRsZsiSostqueieussedesirenyaNant
r18 copy: soiTpaSsEsiTostqueieussedesirenyaIant
r19 fig : quedixoudouzeioursquilsestmisenchemi
r19 copy: quedixoudouzeioursquilsestmisenchemi
r20 fig : nunpeumaldisposequipou~~~aAporterquelque
r20 copy: nunpeumaldisposequipourraaPporterquelque
r21 fig : retardementaladiligencequesanscelaileust
r21 copy: retardementaladiligencequesanscelaileust
r22 fig : peuetauoituolontefairelambertsenest
r22 copy: peuetauoituolontefairelambertsenest
r23 fig : alleauecIluydepeschedemapartpourretour
r23 copy: alleauec-luydepeschedemapartpourretour
r24 fig : nerenleuantieuousa-dressetoutcequilporte
r24 copy: nerenleuantieuousaDdressetoutcequilporte
r25 fig : aFfinqueuousleuoYezetyadioustiezOUreStraI
r25 copy: a-finqueuousleuoIezetyadioustiezETre-traN
r26 fig : GNiezcequeuousestimerezapropoZpourre
r26 copy: CHiezcequeuousestimerezapropoSpourre
r27 fig : ndrelesrdebreuesmieuxinstruictenlacharge
r27 copy: ndrelesrdebreuesmieuxinstruictenlacharge
r28 fig : queieluydonnequeiaybienuoulupasserpar
r28 copy: queieluydonnequeiaybienuoulupasserpar
r29 fig : lexamendeu~~~reboniugementpourlexperience
r29 copy: lexamendeuostreboniugementpourlexperience
r30 fig : etcoNnoissancequeuousauezdesaffairesdedela
r30 copy: etcoGnoissancequeuousauezdesaffairesdedela
v00 fig : iedesireseuleRentquela#d~~~~depesche______
v00 copy: iedesireseuleMentquela-dictedepeschepuisse
v01 fig : arriuerabonportestimantqueparlemoIe_
v01 copy: arriuerabonportestimantqueparlemoYen
v02 fig : dicelleSleschoses---concernAnSmonseruicepou
v02 copy: dicelle-leschosesQUIconcernEnTmonseruicepou
v03 fig : rrontcommencerdyreprendrequelqueforme____
v03 copy: rrontcommencerdyreprendrequelqueformeetdy
v04 fig : estretraictEeSauecunpeuplusdedigni______
v04 copy: estretraict-eZauecunpeuplusdedigniteetde
v05 fig : respectiaycependanteufortagreableslesa____
v05 copy: respectiaycependanteufortagreableslesaduer
v06 fig : tissemensqueuousa#uezdonneal###########dangleterr___
v06 copy: tissemensqueuousa-uezdonnealambassadeurdangleterreet
v07 fig : aud~~~~~~SrdebreuestantdU#laparticuliererec______
v07 copy: audictsieUrdebreuestantdE-laparticuliererecherche
v08 fig : delaquelleuozdeuxdernieresl~~~resfontme_____
v08 copy: delaquelleuozdeuxderniereslettresfontmention
v09 fig : aFfindyprendregardeetempescherquerien____
v09 copy: a-findyprendregardeetempescherqueriennesy
v10 fig : faceamonpreiudicequepoureschau-ferlespro____
v10 copy: faceamonpreiudicequepoureschauFferlesprogrez
v11 fig : commencezcontrelamaisondautricheLesquelG______
v11 copy: commencezcontrelamaisondautricheDesquelZiescay
v12 fig : quele###########tientpresqueSamesmeincommoditeetd______
v12 copy: queleroydespagnetientpresque-amesmeincommoditeetdesadua
v13 fig : ntagedesesdesseinGsquesiCestoitenses______
v13 copy: ntagedesesdessein-squesiLestoitensespropre
v14 fig : sIaisetpuisquecestcontremoyquesonambi____
v14 copy: sPaisetpuisquecestcontremoyquesonambition
v15 fig : sedeSbordeiayocca~~ondedesireretrecherc______
v15 copy: sede-bordeiayoccasiondedesireretrechercherque
v16 fig : tousmoYensluysoientretranchezparles_____
v16 copy: tousmoIensluysoientretranchezparlesquelz
v17 fig : ilmepeuLtendommageriecroyqueuousserez_____
v17 copy: ilmepeu-tendommageriecroyqueuousserezaduer
v18 fig : tydela######queles~~~~desdiguieresaouuertedu_____
v18 copy: tydelaguerrequelesieurdesdiguieresaouuerteducoste
v19 fig : depieContcestassezconuierlesamiZaluy_____
v19 copy: depieMontcestassezconuierlesamiSaluyayder
v20 fig : silzseueullentueoiruEngezdeceluyqui_____
v20 copy: silzseueullentueoiruAngezdeceluyquineles
v21 fig : espargneroitpassilauoitautantdemoYe_______
v21 copy: espargneroitpassilauoitautantdemoIensdeleu
v22 fig : rnuYrequilenadeuolonteuousferezence_____
v22 copy: rnuIrequilenadeuolonteuousferezenceladex
v23 fig : treRentlesofficesqueuouspourrezpou_____
v23 copy: treMentlesofficesqueuouspourrezpourlesy
v24 fig : animernousuerronsaudemeurantquelles______
v24 copy: animernousuerronsaudemeurantquellesseront
v25 fig : lesresolutionsdu####encequitoucheceroY_______
v25 copy: lesresolutionsdupapeencequitoucheceroIaumesur
v26 fig : lesdepeschesquiluyont#estefaicDesp~~~~cG
v26 copy: lesdepeschesquiluyont-estefaicTespardec-
v27 fig : aPRESapreslesquellesilnaurapas-occa~~on_____
v27 copy: a----apreslesquellesilnaurapasDoccasionduser
v28 fig : dedissimu-la~~onquonmauoulupersuaderquil_____
v28 copy: dedissimuLlationquonmauoulupersuaderquilestoi
v29 fig : Pcontrainbtdesuiureattendantquillu_____
v29 copy: Tcontrainctdesuiureattendantquilluyfust
v30 fig : ouuertquelquechemindefaireparoistreso______
v30 copy: ouuertquelquechemindefaireparoistresonaffec
v31 fig : tionalaconserua~~ondeceStecouronne
v31 copy: tionalaconseruationdeceTtecouronne
```

## Word list (generated)

```
words where figures differ from copy:
   14 ia auoir [quelque] figs:quelques
   28 disposition en [laquelle] figs:laquell
   39 bien tost [suiuy] figs:suyuy
   63 ie croy [uous] figs:uoue
   65 uous aura [faict] figs:faics
   71 de uostre [partement] figs:pa~rnement
   97 cette rencontre [mes] figs:mesa
  103 n ont [besoin] figs:besoing
  105 besoin d [estre] figs:estreh
  108 abandonnees de [uostre] figs:u~~~~~~
  109 de uostre [presence] figs:repnce
  111 presence et [si] figs:es
  120 affection au [bien] figs:bian
  123 de mon [seruice] figs:saruice
  127 uous ne [uouldrez] figs:uouldriez
  128 ne uouldrez [deffaillir] figs:defaillir
  152 ledict marquis [soit] figs:sois
  153 marquis soit [passe] figs:parsz
  154 soit passe [sitost] figs:sisost
  161 n y [aiant] figs:anant
  180 qui pourra [apporter] figs:aaporter
  201 est alle [auec] figs:aueci
  213 ie uous [addresse] figs:adresse
  219 il porte [afin] figs:affin
  223 uous le [uoiez] figs:uoyez
  227 y adioustiez [et] figs:ou
  228 adioustiez et [retranchiez] figs:restraigniez
  234 estimerez a [propos] figs:propoz
  268 experience et [cognoissance] figs:connoissance
  278 ie desire [seulement] figs:seulerent
  293 moyen d [icelle] figs:icelles
  296 les choses [qui] figs:
  297 choses qui [concernent] figs:concernans
  308 forme et [d] figs:
  309 et d [y] figs:
  311 y estre [traictez] figs:traictees
  318 de dignite [et] figs:
  319 dignite et [de] figs:
  338 d angleterre [et] figs:
  339 angleterre et [audict] figs:aud~~~~~~
  340 et audict [sieur] figs:sr
  356 font mention [afin] figs:affin
  366 rien ne [s] figs:
  367 ne s [y] figs:
  374 que pour [eschauffer] figs:eschaufer
  383 d autriche [desquelz] figs:lesquelg
  385 desquelz ie [scay] figs:
  389 le roy [d] figs:
  390 roy d [espagne] figs:
  392 espagne tient [presque] figs:presques
  400 de ses [desseins] figs:desseings
  403 que s [il] figs:ic
  408 ses propres [pais] figs:iais
  420 ambition se [deborde] figs:desborde
  428 et rechercher [que] figs:
  430 que tous [moiens] figs:moyens
  438 il me [peut] figs:peult
  458 coste de [piemont] figs:piecont
  464 conuier les [amis] figs:amiz
  473 ueullent ueoir [uangez] figs:uengez
  478 qui ne [les] figs:
  487 de moiens [de] figs:
  488 moiens de [leur] figs:r
  489 de leur [nuire] figs:nuyre
  500 en cela [dextrement] figs:trerent
  507 pourrez pour [les] figs:
  508 pour les [y] figs:
  526 ce roiaume [sur] figs:
  533 ont este [faictes] figs:faicdes
  534 este faictes [par] figs:p~~~~
  535 faictes par [deca] figs:cGapres
  542 aura pas [d] figs:
  545 occasion d [user] figs:
  547 user de [dissimullation] figs:dissimula~~on
  564 il luy [fust] figs:
  572 paroistre son [affection] figs:tion
  577 conseruation de [cette] figs:ceste
```
