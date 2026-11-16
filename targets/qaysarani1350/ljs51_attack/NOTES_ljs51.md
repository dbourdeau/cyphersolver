# Penn LJS 51, f. 106v: the ciphertext-only attempt (log of the folded folder `ljs51`)

Status: folded into `targets/qaysarani1350/` (16 Nov 2026); not a target of its own. This is the working log of the attack as it
stood when it was closed; the comparison with the accepted reading is in `../NOTES.md`, section "The ciphertext-only attempt".
Paths below named `targets/ljs51/` are now `targets/qaysarani1350/ljs51_attack/`.

**Superseded (16 Nov 2026): f. 106v was read by another session in `targets/qaysarani1350/` (one-to-one key from the red
gloss, lam-alif as one sign; a tawil love verse rhyming in -rḍā, validated with `ar-mamluk`). That folder is the target
of record. This folder keeps the failed parallel attempt as a record: its homophone hypothesis, the "reply on the
tashif" theme and several sign identities were wrong. One point from here that the other folder has not checked: the
sender's name after "wa-kataba li" was re-read at 5x in step 13 below as Ibn al-Qubabi [or al-Qabbani], not Ibn
al-Qaysarani.**

Catalogue 2882 (promoted 15 Nov 2026 from the Arabic sweep, `research/sweep_2026-11-15_arabic/`).

## The document

- University of Pennsylvania, Kislak Center, LJS 51, "Collection of alphabets and encoded correspondence", Arabic, Syria?,
  copy dated by Penn "14--"; the text is older: the compiler dates an anecdote on f. 86r to the 730s AH (1330s) and
  corresponds with the Mamluk chancery circle of Ibn Fadl Allah. OPenn image 0084_0217, master TIFF 2339 x 2959 px:
  https://openn.library.upenn.edu/Data/0001/ljs51/data/master/0084_0217.tif
- The volume is a secretary's narrative of cipher verses exchanged with colleagues; each cipher is followed by "fa-halaltuhu"
  and the plaintext. f. 106v is the last page and the only cipher without its plaintext: the manuscript breaks off.
- Top of f. 106v: the plaintext of the cipher on f. 106r (a verse with "aflaja khasmi ... aflahtu fi hujjati wa-khaba
  l-muhtajj"), the compiler's correction ("the right reading is aflajtu with jim; he wrote falahtu with the undotted ha: it
  was a tashif"), then "wa-kataba li Ibn al-Qubabi [?] fihi" (first read here as Ibn al-Qaysarani; corrected in step 13) and the cipher: seven lines, 90 signs, 25 distinct, 22 words
  with dividers (a vertical stroke under three dots).
- After the cipher: "fa-halaltuha fi l-hal ... wa-wajadtuhu ja'ala al-lam alif" and the page ends.
- f. 106r (facing) shows how the compiler describes such ciphers: "wajadtuhu qad wada'a al-lam alif harfan wahidan, wa-kitabatuhu
  min al-shimal ila al-yamin li-tul al-abyat ... wa-zada wawan wa-alifan fi al-akhir li-alla yattadih": lam-alif as one
  sign, writing left to right, and null letters added. So direction, ligatures and nulls are open in each cipher.
- Red ink over the first five signs of line 1 (a later reader's partial gloss): waw, ta, alif, ghayn, sin.

## Work so far (15 Nov 2026)

1. Transcription (`transcription.txt`, `ciphertext.txt`): from the master TIFF, line crops at 1.5x and 2.2x, then checked
   against connected components of the ink (joined glyphs E, P and the head-and-descender signs Z, R, C are single signs;
   the Z family splits into three by the end of the descender; A and B differ by the lower loop; T differs from U; the
   large angular 8 in line 6 is an alif H, not the round 8).
2. A language model was added to `lang/` for this target: `ar-classical-poetry` (788,143 verses of pre-modern Arabic poetry,
   Mamluk first, from the Ashaar dataset; `lang/build_ar_poetry.py`, norm scheme `arabic` = the 28 letters).
3. `solve.py`: simulated annealing over sign -> letter keys, character 5-gram + word bonus. One-to-one keys in both
   directions gave no sense (runs of 15 Nov). Fixing the red-gloss values made the score worse.
4. With only alif fixed (the commonest sign, 20%), the annealer found وامثالك / وامثالها for the two words that share
   NHYKHM: N=و, H=ا, Y=م, K=ث, M=ل, D=ه. Then همام, ايضا (P=ي, X=ض), and كن / همتك / ومنك (F=ك, S=ن, U=ت).
5. Homophones: the text needs two signs for lam (M, A: لها, ميل) and two for ha (D, Q: وامثاله, هوا), and probably more
   than one for alif (Z: الا, ولا, ايضا). `solve.py --homophones` allows this at a penalty.
6. Both line ends scan as tawil (... wa-minka laha ayda / ... wa-amthaluha ayda); the rhyme is -ayda.
7. Current skeleton (unknown signs in capitals):
   ولا E8O | Tمثال | كن | ميل | ال | هوا | هVLR | همتك | ZBوا | ومنك | لها | ايضا ||
   8هيG | وامثاله | همام | ولZ | الZ | ولاRت | ولC | لاهWن | وامثالها | Zيضا
   Eight signs occur once (E O V L B G W C), so sense and metre have to fix them.

8. The compiler's note after the cipher, "ووجدته جعل اللام ألفًا…", read as "he made the lam [as] alif": the alif sign H
   also stands for lam. With that rule (`solve.py --shared H --homophones 5`) the annealer converges on
   وللناس امثال كر/كن ميل ال هول … همتك اقول ومنك لها ايضا ‖ اهيف/رهين وامثاله همام ولا الا ولانت/ولاحت ولا للهجر وامثالها ايضا
   (E=ن, 8=ا, O=س, T=ا, Z=ا, B=ق; runs r8, r9 of 16 Nov).
9. Prosody check by a second reader (16 Nov): the metre is tawil (both bayts end u − u/− | u − − −; each line is one bayt of
   44-46 letters). وَلِلنّاسِ أَمْثالٌ scans and fits the theme (letters of one shape as "amthal"). But the skeleton still
   breaks the metre at three places: w3 (F S, a long syllable where tawil needs a short), w8-w9 (همتك ends short where
   a long is needed; اقول too), and w20 (للهجر ends short before وامثالها ايضا). w14 scans only with the sakin pronoun
   (وَأَمْثالُهْ, a recognised licence). So either S, U and the last sign of w20 are misread, a divider is misplaced, or
   the cipher has a further rule (nulls, as on f. 106r, or another shared sign) not yet found.

10. Without dividers (`solve.py --nodiv`) the model sets S = alif, not nun. With S = ا the line ends become
    وما كلها ايضا (line 1) and ولا للهجا وامثالها ايضا (line 2: al-hija' = the alphabet, the letters of spelling, apt for
    a jim/ha quarrel, and it scans), and w20 ends long as the metre needs.
11. Divider-shift hypothesis (`transcription_divshift.txt`): the scribe puts the divider one sign late after kaf, twice
    (w8/w9 همUك | انوا -> همU | كانوا; w10/w11 وماك | لها -> وما | كلها). The annealer then reads line 1's second half
    as ... هما كانوا وما كلها ايضا (U = alif homophone: "the two of them"; run r12, 16 Nov).
    Line 1's first half (ولل E8O Tمثال كا ميل ال هول هVLR) and line 2's first half (8هيG وامثاله همام ولا الا ولاRU) are
    not settled; possibly the same kaf divider shift after Tمثال.

12. Prosody check of the updated skeleton (16 Nov): bayt 1 scans in full as tawil:
    وَلِلْحُسْنِ (or وَلِلنّاسِ) أَمْثالٌ كَأَمْيَلَ لِلْهَوى ... هَوانٌ هُما كانُوا وَما كُلُّها أَيْضا
    (w5/w6 divider falls between article and noun; w7 هوان with V=و L=ا R=ن, or هزبر). The hawa/hawan pair is the
    classic one-letter pun, apt for a tashif; but the sense of كأميل للهوى and of the last clause is only partly coherent,
    so this is a candidate, not a reading.
    Bayt 2, first half scans with the sakin pronoun: رَهِينٌ (or سُهَيْلٌ) وَأَمْثالُهْ هُمامٌ وَلا إِلى.
    Bayt 2, second half (ولانت/ولاحت ولا للهجا وامثالها ايضا) is one syllable too long; w18-w20 re-checked on the image
    (N M H R U | N A C | M H D W S): the transcription stands.

13. Sibling search through the whole volume (16 Nov, images 0006-0217; master TIFFs of 0067, 0068, 0215-0217):
    - **The sender is Ibn al-Qubabi [or al-Qabbani], not Ibn al-Qaysarani**: at 5x the name after "wa-kataba li" has qaf,
      one dotted tooth, a long kashida and final ya, no sin/ra/nun. The same man is "Ibn al-Qubabi al-Haysub" (the
      calculator) on 0067-0068, author of a 7-line cipher with no dividers whose verses repeat words (qad qad qad ...).
      Earlier notes here said Ibn al-Qaysarani: wrong.
    - 0217 reads: "fa-halaltuhu ba'da ta'ab ... wa-huwa: aflaja khasmi wa-ihtajja bi-hujjati / aflahtu fi hujjati wa-khaba
      l-muhtajj. Wa-l-sawab aflajtu bi-jim wa-laysat aflahtu bi-l-ha' al-muhmala wa-innama tashaffa fa-zannaha aflahtu
      ... Wa-kataba li Ibn al-Qubabi fihi" -> cipher -> "fa-halaltuha fi l-hal bi-hudurihi wa-wajadtuhu ja'ala al-lam alif".
      The last words may be the stock formula "al-lam alif harfan wahidan" (lam-alif one sign), cut by the page end.
    - The circle's tricks named by the compiler: lam-alif one sign (0006, 0024, 0049, 0050, 0089, 0212 "wa-laysa
      al-qa'ida kadhalika", 0216); two shapes for one letter, usually called a slip (0012 mim, 0026 ba, 0041 dal, 0049 ta,
      0105 jim, 0118 shin, 0132 waw; theory 0014: "al-sura wahida wa-l-siyagh mukhtalifa"); nulls waw+alif added at the end
      (0216; 0105, where they gave the cipher away); letters dropped (0104, 0107, 0153); dividers missing (0041, 0050,
      0067, 0153); the "tashifi" type (0033): one sign for all letters of one shape (ba/ta/tha/nun/ya; jim/ha/kha; dal/dhal ...).
    - No other cipher by the same sender with a reply on tashif; no other -ayda rhyme except a saying on 0137.
    Consequences to test: (a) "ja'ala al-lam alif [harfan wahidan]" = lam-alif one sign, rather than the alif sign
    standing for lam; (b) nulls (waw, alif) may be present, which could remove bayt 2's extra syllable; (c) a tashifi
    element (one sign for a shape class) is possible in a reply about a jim/ha misreading.

14. Test (a) of step 13 (16 Nov, runs r13/r13b on `transcription_divshift.txt`, `--lamalif`): no sign is taken as the
    lam-alif ligature, so "lam-alif one sign" gets no support; the alif-also-lam rule scores better (-315.8 against
    -334.9). The closing halves stay stable (… كانوا وما كلها ايضا; … ولا للهجا وامثالها ايضا); w1, w7 and w18 still
    vary between runs (وللحرب/وللشمس/وللعشق/وللحسن/وللناس; هتدي/هجره/هوان; ولايه/ولاها/ولاحت). Bayt 2 counts 29
    syllables against tawil's 28 under every variant, so one letter there is probably a null or a word is misdivided.

15. Final prosody pass (16 Nov) with the circle's documented licences (one null waw/alif, divider moves, homophones,
    tashifi classes). Both bayts scan as tawil:
    وَلِلْحُسْنِ (وَلِلنّاسِ) أَمْثالٌ كَأَمْيَلَ لِلْهَوى ... هَوانٌ هُما كانُوا وَما كُلُّها أَيْضا
    رَهِينٌ (سُهَيْلٌ) وَأَمْثالُهْ هُمامٌ وَلا إِلى ... وَلانَتْ (وَلاحَتْ) وَلا لَهْجًا وَأَمْثالُها أَيْضا
    (bayt 2 needs H in w20 as a null alif; no other single null works; divider moves do not change the count).
    Read as sense: هما كانوا وما كلها أيضا; the rhyme وأمثالها أيضا; the amthal / hawa-hawan letter-play. Not read as
    sense: bayt 1 first half, bayt 2 first half, w18-w20. So this is a scanning candidate, not a reading.

16. Rare signs re-read at 2x on the master (16 Nov): the "8" of w13 has a pointed top loop, the "8" of w1 a round one, so
    they may be two signs (8 and 8') and w1/w13 are then not linked; w7's third sign (L) looks like a small lam, i.e. a
    possible third lam homophone (w7 = ه V ل R); w20's W is a small dal-like hook (للهدى "for guidance" is a reading of
    the same length as للهجا). None of this removes bayt 2's extra syllable.

17. Metre-constrained search (`scansearch.py`, 16 Nov): syllable weights of every fully vowelled token in the poetry
    corpus (87,421 forms; prefixed forms approximated), joined word by word against the tawil hemistich. It recovers
    هما كانوا وما كلها ايضا for bayt 1's second half (and proposes هواك / هناك / هواه for w7). For bayt 1's first half
    over 100,000 readings scan (وللدين / وللنفس / وللشمس / وللصبر / والناس امثال كا ميل الهوى ...): with three
    single-use signs in w1 the metre cannot choose. The opening halves are underdetermined by the signs; only a
    judgement of sense (an Arabist; `BRIEF_arabist.md`) can choose between them.

## Remaining gaps (as at closing; the cipher is read in the parent folder)

- Firm: N=و Y=م K=ث M=ل A=ل D=ه P=ي X=ض F=ك, H=ا (and ل at least in w1). Likely: S=ن, T=ا, Z=ا, E=ن 8=ا O=س (وللناس).
- Not fixed with certainty: E 8 O (وللحسن / وللناس), V L R (هوان / هزبر), G, W, C, Q; bayt 2's second half does not
  scan; the sense of bayt 1 is partly coherent only. Earlier list: the full reading is not established, and the three metre failures (w3, w8-w9, w20)
  must be explained before any reading can be called read. Not externally blocked: the next steps are below.

## Escalation (as at closing)

- Siblings: the volume's ~200 solved ciphers (each with plaintext) are a model of this circle's alphabets and conventions;
  the same correspondent (Ibn al-Qubabi) wrote the cipher on 0067-0068 (step 13).
- Metre: build the tawil constraint into the solver (score only keys whose reading scans), and allow nulls and a
  misplaced divider at w3/w4, w8/w9 and w20.
- Re-read U (w8), S (w3, w10, w20) and W (w20) on the master image with a palaeographer's eye.
- Siblings: page through the ~200 solved ciphers for Ibn al-Qubabi's other messages and for the "lam as alif" rule
  and nulls in this circle's practice; the compiler's preface (ff. 1-9) on methods.
