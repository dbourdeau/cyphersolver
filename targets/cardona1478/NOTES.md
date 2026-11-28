# cardona1478: the Count of Cardona to John II of Aragon, Trapani, 16 July 1478 (catalogue 2855)

Status: read in part (67 of 103 cipher words sure, 0.650; 82 with the probable words; recounted in the cold check after the test). Key recovered from the period glosses on the same page and the clear Catalan around them; a held-out test frozen and stamped by FreeTSA before it was run passed.

AI agents (Claude Opus 5.5) did all of this work on 28 Nov 2026 between 04:08 and 05:05 UTC: a lead agent and two
helper agents, each of which transcribed the cipher blind. No person has checked the transcription, the key or the
reading against the image. Nothing here was published before this folder.

## The document

Archivo Histórico Provincial de Zaragoza (Archivo del Reino de Aragón), Colección Zurita, C_CRAR/000001/0026, DARA
record https://dara.aragon.es/opac/app/item?i=1055722 (PDF AHPZ_C_CRAR_000026.pdf, 3 page images of about
1704 x 2368 px plus three details; fetched 28 Nov 2026 04:11 UTC, SHA-256 kept locally). One leaf: the recto mixes
clear Catalan and runs of cipher signs (17 lines with cipher, about 405 signs); the verso has the address and the
docket "de Cardona". Dated "de Trapena a xvj de juliol any m cccc lxxviij"; signed as the king's "humill e
devotissimo vassall e servidor". The writer is the Count of Cardona, then in Sicily (Ferdinand's letter of 9 June
1478, catalogue 2854, discusses moving him from Sardinia to Sicily).

## Result

1. **There are glosses of the time.** The catalogue says "No decipherment on the sheet"; Gemini 4 Carbon (via @tttzqw) (PR #1021) says
   "partial contemporary Catalan glosses". The image bears this out: a second, browner hand wrote short words over
   or under cipher runs in the middle and lower part of the page (don Gismundo, de son offici, lo senyor de
   Camarasa, la gran justicia que ...), and two lines at the head of the page that give the sense of the first four
   cipher lines (`glosses.md`). Not every run is glossed; the glosses are not letter by letter.
2. **System.** A homophonic letter substitution of about 45 signs, written inside the clear text, with no word
   division; one sign (`Rp`) is g and the two-dot sign is i. Catalan. No code sign was found.
3. **No upstream key fits by shape** (plan step 2): of the 15 commonest signs, at most 4 have a counterpart in the
   1473 table of targets/ferdinand1473, fewer in its 1474 table; ferdinand1478 (PR #1021) is a numeric syllabary;
   juanmanuel1497, claver1497, garcilaso1498 and toledo1479 use other sign families. So no upstream key was decoded,
   as the plan allowed.
4. **Held-out test: PASS.** The key was built from lines L10-L17 only and tested once on lines L01-L09 against the
   glosses there: 0.859 of the gloss letters found in order in the decode (61 of 71), against at most 0.479 for
   200 keys with the same values shuffled (mean 0.284, z 7.6, rank 1 of 201). Pass rule: at least 0.60, above every
   control and 0.15 clear of the best. On the second reader's transcription (report only): 0.831 against 0.437.
   The #1014 "char" form (over the longer string) is 0.341 against at most 0.184.
5. **Reading.** 103 cipher words: 67 sure, 15 probable, 21 holes (`reading_words.tsv`, as recounted in the cold check below;
   the first count was 78 sure, 7 probable, 19 holes of 104). Contents: someone, the son
   of the baron of Castellví(?), was tortured, and named others; Don Gismundo's office; the lord of Camarasa (once
   with three thousand florins); "en açò té lo senyor de Camarasa"; Cardona recalls to the king's excellence "la gran
   justicia" and says Don Gismundo "es pobre"; the charge and the shame; "la justicia del dit senyor de Camarasa".

## Plan and order of work (times UTC)

- 04:11 images fetched (curl; `sources/raw` locally). 04:13-04:44 two blind transcriptions by helper agents (no
  values, interlinear words left out), the second by the helper that had first transcribed catalogue 2865.
- 04:37:14 `plan/PLAN_v1.md` stamped by FreeTSA (`plan/MANIFEST_plan.sha256.tsr`): held-out lines L10-L17.
- About 04:40 the lead, while comparing sign shapes for plan step 2, saw that the run "ae t v m c g h t 3 p gbar xo
  g p s xo" in L12, L14 and L17 fits the gloss "senyor de Camarasa": key work on the held-out lines. The roles were
  swapped: `plan/PLAN_v3_amendment_2855.md`, stamped 04:41:32. Key from L10-L17, test on L01-L09.
- 04:42 glosses over L05-L09 transcribed (`verification/reference_v1.txt`) before any decoding of L01-L09.
- 04:43-04:45 key built from L10-L17 by hand (manual reconstruction from the glosses and Catalan context).
- 04:45:50 `verification/MANIFEST_v1.sha256` stamped by FreeTSA (`.tsq`, `.tsr`; verified with FreeTSA's CA
  certificate). 04:45:55 measured once (`verification/RESULT_v1.json`).
- The plan files give times written by hand ("about 04:40"); the FreeTSA times are the right ones.
- Deviation from the plan: the plan said the lead would rule on the image on every place where the two readers
  differ. To avoid ruling with knowledge of the key, the lead did not; the first reader's signs stand
  (387 of 406 signs agree, 0.953; `transcription/r.flags.tsv`).

## Cold check after the test (28 Nov 2026, from about 05:00 UTC)

By a separate AI agent (Claude Opus 5.5) that did not build the package. All of it was done after the held-out test
and does not change it.
- Scripts rerun: `decrypt.py`, `scripts/reconcile.py`, `scripts/translate.py` and `verification/measure.py` (on a copy,
  both protocols) give byte-identical outputs (the results differ only in `run_utc`). The three FreeTSA tokens verify
  with `openssl ts -verify` against FreeTSA's CA, on both the query and the data; their times (04:37:14, 04:41:32,
  04:45:50 UTC) come before the measurement (04:45:55).
- The 15 places where the two readers differ were put to one fresh helper agent (Claude Opus 5.5, 05:05-05:18 UTC),
  shown only the page image and the two readings of each place as shape descriptions, with no key and no reading. It
  supported the first reader at 9, the second at 5, and could not tell at 1 (L15 #1). Under the rule Daniel Bourdeau
  gave on #1021 (27 Nov 2026), a place a model settled on the image counts as probable, so the four sure words on a
  disputed sign (el twice in L03, dels in L04, e in L16) are now probable. At L01 #4 the helper saw the second
  reader's barred g, which would give turmentat; at L09 #2 it saw a barred g, which makes "aure" unread.
- The word count was redone against `decryption_reader1.txt`: ferli, stat, fet, fer, ha (L03) and hauer (L07) carry
  a letter the tested key does not give, so they are probable or holes; the L07 "a" in "per a auer" used the same
  sign as auer and was removed; "ell" is written "el" as the key gives it. Result: 67 of 103 sure, 15 probable, 21 holes.
- Which words rest on what: every word counted as read is given by the key. Of the 67, 31 also stand under a gloss of
  the time (4 only under the head gloss, read after the test) and 36 are given by the key where no gloss word
  stands; by the notes column of `reading_words.tsv`. No word is counted as read from a gloss alone.

## Remaining gaps

- L01-L04: turmentat (the two readers differ on one sign), castelvi, tran?o (one sign illegible), sab, acor..n,
  sat, torgar, e, alguns: signs with no value in the tested key (fbar, qbar, 8, pdd, dl, o) and one illegible sign.
- L06-L08: son, offici, gran, carrec, pagat, camarasa (an extra hatched sign), florins: signs b, b6, 2, 7 and mx
  give values that do not fit here; perhaps signs the readers merged.
- L10 and L15: the first sign of the line (tloop) has no value; L15 ends in three unread signs.
- "Camarasa" decodes "camarata" each time: sign s is t everywhere else (dit, iusticia, reportaria).

## Values proposed after the test (not covered by it)

m_ = f (fill), fbar = v (Castellví), gx = e, qbar = b (ab), 2 = h (ha). They make the head gloss and the decode
agree, but they were set after the measurement and need a new passage to be tested (#1014, point 6).

## Transcription doubts

The readers' own notes are in `transcription/reader1_NOTES.md` and `reader2_NOTES.md`. Main points: the dipping
starts of L07, L10, L11, L12, L14, L15 and L17; L02 #5 illegible; L08 #5 a hatched m; L03 #31-32 and L15 #32-34;
b/b6 and 7/7bar may be one sign each; L12 u against v in the same run elsewhere.

## Escalation

The values after the test, and the holes in L01-L08, would be settled by a better image or by another letter of
Cardona's in the same cipher (none found in C_CRAR/000001).

## Prior work

No reading of this letter found: García Larragan's post of 16 July 2026 covers 0024 (catalogue 2854) only; a web
search on 28 Nov 2026 (Cardona 1478, Juan II, cifra) found nothing. The sweep by Gemini 4 Carbon (via @tttzqw) (PR #1021) noted the glosses and
the Catalan; it did not transcribe or read the letter.

## Checks not passed or not run

- `docs/_validate.py` was first not run (Project Gutenberg answered 503 on 28 Nov 2026 about 04:55 UTC). In the cold
  check (28 Nov 2026, about 05:25 UTC) it was run once, without `--write`, on the same Gutenberg texts fetched from the
  gutenberg.pglaf.org mirror (`CYPHER_CORPUS_ROOTS`; `tirant.txt`, a local-only part of the ca-gutenberg corpus, was
  missing, so the model is not exactly the repository's). Result, model ca-modern: 380 read tokens, 31 types; reading
  -2.301 per letter, random keys at most -4.332 (z 5.8), shuffled refit at most -3.046, annealer power -2.498:
  **pass**. It scores the whole text, training lines included, so it is not a held-out figure. It is not recorded in
  `profile.json`, and "statistical test" is not claimed in `outcome.verification`.
- `docs/_check_reading.py` rates the reading file "not a reading" (clean-sentence share 0.33, 9 of 27
  sentences, after the cold-check edits). README Conventions say the checker points at weak
  sentences but is not the verdict. The class stays "read in part" because lines L10-L17 and L05 read as Catalan
  sentences; L01-L04 and L06-L09 have holes in most sentences and do not yet read. A reviewer may judge otherwise.

## Files

`transcription/` (both readers, sign lists, notes, reconciliation), `glosses.md`, `key.tsv`, `decrypt.py`,
`decryption_reader1.txt`, `decryption_reader2.txt`, `reading_words.tsv`, `plan/`, `verification/` (protocol,
manifest, FreeTSA query and reply, key, transcriptions and reference as frozen, `measure.py`, results).
Reproduce: `python3 decrypt.py key.tsv transcription/reader1_transcription.txt`; the test refuses to run twice.
No images are in the folder.
