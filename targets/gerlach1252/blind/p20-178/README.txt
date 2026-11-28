gerlach1252 blind pass of the remaining cipher pages, pp.20-123 and 161-178 (27-28 Nov 2026): twelve batches D-O, each a
separate blind transcription, one mechanical decode with the frozen key and one strict judge. Batch P (pp.179-180) has no
cipher. pp.124-160 are not in this pass: they are on main already (blind/p124-137, blind/p138-150, blind/p141-160, the
last as batches A-C, which are not repeated here).

The checks were done with AI tools and no person checked each reading by hand.

BATCHES (by scan; page numbers as the blind reader wrote them, PACKET_INDEX.txt in each folder)
  D  scans 0023-0032  pp.20-29
  E  scans 0033-0042  pp.30-39            (p.39 has no cipher)
  F  scans 0043-0052  pp.40-49
  G  scans 0053-0062  pp.50-57, 68, 69    (the scribe's numbers jump from 57 to 68; no image is missing, the text runs on)
  H  scans 0063-0072  pp.70-79
  I  scans 0073-0082  pp.80-89
  J  scans 0083-0092  pp.90-99
  K  scans 0093-0102  pp.100, 100a, 102-109   (no p.101 in the scribe's numbering)
  L  scans 0103-0112  pp.110-119
  M  scans 0113-0116  pp.120-123
  N  scans 0164-0173  pp.161-170          (p.163 has no cipher)
  O  scans 0174-0183  pp.171-175, 174a, 175 (a second p.175), 176-178   (p.178: 8 cipher lines, then a prayer in clear script)
  P  scans 0184-0185  pp.179-180          clear German prayer and psalm text, no cipher; BLIND.tsv records that, nothing decoded
Scans 0117-0163 (pp.124-160) are the earlier passes on main. The scan-to-page rule changes at the second page sequence
148a-157a (blind/p141-160/README.txt), so pp.161-178 are scans 0164-0183.

WHAT EACH BATCH FOLDER HOLDS (images not committed: PACKET_INDEX.txt gives each IIIF URL with its md5 and sha256)
  packet/PROMPT.txt, packet/SHEET.md   all the blind reader was given, with the images. SHEET.md = ../p141-160/A/SHEET_v2.md
                                       byte for byte (sha256 775ea445...2e53a): sign labels and shapes, no letter values.
  FREEZE.txt                           sha256 of key_frozen.tsv, decode_once.py, shuffle.py, the packet files and the images,
                                       and of tools/after_blind.py, written before any transcription (frozen 27 Nov 2026,
                                       21:19-21:26 UTC; times are our record).
  BLIND.tsv, FREEZE_blind.txt          the blind transcription as handed over, frozen (sha256 + md5 + UTC time) before the decode.
  key_frozen.tsv                       = ../../key_v2.tsv byte for byte (sha256 b47062382f6c2a5139eae147385ec92e1a02d869e2eeafe1f0a711e29d668555).
  decode_once.py, decode_once.txt      one decode, no emendation (the script refuses a second run). Same script as A-C.
  judge/BRIEF.txt, judge/decode.txt    all the judge was given.
  judge/judge.tsv, judge/JUDGE_NOTES.txt  the judge's work (segmented text, S/E/N per line, per-page totals, recurring slips, gists).
  judge/RECOUNT.txt                    the judge's figures re-added by script (tools/after_judge.py): the figure of record.
  shuffle.py, shuffle_out.txt          5,000 key shuffles at each of seeds 20261112 and 7 (same script as A-C).
  reading.md                           the judge's text as German sentences with line numbers; each corrected slip is marked
                                       in place and listed under its page with the decoded form (see its header).
  translation.md                       English of reading.md, holes kept.

ORDER OF EVENTS, PER BATCH
  1. tools/make_batches.py builds the packet and writes FREEZE.txt (before any transcription).
  2. A blind reader (a separate Claude session, Opus, per the decisions log) gets only packet/PROMPT.txt, SHEET.md and the
     scans, and is told not to decipher. It writes BLIND.tsv.
  3. tools/after_blind.py re-checks FREEZE.txt, freezes BLIND.tsv (FREEZE_blind.txt), runs decode_once.py once, and writes
     judge/decode.txt and judge/BRIEF.txt.
  4. A strict judge (a further separate Claude session) gets only judge/BRIEF.txt and judge/decode.txt and writes judge.tsv and
     JUDGE_NOTES.txt: S = letter in a word that reads as sense, E = plausible one-letter slip, N = no sense.
  5. tools/after_judge.py re-adds the judge's figures (judge/RECOUNT.txt), applies our 65% line, and runs the shuffle control.
  6. After the figures: reading.md and translation.md, by further Claude sessions, from judge.tsv and JUDGE_NOTES.txt.
     The first pass stays the figure of record; the reading changes nothing in the counts.

RESULTS OF RECORD (judge/RECOUNT.txt; units = decoded letters plus unknown signs; strict = S/(S+E+N))
  D  pp.20-29          S 4469  E 130  N  41  of 4640  96.3%
  E  pp.30-39          S 3646  E  76  N  28  of 3750  97.2%
  F  pp.40-49          S 3937  E 420  N  79  of 4436  88.8%
  G  pp.50-57, 68-69   S 4484  E  65  N  31  of 4580  97.9%
  H  pp.70-79          S 4652  E 115  N   5  of 4772  97.5%
  I  pp.80-89          S 5643  E 186  N  51  of 5880  96.0%
  J  pp.90-99          S 6113  E  90  N  39  of 6242  97.9%
  K  pp.100-109        S 4589  E  86  N  11  of 4686  97.9%   (see RECOUNT NOTE 1)
  L  pp.110-119        S 4324  E  70  N  23  of 4417  97.9%
  M  pp.120-123        S 1857  E  62  N   5  of 1924  96.5%
  N  pp.161-170        S 3672  E 263  N 146  of 4081  90.0%
  O  pp.171-178        S 3833  E  98  N   2  of 3933  97.5%   (see RECOUNT NOTE 2)
  All                  S 51219 of 53341 = 96.0%  (assembled/SUMMARY.md)
Shuffle control: 0 of 5,000 shuffles at or above the real decode, at both seeds, in all twelve batches (pass = fewer than 5).
Best shuffle per batch -5.1366 to -6.1762 (mean log-prob per letter, lang model de-1500s, order 5); real decodes are in
each shuffle_out.txt (for example D -2.3602).

RECOUNT NOTES (found while filing, 28 Nov 2026; the figures of record are not changed)
  1. K: after_judge.py counts only rows whose line label is L01, L02 ...; the four margin lines of p.109 (M01-M04, 27 units:
     S 25, E 1, N 1) are in judge.tsv but not in RECOUNT.txt. With them K is 4614/4713 = 97.9%, the judge's own figure in
     JUDGE_NOTES.txt, and the whole pass 51244/53368 = 96.0%. RECOUNT.txt (4589/4686) stays the figure of record.
  2. O: the scribe numbered two pages 175. after_judge.py keys rows by page and line, so the two p.175 runs share keys and
     its row check reports "S+E+N != decode letters on 21 rows". That is the key clash, not a miscount: the totals sum every
     row, and a check by position (row n of judge.tsv against row n of judge/decode.txt) finds 0 differing rows in every batch,
     with judge units = decode letters (O 3933 = 3933).

TWO TOOLING NOTES (from the decisions log, 28 Nov 2026)
  1. FREEZE.txt header line. make_batches.py left out the first line "sha256: <key hash>  key_frozen.tsv" that decode_once.py
     needs. Batch D's first after_blind run froze BLIND.tsv and then stopped before any decode (FREEZE_blind_attempt1_nodecode.txt,
     21:37:55Z). The header line was added to FREEZE.txt of D-P at 21:38:07Z; the key file was not changed (its hash is the one
     already frozen, = key_v2), and BLIND.tsv has the same sha256 in both FREEZE_blind files. after_blind.py was then run once
     for D (FREEZE_blind.txt, 21:38:07Z) and once for each later batch. FREEZE.txt itself is not hashed anywhere; every hash
     in it still matches (checked again at filing).
  2. D's first shuffle run failed on "No module named 'lang'" before scoring anything (D/shuffle_out_attempt1_nolang.txt); the
     repository path in after_judge.py was changed to a clone with lang/ and the control run once. after_judge.py was also
     patched to skip pages with no cipher letters (E p.39, N p.163); so tools/after_judge.py here differs from the copy whose
     hash is in blind/p141-160. tools/after_blind.py is the file whose hash is in every FREEZE.txt here.
  Paths inside the tools are those of the working folder (/home/claude/gerlach_next), not of this repository.

SECOND READER (second_reader/)
  A blind second reader (a separate Claude session, Opus) transcribed four sample pages, pp.32, 82, 117 and 174 (scans 0035,
  0075, 0110, 0177), from the images and SHEET.md alone (packet/, FREEZE.txt). COMPARISON.md: sign agreement with the first
  readers 2 x 1792 / (1831 + 1843) = 0.976 (p.32 1.000, p.82 0.947, p.117 0.978, p.174 0.980). Both readers are model sessions
  of the same family, so this is not agreement with a human reader.

ASSEMBLED (assembled/)
  reading_p20-178_de.md, translation_p20-178_en.md: the twelve readings and translations in page order (v0.1, 28 Nov 2026);
  SUMMARY.md: the table above. The German and English are by Claude and are not checked by a person.

KEY SLIPS
  Each judge names recurring slips that look like one sign read the same wrong way throughout: q for w and d for z (D), r for z
  (E), r for u/v (F 300 of 420 E; M 32 of 62), f for long s and p for Latin q (H), g for d/de/k (I 104 of 186 E), l and g for k
  (J, K, O), c for r on a pale sign (N 126 of 263 E). Whether each is a key-table fault or blind-reader naming (as found for
  pp.124-137 on 16 Nov 2026, key_v2/EVIDENCE.md) has not been checked on the images. They are candidates for a key_v3, to be made
  only as a new frozen version and tested on fresh pages; key_v2 is not changed by this pass.

stamps/ holds an external timestamp of this folder (MANIFEST.sha256 with RFC 3161 and OpenTimestamps tokens).
