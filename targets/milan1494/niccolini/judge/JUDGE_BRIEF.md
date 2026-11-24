# Strict judge brief
`decode_once.txt` holds a one-time decode of short cipher passages in four letters of Angelo Niccolini, Florentine envoy in Milan/Pavia, to Piero de' Medici (Aug 1492 - Jan 1493). Each row is one cipher RUN: doc, line.run, decoded letters, and a note with nearby clear words in [brackets] and the transcriber's remarks.
Decode conventions: {a|b} = the sign has two possible values (pick one only if the sense forces it); [22] = a code group (in this cipher 22 is a name code, value unknown to you: treat as N); _ = no value.

Task: segment each run into Italian words (15th-c. Tuscan spelling, abbreviations and run-on words normal) and tag every WORD UNIT:
- S = reads as a real word that fits the context, letter for letter (choosing one value of a {a|b} sign is allowed);
- E = a word is recognisable but needs letters changed, added or dropped (list the emendation);
- N = no word can be made of it (including code groups and _ holes).
Be strict: do not invent readings to rescue strings; a fragment that only makes sense with heavy emendation is E or N.
Write `judge.tsv` (doc, run, unit, decoded, reading, tag, note) and `JUDGE_NOTES.md` with per-doc counts S/E/N and strict share S/(S+E+N), plus a one-line gist per doc if one can be given. Work only in /tmp/nicc_judge. No web, no other files.
