# Independent verification: Selvatico Estense -> Riva, 1719 cipher letters (planned target selvatico1719)

Verifier, 3 Nov 2026. Adversarial check; no solver file was edited. Scratch work (crops, rebuild copy) stayed
outside the folder.

## Verdict

**fix** (outcome class: **read in part**). The status claimed in NOTES.md is honest: the two 1719 letters are
read in part, the 1722 letters (lead 1568) are not read and are not presented as read. The alphabet of the frozen
key is real: on my own blind transcription it turns the held-out cipher into the words the contemporary gloss
gives. But several things must be fixed before a PR: local paths in five scripts, a parser hole that silently
drops 18 groups (one of them is an unmarked missing word in a reading), four or five transcription errors in the
held-out sample, a Cyrillic letter in a reading, and the catalogue framing.

## 1. Blind transcription (done before opening transcription, decryption, reading or key files)

Sample: all cipher lines of f. 5v (lines L11-L15, the start of the held-out passage) and every cipher line of
f. 6r (held out, full page): **188 groups** (well over 300 digits). Gloss read by me over the same lines.

My gloss reading (6r): corriere de da ministri / impiego / alla sua nascita / sia la sua abilità / giorno / buon
gioco / questa / questo demerito / valida / assistenza / di cotesto Re e il maneggio del / [140: gloss looks like
"Matrim." or "Salmour", not settled] con questa figlia del reggente / Stairs / insinuare / animo / Re / seguendo.
5v: la furia di questa nazione / immaginarj / Conte Scotti / [gloss over 11 25 5 24 1 not settled: "fornita"?
"frumento"?] / figura / [57 gloss "comp.ni"?].

Comparison with `transcription_1719.txt` (pass B):

| | groups |
|---|---|
| raw disagreements, curls and marks included | 36 / 188 (19%) |
| value-changing disagreements (curl, dot, superscript ignored) | 9 / 188 (4.8%) |
| after settling on full-size crops: solver wrong | 4 certain + 1 probable (2.1-2.7%) |
| after settling: verifier wrong | 3 (1.6%) |

Settled one by one (full-size crops):

- 5v.L11: solver `c23 31 1 13 3`, verifier `c25 3 1 13 3`. The second digit is an s-shaped 5, distinct from the
  B-shaped 3 beside it; gloss "la furia". **Solver wrong** (2 groups). The reading has to patch it as
  `f[uri]a [a]`; with the corrected transcription the frozen key gives "furia" directly.
- 6r.L09: solver `c3 13 1`, verifier `c23 13 1`. The 2 is clear; gloss "valida". **Solver wrong**; with `c23` the
  key gives "valida" mechanically (the reading has `va[l]ida`).
- 6r.L15: solver `1 7 3`, verifier `173`. Spacing is a little wide, but the gloss gives "Re" over it and 173 = Re
  in the key ("del Re"). Solver's split gives "a m i". **Solver wrong** (the reading marks `[Re]`, so no false
  claim, but the transcription should be `173`). The same code is written `1.73` in 6r.L10.
- 6r.L02: solver `3`, verifier `3_`. A stroke runs under the 3; gloss "impiego" (3_ = in). **Probably solver
  wrong**; ambiguous because the stroke may belong to the gloss above the line below.
- 5v.L12: verifier `17`, solver `14?`. The 4 has its crossbar. **Verifier wrong.**
- 5v.L15: verifier `8 c27-`, solver `5 c24-`. Both shapes are s-shaped 5 and crossed 4. **Verifier wrong** (2).
- Curl and mark differences (c3/3, c2/2, 8/8', 33./33') do not change values under the key's rule and were not
  settled one by one.

Pass B gloss alignment (`work/pass_b_1719_gloss.tsv`) contains several misread gloss words that my reading of the
same images does not support: "apparenza" (gloss is "assistenza"), "denaro" ("demerito"), "che" over 173 ("Re"),
"arrive" ("animo"), "intimone" ("insinuare"). It is a work file, but if it is ever shipped as "the gloss" it must
be corrected or labelled as a rough alignment.

## 2. Rebuild

- `scripts/decrypt.py key_1719.tsv transcription_1719.txt` in a scratch copy: output **identical** to
  `decryption_1719.txt` except that the committed file starts with a UTF-8 BOM (written by another tool). Strip
  the BOM or regenerate with the script.
- `scripts/check_marks.py` (scratch copy, path made relative): passes, 441 words, 269 unmarked (61%). Same as
  claimed.
- Departure tests in the scratch copy: changing "abilità" to "nobilità" in a reading -> FAIL; changing a group in
  the transcription (6r.L13 last `c26` -> `c27`) -> FAIL; dropping letters ("insinua") -> FAIL. The checker does
  fail on an unmarked departure.
- **Hole found:** `norm()` only strips punctuation at the ends of a token, so any token with an inner dot, an
  inner `=` after a superscript, a non-ASCII superscript or `#` is silently dropped by both decrypt.py and
  check_marks.py (no `[n]` placeholder, no warning). 18 tokens are dropped: 4v.L07 `8.4.3`, 4v.L08 `1.13`,
  `7.4.3-`, 4v.L09 `c5.4`, 4v.L12 `12.4.c6.`, 6r.L09 `c27.c2.8-`, 6r.L10 `1.73`, 6v.L01 `c26.3.1`, 12r.L14 `8.4`,
  12v.L06 `c26=^e`, 12v.L12 `c26=^ão`, 12v.L14 `c29.^Cno`, 13r.L03 `c29:^Cno`, `c27.^e`, 13r.L08 `8.^cio`,
  `7.3.1`, 13v.L01 `c#-`, 13v.L04 `2^[?]`. Consequence: a reading can omit those groups with no mark and the
  checker passes. Real case: **6r.L10 reads "di cotesto e il [139] del" and leaves out 173 = Re with no mark.**
  Fix: split dotted tokens into groups (or normalise the transcription), emit `[?]` for any unparsable token, and
  have check_marks require a bracket for it.
- `__pycache__` exists in scripts/; must not be committed.

## 3. Held-out test

Rerun: there is no script; the count (about 31 of 40 legible gloss words on 5v-6v) is manual, as NOTES.md says.
It is graded against an **independent text, the contemporary gloss**, not against the solver's own reading. Good
design, but not reproducible as shipped.

My own count on my blind sample (5v L11-15 + 6r, my transcription, frozen key only): about 50 gloss words; about 36
come out exactly; about 5 come out except for one of the post-test values 18 n / 32 e / 33 i (nazione, nascita,
demerito, reggente, immaginarj); about 9 are code numbers the frozen key does not hold (Conte 55, corriere 69,
ministri 138, maneggio 139, 140, 57, 6_ de, ...). No gloss word contradicted a frozen letter value. This confirms
the alphabet independently. With the solver's transcription two of those hits (furia, valida) are lost to
transcription errors.

Caveat: the second test (27 Oct letter) has no gloss, so it is a sense test, not a graded test.

## 4. Counts and honest headline

check_marks: 441 cipher-passage words, 269 with no mark (61%). By part:

| part | words | unmarked | share |
|---|---|---|---|
| 2 Oct, ff. 4r-5r (the key was built from this gloss) | 136 | 88 | 65% |
| 2 Oct, ff. 5v-6v (held out, gloss partly legible) | 118 | 69 | 58% |
| 27 Oct, ff. 12r-13v (no gloss) | 187 | 112 | 60% |

Doubtful: the 61% counts every unmarked token as a read word, including fragments that are not words in sense:
27 Oct has unmarked "l-", "d", "imag-", "li le e se-", "vi la consenta al", "far", "conti la ... di ... d". The share
of words that read as sense in the 27 Oct letter is lower than 60% (I estimate about 50%). The 6r.L10 "Re" is
missing from the count.

Honest headline: **"Two 1719 letters read in part: 269 of 441 words in the cipher passages (61%) come straight
from the frozen key with no mark; 58% on the held-out pages of the 2 Oct letter. The four 1722 letters (lead
1568) and two undated letters use another table and are not read."** Far below Dan's ~95% for "read". The 1722
letters are at most "not solved" (not even decoded).

## 5. Reading files

- `reading_1719_1002.md`: **B.** On 4r-5r and 6r-6v the line reading and the continuous text give sense
  (Tuscany succession, Lorraine, Orléans as brother-in-law of Lorraine, marriage with Mlle de Valois, Scotti's
  appointment "so out of proportion to his birth", "the daughter of the Regent", Stair, "insinuate into the
  King's mind", "jealousy", "our common master"). Weak places: 4r.L10 "[0_] efic[33]"; 4v.L10-13 "[160]",
  "a[...]"; 5r.L01-06 ("[91] [170]", "[200] [la quale] [78]", "[16_]"); 5v.L12-15 ("[fisi]", "[sip33]",
  "[?] figura", "[57]"); 6r.L10 (Re omitted, see above); 6v.L04-05 ("[264 ...]", "[126]", "[60_]"); 6v.L09 "[52]
  [208]". 4r-5r is gloss-backed and circular for key evidence (fine for a transcription job, but say so).
  The English is a fair rendering of what is read; "[prince?]" for 160 and "[country]" are guesses and are marked.
- `reading_1719_1027.md`: **C** as a reading. Phrases with sense exist (la successione della Toscana; Lorena;
  nella persona di [Orléans]; Monferrato; in mancanza delle linee viventi; Mademoiselle di Valois; la [?] madre;
  seminar confusione), and they show the key works on a second letter. But the continuous text is a string of
  fragments joined by ellipses; many lines do not read: 12r.L14-15 "[miso] [adosati]", 12v.L05 "[fmrlaad]",
  12v.L07 "[danc]", 12v.L14 "[vocа]", 13r.L02 "far [li] sper[a li]", 13r.L03 "[e vo]", 13r.L06 "[pop]",
  13r.L09 "[n il] turn[o]", 13v.L04 "conti la [n] di be[ivi] ... d", 13v.L08 "lo spar[ave] li le e se-". Present
  it as "read in part, fragmentary", not as a reading. The "Queen mother" and "Duchess of Berry" in NOTES are
  conjectures from "la [17]i madre" and "be[ivi]" and must be worded as such.
- **Encoding defect:** 12v.L14 `[vocа]` contains a Cyrillic "а" (U+0430). Replace with Latin "a".

## 6. Vendor names and local paths

No AI vendor or model name in any file. **Local paths found** (must go): `scripts/check_marks.py:16`,
`scripts/merge_1719.py:9`, `scripts/stats.py:4`, `scripts/test_1722.py:8` (folder path under the user's home),
and `scripts/solve_1722.py:14` (path to the main cyphersolver checkout). Use paths relative to `__file__`.
NOTES.md mentions no archive work of WAINUT's own; it names the Archivio di Stato di Modena only as a place where a
key may survive, which is fine.

## 7. Prior art

Dan's `catalogue.json` (main checkout, read only) has **no entry** for Selvatico, Riva or these 1719 letters; the
number 1568 refers to the leads list, not a catalogue id. So selvatico1719 would be a new, non-catalogue target,
and its PR must say plainly that lead 1568 (the 1722 letters) stays unsolved. One web search ("Selvatico Estense
lettere Giuseppe Riva 1719 Parigi cifra Mademoiselle de Valois Autografoteca Campori") found no edition or
decipherment of these letters. The marriage negotiation itself is well known history, so the content is new
evidence on a known story, not a new story.

## Must fix before a PR

1. Remove local paths from the five scripts (relative to `__file__`).
2. Make decrypt/check_marks split dotted tokens and flag any unparsable token; regenerate decryption and counts;
   restore the missing "Re" in 6r.L10.
3. Correct the transcription where settled: 5v.L11 `c25 3 1` (not `c23 31 1`), 6r.L09 `c23`, 6r.L15 `173`,
   6r.L10 `173`; check 6r.L02 `3_`. Then rerun and recount (the unmarked share will rise slightly).
4. Replace the Cyrillic "а" in reading_1719_1027.md (12v.L14).
5. Strip the BOM from decryption_1719.txt (regenerate with the script).
6. Script the held-out test against a corrected gloss file (5v-6v), and report the count split
   training / held-out / 27 Oct instead of one 61%.
7. Present the 27 Oct letter as fragmentary; mark Queen mother / Duchess of Berry as conjectures.
8. Frame as a new target, not catalogue 1568; never commit scans, `__pycache__` or `work/` images.
