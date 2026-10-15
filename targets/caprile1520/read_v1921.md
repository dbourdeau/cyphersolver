# V1921: Caprile to Alfonso I d'Este, Esztergom, 25 Feb 1521 (ASMo Ungheria b. 4, Caprili 1520-21 no. 12)

Not on DECODE. Vestigia 1921 (`vestigia/v1921.json`, "olasz, titkosírás"); image `img/v/v1921_2.jpg` (p. 1; p. 2,
`v1921_1.jpg`, is the address leaf, no cipher). Six cipher runs set inside clear sentences in the last third of the
letter. Reading 2 Oct 2026 with the 1520-21 key (`key21.json`, `key21_counts.json`); corrected transcription in
`v1921_signs.txt`, per-sign values and the measurements in `read_v1921.py`.

**Result: 161 of 166 cipher signs (97.0 %) read as sense; 147 (88.6 %) at grade C.** The 5 unread signs are listed
under gaps. Language check: it-cinquecento −1.79 per character on the reading against −4.12 for the same letters
shuffled with word breaks kept (20 runs); `lm.best_language` puts it-modern first (−2.11), then Latin (−2.57).

Grades: C = every sign at its key value (or a value fixed below); M = one or two signs off the key majority or a
doubtful word; [..] unread signs; [x] supplied.

## The reading in context

Clear text in roman, the deciphered runs in **bold**.

> … il tutto per adviso e scarico di chi ne ha colpa. **E me dicixe [= disse?] ha un omo qui** qual oltra che fa
> mille pacie & da poca riputation ale cose del patron, **dice ogni cosa e revelta [?]**, e ha ditto haver scritto
> al suo mazo che **il custode è stato quel ch'à persuaso [..]** a dire che **[.] Agria era data d'anti il suo
> advento, e[t] che lo toglia in oficio**, e molto sturbato le sue cose, e chi l'ha messo in gran disgratia di
> **suo signore**; il che quando cossi sia, como mi acerta alcuno ch'à veduto le lettere, a V. Ex.a sera poca
> fatica i cominciar a repeter il suo **sopra soi beni, quantunque siano in reg[no?]**. E S. V. Ex.a a questo modo …

| run | signs | reading | grade |
|---|---|---|---|
| L01 | 19 | e me dicixe [disse?] · ha un omo qui | M (dicixe) / C |
| L02 | 20 | dice ogni cosa · e revelta | C / M |
| L02-03 | 31 | il custode è stato quel ch'à persuaso [2 signs] | C |
| L03-04 | 51 | [1 sign] Agria era data d'anti il suo advento, e[t] che lo toglia in oficio | C; K = et M |
| L05 | 10 | suo signore | C |
| L06 | 35 | sopra soi beni, quantunque siano in reg[2 signs] | C (x p = q) |

Translation (gist): "And he told me there is a man here who, besides committing a thousand follies and bringing
little credit to the master's affairs, tells everything and [gives it away]; and he has said he wrote to his
[messenger] that it was the custode [of Eger] who persuaded [him/them] to say that Eger had been given away before his
[the new bishop's] arrival, and that he should take him into office — and has much disturbed his affairs, and put him
in great disgrace with his lord. If that is so, as someone who has seen the letters assures me, it will be little
trouble for Your Excellency to begin reclaiming what is his from his goods, even though they are in the kingdom."
The "patron" and the estate claim are Ippolito d'Este's Eger bishopric, the subject of R1136, R1138 and R1139.

## Key findings (values fixed here)

- **Lone o is not a null.** It is a homophone for h (L01 "ha", L02 "ch'à", L04 "che") and for u (L01 "qui", L03 "suo",
  L06 "quantunque"). The EM counts already said so (o: o 28, h 13, u 10); V1920 confirms ("PHI o y" = che).
- **oo (two lone o together) = b**: "beni" (L06); also R1139 L06 "de[b]ito" (r y o o L h).
- **z+ = q** (z with a cross, not z + t): "qui" (L01), "quantunque" (L06); V1920 "quaranta" has the same z+ LAM.
- **x+ = q**: "quel" (L03). **x followed by the looped p is also q** (xp ligature): "quantunque" (L06), and
  R1136 L10 "x ρ a ss m+ f o/o" = questo. Plain x stays r (21×); its 7 "q" counts in the EM are probably x+ written as x t.
- **EL = f** in "oficio" (L04), as AMP = f in R1139's "Alfonso": the p-signs double for f.
- **K = et** (M) in "e[t] che" (L04); K is t 4× in the counts.
- The m+ ligature can be written with the cross as a looped descender (L02 "m p" = MT, "è sta|to").
- Z = x in "dicixe" (L01), as in V1920's "8 Z q" = Ex.a.

## Remaining gaps (V1921)

- L03 "1 1" after "persuaso", before the clear "a dire": two minim strokes; neither is in the key (no-key-material).
  Perhaps "li" (persuaded them), not claimed.
- L03 QB before "Agria": one sign unexplained (QB is o/t), probably a slip or null (left open).
- L06 last two signs "K PHI" at the torn page edge, after "in reg": uncertain shapes, "regno" expected but not
  enciphered so (illegible).
- Grade-M words: "dicixe" (= disse? a Venetian "dixe" with an extra syllable) and "revelta" (revela?).
