# marignano1546: independent verification, 3 Nov 2026

Verifier: a separate adversarial check. I did not edit any solver file. Scratch rebuilds were made outside the folder.

## Verdict

**fix**. The headline holds: the cipher passage of c. 13r is **read**. All 62 enciphered words read as sense against
the contemporary translation on c. 14r. Several things need fixing before this leaves WAINUT. Two of them are rule
breaks: a vendor and model name plus a local path in `scripts/pass2_blind.py`, and a `__pycache__` folder. There is
also a wrong sentence in the English translation, and the mark checker has a blind spot.

## 1. Blind transcription (whole cipher, about 306 signs, held-out lines M07-M10 included)

I copied all 10 cipher lines by shape from `scans/c13r_cipher.jpg` (full size, 4500 px wide) before I opened the
transcription, the decryption, the readings or the key. Before that I had read only the top of NOTES.md, which gives a
few sign values. I also read the gloss on c. 14r blind.

Raw disagreements with `transcription_c13r.txt`: 9 events in about 306 units (**2.9% raw**). I settled each one on a
full-size crop:

| line | solver | blind | settled |
|---|---|---|---|
| M01 *la* | `n j` | `n h` | solver right (hooked d `j`; I mixed it up with `h`) |
| M01 *luterani* | `... j X w` | `... j X 8 w` | solver right (I added a sign) |
| M02 *ale* | `j t s e` | `h t s e` | solver right |
| M02 *actende* | `c f` | `c s` (sigma) | unresolved. The sign is short with a loop, nearer the sigma `s` of *guer[s]a* than the long `f`. The value is the same either way (t, or c plus a null) |
| M06 *primo* | `v a & o H` | `v a & Lo H` | solver right (the `&` tail is not an L) |
| M07 *professione* | `T a H q Z dd o` | `T a H g s Z dd o` | solver right (one `q` sign, not two signs) |
| M08 *quale* | `9 u j n Z` | `g u j n Z` | **solver wrong on the shape**. It is the long-descender `g` of *quanto*, not the short `9` of *si*. The value q does not change. This also removes the second value "9 = q" |
| M09 | `o Z` | `H Z` | solver right (a round o) |
| M10 *auctore* | `c f` | `c s` | unresolved. A short long-s with a hook. The solver's `f` can be defended. The value does not change |

After settling: **1 solver error (0.3%), 2 open (0.7%), 6 errors on my side.** No settled or open point changes a
plaintext letter. Name-only differences (`W` and `w`, `l` and my "g-like loop") are not counted.

Gloss (c. 14r), read blind. I agree with `clear_c14r.txt` apart from one point where I was wrong. In the last line I
first read "no' mostri far di me"; the full-size crop gives "no' m(i) ne faccia me autore", as the solver has it. The
word after "Qua" in line 1 stays unclear (`[?sel]`; it may be "la"). The gloss covers the whole cipher.

Smaller transcription point: NOTES lists `l?` (M01) as doubtful, but `transcription_c13r.txt` writes plain `l` with no
`?`. So *la* is counted as verbatim, not as doubtful.

## 2. Rebuild

I copied the folder to scratch and ran `decode.py` and `check_marks.py`. Both exit 0. `decryption_c13r.txt` and
`check_marks_output.txt` match byte for byte.

Fault injection in `reading_marked_c13r.txt`:

- luterani → luterini: FAIL, exit 1 (correct)
- cossa → cosa: FAIL, exit 1 (correct)
- tenir → tenor: FAIL, exit 1 (correct)
- **primo → priso: passes, exit 0**. The sign `o` carries s|m.
- **si → qi: passes, exit 0**. The sign `9` carries s|q.

So the checker catches real departures. It cannot catch a wrong pick on any of the 8 sign names that carry two values
(9, g, e, +, f, q, N, o) or on u|v. Each such pick is made by the reader from context and goes unmarked. The checker is
weaker than NOTES suggests.

## 3. Held-out test

I reran it: 74/82 (90.2%), and the shuffled control gives mean 8.1, p95 18, max 28. The numbers match. It is **graded
against the solver's own reading** of M07-M10, not straight against the gloss. That reading was aligned to the gloss,
so the test is only partly independent. Two more limits:

- a unit counts as agreeing when the reading's letter is any of the frozen values, so the two-valued names help;
- a plain transcription job with a full gloss needs this test less. The real control is that every word matches c. 14r.

## 4. Counts and headline

I recounted the words: 62 cipher words. 56 have no mark. 6 have a marked repair: four double letters restored (*guerra*,
*alle*, *occulta*, *faccia*), one doubtful sign (*a* in "aviso a"), and one sign read against its value (*pu{b}lica*).

- Words with no departure other than the scribe's single-written double letters: 60/62 = 96.8%.
- Words read as sense: 62/62.
- Over 95% on either count: **read**.

Honest headline: "62 enciphered words, all read; 56 straight from the signs, 4 with a restored double letter, 1 on a
doubtful sign, 1 read against the sign's value (*publica*). Every word confirmed by the contemporary clear translation.
Transcription job, not a break."

Caveat: a few of the 56 depend on a two-valued sign name resolved from context, and one depends on a single-occurrence
`l`.

## 5. Grades of the reading files

- `reading_marked_c13r.txt`: **A**. It is consistent with the signs and passes the checker. Weak places: *la* rests on
  a single doubtful `l` that is not marked; the `{?a}` after *aviso*.
- `reading_c13r.md` (Italian): **A**. It reads as continuous sense and matches c. 14r word for word, apart from the
  scribe's spellings (*di la*, *grando*, *auctore*, *primo* for "p.o"). Weak places: *pu{b}lica*; "mi ne ... me
  auctore" is redundant but matches the gloss.
- `translation_c13r.md` (English): **B**. Weak places:
  1. "I will send Your Excellency a detailed report [?to] Your Excellency" repeats the addressee and is wrong. It should
     be "I will send a detailed report to Your Excellency [?to]".
  2. "Now Your Excellency will know it better" treats impersonal *si cognoscerà* as having V. Ecc.a for its subject.
     More likely: "Now it will be better known, Your Excellency." The sentence boundary before *L'aparechio* is
     uncertain.
  3. "I have more than my share of it" for *ne ho più di parte* can be defended but is loose.

## 6. Vendor names and local paths (must fix)

- `scripts/pass2_blind.py` line 4 holds a local absolute path (the user folder on the local machine).
- `scripts/pass2_blind.py` line 49 names the AI vendor and the model id.
- `scripts/pass2_blind.py` imports a local helper module that is not in the folder.
- `scripts/__pycache__/decode.cpython-314.pyc` is present and must not be committed.
- `scans/` (12 MB) must stay out of git, as NOTES says.
- NOTES says "a separate vision-model run". The standing wording is "AI language-model agents".

The other files are clean of vendor names, local paths and outside references.

## 7. Prior art

One web search (Marignano, Ferrante Gonzaga, 1546, Ratisbona, cifra, Lutherani) found no edition or decipherment of this
letter. This was one search only, so it is not proof that none exists.

## Must fix before a PR

1. Remove the vendor and model name and the local path from `pass2_blind.py`, or leave that script out. Delete
   `__pycache__`.
2. Fix the English sentence that repeats "Your Excellency"; reconsider "si cognoscerà".
3. In the transcription, mark the M01 `l` as `l?`, as NOTES does, and recount, or drop the claim that it is doubtful.
4. M08 *quale*: rename the sign `9` to `g` (crop check), which removes the value "9 = q".
5. State in NOTES that `check_marks.py` does not check which value is picked for a two-valued sign name. Better: split
   the merged shapes, or mark those picks.
6. Note that the held-out score is against the solver's reading, not straight against the gloss.
