# Reading: ASF MAP LXXII 310: read in part

ASF Mediceo avanti il Principato LXXII, doc. 310 (cc. 380r-381v, pos. 759-762): "Copia della lettera del mag.co or.re Franc.o Pandol. apresso il X.mo alli mag.ci S.ri Otto di pratica", dated "Parisijs die xxvj februarij 1514" (= 26 Feb 1515), continued "Siamo adj xxvij" and "Siamo adi ij di marzo". It is the "alligata copia della mia ad Fiorenza" of 309; 311 is its continuation. 67 cipher lines. Bare letter: no decipherment of the time found. Key: `key_v6.json` (declared merge of the derived keys v5a and v5b of `key_v4.json`, see NOTES.md; **not measured**, the only measured key is v3, partial). Conventions (Daniel's): plain = certain; {x} = probable; [x] = restored; ‹…› = unresolved (tokens shown, `_` = space between tokens). Clear passages of the letter are given in [brackets] for context.

## Status

**Read in part: about 895 units (a word, or an unresolved group counted as one): 701 certain, 109 probable, 0 restored, 85 unresolved groups.** An unresolved group often covers 2-5 words: counting 3 words per group, about 1,065 words and **about 75% read by sense** (the mechanical 91% overstates it). By block: A about 80%, B 80%, C 65%, D 65%, E 70%, F 70%, G 80%, H 80%. Below the 95% rule.

Reservations (declared): (1) pos. 759 (block A) was transcribed by an agent that knew the key: NOT blind; (2) codes not resolved: .22. (probably lanzichenech, from the clear 316 of mid-March, not added to the key), 20./23., .uij.; (3) blocks C, D and E need re-reading on HD images.

## Raw decoding, key v6 (unretouched, `frozen/decode_v6.py`)

    A1 de ll a che h i s ci a qua le si t ro va va i n a n g li te rr a a n ca s ci a do re per que s ta maesta i n si me
    A2 con i l p ri mo p re si de n te di ro a no e ve nu to qui et i l p re si de n te e re s ta to la la ca u sa de ll a
    A3 ve nu ta su a e s ta ta s? si ri t ra e per ri so l ve re li ca pi tu li che si t ra c to no na r que s te du e ma e s ta
    A4 i n a n g li te rr a et per ancora o
    A5 i o ri t ra g h a con li ca pi tu li e ? pe di ti per ancora o si a s pe c ta da l ca n to di que s t maesta i l du b
    A6 di su fo r t et li a l t ri o ra to ri di inghilterra che si t ro vo no qui u so n di re che lo a cc o r do se g u i ra
    A7 a h o mo do et co s to ro da l ca n to lo ro non ci fa nn o du ci ta ti o ne
    A8 de ll a che h i s ci a ve nu n do di a n g li te rr a di f e h a ve re ri n con t ro a h ca le s i l
    A9 n ra te ve s co vo s pa g no lo pa le a me si s pa si ti s t ll e qui et re fe re n do li a vo qui a l du ca di
    A10 su fo r t i l p re fa to du ca li re s po se i l p re fa to n ra te va i n a n g li te rr a per me c t re
    A11 fu o co ? qua e non li ri u s ci ra et mi di co to che i l fu o co non va da piu p re s to di o sa h a che n s t ra si
    A12 i l p re fa to du ca mo l to vo l to a ll e co se n ra n ve si si a o per na tu ra le di s po si ti o ne su a o
    A13 o ? i n t ra c te ni me n to de n ra n ve si  ? o
    B1 li o ra to ri fi a mm i n g h i che si t ro va no qui a do qua n do no i l pa re n ta do di ma da ma re nu a et quo n s
    B2 t ro no fa r ne i n s t a n ti a qua lo a do qua n do no r? i n te n do per ce r to con ta n te di s h o ne s te con di
    B3 ti o ni che non si mu ta n do non ne do ve rr a se g u i re con c lu si o ne a l cu na et ? pa r la n do i l con u n
    B4 per so na gg i o di qua li ta qua le per t ro va r si i n con si g li o ra gi o ne vo l qu fe t ne sa i l t cu to
    B5 mi di s se li o ra to ri fi a mm i n g h i ne l p ri n ci pi o non po s se c to no pa r la re piu su r qui ? i va que n te
    B6 et a l p re se n te so p ra i l pa re n ta do c h i e gg i o no ta n te di s h o ne s te do qua n de che se fu s si s ta d? me
    B7 i o li h a ve ri a li ce n ti a ti ?
    B8 re le do ma n de de p re de c ti si e no fa c t con a c ti fi ci o et con o r di ne ? ancora de l imperadore 
    C1 i l cristianissimo h a h a vu to u l ti qua que n te et per ? du na vi a la co pi a de ll a le g h a con c lu sa n ra imperadore m ?
    C2 ? et ? ? et h a ve n do vi t ro va to u n ca pi tu lo per i l qua le si quo n s t ra va che l h o quo
    C3 de l papa a p re s so li svizeri h a ve va re s po s to non h a ve re qua n da to di si qu l co sa et c c eta s ta to a papa p re
    C4 fi e o i l te r qui ne a h de c la ra re la su a vo lu n ta que s t maesta h a quo n s t ro re s ta re cu sa ti s
    C5 qu fa c t de l papa et i o lo c re do h a ve n do ? s ta ma c ? na vi s to le do m re vo li pa ro le che suamaesta
    C6 u so a ll o o ra to re de l papa et a que p re se n ta n do li i l p re fa to o ra to ? u n r re ve di papa ri n
    C7 g ra ti a to ri o per con to di ne r co na ? quo n s t ro suamaesta ne l u l ti quo de l su o pa r la re con do le r si che le co se
    C8 a l p re se n te non si t ro va s si no i n etn da po s se r fa re qua l che g ra n ? fi ci o a ll a se de a s? s to li qu
    C9 et a ll a papa ca e ra i l de si de ri o di suamaesta ?  ?
    D1 i n con t ra i u no a mi co di co na qua li ta qua le ve ni va da u no
    D2 de ll i o ra to ri di inghilterra et mi di s se ea i l p re fa to o ra to re li h a ve va de c to te ne re per ce r t
    D3 che a ll a gi u n ta di mo n si g no re de ll a g h i s ci a i n a n g li te rr a si con fe r me ri a lo a c ll
    D4 o r do qua le inghilterra h a ve va f c to con la fe li ce me mo ri a de l re pa s sa to
    D4b et con c lu so
    D5 me s to si po t ra ve ni re di ? a qua l che nu o vo t ra c ta to et ca pi tu la ti o ne n ra me pa ti du a re
    D6 ne i o so se i l p re fa to o ra to re si vo le va i n te n de re per con to de ll e co se de l cattolico a l qua le
    D7 me s ta maesta r? che si ri t ra e da ll e pa ro le nu e po r ta o di o non pi ll i o lo et a n da n do i o
    D8 ci per i n co r te i l cristianissimo i n u n lu n go di s co r so de ll e co se de l papa di f e a ll o o ra to re
    D9 ci senza et a me co h a ve va ma n da to la g h i s ci a i n h re to i n a n g li te rr a m e ? pe di to et che
    D10 de c te va la co sa per con c lu sa et che e ra i l ve ro che re s ta va qua l che ? di di f f i cu l t per con to di
    D11 s co ti a ma che a n che que s ta si a s se c te re pa e ?
    D11b de ll a ce g h a
    D12 con c lu sa et sa per e che li svizeri di p ro ? i mo te ne va no a su ri ? u na di e ta per pe n sa re di mo le s ta re suamaesta
    D13 di ce do che con po s to con inghilterra ? g pe n sa va se di o non fu s si con t ro di lu i che ne s su no di que ll i co ll e
    D14 ga ti li po te s si nu o ce re et che i n v re vi t c t le su a n ro n ti e re sa re pa o no m n r ni te et che i l
    D15 p re se n te con si g li o qua ce no i ve da va mo che a ll o ra e ra fi to non e ra te nu to me s ta ma c ti na per n pe su no
    D16 a o t ro con to con c lu de n do ci che i n v re vi gi c r ni fa ri a ? va l ca re tu c ti e go v r na to ri ci a s cu no a l su o pa e se  qu
    D17 et che a ll o ve ri a di p re se n te ‹.uij.› la n ce n ra i n co r so t na et da l p h i na to a l? ? o ?
    E1 se gi a le o per e lo ro non s fo ra v s si no me s ta maesta a h mu ta re o s ni o ne s ta m c ti na ne l ra gi o na
    E2 me n to so p ra de c to suamaesta mi di s se pa r la n do di vo s t re si g no ri e che me ll e h a ve va no fi c t g n t
    E3 e e pe ri e n ti a de ll a fe de lo ro che li re pu ta va per su a a f et e c t oi sa ti ? qua l si vo g li a ca ll a
    E4 di n ra n ci a et che sa ri a m gi o i o so che na s ce s si qua l che o cc a si o ne di po s se re m fi ca re
    E5 ro te s ta ri ll a che mi a s si cu ra va che lo fa re na e mo l to vo le n ti e ri et di co ni s si mo cu o re
    F1 i l cristianissimo do n s t ra du ci ta re che svizeri h a na i no a h fa re ma l che do to con t ro di lu i et con
    F2 n si a ? a l ll e r ta to pe n sa so l da re qua l che nu me ro di ‹.22.› et s pe ra i n u n su ci to s s so r li me c t re i n
    F3 si e me h a ve n do ma n da to a h o f et e ri r si cu o n nu me ro di me ll i che u l ti ma me n te se r vi ro no i l
    F4 re pa s sa to ne suamaesta si e re so n ta per a n co ra de l po g li a r li c re do i o per non vo le re
    F5 me ll a s pe sa senzan ne ce s si ta  ? r ?
    G1 i l cattolico c h i e de
    G2 a co s t t ro di fa re u na t re gu a per t re a nn i et per le co se di m et di i ti l a et ca i n
    G3 su a cattolico si ri t ra e et u n g ra n so s pe c to et ti mo re de ll e co se de l re a me di na s lo et de l go ve r no
    G4 di ca s ti g li a i o per ? po s na ra cc o ll e non c re do che i n que s t maesta ri a a l cu na i n c li na t
    G5 o na a ll e co se de l cattolico
    H1 i l ma ne gg i o n ra co s t ro et arciduca
    H2 non o r s ta n te che per ce r to ri i n te n da che le do ma n de de ll i li a mm i n g h i si ri n e no i n ma gg i o re
    H3 pa r te lo di ta te et per mo l ti si c re de che non o r s ta n te que s to non si h a na i a h fa re a l cu na con c n uu si o ne  ? che

## Reading by sense (Italian)

**Block A (p759, A1-A13)** [clear: … Il gran conestabile per ancora non esce di camera et si crede che resterà libero del suo braccio. Mons.r]
della {Ghiscia}, quale si trovava in Angliterra ambasciadore per questa Maestà insieme con il primo presidente di Roano, è venuto qui, et il
presidente è restato là. La causa della venuta sua è stata, si ritrae, per risolvere li capituli che si tractono {tra} queste due Maestà ‹…›.
[clear: Et oggi ultimamente il sopradetto si è partito per ritornarsene] in Angliterra, et per ancora ‹O›, io {ritraggo}, con li capituli
{expediti}. Per ancora ‹O› si aspecta dal canto di questa Maestà. Il {duca} di {Suffort} et li altri oratori di Inghilterra che si trovono
qui {usono} dire che lo accordo seguirà {ad} {ogni} modo, et costoro dal canto loro non ci fanno {dubitatione}.
[clear: Il fine sen doveria vedere in brevi giorni. Mons.r] della {Ghiscia}, {venendo} di Angliterra, ‹3^3_J_Q› havere {rincontro} {ad}
{Cales} il {frate} {vescovo} {spagnolo} ‹6^5_x^4_3_5^4_r^3_6_6^5_r^3_8^3› ‹6_8_4#_Q› qui, et {referendoli} ‹3_9^2› qui al duca di
{Suffort}, il prefato duca li rispose : il prefato {frate} va in Angliterra per {mectere} fuoco ‹etc?›, {che} non li riuscirà ; et ‹5^3_3^3_2^2_8^2›
che il fuoco non vada più presto ‹…›. Il prefato duca, molto volto alle cose {franzesi}, sia o per naturale dispositione sua o ‹?› {intractenimento}
de' {Franzesi}.
**Block B (p760, B1-B8)**
Li oratori fiamminghi che si trovano qui {domandono} il parentado di madama {Renea} et {monstrono} {farne} {instantia} ; {la} {quale}
{domandono}, {secondo} intendo per certo, con tante {dishoneste} {conditioni} che, non si mutando, non ne doverrà seguire conclusione alcuna.
Et ‹[oggi?]› parlando ‹…› con un personaggio di qualità, quale per trovarsi in consiglio ‹ragionevol qu fe t› ne sa il ‹t_cu_to›, mi disse
li oratori fiamminghi nel principio non {possecto} parlare {più} ‹…›, et al presente sopra il parentado {chieggiono} tante dishoneste
{domande} che, se fussi stato ‹d?› me, io li haveria {licentiati}. [clear: questa cosa bisogna indicarla alla giornata, non sappiendo io …]
‹7^4› le domande de' predecti {sieno} facte con {artificio} et con ordine ‹E› ancora del imperadore.
**Block C (p760, C1-C9)** [clear: … per il ricatto suo.]
Il Cristianissimo ha havuto {ultimamente} et per ‹au?› {d'una} via la copia della legha conclusa ‹t_7^5› imperadore ‹…› ‹20._F_23._etc?›
et havendovi trovato un capitulo per il quale si {monstrava} che {l'homo} del papa appresso li Svizeri haveva resposto non havere {mandato}
di {simil} cosa ‹…› et ‹…› stato ‹…› ad declarare la sua voluntà, questa Maestà ha {monstro} restare {satisfacto} del papa, et io lo credo,
havendo ‹?› {stamactina} visto le {amorevoli} parole che Sua Maestà {usò} allo oratore del papa ‹…›, presentandoli il prefato oratore un
{breve} di papa {ringratiatorio} per conto di ‹ne_r_co_na› ; {monstrò} Sua Maestà nel {ultimo} del suo parlare dolersi che le cose al presente
non si trovassino in {termine} da posser fare qualche gran {beneficio} alla {Sede} {Apostolica} ‹…› et alla ‹papa_ca›, ‹…› il desiderio di Sua
Maestà.
**Block D (p761, D1-D17)** [clear: Siamo adj xxvij … Stamattina in andando a corte]
incontrai uno amico di {bona} qualità, quale veniva da uno delli oratori di Inghilterra, et mi disse ‹ea› il prefato oratore li haveva decto
tenere per certo che alla giunta di monsignore della {Ghiscia} in Angliterra si confermeria lo accordo quale Inghilterra haveva facto con la
felice memoria del re passato [clear: Et henbiunse (?)] et concluso ‹…› si potrà venire ‹…› a qualche nuovo tractato et capitulatione
‹n_ra_me_pa_ti_du_a_re›, né io so se il prefato oratore si voleva intendere per conto delle cose del Cattolico, al quale {questa} Maestà
‹r?›, che si ritrae dalle parole ‹…›, non ‹…›. Et andando io ‹ci per› in corte, il Cristianissimo, in un lungo discorso delle cose del papa
‹di_f_e› allo oratore ‹ci_senza› et a me {come} haveva mandato la {Ghiscia} ‹…› in Angliterra ‹…› {expedito}, et che {teneva} la cosa per
conclusa, et che era il vero che restava qualche ‹?› di {difficultà} per conto di {Scotia}, ma che anche questa si {assecterebbe} ‹…›.
[clear: Subitamente hauto notitia] della {legha} conclusa, et sapere che li Svizeri di {prossimo} ‹…› tenevano ‹…› una dieta per pensare
di molestare Sua Maestà, {dicendo} che, composto con Inghilterra, ‹g› pensava, se Dio non fussi contro di lui, che nessuno di quelli collegati
li potessi nuocere, et che in {breve} ‹…› le sue {frontiere} ‹…› {munite} ‹…›, et che il presente consiglio ‹…› vedavamo che allora era ‹…›
non era tenuto ‹…› per ‹…› altro conto, concludendoci che in {breve} {giorni} faria {cavalcare} tucti e {governatori} ciascuno al suo paese
‹…› et che ‹…› di presente ‹.uij.› lance ‹…› et dal {Delphinato} ‹…›.
**Block E (p762, E1-E5)** [clear: … Et mi persuado che ogni giorno sia per augumentare :]
se già le ‹…› loro non {sforzassino} {questa} Maestà a mutare {opinione}. {Stamactina} nel ragionamento sopradecto Sua Maestà mi disse,
parlando di vostre Signorie, che ‹me_ll_e› havevano facto {gran} {experientia} della fede loro, che li reputava per sua ‹a_f_et_e_c_t_oi_sa_ti›
{qualsivoglia} ‹ca_ll_a› di {Francia}, et che saria ‹m› {gioioso} che nascessi qualche occasione di possere ‹m_fi_ca_re› ‹…› che mi
assicurava che lo farebbe molto volentieri et di {bonissimo} cuore.
**Block F (p762, F1-F5)** [clear: … De quali luoghi li sopradetti sono governatori :]
Il Cristianissimo {dimonstra} {dubitare} che Svizeri ‹h_a_na_i_no› {ad} fare ‹…› contro di lui, et con ‹…› pensa {soldare} qualche numero
di ‹.22.› et ‹…› mectere insieme, havendo mandato ‹…› numero di ‹me_ll_i› che ultimamente servirono il re passato ; né Sua Maestà si è
{resoluta} per ancora del pigliarli, credo io per non volere {quella} spesa senza necessità.
**Block G (p762, G1-G5)** [clear: Per via di uno amico … ritragho com(e)]
il Cattolico chiede a {costoro} di fare una tregua per tre anni et per le cose di ‹m› et di {Italia} ‹…› ; ‹…› Cattolico, si ritrae, ‹…› un
gran sospecto et timore delle cose del reame di {Napoli} et del governo di Castiglia. Io per ‹…› non credo che in questa Maestà ‹ria›
alcuna {inclinatione} alle cose del Cattolico.
**Block H (p762, H1-H3)** [clear: Non si può per ancora far iudicio che fine si habbi ad havere]
il maneggio {fra} costoro et Arciduca, non {obstante} che per certo ‹ri› intenda che le domande delli {Fiamminghi} si ‹ri_n_e_no› in maggiore
parte ‹lo_di_ta_te›, et per molti si crede che, non {obstante} questo, non si habbi ad fare alcuna {conclusione} ‹…› che
[clear: Benchè alcuni altri lo sperino in breve.]

## Detailed notes

The full French working notes (status, prior work, word-by-word justifications, rates, changes in v6) are frozen in `frozen/LECTURE_310.md`.
