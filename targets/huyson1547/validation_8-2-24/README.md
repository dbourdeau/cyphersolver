# Held-out re-test of the frozen key on HHStA Türkei I 8-2-24 (25 Mar 1550)

Brice Dudout (with Claude), 25 Nov 2026. One measurement. Notes in French are the working files, byte for byte (their hashes are cited).

- Item: HHStA StAbt Türkei I 8-2-24 (AIS 7048241), Ferdinand I to Malvezzi, Vienna, 25 Mar 1550, Latin; fol. 123r, the
  9 cipher lines after the line beginning "Z ‡ k" (354 cipher signs). The lines above carry a modern pencil gloss and were left out.
  Native AIS image studied only; no image is committed.
- Reference: the clear draft 8-2-10 fol. 74 (AIS 7048141), identified and transcribed by **Andrew Beling (ajbeling) in
  PR #945** (his file SHA-256 c30df146...c84d04, PR head 443540f9). It is cited, not copied here.
- Frozen before transcription: `cle_K1547_consolidee.json` (SHA-256 8fbf1dd2...d4bcceb; K-C01 `../key_KC01.json` plus the
  sign atlas and the later values of the published reading) and the plan PREREG.md (SHA-256 fcd2c149...; kept in our
  working folder because it names local image paths).
- Frozen before decoding: `transcription_8-2-24.txt` with its table linking the 1550 shapes to key codes (b4110051...).
  Then the mechanical decode `decodage_8-2-24.txt` (8d61ebc1...), and only then the reference.
- System check without decoding (`syscheck_sortie.txt`): every 1550 shape maps to a key code; same nulls, code word Ras and
  doubled-letter numbers as 1547; value-class frequency cosine 1550 vs 1547 = 0.909 (shuffled control max 0.827).
- Score (`scripts/decode_score.py`, `mesure_unique.txt`): character agreement **0.887** (pass mark 0.85); best of 200
  shuffled keys 0.421 (mean 0.332), so the margin needed was 0.721; word agreement 51/70 = 0.729 (reported, not decisive). PASS.

Limits: the transcription was made by one AI agent (Claude) and has not been reviewed by a human. The test covers the key
and the system, not the 1547 hand. The links from the 1550 shapes to key codes are ours, frozen before decoding.
