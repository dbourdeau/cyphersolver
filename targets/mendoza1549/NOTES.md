# mendoza1549: Diego Hurtado de Mendoza to Ferrante Gonzaga, Siena, 3 April 1549 (catalogue 2161)

Status: in progress (read in part; the gaps below are workable, so no write-up yet).

Contributed by WAINUT (lccompany). Work of 12 Nov 2026 by AI language-model agents; no human palaeographer.

## Documents

- Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera H, Hurtado de Mendoza, Diego, sfasc. I,
  cc. 40-46 (14 images; uuid e02077fa-33a9-4749-b581-f88f2d45e9be). Letter in clear on cc. 40r-41v, dated at the
  end of 41v "en Sena iij de abril 1549", not Rome; address on c. 45v.
- **c. 44r**: one page of cipher, 17 lines, 378 signs plus 30 points (`transcription_44r.txt`). This is the target.
- **c. 42r**: a clear sheet laid over c. 44r in the binding (the first cipher line of 44r shows above it in the
  photograph), 14 lines beginning "Y quando huvieremos dado la auctoridad a los ocho...". It is the contemporary
  decipherment of c. 44r. This settles the conflict in the catalogue status: c. 42r is not part of the letter in
  clear, as Brice Dudout said in issue #254.
- c. 43r-v: a clear point-by-point summary of the dispatch, not a key (agrees with Dudout).
- The short struck-through cipher passages in the letter (40v, 41r, 46v) were not transcribed in this round.

Images: IIIF manifest https://edl-jarvis.cultura.gov.it/meta/iiif/e02077fa-33a9-4749-b581-f88f2d45e9be/manifest ;
record https://lodovico.medialibrary.it/media/schedadl.aspx?id=e02077fa-33a9-4749-b581-f88f2d45e9be . Whole-image
requests are refused (422); region tiles of 1024 px work. `scripts/fetch.py` stitches c. 44r at full resolution
(5426 px wide) and c. 42r at half resolution from tiles, one request every 1.6 s. Scans are not in this folder.

## Prior work and prior art (checked 12 Nov 2026)

- Brice Dudout, issue #254 (closed) and PR #265 (closed, not merged): identified c. 42r as the decipherment of c. 44r
  and aligned 340 of 376 signs; his alignment is not on origin/main (research/dudout_leads_2026-11-04 holds only his
  README and candidates.json). The present work is an independent transcription and alignment made from the images;
  his sign count (376) and ours (378 without points) agree closely. Credit for the identification is his.
- targets/mendoza1548 (#216, brackxm): the same sender's syllabary of 1548. Not used to build this key; several of
  its values recur here (n a, mo s, ω e, no r, e lo, u co, ∠ ll, ω̈ qui).
- Print: no edition of this letter found. One web search (12 Nov 2026) on Mendoza, Ferrante Gonzaga, Siena 1549,
  capitan de popolo: nothing. Vázquez and Rose, Algunas cartas (Yale 1935; the catalogue's status line gives 1945,
  its vetting note 1935) and Varo Zafra, Cartas (2016) were not opened (no full text online; see the catalogue
  vetting note). If either prints this letter, it prints c. 42r, the contemporary clear, which is the crib used
  here anyway.

## System

A Spanish chancery syllabary of the family of mendoza1548: 95 distinct sign names in 378 places, plus the point
(30 places). `key.tsv` has 96 entries (the 95 names and the point), one line each under a two-line header. The
signs are syllable signs (consonant shape with vowel marks: dots, bars), single letters, a few joined forms (`ap` n,
`af/` o, `uf/` ci, `cb` que), the doubling-like dash (`- S` sse), the point (one null sign in 30 places; a null or
word mark) and three code groups (3 distinct groups, 4 occurrences): `chu` tiempo (twice), `dis` emperador (once),
`qre` vuestra (once, in "a vuestra Escelencia"). Word spaces are mostly kept.

## Key and held-out test

`align_44r.txt` pairs every sign of c. 44r with its value read against c. 42r. `scripts/build_key.py` takes each
sign's most frequent value: `key.tsv` from all 17 lines, `key_frozen.tsv` from lines L01-L10 only (frozen before the
test). `scripts/heldout.py` applies the frozen key to L11-L17 (147 signs, points not counted; output in
`heldout_44r.txt`):

- frozen key gives the value read in that place: 91 of 147 (61.9%); 91 of the 115 signs the frozen key knows (79.1%);
- same consonant, vowel aside: 99 of 115 known signs (86.1%);
- 32 of the 147 held-out signs (22%) are signs that do not occur in L01-L10.

`key_frozen.tsv` has 74 entries (73 sign names and the point) under a two-line header. The independent reviewer
(13 Nov 2026) rebuilt it from `align_44r.txt` lines L01-L10 and got the same 74 entries, so L11-L17 did not enter
it. This is a weak test in one respect: the held-out lines' plaintext (c. 42r) was in view when the transcription was
made, and the same page supplied the training pairs. It is reported as a number, not as proof.

## Decryption and reading

`decryption_44r.txt` is the mechanical decryption with `key.tsv`. `reading_44r.md` gives the text as sentences;
`reading_44r_marked.md` gives the same reading line by line with every departure marked. `scripts/check_marks.py`
rebuilds the decryption and fails on any unmarked departure (passes). Word count (154 words): 122 verbatim from the
signs, 4 code-group words, 28 with a marked repair, 0 holes. Verbatim share 79.2% (81.8% with code groups): **read in
part**. Every sentence builds; the repairs are single sign values (mostly signs that carry two values in our naming,
see below).

No word comes from c. 42r without a sign under it, but the "verbatim" count needs one qualification. 37 of the 96
key entries rest on one place only (35 sign names that occur once, and `p` and `S`, which occur twice with one place
unexplained). 22 of the 122 verbatim words hold such a sign, and its value comes from the alignment with c. 42r
alone: those words are verbatim by construction. Without them, 100 of 154 words (64.9%) are read from signs whose
value is attested in more than one place. `scripts/reading.py check` prints both counts. The state does not change.

## Where the cipher and c. 42r differ

The cipher has: "ovieremos" (42r huvieremos); "si les damos un capitan" (42r first wrote "man" and struck it:
the decipherer's slip, the cipher never had "mandamos" here); "a vuestra Escelencia no comunique en la corte"
(42r "a V.E. ... no comuniq en Corte": no "que", and the cipher has "la"); "tirano" (42r "tiriano"). These four
places show c. 42r is a decipherment made from c. 44r, not the draft it was enciphered from.

## Remaining gaps

- Shape splits - blocker: not-attempted; `x` stands for both de (8 places) and no (6), `o'` for ga (3) and ta (2),
  `n` for a, co (2), c and f, `lo` for mo and tro (quatro, nosotros), `q'` for ha and a, `9` for do and u (ultimo),
  `e` for lo and le. Each is probably two near shapes merged in our naming; a third look at 3x crops should split
  them. Most of the 28 repairs sit here. Splitting them is the next step toward grade A.
- Three signs unexplained in place - blocker: too-short; `o` in "Florencia" (cipher F-lo-re-?-n-ci-a), `p` in
  "vez", `S` in "Juan". Each of these names occurs once or twice on the page.
- Single-place sign values - blocker: too-short; 22 of the 122 verbatim words hold a sign whose value is attested
  in one place only and comes from c. 42r alone (see Decryption and reading). A second cipher text in the same key
  would test them.
- Cipher passages on cc. 40v, 41r and 46v - blocker: not-attempted; struck through, with clear beside them; not
  transcribed. They are the natural second held-out test and would also test the single-place values.
- Sign names left open after the review - blocker: not-attempted; the reviewer's name differences in L03, L08, L13
  and L16 (see Independent review) were not settled on the image and are left as transcribed.

## Escalation

- [x] siblings: the whole file cc. 40-46 (14 images) opened; c. 42r is the decipherment of c. 44r, c. 43r-v a
  summary; targets/mendoza1548 compared by value
- [x] clear-pages: c. 42r identified as the decipherment (after Dudout, issue #254) and used for the key and the
  held-out test; c. 43r-v checked: a summary of the dispatch, not a key
- [ ] known-keys: the key of targets/mendoza1548 was compared on 8 values (n a, mo s, ω e, no r, e lo, u co, ∠ ll,
  ω̈ qui) but not applied to c. 44r as a test
- [ ] print: one web search; Vázquez and Rose (Yale 1935) and Varo Zafra (2016) not opened (no full text online)
- [x] key-rebuild: key rebuilt sign by sign from the alignment with c. 42r, frozen on L01-L10 and tested on
  L11-L17; docs/_validate.py: pass (below)
- [ ] retry: the 28 repairs and the shape splits not yet retried on 3x crops

## Independent review (13 Nov 2026)

One independent AI language-model agent reviewed the work blind (it did not change the solver's files): grade B,
read in part.

- Sign spot-check before opening the transcription: 4 lines (L03, L08, L13, L16; 92 signs and 8 points) cropped
  from the image. Same segmentation and the same sign count in all 4 lines; name differences only in marks and near
  shapes: L03 `p` (reviewer `ap`) and `o^` (`o`); L08 `8'` and `L:` (marks not seen clearly) and `inf` (`oo`); L13
  `yo` (`yp`); L16 `l'` (`L`) and final `u` (`n`).
- The four places where c. 42r departs from the cipher checked on the image, including the struck-through "man"
  before "damos" on c. 42r.
- `scripts/check_marks.py`, `scripts/decrypt.py key_frozen.tsv` and `scripts/heldout.py` re-run with the same
  results; `key_frozen.tsv` rebuilt from L01-L10 with the same 74 entries.
- The reading read sentence by sentence against the translation: 12 sentences, none with a hole.
- Fixes made after the review: the marked block moved from reading_44r.md to reading_44r_marked.md; the
  single-place qualification of the verbatim count added; sign and symbol counts corrected (378 signs, not 380; 95
  distinct names, points aside); the year of Vázquez and Rose checked.

## Statistical validation (docs/_validate.py, 13 Nov 2026)

`validation.tsv` holds the 408 tokens of c. 44r (378 signs and 30 points) with the value each carries in place,
taken from `align_44r.txt`; 405 read, 3 unread. Model es-golden-age: reading -2.078 per letter; random keys of the
same structure -3.587 (sd 0.170, z 8.9, n = 200); keys annealed onto shuffled ciphertext best -2.218 (mean -2.264,
z 5.2, n = 6); annealer on the real text -2.130; polyphony 0.086. Verdict: pass. The pairs come from the alignment
with c. 42r, so this shows that one consistent key reads the page better than chance and than fitted keys; it is
not a test independent of the crib.

## Dan's reading checker (docs/_check_reading.py, origin/main worktree)

- 12 Nov 2026, `--file` on the sentence text of the reading: es, 12 sentences, 10 clean, clean share 0.833, hole
  rate 0.067 (the holes are period spellings such as ovieremos, auctoridad, hizelo);
- translation_44r.md: en, 19 sentences, 18 clean, clean share 0.947;
- before 13 Nov the marked block sat inside reading_44r.md and folder mode scored that file 0.524. It is now in
  `reading_44r_marked.md`, which profile.json does not name as the reading. Folder mode after the split (13 Nov
  2026): reading_44r.md, es, 12 sentences, 10 clean, clean share 0.833, hole rate 0.067, "readable".

## Integration check (13 Nov 2026)

Checked by the integrator against the contributor's files: `scripts/check_marks.py` passes (154 words: 122
verbatim, 4 code words, 28 repaired, 0 holes); `scripts/heldout.py` gives 91 of 147 held-out signs (61.9%), 91 of
the 115 known (79.1%). c. 44r was fetched again from the IIIF tiles at half size: 17 lines of symbol cipher; lines
1-3 compared with the transcription, and line structure, word breaks and about 35 signs agree (not a sign-by-sign
check of the whole page, and the sign names are the contributor's own shape codes).

- Strict share: 79.2% (122 of 154 words verbatim). The four code words (3 groups, one or two places each) carry
  values from c. 42r alone and are counted as holes here; the contributor's 81.8% counts them. Words resting on a
  sign seen in one place only: 22; without them 64.9%. Class: read in part.
- The key is the alignment with the contemporary decipherment on c. 42r, so this is a reading from an existing
  decipherment with the key rebuilt from it. The frozen-key test (L01-L10 to L11-L17) is a consistency test inside
  one page that was transcribed with c. 42r in view; it is not a test on a second text.
- One key, one entry: the same chancery syllabary as targets/mendoza1548 (Bucure's cifra of Naples 1547), but the
  tables were built separately from each page and not compared beyond 8 values. If either target is finished,
  apply its table to the other as a test; nothing here merges them.
- Not done and workable (so the target stays in progress, no page): the 28 repairs and the shape splits on 3x
  crops, the struck cipher passages on cc. 40v, 41r and 46v as a second test, the table of mendoza1548 applied to
  c. 44r, and Vazquez and Rose / Varo Zafra opened.

