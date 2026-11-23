Status: in progress (read in part, about 74%; the open rows give letters but no Arabic and have no outside blocker; PR #834 is open and Elbaum has not been contacted)

# T-S NS J479: Judaeo-Arabic jottings in an invented sign alphabet (Cambridge University Library, Cairo Geniza)

Cambridge University Library, Taylor-Schechter New Series J479; Princeton Geniza Project (PGP) document 8804. One
paper folio, both sides covered with jottings in many directions. Lead from the Hebrew-script sweep of 6 Nov 2026
(`research/sweep_2026-11_hebrew/`), ranked first of the unread pre-1400 Arabic/Hebrew-script ciphers on 20 Nov 2026.

## Prior work (contamination question)

- **PGP record 8804** (read 20 Nov 2026): Judaeo-Arabic "in an idiosyncratic (unique?) cipher"; no earlier than the
  mid-13th century (hand, formulary, a poem by al-Būṣīrī, 1213-95). Contents listed: (1) the alphabet several times,
  right to left and left to right; (2) the signature *al-faqīr Isḥāq al-yahūdī* several times; (3) two verses of the
  *Qaṣīdat al-Burda* (أمن تذكر جيران بذي سلم); (4) legal jargon *jarā dhālika fī ākhir jumādā al-thāmī(!) sanat ar[...]*;
  (5) two pornographic sections, one ending כל הדה כדב ("all this is lies"). Also two lines of an Arabic-script petition,
  scattered Arabic words and one Hebrew-script word כסתבאן. No transcription or translation is published there.
- **Alan Elbaum**, Cambridge Genizah blog, 22 Jun 2022 ("Secret codes and erotic prose"): about 22 signs written in a
  row several times; mapped to the Hebrew alphabet; language Judaeo-Arabic; an annotated photocopy with Hebrew letters
  over the signs (`img/elbaum_annot.png`, 1200 px, low resolution). Mamluk or Ottoman date.
- Elbaum writes that he came across the fragment while looking for uncatalogued or minimally catalogued documentary
  fragments, and quotes the two Burda verses in S. P. Stetkevych's translation (*The Mantle Odes*, 2010, p. 92).
- So **Elbaum has a working key and has read parts** (the items above). No full reading is published. Our attempt
  starts from the images and the alphabet rows; Elbaum's annotated copy is used only to find lines and, later, to
  check, and that use is recorded here. Anything we find goes to Elbaum before it is published.

## Access

- Cambridge IIIF by plain curl: `https://images.lib.cam.ac.uk/iiif/MS-TS-NS-J-00479-000-0000{1,2}.jp2`. Full size
  3097 x 4366 and 3069 x 4319 (info.json). `stitch.py` fetches 1024-px regions and stitches `img/full1.jpg`,
  `img/full2.jpg`; `img/p1.jpg`, `p2.jpg` are the 2000-px versions. Images git-ignored.
- Elbaum's images: `genizahfragments.lib.cam.ac.uk/wp-content/uploads/2025/05/t-s_ns_j479r.jpg` and
  `..._annotated.png`.

## Method

1. The alphabet rows at the foot of side 2 (22 signs). `glyph_chart.png` labels them I U E A N 4 c B d - < p P q w O
   6 S X 9 C 7 in the order they stand on the page, left to right.
2. Shape transcription of both sides with these labels (`tr_side1.md`, `tr_side2.md`).
3. A Judaeo-Arabic stand-in model, `lang` model `ja-translit` (Arabic papyrus editions and the Qur'an written in
   Hebrew letters, Geniza spelling; `build_ja_corpus.py`).
4. Substitution solve (`solve.py`), crib on the Burda verses and the signature.

## Steps

1. 20 Nov 2026. PGP record, Elbaum's blog post and annotated copy read; full-resolution images stitched.
2. 20 Nov 2026. Alphabet row read; glyph chart made. Common short groups suggest מן and the article אל.

3. 20 Nov 2026. Side 2 transcribed in shape labels by an agent (`tr_side2.md`, 351 signs; it added variant labels
   a s 8 n 2 y h e t g z 5). Frequencies: I 23, - 18, p 16, P 16, < 11 ... in 171 text signs.
4. 20 Nov 2026. **Key and direction found (`readkey.py`).** The scribe writes **left to right**: signs inside a word
   and words inside a line run left to right, and the alphabet rows are in Hebrew order from left to right:
   I א, U ב, E ג, A ד, N ה, 4 ו, c ז, B ח, d ט, - י, < כ, p ל, P מ, q נ, w ס, O ע, 6 פ, S צ, X ק, 9 ר, C ש, 7 ת.
   Variants: a = ת (also for ة), s = ר, 8 = ר, e = ח. The transcriber's p/P and d/q are sometimes swapped.
   Read this way, side 2 gives:
   - the two Burda verses: אמן תדכר גיראן בדי סלם / מזגת דמעא גרי מן מקלה בדם / אם הבת אלריח מן תלקא כאטמה /
     ואומט אלברק פי אלטלמא מן אצם (lines S2L09, S2L07-08, S2L06, S2L05; ض and ظ both written ט);
   - the legal phrase גרי דלך פי אכר גמאדי אלתא[מי] (S2L02);
   - the Hebrew-script word of PGP, כסתבאן (S2L15), here in cipher;
   - the frequent short words פי, יא, מן.
   The system is a simple substitution of the 22 Hebrew letters, written left to right, with a few variant signs.

5. 20 Nov 2026. Side 1 transcribed in shape labels by a second agent (`tr_side1.md`, 328 signs in 18 cipher rows plus
   three Arabic-script lines; new labels e y h z b f o 8 m; f is the side-1 form of P = מ). Under the key: the
   signature אלפקיר אסחאק אליהודי in both margin columns and in S1L11, S1L13; S1L01 ends כל הדה כדב ("all this is
   lies"); S1L06 has אלחמד ללאה רב אלעאלמין; S1L02-05 an erotic passage (קער, רחמה, זבי, גואה, כוסהא, ידכל).
   Only the Arabic petition (S1AR02-03) is upside down relative to the cipher lines.
6. 20 Nov 2026. **Elbaum's annotated copy shows side 1 turned 180°**, with his Hebrew letters reading right to left
   above the signs. So the scribe wrote normally, right to left, and the cipher lines are photographed upside down;
   our left-to-right key is the same key seen the other way up. His legible readings agree with ours where checked
   (חנאמ?ת כל הדה כדב; אל קער; רחמה). This copy was looked at after the key was found, for checking only.
7. 20 Nov 2026. Two agents re-read every line in Hebrew letters under the key, without Elbaum's copy
   (`tr_hebrew_side1.md`, `tr_hebrew_side2.md`).

8. 20 Nov 2026. **Reading compiled (`reading.md`).** What reads: the signature (four times), the two Burda verses
   (with the scribe's phonetic spellings: tanwīn as נ, rhyme vowel as י, ג/ז swapped in מגזת), the date formula
   (גרי דלך פי אכר גמאדי אלתאמי), כסתבאן twice, a love-poetry line (יא כי מן אלהגר יא כלי ...), אלחמד ללאה רב
   אלעאלמין, and an erotic passage in Egyptian colloquial about a woman named Raḥma (אל קער בתאע רחמה, זבי, כסהא,
   ידכל) ending חמאמתי כל הדה כדב, "my dove, all this is lies". Dots mark ض/ظ (under ט), ذ (under ד) and خ (under כ).
   About 314 of 450 non-alphabet cipher letters (70%) are in passages that read: **read in part**.

9. 20 Nov 2026. **Variant alphabet on side 1.** In the side-1 alphabet row S1L14 the 7-sign stands in the ב (and ש)
   slot and the loop-with-tail sign in the צ (and ת) slot. In side-1 text the loop-with-tail is ת (בתאע, חמאמתי) and
   the 7-shaped sign is ב: the S1L04 verb ויתכ then reads ויבכ, the same verb as יבכ in S1L02 (بكّ "to press, ram";
   sexual sense not yet checked in a dictionary). A further agent is attacking the seven unread rows with all slot
   variants (`tr_hard_rows.md`).

10. 20 Nov 2026. **Hard rows** (an agent, `tr_hard_rows.md`; Elbaum's copy used as a check, readings from it marked).
    - **S1L03 is an alphabet row** ב-ל written with the page turned 180° (its "odd" signs are c, 4, E upside down).
    - **The verb is يبكّ** (Lisān al-ʿArab, بكك: "بَكَّ الرجلُ المرأةَ إذا جهدها في الجماع"); S1L02 יבכ גואה and S1L04
      ויבכ גוה כסהא are parallel. ينيك does not fit the three signs.
    - **S2L10 contains רחמה** (Raḥma) again. S2L17's last word may begin يا ليت. S1L10 is a letter trial
      (near-palindromes, each letter in both of its forms).
    - Slot comparison of all 12 alphabet rows: 7 serves for ת, ש and ב; the loop-tail for ת and צ; צ has five forms;
      ר four (9, s, 8, 5). In the text 7 is only ב (side 1), the loop-tail only ת.
11. 20 Nov 2026. **Year** (an agent, `tr_year.md`). The date formula continues one line: **סנת אר** ("the year
    fo[ur]..."), PGP's *sanat ar[...]*, and stops against an alphabet row; no number follows anywhere on the leaf. The
    year ended in 4 or was a round x40 (units come first in Arabic), after c. 1250. S1L13's "174" is three key
    signs (אתו/אבו), not a year.
12. 20 Nov 2026. Recount after steps 10-11: about 304 of 407 non-alphabet cipher signs read (75%); without the
    letter trial S1L10, about 80% of the text rows.

13. 20 Nov 2026. **Dating from formulas and vocabulary** (an agent, `dating_evidence.md`, sources cited there).
    - The petition pairing "المواقف العالية ... اعلاها الله تعالى" is found in only two Geniza petitions: ENA 3754.11
      (PGP 12757, c. 1600) and T-S Ar.41.14 (PGP 21062, "late"). Qalqashandī and the Mamluk chronicles have
      "al-mawāqif al-sharīfa", never "al-ʿāliya".
    - "جمادى الثاني" (masculine) is rare before the 15th century: about 100 dated Geniza documents and the Arabic
      Papyrology Database up to the 16th century use ākhir/ākhira (one Maghribi exception, 1415).
    - The Burda floor: al-Būṣīrī d. c. 1294-97; earliest dated Egyptian copies c. 1365.
    - No dating value: بتاع (already 1217), كستبان, "جرى ذلك", the spelling.
    - **Most likely c. 1400-1650 CE (c. 800-1060 AH), probably 15th-16th century.** With step 11, the Hijri year
      ended in 4 or was a round x40. The weakest link: both late-leaning arguments rest on absence in small samples;
      Ottoman court registers were not searched.

14. 20 Nov 2026. **Orientation of every open row** (an agent, `tr_turned_rows.md`). S1L07 was written with the page
    turned (in the turned crop X has its dot below and N, C, < take chart shapes): [...]?ל קרשכד הדה אלפרא, only הדה
    reads; the blot at its end belongs to the margin column. S1L08, S2L10, S2L13 and S1L13 are in the main
    orientation; S1L08's repeated ל-pairs look like letter practice. No sign moves from unread to read; count about
    302 of 406 non-alphabet signs (74%).
15. 20 Nov 2026. The user asked for the write-up and a pull request with Brice Dudout as reviewer, publishing before
    Elbaum is contacted (the user's decision; Elbaum credited on the page).

16. 20 Nov 2026. **CTTS project, corrected by hand-editing the project files (model-made; for the user's review).**
    Following the repository's CTTS pipeline (`research/ctts/README.md`): 46 straightened bands (one per cipher row,
    signs turned upright; margin columns and upside-down lines included), candidate boxes from a finer segmenter for
    separate-stroke signs (`research/ctts/segment_glyphs.py`, 682 boxes), two blind first-pass labelling agents (one
    per side; overlays and the sign chart only). 5c: the blind labels were aligned with this target's transcription
    band by band (`align_j479.py`): 336 of 637 boxes agreed, 91 disagreed, 162 boxes and 204 transcription signs had no
    counterpart. So the first pass was not a gold standard. Correction (`prep_review_j479.py`, `apply_decisions_j479.py`):
    two reviewers decided every non-agreeing box and every missing sign on enlarged, overlay-free crops, with the
    transcription in view (so the corrected project is no longer independent of it): 167 type changes, 81 boxes deleted
    (stains, fragments of neighbouring lines), 3 merges, 15 splits, 129 boxes added, 103 signs marked uncertain (`?` in
    the type name). Result: **697 boxes in 84 symbol types over 46 images**; 585 of the transcription's 679 signs line up
    with the boxes in sequence. About 58 transcription tokens were wrong on the image (S1L03, S1L07, S1L01, S2L04-06, S2L10
    among them; the alphabet columns S2V01-02 do not correspond to the transcription at all). New labels: `#` (overwritten
    clusters, S1L12, S1V02) and `K` (one sign at the end of S1V01). Computer use of the CTTS window was not available,
    so, as in the it1583 pilot, the corrections were written to `positions/` and `colors.txt` (git-ignored project folder
    `research/ctts/projects/tsnsj479/ctts/`) for CTTS to restore; the project has not been opened or checked in CTTS and no
    person has checked the sign table. The page's table (`key_table_j479.py --corrected`) shows the 592 boxes not marked
    uncertain, drawn here in CTTS's style, not exported from the CTTS window.

    **Second round (21 Nov 2026), after a line-by-line review of the sign table (`ctts_table_review.md`).** The review found
    four errors that change the key and about 70 doubtful cut-outs. 282 boxes (every box in the confused rows U, a, 7, P, p,
    q, d, the resh rows 9/s/8/5, and every flagged cut-out) were re-judged by two reviewers on enlarged crops with context
    (`prep_recheck_j479.py`, `apply_recheck_j479.py`): 58 relabelled, 4 deleted, 17 split, 37 more marked uncertain. Main
    findings: **the cup U (ב) exists only on side 2 (12 boxes)**; on side 1 all 14 flagged U boxes were the tailed loop and
    became `a` (ת) (side 1 now has 15 `a`, 0 U); the 7 row held mostly plain strokes (side 1 now has 2 sevens, side 2 has 4);
    on side 2 the `s` row is the same sign as `8` (6 of 7 relabelled); P/p and q/f/d were redrawn by the curl and stem rules.
    The table no longer prints Hebrew letters for `y`, `n`, `o` (never established) and puts ר on `5`. **Now 711 boxes in
    86 types, 140 uncertain, 569 certain boxes in the table (36 rows); 530 of the transcription's 679 signs line up in
    sequence** (down from 585, because the review corrected the transcription's own side-1 labels, e.g. U for a tailed
    loop). Still open: many boxes are badly placed (too tall, narrow or touching a neighbour) and were not redrawn, a few
    sit on the mount edge, K and the S row are single or mixed shapes; the project has not been opened in CTTS and no person
    has checked it.

    **Third round (21 Nov 2026), on the user's reading of the table.** The user saw that three rows each hold two shapes and
    asked for every row from f downward to be re-reviewed. 168 boxes (rows B, -, <, f, g, h, m, n, o, s, t, y, z) were
    re-judged on enlarged crops (`prep`/`apply_recheck3_j479.py`): **B splits into `B` (pointy printed, 14) and `Bc` (round
    cursive, 6, all on side 1); `-` into `-` (the `>`-like flat top with a diagonal tail, 26) and `J` (backward C, 15);
    `<` into `<` (plain angle, 10) and `<5` (5-shape with a long top stroke, 31)**; the reviewer called four `J`/`-` boundary
    cases by judgement. Below f: 12 boxes deleted (mount-edge ghosts, cracks, a stray cluster), f cut from 19 to 11 certain
    boxes (the rest were stroke clusters or `f` look-alikes, now uncertain), three `s`/`y` boxes became `a`, one `n` became
    `m`; `s` and `t` have no certain box left. All remain model-made. **Now 699 boxes in 83 types, 127 uncertain, 570
    certain boxes in 38 table rows.**

    **Person's check of the table (21 Nov 2026, Daniel Bourdeau, on the printed table, without AI).** He ticked rows
    I, U, p, q, O, 6, S and X as correct; circled 33 cut-outs as wrong (rows A, N, 4, c, B, J, <, w, 9, 7, 5, 8, a, b, f and
    six P cut-outs); drew a long circle with an arrow over the right-hand half of row J (five boxes) meaning they belong in
    `-`; put question marks beside h, m, n and o, and wrote "d" beside o. Applied (`apply_user_marks_j479.py`,
    `marks_applied.tsv`): the circled and questioned boxes are marked uncertain (so they leave the table), the five J
    boxes became `-`, and the o box (S2L22_9, the alphabet row's tet position) became `d`. Rows he did not mark (E, A to c
    apart from the circled cut-outs, B, Bc, d, -, <5, C, 2, e, y, z ...) are not confirmed by anyone. **Now 699 boxes in 82
    types, 169 uncertain, 528 certain boxes in 34 table rows.** Not opened in CTTS.

    **Second pass of the person's check (21 Nov 2026, same person, on the redrawn table of 528 boxes).** Ticked: I, U, E,
    A, 4, c, B, Bc, d, <, p, q, 6, S, X, 9, C, 7, 5, b, e, f, y, z (one tick sits between rows E and A, taken for both,
    and one between N and 4, taken for 4). Circled 13 cut-outs: N (1, the M-shaped S2L15_6), J (1), P (6), O (1, the plain
    ring S1L05_1), 8 (1), a (3). Not marked: `-`, `<5`, w, 2. Applied (`apply_user_marks2_j479.py`, `marks2_applied.tsv`):
    the 13 circled boxes are marked uncertain. **Now 699 boxes in 82 types, 182 uncertain, 515 certain boxes in 34 table
    rows.** In all the person circled 46 cut-outs and moved five J boxes to `-`; h, m, n, o (questioned) are out of the
    table. Rows not yet confirmed: `-`, `<5`, w, 2, and the questioned h, m, n, o. Not opened in CTTS.

    **Round 6 (21 Nov 2026), the owner's two points.** (a) The owner flagged the six circled P cut-outs as probably `f`:
    all twelve P boxes circled in the two passes (6 + 6) show the f shape (a stem with a loop at top right crossing into
    a lower-left loop) and became `f`. (b) The owner thought the 7s are `>`s. A reviewer measured the scribe's alphabet
    rows (S2L23, S2U02, S1L14, S1L09, S2L20): the 10th sign (yod, `-`) is always small (height 26-47, aspect 0.4-0.6, a flat
    dash with a short hook), the 22nd (`7`) is tall (height 78 or more) with a curl and a long straight diagonal tail, and
    the Burda word פי (S2L05) has the small dash. So the hypothesis holds in part: 6 long `>`-shaped boxes of the old `-` row
    became `7`; the small dashes stay `-`; 5 round J hooks became `-` (the series from dash with short hook to rounded hook is
    continuous in S2L09_8 and S1L09 box 11; the 4 large deep-C hooks are in no alphabet slot and stay `J`); 3 old 7 boxes
    went elsewhere (two to `I`, one to `-`); 14 boxes marked uncertain. (c) The owner noted the last three cut-outs of row `a` do not fit: S2L06_5 (a long wavy stroke, perhaps w) is marked
    uncertain, S2L06_21 (a narrow strip over a P stem, overlapping the next box) deleted, and S2L06_22 (one box over a P and an a)
    split into `P` and `a` (`apply_round7_j479.py`). **Now 699 boxes in 82 types, 179 uncertain, 518 certain boxes in 34
    table rows** (`-` 25, `J` 4, `7` 7, `f` 20, `P` 18, `a` 23). The alphabet rows S2V01-02 could not be read for
    these two positions. Not opened in CTTS; the rows `-`, `<5`, w and 2, and the new `7` and `f` contents, are not yet
    confirmed by the person.

    **Per-side sort of the 7 / dash shapes (21 Nov 2026, a fork of the session, on the owner's "yes apply it").** The label test
    (`test_labels_known.py`: nine rows with an established reading decoded from each label version, difflib letter ratio:
    blind first pass 0.52, first correction 0.86, round 5 0.84, round 6-7 0.82) showed round 6's size rule had moved three
    yods of the Burda lines (S2L09 twice, S2L07 once) from `-` to `7`. The long `>`-shaped stroke is the yod on side 2 (גיראן,
    ידי, גרי, פי), while on side 1 it is the scribe's bet in S1L02 יבכ and S1L04 ויבכ but also the yod in the margin
    signatures, so the side-1 rule is not settled. Applied (`apply_perside_j479.py`, `corrections8.tsv`): the three yods back
    to `-`; the resh loop of אלברק (S2L05_10) `?7` to `?8`; the two side-1 text 7 boxes not yet marked (S1L08_5, S1L13_6)
    marked uncertain. Agreement with the established readings 0.841. **Now 699 boxes in 82 types, 180 uncertain, 517 certain
    boxes in 34 table rows** (`-` 28, `J` 4, `7` 3, `f` 20, `8` 7). Decoding the open rows (S1L05-08, S1L13, S2L10, S2L13,
    S2L17, S2U01) from these labels (`decode_ctts.py`) gave **no new word**: the correction work has not improved the reading.

    **Person's review of the key, stated (21 Nov 2026, Daniel Bourdeau).** After the rounds above (24 rows ticked, 46
    cut-outs circled and removed, the P-to-f, 7/dash and `a` points applied, and the final table sent to him), the owner
    states that he reviewed the CTTS key as a human, so it counts as human-reviewed. What that covers: the printed table
    of 518 certain boxes in 34 rows, by eye and without AI; it does not cover the 181 boxes marked uncertain, nor the
    box geometry in the project files, which were not opened in CTTS.

    **More boxes made certain (21 Nov 2026, on the owner's "can't we do better").** 24 of the 180 uncertain boxes sit in rows with an
    established reading (the Burda lines S2L05-09, the signature S1L11, S1L01, S1L02, S1L04, S2L15) and decode to the verified
    letter; they lost their `?` (`settle_by_reading_j479.py`, `settled9.tsv`). These are certain because the verified text needs
    this sign here, not because the person checked them by eye, so the table is less independent of the reading for them.
    **Now 699 boxes in 82 types, 156 uncertain, 541 certain boxes in 37 table rows.** Of the 156: 60 sit in the alphabet rows and
    columns (the slot fixes the letter; not yet used), the rest in text rows, many of them badly placed boxes that need
    redrawing in CTTS, plus the cut-outs and rows the owner circled or questioned.

    **Alphabet rows settled by slot position (21 Nov 2026, on the owner's "yes, do it").** A reviewer matched each of the 60 uncertain
    boxes in the 13 alphabet bands to its slot in the Hebrew order (`alpha_decisions.json`, `apply_alpha_j479.py`,
    `alpha_applied.tsv`): 29 settled, 12 relabelled and settled, 3 fragments deleted, 16 kept uncertain (out-of-sequence boxes,
    shapes that do not fit the slot, one p/P doubt). Row directions: left to right in S2L23, S2L22, S2L21, S2U02, S2U03,
    S1L09, S1L15; right to left in S2L20 (box n is slot 23-n) and S1L14; the columns S2V01, S2V02 read right to left with
    the glyphs turned 180 degrees; S1L03 is a turned alphabet B-to-L; S1L16 is letter practice. Broken sequences: S2V01 (two
    O, two I, a repeated tail), S2V02 (a mount hole over slots 10-12), S1L09 (slot 1 holds a 7-shape), S1L15 (t and y skipped),
    S1L14 (an extra sign after the last I), S2U02 (I U E A twice), S2U03 (tail n, 2, I), S2L22 (box 18 is E where S belongs). These
    boxes are certain by position (the slot fixes the letter and the shape does not contradict it), not by an independent look at
    the shape; weaker settles: S2V01_21, S2V01_9, S2V02_17, S2U03_6, S2L20_4, and S2V01_24 and 25 judged one A. **Now 696 boxes in 80
    types, 112 uncertain, 582 certain boxes in 38 table rows.** Agreement with the established readings unchanged (0.841).

## Result

Key recovered from the ciphertext: the scribe's own alphabet rows (unlabelled, in Hebrew order) plus the frequent
short words פי, יא, מן fixed every sign; the Burda verses then confirmed the key letter for letter. A simple
substitution of the 22 Hebrew letters with a few variant signs and diacritic dots, Judaeo-Arabic plaintext. Read in
part (about 74% of the non-alphabet cipher signs). Elbaum had mapped the signs and read parts before us (PGP 8804); his reading is unpublished, and his
legible annotations agree with ours.

## Remaining gaps

- S1L07 except הדה, S1L08, S2L10 except רחמה, S2L13, S2U01 (about 75 signs) - blocker: open-codes; clear signs that read
  as letters but give no Arabic after every slot variant and both orientations were tried (steps 10, 14); S1L08 and
  S2U01 look like letter practice. Needs a reader of Egyptian colloquial Judaeo-Arabic and Elbaum's own readings.
- First words of S1L05 and S1L06, the tail of S1L13, the last word of S2L17 - blocker: open-codes; letters read,
  meaning not found.
- Holes in the paper (the word after من الهجر in S2L19, 0-4 letters at the start of S1L07, a few in the middle of S1L08) - blocker: illegible; lost in holes.

Not counted as gaps: S1L10 is a letter trial, not text (near-palindromes, each letter in both of its forms); the
Arabic-script lines on side 1 (petition and top line) are not cipher and are read only provisionally.

## Escalation

- [x] siblings: the Geniza's other cipher fragments (T-S NS 70.1, T-S AS 205.186, T-S AS 187.240, T-S 13J18.19) use
  other systems; no sibling leaf by Isḥāq found in PGP.
- [n/a] clear-pages: a single practice sheet; the only clear text is the Arabic-script petition, which is not a
  decipherment.
- [x] known-keys: the scribe's own twelve alphabet rows compared slot by slot (`tr_hard_rows.md`); every variant value
  tried on the open rows.
- [x] print: PGP 8804, Elbaum's 2022 blog post and annotated copy (as a check), the Burda's standard text; nothing
  else published on the fragment (`dating_evidence.md`).
- [x] key-rebuild: frequency, word-pattern and crib work; the variant alphabet of S1L14 gave the verb ويبكّ.
- [x] retry: every open row re-read in both orientations with all variants (steps 10, 14).
