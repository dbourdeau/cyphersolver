# Vetting, 17 Nov 2026 (project): the two Vat. lat. 8214 leads closed into targets/mantua1524

Leads 2956 (BAV, Vat. lat. 8214, f. 68r) and 2957 (f. 198r) came in with the sweep `research/sweep_2026-11-16_vat_lat_8214/`
(PR #715, Andrew Aymeloglu). Both leaves are read with the key of `targets/mantua1524` (PR #716, merged the same day): f. 68r
is decoded, not read (95 of 172 cipher words strict), f. 198r is read in part (11 of 14). One key, one entry: the verdict is
`partly_read`, the leads are closed into that target and are not promoted to the catalogue. `vetting.json` was checked with
`python research/vet.py --check` and written to `research/leads.json` with `--apply`.
