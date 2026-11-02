# "L'Estat du Roy de Navarre et de son party en France", fols. 264r-264v: cipher passages read (Brice Dudout, 29 Oct 2026)

Status: read in part (fols. 264r-264v read, 635 of 666 cipher words in their sense, 95.3%; fols. 263r-263v not re-read; code numbers not read).

Write-up: https://bdudout.github.io/europe-chiffree/en/documents.html#navarre-1583 (local, to be pushed when the GitHub account is restored)

## What this adds

Daniel's key (`../key.json`) is applied **unchanged**. What changes is the transcription of fols. 264r and 264v, re-read sign by sign
on the higher-resolution images of DECODE R8010 (https://de-crypt.org/decrypt-web/RecordsView/8010; P3 = 264r, P4 = 264v; duplicate of DECODE R8505, https://de-crypt.org/decrypt-web/RecordsView/8505), and the reading:
the cipher passages of both folios now read as French sentences.

## Held-out check

The key is Daniel Bourdeau’s (about 50 signs plus the dot groups), applied unchanged. Before reading with it, we tested it on two lines that nobody had yet transcribed: the end of fol. 264v, missing from the working transcription. We transcribed them from the image and froze the copy (SHA-256 hash) before any decipherment. The criterion was fixed in advance: at least 85% of the characters must form French words, and the key must beat 200 control keys with permuted letters. Result, in a single measurement: 0.886, against at best 0.737 for the controls. So it ranks 1st of 201. The difficult lines of fol. 264v were then re-transcribed sign by sign from the image, and the copy frozen before decipherment. This re-reading was not blind: the earlier decoding was known. Every doubtful sign was marked, and any word that depends on one counts as probable. The count follows Daniel Bourdeau’s rule. Details: `validation.md`.

## Reading

666 cipher words on fols. 264r-264v (code numbers not counted): 635 read in their sense (95.3%) under Daniel Bourdeau's 95% rule: 533 certain (80.0%), 96 probable (14.4%), 6 restored (0.9%), 31 unresolved (4.7%). f. 264r alone: 263 words, 97.0%; f. 264v alone: 403 words, 94.3%.

- Date (hypothesis). “Ce faict d’Anuers” (264v) very probably means the “French Fury”, Francis of Anjou’s failed coup on Antwerp on 17 January 1583; the text also speaks of Monsieur as alive and unmarried (before June 1584), of Épernon and Joyeuse, and of an Italian engineer at Lisbon (after 1581). Hence c. 1583, rather than the 1580 of the catalogue title. The setting may be Ségur-Pardaillan’s missions to England and Germany (1583–1584); this is not verified.
- “The Queen”. The reproaches of 264v (“she has not spent a penny on them” since 1570; “money lent in 1576”) probably aim at Elizabeth I, whose 1576 loan paid for John Casimir’s army. That is precisely the part the author put in cipher. A reading hypothesis, not checked in the English papers.
- The code numbers (6, 21, 36, 51, 57, 72, 81, 99, 721) are not read. 81 = the King (Henry III), 21 = Monsieur, 51 = the King of Navarre have been suggested, but these values are not established.
- What the re-reading changed. The working transcription confused neighbouring signs: closed o and open cup (n / i), plain and barred loop (n / u), lunate ε and two-bowled ε (a / s), barred ε and delta (t / a), X and hourglass (l / p). It also filed several different signs under one name (a lying ⊣ = c, a ⅃ = c, a rounded U = h, a mere lead-in stroke). On 264v a line given to the foot of the page was in fact the rising end of the next line (“d’aliances”): it is counted once. An isolated dot attached to the ʃ (“qu’ele”, “esté”, “tenoit”, “traiter”) is read as a mark, not as m: “tenoit” and “traiter” count as probable; for “qu’ele” and “esté” the blind re-reading (next note) confirmed the mark.
- Targeted blind re-reading. Twelve doubtful signs of 264v were shown to a reader (Brice Dudout) with no letter or value: he chose the shape he saw among certain shapes taken elsewhere in the letter. The effect of each answer had been fixed and hashed (SHA-256) before the answers, then applied as it stood. Six words move from probable to certain (“qu’ele”, “tant”, “esté”, “ofrir”, “seruice”, “denier”); two stay probable but read “laissee” and “traitee” (the last sign is e, not s: an unusual agreement); “recherchee”, “font” and “despende” stay probable (no clear choice); the first sign of ‹cissuada› is confirmed as c. No word became unresolved.
- Still unresolved: 31 words, including whole stretches in 3.10–3.12 (after “de Monsieur de”), 3.29–3.30 and 3.43–3.44 (‹dencor›, ‹baones›). ‹cissuada› would read “dissuada” if its first sign were d; it is c in the key, and a restoration never overrides a certain sign.

Files: `transcription_f264r.txt`, `transcription_f264v.txt`, `decryption.txt`, `reading.md`, `corrections.tsv`, `validation.md`.
No image is included (DECODE terms: research use only).
