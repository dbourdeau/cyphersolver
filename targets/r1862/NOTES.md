# DECODE R1862 — Venetian ambassador at Rome to the Doge, 29 April 1628 (ASVe, Busta 27 f. 354)

Catalogue entry: "Unknown sender (Roma) to unknown recipient", 4 pp., numerical, DECODE status "Non-decrypted",
no transcription on the record.

**Result: read in part (cipher-word count, 16 Nov 2026: 497 of 545 cipher words, 91.2%; read before).** The cipher is broken and the key rebuilt from a sibling's contemporary decipherment; 99.1% of
the 1,280 code groups have a value, and the letter reads continuously on all four pages except one line. Measured
share reading as sense: **0.95** line by line against a period Italian model with neighbour context (`measure.py`),
0.92 by a stricter 25-character window (`measure_tok.py`), 0.96 by a hand audit token by token. Twelve tokens of
the word band and one line (P2 L22) stay open.

## What the record is

Four images (`IMG_R1862_I8905_P1`–`I8908_P4`, DECODE login only, not public domain, kept git-ignored in `img/`).
The address is "Ser.mo Principe" (the Doge), so this is an ambassador's despatch. Cipher and clear text alternate:
page 1 and page 2 are cipher (with a clear opening line and a clear paragraph at the foot of page 2), page 3 is
clear to line 11 and cipher to line 27, page 4 opens clear, then cipher, then clear, then cipher.

The sender is the Venetian ambassador at Rome — he reports an audience with Cardinal Barberini and writes to the
Doge and Senate. His name is not established here (see Remaining gaps).

## The cipher and how it was read

The cipher is the one used in DECODE **R1874** (Alvise Mocenigo, Madrid, 26 Oct 1628, ASVe Busta 30 f. 174), a
record that carries its own contemporary decipherment. The key was rebuilt from that pair:

1. R1874's decipherment (images 8955–8959, margin paragraphs 5–16, ~4,800 letters) was transcribed here as known
   plaintext: `../r1874/tx/decipherment.txt`.
2. DECODE's transcription of R1874's cipher was split into five stretches matching those paragraphs (~1.84
   letters per group) and aligned to the plaintext by soft-EM forward–backward (`../r1874/em.py`, `run2.py`).
   The solver was first checked on a synthetic syllabic cipher of the same size, which it recovered exactly
   (`../r1874/synth_em.py`, 97/97 groups).
3. DECODE writes the 5 in two forms; in R1862's clearer hand they are 51 and 53, and keeping them apart is what
   made the grid regular. The first EM run, which allowed a group to stand for nothing, collapsed; capping values
   at 1–4 letters and forbidding nulls fixed it.

The key is a **syllabary grid**: the prefix gives the vowel (6 = a, 51 = e, 62 = i, 53 = o, 64 = u), the last two
digits the consonant (07 b, 08 c, 09 l, 10 d, 11 f, 13 g, 14 gn, 17 gr, 19 l, 20 m, 21 n, 22 p, 23 pr, 24 qu,
26 ss, 27 r, 28 s, 31 st, 33 t, 34 tr, 37 v, 38 z) — 6210 di, 5133 te, 5333 to, 6433 tu. Single letters: 680 a,
6280 e, 6480 i, 5190 o, 6490 u, 692 n, 6292 r, 6482 l, 5390 s. Word codes read from context here: 670 che,
672 con, 6270 in, 6249 il, 5102 del, 5302 nel, 5124/5387 quel, 5384 qual(che), 5374 per, 5142 duca, 6440 sua,
6442 suo, 6240 ave, 5373 part, 6477 poc, 6287 non, 6479 tio, 5347 papa, 6247 Cesare, 673 cose, 6274 molto,
5140 dov, 5174 far, 6439 signor, 5323 pro, 5117 gre, 5208 co. 698/5198/5199/699 stand at the edges of the
ciphered passages and appear to be paragraph marks (R1874 uses 6499 the same way).

**The word band is alphabetical.** Within each prefix row the codes above column 39 run in alphabetical blocks —
row 53: papa 47, part 73, per 74, piu 77, qual 84, quel 87, ques 88; row 64: signor 39, sua 40, suo 42. That
brackets every code still open and is how several were read (6274 "molto" after "in"; 5140 "dov" just below
"duca"). Three values inherited from R1874's EM alignment were wrong and were corrected from this letter:
628 = sa (not "n": "non sarian giamai", "fatto sapere"), 6439 = signor (not "mini": "Sua Signoria Illustrissima",
"il Signor Cardinal Barberino"), 6481 = i.

Working files: `key_over.json` (this letter's key, on top of `../r1874/key2.json`), `tx/groups.txt` (the
transcription, one manuscript line per row), `decode.py` (decipher), `plain.py` → `tx/plain.txt`, `measure.py`
(read fraction), `ctx.py`, `fixline.py`.

The transcription was made from the images here (the record has none) and then checked line by line against the
images with the key in hand. Two systematic traps on this hand: a final n-shape is 2, not 1; and 7 is a ">" with
a long open tail, while 8 is a hook plus a closed loop. Two rows of page 2 had been blended from two physical
lines, and one row was a phantom; those were found by tracking the baselines and re-splitting.

## What the letter says

The ambassador had "opportunissima occasione ... hieri col Cardinal Barberino di parlargli di quel negotio che
lei mi si è commesso con cotesto Eccelso Conseglio, et di cavar anche qualche intimo particolare desiderato da
lei". The Cardinal had twice asked him **whether Palma (Palmanova) was well fortified and what garrison it had,
and whether the pass of the Pontebba was well secured**. Hearing from other quarters that "Imperiali uniti con
Spagna parlavano con molto sprezzo" of the Republic, he asked in turn, "con intiera confidenza", whether those
questions had been put "a qualche fine", and begged that anything of the kind be communicated to him, so that
the Serenissima might learn of it in time "perché da lei fossero trovati i rimedii oportuni" — but without
naming those who dealt in such matters.

Page 2 reports what he learned of "pensieri vasti" and of the Imperialists united with Spain, of arms and men
"che si trovavano in piedi nella Germania", and how guardedly he spoke ("oculati et avvertiti"); he "non potei di
meno di non ..." (the rest of that block is not yet read). The clear paragraph at the foot of page 2 and on page
3 gives the Cardinal's own argument: the Emperor "ha pur troppo che fare in casa propria", must watch the King
of Denmark, Bethlen Gabor, the Dutch and perhaps the Turk; Wallenstein ("il Volestein") would not come to Italy
without his whole army, and quartering it would cost "gran summa d'oro, di che l'Imperatore n'ha gran carestia".

The ciphered part of page 3 reports the Cardinal's remarks on the **imperial aulic council** — "nel qual, se ben
la maggior parte de' consiglieri sia aderente al Re di Spagna" — and that he shows himself "più tosto amorevole
che difidente".

Page 4 (clear) lays the attempt on **Genoa** at the Duke of Savoy's door and argues that Spaniards and
Imperialists, ill satisfied, will trust him less; then in cipher the ambassador "ringratiai il cardinale" for so
confidential a communication and, on the Duke of Savoy's last move, "presi occasione di caricar la mano a fin
che il **Papa** deliberasse mandar la sua persona legato ... per acomodar gli interessi di Mantova e di Savoia
insieme", urging "la facilità che già si averia trovata nel Duca di Savoia di ridursi", and the glory for His
Holiness of "questa opportunità di dar pace al ..." Finally: "il ministro cardinal Barbarino have dato il
sudetto aviso ... di Genova".

This is the opening of the War of the Mantuan Succession (April 1628), with Francesco Barberini directing papal
foreign policy and Venice backing Nevers, so the content sits exactly where it should.

## Two cuts in the Palma passage filled (30 Sept 2026, for the Lasry quotation)

P1 L06-L09 read "perche due volte nelle capele [5349] e avendomi ricercato con bi instanza se Palma sara ben
fortificata". Both points re-checked on the image (IMG_R1862_I8905_P1, lines 7-8): the digits are 5349 and 6202 as
transcribed.

- **5349 = papali (I).** The word band is alphabetical within row 53: 5347 papa, 5373 part, 5374 per, 5377 piu.
  5349 sits right after papa: "nelle capele papali", the papal chapels (cappelle papali) where the ambassadors met
  the Cardinal. It may be the stem "papal" with the next group 6280 "e" as its ending ("papale", the clerk's
  agreement slip); the sense is the same. The old bracket "a par- word" in Remaining gaps is superseded.
- **6202 "bi" = slip for 6222 "pi" (I).** 6202 is bi (P2 L14 du-bi-ta-n-do), which gives no word before
  "instanza". The clerk's slips are all one digit (see below); 6222 = pi gives "con pi[ù] instanza", "with more
  insistence", after "due volte". Alternative one-digit slip: 6242, an unknown word code between 6240 ave and 6247
  Cesare (a b-/ca- word, e.g. "calda"); not excluded. Neither is written into key_over.json, so plain.txt and the
  measured fractions are unchanged.

Quotation for the Lasry list (30 Sept 2026): "… col Cardinal Barberino di parlargli di quel negotio che lei mi si è
commesso con cotesto Eccelso Conseglio, et di cavar anche qualche intimo particolare desiderato da lei, perché due
volte nelle capele [papali] e avendomi ricercato con [più] instanza se Palma sarà ben fortificata, quanto presidio
aveva, se il passo della Pontebba si era ben assicurato …"

## Read share over cipher words only (16 Nov 2026)

README Conventions (16 Nov 2026): the read share counts the words written in cipher only. `tx/R1862_reading.md` puts
the passages written in clear between ⟨ ⟩ (the opening, the foot of p. 2 and top of p. 3, three passages on p. 4) and
leaves the cipher unmarked; the clear passages were removed and the rest of the `## Reading` section counted.

- R1862: 0.953 -> **0.912** (497 of 545 cipher words). Unread, 48: the twelve word-band codes with no value (ten
  standing alone, two inside words: vo[51708]lari, [5370]i); eighteen `[?word]` readings; four words with a letter the
  cipher does not have (co[n], [a]lcun, cardina[le], [g]loria: the clerk left it out, so the letter is supplied); the
  eight words carrying the clerk's one-digit code slips (below, "The clerk's own slips": esprimersi, confidenza,
  altrove, cosi, Mantova, considerati, piu, preparati), which the Conventions' one-digit-slip rule does not cover
  because the key is rebuilt here, not the surviving period key; and the line P2 L22, 14 groups, sized at about 6 words from the letter's 2.4 groups per word (1,283 groups, about 545
  words). The size of P2 L22 is an estimate: counted as one bare mark the share is 0.920 (497/540). Sp[agnuo]li (twice),
  Sp[agna] and Spa[gna] expand the clerk's own abbreviation *sp* in the cipher and count as read; the final ellipsis
  is where the despatch's cipher ends (P4 L31), not a gap. The 0.953 was measured over the whole reading with the
  clear passages.
- Class: read -> **read in part**. The group figure (99.1% of 1,280 groups valued) and the line measure (0.95) are
  unchanged. Remaining gaps already covered the codes and P2 L22 and gains a line for the rest. The eighteen doubtful readings are
  decoded letters whose word division or reading is unsure, and the four supplied letters and eight slipped groups are
  written so on the image; there is no other copy of this despatch to check them against (Escalation, siblings).

## Remaining gaps

- 12 code-group tokens (0.9%) of the word/name band: 6443 x2, 6279 x2, 6478 x2, 5349, 5370, 51708, 5378, 5379, 6241 - blocker: no-key-material; R1874's decipherment does not cover that band, no other letter in this cipher survives on DECODE, and the ASVe key registers that do (Codice Amadi reg. 1269, Busta 4 regs. 8/16/18) are a century older. Alphabetical brackets: 5370 is a "par-" word, 5349 "papal(i)" (I, 30 Sept 2026); 5378/5379 fall between "piu" and "qual"; 6279 between "molto" and "non"; 6443 after "suo"; 6478 between "poc" and "tio".
- one line, P2 L22 (14 groups), image-true after four independent readings - blocker: no-key-material; every group in it is a structural grid value, so the fault is a clerk's slip or a word outside the corpus; exhaustive single- and double-substitution searches over the key's own value set returned nothing.
- words counted unread in the cipher-word share (16 Nov 2026): eighteen [?word] readings, four letters the clerk left out (co[n], [a]lcun, cardina[le], [g]loria) and eight words with his one-digit code slips - blocker: no-key-material; written so on the image; the slips are read through with a key rebuilt here, which the one-digit-slip rule does not cover; settling them needs the chancery's own key or another copy of the despatch, neither of which survives
- the ambassador's name - blocker: no-key-material; he does not name himself, and CSP Venice vol. 21 calendars no Rome despatch of 29 Apr 1628.

## The clerk's own slips

He miscodes as well as misspells, always by one digit, and the slips are recorded in `key_over.json` `_slips` and
read through (the transcription keeps what he wrote): 6220 for 6223 in "esprimersi", 632 for 672 in "confidenza",
5337 for 5137 in "altrove", 5388 for 5308 in "cosi", 68 for 637 in "Mantova", 537 for 627 in "considerati",
6480 for 6490 in "piu", 6222 for 622 in "preparati". His spelling slips are left as written and read through the
same way: sivoia, germinia, voro, avortiti, dovore, partcolar, soto, efetuar, conunicarla.

## Escalation

- [x] siblings: R1874 (Busta 30) gave the key; its second enciphered copy gave more alignment data. A sweep of the entire DECODE record list for ASVe material found no other letter in this cipher.
- [x] clear-pages: this record has none; R1874's images 8955-8959 are its decipherment and were transcribed here
- [x] known-keys: the Codice Amadi (ASVe Inquisitori di Stato reg. 1269, 14 key records) and the Busta 4 key registers (Reg. 8, 16, 18) were opened - all 16th-century or earlier and of other types
- [x] print: CSP Venice vol. 21 (23-30 Apr 1628), Tomokiyo's Venetian pages, Bonavoglia's "Decifra dispacci veneziani": nothing for this despatch
- [x] key-rebuild: soft-EM alignment against R1874's decipherment with a synthetic control; the grid filled by structure; the word codes read from context and bracketed by the alphabetical order of the word band; values inherited from the sibling corrected where this letter disproved them (628 sa, 6439 signor, 6481 i, 634 tra, 5132 stre, 6443 back to open)
- [x] retry: sixteen image passes in all. One manuscript line on page 3 was found untranscribed and added (P3 L26b, "la prego non nominarme"); two page-2 rows had been blended from two physical lines and one row was a phantom; page 4 had two spurious groups.

What would move the rest: another letter in this cipher (ASVe Busta 27 holds more of the series; none is digitised
on DECODE), or the Venetian chancery's own key for it, which is not among the ASVe key records on DECODE.
