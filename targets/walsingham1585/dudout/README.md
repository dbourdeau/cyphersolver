Status: read in part (Brice Dudout, 9 Nov 2026; R4844 sign words: 16 of 19 groups read, about 86% of sign letters read for sense, 3 groups unresolved; sign key from the deciphered pairs DECODE R4689, R4835, R4836, partial by our protocol on held-out R4845, 0.646 vs 0.213; name codes 3 corrected, 14, 27, 37 identified).

# Walsingham to Wotton, 1585: the sign alphabet and the name code from the deciphered pairs (Brice Dudout, with Claude)

A contribution to Daniel Bourdeau's targets `walsingham1585` and `wotton1585`. Daniel's files are not changed; this
folder adds what the **deciphered letters in the same volume** give. Text only: no image, crop or derivative of the DECODE /
British Library scans; signs are written as text labels (`frozen/INVENTAIRE-SIGNES.md`).

Sources (BL Add MS 32657): pairs with the interlinear decipherment of the time, DECODE **R4689** (ff. 93-94,
https://de-crypt.org/decrypt-web/RecordsView/4689), **R4835** (ff. 95-96, .../RecordsView/4835), **R4836** (ff. 109-110,
.../RecordsView/4836), **R4837** (ff. 111-112, .../RecordsView/4837), **R4845** (ff. 198-199, .../RecordsView/4845), all
"Decrypted" on DECODE; target letter **R4844** (ff. 194-195, .../RecordsView/4844).

## 1. Sign alphabet: held-out test (partial)

- Protocol written and hashed before any key was built and before R4837 and R4845 were seen (`frozen/PREREG.md`, French,
  SHA-256 in `frozen/SHA256SUMS`).
- Key learnt on the glossed sign words of R4689, R4835 and R4836 only (`sign_key.tsv`, frozen as `frozen/CLE-S.tsv`).
- Held-out part H = R4845: its sign words transcribed blind by a separate agent (`frozen/H-chiffre.txt`, 29 words), the
  glosses read by a second agent (`frozen/H-gloses.txt`).
- One measurement (`frozen/mesure.py`, `frozen/RESULTAT-MESURE.txt`): **0.646** of letters right against at best **0.213**
  for 200 shuffled keys (margin 0.433). Threshold for "validated" fixed in advance: 0.85, not met: **partial**. The errors
  come mostly from homophones not yet separated (÷ = r/s; ω = e/h/g).

## 2. R4844: the sign words read in part (`reading_R4844_signs.md`)

Your NOTES call these about fourteen words "too short, no key found". The same alphabet is deciphered at the time in the
five pairs above. With the key: **16 of 19 sign groups read** (plot, judgment, her selfe, violent course, [a]bsent, attempt,
traine, Stirling, suspicion, Lorde, Scroupe, secreat, plot, secrecy), 3 unresolved; about **86%** of the sign letters
read for sense, under 95%: read in part. Several are probable (graded in the table).

## 3. Name code (`name_codes.md`)

From the glosses of the pairs: **3 = the Queen / England (your key.md has "France", M)**, 14 = Earl of Leicester, 27 = the
Secretary (Maitland), 37 = Scotland; 10, 19, 36, 39, 40 confirmed. The correction of 3 touches both targets
(`wotton1585/texts/key.md` too); we did not edit your files.

## Limits

One transcriber per part (AI agents), no human palaeographic check. The key is partial; the post-measurement additions
(listed in the key header) are not tested. Prior work re-checked 9 Nov 2026: your targets (name code, R4840-R4843 read);
DECODE marks the pairs Decrypted and R4838-R4844 Non-decrypted; no printed decipherment of the R4844 sign words known
(CSP Scotland viii does not calendar the 10 Sep 1585 letter, per your notes). Read's *Mr Secretary Walsingham* and CSP
Foreign 1584-85 not re-checked.
