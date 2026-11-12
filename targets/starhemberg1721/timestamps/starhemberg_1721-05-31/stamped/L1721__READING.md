# READING. "Starhemberg" file, Campori S cc.17-18 (ab7fcc2d). Vienna, 31 May 1721. READ IN PART (strict 89.42% all; 86.11% on the part the old gloss does not cover). NOT A FIRST for the first half.

Status: a different, simpler system from the Riva-Vienna table (K3 does not apply). A contemporary hand deciphered the first half at the foot of c.17r and stopped mid-word. Key K21 is taken from that gloss only. The second half (36 units) is not covered by the gloss and is read here with that key. Key from a gloss = key transfer, not a ciphertext-only break. b4's ciphertext-only attack on this letter failed and did not notice the gloss.

## Check line (pre-publish)
- Frozen transcription before any decode: tx/starh_31may1721_passA.txt md5 bdf499dcf4ac94fcf85276c999d4620a, 2026-11-11T22:05:54Z [measured]. Not blind (b4 reading and gloss seen). Number sequence identical to b4's frozen transcription (104 groups, compared by eye and in the failed diff output kept in LOG) [measured].
- K3 unchanged, decoded once (control): gibberish; real -6.049 vs shuffled mean -6.471, max -5.433; 597/5000 shuffles >= real (seed 1726). K3 does NOT read this letter [measured]. K3.2 not run: same table plus codes, none relevant.
- K21 (work/KEY_K21.tsv md5 0bbf709160237928df5c7390547d7183; 22 letter signs + 210 = Duca; every value from the glossed half): first decode work/dec_K21_first.txt md5 faccd87d784ebe58d327a84d5132064e.
- Strict per unit (work/LEDGER_K21.txt; codes, units with the '' mark, and 5 reading downgrades = E; none upgraded): S 6+14+20+16+10+12+10+5 = 93; E 1+1+1+1+3+2+1+1 = 11; N 0; 93/104 = 89.42% [measured]. Before the downgrades: 98/104 = 94.23%.
- Held-out (17r.L5 unit 9 to the end, where the gloss gives nothing): S 31, E 5, 31/36 = 86.11% [measured].
- Baseline, 5,000 shuffled keys, seed 1726, b70 quadgram scorer: real -4.334; shuffled mean -6.506, max -5.221; 0/5000 >= real (101 keyed units, 22 types) [measured]. Note: the key was fitted to the gloss on 68 of these units, so this baseline is not independent for that part.

## Literal decode (K21)
17r.L1: «nel resto» s u o s e r e
17r.L2: {210=DUCA} f a «bene» d i c o n t i n u a r e «la sua»
17r.L3: d i u o t i o n c u e r s o l a u g u s t
17r.L4: c a s a d a u s t r i a «tanto più che» g l i e s"
17r.L5: e m p i «mostrano, che» e u e l" i {89} «sono» s t a
17r.L6: t i f e d e l i «à quella hanno» a c e t i s
17r.L7: t a t i «grandissimi» u a n t a g" i «al mio arri-»
17r.L8: «vo le potrò dir di più sopra» {80} p u n t o «fra tanto sono»

## Reading (Italian; clear text in plain, cipher in CAPS; [ ] editorial)
... il mio ritorno in Inghilterra è certissimo, e per dirlo fra di noi, con carattere d'Ambasciatore. Nel resto SUO SER[enissim]o DUCA FA bene DI CONTINUARE la sua DIVOTION[e] VERSO L'AUGUST[a] CASA D'AUSTRIA, tanto più che GLI ESSEMPI mostrano che [QU]ELLI [89: CHE] sono STATI FEDELI à quella hanno AC[QU]ISTATI grandissimi VANTAGGI. Al mio arrivo le potrò dir di più sopra [80: QUESTO] PUNTO. Fra tanto sono di V.S. ...

## English gist
"For the rest, your Most Serene Duke does well to continue his devotion to the august House of Austria, the more so as examples show that those who have been faithful to it have gained very great advantages. On my arrival I shall be able to tell you more on this point."

## Notes [derived unless tagged]
- New here (not in the gloss): "...quelli che sono stati fedeli à quella hanno acquistati grandissimi vantaggi ... sopra questo punto". The gloss ends "mostrano che [struck] è vel:" [measured]. It gives "e v e l" for 20 50 2 16, the same values as K21, and breaks off, which fits a decipherer puzzled by a slip of the writer.
- The two E spots in the new half: 20 (= e in "verso", "essempi") stands where q/qu is wanted in "quelli" (20 50 2 16'' 3) and "acquistati" (10 12 20 23 3 22 23 10 23 30, where 23 = t also stands for u). Read by sense. Possible cause: the writer used 20 for q as well, or slipped. Not resolved.
- '' after a group = doubled consonant (essempi, quelli, vantaggi): 3 of 3 fit [derived].
- 89 = CHE and 80 = QUESTO: one context each [unverified]. 210 = DUCA from the gloss [measured].
- System: 1-5 vowels a e i o u; 10 a, 20 e, 30 i, 40 o, 50 u/v (second vowel set); 12 c, 13 d, 14 f, 15 g, 16 l, 17 m, 18 n, 19 p, 21 r, 22 s, 23 t, 24 t/z. Close in build to WAINUT's Selvatico 1719 table (vowels 1-5, consonants from 6 up) but with different consonant numbers [derived; 1719 table as quoted in cs NOTES, sourced].
- Writer: signs "le Comte de Starhemberg" [measured]; "il mio ritorno in Inghilterra ... con carattere d'Ambasciatore" [measured] fits Conrad Sigmund von Starhemberg, imperial envoy to Great Britain (listed 1724-1727) [sourced: Wikipedia envoy list], not Guido, under whom the catalogue files it [derived].
- "Suo Ser.mo Duca" = the Duke of Modena, Rinaldo d'Este, Riva's master [derived].

## Prior art glance
- Same leaf: the foot gloss (first half). 17v, 18r blank or show-through, 18v address "Monsieur Riva Secretaire faisant les affaires de S.A.S. le Duc de Modene a la Cour de la Grande Bretagne, Londres" [measured, overviews]. cs NOTES: Starhemberg letters "not worked" [sourced]. b4: SA attacks failed, "not read" [sourced]. No web search specific to this letter this run. Lindgren 2016 not obtained [stated].

## Not done / weak points
- 104 units; one reader; not blind. Codes 80, 89 unproven. The q problem is unresolved. The first half is the old decipherer's reading, not ours.
