# PREREG v2 — Morier 1808 (catalogue 2649) — frozen 16/11/2026 BEFORE the new portion is transcribed

Context: v1 measure on /21 0001 failed (S = 0.7286 < 0.85; best control 0.157); /21 0001 is burned.
The 20 missing images arrived (dl/, 40/40, SHA256SUMS.txt checked: all OK).

Key: UNCHANGED, work/key.json SHA-256 270fb39390488181f430d47463c2d9091a9fca3f029a7428aa6a77fefda58466
(fixed on T = /18 + /20 pages already transcribed). It is NOT completed with /20 0006-0007, because those pages are
the second copy of the very text of /18 0012-0014 (gap analysis of 16/11) and so belong to the held-out text.

Held-out H2: every cipher word on IOR/L/PS/9/67/18 images 0012, 0013, 0014; /19 images 0001, 0002, 0004;
/21 images 0002, 0004. Images among these with no cipher numerals are dropped (decided on sight of numerals,
before any decoding). Clear-text lines, docket, signatures in other cipher and 3-4-digit groups are excluded.
/20 0006-0007 are used ONLY as an independent second copy for collating the transcription of /18 0012-0014
(numbers only, not decoded). The transcription is hashed before decoding.

Metric (scripts/v2.py, SHA-256 in v2_scripts.sha256), applied to the decoded words of H2:
- V = Lord Lyons corpus vocabulary ∪ /usr/share/dict/web2 ∪ web2 forms +s/+es/+ed/+d/+ing (and e→ing);
  u↔v and i↔j variants allowed; one-letter words only a, i.
- labels: word (in V); name (in the fixed NAMES list of v2.py: places, persons, titles, abbreviations of the
  period); split (two adjacent pieces whose join is in V or NAMES: a copyist's cut); join (a fused word that splits
  into two read pieces); fail. Reported separately.
- BINDING score S2 = (word + name + split + join) / counted words.
- Controls: 200 within-class shuffles (random permutation of the letter values over the key's numbers), seed 1808,
  same metric. Sanity on T (not held out, 20 controls): S = 0.943, max control 0.232.
- PASS iff S2 >= 0.85 AND S2 >= max(control) + 0.30. ONE measurement; H2 burned afterwards.
- Also reported (non-binding): strict share 'word' only.
