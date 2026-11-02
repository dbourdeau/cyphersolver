# The Japanese reports: method passages, transcribed and translated

Transcription keeps the original spelling (kyūjitai, katakana). [ ] = uncertain reading. Translations by Brice Dudout with Claude.
All reports go from the head of the Army Meteorological Department (陸軍氣象部長: 新妻雄 Niizuma until March 1940, then 三上喜三 Mikami) to the Vice-Minister or Minister of War (東條英機, 板垣征四郎, 畑俊六, 東條英機), classified 極秘 (top secret). National Institute for Defense Studies (防衛研究所), Tokyo, via JACAR; images not reproduced.

| JACAR Ref. | Date | Internal no. | Subject |
|---|---|---|---|
| C01004558500 | 12 Aug 1938 | 陸氣密第四七號 | 蘇聯極東氣象報暗號解讀ノ件報告 (+ annex: old and enciphered format) |
| C01004559200 | 26 Sep 1938 | 陸氣密第六一號 | 極東及ソ聯氣象放送新暗號解讀法ニ關スル件報告 |
| C04120597300 | 12 Oct 1938 | 陸氣密第七一號 | 極東ソ聯氣象放送新暗號解讀法ニ關スル件報告 |
| C01004559500 | 12 Nov 1938 | 陸氣密第八二號 | same |
| C01004816800 | 21 Feb 1940 | 陸氣密第五五號 | 極東蘇聯氣象報用暗號解讀ノ件報告 (+ annex, method) |
| C01004816500 | 29 Feb 1940 | 陸氣密第六一號 | 「モスコー」氣象報放送用暗號一部解讀ノ件報告 (type 17040, with example) |
| C01004816400 | 1 May 1940 | 陸氣密第一四一號 | 「モスコー」氣象報放送用暗號解讀要領ノ件報告 (new subtractors from 29 Apr) |
| C01004816900 | 18 May 1940 | 陸氣密第一六三號 | type 05104 |
| C01004816700 | 25 May 1940 | 陸氣密第一七一號 | type 05080 |
| C01004832500 | 6 Jun 1940 | 陸氣密第［一］七九號 | type 05188 |
| C01004832600 | 16 Jul 1940 | 陸氣密第二［二/三］〇號 | 「モスコー」氣象報放送用暗號解讀ノ件報告: method, worked example, tables 附表第一–四 |
| C01004818600 | 16 Oct 1940 | 陸氣密第四二六號 | 「モスコー」氣象報放送用暗號亂數表變更並解讀ノ件報告 (+ new tables) |

## 12 August 1938 (C01004558500): the first Far East cipher

Image 1:
> 首題ノ蘇聯極東氣象報ハ十一日午前十時ヨリ暗號ノ使用ヲ開始セルヲ以テ之レカ飜譯解讀ニ務メタル結果同日午後八時全部ノ解讀ヲナシ得ルニ到リタルヲ以テ之カ解讀説明書（別紙）ヲ具シ報告ス
> 追而本件ハ昨十一日夜電話ニテ報告濟ミナルニ付爲念申添フ

"The Soviet Far East weather reports went over to cipher on the 11th at 10:00. We set ourselves to translate and decipher them, and by 20:00 the same day we could read them in full. I report, enclosing the explanation of the decipherment (annex). P.S. This was already reported by telephone on the evening of the 11th; I mention it for the record."

Annex (images 3 and 2, the two halves of an A3 sheet), 暗号放送形式説明:
> 暗号放送ハ五字ヲ以テ一群ヲ成シ七群ヨリ成ル。旧型式ノ第一群ト第三群トヲ交換シ第二群ト第五群トヲ交換シアリ。而シテ觀測地點名ニハ4ヲ他ノ各数字ニハ3ヲ非算術加法ニヨリ加算シアリ。第七群ハ０００００ト報ズ、但シ第六群ノ觀測ヲ缺ク場合ニハ第六群ヲ０００００ヲ以テ報シ第七群ヲ缺ク。

"The enciphered broadcast is made of seven groups of five figures. Compared with the old format, group 1 is exchanged with group 3 and group 2 with group 5. 4 is added to each figure of the station index and 3 to every other figure, by non-arithmetical addition. Group 7 is sent as 00000; when the observation of group 6 is missing, group 6 is sent as 00000 and group 7 is omitted."

## Additive changes of 1938 (C01004559200, C04120597300, C01004559500)

Each time: 「首題ノ件［date］以降變更サレタルニ付解讀法左記ノ如ク報告ス」 ("as the key changed from [date], I report the method of decipherment as follows"), with 一、地點 (stations), 二、順序 從前通リ (order of groups: unchanged), 三、亂數 (additives). Values in `key.tsv`. Note of 12 October: 「追而從來ノ例ニ徴スルニ『イルクーツク』局モ近ク他局ト同一亂數ヲ使用スルニ至ルモノト判斷セラル」 ("judging by precedent, the Irkutsk station will soon use the same additive as the others"), which it does from 12 November.

## 21 February 1940 (C01004816800): Far East, key-group system

> 一、第一次作業　第一群ノ數字ヲ左ノ如ク變字ス　暗號 〇一二三四五六七八九× / 原文 六七三四九×二五〇一八
> 二、第二次作業　第二群以下ノ暗號文中「×」ヲ「九」ニ「九」ヲ「×」ニ替換フ
> 三、第三次作業　第二群以下ノ各群ノ數字ヨリ飜譯セラレタル第一群ノ數字ヲ非算術減ス　但シ第一群ノ原文「×」トナリタルトキハ「五」ヲ減ス
> 四、第四次作業　第一群ト第三群トヲ入換フ

"1. Substitute the figures of group 1 by the table: cipher 0123456789× → clear 67349×25018. 2. In groups 2 onward, replace × by 9 and 9 by ×. 3. From each group from the 2nd onward, subtract without carrying the figures of the deciphered group 1; where the clear of group 1 is ×, subtract 5. 4. Exchange groups 1 and 3."

## 29 February 1940 (C01004816500): Moscow, type 17040

Letter: 「當部ニ於テ研究ノ結果「モスコー」氣象報放送用暗號中左記型式ノモノノ解讀法別紙ノ通判明セルヲ以テ取敢ス報告ス　型式 一七〇四〇　追テ他ノ型式ニ就キテハ目下解讀法探求中ニ就キ判明次第報告ス」: "Our studies have established, as in the annex, how to decipher the following type of the Moscow broadcast cipher; I report at once. Type 17040. The other types are being worked on and will be reported as soon as solved."

> 一、第一次作業　別掲換字表ニ據リ左ノ數字ノ換字ヲ行フ　1 第一群ノ第五數字　2 第二群以下ノ第一數字
> 二、第二次作業　換字表下欄記載ノ減數ヲ各群ノ殘リノ四數字ヨリ非算術的減法ヲ行フ　但シ「X」ヨリ數ヲ減スルトキハ「X」トス

"1. Using the substitution table, substitute (1) the 5th figure of group 1 and (2) the 1st figure of each later group. 2. Subtract without carrying, from the remaining four figures of each group, the subtractor written in the lower row of the table; subtracting from X leaves X." Table and example in `key.tsv` and `decryption.txt`.

## May–June 1940: new Moscow subtractors

「暗號形式及換字ハ從前通ニシテ減數ノミ變更ス　減數ハ非算術的ニ行ヒ減數表左ノ如シ」: "Format and substitution are unchanged; only the subtractors change. Subtraction is non-arithmetical; table as follows." From 17 May: 「暗文第一群第一字Xニシテ第二群22000ナルトキノ解讀要領ハ從前通ナリ」: "When the 1st figure of group 1 is X and group 2 is 22000, the method is as before" (a second class of messages with an unchanged key).

## 16 July 1940 (C01004832600): the Moscow key tables

> 蘇聯「モスコー」氣象報中歐羅巴露西亞及其ノ近傍ハ從來暗號化サレアリテ其ノ解讀法ニ就テハ其ノ都度報告セル所ナルガ六月十日及六月二十六日變更ノ暗號形式飜譯要領當部ニ於テ研究ノ結果別紙ノ如ク判明セルヲ以テ報告ス

"In the Soviet Moscow weather broadcast, the part covering European Russia and its surroundings has long been enciphered, and we have reported each method of decipherment. Our studies have established the method of reading the formats changed on 10 June and 26 June, as in the annex."

Annex, 「モスコー」氣象報放送用暗號飜譯要領:
> 一、六月十日變更ノ分（六月二十五日迄）
> イ、第一次作業　放送電文中ヨリ同一數字又ハXノ連續三字引續キ同一數字連續二字合計五字ノ群ヨリ成ル鍵ヲ選ビ出ス（例 55533, XXX99 等ノ如シ）
> ロ、第二次作業　第一次作業ニテ選ビ出シタル群ニ續ク電文（數字）ヲ五字ヲ一群トスル五群（一時及十三時地方時觀測ノ場合）又ハ六群（七時及十九時地方時觀測ノ場合）ニ分ツ（之等五群又ハ六群ハ國際陸上實況形式ニ依ル一地點ノ氣象報ノ暗號化セラレタルモノナリ）
> ハ、第三次作業　電文中ノ7ヲXニXヲ7ニ換字ス
> ニ、第四次作業　附表亂數表中最左端ノ行ヨリ第一次作業ニテ得タル鍵ノ初メ三字ニ相當スル列ヲ選ブ次ニ同亂數表最上列中ヨリ鍵ノ終リ二字ニ相當スル行ヲ選ブ斯クシテ求メタル行ト列ノ交ル所ヨリ始マル亂數ヲ第三次作業迄ニ得タル暗號文ヨリ非算術的ニ減算ス然ラバ國際形式ノ氣象報生文ヲ得
> 尚附表第一ハ奇數日（「モスコー」ニ於ケル）附表第二ハ偶數日（「モスコー」ニ於ケル）ノ放送ニ用フベキ亂數表ナリ
> 亂數ハ最後ニ至リタル時ハ其ノ列ノ冒頭ニ續ルモノトス
> 二、六月二十六日變更ノ分（現在使用中ノモノ）
> 飜譯要領ハ六月十日ノ分ト全然同一ナリ　但シ亂數表ハ奇數日（「モスコー」ニ於ケル）ニハ附表第三ヲ偶數日（「モスコー」ニ於ケル）ハ附表第四ヲ用フベキモノトス
> 尚同一數字ノ十個連續セル群ハ句點ヲ表ス

"1. Format changed on 10 June (valid to 25 June). (a) Pick out of the broadcast the key: a group of five made of three identical figures (or X) followed by two identical figures (e.g. 55533, XXX99). (b) Cut the figures that follow into groups of five: five groups for the 01:00 and 13:00 local-time observations, six for 07:00 and 19:00 (these are the enciphered report of one station in the international land-station format). (c) Replace 7 by X and X by 7. (d) In the table, take the row whose label in the leftmost column matches the first three figures of the key, then the column whose heading matches its last two figures; from their crossing, subtract the run of random figures, without carrying, from the cipher text: this gives the clear weather report in the international format. Table 1 is for odd days and table 2 for even days (in Moscow). At the end of a row, continue from its beginning. 2. Format changed on 26 June (now in use): method identical, but with table 3 on odd days and table 4 on even days. A group of ten identical figures marks a full stop."

Worked example (image 4, folio 1104), 「昭和15年7月6日4時00分受信」, with the marginal note 「七月六日四時（日本標準時間）ハモスコーニ於テハ未ダ五日ナルヲ以テ附表第三ノ亂數ニヨル」 ("6 July 04:00 Japan time is still the 5th in Moscow, so table 3 applies"): see `transcription.txt` and `decryption.txt`.

## 16 October 1940 (C01004818600): new tables

> 「モスコー」氣象報暗號亂數表ハ十月十二日十六時〇〇分ヨリ別紙ノ通變更セルヲ以テ報告ス　尚飜譯要領ハ亂數表變更ノ外ハ從來通ナリ

"The random-figure tables of the Moscow weather cipher changed from 12 October 16:00, as in the annex. Apart from the tables, the method is unchanged." The annex gives two grids (奇數日用 odd days, 偶數日用 even days), one figure per cell: `tables_oct1940.py`.
