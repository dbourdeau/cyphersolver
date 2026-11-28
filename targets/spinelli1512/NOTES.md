# spinelli1512: Giovanni Battista Spinelli, Count of Cariati, to Pedro de Urrea, Venice, 16 April 1512, two letters (catalogue 2865)

Status: read in part (letter A 62 of 83 cipher words sure, 0.747; letter B 70 of 81, 0.864; recounted in the cold check after the test). Key recovered from the period glosses of letter B; a held-out test on letter A's glossed lines, frozen and stamped by FreeTSA before it was run, passed.

AI agents (Claude Opus 5.5) did all of this work on 28 Nov 2026 between 04:08 and 05:05 UTC: a lead agent and two
helper agents, each of which transcribed the cipher blind. No person has checked the transcription, the key or the
reading against the images. Nothing here was published before this folder.

## The documents

Archivo Histórico Provincial de Zaragoza (Archivo del Reino de Aragón), Colección Zurita:
- **Letter A**, C_CRAR/000001/0055, DARA https://dara.aragon.es/opac/app/item?i=1056745 (PDF AHPZ_C_CRAR_000055.pdf,
  4 images of about 1960 x 2700 px): three pages, the news of Ravenna (11 April 1512); 14 lines with cipher.
- **Letter B**, C_CRAR/000001/0056, DARA https://dara.aragon.es/opac/app/item?i=1056746 (PDF AHPZ_C_CRAR_000056.pdf,
  3 images): the same day, more on the battle and its aftermath; 17 lines with cipher.
Both dated "da Venecia adi xvj de aprile 1512", signed "Jo. Bapta Spinelli", addressed to "lo S. don Petro de Urrea
del Consiglio et amb.re del Re N.S. con la M.ta Cesarea". Dockets: "de Venecia del conde de Cariate de xvj de abril":
the writer is Giovanni Battista Spinelli, Count of Cariati, Ferdinand's envoy at Venice. Italian with southern forms.
Fetched 28 Nov 2026 04:11 UTC (curl), SHA-256 kept locally.

## Result

1. **Glosses of the time.** The catalogue says "No decipherment on either leaf". Both letters carry interlinear
   glosses in a second hand over most cipher lines, some struck and rewritten (`glosses.md`). They are not always
   letter for letter (A1.03 gloss "no tenia ...", cipher "no tornasero").
2. **Shared text.** The two letters' cipher shares no run longer than six signs (`scripts/shared_runs.py`), so
   neither gives the other a crib.
3. **System.** A homophonic letter substitution of about 40 signs inside the clear text, no word division; 7 and the
   p-sign with a raised bar (ptop) bracket cipher runs; one code sign (Nplus) stands for "(lo) papa" by the glosses.
4. **Held-out test: PASS.** The key was built from letter B only and tested once on letter A's glossed lines (four
   blocks): 0.725 of the gloss letters found in order in the decode, against at most 0.323 for 200 keys with the
   same values shuffled (mean 0.214, z 15.5, rank 1 of 201); pass rule at least 0.60, above every control and 0.15
   clear of the best. On the second reader's transcription with the same key in that reader's sign names (report
   only): 0.740 against 0.320. The #1014 "char" form is 0.554 against at most 0.246.
5. **Reading** (`reading_words.tsv`; A 62 of 83 and B 70 of 81 cipher words sure as recounted in the cold check below;
   the first count was A 64/82, B 71/81). Letter A: "ogne cosa si ristaurera" (clear) and "fici le cose nostre
   gagliarde", fearing a return to talks with the French; the Council of Ten met yesterday with the Giunta on this;
   Spinelli encouraged the Signoria to hearten the Pope; to treat with the Pope they would want the ten thousand
   Spanish foot made up with Italians, and forty thousand ducats; he is sure the Signoria will do it if the Pope
   moves. Letter B: the Viceroy is to go to Naples, to keep the army together; Prospero Colonna with three hundred men
   at arms; the royal baggage fell to the peasants; six thousand men; many of "our" principal men dead; on the six thousand Spinelli
   is "de contrario voto"; if the French took the state of Milan and did not restore it to the Emperor, they would come
   to terms with the King of France.

## Plan and order of work (times UTC)

- 04:11 images fetched. 04:13-04:44 two blind transcriptions by helper agents (no values, interlinear words left
  out), the second by the helper that had first transcribed catalogue 2855.
- 04:37:14 `plan/PLAN_v1.md` stamped by FreeTSA: key from letter A, test on letter B.
- Then, while transcribing letter B's glosses, the lead aligned two of them by eye (B1.05, B2.01) and saw the
  values: key work on the held-out letter. Roles swapped: `plan/PLAN_v2_amendment.md`, stamped 04:38:03: key from
  letter B only, test on letter A. Before PLAN_v1, a few values had been tried by eye on A1.01 and A2.04-05; none
  held, and none was used. Letter A's glosses had been seen while cutting crops.
- 04:38:54 letter A's glosses transcribed (`verification/reference_v1.txt`), before letter A was decoded.
- 04:39-04:46 key built from letter B (both readers) by hand from its glosses.
- 04:47:00 `verification/MANIFEST_v1.sha256` stamped by FreeTSA (verified with FreeTSA's CA certificate);
  04:47:04 measured once.
- The plan files give times written by hand ("about 04:40", "about 04:55"); the FreeTSA times are the right ones.
- Deviation: the lead did not rule on the image on the places where the two readers differ (700 of 727 signs agree,
  0.963); the first reader's signs stand in the primary test. The first reader writes one sign bx where the second
  separates hx (s) and bx (u/v); in the first reader's names the key gives bx = s.

## Cold check after the test (28 Nov 2026, from about 05:00 UTC)

By a separate AI agent (Claude Opus 5.5) that did not build the package. All of it was done after the held-out test
and does not change it.
- Scripts rerun: `decrypt.py` (both readers), `scripts/reconcile.py`, `scripts/shared_runs.py` and
  `verification/measure.py` (on a copy, both protocols) give byte-identical outputs (the results differ only in
  `run_utc`). The three FreeTSA tokens verify with `openssl ts -verify` against FreeTSA's CA, on both the query and the
  data; their times (04:37:14, 04:38:03, 04:47:00 UTC) come before the measurement (04:47:04).
- The 25 places where the two readers differ were put to one fresh helper agent (Claude Opus 5.5, 05:05-05:18 UTC),
  shown only the page images and the two readings of each place as shape descriptions, with no key and no reading.
  It supported the first reader at 8, the second at 10, neither at 1 (B1.04 #11-12) and could not tell at 6 (three of
  them the same plain p under two names). Under the rule Daniel Bourdeau gave on #1021 (27 Nov 2026), a place a model
  settled on the image counts as probable, so the three sure words on a disputed sign are now probable: e (A1.02, the
  sign before it), spagnioli (A2.08) and de (B1.02).
- The word count was redone against `decryption_reader2.txt`: the code sign Nplus at A2.10 ("se [papa] lo move") had
  been left out and is now counted as a hole; "le" (A1.01) and "lo" (A2.10) are written lle and llo as the key gives
  them (sign 5slash is ll, as in alle and villani). Result: A 62 of 83, B 70 of 81 sure.
- Which words rest on what: every word counted as read is given by the key. Letter A was held out, so its words come
  from a key built without it; its glosses agree with most of them, and about twenty (como ... consiglio de dece se
  fece, ionta credo sulo, quaranta milia ducati, havesemo, tornasero alle ... con francisi) stand where no gloss word
  is. In letter B the key was fitted to the glosses, so its glossed words are read from the gloss as well as from the
  key; the words of B3.05 (se acordaria con re de francia), soperiore, piu and tornare have no gloss word in `glosses.md`. No word is
  counted as read from a gloss alone.

## Remaining gaps

- Sign o gives c in letter B (con, campo) but b is wanted in letter A (dubito, dubitando, delibera): perhaps two
  shapes the readers merged. 3 holes.
- Signs with no tested value: hbar (s in nostre, cossi), fbar (r in confortato), Nplus (code for "papa"), q in
  B1.01; and lam/lamf (s or t) in tutto.
- A2.04-05 "la S. ad dare", A2.07 milia (sign under an ink blot), A2.09 "le spagnoli", A2.10 "la S.",
  B3.02-04 "al ... del stato ... la restituire": decode garbled over a few signs.

## Values proposed after the test (not covered by it)

hbar = s, fbar = r, Nplus = (lo) papa, o = b in letter A. They need a new passage for a test (#1014, point 6).

## Transcription doubts

In `transcription/reader1_NOTES.md` and `reader2_NOTES.md`: about 30 q/p/d bars that may belong to interlinear
words; the start of B3.03; A2.07 and B3.01 blots; pf (et) after clear text may be the clear abbreviation.

## Prior work

No reading found: catalogue 2865 (Daniel Bourdeau's wave 9, 15 Nov 2026) says no decipherment; a web search on
28 Nov 2026 (Spinelli, Cariati, Urrea, 1512, cifra) found none. Urrea's own cipher letters of 1512-13 (catalogue
1074, 1075, RAH) were not compared.

## Checks not passed or not run

- `docs/_validate.py` was first not run (Project Gutenberg answered 503 on 28 Nov 2026 about 04:55 UTC). In the cold
  check (28 Nov 2026, about 05:25 UTC) it was run once, without `--write`, on the same Gutenberg texts fetched from the
  gutenberg.pglaf.org mirror (`CYPHER_CORPUS_ROOTS`) and the archive.org texts of it-nunziature. Result, model
  it-cinquecento: 712 read tokens, 35 types; reading -2.236 per letter, random keys at most -3.312 (z 4.7), shuffled
  refit at most -2.864, but the annealer from a random key on the real text reached -2.217, better than the reading:
  **underdetermined** (the letter model cannot tell this reading from a fitted key on so short a text). It is not
  recorded in `profile.json`, and "statistical test" is not claimed. The held-out test is the evidence.
- `docs/_check_reading.py` rates the reading files "not a reading" (clean-sentence share 0.21 for A, 0.29 for B, 3
  and 4 of 14 sentences, after the cold-check edits). README Conventions say the checker points at weak sentences but is not the verdict. The
  class stays "read in part" because the cipher runs read as Italian sentences in A1, A2.01-03, A2.06-A3.01 and most
  of B, with holes in the others (A2.04-05, B3.02-04). A reviewer may judge otherwise.

## Files

`transcription/`, `glosses.md`, `key.tsv` (second reader's names), `key_reader1_names.tsv` (as tested),
`decrypt.py`, `decryption_reader1.txt`, `decryption_reader2.txt`, `reading_words.tsv`, `plan/`, `verification/`,
`scripts/`. Reproduce: `python3 decrypt.py key.tsv transcription/reader2_transcription.txt`. No images are in the
folder.
