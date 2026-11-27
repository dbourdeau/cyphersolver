# Track B result: VOC cipher of 1623 and 1634 (26 Nov 2026 AEST)

## Bottom line
- The 1634 glosses give a homophonic letter key: 47 numbers valued [measured: frozen/K1634_key.tsv].
- That frozen key decodes the 1623 letter into plain Dutch: same cipher system across 1623-1634.
- Strict first-pass score 32/54 tokens = 59.3%: BELOW the 65% bar. Shuffles 0/5,000 at both seeds.
- The 1623 content was already deciphered in 1623-24 (margins of inv. 1079) and Coolhaas (GM I, 1960) says so. NOT FIRST to read it.
- No PR package prepared: the figure of record misses the bar, and the reading exists. Nothing sent or filed.

## Freezes
- 1634 key and transcription: frozen/FREEZE_1634.txt, Wed 25 Nov 2026 18:04:38 UTC; md5 T1634 136ccc03..., K1634 fe501cd1...
- 1623 transcription, second transcription, scorer, method: frozen/FREEZE_1623.txt, 18:07:33 UTC; md5 T1623 5a9e290e..., score.py e04f5aeb..., METHOD 48944c40...
- Decode run once after that (run_1623_output.txt, decode_1623_firstpass.tsv).
- Disclosed before the freeze (METHOD_1623_test.md): block C was effectively decoded in my head from LEAD.md before freezing; the 1079 margins were glimpsed on overview images.

## Figures (full arithmetic) [measured]
- 1634: 14 glossed passages, 35 cipher words, 217 groups; 47 distinct numbers valued from the glosses.
- 1623: 54 tokens (A 26, B 23, C 5) and 276 groups. Groups whose number is in the 1634 key: 254. Coverage 254/276 = 92.0%.
- Numbers in 1623 not in the key (13): 1, 19, 24, 27, 37, 40, 53, 54, 57, 60, 61, 62, 63.
- Scorer (stated in advance): token counts as sense only if fully keyed and its normalised decode is in a 37,386-type word list
  (types with frequency >= 2 in 1,438,516 HTR tokens of VOC inv. 1068, 1120, 1132, 1151, 1156).
- First pass, figure of record: 32/54 = 59.26%. By block: A 18/26, B 9/23, C 5/5 (18 + 9 + 5 = 32).
  Of the 22 failures, 20 hold an unkeyed number and 2 are fully decoded words absent from the list (sacxen, moschaten).
- Shuffles (values permuted over the same 47 numbers): seed 20261112: 0/5,000 >= 32 (max 11, mean 6.37); seed 7: 0/5,000 (max 11, mean 6.39).
- Second transcription (1079_0263, block B) against frozen block B: 127/127 groups aligned = 100%. NOT blind in the strict sense:
  same transcriber, who had already read block B in two other copies. A truly blind transcription by another reader is still owed.
- Post hoc (not the figure of record): 13 values set from 1623 context (SECOND_PASS_values.tsv) plus 4 = k (EMENDATIONS.md):
  coverage 276/276; corpus score 52/54 = 96.3% (fails: 'kolden', 'moschaten'). With emendation 2 (kolden -> konden), human reading 54/54.
- Independent check after decoding: the margins of 1079_0129 and 1079_0133 match the decode word for word (A 26 words, B 23 words),
  except the last word of A, where the margin's 'conden' supports emendation 2.

## Reading (normalised spelling; cipher in [ ], clear words of the letter outside)
- 1623 A (1080_0376 / 1079_0129): [Vier dagen naer het vertreck van d'Engelse schepen] sijn van meeninge [t'jacht de Hase met ample
  advysen na Nederlant te senden, off d'andre noch soo haest niet volgen konden].
- 1623 B (1080_0380 / 1079_0133 / 1079_0263): [In 't Wapen en Leyden sijn geladen acht en twintich duysent sacken peper, acht hondert
  sockels folie, twee hondert tachtich duysent ponden noten moschaten].
- 1623 C (resolution 2 Oct 1623, 1080_0486): omme de [vlote vant lant] ter gedestineerde plaetsen ontrent [Manilla] te verstercken;
  tot versterckinge vande voors. [vlote]. ('vant lant' read letter by letter; sense not settled.)
- 1634 (1108_1154-55): a [dat is naer den enbocadero van Spirito Sancto opt silver van Aquapulco]; b [Japan, t'jacht Venlo];
  c [Engelse damasten]; d [turckse camelotten]; e [Japan]; f [rassetten, perpetuanen, heresaien]; g [damasten, camelotten];
  h [geel laecken]; i [halve stucken]; k [swarte]; l [swarte laeckenen]; m, n [Japan]; o [tail].

## English
- A: "Four days after the English ships leave, [we] intend to send the yacht de Hase to the Netherlands with full advices, in case the others could not follow so soon."
- B: "In the Wapen and the Leyden are loaded twenty-eight thousand sacks of pepper, eight hundred sockels (mat bales) of mace, two hundred and eighty thousand pounds of nutmegs."
- C: "to strengthen the fleet [of the land?] at the destined places around Manila"; "for strengthening the said fleet".
- 1634 a: "that is, to the entrance (embocadero) of Espiritu Santo, for the silver of Acapulco" (the Manila galleon route).

## The system [derived]
- Homophonic letter cipher, numbers 1 to about 72, 2 to 4 numbers per common letter (a: 9, 10, 18; e: 28, 70, 71; n: 2, 48, 50;
  t: 22, 32, 56, 58; h: 8, 27, 37; f: 1, 19, 62; w: 24, 54, 60 ...). i/j share signs; u/v/w share 31 and 44. Words split by '/'.
  No code words (whole-word signs) seen in the 89 cipher words of both letters (35 + 54 = 89).

## Step 4 (ciphertext-only attack)
- Not run. Its trigger was "coverage too low to read"; coverage is 92.0% and the residual 13 numbers are fixed by context and the margins.

## Verdict
- 1623: decoded with the 1634-derived key, first pass 59.3% < 65%: does NOT meet our read bar on the figure of record, despite 0/5,000 shuffles.
  Content NOT FIRST (contemporary marginal decipherment, noted by Coolhaas 1960). New: key recovery and the 1623-1634 identity of the system.
- 1634: read from existing decipherment (glosses); key rebuilt. Not printed as far as checked.
- 1696: not worked (lower priority).
