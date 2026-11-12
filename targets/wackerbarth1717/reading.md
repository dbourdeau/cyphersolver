# wackerbarth1717 - reading of Relation XXII (French, spelling of the copy), Vienna 14-16 June 1717

**Project count (strict, 12 Nov 2026): 634 of 716 cipher words = 88.5%, read in part** (`integration_recount.py`: a word
counts only when every letter of it as read is given by the gloss value of the number under it, in either volume). The
share lines further down ("641 / 716 = 89.5%", "The share we report is 89.5%") are the contributor's own count, not the
project's.

Status: read in part. The contributor's count (641 of 716 = 89.5%) leaves out the 24 words marked [restored] or unresolved
whose only missing value is 4 = x, 76 = st or 306 = Vienne, which the glosses of the 1715 volume supply (so "à ‹306›" in view
0090 reads "à Vienne"); the project's count takes them in. It counts 31 words that the project's count does not: {Czar} in
view 0097, which rests on a number probably misread, "de" in view 0094 D17 (its e is taken by 79 = la), and 29 words where the reading gives a gloss-valued number other
letters, passes one over or supplies a letter (e.g. {garantir} on "xarentir", {se} on 78, {donner} on "donqer", du from "d"
alone). The marks in the text are the contributor's and are unchanged.

Relation XXII of August Christoph von Wackerbarth to King Augustus II ("Sire"), copy, Vienna, 14-16 June 1717. Dresden,
Sächsisches Hauptstaatsarchiv, 10026 Geheimes Kabinett, Loc. 00713/01, ff. 71-80v (views 0089-0099). The letter mixes clear
French and cipher. Read by sense from `decryption.txt` (frozen key c, frozen transcription), following the frozen rules of
`frozen/AVENANT-3.md` §3. The working fiche is `frozen/lecture/R22-lecture.txt` (hashed in `frozen/LECTURE-AV3.sha256`);
this page shows the same text, grouped by view.

**Simultaneous work: Anne-Simone Rous** (SBG Sachsen, Dresden) studies this cipher correspondence
(Wackerbarth - Flemming, 1700-1720) and lists the 1717 cipher as not deciphered. This reading was made independently of her
and should be cited with her work. See NOTES.md, "Prior art".

**The condition for reading was decided after the measurement.** The protocol required two tests. The ground-truth test A'
FAILED, and the held-out language test B' PASSED. Brice Dudout then accepted B' alone as the condition for reading this
letter (`frozen/AVENANT-3.md`, hashed at 18:04 on 11 Nov 2026). That decision was taken after both results were known. The 95%
rule is kept as the final check. See `validation.txt`.

## Marks

- _italic_ = words written in clear in the copy (not counted).
- plain = certain (every number has a value in key c, the word is regular French of the time).
- {x} = probable (one letter off on a "probable" homophone of c, or a doubtful number N/M? of the transcription).
- [x] = restored (the word contains a number absent from key c, or a letter we added from the sense).
- ‹…› = unresolved (the number is given).
- Numbers of four digits that fit no word were taken for nulls and are not shown: 5632, 5260, 5250, 6520, 5910, 4351, 3094,
  3254, 3421, 3245.
- "…" inside an italic passage = clear text that was not transcribed in full.
- Word division, accents and apostrophes are ours. The copy's spelling is kept (aye, tems, connoitre, raport, Roy).

## Text

**[view 0089]** quoique jusqu'ici j'aye dit à Votre [majesté] que _selon toute apparence la Cour Imperiale_ tâcheroit de gagner {le} tems qui _pourroit l'eclaircir sur l'issue de la campagne de Hongrie, avant qu'elle feroit connoitre ses veritables sentiments par raport a_ [aux] affaires du {N.} je n'ai pourtant rien {obmis} qui ait pu m'en éclaircir _de plus près, ayant à cette fin toujours continué à faire des representations convenables_

**[view 0090]** jusqu'à ce qu'à la fin le comte de [Sinzendorff] chancelier de _la Cour m'a fait savoir_ lundi passé qu'il avoit ordre de me parler de la part de l'Empereur _qu'il_ se rendroit de [Laxenbourg] à ‹306› et qu'il me prioit de m'y trouver alors chez lui _Ayant satisfait à sa demande il me dit : que_ l'Empereur lui avoit ordonné de me faire savoir comme quoi _après une mure deliberation sur la situation des affaires_ ‹4527› du nord l'Empereur {avoit} pris [la] {résolution} de venir [aux] _moyens les plus convenables à faciliter le_ [rétablissement] de la tranquillité de l'Empire et de [la] [paix] [entière] du [nord] ‹…r› des _fondements assés solides pour en_ assurer [la] durée _Mais, comme il seroit difficile d'obtenir ce but, sans qu'on eut pour objet de l'etablir sur un_

**[view 0091]** [juste] {équilibre} [et] d'y procéder selon la [circonstance] de _la conjoncture avec toute la_ circonspection nécessaire pour les conformer [aux] [loix] de l'Empire _àfin d'y procurer par son_ [approbation] l'autorité nécessaire l'Empereur _dans la persuasion de trouver auprés de_ le Roy et le Roy d'Angleterre des {sentim.} conformes [aux] désirs qu' ‹289› _à cette occasion_ lui [Sinzendorf] venoit de me {donner} à connoître de la part de l'Empereur et pour {convaincre} le Roy en particulier de _la confiance, qu'il avoit en_ le Roy lui avoit voulu faire l'ouverture de la disposition où il se trouvoit d'entrer avec Votre [majesté] [et] le Roy d'Angleterre _confidemment_ dans un concert sur ce qu'il y auroit à faire et à {observer} tant _dans la negociation que dans_

**[view 0092]** [l'exécution] pour {rétablir} [la] tranquillité dans l'Empire et la [paix] dans {le} nord _Etant donc necessaire de convenir à cette fin d'un_ plan pour servir de règle tant dans cette négociation que dans [l'exécution] et l'Empereur venant de communiquer au Roy _ses sentiments sur la_ {base} de ce plan l'Empereur s'attendoit _maintenant_ à ce que sur cette [base] le Roy voulut en échange _confidemment_ communiquer ses {sentim.} _: par raport au_ détail {nécessaire} {pour} faciliter les concerts en [question] que par ordre de l'Empereur lui {le} {comte} de Sinsendorff avoit déjà fait hier la même ouverture à St Saphorin pour {se} mettre en état _de se procurer_ des ordres et [instructions] _à cet egard, qu'il venoit ainsi me le dire aussi pour que je fisse la même chose. ⟨Que⟩, quant à lui: il avoit_

**[view 0093]** {obtenu} de l'Empereur [la] permission d'aller _dans une affaire_ particulière qu'il lui importoit {beaucoup} {faire} un tour à [Inspruck] voyage où il mettroit [douze] à [quinze] jours _en quoi il y auroit d'autant moins de tems perdu, qu'il ⟨en⟩ faudroit meme plus à_ St Saphorin et _peutetre aussi_ à moi pour nous procurer {les} ordres [et] instructions nécess. _: àfin de pouvoir ensuite entrer avec d'autant plus de fondement en matiere. Pour conclusion il y ajouta par raport à_ [la] demeure des Russes dans l'Empire que l'Empereur remettroit de nouveau cette affaire à [la] diète de {Ratisbonne} _que_ ‹172› _etoit chargé de m'en parler; que quant à_ [l'expédition] qui se faisoit dans la {chancellerie} d'Autriche pour _le ministre de ce caractere subsistant à_

**[view 0094]** {Ratisbonne} elle étoit déjà partie _Ce qu'il m'en a dit de plus, est conforme à ce que j'ai deja eu l'honneur de mander à Votre Majesté dans ma relation conjointement signée avec Mr. de ⟨Sech⟩ le 9. de ce mois touchant la_ convocation d'un [congrez] particulier pour {abréger} [les] [délibérations] [et] pour faciliter [l'exécution] _le cas l'exigeant. Il y a apparence, qu'à cette occasion_ l'Empereur pourroit entrer avec le Roy et le Roy d'Angleterre dans {quelque} concert _par raport à_ [aux] Russes _si de notre coté on y laissoit entrevoir quelque envie. Ce que Mr. de_ St Saphorin _m'a depuis donné à connoitre de_ l'ouverture que {le} [chancelier] de la {cour} le comte {de} [Sinzendorf] lui a fait _de la part de l'Empereur au sujet de_ {des} {affaires} du nord [et] de [la] demeure des Russes dans l'Empire _est entierement conforme conforme à tout ce que_ ce comte m'a {dit} par ordre de l'Empereur et que _j'ai eu l'honneur de rapporter ci-dessus. Il m'a en meme tems assuré, qu'il alloit incessament_

**[view 0095]** écrire à sa cour pour demander les plein pouvoir [vu] _que je lui avois dit, qu'il feroit bien, de_ se procurer pour se mettre en état _de pouvoir_ entrer de la part du {Roy} son maître dans ce traité d'une plus étroite liaison _dont il avoit eté question. Selon lui: la Cour Imperiale ayant_ été portée jusqu'à [la] démarche de nous faire connoître sa disposition _à l'egard des_ affaires du nord l' _affaire_ pourroit même {être} menée au point d'en venir à une triple alliance entre l'Empereur le Roy d'Angleterre et le Roy _à quelle occasion il croyoit pouvoir apporter beaucoup de facilité à la_ négociation _Vûque regardant les choses ⟨en⟩ de notre coté, ou du coté de la Cour_

**[view 0096]** impér. on rencontroit des difficultés à [s'expliquer] les {premiers} de sorte que lui comme un troisième _pourroit le faire, et ainsi applanir les difficultés._ {l'observation} du secret dans _cette affaire, Sire, est d'autant plus_ recommandée _que je sai de très bonne part, que le_ {les} ministres de l'Empereur {qui} ont {le} timon entre les {mains} n'ont pas voulu _seulement_ admettre un référendaire à _la conference, qui s'est tenuë à cet egard et que le_ [chancelier] de la cour en a fait lui-même {le} {référat} _sur lequel_ l'Empereur a pris la résolution que {ledit} chancelier {a} {donné} à {connoître} à St [Saphorin] et à moi _Votre Majesté trouvera donc maintenant ici l'effet de_ ses assurances que ‹169› m'a donné avant son [départ] et _dont j'ai fait raport dans ma relation du 12. May. A present Votre Majesté sait le_

**[view 0097]** [sentim.] de cette cour ici par raport au {Czar} _Elle voit bien, que_ l'Empereur [est] déterminé de {concerter} avec {les} directeurs des {cercles} _ce qui est necessaire pour faire_ sortir {les} Russes de l'Empire _et peutêtre même pour le_ {garantir} de {leur} retour _Votre Majesté est de plus informée, comme quoi l'intention du_ le Roy d'Angleterre _va encore plus loin en ce qu'il voudroit, qu'on prit avec_ elle {les} mêmes mesures par {raport} à [la] Pologne _C'est ma relation du 22. May, qui en traite. Maintenant Votre Majesté voit aussi, que_ ‹ls› sont {les} sentiments de l'Empereur _par raport à_ [la] [paix] du {N.} elle {les} trouvera _sigrs. Sans doute_ conformes à son attente _au moins n'ai-je rien obmis qui ait pû_ porter [la] chose à son {but} _à quoi il me reste seulemt. d'ajouter pour l'information de Votre Majesté, que selon l'intention du_

**[view 0098]** le Roy d'Angleterre _on ne doit plus_ rendre au ‹184› un pouce de terre des provinces allemandes qu'il a perdues dans l'Empire _A l'occasion, où le_ [chancelier] de la cour m'a fait l'ouverture _ci-dessus de_ [la] {part} de l'Empereur _je lui ai rafraichi la memoire … Ce ministre m'ayant donné à connoitre qu'en_ chemin il auroit {le} plus de loisir à {les} lire avec l'attention nécessaire _Ne pouvant donc dans cette affaire rien faire de plus avant le_ retour du comte de [Sinzendorff] ni avant [la] réception des [nouveaux] ordres et [instructions] ‹1900205› _de Votre Majesté, je me servirai … qui sera_

**[view 0099]** environ d'une [quinzaine] de jours _des bains de Bade, … que je_ m'y rendisse pour prendre moi-même ses ordres je me {tiendrois} {vers} ce tems là prêt pour aller au-devant _de ce qu'il pourra_ plaire au Roy de m'ordonner _à Vienne. le 16. Juin .1717._

## Count (Daniel's rule; cipher words only)

| class | words |
|---|---|
| certain | 575 |
| probable {x} | 66 |
| restored [x] | 66 |
| unresolved ‹…› | 9 |
| **total** | **716** |

**Certain + probable = 641 / 716 = 89.5%: read in part.** With the restored words: 707 / 716 = 98.7%.
Counted by `frozen/scripts/compte_lecture.py` on `frozen/lecture/R22-lecture.txt`; it gives the same figures again.

- Probable words: one letter rests on a "probable" value of c. The commonest cases are 20 (c says ee; the reading wants b:
  obmis, Ratisbonne, base, observer, rétablir, beaucoup, abréger, but), 78 (c says t; the reading wants le / les) and 13 (m or c).
- Restored words: each contains a number that is absent from key c. Most are 4 (x: aux, paix, exécution, loix, Laxenbourg),
  79 (la), 76 (st: majesté, juste, instructions), 38 (h: chancelier), 40 (b), 73 and 89 (z: Sinzendorf, douze, quinze),
  92 (t) and 1000 (et). There are also single cases: 11 (Inspruc-k), 48 (les), 93 (nor-d), 98 (la) and 118 (est).
- Unresolved: ‹306› (a place name: "se rendroit de Laxenbourg à ‹306›"); ‹4527› (before "du nord"); ‹…r› (296/290);
  ‹289›; ‹172› (a person: "‹172› étoit chargé de m'en parler"); ‹169› (a person who gave assurances "avant son départ");
  ‹ls› (a cipher word read "ls", perhaps "quels"); ‹184› (see Reservations); ‹1900205› (a run with no reading).

## A variant that was NOT adopted

Nine homophones are absent from c but appear at least three times in independent words of this letter: 4 x (18 times),
79 la (12), 76 st (7), 1000 et (5), 38 h (4), 40 b (4), 73 z (4), 89 z (3) and 92 t (3). If they counted as probable, the
share would be about **97.9%**. That would need a fourth amendment, a second decision taken after the measurement, and Brice
Dudout has not taken it. **The share we report is 89.5%.** These values are listed as proposals in `key.tsv` section B.

## Reservations

- **Three numbers are probably misread, by the same misreading** (a "ч"-shaped 7 read as 4). They are left as frozen in the
  transcription and counted as they stand:
  - view 0097 G07, transcribed "174?": the sense and the sub-agent's second look (after freezing) give 177 = le Czar
    ("par raport au Czar");
  - view 0097 G15, transcribed "4?": the sense gives 7 = g ("garantir");
  - view 0098 G03, transcribed "184?": the sense gives 187 = le roi de Suède. That value is proved by the decipherment
    sheet of 24 April 1717. Here it is left as ‹184›, unresolved.
- view 0089 M03 "89/39?": read 89 (Sinzendorf).
- view 0094 D11 "de la c‹4›our": one number too many, a slip of the cipher clerk or of our transcription.
- "du N." (0089 L09, 0097 D11) = du Nord, abbreviated by the clerk.
- The clear name "⟨Sech⟩" (0094 G10) has an ornate initial and is doubtful. Zech, the Saxon resident, is likely; this is
  not checked.
- Nobody has re-read the doubtful numbers blind on the images. AI agents only: no human has checked the reading against
  the scans.
