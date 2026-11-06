# WORKLOG: mazzinghi1478 (catalogue 2307)

- 2026-11-06 access: fetched IIIF recto/verso of MAP 89/142 (A0000463/4) and the sibling 72/170 recto (A0000397); full size 1272 px, no larger tier.
- 2026-11-06 transcription: first pass of 89/142 from 2x half-line crops, 29 sign classes (transcription_89_142_v1.txt). Partial.
- 2026-11-06 sibling key: tried pairing 72/170 gloss with cipher; only "publichamente mostra lectere" aligned with confidence (p,u,b,l,i,c,a,m,e,n,t; m,o,s,t,r,a). Partial.
- 2026-11-06 solver: homophonic annealer on it-cinquecento o5 with spaces collapsed onto all-i. Failed.
- 2026-11-06 solver: added frequency-rank start, swap moves and a KL penalty on letter frequencies; sense came out at once (contra di voi molto crudele, la vita, molte volte, grandissimo). Worked.
- 2026-11-06 control: 537-sign Italian passage in a random 29-sign homophonic key, same solver: 655/667 letters right. Worked (control is half the real length).
- 2026-11-06 hypothesis: o = q in "questa" vs o = d in "di": the class o merges two or three signs; likewise 4 (s/l), H (t/h), b/6 (r/v/l). Values taken from context. Partial.
- 2026-11-06 transcription: second pass in 3x two-line crops; split q (flat top, u/v) from rho (t), z4/z‡ from 4; read word by word (reading_89_142.txt).
- 2026-11-06 reading: 111 of 189 cipher words read, 30 doubtful, 48 open (measure_ctonly.py). Read in part. Content: Rome after the Pazzi conspiracy, so Jan 1479 modern.
