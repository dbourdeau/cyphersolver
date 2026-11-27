# LJS 51: TIFF check of three blocks (f. 63v, f. 61v, ff. 73v-74v)

Source: master TIFFs 0084_0131 (f. 63v), 0084_0127 (f. 61v), 0084_0151 (f. 73v), 0084_0152 (f. 74r, fetched from OPenn into
`output/ljs51/master/`); 0084_0126 (f. 61r) and 0084_0153 (f. 74v) were read from the 1422-px web JPGs only (no master fetched).
Crops are in `output/ljs51/crops/` with prefix `v_`. "Read" below means read by me from the image; "not read" means I could not.
Counts of signs come from connected-component counts plus a visual check of every line (overlay images `v_151_ov*`, `v_152_ov*`).
Right-to-left throughout.

## Summary

| Item | Finding | Confidence | Real open lead? |
|---|---|---|---|
| (1) f. 63v | The 6-line sign cipher, the tree figure, the red letters and a verse couplet written turned 90 degrees in the right margin are four renderings of ONE text of 79 letters (79 signs = 79 trees = 79 red letters). The couplet is the plaintext. The earlier note ("no plaintext on the page") is wrong. | high on the 79 = 79 = 79 match; medium on the wording of the verse | The text is solved by the compiler. What is open is the two keys, and here we hold a complete 79-letter crib for both the sign alphabet and the tree script. |
| (2) f. 61v l.1-4 | They are NOT non-words and NOT a cipher. They are strings of real Arabic imperatives in antonym pairs (the four "verses", one per line). Nothing needs decoding; no Caesar/atbash/reversal is involved. The 8-9 line sign block on f. 61r is the ciphertext and these four lines are its plaintext. | high that they are plain Arabic imperatives; medium on individual words in l.2 and l.4 | Yes, as a known-plaintext pair (ciphertext on 61r, plaintext on 61v). The compiler states no rule on 61v. |
| (3) ff. 73v and 74r | Two blocks of 5 lines each, 70 signs (73v) and 76 signs (74r). They share a few glyph shapes but their frequent signs are disjoint; I cannot say they are one alphabet. The compiler's prose is about chancery formulae (tawqi', sabaqa, hamdala, ya'), not about the cipher; the verse text of the second pair is probably given in plain script at the top of f. 74v. | medium | Yes, but weaker: both blocks have a plaintext candidate on f. 74v only in part; key recovery needs the first verse. |

## (1) f. 63v (image 0084_0131)

### Layout
Lines 1-6: cipher of invented signs, divided into groups by a dotted vertical stroke. Line 7: prose (below). Then a figure of
five rows of trees (below, "the figure"). Down the right margin, turned 90 degrees (read by turning the page so that the
margin text lies horizontally): a short line and two longer lines of Arabic (below). Pencil modern numerals at the foot, not part of the book.

### The 6-line sign cipher (counts)
Signs per line, counted from the TIFF (a divider is a dotted stroke; the line ends in one): **15, 14, 15, 14, 15, 6 = 79 signs.**
Groups of signs between dividers, per line (right to left):

| line | groups | signs |
|---|---|---|
| 1 | 4, 4, 7 | 15 |
| 2 | 4, 2, 4, 4 | 14 |
| 3 | 2, 3, 6, 4 | 15 |
| 4 | 2, 2, 2, 4, 4 | 14 |
| 5 | 2, 4, 4, 5 | 15 |
| 6 | 6 | 6 |

(The earlier pass gave 22/21/21/21/21/9 = about 115; that was an over-count. Counting component by component gives 79.)
The signs are Arabic-letter-like invented shapes (an inverted-V hook, an arch, a "3", a lam-like hook, a triangle with stem, a
cup with teeth, a looped "9" and others); a contact sheet of all 79 is `crops/v_131_signsheet.png`.

### The tree figure ("qalam mushajjar")
Five rows, each drawn right to left. Each row is a curved horizontal baseline broken into segments; every segment is a
"word group": the baseline dips and then curls up at its left end, and the next segment starts after a gap. From the baseline rise
single trees, each a vertical stem with pairs of oblique side branches pointing up and outward (like a fir twig or a palm frond).
Trees differ in (a) the number of branch pairs (about 1 to 8), (b) height (the tallest, at the left end of row 1, has about 8 pairs and
is twice as tall as a Y-shaped tree of one pair), (c) whether the tip is a fork (a plain "Y"), and (d) the angle and spacing of the branches.
Same-letter trees look alike on a contact sheet (`crops/v_131_treesheet*.png`): the trees over the letter alif are the short Y-shaped ones
with one or two pairs of branches, those over ya' have 4-6 pairs. My automatic branch counter on the stems is too noisy to give a key,
so I give no shape-to-letter table; I only report that a shape-to-letter correspondence is visible.
Over every tree there is one small red letter or mark. A worm-eaten/stained area near the left of row 1 (one tree split in two by a stain)
and the torn left edge at row 5 do not change the counts.

| row (top = 1) | trees | trees per baseline segment (right to left) | red letters/marks |
|---|---|---|---|
| 1 | 15 | 4, 4, 7 | 15 |
| 2 | 19 | 4, 2, 4, 4, 2, 3 | 19 |
| 3 | 16 | 6, 6, 2, 2 | 16 |
| 4 | 14 | 4, 4, 2, 4 | 14 |
| 5 | 15 | 4, 5, 6 | 15 |
| total | **79** | | **79** |

(Row 3: I count the right-hand segments as 6 + 6; the cipher's own groups at that place read 6, 4, then 2+2+2, which has the same total of 16 for the
stretch; the baseline probably runs over a divider there. Segment sizes of rows 1 and 2 follow the cipher's groups exactly: 4,4,7 / 4,2,4,4 / 2,3.)

### Red letters, right to left (as read from 2x crops; dotted letters are often unclear, so I give what the shapes show)
- Row 1: ا  ي  [stub]  ي  ك  ب  ي  ر  و  ا  ل  ص  ع  ي  ر
- Row 2: ي  ق  و  ل  ل  ي  [vertical stroke = ا]  ط  ع  ن  ع  ش  ا  ي  ب  ه  ر  ك  ن
- Row 3: ص  ن  ب  ك  ر  [stroke = ا]  ن  ا  د  ي  ت  ه  د  ا  ل  ا
- Row 4: ك(a hamza-alif form)  خ/ح  و  ر  ف  ق  ا  ل  ل  ي  ع  ن  د(?)  ي
- Row 5: ي  ح  و  ر  ف(?)  ن  ك  ت  ه  ث  ق  ل  ي  د  ا
Read as the dots would require, these are the letters of the couplet below: the red letters are the plaintext, one letter per tree.

### The plaintext: the margin couplet (turned 90 degrees)
Read from the rotated crop `v_131_mrb_*.jpg` (right to left, two verses plus a short line above them):
- short top line: `والبيت…` (word doubtful; perhaps "and the verse(s)")
- l.1: `ابري كبير والصغير يقول لي اطعن حشاي به وكن صنديدا`  (the margin writes `والصغر`; the red letters give a ya' too)
- l.2: `ناديت هذا الاحول فقال لي عندي بحور وثلثه تقليدا`  (words 3-4 and the last word are the least certain)
Gloss (no more than the words allow): "My needle is big, and the small [one] says to me: 'stab my vitals with it and be a hero!' ... I called this
squint-eyed man and he said to me: 'I have seas and a third of it by imitation'" - a riddle-like, probably ribald couplet; meaning not checked.
Letter counts of the couplet, row by row (my reading): 15 + 19 + 16 + 14 + 15 = **79**, equal to the row sizes of the figure and to the
red-letter counts. Word lengths also match the group structure: row 1 = ابري(4) كبير(4) والصغير(7); row 2 = يقول(4) لي(2) اطعن(4) حشاي(4) به(2) وكن(3);
row 5 = بحور(4) وثلثه(5) تقليدا(6). Cipher lines 1-3 have exactly these group sizes (4,4,7 / 4,2,4,4 / 2,3,6) and lines 5-6 the groups 2,4,4,5 / 6. In
the middle (lines 3-4) the dividers fall inside words (4,2,2,2,4,4 against ناديت 5, هذا 3, الاحول 6, فقال 4 = 18 letters in both).

### Does the cipher fit the plaintext?
Lining up the 79 signs with the 79 letters in order, the sign shapes sort cleanly: ي 11 of 11 signs are the same arch; و 6/6; ن 5/5; د 5/5; ق 3/3; ه 3/3; ر 3/4; ا 9/11; ل 5/9 and ب 2/4 (the misses
may be my reading or misalignment, or genuine variants; the compiler himself notes on f. 64r that he drew a waw "in two forms by mistake"). A simple
monoalphabetic substitution (an invented alphabet with letter-shaped glyphs) fits; I see nothing that suggests more than one alphabet.
Contact sheet: `crops/v_131_signsheet.png`.

### Which plaintext is on the page, and does the tree count match?
Yes: 79 trees = 79 red letters = 79 signs of the six-line cipher = 79 letters of the margin couplet on f. 63v itself. Nothing on f. 63r or 64r is
the plaintext: f. 63r l.1 is the plaintext verse of the block on f. 62v (it continues the "فحله وارسله وهو" of f. 62v l.13), f. 63r l.2-13 is a general
prose passage, and f. 64r has its own six-line block (l.3-8) with its own solution.

### The compiler's Arabic prose on f. 63v (line 7), and what it says
`فحللته وقد كتبته بالقلم المشجر ليقرأه من يعرفه فلا يبلغوا افشا[ءه ؟] و…`
Gloss: "I solved it and wrote it [out] in the tree pen (al-qalam al-mushajjar), so that whoever knows it may read it, and [those who do not
know it] shall not reach (the) divulging [of it]..." The last words are doubtful (`يبلغوا` is read as `يبلو`/`يبلغ` in places) and the line ends with a lone `و`.
That is ALL the prose on the page: the margin couplet is verse, not explanation. **He does not state the key, the rule, or any number of branches.**
What the line implies: the tree figure is a re-encoding of the solved text (the plaintext) in a second script, with the red letters as an aid
for readers who do not know the tree script.

## (2) f. 61v lines 1-4 (image 0084_0127) and the block on f. 61r

### Transcription of l.1-4 (plain Arabic naskh; word division is mine)
- l.1: `صل اقطع مر انه انفع ضر ابك اضحك اسر بع صل اهجر رح`
- l.2: `اغد افن ابش[ر ؟] خز[?] زد انقص`  (the middle words are the most doubtful: `ابوش` / `خرز`)
- l.3: `خذ اعط اشحط ادن اعل اسفل اشف امرض ابد عد`
- l.4: `خن[?] اوف اغدر اجمل اهزل جد اضلل اخلص`  (first word `خز`/`خن`; word division of `اجمل هر لجد` is mine)
These are Arabic imperative verbs in mutually opposite pairs: join/cut (صل اقطع), command/forbid (مر انه), benefit/harm (انفع ضر), weep/laugh (ابك اضحك),
join/shun (صل اهجر), take/give (خذ اعط), go far/come near (اشحط ادن), go up/go down (اعل اسفل), heal/sicken (اشف امرض),
and so on to the end of the line. The earlier note read them as non-words; they are plain-script words, four verses made of antonym pairs. The
previous pass's wording ("a letter-for-letter substitution") is not supported by the TIFF.
Therefore the requested tests were not needed: the text reads as it stands (identity), so no letter shift (Caesar +/- k over 28 letters), atbash,
reversal of words or letters, or ibdal/abjad substitution can be "the" rule; any of them would turn this valid Arabic into non-words. I did not run the transforms mechanically
(there is no reason to), I judged by reading.

### The block it answers
f. 61r (image 0126, web JPG): l.1-2 prose, `...فكتبت بسن(?) من جملة اربعة ابيات لابن المجد الموصلي الواعظ` ("so I wrote [in cipher] from among four verses of Ibn al-Majd al-Mawsili the preacher"),
then a cipher block of 9 lines of invented signs (l.3-11), then prose. I counted the signs of f. 61r roughly from the web JPG: about 105-115 (the first line shows the
word-group sizes 2, 4, 2, 3, ...), against about 125 letters in the four lines on 61v. Same order of size; not equal; not verified sign by sign. The first four sign groups of 61r l.3
(2, 4, 2, 3) agree with the first four words of 61v l.1 (صل 2, اقطع 4, مر 2, انه 3). The dominant, repeated sign at the start of groups on 61r fits the very frequent word-initial alif
of the imperatives (about 26 alifs in the four lines). This supports "61r = the cipher of 61v l.1-4"; it is not a proof.

### Lines 5-13 (the compiler's text), with a line-by-line gloss
l.5 `هذا والله الذي ما حل كاتبه مترجم وهذا بالحزازير اشبه من` - "By God, this is [the kind of thing] whose writer [did not give a solution?]; (a) cipher; and this is more like riddles (ḥazāzīr) than"
l.6 `المترجمات وان رسم مولانا ان يكتب له نظائر هذا فبسم الله ثم` - "ciphers (mutarjamat); and if our lord decrees that one write him the like of this, then in the name of God; then"
l.7 `كتب للمملوك بنا بان ذكره والبيتان بمنه الاربعة واجداول` - "[he] wrote to the slave ... and the two verses [?], the four, and ..." (doubtful, esp. `بنا بان` and `واجداول`)
l.8 `اربي محض ودي فك غير ممحص اعانك عن سوم وان كنت مرخصي` - looks like a quoted verse or message; not read confidently ("my pure affection..., solve [it], not [purified]..." only as a guess)
l.9 `والاخر رابع تلو السنن المذكورين` - "and the other, the fourth, after the [ones] mentioned" (`السنن` doubtful, perhaps the two/three aforementioned)
l.10 `فما انت الا انت في كل حالة وما انا الا ذاك غير مخلص` - "You are none but yourself in every state, and I am none but that [man], not sincere": a verse-like line (probably the reply that sets the answer's tone), not a rule
l.11 `فبالله العجب من هذا الذهن العظيم اقسم بالله لو عاش ابن عدلان` - "By God, how wondrous this great mind; I swear by God, if Ibn 'Adlan had lived"
l.12 `او ابن دنينير او ابن الروم او الكندي وشاهدوا هذا الحل` - "or Ibn Dunaynir or Ibn al-Rum or al-Kindi, and had seen this solution"
l.13 `لاعظمهم وتركوا جميع ما ذكروه في كتبهم وما ادعوه من` - "they would have held them [the solvers] in awe and abandoned all they mention in their books and claimed [continues on f. 62r]"
Does he state the rule? **No.** On this page he names the difficulty ("riddles rather than ciphers"), names the four verses (Ibn al-Majd al-Mawsili) and the earlier authorities (Ibn 'Adlan,
Ibn Dunaynir, Ibn al-Rum, al-Kindi), and boasts of the solution, but states no substitution rule. I found nothing on f. 61v that says ibdal, abjad value or "bab al-maqlub".
Because the plaintext is antonym pairs, a cipher whose plaintext is this unusual word list would be an ordinary substitution with a word list as crib; whether the compiler's "solution" used the antonym
structure as a crib is not stated.

## (3) f. 73v lines 8-12 and f. 74r lines 3-7 (images 0084_0151, 0084_0152)

### Signs per line (right to left; counted from the TIFFs, overlays checked)
f. 73v: l.8 **15** (groups 5,5,5), l.9 **14** (4,2,6,2), l.10 **16** (5,4,7), l.11 **15** (5,2,5,3), l.12 **10** (2,8). Total **70**. (Each line ends in a divider; there is no sign after it.)
f. 74r: l.3 **16** (3,4,4,3,2), l.4 **15** (2,3,4,3,3), l.5 **16** (4,4,8), l.6 **13** (2,4,5,2), l.7 **16** (6,3,6,1). Total **76**.
Counts of one or two signs per line can move if a thin "slash" is a separate sign or part of its neighbour (73v l.8 has one such case).

### Distinct signs
By visual clustering of every sign (`crops/v_cluster_sheet.png`, blue = 73v, green = 74r): about 20 distinct shapes on f. 73v and about 18-20 on f. 74r (clusters merge and split at the edges, so +/- 3).
- Frequent on 73v, absent on 74r: the "K" (about 12 signs), the "3" (about 8), the arch "Π", the "H", the L with a bar.
- Frequent on 74r, absent on 73v: the small "د"-shaped hook (about 16 signs) and the lam-shaped loop (about 13), the "/\" (4), the "و with a long tail" (3).
- Shapes that occur on both: the toothed cup (9 on 73v, 7 on 74r), the "X" with a bar (5 and 3), the triangle on a stem (1 and 1), the looped "9"-shape (1 and 3), an "ε".

### Same alphabet?
Not shown. The two blocks draw on a common pool of glyph shapes (about five shapes are shared and the sign style is the same), but the two most frequent signs of each block
(K and 3 on 73v; د-hook and loop on 74r) never occur on the other page. If one key applied to both, texts of the same language would give the same frequent signs for alif and lam.
So either two different keys drawn from one family of shapes (which fits "in its tabaqa" - see below), or two very different plaintexts. I cannot tell which; the plaintext of 74r would settle it.

### Prose around the blocks, with a gloss (read from 2x crops; doubtful words marked)
f. 73v:
- l.1 `ولما رسم المملوك بكتابة توقيعه الشريف بعود وظيفته` - "and when [he] decreed that the slave write his noble signature [tawqi'] for the return of his post"
- l.2 `وتجديد وظيفة لولك لم يعلم الموقع جاري عادته ما كتب لي` - "and the renewal of a post...[words doubtful] ...the signatory did not know...his usual way, what he wrote to me" (low confidence)
- l.3 `فكتب المجلس السامي وما بعدها بغير ياء ولم يذكر الحمدلله` - "so he wrote 'al-majlis al-sami' and what comes after it without ya', and did not mention the hamdala"
- l.4 `ولا السباقة وهي جل المقصود فارسلت له بعض ...` - "nor the sabaqa [the opening formula], which is most of the point; so I sent him some ..." (last word doubtful)
- l.5 `فوقف عليها وقال اما الحمدلة فاليا[ء] مكتب واما السباقة` - "he looked at them and said: as for the hamdala, ... the ya' is written; and as for the sabaqa"
- l.6 `فلا بد من مرسوم المخدومي العالي اسبغ الله ظلاله` - "so there must be a decree of my master the lofty, may God extend his shade"
- l.7 `فكتبت للمشار اليه عظم الله شانه` - "so I wrote to the aforementioned, may God magnify his station"
- l.8-12 cipher
- l.13 `ثم نظمت شعرا اخر في طريق القلعة وترجمتهما في طبقته` - "then I composed another verse on the road to the citadel and ciphered the two of them (tarjamtuhuma) in its class/layer [tabaqa]" (the last word could also be read as "in its ṭabaqa [of letters?]"; not clear)
f. 74r:
- l.1-2 `القاضي ناصر الدين ابن الشاني(?) موقع الدست الشريف على عجله وارسلتهما اليه` - "the qadi Nasir al-Din Ibn al-Shani(?), signatory of the noble dast, in haste; and I sent the two to him" (the nisba is doubtful)
- l.3-7 cipher
- l.8 `فبعد لحظة طلب الموقع فرسم له بتغيير التوقيع الشريف` - "after a moment he called the signatory and ordered him to change the noble signature"
- l.9 `وكتابته في قطع عريض الحمدلله والياء على جاري العادة` - "and to write it on a broad cut [sheet], the hamdala and the ya' as usual"
- l.10 `والسباقة كما رسم بها فشكرت احسانه وصدقته ثم حلفت` - "and the sabaqa as he ordered; so I thanked his kindness and ... then I swore" (`وصدقته` doubtful)
- l.11 `واقسمت انه ما يمكن تغيير التوقيع بل نصلح بما طلبه المملوك` - "and I swore that it is not possible to change the signature, but we repair [it] with what the slave asked"
- l.12 `من السباقة والالقاب بالياء لا غير فما نعني زمانا تخالفت` - "of the sabaqa and the titles with the ya' and nothing else; [then?] what we mean ... we differed" (low confidence)
- l.13 `انه ما يتغير وهذا هو القصد ففعل ثم ارسل المترجمين` - "that it does not change, and this is the aim; so he did, then he sent the two ciphers (al-mutarjamayn / al-mutarjamatayn)"
f. 74v (read from the web JPG only):
- l.1 `ليّ ان البيت وقد كتب الثاني وهو` - "...that the verse; and the second has been written, and it is:"
- l.2 `ايا بحر الجود بلا مغيض ويا بدرا نضي بلا محاق` - "O sea of generosity without ebb, and O moon [full] without waning" - a verse in plain script, 35 letters; this is the only verse text I could read after the two blocks
- l.3 `تصدق بالسباقة ان نفسي تاهت في السباق ولله التراقي` - read only partly
- l.4 `ونبه ان السباق سقط منه الف وبلا محاق بغير فاصله` - "and he pointed out that in 'al-sibaq' an alif dropped from it, and [that] 'bila muhaq' [was written] without a separator" (a note on a slip in the ciphered text, not a rule)
- l.5 `وانه سهو ثم كتب لبيتين الاولين و مما` - "and that it was an oversight; then he wrote the two first verses, and of what..."
- l.6-13 about thanks, the sabaqa and ya', a remark that the poem was composed "in banter and joking" (`على سبيل البسط والمداعبة`), and that the qadi Amin al-Din al-Hanafi (earlier mentioned, now qadi of Hama) was present and "had written this verse and I solved it on the spot" (`حللته في الحال`). Not read word for word.

### What he says about the answers
That he composed a second verse and ciphered both ("in its tabaqa"); that the two ciphers went to the qadi Nasir al-Din, the chancery signatory; that the story is about whether the signatory would change the formulae; that the second verse is
given plainly on f. 74v (`ايا بحر الجود…`); that a slip (a missing alif, a missing separator) was found in the ciphertext; and that a third man solved it "on the spot". He does not give a plaintext for the 73v block that I could identify (the first verse
is not set out under that heading), and he gives no rule or number of alphabets. "ṭabaqa" is his only technical word and I could not define it from the page.
74r has 76 signs; the 35-letter verse is too short to be the whole of it, so the plaintext of 74r is probably longer than the single verse quoted on 74v (not checked).

### Lead assessment
f. 73v and 74r are real open leads but a step weaker than 61r/61v: two sign blocks with plaintext only partly on the pages, same glyph family, probably two keys.
