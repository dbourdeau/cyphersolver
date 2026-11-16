# Judge notes: Corsi 1513 cipher passages, one strict pass

Source: /tmp/judge_c/decode_once.txt only. One pass, no second tries. Per-row segmentation and counts in judge.tsv
(non-S words carry {E} or {N}). Counting script checked that each segmented row concatenates back to the source row
exactly. Units: one per decoded letter, one per bracket code, one per `_` (always N).

## Totals

Letter A (A0001329 + A0001330, 20 rows)
- S = 43+44+40+8+29+22+25+11+50+57+20+37+56+3+13+45+18+35+36+41 = 633
- E = 11+16+26+0+0+0+0+0+0+10+0+0+13+34+0+0+2+0+28+0 = 140
- N = 15+7+2+0+13+5+0+4+4+2+8+2+1+1+7+1+0+0+1+1 = 74
- Strict share S/(S+E+N) = 633/(633+140+74) = 633/847 = 74.7%. S+E = 773/847 = 91.3%.

Letter B (A0001341, 16 rows)
- S = 9+23+8+22+36+31+9+8+51+31+17+10+34+35+32+14 = 370
- E = 5+17+0+10+2+0+3+6+3+28+10+0+12+12+24+4 = 136
- N = 0+13+4+18+15+17+16+8+11+10+16+0+18+10+4+2 = 162
- Strict share = 370/(370+136+162) = 370/668 = 55.4%. S+E = 506/668 = 75.7%.

## Judging rules applied
- Letters of a word broken by a hole (tutt_, pi_, e_pressamente, _na = una, _sati = usati, ma_ime) scored S; the hole
  itself N.
- Bracket codes scored S (the given word fits). [27: re di Scotia?] and [24: Inghilterra?] are S on context but carry
  the decode's own question mark.
- Words running across a line break (co|ntenteza, be|ne, hi|vessimo, tem|po, nobi|li, molestass|i) scored as one word.
- E for: one substitution/insertion/deletion (hiveva, vestra, fussine, dao = Dio, fattlil = fatto il, essl, l = la),
  and for the systematic c-for-e of letter B (chc, cra, mc, ct, c), each counted as one slip per word.

## Doubts (marked, not resolved)
- A 12 `cche` (Florentine doubling?) E; `feputa` N.
- A 13 `popha reputatilne` read as "pocha reputatione", one slip per word, E.
- A 15-16 `clghmiachno`, `g`, `sassi` N: no sense ("se sua maiesta lo [la]sassi"? not scored).
- A 19, 22 `coioborato`, `coiono` (rr written i, twice): E, but the repetition suggests a sign value problem, not a slip.
- A 23 `corroborarationeche`: E only because the extra "ra" is one syllable sign; by letters it is two.
- A 23b `hamiimo` N. A 26 `a` before confederatu N. A0001330 `c` before "il" N.
- B `dunhtare` twice = "dubitare" with nh for bi: N both times (two letters), but consistent, so likely a key error.
- B 5 `rppcntino`, 6 `bendhc` (benche?), 6 `omcon`, 20 `gmodinalvo` N. B 20 `esare` (Tuscan "essare"?) E with doubt.
- B 8 is mostly holes and N; B 21 `qu talia ct` taken as "...Italia et", `talia` E.

## Gists (only what the S/E text supports)

Letter A (27 Oct 1513)
1. The king's side did not call our ambassador to this communication; Corsi thinks it was handled with the nuncio and
   that Florence is held in low repute there. Almazán, in this first meeting, said "expressly" that it is written from
   there that the Florentine state is not well purged nor strengthened.
2. Corsi calls that a very great falsehood: the citizens, above all the nobles, run the same fortune as the Medici, and
   the city has outward supports; he made them grasp that these were all fables.
3. He hopes the Italian states confederate with His Majesty will hold firm, and that "ours" (the Pope?) showed pleasure
   in it. Not read: lines 11, 15-17 in part.

Letter B (16 Nov 1513)
1. News from Rome: the Medici state is reported not firm or well constituted (one word unread); His Majesty says he
   does not want to prolong [the truce] with France, yet must in any case prorogue it.
2. Having heard of the death of the King of Scots [code 27, doubtful], England [code 24, doubtful] is moved to leave
   him (the French?) to be master there, to get the war off his back; a blow is to be feared.
3. Corsi had time to reply that if the truce held, His Majesty and France together would be very dangerous unless
   [unread] did not molest the affairs of Italy; it is necessary to think hard on this for the common good of all.
   Lines 5-8 and 14 are largely unread.
