# LJS 51: by-eye key tables, pilot report

By-eye key from the compiler's plaintext, not independently confirmed. One row per chain, written as each chain was
finished; details in `keys_eye/<chain_id>.json`. Consistency is over repeated shapes only (occurrences of shapes seen
twice or more in aligned pairs that take the shape's majority letter), at letter / skeleton level.

| chain | signs | letters | aligned pairs | shapes | singletons | consistency letter / skeleton | red agreement | verdict |
|---|---|---|---|---|---|---|---|---|
| 6v.11 | 41 | 39 | 38 | 18 | 7 | 97.0% / 97.0% (33 occ.) | n/a | consistent (simple substitution); 3 surplus signs + 1 dropped letter in فكل / شك / مصرا |
| 9r.7 | 72 | 76 | 72 | 18 | 2 | 100.0% / 100.0% (70 occ.) | n/a | consistent: one shape per letter (18 shapes = 18 letters), no exceptions; hamza never written, one alif dropped |
| 31r.2 | 43 | 43 | 43 | 17 | 8 | 100.0% / 100.0% (35 occ.) | 39/39 | consistent: one letter per shape, 39/39 red agree; ل has two shapes (ring, dot) |
| 57v.4 | 80 | 80 | 80 | 23 | 6 | 100.0% / 100.0% (74 occ.) | 80/80 | consistent: 80 signs = 80 letters, one letter per shape, 80/80 red agree; record's رنقا corrected to رونقا |
| 13r.11 | 40 | 40 | 40 | 12 | 2 | 97.4% / 100.0% (38 occ.) | n/a | consistent: 40 signs = 40 letters; ب and ي share S6 (skeleton cipher there); ل has a second shape S9 |

## Shared alphabets?

No. The five chains use five different alphabets: no two of them write the same letters with the same shapes. This is a comparison
by eye of the shape descriptions and crops in the five JSON files (by-eye key from the compiler's plaintext, not independently confirmed).

Shapes that occur in more than one chain, and the letter each chain gives them:

| shape | 6v.11 | 9r.7 | 31r.2 | 57v.4 | 13r.11 |
|---|---|---|---|---|---|
| numeral ٢ (a hook on a stem) | ض (ا once) | ن | ر | - | ر |
| ٨ / Λ | ل | ف | ع | - | - |
| ٣ with a descender | ا | (ψ fork = ت) | م | - | - |
| ے with a small head | ف (سے) | - | ا | ه | ن |
| small ring ٥ | - | - | ل | ي | - |
| ٦ (a hook on a stem) | - | - | ت | ر | - |
| comb ш over an underbar | ش | - | - | - | ف |
| ayn-like ع / ε | ق | ا | ي | (boxed ع = ح) | - |
| arch Π | - | ح | - | ا (with a long leg = ل) | - |
| ط-like sign | ع | - | ظ (looped) | ط (lying down) | ط (squared) |
| toothed crown | - | س (ᴍ, two triangles) | - | ق (M, three legs) | س (three prongs with a knob) |

- The repeated shapes take different letters in nearly every case: ٨ is ل, ف and ع in three chains; ٣ is ا in 6v.11 and م in 31r.2;
  the ring is ل in 31r.2 and ي in 57v.4; ے is ا, ه and ن.
- Where two chains agree, it is one letter, not an alphabet: ٢ = ر in 31r.2 and 13r.11, but their other letters all differ (ل ring vs
  S-curve, ك flat L vs U with a tall stem, ن lam-alif vs ے, ه ٤ع vs a loop on an upright, و a large 6 vs a bulb). A ط-like sign is ط in
  57v.4 and 13r.11 (drawn differently), and a toothed crown is س in 9r.7 and 13r.11 (two triangles vs three prongs with a knob). These
  look like the same habit, deriving a sign from the plain letter's own shape (ط from ط, the teeth of س), not a shared key.
- The kinds of system differ too: 9r.7 and 57v.4 have exactly one shape per letter; 31r.2 has a second ل (a dot); 13r.11 uses one shape
  for ب and ي (S6) and a second ل; 6v.11 has a second shape where ا is expected (S9, otherwise ض).

Conclusion: each of the five pilot chains is its own substitution alphabet. A key built from one chain will not read another, so the
full run has to build a table per chain (or per run of chains on one folio by one encipherer), not one table for the book.

## f. 63v: sign cipher 63v.1 and tree script 63v.trees

By-eye key from the compiler's plaintext, not independently confirmed. Details in `63v.1.json` and `63v.trees.json`; contact
sheet of the 79 trees in `output/ljs51/keys/63v_trees_sheet.png`.

| chain | signs | letters | aligned pairs | shapes | singletons | consistency letter / skeleton | red agreement | verdict |
|---|---|---|---|---|---|---|---|---|
| 63v.1 | 79 | 79 | 79 | 24 | 8 | 100.0% / 100.0% (71 occ.) | n/a | consistent: one letter per shape; ص two shapes (S8, S17), ل two (S7, S21 in لا); needs the corrected plaintext |
| 63v.trees | 79 | 79 | 79 | (branch counts) | - | 78/79 trees fit the count rule | 78/79 (3.15 under a tear) | consistent: right branches = abjad word, left branches = place in the word |

**Plaintext correction.** Both ciphers, read independently, give the couplet as
ايري كبير والصغير يقول لي اطعن حشاي به وكن صنديدا / ناديت هذا لا يجوز فقال لي عندي يجوز فنكته تقليدا
(a bawdy couplet), not the record's ابري ... الاحور ... بحور وثلثه. Four words change: ايري, لا يجوز, يجوز, فنكته. The red letters over
the trees already say so (the 13 positions the pilot marked doubtful or mismatched are exactly these words), and the sign cipher uses the
same shape for ي in ايري and يجوز as in all other ي, and spells يجوز identically twice (S2 S22 S6 S23). The margin skeleton is compatible
(لايجوز joined resembles الاحوز). The chain records were not edited.

**Tree rule (qalam mushajjar).** Read right to left, rows top to bottom. Each tree is one letter: the number of branches on the viewer's
right gives the abjad word (1 ابجد, 2 هوز, 3 حطي, 4 كلمن, 5 صعف-, 6 قرشت, 7 ثخذ, 8 -غ), the number on the left gives the letter's place in
that word (ا = a Y with one branch each side; ب 2/1, ي 3/3, ر 2/6, غ 3/8). Agreement 78/79; the exception, 3.15 (ل), has its crown torn
(L3 R4 at face value). The order is Eastern (ش 3/6, غ 3/8) except ص = 1/5 in both its trees (Eastern gives 4/5): strict Eastern 76/79,
Maghribi 76/79. Tested and rejected: abjad numeral value as digit/rank (19/79), alphabetical order in 4- or 7-column grids (10-28/79).
Branch arrangement, stem height and arcs carry no letter information.

Key (left/right branch counts, letters attested in the 79 trees): ا 1/1, ب 2/1, ج 3/1, د 4/1, ه 1/2, و 2/2, ز 3/2, ح 1/3, ط 2/3, ي 3/3,
ك 1/4, ل 2/4, ن 4/4, ص 1/5, ع 2/5, ف 3/5, ق 1/6, ر 2/6, ش 3/6, ت 4/6, ذ 3/7, غ 3/8 (م, س, ث, خ, ض, ظ not attested).

## ff. 13r-24v

By-eye key from the compiler's plaintext, not independently confirmed. Plain 1-2x line crops of the master (no segmenter boxes;
`output/ljs51/crops/eye_<chain_id>/`), zooms on line ends and look-alike pairs; details and alignments in `keys_eye/<chain_id>.json`.
Where the cipher spells a word differently from the record's plaintext, the key is built on the text as enciphered and the fit
against the record's wording is kept in the JSON (`fit_against_record_wording`). Consistency over repeated shapes only.

| chain | signs | letters | aligned pairs | shapes | singletons | consistency letter / skeleton | red agreement | verdict |
|---|---|---|---|---|---|---|---|---|
| 13v.10 | 72 | 72 | 72 | 20 | 9 | 100.0% / 100.0% (63 occ.) | n/a | consistent: 72 = 72, one letter per shape; plaintext needs بمرسوم and بخيل (cipher) |
| 14v.7 | 778 | 770 | 756 | 15 classes | - | 95.5% (class level, 756 aligned) | n/a | summary only (tashifi, keyed in research/ljs51_pass/vet_tashifi.md): 15 sign classes = 15 skeleton classes, 722/756 in class |
| 18r.11 | 129 | 130 | 129 | 29 | 9 | 99.2% / 99.2% (120 occ.) | n/a | consistent once the plaintext is read from the cipher (يا من يفك الرمز ... يسقون بالما); homophones, two dal shapes as the compiler says |
| 19r.7 | 145 | 145 | 145 | 26 | 7 | 98.6% / 100.0% (138 occ.) | n/a | consistent: 145 = 145 (record 163 was the segmenter); U-loop sign writes د and ذ |
| 20r.8+47r.1 | 336 | 334 | 334 | 26 | 5 | 98.8% / 99.1% (329 occ.) | n/a | consistent: ONE cipher, riddle verses 1-5 (20r-20v) + 6-8 (47r); 20r-20v part 212 signs / 210 letters, 99.5% / 100% |
| 22r.1 | 167 | 167 | 167 | 32 | 10 | 99.4% / 99.4% (157 occ.) | n/a | consistent: lam-alif one sign and a separate first ta, both as the compiler says; e-loop ع twice, ز once |
| 22v.9 | 81 | 80 | 78 | 20 | 3 | 40.0% / 45.3% (75 occ.) | n/a | inconsistent with letter-shape classes (40%); count and repeats fit the plaintext; not keyed |
| 23r.9 | 125 | 125 | 125 | 22 | 4 | 99.2% / 100.0% (121 occ.) | n/a | consistent: 125 = 125; first word بي, بها, حبي (cipher and clear text) |
| 23v.12 | 37 | 37 | 37 | 14 | 2 | 100.0% / 100.0% (35 occ.) | n/a | consistent: 37 = 37; first word جيتماني (record حيتما[?]) |
| 24r.7 | 74 | 74 | 74 | 28 | 11 | 100.0% / 100.0% (63 occ.) | n/a | consistent: 74 = 74, no nulls (record 86 was the segmenter); ينسخر -> يتمسخر |
| 24v.6 | 81 | 89 | 81 | 21 | 5 | 88.2% / 88.2% (76 occ.) | n/a | partly consistent: letter-shape substitution; breaks in the لا-like and ا-like classes and at قمر البلاغه; 81 signs vs 89 letters |
| 46v.11+13r.1 | 77 | 77 | 77 | 23 | 8 | 100.0% / 100.0% (69 occ.) | n/a | consistent: one cipher of the two verses 13r l.5-7, split in ا|لاثام; 77 = 77, 69/69 |

### 20r.8 + 47r.1: one cipher of the eight-verse riddle

Quire 3 is bound out of place (identity_readings.md section 10), and the cipher bears it out: 20r l.8-20v l.13 is the first half
of the 47r riddle cipher, in the 47r alphabet and with the 47r key unchanged (`keys_eye/47r.1.json`). Keyed as one chain: 336 signs
against 334 letters, 26 shapes, 98.8% of repeated-shape occurrences on their letter (99.1% skeleton); the 20r-20v part alone (verses
1-5) is 212 signs for 210 letters, 206 of 207 (99.5%, skeleton 100%), 59 groups for 58 words. Verses 1-5 as enciphered:

فما وليد ربا في شهر مولده وعاد فيه قديم السن قد نحلا / وما ثياب وقد خيطت بلا ابر وما ادير لها سلك ولا فتلا /
وما فتى ان تهيا هيب جانبه ولا يهاب اذا في الملبس انتعلا / وما جبان لما عان في شرف ان ابطا ساعه مبناهما بطلا /
وما مساكن ترتاح القلوب لها يريدها القوم قد كانت لهم حللا

Against the recorded clear riddle (47r.1 `whole_riddle_as_read`) the cipher reads قد نحلا for مدخلا, وقد خيطت for قد خيطت,
ادير لها for ادبرها [?], تهيا for تهيبا, ان ابطا ساعه for ان لحظا اساعة [?], and writes جبان and ابطا with a second alif (the two
surplus signs). The clear text of 47r l.13-47v l.4 was not re-read on the master here. New shapes on 20r-20v: plain V (خ in خيطت,
ج in جبان), an open ha-like hook (ج in جانبه) and an H-ladder (ذ). The lone divider at the foot of 20v matches the dividers that
open 47r l.1-3 and 5.

### 21r l.1-5: the end of 48r.8, not part of 20r.8

The five rows on 21r l.1-5 (62 signs, 16 groups) are in the 48r.8 sign set (٧, 4-ayn, triangle-over-bars, Λ, X-man, long kaf ...)
and continue the f. 48r cipher. Its 27-label key directly supplies 59 of these values. The continuation also uses W2 for alif and EK for two letters (see `targets/ljs51f48r/reading.md`). The five lines give the close of the f. 21r rhymed prose, from exactly
where 48r.8 stops (after ربها جملته):

وان زادها رفعته فاذكر اسم ربك حين تاوي اليها واشكر نعمه ربك اذا استويت عليها

62 signs = 62 letters, 58 of 59 repeated-shape occurrences one letter per shape (the horned ha-like sign takes ح in حين and ش in
واشكر). Against the clear text (وازدها نعمته ... اذا استوت بك عليها) the cipher has وان زادها رفعته and استويت without بك. Slid
along the whole 293-letter prose, the 48r-key decode matches 44 of 62 letters at the tail and at most 11 anywhere else. So 21r
l.1-5 is the end of the fourth piece, and the فحللته سريعا لسهولته وهو on 21r l.6 is its solution: the top of f. 21r originally
followed f. 48v. That does not fit the quire-3-only model, which keeps 12v -> 21r; since 21v -> 22r reads on, quire 4 (ff. 21-28)
probably stood after f. 48 as well. The joins 12v -> ? and 28v -> 49r (49r.1 begins mid-verse) need checking. Details in
`20r.8+47r.1.json` (`block_21r_1_5`).

### Record errors found (chains_*.jsonl not edited)

- 13v.10: برسوم is بمرسوم (cipher, and the master can be read so); نخيل is بخيل (خيل البريد, post horses). 72 signs, not 77.
- 18r.11: the plaintext's unread middle is read from the cipher: يا من يفك الرمز فك الذي اقوله من غير اعيا / ما ذات قد رمق اهيف
  تاتيك في صبح وامسا / منكوسه الراس كم حزونه قد دقها الدهر بارزا / ترزق بالنار فراخا لها من بعد ما يسقون بالما. The interlinear
  وامسا belongs in the line; رمق is the cipher's reading, not checked on the master. 129 signs, not 133.
- 19r.7: 145 signs, not 163 (no name-riddle extra needed); the cipher has بنصفه and بحذف, and alif for final ى.
- 20r.8: 212 signs on 20r-20v (the record's 297 included 21r l.1-5); its plaintext is riddle verses 1-5, not the 21r prose.
- 22r.1: للحلم (not الحلم); حيا (not اخيا); الخوادر is the end of verse 2, not a variant of المعاشر; لهم عز, كان لهم, يخافون,
  المعاير. 167 signs, not 171.
- 23r.9: first word بي (record ي[?]); بها (not بهن); حبي (not حب). 125 signs, not 132.
- 23v.12: first word جيتماني (record حيتما[?]); 37 signs.
- 24r.7: 74 signs, not 86 (no nulls); ينسخر is يتمسخر.
- 46v.11 + 13r.1: the records' transcriptions are confirmed sign for sign.

## ff. 1r-12v

By-eye key from the compiler's plaintext, not independently confirmed. Every chain in `chains_0006_0029.jsonl` except 6v.11 and
9r.7 (pilot rows above). Plain 2x line crops of the master, 3x zooms on line ends and look-alike pairs
(`output/ljs51/crops/eye_<chain_id>/`); alignments, keys and shapes in `keys_eye/<chain_id>.json`. Where the cipher spells a word
differently from the record, the key is built on the text as enciphered (`plaintext_cipher_form`), with the record's text kept in
`plaintext_record`. Consistency is over repeated shapes only. Rows are segmenter line numbers.

| chain | signs | letters | aligned pairs | shapes | singletons | consistency letter / skeleton | red agreement | verdict |
|---|---|---|---|---|---|---|---|---|
| 1r.2 | 79 | - | - | 50 | 35 | - | red mostly unreadable | no plaintext: inventory only; 18 dividers, 19 groups; the readable red letters (about 40 of 79, few certain) form no words |
| 1v.3 | 90 | 90 | 90 | 20 | 5 | 100.0% / 100.0% (85 occ.) | 88/89 (1 skeleton-level: red ح over خ) | consistent: 25 groups = 25 words; 7 rows (l.3-9); second hemistich as enciphered: فقلت لهم قد لمت طرفي فقال لي اتمنعني من ان اساعد جاريا |
| 2r.4 | 79 (+3 under stain) | 82 | 79 | 21 | 3 | 100.0% / 100.0% (76 occ.) | n/a | consistent: 21 groups = 21 words; verse 1 ends وما بعد شكري للشكور مزيد, verse 2 opens ولو كان مما; answered in full |
| 2v.3 | 67 | 67 | 67 | 25 | 8 | 100.0% / 100.0% (59 occ.) | n/a | consistent: 17 groups = 17 words; قلبي, بنجواك, يخبرني |
| 3r.7 | 80 | 81 | 80 | 23 | 7 | 98.6% / 100.0% (73 occ.) | n/a | consistent: one alif dropped; S10 = د and once ذ; لية for لتذ, تذكر تعديد for تذكرنا عهد |
| 3v.12 | 42 | - | 0 | 26 | 15 | - | n/a | not keyed (inventory): its 11 groups take neither bayt of the record's text as a simple substitution (best fit 25/42 signs, chance level) |
| 4r.9 | 37 | 37 | 37 | 17 | 7 | 100.0% / 100.0% (30 occ.) | n/a | consistent: the verse without قالت, 10 groups = 10 words; م has two shapes (S2, S16) |
| 4v.4 | 37 | 37 | 37 | 14 | 4 | 100.0% / 100.0% (33 occ.) | n/a | consistent: 10 groups = 10 words; one shape per letter, no homophones; plaintext confirmed letter for letter |
| 4v.8 | 87 | 86 | 86 | 24 | 8 | 100.0% / 100.0% (79 occ.) | n/a | partly consistent: one surplus stroke (S24) in ومال; the 5r rows belong (حديثكم runs over the page turn); both bayts present |
| 5r.12 | 51 | 51 | 51 | 19 | 5 | 100.0% / 100.0% (46 occ.) | n/a | consistent once corrected: رايت بحلب اسدا حطوما ... وسط هالته بدره تبهر; the word initials give the compiler's second wording رب احفظ ما وهبت |
| 6r.11 | 86 | 86 | 86 | 24 | 7 | 100.0% / 100.0% (79 occ.) | n/a | consistent: 21 groups for 22 words (يهدي مني is one group); the second وردا is written ودرا |
| 7r.5 | 44 | 44 | 44 | 19 | 8 | 97.2% / 100.0% (36 occ.) | n/a | consistent: the whole of l.10 plus a closing مشربا; S5 = ع and غ; قذا for هذا |
| 7r.12 | 87 | 87 | 87 | 25 | 7 | 98.8% / 100.0% (80 occ.) | n/a | consistent: 29 groups = 29 words; S23 = ذ and د; 8 words differ from the record |
| 7v.12 | 92 | 92 | 92 | 23 | 8 | 98.8% / 100.0% (84 occ.) | n/a | consistent: 26 groups = 26 words; the 7v rows belong; ح and م transposed in الحمبة |
| 8r.11 | 82 | 82 | 82 | 21 | 6 | 97.4% / 97.4% (76 occ.) | n/a | partly consistent: S8 = ق and ن, S12 = ل and once ن; first word انادم; the interlinear ام ناسي is enciphered |
| 8v.10 | 75 | 75 | 75 | 21 | 8 | 100.0% / 100.0% (67 occ.) | n/a | consistent: the 9r row is the end of the verse (بلا طبيب) |
| 9v.3 | 87 | 87 | 87 | 24 | 7 | 98.8% / 98.8% (80 occ.) | n/a | consistent: 23 groups = 23 words, with the interlinear القدر enciphered; سيتبع ... صفوه |
| 10r.2 | 78 | 78 | 78 | 28 | 13 | 100.0% / 100.0% (65 occ.) | n/a | consistent: no درر نثرن in the cipher; الفيروزج |
| 10v.1 | 70 | 73 | 70 | 29 | 12 | 100.0% / 100.0% (58 occ.) | n/a | consistent: lam-alif is one sign (S19, as the compiler says); the hamza of عطاء is not written; 5 plaintext corrections; answered in full |
| 10v.13 | 40 | 41 | 40 | 15 | 6 | 94.1% / 94.1% (34 occ.) | n/a | consistent: ring S7 = ي and the ئ seat; the verse goes on لي وعائد |
| 11r.5 | 32 | 32 | 32 | 11 | 4 | 100.0% / 100.0% (28 occ.) | n/a | consistent, one-to-one; word 2 is ي?تال (يختال?), not جنانك; قلت, not فقلت |
| 11r.10 | 90 | 90 | 90 | 25 | 9 | 97.5% / 98.8% (81 occ.) | n/a | partly consistent: S6 (ل) once for the د of العماد; two bayts rhyming in -ارت once corrected; the interlinear اذا دارت is enciphered |
| 11v.11 | 42 | 43 | 42 | 18 | 7 | 100.0% / 100.0% (35 occ.) | n/a | consistent: the hamza of المرء is not written; سره, not ستره |
| 12r.8 | 82 | 82 | 82 | 23 | 9 | 91.8% / 97.3% (73 occ.) | n/a | consistent at skeleton level once corrected: S10 = ي x6 and ص x2; the interlinear القايل and دلايل are enciphered; answered in full |
| 12v.8 | 41 | - | - | 17 | 7 | - | n/a | no plaintext: inventory only; 9 dividers, 9 groups (6,5,4,5,4,5,2,4,6) |
| 12v.11 | 33 | - | - | 17 | 6 | - | n/a | no plaintext: inventory only; 9 dividers, 9 groups (4,2,7,4,3,3,4,4,2) |

Summary: 22 of the 23 chains with a plaintext key as simple substitutions (skeleton consistency 94-100%), but only on the text
as enciphered. In 19 of them the record's plaintext needs one or more word corrections, and the divider groups then match the
words exactly. Interlinear "variants" on the page are enciphered text in 6r.11 (طلا), 7v.12 (اوا اح), 8r.11, 9v.3, 10v.1 (متفضل),
11r.10 and 12r.8. The records' segmenter-based sign counts are mostly too high (2r.4 85 -> 79, 7r.5 51 -> 44, 12r.8 98 -> 82).
3v.12 is the one chain that does not take its plaintext.

### Record errors found, ff. 1r-12v (chains_*.jsonl not edited)

- 1v.3: 7 rows (l.3-9), not 6; 90 signs, 24 dividers; فما بال (not فمالي), لمت (not لمتم), اتمنعني (not استغفر), من ان اساعد (not من ذا ان غدا).
- 2r.4: 79 signs + 3 under the stain (not 85), 21 dividers (not 18); بركم (not بره); verse 1 ends وما بعد شكري للشكور مزيد (the small مزيد belongs to the verse); ولو كان مما; answered yes.
- 2v.3: 67 signs; قلبي (not لبي), بنجواك, يخبرني; the dropped-ta note does not apply here.
- 3r.7: 80 signs, 15 dividers; لية (not لتذ); تذكر تعديد (not تذكرنا عهد); لوعتي keeps its ي, so the "dropped ya" remark is not borne out.
- 3v.12: 42 signs (not 48); 4r l.4 has لان, not لدن; the signs do not take the record's text.
- 4r.9: confirmed; قالت is not enciphered.
- 4v.4: 37 signs (not 38), 9 dividers (not 8), 10 groups = 10 words.
- 4v.8: 87 signs (not 94; the 5r figures counted show-through); بالخمر, سادتي (tentative, not سادر), ها هي, والمروه (not والمرق); the 5r rows belong.
- 5r.12: 51 signs, 12 dividers; the chain ends in a 4-sign column turned 90 degrees in the left margin of 5v; بحلب (not كلبا), حطوما, وسط هالته, بدره تبهر.
- 6r.11: 86 signs (not 91), 21 dividers; لمن, شعرا, اضل بها, and a final وطلا.
- 7r.5: 44 signs (not 51), 13 dividers; the whole line is enciphered; قذا (not هذا); closing group مشربا; answered yes.
- 7r.12: 87 signs (not 93), 30 dividers; حروفك, تقلق, يشتط, عاش (no ولو), نفس, سمع, بو قط; the cipher writes تنقط for تسقط.
- 7v.12: 92 signs (not about 102), 26 dividers; the 7v rows belong; الحمبة, لم, اوا اح, رميت, بح, كح, عيني, وشحصد; answered yes.
- 8r.11: 82 signs (not 88), 22 dividers; انادم (neither يا ادم nor the errata's ا ادم); ام ناسي is part of the verse.
- 8v.10: 75 signs (not 83), 18 dividers; the 9r row is بلا طبيب, the end of the verse.
- 9v.3: 8 rows on segmenter lines 2-9 (not 7 on 3-10); 87 signs, 23 dividers; القدر is enciphered; سيتبع / صفوه; the "lam-alif sign" is two touching signs (ك + د).
- 10r.2: 78 signs, 18 dividers; no درر نثرن; الفيروزج.
- 10v.1: 70 signs, 17 dividers; محسن متغافل, معان, للغريب, متفضل; ولعمري انه هو كذلك is the compiler's comment.
- 10v.13: 40 signs, 10 dividers; the interlinear وعابد is وعائد and the verse ends طبيب لي وعائد.
- 11r.5: 32 signs (not 33); word 2 ي?تال; قلت.
- 11r.10: 90 signs (not 97), 23 dividers; غربلت, لمن زارت, والخلق, نقت وقد, واختارت, بدو (the page has شدو), وهم زوجها, يظعن (tentative), اذا دارت.
- 11v.11: 42 signs, 10 dividers (not 14); سره; rows are segmenter l.10-12 + one sign on l.13.
- 12r.8: 82 signs (not 98), 20 dividers; لا لاني بحت (not لا ابتخت), نجب, القايل (not القابر), دلايل; answered yes.
- 12v.8: 41 signs, 9 dividers (not 12). 12v.11: 33 signs, 9 dividers (not 11). 1r.2: 79 signs, 18 dividers, rows are segmenter l.2-7; the red ض is a flat stroke at 3x.

## ff. 25r-36v

By-eye key from the compiler's plaintext, not independently confirmed. Plain 1-2x line crops of the master (no segmenter boxes;
`output/ljs51/crops/eye_<chain_id>/`), zooms on line ends and look-alike pairs; signs counted by eye; where the cipher spells a word
differently from the record, the key is built on the text as enciphered and the fit against the record's wording is kept in the JSON
(`fit_against_record_wording`). Signs drawn as Arabic letters are sorted by shape. 31r.2 was done earlier (row above). No chain here has a red gloss.

| chain | signs | letters | aligned pairs | shapes | singletons | consistency letter / skeleton | red agreement | verdict |
|---|---|---|---|---|---|---|---|---|
| 25r.4 | 84 | 84 | 84 | 20 | 5 | 98.7% / 100.0% (79 occ.) | n/a | consistent; needs اليك for the record's لك |
| 25v.4 | 72 | 73 | 72 | 24 | 10 | 100.0% / 100.0% (62 occ.) | n/a | consistent; cipher has بان for ان; انشب in 3 signs; word-initial ي shape |
| 26r.1 | 74 | 75 | 74 | 19 | 3 | 100.0% / 100.0% (71 occ.) | n/a | consistent; ه of وآخره not written |
| 26r.12 | 81 | 81 | 81 | 19 | 4 | 100.0% / 100.0% (77 occ.) | n/a | consistent; last words ابوابه العرب (record الوابه); numeral shapes, plain substitution |
| 26v.11 | 79 | 79 | 79 | 20 | 5 | 100.0% / 100.0% (74 occ.) | n/a | consistent; record text confirmed |
| 27r.10 | 23 | 23 | 23 | 14 | 9 | 100.0% / 100.0% (14 occ.) | n/a | consistent; شويخ confirmed |
| 27v.3 | 71 | 72 | 71 | 19 | 6 | 100.0% / 100.0% (65 occ.) | n/a | consistent; 71 signs, not 77 (no surplus); hamza of حماء not written |
| 28r.2 | 70 | 71 | 70 | 22 | 7 | 96.8% / 96.8% (63 occ.) | n/a | partly consistent: breaks in ه (three shapes, one also ن, one also ت); يجري for جرى |
| 28v.1 | 69 | 69 | 69 | 21 | 7 | 100.0% / 100.0% (62 occ.) | n/a | consistent; عندنا for عندي; يوماك confirmed |
| 29r.4 | 55 | 55 | 55 | 19 | 6 | 98.0% / 98.0% (49 occ.) | n/a | consistent but one sign writes ث (ثم) and ش (تنشرح): the compiler's ثم/تم note |
| 29v.2 | 76 | 76 | 76 | 21 | 6 | 98.6% / 98.6% (70 occ.) | n/a | consistent; كالحاظ; second تغازل has the م sign for ت |
| 30r.4 | 111 | 111 | 111 | 25 | 6 | 100.0% / 100.0% (105 occ.) | n/a | consistent; فانبعثت as enciphered; ق two shapes |
| 30v.7 | 81 | - | - | 19 | 4 | - | n/a | no plaintext: inventory only (`30v.7.json`); the 30r.4 key does not read it |
| 31r.11 | 56 | 56 | 56 | 16 | 5 | 100.0% / 100.0% (51 occ.) | n/a | consistent; 31r l.14 sign is the inserted ا of the first عادوا |
| 31v.11 | 90 | 90 | 90 | 25 | 11 | 98.7% / 100.0% (79 occ.) | n/a | consistent; margin column reads bottom to top and goes inside فهل on 32r l.3; الى ورده |
| 32v.3 | 76 | 76 | 76 | 21 | 6 | 100.0% / 100.0% (70 occ.) | n/a | consistent; ٩٩ is one sign (س); الخدود, فبهم as enciphered |
| 33r.4 | 88 | 90 | 88 | 24 | 8 | 96.3% / 96.3% (80 occ.) | n/a | partly consistent: الحاجري's six signs do not fit the key; منكور without م |
| 33v.6 | 44 | 45 | 44 | 19 | 8 | 100.0% / 100.0% (36 occ.) | n/a | consistent; علمك (record عملك); ب of مقابلي not written |
| 33v.12 | 51 | 51 | 51 | 17 | 8 | 97.7% / 100.0% (43 occ.) | n/a | consistent; السلاليم (record السلالم); the 2 on 34r l.1 is a sign |
| 34r.8 | 77 | 77 | 77 | 18 | 5 | 97.2% / 98.6% (72 occ.) | n/a | consistent, two single breaks (ي in سيأها, ع in عملك) |
| 34v.6 | 84 | 83 | 83 | 21 | 4 | 97.5% / 100.0% (80 occ.) | n/a | consistent; احييت (record اجبت), بمنيف (record ينيف); margin sign = ي of يكتب |
| 35r.6 | 82 | 81 | 80 | 27 | 10 | 98.6% / 100.0% (71 occ.) | n/a | partly consistent: homophones for ب, ن, س; false start (2 signs) before خبير; // is ا |
| 35v.8 | 71 | 71 | 71 | 23 | 11 | 98.3% / 98.3% (60 occ.) | n/a | consistent once read from the cipher: اي من ... كم رمز ... ما حل بان تذكرني ما حلا; fits all the compiler's remarks |
| 36r.11 | 74 | 75 | 74 | 18 | 4 | 95.7% / 98.6% (70 occ.) | n/a | partly consistent: the long-sin sign writes ن, ب and ش; غ of غيرك not written; keyed once on 36v |

### 30v.7 against the 30r.4 key

30v.7 (no plaintext): 81 signs, 19 shapes, 20 groups (lengths 5 2 3 3 2 2 7 3 7 4 4 7 3 4 4 2 3 7 5 4); commonest Cb (cup with a ball, 16),
3 (9), zigzag (8), chevron and ط-shape (7 each). Nine shapes are shared with 30r.4 (chevron, ٩, 3, ع on a flat base, ع with a tail, kaf, ㅈ,
٨, small comb; 35 of the 81 signs), but with the 30r.4 values the groups give no Arabic words (سغ, ·س·, غس·, سمغس ...), the 3-sign would
be غ though it is the second commonest sign, and the two commonest 30v.7 signs do not occur in 30r.4 at all (nor 30r.4's U = ا, ∇ = ن, ٣ = ل
in 30v.7). Same stock of shapes, different alphabet. Structure only: three 7-sign groups have the pattern X Y X _ _ X // with Cb as X (Cb
as ا would give rhyme words of the shape الا--اف/ال-ا-ا-); not tested further. No reading forced.

### Record errors found (chains_*.jsonl not edited)

- 25r.4: لك is اليك (cipher 4 signs). 25v.4: 72 signs (not 75); the cipher has بان for ان.
- 26r.12: the last word is ابوابه العرب, not الوابه [?] (العرب is the overflow under 26v l.9); 81 letters, 81 signs, no two-numeral letters.
- 26r.1: 74 signs = record. 26v.11: 79 signs (not 80). 27r.10: 23 signs (not 24). 27v.3: 71 signs (not 77); no surplus signs.
- 28r.2: the cipher has يجري for جرى and drops the ب of بالله. 28v.1: عندنا (cipher; clear text compatible), not عندي.
- 29v.2: كالحاظ, not كلحاظ; the thin strokes on l.5 are ك (with a dot), not doubtful signs; 76 signs (not 75).
- 30r.4: فانبعثت in the cipher; the record's plaintext has 110 letters, not 109; 111 signs (not 112).
- 31r.11: 56 signs (not 59). 31v.11: the margin column reads bottom to top and belongs inside فهل on 32r l.3, not after l.4; الىورده in the clear text is الى ورده, not الورده.
- 32v.3: الخدود (not الخد) and فبهم (not فهم); 76 signs: each doubled ٩٩ is one sign.
- 33r.4: 88 signs (not 89); الحاجري not matched (open). 33v.6: علمك, not عملك; 44 signs (not 43). 33v.12: السلاليم, not السلالم.
- 34v.6: احييت, not اجبت; بمنيف, not ينيف [?].
- 35r.6: 82 signs (not 85); the // strokes are ا; two abandoned signs at the end of l.6.
- 35v.8: the plaintext is اي من لطراز ملك مصر حلا كم رمز مترجم اتاه حلا / تشريفك لي لمر عيشي حلا ما حل بان تذكرني ما حلا
  (record: يا ... كم [?] من ... ما حل بازدكرن ملحلا); the small 4 on l.9 is an inserted ا and counts (71 signs).
- 36r.11: غ of غيرك not written in the cipher (record text otherwise confirmed).

## ff. 37r-48v

By-eye key from the compiler's plaintext, not independently confirmed. The signs were counted in reading order on line crops of the master. The percentages use repeated-shape occurrences only.

| chain | signs | letters | aligned pairs | shapes | singletons | consistency letter / skeleton | red agreement | verdict |
|---|---|---|---|---|---|---|---|---|
| 37r.1 | 49 | 49 | 49 | 17 | 6 | 90.7% / 93.0% (43 occ.) | 48/49 (skeleton 49/49) | consistent with two two-letter signs (V = ا/د, hook = ب/ي) as the style note says; فقبل confirmed |
| 37r.11 | 88 | 87 | 87 | 24 | 7 | 96.3% / 100.0% (81 occ.) | n/a | consistent; one surplus sign in ابث; ٦١ is one sign (ه) |
| 37v.12 | 92 | 90 | 90 | 22 | 3 | 94.3% / 95.4% (87 occ.) | n/a | partly consistent (cant): breaks only inside cant words where page and cipher differ; طخفخف, وبيذ اهو |
| 38v.10 | 89 | 89 | 89 | 16 | 1 | 98.9% / 98.9% (88 occ.) | n/a | consistent; first word ايا in the cipher (record ابا); ق and ك share one sign |
| 39r.10 | 87 | 87 | 87 | 25 | 9 | 100.0% / 100.0% (78 occ.) | n/a | consistent, one letter per shape; record text confirmed |
| 39v.12 | 101 | 100 | 100 | 22 | 7 | 98.9% / 98.9% (93 occ.) | n/a | consistent; one surplus sign and one break, both in the group for عن (40r l.7-8); س two shapes; 40v l.1 belongs |
| 40v.5 | 72 | 73 | 72 | 19 | 6 | 100.0% / 100.0% (66 occ.) | n/a | consistent, one letter per shape, no homophones; الله written with one ل |
| 41r.3 | 60 | 60 | 60 | 20 | 4 | 100.0% / 100.0% (56 occ.) | n/a | consistent; the cipher divides خد / يه; ي two shapes; needs بحره for the record's حمرة |
| 41v.8 | 42 | 42 | 42 | 15 | 4 | 100.0% / 100.0% (38 occ.) | n/a | consistent, one letter per shape; record text confirmed |
| 42r.2 | 104 | 104 | 104 | 21 | 6 | 98.0% / 99.0% (98 occ.) | n/a | consistent; one break (the ρ sign writes س and the ك of اتبكي); ك three shapes, ح two |
| 42v.3 | 79 | 79 | 79 | 27 | 11 | 95.6% / 97.1% (68 occ.) | n/a | consistent with lam-alif as one sign; three breaks (ط of خطا, ه of صبابة, ث of ثكلان); قصت in the cipher, not قصب |
| 43r.1 | 37 | 37 | 37 | 15 | 5 | 100.0% / 100.0% (32 occ.) | n/a | consistent: one letter per shape, one shape per letter; record transcription confirmed |
| 43r.6 | 35 | 34 | 34 | 17 | 9 | 100.0% / 100.0% (25 occ.) | n/a | consistent; one surplus sign (ن doubled in زمانا); third word بيك in the cipher (∇ = ي), not بفك |
| 43r.11 | 42 | 42 | 42 | 13 | 4 | 100.0% / 100.0% (38 occ.) | n/a | consistent: one letter per shape, one shape per letter; سقوني repeats sign for sign; record confirmed |
| 43v.11 | 89 | 89 | 89 | 23 | 6 | 98.8% / 100.0% (83 occ.) | n/a | consistent; 89 signs (margin < on 43v l.11 counts); الغمائم (record الغمام) and خبت (record جبت [?]); الاناعم, وادقه confirmed |
| 44r.10 | 84 | 84 | 84 | 19 | 5 | 100.0% / 100.0% (79 occ.) | n/a | consistent: one letter per shape, one shape per letter; the cipher has واين ذاك الواحد (record وان, its guess وانت) |
| 44v.9 | 42 | 42 | 42 | 13 | 4 | 100.0% / 100.0% (38 occ.) | n/a | consistent: one letter per shape, one shape per letter; فوا / عجبا two groups; ومسي without hamza |
| 45r.2 | 60 | 60 | 60 | 21 | 8 | 100.0% / 100.0% (52 occ.) | n/a | consistent; ي two shapes (cup, hooked P in ارقني); all six ر one shape (no ر homophone); ورقا without hamza |
| 45r.11 | 82 | 82 | 82 | 21 | 6 | 98.7% / 98.7% (76 occ.) | n/a | consistent; الاولى as on the master (record's الاوايل not enciphered; 82 = 82 with الاولى); one break (٣-loop writes ح x4 and ض once); و two shapes |
| 45v.13 | 67 | 67 | 67 | 19 | 3 | 100.0% / 100.0% (64 occ.) | n/a | consistent: one letter per shape, one shape per letter; record transcription confirmed |
| 46r.11 | 78 | 79 | 78 | 20 | 4 | 100.0% / 100.0% (74 occ.) | n/a | consistent; the cipher has لان الي وزارة شام (لأن ألي), not لانال; سامها written in 4 signs |

## ff. 49r-60v

By-eye key from the compiler's plaintext, not independently confirmed. The signs were counted in reading order on line crops of the master. The percentages use repeated-shape occurrences only.

| chain | signs | letters | aligned pairs | shapes | singletons | consistency letter / skeleton | red agreement | verdict |
|---|---|---|---|---|---|---|---|---|
| 49r.1 | 42 | 42 | 42 | 18 | 7 | 100.0% / 100.0% (35 occ.) | n/a | consistent: 42 = 42, 12 groups = 12 words; ي three shapes, د two; record transcription confirmed (its Q/Q2 one shape) |
| 49v.2 | 86 | 85 | 85 | 23 | 6 | 100.0% / 100.0% (79 occ.) | n/a | consistent once read from the cipher: verse 2 ends من ابن دنينير او ابن دريهم (the 50r dispute), not وان ذكرهم; also حرك, قطرة (ق inserted), اوحدا, فانحل; 1 surplus margin mark |
| 50v.1 | 85 | 85 | 85 | 21 | 4 | 100.0% / 100.0% (81 occ.) | n/a | consistent: 85 = 85 (the text has 85 letters, not 86), 19 groups = 19 words; ج two shapes (جزازة, تجودوا), the compiler's slip; erased patch l.6 not counted |
| 51r.5 | 38 | 38 | 38 | 21 | 12 | 96.2% / 96.2% (26 occ.) | n/a | partly consistent: 38 = 38 and 12 groups = 12 words with جاد لي منك (record omits لي; the reply 51v.9 has it); breaks in the Ч-shapes (right-long Ч = ب twice and ل once; ل has three shapes) |
| 51r.10 | 68 | 68 | 68 | 19 | 5 | 100.0% / 100.0% (63 occ.) | n/a | consistent: 68 = 68 (the two itlaq alifs not enciphered; record 70), 19 groups = 19 words, one letter per shape; ا / و near twins told apart by the cap |
| 51v.9 | 48 | 48 | 48 | 21 | 7 | 100.0% / 100.0% (41 occ.) | 48/48 | consistent: 48 = 48 = 48 red, 15 groups = 15 words; ر two shapes (Rm x5, Tr x2), ك two (Kj, Ll), ي two; the two red ف are drawn like خ |
| 52v.4 | 51 | 51 | 51 | 20 | 5 | 100.0% / 100.0% (46 occ.) | 51/51 | consistent: 51 = 51 = 51 red, 14 words (قابل over the line end); one letter per shape; س two shapes; letter-shaped signs with other values (خ-shape = ب, ٮ = س, ط-shape = ت) |
| 53r.3 | 33 | 33 | 33 | 12 | 4 | 100.0% / 100.0% (29 occ.) | 33/33 | consistent: 33 = 33 = 33 red, 10 groups = 10 words; 12 shapes for the 12 letters the compiler counts, one to one |
| 53v.6 | 34 | 34 | 34 | 16 | 8 | 96.2% / 96.2% (26 occ.) | n/a | partly consistent: 34 = 34, 10 groups = 10 words; breaks only in the Π-form (ا in داب, ما; ه in منه); ا also has an H-form; ي (٣ with a loop) and ل (plain ٣) differ |
| 54r.2 | 39 | 39 | 39 | 17 | 7 | 100.0% / 100.0% (32 occ.) | n/a | consistent: 39 = 39, 9 groups = 9 words (three words over line ends); one letter per shape, one shape per letter |
| 54v.1 | 44 | 44 | 44 | 15 | 4 | 97.5% / 100.0% (40 occ.) | 44/44 | consistent: 44 = 44 = 44 red, 13 groups = 13 words; one sign writes ذ (ذو) and د (مدحه), the only break; 7 ج all the H-sign, 3 alifs |
| 54v.9 | 50 | 50 | 50 | 17 | 5 | 100.0% / 100.0% (45 occ.) | 50/50 | consistent: 50 = 50 = 50 red, 13 words (two over line ends); one letter per shape, one shape per letter; ف / ت near-twin signs kept apart by bowl size (and by the red dots) |
| 55r.7 | 74 | 74 | 74 | 20 | 7 | 97.0% / 100.0% (67 occ.) | n/a | consistent: 74 = 74 (record 75), 18 groups = 18 words; the Ω-arch writes ف (6) and ق (2), one skeleton; ر and ه two shapes each |
| 55v.5 | 80 | 80 | 80 | 20 | 4 | 97.4% / 97.4% (76 occ.) | n/a | partly consistent: 80 signs = 80 letters, 23 groups = 23 words once read from the cipher (يدري ما به حكما; يقضي في ما علما); 97.4% / 97.4% over 76 repeated occurrences; the only breaks are in ك: the abraded ك of وحاكم is drawn like the ل cup, the ك of ضميرك like the ص U-hook, and the ك of حكما has a shape of its own A second by-eye pass distinguishes the two kaf forms by the double tooth and gives 76/76. Both passes agree on every letter. |
| 56r.4 | 75 | 75 | 75 | 17 | 3 | 100.0% / 100.0% (72 occ.) | n/a | consistent: 75 signs = 75 letters, 19 groups = 19 words once read from the cipher (ولا حسن الا سماع حديثكم ..., and فانقلي); one letter per shape, one shape per letter; the numerals are a plain substitution (١ ي, ٢ م, ٤ ل, ٥ و, ٧ ف, ٨ ع); ١٤٨ is على, ١٤٨ H عليك The line-6 shaft may instead belong to the preceding lam, yielding 74 signs and فانقل as in the clear copy. |
| 56r.13 | 32 | 32 | 32 | 16 | 6 | 100.0% / 100.0% (26 occ.) | n/a | consistent: one letter per shape, one shape per letter; 32 signs (two erased signs on 56r l.13 not counted); record confirmed |
| 56v.8 | 31 | 31 | 31 | 18 | 9 | 100.0% / 100.0% (22 occ.) | n/a | consistent: one letter per shape, one shape per letter; 31 signs; same sign family as 56r.13, different alphabet |
| 57r.2 | 38 | 38 | 38 | 20 | 12 | 100.0% / 100.0% (26 occ.) | n/a | consistent; ش two shapes (the compiler's admitted slip), ي two; 38 signs; record confirmed (يطمين) |
| 58r.11 | 77 | 77 | 77 | 22 | 7 | 98.6% / 100.0% (70 occ.) | n/a | consistent; the curled T writes ب x2 and ن once (one skeleton); وثباته وثباته, عداته وعداته, both وكفت repeat sign for sign |
| 59r.2 | 49 | 49 | 49 | 15 | 2 | 100.0% / 100.0% (47 occ.) | n/a | consistent with verse 2 as enciphered (كنا ▱شا رشده فما نشا كما نشا); against the written كانشاء ... انشا 4 signs break; ▱ seen once, unread |
| 59v.7 | 29 | 29 | 29 | 7 | 0 | 100.0% / 100.0% (29 occ.) | 29/29 (skeleton 29/29) | consistent: 7 shapes for the 7 letters, one to one; red 29/29; record confirmed |
| 60r.5 | 72 | 72 | 72 | 19 | 3 | 100.0% / 100.0% (69 occ.) | n/a | consistent: one letter per shape; ع two shapes; 72 = 72 with اه / وا / شوقا as enciphered; record confirmed |
| 60v.2 | 78 | 78 | 78 | 22 | 8 | 100.0% / 100.0% (70 occ.) | n/a | consistent: one letter per shape, one shape per letter; لا يخطر in the cipher (record لا تخطر); 78 signs |

## ff. 61r-72v

By-eye key from the compiler's plaintext, not independently confirmed. The signs were counted in reading order on line crops of the master. The percentages use repeated-shape occurrences only.

| chain | signs | letters | aligned pairs | shapes | singletons | consistency letter / skeleton | red agreement | verdict |
|---|---|---|---|---|---|---|---|---|
| 61r.3 | 113 | 113 | 113 | 24 | 3 | 99.1% / 100.0% (110 occ.) | n/a | partly consistent: the marginal correction supplies a second rāʾ; the pendant sign takes both sīn and shīn in the recorded words. |
| 62r.3 | 32 | 32 | 32 | 18 | 9 | 100.0% / 100.0% (23 occ.) | n/a | consistent once the opening group is read: 32 signs = 32 letters, 7 groups = 7 words (5,4,6,4,6,4,3), one letter per shape (23/23 repeated); the cipher has a five-sign word يخوتا before شحطت (probably يا اخوتا, "O my brothers", written as one word: the "word of two words in Mushaf spelling" beginning with يا of the solving story), and دياركم as one group; tentative |
| 62v.10 | 36 | 36 | 36 | 19 | 12 | 100.0% / 100.0% (24 occ.) | n/a | consistent: 36 signs = 36 letters, 10 groups = 10 words; one letter per shape; ذ has two shapes (heart loop in اذا, φ-loop in العذال) |
| 64r.3 | 76 | 76 | 76 | 25 | 10 | 98.5% / 98.5% (66 occ.) | n/a | consistent once read from the cipher: 76 signs = 76 letters (with two composite signs), 20 groups = 20 words; one letter per shape except the 4-flag (ف x4 and ث in مكلثم); the text as enciphered has يعض (record بعض), مشفق (record مشفو) and يمص (record مص); و two shapes (2-hook, box), as the compiler says |
| 65r.5 | 64 | 58 | 58 | 24 | 5 | 100.0% / 100.0% (53 occ.) | n/a | consistent on the text as enciphered (tentative where marked): 64 signs including the 5 margin signs, 58 aligned to 58 letters, 53/53 repeated-shape occurrences on their letter; هن (not هيف), لي (not بي), صلب (not صلت); ناعم عريض completed from the l.7 margin through the arc (insertion) mark; the l.8 arc word (record حزين) not read |
| 65v.2 | 90 | 90 | 90 | 22 | 7 | 98.8% / 98.8% (83 occ.) | n/a | consistent once read from the cipher: 90 signs = 90 letters, 18 groups = 18 words; one letter per shape except the closed-head ε (د x3, ز in حازوا); the cipher reads تخرج ويخرج ويسعوا ... ترجع ويرجع ... تحاسبه مثلما يقعد يحاسبها (q-loop ت for her, d-loop ي for him) |
| 65v.13 | 77 | 76 | 76 | 18 | 5 | 100.0% / 100.0% (71 occ.) | n/a | consistent: 77 signs (one surplus) for 76 letters, 20 groups = 20 words, one letter per shape (71/71 repeated); لوقفني is لوقفتي in the cipher (triple arch = ت); ي of متيم not enciphered; ف has two shapes (فتى, لوقفتي) |
| 66r.10 | 72 | 72 | 72 | 22 | 6 | 100.0% / 100.0% (66 occ.) | n/a | consistent: 72 signs = 72 letters, 19 groups = 19 words, one letter per shape and one shape per letter (66/66 repeated); the record's doubtful اندبلت is enciphered ت ذ ب ل ت (تذبلت, i.e. the verb ذبل "to languish"); امتص confirmed |
| 66v.11 | 75 | 75 | 75 | 22 | 7 | 97.1% / 97.1% (68 occ.) | n/a | partly consistent: 75 signs = 75 letters, 19 groups = 19 words; breaks in the hook Hk (ق in قولك, القهوة; ل in هل) and the plain e-loop Ep (ف in فيمن, د in دنياه); ت has two shapes (ᔕ in ظفرت, ayn-hook in يغتنم) |
| 67r.8 | 72 | 72 | 72 | 20 | 4 | 100.0% / 100.0% (68 occ.) | n/a | consistent once read from the cipher: 72 signs = 72 letters, 19 groups = 19 words, one letter per shape (68/68 repeated); the first verse is من تحرز كافات الشتا كفاه مع حسن عطيته بمن ينشاه (the "kafs of winter" the compiler's comment names), not من خمر زكا فاق الشتا ... عفته ... انشاه; ن has two shapes (ዋ, Π), ت two (Δ-stem once) |
| 67v.9 | 78 | 78 | 78 | 18 | 2 | 100.0% / 100.0% (76 occ.) | n/a | consistent once read from the cipher: 78 signs = 78 letters, 25 groups = 25 words, one letter per shape and one shape per letter (76/76 repeated); the cipher has فيه where the record has به (the Ω-hook is ف as in يعرف, the middle sign the ي form); ا and ي are told apart by one tooth vs two under the ayn-head |
| 68r.6 | 55 | 55 | 55 | 20 | 5 | 100.0% / 100.0% (50 occ.) | n/a | consistent: 55 signs = 55 letters, 14 groups = 14 words, one letter per shape and one shape per letter (50/50 repeated); record confirmed; على has 3 signs (ع ل ي), not 2; the ن of من is under the worm track |
| 68v.2 | 79 | 77 | 77 | 25 | 6 | 100.0% / 100.0% (71 occ.) | n/a | consistent on the text as enciphered: 79 signs (2 under the stain) for 77 letters, 18 groups = 18 words, one letter per shape (71/71 repeated); the cipher reads يا هادمي ها دمي ... وخلصني اخير مما تعذبني وتمغصني تصل وترجع بهجرانك تنغصني بسي عسل وزنا بيسه ت..; ي has two shapes (initial L-hook, cup-hook); tentative in the singletons and the end |
| 68v.13 | 81 | 81 | 81 | 12 | 4 | 90.9% / 100.0% (77 occ.) | n/a | consistent at skeleton level: 81 signs = 81 letters, 20 groups = 20 words; 12 shapes for the 13 dotted letters, one letter per shape except ٣, which writes both ت and ث (77/77 at skeleton level, 70/77 at letter level: ت 9, ث 7); no undotted letter, as the compiler says; the cipher has بجنبي, تجنبتني and the pattern ـيبي (غيبي, جيبي, خيبي, شيبي) where the record reads نخبي, تجنبني, غبي, جبي, خبي, شبيي; the first word has ن where the record has ق (ثقبت) |
| 69r.12 | 68 | 68 | 68 | 23 | 9 | 100.0% / 100.0% (59 occ.) | n/a | consistent: all recurring signs retain their values, and two different signs represent jīm as the compiler records. |
| 69v.11 | 73 | 73 | 73 | 20 | 6 | 100.0% / 100.0% (67 occ.) | n/a | consistent once read from the cipher: 73 signs = 73 letters, 16 groups = 16 words; one letter per shape and one shape per letter (67/67); record ادمعي is مدمعي (cipher H = م, and the clear text on 70r l.9 has مدمعي), بهذا is فهذا in the cipher |
| 70r.11 | 82 | 82 | 82 | 24 | 8 | 100.0% / 100.0% (74 occ.) | n/a | consistent: the word division gives زر حي سعدى, and the repeated zāy supports فاز. |
| 70v.11 | 62 | 62 | 62 | 22 | 8 | 98.1% / 100.0% (54 occ.) | n/a | partly consistent: the repeated signs recover خيامهم and فيها رشا; the toothed-curve family covers both ʿayn and ghayn. |
| 71r.10 | 48 | 48 | 48 | 19 | 7 | 100.0% / 100.0% (41 occ.) | n/a | consistent: the exceptional opening and every subsequent word align, 48 signs in 13 groups. |
| 72r.12 | 67 | 67 | 67 | 24 | 10 | 100.0% / 100.0% (57 occ.) | n/a | consistent: the shorter cipher wording is ما فهت به لافظا. |
| 72v.9 | 72 | 71 | 71 | 21 | 3 | 100.0% / 100.0% (68 occ.) | n/a | consistent: 72 signs (one surplus) for 71 letters as enciphered, one letter per shape and one shape per letter (68/68); the third word is همي (همى, "poured"), not مني; واحيا is enciphered و ح ي ي; a lone ن-sign at the end of l.9 is surplus |

## ff. 73r-84v

By-eye key from the compiler's plaintext, not independently confirmed. The signs were counted in reading order on line crops of the master. The percentages use repeated-shape occurrences only.

| chain | signs | letters | aligned pairs | shapes | singletons | consistency letter / skeleton | red agreement | verdict |
|---|---|---|---|---|---|---|---|---|
| 73r.5 | 82 | 82 | 82 | 23 | 7 | 98.7% / 98.7% (75 occ.) | n/a | partly consistent: one shape has ن three times and ز once in عز. The other repeated shapes take one letter. |
| 73v.8 | 69 | 69 | 69 | 20 | 5 | 100.0% / 100.0% (64 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 74r.3 | 76 | 76 | 76 | 19 | 3 | 100.0% / 100.0% (73 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 75r.1 | 44 | 44 | 44 | 19 | 7 | 100.0% / 100.0% (37 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 76r.4 | 71 | 71 | 71 | 20 | 7 | 100.0% / 100.0% (64 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 76v.6 | 38 | 38 | 38 | 16 | 6 | 96.9% / 100.0% (32 occ.) | n/a | partly consistent: consistent at skeleton level: the small zig takes ظ twice and ط in بخط. Later ظ is written with an open loop on a sloping foot. |
| 77r.3 | 38 | 38 | 38 | 15 | 5 | 97.0% / 100.0% (33 occ.) | n/a | partly consistent: consistent at skeleton level: the small circle is ظ throughout except in بخط where it is ط. |
| 77r.10 | 85 | 85 | 85 | 22 | 4 | 98.8% / 98.8% (81 occ.) | n/a | partly consistent: the upright-bowl label takes م three times and ك in بذلك. Two figure-eight variants write ب. |
| 77v.9 | 94 | 94 | 94 | 21 | 8 | 100.0% / 100.0% (86 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 78r.12 | 88 | 88 | 88 | 33 | 20 | 100.0% / 100.0% (68 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 78v.13 | 39 | 39 | 39 | 17 | 8 | 96.8% / 96.8% (31 occ.) | n/a | partly consistent: the squared H with a closed foot is read ث in الثم and ل in اقبل; an additional stacked box also takes ل. |
| 79r.5 | 83 | 83 | 83 | 22 | 8 | 100.0% / 100.0% (75 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 79v.1 | 82 | 82 | 82 | 25 | 9 | 100.0% / 100.0% (73 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 79v.10 | 81 | 81 | 81 | 24 | 10 | 98.6% / 100.0% (71 occ.) | n/a | partly consistent: the dotted crescent gives ت five times and ب once. Other repeated shapes have one value each. |
| 80r.9 | 82 | 82 | 82 | 24 | 8 | 100.0% / 100.0% (74 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 80v.9 | 73 | 73 | 73 | 22 | 5 | 98.5% / 100.0% (68 occ.) | n/a | partly consistent: the open crossed loop covers ي and ت, which share a skeleton. Other repeated shapes remain consistent. |
| 81r.5 | 73 | 74 | 73 | 27 | 11 | 98.4% / 100.0% (62 occ.) | n/a | partly consistent: one short group and its repeated table-shape leave فلقد unresolved. Remaining word alignments use a consistent substitution. |
| 81v.6 | 68 | 68 | 68 | 19 | 6 | 100.0% / 100.0% (62 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 82r.9 | 85 | 85 | 85 | 19 | 5 | 97.5% / 98.8% (80 occ.) | n/a | partly consistent: two shapes have multiple values: the tall hook ع/غ shares a skeleton, and the dotted stem-bowl ز/م does not. |
| 82v.7 | 42 | 42 | 42 | 20 | 9 | 100.0% / 100.0% (33 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 83r.1 | 48 | 48 | 48 | 12 | 6 | 97.6% / 97.6% (42 occ.) | n/a | partly consistent: the four-like sign appears both for و and for ن in the final word. Other repeated shapes take a single value. |
| 83r.13 | 100 | 100 | 100 | 23 | 9 | 100.0% / 100.0% (91 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 83v.12 | 74 | 74 | 74 | 18 | 6 | 100.0% / 100.0% (68 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 84r.12 | 93 | 93 | 93 | 24 | 5 | 97.7% / 97.7% (88 occ.) | n/a | partly consistent: two letter assignments in اني conflict with otherwise regular shape values; all other groups have a consistent reading. |

## ff. 85r-96v

By-eye key from the compiler's plaintext, not independently confirmed. The signs were counted in reading order on line crops of the master. The percentages use repeated-shape occurrences only.

| chain | signs | letters | aligned pairs | shapes | singletons | consistency letter / skeleton | red agreement | verdict |
|---|---|---|---|---|---|---|---|---|
| 85r.5 | 30 | 30 | 30 | 16 | 9 | 100.0% / 100.0% (21 occ.) | n/a | consistent: all repeated signs keep one value. Two related shapes write ي. |
| 85r.10 | 79 | 79 | 79 | 16 | 3 | 96.1% / 97.4% (76 occ.) | n/a | consistent with shared signs for ت/ض and ب/ي and two distinct forms for ع. |
| 85v.8 | 70 | 70 | 70 | 22 | 9 | 100.0% / 100.0% (61 occ.) | n/a | consistent: the signs support يعتريها continuously, with the capped coil of ر and the bent foot of ي, as in الشريف. |
| 86r.4 | 26 | 26 | 26 | 12 | 3 | 100.0% / 100.0% (23 occ.) | n/a | consistent: the repeated five-sign group at each line end is تراكم. |
| 86r.9 | 89 | 89 | 89 | 23 | 6 | 98.8% / 98.8% (83 occ.) | n/a | consistent apart from the anchor-shaped sign for ص in تصيح and ن elsewhere. Opposite-facing brackets distinguish د and ذ. |
| 86v.9 | 41 | 41 | 41 | 19 | 9 | 100.0% / 100.0% (32 occ.) | n/a | consistent on the visible main-line signs; an arc over the ن-shape in الدنيا has no independently established value. |
| 87r.3 | 117 | 117 | 117 | 24 | 5 | 100.0% / 100.0% (112 occ.) | 114/117 | consistent: all repeated black signs keep their letter, including خ in الخلق; the red gloss differs at three positions. |
| 87v.8 | 130 | 130 | 130 | 22 | 1 | 99.2% / 99.2% (129 occ.) | 130/130 | consistent apart from the looped-cross sign for و and the first د of دليل. The marginal ر restores كثرت. |
| 88r.12 | 66 | 66 | 66 | 19 | 6 | 100.0% / 100.0% (60 occ.) | n/a | consistent: every repeated sign takes the same letter. |
| 88v.10 | 44 | 43 | 43 | 16 | 6 | 100.0% / 100.0% (38 occ.) | n/a | partly consistent: all repeated signs keep one value; the dotted cup in the final word has no second example. The damaged line gives ليلة الـ؟ـار. |
| 89r.4 | 81 | 81 | 81 | 21 | 5 | 100.0% / 100.0% (76 occ.) | n/a | consistent: the corrected reading supplies a distinct shape for each represented letter. |
| 89v.4 | 85 | 85 | 85 | 24 | 9 | 100.0% / 100.0% (76 occ.) | 85/85 | consistent: each recurring form keeps the same aligned letter. |
| 90r.4 | 79 | 79 | 79 | 23 | 8 | 100.0% / 100.0% (71 occ.) | 79/79 | consistent: the recurring signs resolve the damaged or lightly dotted wording at the end. |
| 90v.1 | 72 | 72 | 72 | 20 | 4 | 100.0% / 100.0% (68 occ.) | 72/72 | consistent: the recurring invocations and individual signs agree throughout. |
| 90v.12 | 72 | 72 | 72 | 20 | 6 | 100.0% / 100.0% (66 occ.) | 72/72 | consistent: 72 signs give 72 letters, including the shorter opening of the second verse. |
| 91r.12 | 85 | 85 | 85 | 19 | 3 | 100.0% / 100.0% (82 occ.) | n/a | consistent: short and extended four-like signs distinguish yāʾ and wāw in all eleven comparisons. |
| 91v.10 | 84 | 84 | 84 | 21 | 4 | 100.0% / 100.0% (80 occ.) | n/a | consistent: all repeated shapes keep one value. |
| 92r.10 | 64 | 64 | 64 | 17 | 3 | 100.0% / 100.0% (61 occ.) | n/a | partly consistent: the group after مدنف reads كييب by recurrent shapes, against كيف in the verse. |
| 92v.9 | 77 | 77 | 77 | 22 | 9 | 100.0% / 100.0% (68 occ.) | n/a | partly consistent: the signs resolve قرن تيممه and the final ـده of فيقتصده; a few singleton values depend on the verse. |
| 93v.1 | 36 | 36 | 36 | 15 | 6 | 100.0% / 100.0% (30 occ.) | n/a | consistent: all recurring forms retain one value. |
| 93v.7 | 38 | 38 | 38 | 16 | 7 | 100.0% / 100.0% (31 occ.) | 36/36 | consistent: 38 black signs match the 38 letters in the reconstructed verse. |
| 94r.3 | 89 | 89 | 89 | 22 | 4 | 100.0% / 100.0% (85 occ.) | n/a | consistent: repeated fāʾ, wāw and tāʾ support جفوته where the record prints حقوقه. |
| 94v.5 | 60 | 60 | 60 | 19 | 7 | 100.0% / 100.0% (53 occ.) | n/a | consistent: the first group gives يمين, with four shapes independently assigned in the remainder. |
| 95r.10 | 79 | 79 | 79 | 21 | 7 | 100.0% / 100.0% (72 occ.) | n/a | consistent: the second verse gives بالدما and فلهذين. |
| 95v.10 | 40 | 40 | 40 | 16 | 7 | 100.0% / 100.0% (33 occ.) | 40/40 | consistent: the raised lām after wāw in فلولا matches the inline lām in ولولا. |
| 96r.2 | 128 | 128 | 128 | 22 | 3 | 100.0% / 100.0% (125 occ.) | n/a | consistent: repeated groups resolve در بحر and the blessing احياكم; اتنقاكم is retained in its written sign order. |

## ff. 97r-106v

By-eye key from the compiler's plaintext, not independently confirmed. The signs were counted in reading order on line crops of the master. The percentages use repeated-shape occurrences only.

| chain | signs | letters | aligned pairs | shapes | singletons | consistency letter / skeleton | red agreement | verdict |
|---|---|---|---|---|---|---|---|---|
| 97r.1 | 76 | 76 | 76 | 20 | 8 | 100.0% / 100.0% (68 occ.) | 76/76 | consistent: all recurring sign values agree with the verse and the red glosses. |
| 97v.2 | 43 | 43 | 43 | 14 | 2 | 100.0% / 100.0% (41 occ.) | 43/43 | consistent: 43 black signs agree with 43 gloss letters. |
| 97v.9 | 34 | 34 | 34 | 15 | 9 | 100.0% / 100.0% (25 occ.) | 34/34 | consistent: the three ذهاب groups repeat their letters in the same order. |
| 98r.2 | 76 | 76 | 76 | 20 | 5 | 100.0% / 100.0% (71 occ.) | n/a | consistent: the two matching forked forms in بمسمن are the mīm of من and دايما. |
| 98r.13 | 69 | 70 | 69 | 16 | 5 | 100.0% / 100.0% (64 occ.) | n/a | consistent: 69 signs align to 70 letters, identifying the absent mīm of أبوكم. |
| 98v.10 | 51 | 50 shortened / 62 full | 0 | 17 | 5 | — | n/a | not keyed: the two written forms on f. 99r do not fit the observed groups under ordinary letter substitution. Catalogue 3942 remains open. |
| 99r.10 | 86 | 86 | 86 | 22 | 6 | 100.0% / 100.0% (80 occ.) | n/a | consistent: dāl and dhāl differ by the internal dot in the angle. |
| 99v.13 | 26 | 26 | 26 | 13 | 6 | 100.0% / 100.0% (20 occ.) | n/a | consistent: 26 signs when the sublinear insertion is counted. |
| 100r.8 | 47 | 47 | 47 | 17 | 6 | 97.6% / 97.6% (41 occ.) | n/a | partly consistent: the tailed left-loop family has readings bāʾ and ʿayn if treated as one form. |
| 100v.6 | 52 | 52 | 52 | 16 | 2 | 98.0% / 98.0% (50 occ.) | n/a | partly consistent: one pronged sign reads ب in three places and س once; the other repeated shapes give a single letter. |
| 101r.2 | 74 | 74 | 74 | 21 | 9 | 95.4% / 95.4% (65 occ.) | n/a | partly consistent: the open crossed shape appears equally often for ه and ح. Other repeated forms keep a single value. |
| 101v.2 | 61 | 61 | 61 | 16 | 3 | 100.0% / 100.0% (58 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 102r.1 | 72 | 72 | 72 | 24 | 8 | 98.4% / 98.4% (64 occ.) | n/a | partly consistent: و in قويقا and س in جالسا share the same looped form. Other repeated shapes remain consistent. |
| 102r.12 | 41 | 41 | 41 | 18 | 11 | 100.0% / 100.0% (30 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 102v.11 | 73 | 72 | — | — | — | — | n/a | Maqlub. Within each word, copy the even positions in order, then the odd positions in reverse. Ignore the spaces in the resulting text. The rule record lists the copy's exceptions. |
| 103r.4 | 83 | 83 | 83 | 20 | 4 | 100.0% / 100.0% (79 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 103v.2 | 57 | 57 | 57 | 19 | 7 | 96.0% / 96.0% (50 occ.) | n/a | partly consistent: the damaged three-sign group provisionally aligned to هنا repeats the same apparent form. Other repeated forms have consistent values. |
| 103v.11 | 63 | 65 | 63 | 21 | 7 | 100.0% / 100.0% (56 occ.) | n/a | consistent: each repeated shape takes one letter. |
| 104v.2 | 90 | 90 | 90 | 19 | 5 | 100.0% / 100.0% (85 occ.) | n/a | consistent: the three occurrences of اذا and both هي groups repeat identically. |
| 105r.1 | 47 | 47 | 47 | 17 | 6 | 100.0% / 100.0% (41 occ.) | n/a | consistent: 47 signs; the first and sixth words differ from the earlier copy at 100r.8. |
| 105r.11 | 52 | 52 | 52 | 15 | 4 | 100.0% / 100.0% (48 occ.) | n/a | consistent: each of the four فقلت groups uses the same crescent, V, flag and short hook. |
| 105v.6 | 130 | 131 | 129 | 28 | 6 | 100.0% / 100.0% (124 occ.) | n/a | partly consistent: the enciphered opening and all following groups can be read; one isolated mark at the end of the heading is unassigned. |
| 106r.11 | 42 | 42 | 42 | 12 | 1 | 100.0% / 100.0% (41 occ.) | n/a | consistent: the left- and right-pointing double lobes distinguish tāʾ and jīm throughout. |
