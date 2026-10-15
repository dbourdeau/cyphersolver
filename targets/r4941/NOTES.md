# Keresdi Bethlen collection, letter of 1648 in a different substitution, DECODE R4941 (Keresdi_Bethlen_15-05)

Status: in progress

Split on 14 Oct 2026 from `targets/transylvania1645/` under the one-key rule (George Lasry, 14 Oct 2026). R4941 is
in the same Keresdi_Bethlen_15 series as R4937-R4942, but its cipher is a different substitution: the alphabet family
that reads R4936 and R4940 (`targets/transylvania1645/`, a different cipher, with its own entry) does not fit it. The
Kemény_XIX_1628 records are `targets/kemeny1628/`.

## Record

R4941, Romanian National Archives, Cluj, Keresdi_Bethlen_15-05, DECODE year 1648, four images, symbol set "alphabet",
status N/A. Images (23 Sept 2026; manifest `targets/transylvania1645/image-manifest.json`) are git-ignored in the main
checkout under `C:\Users\dbour\cypher\transylvania1645\` (`IMG_R4941_*`). Metadata `R4941-metadata.txt`.

## Work so far (23 Sept 2026, in the transylvania1645 session)

- `R4941-extract.txt`: a provisional extract of the cipher on pages 1-2. Pages 3-4 not inspected.
- hu-modern quadgram and quintgram annealing (`targets/transylvania1645/attack.py R4941-extract 5`; results
  `R4941-extract-result.json`, `R4941-extract-5gram-result.json`, moved here): no coherent Hungarian. The R4936
  family mapping does not fit. Long-s/f and g/q are suspected transcription confusions. `attack.py` reads its input
  from its own folder, so to rerun it copy the extract back or pass a path; its `sys.path` points at `targets/`, not
  the repository root, and needs fixing for `lang`.

## Next work

1. Inspect all four images; re-transcribe pages 1-2 against full-resolution crops and add pages 3-4.
2. Attack the corrected transcription on its own (homophones and nulls allowed), with a planted control.
3. Record every step in `profile.json` (`python docs/_check_profile.py r4941`).

No write-up while in progress.
