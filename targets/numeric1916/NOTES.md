# Numeric telegraph codes of June–July 1916: 共密, 容密, 辰密 (Huang Xing and the Shanghai group)

Status: no write-up. Retired 5 Nov 2026: split into `targets/gongmi1916/`, `targets/rongmi1916/` and `targets/chenmi1916/` (one key, one entry; Brice Dudout's pull request #266, landed on Dan Bourdeau's condition that this target be retired in the same change). This folder stays as the archive of the independent check (20 Oct 2026) and the b21 re-read (23 Oct 2026), and holds N01 and N09 (`dudout/`), which are other keys.

## Retired 5 Nov 2026: where everything went

- Pages and ledgers: `docs/numeric1916.html` is a stub pointing to the three pages; the README row and the SOLVED_CATALOGUE row are replaced by one row per key; the `PAGES`/`IMAGES` entries, portraits, key-web node and reveal file moved to the new slugs.
- Profile: `profile.json` moved to `profile.pre-split.json` so that the paper data count each telegram once. The three new profiles carry the telegrams, the key recoveries and the project's verification steps. Not carried: the Dudout 28 Oct credits for N01 (Gaimusho tables) and N09 乾密 and the Tomokiyo pointer for the N09 model, which belong to two other keys that still need their own targets.
- Dating and credit of the keys (Dudout against Tomokiyo, checked 5 Nov 2026): see "Dating and credit" in the `NOTES.md` of the three new targets. The keys were published 17-19 Oct 2026 (the 19-20 Oct above is the email and the check made here); the Cryptiana section that reads them as a renumbered 明密 book is undated (page last modified 24 Oct), is cited by Wenmi as 23 Oct, and itself credits the formulas to Dudout.
- Our N24 灰 conjecture (2530 read 2520, the 10th) is in this folder's readings only; the Wenmi edition used by the new targets keeps 〔滠〕.

**23 Oct 2026, re-read (REREAD_BRIEF, b21)**: 共密 and 容密 read from Brice Dudout's proposed readings on his Wenmi pages, checked group by group against our decoder (`texts/gongmi-rongmi_reread_log.md`). His page digit tables are newer than `groups.tsv` for 共密: 20 groups re-read by him on the scans (一/二/三 look-alikes; `texts/gongmi_corrections.tsv`). Every character of the readings is the figure's own value except 21 (共密) and 41 (容密) on a one-digit alternate, 3 and 15 supplied from context ([x]), 21 and 47 kept as [?x], 6 illegible groups (`texts/*_align.tsv`). One value added here: N24 灰 (2530 read 2520, the 10th; sense-checked, for review). N35 sheet 1 checked on the JACAR scan (B03050089500 p. 2). Explicit-hole score, one character = one word: 0.91 and 0.91 (Chinese is not scored by `_check_reading.py`). Readings `texts/gongmi_reading.md`, `rongmi_reading.md`; English `texts/gongmi_en.md`, `rongmi_en.md`. fraction_read 0.11 -> 1.0.

**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): the decode files are verbatim decoder output. 辰密 reads; 共密 (N32, N33, N35) and 容密 (N19b, N21, V4D) carry clusters of mis-decoded characters (圄會 for 國會, 代噸 for 代表) that break whole clauses, and no translation is in the folder (Dudout's Wenmi pages have them). Both are *decoded, not read*; class read in part kept; fraction_read 0.9238 -> 0.11 (辰密's 232 of 2,100 groups).

Contributed result. Brice Dudout (contributors.json `dudout`), working with Claude (mainly Opus 5.5; early trials with
Codex), recovered three keys for numeric telegrams intercepted in Japan in June and early July 1916, and sent them in
an email of 19 Oct 2026. On 15 Oct 2026 he agreed to cross-posting with attribution and to inclusion in the paper
metadata. This folder holds an independent check of his keys, made here on 20 Oct 2026, not a new decipherment.

Related, different systems with their own pages: `targets/sunyatsen/` (condensers, Sun Yat-sen's circle, 1916–17;
`docs/sunintercepts.html`) and `docs/huangxing.html` (Huang Xing, 25 May 1916, romanised kana). Note for the
write-up: these are three keys under one target, against the "one key, one entry" rule (writeup skill section 0);
kept together here because the task asked for one page. Splitting into gongmi1916 / rongmi1916 / chenmi1916 is the
clean alternative if George Lasry wants it.

## Sources

- JACAR (Diplomatic Archives of the Ministry of Foreign Affairs of Japan), series 特定人ノ発受郵便物取調,
  B03050089200, B03050089300, B03050089400, B03050089500 (June 1916) and vol. 4, B03050089900 and B03050090000
  (late June, received 2 July). Japanese telegraph-office forms (送達紙 / 頼信紙) copied by the police; four-digit
  groups written in kanji numerals in a grid, read in columns right to left, top to bottom, sheet after sheet.
- Brice Dudout, *Wenmi*: https://bdudout.github.io/wenmi/en/gongmi.html, .../rongmi.html, .../chenmi.html,
  the article .../juin1916.html and the method page .../method.html.
- Repository: github.com/bdudout/wenmi, `solver/numeric1916/` (commit 7e148a7, 20 Oct 2026): `common.py` (keys),
  `verify.py`, `search_*.py`, `data/messages.json` (digits as re-read by him, sheet refs, published raw text).

## The clear prefix

The first two groups of each form are in clear CTC and name the code: 0364 1378 = 共密, 1369 1378 = 容密,
6591 1378 = 辰密. Hsueh Chun-tu's edition of Huang Xing's drafts (黃興等電稿) records the code name at the head of
each telegram, one per correspondent (辰密 for Zeng Jiwu in Hunan, 共密 for Li Shucheng and Chen Jiahui ...), so the
prefixes are names of code books issued to correspondents (Dudout, juin1916 page).

## The three keys (as he states them)

P is the number in the Chinese telegraph code (CTC); none of the keys has been found in a historical code book.

- **共密** (9 telegrams, 555 groups): replace the tens digit t by φ(t), φ = 9 7 6 1 4 0 5 2 8 3; P = (9000 − C′) mod
  10000. Example: 1188, tens 8 → 8, 9000 − 1188 = 7812 黎; 7528, tens 2 → 6, 7568, 9000 − 7568 = 1432 就.
- **容密** (14 telegrams, 1306 groups): per-place digit substitution, thousands 0123456790, hundreds identity,
  tens 0198276543, units 9801723456; P = σ(C) + 0901 mod 10000 with ordinary carries. No group starts 00; the
  encipherer writes 90 instead (thousands 9 → 0). Example: 2081 → 2048, + 0901 = 2949 款; 9084 → 0047, + 0901 =
  0948 國.
- **辰密** (4 telegrams, 239 groups): the CTC reordered. The first two digits give the page, numbered backwards over
  the numbers without a zero (99 = page 00, 91 = 08, 89 = 09 ..., 11 = 80); tens T = 3987102645, units
  U = 1 9 5 4 3 2 6 7 8 10 (units 9 stands for 10 and carries). Example: 9950 4220 6219 → 0001 5281 3500 = 一興灰
  (6219: page 62 → 34, tens 1 → 9, units 9 → 10: 3400 + 90 + 10 = 3500 灰, the day code for the 10th).

## How he found them (method pages)

No cribs. 共密: exhaustive search over the 10,000 constants K with the best tens permutation for each (Hungarian
assignment), scored by a CTC unigram/bigram model trained on published 1915–16 telegrams; Codex made the first
trials. 容密: only 90 first-sheet groups at first, too few; once ~590 groups of continuation sheets were read,
annealing four per-place substitutions gave readable text; the anomaly 借甸 (3949) for 借款 (2949), off by 1000
exactly when the hundreds made no carry, showed the additive. The exact key was computed on N02, N08, N11, N12;
the 90 = 00 rule was added from the groups beginning 90. 辰密: 容密/共密 trials failed; no 0 in the first two digits
and a concentration on a few pages suggested a frequency-ordered book; annealing a permuted-page + permuted
tens/units model on N13, N16, N26 (201 groups) gave readable text; the page table followed the zero-free
countdown, which was then imposed; two aberrant characters from groups ending 9 (劈 for 力, 滠 for 灰) gave 9 = 10.

His checks: 容密 key from four telegrams reads the other ten unrefitted (incl. N14 dated 佳 = 9th, as on its
header), refitting on all 590 groups returns the same tables; 辰密 N05 was not used in the search, has no prefix,
and reads straight through; N16 ends 灰, matching its header date (10th); three vol. 4 telegrams (V4B, V4D, V4E)
were never used to find the keys and read unchanged; names fit June 1916 office-holders (張國淦, 谷鍾秀, 張孝準,
趙夷午 = Zhao Hengti, 湯督 = Tang Xiangming, 濟武 = Tang Hualong). Every digit was re-read blind by him on the
scans, except V4B (only 4 of its 22 sheets so far); for V4B, V4D, V4E his digit file includes framing repairs
(one digit missing or extra) deduced from the decoding, still to be checked on the scans.

His counts: 共密 9 telegrams, 555 characters, 510 read, 45 doubtful; 容密 14, 1306, 1198, 102 doubtful,
6 illegible; 辰密 4, 239, 232, 7 doubtful. Total 2100 cipher groups, 1940 read without doubt (92.4%).

## Independent check here (20 Oct 2026)

1. `verify.py` (read first; run with `python -I` from the scratchpad through a runpy wrapper, his directory on
   sys.path): reproduces 32/32 published raw texts (27 cipher + 5 clear). Scores per code (mean LM gain per code)
   against the maxima of 200 random keys of the same form and 200 digit shuffles:
   共密 3.492 vs −1.450 / −1.224; 容密 3.179 vs −1.665 / −1.455; 辰密 3.773 vs −1.588 / −1.177.
   (His README quotes 3.50 / 3.26 / 3.77; the 共密 and 容密 figures moved when V4B, V4D, V4E were added.)
2. `search_gongmi.py --nulls 3`: from scratch, K = 9000 and φ exactly; score 3.492; shuffled-digit nulls
   −1.102, −1.065, −1.088 (6 s).
3. `search_rongmi.py --nulls 2`: step 1 (four substitutions) 2.175; step 2 K = 0900, hundreds and tens tables
   exact, units table = published + 1 (equivalent to K 0901 up to the carry), thousands differs on 7/8/9 (the
   90 = 00 rule is not modelled); score 2.608 against the published key's 3.179; shuffled nulls −1.095, −1.185.
   As his README says: the last manual step is not reproduced by the search.
4. `decode.py` here: written from the key statements, not importing his code; CTC from the Unihan
   kTaiwanTelegraph table already in `targets/sunyatsen/tw.csv` (kMainlandTelegraph `cn.csv` fallback). The
   kTaiwanTelegraph table agrees with his `code2ch.tsv` on all 9022 shared codes (the mainland table only on 4462
   of 7078: simplified forms). Applied to his re-read digit streams (`groups.tsv`, copied by `extract_groups.py`):
   **2472 of 2472 groups give the same character as his published raw text, 32/32 telegrams identical**; the
   cipher part is 555/555 共密, 1306/1306 容密, 239/239 辰密. 8 groups carry an illegible digit (3 共密, 5 容密);
   he counts 6 illegible in 容密. Output in `decode_out.txt`.

What this check does and does not show: the keys as stated decode his digits into his texts exactly, and the
key-search and null controls rerun as he reports. It does not re-read the digits on the scans (one form, N16-1,
was compared by eye for its first 12 digits: 6591 1378 9947 2777 4651, matching), nor the translations.

## Content (his summary, checked against his texts)

They fill the gap in Huang Xing's published drafts between 8 and 20 June 1916. Arms bought in Japan for Zhejiang
(Governor Lü Gongwang): about 10,000 rifles, ten or so mountain guns, machine guns (N02, N12), ammunition per
weapon (N21), payment before 30 June (N36); a one-million loan through 芳川 and the Zhaoqing five-million loan;
tobacco taxes as security (N25). Japan will not lend to Beijing before North and South are unified (N17, 10 June;
N19b, 11 June). Huang Xing's five conditions to Li Yuanhong: restore the 1912 Provisional Constitution and the old
Parliament, no amnesty, Duan's cabinet to resign, move Wang Zhanyuan, bring the party leaders to Beijing (N17).
"No legal solution without armed force" (N19b); a Hunan division under Zhao Hengti for Li (N16). The Shanghai group
reports the meeting at Tang's house (N24). Li Yuanhong's reply of 14 June is in clear (N34). Late June: Duan back to
three delegates per province (V4B).

Correspondents: Tokyo side Huang Xing (興, 克強) and Zhang Xiaozhun (準, 潤農), at 青山南町三ノ五三; Shanghai side
the group of Yin Ruli, Huang Fu and Ge Jing'en (signing 李/驪, 郛, 恩), relaying to and from Lü Gongwang; the
辰密 telegrams go to the Hunanese group's address ヒツキン, 277 Avenue Joffre.

## Verification 4, 23 Oct 2026

The v4 sweep cannot score Chinese. chenmi had no reading (only the unpunctuated decoder output and Dudout's web
translation): `texts/chenmi_reading.md` and `chenmi_en.md` now give the four telegrams punctuated, figure values kept,
盻 → [盼] supplied as in rongmi, and 偕, 一不, 畎, 羶 as `[?x]`. On the b21 rule (explicit holes, one character = one
word, supplied characters counted as holes): 19/19 sentences clean, 5 holes in 239 characters. gongmi (0.91) and rongmi
(0.91) were re-judged as a reader on their b21 readings. All three keep read, grade B.

## Remaining gaps
- 共密: 45 doubtful characters in 9 telegrams - blocker: illegible; uncertain digit readings or rare codes, marked on his pages
- 容密: 102 doubtful and 6 illegible characters in 14 telegrams - blocker: illegible; uncertain digits on the police copies, and recurring anomalous codes (繒 for 生, 盻 for 盼) kept as marked
- 辰密: 7 doubtful characters (four single-digit probable readings, 一不 for 不一, 盻 for 盼) - blocker: illegible; single-digit uncertainties on the forms
- V4B (容密, 265 groups): only 4 of its 22 sheets re-read blind; framing repairs in V4B, V4D, V4E still to be checked on the scans - blocker: needs-physical-access; contributor's re-reading of the JACAR scans, not done here
- N07 (prefix 共密, does not decode under the 共密 key; only the first sheet transcribed), N06 (和密), N09 (乾密), N01 and N03 (no prefix) - blocker: no-key-material; other keys or the other direction's book, no plaintext, only first sheets transcribed by the contributor
- ~~共密 and 容密 telegrams: decoded, not read~~ closed 23 Oct 2026 (b21): both read from Dudout's proposed readings checked group by group; 共密 21 [?x], 容密 47 [?x] + 6 illegible groups left - blocker: illegible; digits to re-read on the police copies, or names and date codes (telegram endings)

## Escalation
- [x] siblings: his 32-telegram set covers every form in B03050089200-89500 and the vol. 4 items; the unread five are listed above
- [n/a] clear-pages: the five clear telegrams (N04, N10, N29, N31, N34) are context, not decipherments of the cipher ones
- [x] known-keys: 共密 and 容密 keys tried by him on 辰密 and on N07 before the 辰密 search; they do not read them
- [x] print: Hsueh Chun-tu ed., 黃興等電稿 checked by him: nothing between 8 and 20 June; 黃興集 and Li Yuanhong's correspondence not yet checked
- [n/a] key-rebuild: contributed result; the keys decode his digits exactly here, the open pieces need digits or other keys
- [n/a] retry: the doubtful characters are digit-level uncertainties on the police copies, a re-reading of the scans rather than a key question
- [x] retry (23 Oct 2026, b21): one-digit variants listed for every unresolved group; N24 灰 adopted, V4E [?垣] kept as conjecture, the rest left; N35 sheet 1 re-read on the JACAR scan

## Files

- `extract_groups.py` — copies his digit streams from `messages.json` into `groups.tsv` (CC BY 4.0, attributed).
- `groups.tsv` — 32 telegrams: id, code, prefix, direction, day, JACAR sheets, digit groups, his raw text.
- `ct_gongmi.txt`, `ct_rongmi.txt`, `ct_chenmi.txt` — the cipher groups per code, one telegram per line (measured
  with `_check_profile.py --measure ... --drop-first`: 555 / 1306 / 239 tokens, 330 / 571 / 167 distinct).
- `decode.py` — independent decoder; `decode_out.txt` — its comparison output.

## N01 and N09 by Brice Dudout (28 Oct 2026)

Full texts of N01 (Gaimushō tables) and N09 乾密 in `dudout/`; see `dudout/README.md`.
