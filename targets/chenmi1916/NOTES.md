# 辰密 (Chenmi), 4 numeric telegrams of June-July 1916 (Huang Xing's circle, Tokyo <-> Shanghai), JACAR

Status: read (Brice Dudout, Wenmi, 19-20 Oct 2026; 4 telegrams, 239 cipher groups: 232 certain, 7 probable, 0 unresolved; 100.0% read as sense).

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site: https://bdudout.github.io/wenmi/en/chenmi.html (key, telegrams,
translations), with the article https://bdudout.github.io/wenmi/en/juin1916.html and the method page
https://bdudout.github.io/wenmi/en/method.html. **The reading of the key as a renumbered 明密 code book is Satoshi
Tomokiyo's** (Cryptiana, 23 Oct 2026, https://cryptiana.web.fc2.com/code/chinesecrypto_e2.htm; see key.md).

## Relation to `targets/numeric1916`

These telegrams are already in `targets/numeric1916`, which holds the three codes 共密, 容密 and 辰密 under one target and
whose NOTES say: "these are three keys under one target, against the 'one key, one entry' rule ... Splitting into
gongmi1916 / rongmi1916 / chenmi1916 is the clean alternative". This folder is that split for 辰密, proposed with its two
siblings (`rongmi1916`, `gongmi1916`) in one pull request. Nothing in `numeric1916` is changed: its independent check
(20 Oct 2026: `decode.py` reproduces every group of the published raw texts; `verify.py` and the key searches rerun) and
its re-read of 23 Oct 2026 (b21) stand and are not repeated here (the project's credit stays on numeric1916). If the split is accepted, the 辰密
document of `numeric1916` can point here; if not, this folder can simply be dropped.

What this folder adds: the texts in the current state of the Wenmi edition (digits re-read by Brice Dudout, including
the vol. 4 telegrams), a standalone key file with S. Tomokiyo's renumbered-book tables, and the credits for that
reading of the key.

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
