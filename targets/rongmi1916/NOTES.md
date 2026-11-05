# 容密 (Rongmi), 14 numeric telegrams of June-July 1916 (Huang Xing's circle, Tokyo <-> Shanghai), JACAR

Status: read (Brice Dudout, Wenmi, published 19 Oct 2026; 14 telegrams, 1306 cipher groups: 1198 certain, 55 probable, 48 unresolved, 6 illegible; 95.9% read as sense).

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site: https://bdudout.github.io/wenmi/en/rongmi.html (key, telegrams,
translations), with the article https://bdudout.github.io/wenmi/en/juin1916.html and the method page
https://bdudout.github.io/wenmi/en/method.html. **The reading of the key as a renumbered 明密 code book is Satoshi
Tomokiyo's** (Cryptiana, https://cryptiana.web.fc2.com/code/chinesecrypto_e2.htm; see key.md and the dating note below).

## Relation to `targets/numeric1916` (retired 5 Nov 2026)

These telegrams were first in `targets/numeric1916`, which held the three codes 共密, 容密 and 辰密 under one target
against the "one key, one entry" rule. Brice Dudout's pull request #266 proposed this split; it is landed on 5 Nov 2026
on Dan Bourdeau's condition that `numeric1916` be retired in the same change, and `numeric1916` is now `Status: no write-up`: its page
`docs/numeric1916.html` is a stub pointing to `rongmi1916`, `chenmi1916` and `gongmi1916`, its README and
SOLVED_CATALOGUE rows are replaced by one row per key, and its profile is kept as
`targets/numeric1916/profile.pre-split.json` outside the paper data (the three new profiles carry the telegrams).
The folder stays as the archive of the independent check (20 Oct 2026: `decode.py` reproduces every group of the published
raw texts, `verify.py` and the key searches rerun) and of the b21 re-read of 23 Oct 2026; both are carried into this folder's
profile as verification steps. N01 (Gaimusho tables) and N09 乾密 (`numeric1916/dudout/`) are other keys and are not part of this target.

What this folder adds to the pull request's texts: nothing of the independent check is repeated; where the b21 re-read
differed from the Wenmi edition it is noted under Counts or Remaining gaps.

## Dating and credit (checked 5 Nov 2026)

Dan Bourdeau's condition for accepting the split of `numeric1916` was that Brice Dudout's recovery of the keys be checked
against Satoshi Tomokiyo's publication of the same material, so that this project claims no priority it does not have.

- **Cryptiana** (https://cryptiana.web.fc2.com/code/chinesecrypto_e2.htm, "Mingmi (明密) Format Code: Gongmi (共密), Rongmi (容密), Chenmi (辰密)"), fetched 5 Nov 2026:
  "First posted on 18 September 2026. Last modified on 24 October 2026." The section carries no date of its own;
  the 23 Oct 2026 date comes from Wenmi, which cites it (Wenmi commit 32c6b9f, 22 Oct 2026 21:59 UTC, "Cryptiana,
  23/10/2026"; the Wenmi pages say "Cryptiana, 23 October 2026"). The Wayback Machine holds one capture of the page,
  2 Oct 2026, before the section. So the earliest date of Tomokiyo's section cannot be fixed from his page, and it
  is not needed: **the section itself credits the keys to Dudout** ("Brice Dudout continues to discover new keys";
  "The formula found by Dudout" for 共密 and 容密; for 辰密 "Dudout describes a coordinate system ... He discovered
  the pages are numbered backwards"). What it adds, and what Wenmi credits him for, is the reading of the three keys as
  one renumbered 明密 code book (pages, columns and rows rewritten by hand).
- **Dudout's public record** (GitHub API commit dates of github.com/bdudout/wenmi, UTC): partial 共密 edition and key
  C51, 17 Oct 2026 21:35 (012829e); 容密 key and eleven telegrams, 19 Oct 10:11 (20f26a7); 辰密 page, key and four
  telegrams, 19 Oct 15:15 (37853ad); the June 1916 article, 19 Oct 12:51 (3636ba8); the independent-control tools
  `solver/numeric1916`, 19 Oct 17:04 (b5439a7); the renumbered-book block credited to Tomokiyo, 22 Oct 21:59
  (32c6b9f). In this repository his email of 19 Oct 2026 is recorded in `targets/numeric1916/NOTES.md` and the folder
  was first committed on 20 Oct 2026 (f0ceee851d).
- **Finding.** The three keys were recovered and published, as formulas, three to six days before the Cryptiana
  section is dated, and the section credits them to Dudout. The earliest public date for his 共密 key is 17 Oct, not
  19-20 Oct (19 Oct is 容密 and 辰密; 20 Oct is the date of the check made here). Commit dates are the committer's
  clock and can be set by the author, but the email of 19 Oct and the 20 Oct commit here agree with them. Nothing
  found contradicts Dudout's priority for the keys, and nothing gives this project any: the check made here is
  an independent decoder run on his digits.
- **Credit recorded.** Dudout: key recovered ciphertext-only (outcome.method), digits, readings. Tomokiyo:
  `identification` (the renumbered 明密 book model), dated 2026-10-23 as cited by Wenmi with the Cryptiana page
  showing 24 Oct as its last modification. Tomokiyo is also credited `key corrected` for the page-80 numbering (89, where the formula gives 99);
  the swap 8012 -> 8102 in N25 itself is credited by Cryptiana to Dudout ("Dudout found that 8012 is an enciphering
  error for 8102") and by Wenmi to Tomokiyo's observation that 8012 reads in neither version, so the two accounts
  differ and both names are kept.

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
