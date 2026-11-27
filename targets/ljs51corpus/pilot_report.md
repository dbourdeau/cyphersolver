# LJS 51 key rebuilding: pilot on four chains (28 Nov 2026)

Tool: `targets/ljs51corpus/rekey.py` (`python rekey.py A | A2 | A3 | B | C | C2 | D`). Key tables: `keys/<chain>.json`
(key, alignment sign by sign, selection table, measures, controls, held-out lines). Cluster sheets:
`output/ljs51/keys/<chain>/key_sheet.png` (one row per cluster) and `cluster_NN.png` (every member, labelled with the
aligned letter in transliteration and its sign index). Held back from the site, README and DECODE (CORPUS rule of 27 Nov).

## How to read the numbers

- Signs come from `segment.py` (right to left, dividers kept as soft word breaks). Shape classes: HOG + blurred pixels + box size,
  PCA(30), Ward; the number of classes k is chosen **by the fit itself** among a small grid (highest z-score of letter-side fit plus
  rasm purity against 8 shuffles). Silhouette is printed in each chain's `selection` table; it is flat (0.25 to 0.37) and picks nothing.
  Choosing k with the plaintext is a degree of freedom, so the control below repeats the whole procedure with that k fixed.
- Alignment: global DP, hard EM (key re-learned from its own alignment, 10 rounds, position prior only in the first three). Moves:
  match, surplus sign, dropped letter, lam+alif on one sign; hamza is a letter that may be dropped cheaply; dividers score +1.2
  at a plaintext word end, -1.6 inside a word.
- **A key learned from its own alignment is self-consistent evidence only.** Three measures say how much more than that:
  1. *Control*: the same signs, the same k, the same EM against the letters shuffled (word layout kept), 100 shuffles. Mean and maximum are given.
  2. *Held-out*: leave one line out. The key (class to letters) is learned from the aligned pairs of all other lines; the held-out
     signs are decoded top-1 (class to its most likely letter) and compared with the letter the full alignment puts there.
     "rasm" = same skeleton group (b t th n y; j H kh; d dh; r z; s sh; S D; T Z; c gh; f q; others alone), the right target for tashifi.
     The held-out figure also has a shuffled control (30 shuffles, key learned from the shuffled alignment).
     Caveat: the plaintext span of the held-out line is taken from the full alignment (the key is not).
  3. *Fit definitions*. **letter-side fit** = share of aligned pairs whose class is the modal class of their letter (the "722 of 770" kind
     of figure); **class purity** = share whose letter is the modal letter of their class; **rasm purity** = share whose letter lies in the
     modal skeleton group of their class (class to group). For a tashifi cipher the last is the one that must be high.
- "aligned" = signs in a match move / signs.

## Summary

| chain | signs | letters | aligned (matched signs) | fit (letter-side / rasm purity) | control (mean, max) | held-out top-1 | held-out control | verdict |
|---|---|---|---|---|---|---|---|---|
| A f. 63v l.1-6 (image 131) | 79 | 79 | 98.7% (78/79; 1 surplus, 1 dropped) | 79.5% letter-side, 82.1% class purity, 87.2% rasm | 36.3% / 42.3% (letter-side) | 60.3% letter, 67.9% rasm | 3.0% / 9% | key rebuilt in part |
| A2 trees f. 63v l.8-12 | 78 (by red anchors) | 79 | 100% (forced) | 41.0% | 40.0% / 47.4% | 2.6% | 1.2% / 5% | failed |
| A3 red letters over the trees | 78 | 79 | 100% (forced) | 39.7% | 37.7% / 46.2% | 2.6% | 2.6% / 6% | failed |
| B f. 57v l.4-10 (image 119, not 120) | 79 | 80 | 94.9% | 52.0% letter-side, 25.3% purity | 47.8% / 57.3% | 1.3% | 2.0% / 9% | failed (no fit above chance) |
| C f. 9r l.6-11 (image 22), first 37 signs, 1 sign per letter | 76 (37 used) | 38 | 100% of the window | 64.9% letter-side, 78.4% purity | 45.7% / 54.1% | 27.0% | 4.1% / 11% | partly: first half only, not a key |
| C2 same block, 2 signs per letter | 76 | 38 | 97.4% | 40.5% | 40.3% / 43.2% | 0% | 3.2% / 11% | failed (hypothesis not supported) |
| D tashifi ff. 14v l.7 - 16v l.5 (images 33-37) | 778 | 770 | 96.9% (754 pairs; 24 surplus, 16 dropped) | **93.6% rasm purity (91.7% of all 770 letters)**; letter-side 76.0% (18 clusters split 15 classes) | rasm 24.3% / 26.8%; letter-side 17.9% / 19.4% | 93.6% rasm (letter 56.4%) | 3.4% / 5.1% rasm | key rebuilt |

Segmenter counts on the master: C has 76 signs on the segmenter's lines 6-11 (the brief says lines 7-12 and 80 signs: a line-number offset;
the segmenter's page index counts the single-line block at the top as line 1), D has 778 where the earlier agent counted 766 (+12: 9 of them on 16r,
where the segmenter reads 199 against 190).

## A. f. 63v l.1-6 (image 131): the couplet, one sign per letter

Plaintext as read on the master (right margin turned 90 degrees clockwise; the line "والبسيط" above it is the metre, not part of the text):

    ابري كبير والصغير يقول لي اطعن حشاي به وكن صنديدا
    ناديت هذا الاحول فقال لي عندي بحور وثلثه تقليدا

Draft confirmed word for word. 40 + 39 = 79 letters (hamza-free). Doubtful: "ثلثه" (smudged by a
thumb mark in the second hemistich; the letters are ث ل ث ه as far as visible).
Signs: 79 on the segmenter's lines 1-6 (15, 14, 15, 14, 14, 7), 19 dividers; 79 = 79 letters. 22 clusters (k = 22 chosen; grid 10 to 36 gives letter-side
fit 85 to 63% as k rises, z-scores 10 to 13 against shuffles at every k).
Fit: 78 of 79 signs aligned, 1 surplus sign, 1 letter dropped; fit 79.5% against 36.3% (max 42.3%) for shuffled text; held-out lines 60.3% top-1 letter
(control 3.0%, max 9%); per-line held-out consistent letters: l.1 10/15, l.2 9/14, l.3 10/15 (14/15 as a set), l.4 6/14, l.5 7/15, l.6 5/6.
Cluster sheet: `output/ljs51/keys/f63v_couplet/key_sheet.png`. Key table (cluster: letters aligned): c0 ي 11 (ب 1, ا 1); c15 ا 9 (ل 1); c1 و 5;
c9 ن 4 (ش, ث); c4 ل 4; c2 د 4; c12 ر 3; c16 ق 3; c10 ه 3; c8 ك 2 (ن, ل); c6 ص 2; c11 ب 2 (ت); c3 ل 2; c17 ع 2; the other 8 clusters hold one or two signs.
The shapes are one letter-like sign per letter shape (alif a chevron, ya a clean arch, waw a "3", ayn a comma-like C), with look-alike pairs
(ya/ba/nun, lam/kaf, lam variants as 4 clusters).
Problems: (1) with 79 signs and about 20 distinct letters most classes have one to four members, so a class seen once cannot be checked and a held-out line
meets unseen classes (the held-out misses are mostly letters whose only occurrence was in the held-out line); (2) over-split (lam in 3 clusters, dal/ayn singletons);
(3) the first three signs of the block share a segmentation error with a dot (c8 contains a dotted alif). Verdict: key rebuilt in part (the 12 most frequent
letters are consistent; a full 28-letter alphabet cannot come out of 79 signs on its own, it needs the sibling chains that use the same alphabet).

### A2/A3. The tree figure, 5 rows under the couplet

There are 78 red letters of letter size under the five tree rows (14, 17, 17, 14, 16 per row), not 79: one is lost or merged. The tool takes one tree per red letter (a
window under it, constant scale) and the red letter's own crop, in reading order (rows top to bottom, right to left).
Result: neither the trees (letter-side fit 41.0% against 40.0%, max 47.4%) nor the red letters (39.7% against 37.7%) align with the couplet; four other orderings
(reversed, rows left to right, boustrophedon, bottom up) give z-scores below 2.5 as well. Causes: (a) my tree crops are poor (the window cuts the crowns of tall trees,
takes branches of the neighbours, the baseline arcs, the next row's red letters); silhouette of the tree clusters is 0.08 to 0.12, i.e. no shape classes found;
(b) the red letters are 15 to 55 px strokes and my crop features cannot separate them; I read the first red letter of row 1 by eye (an alif, the first letter of the plaintext), but did
not read the rest, so whether the red letters spell the couplet at all is **not established**; (c) the picture is organised in arcs sharing a baseline, not in a row of trees, so
the reading order is unknown. The brief's idea (trees differing by number of branch pairs, height, a Y fork) needs a proper tree segmenter: stem by vertical opening finds about 100
stems including text strokes and misses the tall trees. Key tables: `keys/f63v_trees.json`, `keys/f63v_treered.json` (not meaningful).

## B. f. 57v l.4-10 red-glossed block (image 119; image 120 is f. 58r)

The brief names image 120; the block is on **image 119** (f. 57v, formula 6 + 2*56 + 1). Image 120 (f. 58r) has the second verse on its top lines and below the compiler's
account, and a second cipher of 42 signs on its lines 12-14 which I did not use.
Plaintext as read on the master. f. 57v l.12-13:

    على وجهه ماء الجمال المرقرق يزيد اذا رددت طرفك رونقا          (43 letters with hamza)

f. 58r l.1-2 (the second verse): `تبدي فاخفي صبر عشاقه وكم عيون بدر مع حين اشرقا` (37 letters; "بدر" and "حين" doubtful, last word broken over the line end: اشر / قا). Total 80 letters
for 79 signs and 87 red marks (76 red letters after dropping specks and dots).
The compiler's account on f. 58r l.3-9 says he wrote two verses and, from the first, put its sadr on the ajz of the second and "arranged" the rest; I read it only in part, so the cipher
may encode a recombination of the two verses, not verse 1 then verse 2. Not checked.
Result: no fit above chance. 79 signs against 80 letters aligned 94.9% (4 surplus, 5 dropped), letter-side fit 52.0% against 47.8% (max 57.3%), class purity 25.3% against 24.9%;
held-out top-1 1.3%. k = 10 was chosen only because every z-score is near 0 (grid 10 to 36). Cluster sheet: `output/ljs51/keys/f57v_glossed/key_sheet.png`.
Red letters as an independent key: I read the 13 red letters over l.4 by eye on the master: عليوجههماالجم, i.e. exactly one red letter per sign, and they spell the plaintext
for the first 10 letters (على وجهه ما), then the red text lacks one of the letters of ماء ال (the hamza, or the alif of the article); 9 of 13 agree with the DP letters
(the DP puts the hamza on a sign). Over the whole block the segmenter finds 76 letter-sized red marks on 72 signs, 4 signs with two. Automatic red-letter clustering plus
alignment (run during the pilot, not kept in the tool) gave 43.2% against 38.2% (max 41.9%) for shuffled text: no better than chance. So the gloss does look like the plaintext on the page, but neither my black-sign
classes nor my red-letter classes show it statistically.
Causes: (1) many shapes for few letters: the same letter has two or three drawings (the two ه of وجهه are different shapes; ج has a plain and a crossed form), and the arch (∩) is used
for alif, lam and ya alike, so the classes are look-alike groups plus variants (in line 4 the gold letters fall in black classes: ل in the same class as ع and و at k = 10), which
at 79 signs leaves single occurrences; (2) the reading of the plaintext against the cipher is not fixed (see the compiler's account above); (3) red letters are small and drawn
cursively, my red crops are weak features. What would work: transcribe the red letters by eye on the whole block (the first line shows it is feasible), take the red text as the plaintext
of the block and use it to learn the black key by DP, then compare with the page plaintext.

## C. f. 9r second block (image 22), segmenter lines 6-11

Plaintext at the foot of the page (22 l.13, after "فحللته" on l.12) as read on the master: `لا تكن ناكحا السوداء ما عشت فشر المناكح السودا` ("آ" after السود read as the alif and
hamza of السوداء). 37 letters (38 with the hamza); 9 words. The first block above (l.1, 7 numeral-like signs) and its plaintext (l.3-4, "بكيت على الشباب ...") are a different item and not used.
f. 9v l.1 ("اخبر فيها ونصف اسمها الاول سوء وآخر الاسم داء") is a comment on the riddle (sū' + dā' = sawdā'), not a continuation of the verse, and there is no more text of the verse after it.
The signs do not fit the length: 76 signs and 17 dividers (18 groups) against 38 letters and 9 words, i.e. exactly twice as many in both counts.
Tests: (a) two signs per letter (units of 2 consecutive signs, DP on units, and a rigid pairing with 1000 shuffles): no repetition of unit types for repeated letters,
letter-side fit 40.5% against 40.3% (C2), and the rigid consistency of repeated letters is at chance for every k from 8 to 24 (p about 0.5 or worse). The abjad-digits idea is also out: written as decimal
digits the plaintext would be 63 or 64 signs, not 76. (b) One sign per letter, plaintext against any 37-sign window of the 76: only window 0 (the first 37 signs) stands out: letter consistency 65%
against 51% for the best window of shuffled text (p < 0.003, 300 shuffles). With the first 37 signs the tool gives: 37 of 38 letters aligned, 0 surplus, fit 64.9% (control 45.7%, max 54.1%), class purity 78.4%
(control 55.4%), z-scores 4 to 9 over k; held-out 27.0% (control 4.1%, max 10.8%), per held-out line 6/13, 2/15, 4/10. A 40-sign window loses the effect (55% against 47%).
So the plaintext on the page seems to be the answer to the **first half** of the block; the second half (39 signs, 9 groups) has no plaintext on f. 9r or f. 9v that I found: it would
be the second hemistich or second verse, absent or on a page I did not check. The key is not rebuilt (about 18 classes from 37 signs, most seen once or twice). Verdict: partly (length mismatch explained
as half the text missing; no usable key). Cluster sheet: `output/ljs51/keys/f9r_block2_first37/key_sheet.png`; `keys/f9r_block2_first37.json`, `keys/f9r_block2_pairs.json`.
The chain length expected by the brief (80 signs) was not reproduced (76).

## D. The tashifi run, ff. 14v l.7 to 16v l.5 (images 33-37)

Plaintext: the two poems of 16v l.7-13 and 17r l.4-17v l.4 (images 37, 38, 39), re-read on the master TIFFs. Differences from the earlier agent's draft: 17v l.1 ends **قويم**
(the broken word at the line end is qaf-waw-ya-mim, not fa-waw-ya-mim; same sign class); l.7 of poem 2 read للملك (the draft had بالملك), l.6 of poem 1 ظله (draft ظلمه), l.6 of poem 2 قلايد (فلايد),
and قاصديه (قاصده) with a yod; "لدنيا" is as written (لدينا has the same letters). Doubtful: للملك, قاصديه (each changes the letter count by one) and the order ي/ن in لدنيا (same sign class). 770 letters in my text.
Signs: 778 (107, 191, 204, 199, 77), the one sign on 16v l.6 is missed by the segmenter (that line is classed as naskh).

Result (18 clusters chosen; the grid 12 to 32 gives rasm purity 82 to 95%, controls 24%):
aligned 754 of 770 letters (97.9%) and 754 of 778 signs (96.9%): 24 surplus signs, 16 dropped letters. **Rasm purity 93.6%** (706 of 754 aligned pairs; 91.7% of all 770 letters) against
24.3% (max 26.8%, sd 0.7) for shuffled text, z about 100 on the control spread; the earlier agent reported 94% (722 of 770, 34 mismatches, 28 surplus, 14 letters unaligned), so the tool reproduces the figure
from scratch to within about 2 points of all letters (706 against 722 identical-class letters); my 48 class mismatches and 24 surplus signs against its 34 and 28.
Held-out (leave one line out, 53 lines): top-1 rasm group 93.6% (control 3.4%, max 5.1%); letter-set consistency 94.3%; strict modal class 75.1%.
Class by class against the earlier 15-class key (share of the group's aligned letters falling in my clusters whose modal group is that group):

| earlier class | letters | letters aligned | my clusters | share in own clusters |
|---|---|---|---|---|
| S1 | ا | 117 | c17 (76), c16 (41) | 97.4% |
| S2 | ب ت ث ن ي | 166 | c0 (75), c2 (99) | 95.8% |
| S3 | ج ح خ | 28 | c8 (25) | 85.7% |
| S4 | د ذ | 24 | c7 (22) | 87.5% |
| S5 | ر ز | 43 | c9 (51) | 97.7% |
| S6 | س ش | 20 | c14 (16) | 80.0% |
| S7 | ص ض | 12 | c4 (12) | 91.7% |
| S8 | ط ظ | 12 | c15 (12) | 100% |
| S9 | ع غ | 34 | c3 (33) | 94.1% |
| S10 | ف ق | 48 | c13 (58) | 100% |
| S11 | ك | 20 | c6 (19) | 95.0% |
| S12 | ل | 93 | c11 (59), c10 (30) | 94.6% |
| S13 | م | 60 | c1 (48) | 76.7% |
| S14 | ه | 29 | c12 (33) | 100% |
| S15 | و | 47 | c5 (45) | 95.7% |

All 15 groups are recovered as separate clusters, and 3 groups come as two clusters (alif 2, ba-class 2, lam 2); none merge two groups. The class-purity figure of
each cluster (modal group / members): c14 16/16, c11 59/59, c6 19/19, c0 73/75, c17 73/76, c1 46/48, c12 29/33, c2 86/99, c13 48/58, c9 42/51, c10 29/30, c5 45/45, c8 24/25, c4 11/12, c16 41/41, c7 21/22, c3 32/33, c15 12/12.
Weak points: mim (S13: 13 of 60 mim fall into the ba-class cluster c2, the two signs differ by a small curl) and the ra cluster (c9 takes 9 non-ra signs), fa/qaf (c13 takes 10 others).
Verdict: key rebuilt, same 15 classes and the same figure as the earlier agent. Still a self-consistent key (the shuffle control and the held-out lines are the evidence that it is not an artefact);
no hand check of the sign-by-sign alignment. Cluster sheet: `output/ljs51/keys/f14v_tashifi/key_sheet.png`.

## What the tool needs before it can run over all 209 chains

1. **Plaintext per chain, read from the master.** This is the bottleneck, not the clustering. The pilot shows three kinds of mismatch that the tool cannot repair: plaintext that covers only part of
   the block (C: half), plaintext that is a recombined or other text than the one on the page (B), and numbering slips in the page pass (B image 119 vs 120, C lines 6-11 vs 7-12, 76 vs 80 signs).
   Each chain needs `chains.json` with image, lines, plaintext, and a flag for "plaintext covers signs a to b" (the window option exists: `window=(a, b)`).
2. **A chain-level length test first** (signs against letters, dividers against word breaks, and the window scan used on C) so that chains that cannot align are flagged before clustering.
3. **A better segmenter output for non-standard blocks**: lines classed as naskh that are cipher (B on image 120, a single cipher sign on 16v l.6), dots and flags
   split off their signs, specks among the red letters (filter at 16 px is crude), mixed lines. D has 778 signs for 770 letters.
4. **Pooling by key.** A 79-sign chain cannot yield a 28-letter key (A: most classes have one to four members, held-out 60%). Chains that share an alphabet should be clustered and aligned jointly
   (classes shared across chains, key table per alphabet family); this also fixes k, which is now chosen with the plaintext. The EM already takes any sign list, so pooling needs only a chain list per family.
5. **A red-letter reader.** Red glosses are the independent key, but my crops of 15-55 px strokes cluster at chance level; read them by eye on a sample, or train a small classifier on red letters
   whose value is known from the first chains (D has none). The same holds for the tree figure: it needs its own segmenter (stems, branch pairs, forks) and a decision on reading order.
6. **Variants and many-to-one shapes** (B): allow several classes per letter explicitly (homophone model) and shared classes (look-alike groups), and report letter-side fit and rasm purity separately, as done here.
7. **Multi-sign units and numerals** (C): the pair test showed no two-sign structure, but numeral blocks in the manuscript need a unit model with a free unit length; a unit of 1 to 3 signs with DP over unit length is the natural extension.
8. **Speed is fine**: D (778 signs, 18 clusters, 100 shuffles, 30 held-out shuffles, 6-point k grid) takes about 45 s; the 209 chains will run in minutes once plaintexts exist.
9. **Hamza and lam-alif**: hamza is a letter that can be dropped (D drops 16 letters, mostly hamza, alif of the article and run-together words); lam-alif folding is implemented but did not trigger in any chain; the
   gap costs are fixed constants, not fitted per page.
