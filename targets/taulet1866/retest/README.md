# retest/ - one re-test of the frozen key on new material, N.94 (10 Nov 2026)

Files of the single re-test, check with `shasum -a 256 -c SHA256SUMS` from this folder. They are in French and were
not edited after hashing, except PREREG.md (see below).

- PREREG.md - pre-registration, written at 13:18 CET before any number of N.94 was transcribed or decoded: frozen key
  and script unchanged, held-out portion H = all runs of views 43, 87, 78 of N.94, plus view 26 if under 300 numbers,
  criterion unchanged, one measurement. **Redacted copy**: two lines name our private image store and an internal
  instruction file; they are replaced by bracketed words. SHA-256 of the original, recorded in our log at 13:18 CET:
  009129999aadde161a9cbd9a25c794c55d2214973ea8185f090c4e17d3f6f0df; SHA-256 of this copy in SHA256SUMS. Nothing else
  changed (the hashes of the four PARES views it lists are hashes only; no image is included).
- transcription.txt - the 17 runs of H (325 numbers), one mechanical pass before any decoding; the bracketed comment
  lines give the clear words between runs.
- decode.txt - decoding of H by the frozen key (`../frozen/KEY.tsv`), "?" = number not in the key.
- clair.txt - the reading by sense (French notes; see `../reading_n94.md` for the English write-up and two counting
  slips of this file).
- MESURE.txt - output of the one measurement, made with `../frozen/measure.py` on `transcription.txt`, `../frozen/KEY.tsv`
  and `lang/lexicons/es.json.gz`, `--part H`: car 0.960, best of 200 controls 0.699, margin 0.261, "NON VALIDEE".

H is burnt: it will not be measured again.
