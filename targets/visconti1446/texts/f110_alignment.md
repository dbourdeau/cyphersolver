# BnF ital. 1583 f. 110 (DECODE R7902): duke's cipher letter, Milan 1 Nov 1446, read with the P17 key against the copy in ital. 1597

Pass 2, 29 Oct 2026. Transcription: `f110_transcription.tsv` (folio `110` = recto, 41 lines, image
`../decode/IMG_R7902_I35645_P1.png`; folio `110v` = verso, 17 lines, upper part of `IMG_R7902_I35645_P2.png`; the
lower part of P2 is show-through of the recto). Each line cropped at native resolution and upscaled 3.5-8x.
Pass 1 (21% sense, verso not transcribed) is kept as `f110_transcription_pass1.tsv` / `f110_reading_pass1.md`.

Crib: `f110_copy1597.md`, the 19th-century copy in BnF ital. 1597 f. 123r-v (Gallica btv1b10037396j, canvases
126-127), "(41.) 1446 1er 9bre. Au Cte François Sforza". Alignment by script (edit-distance alignment of the key
values to the copy's letters, `u`=`v`, `i`=`j`=`y`); the TSV note column gives, for each sign, the copy letters it
was aligned with and the verdict (`agree`, `variant` = one-letter difference of a short group, `differs`,
`unread`, `null`, `name-open`).

**The copy is itself a decipherment of this cipher, not an independent clear text.** It writes *gi* for *vui* four
times (*con gi*, *contra gi*, *tra gi et nui*, *sustenere gi*), exactly where the cipher has II + 3 (g + i, the
group the working key reads *vuy*); it writes *in za*, *de za* where the cipher has the z sign + a; and at both
places where the cipher has the name sign ∿ð+ (a blank heading in P17) it leaves a blank marked "V+". Whoever
made it read the slip with a P17-type key and could not resolve that one name. The agreement figures below
therefore measure our transcription against an earlier reading of the same signs, not against the duke's clear.

Notation as in `f005_reading.md`: **K** = key values concatenated (`[WORD]` word signs, `·` nulls, `[?]` not read,
`[∿ð+]` the unresolved name sign); **R** = reading with the copy's word division; **T** = the copy's letters over
the same span (normalised, accents dropped), with its line numbers. Values marked "value from the copy only" in
the TSV are counted as unread.

## Counts (script over the TSV)

| slip | tokens | nulls | agree with copy | one-letter variants | differ | unread | name sign open | sense (agree+variant) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| f. 110r | 1937 | 18 | 1833 | 18 | 7 | 59 | 2 | 1851 (96.5% of non-null) |
| f. 110v | 775 | 5 | 526 | 10 | 3 | 231 | 0 | 536 (69.6% of non-null) |

The verso is cramped (signs touch, letters stacked above the line) and the binarized DECODE image merges them; the
231 unread verso tokens are runs I could not segment, mostly in vv. 1, 8, 9, 15-17 (the date and title).
Verso readings are less secure than the recto's: several verso values were accepted on shape plus position.

## Where cipher and copy differ

- r5/41-42: the cipher has *molto propici*, the copy *meglo propicia*.
- r24/1: CON written as 6 with a dot for *com-* of *compagnia*.
- r25/15: cipher *facto*, copy *faito*.
- r30/7-8: cipher *fazati* (ħ with ring + at), copy *fagiti* (*lo fagiti*).
- r32/10: cipher *mane*, copy *mani* (the copy itself has *mane* at l. 36).
- r32/32: ∴ (p) where the copy has *Tanaro*: the cipher reads *de la dal Panaro*. Both are rivers; Panaro (Modena)
  fits a frontier between the duke's lands and Sforza's Romagna/Marche side. Not decided; the sign is a clear ∴.
- r32/39: c∞ (ac) where the copy has *ab* (*habiano*): probably my misreading of co (ab) as c∞.
- r35/17 and 35/37: cipher *le cose vostre* and *che ne erano*, copy *le cose nostre* and *che ve erano*.
- r40/2, r41/34: *et* for *e*; g# (t) where the copy has *f* of *fanti* (doubtful sign).
- r17/2, r19/1, r39/34: one letter not written in the cipher (*[c]osi*, *[p]otese*, *[p]osati*).
- v2/22: 9ρ (QUA) where the copy has *quele*; v5/26: +o (d) where the copy has *r* of *apreso*.
- Two signs unread where the copy has a value: r1/2 (ffl-like, a P17 null, copy *l* of *Illustris*), r38/17 (ꝑ-like,
  copy *o* of *provisione*); r12/41 is a small interlinear insertion I cannot read (copy *ro*).

## Lines

### f. 110r

1. K `ilustrisgeneretfilinostercarisime··molteetmolteuolten[?]ehavetiavisati[CHE]mai[NON][CON]desc`
   R i[?]ustris gener et fili noster carisime ··molte et molte uolte n[?]e haveti avisati che mai non condesc
   T illustris gener et fili noster carissime molte et molte volte ne haveti avisati che mai non condesc  (copy l. 1-2)
   Notes: pos 2 unread (ffl-like; P17 null ffl.; copy l of Illustris); the copy has *l*.
2. K `enderestiadesere[CON]ui[PER]necesitateet[PER]·modo[CHE]poresemodire[CHE][PER]necesitateuehavesemohav[?]`
   R enderesti ad esere con ui per necesitate et per ·modo che poresemo dire che per necesitate ue havesemo hav[?]
   T enderesti ad essere con nui per necessitate et per modo che poressemo dire che per necessitate ve havessemo hav  (copy l. 2-3)
3. K `[?][?][NON][PER]uolontauostrabona[CHE]mai[NON]funostraopinione[PERCHE][COME]fustistatopiu[?]`
   R [?][?] non per uolonta uostra bona che mai non fu nostra opinione perche come fusti stato piu [?]
   T uto et non per volonta vostra bona che mai non fu nostra opinione perche come fusti stato piu  (copy l. 3-4)
4. K `[?]orteetpiupossentesiandostatounamedesmacosa[CON]nuitantomeglohaviam`
   R [?]orte et piu possente siandostato una medesma cosa con nui tanto meglo havia m
   T forte et piu possente siando stato una medesma cosa con nui tanto meglo havia m  (copy l. 4-5)
5. K `[?][?][?]alstatonostroetanuietn[?]are[CHE]lafortunauesiastatamoltopropici`
   R [?][?][?] al statonostro et a nui et n[?]are che la fortuna ue sia stata molto propici
   T etuto al stato nostro et a nui et ne pare che la fortuna ve sia stata meglo propici  (copy l. 5-6)
   Notes: pos 41 ol where the copy has *eg*; pos 42 t where the copy has *l*.
6. K `aetfavorev[?]eethabiabenprouedutoa[QUE]sto[PERCHE]mai[PER][?]cloalcuno[?][?]iaoc[?]ors`
   R a et favorev[?]e et habia ben proueduto a questo perche mai per[?]clo alcuno [?][?]ia oc[?]ors
   T a et favorevole et habia ben proveduto a questo perche mai periculo alcuno sia occors  (copy l. 6-7)
   Notes: pos 35 l where the copy has *ul*.
7. K `oeltempopassato[NON]uesitiuolutomutaredeopinioneetadesopoteritidire[CHE]facend`
   R o el tempo passato non uesiti uoluto mutare de opinione et adeso poteriti dire che facend
   T o el tempo passato non ve siti voluto mutare de opinione et adeso poteriti dire che facend  (copy l. 7-8)
8. K `·[?][?]ocioeuen·endoadesereunamedesmacosa[CON]nuilofariti[PER]uolontauostra`
   R ·[?][?]o cioe uen·endo ad esere una medesma cosa con nui lofariti per uolonta uostra
   T olo cioe venendo ad essere una medesma cosa con nui lo fariti per volonta vostra  (copy l. 8-9)
9. K `[NON][PER]necesita·certificandoue[CHE]dapoilarotaseguitaalegentenostreinza`
   R non per necesita ·certificandoue che dapoi larota seguita alegente nostre in za
   T non per necesita certificandove che dapoi la rota seguita a le gente nostre in za  (copy l. 9-10)
10. K `sempresiamo[PER]severatiinopinionedeuolerepiutostopatire[CHE]livenetianihavesen`
   R sempre siamo perseverati in opinione de uolere piutosto patire che li venetiani havesen
   T sempre siamo perseverati in opinione de volere piutosto patire che li venetiani havessen  (copy l. 10-11)
11. K `oelstatonostrointegramente[CHE]uuinehavestipurunomicosoloetin[QUE]sta`
   R o el stato nostro integramente che uui ne havesti pur uno mico solo et in questa
   T o el stato nostro integramente che vui ne havesti pur uno miclo solo et in questa  (copy l. 11-12)
   Notes: pos 38 o where the copy has *lo*.
12. K `[?]opinionesiamosempre[PER]severatifin[CHE]havemorecevuto[QUE]stouostrobreved[?]`
   R [?]opinione siamo sempre perseverati finche havemo recevuto questo uost[?] breve d[?]
   T opinione siamo sempre perseverati finche havemo recevuto questo vostro breve d  (copy l. 12-13)
   Notes: pos 41 unread (small interlinear insertion over a caret); the copy has *ro*.
13. K `[?]icato[CHE][?]nehav[?][?]rtodatoa[QUA]trodelpresenteel[QUA]lebeninteso[CON]siderando[QUANTO][?]`
   R [?]icato che [?]ne hav[?][?]rto dato a quatrodel presente el quale ben inteso considerando quanto[?]
   T uplicato che ne haviti scripto dato a quatro del presente el quale ben inteso considerando quant  (copy l. 13-14)
   Notes: pos 13 r where the copy has *ri*; pos 14 t where the copy has *pt*; pos 48 quanto where the copy has *quant*.
14. K `tohumanamenteuesitimostoascriuenne[CHE][NON]neparelhavestipossutofare[CON]piuh`
   R to humanamente uesiti mosto ascriuenne che non nepare l havesti possuto fare con piu h
   T o humanamente ve siti mosto a scrivenne che non ne pare l havesti possuto fare con piu  (copy l. 14-15)
   Notes: pos 1 t where the copy has *-*; pos 50 h where the copy has *-*.
15. K `humanitateseuefusemopadreofigloloolapiucaracosahabiatiin[QUE]st`
   R humanitate se ue fusemo padre o figlolo o la piu cara cosa habiati in quest
   T humanitate se ve fusemo padre o figlolo o la piu cara cosa habiati in quest  (copy l. 15-16)
16. K `omondonehatutofaco[?]mutaredeopinione[PER]modo[CHE]havemodeliberato[NON]esere`
   R o mondo ne ha tuto faco[?] mutare de opinione per modo che havemo deliberato non esere
   T o mondo ne ha tuto facto mutare de opinione per modo che havemo deliberato non esere  (copy l. 16-17)
   Notes: pos 15 o where the copy has *-*.
17. K `·osi[PER]tinacietobstinati[COME]sitiuui[PERCHE][NON]uolemop[?]ctodire[CHE][NON]habiamonecesitat`
   R ·osi pertinaci et obstinati come siti uui perche non uolemo p[?]cto dire che non habiamo necesitat
   T cosi pertinaci et obstinati come siti vui perche non volemo puncto dire che non habiamo necesitat  (copy l. 17-18)
   Notes: pos 2 os where the copy has *cos*.
18. K `edeuiancidicemo[CHE]nehavemotantobisognoettantanecesitate·[QUA][?]tadirese·`
   R e de ui anci dicemo che ne havemo tanto bisogno et tantanecesitate ·qua[?]tadire se ·
   T e de vui anci dicemo che ne havemo tanto bisogno et tanta necessitate quanta dire se  (copy l. 18-19)
19. K `oteseetcrediamo[NON]laporesemohaveremaiore[COME]habiamosi[CHE]subuen·endoneu[?]i`
   R otese et crediamo non laporesemo havere maiore come habiamo siche subuen·endone u[?]i
   T potese et crediamo non la poresemo havere majore come habiamo siche subvenendone vui  (copy l. 19-20)
   Notes: pos 1 ot where the copy has *pot*.
20. K `[?]essotantopiu·uesaremoobligati[QUA]ntolofaritisiand[?]nuiinlomaiore`
   R [?]esso tanto piu ·ue saremo obligati quanto lo fariti siand[?] nui in lo maiore
   T adesso tanto piu ve saremo obligati quanto lo fariti siando nui in lo majore  (copy l. 20-21)
21. K `bisogno[CHE][?][?]oteseuenirein[QUE]stomondo·ondeueavisamo[CHE]siamo[CON]tenti`
   R bisogno che [?][?]otese uenire in questo mondo ·onde ue avisamo che siamo contenti
   T bisogno che ne potesse venire in questo mondo onde ve avisamo che siamo contenti  (copy l. 21-22)
22. K `benintenderse[CON]giethavemodeliberato[NON]faremai[CON]traginelstatouostronelec`
   R ben intenderse con gi et havemo deliberato non fare mai contra gi nel stato uostro nelec
   T ben intenderse con gi et havemo deliberato non fare mai contra gi nel stato vostro nele c  (copy l. 22-23)
23. K `oseuostreet[QUA]nto[PER]respectoalaspecialitateuostracioeala[PER]sonaala`
   R ose uostre et quanto per respecto ala specialitate uostra cioe ala persona ala
   T ose vostre et quanto per respecto a la specialitate vostra cioe a la persona a la  (copy l. 23-24)
24. K `[CON]pagniaetalstatouostr[?]faretuto[QUE]lo[CHE]saperitietuoritidomandareelsim`
   R conpagnia et al stato uostr[?] fare tuto quelo che saperiti et uoriti domandare el sim
   T compagnia et al stato vostro fare tuto quelo che saperiti et voriti domandare el sim  (copy l. 24-25)
   Notes: pos 1 con where the copy has *com*.
25. K `iledicemodeli[∿ð+]·delfactodelivenetianisiamoetiandio[CON]tentifarne[QUE]louor`
   R ile dicemo deli [name] ·del facto deli venetiani siamo etiandio contenti farne quelo uor
   T ile dicemo de li # del faito de li venetiani siamo etiandio contenti farne quelo vor  (copy l. 25-27)
   Notes: pos 10 name sign ∿ð+ (P17 blank heading); the copy leaves a blank 'V+'; pos 15 ac where the copy has *ai*.
26. K `it[?]etuepiacera[CON][QUE]sto[CHE][NON]habianodelnostrocosaalcunaoltra[QUE]lo[CHE]t`
   R it[?] et ue piacera con questo che non habiano del nostro cosa alcuna oltra quelo che t
   T iti et ve piacera con questo che non habiano del nostro cosa alcuna oltra quelo che t  (copy l. 27-28)
27. K `enevanoinancelarotadelinostri·recordandoue[CHE]nuiintendemoeserue`
   R enevano inance la rota deli nostri ·recordandoue che nui intendemo eserue
   T enevano inance la rota de li nostri recordandove che nui intendemo esserve  (copy l. 28-28)
28. K `bonpadreethaverue[PER]·bonfigloloetuolemoetintendemoda[QUE]stahora`
   R bon padre et haverue per ·bon figlolo et uolemo et intendemo da questa hora
   T bon padre et haverve per bon figlolo et volemo et intendemo da questa hora  (copy l. 29-29)
29. K `inanc[?][CHE]neposatisempreinganarealuostromodo[PERCHE]fazati[COME]uoritisemprecred`
   R inanc[?] che neposati sempre inganare al uostro modo perche fazati come uoriti sempre cred
   T inance che ne possati sempre inganare al vostro modo perche fazati come vorriti sempre cred  (copy l. 29-31)
30. K `eremol[?]fazati[PER]beneetabonfineetbonamenteet[NON]malamentebenueconfortam`
   R eremo l[?] fazati per bene et abon fine et bonamente et non malamente ben ue confortam
   T eremo lo fagiti per bene et a bon fine et bona mente et non malamente ben ve confortam  (copy l. 31-32)
   Notes: pos 7 az where the copy has *ag*; pos 8 at where the copy has *it*.
31. K `oetpregamo[CHE]da[QUI]inanceintutelecosehaveritiapraticare[CON]nuiuoglatipratic`
   R o et pregamo che daqui inance in tute le cose haveriti apraticare con nui uoglati pratic
   T o et pregamo che daqui inance in tute le cose haveriti a praticare con nui voglati pratic  (copy l. 32-33)
32. K `arleo[PER]lemanedeuostrifidati[CHE]sianodeladalpanaroet[NON]hacianoalcunad`
   R arle o per le mane de uostri fidati che siano dela dal panaro et non haciano alcuna d
   T arle o per le mani de vostri fidati che siano de la dal tanaro et non habiano alcuna d  (copy l. 33-34)
   Notes: pos 10 e where the copy has *i*; pos 32 p where the copy has *t*; pos 39 ac where the copy has *ab*.
33. K `ependentiadezao[PER]delinostri[CHE]havemofidati·recordandoue[CHE]laprin`
   R ependentia de za o per deli nostri che havemo fidati ·recordan doue che la prin
   T ependentia de za o per de li nostri che havemo fidati recordan dove che la prin  (copy l. 34-35)
34. K `[?]alecasonedetutilidebatiseguitifinoa[QUI]tragietnuiestatalohaver`
   R [?]ale casone de tuti li debati seguiti fino a qui tra gi et nui e stata lo haver
   T cipale casone de tuti li debati seguiti fino a qui tra gi et nui e stata lo haver  (copy l. 35-36)
35. K `[?]factopraticarelecoseuostre[PER]lemanedelinostri[CHE]neeranosuspec`
   R [?] facto praticare le cose uostre per le mane deli nostri che ne erano suspec
   T e facto praticare le cose nostre per le mane de li nostri che ve erano suspec  (copy l. 36-37)
   Notes: pos 17 u where the copy has *n*; pos 37 n where the copy has *u*.
36. K `tili[QUA]lisonostaticasonedefarnehaveresuspectoancoragi·avisandoue`
   R ti li quali sono stati casone de farne havere suspecto ancora gi ·avisandoue
   T ti li quali sono stati casone de farne havere suspecto ancora gi avisandove  (copy l. 37-37)
37. K `apreso[CHE]se[PER][QUE]stouostrointenderue[CON]nuio[PER][QUE]lealtrecasoneuoglia`
   R apreso che se per questo uostro intenderue con nui o per quele altre casone uoglia
   T apreso che se per questo vostro intenderve con nui o per quele altre casone voglia  (copy l. 38-38)
38. K `[?][?]ilvenetianiuetolesenolaprouisioneuostra[CHE]uedanonuisiamo[CON]tenti`
   R [?][?]i lvenetiani ue toleseno la pr[?]uisione uostra che ue dano nui siamo contenti
   T se sia li venetiani ve tolesseno la provisione vostra che ve dano nui siamo contenti  (copy l. 39-39)
   Notes: pos 4 l where the copy has *-*; pos 17 unread (ꝑ-like p with stroke; copy o of provisione); the copy has *o*.
39. K `[?]ue[QUE][?][?]prouisionemedesma[CHE]uedanoli[∿ð+]acio[CHE]ueosatisusteneregielstato`
   R [?]ue que[?][?] prouisione medesma che uedano li [name] acioche ue osati sustenere gi el stato
   T darve quela provisione medesma che ve dano li # acioche ve posati sustenere gi el stato  (copy l. 40-41)
   Notes: pos 27 name sign ∿ð+ (P17 blank heading); the copy leaves a blank 'V+'; pos 34 os where the copy has *pos*.
40. K `[?]et[?]teuostre·[?]apresoueavisamo[CHE]oltra[QUE]loedictod[?][?]ranuisiam`
   R [?]et [?]te uostre ·[?]apreso ue avisamo che oltra quelo e dicto d[?] [?]ra nui siam
   T et le gente vostre apreso ve avisamo che oltra quelo e dicto de sopra nui siam  (copy l. 41-42)
   Notes: pos 2 et where the copy has *e*.
41. K `o[CON]tentiai[?]arueetfavoriruede[?]avalitre[?]il[?][?]ettantimil[?]eanostresp[?][?]`
   R o contenti ai[?]arue et favorirue de [?]avali tre [?]il[?][?] et tanti mil[?]e anostre sp[?][?]
   T o contenti ajutarve et favorirve de cavali tre milia et fanti mille a nostre sp  (copy l. 42-43)
   Notes: pos 34 t where the copy has *f*.

### f. 110v

1. K `li[QUA]li[PER]severarano[CON]gifin[?][?][?][?][?][?][?][?][?][?][?][?][?][?]presa[CHE]uoglatipiglare[?][?][?]`
   R l i quali perseverarano con gi fin[?][?][?][?][?][?][?] [?][?][?][?][?] [?][?]presa che uoglati piglare [?][?][?]
   T se li quali perseverarano con gi fino a guerra finita in ogni impresa che voglati pigliare excepto  (copy l. 43-44)
   Notes: pos 1 l where the copy has *se*; pos 2 i where the copy has *li*; pos 45 ar where the copy has *iar*.
2. K `[CON]trasanctachiesa[?][?][?][CON][?]ra[QUA]leterre[CHE]teneimmed[?]ate[?][?][?][?][?]chhesa[?][CON]tral[?][?]`
   R contra sancta chiesa [?][?][?] con[?]ra quale terre che tene immed[?]ate [?][?][?][?][?] chhesa [?]contra l[?][?]
   T contra sancta chiesa zoe contra quele terre che tene immediate sancta chiesa contra le  (copy l. 44-45)
   Notes: pos 22 qua where the copy has *que*; pos 46 h where the copy has *i*.
3. K `[QUA]lemai[NON]faresemo[PER][CON]dictione[?]delmondo·[NON]intendendomi[?]a[?][QUE]le[CHE][?][?]`
   R quale mai non faresemo per condictione [?]del mondo ·non intendendo mi[?]a [?]quele che [?][?]
   T quale mai non faresemo per condictione del mondo non intendendo miga quele che tenes  (copy l. 45-46)
4. K `s[?]oiuicariifeudataribosu[?]recomendatim[?]olaente[QUE]le[CHE]lachiesapr[?][?]`
   R s[?] oi uicarii feudatarib o su[?] recomendati m[?]olaente quele che la chiesa pr[?][?]
   T seno soi vicarij feudatarij o sui recomendati ma solamente quele che la chiesa propr  (copy l. 46-48)
   Notes: pos 3 o where the copy has *so*; pos 16 b where the copy has *i*; pos 32 en where the copy has *men*.
5. K `ieetimed[?]atetene[COME]ed[?]to·avisandoueapdeso[CHE][NON]d[?][?][?][?][?][?][?][?]deuolereesere`
   R ie et imed[?]ate tene come ed[?]to ·avisandoue apdeso che non d[?][?][?][?][?][?][?][?] de uolere esere
   T ie et immediate tene come e dito avisandove apreso che non dicemo miga de volere esere  (copy l. 48-49)
   Notes: pos 26 d where the copy has *r*.
6. K `adefesadelachiesaneadoffesauostra[PER]la[?][?][?][?]h[?]esaanci[?][?][?][?][?][?][?][?][?][CHE][NON]saremo`
   R a defesa de la chiesa ne ad offesa uostra per la [?][?][?][?]h[?]esa anci [?][?][?][?][?][?][?][?][?] che non saremo
   T a defesa de la chiesa ne ad offesa vostra per la chiesa anci siati certo che non saremo  (copy l. 49-50)
7. K `[PER]defesa[?]es[?]achies[?]aneadoffesauostra[PER]la[?][?]hiesa·[?]recordando[?]`
   R per defesa [?] es[?]a chies[?]a ne ad offesa uostra per la [?][?]hiesa ·[?]recordando[?]
   T per defesa de essa chiesa ne ad offesa vostra per la chiesa recordandov  (copy l. 50-51)
8. K `eapreso[CHE]da[QUI][?][?][?][?][?][?][?][?][?][?][?][?][?][?][?][?]nuifaremo[?][?][?][?][?][?][?][?][?][?][?][?][?][?][?][?]`
   R e apreso che da qui [?][?][?][?][?][?][?][?][?][?][?][?][?][?][?][?] nui faremo [?][?][?][?][?][?][?][?][?][?][?][?][?][?][?][?]
   T e apresso che da qui inance in queste pratiche nui faremo mentione similmente de no  (copy l. 51-52)
9. K `[?]le[CON]tralamaiestadelrederag[?][?]ona[PER][QUE]lo[CHE]lteneinelreame·[?][?][?][?][?][?][?][?][?][?][?][?]`
   R [?]le contra la maiesta del re de rag[?][?]ona per quelo chel tene in el reame ·[?][?][?][?][?] [?][?] [?][?] [?] [?] [?]
   T n fare contra la maiesta del re de ragona per quelo chel tene in el reame et questo faremo per dui res  (copy l. 52-54)
   Notes: pos 2 l where the copy has *r*.
10. K `pecteiluno[PER]nostrohonorelaltroacio[CHE][NON]havendo[?][?][?][?]os[?][?][?]`
   R pectei l uno per nostro honore l altro acioche non havendo [?][?][?][?]os[?] [?][?]
   T pecti l uno per nostro honore l altro acioche non havendo questa cosa efecto  (copy l. 54-55)
   Notes: pos 4 e where the copy has *-*.
11. K `mai[NON]uenese[?]eorechiede[?]am[?]t[?]o[?][?][?]havesemo[CON]sen[?][?][?][?][?][?][?][?]`
   R mai non uenese [?]e orechie de [?]a m[?]t[?]o[?][?] [?] havesemo con sen[?][?][?][?] [?][?] [?][?]
   T mai non venesse a le orechie de la majesta soa che havesemo con sentito fare contro si in el  (copy l. 55-56)
   Notes: pos 22 t where the copy has *s*.
12. K `reamem[?][?][?][?][?]erto[CHE]de[?][?]to[?]uifaremosempre[QUE]lo[?][?][?][?][?][?][?]`
   R reame m[?][?][?] [?][?]erto che de [?][?]to [?]ui faremo sempre quelo [?] [?][?][?] [?][?] [?]
   T reame ma siati certo che de questo nui faremo sempre quello ve piacera et questo ten  (copy l. 56-57)
13. K `itilo[PER]certoet[PER]fermo[?]benuedicemo[CHE][?][?][?][?][?]possiamostarein[?][?][?][?][?]`
   R itilo per certo et per fermo [?]ben ue dicemo che [?][?][?][?] [?] possiamo stare in [?][?][?][?][?]
   T itilo per certo et per fermo ben ve dicemo che nui non possiamo stare in pendente  (copy l. 57-58)
14. K `et[?][?][?][?]prestouenireale[CON]clusione[PERCHE]sel[?][?]dic[?]f[?][?][?]l[?]osefor[?][?][?][?][?][?][?][?]`
   R et [?][?][?][?] presto uenire a le conclusione perche sel [?][?] dic[?]f[?][?][?] l[?]ose for[?][?][?][?][?][?] [?][?]
   T et che voglati presto venire a le conclusione perche sel se diferisse le cose forse piglar  (copy l. 58-59)
   Notes: pos 31 ic where the copy has *i*.
15. K `ianotalforma[CHE]poise[?]enuolest[?][?][?][?][?]p[?][?]tiproueder[?][?][?][?][?][?]`
   R iano tal forma che poi se[?]en uolest[?][?][?][?] [?] p[?][?]ti proueder[?][?][?][?][?] [?]
   T iano tal forma che poi seben volesti non poteristi provedergli data med  (copy l. 59-61)
16. K `[?][?]dieprimonouem[?]ris[?][?]·[?][?][?][?][?][?][?][?][?][?][?]d[?][?]ed[?]ol[?][?]`
   R [?][?] die primo nouem[?]ris [?][?]·[?][?][?][?][?][?][?][?][?] [?][?] d[?][?]ed[?]ol[?][?]
   T iolani die primo novembris etc filippus maria anglus dux mediolani  (copy l. 61-62)
17. K `e[?][?][?][?][?]e[?][?]omesac[?]uedom[?][?][?]`
   R e[?] [?][?][?][?]e[?][?]omes ac [?]ue dom[?][?][?]
   T etc papie anglerieque comes ac janue dom  (copy l. 62-63)

## Summary

Filippo Maria Visconti to his son-in-law Francesco Sforza, Milan 1 November 1446 (date and title on the verso,
partly read; the copy gives *Data Mediolani die primo novembris*). Sforza has often said he would never come to the
duke out of necessity; the duke now admits, after receiving Sforza's brief of the 4th, that he has great need of
him, resolves never to act against him, offers the Venetian question to Sforza's wishes provided Venice keeps
nothing beyond what it held before the rout of the duke's army, asks that negotiations go through trusted men "da la
dal Panaro/Tanaro", promises to pay the provision the [name sign ∿ð+] pay him if Venice withdraws its own, and offers
3000 horse and 1000 foot at his own expense for any enterprise except against the lands held directly by the
Church, with a reservation for the King of Aragon's kingdom; he asks for a quick conclusion.

Open: the name sign ∿ð+ (2 tokens; the copy's maker could not read it either), the unsegmented verso runs, and the
few signs listed above.
