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
