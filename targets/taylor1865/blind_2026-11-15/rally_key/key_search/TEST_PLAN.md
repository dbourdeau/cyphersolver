# Test plan: key search on the second telegram of 11 April 1865 (T11), vol. 11 frame 0046

Written 15 November 2026 before any of the computations below were run. Each step is run once; the log of each run
is kept in `results/`. A miss is reported as a miss.

## Data
- T11 cipher text, reader B1 and reader B2 separately, preferred readings (first form of each `[X/Y]`), from
  `output/taylor1865_open_2026-11-15/transcriptions/readerB{1,2}_transcription.tsv` (frozen there,
  `test/FROZEN.sha256`). Both 107 letters, 25 groups. "Agreed text" = B1 where they agree, the doubtful letters listed
  in the notes; scored as the two readers' texts, never merged into a third text that nobody read.
- Calibration telegrams (key known): T03 (109 letters, COMPLETE VICTORY), T05 (87), T06 (79), T08 (78), T09 (57),
  S1 (180), S2 (61) (COME RETRIBUTION), from the same transcription files, same readers' pairs.
- English model: mean log10 quadgram probability, model from the Official Records Ser. I vol. 49 pt. 2 OCR (as in
  the earlier test), floor log10(0.01/N).

## A pencil observation made before this plan (on the image, by me, an AI reader)
Faint pencil numerals "15" stand above T11 at cipher letters 30, 60 (or 59), 75, 90 (or 89; read "13" by the
readers) and 105 (counting cipher letters only, B1's text, 1-based): every fifteenth letter. In T10 (read with COME
RETRIBUTION at phase 0) a "15" stands over the 15th cipher letter. So someone in pencil counted a 15-letter key from
the first cipher letter of T11 across the clear words. This is treated as a hypothesis (period 15, phase 0,
continuous over cipher letters only), not assumed: step (a) tests period independently, and steps (b)-(c) try all
phases anyway.

## (a) Key length
- Index of coincidence of each reader's text; average column index of coincidence for periods 1-20; Kasiski:
  repeated sequences of length >= 3 and their distances, with factors.
- Calibration: the same on each calibration telegram; report the rank of the true period 15 among periods 1-20.
- Control: 200 shuffles of T11 (own letters); report how often a shuffle's best period is 15 and how often the
  period-15 column IC is as high as T11's. Reported, no pass mark (descriptive). What 107 letters can and cannot show
  is stated in the notes.

## (b) Known keys used another way
Keys: COMPLETEVICTORY, COMERETRIBUTION, MANCHESTERBLUFF, THENAVYOURPRIDE.
Options, each combination: rule in {Vigenere p=c-k, Beaufort p=k-c, variant Beaufort p=c+k}; key forwards or
reversed; start offset 0-14; key continuous over cipher letters, or restarted at offset s at each cipher word
(each group), or restarted at each run of cipher between clear words (5 runs: before "as the", before "on that",
before "If you can", before "Can have four or five", to the end); tableau slip: shift d in {0, +1, -1} added to every
letter (clerk using the row above or below). Key applied also over clear words (key advanced over the letters of
the clear words "as the", "on that", "If you can", "Can have four or five" counted in sequence) as one more
alignment option.
Score: best quadgram mean over all options. Controls: 400 shuffles of the reader's own letters, each maximised over
the same full option set. Pass: real best > max of 400 controls, for both readers, with the same key and option.

## (c) Key list
Literature keys (sources in notes): MANCHESTERBLUFF, COMPLETEVICTORY, COMERETRIBUTION (Kahn, The Codebreakers;
Official Records; Gaddy), BALTIMORE (Boklan, Cryptologia 2006: a fourth Confederate key), THENAVYOURPRIDE and
OURNAVYOURPRIDE (the merged target, 9 Jan 1865), plus any key phrase named in the Taylor transcriptions or merged
notes (searched for "key", "cipher", "change"). Each key at its own length, all offsets, Vigenere/Beaufort/variant,
forwards/reversed, tableau shift 0/+-1, continuous over cipher letters. Same controls (400 shuffles maximised over
the same options and the same key list); same pass mark.

## (d) Crib dragging
Cribs (upper case, letters only): MOBILE, MAURY, SELMA, MONTGOMERY, MERIDIAN, DEMOPOLIS, FORREST, WILSON, CAVALRY,
RAILROAD, COTTON, STORES, EVACUATE, ENEMY, GENERAL, BYORDER, IMMEDIATELY, TROOPS, ARTILLERY, INFANTRY, TRAINS,
STEAMBOATS, BOATS, TRANSPORTATION, REGIMENTS, BRIGADES, WAGONS, CARS, ENGINES, POSITION, MOVEMENT, COLUMBUS,
CLAIBORNE, GUNS, AMMUNITION, PROVISIONS, SUPPLIES.
For each crib, reader and position i (crib inside the text), Vigenere key fragment k = c - p at key positions
(i..i+L-1) mod 15 (phase-0 hypothesis; the unknown key absorbs any phase). A fragment is "English" if its quadgram
mean (fragments >= 5 letters) is above the 99th percentile of fragments from all cribs at all positions on 200
shuffled texts. Consistency: two kept fragments are compatible if they agree on every shared key position and do
not overlap in the text; a set is consistent if pairwise compatible; report the largest number of key positions
covered by a consistent set of >= 2 fragments from different cribs, and the implied partial key. Control: the same
on 200 shuffled texts; pass: real coverage > max of controls, both readers.

## (f) Unknown 15-letter key by hill-climbing (added: the direct test of the verifier's hypothesis)
Period 15, phase 0, Vigenere and Beaufort (variant Beaufort is Vigenere with the key negated, so it is covered).
Score: quadgram mean of the whole plaintext. Search: 30 random restarts, each a coordinate ascent over the 15 key
letters (all 26 values per position, repeated until no gain), seeds fixed (1865). Calibration first: the same
search on each calibration telegram must recover >= 12 of its 15 key letters on at least 5 of the 7 calibration
telegrams, else the method is reported as not able to work on texts this short and (f) is not used as evidence.
Controls: the same search on 100 shuffles of each reader's text. Pass: real best > max of the 100 controls, both
readers; a passing key then goes to (e).

## (e) Candidate key
A key counts only if (1) it passes its step for both readers, (2) its decryption gives connected English over most
of the text (at least two thirds of the 25 groups give words or word fragments that fit the clear words around
them) on both readers' texts, judged group by group in a table, (3) it beats every control. Then it is tried on the
other telegrams of 10-11 April (T07-T10) at all offsets. Words that need a letter neither reader gave are marked
corrected.

## Not done
No new transcription; no search of other volumes; nothing posted.
