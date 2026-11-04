# 共密 (Gongmi), 9 numeric telegrams of June-July 1916 (Huang Xing's circle, Tokyo <-> Shanghai), JACAR

Status: read in part (Brice Dudout, Wenmi, 17-20 Oct 2026; 9 telegrams, 555 cipher groups: 510 certain, 24 probable, 21 unresolved; 96.2% read as sense. Published on the site as a partial critical edition with a candidate key; N07, under the same prefix, does not read with it).

Contributed by Brice Dudout (Wenmi, https://bdudout.github.io/wenmi/ ; repository https://github.com/bdudout/wenmi, CC BY 4.0), with Claude Opus 5.5 agents. Published on the Wenmi site: https://bdudout.github.io/wenmi/en/gongmi.html (key, telegrams,
translations), with the article https://bdudout.github.io/wenmi/en/juin1916.html and the method page
https://bdudout.github.io/wenmi/en/method.html. **The reading of the key as a renumbered 明密 code book is Satoshi
Tomokiyo's** (Cryptiana, 23 Oct 2026, https://cryptiana.web.fc2.com/code/chinesecrypto_e2.htm; see key.md).

## Relation to `targets/numeric1916`

These telegrams are already in `targets/numeric1916`, which holds the three codes 共密, 容密 and 辰密 under one target and
whose NOTES say: "these are three keys under one target, against the 'one key, one entry' rule ... Splitting into
gongmi1916 / rongmi1916 / chenmi1916 is the clean alternative". This folder is that split for 共密, proposed with its two
siblings (`rongmi1916`, `chenmi1916`) in one pull request. Nothing in `numeric1916` is changed: its independent check
(20 Oct 2026: `decode.py` reproduces every group of the published raw texts; `verify.py` and the key searches rerun) and
its re-read of 23 Oct 2026 (b21) stand and are not repeated here (the project's credit stays on numeric1916). If the split is accepted, the 共密
document of `numeric1916` can point here; if not, this folder can simply be dropped.

What this folder adds: the texts in the current state of the Wenmi edition (digits re-read by Brice Dudout, including
the vol. 4 telegrams), a standalone key file with S. Tomokiyo's renumbered-book tables, and the credits for that
reading of the key.

## The documents

Copies made by the Japanese police and Communications Bureau of telegrams sent or received by Huang Xing's household in
Tokyo (青山南町三ノ五三) and the Shanghai group, JACAR, Diplomatic Archives of the Ministry of Foreign Affairs of Japan,
series 1.6.1.4-2-1-2 "特定人ノ発受郵便物取調" (B03050089300, B03050089400, B03050089500, B03050090000). The forms carry no decipherment. Digits in kanji
numerals in a grid; every digit re-read blind by Brice Dudout on the scans (V4B: 4 of 22 sheets). No image is
reproduced here.

- N17 | 10 June 1916 | Tokyo → Shanghai | JACAR B03050089300, PDF pp. 16R, 16L, 17R, 17L, 18R, 18L, 19R, 19L, 20R, 20L, 21R, 21L, 22R, 22L (165 groups)
- N18 | 11 June 1916 | Tokyo → Shanghai | JACAR B03050089300, PDF pp. 23R, 23L, 24R, 24L, 25R, 25L (62 groups)
- N23 | 13 June 1916 | Shanghai → Tokyo | JACAR B03050089400, PDF pp. 14R, 14L, 15R (30 groups)
- N32 | 14 June 1916 | Shanghai → Tokyo | JACAR B03050089400, PDF pp. 39R, 39L, 40R, 40L, 41R (54 groups)
- N27 | 15 June 1916 | Tokyo → Shanghai | JACAR B03050089400, PDF pp. 31L, 32R (14 groups)
- N30 | 15 June 1916 | Tokyo → Shanghai | JACAR B03050089400, PDF pp. 36R, 36L, 37R (31 groups)
- N33 | 15 June 1916 | Shanghai → Tokyo | JACAR B03050089400, PDF pp. 41L, 42R, 42L, 43R, 43L, 44R (70 groups)
- N35 | 16 June 1916 | Tokyo → Shanghai | JACAR B03050089500, PDF pp. 2R, 2L, 3R, 3L, 4R, 4L, 5R, 5L (91 groups)
- V4E | 2 July 1916 | Shanghai → Tokyo | JACAR B03050090000, PDF pp. 1L, 2R, 2L, 3R (38 groups)

The first two groups of each form are a clear CTC prefix naming the code (0364 1378 = 共密). Hsueh Chun-tu's edition
of Huang Xing's drafts (黃興等電稿) records such a code name at the head of each telegram, one per correspondent, so the
prefixes are the names of code books issued to correspondents (Wenmi, "Les livres X密").

## The key

Full statement in `key.md` (formula, and S. Tomokiyo's renumbered-book tables). How it was found:

Recovered without cribs in October 2026: exhaustive search over the 10,000 constants K, with the best tens
permutation for each (Hungarian assignment), scored by a CTC unigram/bigram model trained on the telegrams already
published on the site (1915-1916); Codex made the first trials. The search returns K = 9000 and φ exactly. The key was
found on N17 and N18 and reads the other telegrams; V4E (2 July, vol. 4) was not used and reads unchanged.

Checks (Wenmi `solver/numeric1916/verify.py`): the key reproduces every published raw text from the digits; its
language-model score is far above random keys of the same form and above shuffled digits (figures rerun in
`targets/numeric1916/NOTES.md`, 20 Oct 2026).

## Why "read in part"

The Wenmi page publishes these nine telegrams as a partial critical edition: C51 is presented as a candidate
reconstruction (the historical code book is not identified; a printed CTC exemplar of uncertain date agrees on 14
targeted entries), 21 characters remain unresolved (signatures and date codes at the ends of N32 and N33, names in N27,
N30, N35, V4E) and N07, which carries the same clear prefix 共密, does not read under C51 (another copy of the book, or a
faulty stream). The share of characters read as sense is above 95%, but we keep the class the edition itself gives.

## Counts (Daniel's rule, from reading.md)

510 certain, 24 probable ({x}), 21 unresolved (〔x〕), of
555 cipher groups: 96.2% read as sense. Status of the groups in decryption.txt: 510 ok, 45 doubtful.

## Remaining gaps

- 21 characters kept as 〔x〕: the endings of N32 (會逵境) and N33 (會城), names in N27 (參薾), N30 (釆), N35 (伋, 凌, 蓷, 黏, 嗹, 奡), N17 (漠, 廖), V4E (圉, 覃) - blocker: illegible; no one-digit variant gives an evident character: digits to re-read on the copies, or names and date codes
- N07 (prefix 共密, first sheet only) does not read under C51 - blocker: no-key-material; another copy of the book or a faulty stream, no plaintext
- V4E framing repairs deduced from the decoding - blocker: needs-physical-access; to be checked on the JACAR scan

## Escalation

- [x] siblings: the neighbouring forms of the same JACAR volumes (vol. 3 B03050089200-89500, vol. 4 B03050089900-90000) were transcribed; Rongmi, Chenmi, Qianmi, N01 and the clear telegrams read from them.
- [n/a] clear-pages: the police copies carry no decipherment and no clear version of these telegrams was found in the same files.
- [x] known-keys: the Rongmi and Chenmi keys (eight reading orders) and the renumbered-book model that read Qianmi (C104) tried on N07; negative.
- [x] print: Hsueh Chun-tu's edition of Huang Xing's drafts (黃興等電稿), Tomokiyo (Cryptiana) and online searches: texts not found.
- [x] key-rebuild: the key was rebuilt exactly (exhaustive search over K and the tens permutation) and confirmed by S. Tomokiyo's renumbered-book reading.
- [x] retry: every 〔x〕 retried with its one-digit variants (Wenmi pages; checked again in numeric1916, b21), and 20 digits re-read on the scans by Brice Dudout.

## Files

- `transcription.txt`: the digit groups, one telegram per line (prefix left out).
- `decryption.txt`: group, CTC number, character, status, with dates, routes and JACAR sheets.
- `reading.md`: the punctuated Chinese reading; `translation.md`: English.
- `key.md`: the key (CC BY 4.0).

## Prior work

None known for these texts: they are not in Hsueh Chun-tu's edition of Huang Xing's 1916 drafts, which has nothing
between 8 and 20 June, nor found online (Wenmi, Juin 1916 article). 黃興集 and Li Yuanhong's correspondence not yet
checked. The key is a reconstruction: no historical copy of the 共密 book has been found.
