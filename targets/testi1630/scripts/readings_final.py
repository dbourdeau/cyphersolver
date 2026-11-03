# readings_final.py : write reading_<doc>.md (whole letter, clear and cipher marked apart, editorial notes) and translation_<doc>.md, recount the words,
# and compare each reading with its decryption letter by letter. Every departure must appear in the editorial notes.
import re,glob,unicodedata
NOTE=("Plain text was written in cipher. *Italics* were written in clear. Marks: `[x]` a letter damaged, lost or changed by the editor "
      "(each change is listed under Editorial notes); `[?word]` doubtful; `[...]` hole; `[deleted]` ink struck out by the writer. "
      "Writer's spelling is kept in the cipher. Word division, accents and punctuation are added. Abbreviations in the clear text are expanded. "
      "The clear text was read from the images and is less tested than the cipher. The letter-for-letter text is in the decryption file.")
D={}
D['cc07r_1630-02-07']=dict(title="c. 7r, 7 Feb 1630: Francesco I d'Este, countersigned Fulvio Testi, to Ottavio Bolognesi. No decipherment in the file",
it="""*Francesco Duca di Modona &c.*

*A quello che più diffusamente per l'altra nostra vi habbiamo scritto* l'aviso che ci ariva in questo punto de la retentione del principe di Corre[g]gio, e gli sta come prigione in Correggio attorniato e guardato dagli alemani e con precetto di constituirsi in Sabioneta dentro il termine di venticinque giorni. Il negotio strigne e dubitiamo grandemente che le cose di questo signore non vadano a traverso. Sollecitate vi negli offici e se è possibile guadagnate il punto della preventione. Sappiamo che vi premerà il pericolo del vostro principe naturale, perché noi medesimi il [?compiamo], ma dopo che irreparabile è la su[a] ruina non lasciate di cooperare a nostri interes[s]i, quali come vedete stanno tutti appoggiati ala vostra fede. *Promettendovene un merito singolare et aspettandone effetto di prontissima gratitudine. E Dio vi contenti. Di Modena li 7 febbraio 1630.*

*Francesco. Don Fulvio Testi.* At the foot: *Bolognese.*""",
en="""*Francesco, Duke of Modena &c.*

*To what we wrote to you at more length in our other letter* [we add] the news that reaches us at this moment of the detention of the prince of Correggio; he is held as a prisoner in Correggio, surrounded and guarded by the Germans, with an order to present himself at Sabbioneta within twenty-five days. The business is pressing, and we greatly fear that this lord's affairs will go wrong. Press on with your offices and, if possible, gain the point of forestalling. We know the danger of your natural prince will weigh on you, since we ourselves [?feel for] him; but once his ruin is beyond repair, do not fail to work for our interests, which, as you see, all rest on your good faith. *We promise you a singular merit for it, and you may expect the effect of a most ready gratitude. God content you. Modena, 7 February 1630.*

*Francesco. Don Fulvio Testi.* At the foot: *Bolognese.*""",
notes=["l. 14, \"compiamo\": the signs are certain (D N o # 2 A o N). As written it gives no sense here. A slip for compatiamo or compiagniamo would fit; neither is adopted. The translation \"feel for\" is a guess from context.",
"The clear opening runs straight into the cipher with no main verb. \"We add\" in the English is supplied.",
"l. 4, Corre[g]gio: one g sign on the page; l. 5 has two. Writer's slip, changed by the editor. l. 8, strigne: the signs are g then n, a form of stringe. The earlier text had swapped them. l. 14, su[a]: the last sign is at a tear, only its left stroke remains. l. 15, cooperare a: the a sign is on the page and had been dropped. interes[s]i: the second s runs into a hole at the edge.",
"Thin vertical strokes run through the cipher of l. 8-16 and fall at word divisions. They are a reader's marks, not signs. So is a small dark cross above \"cose\" at l. 9. See NOTES.",
"All cipher lines were read sign by sign on full-resolution strips in the final round. The changes are in retranscription_log_c7r.tsv."])
D['cc09_1630-02-15']=dict(title="cc. 9r-9v, 15 Feb 1630: Francesco I d'Este, countersigned Fulvio Testi, to Ottavio Bolognesi. Marked Duplicato. No decipherment in the file",
it="""*Duplicato. Francesco Duca di Modana &c.*

*Tutti gli avvisi che voi ci date colla vostra delli 26 del passato ci sono stati carissimi:* trato e il mottivo che da quel tal ministro di Cesare fu fatto al dottore Genuino. *Sin dal principio* quando sentimo diferirsi la risul[u]zione intorno al nego[z]io del *[?Feudo]* e vedemmo la cosa incaminarsi per via delle lunghezze, dubbitammo che questi fossero pretesti per nutrirci di speranze e per cavarne appunto da n[o]i in queste [c]ongiunture tutto quello che credono poter loro essere di servigio. *Desideriamo però* d'inganarci, e ci dorrebbe che non fosse trattato con noi con quella candidezza che costì si professa, e che per altro merita la nostra isquisita divozione. Sarà bene che voi stiate o[c]ulato e che, vegnendone il taglio, ne facciate come di vostro senso qualche tocco a quei ministri che voi havete per più confiden[t]i, ma la cosa è dilicata e bisogna maneggiarla. *Si è sparsa voce, e viene registrata publicamente* che gli alemanni habbiano tolto il feudo al principe di Castiglione per essersi dimostrato forse troppo parziale de' veneziani. Se ciò è vero, che voi di ragione il saperete, grande strada si apre a cotesti ministri di favorir noi e di dare in un medesimo tempo soddisfazione al duca di Guastalla. A noi si potrebbe concedere Correggio, all'altro il principato di Castiglione, che amendue per la vicinanza de' detti stati rimarressimo egualmente accomodati. Proponete et adoperatevi colla solita fede et accuratezza, perché riuscendo il negozio colmerete d'un merito straordinario ogni vostra passata azione. *Non vi scordate di* [?roliet] invigilate alle [deleted] cose della Mirandola, perché qui comunemente si tiene ch'elle siano incamminate per via molto sinistra, e in questo caso la prevenzione sarà di gran vantaggio. *Habbiamo a memoria* il ripiego della permuta *che per altre nostre vi habbiamo accennato, e servitevene opportunamente. Che senza più vi auguriamo da Dio ogni contento. Di Modana li 15 febbraio 1630.*

*Francesco. Don Fulvio Testi.* At the foot of c. 9r: *Ottavio Bolognesi.*""",
en="""*Duplicate. Francesco, Duke of Modena &c.*

*All the news you give us in your letter of the 26th of last month has been most welcome:* the [?move] and the motive that was put by that minister of the Emperor to doctor Genuino. *From the very start*, when we heard that the decision on the business of the [?Fief] was being put off and saw the matter being sent along the road of delay, we suspected that these were pretexts to feed us with hopes and to draw from us in these conjunctures all that they think may serve them. *We wish, however,* to be mistaken, and it would grieve us not to be dealt with in that candour which is professed there, and which our exquisite devotion otherwise deserves. It will be well that you stay watchful and that, if the occasion comes, you drop some hint of it, as if on your own account, to those ministers you hold most in confidence; but the matter is delicate and must be handled with care. *Word has spread, and is being reported publicly,* that the Germans have taken the fief from the prince of Castiglione for having shown himself perhaps too partial to the Venetians. If this is true, as you will surely know, a great road opens for those ministers to favour us and at the same time satisfy the duke of Guastalla. Correggio could be granted to us and the principality of Castiglione to the other, so that both, by the nearness of those states, would remain equally well accommodated. Propose this and work at it with your usual faith and care, for if the business succeeds you will crown all your past actions with an extraordinary merit. *Do not forget* [unresolved word]; keep watch on the affairs of Mirandola, for here it is commonly held that they are on a very bad road, and in that case forestalling will be of great advantage. *We remember* the expedient of the exchange *which we mentioned to you in other letters of ours, and use it at the right moment. With nothing more, we wish you every content from God. Modena, 15 February 1630.*

*Francesco. Don Fulvio Testi.* At the foot of c. 9r: *Ottavio Bolognesi.*""",
notes=["c. 9r l. 5, risul[u]zione: blot over one sign, restored from sense. l. 9, n[o]i: hole in the paper after the n sign, restored from sense.",
"c. 9r l. 6, nego[z]io: the sign is torn. Its top bar favours z; t is not excluded. c. 7r has negotio, c. 9v negozio.",
"c. 9r l. 9, [c]ongiunture, and l. 14, o[c]ulato: the sign on the page is A-shaped, so the signs give \"aongiunture\" and \"oaulato\". Sense needs c. Both readers agree on the shape; on l. 14 a blot sits at its foot. Changed by the editor. The same thing happens in c. 11r (\"proaessi\").",
"c. 9r l. 12, candidezza: the a stands above the line, over the next sign. An insertion by the writer.",
"c. 9r l. 15, vegnendone: the signs are v-e-g-n-e-n-d-o-n-e. The earlier text \"vedendone\" was a repair and is withdrawn.",
"c. 9r l. 17, confiden[t]i: the signs give \"confidenui\", u for t. Writer's slip, changed by the editor. dilicata: the signs have i, not e, under a blot.",
"c. 9r l. 22, di favorir: the signs have i. The earlier \"da\" is withdrawn.",
"c. 9v l. 6, colmerete d'un: the d sign is on the page and had been dropped.",
"c. 9v l. 8, [?roliet]: letters r-o-l-i-e-t, read the same by both readers. Perhaps a name followed by et (\"Roli et invigilate\"), but the name is not identified and the sentence does not settle it. Left open. A solid black block follows \"alle\", about 2 signs, struck out by the writer.",
"c. 9r l. 3, trato: as written, single t. l. 6, [?Feudo]: clear word, doubtful."])
D['cc11r_1630-02-15']=dict(title="c. 11r, 15 Feb 1630: Francesco I d'Este, countersigned Fulvio Testi, to Ottavio Bolognesi. No decipherment in the file",
it="""*[?Duplicato, heavily overwritten.] Francesco Duca di Modana &c.*

*Scriviamo per giunta di quello che per altre nostre vi habbiamo scritto le presenti due righe. Se nel maneggio di cotesti interessi conoscerete che* il duca della Mirandola corra qualco rischio, e che vi sia pensiero di formar anche contro di lui pro[c]essi e cause, datene parte a Sua Eccelenza e raccontatele il fatto puro e nudo come sta, senza diminuirlo o scemarlo, anzi sarà bene che più tosto l'amplifichiate, perché la soverchia fiducia non l'induca a trascurarlo. *Mandiamo poi* la lettera aperta in nostra mano. *E Dio vi contenti. Di Modana li 15 febbraio 1630.*

*Francesco. Don Fulvio Testi.* At the foot: *S. Ottavio Bolognesi.*""",
en="""*[?Duplicate.] Francesco, Duke of Modena &c.*

*We write these two lines in addition to what we wrote to you in other letters of ours. If in handling those interests you learn that* the duke of Mirandola runs some risk, and that there is thought of bringing trials and suits against him too, inform His Excellency and tell him the fact pure and naked as it stands, without lessening or diminishing it; indeed it will be well that you rather enlarge it, so that excessive trust does not lead him to neglect it. *We then send* the letter open, in our own hand. *God content you. Modena, 15 February 1630.*

*Francesco. Don Fulvio Testi.* At the foot: *S. Ottavio Bolognesi.*""",
notes=["l. 5, qualco: as the signs stand, for qualche. Kept. che vi sia: there is no q sign; the earlier \"che qui sia\" is withdrawn.",
"l. 6, pro[c]essi: the signs give \"proaessi\", an A-shaped sign where sense needs c. Changed by the editor.",
"l. 8, diminuirlo o scemarlo: there is no n sign; the earlier \"no scemarlo\" and its note are withdrawn.",
"\"Sua Eccellenza\" is not identified. It may be the duke of Mirandola himself. In c. 23r the clear text uses S. E. for the prince of Correggio."])
D['cc16_1630-02-22']=dict(title="cc. 16r-16v, 22 Feb 1630: Francesco I d'Este, countersigned Fulvio Testi, to Ottavio Bolognesi. No decipherment in the file",
it="""*Francesco Duca di Modona &c.*

*[?Ora ci è] uscito di mente un punto assai principale, e però aggiungiamo anche queste due righe a quello che per l'altre due nostre diffusamente vi habbiamo scritto.* Può sucedere di leggiero che, proseguendo la guerra in Ita[lia], cotesti mini[s]tri facciano instanza d[i a]ver da noi danari e munitioni, e le larghissime offerte fatte dal marchese di Villafranca servirà loro d'invito e di pretesto. Quante alle munizioni, egli è di dovere che noi teniamo ben provedute le [n]ostre piazze, stante la giustissi[ma ge]losia in che ci [deleted] tengono i principi circonvicini, e tanto è lontano che noi potiamo soministrarne ad altri, che siamo in necessità di procurarne a noi medesimi da altra parte. Circa il denaro voi sapete l'angustia del paese. Oltre la grossa somma che si è sborsata al conte di Collalto per esimerci [d]all'alloggio, possiamo con verità asseverare che in pochissimo tempo per fare provisione di grani sono da questi stati usciti più di qua[tt]rocentomila scudi, e che questi popoli, come tutti gl[i] altri d'Italia, sono restati per la continuata sterilità delle stagioni [?coni] vuoti et esausti che sarebbe mera impietà l'aggravarli di vantaggio. *In evento che ve ne sia fatto alcun motivo, servitevi delle sopradette ragioni, e mostrate di farlo non di nostra commessione ma di vostro proposito. Avvertite però sempre di non ventilare in cotesta materia se non ricercato, e per necessità. Sarà forse anche opportuno che* rinoviate ma con garbo al *[?Inviato predetto]* la speranza dell'accasamento tra suo figlio e la principessa Margarita no[str]a sorella, non solo per agevolare il ne[go]zio di Corre[g]gio, ma per facilitar anche quello del nostro matrimonio. Avvertite però di farlo in modo conveniente e che non possa pregiudicare alla nostra dignità. *Dio vi conceda ogni bene. Di Modena li 22 febbraio 1630.*

*Francesco. Don Fulvio Testi.* At the foot of c. 16r: *Bolognesi.*""",
en="""*Francesco, Duke of Modena &c.*

*[?It has] slipped our mind a very important point, and so we add these two lines to what we wrote to you at length in our other two letters.* It may easily happen that, if the war goes on in Italy, those ministers will press to have money and munitions from us, and the very large offers made by the marchese of Villafranca will serve them as invitation and pretext. As to munitions, it is our duty to keep our fortresses well supplied, given the most just jealousy in which the neighbouring princes hold us; and we are so far from being able to supply others with them that we are obliged to procure them for ourselves from elsewhere. As to money, you know the straits of the country. Besides the large sum paid out to Count Collalto to exempt us from the quartering, we can truly affirm that in a very short time more than four hundred thousand scudi have gone out of these states to buy grain, and that these peoples, like all the others of Italy, have been left [?so] empty and exhausted by the continued sterility of the seasons that it would be sheer cruelty to burden them further. *Should any move be made to you about this, use the reasons given above, and show that you do so not on our commission but of your own accord. Take care always not to raise this matter unless asked, and of necessity. It will perhaps also be opportune that* you renew, but with tact, to the *[?said envoy]* the hope of the match between his son and the princess Margarita our sister, not only to ease the business of Correggio but also to further that of our own marriage. Take care, however, to do it in a suitable way and so that it cannot prejudice our dignity. *God grant you every good. Modena, 22 February 1630.*

*Francesco. Don Fulvio Testi.* At the foot of c. 16r: *Bolognesi.*""",
notes=["c. 16r l. 5, Ita[lia], l. 6, d[i a]ver, l. 11, giustissi[ma ge]losia, l. 21, qua[tt]rocento, c. 16v l. 1, gl[i], l. 10, no[str]a and ne[go]zio: stains, holes or tears, restored from sense and traces. In giustissi[ma ge]losia the box and the g and e show in part under the stain.",
"c. 16r l. 6: mini[s]tri has a blot over the s. \"d[i a]ver\" is followed by blank paper. The earlier \"[?per]\" is not on the page and is withdrawn.",
"c. 16r l. 7, munitioni, with t; l. 9, munizioni, with z. Both are as written. larghissime has the h sign.",
"c. 16r l. 8: \"servirà\" with a plural subject, as written. l. 9: \"Quante\" for quanto, as written.",
"c. 16r l. 12: a blot over 4 or 5 signs after \"che\", taken as a deletion because the sentence runs through it.",
"c. 16r l. 14, soministrarne: one m, as written, with the n sign. l. 15, procurarne and da altra parte, as written.",
"c. 16r l. 16, l'angustia: the signs are l-a-n-g-u-s-t-i-a. The earlier \"lo stato\" was a repair and is withdrawn.",
"c. 16r l. 18, [d]all': the signs are c-a-l-l, c for d. Writer's slip, changed by the editor. The earlier text hid the sign. l. 19: there is no e before possiamo; the earlier \"e\" is withdrawn.",
"c. 16v l. 1, restati: the signs r e are on the page and had been dropped.",
"c. 16v l. 2, [?coni]: the signs are certain and both readers agree. Sense needs così. Left doubtful, not changed.",
"c. 16v l. 3: \"l'aggravarli\", the l sign is on the page.",
"c. 16v l. 11, Corre[g]gio: one g sign on the page. Writer's slip, changed by the editor. \"facilitar\": no e on the page.",
"Whose son is meant depends on the doubtful clear word at c. 16v l. 8."])
D['cc20_1630-03-01']=dict(title="cc. 20r-20v, 1 Mar 1630: Francesco I d'Este, countersigned Fulvio Testi, to Ottavio Bolognesi. No decipherment in the file",
it="""*Francesco Duca di Modona &c.*

*L'intendere dalle penultime vostre, che il Corriere di Venezia è stato svaligiato a' i confini di Gradisca ci fa dubitare, che alcuni dispacci che vi habbiamo spediti per negozi a Noi molto importanti non siano stati intercetti, ò non habbiano incontrato sinistro ricapito. Vene mandiamo però con questa i dupplicati, rinovandovi gli ordini medesimi, mentre non gli habbiate a quest'ora eseguiti.* Già voi stesso vedete che le cose del principe di Correggio sono pessimamente incaminate. *La vostra fede sù la quale s'appoggiamo tutte le nostre negoziazioni può acquistarvi merito straordinario. Ma cotesti interessi* come che siano qu[a]lificati da grandissi[m]e circo[s]tanze portano seco suspi[z]ioni e gelosie. *Non è compatibile col nostro servigio, e non è forse anche permissibile alla vostra riputazione che in un tempo medesimo voi trattiate le cose nostre, e che nello stesso procuriate quelli de gli altri:* quanto gli affari del signor duca della Mirandola e quelli del principe del [p]rincipe di Correggio siano presentemente discrep[a]nti d[a] nostri, ci[a]scuno il conosce. *Fa di mestiere o che rinnunciate gli uni, ò che lasciate gli altri, perché il servire a più d'un Signore è totalmente impossibile. Ma della vostra volontà ci promettiamo ogni più sicura, et amorevole dimostrazione, nè potràmo mai credere, che nell'animo vostro prevaglia il desiderio dell'altrui comodo alla premura de' nostri interessi. Stiamo nel resto sù le commissioni contenute ne dupplicati, e vi replichiamo solamente la vigilanza, e la sollecitudine.*

*La levata de' grani, che ci proponete in coteste parti, non comple al nostro servizio, e rimossi tutti gli altri rispetti la sola lontananza basterebbe per difficultarne l'effetto. Tanto potrete rispondere a quelli, che ve n'hanno parlato. E senza più vi auguriamo da Dio Signore vera contentezza, e prosperità. Di Modona il primo di Marzo 1630.*

*Francesco. Don Fulvio Testi.*""",
en="""*Francesco, Duke of Modena &c.*

*Learning from your last letter but one that the courier of Venice was robbed at the borders of Gradisca makes us fear that certain dispatches we sent you on business of great importance to us may have been intercepted, or met with some mishap. We therefore send you the duplicates with this letter, renewing the same orders, in case you have not carried them out by now.* You yourself already see that the affairs of the prince of Correggio are going very badly. *Your good faith, on which all our negotiations rest, can earn you extraordinary merit. But those interests,* however much qualified by very great circumstances, bring with them suspicions and jealousies. *It is not compatible with our service, and perhaps not even permissible to your reputation, that at one and the same time you handle our affairs and in the same breath procure those of others:* how far the affairs of the lord duke of Mirandola and those of the prince of Correggio are at present at odds with ours, everyone knows. *You must either give up the one or leave the others, for to serve more than one Lord is wholly impossible. But of your will we promise ourselves every surest and most loving proof, nor could we ever believe that in your mind the desire for another's advantage prevails over the urgency of our interests. For the rest we stand by the commissions contained in the duplicates, and repeat to you only vigilance and diligence.*

*The raising of grain that you propose to us in those parts does not suit our service; and all other considerations aside, the distance alone would be enough to make it difficult. So much you may answer to those who have spoken to you of it. With nothing more, we wish you from the Lord God true contentment and prosperity. Modena, 1 March 1630.*

*Francesco. Don Fulvio Testi.*""",
notes=["c. 20r l. 12, qu[a]lificati: the signs give \"quclificati\", the closed D sign for a. Writer's slip, changed by the editor.",
"c. 20r l. 12, grandissi[m]e, and l. 13, suspi[z]ioni: a blot covers one sign each. Restored from sense.",
"c. 20r l. 12, circo[s]tanze: the signs give \"circontanze\", n for s. Writer's slip, changed by the editor.",
"c. 20r l. 17-18: \"del principe del qrincipe\". q for p is changed to [p]; the repeated \"del principe\" is kept as written. Both readers agree on the signs.",
"c. 20v l. 1, discrep[a]nti d[a] nostri, ci[a]scuno: on this line every a is written with the closed D sign, so the signs give \"crepcnti dc nostri cicscuno\". Changed by the editor. There is no i after da and no e before ciascuno; the earlier \"dai nostri, e ciascuno\" is withdrawn.",
"The clear text explains the letter: the courier of Venice was robbed at Gradisca, and duplicates are enclosed. c. 9r is marked Duplicato."])
D['cc23r_1630-03-14']=dict(title="c. 23r, 14 Mar 1630: Francesco I d'Este, countersigned Fulvio Testi, to Ottavio Bolognesi. Key source. Later decipherment at c. 22: a transcription job, not a break",
it="""*Francesco Duca di Modana &c.*

*Coll'opportunità del presente Corriere che il Signor Principe di Correggio spedisce costà per li suoi correnti affari a voi molto ben noti v'ordineremo qualche cosa di nostro servigio oltre quello che per altra nostra vi habbiamo scritto a favore di S. E.* Ci contentiamo che informiate il Carnevale, ma avvertite che coteste informazioni siano tali che non possano pregiudicare a nostri interessi. Dategliele più generali che sia possibile, e ricordatevi ch'essendo irreparabile il precipizio di questo signore noi dobbiamo premere nel nostro servigio più che in quello degli altri, sicome voi siete obligato a cooperarci con affetto e sentimento proporzionato alla nostra confidenza. Regolatevi conforme alla vostra solita prudenza. *E Dio vi contenti. Di Modana li 14 Marzo 1630.*

*Francesco. Don Fulvio Testi.*""",
en="""*Francesco, Duke of Modena &c.*

*With the chance of the present courier, whom the Lord Prince of Correggio is sending there for his current affairs, well known to you, we shall order you something of our service, beyond what we wrote to you in another letter of ours in favour of His Excellency.* We agree that you inform Carnevale, but take care that this information be such as cannot prejudice our interests. Give it to him in as general terms as possible, and remember that, the fall of this lord being beyond repair, we must press our own service rather than that of others, just as you are bound to work with us with an affection and feeling in proportion to our trust. Govern yourself by your usual prudence. *God content you. Modena, 14 March 1630.*

*Francesco. Don Fulvio Testi.*""",
notes=["c. 22 is a clear copy in a later hand, headed \"Copia dall'autografo\". It has \"molto\" after premere, a struck \"sito\" after questo, and a closing \"e Dio vi contenti\" that is in clear here.",
"Carnevale is not identified. The writer of c. 22 could read this cipher; see NOTES."])
D['cc13r_1630-02-22_lines1-8']=dict(title="c. 13r, 22 Feb 1630, first 8 cipher lines only. Held-out passage. Later decipherment at c. 15: a transcription job, not a break. READ IN PART",
it="""[Clear text before this passage, and the rest of c. 13r, c. 13v and c. 14r, not transcribed.]

Per agevolare l'esi[to] delle sue negoziazioni ha fatte a cotesti ministri et all'imperatore stesso offerte grandissime della persona nostra e de' nostri stati, e ch'egli è fi[n g]iunto ad esibire e promettere a *[?fermo]* in queste turbolenze d'Italia quindecimila fanti e quattrocento cavalli. *Supponiamo che* la mente del marchese fosse rettissima, ma non può negarsi che questo""",
en="""[Not transcribed.]

To ease the outcome of his negotiations he has made to those ministers and to the Emperor himself very large offers of our person and of our states, and he has gone as far as to offer and promise *[?for certain]* in these troubles of Italy fifteen thousand foot and four hundred horse. *Let us suppose that* the marquis's mind was entirely upright, yet it cannot be denied that this""",
notes=["Only this passage was transcribed. c. 15, in a later hand, covers the rest. The catalogue marks the addressee of cc. 13-15 as uncertain.",
"l. 5, [?fermo]: a clear word, fe + minims + o; c. 15 leaves it out. \"Promettere a fermo\", to promise firmly, fits better than the earlier \"a ferro\", which is withdrawn."])
D['cc73-74_1636-02-02']=dict(title="cc. 73r-74r, 2 Feb 1636: Francesco I d'Este to Ottavio Bolognesi. Lettera F. Same key as 1630. No decipherment in the file",
it="""*Francesco Duca di Modona &c.*

*Hieri giunsero in un medesimo tempo in questa Città due mandati da Savoia, e Parma per rappresentarci la necessità c'havevano i collegati [?per] la penuria de' viveri d'alloggiare sul nostro la Cavalleria francese, e Savoiarda, e la fanteria ch'era sul Parmegiano, e per persuaderci a contentarcene sotto pretesto di trattare amicabilmente e di pagare i viveri. Hora mentre noi pigliamo un poco di tempo a rispondere, e havere qualche campo di pensare e provedere a quello che si conveniva, ecco che questa notte, essendo tuttavia qui i sudetti mandati, la gente passa all'improvviso sul nostro [?per strada] di [?Poviglio] et occupa di primo tratto la Terra di [?Castelnovo] di Sotto, avanzandosi anche più oltre a [?sei] miglia. La temerità di quelli che hanno havuto ardire di portarci una tale ambasciata, a cui immediatamente dovea succedere questa hostilità meritava forse maggior risentimento di quello che habbiamo fatto, ma ci siamo contentati di [?farli ... brevissimamente] ad uscire dal nostro Stato sotto pena della vita. Fin hora non si penetra a che termine arrivino i disegni de' nimici, ma intendendosi che si fortifichino nella detta Terra di [?Castelnovo], che facciano venire nuova gente, et il canone, e che si sentano anche mossi nel Parmegiano dalla parte di Montecchio, s'argomenta che habbiano [?più magg.] che di godere la comodità dell'alloggio, e che particolarmente mirino a Correggio, et a rimettere il Signor Siro in Stato, havendo anche del medesimo molti altri rincontri:* noi siamo risoluti di mostrare la fronte a chi ci ha tanto offeso, e se no[n] potremo difendere la camp[a]gn[a] difenderemo [a]lmeno le piazze più principali, pronte a tutte l'oportunità che [h]averemo da f[r]ontare e mortificare i nimici. Ci rincresce per[ò] in[f]initamente che siam[o] cos[t]retti i[n] questa nece[s]ità in tempo che il no[s]tro stato è sconcertatisimo sì per le genti mandate a Milano, che ne hano fatto fuggire le migliaia per la fama de' disa[g]gi intolerabili che s[o]frivano in [?prometterci]. *Con la confidenza diamo parte al Signor Principe Borso di quanto passa. Procurate di fargli havere sicura la lettera con che vi auguriamo ogni prosperità. Di Modena li 2 febbraio 1636.*

Bisogna che [S]. M. si risolva d'applicar magiormente alle cose d'Italia, altrimente si perderano i suo stati imperiali et i principi suoi aderenti anderano a traverso.

*Francesco.*

In questo punto ci giunge aviso sicuro che sono arrivati a Bolo[g]na ducentomila scudi rimessi al legato per far levata di gente, e che vi s'aspetta fr[a] poco il cardinal Antonio Barberino. Anche di questo avviso [deleted] darete parte a S. M. et ai ministri.

*[Countersignature.]* At the foot of c. 73r: *Ottavio Bolognesi.*""",
en="""*Francesco, Duke of Modena &c.*

*Yesterday there came to this city at one and the same time two envoys from Savoy and Parma, to put to us the need the allies had, because of the shortage of provisions, to quarter on our land the French and Savoyard cavalry and the infantry that was in the Parma territory, and to persuade us to agree to it on the pretext of dealing most amicably and paying for the provisions. Now while we took a little time to answer and to have some room to think and provide for what was fitting, behold, this night, with those envoys still here, the troops pass suddenly onto our land [?by the road] of [?Poviglio] and at the first stroke occupy the town of [?Castelnovo] di Sotto, pushing on [?six] miles further. The temerity of those who dared bring us such an embassy, to be followed at once by this hostile act, perhaps deserved a sharper response than the one we made, but we were content to [?have them told very briefly] to leave our State on pain of death. So far no one can tell how far the enemy's designs reach, but hearing that they are fortifying themselves in the said town of [?Castelnovo], that they are bringing up new troops and the cannon, and that they are also reported moving in the Parma territory on the side of Montecchio, it is inferred that they have [?more in mind] than enjoying the comfort of quarters, and that they aim in particular at Correggio and at putting Signor Siro back in his State, of which we have many other indications:* we are resolved to show our front to those who have so offended us, and if we cannot defend the countryside we shall defend at least the chief strongholds, ready for every opportunity we shall have to confront and mortify the enemy. It grieves us however infinitely that we are forced into this necessity at a time when our state is in the greatest disorder, both from the troops sent to Milan, which have made thousands flee for the fame of the intolerable hardships they suffered in [unresolved word]. *In confidence we are telling Prince Borso what is happening. See that the letter reaches him safely. With this we wish you every prosperity. Modena, 2 February 1636.*

His Majesty must resolve to give more attention to the affairs of Italy; otherwise his imperial states will be lost and the princes who adhere to him will go to ruin.

*Francesco.*

At this moment sure word reaches us that two hundred thousand scudi have arrived at Bologna, sent to the legate to raise troops, and that Cardinal Antonio Barberini is expected there shortly. Of this news too you will inform His Majesty and the ministers.

*[Countersignature.]* At the foot of c. 73r: *Ottavio Bolognesi.*""",
notes=["The cipher is in three parts: one on c. 73v running into c. 74r, then after the date five rows above the signature and six below it. The last two parts are postscripts.",
"A small caret above a sign doubles its letter (ff, tt, zz, gg, pp, rr, ss, ll, vv). The 1630 letters write doubles out.",
"c. 73v row 2, no[n]: the sign after no has a long stroke with a ball. The key-free reader took it as f; sense needs n, and the V sign often has a ball. Changed by the editor.",
"c. 73v row 3, camp[a]gn[a]: the a is written with the closed D sign twice, as in c. 20v. Changed by the editor. [a]lmeno: stain over the sign.",
"c. 73v row 4, [h]averemo; row 5, f[r]ontare: blots. Restored from sense. \"Frontare\" stands without a.",
"c. 73v row 6, per[ò], in[f]initamente, siam[o], cos[t]retti: signs under blots, restored.",
"c. 73v row 7, i[n]: the signs give \"io\". Changed by the editor. nece[s]ità and no[s]tro: the signs give \"neceuita\" and \"noutro\", u for s. The plus sign and the x sign are close in this hand. Changed by the editor.",
"c. 73v row 10, s[o]frivano: the sign after s is a tick, n by the key. Changed by the editor. disa[g]gi: the sign under the caret is an open curve and not the reversed g of this hand, so g rests on sense alone.",
"c. 74r row 0, [?prometterci]: the fourth sign leans to the box: it has vertical sides, unlike the clean triangle six signs on. The earlier \"procetterci\" is withdrawn. The sense after \"in\" is still not clear, so the word stays doubtful.",
"c. 74r row 5, [S].: blot over the sign, the x shape shows. Rows 11 and 13: Bolo[g]na and fr[a], blots over one sign each. Row 14: an oval blot after avviso, taken as a deletion because the sentence runs through it.",
"S. M. is not named. \"Stati imperiali\" points to the Emperor. Where Bolognesi was in February 1636 is not stated in the letter.",
"c. 73r, questa notte: the page has \"questa\" at the line end and \"notte\" on the next line. The earlier \"[?questa passata]\" is withdrawn.",
"Clear text read from reduced images, first pass. Place names and the phrases marked [?] need a palaeographer. The countersignature on c. 74r was not read."])
def norm(s):
    s=re.sub(r'(\[.\]|.)\^',r'\1\1',s)
    s=re.sub(r'\*[^*]*\*',' ',s); s=re.sub(r'\[Clear text[^\]]*\]',' ',s).replace('[...]',' ').replace('[deleted]',' ').replace('[Countersignature.]',' ')
    s=unicodedata.normalize('NFD',s.lower()); s=re.sub(r'[^a-z]','',s); return s.replace('v','u')
# Counts. Cipher passages only: clear text in italics and the editor's "At the foot" labels are removed before counting; elided forms are split.
# A: words reading as sense, doubtful words out. B: A, also without writer's slips and changed readings (the words in SLIP). Lost or blotted signs stay, and so do
# the closed a and open c, a shape variant seen in several letters, and a single letter for a double. C: A without any word holding a restored or changed letter.
SLIP={'cc09_1630-02-15':["confiden[t]i"],'cc11r_1630-02-15':["qualco"],'cc16_1630-02-22':["[d]all'"],'cc20_1630-03-01':["circo[s]tanze","[p]rincipe"],
      'cc73-74_1636-02-02':["no[n]","i[n]","nece[s]ità","no[s]tro","s[o]frivano","disa[g]gi"]}
for d,v in D.items():
    with open(f'reading_{d}.md','w',encoding='utf8') as f:
        f.write(f"# {v['title']}\n\n{NOTE}\n\n## Italian\n\n{v['it']}\n\n## Editorial notes\n\n"+''.join(f'- {n}\n' for n in v['notes']))
    with open(f'translation_{d}.md','w',encoding='utf8') as f:
        f.write(f"# {v['title']}: English\n\nThe holes are those of the Italian reading. *Italics* mark what was written in clear.\n\n{v['en']}\n")
    s=re.sub(r'\*[^*]*\*',' ',v['it']); s=re.sub(r'\[Clear text[^\]]*\]',' ',s).replace('[deleted]',' ').replace('[Countersignature.]',' ')
    s=re.sub(r'At the foot[^:]*:',' ',s)
    w=re.findall(r"\[\?[^\]]+\]|[^\s,.;:()]+",s); w2=[]
    for x in w:
        w2+= [x] if x.startswith('[?') else [p for p in re.split(r"(?<=[a-zàèéìòù\]])'",x) if p]
    db=[x for x in w2 if x.startswith('[?')]; res=[x for x in w2 if ('[' in x or ']' in x) and not x.startswith('[?')]
    sl=[x for x in w2 if x in SLIP.get(d,[]) or x+"'" in SLIP.get(d,[])]; assert len(sl)==len(SLIP.get(d,[])),(d,sl)
    n=len(w2); a=n-len(db); b=a-len(sl); c=a-len(res)
    print(f"{d}: words {n}; A {a} ({100*a/n:.1f}%); B {b} ({100*b/n:.1f}%); C {c} ({100*c/n:.1f}%)"); print('   doubtful',db,'slips',sl,'restored',len(res),res)
    if d.startswith('cc13'): continue
    dec=''
    for l in open(f'decryption_{d}.txt',encoding='utf8'):
        if l.startswith('#'): continue
        t=l.split(':',1)[1]; dec+=re.sub(r'\{.*?\}',' ',t).replace('[deleted signs]',' ')
    a=norm(dec); b=norm(re.sub(r'At the foot[^:]*:','',v['it'])); ops=[o for o in __import__('difflib').SequenceMatcher(None,a,b,autojunk=False).get_opcodes() if o[0]!='equal']
    print('   letters',len(a),len(b),'departures',[(a[max(p-5,0):q+5],b[r:t]) for o,p,q,r,t in ops])
