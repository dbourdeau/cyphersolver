# Kagoshima / Ryukyu 1879: three Army Ministry cipher drafts, 1877 kana tables nos. 4, 1 and 6

Status: read in part as a target (docs 1 and 2 read, doc 3 read in part; contemporary plaintext on the drafts; 96/99 words = 97.0%: doc 1 35/35, doc 2 20/20, doc 3 41/44). Catalogue 2572 and 2573; doc 3 (JACAR C10072244400) is a third draft of the same affair, not in the catalogue.

Contributed by Brice Dudout (Europe chiffrée), with a Claude Opus 5.5 agent, 13 Nov 2026.

## What the drafts are

The JACAR record text (内容) of 2572 and 2573 looks like a kana string that is partly in clear. The images show why: each draft carries the cipher **and**, sign by sign beside it, the plaintext kana (2572: two sub-columns per column, cipher right, plaintext left; 2573: plaintext in large kana, cipher in small kana to the right; doc 3: alternate lines). The JACAR transcriber interleaved the two. So the plaintext is contemporary and on the leaf: the reading is the clerk's; our part is the transcription, the identification of the tables, the kanji and the translation, and a check that the cipher follows the tables.

| doc | shelfmark | catalogue | table | words | check (signs matching the table) |
|---|---|---|---|---|---|
| 1 | JACAR C10072242200, frame 0533 (0534 blank), 陸軍省-雑-M12-2-150 | 2572 | no. 4 (header 四号) | 35/35 | 95/96 |
| 2 | JACAR C10072242900, frame 0545, 陸軍省-雑-M12-2-150 | 2573 | no. 1 | 20/20 | 45/47 |
| 3 | JACAR C10072244400, frames 0575-0576, 陸軍省-雑-M12-3-151 | - | no. 6 (header 第六号) | 41/44 | 132/138 |

NIDS, Ministry of Defense. No images included (JACAR, all rights reserved).

## System and key

The Army's kana substitution tables of 1877 (隠語表 第一号-第二十二号, 参謀部, JACAR C09084568800; rules of 22 Dec 1876 in C08052370500, in force 15 Jan 1877). Each table pairs the iroha (44 signs, without ヰ オ ヱ ン) with one fixed cipher sequence, shifted by 8 - 2n (mod 44) for table n (checked on the images of tables 1, 2, 4, 5, 6, 19-22). Voicing marks are carried over. `key.tsv` gives tables 4, 1 and 6. The table system is described by Satoshi Tomokiyo (Cryptiana, meijiarmy.htm); these three drafts show it still in use in 1879.

## Check (frozen protocol)

Protocol and transcription frozen by SHA-256 before any key test. The pre-registered hypothesis H1 (one key learned on doc 1, applied to doc 2) failed (2.1%), because the drafts use different tables; this was seen and an addendum frozen before computing the documentary check: each table, applied to the plaintext, reproduces the transcribed cipher for 99.0% / 95.7% / 95.7% of signs, against at most 18.8% / 25.5% / 17.4% for 200 controls (the 21 other tables and 179 random alphabets); 185 held-out signs outside doc 1. Misses are glyph confusions of this hand (ヌ/ス, ル/レ, エ/ユ, ゴ for a voiced ヨ/ニ/ユ). The transcription was made by the agent while the key was known; against the independent JACAR record string the documentary table also wins clearly (matching blocks 0.82 / 0.42 / 0.63 against at most 0.08 for the other tables).

## Readings

- Doc 1 (2572): 鹿児島屯在隊出張ハ出征ニ非ザル故、出征手当ハ勿論賜ラズ。出発日限未定ナリ。決定次第申シ進ズベシ。携帯ノ外ノ弾薬ハ当地ヨリ送ル方便利ナラン。御考ヘ如何ニ。 A short passage is struck out on the draft (not counted).
- Doc 2 (2573): 琉球ヘ出張兵隊ノ為、小屋ハ建ツルニ及バズ。是等ノ事ハ益満大尉ヘモ申シ遣ハス。 The sign マ of マスミツ looks like テ in the plaintext but the cipher (レ, table 1) gives マ.
- Doc 3: 鹿児島屯在兵ノ内半大隊、琉球藩ヘ出張ヲ命ゼラレタル処、残リ半大隊モ何時出張ノ令アルモ計リ難キニ付キ、先般達シタル数箇条ノ内第二・四・五・六・七条ニ基ヅキ … 不足品ハ申シ達スベシ (3 words unresolved).

Context: the Ryukyu Disposition of March-April 1879, when a half battalion backed the annexation of the Ryukyu domain (Okinawa prefecture).

## Prior work

The plaintext is on the drafts themselves (credit: contemporary). The tables are in the archive (C09084568800) and the system is described by Tomokiyo. No published reading of these three drafts found (JACAR, Cryptiana, this repository, Japanese web search, 13 Nov 2026); Nagata 1989 and the NDL were not checked.
