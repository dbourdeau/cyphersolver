# no. 63, ff. 115r (line 28)-116v: blind sign sheet 2411 (24 Nov 2026, Brice Dudout, with Claude)

This sheet follows the re-read of PR #440. It put seven doubtful signs from `../DOUTES.md` to Brice Dudout as a blind sheet:
- one boxed sign per question;
- forms chosen from thumbnails cut from the same letter;
- no values, no readings;
- three control signs: **3/3 passed**.

The selection rule (`sheet-2411-rule.md`, in French, byte for byte as hashed, SHA-256 09f79002...) was fixed before
the thumbnails were built. The key (`sheet-2411-key.json`) was opened only after the answers (`sheet-2411-answers.json`)
were exported. Results: `sheet-2411-results.tsv`.

Images: Gallica btv1b9060015d (public), views 119-121. No image is committed.

## What the answers settle
1. f. 115v l.23 "la **lega** aperta": the sign is S (g), not the double-crossed s, so *lega*, not *lesa*.
2. f. 115v l.00 "**rendera**": the 2nd sign is the gamma-like 7 (e), not iota (o), so *rendera* as written.
3. f. 115r "per **meter** l'esercito": the 2nd sign is the n with inward tail (e), not pi.
4. f. 116v l.00 "**oficio**" and f. 115v l.31 "monstrerebe": both doubtful signs are the looped delta (o), confirmed
   twice. *monstrerebe* stays {probable}: the signs give "monstrrebe".
5. f. 116v l.09 "**deposition**": iota (o).
6. f. 115v l.33 "pa" (6 = p): confirmed, but it gives no word; the group stays unresolved.

## One sign, not two (the reader's form remark)
At q04, Brice noted that our "n with inward tail" (e) and an "italic n" we had labelled n are the same form. Lasry's
key has a single n sign, pi (overhanging bar), and the n with inward tail = e. We tested both merges with the frozen key:
- all to n breaks 11 sure words (et x3, l'esercito, spagnole, unde, essere...);
- all to e breaks the pi words (up to 214 sure words).

Where the italic n can be seen it reads e, and pi carries n. No two-value homophone is shown. **Adopted: italic n =
e.** It is applied at the three places seen, all classed {probable}:
- f. 115r "in compagna **et** per eser qui" (was unread);
- f. 115v l.23 "si sarebe";
- the f. 116v l.00 group, which stays unread.

## Recount (95% rule, 841 cipher words; `../no63_reading_2411.md`, `../no63_signs_2411.txt`)

| | sure | probable | restored | unresolved | code signs | sure + probable |
|---|---|---|---|---|---|---|
| 12 Nov (PR #440) | 743 | 52 | 9 | 25 | 12 | 795/841 = 94.5% |
| after sheet 2411 | **748** | **48** | 9 | **24** | 12 | **796/841 = 94.6%** |

That is 5 more sure words (meter, rendera, lega, oficio, deposition) and one more probable (et). Sure words only:
88.3% -> 88.9%. The stretch is still under 95%, by 3 words. Daniel's rule M (no controls, diagnostic only):
0.919 -> 0.919 (3479 -> 3481 of 3787).

## Not done
- A sign-by-sign review of the other n tokens (pi presumed) for further italic n.
- The looped delta read as U in "bozUSnuzg" (f. 115v l.31).

## Credit
- Blind reader of the sign forms: Brice Dudout.
- Selection rule, sheet and integration: Claude (AI agent).
- Images: Gallica / BnF.

# Sheet 2411-95 (24 Nov 2026, Brice Dudout, with Claude): three single-sign groups

After sheet 2411 the stretch stood at 796 of 841 words sure or probable (94.6%), 3 words under the 95% line. Three
unread groups each hinged on one sign that could be pi (n) or the n with inward tail / italic n (e, Lasry's key, merged
at sheet 2411). They were put to Brice Dudout as a second blind sheet: one boxed sign per question, the two forms shown
as thumbnails cut from the same letter, no values, no readings, three control signs: **3/3 passed**.

The selection rule (`sheet-2411-95-rule.md`, in French, byte for byte) was written before the thumbnails. Its first hash
was 638de718...; amendment 1 (written after the first contact sheet, before anything was shown to the reader) gives the
final hash 19fd37eb..., recorded before the answers. The key (`sheet-2411-95-key.json`, box coordinates on the Gallica
views only) was opened after the answers (`sheet-2411-95-answers.json`) were exported. Results: `sheet-2411-95-results.tsv`.
Images: Gallica btv1b9060015d (public), views 119-121. No image is committed.

## What the answers fix (all three: n with inward tail = e)
1. f. 116r l.16, "nt" -> **et**: *si rispondese, et ben che con buone et vive ragion* (was unread). Sure.
2. f. 116r l.16, lone n -> **e**: *vive ragion e si sforsasi* (was unread). Sure.
3. f. 116r l.31, first sign of nS9pgruo -> **egli° era**: *del qual si parla egli era il marchese di Mantoa*. The letters
   spell "eglierail"; the cut egli era | il is fixed by sense only, so the word is **probable**.

The frozen key is unchanged; only these three signs of the sign file change (`../no63_signs_2411_95.txt`,
`../no63_reading_2411_95.md`). No sure word is broken (two decoded lines differ).

## Recount (95% rule, the same 841-word base)

| | sure | probable | restored | unresolved | code signs | sure + probable |
|---|---|---|---|---|---|---|
| after sheet 2411 (PR #949) | 748 | 48 | 9 | 24 | 12 | 796/841 = 94.6% |
| after sheet 2411-95 | **750** | **49** | 9 | **21** | 12 | **799/841 = 95.01%** |

**The margin is nil.** 95% of 841 is 798.95 words, so 799 is at the line by 0.05 word; one word downgraded gives 798
(94.9%). It holds only on sure + probable; on sure words alone it is 750/841 = 89.2%. With the stricter tokenisation of
our counting script (apostrophes split: 748 sure + 49 probable of 839 words) it is 797/839 = **94.99%**, i.e. not
reached. We state it as "at the 95% line on sure + probable, on the 841-word base", not as exceeded; the state is left
to the maintainer (we leave it read in part). Daniel's rule M was not re-run (the it-cinquecento corpus could not be
downloaded tonight); only three signs changed.

## Still open
The other n tokens (pi presumed) and the looped delta read as U in "bozUSnuzg" (f. 115v l.31).

## Credit
- Blind reader of the sign forms: Brice Dudout.
- Selection rule, sheet and integration: Claude (AI agent).
- Images: Gallica / BnF.

# Sheet 2411-95b (25 Nov 2026, Brice Dudout, with Claude): two single-sign groups, to clear the line

After sheet 2411-95 the stretch stood at 799 of 841 words sure or probable (95.01%), at the line by 0.05 word only. Two
doubts that each hinge on one sign whose form can be seen on the image were put to Brice Dudout as a third blind sheet:
one boxed sign per question, the forms shown as thumbnails cut from the same letter, no values, no readings, three
control signs: **3/3 passed**.

The selection rule (`sheet-2411-95b-rule.md`, in French, byte for byte, SHA-256 b589c88e...) was written and hashed
before the thumbnails were built. The key (`sheet-2411-95b-key.json`, box coordinates on the Gallica views only) was
opened after the answers (`sheet-2411-95b-answers.json`) were exported. Results: `sheet-2411-95b-results.tsv`.
Images: Gallica btv1b9060015d (public), views 119-121. No image is committed.

## What the answers fix
1. f. 115r l.28+ (s115_10): the looped sign after do9yS7n has the form of the looped B (z, as in "Abruzz", f. 115v):
   *con ogni cura et diligenza si dovrebe°* (was "diligen[tia]", restored). Sure.
2. f. 115v (v115_24): the first sign of (5)v9 is the barred looped delta (o): *il che non poco conferiva et serviva o al
   tirar Papa in lega, o per il meno...* (was unread). Sure.

The frozen key is unchanged; only these two signs of the sign file change (`../no63_signs_2411_95b.txt`,
`../no63_reading_2411_95b.md`). No sure word is broken (one decoded line differs).

## Recount (95% rule, the same 841-word base)

| | sure | probable | restored | unresolved | code signs | sure + probable |
|---|---|---|---|---|---|---|
| after sheet 2411-95 | 750 | 49 | 9 | 21 | 12 | 799/841 = 95.01% |
| after sheet 2411-95b | **752** | 49 | **8** | **20** | 12 | **801/841 = 95.24%** |

95% of 841 is 798.95 words: the margin is now 2.05 words (was 0.05). With the stricter tokenisation of our counting
script (apostrophes split, 839 words) it is 750 sure + 49 probable = 799/839 = **95.23%**, so the line is now reached
on both counts (it was 94.99% there). This holds on sure + probable ("read by sense"); on sure words alone it is
752/841 = 89.4%. Rule M was not re-run (the it-cinquecento corpus could not be downloaded); only two signs changed.
The state (read in part or read) is left to the maintainer.

## Not put to the sheet
"egli era" (f. 116r l.31: the group runs on with no visible cut) and vol[e]ndo (no sign between the two letters) cannot
be decided from the form; the other unread groups need several signs or give a value without a word. The T/b and
pi/italic-n probables are unchanged.

## Credit
- Blind reader of the sign forms: Brice Dudout.
- Selection rule, sheet and integration: Claude (AI agent).
- Images: Gallica / BnF.
