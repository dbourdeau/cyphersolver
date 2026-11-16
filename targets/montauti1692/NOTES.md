# montauti1692: Cosimo III's autograph letter cipher in his letters to Montauti (Penn Ms. Codex 533), key rebuilt from the interlined despatches of Codex 534

Status: in progress (folder only, no page; contributed by Andrew Beling, with AI agents)

Holder: University of Pennsylvania Libraries, Kislak Center for Special Collections. Ms. Codex 533 (36 autograph letters
of Cosimo III, Grand Duke of Tuscany, to his envoy Anton Francesco Montauti, 80 leaves); Oversize Ms. Codex 534 (279
despatches of the Florentine secretariat to Montauti, 1689-1699, signed "Il gran duca di Toscana"); Oversize Ms. Codex
531 and Ms. Codex 536 as context. All online with IIIF (`sources.md`).

## Result

- **The Grand Duke's two-sign letter cipher is rebuilt and tested.** In Codex 534 the secretariat wrote some letters in
  the same cipher that Cosimo uses in his own hand, and the recipient (Montauti or his secretary) wrote the plaintext
  letter over each group. A key built from those interlines (key v2, 22 groups for 19 letters) was frozen, then scored
  on an interlined letter it had not seen: **76 of 92 groups (82.6%) agree; 200 shuffled keys reach at most 35.9%.**
- **Cosimo's own cipher passages in Codex 533 are read for the first time, as far as we found.** They were transcribed
  twice (one pass blind), the 116 sign-level disagreements were checked on the image (112 settled, 4 left open), and the 35 runs were decoded:
  by this package's count 15 read whole, 15 in part, 5 not at all (`readings/runs_533.tsv`). By words, 30 of Cosimo's 87
  cipher words (34.5%) are sure, 42 of 87 (48.3%) with the two context-only values (`readings/words_533_strict.tsv`).
- **What the cipher hides is mostly his daughter's household.** Anna Maria Luisa de' Medici, Electress Palatine ("mia figlia",
  "mia figliola"), the Elector Palatine, Düsseldorf, the court and "toscani" there, a favourite lady of the bedchamber,
  and the Duke of Savoy.
- **The first letter (ff. 1r-1v, undated), in the independent verifier's words:** "In an undated letter partly in
  cipher (after the 1691 marriage), Cosimo III tells his envoy Montauti that the Elector Palatine has let him know of a
  report, written to the Elector, that Cosimo's daughter had written to Cosimo asking permission to return home and
  separate from her husband. Cosimo says such talk shames and offends his and his daughter's reputation, speaks of
  'such calumnies', and asks Montauti to use all his skill against it, if need be by a journey to Düsseldorf."
  - This is a report at second or third hand that Cosimo passes on and treats as calumny.
  - There is no explicit denial among the words read.
  - The person who wrote to the Elector is unread.
  - The letter has no date.
  - The clear text at 1r lines 5-6 and 11-13 needs a palaeographer before anything is quoted (so do 1v lines 1 and 3).
  - The standard accounts of the Electress call the marriage happy and mention no such report (section "History").
  - Nothing here says that the Electress asked to leave her husband.
- **The same cipher, bare, in the secretariat's letters of 1694** (Codex 534 ff. 114r-116v, Codex 531 f. 4r) reads at
  about 85-95% by the reading agent's estimate: the Duke of Savoy's offer of a daughter for the King of the Romans,
  Abbot Grimani at Vienna, the Elector of Cologne and Liège, a Bavarian-Polish marriage.

Full passage, marks and corrections: `readings/letter_1r1v.md`. Reading with a key rebuilt from a period decipherment
is not an independent solution of the system; Cosimo's own passages have no period decipherment anywhere we looked.

## Who read it before us

- **Montauti**, the recipient, read Cosimo's letters (that was their purpose). Nothing in Codex 533 is deciphered on the
  page: no interline, no marginal note, on any leaf.
- **The recipient's interlinear decipherments in Codex 534** (ff. 14r, 15r, 21r, 396v; Montauti or his secretary)
  read the secretariat's own letters in this cipher. The key here is rebuilt from them; their credit is in the profile.
- **No print found.** Checked: Stefano Casciu 2006 (read in full); Marcello Verga 2006 (read in full); the *Dizionario
  Biografico degli Italiani* (DBI) entries for Anna Maria Luisa (Gencarelli 1961) and Cosimo III (Fasano Guarini 1984);
  Riguccio Galluzzi, *Istoria del granducato*, vol. IV (1781, full-text search); Hermine Kühn-Steinhausen's 1938 article on the
  Düsseldorf festivities (only that article; her 1938 edition of the letters is under "Not read"); Neue Deutsche Biographie for Johann Wilhelm (Braubach 1974); Zacour and Hirsch's
  Penn catalogue (1965; cited from Penn's record, not opened). There is no DBI entry for Anton Francesco Montauti.
- **Not read:** Harold Acton, *The Last Medici* (1932, revised 1958): borrow-only copies; a HathiTrust in-volume search
  found no "Montauti" but the passages were not read. Kühn-Steinhausen's edition of the Electress's letters
  (*Düsseldorfer Jahrbuch* 40, 1938) and her 1939 biography: not online.
- **Unreachable:** the inventories of the Archivio di Stato di Firenze (Florence State Archive; every cultura.gov.it
  host refused connection on 14 Nov 2026) and the Medici Archive Project's database (login required). Either could
  hold the other side of this correspondence or a key.
- **Upstream repository:** no target for Montauti, Cosimo III or these shelfmarks. `research/leads.json` has one Cosimo
  III lead, no. 2076 (to Francesco Terriesi in London, matched on "cipher" in ArchiveGrid), unrelated.
  `research/medici_bia/README.md` lists **Oversize Ms. Codex 531** under "Leads looked at and not kept": Cosimo's
  1694-96 letters there carry "two-digit groups such as 13 14 16 19 25, some with superscripts" with a full
  interlinear decipherment, and the note calls the volume "a good key-rebuild source for the 1690s Florence-Vienna
  cipher". **This target is a different cipher.** Codex 531's interlined passages are in a dotted table of 1-3 digit
  groups with superscript marks (called System A in these notes). Codex 533 and the bare passages of Codex 534 (and one
  in Codex 531, f. 4r) use a run-on two-sign cipher with an eleventh sign, a w in the clerks' hands and a c with a loop
  in Cosimo's (System B). A 531 key cannot read 533. The System B key comes from Codex 534, which the upstream note
  does not mention.

What this target adds: the reconstruction of the Grand Duke's System B from the interlined letters of Codex 534, the
held-out test, the double transcription of Cosimo's runs, and the first reading of his cipher passages.

## The cipher (System B)

- **A letter cipher of two-sign groups.** The signs are the digits 0-9 and an eleventh sign, written by the clerks as a
  w and by Cosimo as an open c joined to a loop (often looking like c6 or c8). On f. 14r of Codex 534 the recipient
  wrote one letter over each group.
- **Few homophones:** a = 11 or w2, e = 21 or w4, o = 41 or 40 (and ww, by context); u/v = 51 or 91; i = 31 or w6.
- **Names are spelled out** ("signor Elettor Palatino", "Principessa", "Savoia"). Some groups with 0, 1 or three digits
  carry no letter and look like **code numbers** for persons or titles (in 534: 10, 110, 104, 106, 116, 13, 22, 27; in
  533: 14, three times after "la/della"). They are not read.
- **Cosimo's habits** (seen on the image): the second of two w-signs is often only an 8-like loop; the 5 has a hooked
  head with a descender that looks like a 9; one sign sometimes serves two groups (6 w w = 6w ww); doubled letters are
  often written once. The clerks share signs the same way (5w4 for 5w w4).
- **That Cosimo uses the clerks' table** is inferred, not attested: under the reading c+loop = w, his groups decode to
  the clerks' letters and give Italian. No interlined autograph letter was found.

## Key

| file | what | sha256 |
|---|---|---|
| `key/key_v1.json` | 20 groups, from Codex 534 f. 14r only (round 2) | 8bedce85... |
| `key/key_v2.json` | 22 groups, ff. 14r and 15r (round 3); frozen before the clean test | 64783ab8... |
| `key/key_v3.json` | v2 + w6 = i (f. 396v, one attestation) + 91 = u (f. 21r, read after the test) | bdc8b174... |
| `key/key_v3_context.json` | **context only**: ww = o, 62 = q; not under any interline | f5115d38... |

- **Source of every value**, folio and line in Codex 534: `key/key_entries.tsv` (written by `scripts/key_sources.py` from
  the pair files `key/pairs_534_f14r_f15r.tsv`, `key/pairs_534_f396v.tsv` and the test files).
- **The two context-only values** and every reading that depends on them: `key/CONTEXT_VALUES.md`. In the reading files
  a letter that rests on them is marked "+".
- **No q, j, x, y or k** is attested; z = 76 once.
- Order of freezing and testing: `key/FREEZE.txt`. Check: `python scripts/run_tests.py` (`test/run_tests_output.txt`).

## Tests

Plans written before each run: `test/TEST_PLAN.md`.

| test | key | held-out | result | 200 shuffled keys | caveat |
|---|---|---|---|---|---|
| Round 3, the clean test | v2, frozen | Codex 534 f. 21r (Florence, 5 Dec 1690), not used for the key. Cipher transcribed from crops with the faint interline blanked out and frozen (sha256 0727229d...) before the interline was read | **76 of 92 covered groups (82.6%)** match the interline | at most 35.9%, mean 23.9% | The alignment step (difflib) inflates the shuffled baseline. The misses are misreadings of the clerk's digits (56 read as 50 twice; probably 42 as 4w), not key errors. 91 = u was learned from this letter after scoring. |
| Round 2, the earlier test | v1, frozen | Codex 534 f. 15r (Florence, 20 Nov 1690), four interlined segments, 39 groups | 39 of 39 | at most 28.2%, mean 6.2% | The reader knew key v1 while reading the interline, so a reading bias cannot be excluded; one doubtful letter (s or g) was scored as unreadable. f. 15r pairs went into key v2 afterwards. |

Both test the secretariat's table. Key v3's two additions and the context values were not tested on held-out
material; Cosimo's use of the table is supported by the Italian it gives, not by a test.

## Transcription of Codex 533

- **Pass A** (`transcriptions/passA_forward.tsv`, forward, 850 signs): by the agent that knew key v2; not independent.
- **Pass B** (`transcriptions/passB_backward.tsv`, backward from 70v to 1r, 811 signs in 34 runs): a separate agent with
  no key, no earlier transcription and no access to pass A; its sign forms are in `transcriptions/B_digit_reference.md`.
- The passes agreed on 704 of pass B's 811 signs (86.8%; pass A has 850; `transcriptions/compare_AB_raw.txt`). The 107 differing places split into
  **116 sites** (`transcriptions/disagreements.tsv`); each was checked on full-size crops
  (`transcriptions/disagreements_settled.tsv`): pass B right 91, pass A right 17, mixed 2, neither 2, unsettled 4
  (35v line 0.635, signs 21-30).
- Frozen: first reconciled `transcriptions/reconciled_533.tsv` (pass B base with pass A variants, sha256 d1ec7443...);
  second `transcriptions/reconciled_533_v2.tsv` (every site checked on the image, 112 settled and 4 left open, sha256 d2866b78...). Earlier first-pass transcription
  (made before the two-sign unit was known): `transcriptions/codex533_firstpass_round2.tsv`.
- Decodes: `decode/decode_reconciled_keyv2.tsv`, `decode/decode_rec2_v3.tsv` (key v3: 303 of 401 groups take a letter,
  75.6%), `decode/decode_rec2_v3ctx.tsv` (with the context values: 318 of 401, 79.3%); `decode/flex_reconciled.txt` lists
  the letters each group could give under the allowed confusions.

## Readings, run by run

`readings/runs_533.tsv`: for each run the folio and line, the clear words before it, the groups, the letters (marked),
the Italian as decoded with holes, normalized Italian, English, and the share read. Per letter: `readings/L*_groups.txt`,
`L*_decode.txt`, `L*_it.txt`, `L*_en.txt` (written by `scripts/make_texts.py`; the first letter's `L01_it.txt` and
`L01_en.txt` are the verifier's text). The bare passages: `bare/P1-P4_*.txt`, `bare/bare_passages.md`.

| letter (Codex 533) | date line as read | cipher, normalized | read |
|---|---|---|---|
| ff. 1r-1v | none (breaks off) | l'El[e]ttor[e] Palatino; mia figlia mi havea; permission[e]; ritornare qua; separarsi; marito; mia et di mia figl[i]a | whole (7 runs) |
| f. 3r | "[L...] li 2[?] d'8bre[?]" | la [14]; la [14] o[..] | part |
| f. 19r | "Firenze li 2[?] [8bre?]" | "55 14", perhaps a plain number | not read |
| ff. 21r-22r | "Firenze li 23 di Giugno[?]" | [c]onte [..] (a name?); sono sodisfatt[i] del duca d[i] Savoia | part; whole |
| f. 25r | "Firenze li [1?] di Lug./Ag.[?]" | costà; addit[a]ssi(?); two runs not read | mixed |
| ff. 26r-27r | "Firenze li 11 d'Aprile 1693" (year probable) | servivi[..]; relation[e] del [eight code-like groups]; havrà [..] con l[..] | part |
| ff. 28r-29v | "Firenze li 25 d'Ottobre" | [mia?] figliola; corte; toscani | most |
| ff. 35r-35v | "Firenze li 14 [month?]" | fussi disgustat[o] del [..] della corte; per mezo della d[o]n[n]a(?) di camera favorita dell[a] [14]; mandarai(?) [..] | most |
| ff. 36r-37r | "[Firen]ze li [1/16?] d'Agosto" | not read | none |
| ff. 53r-55r | "Livorno li 13 di Marzo [1]693" | "il Spagna(?)", conjecture | part |
| ff. 56r-57r | "Firenze li 19 d'Ottobre" | mia figlia; viaggio a Dusseldorf | whole |
| ff. 62r-63v | "Firenze li 23 Sett.bre" | li tempi; [..] qualche facilità; ult[i]mo(?) | most |
| ff. 70r-72r | "Pisa li 17 Gennaio 169[3]" (last digit retraced) | agosto | whole |

**Counts.** 35 runs (34 plus the doubtful one on 19r). This package: 15 whole, 15 in part (5 of them most), 5 not read.
The round-4 working notes counted 15 whole, 14 in part, 6 not read; round 4b, after the image check, 16 whole, 17 in
part, 2 not read. The differences are calls on short runs with a code number (3r) or a single word (22r, 25r b, 36r).
Measured bounds: 40.2% of Cosimo's 403 groups (162) lie in runs read whole; 79.3% of the 401 groups in
`decode/decode_rec2_v3ctx.tsv` (318) take a letter value (78.9% if counted against 403); "about 60% read as
Italian" lay between and was our estimate. Measured by words (15 Nov 2026, `readings/words_533_strict.tsv`, after Daniel
Bourdeau's review of PR #665): 30 of 87 cipher words sure (34.5%), 42 of 87 (48.3%) with the context-only values
ww = o and 62 = q. A word is sure when every letter comes from frozen key v3, read on the signs as transcribed, with no
context-only value, no letter supplied or replaced by sense, no doubt mark and no unread group. Daniel Bourdeau counts
37 and 51 of 87; the difference is the seven words with a supplied or replaced letter (l'El[e]ttor[e], figl[i]a,
d[i], relation[e], disgustat[o], [d]ell[a], dell[a]), which README Conventions counts as holes. The first letter
(1r-1v) is 9 of 16 sure (Daniel Bourdeau: 11 of 16) and L70 (agosto, on ww = o) 0 of 1; both are read in part.

## History and significance

Kept apart: **(L)** what the letters say; **(H)** established history, with its source; **(I)** our inference.

- **(H)** Cosimo III de' Medici ruled Tuscany 1670-1723 (DBI, Fasano Guarini 1984). His only daughter, Anna Maria Luisa
  (1667-1743), was married by proxy in Florence on 29 April 1691 to Johann Wilhelm of Pfalz-Neuburg, Elector Palatine;
  the wedding was blessed at Innsbruck and the couple entered Düsseldorf on 19 July 1691 (Casciu 2006, p. 32; Galluzzi
  IV, p. 297; Kühn-Steinhausen 1938, p. 68). Casciu calls the marriage happy, built on real affection (p. 32); there
  were no children (one miscarriage, 1692; Casciu p. 35). She returned to Florence only as a widow, in 1717 (Casciu
  p. 40; DBI). The marriage was bound up with the Emperor's grant of royal treatment to Cosimo in 1691 and with the
  imperial contributions levied on Tuscany (DBI Gencarelli; Galluzzi IV, pp. 295-296).
- **(H)** Montauti was Cosimo's envoy at the imperial court in Vienna until 1699 and then Secretary of War (Penn's record
  of Ms. Coll. 180); the Codex 534 despatches run 1689-1699. He was among "her father's envoys" at the Düsseldorf
  carnival of February 1697 (Kühn-Steinhausen 1938, p. 72, citing the Electress's letter of 9 Feb. 1697, Florence State
  Archive, Mediceo del Principato 5835, doc. 63). Cosimo addresses him "Sig. Abate" in most of Codex 533 and "Sig.
  Marchese" in its last letters.
- **(L)** In Codex 533 Cosimo puts in cipher his daughter ("mia figlia", "mia figliola"), the Elector Palatine,
  Düsseldorf ("viaggio a Dusseldorf", 57r), the court and "toscani", a favourite lady of the bedchamber, and the Duke of
  Savoy. In the first letter the Elector tells him of a report, written to the Elector, that the daughter had written to
  ask leave to return and separate; Cosimo speaks of shame, of offence to his and her reputation and of "simili
  calunnie", and tells Montauti to act, if need be by going to Düsseldorf.
- **(H)** None of the sources opened mentions any wish, request or rumour in 1691-1700 that she would return or separate,
  nor a calumny about the couple (`history_sources.md`).
- **(I)** The letter therefore adds to the literature rather than contradicting it: what it records is a report, not a
  fact, and Cosimo treats it as calumny. Kühn-Steinhausen's own surmise (1938, p. 72) that the Elector wished to show his
  father-in-law's men that the daughter lived happily would fit an answer to such a report; no source makes the link.
- **(I)** Why it matters: the last generation of the Medici had no heirs, and the dynasty's end turned on Cosimo's
  children and their marriages; Anna Maria Luisa is the one who later secured the family's collections for Florence
  (Casciu 2006, title and theme: "Dal fasto barocco delle corti al Patto di famiglia"; the Family Pact itself was not
  re-checked here). Coded instructions from the father to his envoy about his daughter's marriage show how Cosimo handled
  that marriage privately, through an autograph channel kept apart from the secretariat, whose ciphered despatches in
  Codex 534 deal with Savoy, Liège, Poland and the imperial court. That division of channels is our inference from what
  reads so far.

## Reading review

Preliminary. `CONTRIBUTING.md` (14 Nov 2026): a reading merges only with a `reading_review` graded A or B,
"recorded by the reviewer, not by the author of the reading". The grades in `profile.json` (13 entries) were
written by Andrew Beling's own AI agents and are kept as preliminary grades: `by` is "Author's agents (Andrew
Beling, with AI agents)" and each note begins "PRELIMINARY: author's self-check, not a reviewer's grade. For a
maintainer to confirm or replace.", followed by the agents' own reading note. No grade letter was changed.

## Integration check (15 and 16 Nov 2026, pull request #665)

Checked when the pull request was reviewed; the contributor's commits are unchanged. An AI agent working for the
maintainers did this; no person has checked the transcriptions or the readings.

- **Tests re-run** (`scripts/run_tests.py`): the eight recorded hashes match; key v1 on f. 15r 39 of 39 (shuffled keys
  at most 28.2%); key v2 on the held-out f. 21r 76 of 92, 82.6% (200 shuffled keys at most 35.9%, mean 23.9%). As
  recorded. That each key and the f. 21r cipher were frozen before the interline was read is by the contributor's
  record.
- **Images.** Penn's Colenda manifest of Ms. Codex 533 answers without a bot check and carries the rights statement
  NoC-US with the attribution to the University of Pennsylvania Libraries. Crops of f. 1r (runs a to f, 69 groups) and
  f. 22r (run a, 28 groups) were fetched from Penn's IIIF server and compared sign by sign with
  `transcriptions/reconciled_533_v2.tsv`: all 97 groups agree at 1900 px across the page; one 6 or 0 in run c of 1r is
  not safe at that size. Not sampled: Codex 534 (the interlines that give the key, and f. 21r), the bare passages, the
  other runs of Codex 533.
- **Own decoder** from `key/key_v3.json` and the two context values gives the letters of `readings/runs_533.tsv` for
  those runs and of the four bare passages (`bare/P1_decode.txt` to `P4_decode.txt`).
- **Word count.** The review of 15 Nov 2026 counted 37 sure words of 87 (51 with the context-only values) and 11 of
  16 in the first letter, admitting words with a supplied or replaced letter. README Conventions counts a letter
  supplied where the cipher has nothing as a hole, and the one-digit rule does not apply to a key rebuilt here, so the
  contributor's recount stands: 30 of 87, 42 with the context-only values, 9 of 16 in the first letter
  (`readings/words_533_strict.tsv`, recounted here). The entries of ff. 21v-22r and 35r-35v now carry the count from
  that list (2 of 10, 6 of 15) in place of the estimate by groups. The shares of the four bare passages are still the
  reading agent's estimates.
- **Reading reviews, recorded by the reviewer.** Graded B: ff. 1r-1v, the clause of f. 22r, the two clauses of
  ff. 35r-35v, and bare passage P1. Graded A: bare passages P2, P3 and P4, each a whole sentence with only code
  numbers open. **Marked decoded, not read:** ff. 25r, 26r, 28v, 56r-57r, 63r and 70v. Their cipher words stand as
  the list gives them (f. 56r-57r *mia figlia* and *Dusseldorf*, all sure), but the clear text around the runs is not
  transcribed, so no sentence is shown and a reviewer cannot grade one. Transcribing the clear sentences of those
  leaves would let them be read in part.
- **Prior art and duplicates.** No target, catalogue entry or lead uses this key or these leaves.
  `research/medici_bia/README.md` looked at Codex 531 only and did not keep it; a cross-reference is added there.
- **Credit.** The contributor's role is now "new cipher with solution": Codex 533 was in no ledger.
- The folder stays `Status: in progress` with no page: the bare pages of Codex 534 are not attempted and Penn
  Ms. Coll. 180 Folder 114 is not seen.

## Limits

- By words, 30 of Cosimo's 87 cipher words are sure (34.5%), 42 with the context-only values (measured above).
- **Runs not read:** six by the round-4 count, five by this package's (19r, 25r a, 25r b, 26r b, 36r).
- **The block on 26r** ("relatione del" + 13 14 19 25 34 39 36 37) has no w-sign and only 1-3-9 digits: it looks like a
  different table (System A of Codex 531, or code numbers). Not read.
- **Dates:** the cipher letters carry place, day and month; a year is legible only on three (26r-27r "1693", probable;
  53r-55r "[1]693"; 70r-72r "169[3]", retraced in later ink). **The first letter has no date line at all.**
- **Blindness:** the verifier of 1r-1v had read the `_sources` note of `key/key_v3_context.json`, which names "ritornare
  qua", "Palatino", "marito", "Dusseldorf" and "havea"; its readings of those words are not fully blind.
- **Penn Ms. Coll. 180, Folder 114** ("Documents with code for diplomatic ciphers, 1689, 1694") was not seen. It would
  confirm the table, the context values and the code numbers.
- The bare 534/531 passages were read in one forward pass by one agent (backward only for 531 f. 4r and 115r lines 1-4).
- All readers are AI agents. No person has checked a reading.
- The clear text of Codex 533 is transcribed only around the cipher runs, and on 1r-1v; it needs a palaeographer.

## Decrypt audit, 16 Nov 2026

`research/decrypt_audit/detail.py montauti1692` could compare two of the 17 texts, the bare passages P1 and P2 (the others are under 100 letters): 23 of 63 and 28 of 50 compared words depart, 51 of 113 (45%). All 17 texts were then checked with an own read-only snippet: `key/key_entries.tsv` (26 groups, the two context-only values included) applied to each `*_groups.txt`, compared with `*_decode.txt`, and the decode compared with the CAPITALS of `*_it.txt`. The folder's scripts were not run.

- **Key against the decode files.** Of 892 groups, 781 take the key's letter as printed (91 = u is printed v six times); 77 have no value and are printed `?` or `[n]`; 27 letters, all in Codex 533, rest on a digit read differently from the transcription (96 as 56 m, 92 as 52 h, 68 as 6w t, 06 as 66 s ...) and carry `*` in `readings/L*_decode.txt` and `readings/runs_533.tsv`. Those are readings of the signs, not key values, and were not added to the key. Two places do not follow: L19 19r a, group 55 is printed `?` (the key gives l); L35 35r a, "d e l l a" has five letters for the four groups 46 21 55 11 (also in `runs_533.tsv`).
- **Cause D, clear text of the manuscript.** The phrases of P1 and P2 that the key does not produce ("che si supponeva fatta", "della sua di Lei", "non sono però a lungo andare", "le cose per la naturale") are the clerk's clear words around the cipher runs: in braces in `bare/P*_decode.txt`, in lower case in `bare/P*_it.txt`. No code number is given a value; all stay [n].
- **Clear words printed as cipher.** In `bare/P1_it.txt` nine clear words stand in CAPITALS (IL before [110], LE INCUMBENZE, AL [22], DA [106], DI MED.O, A [106], AL VESCOVATO, IL [22]), in `P2_it.txt` two (DURANTE LA), in `P4_it.txt` the DE of DEL [10]; `P*_decode.txt` has each of them in braces as clear.
- **Cause C, stated only as "normalized".** Consonants the cipher writes once are doubled without a bracket in 17 words: DELL'ABATE (twice), ALLA, L'ELETTOR (twice), NOZZE, DETTA, L'AUGUSTISSIMA, L'ELETTORALE, D'ACCASARE, DALL'ABATE, PROGETTI, TUTTI, S'OPPONGA, COLL'ABATE; PERMISSION[E] (L01), DUSSELDORF (L56).
- **Cause B, letters changed, dropped or supplied with no bracket in the reading file** (14 places, hand count): P1 GRIMANI (the last three groups are unread, the I is supplied), D'ACCASARE (decoded i dropped), SÌ IN (one decoded i printed twice), POLONIA (one of two decoded o dropped), LIEGI twice (decode liege), LE S[UE] NOZZE (the code group [22] between "si" and "noze" is not printed), L'AUGUSTISSIMA CASA E (decode "augustisime ca casea e": e printed as a, "ca" and an e dropped); P2 CIRCOSPEZIONE (decode "circospezt one", the group marked doubtful in `P2_groups.txt`); P3 S'OPPONGA (decoded i dropped); L01 L'EL[E]TTORE (decode "l e l t t* o r r": the final E replaces r; `L01_decode.txt` brackets it, `L01_it.txt` does not); L25 COSTÀ (decode "costaa"); L35 DELLA (above) and D[O]N[N]A(?) (decoded c dropped, final A where the group has no value).
- **Emended digits not marked in the reading files.** 23 words of `readings/L*_it.txt` hold a letter that rests on a re-read digit, marked `*` in the decode file but not in the reading: L01 L'EL[E]TTORE, MIA (twice), HAVEA, PERMISSION[E], MARITO; L21 MIL, SONO, DEL; L26 RELATION[E], HAVRÀ, CON; L28 FIGLIOLA, CORTE, TOSCANI; L35 DISGUSTAT[O], FAVORITA, MANDARAI(?); L56 MIA; L63 LI, QUALCHE, ULT[I]MO(?); L70 AGOSTO.
- **Cause F.** The script cannot see the braces and capitals convention, and the `+` (shared sign) and `?` marks of the group files split or hide a few groups.

Nothing was changed in the key, the group files or the readings; `key/key_entries.tsv` holds every value the folder establishes. After: 51 of 113, unchanged. Not checked: any group against an image, and `readings/letter_1r1v.md` and `readings/words_533_strict.tsv` against these counts.

**Marked on 16 Nov 2026.** Marks only; a script check confirmed that the letters of each file are the same before and after.

- Brackets, 9 places: `bare/P1_it.txt` GRIMAN[I], SÌ [I]N, LIEG[I] (twice), L'AUGUSTISSIM[A]; `bare/P2_it.txt` CIRCOSPEZ[I]ONE; `readings/L01_it.txt` L'EL[E]TT*OR[E]; `readings/L35_it.txt` DEL[L]A and D[O]N[N][A](?).
- Stars, 27 letters in 23 words of `readings/L01, L21, L26, L28, L35, L56, L63, L70_it.txt`: `x*` after each letter that rests on a re-read digit, copied from the `*` of the decode file of the same name. The starred letters of the decode files that fall in an unread stretch (28v a) or under an existing bracket (22r a, D[I]) have no letter in the reading and got no star.
- Re-cased, 12 clear words that stood in capitals: nine in `P1_it.txt` (il, le, al, da, di med.o, a, al, il), "durante la" in `P2_it.txt`, and the "de" of "deL [10]" in `P4_it.txt`.
- Left without a mark in the text, 5 of the 14 places, because the departure is a decoded letter or group that is not printed and there is nothing to bracket: D'ACCASARE and S'OPPONGA (elided i), POLONIA (one of two o), LE S[UE] NOZZE (code group [22]), COSTÀ (second a); likewise the "ca" and e dropped before CASA E and the c dropped in D[O]N[N][A]. Each is stated in a header line of its file.
- Header lines: a second comment line was added to `bare/P1-P4_it.txt` and `readings/L01, L21, L25, L26, L28, L35, L56, L63, L70_it.txt`, stating the marks, what "normalized" covers (consonants doubled without a mark, elided vowels) and, for the bare files, that the unedited output of the key is the `_decode.txt` file. No existing header line was changed.
- `scripts/make_texts.py` and `scripts/make_bare_texts.py` write these files; a re-run would remove the marks and header lines unless the scripts are changed first. They were not run or changed.
- `research/reading_audit/v2_score.py <file> it`, hole rate before and after: P1 0.287, 0.324; P2 0.069, 0.079; P4 0.038, 0.038; L01 0.215, 0.209; L21 0.333, 0.300; L26 0.333, 0.333; L28 0.182, 0.160; L35 0.353, 0.333; L56 0.273, 0.250; L63 0.333, 0.333; L70 0.400, 0.333. The falls in the L files are not real: the scorer splits a word at each `*` and so counts more words; it does not count a starred letter as a hole.

## Remaining gaps
- Codex 533 runs 19r, 25r a, 25r b, 26r b, 36r - blocker: no-key-material; letters decode in part but form no word, and no interline or key covers Cosimo's hand
- Code numbers 14 (533 3r, 35v), 13, 22, 27, 104, 106, 110, 116, 10, 90, 30, 39 (534/531) - blocker: open-codes; no interline gives them; Penn Ms. Coll. 180 Folder 114 not seen
- 26r c block of eight groups (13 14 19 25 34 39 36 37) - blocker: no-key-material; probably another table (System A) or code numbers
- Clear text of 1r lines 5-6 and 11-13, 1v lines 1 and 3 - blocker: illegible; needs a palaeographer
- 35v line 0.635 signs 21-30 - blocker: illegible; the two passes and the image check leave both readings open
- About 50 pages of bare System B in Codex 534 ff. 1-113 (listed in bare/bare_passages.md) - blocker: not-attempted; out of this package's scope, readable with key v3

## Escalation
- [x] siblings: Codex 534 paged (ff. 120-586 surveyed; ff. 1-119 on contact sheets); Codex 531 and 536 sampled; the interlined 534 letters are the key source
- [x] clear-pages: no clear copy or decipherment of any Codex 533 run anywhere in the volume (every leaf paged)
- [x] known-keys: the upstream medici_bia note's Codex 531 key is a different system (System A); DECODE searched for Montauti and Cosimo III by the 13 Nov sweep, 0 records
- [x] print: Casciu, Verga, DBI, Galluzzi, Kühn-Steinhausen's 1938 festivities article, NDB: nothing (her 1938 edition of the Electress's letters and her 1939 biography not read); Acton not read; Florence State Archive inventories and the Medici Archive Project unreachable
- [x] key-rebuild: w6 = i (interline f. 396v plus context), 91 = u (f. 21r), ww = o and 62 = q (context only, kept apart)
- [x] retry: every run re-decoded on the second reconciled transcription with key v3 and the context values; unread runs tried again in round 4b

## Images and rights

Penn's IIIF manifests mark Ms. Codex 531, 533 and 534 "http://rightsstatements.org/vocab/NoC-US/1.0/" (No Copyright -
United States: in the public domain under United States law; status elsewhere not determined), with the attribution
"Provided by the University of Pennsylvania Libraries." On that statement, and because other targets here commit
crops, four small crops of the cipher lines of 1r-1v (1200 px wide, 76-128 KB each) are committed in `images/` as the
evidence for the passage on the Electress: `c533_1r_l04-05_elettore_palatino.jpg`, `c533_1r_l06-07_mia_figlia_mi_havea.jpg`,
`c533_1r_l08-10_permissione_ritornare_separarsi_marito.jpg` and `c533_1v_l01-03_cipher_mia_figlia.jpg`. Rights statement:
No Copyright - United States (Penn), attribution "Provided by the University of Pennsylvania Libraries". No other image
is committed. The full images stay with Penn; folio numbers and manifests are in `sources.md`.

## Files

- `sources.md`: manifests, folios, rights. `history_sources.md`: the literature check.
- `key/`, `test/`, `transcriptions/`, `decode/`, `readings/` (with `readings/verify/`, the verifier's record), `bare/`,
  `scripts/`, `images/`, `validation.tsv`, `profile.json`.
- Scripts take paths as arguments or run from this folder: `run_tests.py` (hashes and both tests), `key_sources.py`,
  `make_texts.py`, `make_bare_texts.py`, `heldout_test.py`, `heldout_align.py`, `decode_runs.py`, `flex.py`,
  `compare_passes.py`, `disagreements.py`, `bare/bare_decode.py` (reads the round-4 working folder; kept as a record).

## Credits

Andrew Beling, with AI agents (Claude): the key rebuilt from the Codex 534 interlines, the tests, the two transcriptions
of Codex 533, the reading. The first letter was checked by a second AI agent of ours that read it blind from the images
first. The recipient's interlinear decipherments in Codex 534 (Montauti or his secretary, 1690) supply the key.
