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
