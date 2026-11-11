# Meiji 1874: three Army telegrams on the end of the Taiwan expedition (Oct-Nov 1874), army 1-7 coordinate square

Status: read in part (Brice Dudout, 28 Oct 2026, credits corrected 10 Nov 2026; 65 of 72 cipher words certain or probable = 90.3%: telegram 1 20/20, telegram 2 27/29, telegram 3 18/23; telegrams 1 and 2 were first deciphered by Ohno Tetsuya in 2010 and are re-read here independently; telegram 3 is not in Ohno and is read here for the first time, to our knowledge).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Not in the catalogue. Published on L'Europe chiffrée, https://bdudout.github.io/europe-chiffree/fr/documents.html#meiji-1874 (credits corrected 10 Nov 2026).

## Prior work and credits

- **The cipher is not new.** The army's 1-7 coordinate square of 1874 (電信隠語, Yamagata, Oct 1874) is described by
  - 長田順行 Nagata Junkō, 『西南の役と暗号』 (1989), p. 170 (a variant, Satoshi Tomokiyo's "meijiarmy6", same layout as ours once rows and columns are swapped);
  - 大野哲弥 Ohno Tetsuya, 「明治7年の陸軍省暗号の制定：佐賀の乱後の陸軍暗号電報利用状況」, 情報化社会・メディア研究 7 (2010), pp. 37-44;
  - Satoshi Tomokiyo, Cryptiana, https://cryptiana.web.fc2.com/code/meijiarmy.htm (2014), tables "meijiarmy1" to "meijiarmy9". Our key is his "meijiarmy1" (HO = 15).
  We found it independently on 28 Oct 2026 as the a-priori hypothesis of our protocol, before we knew of these works; we do not claim the key.
- **Telegrams 1 and 2 were first deciphered by Ohno Tetsuya (2010)**: his no. 4031 = JACAR C04025783900 (telegram 1) and no. 4027 = C04025783500 (telegram 2), both in meijiarmy1. Our readings of them are independent re-readings (role here: verification).
- **Satoshi Tomokiyo** read the continuation of telegram 2 in C04025783600 (frame 1812) with this key (personal communication, 30 Oct 2026) and confirmed two readings in telegram 3. He also deciphered Ohno's no. 4028, enciphered with the "meijiarmy4" table issued on 30 Oct 1874 (communication of 10 Nov 2026). C04025783600 frame 1813, which does not read with meijiarmy1, is probably that no. 4028 (to be confirmed). Frame 1813 is not included here.
- **Telegram 3** (Major Ōnuma, Nagasaki, 22 Oct 1874, JACAR C10071951300) is not in Ohno's article, which cites C04025783500 and C04025783900 only. To our knowledge this is its first reading (read in part).
- Our own prior-work check of 28 Oct 2026 (web JA/EN, the NDL column on Meiji cipher tables, this repository) found none of this; it was incomplete. Satoshi Tomokiyo pointed out the descriptions of the cipher on 29 Oct 2026 and, having obtained Ohno's article, Ohno's decipherments on 10 Nov 2026. Thanks to him.

## Documents

| telegram | shelfmark | date | first reader | here |
|---|---|---|---|---|
| 1 | JACAR C04025783900, frames 1819-1820 | 8 Nov 1874, Army Ministry to a garrison | Ohno 2010 (no. 4031) | re-read, 20/20 words |
| 2 | JACAR C04025783500 frame 1811 + C04025783600 frame 1812 | 8 Nov 1874, Army Ministry to the garrisons | Ohno 2010 (no. 4027); frame 1812 also read by Tomokiyo | re-read, 27/29 words (read in part) |
| 3 | JACAR C10071951300, frames 0712-0713 | 22 Oct 1874, Major Ōnuma, Nagasaki, to Yamagata | (none known) | first reading, 18/23 words (read in part) |

Ministry of Defense, National Institute for Defense Studies, Army Ministry records. No images are included: JACAR images are "All rights reserved".

## System and key

Each pair (row, column) points into a 7 x 7 square filled with the iroha in its traditional layout of seven kana per line (いろはにほへと / ちりぬるをわか / よたれそつねな / らむうゐのおく / やまけふこえて / あさきゆめみし / ゑひもせす), the last two cells holding the dakuten and handakuten, enciphered as separate signs (ダンパン = タ゛ム ハ゜ム). ム also stands for ン. `key.tsv`.

This was the a-priori hypothesis written in our protocol before any computation; the square is used unpermuted. Only cells 76 and 77 were fixed on telegram 1.

## Check of the key on a held-out telegram

Key and transcription frozen (SHA-256) and then applied unchanged to telegram 2 (63 pairs of frame 1811, cursive), held out: it reads 支那ノ談判既ニ破レタル趣 … 尚確報. Against 200 random permutations of the 49 cells: kana trigram score -5.03/char vs at best -5.30; 11 lexicon hits vs at best 2; 0 of 200 controls reach the true key. Since the key is published (Nagata 1989, Ohno 2010, Tomokiyo 2014), this only checks our transcription and reading.

## Readings (Daniel Bourdeau's 95% rule: certain + probable words; restored words not counted)

- Telegram 1 (`reading.md`): 支那談判平穏ニ相済ミ、支那政府ヨリ償金ヲ出ス筈ニ約定成シ{タ}ル趣、唯今電報ヲ得タリ。 20 words: 19 certain, 1 probable = 20/20.
- Telegram 2 (`reading_2.md`): 支那ノ談判既ニ破レタル趣…尚確報アラバ速ヤカニ申シ達スベキニ付キ、浮説等信用スベカラズ. 29 words: 23 certain, 4 probable, 1 restored, 1 unresolved = 27/29 (93.1%; 28/29 with the restored word). Doubtful signs settled by targeted visual reviews by Brice Dudout (shapes only).
- Telegram 3 (`reading_3.md`): 北京ヨリ書翰ヲ落手セリ、支那政府ヨリ大久保全権…本月二十日マデニ返答スベシ、其ノ上ニ引払ルナルベシ. Cipher and clear text mixed, pairs not separated. 23 words: 12 certain, 6 probable, 4 restored, 1 unresolved = 18/23 (78.3%; 22/23 with the restored words, which depend on two declared cipher-clerk corrections; strict reading without them about 77%).

Files: `transcription*.txt`, `decryption*.txt`, `reading*.md`, `translation*.md`, `key.tsv`.

## Scope and related targets

- One key, one entry: all three telegrams use meijiarmy1. C04025783600 frame 1813 does not read with it and is probably Ohno's no. 4028 in Tomokiyo's meijiarmy4 table of 30 Oct 1874 (deciphered by Satoshi Tomokiyo, 10 Nov 2026); it would belong in its own target and is not included.
- Not the same system as `army1901`, `army1901in` or `army1902` (the Army's numeric kana ciphers of 1901-04, different tables and period); no overlap of documents.
- Outcome by part: telegrams 1-2 read with known key, prior decipherment in print (Ohno 2010), found after reading and not used (contamination: none in the reading, but not a first break); telegram 3 read with known key, no prior reading known.

## Remaining gaps

- telegram 2, pair 53 (ケ) and the restored [速ヤカニ] - blocker: illegible; the written digits give no word (clerk's slip), no second copy known
- telegram 3, group リシム and four restored words resting on two declared clerk corrections - blocker: illegible; no second copy known
- word-by-word comparison with Ohno 2010 - blocker: needs-physical-access; the article is not online and was not seen here (content reported by Satoshi Tomokiyo)

## Escalation

- [x] siblings: C04025783600 opened; frame 1812 is the continuation of telegram 2, frame 1813 is another table (meijiarmy4)
- [x] clear-pages: telegram 3 carries its own clear head; no clear copies of the cipher parts in the records
- [x] known-keys: Tomokiyo's meijiarmy1-9 tables; meijiarmy1 fits all three telegrams
- [x] print: Nagata 1989, Ohno 2010 (via Satoshi Tomokiyo), Tomokiyo 2014 Cryptiana
- [n/a] key-rebuild: the key is complete (49 cells known); the gaps are clerk errors, not missing values
- [x] retry: doubtful digits re-examined in Brice Dudout's visual reviews (plates C02, C03, C05, C07, C09)
