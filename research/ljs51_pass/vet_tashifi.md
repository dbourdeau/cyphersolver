# Penn LJS 51: vetting of the long "tashifi" cipher (ff. 14v l.7 - 16v l.6)

Date 27 Nov 2026. Sources: master TIFFs 0084_0033-0037 (ff. 14v-16v), web JPEGs 0084_0032 (f. 14r), 0038-0040 (ff. 17r-18r).
Working crops (git-ignored): `output/ljs51/crops/t_*` (`t_key_sheet.png` = one drawing per sign class).
Method: connected-component segmentation of the cipher lines, shape clustering, then a dynamic-programming alignment of
the sign string against the plaintext the compiler writes on 16v-17v. Counts are automatic, checked by eye on the
overlays, not every sign by hand. Arabic is transcribed as written (dots as I could see them); `[?]` = doubtful.

## Verdict in one paragraph

Not an open lead. The compiler's own plaintext (two poems, 16v l.7-13 and 17r l.4-17v l.4, 770 letters) is the **whole**
plaintext of the run, not an extract: the run has about 766 signs (770 expected), starts with the first letter of the
first poem and ends with the last letter of the second, and 722 of the 770 letters (94 %) line up with a sign of the
one class the key assigns them. The system is exactly as the compiler describes it (one sign per undotted letter
shape, 15 sign classes plus a word divider). The key is therefore recoverable and the run is "read with the key
recovered from the compiler's adjacent plaintext", not unsolved. What is left is cleaning (about 6 % of positions
disagree, from my automatic clustering and from doubtful words in my transcription), not a cryptanalytic problem.

## (1) The compiler's technique note (14v l.1-6) and the riddle (14r l.7-14v l.1)

14v l.1 (end of the riddle): `يرى فعلا وفعلا وهو فعل بين لصاحب القلب السليم` (read `يري` as written, undotted-looking).

14v l.2-6, literal (line breaks as on the page):

    فكتبت الجواب مترجما بنوع يسمى التصحيفي وهو ان
    يجعل للشكل وما مثله من الحروف في العربي صورة
    واحدة فيجعل الباء والتاء والثاء والنون والياء صورة
    واحدة والجيم والحاء والخاء صورة واحدة والدال
    والذال كذلك الى آخر الحروف

English: "So I wrote the answer, put into cipher (mutarjam) by a kind called the tashifi, which is that one makes
a single form (sura) for a shape and for what is like it among the Arabic letters: so one makes ba', ta', tha',
nun and ya' one form, jim, ha' and kha' one form, dal and dhal likewise, to the end of the letters." Tashif is the
classical word for misreading letters that differ only in their dots. So the cipher is the undotted skeleton (rasm)
alphabet with one invented sign per skeleton class. The "key" is the table class -> sign; nothing else is secret.
Only three groups are named; "to the end of the letters" leaves the others to be inferred (see the inventory below,
which recovers all 15).

Riddle, 14r l.4-13 (the compiler's prefatory lines are 14r l.4 `فحل ذلك سريعا لسهولته وهو` and the verse answer to the
7-line block, l.5-6; then): 14r l.7 `وكتب لي فسح الله في مدته لغزا من نظمه السعيد` ("and he wrote to me, may God prolong
his term, a riddle of his fortunate verse"; the sender is not named). Then, literally:

    وما علم على فرد مثنى رباعي يمارس بالنجو[م]   (the final م stands detached at the margin; read as بالنجوم)
    نواصله اذا شينا بلام ونقطعه كما نهوى نجيم     (last word as written; 17v reads it as the letter jim: بجيم?)
    اذا نطق المغيظ بعكسه فالجواب بشطر راي الكريم
    هو اسم معرب دخلت عليه حروف في زمن قديم
    فكانت عاملات فيه رفعا ونصبا يستفز نهى الحليم
    وان ضعف او حرف شيا فذاك الفعل يامر بالوجوم
    يرى فعلا وفعلا وهو فعل بين لصاحب القلب السليم

Tentative English: "What is the name of a single thing, doubled, four-lettered, plied by the stars? We join it with lam if
we wish, and cut it as we like with jim. If the enraged one pronounces its reverse, the answer is half 'the opinion of the
generous'. It is a declinable noun that particles entered in ancient times and which then governed it in the nominative and
accusative, to the irritation of the forbearing mind. And if it is doubled or a letter is [changed], that verb commands
silence. It sees a verb and a verb, and it is a clear verb to him of sound heart." (Grammar-and-letters riddle; my
translation of the clue words `[?]` is loose.)

What the riddle is, per the compiler's own commentary (17v l.5-18r l.7, read below): the answer word is **mahmah**
(a trackless desert, navigated by stars). Derivation: take `wahm` (وهم); the clue "without the stud" (`بلا عود`) removes
the waw (waw = the stud camel, fahl, 'awd; jim = the she-camel, "waw is jim's mate"); `hamm` remains; reversed and doubled
(`مضعف عكس`) it gives `mahmah`. He says only a few specialists could follow this ("very remote"). He opened the
answer poem with it: first hemistich `سلكنا مهمه القفر الصميم`. The other clue words are answered by words placed
inside the answer poem (`همهم`, `مه`, a `...مم` word, and the rhyme in mim/khim: see commentary).

So the riddle is the compiler's *link* to the cipher: the cipher text is his versified answer, written in tashifi.

## (2) Cipher structure

Counts by my segmentation (signs only, dividers and specks excluded; per-line error about +-1, a few merged or split
glyphs). Lines are numbered on the page. Earlier page passes counted dividers as signs and miscounted lines (15r has
13 lines, not 12; 15v has 14, not 13).

| page | lines | signs per line | total signs | dividers |
|---|---|---|---|---|
| 14v l.7-13 | 7 | 14, 14, 17, 17, 13, 14, 16 | 105 | 22 |
| 15r | 13 | 16, 14, 15, 16, 15, 16, 13, 15, 15, 14, 11, 13, 18 | 191 | 38 |
| 15v | 14 | 17, 15, 16, 12, 15, 14, 15, 15, 14, 13, 13, 16, 15, 15 | 205 | 36 |
| 16r | 13 | 16, 13, 14, 15, 17, 14, 13, 16, 15, 15, 14, 12, 16 | 190 | 43 |
| 16v l.1-5 | 5 | 14, 15, 16, 14, 15 | 74 | 15 |
| 16v l.6 | 1 | 1 (then divider, then `فحلها وكتب منها ما ذكر`) | 1 | 1 |
| total | 53 lines | | 766 | about 155 |

(Checked against overlay images, not sign by sign. 15v l.12 shows 0 dividers; probably a missed detection.)

Sign inventory: **15 sign classes + the divider**. Drawn variants exist inside a class (alif 5 clusters, ba-class 3,
fa, lam, ra, waw 2 each); variants are not positional (tested against initial/medial/final) and I treat each class
as one sign. Class = the plaintext letters that land on it in the alignment (letters counted in the plaintext in brackets).

| label | sign drawing | letters (n in plaintext) |
|---|---|---|
| S1 | tall stem with a diagonal arm and a second arm to the right, K-shaped | alif (122; glyphs 122) |
| S2 | small closed loop head on a descending stem, with a three-toothed horizontal comb to its right | ba ta tha nun ya (alif maqsura) (172; 183 incl. fragments) |
| S3 | flat-topped arch with two descending legs (pi shape) | jim ha kha (29) |
| S4 | chevron < open to the right | dal dhal (24) |
| S5 | flat bar with a small hook at the left start and one descending right leg | ra zay (43) |
| S6 | narrow 4-shaped sign, loop head and single stem, no comb | sin shin (21) |
| S7 | long shallow sweep with a small tooth, bowl-like, rising at the left end | sad dad (12) |
| S8 | tall narrow closed loop on a stem (taller than S2/S6) | ta za (emphatic) (12) |
| S9 | small ring, o | ayn ghayn (35) |
| S10 | square-hooked sign with a comb top and a long base stroke | fa qaf (48) |
| S11 | tall hooked left stroke with a small bowl/comb | kaf (20) |
| S12 | three-toothed comb on a short stem (numeral-3 look) | lam (92) |
| S13 | loop head with a leftward curl on a stem | mim (62) |
| S14 | 3-like sign with a long curved base sweeping right | ha / ta marbuta (29) |
| S15 | large open arc C with a small tooth inside | waw (47) |
| div | stem with three dots above (also a small speck variant) | word break |

Hamza (2 in the plaintext) seems to have no sign. Lam-alif is written as lam + alif (two signs) where tested (few cases,
low confidence). Same-shape pairs are merged exactly as the note says and, beyond the three it names, also ra/zay,
sin/shin, sad/dad, ta/za, ayn/ghayn, fa/qaf, ha/ta marbuta, i.e. 15 undotted skeleton classes.

Word dividers: yes, the dotted stem. About 154 found. 140 of them sit at a plaintext word end (91 %); 136 of the 185
plaintext word ends carry one (74 %); so the dividers are real word breaks but the scribe (or my detection) leaves about
a quarter of the breaks unmarked (typically a proclitic or short word run on, e.g. `لجه|الليل` written without a break).
Only 22 of 52 lines end (left side) with a divider and 3 start with one, so lines are not hemistichs; line breaks fall
anywhere.

One text or several? One continuous run. No new heading, no formula such as `fa-halaltuhu`, no change of sign set,
no gap between 14v l.7 and 16v l.6; the first line 14v l.7 follows the technique note directly; the only compiler words
are on 16v l.6 after the last sign. The earlier suspicion of several blocks is not supported by the cipher. The
*plaintext* is two poems, and they are joined without a break in the cipher: the first poem ends and the second begins
inside 15r line 11 (sign 265 of the run, `...من خيم وخيم | على يا بان فضل الله...`).

## (3) What the plaintext is

16v l.6, after the last cipher sign: `فحلها وكتب منها ما ذكر` ("he solved it and wrote from it what is mentioned").
(Who "he" is is not stated; the sender of the riddle, i.e. the person the answer was addressed to, is the natural
reading. Not certain.)

Poem 1 (answer poem, thanks and desert journey), 16v l.7-13, literal as written (two hemistichs per line):

    سلكنا مهمه القفر الصميم وخضنا لجه الليل البهيم
    وجبنا بالمفاوز كل نائ وردنا في السباسب كل ميم
    اردنا ان نفوز بعذب ماء وردنا في الفيافي شبه هيم
    وردنا شرقها والغرب حتى وردنا شاطي البحر العظيم
    اخذنا عنك فصفا لدنيا ورق وراق باللطف العميم
    قصدنا ظلمه فضفا علينا وحولنا عن المرعى الوخيم
    بغير تكلف حنو ويغنيني وجبر الكسر من خيم وخيم

Corrections to earlier readings, confirmed by the cipher: l.7 second hemistich reads `لجه الليل` ("the depth of the night"),
not `حجب`; l.11 `لدنيا` may be `لدينا`; `ظلمه` may be `ظله`; l.13 `حنو`, `ويغنيني` doubtful. 262 letters, 60 words.

Poem 2 (praise of a patron, "Ibn Fadl Allah"), 17r l.4-13, then 17v l.1-4:

    على يا بان فضل الله حطت ركائب كل سباق عليم
    بحل المشكلات وكل صعب بجلى الكرب والخطب الجسيم
    يوشى بالبراع مدبجات تفوق فلايد الدر النظيم            (فلايد = قلايد?)
    ويغني رايه والجاش جيشا عن الرايات بالملك العقيم        (بالملك / للملك?)
    زكا اصلا وفرعا فهو يدعى الكريم ابن الكريم ابن الكريم
    الوف للفضائل والعطايا نفور عن مواحش كريم               (مواحش? word before كريم not clear)
    هو السم الذعاف لمن يبادي هو الحلو الفكاهه للنديم
    وبلغني قاصده بطلق وجه واخلاق ارق من النسيم
    اذا ما هم المغتاظ ياتي ببشر شيمه البر الحليم
    بمنه ما فاه دهرا للمداني وصه ما قال يوما للغريم
    ولم يرم العدو بسهم نطق ومتكل على نجح فو[ ]يم        (17v l.1: a gap before the final يم at the margin; the cipher has four signs there, fa waw ya mim)
    مضعف عكس ما انا فيه ونم بلا عود فاو زوج جيم          (17v l.2)
    ومالي غيره من بعد ربي طبيب قربه برء السقيم            (17v l.3)
    ادام الله رفعته ليبقى على الايام في عز [ ]مقيم        (17v l.4; a gap before مقيم)

508 letters, 125 words. Lines 11-12 of this poem (17v l.1-2) are the riddle's clue words spelled into the verse
(`مضعف عكس ما انا فيه ونم بلا عود فاو زوج جيم`).

17r l.1-3, the remark, literal:

    كتب الى هنا وكتب تحتها وبقية الالحان والفصل
    معلوم اذ قد حل هذا القدر الكافي للسبب [?]
    وسمه الجواب

Rendering: "[It/he] was written/wrote up to here and was written/wrote beneath it; and the rest of the allusions
(alhan) and the section (fasl) is known, since this sufficient portion has been solved; and call it 'the answer'."
The verb is undotted (kataba or kutiba) and `للسبب` is not secure. I read it as marking the break between the two
poems and the move to the commentary below, not as a statement that the cipher is longer than the quoted text, because
the numbers say the quoted text is the cipher's whole content (below). Reading of `الالحان والفصل` not secure.

17v l.5-13 (commentary, literal; doubtful words marked):

    لما الغز في المهمه صدرت به الجواب ولما ذكر
    اللام ثم الجيم ذكرت الميم والميم البسير [?] في اللغه
    ذكره الخليل في كتاب العين منقول من المجاب والخير
    بالكسر الكرم والخيم الشيمه ذكرته لمجانسته ما قبله
    في البيت وما قبله في القافيه اطاعي [?] ومكمل
    تام ومثله في التشبيه كريم مع الكرم قبله وانبت
    بلفظه مه جواب قوله فذاك الفعل يامر بالوجوم وقبلها
    همهم جواب قوله اذا نطق المغيظ بعكسه وقول
    بشمم [?] جواب قوله بلام فاللام السمم [?] وان كان اللام ايضا

18r l.1-10:

    اسم المقده [?] لغه حبشيه لما ذكر واحتمل ارادته
    اكتفا بالسهم ومثل مضعف عكس ما انا فيه الى
    اخر الملكان [?] قد ذكر الجيم وفي اللغه الجيم الناقه المسنه
    ذكرت الواو وهو الفحل من الابل فهو زوج الناقه
    والفحل هو العود بالفتح فالعود هو الواو وبقوله بلا عود
    اي اذا حذف من وهم الواو يبقى هم فاذا عكس
    وضعف صار مهمها وهذا لا يفهمه الا بعض
    الخواص فانه بعيد جدا ولحضرة الشيخ بدر الدين
    حسن الجولاني مترجمات من انشاء على سبيل الامتحان
    وهي الغاز ايضا اولها

(18r l.11-13 is the next cipher, different sign shapes, a new item: not part of the tashifi run.)

Gist: the answer opens with mahmah because the riddle's answer is mahmah; when the riddle named lam then jim, the
answer names mim (rhyme and word play: khim, khir, "mim" as a lexical item, citing al-Khalil, Kitab al-'Ayn); each riddle
clue has its answer word planted in the poem (`مه` for the "verb that commands silence", `همهم` for "when the enraged one
pronounces its reverse", a `-mm` word for "with lam"); the waw/jim/camel explanation yields mahmah from wahm.

**Does the compiler give the whole plaintext or an extract?** The whole. Numbers:

- plaintext letters, poem 1 + poem 2: 262 + 508 = 770 (185 words), counting hamza as a letter.
- cipher signs found: 766 (105 + 191 + 205 + 190 + 74 + 1). Difference -4 (0.5 %), inside my segmentation error.
- Per-class check (plaintext letters / glyphs of that sign class): alif 122/122, lam 92/92, dal 24/24, kaf 20/18,
  mim 62/64, waw 47/48, fa-qaf 48/46, ra 43/47, sin 21/18, jim 29/26, ha 29/36, ayn 35/32, sad 12/15, ta 12/13;
  only the ba-class is inflated (172/183) by ink fragments I classed with it.
- Alignment: the first line of the run (14v l.7, 14 signs) is `سلكنا مهمه القفر` (word 2 is the pattern B-E-B-E =
  m-h-m-h; word 3 shows the same sign twice for qaf and fa); the second line is `الصميم وخضنا لجه`. The last sign of the
  run (16v l.6, one sign) is the mim of `مقيم`. A global alignment of all 766 signs on the 770 letters gives 722 identical-class
  matches, 34 class mismatches, 28 surplus glyphs (mostly specks and dot fragments, a few merged or split glyphs) and
  14 letters without a glyph. The mismatches are scattered, none clusters at either end.
- The key is learned from this alignment (seeded only on the first 110 signs), so 94 % is a self-consistency figure, but
  each class has 1-5 drawings and 95.5 % of aligned pairs fall into the class's own set; chance agreement of 15 sign
  classes with the 15 skeleton classes in this way is not plausible.

Sign count vs letter count treating same-shape letters as one sign: the sign count equals the letter count (one sign per
letter, same-shape letters share a *sign type* but each occurrence is still one sign). Prefix test: the whole run, not a
prefix, fits.

## (4) Is the remainder unrecovered?

No remainder to recover. Nothing of the run lies outside the written plaintext; the compiler's "he wrote what is
mentioned" does not leave a cipher residue. A solver has: the 15-class inventory, the length (about 766-785 signs), the
rule in the note, the word dividers, and the plaintext. Open items are small: (a) the 34 mismatches and 28 surplus glyphs
need a hand pass to make a sign-by-sign transcription (my counts come from segmentation, not from a hand-keyed
transcription), (b) about ten doubtful words in the plaintext transcription (listed in brackets above) which the
cipher itself can settle (it already corrected `حجب` to `لجه`), (c) hamza and lam-alif handling, (d) the exact sense of
17r l.1-3.

## Confidence and lead status

- (1) technique note and rule: high (clear script, 14v l.2-6). Riddle transcription: medium-high; translation tentative.
- (2) structure: medium-high on lines, inventory (15) and dividers; per-line counts +-1-2.
- (3) plaintext: medium-high; individual words [?] as marked. Fit with the cipher: high (722/770 identical-class, first and last signs on the first and last letters).
- (4) no unrecovered remainder: medium-high.
- **Real open lead? No.** It is a finished reading in the volume's own words: outcome type "key recovered from adjacent
  plaintext (the compiler's)", no external key needed, no ciphertext-only problem left. Value for the project: a clean
  benchmark/profile of a Mamluk rasm-class substitution with full plaintext and an explicit statement of the rule; worth a normal target write-up (not an "open" catalogue entry). The riddle (mahmah from wahm) is
  an Arabic wordplay puzzle, separate from the cipher.
