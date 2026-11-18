# Gian Giacomo Medici, marquis of Marignano, to Ferrante Gonzaga, Ratisbon, 12 June 1546 (Biblioteca Estense; not in the catalogue)

Status: read (3 Nov 2026), the cipher passage of c. 13r, read from the contemporary clear translation on c. 14r, with a
key rebuilt from it. This is a **transcription job, not a break**: the contemporary translation covers the whole cipher
passage. Contributed by WAINUT; the work was done with AI language-model agents viewing the images. No human palaeographer has
checked it. Not in the catalogue: a new find from a WAINUT sweep of online archive records.

Word counts (`scripts/check_marks.py`, output `validation/check_marks_output.txt`): 62 words in cipher. 55 come verbatim
from the signs; 7 carry a marked repair (four double letters restored; two doubtful signs, in *di [?l]a* and *aviso [?a]*;
one sign read against its value in *pu{b}lica*). All 62 read as sense (100%); by the README read bar the three words on a
doubtful or contradicted sign are holes, so the read share is 59 of 62 (95.2%), above the 95% bar; the same 59 have no
departure from the signs other than the scribe's single-written double letters (the independent check gives 60, 96.8%:
it counted *di la* before its *l* was marked doubtful; see Corrections). A further seven clear words stand in
the passage (*Qua, Hora, meglio, L'aparechio, -cular, questa, cosa*) and are not counted. The code *eti* (V. Ecc.a) is
counted three times as a word.

## Document

- Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera M, Medici (de'), Gian Giacomo (1497-1556),
  cc. 13-16 (8 canvases; canvases 5-8 repeat cc. 14v-16v). Record: "La c. 14 contiene traduzione della porzione cifrata
  della lettera."
- IIIF manifest: https://edl-jarvis.cultura.gov.it/meta/iiif/b7483cb6-6dd0-4523-a71d-2fbccbe6d10d/manifest
  (CC BY-NC-SA; images not stored in git).
- c. 13r: the letter. After the clear opening, 10 lines of cipher (306 signs and groups) run from "Qua ..." to "... n a o :".
  The letter then goes on in clear ("Mando a Milano e Genova per far provisione d'homini per l'artegliaria ..."). c. 13v:
  "Da Ratisbona alli xii di Giugno M.D.XLVI", "Humil servitor"; the address to Ferrante and the dorse "Il M.se di Marignano" are
  on c. 14v.
- c. 14r, top: the clear translation of the cipher, in a small hand (`clear_c14r.txt`). c. 14r, bottom: a clear
  postscript about Sebastiano de Perego (not part of this job).

## The system

A letter substitution with homophones, written in signs that look like Latin letters (n, u, c, a, h, k, r, t, v, L, &)
and others (a double-crossed sign `H`, a daggered 3 `T`, a delta `D`, a hooked d `j`, x-like signs with a dot `X`, a tail
`Z` or a loop `8`). The sign names describe shapes, not values: `n` is l, `a` is r, `h` is m, `r` is o, `c` is c. Words are
divided by commas and slashes. Further:

- vowels have two or more signs: a = `j` `8`; e = `Z` `e`; o = `H` `r`; i = `&` `w` (and `e`);
- a small sigma-shaped sign `s` is a null: *guer[s]a*, *al[s]e*, *li[s]*, *provisi[s]one*;
- four groups of dotted vowels (`{onu}`, `{nao}`, `{nou}`, `{anu}`) stand apart at sentence breaks and at the end: nulls
  or stops;
- `eti`, written like a clear word, is the code for *V. Ecc.a* (three times);
- clear words are mixed in where the writer did not bother to encipher (*Qua*, *Hora*, *meglio*, *L'aparechio*,
  *questa cosa*, and *-cular* after the enciphered *parti-*);
- double letters are written once.

Several sign names carry two values (`g` s|q, `e` e|i, `+` g|h, `f` r|t, `q` t|f, `N` f|c, `o` s|m; and `u` u|v). Most are
probably two similar shapes merged under one name in the transcription; this is flagged in `key.tsv` ("shape?") and not
settled on the image. (`9` s|q is gone: the one `9` read q, in *quale*, is the long-descender `g`; see Corrections.)
In the reading 29 letters fall on such a name, plus 11 on u|v: 40 of 239 sign units (16.7%; 12.1% without u|v). The list
is printed by `scripts/check_marks.py`. Each of these letters was picked to match the word of the clear translation on
c. 14r; none is a free choice by the reader. But the pick is checked by eye against c. 14r, not by the script.

## Transcription: two passes before alignment

1. Pass 1 (`validation/pass1.txt`): eye copy by sign names from full-size line strips. **Not blind**: this reader had seen
   c. 14r and had tried a first alignment on 3 Nov before copying. Signs were copied by shape, not moved toward the
   translation.
2. Pass 2 (`scripts/pass2_blind.py`, `validation/pass2_raw.txt`): a separate run by AI language-model agents on the same
   lines, given a legend of shapes and names only (no values, no translation, no key). The script's call to the model
   client is left as a stub: the client is not part of this folder.
3. The passes differ on 53 of 306 units (17%). About half of these are naming, not shape: the hooked-d sign was named `h`
   or `D` by pass 2, and clear words were copied as signs. Each difference was settled on full-size crops
   (`scans/strips/zA.png`, `zB.png`; log `validation/adjudication.tsv`). Pass 2 found two errors of pass 1 (an L that is
   not there; the sigma-shaped sign, which pass 1 had merged with long s). Pass 1 found that pass 2 had dropped three signs.
   Three signs stay doubtful (`l?` M01, `j'?` M07, `o?` M09).
4. Independent blind check (`VERIFY.md`, 3 Nov): the whole cipher, about 306 units, copied by shape before any solver
   file was opened. 9 raw differences (2.9%); after full-size crops 6 were the checker's errors, 1 ours (M08 *quale*,
   corrected), 2 open (`f` or sigma `s` in *actende* and *auctore*; the value is the same either way).

## Key, freeze and held-out test

The key was built from the pairs on lines M01-M06 (cipher words against c. 14r) and frozen (rows `frozen` in `key.tsv`).
Lines M07-M10 were then aligned with the frozen table as the held-out stretch.

- Held-out: 82 sign units. The frozen key agrees with the reading on 75 (91.5%; 74, 90.2%, before *quale* was corrected
  from `9` to `g`). Of the other 7, six are signs that do not occur on M01-M06 (`j'`, `F`, `N` twice, `1`, `{anu}`). One is
  a second value for a sign name (`q` gives t on M01 and f on M07), which is the merged-shape question above.
- Shuffled tables: with the frozen letter values permuted at random among the sign names (1000 runs; nulls and `eti`
  fixed), the same stretch scores a mean of 8.1/82, 95th percentile 18, maximum 28. The frozen key's 75 is far outside that.
- Limits of this test. It is scored against our own reading of M07-M10, and that reading was itself aligned to c. 14r, so
  it is only partly independent. A unit counts as agreeing when the reading's letter is any of the frozen values of its
  sign name, so the two-valued names help it. For a transcription job with a full contemporary translation the stronger
  control is that every word matches c. 14r.

## Reading

`reading_c13r.md` (Italian), `translation_c13r.md` (English), `reading_marked_c13r.txt` (line by line with marks).
`scripts/check_marks.py` rebuilds the decryption (`scripts/decode.py`, `decryption_c13r.txt`) from `transcription_c13r.txt`
and `key.tsv`, walks the reading unit by unit (nulls must be consumed explicitly), and exits 1 on any unmarked departure.
It passes (`validation/check_marks_output.txt`).

**What the checker cannot see.** A letter passes when it is *any* of the values of its sign name. For the two-valued
names (`g e + f q N o`, and `u` u|v) it cannot tell whether the right value was picked. The independent check showed this:
*primo* changed to *priso* and *si* changed to *qi* both pass with exit 0. Real departures (*luterini*, *cosa*, *tenor*)
fail. The checker now prints every two-valued pick so that a reader can check them against c. 14r; it does not check them
itself. Splitting the merged shapes on the image would close this; it was not done by the contributor. Brice Dudout did it on 14 Nov 2026
for six of the seven names (next section); `key.tsv` and the transcription still use the merged names.

Summary: from the imperial court at Ratisbon, Marignano tells Ferrante Gonzaga, governor of Milan, that the war against
the Lutherans is decided. Provisions are being made, and he has more than his share in them. The preparation is great,
and he will send a detailed report by the next courier. The court professes to keep the matter secret, though it is
already public; Ferrante is not to name Marignano as his source.

Historical context: in June 1546 Charles V, at the Diet of Regensburg, was preparing war on the Schmalkaldic League
(the treaty with Paul III is dated 26 June; the war began in July). Marignano commanded for the emperor in that
campaign. The letter is one witness to how the decision travelled before it was announced. This is general knowledge,
not checked against literature here.

## Cipher against the contemporary translation

The translation on c. 14r follows the cipher closely but normalises the spelling: *della* for *di la*, *grande* for
*grando*, *autore* for *auctore*; it abbreviates *primo* as "p.o". No content differs.

## Corrections after the independent check (3 Nov 2026)

- M08 *quale*: the first sign was copied `9`; on the full-size crop it is the long-descender `g` of *quanto* (M03), not the
  short-stemmed `9` of *si* and *resolta*. Renamed `g`; the key row `9 = q` is removed. No plaintext letter changes.
- M01: the looped `l` of *di la* was listed as doubtful here and in `validation/adjudication.tsv` but written plain `l` in
  the transcription. Now `l?` in the transcription and `{?l}` in the reading. Count: 55 verbatim, 7 with a marked repair
  (was 56 and 6).
- English translation: the sentence that named "Your Excellency" twice is corrected; *si cognoscerà* is now taken as
  impersonal ("it will be better known").
- `scripts/pass2_blind.py`: the local path and the model-client call are removed (stub); `__pycache__` deleted.
- `scripts/check_marks.py`: prints the two-valued picks and states the held-out test's basis.

## Independent verification by Brice Dudout (PR #570, 14 Nov 2026)

Brice Dudout (`VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) wrote a decoder that reads only `key.tsv`,
`transcription_c13r.txt` and `reading_marked_c13r.txt`: 239 sign units, 238 give a key value of their sign name; the
exception is the marked *pu{b}lica*. Re-run here: the same.

He then looked at the two-valued sign names on the Estense image of c. 13r and found that six of the seven are two
different shapes, one value each (table in his file): `+` g/h, `g` s/q, `o` s/m, `N` f/c, `f` r/t, `e` e/i. `q` (t/f)
may be two shapes; `u`/`v` was not looked at. Checked here on full-size crops of M01-M02 and M07-M09 (Estense IIIF,
regions of 1,000 px): the epsilon (e: *luterani*, *ale*) and the round e (i: *provisione*) are different signs; the small
joined o of *pu?lica* is the s shape and the tall dark oval of *me* the m shape; the g of *provisione* has a closed
loop and that of *quale* a long descender; the cross of *già* is plain. The other rows of his table were not re-read
here. The split is not written into `key.tsv` or the transcription: that is a renaming job still to do, and it would let
`scripts/check_marks.py` test the 29 letters that now rest on a pick.

Consequences applied:

- **M08 reads *tener*, not *tenir*.** The fourth sign is the epsilon (seen here on the crop), which is e in the seven
  other places; the round e is the i sign. The reading had taken *tenir* from c. 14r. `reading_c13r.md` and
  `reading_marked_c13r.txt` now have *tener*; the sense and the counts do not change.
- **Read share recorded as 0.952, not 1.0.** By the README read bar a word on a doubtful sign or read against its sign is
  a hole: *di [?l]a*, *aviso [?a]* and *pu{b}lica* are three of the 62 cipher words, so 59 of 62. The class stays read.
  (`research/reading_audit/v10_relabel.py` gives 0.977 because it counts the whole file, notes included.)

## Remaining gaps

Unread or unsettled pieces of the cipher (as in profile.json outcome.gaps):

- Doubtful signs `l?` (M01, *di la*), `j'?` (M07, *a*), `o?` (M09, *publica*, read against the sign's value) - blocker:
  illegible; single occurrences, every word confirmed by c. 14r.
- `f` or sigma `s` in *actende* (M02) and *auctore* (M10) - blocker: illegible; open after the independent check, same
  value either way. Brice Dudout (14 Nov 2026) reads it as neither: one shape in both words, a bowl into a hooked
  descender, a third sign for t. Not re-read here; not checked by a palaeographer.
- The dotted-vowel groups `{onu} {nao} {nou} {anu}` - blocker: too-short; null or stop marks, not proved either way.

Not unread pieces, but open (profile.json outcome.notes):

- Merged shapes: seven sign names carry two values (and u|v); 29 letters of the reading (plus 11 u|v) rest on such a pick,
  fixed by c. 14r and not by the checker. Not split on the image (e.g. the two `g` shapes, the two epsilons). No word
  depends on the split: each is fixed by its pair on c. 14r.
- One letter only: there is no second text in this key to test it outside its own pairs.
- The clear rest of the letter (c. 13r-v) and the postscript on c. 14r were not transcribed; not part of this job.
- Prior art: one web search only.

## Escalation done

Imperial keys held in the repo tested first (below); sign-first transcription in two passes, one blind; adjudication on
full-size crops; key frozen on six lines and tested on four, with a shuffled-table control; `check_marks.py`; one prior-art
search.

## Imperial keys tested and ruled out

- `targets/gonzaga1549/wainut` (Charles V and Prince Philip to Ferrante): a Spanish syllabary of consonant bases with vowel marks.
  On these pairs it does not fit (its `a` is m and `u` is c; here `a` is r and `u` is u). Ruled out.
- `targets/ercole1544` (Ercole Gonzaga to Ferrante): a reciprocal half-alphabet of Latin letters (a<->n, c<->p ...). Here
  `c` is c and `n` is l. Ruled out.

## Prior art

Checked 3 Nov 2026: Dan Bourdeau's repo (origin/main: catalogue, leads, targets, research notes) and open PRs for
Marignano, Medeghino, Gian Giacomo Medici: no target or lead for this letter. One web search (Marignano, Ferrante Gonzaga,
Ratisbona, 12 June 1546, cifra): no edition or decipherment of this letter found.

## Files

- `transcription_c13r.txt`: the cipher sign by sign (sign names describe shapes, not values).
- `key.tsv` (full, with `frozen` and `later` rows), `key_frozen.tsv` (the rows frozen from M01-M06).
- `decryption_c13r.txt`: rebuilt by `scripts/decode.py`.
- `reading_marked_c13r.txt` (line by line, every departure marked), `reading_c13r.md` (Italian), `translation_c13r.md`
  (English), `clear_c14r.txt` (the contemporary clear translation).
- `scripts/`: `decode.py` and `check_marks.py` (standard library); `fetch.py`, `mstrips.py`, `mzoom.py` (need the images and
  Pillow/numpy; a record of the method); `pass2_blind.py` (the blind second pass; the model client is a stub);
  `diffpasses.py`.
- `validation/`: `pass1.txt`, `pass2_raw.txt`, `adjudication.tsv`, `check_marks_output.txt`.
- `VERIFY.md`: the independent check of 3 Nov 2026, unchanged except that a local folder name and one phrase were
  redacted. Its counts predate the corrections above (it has 56 verbatim, 74/82 held-out).

No images are in the folder. Fetch them from the IIIF manifest above with `scripts/fetch.py`.
