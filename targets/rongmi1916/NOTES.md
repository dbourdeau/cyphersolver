# 容密 (Rongmi), 14 numeric telegrams of June-July 1916 (Huang Xing's circle, Tokyo <-> Shanghai), JACAR

Status: read (Brice Dudout, Wenmi, 19-20 Oct 2026; 14 telegrams, 1306 cipher groups: 1198 certain, 55 probable, 48 unresolved, 6 illegible; 95.9% read as sense).

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site: https://bdudout.github.io/wenmi/en/rongmi.html (key, telegrams,
translations), with the article https://bdudout.github.io/wenmi/en/juin1916.html and the method page
https://bdudout.github.io/wenmi/en/method.html. **The reading of the key as a renumbered 明密 code book is Satoshi
Tomokiyo's** (Cryptiana, 23 Oct 2026, https://cryptiana.web.fc2.com/code/chinesecrypto_e2.htm; see key.md).

## Relation to `targets/numeric1916`

These telegrams are already in `targets/numeric1916`, which holds the three codes 共密, 容密 and 辰密 under one target and
whose NOTES say: "these are three keys under one target, against the 'one key, one entry' rule ... Splitting into
gongmi1916 / rongmi1916 / chenmi1916 is the clean alternative". This folder is that split for 容密, proposed with its two
siblings (`chenmi1916`, `gongmi1916`) in one pull request. Nothing in `numeric1916` is changed: its independent check
(20 Oct 2026: `decode.py` reproduces every group of the published raw texts; `verify.py` and the key searches rerun) and
its re-read of 23 Oct 2026 (b21) stand and are not repeated here (the project's credit stays on numeric1916). If the split is accepted, the 容密
document of `numeric1916` can point here; if not, this folder can simply be dropped.

What this folder adds: the texts in the current state of the Wenmi edition (digits re-read by Brice Dudout, including
the vol. 4 telegrams), a standalone key file with S. Tomokiyo's renumbered-book tables, and the credits for that
reading of the key.

## The documents

Copies made by the Japanese police and Communications Bureau of telegrams sent or received by Huang Xing's household in
Tokyo (青山南町三ノ五三) and the Shanghai group, JACAR, Diplomatic Archives of the Ministry of Foreign Affairs of Japan,
series 1.6.1.4-2-1-2 "特定人ノ発受郵便物取調" (B03050089200, B03050089300, B03050089400, B03050089500, B03050089900). The forms carry no decipherment. Digits in kanji
numerals in a grid; every digit re-read blind by Brice Dudout on the scans (V4B: 4 of 22 sheets). No image is
reproduced here.

- N11 | 8 June 1916 | Tokyo → Shanghai | JACAR B03050089200, PDF pp. 51R, 51L, 52R, 52L, 53R (58 groups)
- N12 | 8 June 1916 | Tokyo → Shanghai | JACAR B03050089200, PDF pp. 53L, 54R, 54L, 55R, 55L, 56R, 56L (82 groups)
- N14 | 9 June 1916 | Tokyo → Shanghai | JACAR B03050089300, PDF pp. 7L, 8R, 8L, 9R (47 groups)
- N19b | 11 June 1916 | Tokyo → Shanghai | JACAR B03050089300, PDF pp. 27R, 27L, 28R, 28L, 29R, 29L, 30R, 30L, 31R, 31L, 32R, 32L (143 groups)
- N21 | 13 June 1916 | Shanghai → Tokyo | JACAR B03050089400, PDF pp. 6R, 6L, 7R, 7L, 8R, 8L, 9R, 9L, 10R (107 groups)
- N28 | 14 June 1916 | Tokyo → Shanghai | JACAR B03050089400, PDF pp. 32L, 33R (18 groups)
- N36 | 16 June 1916 | Shanghai → Tokyo | JACAR B03050089500, PDF pp. 6L, 7R, 7L, 8R, 8L (58 groups)
- V4B | 25 June 1916 ? | Shanghai → Tokyo | JACAR B03050089900, PDF pp. 7L, 8R, 8L, 9R, 9L, 10R, 10L, 11R, 11L, 12R, 12L, 13R, 13L, 14R, 14L, 15R, 15L, 16R, 16L, 17R, 17L, 18R (265 groups)
- N02 | June 1916 (day not read) | Tokyo → Shanghai | JACAR B03050089200, PDF pp. 7L, 8R, 8L, 9R, 9L, 10R, 10L, 11R (93 groups)
- N08 | June 1916 (day not read) | Tokyo → Shanghai | JACAR B03050089200, PDF pp. 47R, 47L, 48R, 48L (46 groups)
- N19a | June 1916 (day not read) | Tokyo → Shanghai | JACAR B03050089300, PDF pp. 26R, 26L (17 groups)
- N24 | June 1916 (day not read) | Shanghai → Tokyo | JACAR B03050089400, PDF pp. 15L, 16R, 16L, 17R, 17L, 18R, 18L, 19R, 19L, 20R, 20L, 21R, 21L, 22R, 22L, 23R, 23L (200 groups)
- N25 | June 1916 (day not read) | Shanghai → Tokyo | JACAR B03050089400, PDF pp. 24R, 24L, 25R, 25L, 26R, 26L, 27R, 27L, 28R, 28L (113 groups)
- V4D | June 1916 (day not read) | Shanghai → Tokyo | JACAR B03050089900, PDF pp. 54R, 54L, 55R, 55L, 56R (59 groups)

The first two groups of each form are a clear CTC prefix naming the code (1369 1378 = 容密). Hsueh Chun-tu's edition
of Huang Xing's drafts (黃興等電稿) records such a code name at the head of each telegram, one per correspondent, so the
prefixes are the names of code books issued to correspondents (Wenmi, "Les livres X密").

## The key

Full statement in `key.md` (formula, and S. Tomokiyo's renumbered-book tables). How it was found:

Recovered without cribs in October 2026: with only 90 first-sheet groups the search had too little text; once
about 590 groups of continuation sheets were read, annealing four per-place digit substitutions (the starting model
came from Codex trials) gave readable text; the anomaly 借甸 (3949) for 借款 (2949), off by exactly 1000 when the
hundreds made no carry, showed the additive. The exact key was computed on N02, N08, N11, N12, then read the other
telegrams without refitting (N14 ends 佳 = the 9th, as on its header); refitted on all re-read groups it returns the same
tables. The "90 = 00" rule was added afterwards from all groups beginning 90. The two vol. 4 telegrams (V4B, V4D) were
never used in the search and read unchanged.

Checks (Wenmi `solver/numeric1916/verify.py`): the key reproduces every published raw text from the digits; its
language-model score is far above random keys of the same form and above shuffled digits (figures rerun in
`targets/numeric1916/NOTES.md`, 20 Oct 2026).

## Correction from S. Tomokiyo's reading of the key

Written page 80 is the only cell where his renumbered book differs from the formula (89 against 99). The one group
concerned, 8012 in N25, read in neither case; the swap 8102 gives 一, so N25 now reads "又浙督已派吳兆蓮君赴日與公接洽，
一切到乞賜教" ({一} in reading.md; decryption.txt keeps the figure's value, 9911, marked doubtful). Credited to him as
"key corrected".

## Counts (Daniel's rule, from reading.md)

1198 certain, 55 probable ({x}), 48 unresolved (〔x〕), 6 illegible, of
1306 cipher groups: 95.9% read as sense. Status of the groups in decryption.txt: 1198 ok, 103 doubtful, 5 illegible.

## Remaining gaps

- 48 characters kept as 〔x〕 (decoded value not understood), mostly N36 and V4B - blocker: illegible; one-digit uncertainties on the police copies (一/二/三) or names, to be re-read on the scans
- 6 illegible groups (N12, N21, V4B) - blocker: illegible; digit unreadable on the copy
- V4B: 18 of 22 sheets not yet re-read blind; framing repairs in V4B and V4D still to be checked on the scans - blocker: needs-physical-access; better images or a re-read of the JACAR scans

## Files

- `transcription.txt`: the digit groups, one telegram per line (prefix left out).
- `decryption.txt`: group, CTC number, character, status, with dates, routes and JACAR sheets.
- `reading.md`: the punctuated Chinese reading; `translation.md`: English.
- `key.md`: the key (CC BY 4.0).

## Prior work

None known for these texts: they are not in Hsueh Chun-tu's edition of Huang Xing's 1916 drafts, which has nothing
between 8 and 20 June, nor found online (Wenmi, Juin 1916 article). 黃興集 and Li Yuanhong's correspondence not yet
checked. The key is a reconstruction: no historical copy of the 容密 book has been found.
