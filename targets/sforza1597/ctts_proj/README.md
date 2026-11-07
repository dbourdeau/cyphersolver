# CTTS project for R5464 (two leaves), for hand correction

Open with CTTS 3.7 (https://www.cryptool.org/en/ctts/): put `R5464_P1.png` and `R5464_P2.png` (the deskewed leaves, regenerate with
`export_ctts.py`, they are DECODE images and are git-ignored) in this folder next to `colors.txt`, `key.txt` and `positions/`, then run
`java -jar ctts-3.7.0.jar` in it. Loading was checked on 7 Nov 2026: "Read key.txt - 60 homophones", "60 assigned",
2,066 + 1,274 symbols (all assigned).

- `positions/*_positions.txt`: one box per sign (x y w h colour-index), made by the sensitive detector (block 41, C 12, big area 100).
- `colors.txt`: symbol types; type `#N` is cluster `sN` of `ctts/r5464_best/tokens.txt`.
- `key.txt`: the key after the word-guided refinement (`ctts/r5464_best/key_refined.txt`); about 27 % of the text then falls in words of
  4+ letters. It is a machine key: check the weak letters (c, d, g, h, m, p, v) and the clusters that look like two signs in one box.
- Line endings must be LF (CTTS fails on CR); `.gitattributes` should keep them so.
Regenerate: `EXP_PKL=ctts/r14.txt.pkl EXP_SRPREFIX=sr_r14_ SR_BIGAREA=100 SR_OVERLAP=0.4 SR_RING=14 python export_ctts.py ctts_proj/R5464 ctts/kr_r14_key.txt`
