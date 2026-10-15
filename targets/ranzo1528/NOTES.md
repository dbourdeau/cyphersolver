# Ranzo's code, 1528: the letter to "Garbino" (BnF fr. 3022 no. 20) and Hieronimo Ranzo's letters (fr. 2988, fr. 3019; DECODE R1894, R4450; catalogue items 7 and 170)

Status: read in part (14 Oct 2026), by others: Paolo Rosson with Claude (6 Oct 2026, on this project's transcription) and George Lasry with Claude Opus 5.5 and GPT-6 Astra (6 Oct 2026, on Norbert Biermann's transcription; contributed 14 Oct 2026, `lasry/`). This project's own annealer recovered only function words. Split from `targets/vasto1527/` on 14 Oct 2026.

Gallica: fr. 3022 ark `btv1b90601558` (view = canvas; ink folio ≈ (view+1)/2), fr. 2988 `btv1b9059908w`, fr. 3019 `btv1b9059994n`, Clair. 327 `btv1b9000764n`.

## The pieces

| 20 | ff. 44r–46v (views 86–91) | Italian letter, Madrid 11 April 1528, **to "Garbino"** (endorsement, f. 47v); the writer is almost certainly **Hieronimo Ranzo**, Gattinara's man (same code as Ranzo's signed letters, below) | **not solved.** Code structure established, full transcription made, function-word skeleton only. See below. |
- **ff. 48–50v of fr. 3022 (nos. 20bis–21)** is Garbino's espionage kit:
- **ff. 48–50v (nos. 20bis–21)** is Garbino's espionage kit:
  - A jargon sheet: cover letters are signed "Antonio de Cosenza" and addressed to "Andrea Romano in Valencia", and news is disguised as grain prices.
  - A code-name list, e.g. Imperatore = "Joan Jacobo", Marchese del Guasto = "portolano de Gergenti", Garbino = "antonio petra".
  - The **"Aditione nel zifra"** (`additione.json`).

## No. 20 and the Ranzo letters (from the work of 18 Sept 2026)

**System.** Each group is a base letter with a superscript number: c170, i100, p149 and so on; the base letter is
the initial of the word or syllable. The addition sheet (f. 50; a327 apresso, c327 Cartagenia, h106 havendo, s395
soa santita) has the same design, **but it is not this code's key** (George Lasry, 14 Oct 2026; checked the same
day): of its 113 groups only g217 (once) occurs in the 3,912 transcribed groups of no. 20 and Ranzo's letters, and
its numbers overlap those the letters use (it starts b at 157, the letters run to b215; a323, c325, p383, s387).
The 18 Sept reading that it "continues each base list (a1–326, b1–156 …)" was wrong. It is shown on the page for
illustration only.

**The numbering within a letter is not alphabetical.** Tested in `n20/alphatest.py`:
- no. 20 scores z = −0.5 against a shuffled-order null.
- The test's power check, a genuinely alphabetical code applied to Castiglione's letters, scores z ≈ +6.5.

So a number carries no positional information. Other bases:
- **z** (z6–z9, z15): behaves as nulls or punctuation.
- **y** (y2–y53, ~130 tokens): a genuine list of unknown initial. Its glyph resembles the addition sheet's x.
- **Q** and **D**: rare extra lists.

**Ciphertext in the same code.**

| source | groups | notes |
|---|---|---|
| no. 20 (`n20/f44r.txt` … `f46v.txt`) | 1,315 (546 types) | transcribed from full-resolution scans |
| Ranzo's signed letters, BnF fr. 2988 ff. 2r–v, 9r–10v (ark btv1b9059908w, views 6, 7, 17–20) | ~2,600 | `n20/ranzo_c0*.txt`, transcribed by six subagents. f. 2v is marked "dup.ª" (duplicate). |
| **Total** | ~3,900 | 316 group types shared between the two sources |

fr. 2988's other "pièces en chiffre" (views 43–87, alternating with clear copies of Doria letters, July–Aug 1528) are a dense symbol cipher of the French side, not this code; checked views 56 and 60. Ranzo in fr. 3019 no. 27 (f. 73) is views 114–116 of btv1b9059994n: signed 'Hieronimo Ranzo', all in cipher, no interlinear or separate decipherment (view 118 is an unrelated 1559 docket); not transcribed. No duplicate or crib either: the no. 20 and Ranzo transcriptions share nothing longer than stock three- and four-group phrases. Cipherbrain (17 May 2016, comments by Norbert Biermann and Thomas, 2017) found no known nomenclator for Ranzo's code. Also and
possibly fr. 3019 no. 36 (f. 94, "Reporto de homo … venuto da Genova", chiffré).

**Clair. 327 ff. 279–280** (btv1b9000764n views 263–264) is an 18th-century copy of no. 20. It is headed
"Vol. 86 fol. 44 … Lettre non signée écrite au seigneur Garbino du 11 d'avril 1528 … partie en chiffre, partie
non", and has no decipherment. **Clair. 314 f. 337** (btv1b90007741 view 252) copies the addition and jargon
sheets. No French decipherment and no base key was found.

**Attack (`n20/solve2.py`).** A word-substitution annealer:
- each group type maps injectively to a word with the right initial
- z-groups are optional nulls
- scoring is a Kneser–Ney word-bigram model on Castiglione's *Lettere* (1769–71 ed., long-s OCR repaired) plus Guicciardini/Machiavelli from Wikisource

It was validated on a held-out 3,900-word Castiglione control encoded the same way: **token accuracy ~46%,
type accuracy ~9%**. So on the real text it can deliver only the function-word skeleton. That skeleton is
stable across six restarts:
- che (c170), il (i100), per (p149), la/le (L10/L47), re (r41), non (n38), si (s8), sua (s233)
- tanto (t89), tempo (t10), ma (m8), ne (n8), mi (m170), più (p246), molto (m7), nel (n90)
- ha/ho (h57/h30), in (i29), perché (p150), con (c227), a (a127), o (o113), io (i286), al (a137)

Content words are not recovered. **A reading needs the base key or real cribs.** The most promising crib
sources are:
- Garbino's side of the correspondence;
- Ranzo's letters in Spanish or Italian archives with contemporary decipherments;
- Gattinara's papers.

**DECODE R1894 (catalogue entry 170), 21 Sept 2026.** The record "BNdF AncienFonds invnr.2988 ff9-11" (Ranzo, Italian, 4 pp.,
dated 1520 by BnF's 1520-29 range) is the fr. 2988 Ranzo letter already transcribed above. The record has no key, decipherment or
transcription. Nothing new was attempted, and the entry is marked "attempted, open" in the same state as no. 20.

**Prior art found 14 Oct 2026 (Cryptoole alert check).** Paolo Rosson, with Claude and on our transcription, published a reading of
the Ranzo code on 6 Oct 2026: <https://pangoleen.github.io/cipher-readings/centurione-1528.html>. It covers no. 20 (the "Garbino"
letter, ff. 45r-46v), the first Ranzo letter from its duplicate fr. 3019 ff. 73r-74r (Madrid, 27 March 1528) and the last two lines
at fr. 2988 view 20. Their figures: 86% of the cipher text in connected stretches, about 85% of tokens right (92% inside the
stretches), key table of 779 values (117 sure, 595 probable, 67 guesses), weakest page f. 46v at 66%; no per-letter numbers, no
palaeographer check. Cryptoole (IT1520-1) marks the case solved, 6 Oct 2026, Rosson and Lasry. This contradicts the "not solved"
verdict above for no. 20 and the 'no duplicate' remark about fr. 3019 no. 27. **Not yet done:** compare their key and readings
with `n20/` and `n20/ranzo_c0*.txt`, measure what fraction of R1894 (fr. 2988 views 17-20) and R4450 is read, and decide the
outcome.method (read from existing decipherment, not our own). Until then the status of nos. 20 and R1894 stays open.

**Comparison and measurement, 14 Oct 2026.** `measure_rosson.py` applies Rosson's `key/table.tsv` and `transcription_corrections.tsv` (downloaded from his repository, not copied here) to our transcriptions:
`python measure_rosson.py <his folder> n20/f44r.txt ... n20/ranzo_c020.txt`.

| files | groups | sure | probable | guess | null | no value | in runs of 6+ sure/probable |
|---|---|---|---|---|---|---|---|
| no. 20 (f44r-f46v) | 1,311 | 653 | 517 | 37 | 60 | 44 | 1,046 (79.8%) |
| R1894 = fr. 2988 ff. 9r-10v (c017-c020) | 1,776 | 922 | 769 | 25 | 36 | 24 | 1,654 (93.1%) |
| fr. 2988 ff. 2r-v (c006, c007; not R1894) | 816 | 416 | 342 | 14 | 28 | 16 | 724 (88.7%) |

- The measure applies decode.py's rule that g above 214 is s and t above 196 is r (an earlier pass without it gave 66-81%).
- His key was built on this transcription for fr. 2988 and f. 3022, so the fit is not independent. His own check of the images moved 57 'g' to s and 63 't' to r in fr. 2988; our transcription stands corrected there.
- Spot reads of c017 and c020 are coherent 1528 Italian (instructions to write through Hieronimo Ranzo, "zifra grande nostro", payments by the army).
- Below the 95% read bar on every measure, so: **read in part, by Rosson with Claude**. R4450 is a copy of fr. 2988 f. 9, so it is covered as far as f. 9 is (views 17-18); no separate transcription.
- Outcome method for no. 20 and R1894: read from existing decipherment (others', 6 Oct 2026). Our own contribution is the transcription, now partly corrected by his image check.
- Not rerun: his blind controls (`evidence/controls.md`, 87.6% and 93.4% on made-up codes).


## George Lasry’s independent Ranzo contribution — 14 October 2026

Contributed by George Lasry, based on Norbert Biermann’s 2021 transcription, with the decipherment achieved in collaboration between Claude Opus 5.5 and GPT-6 Astra. The Codex consolidation is dated 6 October 2026. See `lasry/NOTES.md` for the five-letter scope, documented crib/structural recovery, limited historical-addition checks, 871-entry working key, exact counts and open issues. The preceding project/Rosson measurements are not replaced.

Tomokiyo’s Cryptiana article, https://cryptiana.web.fc2.com/code/ranzo.htm (6 Oct 2026), records Lasry’s solution report arriving hours after Rosson’s email. Rosson’s solution was independent and contemporaneous, as Lasry reports; no public-priority claim is made. The contributions use different transcriptions: Biermann’s here, Bourdeau’s for Rosson.

Validation of the new packet reproduces 541 line-aligned readings, 6,428 cipher occurrences and every key frequency. Of 6,221 non-null occurrences, 5,967 receive a proposed value, including 841 tentative occurrences; 254 remain unassigned. The 95.9% is assignment coverage, not measured plaintext accuracy. Two continuous three-sentence excerpts have exact token boundaries, readable Italian and complete English translations. The visual key contains all 871 proposed mappings, preserving case and uncertainty.

This is publication of existing results, not a renewed solving run. The user ended the key-comparison exercise and requested this contribution. Original files remain untouched.

## The five letters of George Lasry's package, as documents (14 Oct 2026)

`profile.json` now lists every letter his edition covers (counts from `lasry/counts.json`, his non-null
occurrences given a proposed value, tentative ones included):

| profile id | letter (Lasry no.) | shelfmark | occurrences | non-null valued |
|---|---|---|---|---|
| fr2988f2 | 1 | BnF fr. 2988 ff. 2r-v; duplicate fr. 3019 no. 27 ff. 73r-74r (Madrid, 27 March 1528) | 818 | 764 of 790 |
| r1894 | 2 | BnF fr. 2988 ff. 9r-10v (DECODE R1894); copy fr. 20506 ff. 136-138 (R4450) | 1,781 | 1,703 of 1,746 |
| no20 | 3 | BnF fr. 3022 no. 20, ff. 44-47; copy Clair. 327 ff. 279-280 | 1,314 | 1,185 of 1,249 |
| fr4050 | 4 | BnF fr. 4050 ff. 79-81 | 1,559 | 1,440 of 1,530 |
| fr6638 | 5 | BnF fr. 6638 pp. 67-70 | 956 | 875 of 906 |

Letters 4 and 5 have not been seen or transcribed by this project; Biermann's transcription gives no Gallica link
for them. Letter 1 is transcribed here too (`n20/ranzo_c006.txt`, `c007.txt`); Rosson's key values 88.7% of its
groups in connected runs.

## Assumptions for George's review

- All five letters are treated as one code, Ranzo's, on the evidence of his package: one 871-entry key reads all
  five. For fr. 4050 and fr. 6638 this project has no independent check (no image seen, no shared-group count of
  its own).
- fr. 4050 and fr. 6638 carry no date in his files; the profile gives them the year 1528 of the other three, with
  the date "unknown".
- His credit stays a single "solution" credit covering the five letters; Rosson's covers what his page reads
  (no. 20, the fr. 3019 duplicate of letter 1, the last lines of fr. 2988 view 20), and his key applied here
  values letters 1-3 as measured above.

## Remaining gaps

- No. 20 and the Ranzo letters of fr. 2988 ff. 9-10 (R1894/R4450): 84 groups without a value (of 3,903 parsed in all twelve files), 76 guesses, and 79.8% (no. 20) and 93.1% (R1894) in connected stretches - blocker: open-codes; Rosson's key (6 Oct 2026) reads the rest, our own annealer never did. Still to do: compare his islands with the images page by page; transcribe fr. 2988 ff. 2r-v and fr. 3019 f. 73 (the duplicate) here.

## Escalation

- [x] siblings: Ranzo's signed letters in fr. 2988 ff. 2r-v and 9r-10v transcribed (n20/ranzo_c0*.txt); fr. 3019 no. 27 (f. 73) located, the duplicate of fr. 2988 f. 2; R4450 is a copy of f. 9.
- [x] clear-pages: Clair. 327 ff. 279-280 and Clair. 314 f. 337 are 18th-c. copies without decipherment; fr. 2988's other cipher pieces are a different French cipher.
- [x] known-keys: none in the archive; Cipherbrain (2016-17) found no nomenclator. Rosson's key (6 Oct 2026) and George Lasry's key (6 Oct 2026) now exist and were measured or imported.
- [x] print: Cipherbrain 2016; Tomokiyo, cryptiana ranzo.htm (6 Oct 2026); Rosson's page.
- [x] key-rebuild: word-substitution annealer with an Italian word-bigram model, validated on an encoded Castiglione control (~46% tokens): function words only.
- [n/a] retry: the open groups are those of Rosson's and Lasry's keys; a retry means comparing their readings with the images page by page, not yet done.

## Files

- `n20/`: transcriptions (no. 20 `f44r.txt`-`f46v.txt` and Ranzo `ranzo_c0*.txt`), `load.py`, solvers (`solve.py` and `anchor.py` assume alphabetical order, now refuted; `free.py`, `solve2.py`), `alphatest.py`, `calib.py`
- `additione.json`: the addition sheet (fr. 3022 f. 50-50v), another code of the same design, not this code's key
- `measure_rosson.py`: applies Rosson's key to the transcriptions
- `lasry/`: George Lasry's contributed edition (Biermann transcription, 871-entry key, decode, excerpts, verify.py)
- `ita/`: Italian corpus preparation for the annealer; the corpus texts are not committed

## 14 Oct 2026: split from targets/vasto1527

This code sat in `targets/vasto1527/` (catalogue item 7, BnF fr. 3022 nos. 6, 10, 20) until 14 Oct 2026, on a page
titled "Del Vasto to Charles V, and a letter to Garbino". Del Vasto's letters (nos. 6, 10, 19) are in letter
ciphers with code groups; this is an initial-letter code with numbered word lists, a different system. George
Lasry pointed out that entries combining different ciphers are confusing. Moved here: `n20/`, `lasry/` (George
Lasry's contribution, untouched), `additione.json`, `measure_rosson.py`, `clairfetch.py`, `ita/`; the reveal file
became `docs/reveal/ranzo1528.json`. Page: `docs/ranzo1528.html`.
