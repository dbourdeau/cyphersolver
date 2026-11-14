# Pigeongrammes and telegraph ciphers, France 1870-71 (Pillon / Debove collection)


Write-up: `docs/pigeongrammes1870.html`, about the inspectors' code only (outcome since 13 Nov 2026: key recovered based on adjacent plaintext, read in part, 62% of groups valued as written, strict count of record; 65% with the assumed digit slips; profile.json). The Favre / delegation code (Chaudordy letter, 18 Dec 1870) is a different cipher, still in progress, with no page of its own yet; its sections below are working notes.

## Source
Alexandre Pillon (collector) and Bruno Debove, via the forwarded email of 7 Nov 2026.
Share: grosfichiers.com/LNfgdfb7tcb, Pigeongrammes.zip, 2.9 GB, expires 21 Nov 2026. Data kept OUTSIDE the repo at
`C:/Users/dbour/pigeon_dl/data/` (46 xlsx/docx/png fetched by HTTP range request; the 130 JPG/TIF scans, ~2.9 GB, not
fetched: C: had 4 GB free). `index.json` there lists the zip members. Article: Pillon and Debove, "Le pigeongramme chiffre
de 1871", Le Lien philatelique no. 144, Sept 2025. Do not publish or send anything to the cc list before asking the user.

## What the collection holds (LIST_Pigeongrammes.xlsx, 66 rows)
- R1: prefects' code, 4-digit, alphabetical, about 1,070 entries reconstructed (Repertoire1.xlsx).
- R2 "Chiffre nouveau": numbers 1-~2300, disordered, several numbers per word; 926 entries (Repertoire2_ChiffreNouveau.xlsx).
- R3 "Chiffre stations/Marine": 82 entries (Repertoire3).
- "Unknown directory": 4-5 digit groups, values to ~5,800, used on many Jules Favre pigeongrammes (2eme serie 15, 31, 38 ...).
- Short items: inspectors' cipher, navy cipher, British Embassy (Lyons) cipher, a period telegraph directory.

## Chaudordy letter (701218)
1,428 numeric groups, 632 distinct, max 2272. NOT the unknown directory: its value range and frequent groups
(10, 82, 89, 65, 25, 60, 44, 62) match R2. Applying Pillon's R2 table covers 872/1428 groups (61.1%) and gives
diplomatic vocabulary (FRONTIERE, PAYS, PRUSSE, ETRANGER, REFUS, FAVORABLE). Not yet a reading: R2 homophone entries
conflict (82 = FAIRE x22 is implausible), no control run yet.
Prior art: Feldman auction lot (davidfeldman.com, 2013 May airmails 10262; 2018 Mar France 1356) describes a numeric
Favre-to-Bordeaux dispatch "n 36 Mr de Chaudordy", 18 Dec 1870, captured by the Prussians; no decipherment found.
Pillon's R2 sheet cites a published plaintext (archive.org sim_revue-historique_january-april-1884_24, p.348) for DIL_23.

## Result 7 Nov 2026: Chaudordy is in the unknown directory, not R2
Control run (pigeon_freq.py). Top-30 most frequent groups shared with the Chaudordy letter: R2's own letters 4;
R1 letters 0; but the "A Jules Favre" pages with no reconstruction share 10-13: 2emeS-35 (13), 2emeS-34 Favre page (11),
AJulesFavre_710126 (12), 2emeS-23 left (10), AJulesFavre_711019 (8), 2emeS-15 (6). Common top groups 10, 88, 89, 82, 913, 48.
The 61% R2 coverage was a range artefact: the earlier R2 "decode" is withdrawn.
Pooled (pigeon_pool.py): 8 transcriptions, ~10,900 groups, values to ~2,300, one code. 40 four-group runs recur across
different letters (366,157,1326,1719 in four letters; 490,442,352,310 in three), so these letters share phrases and the code.
Stereotyped openings: 2156 839 .. 1383 .. 732 883 in 2emeS-34 and AJulesFavre_711019.
Caveats: transcriptions are Pillon's (some ?, ??? cells); AJulesFavre_710126 has values to 17189 (transcription slips);
2emeS-35 mixes Gambetta (R2) and Favre columns, only the Favre columns belong in the pool.

## Step 1 result (7 Nov 2026): the plaintext of the Chaudordy letter is in print
Jules Favre, "Le Gouvernement de la Defense nationale", vol. 2 (1871), "Simple recit", pp. 265-270 (archive.org
gouvernementdela02favr, OCR _djvu.txt): "A M. de Chaudordy, a Bordeaux. 18 decembre 1870. Nos communications par ballon sont si
incertaines ..." to "Nous sommes pleins d'espoir. Jules Favre.", printed "sans y rien retrancher". Cleaned text:
chaudordy_18dec_plain.txt (1,267 words, 6,215 letters; extract_plain.py; two OCR slips repaired by hand, not re-checked
against the page image). Cipher: 1,428 groups, 1.13 groups per word, and the cipher opens straight with the text
("763 637 386 1980" = nos communications par ballon), no header. The Prussians' copy (Feldman lot: "n 36", "Aus Paris per
Luftballon") is a duplicate of the letter carried by another balloon; Favre's 21 Dec letter says duplicates travel separately.
Favre's 17 Dec midnight dispatch (to Chaudordy, same book p. 264) and his 16 Dec letter (p. 259-260) are also printed.
The Enquete parlementaire "Depeches telegraphiques officielles" (1875, 2 vols, by departement) holds prefect telegrams, not
Favre's letters; Chaudordy's telegram n 5,505 of 18 Dec there paraphrases the 17 Dec dispatch.

## Step 2 result: known-plaintext alignment (partial)
Position-match anchors (anchors.py: a group whose every occurrence lines up in order with every occurrence of one word, at
the same position ratio): 1792=conference (9 of 11 occurrences), 1980=ballon (3/3), 2232=bruxelles (3/3), 944=question (4/4),
977=sauf (3/3), 723=premiere (3/3), 998=partir (3/3), 862=comme (4/4), 835=cependant (3/3), 182=negociations (3/3), 740=the
Angleterre group (3/3). Also confirmed by repeats: 32 1413 43 1024 1319 = "des 10 et 12 decembre" (1413=10, 1024=12, 1319=decembre).
Structure: a homophonic code, whole words for some terms (names, "conference", numbers), syllables for others (reconnais =
44 1827 234 in the HMM reading), several groups for "de" (25, 57, 81, 967 ...). Not nulls on the evidence so far.
HMM word alignment (align_hmm2.py nulls; align_hmm3.py anchor prior; EM on the single letter): first ~140 groups align
as readable word-for-word text and match every anchor; later stretches read as French only because the plaintext is the
reference, and the recovered lexicon is NOT yet consistent (17 of 281 repeated groups map to one word). The letter-level
aligner (each group emits a letter chunk) failed (probability bookkeeping gave NaN) and was removed. So: plaintext known,
alignment hypothesis only, no verified codebook beyond the anchors above.
The other Favre-family letters (pool.json, 8 letters) are NOT yet read.
Full zip downloaded: C:/Users/dbour/pigeon_dl/Pigeongrammes.zip (2,935,235,727 bytes, chunked range requests; resume with
-C - does not work on this host, it re-appends). Enquete and Favre OCR in C:/Users/dbour/enquete/.

## Correction and scan check (7 Nov 2026, later)
- Pillon ALREADY HAS the printed text: his folder holds TrasncriptionChaudordyEventuelle1-4.png, page images of Favre's
  "Simple recit" pp. 265-270 (named "eventuelle" = possible). So the plaintext is not a new find; what is new is evidence that
  it is the plaintext (below). Do not present it to him as a discovery.
- The scan (MessageChiffre_Chaudordy1.jpg, local in pigeon_dl/scans_chaudordy/) opens with a plain-text header line:
  "N 36. Mr de Chaudordy a Bordeaux, 18 decembre 1870" = Favre's printed heading. Cipher then starts 763 637 386 1980.
  Page 1 ends "... armistice avec ravitaillement" groups (1915 161 947 620 .. 55 82 151 604 201 186); page 2 = Chaudordy2.jpg.
- Transcription spot-check of spreadsheet row 9 vs the scan (913 607 185 938 216 628 1792 1827 283 44 333 64 129 552 330 ...):
  identical. The groups are not the problem.
- Windowed bootstrap (align_slide.py, seeded by the first 100 groups): reads as the printed text for roughly the first 330
  groups (e.g. 1827 283 44 = j'avais pense que; 913 607+185 = nous devions; 513 862 1997+1293+1296 = poser comme condition;
  30 459 1988 = sine qua non; 1915 = armistice, 620 235 55 82 151 = ravitaillement), then loses sync (nulls pile up).
  Likely causes, not yet fixed: elisions (l', d', qu') coded as separate or merged groups (my tokens merge them: "d'armistice"),
  and a flat null cost. Trusted entries so far are only those used in the first ~200 groups (86 groups, noisy).
- Third occurrence of the armistice/ravitaillement run in the cipher (1915 567 947 620 231 55 82 151, group ~335) matches the
  print's "quinze jours d'armistice avec ravitaillement": the cipher follows the printed text, it does not diverge.

## Elision fix and waypoint runs (7 Nov 2026, evening): no consistent codebook yet
- align_slide2.py (kept): tokens split at elisions (l' d' qu' jusqu' ...), a unit = one token or elision+word coded together.
  Result unchanged from the unsplit version: 34/250 repeated groups consistent, nulls climb from group ~200. So elisions were
  NOT the cause. It reads as the printed text up to roughly group 330 (see the 28-line extract in the log of this session:
  1827 283 44 = j'avais pense que; 913 607+185 = nous devions; 30 459 1988 = sine qua non; 1915 = armistice ...).
- Hard waypoints from repeated cipher runs against repeated printed phrases (cipher group index : token index):
  56:47 (32 1413 43 1024 = des 10 et 12), 342:320 (same run), 172:161 and 289:261 (216 628 1792 = a la conference),
  214:194, 306:288, 935:931 (1915 .. 947 620 .. 55 82 151 = armistice avec ravitaillement; the 306 copy reads 567 for 'avec').
  Cipher groups per printed token between waypoints: 56/47, 116/114, 42/33, 75/67, 17/27 (!), 36/32, 593/611, 493/427.
  Typical 1.1; the 289->306 stretch (17 groups for 27 tokens) and 342->935 (593 for 611) are short: either one group codes a
  phrase there, or the transmitted letter is a shorter version of the printed one. A banded DP with phrase units absorbed the
  difference without gaining consistency (1/271), so those runs were discarded (align_band.py, align_wp.py deleted).
- What this supports: the cipher IS this letter (header, four exact-repeat anchors, order and spacing), but it is not
  word-for-word the printed text, so a plain known-plaintext codebook cannot be built from the print alone beyond ~330 groups.

## Options 1-5 run (7 Nov 2026, late)
1. Cross-letter check (crossletter.py): codebook of 63 single-group words from the first 200 groups, scored by word pairs seen in
   Favre's 287k-word text vs a shuffled codebook. Chaudordy itself 73 vs 36 (training letter), other seven letters together
   42 vs ~35: no usable confirmation (few known groups per letter: 56-264). The early codebook does not transfer yet.
2. Scan page 2 (MessageChiffre_Chaudordy2.jpg): the transcription covers both pages (page 1 ends at group ~925, page 2 runs
   ~935-1428, last line 423 953 57 946 863 30 65 473 2054 337 135 842 65 2192 2226). No missing block. The page carries a German
   note "Aus Paris per Luftballon" and a signature/initials "C. o. n. P" (Prussian handling). Digit shapes: the writer's 5/9/6 are
   close; confusable high-frequency pairs (65/69, 55/59, 85/89, 95/99) were NOT checked against the ink (scan has an EXIF
   rotation; crops need rotating first). Open risk for any consistency test.
3. Printed sources: Favre's book prints three Favre->Chaudordy balloon letters: 16 Dec (Paris, ~640 words, p. 259-260), 17 Dec
   midnight dispatch (p. 264-265), 21 Dec (~250 words, p. 271-272) besides the 18 Dec letter. Direction matters: pigeongrammes
   went INTO Paris, so the "A Jules Favre" pool letters are Chaudordy/Gambetta/Steenackers to Favre; the book quotes some
   Chaudordy letters (19 Nov, 23 Nov receipt, 10 and 12 Dec summaries) as short extracts. None matched to a pool letter yet.
4. Structure of the pooled code (8,351 groups <= 2400, 1,513 distinct values, 7 letters): not alphabetical (initials of 11 anchor
   words in number order: n p c c q s p d c b b); frequency-banded like R2 (values 1-100 carry 25% of tokens, ~20 per value;
   100-1000 carry 56%; above 1000 only 19%, ~2.4 per value); Spearman(value, count) -0.35; 80-87% of each letter's tokens are
   values used by >= 3 of the letters = one shared table. 1792/628 style syllable spellings coexist with whole-word codes.
5. Short items: British Embassy cryptogram (701024_ChiffreAmbassadeAngleterre.xlsx): 4-digit groups to 7305, ~170 groups, its own
   code (Lord Lyons, 23 Oct 1870), no crib: not attempted beyond inspection. Inspectors' cipher (2emeS-1, "Tours 2 novembre (chiffre des
   inspecteurs)"): a MIXED clear/coded telegram, 1,173 tokens = 736 four-digit groups (343 distinct) + 437 clear words (names and
   addresses in clear: Nantes, Rennes quai de l'Universite 2). Commonest groups 0101 (49), 0201 (31), 0301 (28), 4914, 2119, 8328.
   inspecteurs_cloze.py (word-bigram fill-in, one word per group): log-prob -7085 random -> -5025, but the output is dominated
   by "de/la" and is NOT a reading; it only shows the text is about the telegraph service, the war, Paris/Tours. Best lead:
   the original circular is probably printed in Steenackers, "Les telegraphes et les postes pendant la guerre de 1870-1871" (1883);
   with the real plaintext this 736-group text would give a codebook directly (clear words anchor the alignment).

## Scan check and source hunt for the inspectors' circular (7 Nov 2026, night)
Scan check (rotated crops of rot_MessageChiffre_Chaudordy1.jpg / 2.jpg, enlarged 3x; lines 2-5 of page 1 and the last line of page 2,
about 100 groups read against the sheet). Writer's digits: 9 has a straight q-like descender, 8 is a two-loop figure, 5 has a hooked
top (resembles a long s), 4 resembles an open L, 7 has a long descender. Result: 2 misreads in ~100 groups (~2%): line 4 col 2
is "50" not "80" ("80" occurs once in the whole letter, "50" four times), line 4 col 11 is probably "635" not "639". Pillon's
double readings "60/40", "65/165?" and "2/361" were split into two groups each by my extraction (3 spurious groups); fixed to the
first value (image shows 60; the 65 is smudged; 2/361 undecided). Corrected list: chaudordy_nums.json (1,425 groups; original
kept as chaudordy_nums_orig.json). Re-running the alignments on it changed nothing (windowed consistency 28/257 vs 34/250), so
transcription slips are NOT what blocks the codebook. Line 63 (fold tear, bottom of page 1) is damaged: 14 cells with '?'.
Underlines in the scan (888 on lines 1 and 3, 66, 50 elsewhere) are in the same ink: probably the copyist's marks; meaning unknown.
Source hunt for the inspectors' circular (Tours 2 Nov 1870): archive.org has no Steenackers 1883 book under any search I tried
(catalogue by creator/title, full-text for "sorte de secousse", "chiffre des inspecteurs"); the Enquete telegram volumes and Favre's
book do not contain it. What exists: the Algeria volume of the commission report (archive.org sc_0000928533_00000001739293, de la
Sicotiere, 1875) prints Dec 1870 telegrams headed "(Chiffre des inspecteurs)" between Algiers and Bordeaux (Du Bouzet, Cremieux),
so this cipher was used by the government and its commissioners, not only inside the telegraph administration; plaintext only,
no ciphertext. Still to try: Gallica copy of Steenackers 1883 (needs Chrome), HathiTrust/Google Books full text, Pillon.

## Gallica and HathiTrust for Steenackers 1883 (7 Nov 2026, Chrome)
- Steenackers, "Les telegraphes et les postes pendant la guerre de 1870-1871: fragments de memoires historiques" (Charpentier, 1883,
  620 p.): Gallica ark:/12148/bpt6k220903s (public domain, 622 views) and HathiTrust hvd.hn6bui (Harvard copy, full view, 638 scans).
- Gallica: SRU catalogue query works in Chrome; the content-search service returns 0 hits for every word (not indexing this book) and
  per-page texteBrut / item pages hit a Cloudflare "Verify you are human" / ALTCHA check (not clicked; left for the user).
- HathiTrust: in-book search works without login (babel.hathitrust.org/cgi/pt/search?q1=TERM&id=hvd.hn6bui). Searched, no matching
  passage: "chiffre des inspecteurs", "Tours, 2 novembre", "reussite presque certaine", "Fosse Nantes", "Rennes Universite",
  "Nantes Rennes pigeons". Hits that are NOT the circular: "secousse" p.407 (balloon landing), "colombophiles" p.254,
  "parti pris" p.272 (list of messengers), "inspecteurs" p.608 (circular of 2 Feb 1871). So the 2 Nov telegram is probably not
  printed in this book, or is printed with different wording than Pillon's clear words (his clear words may be his own guesses).
- Not yet done: page-by-page text of hvd.hn6bui (seq=N&format=textonly, 638 pages) for a local search by name/date; Pillon's
  scan of the original telegram would tell whether the clear words are original.

## Pillon's reply (7 Nov 2026, evening) and what it changes
Sent by Dan (shortened draft); Pillon answered inline, in English. His answers:
- Confirms the Chaudordy letter and the "A Jules Favre" pages share the unknown nomenclator ("Exact"). Asks whether the sheet
  701218_2emeS-34_Gauche is this letter's family (it is a separate letter, same code) and whether we have a partial reconstruction.
- Digit confusions 5/8 and 5/9 are real in his transcriptions; the original clerks also made encryption errors.
- The CLEAR WORDS in the inspectors' telegram ARE in the original (so it is a genuine mixed clear/coded telegram, and the clear
  words are fixed context). He sent the original scan: "Steenackers a Mercadier, rue de Grenelle St Germain 103, Paris. 2me Serie
  n 1. Tours 2 Novembre (chiffre des inspecteurs)", a pigeon dispatch, with a printed Gambetta proclamation "A L'ARMEE" and a
  stamp "Cabinet du Directeur General" on the film print. (Image sent in chat; snips of the scan are now on the site, with his permission from 8 Nov 2026.)
- His reading of the logic: like R1, with "beacons" 0101, 0201, 0301 that mark syllables.
- No plaintext exists for any "A Jules Favre" page: every message in the unknown nomenclator is fully enciphered.
R1 test (7 Nov): only 18% of the inspectors' groups are in R1's table (10% by chance) and the values make no sense in context:
R1 is NOT the inspectors' table; the inspectors' code has its own table with R1-like logic.
Structure seen in the telegram (hypothesis, from the scan): 0101/0201/0301 act as brackets around spelled proper names
("Faites dire au 4007 0301 9802 6124 0301 que 5218 0301 9802 6124 0301 ...", "0301 1114 5911 0131 0423" a second name, both for
people at Nantes (quai de la Fosse 25) and Rennes (quai de l'Universite 2)). The same 6-group run 8328 9214 0218 4906 3316 8328
opens and closes the telegram (0101 ... 0201 / 0101 ... 0101), first and last group equal. Guess to test: a person's name spelled
in syllables, e.g. ER-NEST-MER-CA-DI-ER = Ernest Mercadier (6 syllables, first and last "er"), the addressee. UNVERIFIED: do not
quote it as a reading. Test it against the other spelled names (5504 1122 2514 3316 ends in the same 3316).
For the Chaudordy/Favre code the analogous idea: the commonest low groups (10, 82, 89, 65, 913 ...) may be balises/markers
(R1 has 0104 adjective, 0107 end of paragraph, 0119 plural, 0122 feminine, 0128 future, 0136/0137 syllabic ...) rather than words,
which would explain why a one-group-per-word alignment drifts. Not tested yet.

## Name crib on the inspectors' telegram (7 Nov 2026): tentative syllable values
inspecteurs_runs.txt lists all 157 coded runs with clear-word context; inspecteurs_syllables_tentative.md has the table.
Repeated runs: 0101 [8328 9214 0218 4906 3316 8328] 0201 opens and closes the telegram = S-TEE-N-ACK-ER-S (Steenackers); after "a":
0102 [5504 1122 2514 3316] 0102 = MER-CA-DI-ER (Mercadier); 6816 4001 6129 8328 (x3) = PI-GE-ON-S (pigeons); 0919 5121 6129 (x2)
= BAL-L-ON (ballon?). Cross-checks: 8328 = S (initial in Steenackers, final in pigeons), 3316 = ER (final in both names),
6129 = ON (pigeons and ballon). The telegram is about pigeon fanciers (20 and 48 in clear, "qui restent ... et reviennent").
Still tentative (one document, no independent confirmation); the other beacons' meaning and ~320 groups are open.

## Steps 1 and 2 after the name crib (7 Nov 2026)
Step 1 (apply the tentative syllables to the other bracketed runs): the table covers only 52 of 736 coded groups (7%). The Nantes
and Rennes correspondents' names (9802 6124; 1114 5911 0131) contain no known syllable, so they cannot test it. No conflict found.
New: 7508 8328 recurs in the same frame ("0101 7508 8328 8628/8626 ..."; "20 ... 7508 S 8626 qui restent 48"): possibly a second
way to write pigeons (a whole-word group plus S, next to the spelled PI-GE-ON-S); only two occurrences, treat as a guess.
Step 2 (are the low Chaudordy groups inflection markers like R1's balises?): in the aligned region (first 330 groups, 100
content tokens) plural, feminine and other words use the same number of groups relative to syllables (-0.33, -0.38, -0.49; infinitives -1.12,
n=8), so no sign that inflected words take extra marker groups. Groups under 100 are 23% of the aligned groups; only 43%
align to function words, and just three are consistent (57 = de x4, 5 = un/une, 62 = la). The alignment is too weak to settle
it: markers neither supported nor excluded. Not pursued further.

## Looking for the Nantes and Rennes fanciers (7 Nov 2026, no input from Pillon needed)
Searched: Dagron, La poste par pigeons voyageurs (Gutenberg 19588; short, none of the names); Steenackers 1883 on HathiTrust (hvd.hn6bui:
"Nantes" only p.598, a list of thanks; no "Rennes" hit); archive.org full text for the two addresses (no hit).
Best context found: Societe d'acclimatation, Bulletin 2e serie t. IX (Oct 1872), "La poste par pigeons voyageurs" pp. 624-664
(archive.org bulletindelasoci0209soci, OCR kept in C:/Users/dbour/pigeon_src/). It names the Paris colombophile society
"L'Esperance": Ed. Cassiers (president), Louis Van Rosebeke (vice-president), Nobecourt, Traclet, Thomas; Steenackers directing
the pigeon service at Tours; Rampont (posts, Paris); Chassinat, Ségalas, Dagron, de Lafollye. No Mercadier, no Nantes/Rennes fancier.
Guess only: the two bracketed names (9802 6124 = 2 syllables; 1114 5911 0131 = 3) could be fanciers such as TRA-CLET and NO-BE-COURT,
but neither candidate shares a syllable with the known values, so this cannot be tested. Not recorded as a reading.
Conclusion: the remaining routes need Pillon (what the different beacons mean; other pieces in the inspectors' cipher) or a new source
naming the Nantes and Rennes correspondents.

## Date test across the Favre-family letters (7 Nov 2026): an independent check of 1792 = conference
The scans carry clear headings (e.g. 2emeS-15: printed "Service des depeches par pigeons voyageurs organise par M. Steenackers ... a M. Mercadier,
rue de Grenelle St Germain 103", "Depeches officielles, 2me Serie N 15", "A Monsieur Jules Favre, 14 novembre 1870"). So each page has a date.
Occurrences by letter (headings from Pillon's list and the scans): 1792 (conference) 0 in 24 Oct and 14 Nov, 7 on 28 Nov, 1 on 18 Dec,
9 in the Chaudordy letter, 5 on 20-21 Dec, 2 on 19 Jan, 3 on 26 Jan. History: the Russian circular/London Conference question
begins in November. So 1792 behaves like "conference" across letters, a check independent of the Chaudordy alignment. 1915 (armistice)
7 on 14 Nov, 7 on 28 Nov (Thiers mission, armistice talk), 3 in Chaudordy, none in January; 2232 (Bruxelles, the proposed meeting place)
only on 18 Dec (3 in Chaudordy, 1 on the 2emeS-34 left page). 740 is NOT settled: the anchor said Angleterre, the alignment of the first
groups puts it at "la Russie" (2066 = l'Angleterre there).
Favre quotes only two lines of Chaudordy's letters of 20 Dec ("Je ne doute pas de votre grande utilite a Paris, mais ici vous etes necessaire")
and 29 Dec (Angleterre ... adhesion a la Conference ... necessaire hors de la capitale ... arguments de mon rapport precedent ...): too short to
locate in the pool without a dictionary. The method (date and topic profiles of groups) can propose more anchors; each needs checking.

## History-timed cribs (timing_cribs.py, 7 Nov 2026)
Letters by date (groups, A Jules Favre columns only for 2emeS-35): 24 Oct 649; 14 Nov 1,470; 28 Nov 1,091; 18 Dec (2emeS-34 left) 1,401; 18 Dec
(Chaudordy, Favre out) 1,425; 20-21 Dec 1,785; 19 Jan 1,053; 26 Jan 1,280.
Validation: a history-only profile ("absent in the two earliest letters, present from 28 Nov: the Conference question") ranks 1792
(conference) FIRST among 642 groups used >= 5 times; 977 (sauf, from sauf-conduit) is 10th and 998 (partir) 11th, 1980 (ballon) 57th,
while 1915 (armistice) and 944 (question) are not conference-timed (ranks 610, 596), as expected. So the method finds topic vocabulary,
roughly: 3 of the top 11 groups are verified conference words. Runners-up (780, 64, 947, 587, 2, 352, 125, 160) are NOT identified:
their Chaudordy-aligned words are mixed (780 = vous/et/nous/paraît ...; 64 = repousser/le/combattaient...). 780 has 0 uses in the 24 Oct and
14 Nov letters (about 2,100 groups) although a pronoun like "vous" should be common there: either another homophone was used earlier or
the table or clerk changed in late November (to check with Pillon: R2 is called the "new cipher" in some correspondences).
Table stability (cosine of group-usage vectors, groups used >= 5 times): neighbouring dates are closest (24 Oct vs 14 Nov 0.67, 14 Nov vs 28 Nov 0.76,
18 Dec 2emeS-34 left vs 20-21 Dec 0.79); the Chaudordy letter (Favre writing OUT) is the least like the others (0.47-0.70). Same table
overall, but usage differs with date, topic and direction (the homophone choices differ by writer).
Limits: eight letters is too few to name a group from its profile alone; no new value was added to the codebook.

## Pillon's second reply and the alphabetical test (7 Nov 2026)
Pillon: x01 tags: do not read too much into the first digit; in R1 balises 0136/0137/0138 are interchangeable, mostly paired
0136 xxx 0136 or 0136 xxx 0137 (consistent with the bracket pairs seen here). He suggests the inspectors' code is almost alphabetical
(83xx = S, 92xx = T) and proposes "J'ai recu votre depeche" for 5926 0603, and capitale for 2215. He does not know who is at the Nantes and
Rennes addresses (quai de la Fosse was a commercial area). Wants the list of reliable values (favre_reliable_values.md).
Alphabetical test (alpha_test.py): place the 13 syllable values in an alphabetical list of French words from Favre's books; their
fractional position predicts value/9999 with mean error 0.012-0.016 (random mapping about 0.33). So the inspectors' table IS an alphabetical
lexicon laid out over 0000-9999 (R1's own letter ranges, scaled: A 01-06, B 07-09, C 09-13, D 14-17 ... S 47-52, T 52-54 of 58 hundreds, have
the same shape). Consequences: (1) 4906 is a K-initial syllable ("ack" would sit at 0.00, K at 0.5) and 0218 is A-initial (N would be at 0.58):
Steenackers is spelled S-TEEN-A-K-ER-S (phonetic), so no "A and E reversed" is needed; (2) 5926 is NOT "recu" (recevoir would sit near 0.77, the number is
0.593) and 0603 is NOT "depeche" (0.25 vs 0.060): both are off by about 0.18, ten times the typical error; 2215 = capitale is also unlikely
(capitale about 0.14, number 0.22); (3) the Favre-family code is NOT alphabetical (verified words: negociations 182, premiere 723,
cependant 835, comme 862, question 944, sauf 977, conference 1792, ballon 1980, Bruxelles 2232 are in no alphabetical order).
Position-constrained fill-in (inspecteurs_alpha_cloze.py, window +-0.03 of the number's position, bigram LM, clear words fixed):
produces mostly frequent corpus words (Alger, septembre, il, de): not a reading. It ignores bracketed spelled runs and syllable entries. Next version
must treat bracket runs as syllable spelling (fix the S/ER/ON/PI/GE/K/A/TEEN/MER/CA/DI values) and use a telegraph-vocabulary LM.

## Spelled-run solver for the alphabetical inspectors' code (spell_solver.py, 7 Nov 2026)
Method: split a candidate string into as many pieces as there are groups so each piece's alphabetical position (in a French word list built
from Favre's books, the Enquete volumes and the 1872 pigeon-post article) matches value/9999 (+0.015 bias found in alpha_test.py).
Validation on the known runs, rank among ~24,000-31,000 candidate strings: pigeons rank 8 (err 0.012), Mercadier rank 30 (0.025), ballon 145
(0.013), Steenackers/Steenakers ranks 6-8 (0.015); the correct string is always in the top 0.5% but not always first, so this SHORTLISTS, it does not decode.
It also rejects "Ernest" for the first-name run 6819 3412 (err 0.17): 6819 is a P-initial entry (the best fits are Pierre, placer, pigeonniers;
unresolved). It supports 5711 = monsieur (+0.016), 4007 = general (+0.011), 1206 = capitale/capitaine (+0.000), 0603 an A-word such as appui
(Pillon's "depeche" is 0.19 off; "recu" for 5926 is 0.17 off, 5926 is an M/N-word such as mourir/mouvement/militaire/moyen), 2215 not capitale.
Names: the third spelled name 9113 8317 1504 fits TROCHU (err 0.011; next best name 0.052 among 51): "Faites dire au general Trochu que ... est en ... a Rennes
quai de l'Universite 2" (hypothesis: personal news for relatives, genre typical of pigeon dispatches). The Nantes name 9802 6124 fits VINOY (0.012,
close second 'Vergne' 0.015: not discriminating). The Rennes name 1114 5911 0131 fits no sieges-era name well (best 0.022). All of this is a
hypothesis until another document confirms Trochu or Vinoy.

## Pillon on Mercadier (7 Nov 2026): his decomposition vs the alphabetical rule
Pillon: MERCADIER = 5511 0101 6819 3412 0102, i.e. MER = 5511, then 6819 3412 = CAD + IER or CA + DIER (beacons neutralised).
Scored against the alphabetical rule (word-list position of each piece vs value/9999 + 0.015; typical error on other anchors 0.012-0.016):
- his MER-CAD-IER: mer +0.019, cad -0.569, ier +0.108, mean 0.232; MER-CA-DIER: ca -0.570, dier -0.073, mean 0.221. 6819 sits at P (0.70), CA/CAD at 0.13.
- mine MER-CA-DI-ER = 5504 1122 2514 3316: +0.020, 0.000, +0.016, +0.005, mean 0.010.
- the pair 6819 3412 fits PI + ERRE (-0.004, -0.004), i.e. "Pierre" (or another P-E word); 5511 sits at 'mai...' (0.566): "M." or maitre/maison, not a certain MER.
Open: (a) 5504 1122 2514 3316 also stands alone in "voici la reponse de 5219 [name] 9550 en ..." where the addressee quoting himself would be odd;
(b) Mercadier's first name is given as Ernest in sources, not Pierre; (c) the rule is "almost alphabetical", exceptions possible. Both readings are
therefore unconfirmed; the rule disfavours CAD = 6819 strongly (0.57 off, 40 times the typical error). Ask Pillon how he got CAD / IER.

## Pre-reply checks (7 Nov 2026)
Scan check of the telegram (Pillon's scan, enlarged crops): header "(chiffre des inspecteurs) 0101 8328 9214 0218 4906 3316 8328 0201 a 5511 0101 6819 3412 0102
5504 1122 2514 3316 0102" and the name lines "0301 que 5218 0301 9802 6124 0301 3407 bien 7027 0312 a Nantes quai de la Fosse 25 et a 5711 0301 1114 5911 0131 0423 de 1206 au
4007 0201 9113 8317 1504 0201 que 5218 0301 1114 5911 0131 est en 1026 8416 0303 a Rennes quai de l'Universite 2" all match his transcription digit for digit.
Chance test (28,897 candidate strings, 4-12 letters): for 9113 8317 1504 only ONE string fits as closely as Trochu (mean error <= 0.011), 0.04% fit within 0.015;
testing 51 names, the chance that some name fits this closely by luck is about 0.15%. So Trochu (and 4007 = general) is a real signal.
For 9802 6124 (two groups) 0.7% of strings fit as closely as Vinoy (202 strings): Vinoy is NOT supported (about a 30% chance that some of 51 names fits). Drop it.
The Rennes name 1114 5911 0131 remains unidentified. Mercadier decomposition still open (see above).

## Pillon withdraws the Mercadier correction (7 Nov 2026)
Pillon: disregard the previous email; there is ANOTHER recipient before Mercadier, "5511 0101 6819 3412", not Mercadier's first name (authors rarely put first
names in a heading). So the heading reads: Steenackers a M.(5511) [6819 3412] [5504 1122 2514 3316 = Mercadier]; my MER-CA-DI-ER reading stands (all four within 0.02).
5511 fits "M." (-0.007; monsieur is +0.036). 6819 3412 = a surname P + E... (18 of 3,644 capitalised names fit within 0.005: Pierret, Pierron, Perret, Perrier, Piet, Pierre ...): not specific.
Search found no Pierret among siege-era telegraph officials; Mercadier was director of telegraphs at the siege and rue de Grenelle 103 was the central Paris post (consistent).
Open: who the other recipient is.

## Blind check of the genre reading (7 Nov 2026): family news for generals' wives
Prediction made before computing: the last paragraph passes personal news ("Faites dire au general X que Madame X est bien portante a Nantes ...", "en bonne sante").
Fits (word-list position vs value/9999 + 0.015; typical error 0.012-0.016): 3407 = est (0.000), 7027 0312 = PORT + ANTE (-0.010, +0.004), 1026 8416 = bonne sante
(-0.004, -0.009; the pair occurs three times: "9550 en 1026 8416 frere", "... 0201 1026 8416 0109. J'envoie a", "est en 1026 8416 0303 a Rennes"), 4007 = general (+0.011),
5218 = madame (+0.023; weaker: leur/lettre fit at +0.005). Null: a random word pair fits two random groups within 0.01 each in 0.05% of trials.
So the whole-word alphabetical rule holds on words that were not used to calibrate it, and the paragraph reads: "Faites dire au general [9802 6124] que Madame [9802 6124] est bien
portante a Nantes, quai de la Fosse 25, et a M. [1114 5911 0131 0423] de 1206 [Brest/Bretagne?], au general Trochu que Madame [1114 5911 0131] est en bonne sante a Rennes,
quai de l'Universite 2." Names other than Trochu remain unidentified; Vinoy stays unsupported.

## Benchmark loop on the inspectors' code (bench_loop.py, 7 Nov 2026)
Benchmark: 10 items with independent support (general, est, bonne, sante, portante, trochu, mercadier, pigeons, steenackers, ballon). The solver sees only
the group values and the adjacent clear word and ranks the gold string among ~29,000 candidates (words, names). Score = mean reciprocal rank (MRR).
Rule: one hypothesis per loop, weights fixed in advance; keep if MRR rises by >= 0.01; stop after 3 consecutive rejections.
Loop 0 baseline (position only, sigma 0.02, +0.015 bias): MRR 0.190, top-10 4/10.
Loop 1 frequency prior (log unigram): 0.565 (+0.375) KEPT. Loop 2 bigram LM with the clear neighbours: 0.615 (+0.049) KEPT.
Loop 3 isotonic calibration from R1's own numbering instead of the bias: 0.523 (-0.091) rejected (R1's lexicon has no syllable entries, so its letter ranges do not transfer).
Loop 4 spelled-piece length prior (<= 4 letters): 0.617 (+0.002) rejected. Loop 5 name bonus for runs of >= 3 groups: 0.612 (-0.003) rejected. STOP.
Final: MRR 0.615, 6 of 10 gold items ranked first (general, est, trochu, mercadier, pigeons, steenackers); weak: bonne (18), sante (87), portante (468), ballon (13).
Untested (the loop stopped): H6 syllable count = group count (expected to fail: 'pigeons' is 4 groups, 'portante' 2).
Caveats: ten items, chosen because they were recognised (the easiest cases); Steenackers, Mercadier and Trochu were added to the candidate list from the printed heading and
history; bias and sigma were set from the earlier anchor fit, not retuned; accepted hypotheses are generic (frequency, context).
Next use: apply the final scorer to every unit of the telegram (apply_telegram.py) and read only high-margin outputs.

## Joint decoder loop (joint_loop.py, 7 Nov 2026)
Why: apply_telegram.py treated every unbroken run of groups as ONE spelled word, which is wrong (1026 8416 = two words 'bonne sante'; 7027 0312 = one spelled word 'portante'); its output
(septembre, lethargie, desiderata ...) is discarded. New decoder: beam-Viterbi over the whole telegram; clear words fixed; beacons reset the LM; chunks of k groups are whole-word (k=1) or spelled (k>=2)
words; chunk score = alphabetical position fit (sigma 0.02, +0.015) + log unigram - 1.0 per spelled chunk; chunks chained by a bigram LM. Benchmark: 20 gold word occurrences
(general x2, est, bonne x3, sante x3, portante, trochu, mercadier x2, pigeons x3, steenackers x2, ballon x2), hit = exact word at that place. Keep a hypothesis if it adds >= 1 hit; stop after 3 losses.
L0 whole-word groups only: 3/20. L1 beacon-bracketed run may be one spelled word: 11/20 (+8) KEPT. L2 free segmentation (chunks of up to 4 anywhere): 11/20 rejected.
L3 consistency voting (one meaning per group): 10/20 (-1) rejected. L4 monotone neighbour bounds: 11/20 (+0) rejected. STOP (3 in a row). H5 (100 candidates) and H6 (weaker prior) not reached.
Final decode (config: bracket-spelled only): hits = general x2, est, trochu, mercadier x2, pigeons x3, steenackers x2; misses = bonne|sante x3 (decoded ce|son, ce|soir), portante (qu|au), ballon x2 (citoyens).
Reading: the spelled-name mechanism is the big lever; ordinary words still lose to function words on frequency. Side hypothesis from this decode: 6819 3412 = 'prefet' (P-R + E-T), so the heading would read
"Steenackers a M./le prefet [..] Mercadier" (unverified; positions only). Next candidates: piece-level consistency across spelled runs (6129 = on in pigeons and ballon would give bal|l|on), domain LM for
telegraph/pigeon-post words, joint decoding of 'est bien portante' as spelled.

## Pillon's suggestions of 13 Nov 2026: PIERR-ET, messieurs, et, VIN-OY, DUC-ROT (heading_test.py)
Pillon (two emails, relayed by Dan): 6819 3412 = PIERR + ET (alphabetical, and a likely recipient); then "5511 0101 6819 3412 0102 5504 1122 2514 3316 = messieurs Pierret et
Mercadier" with 5511 = messieurs, 6819 = Pierret, 3412 = et; 0919 5121 6129 = BAL-L-ON; 4007 = general; after 4007 the names 9802 6124 = VIN-OY? and 2722 7802 = DUC-ROT?
Tested against the alphabetical rule (vocabulary here: wiki/topic_counts.json, 2,082 words used twice or more; the Favre/Enquete corpus of the earlier sections is not in the
repo, so the errors differ slightly) and against the telegram's own structure:
- 3412 = et: SUPPORTED. Position -0.005 (est = 3407, already supported, is five entries below). Context: "0101 0919 5121 6129 0201 3412 0201 6816 4001 6129 8328 0301" is
  [ballon] 3412 [pigeons], two runs identified independently, joined by 3412; also "2405 9211 3412 2405 7102" and "de 0530 3412 de" (the same word either side).
- 5511 = messieurs, 5711 = monsieur: SUPPORTED by structure. 5511 occurs once, in the heading, before THREE bracketed names in a row: [6819 3412] [5504 1122 2514 3316 =
  Mercadier] [5005 9701 2729]. 5711 occurs six times, each time before ONE bracketed run. Three later paragraphs open "0109 5711 [name]" with the same three names in the same
  order: [6519 3412] (5/8 slip for 6819), [5504 1122 2534 3316] (Mercadier, 1/3 slip), [5006 9701 2729]. Positions: messieurs +0.004, monsieur +0.001 ("M." -0.027 in this vocabulary).
  So the telegram has three addressees and a paragraph for each; 0109 closes a paragraph. This replaces "5511 = M." (C016).
- 6819 3412 = one name, P... + ET: in its own paragraph the run stands alone after "monsieur" and before 0109, so 3412 is inside the name there (the piece ET), not the word
  "et" before Mercadier. That fits Pillon's first version (PIERR-ET) and not his second (6819 = Pierret, 3412 = the word et). 6819 is three entries after PI (6816); "pierre"
  fits at +0.005. Pierret is consistent, not confirmed: entries such as pic, pie, pied would sit in the same three places, and two web searches (13 Nov) again found no Pierret
  in the Paris telegraph service of 1870. The "prefet" side hypothesis (P-R + E-T) is dropped: a title would not follow "monsieur" as a spelled run in a list of names.
- Third addressee 5005/5006 9701 2729: unidentified. 5006 is also a frequent stand-alone group (le fits at +0.001), 9701 is a V entry below vin, 2729 ends many runs (an E entry?).
- "voici la reponse de 5219 [Mercadier]": 5219 is the entry after 5218 (madame, hypothesis); mademoiselle fits at +0.003. This answers open point (a) of the 7 Nov section: the
  sender of the reply is a relative of Mercadier, not Mercadier quoting himself. Guess only.
- BAL-L-ON: unchanged (hypothesis, C007); the frame "ballon et pigeons" now reads through.
- VIN-OY for 9802 6124: NOT supported, as before (0.7% of strings fit two groups this well). New: 6124 lies BELOW 6129 (on), and "oy" sorts after "on" (+0.027); a phonetic
  "oi" would sort correctly (+0.008). Vinoy stays a guess.
- DUC-ROT for 2722 7802: NOT supported. duc fits 2722 (+0.017), but 7802 lies below 8317 (RO in Trochu) while "rot" sorts after "ro" (+0.037, about three times the typical
  error); 7802 sits at the start of R (r -0.020, re -0.017). The pair also occurs with no "general" before it ("... 0312 9516 0102 2722 7802 0101 1417 du 1118 recemment cree"),
  and 7802 opens other runs ("qui 7802 5102 tous les points les plus importants", "nous donne un 7802 3207"), so it is a piece such as R or RE. The general's name is open.
Does it help? Three whole-word values (et, messieurs, monsieur) and the paragraph structure (three addressees, 0109 as paragraph end) are added; no new passage reads. Asked
of Pillon: whether a Pierret (or Pieret, Piet ...) and a third official L-V-E appear in his sources next to Mercadier.

## Working reading of the inspectors' telegram (13 Nov 2026, later): about 58% of the groups have a value
Dan asked to keep going after the Pillon test. Method: read the telegram by context, using the code as a PAGED alphabetical book.
- Structure: a group PPLL is page PP (01-99) and line LL (01-30; only 5 of 754 groups have LL > 30, slips or misreads), so about 2,970 entries; rank = (PP-1)*30+LL.
  Single letters open their sections (c 1121 before ca 1122; d 2112; e 2729; f 3616; h 4113; k 4906; l 4914; n 5901; o 6019; r 7703; s 8328; t 9113; v 9612; y 9915).
  Pages 01-03 and 05, low lines, hold marker groups (beacons 0101/0201/0301/0501/0102/0103, paragraph end 0109, and endings such as 0311 past participle, 0312 -ant,
  0212 adjective/-aire/-ant, 0211 plural (unsettled: see 14 Nov), 0303 noun ending, 0307 imperfect, 0305 future or conditional since 14 Nov): like R1's balises. Their exact meanings are NOT settled.
- interval_cands.py lists, for a group, the French words that sort between the nearest known values (wordfreq list); anchors_inspecteurs.json holds the values; the
  machine gloss is inspecteurs_2nov_gloss.txt and the sentence reading, with holes and an English version, is inspecteurs_2nov_reading.md.
- Values: 197 groups (was 23). Coverage: 438 of 754 group occurrences have a value (58%), 193 are marker groups (26%), 123 are unread (16%).
- Order check: sorted by rank, the 197 readings are in alphabetical order with 1 inversion (5511 messieurs before 5512 ?mesures); a random assignment gives 98 on average
  (minimum 83 in 2,000 shuffles). CAVEAT: the values were proposed knowing roughly where each group sits, so this test is partly circular; it shows the readings are
  mutually consistent at line level, not that each is right. Three first guesses failed it and were withdrawn (1516 combattre, 7126 preciser, 5825 mon).
- Independent support comes from pieces that recur in different words: 0503 air (l'air d' / circul-air-e), 0607 an (Je-an / an-gl..), 4009 ger (Saint-Ger-main twice),
  2011 cot (cot-e / cot-on), 5006 le (col-le, fil-le, le-t-h-ar-gi-e, article), 2703 donner (pour donner / etant donnees), 6129 on (pigeons, ballon, coton), 1216 car and
  6816 pi (Pi-car-d twice), 2112 d (Picard, Herold, d'y), 7508 pru (Prussien twice), 8328 s, 3316 er, 0814 au (Rousse-au, Pont-Au-demer, au).
- Names and places read: rue Jean-Jacques Rousseau (the Paris post office), Picard, Saint-Germain-en-Laye, Pont-Audemer, Prussiens, Madame Herold (H?-RO-L-D),
  Jules [Fa]vre (needs 0617 to be a slip for 3617; not checked on the scan), Trochu. Content: Steenackers tells his Paris colleagues what line to take towards the post
  office (services rendered, the capital not cut off, balloon and pigeon post, the pigeon service to be extended to private messages, the decree uniting posts and
  telegraphs, the decree ending the post's monopoly on carrying newspapers), a report of 20 Prussians leaving Saint-Germain daily with pickaxes, advice on coating
  cotton balloons with strong glue, then a paragraph of personal news for each of the three addressees.
- Digit slips assumed (written -> meant), all 3/5, 0/6 or 5/8 type: 8312->8512 (se, in Rousseau), 3304->5504 (mer, Pont-Audemer), 3227->5227 (main), 0816->6816 (Picard),
  1017->1617 (colle), 6519->6819, 2534->2514, 5005->5006, 3121->5121, 0129->6129, 6180->6120. To check on the scan.
- Pillon's items after this pass: 5121 in ballon is not L (l = 4914); it sorts between lie 5102 and lui 5209 (ll or lo). VIN-OY: 6124 sorts below on, so "oi" (phonetic)
  is possible, still unconfirmed. DUC-ROT: 7802 = re (relie, renseignement), so 2722 7802 is D..-RE, not Ducrot; it also follows a first name ("votre ami [0312 9516] [2722 7802]").
  Third addressee 5006 9701 2729 = LE-V..-E. The "prefet" idea for 6819 3412 stays dropped.
- Second pass (13 Nov, same day): 233 values, 475 of 754 occurrences (63%), 193 markers, 86 unread; 0 inversions among the 233 (the earlier one was 7119/7208, now pour / pouvoir).
  New: chemins de fer (1422 3716; "desorganisation des chemins de fer due a la guerre"), FER-RY + il (3716 8327 4314), retabli, developpons, ici, "a l'Officiel si c'est possible" (8625 si),
  enleve, causant, unique, repartir, MEL-ASSE (colle forte et melasse), nomme, SECRET-AR-I-AT general, "il ne sera plus transmis aucune depeche" (9411 0815 2319), mere, TANT-E, HE-RO-L-D,
  LEG-O-F (Le Goff?), "mille remerciements a tous trois" (three addressees again), "votre toujours devoue", RIC-ARD, EV-EIL, etudiant. 2722 7802 = DUP?/DUC?-RE (Dupre?) open.
  Still unread, by type: names (third addressee LE-V..-E, the Nantes and Rennes names, 0402 4712, 1002 5825 9924 T, 7708 5825 9511 D, 3920 8914 3005 5824, 0312 9516, the place 9620 3328 3824,
  prefect of 0903 2719); single words with several candidates (7126, 1516, 3921, 3601, 3604, 4423, 0703, 3408 2809, 3215, 6808, 6005 9029, 4125, 0702, 0420, 0421, 6301, 0530, 3019, 3021, 2704,
  5413 6421, 8122, 2329, 2705, 8517 5024, 5308, 1027, 4515, 5215 9010, 3927, 8319, 7122 3030 1502, 6714 4905); the marker groups.
- Third pass (13 Nov): 236 values, no inversion. Occurrences: 485 of 754 valued (64%), 172 marker groups with a working function (23%; functions listed under "_markers" in
  anchors_inspecteurs.json: brackets, paragraph end, plural, participles, imperfect, adjective and noun endings; 0113 = a / à in all 8 uses), 97 unread (13%, 86 distinct groups).
  Correction of sense: "... et a M. [1114 5911 0131], AIDE DE CAMP (0423, 1206) au general Trochu, que Madame [same name] est en bonne sante a Rennes": the Rennes news is for an
  aide-de-camp of Trochu, not for Trochu. The name fits BRU-NE-T (guess; a web search did not confirm a Brunet on Trochu's staff). 1027 = bonnes ("vos bonnes communications").
  Withdrawn: 3604 = excavation (the clear word before it is "la", so the entry starts with a consonant; f.. such as fable is possible, which would put the start of F before 3604).
  Candidates noted but not adopted: 6005 9029 0312 = notaire/notable + surintend-ant; 4423 = inertie/incurie; 8122 = reste; 4519 = installee; 2329/2705 = second forms of depeche/donner.
- Correction from the claims review (13 Nov): the slips are THIRTEEN written groups, 16 occurrences (the eleven listed above plus 4913 and 4915 for 4914); not all are 3/5, 0/6 or 5/8 (2534 is 3/1, 6180 8/2, 5005 5/6).
  The single inversion of the first pass was 7119/7208 (not 5511/5512). The transcription file has 754 groups, 349 distinct, 0101 52 times, and no four-digit number in clear; 736/343/49 was the 7 Nov count.
  PRU-S-SIE-N occurs once; the second run is PRU-S-[8626], 8626 unread. 3927 = garde is used in 'mettre en garde' only; in L-[3927]-E it is unread.
- Slip test and adjacent-form test (13 Nov, after publication; no outside source used). For each unread group every one-digit change that gives a known group was listed
  and judged in its sentence. Adopted as ASSUMED slips: 8319 -> 2319 ("restreint aux depeches officielles"; the next group 6180 -> 6120 has the same 8/2 confusion),
  3019 -> 5019 ("on les a vus se diriger"), 3021 -> 5021 ("que ses lettres par ballon monte arrivent bien"), 8626 -> 8628 (PRU-S-SIE). From the book order: 9010, one line
  before succes 9011, = succeder, 5215 = m ("charge de me succeder"). Not adopted: 5308 -> 5508 (mere; maison also fits unslipped), 2329 / 2705 as second forms of depeche /
  donner, 2704 (dont / donnee), 6005 between nos and notre (notaire / notable), 4125 after hardi, 8517 before secret. No fit: about 150 other one-digit neighbours.
  Now: 238 values, no inversion; 491 of 754 valued (65%), 172 markers (23%), 91 unread (12%, 80 distinct); SEVENTEEN assumed slips, 20 occurrences, none checked on the scan.
- Strict count (13 Nov, figure of record; README read bar: guessed, assumed or restored values are holes; `python3 -I coverage.py`): 469 of 754 valued as written (62.2%),
  172 markers (22.8%, counted apart), 113 holes (15.0%) = 89 groups unread as written + the 20 assumed-slip occurrences + 4 occurrences these notes call a guess or unread
  (5219 mademoiselle "guess only"; 9802 vin x2, which exists only as the unsupported VIN-OY, and Remaining gaps lists 9802 6124 as an unread name; 3927 in L-[3927]-E).
  Rule: a value counts when the group as written has it in anchors_inspecteurs.json and these notes do not call that value a guess or that occurrence unread. Values marked
  "hypothesis" with a stated position test (5218 madame, 0919 bal in BAL-L-ON) stay counted, as do 9010 succeder and 5215 m (adopted from the book order). The 491 / 65% above
  is the looser count with the assumed slips.
- Automatic ranking test (13 Nov): for 38 unread groups with known neighbours on both sides, every word in the book interval (wordfreq, 30,000 words) was scored in its
  sentence with the fr-modern character model (order 5, with spaces) plus word frequency and position. Result: negative. The top choices are frequent words with no sense in
  place (pourquoi, longtemps, france, influence); the intended word, where one is guessed, is rarely first (mesures and claire are; dont is). A character model cannot choose
  a word; a word-level model of 1870 administrative French would be needed. Nothing adopted.
- NOT a reading by the README bar (95% of tokens): this is "read in part", from one transcription, with no second text in this code to test the values on.

## Pillon's reply of 14 Nov 2026 (marker groups; relayed by Dan)
He asked for all partial decryptions (he found the Full texts section of the page, which holds ciphertext and gloss; the sentence reading is inspecteurs_2nov_reading.md), and read the markers as R1-style tags.
Tested against the contexts (inspecteurs_2nov_gloss.txt): 0312 -ant, 0212 adjective (revolution -> revolutionnaire), 0307 imperfect: agree. 0305 = FUTURE: adopted ("celui qui [etre] 0305 charge de" = sera charge;
the single occurrence fits future or conditional, not the imperfect we had). 6221 = ORGANISER with its conjugations and ORGANISATION: supported, it is a verb in "c'est nous qui avons organise le systeme" and a noun in
"4914 6221 etablie" (l'organisation etablie). 4914 = le/la/l' compatible (first entry of L); 0814 = au/a la/aux compatible. 0211 = FEMININE: not settled. "communication 0211 qui relie" (singular verb) favours feminine;
"enfant 0211" and "ami 0211 0109" (amie or amities) fit either feminine or plural; kept as unsettled. 3921 = HAUTEUR: rejected by position, the H section opens at 4113 (h, habit 4116, hardi 4124) and 3921 lies just
before garde 3927 (G); "a la hauteur des circonstances" is the idiom but 3921 would have to be a slip. PIERRET from Gemini: no independent evidence (it repeats his own PIERR-ET reading); source asked for.
Gemini's other candidates to be run against the spelled runs only if he names sources.

## Wiki and engine (7 Nov 2026): start here
`wiki/` is the project's knowledge tree, built on Karpathy's LLM-wiki pattern (gist 442a6bf5..., raw sources / wiki / schema; ingest, query, lint; index.md and log.md): read `wiki/SCHEMA.md`, `wiki/PROCESS.md`, `wiki/index.md`
and `wiki/syntheses/Z01.md` (overview and ranked next steps) before anything else; `wiki/log.md` has the history including two rolled-back false acceptances. Machine state: `wiki/lexicon_inspectors.json`, `wiki/lexicon_favre.json`.
Tools (run from this folder): `python wiki/tools/lint.py` (must print result: clean), `python wiki/tools/build_index.py`, `python wiki/tools/engine.py calibrate|loop`.
Result of the rebuilt process: calibrated gate, 0 engine acceptances after the context-margin rule (355 units proposed), best near-misses recorded as hypothesis claims C100-C105. Earlier sections of this file are the chronological working notes the wiki was seeded from.

## Next
1. Chaudordy: accept the ~330-group reading as tentative; test whether the codebook entries from it recur in the other Favre letters
(cross-letter validation is independent of the print); ask Pillon whether the original dispatch (p. 2 scan, MessageChiffre_Chaudordy2.jpg)
has a different ending or interpolations.
2. Read the other pooled Favre letters with that codebook; look for the printed plaintext of Favre's letters of 28 Nov, 20-21 Dec,
19 and 26 Jan (Favre's book vols 1-2, Chaper report). 3. Check whether the code is alphabetical like R1. 4. Fetch the scans needed (2emeS-15, 31, 38) by range request.
5. profile.json once the work is more than a first pass.

## Second round, 8 Nov 2026 (summary for the write-up; scans and transcriptions published from 8 Nov, see below)
At the collector's request 12 untranscribed page scans (about 14,000 groups) were transcribed by reading them with Claude; the R1/R2/R3 contents stay outside the repo and are his unpublished work; the page names counts and percentages, never tables. Update 8 Nov 2026 (later): the collector agreed that his scans and the transcriptions of them are published; the AI transcriptions (workbook and per-page texts), six snips and his transcription files are now on the site / in this folder (DATA_NOT_INCLUDED.md); repertoires, Excel files, R2 gap table and the zip stay unpublished.
- Pilot on one hand-typed telegram: 271/283 groups exact (95.8%), misses all one digit (3/8, 1/2, 9/0), 8 of 12 flagged. Re-reads: four spots unreadable
  (one Favre block on the 23 Oct page, top 14 lines of one page, lower part of one small block, one blurry block); one page unreadable.
- Codes: R1 (24 Oct Gambetta-Favre, coverage 94%, z=18.8; Steenackers-Trochu blocks of 23 Oct, coverage 80-90%, cosine 0.83-0.90); R2 (13 Nov Tours telegram,
  coverage 89%, z=4.1; printed in Enquete parlementaire, Depeches telegraphiques officielles II pp. 302-304, Favre II pp. 108-110); Favre/delegation code
  (8, 10, 19 Nov, 5 Dec, 23 Oct Favre block; cosine 0.53-0.75; 701119 = 0.62); 7 Dec table third block unplaced. R2 vs Favre not separable by cosine (0.45).
- R2 gap alignment: twelve new R2 entries sent to the collector (not listed here); two transcription slips of ours found.
- Favre code doubled pool (17,658 positions): 628/1792, 620/1915, 1908/1915 replicate on the new half; 310/1915 passes; 1440 fails; date profile null;
  Chao1 about 2,200 (corrects "larger than 2,300"). No word values.
- Printed-text search: no match except 13 Nov; 7 Dec table probably Chaudordy's dispatch of 7 Dec (Favre II p. 255); Quai d'Orsay papers not checked.
- Corrections: old overlap figure 87-95% wrong (mixed pool); 701119 is Favre family; 701023 block 2 is R1; a seven-group run read on 2emeS-2 does not exist.
- Open requests to the collector: beacon pairs, recipients 6819 3412 (P...-ET, Pierret?) and 5006 9701 2729, Nantes/Rennes names, other ciphertext, rescans of the four weak spots.

## Remaining gaps
- names and places (third addressee LE-V..-E, first addressee P..-ET, 9802 6124 at Nantes, the aide-de-camp 1114 5911 0131, 0402 4712, 1002 5825 9924 T, 7708 5825 9511 D, 3920 8914 3005 5824, 0312 9516 / 2722 7802, place 9620 3328 3824, prefecture 0903 2719) - blocker: no-key-material; spelled once or twice, no second text in this code, no source naming them found
- about 30 single groups with several candidates (list in the third-pass note above) - blocker: no-key-material; each occurs once or twice, so no second use of the group exists to test a candidate on, no second text in this code, and no 1870 administrative-French word model in lang/ to choose between the words that fit the interval (retried 14 Nov: 3921 hauteur rejected by position)
- seventeen assumed digit slips (20 occurrences, counted as holes) and the doubtful 0617 - blocker: needs-physical-access; the full scan is with the collector and on the owner's machine, not in the repository
- exact meaning of the marker groups on pages 01-03 and 05 - blocker: no-key-material; working functions only

## Escalation
- [x] siblings: the collection's other pages were sorted on 8 Nov (R1, R2, Favre/delegation code); none is in the inspectors' code
- [x] clear-pages: the clear words inside the telegram are the adjacent plaintext used; no separate clear copy exists in the collection
- [x] known-keys: R1 tested on 7 Nov (18% of groups in its table, 10% by chance, no sense): not the inspectors' table
- [x] print: Steenackers 1883 (HathiTrust), Dagron, the 1872 Bulletin article searched on 7 Nov; the telegram is not printed there; web searches of 13 Nov for Pierret and for Trochu's aides-de-camp found nothing
- [x] key-rebuild: alphabetical bracketing of the paged book (interval_cands.py), three passes on 13 Nov, 23 to 236 values
- [x] retry: every unread group listed again with the tightened intervals in the third pass; candidates recorded, none adopted without a second support; retried again on 14 Nov against Pillon's suggestions (0305 settled, 3921 rejected, 0211 unsettled)
