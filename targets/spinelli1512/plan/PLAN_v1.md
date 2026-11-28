# Plan for catalogue 2855 and 2865, written before any key work

Written 28 Nov 2026, about 04:40 UTC (27 Nov 23:40 EST), by the lead AI agent (Claude Opus 5.5). Local only.

State at writing: images fetched (sources/raw/aragon_2026-11-28/, SHA256SUMS); two blind helper transcriptions
requested per letter (helper_2855 and helper_2865 done; helper2_2855 and helper2_2865 running, the same two helper
agents swapped over, each on a letter it had not seen). The lead has looked at the pages and at some glosses while
cutting crops. Before this plan, while reading glosses, the lead tried a few sign values by eye on 2865 (A1.01,
A2.04-05, B1.01-02); none held together. No solver has been run and no key exists.

Finding already made on the image (not key work): both items carry interlinear glosses in a second hand. 2855: partial
glosses over some cipher groups (names and phrases). 2865: glosses over or under many cipher lines of both letters,
some struck and rewritten. The catalogue's "No decipherment on the sheet" is wrong for both.

## Common rules

- Transcription used for all key work: consensus of the two blind helper readings, made by `scripts/reconcile.py`
  (alignment per line; agreed signs taken; disagreements kept as the first reader's sign with a flag, and the lead
  rules on the image for flagged signs before key work, recording each ruling).
- Gloss transcription: made by the lead from the images, line by line, with the cipher line each gloss covers, before
  key work. Struck gloss words kept and marked.
- Counting: words under a legible period gloss are "read from existing decipherment". Words read only through a
  rebuilt key count as read only where every letter is decoded; a supplied letter makes the word a hole. Words
  decoded but doubtful are probable, not read.
- Held-out tests follow Daniel Bourdeau's proposed rule #1014. The freeze is published by an RFC 3161 timestamp
  from **FreeTSA (https://freetsa.org/tsr)**, approved by Andrew for these two items: `openssl ts -query -data
  MANIFEST_v1.sha256 -sha256 -cert`, sent by curl, `.tsq` and `.tsr` kept, verified with FreeTSA's CA and TSA
  certificates before measuring. The protocol names the `.tsr` before the freeze. Measured once.
- Metric: #1014's "char" metric (difflib ratio of decoded letters against the gloss letters, over the longer string,
  normalised: lowercase a-z, j->i, v->u, k->c, y->i, h kept), summed over held-out runs as matched letters over total.
  Controls: 200 keys made by shuffling the frozen key's values over its signs, seed 20261128. Pass: score >= 0.60,
  score above every control, and margin over the best control >= 0.15.

## 2865 (Spinelli to Urrea, 16 Apr 1512, letters A = 0055 and B = 0056)

1. Shared text: compare the two letters' cipher (and clear text) for common runs of 6+ signs; report.
2. Key building uses **letter A only** (its cipher and its glosses), with ciphertext-only modelling of letter A
   (Italian; corpus = Morosini 1588 plain text and the repository's Italian model). Letter B's cipher and glosses are
   not used to build or adjust the key.
3. Held-out passage: **all glossed cipher runs of letter B**, aligned to their glosses as transcribed before key work.
   Reference = the gloss letters. If the glossed runs of B hold under 150 cipher signs, all of letter B is still the
   passage (no smaller choice).
4. Simple-substitution solve: if letter A's glossed material is too thin, a homophonic hill-climb on letter A's cipher
   with the Italian model, seeded by gloss alignments; the key is what it ends with, frozen before B is decoded.
5. After the test: read the unglossed cipher of both letters with the frozen key; count strictly.

## 2855 (Cardona to John II, Trapani, 16 Jul 1478)

1. Glosses: record each gloss, its place and the cipher run it covers.
2. Upstream keys unchanged: compare the sign shapes with the keys of ferdinand1473 (1473 and 1474), ferdinand1478
   (WAINUT, PR #1021, numeric), toledo1479, garcilaso1498, juanmanuel1497 (Lasry no. 95) and claver1497. A key is
   tried only if at least half of 2855's frequent signs (top 15) have a shape match in it; then the glossed runs are
   decoded unchanged and scored against the glosses with the metric above (no controls needed for a plain miss).
3. Key from glosses and the clear Catalan context: build on glossed runs in helper lines L01-L09; held-out = glossed
   runs in L10-L17. If the held-out glossed material is under 40 gloss letters, the test is underpowered: no test is
   run and the key is reported as proposed, not tested.

## What would stop the work

A claim found on #542, the _claims reader or an open pull request; a printed decipherment of either item.
