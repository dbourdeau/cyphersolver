# PREREG C06 — Dörffler (catalogue 1773): TABLE-C06 = TABLE-C04 + M. German's additions, one measure on a fresh portion

Written 17 Nov 2026 by Brice Dudout's decipherment thread (Claude Opus 5.5 agent), BEFORE any fresh portion was
transcribed or decoded with TABLE-C06. New protocol, new hash, never retroactive. C03, C04 and C05 stay FAILED.

## Table (frozen before this PREREG)
`TABLE-C06.json`, SHA-256 **7f6c28908a409508ac706ee4c51d495730ac8dd34e172ed009efd944d26c062f**.
= `table/TABLE-C04.json` (SHA-256 14b38f499a961b99bc7707aa71106cf5f5ca140eaa27faae1728db827b41ef28), unchanged,
+ `ADDITIONS-German2026.tsv` (SHA-256 4eba0e5fff2b70117ce03046efa7ab25949e83d63e05d3170058b7aba20b33b3; copy of
`german2026/proposal/ADDITIONS.tsv`, PR #742, commit ca0ee14b), applied as written: 15 fills
(148 an, 175 heit, 191 mich, 201 ohn, 213 uber, 230 zwischen, 233 zwey, 234 drey, 253 alliance, 254 ambassade,
269 churfurst, 275 conjun, 307 general, 323 moscau, 336 schwed) and 6 weaker values listed under `_weaker`
(210 viel, accepted correction of C04 "wider"; 226 wur, probable correction of C04 "wer"; 295 ekm; 301 franckreich;
312 hertzog; 317 konig). Additions: Mike German (Steps Ventures). No value may be added or changed after this point.

## Fresh portion (the critical point)
Spent, never usable for C06: everything in `german2026/transcription/pages.txt` (all 136 coded pages of 19/100-103:
the fit half was used to derive the additions, the test half was measured with them), and in particular
19/102 img. 467, 468, 470, 474, 475, 476 and 19/100 img. 277, 304.
Eligible, in this order of preference:
1. Oxenstiernska samlingen, Gabriel Turesson Oxenstierna af Croneborg, SE/RA/720701/III/03/E 1109 (1681-87) and
   E 1110 (1688, 1690, 1691), "Inkomna brev Dörffler, S." (not digitised on 17 Nov 2026);
2. a coded page of SE/RA/2115/I/19/100-103 that is NOT in `pages.txt` (none known);
3. a coded page of Dörffler's earlier volumes SE/RA/2115/I/12/60-62 (1667-79) (none found: see README).
The portion is fixed by its shelfmark and image numbers in an addendum (`PREREG-C06-ADDENDUM.md`, hashed) BEFORE
its first transcription. Size: the scored pairs must hold >= 150 cipher groups AND >= 300 gloss letters, otherwise
the result is FAIL (insufficient), no fallback.

## Transcription (two blind passes, then frozen)
Cipher: pass A and pass B by two independent readers (the second never sees the first, nor the table, nor any decode);
disagreements decided on the image by digit shape only, logged; result `T-C06.txt` hashed in the addendum BEFORE the
gloss is read. Gloss: two readings blind to each other (B launched only after A is written), reconciled on letter shapes
and the gloss's own sense, never the cipher; illegible words marked `[?]`; result `G-C06.txt` hashed BEFORE any decode.
Each gloss line is tagged with the id of the cipher line directly UNDER it (observed rule, C03).

## Metric (robust to word boundaries: the lesson of C05)
`measure_c06.py` (SHA-256 in SHA256SUMS), a re-implementation of M. German's "clerk's letters" measure
(PR #742, `scripts/p5.py`: norm, local_match, gloss_score, shuffled): letters only; for each gloss line of >= 4
letters, the letters it shares in order with the decode of the cipher line under it plus the next cipher line of the
same half-page, counting matching runs of >= 3 letters; S = matched / total gloss letters. Word boundaries play no role.
Controls: **200** tables = TABLE-C06 with its values shuffled among its numbers, `random.Random(20261117)`.
TABLE-C04 is printed beside it for information only; it does not decide.

## Threshold (declared now)
**PASS = S >= 0.70 AND S >= max(200 controls) + 0.30.** Anything else = FAIL.
Why 0.70 and not the default 0.85: on this metric the published key reaches 0.714-0.753 on every volume outside
19/102 and 0.716 on Mike German's held-out half (shuffled best 0.13-0.16), because the clerk's decryptions are loose
paraphrases; 0.85 would fail a correct key. 0.70 asks the extended table to do at least as well as the validated
TABLE-C04 does on independent material, and the +0.30 margin is the dossier's margin since C03.
Self-test on spent 19/102 img. 474 (German's transcription, no bearing on any verdict): C04 0.685, C06 0.733,
controls max 0.17-0.19.

## Order
1. Hash this PREREG, `TABLE-C06.json`, `measure_c06.py`. 2. Addendum fixing the portion (hashed). 3. Cipher passes,
frozen. 4. Gloss passes, frozen. 5. ONE run: `python3 -I measure_c06.py TABLE-C06.json T-C06.txt G-C06.txt
../table/TABLE-C04.json` -> `MEASURE-C06.txt`. The portion is then spent.

## After the verdict
PASS: reading of unglossed passages counted by Daniel Bourdeau's rule (>= 95 % of words read by the sense = read,
otherwise read in part), sheet sure / {probable} / [restored] / <unresolved>, English translation; glossed passages
stay "existing decipherment (partial contemporary interlinear)". FAIL: published as is, no reading.
