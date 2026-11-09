# Reading: ASF MAP LXXII 307: read in part

ASF Mediceo avanti il Principato LXXII, doc. 307 (c. 369r, pos. 747): "Copia di lettera del mag.co oratore fiorentino Franc.o Pand. al Xmo alli mag.ci S.ri Otto di Pratica de di xvj di febraio M.D.XIIIJ" (Florentine style = 16 Feb 1515). 24 cipher lines in 5 blocks between clear passages. Bare letter: no decipherment of the time found. Key: `key_v6.json` (declared merge of the derived keys v5a and v5b of `key_v4.json`, see NOTES.md; **not measured**, the only measured key is v3, partial). Conventions (Daniel's): plain = certain; {x} = probable; [x] = restored; ‹…› = unresolved (tokens shown, `_` = space between tokens). Clear passages of the letter are given in [brackets] for context.

## Status

**Read in part: 291 cipher words, 205 certain, 57 probable, 0 restored, 29 unresolved = 90% read by sense.** By block (key v5a counts; v6 moved two words to certain and one to unresolved): block 1 about 92%, block 2 about 83%, block 3 (13 words) about 69%, block 4 about 96%, block 5 about 95%. Below the 95% rule.

## Raw decoding, key v6 (unretouched, `frozen/decode_v6.py`)

    L1 che c h i fu i l su i ve ro che v nn e qua et qua li e ra no que ll i a mi ci di co s to ro che lo
    L2 ma n do ro no ? la qua le no t ti a a l p re se n te non e ne ce s sa ri a
    L3 c h i si ma n di s si i l p re fa to h i ve ro et c h i si e no que ll i h o di si ni
    L4 che co s to ro i n t ra c te n ge no ne svizeri se n do co sa t n t m l t se c re t per i l ? i cu lo
    L5 che ne po t re s e su cc e de re a que ll i p ri v ti da lo ro ca n to ni
    L6 que s ta maesta h a ve re ma n da to u no h o quo a svizeri ri t ra g h ? ci e
    L7 di cu o n lo co che i l p re fa to a n do con ma n da to de l da o a o g co n et pe re che i l ca s r to
    L8 h o si a di h a ve re t ro g to li svizeri cu o s ti na ti h a ve n do li lo ro re s po s to ma ra vi
    L9 g li a ri de ll a p ro su n t o ne su a se n do e n t ra to ne l pa e se lo ro senza sa l vo con
    L10 do c t m n s t ra n do per que s ti vo l t a cc e tt a o ne la s cu sa qua che i n fu t ru ?
    L11 ne ? u no a l t ro che lo fe ce s si se ne lo de re s e
    L12 volere i l cristianissimo per co no di m co du mm o do che suamaesta te n ga lo a s fu t me n to di di g u n
    L13 so ll i ci ta no la p ra ti ca de l pa re n ta do di da ma da re ne a con i l lo ro si g no re co s to ro
    L14 non li de s pe ra no et i n t ra c t n ge no la p ra ti ca ne i o so gi a con che di no ma et
    L15 che fi ne la co sa si h a s i a h h a ve re ma a cc e r to m vo s t re ci g no
    L16 ri e per t ra g lo di co n lo co che e fi a mm i n g h i so ll i ci ta no la co sa
    L17 et co s to ro la i n t ra c t n ge no  ? r ?
    L18 co s to ro non fa nn o du ci o a l cu no di h a ve re a h ri nn o va re lo a cc o do con inghilterra m fi no a l p re se n te
    L19 non se ne pu o di re co sa a l cu ni di ce r t
    L20 que s ta maesta con t ni a me n t a f s e r ma volere con g ro s si s si me fo r ve fa re la i m p re sa di i t li a senza
    L21 re s t ri n ge r si per a g? a l cu no de te r ma n t c re do che suamaesta ne h a s i g ra n di s si sa vo lu n t
    L22 ma la ra gi o ne non v o le per nu ll a che que s to a mm o la s s sa fa re
    L23 de ll a t re gu a con s s g na per ancora non si i n te n do co sa a l cu na ne l h o ma de l cattolico secondo
    L24 i n te n do h a h a v tu che u no va l ta a u di e n t a di que s ta maesta

## Reading by sense (Italian)

**Block 1 (L1-L5)** — clear before: « V.S. per la loro de' 4 del passato monstrono desiderar di saper s'io » ; clear in between:
« Come V.S. di sotto intenderanno, né anche io in tal cosa potrei satisfare a quelle per non sapere nominatim ».
‹D› chi fu il {Svizero} che venne qua et quali erano quelli {amici} di costoro che lo mandorono ‹etc?›, la quale notitia al
presente non è {necessaria} … chi si {mandissi} il prefato {Svizero} et chi {sieno} quelli ‹r O 3^3 r^3 t^3› che costoro
{intractengono} ne' Svizeri, sendo cosa ‹8 t 8› ‹5 c 8› {secreta} {per} il {periculo} che ne {potresse} succedere a quelli
{privati} da loro {cantoni}.
**Block 2 (L6-L11)** — clear before: « Per la mia de' xiij del passato si scripse ».
questa Maestà havere mandato uno {homo} a' Svizeri. {ritraggo} ‹▓ 2^3 Q› di {buon} {loco} che il prefato andò con mandato del
‹3^5 2 3 2 G 2^2 y›, et perché il ‹2^5 6 d 8^2› ‹r O› ‹r^3 3› di havere {trovato} li Svizeri ‹D^1› ostinati, havendoli loro
resposto {maravigliarsi} della {prosuntione} sua, sendo entrato nel paese loro {senza} salvocondocto, monstrando {per} questi
‹9^2 c 8› ‹3 c# Q t# 3 O t^4› la {scusa} ‹S^5 D› in futuro ‹▓› ne ‹barré› uno altro che lo {facessi}, se ne ‹x^2 3^4 7^4 6 Q›.
**Block 3 (L12)** — clear before: « concludendoli esser disposti ».
{volere} il Cristianissimo {per} ‹2^2 t^2 3^3 5› ‹2^2 3^1 m# O 3^2› che Sua Maestà tenga lo ‹3 6 y^1 8 5^4 y 8^2› ‹3^3 3^3 4 p y›.
**Block 4 (L13-L17)** — clear before: « Qua è una honorevole ambasciata dello arciduca, capo el conte di Nansot, e quali » ;
clear in between (end of L14): « [et] io non saprei dire ».
sollicitano la pratica del parentado di madama {Renea} con il loro signore. Costoro non li {disperano} et {intractengono} la
pratica, né io so già con che ‹3^3 t^2 5^5› et … che fine la cosa si {habbia} a havere ; ma {accerto} ‹A› vostre {Signorie}
‹α› {traggo} di {bon} {loco} che e' {Fiammenghi} sollicitano la cosa et costoro la {intractengono}.
**Block 5 (L18-L24)** — new paragraph ; clear after: « Questa M.tà iudicando di gran danno la pompa de' vestimenti … ».
Costoro non fanno {dubio} alcuno di havere {a} rinnovare lo {accordo} con Inghilterra ; ‹A› fino al presente non se ne può dire
cosa {alcuna} di certo. Questa Maestà {continuamente} {afferma} {volere} con {grossissime} {forze} fare la impresa di Italia
senza {restringersi} per ‹3 4^0› alcuno {determinato} ; credo che Sua Maestà ne {habbia} {grandissima} {voluntà}, ma la ragione
non vole per nulla, che questo {anno} la ‹6 6 r^5› fare. Della tregua con {Spagna} per ancora non s'intende cosa alcuna ; né
l'{homo} del Cattolico, secondo intendo, ha {havuto} ‹D› {una} {volta} {audientia} di questa Maestà.

## Changes from the v5a reading

The word sign α is read *per* (key v6): L4 "{secreta} {per} il {periculo}", L22 "la ragione non vole per nulla" (unresolved -> certain), L23 "Della tregua con {Spagna} per ancora non s'intende" (the formula of the pair 345/346; probable -> certain); L16, the only place where *et* would read better, is left unresolved (‹α›).

## Detailed notes

The full French working notes (status, prior work, word-by-word justifications, rates, changes in v6) are frozen in `frozen/LECTURE_307.md`.
