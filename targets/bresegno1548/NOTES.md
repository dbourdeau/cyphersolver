# bresegno1548: Bernardo Bresegno to Ferrante Gonzaga, Rome, 5 Oct 1548 (catalogue 1563, first letter)

Status: in progress. Not yet written up: no site page or README row. Read in part, with escalation steps still open (see Remaining gaps and Escalation). The status below is the contributor's.

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera B, Brezeno (abate), cc. 15-16, 22. Cipher on
c. 15r (24 lines), contemporary decipherment bound in as c. 22r ("il decifrato del n. 8").

Status, 3 Nov 2026: **read in part, as a transcription job.** c. 22r already deciphers the whole cipher, so this is
not a break. The new work is a sign-first transcription, the key rebuilt from the pairs with a held-out test, and a
reading checked against the signs. 204 of 250 words (81.6%) come verbatim from the signs; the full text is known only
from c. 22r. An earlier version of this note said "read"; the independent check (`VERIFY.md`) downgraded it, and that
is right: on the signs the letter is under the 95% bar. The second letter of catalogue 1563 (Juan Manrique, 1554) uses
a different key, is not solved and is not part of this target.

Contributed by WAINUT. The work was done with AI language-model agents.

## Word count against the 95% rule

| measure | count |
|---|---|
| words in the cipher passage (c. 22r; a code group counts as one) | 250 |
| words that read as sense | 250 (100%), only because c. 22r gives them |
| words verbatim from the signs | 204 (81.6%) |
| words with at least one marked departure | 46 |

Read in part. On the signs alone the reading is under 95%. The counts come from `scripts/reading.py check`
(`scripts/check_marks.py` runs the same check). Before the independent check the count was 196 (78.4%). The two sign
fixes the check settled (L02 `d^5`, L19 `#^2 7^2`) give 198 (79.2%). Four digit placements settled on crops after the
check (L02 twice, L03, L05, L17) give the other six words. They were looked for where the reading had marks, so they
are not independent of c. 22r (see Transcription).

## Collision and prior art (3 Nov 2026)

- Dan's repo at origin/main d803a1d8d: no target for 1563; `gonzaga1549/wainut/NOTES_ferrante1549.md` (then `ferrante1549/NOTES.md`) lists 1563 as "not tested". Open
  PRs #227, #216, #201: none about these letters.
- Two web searches (Bresegno/Brezeno, Ferrante Gonzaga 1548, Morone, cipher; Campori) found no edition or study. The independent check made one more (Fierravante/Fieravante, 1548, Bologna, Tor di
  Nona, Ferrante Gonzaga, Morone) and found none. The
  catalogue's vetting of 29 Oct found none either.

## The system

Consonant signs with a vowel number written above them, plus bare signs, doubles and a few code groups:

- vowel numbers: 2 a, 3 e, 4 i, 5 o, 6 u (`d^3` de, `C^4` ti, `ms^2` la);
- consonant bases: `o` c, `L` n, `#` s, `s` r, `d` d, `C` t, `ms` l, `q` h (`q^3` ze, `q^4` zi), `O` m, `a` p, `7` u/v,
  `x` b, `h` g, `hs` ll, `rs`/`Lx` f, `n` j, `D` y;
- bare signs: `2` and `3` a, `4` and `o` e (bare `o` is also c before h), `a` o (p before r or l, a rule in the
  decoder), `7` and `T` u, `+` q, `D` y; a bare consonant base is the consonant alone;
- doubles `{bar}` ss, `{bir}` rr, `{barn}` ssi;
- code: `Os` V. Ex., `{Per}` su Mag., `{Ar}` Papa, `{mi}` Cardenal, `{Gra}` Bolona, `{Bran}` Duque de Florencia.

It is not the Imperial syllabary of `gonzaga1549 (WAINUT's table, formerly ferrante1549)` (dots and bars over a base for the vowel) and not the table of PR
#216; same family of idea, different marks. `cifuentes1534` (Charles V's Rome correspondence, base signs with
superscript digits 1-10) describes a similar system; I did not compare the two.

## Key, held-out test

- `SIGN_CONVENTIONS.md` fixed the sign names before any decoding.
- Pass 2 is blind (`transcription_c15r_pass2.txt`, about 708 signs): a separate agent with no key, no c. 22r, told to
  ignore the interlinear glosses. Pass 1 (`work/pass1_L01_06.txt`, L01-L06) was made before pass 2 was opened. Raw
  agreement on L01-L06: 143 of 168 signs (85.1%).
- `scripts/align_em.py` aligned pass 2 L01-L16 with c. 22r up to "entonces" (segmental EM, 0-4 letters per sign).
  `key_frozen.tsv` was written from that table and frozen.
- **Held-out:** L17-L24, pass 2 signs, frozen key, no later values: 0.869 of 367 clear letters matched in order, 0.826
  in runs of 4+. 200 shuffled tables: best 0.327 and 0.093 (`scripts/heldout.py`, `work/heldout_pass2.txt`).
- **The held-out passage was not fully unseen.** An alignment over all 24 lines, `work/p2_all_pairs.tsv` and
  `work/p2_all_table.tsv` (written 18:34), was made before the L01-L16 tables and `key_frozen.tsv` (18:41). The frozen
  rows cite only L01-L16 counts, but whoever froze the key had already seen held-out pairs. This note did not say so
  before the independent check.
- Independent replication: the verifier's own blind transcription of L19-L24, run through `key_frozen.tsv` against
  c. 22r, gives 0.872 in order and 0.843 in runs (best shuffled table 0.343 and 0.077). That lowers the concern above.
- `key.tsv` = frozen key + code groups seen only after L16 (values from c. 22r) + the rule for bare `a`. **The bare-`a`
  rule (p before `s` or `ms`, otherwise o) is post hoc:** it was added after the freeze, from L13, L15 and L18, and L18
  is in the held-out passage. It raises the verbatim count.

## Transcription

`transcription_c15r.txt` is pass 2 with the changes logged at its foot. Every pass 1 / pass 2 disagreement on L01-L06
that changes letters was settled on 1.5x crops of the full-size scan:

- L01 `o^5?` (digit visible; pass 2 had none);
- L02 `Lx` kept (bar across the stem visible);
- L03 `4?` kept doubtful (pass 1 `+`; the shape is between the two);
- L04 `#^6` (two 6s visible); blot `o?` doubtful (pass 1 `3`); `C` bare: the 4 over it is in the glossator's ink;
- L05 `n`, `h^6` (pass 1), not pass 2's `h`, `d^6`;
- L06 `q` bare (the 2 beside it is the glossator's), `a^6` (pass 1); `ms^3?`, `s^5?`, `ms^2?` doubtful: those digits sit in
  the gloss line and may be the glossator's.

An earlier version of this note said that the other disagreements "only move a superscript between neighbours
(`s^5 L` / `s L^5`), which gives the same letters". **That was wrong:** `s^5 L` gives "ron", `s L^5` gives "rno". After
the independent check they were settled on 1.6x-2x crops (log at the foot of `transcription_c15r.txt`):

- L02 `d^3` -> `d^5`: a single stroke with a top flag, this hand's 5 (the verifier's reading; the gloss above has
  "cu na do").
- L19 `# 7^22` -> `#^2 7^2`: each 2 stands right after its own sign (the verifier's reading). Held-out passage.
- L02 (twice), L03, L05, L17: `s L^5` -> `s^5 L`, `s L^2` -> `s^2 L`, `7 L^2` -> `7^2 L`. In each place the digit stands
  right after the first sign, over the upper left of the `L`. This hand writes a digit after its own sign, and an `L`'s
  own digit at its upper right (L19 `L^3`). Pass 1 had the same attachment at L02, L03 and L05. L17 is in the held-out
  passage. These six were looked for because the reading had marks there, and each fix agrees with c. 22r. The image
  supports them, but the search was not blind.
- L04 `L` -> `L^5?`: a small 5 in the cipher ink at the upper right of the `L`. Pass 1, pass 2 and the verifier did not
  settle it; kept doubtful. It changes a mark in "noche" but no word count.
- L18 `q^4 q^5` ("hizo", signs give zi ho): the verifier listed it as a possible attachment choice. It is not: the 4 and
  the 5 each stand at the upper right of their own `q`. Kept, and marked in the reading.

L07-L24 have the blind pass only. Apart from L17, L18 and L19 above, digit placement there was not checked on crops.

## Reading

`reading_c15r.md`: the Spanish (c. 22r, checked at full size, `clear_c22r.txt`) and a marked text in which every
departure of the signs is marked (`{a/e}` changed, `{+s}` no sign, `{-e}` sign value not read, `[V. Ex.]` code).
`scripts/reading.py check` rebuilds the decryption from the transcription and `key.tsv`, walks the marked text unit by
unit and exits 1 on any unmarked departure; removing one mark makes it fail. `decryption_c15r.txt` is the line-by-line
decryption; `scripts/diff_clear.py` lists the departures (59 places; 997 of 1055 clear units in order, 0.945).
`translation_c15r.md` is the English.

## Contents and context

Rome, 5 Oct 1548. Cardinal Giovanni Morone, legate of Bologna until July 1548 and so the former legate by October, told Bresegno that "Fierrauante" had been confronted
with his brother-in-law in the Castel Sant'Angelo; the brother-in-law was taken by night to Tor di Nona and put to the
rope. He confessed a plan of his own to hold the Palace (of Bologna, it seems) with 300 men until the Duke of Florence
sent help. He said he had put it to Ferrante, who would give no commission without the Emperor's leave but told him to
keep the talks going, and that he had made promises in Ferrante's name. Bresegno asks Ferrante to keep this to himself,
because Morone told it to the Pope in confidence. The year is the one after the murder of Pier Luigi Farnese (Sept
1547), with Ferrante holding Piacenza. "Fierrauante" is not identified here.

## Remaining gaps

- L07-L24 rest on one blind pass; no second reader there.
- Some superscript digits may be the contemporary decipherer's additions: he wrote digits in his lighter ink (seen over
  `C` in L04 and beside `q` in L06). Three L06 digits are marked doubtful for this; other lines were not checked for it.
- 46 words carry marks. Main kinds: bare `o` for c in ch/cl (8); `q^6` where the text has cho (3); single letters for
  doubles; a/o/i missing; L14 ink blot `[?]`; L05 struck `~o hs~`; L24 "a el el Papa" and three closing groups
  `{bor} 2 {bur}` with no counterpart in c. 22r (left as nulls).
- `{Gra}`, `{Bran}`, `{barn}`, `{mi}` occur once or twice each; their values rest on c. 22r.
- The two values of bare `o` (e, and c before h) and of bare `a` (o, and p before r/l) may be look-alike signs that the
  transcription does not separate.

## Independent check (`VERIFY.md`, 3 Nov 2026)

A separate AI language-model agent read the signs before it opened any solver file. Sample: L01-L04 and L19-L24, about
287 signs (L19-L24, about 175 signs, are in the held-out passage). Raw disagreement 16 of 287 (5.6%), 11 (3.8%) at sign
level. After settling on 2x-2.5x crops the solver was wrong at 1 place for certain (L02 `d^5`), 1 probably (L19
`#^2 7^2`), 1 unresolved (L04 `L^5`): 0.7-1.0%. Both fixes are applied, and L04 is kept doubtful. `decrypt.py` and
`reading.py check` reproduce the files. The check fails on an unmarked departure and on a stale mark. The held-out test
reproduces (0.869 vs 0.327 for the best shuffled table). The check's own blind L19-L24 through the frozen key gives
0.872. Verdict: downgrade from "read" to "read in part"; the reading and the translation graded A, the raw decryption B.
`VERIFY.md` is the check as written; it quotes the counts and the NOTES text from before these fixes.

## Images (not in git; CC BY-NC-SA)

- https://edl-jarvis.cultura.gov.it/meta/iiif/385ede35-d32a-416d-b7b1-5ca167bc241d/manifest (c. 15r canvas
  1, c. 22r canvas 5); record https://lodovico.medialibrary.it/media/schedadl.aspx?id=385ede35-d32a-416d-b7b1-5ca167bc241d
- Fetched full size as tiles of at most 1500x640 (`scripts/fetch_tiles.py`), one request a second, User-Agent
  WAINUT-research.

## Files

`SIGN_CONVENTIONS.md`; `transcription_c15r_pass2.txt` (blind), `transcription_c15r.txt` (final, with its change log);
`clear_c22r.txt`; `key_frozen.tsv`, `key.tsv`; `decryption_c15r.txt`; `reading_c15r.md`; `translation_c15r.md`;
`VERIFY.md` (the independent check, unchanged); scripts `decrypt.py`, `reading.py` and `check_marks.py` (mark check),
`diff_clear.py`, `heldout.py`, `align_em.py` (standard library), `fetch_tiles.py`, `line_strips.py` (need Pillow and
the images); `work/` (alignment tables, pass 1, held-out output).
