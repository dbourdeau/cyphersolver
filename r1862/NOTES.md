# DECODE R1862 — Venetian ambassador at Rome to the Doge, 29 April 1628 (ASVe, Busta 27 f. 354)

Catalogue entry: "Unknown sender (Roma) to unknown recipient", 4 pp., numerical, DECODE status "Non-decrypted",
no transcription on the record.

**Result: read in part (91% of the code groups).** The cipher is broken and the key rebuilt; the letter is read
continuously on all four pages except four lines, and 98.8% of its code groups have a value. What is left are
thirteen word codes and the four lines that turn on them.

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

## Remaining gaps

- 15 code-group tokens (1.2%): 6478 x2, 5386 x2, 5349, 5389, 5370, 51708, 683, 5378, 5379, 6279, 5189, 699, 6241 - blocker: open-codes; all in the word/name band, which R1874's decipherment does not cover, and no other letter in this cipher is on DECODE. Their alphabetical brackets are known: 5370 is a "par-" word, 5182 an f/g/h word, 6279 an m/n word, 6443 a t/u/v/z word.
- four lines that are image-true but give no sense: P1 L17, P2 L17, P2 L22, P2 L26 (about 55 groups) - blocker: open-codes; each was re-read digit by digit by three independent passes, and they turn on those codes or on the clerk's own slips (he writes "sivoia" for Savoia, "germinia", "dovore", "avortiti")
- the ambassador's name - blocker: open-codes; not in the letter, and CSP Venice vol. 21 calendars no Rome despatch of 29 Apr 1628

## Escalation

- [x] siblings: R1874 (Busta 30) gave the key; its second enciphered copy gave more alignment data. A sweep of the whole DECODE record list for ASVe material found no other letter in this cipher (only 16th-century Busta 6-30 letters, the Busta 4 key registers and the Codice Amadi).
- [x] clear-pages: this record has none; R1874's images 8955-8959 are its decipherment and were transcribed here
- [x] known-keys: the Codice Amadi (ASVe Inquisitori di Stato reg. 1269, 14 key records on DECODE) and the Busta 4 key registers (Reg. 8, 16, 18) were opened - all 16th-century or earlier, graphic-sign and letter-plus-number systems, none of this type
- [x] print: CSP Venice vol. 21 (23-30 Apr 1628), Tomokiyo's Venetian pages, Bonavoglia's "Decifra dispacci veneziani": nothing for this despatch
- [x] key-rebuild: soft-EM alignment against R1874's decipherment with a synthetic control; then the grid filled by structure, the word codes read from context, and three inherited values corrected (628, 6439, 6481) using the alphabetical order of the word band
- [x] retry: eleven image passes in all; one manuscript line on page 3 was found untranscribed and added (P3 L26b, "la prego non nominarme"), two page-2 rows had been blended from two physical lines and one row was a phantom

What would move the remaining gaps: another letter in this cipher (ASVe Busta 27 holds more of the series; none is
digitised on DECODE), or the Venetian chancery's own key for it, which is not among the ASVe key records on DECODE.
