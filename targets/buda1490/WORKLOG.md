# Worklog, buda1490 (DL 46150, catalogue 1235)

One line per step, failures included. The reading rounds of 29 Oct were stamped "10-30" in part of the working log
(worklog_reading.md); that was a clock slip, all of them ran on 29 Oct 2026.

- 2026-10-28 (sonnet) Read buda1489 NOTES, key_R5411.md, the 1235 verification record; planned to test R5411. Worked.
- 2026-10-28 (sonnet) Hungaricana viewer for charter 228061: tiles blocked by CORS in the built-in browser, tile URLs encrypted; only 829 px thumbnails. FAILED; stub "not attempted / blocked".
- 2026-10-29 Direct requests to the Hungaricana tile CDN return 403. FAILED (nothing bypassed).
- 2026-10-29 The user (harrison-bornstein) fetched the three images (orig_1 p. 1, orig_2 pp. 2-3, orig_3 p. 4) in their own browser and supplied them. Worked.
- 2026-10-29 WSL restart lost the first session's work kept under /tmp (crops, first transcription, solver runs); redone in a persistent folder (/home/.../cyphersolver-1235). FAILED, then redone.
- 2026-10-29 Control: synthetic Latin homophonic text of the same length and alphabet size (control.py, ctl_ct.txt) for the annealer; outcome not recorded in the working files.
- 2026-10-29 Transcription pass 1 of the four pages by agents from 2x line crops (p1-p4_pass1.txt), sign sheet inv/SHEET.png (signs.md). Worked; 3,199 tokens.
- 2026-10-29 Annealer (hsolve.py, la 4-gram, letter-frequency penalty), several restarts (key0-key4). Partial: Latin fragments.
- 2026-10-29 Crib "reuerendissimam dominationem uestram" (P1L04-05, P1L24-25): D = m, confirmed by dictum, secum, mecum. Worked (key5).
- 2026-10-29 Image check of P1L04, L02, L28 against the transcription; "reuerend F M 2 D F x" unresolved with one key. FAILED.
- 2026-10-29 Re-anneal with 17 crib-fixed signs (key6): not better in reading; kept key5 values for tp, T, p, s, f, 6, aN. FAILED.
- 2026-10-29 q reads u, s and o; g t and o; h l and f: the labels merge shapes. Pilot q split on three lines (qsplit.md). Partial.
- 2026-10-29 Word division of all lines, build.py: strict words read 23.4%, doubtful 13.2%, open 63.3%. Partial (round 1 baseline).
- 2026-10-29 Shape-only q split on every page by agents (q -> qA / qB / 4; p*q.txt, logs): qA = s, qB = u. Worked.
- 2026-10-29 Digraphs oH = q, Ho = p; s = h, T = b, p = x, 8 = h, & = et (key_final, dec9.py); new annotation: strict 50.9%. Partial.
- 2026-10-29 Split round 2 by agents (g, oo, h, 8, 6, 3, P; p*r.txt): gA/gB on p.3-4, ooA/ooB, hA/hB, 8A/8B/8C, 6A/6B. Worked; 3 and P one shape.
- 2026-10-29 key10/key11 restoring evidence-based values the annealer lost; ooA = u, ooB = s, hB = f: strict 55.7%. Partial.
- 2026-10-29 "6 gA" = ll (excellentia, tabellarium) but st in istud: left 6 = s. Partial.
- 2026-10-29 Round 4 (dec12): G a null pair, O after a u-sign = m, nulls dt, A, y, ff, dx: strict 70.4%. Partial (several of these "nulls" proved to be code signs).
- 2026-10-29 Round 4, not adopted: qB = f (no shape split), ooA = s, 3 = g. Ruled out at the time.
- 2026-10-29 Image repairs round 5 by agents (fix only what the image shows; transcription_fixes_p*.md): 3G, jB, Tx, Ob new labels; dec13 (u/s polyphony, G p null pair, "v e D" code group): strict 75.6%. Partial.
- 2026-10-29 Round 6 repairs and dec14 (X = ss, n context rule, s = h/f, qB = u/s/f, aN and K null): strict 79.2% of 539 words, tokens 78.4% (key14). Partial; 96% not reached.
- 2026-10-29 Search for the minute in Vestigia (scripts/vsearch.py over the vestigia.hu API, dates Oct 1490 - Feb 1491; candidates 190, 191, 193, 194, 559, 2005 opened): document 194 = ASMi Sforzesco 642, novembre no. 8, minute of the same letter. Worked.
- 2026-10-29 Transcribed the minute from the Vestigia images (clear.txt: insertions, deletions, marginal addition marked). Worked.
- 2026-10-29 First comparison of the minute with the key14 reading (differences.md): insertions enciphered, deletions not. Worked.
- 2026-10-29 EM alignment of the four pages with the minute (ext/em_align.py, 6 iterations) and key rebuilt from it (ext/report.py -> key_external). Worked: tokens 95.2%, minute words 81.7%.
- 2026-10-29 key14 against the external key: 60 of 81 signs right (96.2% of tokens); code signs ff, Tx, Ga, Gp, dt, dx, K had been taken as nulls; ooB majority wrong. Blind reading 396/424 = 93.4% exact. Worked.
- 2026-10-29 41 isolated one-sign disagreements listed as transcription suspects; not yet checked on the image. Open.
- 2026-10-29 Packaging: compared with ../buda1489/key_R5411.md: R5411 has a = r, 1, f, here a = to, F, L: a different alphabet, ruled out; R5407 (A = ⊥) flagged for a check.
- 2026-10-29 Packaged into targets/buda1490: sense measure (measure.py) 534/624 = 85.6% read, 87.3% of undamaged; read in part. Two suspects found to be alignment artefacts (habere uelit tantum).
- 2026-10-29 Image check of the 39 transcription suspects (shape only): 11 fixed (p1-p3.txt, p1r-p3r.txt, alignment.json; crops in transcription/checks/), 19 confirmed as written (writer departures), 9 ambiguous and left; verdicts in transcription/suspects.md. measure.py: 544/624 = 87.2% read (88.9% of undamaged), up from 534. Partial.
- 2026-10-30 Review of PR #199. Retry pass (scripts/retry.py -> reading/retry.md): the 80 unread words re-run under an extended key (minority values in >= 2 other places, look-alike labels, y as code). 17 regained and adopted in measure.py: qA = i (4 words) / t (3), all image-confirmed qA; y = 200,000 (4 words); cotraxerat, prefatu (nasal left out); debeat, necessarie, and P2L22 "neque [u]ieat a quibus" (3 words). 544 -> 561 of 624 (89.9%). Partial.
- 2026-10-30 Key R5407: de-crypt.org refused by the session's network policy (proxy 403); no DECODE cookie here. Only the known value A = ⊥ compared: L = a (38/38) here, h in R5411; chance agreement about 1 in 20. Partial (record not opened).
- 2026-10-30 Statistical validation: lang model la-letters added (Latin Library letters via raw.githubusercontent.com; Gutenberg refused); validation.tsv from scripts/make_validation.py; docs/_validate.py: reading -2.140, random keys -5.566 (z 9.8), shuffled refit best -3.214 (z 41.0), annealer on real text -2.185: pass. Negative control (--control --quick): underdetermined, not pass. Worked.
- 2026-10-30 Circularity note in NOTES ("The minute as evidence"): what rests on the minute (key values, code signs, suspects, damage fills) and what does not (key14 blind reading 93.4%, LM validation, Latin where the minute differs). Worked.
- 2026-10-30 Regrade of the read words (scripts/regrade.py -> reading/regrade.md), the doubtful-reading half of the retry step: every read word decoded again with all values a key allows. 561 read: B 466 (key.json and blind key14 both give it), K 16, X 7 (qA = i/t), C 72 (code signs), D 0. The crossed stretches P3L04-05 (habere uelit tantum) and P2L22 (neque ... a quibus) spell out under key values. No reading withdrawn; 466 of 624 words (74.7%) do not rest on the minute. Worked.
