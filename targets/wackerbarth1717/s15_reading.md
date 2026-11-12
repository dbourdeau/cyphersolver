# wackerbarth1717 - reading of the letter of 20 November 1715 (French): Wackerbarth (camp before Stralsund) to his wife in Vienna, copy

**Project count (strict, 12 Nov 2026): 741 of 922 cipher words = 80.4%, read in part** (`integration_recount.py`: a word
counts only when every letter of it as read is given by the gloss value of the number under it, in either volume). The
96.75% below is the contributor's own count, not the project's.

Status: read in part. The contributor's own count (774 certain, 118 probable, 12 restored, 18 unresolved = 892/922 = 96.75%, reading v2, after
the blind plate W1) also counts 51 words that rest on a value deduced inside this letter or taken from the non-blind reading of
24 April 1717: 96 = le (19 words), 72 = ch (8), 1000 = et (6), 85 = st (4), 64 = c (3), 70 = x (3), 73 (3), 284 = comte (2),
40 = b (2), 609 and 11 (1 each; "boucher" has two of these numbers); two of them ("alliés" in view 0381 right, "ministre" in view 0386 right) are printed below as
certain. In Relation XXII the same kind of word was marked restored and not counted. The marks in the text are the
contributor's and are unchanged. The project's count also leaves out 98 words where the reading gives a gloss-valued
number other letters ({devant} on "desant", {assaut} on "attaut", {triste} on "tuiste"), passes one over ({Poel} on "poeh",
{puisque} on "suque") or supplies letters with no number under them (36 of these are words whose cipher stops short of the
end, possibly the clerk's abbreviations: réellem, allem, Strals ...). Dresden, HStA 10026 Loc. 00712/05, ff. 307-314 (views 0380-0387).

> **Simultaneous work: Anne-Simone Rous.** Anne-Simone Rous (SBG Sachsen, Dresden; "The Keys of Diplomacy", University of Tartu
> repository) works on the Wackerbarth-Flemming cipher correspondence 1700-1720 and reports a glossed simple substitution in 1715.
> Nothing we have seen says that she has read ff. 307-314; she may have. This reading was made without contact with her and must be
> cited as simultaneous work alongside hers.

## Title and attribution (correction)

The volume is catalogued as Flemming-Wackerbarth correspondence, and our own first working inventory of it (made from
thumbnails) had labelled this letter "Flemming (camp before Stralsund) to Wackerbarth". We think it is **Wackerbarth (camp before
Stralsund) to his wife, the Countess of Wackerbarth, in Vienna: a copy**. The attribution is probable and strong:
- the heading of f. 307 reads "Reponse à la lettre de 306. au camp devant Stralsund le 20e 9bre 1715" (first transcribed "8bre": see the date note below), and 306 = Vienna by a gloss
  of the time (view 0389 L31, "la cour de 306" glossed "la cour de Vienne");
- the letter answers "celle du 5me du courant"; the next piece, f. 315 (view 0388), is the "Extrait d'une lettre de 306.66.857 ...
  en date du 5 de 9bre 1715", reporting the same "raisonnement", and a hand of the time wrote above it "La Comtesse de Wa..." and
  "au C. de Wa...";
- the cipher reads "Voilà, ma {chère} femme, de quoi répondre ..." (view 0387 g L12: "ma" and "femme" certain, "chère" probable);
- f. 306 (view 0379), just before, is a jesting "Pleinpouvoir" signed "Le Comte de Wackerbart", "fait au camp devant Stralsund le
  12. ?bre 1715" (month hard to read), which names Flemming in the third person;
- the writer directs the siege batteries and writes to General Dücker and to Count Virmond, the Emperor's minister.
Against: a private letter to the countess is not expected in this cabinet volume. We take ff. 307-314 for a copy sent on to a third
party: a clean secretary's copy, unsigned ("Je suis" only), with marginal notes of a decipherer in another hand ("il sera delogé",
"prisonnier", "le Roy"). Wackerbarth's command of the Saxon corps at Stralsund is confirmed in the literature (NOTES.md, Historical context).

**Date corrected (11 Nov 2026 update): 20 November 1715, not 20 October.** The heading of f. 307 and the title of f. 315 write the month as "9bre" (November), not "8bre": the figure is a 9 with a long descender, the same shape as the 9s in the cipher of view 0388 (e.g. "9.14" = i n in L01). Our first transcription read "8bre"; the frozen transcription files keep that reading unchanged (see the note at the head of `s15_transcription.txt`). The content agrees with November: the letter speaks of the Swedish entrenchment taken before Stralsund (night of 4-5 November 1715) and of the capture of Rügen (landing at Stresow, 15-16 November 1715), while the guns are not yet all in battery. The countess's letter answered is therefore of 5 November 1715. The month of the jesting full power at f. 306 (view 0379, "le 12. ?bre 1715") is hard to read and is left open.

## Marking (cipher words only)

Clear text of the letter is in « … » and NOT counted. Plain word = certain (all its groups read by the frozen key K1715, the word
obvious); {word} = probable: a value taken from S1/1717 (key.tsv section A) or deduced in this letter (**72 = ch** comes from 1717,
**96 = le** is deduced here, 19 occurrences; also 85 st, 70 x, 64 c, 284 comte, 75 s), or a misread or miswritten group corrected
by the immediate context; [word] = restored (letters missing or contradicted); ‹…› = unresolved. 187 = "roi de Suède" counts as
3 words, 168 = "l'Empereur" 2, 150 = "le roi" 2.

## Deviations (declared)

- A reduced thumbnail of view 0380 (and a 450-px contact sheet of 0380-0387, unreadable) was seen at the start, before the
  protocol, to locate the pages; nothing was decoded from it.
- While checking hashes, the control portion CIBLE-0384-g was displayed on screen before the protocol (PREREG-1715) was written;
  the key is a deterministic function of the training files, hashed in the same command before that display.
- Sub-agent A wrote the clear words "roit-on" for "voit-on" (0382-d L06), noticed after hashing; clear text only, not counted.
- The certain/probable classification was made by a single reader (the agent); only the nine words checked by Brice Dudout's
  blind plate W1 had a second, human look (shapes of digits only).
- One frame of the plate (control K1) was re-set after the first build of the plate, before any answer was exported.
- In 0386-d L03 the group read 96 looks like 46 (agent's remark, not tested); a review of 96 = le is suggested.

## Reading v2 (French, as frozen; v1 is kept in the dossier)

Below, unchanged, the body of LECTURE-1715-10-20-v2 (= v1 plus three words made certain by plate W1: 0383 d L14 beaucoup (66),
0384 g L11 embrasser (25), 0385 g L22 mal (25)).

== 0380-d (f. 307)
« …un raisonnement, qu'on Vous a tenu de »
L01-02 l' interest des alliés du nord « par rapport à » au roi de Suède
« Il y a à la verité beaucoup de solide … il y paroit assés evidemment, »
L03-05 « que » ce n' est qu' autant que roi de Suède y trouve son compte « Mais passe quant à cela, pourvû que nous »
L06-08 y trouvions de même réellement {notre} {convenance}
« Vous lui avés fort bien repondu, … ou que l'occasion se presentant Vous pourrés naturellement mettre ce discours sur le tapis, je Vous dirai : qu'il est trés-certain, qu'on »

== 0381-g (f. 307v)
L01-02 « delo- » délogera infailliblement roi de Suède « tout à fait » de l' Allemagne « où »
L03-05 « jusqu'à present il ne lui » reste plus que Stralsund et {Wismar}
L06-07 {devant} Stralsund l' attaque est [poussée] « à un tel point, qu'à moins que »
L08-10 roi de Suède « ne veuille attendre » la dernière extrémité « je veux dire : » un {assaut} général « il n'en sçaura tirer autre avantage, que la satisfaction d'en avoir »
L11-12 resté {le} maître « quelques jours » de plus ‹400›
L13-17 « depuis que » l' {isle} de {Poel} a {esté} enlevée sans aucune perte du [côté] des alliés du nord {Wismar} « se trouve tellement »
L18-22 serrée par terre et par mer « que pour peu que ceux, qui » tiennent cette place bloquée « cessent d'attention, il est impossible, que » elle puisse

== 0381-d (f. 308)
L01-04 « éviter de » {tomber} {encore} cet hiver « Lorsqu'il soit besoin de » l' {assiéger} dans les {formes}
L05-08 « Cette situation des affaires » du roi de Suède « Vous pouvés assés voir, que » ce ‹183› « ne sçauroit plus empecher d'être en peu de tems » {tout} à fait délogé de {l'} {Empire} « ou »
L09-12 du {duché} de deux ponts presqu' [il] « ne sçauroit gueres » incommoder {les} {alliés} du nord
« Le mal, qui arrive par là ne sçauroit être regardé, que comme »
L13-16 un fruit de la {propre} {volonté} de sa majesté suédoise {puisque} ni « la bonne disposition de »
L17-24 {des} alliés du nord pour le rétablissement de la paix « ni les » {exhortations} de l' Empereur et de ses ‹c?eill› « amis pour cette » même paix et pour le « retablissement de » la tranquillité et du repos dans {l'} {Empire} « ni la » {triste}

== 0382-g (f. 308v)
L01-12 situation ‹251› {de} ses affaires « en comparaison de celles de » ses {ennemis} {le} déplorable état de son peuple et « l'épuisement de » ses {propres} forces soit « en » monde soit en argent soit « en autres » besoins pour continuer une {guerre} « seulement avec » ‹aiparene› de « hu[é]es? » contre tant d' ennemis dont
L13-20 {chacun} « en particulier se trouve » {maintenant} « en état de » soutenir la guerre contre lui surtout « à présent qu'il » sera bientôt réduit à un tel point que « difficilement » une puissance {étrangère} voudra s' embarquer avec lui
L21-25 « à moins que ce ne fût » le Turc dont {le} secours est si « éloigné, qu'il est » incapable de redresser ses affaires enfin l'

== 0382-d (f. 309)
L01-08 {expérience} « même n'ayant pû » persuader ce [prince] « par la » continuation de la guerre {que} rendroit « de plus en plus » sa condition pire « Sçau-voit-on regarder » autrement son {état} que « comme un » fruit de sa {propre} {volonté}
L09-18 « il est encore trés-certain, que » le roi est fort disposé à la paix mais à une paix générale aucunement séparée {et} « telle que » raisonnablement la [conjoncture] la peut faire demander {et} telle « aussi, qu'elle doit être pour » assurer ‹270› ‹aue› [le] « fondement » {le} repos « qui en est le but. »
L19-25 « Je Vous dirai de plus que » {le} {roi} n' est aucunement intention [né] de donner {les} mains à une ruine totale de la « Couronne » de Suède « et » le roi est allé si loin « dans ce sentiment » qu' il l' a même

== 0383-g (f. 309v)
L01-02 stipulé dans {les} « traités avec » ses alliés
« Il me semble, que ceci fait assés voir ses »
L03-08 bonnes dispositions pour la {paix} pourvu qu' elle ne soit pas d' une nature qui mette le fondement à une nouvelle guerre mais qu' « on y trouve toute la seureté, qu'on puisse raisonnablement desirer : D'ailleurs le raisonnement, qu'on Vous a tenu, me paroit ressembler en quelque manière à »
L09-14 la lettre {que} {Mr} {le} {comte} de {Croissy} {écrivit} au commencement de cette campagne « où il prouvoit » la fermeté du roi de Suède {et}
L14-20 où il représentoit « les inconvenients, où le » s {alliés} alloient s' exposer en prenant la {résolution} d' attaquer ce [prince] dans Stralsund et Rugen ‹4008› ‹10009› ‹680›

== 0383-d (f. 310)
« Il est vrai, que dans le raisonnement, qu'on Vous a tenu, il y a plus de moderation ; mais, »
L01-04 « nous » dépeignant ce {qu'} « nous » aurions à craindre de ce {prince} en Pologne et {le} dépeignant « d'une maniere, que nous en »
L05-10 devrions craindre plus qu' aucun des autres puissances qui lui font la guerre « nous donnant en même tems de la » fermeté de {ce} [prince] à {poursuivre} ses
L11-16 desseins une idée « qui nous doit persuader, que nous » en avons beaucoup à {craindre} pourroit-on {raisonnablement} « esperer, que pareilles insinuations puissent avoir un effét Different à celui de »
L17-22 la lettre de Mr Croissy « qui n'a produit qu'une » plus étroite liaison entre les alliés et l' « augmentation » des ennemis du roi de Suède pour {le}

== 0384-g (f. 310v) — PORTION DE CONTRÔLE
L01-03 réduire à une paix telle que « la conjoncture » la peut raisonnablement demander
L04-09 « et que » roi de Suède s' est fait une raison de rejetter ces suites {fâcheuses} {qu'} on nous « fait » envisager ne « nous doivent »
L09-13 elles pas porter à embrasser les moyens les plus sûrs pour nous « mettre à couvert »
L14-21 « de » ce {qu'} on nous veut faire craindre des {débris} que roi de Suède pourroit amasser pour retourner de nouveau en {Pologne} se mettre à la tête de nos rebelles
L22-26 {donc} « à ce que celui qui vous a si confidemment parlé, assure, » il trouvera les deux tiers pour lui {et} quel

== 0384-d (f. 311)
L01-07 moyen {pourroit} être plus « sur et » plus efficace que de détruire lorsque « nous le pouvons, » ces débris avant « qu'ils puissent servir » de moyen à fortifier
L08-14 roi de Suède dans une fermeté « aussi » pernicieuse pour lui que pour « nous autres » tout ce qui reste de ces débris qu' on nous veut faire {craindre} et « ce qui n'en a pas été » détruit
L15-23 sur l' isle de {Usedom} « dans le » {retranchement} qu' on lui a enlevé ici devant {Stralsund} et sur l' isle de Rugen se trouve « à présent avec » la propre {personne} du roi de Suède dans la ville de Stralsund

== 0385-g (f. 311v)
L01-04 « qui » du côté de terre {est} « entièrement en » {clavée} et ne {le} sera pas {moins} par mer
L05-12 « depuis » la prise de Rugen si « le » s danois comme ils « assure » nt « ont envoyé » des prames et des frégates « pour » {boucher} des deux côtés la sortie de Stralsund par eau
L13-24 « Dans cette situation, où les » [débris] des forces du roi de Suède et sa {propre} personne dont [nous] [devons] craindre {le} retour en {Pologne} « se trouvent en » fermés dans {Stralsund} « ne devons nous pas pren- » prévenir {le} mal qu' « à ce qu'on prétend, nous » menaces

== 0385-d (f. 312)
L01-05 ‹ce› {tâcher} de détruire ces débris lorsqu' il est dans notre pouvoir de le faire
L06-09 « Le reste, qui est » dans {Wismar} ne pouvant plus se sauver et {devant} succomber « ainsi que je l'ai dit ci-dessus. »
L10-21 « Cette situation, où » roi de Suède « se trouve actuellement, ne lui » laissant aucun « aucun » parti à prendre que de {nous} rendre la place et d' accepter la {paix} ou d' « attendre un » assaut général et de {s'} {exposer} à « être » massacré « avec tout » son monde ou d' être « fait » prisonnier « me fera embrasser »

== 0386-g (f. 312v)
L01-07 « le parti » d' écrire au général {Ducker} « dès aussitôt que la plus grande partie de » nos canons {et} de nos mortiers seront menés aux batteries « Surtout »
L07-14 me trouvant si près de l' angle {saillant} de la {contrescarpe} que « au plutard » je pourrai me rendre maître en ‹357› ou ‹358› fois ‹365› ‹358› heures et « faire » jouer
L15-21 « en même tems tous » les canons {et} mortiers {et} j' {essaierai} « avant que d'en venir là, si par les représentations, que je ferai au dit » général « par » ma lettre il « pourroit » {toucher} {le} cœur de son roi « pour qu'en prenant la résolution »

== 0386-d (f. 313)
L01-05 « de » rendre la ville et de venir à une {paix} générale ce prince détourne {le} mal qu' « il ne sçauroit plus éviter autrement. En usant de la sorte n'est ce pas donner une nouvelle marque indubitable de la bonne intention » {du} roi pour la {paix}
« J'écrirai encore aujourd'hui à Mons.r »
L08-10 le {comte} Virmond ministre de l' Empereur pour {le} prier « de venir se rendre incessament auprès de moi, afin que »
L11-18 roi de Suède par l' état pitoyable où il se trouve par la compassion qu' il doit à son peuple et « par mes représentations se laissant fléchir pour en venir » à traiter de la paix cela « puisse toujours » se faire sous la

== 0387-g (f. 313v)
L01-02 direction et par la médiation de l' Empereur
L03 « J'espère que ceci convainquera de plus » ‹68›
L04-07 « des égards, que » le roi « a en toutes occasions pour le » gloire et {les} intérêts de sa majesté impériale
L08-11 « Je ne puis que me persuader que » ‹94› cour impériale lui en saura bon gré et que ‹échangée/engagée› elle « épousera en toutes occasions les intérêts … avec le même empressement. »
L12 « Voilà, » ma {chère} femme « de quoi répondre à ceux, qui vous tiennent des discours … sans affectation. »
L13-14 « Je travaille » non sans espérance de succès « à porter »

== 0387-d (f. 314)
L01-06 « à porter le » {choses} ici à un point {que} {les} opérations de la guerre « ne nous y puissent plus fournir de » sujet d' {occupations} « Je suis »
