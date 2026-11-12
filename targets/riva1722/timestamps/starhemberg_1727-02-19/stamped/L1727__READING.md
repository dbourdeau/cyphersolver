# READING. "Starhemberg" file, Campori S cc.23-24 (e7f7d383). Vienna, 19 Feb 1727. READ IN PART (strict 86.60%, below 95%).

Status: key transfer (K3, built from 1726 sibling glosses and the 1722 letters), not a ciphertext-only break. One reader, key-aware, no second reader.

## Check line (pre-publish)
- Frozen transcription before decode: tx/starh_19feb1727_passA.txt md5 cd77a13e60fb98bf096d1b1c0030b621, 2026-11-11T22:02:19Z [measured]
- Key: KEY_K3.tsv md5 65b083be69e3a4c6219c65566aee20fc, unchanged, decoded once: work/dec_K3.txt md5 9860c75d13e8292265762dda55624c72 [measured]
- Strict (work/LEDGER_K3.txt, per unit, codes = E): S 15+19+22+20+8 = 84; E 4+3+1+2+3 = 13; N 0; X 0; 84/97 = 86.60% [measured]. Parser default before the 2 reading downgrades: 85/97 = 87.63%.
- K3.2 (training, separate): identical decode and ledger, 84/97 = 86.60%; none of its additions occurs here [measured]
- Baseline, 5,000 shuffled keys, seed 1726, b70 quadgram scorer: real -4.138; shuffled mean -4.976, max -4.428; shuffles >= real 0/5000 (89 keyed units, 50 types) [measured]

## Literal decode (K3)
23r.L1: «... et s'il fait encore l'amour à la» TUTTO si n qua e fi d ta ma su a {264} p re ra {288} di o s
23r.L2: se r va r e {276} di li re n te MENT a de s so TUTTO {227=QUEL} CHE si pa s
23r.L3: se ra ne i a f fa ri pa r ti co la r MENT CON pa l m to c ca n
23r.L4: te la su a CON do t ta ta n to p re se n te {229} la fu tu ra e
23r.L5: {228} mi su re pi g li e ra {227=QUEL} {128=CORTE} «pour moi je crois, que»

## Reading (Italian; [ ] = editorial or proposed code value)
Tutto sin qua è fi[n]ta, ma Sua [264: Eccellenza?] pre[g]a [288: V.S.] di osservare [276: ?] diligentemente adesso tutto quel che si passerà nei affari, particolarmente con Palm, toccante la sua condotta tanto presente [229: quanto/che] la futura, e [228: quali/che] misure piglierà quella Corte.

## English gist
"Everything up to here is a blind. But His [Excellency] asks [you] to watch [...] closely, now, everything that happens in affairs, particularly with Palm, as to his conduct both present and future, and what measures that Court will take."

## What the letter is [derived unless tagged]
- The French clear text is domestic cover: the Count has had no letters from his household in London, asks after his children's health, and whether "Mr le Baron d'Eisenberg" still "fait l'amour à la ..." [measured, clear text read on the page]. The cipher starts exactly where the lady's name should stand, and its first words say the clear text is a feint. The clear text then resumes "pour moi je crois, que si cette personne l'aime veritablement le parti ne seroit pas si mauvais" (23v) as if a name had been given [measured].
- Emendations: L1 unit 7 was transcribed 30|80 (overwritten digit); first alternative 30 gives "fi-d-ta", second 80 gives "fi-n-ta" = finta. Counted E either way. L1 unit 15 "51" (K3 ra) gives "p-re-ra": read prega (or pregherà); E. L2 unit 9 "52" (K3 re) gives "di-li-re-n-te": read diligente, so plain 52 = ge; E.
- Training note (NOT applied): plain 52 = ge now has two contexts (b70 K3_LOG "in-GE-ni-arsi" on 20 Mar 1726 + "dili-GE-nte" here). Plain 51: K3_LOG has 51 = ra in "onorari", "apertura" (1726), here "prega" wants ga. Conflict left open.
- Codes: 288 = V.S. fits all four contexts (b57 20 Mar 1726: "da 288 domandate", "tanto 288 che l'amico", "288 si spieghi"; here "prega 288 di osservare") [derived]. 228 = QUAL(E)/CHE fits three (b70 25r.L17 "per la 228", 23v.L05 "questa Corte 228 non cerca"; here "e 228 misure") [derived]. 229 (tanto ... 229 ...) = QUANTO or CHE, one context [unverified]. 264 after "Sua" = ECCELLENZA, one context [unverified]. 276 open (also b57 21r.L06).
- Palm = Karl Joseph von Palm, the Emperor's resident in London, listed 1726-1727 [sourced: Wikipedia list of Habsburg envoys to Great Britain]. "Quella Corte" = the British Court [derived]. Historical setting from general knowledge, not checked in a source this run: Palm's memorial against the King's speech and his expulsion from London fell in March 1727, weeks after this letter [unverified].
- "S.E. mon Comte" with a household and children in London = Conrad Sigmund von Starhemberg, imperial envoy to Great Britain 1724-1727; his fifth son Georg Adam was born in London in August 1724 [sourced: Wikipedia, "Georg Adam, Prince of Starhemberg" and the envoy list]. The catalogue files the letter under GUIDO von Starhemberg. Guido as writer or principal does not fit children and a house in London [derived]. This likely applies to the 1721 and 1726 letters of the same file too ("il mio ritorno in Inghilterra ... con carattere d'Ambasciatore", 31 May 1721 clear text) [derived]. Flag for the Cyphersolver entries #425: attribution should be re-checked.
- Writer: a secretary, signs "Jean Joseph de G..." (surname runs into the gutter; not read) [measured]. Address 24v: "Monsieur Riva Secretaire faisant les affaires de S.A.S. le Duc de Modene à la Cour de la Grande Bretagne, Londres" [measured, overview].
- Baron d'Eisenberg and "son livre de manège" (23v clear): a Baron d'Eisenberg published a riding manual in London in 1727 [unverified, memory only].

## Prior art glance
- Leaves either side: 23v (clear French, end of letter, signature), 24r blank with show-through, 24v address; cc.21-22 = 20 Mar 1726 (ours). No decipherment on any leaf of this record [measured, overviews b57 img/ov].
- cs/targets/selvatico1719/NOTES.md: "five Starhemberg letters ... not worked", blocker not-attempted [sourced]. b57 SHORTLIST rank 3: "too short alone", not worked [sourced]. Lindgren 2016: named in b70/b75 logs as not obtained; still not obtained [stated].
- 1 web search (generic: Starhemberg, London 1727, Palm, Riva) returned no edition or decipherment of this letter [measured]. Italian archive editions not checked. So: no prior reading found; "never read" cannot be proved.

## Not done / weak points
- 97 units only. One reader, key-aware. No second pass. 5 code numbers open or only proposed. Clear text read at overview scale, not transcribed diplomatically.
