**Freeze: LJS 51 blind key confirmation (ciphertext only) and Ibn ʿAdlān's length rule**

- Manifest SHA-256: `f2e53f5726ff25bcaef7f6a4c84dc8a43fc0387073a19d20ecba66cc2662eb6d` (`MANIFEST.sha256`, 34 files)
- Frozen: 2026-11-28T14:35:43Z (UTC)
- Base: `origin/main` d8ac608093
- Files: PREREG, the solver (C annealer + Python wrapper), our own letter 4-gram model (4 OpenITI texts, not `lang/`), the 18 sign-only transcriptions taken from `keys_eye/*.json` `cipher_lines`, the selection table, the measurement script.
- Chains (18): lot L 20r.8+47r.1, 22r.1, 19r.7, 105v.6, 18r.11, 23r.9, 61r.3, 30r.4, 42r.2, 39v.12; lot E (seed 5151, two per 30-45/46-60/61-75/76-90 signs) 56v.8, 6v.11, 41r.3, 31r.11, 35v.8, 69v.11, 46r.11, 82r.9.
- Reference: the compiler's plaintext (`chains_all.json`), never read by the solver.
- Criterion per chain: character agreement (difflib, over the longer string) ≥ 0.85 AND ≥ best control + 0.30; word agreement reported, not decisive.
- Controls: 200 per chain, shuffled ciphertext (divider positions kept), re-solved by the same solver.
- Seeds: 2811 (cipher), 2811+i (control i); 20 restarts, 500 000 iterations, λ = 8.
- One measurement, run only after this comment is posted.
