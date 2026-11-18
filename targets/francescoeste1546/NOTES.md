# Francesco d'Este to Ferrante Gonzaga, 13 Apr 1546 (new find, Biblioteca Estense; not in the catalogue)

Status: in progress. Not yet written up: no site page or README row. Read in part, with escalation steps still open (see Remaining gaps and Escalation). The status below is the contributor's.

Status, 3 Nov 2026: **read in part. c. 42r is read through the contemporary interlinear decipherment; cc. 42v-43r (40
cipher lines) are not transcribed, only a key test was run on them.** This is a transcription job, not a break: a
contemporary decipherment is written above every cipher line.

| Document | Cipher | Words | Read as sense | Sign for sign, no mark | Unread groups | Status |
|---|---|---|---|---|---|---|
| c. 42r | 14 lines, 476 signs | 85 | 85 of 97 word slots (87.6%) | 57 of 97 (58.8%) | 12 | read in part |
| cc. 42v-43r | 40 lines, about 1,370 signs | | | | | not transcribed; key tested |
| cc. 43v-45v | not examined | | | | | not examined |

c. 42r carries about a quarter of the letter's cipher (476 of about 1,830 signs). Its 85 words of decipherment are all
carried by signs; 57 match the signs unit by unit with no mark, 28 have at least one marked unit (a value seen only once on
the page, a letter with no sign, or a doubtful sign). 12 groups of signs have no decipherment above them (11 until the
check of 14 Nov 2026, below); all but part of
the first stand under the writer's superscript digits 6 or 4. Counting each as an unread word slot, 85 of 97 read as sense
(87.6%), under the 95% bar. `scripts/check_marks.py` prints 87 words because "risoluto" and "senza" run over a line end,
and 15 unread runs because it also counts four single raised o's after omega inside words (a writing convention, see
below).

Contributed by WAINUT; the work was done with AI language-model agents viewing the images. No human palaeographer has
checked it.

## Document

- Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera E, Este (d'), Francesco (1516-1578),
  cc. 42-45 (8 canvases). Record: "Lettera parzialmente cifrata (ma decifrata in interlinea)."
- IIIF manifest: https://edl-jarvis.cultura.gov.it/meta/iiif/f97ba5b9-2720-411a-9c3a-04e1e5a61bab/manifest
  (CC BY-NC-SA; no images in this folder).
- 54 lines carry cipher: c. 42r (14, from "Sapera dunq" on), 42v (21) and 43r (19), about 1,830 signs. Some lines mix
  clear words and cipher. 43v-45v were not examined.
- Not in the catalogue. Entry 1564 mentions this letter only as a "deciphered sibling" in the same fonds.

## The system

A homophonic letter substitution with about 45 invented signs, many shaped like Latin or Greek letters (33 distinct on
c. 42r). Most letters have two or more signs (i: x, w; s: `n o`, []; a: q, L; d: pi, e; r: `o v`, L). No word division.
Small digits 6 and 4 written above some signs are the writer's; the decipherer copies them instead of a word. Their meaning
is open (code markers or nulls). Sample values: q a, m o, `o +` e, 3 c, T l, `o v` r, 4 n, ps h, A t, pi d, [] s, 8 o,
y g, b t, x i/p. See `key_c42r.tsv`.

The key does not match the Ferrante keys tested: `targets/gonzaga1549/wainut` and `targets/ercole1544` (letter and syllable
systems with other sign sets), the Bresegno 1548 key (consonant + vowel-digit) and Marignano 1546 (letter-shaped signs,
other values: q, a, x, T differ).

## How the key was obtained

1. Sign inventory: an AI language-model agent named the shapes from a sample sheet, with no values (`scripts/inventory.py`,
   `validation/legend.md`).
2. Blind sign passes on tight bands that cut away most of the interlinear clear, with the legend only, no key and no clear.
   Passes A and B (two different AI language-model agents, whole lines, all three pages): `validation/passA.txt`,
   `passB.txt`. Pass C (c. 42r only, half lines at full size): `validation/passC_c0.txt`. A and B agree on 76% of signs.
3. c. 42r was settled by majority per aligned sign (`scripts/settle.py`, `validation/settle_log.tsv`,
   `validation/transcription_c42r_majority.txt`), then changed by eye on crops (`validation/adjudication_c42r.tsv`).
   **Correction:** an earlier version of these notes said every line had then been read by eye on full-size crops. That
   check was not effective. The independent verification (`VERIFY.md`) found a 4-sign group left out, five clear signs
   missing at the end of L11 and about 22 wrong signs (4.8%). They were corrected on enlarged crops on 3 Nov 2026
   (`validation/corrections_2026-11-03.tsv`, below).
4. The clear was read afterwards (`scripts/gloss.py`) and corrected by hand per line (`clear_c42r.txt`; words split across
   lines are put on the line of their signs: "ri|soluto" L02/L03, "sen|za" L11/L12).
5. Key: each line aligned with its clear by dynamic programming (a unit = one sign or a sign pair), P(letter | unit)
   re-estimated by hard EM (`scripts/learn.py`, `scripts/read42r.py`). Sign groups under the writer's 6/4 digits with no
   gloss above them, located on the image (`validation/unglossed_c42r.tsv`: L05, L06, L09, L11), may only be left unread
   by that alignment. This uses the image, not the clear.
6. In this hand raised o + v (r), o + + (e), n + raised o (s) and n + raised c (m) are written as one sign each; they are
   transcribed as two names and read as one unit. Omega often has a raised loop after it, transcribed `w o`; the loop is
   left unread.

## Held-out tests

- **Inside c. 42r.** Key learned on L00-L06 and frozen, applied to L07-L13 (215 clear letters) with the plain alignment
  (the 6/4 groups not used): the frozen key's top value matches 176 letters (81.9%). 500 shuffled tables: mean 24.2%,
  max 39.5%. Before the corrections it was 160 of 212 (75.5%; shuffled mean 23.0%, max 32.1%).
- **On 42v-43r.** Key learned on c. 42r (pass A, before the corrections) and frozen (`key_frozen.tsv`), applied to 42v and
  43r (1,151 clear letters of a machine read of the gloss): 73.1% with pass A, 67.2% with pass B; 200 shuffled tables mean
  28%, max 40% (`scripts/heldout.py`). The gloss read and the passes of 42v-43r were not checked, so this shows only that
  the key generalises. It is not a reading of 42v-43r.

## Independent verification and what changed

`VERIFY.md` is the report of an AI reader who took no part in the solving. It transcribed the whole cipher of c. 42r blind
(483 sign names, 15 lines, including all of L07-L13), read the gloss itself, rebuilt the files and tested `check_marks.py`.
Its verdict was "fix", status read in part. Its figures are for the files before the fixes below.

Applied on 3 Nov 2026, each sign change checked on enlarged full-size crops (`validation/corrections_2026-11-03.tsv`):

- Transcription: opening group `n o pi w` added (end of the line "Sapera dunq", now at the start of c0L00); L00 `T e m`;
  L01 `8 e 4 o +`; L03 two raised o's restored (`o v`); L05 `T 4`; L06 last sign `Yx` (a goblet/Y with a diagonal stroke,
  new name), not q; L07 extra r removed; L08 `3 ps o +` in "che"; L09 a 4 added in "beneficio"; L10 raised o restored in
  "consultare", and "Spagna" as `[] x q y 4 m`; L11 `n o o + 4` added at the end; L12 two raised o's restored and
  `x 4 q o v` in "determinare"; L13 `e L?` for "da" and `T o + w` for "lei".
- Gloss: "de" (not "do", L06), "volerne" (not "volere", L12), "tutto" (not "mai", L13; the gloss word has ascenders and
  five letters, and the signs `A a r b m` give t-u-t-t-o). Clear context in the reading: "me ne allegro", "E che ben mi
  dispiace", "non si restarà".
- Reading rebuilt by `scripts/read42r.py`; `scripts/check_marks.py` now also fails if the letters of a reading line differ
  from the decipherment of that line (a deleted no-sign mark now fails, exit 1).
- The lines through `q U x n q` (L02) and `L ps 4 m m` (L04) are now described as possibly deletions or abbreviation bars.

Where we differ from the verification, checked on the image:

- **L10 "Spagna".** The verification gives `[] x q ps 4 m`. We agree there is one sign and no `o v`, but the sign has a
  descender, the form of y (g) seen in "Granuela" and "signoria", not the flat-bottomed psi of "che". We name it y.
- **L08 "signoria".** Left open by the verification (`+` or 4, leaning 4). At 6x it is a closed 4; now `y 4 m`.
- **L13 second "da".** The first sign is e; the second may be L or the u-shaped a. Kept as `L?`, marked doubtful.
- **L00 "Sicilia"** (a possible v after omega): read as omega's trailing loop, not a sign. **L02** last sign of the barred
  group: q (straight descender).

After the fixes the marked reading is aligned in L06 (de), L08 (che), L09 (beneficio), L11 (venendo) and L13 (da, lei,
tutto). Still awkward: "Spagna" in L10 (`4 m` taken as one unit for "na") and "volerne determinare" in L12 (the
alignment gives one o + to "de-" and marks a missing e in "volerne"). Both are marked, not hidden.

## Independent verification by Brice Dudout (PR #570, 14 Nov 2026)

Brice Dudout (`VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) decoded `transcription_c42r.txt` from the key
files alone: the top values give 320 of the 381 letters of the interlinear decipherment in order with `key_c42r.tsv`
(0.840), 313 with `key.tsv` pass A (0.822), 302 with pass B (0.793). No key value changes. Re-run here: the same figures.

Two points follow from the check, both confirmed here:

- **12 unread groups, not 11.** `reading_c42r.md` has 12 `[?]` in the cipher passages; NOTES, the profile and
  `scripts/check_marks.py` counted 11, because the script counts unglossed runs per line and L11 has two of them: one at
  the head of the line and one before the cipher of "venendo", with the clear words "me ne allegro però, perchè fra
  tanto" between them. Seen here on the Estense image of c. 42r (the line is legible at 1,000 px wide: signs under the
  digits 6 4 at the line head, clear words, then more signs under 6 4). The count is therefore 85 of 97 word slots,
  **0.876** (was 0.885). `check_marks.py` is left as it is and still prints 11 for this reason.
- **The 0.969 of `research/reading_audit/v10_relabel.py` is not a read share of the cipher.** The reading file has no
  `## Reading` heading, so that measure counts the preamble, the notes and the clear text of the letter (441 words).
  On the cipher passages alone it gives 90 words and 12 holes, 0.882. The class stays read in part.

Not checked here: any other sign on the image; cc. 42v-43r.

## Remaining gaps

- cc. 42v and 43r (40 cipher lines, about 1,370 signs): transcription not settled. Only the two model passes exist.
- c. 42r: 28 words carry a marked unit, most values seen only once on this page (42v-43r would test them) or letters the
  decipherer wrote in abbreviations. One sign is doubtful (L13).
- The writer's 6 and 4 digits: not understood. 12 groups stand under them unread (two of them on L11).
- The gloss read is a model read corrected by hand at word level; the clear text of the letter around the cipher is a
  first transcription.
- 43v-45v were not examined. No human has checked any sign.

## Content (from the interlinear decipherment)

Francesco reports, after the departure of "Natale", that the Emperor will not deal with the affairs of Sicily (about which
Francesco had written of his own interest after the death of the Marchese del Vasto, 31 Mar 1546) until the consultation in
Spain, though neither he nor Granvelle has told him Francesco's mind. Granvelle has promised to do all he can for him.
Francesco regrets that the matter goes to Spain but is glad of it, because meanwhile Ferrante may come, without whom the
Emperor will decide nothing, and then he expects everything from Ferrante. 42v-43r (not transcribed) name, among others,
the Conte Francesco da Landriano, the governorship of the Spanish infantry for the new Marchese del Vasto, the Prince of
Sulmona, Don Raymondo de Cardona and the Duke of Alba (from the machine read of the gloss, unverified).

## Prior art

Checked 3 Nov 2026: the catalogue, leads, targets and research notes in this repository and the open PRs. Only the pointer
in entry 1564 was found. Two web searches ("Francesco d'Este" "Ferrante Gonzaga" 1546 cifra, with Granvela and "marchese
del Vasto"): no edition or decipherment of this letter. Gonzaga correspondence editions were not opened.

## Files

- c. 42r: `transcription_c42r.txt`, `clear_c42r.txt` (the decipherment per line), `key_c42r.tsv`, `decryption_c42r.txt`,
  `reading_marked_c42r.txt`, `reading_c42r.md` (Italian), `translation_c42r.md` (English).
- `key.tsv`: key learned from passes A and B over all three pages (not settled). `key_frozen.tsv`: the c. 42r key frozen
  for the 42v-43r test (pass A).
- `scripts/`: fetch.py, lines.py, bands.py (images); inventory.py, pass_blind.py, pass_blind_prompt.py, pass_c.py,
  gloss.py (agent passes; `agent.py` is a placeholder for the API client, which is not included); settle.py, learn.py,
  heldout.py, read42r.py, check_marks.py (standard library).
- `validation/`: legend.md, passes, settle and adjudication logs, gloss_raw.txt, key_learn*.tsv, key_frozen_c0_*.tsv,
  heldout_c42r.txt, check_marks_output.txt, unglossed_c42r.tsv, corrections_2026-11-03.tsv.
- `VERIFY.md`: the independent verification, unchanged except for two phrases neutralised under our house rules: a
  provider and model name in section 6, and a remark in section 6 not about this target.

Rerun: `python scripts/read42r.py` then `python scripts/check_marks.py`, from this folder.
