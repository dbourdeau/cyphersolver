Brief 2: clear text around every code number (Vienna -> Schenck letters, 1706)

Folder: C:/Users/dbour/cypher/.worktrees/sieniawski1708/targets/sieniawski1708/
Images: img/IMG_R<rec>_*.jpg (full resolution). Existing transcription: transcr/R<rec>.txt (the header says which
image is which page, in reading order). Decoded runs of the letter cipher: transcr/RUNS_FINAL.txt (key: a=7-9,
b=10-12 ... three numbers per letter, alphabetical, no j/v; 70=w, 76-78=y, 79=z).

Goal: the 3-digit code numbers (100-599) stand for persons, courts, places and things. To identify them we need the
German clear text around each one read as completely as possible. The first transcription left many [?].

For each letter in your share, produce transcr/CTX_R<rec>.txt containing, for EVERY sentence that holds a code
number (3-digit, or the small codes 83 / "3." / "2." / "5."), or a dotted letter sign (o., b., L., d., e., f., g., c.,
m., p., oo, ooo):
  [page:line] the whole sentence, re-read at full resolution (crop at native resolution, 2-3 lines per strip,
  enlarge 1.5-2x), with the cipher runs replaced by their decoding in {braces}, codes kept as numbers, dotted
  signs kept as written; [?] only where a word truly cannot be read; alternatives as word1|word2.
  then on the next line: "  codes: 187=? (subject of 'hat mir gesagt'; masculine; in Vienna) ..." - for each code
  in the sentence, the grammatical role and gender/number signals (der/die/das, Er/Sie/Ihro, "Ihro Mayt",
  "Königl.", "Hof", verbs in plural), and any small mark, letter or word written over or near it (another ink).
Also re-read the whole letter's clear text where it bears on who is who (persons named in clear, places, dates,
news), and update transcr/R<rec>.txt in place where you are sure of a better reading (append "(ctx: was ...)").

At the end of each letter's file add a short section "## people and things named in clear" listing every name,
title, place and event written in clear in that letter.

Write each letter's file as soon as that letter is done. Budget: up to ~45 crops. Do not touch git or files outside
transcr/ and img/crop/ (crop names prefixed "ctx_<rec>_"). Report at the end: per code, your best guess of what it
stands for with the evidence, and anything written over codes.
