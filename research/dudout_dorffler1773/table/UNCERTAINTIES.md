# UNCERTAINTIES — dorffler-1686 (proposal only; nothing here is validated)

## Position of the gloss (main cause of the earlier EM failures)
- On 470 R, 475 L/R, 467 R, 468 L/R the gloss of a cipher line sits ABOVE that line (in the interline over it), and it
  runs on continuously through clear-text insertions. T-train's "gloss below" pairing is shifted by one line.
  Consequence: 211.77.53 = "von dem" in both places (no contradiction; "tiam ad-" belongs to the next line).
- Several lines T-train marks X (clear) are in fact the gloss of the first cipher line (475_R1 line 1, 467_R1 line 1).

## System (as proposed)
- Not "one group per syllable with nulls": mostly single letters + CV/VC syllables + a few words/names (>=250?).
  28 and 54 are both "n" (not nulls); 33/59 = s; 34/60 = t; 16/42 = c (ch is written c+h: 16.22, 42.22, 16.48);
  22/48 = h; 25/26/51 = l; 32/58 = r; 180/188/100 = "lich"; 19/45/46/20 = f; 14/40 = a; 18/10/44 = e; 23/49 = i/j.
- Double dots over a group (seen on 121, 80, 95, 99, 109, 125, 140, 110?) = umlaut of the syllable (rä, dü, hü, kö,
  mö, rü, wü). Single dots after a group look like ordinary separators/punctuation. Dots were NOT recorded
  systematically in ALIGN.tsv (no ":" marks): to be redone on the originals.

## Readings I could not settle (digit confusions 1/7, 0/8, 3/8, 6/8, 21/26, 87/67, 127/122/137, 131/231)
- ALIGN.tsv groups are my reading of the crops, in places corrected by sense (e.g. 67 for T-train 87 in "benachbarte",
  231 for 131 in "ein recit", 127 for 137 in "dieses", 38 for 30 in "seyn", 108 for 100 in "administriren",
  209 for 129 in "vermessen", 98 for 90 in "Jablonowski"). Each such correction is a hypothesis, not an observation.
- 88: gi (Regierung) but also seen where "n"/"s" is expected (470_R1 l5; 475_R3 l2) -> probably 2-3 different numbers.
- 100/180/188 = lich: three homophones or misreadings of one another; 100 vs 108 (mi) confusable.
- 19 = f (affection, frembden, suffisant, greiffen) but "zu 19.127.28" is glossed "Posen" (470_R1 l2): unresolved.
- 64: y (frey, seyn) vs first group of "Bidzinsky" (64 or 68 = bi?).
- 21 = g, but "andermahl" ends 106.22.21 (21 or 26 = l?). 20 = f (Schrifft x2) but "übel" = 35.67.20 (20/26/25?).
- 22 = h is firm (Thron, sehr, mehr, dehnen, dehrer); 77.22.112.54 "denen" is spelled "dehnen".
- 78 = di (Subsidio, mediation) vs "gefunden" 87.85.78 (78 = "den"? or 85.28.157 as on 467_R1 l4).
- 131 = ta (Stadt, Littauer, Estat, instantiam) but 475_L1 l5 "21.33.131.44.27.188.34.65.165.94.." under
  "von seinem Sitz erhoben" does not decode with the table: line left out of ALIGN.tsv.
- 145 = zu, but 470_L1 l1 "patria(m)" is followed by 145 where the gloss has no "zu" (40.145 = "am"?).
- 197 = noch (x3) but 197.25.43.132.58 under "(ge)melter"; 176 = wah(r)? / aber?; 149 = auch (x2) vs 145 "zu-sammen".
- 209 = ver (x10) also stands in "Chur-fürsten" 209.10.28 (475_R1 l6): ver/für homophone or code "Fürst"; 305 = Fürst?
- 212 = vor (vorzusehen, vorschein, bevorab) but "verstattet", "vorgelesen?" -> vor/ver not separated.
- 223 = wi (wider, wie); gloss "unterdrücket" at 475_R2 l6 reads from the cipher as "wi-der-ra-t-he-n" (widerrathen).
- Number/name codes with one occurrence: 237, 246, 248 (dreissig tausend), 333 (Rhein-), 75 (Cur[land]/cu), 342
  (Ungar), 301/303 (Franckreich/Frantzösi-), 346 (Wien), 255 (Armee), 284 (Cron), 261, 294, 332, 331, 316, 305.
- Unattached / unreadable gloss: 470_R1 l1 (its gloss is above the crop); 475_L2 l2 ("Succamerarius...?");
  475_L3 l4; 467_R3 l1; 468_L1 l5-7; 468_L2 l1-2; 468_R1 l1-2, l6; 468_R2 l7-9; 468_R3 l1-2; 468_R4 l1-2.
  Words marked "?" in ALIGN.tsv are guesses from the cipher, not readings of the gloss.

## Strength of evidence
- In-sample only, and partly circular (gloss readings and group readings were adjusted jointly with the table).
  Character accuracy of decoded vs gloss words: 0.94 (470/475, 373 words), 0.95 (467/468, 250 words);
  with the table restricted to groups already aligned on 470/475: 0.91 on 467/468; 200 shuffled keys: max 0.085.
  This shows the alignment is not chance; it does NOT validate the table: only the held-out image can.
