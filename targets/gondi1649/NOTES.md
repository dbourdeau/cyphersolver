# Giovanni Battista Gondi to Commendator Galilei, 11 May 1649 (new find, Biblioteca Estense)

Status: in progress. Not yet written up: no site page or README row. Classed read, so it is ready for the /writeup skill. The status below is the contributor's.

Not in the catalogue and not on DECODE: found in a sweep of the Estense Autografoteca Campori for letters marked as
ciphered. No catalogue number.

Status, 3 Nov 2026: **read** (the cipher part of c. 1r), deciphered with a key recovered from the adjacent
interlinear decipherment. This is a **transcription job, not a break**: a contemporary decipherment written between the
cipher lines covers all of it.

Word counts (`scripts/check_marks.py`, output in `validation/check_marks_output.txt`; word lists by
`scripts/count_words.py`): 102 words in the cipher reading. 86 come verbatim from the signs, 14 carry a marked repair and
2 are context-only or unread. The 14 are: 9 double letters written once (a convention of this cipher), one doubtful
sign each in *replica* and *ragione* (settled by sense), *che* and *et* read from unbarred signs (value repairs), and
*a* restored before V.S. on L07 (no sign at all, so not a read word). The 2 are code 273 (Vicerè from context only) and
the unread pair `5 8`. An earlier draft of this report said "84 of 102 verbatim"; that was wrong, the script gives 86.

Of the 101 sign-bearing words, **99 (98.0%) are read from the signs under the cipher's own conventions**, *che* and *et*
included as value repairs. Without the two value repairs: 97 of 101 (96.0%). Without the two words on a doubtful sign
as well: 95 of 101 (94.1%); dropping also *pesar* (a forced literal reading, see Findings): 94 of 101 (93.1%).
**Disagreement with the check:** the independent check gives 98 of 101 (97.0%) for the first figure. We could not
reproduce that: with 101 sign-bearing words and only `5 8` and 273 not read, 99 remain. `scripts/count_words.py`
prints every word in its class, so the count can be checked word by word. Both figures are above the 95% bar; the
strictest is below it.

Prior art: none found (below). Contributed by WAINUT; the work was done with AI language-model agents.

## Document

- Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera G, Gondi, Giovanni Battista, cc. 1-2
  (4 canvases). Catalogue record: "Lettera parzialmente cifrata (ma decifrata in interlinea). Il destinatario è indicato
  come: Commendator Galilei."
- Record: https://lodovico.medialibrary.it/media/schedadl.aspx?id=d3fd6a93-7004-499d-a257-96f86cb81f0e
- IIIF manifest: https://edl-jarvis.cultura.gov.it/meta/iiif/d3fd6a93-7004-499d-a257-96f86cb81f0e/manifest
  (images CC BY-NC-SA; not stored in git). Cipher only on c. 1r, lower half: 14 cipher lines (about 560 signs); c. 1v-2v
  are clear.
- Sender: Giovanni Battista Gondi, secretary of state of Grand Duke Ferdinando II. Recipient "Commendator Galilei": not
  identified here (a knight-commander of the Galilei family serving Tuscany abroad; open).

## The system

A Tuscan letter cipher with a small code, no word division:

- vowels are single digits: 3 a, 4 u/v, 5 o, 6 e, 7 i;
- consonants are a digit followed by 0: 10 c (and b), 30 l or r, 40 n or s, 50 m, 60 t; plus W (an omega-shaped sign)
  d or z, 9 p (and q), 1 g (and f), 2 g. Several consonant signs are polyphonic (one sign for two letters);
- double letters are written once (*acenni*, *posa*, *scritura*);
- barred signs are words: 7^ non, 5^ che, 4^ e, W^ per, 6^ chi (inside *richiamata*);
- three-figure groups starting with 2 are names and titles: 217 di/de/del, 261 Signor, 262 V.S., 264 S.E., 267 S.A.,
  223 Vicerè, 252 quelli, 273 (context: Vicerè); W0 is *con*.

`key.tsv` lists every value with its status and evidence.

## How the key was obtained; held-out test

1. Signs were copied first, before decoding: pass 1 by eye on full-size crops (`validation/pass1.txt`); pass 2 by a
   separate AI language-model agent on tight cipher-only bands, with no key, no clear text and no decipherment
   (`scripts/pass2_blind.py`, output `validation/pass2_raw.txt`). The passes differ on 39 of 558 signs; each difference
   was settled on full-size crops (`validation/adjudication.tsv`). Pass 2 was right at 9 of the 25 disputed places (missed
   bars, an extra 3, a spurious 0 and comma, the start of L09, misread *era*); pass 1 at the rest. The blind rate is for
   the whole of c. 1r, before adjudication. No sign was moved toward the
   interlinear text; where a sign stays unclear it is marked doubtful (`6?` in *replica*, `2?` in *ragione*).
2. The key was built from the pairs (cipher against the interlinear decipherment) on lines L00-L06 only, then frozen
   (rows `frozen` in `key.tsv`).
3. Held-out test: lines L07-L13 (148 sign units) were decoded with the frozen rows. The frozen key agrees with the
   reading on 139 units (93.9%). The other 9 are values the training lines did not contain: three second values of
   polyphonic signs (f for 1, b for 10, q for 9), four code groups (252, W0 twice, 273), 2 as g, and the unexplained
   pair 5 8. No frozen value was contradicted. Output: `validation/check_marks_output.txt`.
   **Limit of this test:** it is graded against our own reading of L07-L13 (`ASSIGNED` in `check_marks.py`), not
   against an independent transcription of the interlinear text, and that reading was made with the interlinear text in
   view. Many frozen values are two-way (30 l|r, 40 n|s, 10 c|b, 9 p|q), so agreement is easy. The test shows that the
   key is consistent across the letter; it is not an independent proof of it.

## Reading

`reading_c1r.md` (Italian and English, the cipher placed in the letter), `reading_marked_c1r.txt` (line by line with
marks). `scripts/check_marks.py` rebuilds the decryption (`scripts/decode.py`, `decryption_c1r.txt`) from
`transcription_c1r.txt` and `key.tsv`, walks the reading unit by unit, and exits 1 on any unmarked departure. It passes.

Summary: Gondi tells Galilei to find out whether the Viceroy (S.E.) thinks nothing more is needed or simply does not want
Galilei there. The Grand Duke has not yet decided to recall him and waits for "categorical" answers from Vincenzio de'
Medici on a chapter of a paper of the Viceroy that was sent the week before. The Grand Duke's reply to the Viceroy's
letter will follow. In Milan the Viceroy's notions were very badly received, and the Grand Duke had taken offence at them,
with reason.

## Findings: where the cipher and the contemporary decipherment differ

These are kept as the signs give them. They are not repaired toward the interlinear clear.

1. L01: the signs give *pesar* (p-e-n/s-a-l/r) with no *di* before S.E.; the decipherer wrote "pensiero di S.E.".
2. L12: the signs give *malis.* (malissimo, abbreviated); the decipherer wrote "malam.te" (malamente).
3. L09: two signs, `5` and a B-shaped sign, stand before *aver*; the decipherer wrote "havere". They are not explained:
   no other occurrence, no value in the key.

The decipherer's clear therefore follows the sense, not the letters. It was made from the cipher, not copied from a
draft of the letter.

## Context (not from the document; general knowledge, unverified here)

In May 1649 the Viceroy of Naples was Inigo Velez de Guevara, count of Onate (1648-1653), and the Viceroy of Sicily was
Don Juan José of Austria. Milan had a governor, Luis de Benavides, marquis of Caracena, not a viceroy. "In Milan those
notions were very badly received" therefore points to a viceroy outside Milan, most likely Naples, and to Galilei being
the Tuscan envoy at his court. This is context only: the document names neither the Viceroy nor the place. One web
search (3 Nov 2026) for a Commendatore Galilei serving Tuscany in 1649 found nothing.

## Remaining gaps

- `5 8` on L09: unread. One occurrence; no outside blocker except that it occurs only once. The independent check
  read the same place as `5 0? B`: it sees a loop between the 5 and the B-shaped sign, which our adjudication did not
  accept. Unresolved; it does not change the reading, since neither side reads the pair.
- Code 273 on L13: read as Vicerè from context only (223 is Vicerè on L06). A second letter of this correspondence would
  settle it.
- Doubtful signs: `6?` in *replica* (L07) and `2?` in *ragione* (L13). Both are settled by sense, and both are marked.
- *che* (L01) and *et* (L12) are read from a 5 and a 4 that show no bar. The bar may be shared or faint.
- The identity of the Commendator Galilei and of the Viceroy (S.E.): not in the document.
- The clear text of the letter (cc. 1r-2v) was read only around the cipher, and roughly. It is not part of this job.
  Two clear phrases in `reading_c1r.md` are marked rough after the check: the opening "Se già havessi detto ..." and
  "portarla a S.A." (the check reads the clear as "portar all'A.S.").

## Independent check (VERIFY.md)

One AI language-model agent that took no part in the solving checked the work on 3 Nov 2026 (`VERIFY.md`). Verdict
**fix**, recommended status **read** as a transcription job. In short:

- Blind signs: before opening any solver file it copied 280 signs (184 units) of L04, L07, L08, L09, L11, L12 and L13
  from its own full-resolution crops (the held-out passage except the 3 signs of L10). Raw disagreement 2 of 280 (0.7%).
  On a 2x crop: L09 *veduto* ours right (it had taken the loop of W for a 0); L09 start `5 8` against its `5 0? B`,
  unresolved, unread either way. 0 solver errors found. The rest of c. 1r (L00-L03, L05, L06, L10) had no blind
  second reader apart from our own pass 2.
- Rebuild: `decode.py` and `check_marks.py` reproduce `decryption_c1r.txt` and `validation/check_marks_output.txt`
  byte for byte; `check_marks.py` fails on planted errors (an unmarked changed letter, a doubtful sign without its mark,
  a restored word written as plain text).
- Held-out test reproduced (139 of 148), with the limit stated above.
- Reading grades: `reading_marked_c1r.txt` A, `reading_c1r.md` B, `translation_c1r.md` B.
- Its fixes, applied: vendor and model names and a local path removed from `scripts/pass2_blind.py` (the model call now
  goes through a helper that is not included); "vision model" reworded; the verbatim count made consistent (86); the
  headline restated per sign-bearing word; "da far la prima di aver veduto" retranslated "to do it before having seen";
  two loosely read clear phrases marked `[rough: ...]`; the limit of the held-out test stated.
- One disagreement: the count of sign-bearing words read (it says 98 of 101, we count 99; see the top of this file).
- `VERIFY.md` is the check's report unchanged except three lines (section 6) that quoted a model-provider name, a model
  name, a local path and an archive not otherwise mentioned. Each is marked `[redacted for the PR: ...]`. Its figures
  and must-fix list predate the fixes above.

## Escalation done

Sign-first double transcription with a blind second reader; adjudication on full-size crops; frozen-key held-out test;
key checked at every occurrence by `check_marks.py`; one search each for prior art and for the persons.

## Prior art

Checked 3 Nov 2026: Dan Bourdeau's catalogue, leads, targets and research notes (origin/main) and open PRs for
Gondi/Galilei/1649: only the French Gondi targets of 1594, unrelated. One web search ("Gondi" "Commendatore Galilei"
1649 cifra): no edition or decipherment of this letter found; Gondi papers exist at Penn (Kislak) and the Morgan
Library, not this letter.

## Files

`transcription_c1r.txt` (signs), `key.tsv` (every value with status and evidence), `key_frozen.tsv` (the rows frozen
before the held-out test), `decryption_c1r.txt` (rebuilt by `scripts/decode.py`), `reading_marked_c1r.txt` (line by
line, every departure marked), `reading_c1r.md` (Italian, cipher in its place in the letter), `translation_c1r.md`
(English), `VERIFY.md` (independent check), `validation/` (pass 1, blind pass 2, adjudication, check output).

Scripts: `scripts/decode.py`, `scripts/check_marks.py`, `scripts/count_words.py` (standard library; run
`python scripts/check_marks.py` from this folder or anywhere). `scripts/fetch.py` (polite IIIF fetch, one request at a
time, 1 s apart), `scripts/strips.py`, `scripts/zoom.py` (need Pillow, numpy and the images) and `scripts/pass2_blind.py`
(needs Pillow, the images and a local model helper that is not included) are a record of the method. No images are
included; `scripts/fetch.py` fetches them from the manifest above.

## Note, 4 Nov 2026: class corrected to read in part; not written up

The profile class was "read" (98.0% of the sign-bearing words, strictest count 93.1%). Three gaps are marked
`not-attempted` (a blind reading of L00-L03, L05, L06 and L10 beyond the one independent check; the clear text of
cc. 1r-2v; the identity of the Commendator Galilei and the Viceroy), and the read bar allows no gap `not-attempted`, so
the class is now "read in part" and the target stays `Status: in progress`. The first two need the Estense images, which
were not reachable from the maintainer's session. A web search for the Commendator Galilei on 4 Nov 2026 found nothing
(it supports only that Gondi was first secretary of state to Ferdinando II from 1641); Brovadan's 2020 chapter on Gondi's
letters and the Florentine state archive (Mediceo del Principato) are untried. Also still missing: a statistical
validation record (`docs/_validate.py --write` or `--na` with a reason).

