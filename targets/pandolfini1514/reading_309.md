# Reading: ASF MAP LXXII 309: read in part

ASF Mediceo avanti il Principato LXXII, doc. 309 (c. 378r, pos. 755): letter of Francesco Pandolfini to Lorenzo de' Medici, "Ex Parisiis die xxvj februarii M.D.xiiij" (= 26 Feb 1515), in clear with two cipher blocks (A: 3 lines, B: 4 lines). Bare letter: no decipherment of the time found. Key: `key_v6.json` (declared merge of the derived keys v5a and v5b of `key_v4.json`, see NOTES.md; **not measured**, the only measured key is v3, partial). Conventions (Daniel's): plain = certain; {x} = probable; [x] = restored; ‹…› = unresolved (tokens shown, `_` = space between tokens). Clear passages of the letter are given in [brackets] for context.

## Status

**Read in part: 83 cipher words, 59 certain, 16 probable, 0 restored, 8 unresolved = 90% read by sense.** Block A 31 words (about 94%), block B 52 words (about 88%). Below the 95% rule.

## Raw decoding, key v6 (unretouched, `frozen/decode_v6.py`)

    A1 le o f s e r te che ma da ma di a n ge l m so p ra i l ra ge o na me n te di l ‹.48.›
    A2 a t ca no ne fe ce a di pa s si t a ll o l o ra to re de l papa de l pa re n ta do de ll a fi g li a de l
    A3 du ca va le n t no per vo s t ra ma g ni ? ce n t di
    B1 fi no a g che le i non ve gg i a che con le o c g e si a h n e ri s ca e ? a h
    B2 a l t ri che a suamaesta la qua le con de si de ri o a s pe c ta ve de re che re so lu ti o ne et de o la ra t o ne
    B3 fa ra la papa a l g? a f e o g na ? to li da ll a le ga nu o va me n te fa o ta pa re n do li da que s to
    B4 po s se r co no s ce re qua l si a la me n te di papa ve r so di suamaesta 

## Reading by sense (Italian)

**Block A (A1-A3)**
le {offerte} che madama di {Angolem} sopra il {ragionamento} del ‹.48.› ‹3 Z 2^5 t^2› ne {fece} a dì {passati} {allo} {oratore}
del papa del parentado della figlia del {duca} {Valentino} {per} vostra {Magnificentia}.
**Block B (B1-B4)**
[clear before: … multiplicando] fino a ‹4› che lei non {veggia} che con le ‹O 0 4 Q› ‹r^3 3 r t Q› ‹7^3 6 2^5 Q? u? 3 r› altri che a Sua
Maestà, la quale con desiderio aspecta vedere che resolutione et {declaratione} farà {la} papa ‹3 c 4^0› ‹3 J Q O G t^5 L#^4 8^2 x^3›
dalla lega nuovamente {facta}, parendoli da questo posser {conoscere} quale sia la mente di papa verso di Sua Maestà.

## Detailed notes

The full French working notes (status, prior work, word-by-word justifications, rates, changes in v6) are frozen in `frozen/LECTURE_309.md`.
