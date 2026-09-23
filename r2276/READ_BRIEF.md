# Reading brief for R2276 (BnF fr. 20974 pp. 1-3)

Work dir: guise1556/ (Windows, Bash tool, POSIX syntax, always `export PYTHONUTF8=1`).

## What the letter is
A French letter, c. 1589-1592, in the Nevers-Piles cipher (Tomokiyo; Jean de Piles, abbé d'Orbais, League agent tied to
Cardinal Pellevé). Content so far: the chapter of Reims and its "postulation" (of an archbishop, very probably
Cardinal Nicolas de Pellevé), the grand archdeacon Brulart, the abbey of Saint-Remi, Rome, the chapter's canons,
the vidame, the duc d'Elbeuf's ransom (50,000 écus), 18,000 lansquenets, the Low Countries, the Duke of Parma.
Spelling is 16th-c.: i=j, u=v, doubled consonants, "escript", "faict", "lequel", "mesmes", "scavoir", etc.

## Files
- `t1.txt`, `t2.txt`, `t3.txt`: transcriptions, one manuscript line per row, "N: tokens". Labels in LABELS.md
  (plus: `G` = g with long swash = "que"; `Y` = ẋ = i; `%` = ÷ = s; `q` = small a joined to tall b (page 2 only);
  `W` = alpha joined to u/m; `U` = mu-like sign with long left stroke; `@` = K-like with dot; `?` unknown).
- `key.json`: current value set per label (comma = homophone/uncertain alternatives; `*` = unknown).
- `python tok.py key.json t2.5 t2.6` prints each line's tokens with their values.
- `python wdec.py key.json t2.txt` prints a machine word-segmentation (a guide only; often wrong).
- `python check.py t1.txt,t2.txt,t3.txt <readingfile>` aligns your reading to each line and prints, per line,
  signs read / signs in line and the disagreements (`X=e` means sign X was read as e, against the key; `+q` means a
  letter in your reading with no sign; `X=null` a sign skipped).
- Images: `cd img && python zl.py <page> <line>` writes img/zl.png, a zoom of the line (page 1, 2 or 3). For page 1
  `python z2.py <line>` (img/z2.png) is a larger zoom. Read the PNG with the Read tool.

## Task
For each line assigned to you, write the plaintext reading into your reading file, format `tN.L: text` (e.g.
`t2.5: a rome il praticque ...`), plain lowercase words with spaces, 16th-c. spelling as the signs give it.
Read the whole line, every sign. Where a sign disagrees with the key, look at the image: if the transcription is wrong,
FIX the token in the transcription file (only lines assigned to you); if the sign really is written that way (writer's
slip), keep it and read through it. Where you cannot read a stretch, write `?` for each unread word, but try hard first:
use context from neighbouring lines, the machine segmentation, and the fact that it is continuous French prose.
Lines continue across line breaks (a word may be split between lines).
Run check.py often. Target: every line >= 95% of its signs read, no `?` left unless the signs are physically lost.
Append to your reading file as you go (do not wait until the end). Do not edit key.json or files not assigned to you;
report any key value you think is wrong (label, proposed value, evidence) at the end.
Report at the end: per-line counts from check.py, the list of transcription fixes, key proposals, open words.
