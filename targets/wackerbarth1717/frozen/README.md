# wackerbarth1717/frozen - working files as frozen (French)

This is a copy of the working folder, kept byte for byte so that the `.sha256` files can be checked. Run `shasum -a 256 -c
<file>.sha256` from this folder; for `releves/*.sha256` and `AVENANT2-VERITE.sha256`, run it from `releves/`.

There are three exceptions:
- `PROTOCOLE.md` line 4: one storage location was removed for publication. It therefore no longer matches
  `PROTOCOLE.sha256` (bcd3da00...). No other change was made.
- Left out: the session log (HANDOFF.md); a transcription brief for sub-agents that names local folders; `scripts/strips.py`
  (it crops the private scans).
- No image, crop or derivative of the Dresden scans is included anywhere. The scans are "In Copyright" (InC) on
  archiv.sachsen.de. Headers that say "PRIVÉE" or "privé" refer to that rule, and to the working files before this
  publication.

## Order of work (all 11 Nov 2026)

1. `PROTOCOLE.md` + `PROTOCOLE-AVENANT-1.md`. Key `KEY-W1717.tsv` (TRAIN = glossed views). Single run `scripts/mesure.py`
   -> `MESURE.json` / `MESURE.txt`: tests A and B both FAILED. Diagnosed afterwards in `DIAGNOSTIC-POSTHOC.txt` and
   `ESSAI-OPUS.md`.
2. `PROTOCOLE-AVENANT-2.md`: keys `KEY-W1717b.tsv` / `KEY-W1717c.tsv` (`scripts/build_key_bc.py`). Calibration in
   `ETALONNAGE.json`, then `PROTOCOLE-AVENANT-2BIS.md` and `ETALONNAGE-BIS.json`. Single run `scripts/mesure2.py` ->
   `MESURE2.json`: A' FAILED, B' PASSED.
3. `AVENANT-3.md`, a post hoc decision: B' alone is the condition for reading Relation XXII, with 95% as the final check.
   New transcriptions were frozen before decoding: `releves/R22-0094...0099` (`R22b.sha256`), `R22-0090-fin`, `A24-*`,
   `S2-*`. Reading with `scripts/decode_lecture.py` and `scripts/compte_lecture.py` -> `lecture/`, `LECTURE-REL22.md`,
   `LECTURE-A24-0063.md`, `LECTURE-S2-K0.md`, `RESUME-HISTORIQUE.md`. The proposal `KEY-W1717d.tsv` is not used for counts.
   All are hashed in `LECTURE-AV3.sha256`.

The scripts `lm.py` / `mesure2.py` expect a French lexicon and two French corpus extracts (16th-18th c.), which are not
included. The measured numbers are in `MESURE2.json`.
