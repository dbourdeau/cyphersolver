# LJS 51: suspected Arabic errors checked on the master TIFFs

Status: in progress (corpus project; nothing here applied to chains_*.jsonl or the translations).

Source: the "Suspected Arabic errors" lists at the end of the eight `translation_*.md` files, one row per item
(multi-word items split where the words are in different places). Every word was looked at on the master
(`output/ljs51/master/0084_NNNN.tif`), first in a line band, then in a 3x crop (saved in `output/ljs51/crops/err/`) where
the dots mattered. Readings give letters and dots as they stand. No reading was chosen because it scans better.

Verdicts: **a** = the record misread the page (page reading given); **b** = the page has the record's form, so a
suspected form is the compiler's or copyist's own variant or slip; **c** = not settled from the image (reason given).
"Cipher" quotes the chain record's own counts unless it says otherwise. Cipher groups were **not** recounted sign by sign
in this pass. The two fit checks below are letter-count arithmetic against the recorded sign totals.

Counts: a = 32, b = 56, c = 43 (total 131 rows).

| # | chain | folio/line | record | page | cipher | v | note | fit change |
|---|---|---|---|---|---|---|---|---|
| 1 | 2r.4 | 2r l.13 | بالجزء | بالعجز (ب ا ل, then an ع head over a ج bowl with its dot below, ز with its dot) | not counted | a | Water-stained but legible at 3x. Same letter count (6), so no change to the fit. |  |
| 2 | 2r.4 | 2r l.14 | ما للاستطاع | ما لا يستطاع (alif, lam-alif, then a tooth with two dots below and ت dotted above) | not counted | a | The suspected ما لا يستطاع is what the page has. Same letter count (10). |  |
| 3 | 2r.4 | 2r l.14 | ولو كان ما يستطاع | ولو كان ما يستطاع (no مما) |  | b | The page has ما. The metre wants مما, so the shortfall is the compiler's, not the record's. |  |
| 4 | 2r.4 | 2r l.13 | وما بدلت شكري للمشكور | وما ?? شكري للشا?ر: the third word looks like ٮعد/ٮٮد; the last word has two lams, a tooth with dots, kaf and ر |  | c | Stained. The last word does not clearly show the م and و of المشكور (للشاكر is possible). Not settled. |  |
| 5 | 2v.3 | 3r l.4 | لبي ... صلف | لبى ... صلف (ص, a tall lam, ف with its dot). The first letter of لبى is overwritten by a darker stroke (a correction). |  | b | The page has صلف, not صدق. The munsariḥ problem is in the text as written. |  |
| 6 | 3r.7 | 3v l.5 | منذ لذة | منذ لتذ (lam, a tooth with two dots above, a final dhal with its dot; no separate ta marbuta) | not counted | a | The letters stand as لتذ, and the sense is still unclear. Same letter count. |  |
| 7 | 3r.7 | 3v l.5 | لوعني | لوعتي (two dots stacked above the tooth after ع) | not counted | a | Same count. لوعتي "my anguish" construes. |  |
| 8 | 3r.7 | 3v l.5 | انها جت | ا, [dot above] ه-loop, ا, ج (dot below), ت: either انها جت or اهاجت |  | c | One dot sits above the ه loop. It may be a nun's dot (انها) or a stray mark (اهاجت "stirred up"). Not settled. |  |
| 9 | 4v.8 | 5v l.7-8 | سادر ... ها ... والمرق | سادر (no dot on ر) ... ها: ... والمرق (ق with two dots) |  | b | The page agrees with the record. The ṭawīl problem is in the text as written. |  |
| 10 | 5r.12 | 5v l.11-12 | كلبا / احطوما / النه | كلبا (ب dotted below) / احطوما / النه, all as recorded | not checked | b | All three acrostic misfits stand on the page. They are the compiler's, unless the cipher has the prayer letters (cipher not read here). |  |
| 11 | 6r.11 | 6v l.7 | مني وصلا لا شعر اضلها في قربه جبلا | ... منى وصلا لا شعرا(?) اضلها فى قربه جبلا: two alifs stand between شعر and the ض, so the page may read لا شعرا اضلها |  | c | The construe and metre problem is not resolved by the image. فدا لمن is also possible (a tall stroke after فدا). |  |
| 12 | 6v.11 | 7r l.3 | وما مصرا الا | وما مصر الا (one alif only, before the lam-alif) | record: 41 signs / 39 letters | a | The record counted the alif of الا twice. | letters 39 -> 38 against 41 signs |
| 13 | 7r.5 | 7r l.10 | يغلب صفوا ويكدر | يغلب صفوا او يكدر (صفو + tanwin alif, then a second alif + و) | record: 51 signs / 38 letters | a | The missing syllable of the ṭawīl is on the page (او). | letters 38 -> 39 |
| 14 | 8r.11 | 8v l.6 | يا ادم | ا ادم: alif, a second upright with a hamza-like mark, د, م. No ya, and no dotted nun tooth |  | a | Not يا. The suspected انادم is not supported (no nun tooth). Read أآدم / ا ادم. | letters 76 -> 75 against 88 signs |
| 15 | 8r.11 | 8v l.7 | بمنعه | يمنعه (two dots stacked below the first tooth) |  | a |  |  |
| 16 | 9v.3 | 9v l.13 | صفو الكدر | صفو (no ه), then the interlinear الكدر |  | b | The page has صفو. The suspected صفوه is not written. |  |
| 17 | 10r.2 | 10r l.10 | ... من دخان (verse ends) | ... من دخان + العرفج, written below the end of l.10 (above l.11) as the rhyme word | record: 87 signs / 77 letters | a | The missing -aj rhyme is on the page: من دخان العرفج. The record left out the word written below the line. | letters 77 -> 83 against 87 signs |
| 18 | 10v.1 | 10v l.7-9 | يحسن ... فاضل; معاز | يحسن (nothing follows on l.7); over فاضل an interlinear مسعا/مشفا فل; a further word above l.9 at the left (read at low resolution as متفضل, not verified); معاز as recorded |  | c | The interlinear words may be the missing hemistich ends, but they are not read with certainty. |  |
| 19 | 13r.11 | 13v l.7 | بكوه | بكوه, but the kaf's top bar is in a browner ink: the word was first written بلوه ("trial") and a bar was added to make the ل a ك | not checked | c | Page as finally corrected = record. Whether the original بلوه or the corrected بكوه is the text can be settled by the ل/ك sign of the cipher (not read here). |  |
| 20 | 13v.10 | 14r l.6 | نخيل البريد | skeleton ٮحٮل: one dot above the head, one dot above the second tooth, two dots below |  | c | The dots do not give one clean reading (نخيل / بخيل / خيل are all possible). |  |
| 21 | 14v.7 | 17r l.13 (poem 2 l.10) | بمنه | بمه (ب dotted below, م, ه; no nun) | not counted | a | بمه "mah!" is the answer word the commentary says is planted there. | letters 770 -> 769 |
| 22 | 14v.7 | 17v l.2 (poem 2 l.12) | ونم | و + an undotted tooth + م, with a small ring (sukun) above. Not an initial ه loop | not counted | c | نم or هم: the tooth has no ه loop but no dot either. The cipher (nūn and hāʾ are different classes) can settle it. |  |
| 23 | 14v.7 | 17r l.11 (poem 2 l.8) | وبلغني قاصديه | وبلقى قاصديه: و, a tooth with one dot below, ل, a closed ق/ف head with a dash above, final ى. No nun tooth | not counted | a | The page has a 5-letter word close to the suggested ويلقى ("he meets"). It is not وبلغني. | letters -1 |
| 24 | 19r.7 | 19v l.9 | قمرا اذا | قمر اذا (one alif) | record: 163 signs / 145 letters | a | The alif of اذا was counted twice. | letters -1 |
| 25 | 19r.7 | 19v l.11 | ومدد شددت | ومد شددت (و م د with a damma; only one dal) |  | a |  | letters -1 |
| 26 | 19r.7 | 19v l.11 | وحذف لرابع | نحذف(?) لرابعه: لرابعه with a final ه; the word before it starts with a tooth dotted above (no و seen) |  | a | لرابعه is on the page (+1 letter). The first letter of the حذف word is not settled. | letters +1 (net 145 -> 144) |
| 27 | 22r.1 | 22v l.4 | التناثر | التهاتر/التهاثر: ال, a dotted tooth, a hanging medial ه loop, ا, a dotted tooth, ر | not counted | a | The page has the ه the translation predicted (التهاتر "mutual abuse"). |  |
| 28 | 22r.1 | 22v l.5 | اخيا | لاقوا + a word with a ج/ح head (one dot inside the bowl) and يا |  | c | Neither اخيا nor حياء is clearly written. Not settled. |  |
| 29 | 22r.1 | 22v l.6 (interlinear) | الجوادر | الخوادر (dot above the ح head, none below) |  | a | This is the translation's guess الخوادر "lions in their lairs". |  |
| 30 | 22r.1 | 22v l.7 | هو / عارهو / انتقام / المعابر | كان هم وصما (one و between هم and صما) ... عاره وما ... الا اتقا المعابر (ا, a dotted tooth, ق, ا; no final م; المعابر with ب dotted below) | record: 171 signs / 165 letters | a | The suggested اتقاء is on the page as اتقا. The record doubled the و twice (همو و, عارهو و). المعابر stands, so المعاير is not supported. | letters 165 -> 161 |
| 31 | 22v.9 | 23r l.4-6 | لبني ... حذرا ... اثبتك عذرا | لبني (ب dotted below, ن dotted above) ... حذر ... اثبتك اعتذر (ا ث ب ت ك ا ع ت ذ ر). The second لبني has its dots differently placed (two below) |  | a | The piece rhymes in -ar (حذر / اعتذر / نذر). The first لبني is as recorded, the second is not settled. | net 0 |
| 32 | 24v.6 | 25r l.2 | يا قمر البلاغه ... المخادم | as recorded; المخادم with the dot above خ; الاقاليم is written above l.2 as the end of l.1 |  | b | The over-long basīṭ is in the text as written. |  |
| 33 | 25r.4 | 25v l.1 | طلب لك | طلب لك (no الي) | record: 86/84 signs / 81 letters | b | Written as recorded. The kāmil wants طلب اليك; if the cipher has the extra letters, the slip is the copyist's. |  |
| 34 | 25r.4 | 25v l.1 | تطلب [?] | نتطلب: three dots over the two teeth (one for ن, two for ت) | not counted | a |  | letters 81 -> 82 |
| 35 | 25v.4 | 25v l.13 | علمت ان | علمت ان: the ت runs straight into the alif; no ب tooth or dot |  | b | The page does not have بان. The wāfir problem is in the text as written. |  |
| 36 | 26r.12 | 26v l.9 | الوابه [?] | الوابه as recorded (ا ل و ا ب ه, ب dotted below) | record: 7 surplus signs | c | The page has no -ābu rhyme word. The 7 surplus signs point to a different word in the cipher, which was not recounted here. |  |
| 37 | 27v.3 | 27v l.12 | يا من اين | يا من اين as recorded | record: 5 surplus signs | b |  |  |
| 38 | 28v.1 | 29r l.2 | عندي يوماك | عند + a free-standing alif + يوماك (ي dotted below, و م ا ك) |  | b | The ك of يوماك is clearly written. The page also shows عند + alif where the record has عندي, which is not settled (c for that word). |  |
| 39 | 30r.4 | 30v l.2 | فقالت ان الشيخ | فقالت اظن/اطن الشيخ (ط between the alif and the ن; one dot near it) | record: 121 signs / 109 letters | a | اظن "I think" fills the missing wāfir syllable. | letters 109 -> 110 |
| 40 | 31r.2 | 31r l.7 | اري (record) / ارى (gloss) | اري |  | b | Spelling only. |  |
| 41 | 33r.4 | 33v l.1-2 | فجي بمثل قول الحاجري / النوم منكور | as recorded |  | b |  |  |
| 42 | 33v.6 | 33v l.11 | حلي, فخد, ونظر | as recorded at band scale (فخد with no dot on د) |  | c | The 3x crop missed the word. Not re-read. |  |
| 43 | 33v.12 | 34r l.4 | كيما ... تخنف | as recorded |  | b |  |  |
| 44 | 34r.8 | 34v l.4 | سيأها ... بما عملك سام | as recorded |  | b |  |  |
| 45 | 34v.6 | 35r l.1-2 | ينيف [?] ... تطيف [?] | a tooth with two dots below + ?ٮف (يميف/ينيف); the line end starts with a tall stroke or a dotted tooth (لطيف / نطيف) |  | c | Dots ambiguous. تطيف (two dots) is not what the page shows. |  |
| 46 | 35v.8 | 36r l.8-9 | كم [?] ... بازدكرن [?] ملحلا [?] | كم من (the stroke after كم is the tail of the م) ... باز دكرن ملحلا as recorded |  | c | The end of the line is not Arabic as written. The vocative the compiler mentions is not visible. |  |
| 47 | 36r.11 | 36v l.11 | احوم | احنو (ا, ح, a tooth with one dot above, و) | not counted | a | The translation's احنو is what the page has, and it ends in و, as the compiler says. | same count (4) |
| 48 | 37r.1 | 37r l.7 | فقيل العشيه | فقبل العشيه (one dot below the tooth after ق) | not counted | a | fa-qabla l-ʿashiyya "before evening". Same count. |  |
| 49 | 37v.12 | 38r l.8-11 | ففع [?] ... نفد | as recorded (cant) | record: 97 signs / 90 letters | c | Cant words. Their word division cannot be checked against sense. |  |
| 50 | 38v.10 | 39r l.7 | ابا [?] | ابا (one dot below) |  | b | The page has ابا. The sense wants ايا, so this is the compiler's slip. |  |
| 51 | 39r.10 | 39v l.10 | دايبه | دايبه | record: 5 letters confirmed | b |  |  |
| 52 | 39v.12 | 40v l.1 | عن | عن | record: 3 signs | b | The written word is عن. The cipher has 3 signs (not recounted). |  |
| 53 | 40v.5 | 40v l.13 | من الله ما زال | من الله ما زال (من joined to الله) |  | b |  |  |
| 54 | 41r.3 | 41r l.9 | من صب في خديه دمعة | not re-cropped (the band showed l.10-11) | record: exact count | b | The count fits exactly, and no misreading was suspected. |  |
| 55 | 42v.3 | 42v l.11-12 | سالت خطا ... قصب [?] | as recorded (بهواني written above the line end) |  | b |  |  |
| 56 | 43r.6 | 43r l.9 | هل بفك جود | as recorded | record: زمانا 6 signs for 5 letters | b |  |  |
| 57 | 43v.11 | 44r l.5-6 | من جبت [?] / الاناعم [?] وادقه | as recorded | record: groups 4+6 against 3+7 | c | The written words are as recorded. The word division lies in the cipher. |  |
| 58 | 44r.10 | 44v l.4 | وان | وان (لك in the right margin) | record: وانت | b | The cipher's وانت is a variant of the written وان. |  |
| 59 | 44v.9 | 44v l.13 | ومسي | ومسيء (a hamza is written over the final ya) | record: cipher = written letters | a | Spelling. The hamza gives musīʾi, which fills the missing ṭawīl syllable. |  |
| 60 | 45r.11 | 45v l.6 | الاولى | الاولى | record: الاوايل | b | The cipher's الاوايل is a variant. |  |
| 61 | 45v.13 | 46r l.8 | باعفاي من وزارة الشام | as recorded |  | b |  |  |
| 62 | 46r.11 | 46v l.8 | سامها | سامها | record: 4 signs for 5 letters | b |  |  |
| 63 | 47r.1 | 47v l.5-7 | ولا طعام / وهم / هروت مروت / الكرث / يستانفنه | ولاطعام, وهم, وما هروت ?روت (the second word's first letter is unclear), الكرث, يستانفنه | record: cipher writes يستنفنه | c | Not understood. The page agrees with the record except for the doubtful م of مروت. |  |
| 64 | 57v.4 | 57v l.13 | رونقا | رونقا (و written) | record: رنقا, 4 signs | b | The written text is right. The cipher (and red gloss) drop the و. |  |
| 65 | 55r.7 | 55v l.1 | افما نهاك يا سعاد نهاك | as recorded |  | b |  |  |
| 66 | 55v.5 | 55v l.13, 56r l.1 | كمابه / في سما علما | كمابه حكما / في سما علما as recorded | record: count fits كمابه | b | In the compiler's text, not the record. |  |
| 67 | 59r.2 | 59r l.9 | كانشاء | كانشاء (with hamza) | record: groups 3+3, second like نشا | b | Page = record. The cipher has كان نشا or similar: a variant (not recounted). |  |
| 68 | 49v.2 | 49v l.10, l.12 | خدك ... قطنة / وان ذكرهم | خدك (the dot is above the ح head); فطنة/قطنة still open; l.12 as recorded |  | b | The page does not have حدك. |  |
| 69 | 54v.9 | 55r l.2 | نديمي قم فاسقني | as recorded |  | b |  |  |
| 70 | 53r.3 | 53r l.7 | ما اوليتني يا ولي كل على | as recorded (ما written above مطلق) |  | b |  |  |
| 71 | 51r.5 | 51v l.7 | بدر من بحر علم تدفق | as recorded |  | b |  |  |
| 72 | 50v.1 | 51r l.3 | رسايلكم الله لنا | رسايلكم انس لنا (alif, an undotted tooth, س; no lam-lam-ha) | record: 85 signs / 86 letters | a | رسايلكم انس لنا "your letters are company for us". | letters 86 -> 85 = 85 signs (exact) |
| 73 | 57r.2 | 57r l.8 | يثنيك / فبصدق / يطمين | as recorded |  | b |  |  |
| 74 | 51r.10 | 51v l.4-5 | علمت / يغيب (dotted بغيب) | علم + a tooth with one visible dot + an alif joined to it + نك (علمنا نك or علمت انك); يغيب: the crop missed the word |  | c | One visible dot on the tooth points to ن (علمنا), but the alif is shared. Not settled. |  |
| 75 | 60v.2 | 60v l.11 | ذكرنا (dotted ذكريا) | not resolved at the crop taken |  | c | The 3x crop missed the word. |  |
| 76 | 67r.8 | 67v l.1 | الشنا [?] | الشتا (two dots stacked vertically above the tooth) | not counted | a | The "kaf of winter" the compiler names. Same count. |  |
| 77 | 67r.8 | 67v l.1 | فاق | فاق (ف dotted, ا, ق) |  | b | Written فاق. The compiler's كاف may be a play on it. |  |
| 78 | 64r.3 | 64r l.11 | بعض / مشفو / مص | ٮعض (an undotted first tooth) / مشفو (ends in و; a brownish mark above, possibly the qaf the record mentions) / مص | record: مص 3 signs | c | يعض and بعض share the skeleton. مشفق is not written out. The cipher decides (not read here). |  |
| 79 | 72r.12 | 72v l.6 | فهمت | فهمت, with a gap before لفظا |  | b |  |  |
| 80 | 62r.3 | 62v l.8 | شحطت ديار كم | as recorded | record: 15 signs for 10 letters in the first three groups | c | The written text agrees with the record. The opening of the cipher differs (a "word of two words" beginning يا), which was not recounted. |  |
| 81 | 61r.3 | 61v l.1 | اسربع | اسربع (no dots on the س) |  | b | اشر is not written. |  |
| 82 | 65v.2 | 65v l.9-10 | خز[?]ج وخرج / ولسعوا / ورجع / خاسبه | خ?ج (cut by a paper crack) وخرج ولسعوا (no dots seen on the teeth) / ترجع ورجع / خاسبه | record: تخرج وتخرج, ولشعوا, وترجع, تحاسبه | b | The page agrees with the record. The cipher's forms are variants of the compiler's (first word physically damaged). |  |
| 83 | 63v.1 | 63v right margin (rotated) | ابري ... الاحور [?] ... بحور وثلثه [?] | ايري (two dots below the tooth) ... هذا لا يجوز (lam-alif, then a word with a dot below its head and ز dotted above) ... عندي يجوز (one dot below the head, a faint dot over the ز) [smudged word] تقليدا | tree script and sign cipher: ايري ... لا يجوز ... يجوز فنكته (keys_eye/63v.*) | a | The margin confirms ايري, لا يجوز and يجوز. The record split لا يجوز as الا حور and misdotted the rest. The word before تقليدا is rubbed out on the page and cannot be read there, so فنكته rests on the two ciphers (that word alone is c). | count stays 79 |
| 84 | 65r.5 | 65r l.13 | حزين [?] | حزي + an undotted final ن/و curve (حزيں) |  | c | The record's حزيو / حرنو is possible. Not settled. |  |
| 85 | 70r.11 | 70v l.5 | زرني [?] سعدي | زر + a ح-like head with a shadda + ي: زرني is not clear | record: 2+2 division | c |  |  |
| 86 | 72v.9 | 73r l.2 | مني [?] | م + an undotted tooth + ى (no dots at all) |  | c | منى / مني: not settled. |  |
| 87 | 70v.11 | 71r l.7 | تقل (compiler's wording) | تقل |  | b | Written تقل. Probably the compiler's slip for تقتل. |  |
| 88 | 66r.10 | 66v l.9 | اندبلت [?] | not resolved (the crop missed the word) | record: 5 signs | c |  |  |
| 89 | 65v.13 | 66r l.7 | لوقفني [?] | لوقفني as recorded | record: one 6-sign group | b |  |  |
| 90 | 67r.8 / 67v.9 / 68r.6 / 65v.13 | cipher | آمر / به / على / متيم | written as recorded (آمر seen on 67v l.2) | record: آمره; به 3 signs; على 2; متيم 3 | b | Divergences in the cipher, not in the written text. |  |
| 91 | 68v.2 / 68v.13 | 68v l.8-9; 69r l.7-10 | rare and coined words | not re-read |  | c | No single correction was proposed. |  |
| 92 | 78v.13 | 79r l.3 | اسيافا فاسفكن | one string اسيافاسفكن: ا س ي ا ف ا س ف ك ن, so only one فا. Read اسيافا سفكن | record: 39 signs; the word has 4 signs (سفكن) | a | The record doubled فا. With the page reading the chain fits exactly. | letters 41 -> 39 = 39 signs (exact) |
| 93 | 73v.8 | 74v l.6 | ويهنى | not resolved (the crop cut the word) | record: 5 signs | c |  |  |
| 94 | 77v.9 | 78r l.6 | ماتا / افنات | تفتنها ما + a tall stroke and dots that may be the verse-end mark and not تا | record: ends in the ta-ta pair; افنات 6 signs | c | Small, crowded line. Not settled. |  |
| 95 | 82v.7 / 83r.1 | 82v l.11-12 | اضمارا (assigned twice) | one word اضمارا, written once between l.11 and l.12 at the left: the end of the verse of 82v.7 |  | a | There is only one word. It belongs to 82v.7, and the 83r.1 heading should not carry it. |  |
| 96 | 74r.3 | 74v l.2 | ايا بحرا لجود | ايا نحرا لجود: the tooth of بحرا is dotted ABOVE; one alif (the tanwin alif) before لجود |  | c | The dot above is a copyist's slip for بحرا. The metre problem is not settled by the image. |  |
| 97 | 83r.1 | 83r l.6-7 | التناسا | التناسا | record: التناسيا | b | Spelling. The cipher is fuller. |  |
| 98 | 79v.10 | 80r l.3-5 | يشين / سراتها / تفوت | as recorded at band scale |  | c |  |  |
| 99 | 73r.5 | 73r l.12-13 | في / مو رياض | في; مو رياض lies under a paper crack | record: 3 signs for في | c | Physical damage (crack). |  |
| 100 | 82r.9 | 82v l.3 | فدا حالون / رزه | as recorded |  | c |  |  |
| 101 | 83v.12 | 84r l.7 | فقلنا [?] / احدى | فقلنا; احدى written with a joined first stroke | record: فقلت | b | The cipher's فقلت is a variant. |  |
| 102 | 84r.12 | 84v l.7 | ويمنك / وبينك | not resolved at band scale |  | c |  |  |
| 103 | 81r.5 | 81r l.12-13 | مزوجا / بطومار | مزوجا; بطومار |  | b |  |  |
| 104 | several (73v.8 ... 84r.12) | cipher | divergences in the cipher listed in the translation | written words not re-read one by one | record counts | b | Divergences in the cipher, not in the written text (record). |  |
| 105 | 85v.8 | 86r l.2 | يعتز بها | يعتر ٮها: the ت is dotted, the ر has NO dot, and the tooth after it is undotted, i.e. the letters of يعتريها | record: one 7-sign group, 4th sign = ر of الشريف | a | The suggested يعتريها is the page's own reading. The record's ز dot is not there. | same letters (7), now one word = one group |
| 106 | 90v.12 | 91r l.7 | يكررها | يكررها (band scale; the 3x crop missed the word) | record: يكرر, 4 signs (and the red gloss) | b | Written يكررها. The cipher and gloss have the metrical يكرر. |  |
| 107 | 86r.9 | 86v l.6 | فقلت ... جرحي | قلت (no ف) ... الى جرحني (a dotted nun tooth, band scale) | record: 5-sign word جرحني; قلت | a | Both forms are the cipher's. Net count 0. | net 0 (89 = 89) |
| 108 | 94v.5 | 94v l.12 | عبيدهم ... بعدهم | عبيد لهم (لهم written separately) ... بعدهم | record: لهم after عبيد; بعدهم group 6 signs | a | لهم is on the page (a). بعدهم is as written (b for that word; the cipher and 95r have بعهدهم). | letters 57 -> 58 |
| 109 | 90r.4 | 90r l.12 | فيذبل من شغلوف | as recorded at band scale |  | c |  |  |
| 110 | 92v.9 | 93r l.6-7 | قرنثمه / فيقتصك | as recorded at band scale (the end of فيقتص? is unclear) | record: 3+5 and 8 signs against 6 and 6 | c |  |  |
| 111 | 88v.10 | 89r l.1-2 | العذير [?]; holed second line | not re-read |  | c | Physical damage (hole). |  |
| 112 | 96r.2 | 96v | درنحوا [?] / القاكم / الرب وابقاكم | not re-read |  | c |  |  |
| 113 | 87r.3 | 87v l.1 | بات / بان | not re-read |  | c |  |  |
| 114 | 93v.7 | 93v l.11 | [م]دا [?] | blotted before دا |  | c | Physical (ink blot). |  |
| 115 | 95r.10 | 95v l.6 | فهذين | فهذين | record: count agrees | b |  |  |
| 116 | 86r.4 | 86r l.3 | تخميسها [?] | تخميسها / تخمسها at band scale |  | c |  |  |
| 117 | several (85r.5 ... 93v.7) | cipher | divergences in the cipher listed in the translation | not re-read one by one | record counts | b | Divergences in the cipher, not in the written text (record). |  |
| 118 | 102v.11 | 103r l.1 | وبقيت طرد | وبقيت طرد (the ت runs straight into طرد; no ما) | record: maqlub بيتقو + ام | b | Page = record. ما stands only in the cipher, so the omission is the copyist's. |  |
| 119 | 102r.1 | 102r l.8 | اذ جاوز | اذ جا وزحده (no ت) | record: 5 signs, first = ta | b | The page has no ت. The cipher's تجاوز is a variant. |  |
| 120 | 102r.1 | 102r l.9 | بشفين / نحرا / ثعال | بشفين (ب, ش, ف, ي dotted below, ن dotted) / نحرا / ثعال as recorded | record: 6 signs ending in ha (بشفتيه) | b |  |  |
| 121 | 103v.11 | 104r l.10 | هونت[ا?] | هونت الا: there is one alif only, and it belongs to الا | record: هونت, 4 signs | a | The bracketed alif is not a letter of هونت. | -1 if the alif was counted |
| 122 | 106r.11 | 106v l.2 | احج / واحتجت / حجي / المحتج / افلحت | the short forms as recorded; افلحت with an undotted ح | record: احتج / واحتججت / حججي / المحتجج, 42 signs | b | The page has the short forms, and the cipher's are fuller. افلحت against the compiler's correction افلجت. |  |
| 123 | 105r.11 | 105v l.3-4 | للجنة / للنار | للجنة (two joined lams); the second word shows only one tall stroke after فقلت (لنار / النار) | record: الجنة / النار | c | The first word is as recorded. The second is not settled. |  |
| 124 | 103v.2 | 103v l.8 | برار | برار | record: cipher also برار | b | In the piece as sent. |  |
| 125 | 105v.6 | 106r l.7-9 | عبيص / النجمت / ولا الست / العكروا | not re-read; the start of 106r l.7 is lost in a paper repair |  | c | Physical (repair). |  |
| 126 | 98v.10 | 99r l.2-3 | زوى / كامنا خفوق | not re-read |  | c |  |  |
| 127 | 101v.2 | 101v l.9 | دشا | the crop cut the first letter | record: grouping 4+2+3 (رشا) | c |  |  |
| 128 | 102r.1 | 102r l.8 | اذجا وزحده (spacing) | اذ جا وزحده |  | b | Spacing only. |  |
| 129 | 100r.8 | 100v l.2 | ولما فه | ولما فه | record: 3+3 | b | Spacing only. |  |
| 130 | 106v.6 | 106v | [..ه..] | damaged |  | c | Physical. |  |
| 131 | several (98r.13 ... 106v.6) | cipher | divergences in the cipher listed in the translation | not re-read | record counts | b | Divergences in the cipher, not in the written text (record). |  |

## Category (a): corrections

- 2r.4 (2r l.13): بالجزء -> بالعجز
- 2r.4 (2r l.14): ما للاستطاع -> ما لا يستطاع
- 3r.7 (3v l.5): منذ لذة -> منذ لتذ
- 3r.7 (3v l.5): لوعني -> لوعتي
- 6v.11 (7r l.3): وما مصرا الا -> وما مصر الا
- 7r.5 (7r l.10): يغلب صفوا ويكدر -> يغلب صفوا او يكدر
- 8r.11 (8v l.6): يا ادم -> ا ادم: alif, a second upright with a hamza-like mark, د, م. No ya, and no dotted nun tooth
- 8r.11 (8v l.7): بمنعه -> يمنعه
- 10r.2 (10r l.10): ... من دخان (verse ends) -> ... من دخان + العرفج, written below the end of l.10
- 14v.7 (17r l.13 (poem 2 l.10)): بمنه -> بمه
- 14v.7 (17r l.11 (poem 2 l.8)): وبلغني قاصديه -> وبلقى قاصديه: و, a tooth with one dot below, ل, a closed ق/ف head with a dash above, final ى. No nun tooth
- 19r.7 (19v l.9): قمرا اذا -> قمر اذا
- 19r.7 (19v l.11): ومدد شددت -> ومد شددت
- 19r.7 (19v l.11): وحذف لرابع -> نحذف(?) لرابعه: لرابعه with a final ه; the word before it starts with a tooth dotted above
- 22r.1 (22v l.4): التناثر -> التهاتر/التهاثر: ال, a dotted tooth, a hanging medial ه loop, ا, a dotted tooth, ر
- 22r.1 (22v l.6 (interlinear)): الجوادر -> الخوادر
- 22r.1 (22v l.7): هو / عارهو / انتقام / المعابر -> كان هم وصما
- 22v.9 (23r l.4-6): لبني ... حذرا ... اثبتك عذرا -> لبني
- 25r.4 (25v l.1): تطلب [?] -> نتطلب: three dots over the two teeth
- 30r.4 (30v l.2): فقالت ان الشيخ -> فقالت اظن/اطن الشيخ
- 36r.11 (36v l.11): احوم -> احنو
- 37r.1 (37r l.7): فقيل العشيه -> فقبل العشيه
- 44v.9 (44v l.13): ومسي -> ومسيء
- 50v.1 (51r l.3): رسايلكم الله لنا -> رسايلكم انس لنا
- 67r.8 (67v l.1): الشنا [?] -> الشتا
- 63v.1 (63v right margin (rotated)): ابري ... الاحور [?] ... بحور وثلثه [?] -> ايري
- 78v.13 (79r l.3): اسيافا فاسفكن -> one string اسيافاسفكن: ا س ي ا ف ا س ف ك ن, so only one فا. Read اسيافا سفكن
- 82v.7 / 83r.1 (82v l.11-12): اضمارا (assigned twice) -> one word اضمارا, written once between l.11 and l.12 at the left: the end of the verse of 82v.7
- 85v.8 (86r l.2): يعتز بها -> يعتر ٮها: the ت is dotted, the ر has NO dot, and the tooth after it is undotted, i.e. the letters of يعتريها
- 86r.9 (86v l.6): فقلت ... جرحي -> قلت
- 94v.5 (94v l.12): عبيدهم ... بعدهم -> عبيد لهم
- 103v.11 (104r l.10): هونت[ا?] -> هونت الا: there is one alif only, and it belongs to الا

## Corrections that change a chain's letter count against its signs

- 78v.13: 41 -> 39 letters = 39 signs (exact fit; the cipher's 4-sign سفكن).
- 50v.1: 86 -> 85 letters = 85 signs (exact fit).
- 10r.2: 77 -> 83 letters against 87 signs (the rhyme word العرفج).
- 22r.1: 165 -> 161 letters against 171 signs (اتقا, عاره, هم).
- 6v.11 (39 -> 38 against 41), 19r.7 (145 -> 144 against 163), 8r.11 (76 -> 75 against 88), 7r.5 (38 -> 39 against 51),
  25r.4 (81 -> 82 against 84-86), 30r.4 (109 -> 110 against 121), 94v.5 (57 -> 58 against 61), 14v.7 (770 -> 768 against 778),
  103v.11 (one fewer if the bracketed alif was counted).
- No change in count: 2r.4, 3r.7, 22v.9, 36r.11, 37r.1, 63v.1, 67r.8, 85v.8 (one 7-letter word now matches the one 7-sign group), 86r.9.

## Not done in this pass

- Cipher groups were not recounted sign by sign. All cipher figures are the records'.
- Rows marked c because a crop missed the word (33v.6, 51r.10 يغيب, 60v.2, 66r.10, 73v.8, 90v.12 at 3x) need one more crop.
- The "divergences in the cipher" groups (rows for 0126 #14, 0150 #13, 0174 #13, 0198 #13) were taken from the records, not re-read.
