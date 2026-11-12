# READING. Giorgio Olivazzi to Giuseppe Riva, Milan 17 Apr 1725. Campori O cc.1-2 (849b6bb7). DECODED, READ IN PART ONLY (strict 68.88%).

Status: the Riva-Vienna table (K3) reads this letter too. Key transfer, not a ciphertext-only break. One reader, key-aware, a hard cursive hand read at half scale: treat as a first pass, not a finished reading.

## Check line (pre-publish)
- Frozen transcription before any decoder run: tx/olivazzi_17apr1725_passA.txt md5 b7dac6993ca6eaedfdaacac2eb719164, 2026-11-11T22:11:46Z [measured]
- K3 unchanged (md5 65b083be69e3a4c6219c65566aee20fc), decoded once: work/dec_K3.txt md5 c1240a411ec6f0c091aa6106885f933f [measured]
- Units: 2r 179, 2v 197, all 376 [measured, ledger sums].
- Strict with 43 reading downgrades, none upgraded (work/LEDGER_K3.txt, work/overrides.tsv): 2r 134/179 = 74.86%; 2v 125/197 = 63.45%; ALL S 259 + E 112 + N 5 = 376, 68.88% [measured]. Per-line sums are in the ledger file.
- Parser default, no downgrades (keyed and cleanly transcribed, not "right"): 2r 152/179 = 84.92%; 2v 150/197 = 76.14%; ALL 302/376 = 80.32% [measured]. Check: 302 - 43 = 259.
- K3.2 (training, separate): identical decode (diff empty) and ledger, 259/376 = 68.88%; none of its additions occurs [measured].
- Baseline, 5,000 shuffled keys, seed 1726, b70 quadgram scorer: real -3.977; shuffled mean -4.749, max -4.314; 0/5000 >= real (318 keyed units, 71 types) [measured].

## Literal decode: work/dec_K3.txt (36 lines)

## Reading (clear text in plain and only roughly read; cipher in CAPS; [..] = code or unread)
2r: ... DI [259] E DI ME?, e secondo l'ordine della carità comincio da chi dovrebbe per altre ragioni esser l'ultimo. ... buoni uomini, cioè I RE[G]ENTI E [359], han tirato dal loro partito [..] [292] E TUTT' UNITI han sempre pensato A FARMI CONTRASTO, e perché chi si regola con giustizia non si obbliga se non i galantuomini, e questi SON PO[CHI = 5_], e per contrario quelli che non lo sono, CHE SON MOLTI, COSÌ HO [179] [CHI] possono far male, e non vi È [..] [178] soggetto per bene, massimamente PERCHÉ [con fa-lo-ni-e-ri?] NON È STATO ASSISTITO CHE DA [341] CHE HA buon cuore per me MA NON PO[T]EVA FAR certe figure. Dopo aver provate tutte le strade possibili in un anno e mezzo, ora LA [181] NOSTRA MI HA FATTO raccomandare, e saprò in breve con qual frutto. IL CONTRASTO CHE MI SI FA NON ha per oggetto quelle mercedi delle quali si tratta. Questo è LA SCUSA. IL VERO disegno è di rendermi IN MAL CONCETTO PERCHÉ [..] NON POSSA PRETENDERE avanzamento NÉ [178] autorità, E PRESO IL [300] PER FARMELO CONTRARIO [352] E [354] si sono serviti dell'inquisizione CHE [..] È STATO IL RELATORE [..] [259] IL [142] [143], ed non ci è voluto di più PER FARMI [177] mille e poi mille TORTI ogni giorno, che MI SONO [0_] PENOSI [..] degna cagione.
2v: Vengo A [259] [261], e distinguo tre interessi. PER [121] SI È TORNATA [130] esibire AL [219] sotto certe CON[DIZ]IONI CHE NON SONO ... IL MALE È [360] LO SECONDA parte per suo fratello CON IL [219] E PA.. PER SOSTENERSI UNITO [..] [300]. Non ho altra speranza se non che Dio assista la ragione ... Se codesto [233] [236] SCRIVESSE, forse gioverebbe. L'altro è del [170] [196] E DE[L] [300], E COSÌ [..] ... [TE]MENDO DI DOVERLO lasciare PER TOGLIER[LO] AL [142] ... HA SINO PROPOSTO sotto mano DI MANDARE UNA [..] ... e qualche amico mi scrive CHE VI POSSA RESTAR.. [341] ... né mi parlano più DI CHI DEBBA VENIRE. ... [226] [309] FANNO IL DIAVOLO [die]TRO DEL [142]. Gran caso pare che sia ... riconciliato, cui si voglia far servire LE VENDETTE transversali: mal esempio. ... [334] ... BESTIA ... [341] sempre onorato, attento, e conosciuto. FREDDO [339] ... OPERA IN ciò che può.

## English gist [derived]
Olivazzi tells Riva that the "good men" of Milan, the Regents and [359], have drawn others to their side and, all united, have always worked to oppose him. Honest men are few, the others many. He has been backed only by [341], who is well disposed but could not act openly. After a year and a half of trying every road, "our [181]" has now had him recommended. The opposition is not about the favours in question: that is the excuse. The real aim is to give him a bad name so that he cannot claim advancement or authority. To turn [300] against him they used the inquisition (enquiry), and he has suffered a thousand wrongs. On 2v he sets out three interests: a post offered again to [219] on conditions; someone backing his brother with [219] to stay in with [300]; a wish that "that [233 236]" would write; fear of having to give something up; and others who "raise the devil" behind the [142]'s back and pursue "indirect vendettas".

## Identifications
- Writer signs "Giorgio Olivazzi" on 2v [measured]; addressee "Sig. Giuseppe Car.mo" [measured]; b4 PRIOR_ART names Riva as recipient [sourced]. Clear text of 1r speaks of Riva's journey (Frankfurt, Holland) [measured, overview scale].
- "I Regenti" fits the Regents of the Supreme Council (Milan/Italy business) [unverified, general knowledge]. No code number identified with confidence. 142 = PADRONE and 261 = SERENISSIMO are K3.1 values from Selvatico; whether they hold in Olivazzi's use is not tested [unverified]. 5_ = CHI (K3_LOG candidate) fits "son po-CHI" and "di CHI debba venire": 2 more contexts [derived]. 300 is the main actor (6 occurrences) [measured].
- Plain 52 = ge again ("reGEnti"), third context with 1726 and 1727 [derived].

## Finding
- The table is not a Starhemberg or Selvatico private key: a third writer, in Milan, uses it with Riva in 1725. So it is Riva's own (Modenese) cipher shared with his correspondents [derived].

## Prior art glance
- No gloss on 1r, 1v, 2r, 2v [measured, overviews]. b48 TRIAGE: "~55 number groups, too short" (the count was wrong: 376 units) [sourced/measured]. b4 PRIOR_ART: "no decipherment noted; no repo target" [sourced]. No web search for this letter in this run. Lindgren 2016 not obtained.

## Not done / weak points
- 43 units downgraded as unread, 5 lost in the gutter, 69 doubtful or codes. Underlines in this hand are hard to place; 1 vs 7 vs 2 are near-identical strokes. A second pass at full scale, line by line, is needed before any claim. Clear text not transcribed properly. Codes unresolved: 259, 359, 292, 179, 178, 341, 181, 300, 352, 354, 143, 177, 121, 130, 219, 360, 233, 236, 170, 196, 131, 164, 160, 309, 208, 334, 339.
