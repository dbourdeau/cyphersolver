# Gordon's numeral note to the Mudir of Dongola, 1884 (Durham SAD.250/1/550)

Status: closed from the evidence, 14 Nov 2026 (not read; open leads are physical sources)

A single leaf from the siege of Khartoum: an Arabic note from General Gordon to Mustafa Pasha, Mudir of Dongola,
made of two-digit Arabic-Indic numeral groups with a few words and two closing lines in clear Arabic. Nothing is
read. This folder holds the transcription, the statistics and the first test of the Durham key table. Catalogue
entry 2939.

## The document

- **Shelfmark.** Durham University Library, Archives and Special Collections, Sudan Archive, Wingate Papers,
  SAD.250/1/550, with the covering letter SAD.250/1/549 (Elwin Palmer to Grenfell, 15 Nov 1886).
- **Images.** Free on Durham's IIIF server, no login. Manifest
  `https://iiif.durham.ac.uk/manifests/trifle/32150/t2/mq/j7/t2mqj72p714z/manifest` (leaves 549, 549v, 550); leaf 550 is
  2107 x 3264 px. The server returns at most 1024 px a side per request, so the leaf was read in tiles and row strips.
  Images are not kept in the repository.
- **What Palmer says (leaf 549).** The scrap "containing figures signed by Gordon" was found among papers from Dongola;
  Gordon "evidently had a code"; a Dongola employee, Khalil Ibrahim, "has the key". The finding aid says only "a note
  written in code by Gordon".
- **What is on the leaf.** A clear Arabic address line at the top (to His Excellency Mustafa Pasha, Mudir of Dongola);
  about 15 rows of six to eight groups; clear Arabic words between groups in five rows ("as previously written"
  among them); two closing lines of clear Arabic with a few groups in them; a date at the foot whose year digits are
  not clearly legible (1300-1302; day read as 16) and Gordon's signature. Some groups are struck under a bar and
  corrected above it; a few are in a lighter brown ink.

## Prior work

Nothing found. DECODE, Tomokiyo and Lasry have nothing on Gordon or Khartoum. Hake's edition of the Khartoum journals
(Appendix U) prints Gordon's plain-Arabic notes to the Mudir of 8 Aug and 28 Sep 1884 and says the Mahdi seized a
cipher to the Mudir dated 22 Sep 1884 without printing it; this leaf is probably not that item (it was found at Dongola).
See `research/sweep_2026-11-14_africa_north_east_literature/` and `research/vetting_2026-11-14_*`.

## Transcription (`transcription.txt`)

119 groups, 26 distinct values, read from the images on 14 Nov 2026 (`docs/_check_profile.py --measure`). Reading
order is right to left, as for the Arabic; each group is two numerals written left to right.

Glyph classes in this hand: tall stroke 1; hook 2; two-prong 3; epsilon-shaped 4; ring 5; six-shape 6; V 7; caret 8;
9-shape 9. Zero does not occur. **Uncertain pairs:** the two-prong and epsilon glyphs (3 and 4) and the hook and
six-shape (2 and 6) are the easiest to confuse; every reading is a best reading, not a checked one. A second reader
should check the groups before anyone relies on single values.

Corrected groups (struck value, then what stands above the bar), entered in `transcription.txt` as the final value:
92 to 62 in rows 1, 3, 6 and 8 (once more bare 92 stands in row 5 and bare 62 in rows 5 and 7); 99 to 64 to 54 in the
cell between rows 3 and 4 (entered as row 4's fifth group, leaving row 3 with seven groups). Lighter-ink groups: 35 in
row 1 (first digit uncertain, 35 or 45), 69 in row 4, 38 in row 10, 39 in row 12.

## What the statistics show

`python analysis.py` prints them.

- 119 groups over 26 distinct values; coincidence index 0.065 against 0.036 for 28 equally likely symbols, so the
  values repeat the way letters of a text do, not like unique codes.
- The values are structured: the first digit is 1, 2, 3, 5, 6, 7 or 8 in 116 of 119 groups (3 alone in 44), the second
  digit 2, 4, 5, 7, 8 or 9 in 116 of 119; 20 of the 26 distinct values (113 of the 119 groups) lie inside the 7 x 6 grid
  those digits make (42 cells). That points to a table with row and column labels, not 100 arbitrary codes; the six
  values outside the grid (36, 47, 49, 63, 86, 92, each read once or twice) are the likeliest transcription errors.
- Most frequent: 38 (20), 27 (12), 82 (10), 34 (8), 74 (7), 14 (7), 39 (7), 62 (6), 57 (5), 84 (5).
- The same short runs return across rows (for example 27 74 27, 14 39 82), which a codebook for words would also show.

## The test of the Durham key table (SAD.250/1/81)

Leaf 81 (also in the Wingate Papers, `https://n2t.durham.ac.uk/ark:/32150/t1m6969z078q.html`) is a pencil table:
Latin letters against two-digit numbers in several columns headed with officers' names (Wolseley, Kitchener, Nubar,
Hunter among them) and, on the right, two Arabic-alphabet columns, each a column of letters followed by a column of
two-digit numbers (N1 beside the rightmost letters, N2 at the left edge). Both were read at 1.5x from native-resolution
crops on 14 Nov 2026 into `table_key.tsv`: 27 of the 28 letters (sin not read), each reading marked H, M or L
(most are L for N1: the numbers are small, in grey pencil, with small letters written under some cells and several
numbers that look alike under the 3/4 and 2/6 glyph confusions). `python analysis.py` runs everything below.

- **N2 does not read the note.** In all four variants (as read, digits reversed, each with and without 3=4 and 2=6)
  random reassignment of the same letters scores as well or better in 65 to 88 percent of 4000 draws. The most
  frequent group, 38 (17 percent of the note), is dhal in N2, and alif is 56, which never occurs (nor 65). N2 does
  share part of the note's digit pattern (78 percent of its values lie in the grid the note keeps to, against 52
  percent by chance and 95 percent for the note), so it may be a keying of the same family, not the same key.
- **N1 does not read it either, with one marginal hint.** As read, 41 percent of the note's groups map and only 2.5
  percent of random reassignments of the same letters score as well (38 maps to shin, kaf or lam, 74 to mim or ha, 35
  to alif); that is one of eight variants (about 0.2 after correcting for them), disappears when 3=4 and 2=6 are
  allowed (18 percent), and rests on low-confidence readings. The note's next most frequent values, 27, 82 and 34,
  are not in N1 at all, and N1's own digit pattern (44 percent inside the grid) looks like chance.
- **The Latin-letter columns were not tested** against the Arabic note (wrong script); an earlier look at the third
  column (26 numbers) found 5 values in common and a different second-digit spread.
- **Verdict.** The table, as read, does not decipher the note. It does show the family: pairs of digits from 1-9 for
  letters, one keying per correspondent. The note is probably another keying (Gordon's own, or the one Khalil Ibrahim
  held) that the table does not record.

## The crib attack (14 Nov 2026)

`crib_attack.py` and `crib_drag.py`; plaintext model: a letter trigram trained on the first 85 percent of the
`ar-wikipedia-sample` corpus (modern prose, held-out 15 percent used for controls). All results are from the
transcription as it stands (119 groups; the uncertain 3/4 and 2/6 readings are not corrected for).

- **Frequency profile.** Sorted by frequency the note's 26 values track Arabic letters closely (top four 16.8, 10.1,
  8.4, 6.7 percent against alif, lam, ya, mim 17.6, 11.1, 8.9, 6.8; correlation 0.995). That proves little: any skewed
  profile correlates that well. "38 27" (alif-lam if 38 and 27 are those letters) occurs twice, as often as independence
  predicts.
- **Key-free structure test.** Against 3000 shuffles of the note the repeated bigrams (31 against 22) and repeated trigrams
  (7 against 1.7) are 3.2 and 4.0 standard deviations high, so the order of the groups is not random: it repeats like
  language or a code. Against 3000 real 119-letter Arabic slices the note is ordinary on repeats (z about -1) but has
  no dominant bigram (its commonest occurs 4 times, real Arabic about 9, z -2.2) and uses more distinct symbols (26
  against 22, z +2.2; transcription errors would add symbols).
- **Substitution attack with controls** (annealing, 10 restarts x 20,000 steps, 20 controls each). Best score -311 for the
  note, against -334 to -317 for shuffled notes and -308 to -253 for held-out Arabic slices enciphered with random keys:
  better than every shuffle, worse than every real control. The best decode is not Arabic (a few short words that the
  corpus favours, such as مصر, appear by chance). Splicing the clear words in as known plaintext does not improve it.
- **Repeats inside the note** (possible repeated words): 27 59 38 34 (rows 9 and 15), 75 27 74 39 (rows 9/10 and 14/15),
  27 74 39 (three times), 74 27 38 (twice), and 38 75 34 (end of row 10 and start of the closing groups, followed by 14
  and by 49 respectively: a stem with different endings).
- **Crib dragging** on the four closing groups 38 75 34 49, which follow the clear words "did not give them":
  each of the 156 commonest four-letter Arabic words (four distinct letters, frequency 20 or more) was forced onto
  them and the rest optimised, against 156 random four-letter strings through the same procedure. Real cribs average
  -354.1, random -354.9; 12 of 156 real cribs beat the random 95th percentile where about 8 are expected, and the best
  (اصبح, يوسف, ابرز) leave the rest of the decode unreadable. No crib stands out.

**Reading of the results.** The note's order has real structure, so it is not noise, but it does not behave like a
letter-for-letter substitution of running Arabic prose: no dominant article bigram, an inflated symbol count, and an
attack that cannot get above the middle of the null-to-real range. Together with the clear words (men, a payment "to
each") the likelier reading is a code or a mixed system in which the groups carry names, titles, ranks or sums, with
repeated units (27 59 38 34, 27 74 39, 38 75 34) as the repeated words. A letter-substitution attack needs a longer text
or a trusted crib; neither exists here.

## Step 2: other Arabic-numeral material (14 Nov 2026)

Aim: find the repeated units (27 59 38 34, 27 74 39, 38 75 34) in other numeral text of the same milieu, or the earlier
letter the note cites. `survey_durham.py` reproduces the survey.

- **Digitised Durham units scanned leaf by leaf (278 leaves):** SAD.250/1/1-58 (Oct 1884), 59-96 (Nov-Dec 1884, with
  the table at 81), 97-133 (Jan-Feb 1885) and 528-606 (1886-87, with the note). The only leaf of numeral groups is
  SAD.250/1/550 itself. The rest are English letters and orders, maps, returns, Arabic letters (SAD.250/1/31, 39, 102,
  104-106: plain Arabic, among them Gordon's of 21 Oct 1884 to Muhammad Khashm al-Mus), and the table 81/81v.
  Other leaves with figures (125, 133) are supply returns and a memo.
- **Not digitised, so not reachable from here:** TNA PRO 30/57/4/75-109 (Kitchener's telegrams in Arabic script, and
  4/77-78 "please use Arabic cipher", 24-25 Aug 1884; Kew), Durham SAD.101/15/1-25 (the pouch of fragments "with
  handwritten Arabic words and numerals" found on the Khalifa, 1899), the Hicks Pasha registers (SAD.866, SAD.600), the
  Arab Bureau files with coded Arabic messages of 1916 (SAD.138/10, SAD.141/3; Durham reading room).
- **Digitised but not scanned:** the Khalifa's papers SAD.101/12 (letters, lists and returns of 1898-99; numerals in
  lists, not expected to be a cipher) and the later Wingate series (1894 on), too late to hold the earlier letter.
- **The earlier letter the note cites** ("as previously written") was not found: nothing in 250/1 from Oct-Nov 1884 is a
  Gordon numeral text, and the four "Arabic cipher letters" Gordon sent by Kitchener's messenger in Nov 1884
  (Hansard 14 Nov 1884) are not in the digitised units.
- **Result.** No second numeral text online to compare with; the repeated units could not be tested against a
  codebook. The leads left are physical: Kew (PRO 30/57/4) and the Durham reading room.

## Remaining gaps

- No key: Khalil Ibrahim's key is not known to survive, and the table does not list a column that reads the note.
  Blocker: no-key-material.
- A human Arabic reader for `clear_words.md` (the clear lines were read by the model, the last words of both closing
  lines and the signature block not at all) and a second reader for the groups. Blocker: not-attempted.
- The table readings are low-confidence (N1 mostly L, sin missing). A colour or raking-light image of SAD.250/1/81 would
  settle the grey pencil. Blocker: illegible.
- The year digits at the foot of the leaf (1300-1302). Blocker: illegible.

## Escalation

Done (14 Nov 2026): images read at native size; DECODE, Tomokiyo, Lasry and Hake searched; transcription, statistics,
both Arabic columns of the table read and tested against Arabic letter frequencies (corpus
`ar-wikipedia-sample` in `lang/sources.json`); the clear Arabic read (`clear_words.md`).

Next, in order:

1. (Done online, negative.) Look for the earlier letter and for the repeated units in the digitised Durham units.
   Left: TNA PRO 30/57/4/75-109 at Kew (Kitchener's Arabic-script telegrams, "please use Arabic cipher"), Durham
   SAD.101/15 (the Khalifa's pouch of Arabic words and numerals) and SAD.866/SAD.600 (Hicks Pasha registers), which
   need a visit or an order for images; a shared codebook would show the same units there.
2. Find the four "Arabic cipher letters" of Nov 1884 and any decode of Gordon's: ask Durham and TNA.
3. Have a human Arabic reader check `clear_words.md` and the groups; correct the 3/4 and 2/6 readings and rerun
   `python crib_attack.py` (about 2 minutes).
4. Ask Durham whether the Sudan Archive holds Khalil Ibrahim's key or a decode (reading room), and for a better image
   of SAD.250/1/81.
