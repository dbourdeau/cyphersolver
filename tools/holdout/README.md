# Held-out tests: freeze, publish, then measure

A held-out test checks that a key predicts text it was not built from: the key, the transcription and the choice of
passage are fixed first, the key is scored once on the passage, and the score is compared with keys whose values are
shuffled among the same codes. The test means something only if the files were fixed **before** the measurement.
Hashes show that files did not change after a manifest was written; they do not show when it was written. Until now
that order rested on the contributor's record. These tools make it checkable from the repository.

The scheme and much of the code come from Brice Dudout's method kit (26 Nov 2026; code MIT, texts CC BY 4.0). The
changes here: the measurement refuses to run until the frozen state has left the machine; the result records the
manifest's hash and commit and the hash of the scripts; a per-group metric; hashes that ignore CRLF; a checker.

## The steps

All files of one test live in `targets/<target>/verification/`, with a version number: `PROTOCOL_v1.json`,
`MANIFEST_v1.sha256`, `RESULT_v1.json`. A second test is `v2`, never an edit of `v1`.

1. **Write the protocol** (`PROTOCOL_v1.json`; fields in the header of `measure.py`): the key, the held-out passage,
   the reference or lexicon, the metric, threshold, margin, controls, seed and result file name. Choose the passage
   before the key is built, at least 300 cipher characters or 150 groups where the document allows it.
2. **Freeze**:
   `python tools/holdout/freeze.py freeze targets/<t>/verification/MANIFEST_v1.sha256 PROTOCOL_v1.json key_v1.tsv holdout_v1.txt reference_v1.txt`
   (run from `targets/<t>/verification/`, or give paths; files may sit elsewhere in the repository).
3. **Publish the freeze**, one of:
   - commit the manifest and every file it names, and push the commit to GitHub (a branch of your fork is enough at
     measurement time, but the commit has to reach `main`'s history, so do not let the pull request be squashed: send
     the freeze as its own pull request, or merge it with a merge commit);
   - stamp the manifest with an RFC 3161 service, as Malcolm McBratney's `timestamps/` folders do
     (`openssl ts -query -data MANIFEST_v1.sha256 -sha256 -cert -out MANIFEST_v1.sha256.tsq`, send it to a public
     TSA, keep the `.tsr`), name the reply in the protocol as `"timestamp": {"rfc3161": "MANIFEST_v1.sha256.tsr"}`
     **before freezing**, and commit both;
   - post the manifest's SHA-256 (printed by `freeze`) in an issue comment, and give the comment's URL to the
     measurement: `measure.py PROTOCOL_v1.json --issue-comment=URL` (checked later with `check.py --online`).
4. **Measure once**: `git fetch`, then `python tools/holdout/measure.py targets/<t>/verification/PROTOCOL_v1.json`.
   It refuses if the result exists, if a frozen file changed, if a file is missing from the manifest, if the frozen
   files are not committed, or if none of the three proofs of step 3 holds.
5. **Commit and push the result** at once, then record it in the target's `profile.json` as a solution step (score,
   best control, z, verdict, manifest hash) and in `NOTES.md`.

`python tools/holdout/check.py [target ...]` checks every result: not a dry run, frozen files unchanged, the manifest
commit holds the manifest, and the order shown by git ancestry, by the RFC 3161 time, or (with `--online`) by the issue
comment. It prints `result: valid`. `python tools/holdout/test_holdout.py` runs the tests in a throwaway repository.

## Choosing the metric

- **group** (preferred when a reference exists): share of held-out groups whose key value equals the aligned
  reference value. The reference has one token per held-out token (`-` null, `?` unknown, `|` at the same breaks).
- **char**: letters matched by `difflib` against an independent plaintext, over the longer string. Shuffled
  nomenclator values keep real words and syllables, so controls score high (about 0.70 on Brice Dudout's real
  nomenclators), which makes a 0.30 margin hard to reach.
- **lex**: share of decoded letters covered by words of an independent, frozen word list; for ciphertext-only
  targets with no reference. Even a perfect key stays below 1.

On a 56-group synthetic nomenclator (`test_holdout.py`) the best of 200 shuffled controls ranged 0.13-0.34 on the
group metric and 0.39-0.47 on the char metric over eight seeds; the group metric's best control is driven by frequent
words landing on their own codes and falls as the passage grows.

## What a pass shows

That the code-to-value assignment is far from random on that passage, if the key was built without seeing it. Not that
every value is right: the threshold tolerates roughly 15% wrong groups or letters. Not that the transcription is right:
the test scores the key on the transcription as frozen. The threshold and margin are conventions. The result also gives
the rank among the controls (with 200 controls the smallest p is 0.005) and z, the distance from the control mean in
control standard deviations.

## Older tests

Held-out tests made before this convention (Morier 1808, Taulet 1866, Ridolfi 1646 and others) are not re-scored. Their
order of events rests on the contributor's record and on any `timestamps/` stamps, and their pages say so.
