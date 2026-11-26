# WORKLOG vaudreuil1759c (catalogue 1390)

5 Nov 2026.

- Split from `targets/vaudreuil1760/`: the 1757 table found for catalogue 1391 was tried on this letter (same office, 1759) and fits.
- Fetched the images from the LAC image server (curl -L; retry the requests that return nothing).
- Transcribed the whole letter (354 groups) into `transcription.txt`; decoded it into `decode.txt`; measured `ct.txt` with `docs/_check_profile.py --measure`.
- Doubtful cells met here: 0 group(s); 2 group(s) cut at the gutter. Cells settled on the four letters together: 452 fret, 301 trou, 133 oit, 367 crai, 195 vrai, 613 cas.
- Not done: reader review of the decode as sentences, English translation, the alphabetical key sheets for the doubtful cells, a clear copy.
- Reader review (5 Nov): fetched e000874976-77 and compared every line with the transcription. Corrected f.75r line 2: 393 -> 593 (the decode gave "l succès prochaine", the image gives "l'année prochaine"); distinct groups 130 -> 129. Wrote reading.md and reading_en.md.
- f.76r: 389 (m) and 488 (Iroquois) read as written on the image but the sense is "seront" and "d'elle-même" (309 se, 498 elle): kept as written, sense supplied. Cut groups restored: 337 loi, 271 r. Unread: f.75v 323 + s ("les [?] sont trop grands"); table cell 323 reads "pu", set "ju" on cat. 1391.
- Class changed from "not read" to "read" (99.4%); profile.json updated and valid. Not done: outside reader, write-up page, README row, DECODE queue.
