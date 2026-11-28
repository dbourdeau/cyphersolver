# Amendment to PLAN_v1 (2855 only), written 28 Nov 2026 before any solver run on 2855

What happened: while comparing helper_2855's transcription with the upstream 1473/1474 shape tables (step 2 of
PLAN_v1), the lead noticed that the sign run "ae t v m c g h t 3 p gbar xo g p s xo" occurs three times in lines
L12, L14 and L17 and fits the gloss "senyor de Camarasa" written in those lines (ae = s, t = e, v = n, m = y, c = o,
g = r, h = d, 3 = c, p = a, gbar = m, xo = a, s = s). PLAN_v1 set L10-L17 as 2855's held-out lines, so they can no
longer be held out.

Change: roles swapped. **The 2855 key is built from lines L10-L17 only** (helper_2855 numbering; their cipher,
glosses and clear context), and **the held-out passage is all of lines L01-L09**, scored as one block against all
glosses written in that part of the page (transcribed now, before key work continues), with PLAN_v1's metric,
controls, seed and pass rule. The run also appears at the end of L07; that is allowed (the key predicts it).
If the L01-L09 glosses hold under 40 letters, the test is underpowered and is not run.

Step 2 result recorded now (no decoding needed): the shape gate is not met by any upstream key. Of 2855's 15 most
frequent signs (helper_2855 names g, t, p, s, ae, xo, h, v, c, 3, ls, m_, b6, 7bar, dot2), the 1473 shape table of
ferdinand1473 has counterparts for at most p (its P), 3, g (its 9) and t (its T): 4 of 15; the 1474 table fewer;
ferdinand1478 (PR #1021) is a numeric syllabary; juanmanuel1497 / claver1497 / garcilaso1498 / toledo1479 are other
sign families. So no upstream key is tried, as PLAN_v1 allows.
