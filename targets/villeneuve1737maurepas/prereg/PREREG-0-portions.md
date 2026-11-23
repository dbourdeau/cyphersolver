# PREREG-0 — villeneuve-1737 (cat. 538), Archives nationales, AE/B/I/414 — designation of portions
Date: 2026-11-20 (before any key is built; no decoding done yet)

Images: 26 JPEG received 20/11/2026 (frames 0060-0062, 0092-0097, 0197-0202, 0229-0239). Frame 0229 = clear text, cipher starts 0230.

Letters:
- T1 = 18 Feb 1737 (target, "non déchiffrée"): frames 0060, 0061 L+R, 0062 L.
- T2 = 2 Apr 1737 (target, "partiellement chiffrée, non transcrite"): frames 0092, 0093 L+R, 0094 L+R, 0095 L+R, 0096 L (clear text from 0096 R to 0097 L; 0093-0097 carry the header strip of a 10 Apr 1737 sheet behind, not a separate cipher letter).
- W1 = 9 Jul 1737, interlinear period decipherment: frames 0197, 0198 L+R, 0199 L+R, 0200 L+R, 0201 L+R, 0202 L.
- W2 = 29 Jul 1737, interlinear period decipherment: frames 0230 L+R, 0231 L.

Portions:
- TRAIN = W1 frames 0197, 0198, 0199 + W2 (0230, 0231): key is built ONLY from these cipher groups and their glosses.
- HELD-OUT (measure, one measure only, burnt after) = W1 frames 0200 L+R, 0201 L+R, 0202 L. Glosses of these frames are not used for the key.
- Targets T1, T2 are not decoded before the key and PREREG-1 are frozen by SHA-256.

Measure (fixed now): decode the held-out cipher groups with the frozen key; compare to the period interlinear gloss, character agreement after normalisation (lowercase, letters a-z only, accents stripped, u/v and i/j merged), alignment by edit distance (1 - Levenshtein/len(gloss)). Controls: 200 keys made by shuffling the frozen key's values among its codes (seeded, seed fixed in PREREG-1). Pass = score >= 0.85 AND >= best control + 0.30. Word agreement reported, not decisive. Held-out under 300 cipher groups = « non mesurable ».
