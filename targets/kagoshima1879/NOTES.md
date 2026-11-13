# Kagoshima / Ryukyu 1879: three Army Ministry cipher drafts, 1877 kana tables nos. 4, 1 and 6

Status: read (integration check, 13 Nov 2026: 98 of 99 words read, 99.0%, sure words only: doc 1 35/35, doc 2 19/20, doc 3 44/44; the contributor's figure was 96/99 = 97.0% with probable words counted, and doc 3 read in part. The three gaps of doc 3 and the probable word of doc 1 are settled by the Ministry's own kanji drafts of the same messages, JACAR C10072244300 and C10072242100; the one open word is the name マスミツ (益満?) in doc 2). Catalogue leads 2572 and 2573; doc 3 (JACAR C10072244400) is a third draft of the same affair, not in the catalogue.

Contributed by Brice Dudout (Europe chiffrée), with a Claude Opus 5.5 agent, 13 Nov 2026.

## What the drafts are

The JACAR record text (内容) of 2572 and 2573 looks like a kana string that is partly in clear. The images show why: each draft carries the cipher **and**, sign by sign beside it, the plaintext kana (2572: two sub-columns per column, cipher right, plaintext left; 2573: plaintext in large kana, cipher in small kana to the right; doc 3: alternate lines). The JACAR transcriber interleaved the two. So the plaintext is contemporary and on the leaf: the reading is the clerk's; our part is the transcription, the identification of the tables, the kanji and the translation, and a check that the cipher follows the tables.

| doc | shelfmark | catalogue | table | words | check (signs matching the table) |
|---|---|---|---|---|---|
| 1 | JACAR C10072242200, frame 0533 (0534 blank), 陸軍省-雑-M12-2-150 | 2572 | no. 4 (header 四号) | 35/35 | 95/96 |
| 2 | JACAR C10072242900, frame 0545, 陸軍省-雑-M12-2-150 | 2573 | no. 1 | 19/20 (contributor 20/20) | 45/47 |
| 3 | JACAR C10072244400, frames 0575-0576, 陸軍省-雑-M12-3-151 | - | no. 6 (header 第六号) | 44/44 (contributor 41/44) | 132/138 |

NIDS, Ministry of Defense. No images included (JACAR, all rights reserved).

## System and key

The Army's kana substitution tables of 1877 (隠語表 第一号-第二十二号, 参謀部, JACAR C09084568800; rules of 22 Dec 1876 in C08052370500, in force 15 Jan 1877). Each table pairs the iroha (44 signs, without ヰ オ ヱ ン) with one fixed cipher sequence, shifted by 8 - 2n (mod 44) for table n (checked on the images of tables 1, 2, 4, 5, 6, 19-22). Voicing marks are carried over. `key.tsv` gives tables 4, 1 and 6. The table system is described by Satoshi Tomokiyo (Cryptiana, meijiarmy.htm); these three drafts show it still in use in 1879.

## Check (frozen protocol)

Protocol and transcription frozen by SHA-256 before any key test. The pre-registered hypothesis H1 (one key learned on doc 1, applied to doc 2) failed (2.1%), because the drafts use different tables; this was seen and an addendum frozen before computing the documentary check: each table, applied to the plaintext, reproduces the transcribed cipher for 99.0% / 95.7% / 95.7% of signs, against at most 18.8% / 25.5% / 17.4% for 200 controls (the 21 other tables and 179 random alphabets); 185 held-out signs outside doc 1. Misses are glyph confusions of this hand (ヌ/ス, ル/レ, エ/ユ, ゴ for a voiced ヨ/ニ/ユ). The transcription was made by the agent while the key was known; against the independent JACAR record string the documentary table also wins clearly (matching blocks 0.82 / 0.42 / 0.63 against at most 0.08 for the other tables).

## Readings

- Doc 1 (2572): 鹿児島屯在隊出張ハ出征ニ非ザル故、出征手当ハ勿論賜ラズ。出発日限未定ナリ。決定次第申シ進ズベシ。携帯ノ外ノ弾薬ハ当地ヨリ送ル方便利ナラン。御考ヘ如何ニ。 A short passage is struck out on the draft (not counted).
- Doc 2 (2573): 琉球ヘ出張兵隊ノ為、小屋ハ建ツルニ及バズ。是等ノ事ハ益満大尉ヘモ申シ遣ハス。 The sign マ of マスミツ looks like テ in the plaintext but the cipher (レ, table 1) gives マ.
- Doc 3: 鹿児島屯在兵ノ内半大隊、琉球藩ヘ出張ヲ命ゼラレタル処、残リ半大隊モ何時出張ノ令アルモ計リ難キニ付キ、先般達シタル数箇条ノ内第二・四・五・六・七条ニ基ヅキ、食料ヲ除キ準備ノ目途ヲ以テ、不足品ハ申シ達スベシ (the contributor left 3 words unresolved; settled by the kanji draft C10072244300, see Integration check).

Context: the Ryukyu Disposition of March-April 1879, when a half battalion backed the annexation of the Ryukyu domain (Okinawa prefecture).

## Prior work

The plaintext is on the drafts themselves (credit: contemporary). The tables are in the archive (C09084568800) and the system is described by Tomokiyo. No published reading of these three drafts found (JACAR, Cryptiana, this repository, Japanese web search, 13 Nov 2026); Nagata 1989 and the NDL were not checked.

## Integration check (13 Nov 2026)

Verified for the maintainer before merging PR #536 (Brice Dudout). The PR carries no scripts; the checks below were
made with a decoder written for the check from the cipher sequence in the key.tsv header, not from its columns.

- **Tables.** The 44-sign sequence of the header gives the three key.tsv columns exactly as shifts: table 4 = shift 0,
  table 1 = shift 6, table 6 = shift 40 (44/44 signs each), which fits "table n = shift 8 - 2n" counted from table 4.
  The table images of C09084568800 were fetched (JACAR PDF) but the 22 tables were not re-read here one by one.
- **Signs.** Each document's own table applied to the plaintext column reproduces the transcribed cipher for
  95/96, 45/47 and 132/138 signs (same figures as the contributor's). The other 43 shifts reach at most 0.010,
  0.021 and 0.014; 179 random alphabets reach at most 0.167, 0.170 and 0.130 (the contributor's 200 controls:
  0.188, 0.255, 0.174; their control script is not in the PR, so those figures are by the contributor's record).
- **Failed pre-registered test.** The contributor's frozen hypothesis H1 (one key learned on doc 1 applied to doc 2)
  failed: 0.021 of signs. It failed because the drafts use different tables; the addendum (one table per document,
  identified from the headers 四号 and 第六号) was declared after that result, before the documentary check, by the
  contributor's record (no external timestamp).
- **Images.** JACAR serves each item as a PDF at /content/item/aj12/<id>/raw/<file>.pdf (the path is in the viewer
  page's najContentList), fetched with curl. On frame 0533 (doc 1) columns 1-2 were compared sign by sign: 33 cipher
  signs and their plaintext agree with transcription.txt; on frame 0575 (doc 3) line 1 (19 cipher signs and plaintext)
  agrees, and line 6 around the gap agrees with the transcription's question marks. 52 cipher signs in all, 52 agree.
  The images are not reproduced (JACAR marks them All rights reserved).
- **Siblings: the kanji drafts.** The neighbouring JACAR records hold the Ministry's own kanji-kana drafts of two of the
  messages: C10072242100 (frame 0531, "２月１７日 鹿児島出張の件諸注意") for doc 1 and C10072244300 (frame 0573,
  "曽我 ３月１日 鹿児島屯在隊の内半大隊琉球藩出張命令について") for doc 3. Doc 3's open stretch reads there
  「食料ヲ除キ準備ノ目途ヲ以テ不足品ハ申出ツヘシ」: the kana ノヅキ ジコムビ ノ モクド are 除キ 準備 ノ 目途
  (the clerk's ヅ for ゾ and コ for ユ; the cipher sign at the コ looks like ソ, which is ユ in table 6). Doc 1's
  draft ends 「御考如何」, which confirms 御考ヘ. The kanji drafts are not word for word the cipher texts (doc 3:
  屯在隊 against トムサイヘイ, 申出ツヘシ against モウシタツヘシ; doc 1: 都合 against ベンリ, and an insertion
  over the struck passage), so they confirm the readings but are not the texts that were enciphered. They also date
  the messages: doc 1 17 Feb 1879, doc 3 1 Mar 1879 (from the JACAR record titles).
  No kanji draft of doc 2 was found in the records next to it (C10072242600 to C10072243000 opened by title).
- **Count, strict rule.** Probable words count as holes. Doc 1: 35/35 (御考ヘ confirmed). Doc 2: 19/20 (the name
  マスミツ is certain as kana, from cipher and plaintext, but its kanji 益満 and the officer are not identified).
  Doc 3: 44/44 in the contributor's word units. Total 98/99 = 99.0%: the class is read. The contributor's figure
  (96/99 = 97.0%, sure and probable, doc 3 read in part) was made before the kanji drafts were found.
- **Method.** read from existing decipherment: the plaintext is on every leaf, written by the clerk beside the cipher;
  the tables (an archive key) were used to check the transcription, not to obtain the text.
- **One key, one entry.** The three drafts use three tables of one issue (隠語表 第一号-第二十二号, 1877), which are
  shifts of one sequence; they are one key family, issued together, and the three drafts belong to one affair and one
  file. They stay in one target, with each document's table named.
- **Prior art.** Satoshi Tomokiyo's Cryptiana page (meijiarmy.htm, section 多表式換字（1877）, opened 13 Nov 2026)
  describes the system in full: the revised 電信隠語 issued by Yamagata at the end of 1876, in force 15 Jan 1877
  (C08052370500, C08052393200), with tables 第一号 to 第二十二号, each pairing the iroha (44 signs) with the iroha
  in reverse order, each table shifted two places from the last; the table number is written in clear at the head
  of the message; he takes it to have been a cipher disk, and cites Nagata 1989, pp. 151-160. So the key and its
  shift rule are published; the contributor's check of the rule on the table images is a confirmation, not a find.
  The header sequence of key.tsv is the reversed iroha, rotated. No reading of these three drafts was found in the
  repository or on that page. Nagata 1989 and the NDL were not checked, by the contributor or here.

## Remaining gaps
- doc 2, the name マスミツ (益満?) - blocker: needs-physical-access; the kana are certain (cipher レ = マ in table 1, the plaintext sign is ambiguous), the kanji and the officer need an 1879 Army officer list, not reached online here
- doc 1, the short struck-out passage after トウチヨリ - blocker: illegible; struck through in both columns on the draft and not part of the message sent (the kanji draft has an insertion there instead); not counted

## Escalation
- [x] siblings: neighbouring records C10072242100 to C10072244500 opened by title; C10072242100 and C10072244300 are the kanji drafts of docs 1 and 3 and settle doc 3's gap
- [x] clear-pages: the plaintext is on each draft beside the cipher
- [x] known-keys: the 1877 Army tables (C09084568800); tables 4, 1 and 6 fit
- [n/a] print: Nagata 1989 and the NDL not checked; no printed reading is needed, the plaintext is on the leaves
- [n/a] key-rebuild: the key is the archive's own table set; nothing to rebuild
- [x] retry: doc 3 line 6 re-read on the image against the kanji draft; the name in doc 2 re-checked against table 1
