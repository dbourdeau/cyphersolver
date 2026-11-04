# Independent verification, 3 Nov 2026 (planned target `stmauris1548`)

Verifier: a separate AI language-model agent, working adversarially. I transcribed first, without the solver's
transcription, key, decryption or readings. Then I compared, reran the scripts in a scratch copy, and read both
readings. I edited no solver file.

**Verdict: FIX.** The break is real and the status "read in part" is right for both letters. Before a PR, though,
the key has several sign values that the text itself contradicts, and one transcription conflation can be fixed now.
Fixing them should raise the verbatim counts. Until they are fixed, the counts below are the honest figures.

## 1. Blind transcription (9r rows 1-16 of the held-out letter of 2 Aug 1548)

I transcribed 9r L01-L16 from `scans/c9r_L*.jpg` using only `SIGNS.md` (392 tokens). After that I aligned my file
with `transcription_l4_blind.txt` row by row, which gave 376 aligned sign positions.

- Raw: 17 positions differ (4.5%). Six of them are naming only: my `b` is the reader's `N12` (5 times), and my `3` is
  `N19`. That leaves **11 shape disagreements (2.9%)**.
- I settled them on 2-3x crops:
  - The solver's reader was right in 9 cases, and I was wrong:
    - 9r L01 `6o` (I wrote `6`).
    - 9r L02: the gamma-shaped `y` (I wrote `x`).
    - 9r L03 and L06 `N13`, a hooked stem with a loop (I wrote `+o`).
    - 9r L05 `N6` (I wrote `8`).
    - 9r L05 `dd` (I wrote `6o`).
    - 9r L10 `fs` (I wrote the N13 shape).
    - 9r L15 `N17`, A-like (I wrote `fs`).
    - 9r L06 and L11 `N15`: an 8 with a bar on top, which is not the plain `8`. I had merged the two.
  - One case is still open: 9r L01 `5` or `5o`. The ring is merged with the 5, and the reader already marks it doubtful.
- **Settled: 0 confirmed errors on the solver's side in 376 signs. One doubtful case was already flagged by the reader.**
  For 9r L01-L16 this works as a second blind pass. 9r L17-L18 and all of 9v still rest on one pass.
- Gloss over the cipher:
  - Over 9r row 1 the gloss "L on" stands above `W w x:`. The table gives "lon" there. This is a small independent
    check inside the held-out letter.
  - I read the gloss over 3r row 2 myself: "u r c/e ? a a p i g n a t e l ? n p o r t a l a". It agrees with all 15
    pairs in `gloss_seeds.tsv`, including the conflict NOTES discloses: the gloss gives **a** over `vt`, and the key
    has `vt` = s.
  - Over `O` the glossator wrote a dotted, i-like mark. The seed file leaves `O` out, which I think is right because
    the mark is unclear.

## 2. Rebuild

- In a scratch copy, `check_marks.py` reproduced the counts, `--write` regenerated `decryption_l2.txt` and
  `decryption_l4.txt`, and the regenerated files are **byte-identical** to the originals.
- I injected three unmarked departures, and `check_marks` **exits 1** on each:
  - one changed letter ("Piedmonx");
  - one silently dropped letter ("toutefois");
  - one transcription token changed without a matching decryption.
- The checker does have one blind spot: it deletes anything in parentheses inside "## French". Today that only hides
  the "(3r, after ...)" notes, but it would hide anything else put in parentheses.

## 3. Held-out test

- I reran `heldout.py`. It reproduces the published figures:
  - 830 tokens, 96.0% of them with a key value;
  - 4-gram score -4.176 against a maximum of -5.181 over 200 shuffled tables;
  - word cover 0.217 against a maximum of 0.077.
- The test compares scores with permuted tables. It does **not** grade against an independent text, because there is
  no gloss on 9r-9v apart from "L on". The word counts for 2 Aug come from `check_marks.py`, and that script grades
  against the solver's own reading.
- **The 2 Aug transcription is not purely blind.** `transcription_l4.txt` maps the reader's `n` to `y` ("same shape
  class"). The reader's own gamma-shaped `y` (9r L02, 9v L16) was kept as `y` too, so two shapes the blind reader kept
  apart are merged into `y` = a.
  - Both gamma places read better as e: "ie n{e/a}" becomes "ie ne", and "defansive" becomes "defensive".
  - The `{e/a}` repair is therefore an artefact of the merge.

## 4. Key values contradicted by the text (must fix or flag)

| sign | frozen value | what the text needs | evidence |
|---|---|---|---|
| `8` in 10 Jan | q | **b** in 5 of 17 | qien (bien) x2, arquequsiers, puqliques, tresqien. A crop of 3r L17 ("bien") shows an 8 with a bar on top, the same shape as the held-out `N15`, which reads b in ambassadeurs (x2) and possible. The 10 Jan transcription merges `8` and `N15`. |
| `N6` | e | **m** | Never e verbatim. m in confidamment, comme, commandement, monsieur; q once; dropped once as a null. |
| `Le` | c | ll / nn in 7, c in 2 | represaille, iournellement, Excellence, personne, donner, conseiller, bonne (?); c only in cependent, vices. Either a geminate sign or two shapes merged. NOTES says "doubled letters are written out", and this contradicts it. |
| `R` | g | g 6/6 in 10 Jan; **x** 3/3 in 2 Aug | eulx, ceulx, Excellence. Check whether the two readers' `R` is the same shape. |
| `x` | a | a in 17, **h** in 3 | Rochelle, chemin, hors. The key has **no h at all**. chasteau and empescheront take h from `d` (r), also as repairs. |

## 5. Counts and headline

These are the counts from `check_marks.py`, which I confirmed:

| letter | words | verbatim | with marked repairs | proposed | holes |
|---|---|---|---|---|---|
| 10 Jan 1548 | 255 | 200 (78.4%) | 236 (92.5%) | 4 | 15 |
| 2 Aug 1548 | 178 | 133 (74.7%) | 171 (96.1%) | 2 | 5 |

- Combined: 333 of 433 words verbatim (76.9%).
- Neither letter reaches the 95% verbatim bar. Both are **read in part**.
- The 96.1% "with repairs" for 2 Aug includes 26 letters filled from context for signs that are not in the table. It
  must not be presented as "read".
- The letters of 1547 and of 12 Mar 1548 are not transcribed.

**Honest headline:** two of four cipher letters are read in part: 10 Jan 1548 (78% of 255 words verbatim) and
2 Aug 1548 (75% of 178 words verbatim, held out with a frozen key). The 1547 and March 1548 letters are not yet
transcribed.

## 6. Reading grades

- `reading_l2.md`, 10 Jan 1548: **B**.
  - Paragraphs 2 to 6 read as coherent French: Dorsey's courier, Mirandola and the arquebusiers, the castle, La
    Rochelle to Scotland, peace and temporising.
  - Weak places:
    - Paragraph 1 is a skeleton between holes: pecesarlauest, fdeluialion, estronestdauandre.
    - "[...:deqtdeborqonnancieneuendant]" sits in the temporising sentence. The barred-8 = b split may help here.
    - The last paragraph (captain of Finale) is mostly holes.
- `reading_l4.md`, 2 Aug 1548: **B**.
  - Paragraph 2 reads well throughout: the passage of the prince, guarding his person, the French party in Italy.
  - Weak places:
    - "et sera qu'on la [?fanterie] demeure ... avec aultres ambassadeurs" does not make sense as given.
    - The holes after "par ou ie" (loureroies, perhaps "loueroie") and after "aisemant".
    - The first word of paragraph 3 is a hole ("[...:sdla]"), so the antecedent of "avec lequel" and the partner in
      the defensive league are lost.

## 7. Vendor names and local paths

I grepped all .md, .txt, .tsv and .py files and `.gitignore` for vendor and model names, user paths, archive or HTR
mentions: **no hits**. `fetch.py` sends the User-Agent "WAINUT-research". `scripts/__pycache__/` and `scans/` are
git-ignored.

## 8. Prior art

I ran one web search: Saint-Mauris, Ferrante Gonzaga, 1548, cifra, Estense, Campori. It found no edition or
decipherment of these Modena letters. It did turn up British Library copies of Saint-Mauris's letters to Covos
(June 1547 to October 1548), which may hold related clear text, and the Estense Autografoteca description. NOTES
already cites Pierrot et al. (HistoCrypt 2023) as a different table.

## Must fix before a PR

1. Split the 10 Jan `8` into `8` (q) and the barred 8 (`N15`, b). Recheck all 17 on crops. Rerun the solve and the
   counts.
2. Correct or flag `N6` (m, not e). As a post-held-out correction, keep the frozen file and add a corrected key.
3. Resolve `Le`: either a geminate sign or two shapes. Fix the NOTES sentence "doubled letters are written out".
4. Check `R` (g / x) and `x` (a / h) on crops for hidden shape splits. Say that the key has no h.
5. Undo the `n`+`y` merge in `transcription_l4.txt`. Keep the gamma sign separate and recount.
6. Do a second blind pass of 9r L17-L18 and 9v. This verification covers 9r L01-L16 only.
7. Make the verbatim percentage the headline, not "with marked repairs". Verify the historical notes (Dorsey,
   Pignatelli, the La Rochelle sailing, the defensive league) before publication.
