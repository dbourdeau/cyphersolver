# Sforza chancery letters in cipher, ASMi Carteggio Sforzesco cart. 1597 (catalogue 1310; DECODE R5380-R5474)

Status: in progress. Triage only (6 Nov 2026); nothing read yet.

## Fetched (6 Nov 2026, via the DECODE cookie, `fetch_all.py`)
All 174 cart. 1597 records: 115 key sheets (record_type 2, R5301-R5414, R5469-R5471, nos. 1-114, 169-171) and 59 ciphertext
records (record_type 1, R5380, R5391, R5415-R5468, R5472-R5474). PDFs in `pdf/`, page renders in `png/`, contact sheets in
`sheets/` (all git-ignored: DECODE images are not ours to republish). Record pages in `rec/`.

## What the box holds
- Keys (nos. 1-114): 18th-century style copies headed with correspondent names (Angelus cum cifra Vincentii, Cosimo de
  Medici, Roberto de Malatestis a Sagramoro de Arimino 1468, Chiave di Antonio da Pistoia 1458, ...). Each is a letter
  alphabet with homophones, nulls (insignificantes), doubles (ss, ll ...) and a few word signs. Signs are geometric.
- Letters (nos. 115-168, 172-174): not one hand or one key. R5415-R5424 are whole letters in a cursive Greek-looking sign
  alphabet, no word division (R5416 and R5419 are dense full pages); R5421 and R5423 are clear text; R5425/R5426 are dense
  small-hand ciphers. R5430 (no. 130, ~15 lines) repeats one sign string four times (a name or title).
- So this is a pool of many alphabets, each needing its own key, not one cipher.

## Next steps
1. Match each letter's sign shapes to a key sheet (the key sheets seen so far, nos. 1-60 sheets k00-k02, use geometric
   signs unlike the R5415-R5419 Greek-looking letters; keys not yet viewed: sheets k03-k22).
2. Transcribe the shortest unmatched letter (R5430) and run a homophonic solver if no key fits.

## 6 Nov 2026: catalogue 1310 split into sign families (ids 2399-2408)
`split1310.py` retired #1310 and promoted ten entries by sign hand, seen on the full PDFs: A (R5425-5430), B (R5420, 5434,
5438, 5441, 5450, 5454, 5455, 5458, 5466), C (R5415, 5417, 5418, 5424), D (R5416, 5419, 5456), E (R5433, 5435, 5437, 5443-5445,
5447, 5457, 5467), F (R5459, 5460, 5463-5465), G (clear letters with cipher passages: R5422, 5436, 5440, 5442, 5446, 5451,
5452, 5461, 5472-5474), H (R5448, 5449), I (R5453, 5462), J (R5380, 5391, 5439). R5421, R5423, R5431, R5432, R5468 are clear
leaves or wrappers, not ciphers. Families are a proxy for keys: split further when a key sheet is matched.

## 6 Nov 2026 (later): families F and E, key matching attempted, no match
Viewed R5460 (cart. 153, family F) at 330 dpi. It is Italian, about 330 signs in 8 lines of continuous cipher with a few clear
words inside (a line has "cum ... Re de Franza"), then a clear postscript: "Lo figliolo de lo signor Tiberto hogi e partito de
qui, licentiato sotto pretensione de la fera che ritornera de qui a uno mese". So the language is fifteenth-century Italian and
the clear tail names Tiberto (Brandolini, d. 1455) as the context. Sign inventory by eye: #, 8, infinity, o-bar-o, phi, perp, T,
double-stroke "ff", "tt", "bb", barred q and p, slashes; some arabic numerals (12, 2, 8) are mixed in.
Compared by eye with the alphabet rows of key sheets R5329-R5344 (Ottone del Carretto, Antonio da Trezzo, Bartolomeo da Recanati,
Angelo de Amelia ...): the Angelo de Amelia keys (R5337, R5341) use tally-like bar and dot signs and a nomenclator of
"o-bar-o" groups, close in kind to F but not shape-for-shape; nothing confirmed. The remaining ~85 key sheets were not
compared in detail. A match needs a transcription of R5460 as sign tokens and a column-by-column check, not an eyeball scan.

## 6 Nov 2026 (later still): R5460 transcription attempt, stopped
Automatic route failed: thresholding plus connected components (OpenCV, `seg5460.py` in the local checkout) cannot separate the
signs, because the long slash, p and q tails run through neighbouring lines and the ligatures (ff, tt, bb, o-bar-o) touch their
neighbours; boxes merged two to five signs. Lines were cut by an ink-projection profile (rows at y = 318, 428, 549, 672, 803,
939, 1067, 1198 on the 330 dpi render; the clear postscript follows). Reading lines 1-2 by eye shows a clean enough hand, but a
usable token transcription (about 330 signs, about 30 shapes, with the tall slash either part of a sign or a word mark) is a
manual job; no tokens exist yet and no solver has been run. Do not treat R5460 as attempted-and-failed: it is not yet attempted
as a solve.

## 6 Nov 2026 (night): own sign reader + CTTS solver on R5460, first signal
`signreader.py` (this folder): deskew, track and straighten each text line, segment glyphs (connected components merged by x
overlap, neighbour-line fragments and specks dropped), cluster by shape (28x28 blurred bitmap + aspect, Ward, 45 clusters). On
R5460 it finds 374 glyphs in lines 1-8; the cluster montages are mostly coherent (8, #, ff, infinity, o-bar-o, tt, T, two
slash families, b-bar ...), with some mixing (b/d/h, 9/1/p-tail). `ctts/r5460_tokens_v1.txt` holds the tokens.
CTTS solver (ITALIAN, 5-grams, max 4 homophones, 120 s): real tokens 9.54 M (first run 9.65 M); four runs on the same tokens
shuffled in order: 9.41, 9.08, 9.05, 9.14 M. Real beats every shuffle, z about 2.7: suggestive of Italian under the clusters but
NOT proven (run-to-run spread about 0.1 M, and shuffled text also yields Italian-looking fragments such as "questa", "altrimente").
Fragments in the real decryption ("consilio", "mostra", "per", "persone") are not evidence on their own. Next: fix cluster
errors, add R5459, R5463-R5465 (same family F) for power, test with a held-out check, treat "/" as a separate token.

## 6 Nov 2026 (late): pooled clustering of family F, F2 solve, entry split
`signreader.py extract` now processes any page (pitch-aware line finder, tracked and straightened strips); `pool.py` and
`f2tokens.py` pool glyphs across pages. Results: R5464 and R5465 share clusters (about 40-60% each) and are one hand (F2, about
4,100 signs on their first leaves); R5463 has its own clusters (59-73% of several come from it); R5459 and R5460 share with each
other. Catalogue 2404 therefore keeps R5459+R5460 (F1) and gains 2409 (R5464, R5465) and 2410 (R5463).
F2 through the CTTS Italian solver (5-grams, 4 homophones, 180 s): real 3.35 M, shuffled tokens 3.53 M, i.e. no language signal.
Repeat test independent of the solver (3-, 4-, 5-gram repeats, real against shuffled, n = 20-300 clusters): real about equals
shuffled everywhere. So either the clusters are too noisy or the key spreads each letter over many homophones. The earlier
R5460 z of about 2.7 should be read as inconclusive. Not done: a held-out check (nothing to hold out while no key candidate
passes), cluster errors still unmeasured (no hand-labelled ground truth).

## 6 Nov 2026 (night): reader fixed, family A and F2 tested, no reading
**Correction.** The 'strong repeats' in family A (42 repeated 8-sign strings, none in shuffles) were an artifact: the line tracker
followed one line twice (R5425 lines 17-18, R5427 lines 2-4, R5429 lines 18-19), and on dense pages (pitch 55-70 px at 330 dpi)
the strips were taller than the line spacing, so glyphs merged across lines (median glyph height 123 px). Fixed in `signreader.py`:
strip half-height = 0.55 x pitch, each tracked line floored 0.6 pitch below the previous one, duplicate lines dropped. The earlier
F2 result (no signal) was produced by the same bug.
**After the fix** (`repeats.py`: repeated k-gram counts of the token stream, real against shuffled order):
- Family A (R5425-R5430, tiny hand, glyphs about 17 x 23 px at 330 dpi): real equals shuffled, no sequence structure; the reader fails
  on this hand (fragments in the clusters); needs a higher-dpi render and a finer segmenter before any test means anything.
- F2 (R5464, R5465, 3,788 glyphs, 60 clusters): 3-gram repeats 183 vs 60 (shuffled), 4-gram 12 vs 2; at 90 clusters 106 vs 27 and 5 vs 1.
  Real sequence structure. Hand check of 15 clusters (16 glyphs each): about 88 % pure, two mixed clusters (arc/L/q and a misc one).
- CTTS solver on F2, 240 s, real vs shuffled tokens: Italian 4 homophones 4.26 M vs 3.53 / 3.57 M; Latin 4.42 vs 3.69 M; Italian 6
  homophones 4.91 vs 4.01 M. A steady +20 % in both languages, which points to generic repetition structure, not to one language.
  Decryptions are not readable; dictionary-fragment counts are close to the shuffled ones (89 vs 56 for Italian 6).
**Status of F2:** sequence structure present, language not identified, no reading. Possible reasons: sign errors (about 12 %),
a nomenclator or syllabic key (the cart. 1597 keys have syllable tables and word signs), a language other than Italian or Latin.
Next for F2: split the mixed clusters, test a syllabic hypothesis (pairs of signs as units), compare the repeated 4-grams with the
syllable tables of the geometric keys.

## 6 Nov 2026 (night, later): F2 splits again; R5464 converges
Simulation (3,788 Italian letters, 60 signs, 0/8/15 % mis-read signs, CTTS solver 240 s): scores 13.8 / 10.5 / 8.2 M, accuracy
86 / 79 / 75 % (limited by the 4-homophone cap). The pooled F2 score (4.26 M) was far below even the 15 % case, so noise alone did not
explain it. Cluster-share cosines between leaves: R5465 P1/P2 0.94, R5464 P1/P2 0.86, R5464 vs R5465 only 0.46-0.63. So R5464 and
R5465 are different alphabets and pooling them mixed two keys. Run separately (5 homophones, 300 s, real vs shuffled tokens):
R5464 (P1+P2, 3,198 signs) 6.68 M vs 4.06 M (ratio 1.65); R5465 (P1+P2, 5,737 signs) 4.61 M vs 3.49 M (1.32).
R5464 decryption: 36 Italian dictionary words of 5+ letters against 10 in the shuffled run ("impedito", "venire", "rotto", "certa",
"senti"); variants (45 / 80 clusters, 6-grams, 6 homophones) keep finding "venire", "della", "etiam", "amici", "tornare", "havea".
The solver locked 11 single-sign letters after matching 12-letter stretches of the Italian corpus. Three runs on the same tokens
agree on 40 of 60 cluster-to-letter assignments (chance would be about 1 in 20 each): `ctts/lock64_v1.txt`. HeadlessSolve now takes a
lock file (cluster=letter) so the key can be refined the way Lasry does in the GUI. Status: R5464 partly decoded, not read.
Also note: the pencil stamps show R5464 P1 and P2 may be two separate letters (nos. 158/159 vs 165); not yet checked.

## 7 Nov 2026: reader v2 (dots kept), languages, R5464 and R5465 as separate keys
- Language test on R5464 (same signs, real vs shuffled, 5 homophones, 300 s): Italian 6.68/4.06 = 1.65, Latin 1.38, Spanish 1.36,
  French 1.32, German lowest (2.8 M raw). Italian it is.
- Reader errors seen in the outlier montages: many signs differ only by a dot (V / V with dot, circle / circle with dot, perp / perp with
  dot) and v1 threw the dots away as specks. v2 (`signreader.py extract2`, `segment_strip2`, `feat2`) attaches small components to the
  nearest sign and adds dot-position flags. R5464: 6.68 M -> 8.13 M (per sign 2,088 -> 2,572); both seeds reach the identical optimum.
  Simulation reference per sign (3,788 letters, 60 signs): clean 3,632; 8 % mis-read 2,760; 15 % 2,162, so the real reader sits near 10 %.
- k-means refinement of the Ward clusters and 45/60/80/100 clusters made no difference (2,294 / 2,452 / 2,564 / 2,570 per sign).
- Rejected: language-guided re-assignment of signs (`em_reader.py`): the same procedure on shuffled glyph order improves the letter model
  as much (-3.8 to -2.4 against -3.4 to -2.3) and erases the real text's dictionary advantage. Do not use it.
- Decryption of R5464: about 8 % of letters fall in Italian dictionary words (shuffled 1.6 %); fragments only (scrivere, tornare, amici,
  venire, della, havea, atione). Not read. What is missing is probably not sign accuracy alone: doubled-letter signs, nulls, word signs and
  abbreviations are outside the solver's model and cap the score even with perfect signs.
- R5465 (v2, 80 clusters, 5,636 signs): 5.13 M vs 3.37 M shuffled (1.52). Catalogue: 2409 now R5464 alone, 2411 = R5465.
- Tried and failed: ranking the 115 key sheets by shape against the sign clusters (no sharp winner: bars, circles and crosses occur in all of them).
Next: model doubles and nulls explicitly (extend the wrapper's reference text with doubled-letter tokens), try the same on F1 (R5460, R5459),
F3 (R5463), the geometric E family; test cribs from the standard salutation at the head of R5464 P1.

## 7 Nov 2026 (later): alphabets of family F, small groups, key-column test
Cluster-share cosines with the v2 reader (100 clusters, all F leaves): R5464 P1/P2 0.89, R5465 P1/P2 0.95, R5459/R5460 0.94, R5463 alone;
between groups 0.24-0.49 (R5465 and R5459/R5460 are the closest pair, 0.44-0.48). Four alphabets, no further pooling possible.
Small groups through the CTTS Italian solver, real vs shuffled: F1 (R5460 + R5459, 779 signs, includes by mistake the three clear lines
of R5460) 6.85 vs 6.45 M (1.06); F3 (R5463, 988 signs) 6.98 vs 6.26 M (1.12): too little text for the solver to separate from chance.
Key-column match (`keycols.py`): for the 23 key sheets whose letter header and columns could be extracted automatically, the solver's R5464
cluster-to-letter assignments fit none of them beyond chance (best z 2.9 over 23 sheets, not significant); the column extractor finds only a
fraction of each sheet's signs, so this does not exclude any key.
State at the end of this session: R5464 partly decoded (about 8 % of letters in Italian dictionary words), R5465 shows a language signal
(1.52) but no reading, nothing read. What would still move it: (1) Lasry-style manual iteration in the CTTS GUI on R5464 (transcription
fixes by eye, key locking and editing, doubles and nulls marked), (2) hand-built key-sheet columns (read the sheets by eye, 23 letters x up
to 5 signs) to test each of the 115 against the four alphabets properly, (3) the Milan inventory entry for cart. 1597 (fetch via Chrome)
to learn sender and date and so which key sheet applies.

## 7 Nov 2026 (end): shape-family check, coarse families, Chrome leads
- **Independent check of the R5464 key.** The solver never sees sign shapes, yet its letter groups are visually coherent families
  (`ctts/h64_keytable*.png`, medoid sign per cluster): all four V-clusters (V, V with dot, ...) -> e; the phi shapes -> o; the q/9 shapes -> n;
  the R shapes -> s; the left-arrow shapes -> i; x-with-loop shapes -> a; perp-with-dot and = -> r; o-bar-o and = -> t. This is how the Sforza
  keys are built (a letter's homophones are variants of one base sign), so the main letters of the key are very probably right.
- Coarse tokenisations (22 / 26 / 30 / 36 shape families, 3 homophones, 180 s): dictionary coverage of the decryption 4.9 / 6.0 / 6.9 % against
  8 % for 60 clusters: the true alphabet is not just the families. The remaining letters (c, v, d, h, p, m, g, f) are the weak part.
- **Milan inventory (VS 2/1)**: the host resets the connection from this machine (curl, WebFetch and Chrome all fail), so it is not a bot check.
- **Senatore and Tricarico, Dispacci sforzeschi da Napoli VIII/1 (2022)**, https://www.iris.unina.it/retrieve/4a7500c7-3240-42f4-922c-4a69ec731e6b/
  (Cloudflare check passes by itself after about 8 s in Chrome; the PDF viewer gives no text, pages are read from screenshots, page box accepts a number):
  inventory with regesti of the Sforza correspondence from Naples, 8 Sept 1451 - 31 Dec 1459 (ASMi, Sforzesco 195-201), says letters in cipher
  without a contemporary decipherment "sono state tutte decifrate" and has a section of Tavole with the reconstructed ciphers (Antonio da Trezzo
  and others; the 1597 box holds two late-19th-century reconstructions used for them). If R5464 and the other letters are Naples dispatches of
  those years, their contents are summarised there and the key tables are printed there. Not yet matched (the Tavole section is near the end,
  about pp. 340-363; not read).
Open: read the Tavole of that inventory and compare with the four alphabets; hand-read key sheet columns; CTTS GUI iteration on R5464.

## 7 Nov 2026 (final of session): key sheets vs R5464 families, period language model
- Shape-family test of the 97 key sheets with enough glyphs (distance from the e/a/i/o/n/r/s/t/l families of the solver key to the nearest glyph
  of each sheet): best sheets R5350, R5348, R5345 at mean distance 1.35-1.40 (median 1.65): no sheet contains these shapes. R5464's alphabet is
  probably not among the surviving key sheets (or they are redrawn too freely to match).
- Period language model (`ctts/lm_qc/italian.txt` = lang/corpora it-quattrocento-tuscan + 1.2 MB it-renaissance + 1.0 MB la-latlib-letters, replacing the
  CTTS Italian corpus on the class path: `java -cp "lm_qc;headless/classes" ...`): R5464 v2 tokens 15.44 M against 9.23 M shuffled (ratio 1.67);
  dictionary coverage of the decryption (6,000-word list from the same corpus) 10.9 % against 3.7 % shuffled. Fragments only (scrivere, tornare,
  amici, molto, rima, dio); no sentence reads. The corpus file is derived from lang/corpora (git-ignored) and is rebuilt by the two lines in this note.
Conclusion for R5464: key partly right (families check), text not readable with the signs as read (about 10 % errors) and a solver without doubles,
nulls or word signs. A full reading needs hand correction in the CTTS GUI.
- Latin-only corpus (la-latlib-letters + 5 MB la-gutenberg) on R5464 v2 tokens: 14.18 M against 9.42 M shuffled (ratio 1.51), below the period Italian corpus (1.67) and the generic Italian one: the language is Italian (with Latin words in the chancery manner), not Latin.
- Cloudflare "Verify you are human" appeared on the Naples inventory PDF (iris.unina.it) on 7 Nov; not clicked (policy). The Chrome tab is left open on it; once a person clears the box the Tavole (pp. ~340-363) can be read from screenshots (page box accepts a number).
