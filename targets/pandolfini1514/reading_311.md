# Reading: ASF MAP LXXII 311: read in part

ASF Mediceo avanti il Principato LXXII, doc. 311 (cc. 382r-v, pos. 763-764): continuation of the copy to the Otto di Pratica of 310, "Tenuta adi iiij" [March 1515], sent "ad Lione alla ventura". About 37 cipher lines between clear passages. Bare letter: no decipherment of the time found. Key: `key_v6.json` (declared merge of the derived keys v5a and v5b of `key_v4.json`, see NOTES.md; **not measured**, the only measured key is v3, partial). Conventions (Daniel's): plain = certain; {x} = probable; [x] = restored; ‹…› = unresolved (tokens shown, `_` = space between tokens). Clear passages of the letter are given in [brackets] for context.

## Status

**Read in part: about 534 units, 424 certain, 44 probable, 1 restored ([24], written in clear inside the cipher), 65 unresolved groups.** Mechanical rate about 88%; an unresolved group often covers 2-3 words, so the real rate is **about 80-85%**. By block: A about 86%, B 88%, B continued 61%, C 91% (B15-B16 nearly illegible), P.S. 86%. Below the 95% rule.

Declared: the transcription is NOT blind (doubtful shapes settled while reading), so 'certain' here means read by the key without retouching on a transcription whose doubtful shapes were settled by reading.

## Raw decoding, key v6 (unretouched, `frozen/decode_v6.py`)

    A1 ve n ga la con c lu si o ne de ll o a pu n ta
    A2 me n to con inghilterra la qua le co s to ro i n r re vi s pe ra no a h o mo do s?
    A3 de ll a o pi ni o ne che e ra che i l du ca di su fo r l do ve s si s r
    A4 li a re per mo g li e ra la re gi na ci a n c h a que s ta fa ma per di c re s ce et ne l s c t di
    A5 h o mi na di co na qua li ta et qua l che a n g le se di ca sa la re gi na me de si ma do n s t ro n et o ri a r l
    A6 do le n do se ne cc
    A6b u na ta n ti fa ma so so a s s r h senza qu l che
    A7 fo n da me n to da per etn re s g na n te de ll a ra gi o ne di vo g li o ri re g ca re a c re di g lo con lo et s?
    B1 ci fu ro na le c c t re da ro ma de a ‹.xxiiij.› et i o i n te n do et di lo co
    B2 ce r to che u n g ra n per l so na gg i o et di co na qua li ta s c ri ve di la a cc e o r t n do qua s t cristianissimo
    B3 re so lu ti s si ma m n te che la papa et le si g no ri e du s t re e ra no e n t ra ti ne ll a le g h a
    B4 u l ti ma me n te con c lu sa et a n da n do i o que s ta ma c t na t i n co r te t ro va i que s ta no ti ti a
    B5 et gi a se da na t m l pe c to di qua l che co no per so na gg i o et pa r la n do a que s ta maesta a h
    B6 ri c h i e s ta de l con so lo di vo s t re si g no ri e re si de n te a li o ne i ll ri co r da i
    B7 a rm a non pa p re s ta re fe de a que ll o che qua l c h u no s pa r re va per la co r te che
    B8 vo s t re si g no ri e fu s so no e n t ra te ne ll a le g h a cc la qua le da re s po se
    B9 che a l h a ve re vi s to fi no a qua ta n ta fe de et o r se r va n t a ve r so la co ro na non
    B10 e ra per c re de r lo fi no a g che non lo ve de s si c h i ne da la no t ti di da ro ma
    B11 ri t ra g h o etn h o mo di qua li ta da po s se r lo sa per e et per vi a ? de l papa
    B12 ne ma n co per vi a de ll i o ra to ri imperadore et cattolico et per re la t o ne di c h i h a vi s to
    B13 la le c te ra i l p re fa to ne s c ri ve di so r te che i o non mi ma ra vi g li e re i o che que s ta
    B14 cristianissimo pe l se c re to su o te ne s si la co sa per ce r ta c h i me ne h a da to li no ti ti a
    B15 non mi h a e e p re s se me n te ve l to et mi sa re c h o mo qua da mo l t vi t si mi ri a r et ri s con t ri
    B16 i o so no c h i a ro che e su to i l ma r di na li di pa ce v no s?
    C1 per vi a du no pa r ti cu la re da co di o di e su to fa o to
    C2 i n te n de re i l cristianissimo per vi a di ro sa etn su to a cc e o r ta to la papa con le si g no ri e vo s t re
    C3 et e n t ra te ne ll a le g h a et h a ve re senza su r s c ri p ti a l cu ne t s t l cc na i ll a n da
    C4 que s to pa r ti cu la re che la le g s r h a du ca ti t re n ti ma la i l me se a svizeri et t re n ti ma la
    C5 a l t ri a l vi ce re di s pa g na et che que s t de l co so no pa ga ti per e qua l s c te
    C6 da ll a papa da ‹.16.› et ‹.17.› i o non so qua n ta fi di si a da p re s ta re a que s to co sa non h a ve n do
    C7 a l cu na no ti ti a da ll e ba n de di co s t et pe n h n da sa a n che che la papa si a per h a ve re g re n re s s c t
    C8 a h a r ma re a ll e s pe se su e et fa re po te n te i n i ta li a imperadore et cattolico de qua l i o c re do che
    C9 per na tu ra et per a ll i de n te qua l si s s sa di re nonn i o re n ri s co t le no t ti di
    C10 me l mo do che e ll a e ve nu ta di qua a ll i o che vo s t re si g no ri e non si ma ra vi g li no
    C11 se ve ri fo n do si la co sa si c a l te r s si la co na di s po si ti o ne di que s t maesta ve r so le ‹.16.›
    C12 non sa ri a g ra n fa o to che qua s t cristianissimo a ll e r ta ta si de ll a co sa vo l ta s si to t l me n te l ni ca a h
    C13 g ve ni re con imperadore et con cattolico ne li do v h ll i a qua n c h a re mi a vo le n di h le i i n qua l che s r te
    C14 a co mo di re et g en s t ri a ri p po a et? ? e si vi a che imperadore et cattolico non h a nn o
    C15 lo a ni ca a l e no da que s to h a ve n do si ri se r va to a u o to ri ta ne ll a ca pi tu la ti o ne fa o to
    C16 u l ti ma me n te con svizeri di po s se r con ve ni re con cristianissimo cc f che si ma n s t re per le co s e ve nu te
    C17 et di de ta ca s tu l ti o ne

## Reading by sense (Italian)

**Block A (A1-A2)** [Io mi penso che noi non siamo per partire di qui fin che non]
venga la conclusione dello {appuntamento} con Inghilterra, la quale costoro ‹W_y_d_7^4_9^3› sperano {ad} {ogni} {modo}.

**Block B (A3-A6)** [Per la mia de' xx si disse]
della {opinione} che era che il duca di {Suffolc} {dovessi} {pigliare} per moglie ‹7^5› la regina bianca. Questa fama ‹P› {dì} cresce, et nel ‹6_0_8_3^3› {homini} di bona qualità et qualche anglese di casa la regina medesima ‹3^2_y_6_Z_7^2_t› et ‹O_7^3_3_d_x› dolendosene.

**Block B continued (A6b-A7)** [Io mi maraviglio assai che]
una {tanta} fama ‹r^2_r^2_3› ‹6_6_d_r› senza qualche fondamento ‹3^5› per ‹F^n_7^4_6_G_t^5_y_8^4› della ragione ‹3^3_9^2_G_x^3_O› {ricercare} ‹3_0_7^4_3^3_G_x^2› ‹D^n_x^2› et.

**Block C (B1-B16)** [Hiersera ad notte]
‹2^3_y^1_7^2_t^5› lettere da Roma de' [24], et io intendo di loco certo che un gran personaggio et di bona qualità scrive di là, {accertando} questa Maestà resolutissimamente che il papa et le Signorie {vostre} erano entrate nella legha ultimamente conclusa. Et andando io questa mattina in corte trovai questa notitia, et già ‹r^4_3^5_t^5_8› ‹A_c› {petto} di qualche {bono} personaggio. Et parlando a questa Maestà ‹3_r› a richiesta del consolo di vostre Signorie residente a Lione, ‹W_H› ricordai a {Sua} {Maestà} a non ‹L^5› prestare {fede} a quello che qualchuno {spargeva} per la corte, che vostre Signorie fussono entrate nella legha. La quale ‹3^5› {rispose} che a l'havere visto fino a qua tanta fede et {observantia} verso la Corona non era per crederlo fino a ‹4› che non lo vedessi. Chi ne dà la {notitia} da Roma ritragho ‹F^n› homo di qualità da posserlo sapere, et per via ‹E› del papa, né manco per via delli oratori dello imperadore et del cattolico, et per {relatione} di chi ha visto la lettera; il prefato ne scrive di sorte che io non mi {maraviglierei} ‹O› che questa Maestà pel secreto suo tenessi la cosa per certa. Chi me ne ha dato la notitia non mi ha ‹Q_Q› {presentemente} ‹9^4_x_8^2› et ‹5^3_r^5_7^4› ‹0_r_O_5^2› ‹S^5_3^5_5^2_c_8› ‹9^3_Z_r^3_5^3_7^3_3_7› et {riscontri} ; io sono chiaro che è suto il {cardinale} ‹3^3_6^5› ‹2^4_9_t^2›.

**Postscript (C1-C17)** [Post.ta : Siamo ad notte et di nuovo]
per via d'uno particulare ‹3^5_2^2_3^3_O_3^3› è suto facto intendere al Cristianissimo, per via di ‹3^3_7^2_r^5›, ‹F^n› suto {accertato} il papa con le Signorie vostre et entrate nella legha, et havere ‹T› {subscripti} alcune ‹Z_6_8_x_c#› ‹t^5_W_H_3_y_3^5›, questo particulare : che la lega ‹6_d_r_3› ducati trentamila il mese a Svizeri et trentamila altri al viceré di Spagna, et che questo ‹3^4_c› ‹2^2› sono pagati per {equal} {parte} dal papa, da ‹.16.› et ‹.17.›. Io non so quanta {fede} sia da prestare a questa cosa, non havendo alcuna notitia dalle bande di {costà}, et {pensando} anche che il papa sia per havere ‹G_7^4_y_7^4› ‹6_6_0_8_3_r› {armare} alle spese sue et fare potente in Italia lo imperadore et il cattolico, de' quali io credo che per natura et per {accidente} {qualsisia} ‹3^3_7^4› ‹M^n› io ‹7^4_y_7^3_6_2^2› ‹8_x^4_t^2_8_8^3_3^3› ‹5^4_c› modo che ‹Q_4#_3› è venuta di qua ‹3_4#_W_O›, che vostre Signorie non si maraviglino se, {verificandosi} la cosa, si {alterassi} la {bona} dispositione di questa Maestà verso le ‹.16.›. Non saria gran facto che questa Maestà ‹3_4#_Q_d_8^5_8^5› ‹r^3› della cosa voltassi totalmente ‹x_t^3_2^5_3_r› ‹G› venire con lo imperadore et con il cattolico, ‹t^4_x^3_3^2_9_r_4#_W_3› ‹S^5_y_O_r_3_7^4› ‹5^3_3› ‹9^2_x^4_y_3^3_r_x^4› in qualche sorte accomodare et ‹4_Q^n› ‹6_Z_7^3_3_7^3_L_6^2_3› ‹Q_r^3_9^3_3›, che lo imperadore et il cattolico non hanno l'{animo} {alieno} da questo, havendosi riservato auctorità nella capitulatione facto ultimamente con Svizeri di posser convenire con il Cristianissimo ; ‹J› che si {mostra} per le cose venute et di detta capitulatione.

## Changes from the v5b reading

A2: "sperano {ad} {ogni} {modo}": the same group "3 r 2" stands in 310 A7 ("lo accordo seguirà ‹3 r 2› modo") and the clear 316 has "seguirà ad ogni modo"; the exact value of the group is not established (unresolved -> probable). Key v6 writes 0 before 8 as c: "mactina", "lectera", "lectere" (spelling only).

## Detailed notes

The full French working notes (status, prior work, word-by-word justifications, rates, changes in v6) are frozen in `frozen/LECTURE_311.md`.
