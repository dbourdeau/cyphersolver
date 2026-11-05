# 辰密 (Chenmi), 4 numeric telegrams of June-July 1916 (Huang Xing's circle, Tokyo <-> Shanghai), JACAR

Status: read (Brice Dudout, Wenmi, published 19 Oct 2026; 4 telegrams, 239 cipher groups: 232 certain, 7 probable, 0 unresolved; 100.0% read as sense).

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site: https://bdudout.github.io/wenmi/en/chenmi.html (key, telegrams,
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
  showing 24 Oct as its last modification.

## The documents

Copies made by the Japanese police and Communications Bureau of telegrams sent or received by Huang Xing's household in
Tokyo (青山南町三ノ五三) and the Shanghai group, JACAR, Diplomatic Archives of the Ministry of Foreign Affairs of Japan,
series 1.6.1.4-2-1-2 "特定人ノ発受郵便物取調" (B03050089200, B03050089300, B03050089400). The forms carry no decipherment. Digits in kanji
numerals in a grid; every digit re-read blind by Brice Dudout on the scans (V4B: 4 of 22 sheets). No image is
reproduced here.

- N05 | 3 June 1916 | Tokyo → Shanghai | JACAR B03050089200, PDF pp. 25R, 25L, 26R, 26L | no prefix (38 groups)
- N13 | 9 June 1916 | Tokyo → Shanghai | JACAR B03050089300, PDF pp. 3L, 4R, 4L, 5R, 5L, 6R, 6L, 7R (88 groups)
- N16 | 10 June 1916 | Tokyo → Shanghai | JACAR B03050089300, PDF pp. 11L, 12R, 12L, 13R, 13L, 14R, 14L, 15R, 15L (104 groups)
- N26 | 13 June 1916 ? | Tokyo → Shanghai | JACAR B03050089400, PDF pp. 31R (9 groups)

The first two groups of each form are a clear CTC prefix naming the code (6591 1378 = 辰密). Hsueh Chun-tu's edition
of Huang Xing's drafts (黃興等電稿) records such a code name at the head of each telegram, one per correspondent, so the
prefixes are the names of code books issued to correspondents (Wenmi, "Les livres X密").

## The key

Full statement in `key.md` (formula, and S. Tomokiyo's renumbered-book tables). How it was found:

Recovered without cribs in October 2026 after the Rongmi and Gongmi models failed: no 0 in the first two digits and
a concentration on a few pages suggested a reordered book. A "permuted page + permuted tens and units" model, fitted by
simulated annealing on N13, N16 and N26 (201 groups), gave readable text far above shuffled controls; the page table it
found followed the zero-free countdown, which was then imposed; two aberrant characters from groups ending in 9 (劈 for
力, 滠 for 灰) gave "9 = 10". N05, not used in the search and without prefix, then reads straight through (blind check),
and N16 ends with 灰, the code for the 10th, as on its header.

Checks (Wenmi `solver/numeric1916/verify.py`): the key reproduces every published raw text from the digits; its
language-model score is far above random keys of the same form and above shuffled digits (figures rerun in
`targets/numeric1916/NOTES.md`, 20 Oct 2026).

## Counts (Daniel's rule, from reading.md)

232 certain, 7 probable ({x}), 0 unresolved (〔x〕), of
239 cipher groups: 100.0% read as sense. Status of the groups in decryption.txt: 232 ok, 7 doubtful.

## Remaining gaps

- 7 characters read as probable (one-digit variants, 一不 for 不一, 盻 for 盼); nothing unresolved - blocker: illegible; single-digit uncertainties on the forms

## Files

- `transcription.txt`: the digit groups, one telegram per line (prefix left out).
- `decryption.txt`: group, CTC number, character, status, with dates, routes and JACAR sheets.
- `reading.md`: the punctuated Chinese reading; `translation.md`: English.
- `key.md`: the key (CC BY 4.0).

## Prior work

None known for these texts: they are not in Hsueh Chun-tu's edition of Huang Xing's 1916 drafts, which has nothing
between 8 and 20 June, nor found online (Wenmi, Juin 1916 article). 黃興集 and Li Yuanhong's correspondence not yet
checked. The key is a reconstruction: no historical copy of the 辰密 book has been found.
