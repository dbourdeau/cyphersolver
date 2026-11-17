# Brice Dudout's reading of the letter of 15 Oct 1552 (catalogue 1332)

Ferdinand I to G. B. Castaldo, Vienna, 15 Oct 1552, Ambrosiana G 275 inf., ff. 34r-35v. Claimed 29 Oct 2026
(commit bc65ae2a on bdudout/cyphersolver, branch `dudout/castaldo1552`, target `castaldo1552`), independent of
the reading in this folder. Added here on request (issue #746) so that the two readings can be compared.

Key rebuilt from the contemporary marginal glosses of the sister letters of 13 and 18 Oct; held-out word scores
0.73 (f. 44v) and 0.78 (f. 45v), letter of 22 Oct, against at most 0.03 for 200 control keys; 316 of 319 words
read, 273 sure (41 probable, 2 restored, 3 unresolved code groups). Code C8 = Lippa from the gloss of f. 45v.

All files are copied byte for byte: their wording and figures are those of 29 Oct, not revised. No image is
included (Ambrosiana images were used for study only).

## Files from commit bc65ae2a (`targets/castaldo1552/`)

| file | content |
|---|---|
| `NOTES.md` | write-up of 29 Oct (method, scores, reading counts) |
| `profile.json` | profile as prepared for `targets/castaldo1552` (kept under its original name; not a target profile here) |
| `key.tsv` | key K2: sign, value; nulls and codes in the header |
| `signs.md` | ASCII codes used for the signs, with descriptions |
| `transcription.txt` | ff. 34r-35v, one manuscript line per line, ASCII sign codes |
| `decryption.txt` | sign-by-sign decryption of `transcription.txt` with K2 |
| `reading.md` | established Latin text: sure / {probable} / [restored] / <unresolved> |
| `translation.md` | English translation |

## Working files of 29 Oct (`controls/`, from our folder `italie-divers-v23b/n1332-castaldo/c01/`, French notes)

| file | content |
|---|---|
| `PROTOCOLE.md` (+ `.sha256`) | protocol written and hashed before any computing (the hash file gives the path `c01/PROTOCOLE.md`) |
| `G_c10r.txt`, `K_c10r.txt`, `K_c37r_a.txt` | key construction: gloss and cipher of f. 10r (13 Oct) and f. 37r (18 Oct) |
| `K1.json` (+ `.sha256`) | key K1, frozen before the held-out passages were transcribed |
| `AVENANT-V.md` (+ `.sha256`) | addendum written before transcribing the first held-out passage: block, score definition, 200 controls (random permutations of the key values) |
| `V_c44v.txt` (+ `.sha256`) | held-out cipher, f. 44v, transcribed and frozen before the margin was read |
| `G_c44v_L10-24.txt` | the contemporary gloss of that passage |
| `V_score.txt` | result with K1: 0.918 characters, 0.731 words (49/67); controls at most 0.312 / 0.030 |
| `AVENANT-V2.md` (+ `.sha256`) | second addendum, before the second held-out passage. It names f. 46v; the passage actually transcribed and scored is f. 45v ll. 1-16, as the headers of `V2_c45v.txt` and `G_c45v_L1-16.txt` say |
| `K2.json` (+ `.sha256`), `K2m.json` | key K2 (K1 + 9, &, y, *, 8) and the mechanical form used for scoring |
| `V2_c45v.txt` (+ `.sha256`) | second held-out cipher, f. 45v ll. 1-16, frozen before the margin was read |
| `G_c45v_L1-16.txt` | the contemporary gloss of that passage |
| `V2_score.txt` | result with K2: 0.932 characters, 0.778 words (49/63); controls at most 0.282 / 0.032 |
| `T_c34r.txt` ... `T_c35v.txt`, `T_SHA256.txt` | transcription of the target letter, frozen before decoding |
| `SIGNES.md` | sign codes (source of `signs.md`) |
| `LECTURE.txt`, `LECTURE_normalisee.txt` | reading with the word counts, and the same in normalised spelling |

All `.sha256` files and `T_SHA256.txt` check against the copies here.

Not included: the scoring script and the 200 individual control scores were not kept; only the maximum and
mean of the controls are in the two score files. The score is defined in `AVENANT-V.md` (alignment with nulls
and omissions; characters = identical aligned letters / gloss letters; words = gloss words entirely correct).

Transcription, key and reading by AI agents (Claude, Anthropic) under rules set by Brice Dudout (L'Europe chiffrée).
