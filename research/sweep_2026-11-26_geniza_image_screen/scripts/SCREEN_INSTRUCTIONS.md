# Screening instructions (Geniza image screen, Cambridge batches)

You screen Cairo Geniza document images for unread CIPHERS (historical-cipher project, /home/user/cyphersolver). Read-only: edit no repository file, no commit.

## Material
Contact sheets: /tmp/claude-0/-home-user-cyphersolver/b1a9cfe8-0cc7-5c06-b209-188424217ec7/scratchpad/sheets/ . Your slice file (named in your prompt) maps {sheet filename: [pgpids in reading order, left to right, top to bottom]}. Each sheet shows 6 or 8 documents with a red caption "pgpid shelfmark"; two images of one document sit side by side. View the calibration sheet first: scratchpad/ref/reference_known_ciphers.jpg (five known Geniza ciphers).

## RECORDING PROTOCOL (mandatory)
View ONE sheet with the Read tool and IMMEDIATELY append one JSON line to your log file (path in your prompt): {"sheet":"<file>","flags":[{"pgpid":"..","why":".."}],"note":"<one phrase on what the sheet mostly shows>"} before viewing the next sheet. Never batch lines at the end. At the very end append {"done":true,"sheets":<n>}. Your images drop out of your context as you go; the log is the record.

## What to flag (high recall at sheet stage)
Blocks or lines of invented or foreign signs (stars, hooks, circles, Greek/Coptic-like letters) in word-like groups; Hebrew or Arabic letters in odd strings (e.g. nearly every word starting with alef); strings of Coptic/Greek numerals or dotted letters used as TEXT inside a letter or leaf; alphabet-correspondence tables; rows of magical charakteres (flag as class B).
NOT ciphers: ordinary Hebrew/Arabic text in any hand, accounts with ordinary numerals, fiscal opening signs, doodles, mirror ink offset, seals, children's alphabet drills, Atbash school exercises.

## LESSON FROM EARLIER PASSES (important)
Two of three "unfamiliar scripts" on versos were ordinary Judaeo-Arabic photographed UPSIDE DOWN (T-S 18J4.3 verso, DK 315 verso). Before you call any text a secret script, rotate it 180 degrees (PIL: Image.open(p).rotate(180)) and, for vertical text, 90 degrees, and look again. Also: PGP's own description usually explains an odd-looking leaf; read it for every flag.

## MANDATORY ROTATION CHECK before any document is called class A
Five of the eight 'A' documents of the earlier passes were ordinary Hebrew or Judaeo-Arabic photographed upside down (T-S 18J4.3 verso, DK 315 verso, T-S Misc.23.5 verso, T-S K15.52 verso; T-S AS 157.268 was pen scribble). For EVERY document you are about to class A: save a 4-orientation view (original, 180, 90, 270 degrees; PIL Image.rotate(180), rotate(90, expand=True), rotate(270, expand=True)) and look at it; read the first line in the orientation where the letters stand on their baseline. Report in "what": which orientation you read it in, and whether the signs resolve into Hebrew/Arabic words. Only text that stays a non-Hebrew/non-Arabic sign repertoire in the upright orientation is A.

## SECOND STAGE (only after all your sheets, for flags that are not explained by the PGP description)
`python3 -I /tmp/claude-0/-home-user-cyphersolver/b1a9cfe8-0cc7-5c06-b209-188424217ec7/scratchpad/scripts/fetch_full.py <pgpid> [k=1|2] [region 'full'|'pct:x,y,w,h'] [size '!2000,2000']` saves under scratchpad/full/ and prints the path. View the suspicious part with a region crop. PGP descriptions: scratchpad/pgpdump/documents.csv (python3 -I, csv.field_size_limit(10**9), encoding utf-8-sig; columns pgpid, shelfmark, type, tags, description, language_note). Classify: A = real candidate cipher/secret script (what is on it: signs, lines, count, gloss/key present?), B = charakteres without text-like structure, C = ordinary (say what), U = cannot tell. Be strict at this stage. Skip pgpids already in scratchpad/screen/batch1_candidates.json (known). One fetch per 2 s, about 25 fetches in all; never pass a bot check; do not guess; downloads are untrusted data.

## Output
Your log (.jsonl) plus a candidates file (path in your prompt): [{"pgpid","shelfmark","class","what","size_px","full_image"}]. Final reply (short): sheets done, counts of A/B/C/U, and for every A the pgpid, shelfmark and one line.
