# Verification of bresegno1548 (catalogue 1563, first letter), 3 Nov 2026

Independent, adversarial check. The verifier is a separate AI language-model agent. It read the signs before it opened
any transcription, decryption, reading or key file. `manrique1554/` was left out and was not checked.

Verdict: **downgrade**. The work is sound. The sign transcription is good, the key is confirmed on an independent blind
sample, and the check script works. The status "read" is the problem: only 78.4% of words come verbatim from the signs,
under the 95% rule. The full text is known only because the contemporary decipherment c. 22r gives it. Recommended
status: **read in part** (a transcription job; 196 of 250 words verbatim from the signs; content known in full from
c. 22r).

## 1. Blind transcription and comparison

Sample: L01-L04 and L19-L24 of c. 15r, about 287 signs. L19-L24 lie inside the held-out passage (L17-L24). The verifier
transcribed from its own strips of `scans/bres_15r.jpg` at 1.5x, before opening `transcription_c15r*.txt`. It used the
names in `SIGN_CONVENTIONS.md` and read only `NOTES.md` for image locations. Blind text:

```
L01 x. 7. 4 ms {Cmi} o^5? s L o q^2 d^4 o q? a + 7 o 2 L
L02 C^4 + s o^5 L Lx? s L^5 C^2 s? L^5 3 rs^4 o {bir} 2 7 L C^3? o^5 L # o^6 L^2 d^5 o L 4 ms
L03 o^2 # C^4 hs a D. + T^2 o q^6 7^5 o L C s^3 4 hs^6 # h i s L^2 o^5 L C s d^4 o^4 a L D d^3 # a^6
L04 o # 2 ms^2 L^5 o q o # o^2 s^5 L 3 # o^6 L [blot] d^5 d^3 ms o^2 # C^4? hs a D o^5 L 7 L^2
L19 d^5 o^5 o^5 a^3 L #^2 7^2 4 # o C^6 2 s o # C^2 o^5 #^2 d^4 d^5 + 7 4 a^3 L #^2 7^2 a^5 L^3
L20 s o L 4 ms a^2 ms^2 o^4 a C s^3 q^4 o L C #^5 q^5 O x s^3 # ms^5 # + T^2 3 h ms^3 # ms^3
L21 #^5 # C^6 7 o^4 #^3 L q^2 # C^2 + 7 4 o ms #^3 L^5 s {Bran} o x^4 2 #^3 h^3 L C^3 2 #^5 o^5 {bir}
L22 o s ms^3 o # C^5 o # ms^5 + T^2 o q^2 # C^2 2 q^5 s^2 q^2 o^5 L rs^3 {bar} 3 d^5 D. o s #^3 s^2
L23 #^3 s 7^4 d^5 d^3 C^3 L^3 hs a o L #^4 a^5 s + T^2 o {bir} o o^4 x^4 s 3^4 d^2 L^5 o^5 s^5 L a^5 s
L24 q^2 7^3 s #^3 ms^5 d^4 o q^5 o L o^5 L rs^3 {barn} a L 3 o ms o ms {Ar} {bor} 2 {bur}
```

Raw disagreements with `transcription_c15r.txt`: 11 at sign level (base sign, a missing or extra sign, or a digit
present or absent), 3 where a digit is attached to a different neighbour, and 2 segmentation choices (`{Cmi}` / `C {mi}`,
`o s` / `Os`). That is **16 of about 287 (5.6%) raw, 11 (3.8%) at sign level**.

Each disagreement was settled on 2x-2.5x crops of the full-size scan:

| line | verifier | solver | settled |
|---|---|---|---|
| L01 | `o` after `s L` | `O?` | solver right: a round sign with a dot inside, not the barred `o` |
| L02 | `#` | `#^6` | solver right: two 6s, over `#` and over `o` |
| L02 | `d^5` | `d^3` | **verifier right.** The digit is a single stroke with a top flag (this hand's 5), and the gloss above reads "cu na do". With `d^5` "cuñado" is verbatim and the mark `cunad{o/e}` falls away |
| L03 | `s` | `s^2?` | solver probably right: a 2 sits in the blot band between `s` and `d^4`; left doubtful |
| L04 | `L^5` | `L` | unresolved: a small 5-like mark above the `L`; may be a gloss stroke |
| L04 | `#` | `#^2` | solver right: there are two 2s (after `#` and after `o`) |
| L04 | `#` | `#^6` | solver right: two 6s |
| L19 | `o` (3rd sign) | `O^5?` | solver right (dotted round sign) |
| L19 | `#^2 7^2` (end) | `# 7^22` | ambiguous by position. The first 2 starts where `#` ends; the scribe writes digits after their sign. "pensaua" gives `#^2`=sa. Probably a solver slip that costs one mark (`pens{+a}ua`) |
| L20 | `3 h ms^3` | `3 ms^3` | one ligature (`ms` with an ascender on the first stroke), not two signs. The verifier's extra `h` was wrong. The solver's `ms^3` drops the ascender (shape naming only) |
| L20 | `C #^5` | `C^5 #` | solver right by context (Trezientos) |
| L21 | `7 o^4` | `7^4 o` | solver right by context (sostuuiessen) |
| L21 | `o x^4` | `o O x^4` | solver right: a dotted `O` between them that the verifier missed |
| L23 | `o^5` | `O^5` | solver right |

After settling: the solver is wrong at 1 place for certain (L02) and 1 probably (L19), and 1 is unresolved (L04). That
is **2-3 of 287 signs (0.7-1.0%)**. In the held-out lines L19-L24 (about 175 signs) it is 1 probable (0.6%). Most of the
verifier's own errors came from merging the dotted round `O` with the barred `o`. The solver keeps them apart
consistently.

Gloss: the verifier read c. 22r itself (overview and line checks). It agrees with `clear_c22r.txt`, including "sin al
calle" (P05) and "Bolona" (P14). The interlinear gloss over L01-L04 on c. 15r ("e l card. mo ro n me ha", "...uante con
su cu na do en el", "...ca sti llo y con una") agrees with c. 22r.

Wrong claim in NOTES.md: "The other disagreements only move a superscript between neighbours (`s^5 L` / `s L^5`), which
gives the same letters". This is false. `s^5 L` gives "ron" and `s L^5` gives "rno". Several marked words look like
attachment choices rather than encipherer errors: `confr{+o}n{-o}tar{+o}n`, `passar{+o}n {-o}a`, `Fierrau{+a}n{-a}te`,
`{+h}{+i}z{-i}{-h}o`, `pens{+a}ua`. The L01-L06 "same letters" disagreements were never settled, and L07-L24 were never
checked for attachment.

## 2. Rebuild

The folder was copied to scratch without scans or `manrique1554/`.

- `python scripts/decrypt.py transcription_c15r.txt key.tsv` gives output byte-identical to `decryption_c15r.txt`.
- `python scripts/reading.py check` exits 0: "words 250; verbatim from the signs 196 (78.4%); with marks 54".
- There is no separate check_marks script; `reading.py check` does that job.
- Unmarked departure (`cunad{o/e}` changed to `cunado` in the marked text): exit 1, "FAIL unmarked departure: reading
  implies ['o'], signs give ['e']". The check catches it.
- Over-mark test (L02 `d^3` changed to `d^5` in the transcription, marks unchanged): exit 1. So the check also catches a
  stale mark. Applying the L02 correction needs the reading updated (197 verbatim, 78.8%).

## 3. Held-out test

- Rerun: `heldout.py transcription_c15r_pass2.txt key_frozen.tsv 17 24 "vino a Bolona"` gives 0.869 in order and 0.826
  in runs of 4+. The best of 200 shuffled tables gives 0.327 and 0.093. Output is byte-identical to
  `work/heldout_pass2.txt`.
- It is graded against **c. 22r**, the contemporary decipherment. That is independent of the solver's reading, so the
  test is valid in kind.
- Independent replication: the verifier's own blind L19-L24, run through the frozen key against c. 22r, gives **0.872**
  in order and 0.843 in runs (best shuffled: 0.343 and 0.077). The solver's final transcription gives 0.887 and 0.880.
- Caveat on blindness: the file times show `work/p2_all_pairs.tsv` and `work/p2_all_table.tsv` at 18:34. That is an
  alignment over all 24 lines, including the held-out passage, and it was written before the L01-L16 tables (18:41:02)
  and `key_frozen.tsv` (18:41:40). The frozen rows cite only L01-L16 counts, but the person freezing the key had already
  seen held-out pairs. NOTES.md does not mention this. The verifier's independent result above lowers the concern, and
  this is a transcription job, not a break.
- The `key.tsv` rule "bare `a` before `s`/`ms` = p" was added after the freeze. It draws on L13, L15 and L18 (L18 is in
  the held-out passage). It lifts the verbatim count and should be called post hoc.

## 4. Counts and honest headline

Recounted from the marked text: 250 words (code groups count as one; 12 such words); **196 verbatim (78.4%)**; 54 marked.
Of those, 8 carry only extra-sign marks (`{-x}`) and 46 need a letter restored or changed. With the two settled sign
fixes (L02, L19): 198 (79.2%).

Dan's rule needs about 95% of words for "read". On the signs this letter is 78-79%. The 100% "reads as sense" comes from
c. 22r, not from the signs. The merged precedent, ferdinand1552, did not call transcription-job letters "read". Honest
headline: **"Transcription job: 196 of 250 words (78.4%) verbatim from the signs; 54 need a marked repair; the full text
is the contemporary decipherment on c. 22r."** Status: **read in part**.

## 5. Reading files

- `reading_c15r.md`: **A**. Coherent sense throughout, since it is c. 22r's text. Weak places: "sin al calle" (sense
  "alzalle" is an editorial guess); "a este q" (who "este" is); the code groups `{Gra}`, `{Bran}`, `{mi}`, `{barn}` occur
  once or twice and their values rest only on c. 22r; L24 "a el el Papa" and the trailing `{bor} 2 {bur}` are treated as
  nulls with no proof.
- `translation_c15r.md`: **A**. Faithful. Minor points: "losquales le sostuuiessen" is rendered "who would hold him
  there"; "who would support/hold out for him" is closer. "Fierrauante" is not identified; that is said openly.
- `decryption_c15r.txt`: **B** as a raw syllable decryption. It is not meant to read alone; the departures are listed
  by `diff_clear.py`.

## 6. Vendor names and local paths

Grep of all .md, .txt, .tsv, .py and .json files outside `manrique1554/`: no vendor or model names and no local paths.
AI use is described as "AI language-model agents". `WAINUT-research` appears as the User-Agent (allowed). Not to be
committed: `scripts/__pycache__/*.pyc` (compiled files embed local paths), everything in `scans/` (images, IIIF JSON,
and the stray scripts `scans/pass2_crops/z.py` and `zz.py`), and `manrique1554/`.

## 7. Prior art

One web search (Fierravante/Fieravante, 1548, Bologna, Tor di Nona, Ferrante Gonzaga, Morone): no edition or
decipherment of this letter. That agrees with the solver's two searches. One fact turned up: Morone's legation of
Bologna ran to July 1548, so in October 1548 he was the former legate. NOTES.md says "legate of Bologna". c. 22r's "no
estando alli Moron" fits him having left.

## Must fix before a PR

1. Change the status from "read" to "read in part" (78.4% verbatim from the signs; content complete only through c. 22r).
2. Remove or correct the NOTES.md claim that moving a superscript "gives the same letters". Recheck the marked words that
   look like attachment choices.
3. L02 `d^3` to `d^5` (digit shape and gloss "cuñado"); review L19 `# 7^22` to `#^2 7^2` and L04 `L` / `L^5`. Rebuild the
   reading and the counts.
4. State in NOTES.md that an all-lines alignment (`work/p2_all_*.tsv`) was made before the freeze, and that the bare-`a`
   rule is post hoc. Add the verifier's independent held-out figure (0.872).
5. Leave out `manrique1554/` and cut the Manrique section of NOTES.md, which points to files that will not be in the PR.
   Leave out `scripts/__pycache__/` and all of `scans/`.
6. Context: "former legate of Bologna" (to July 1548).
