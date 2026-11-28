# Plan: Narváez's key 313, unchanged, on six unread letters of the felicista network (CEHM-Carso, Fondo DCXXI)

Written by an AI agent (Claude Opus 5.5) on 25 Nov 2026, about 19:50 EST, before any cipher run of these letters is
transcribed or decoded under this plan. No person has checked it. Hashed with `shasum -a 256 PLAN.md > PLAN.sha256`.

## What was seen before this plan (stated so that the order can be judged)

- The 24 page images below were looked at once, at reduced size (1,000 px), to sort them; four handwritten slips were
  seen in the same pass.
- Seen in that pass, without trying to: in DCXXI.5.442.1 the pencil digits "3133133" over the run GHOBWHP (f.1), a
  pencil word over the run OFALDR (f.1), a pencil name under the signature run M. FPUWFV (f.3); in DCXXI.6.576.1
  ink and pencil words written between the lines of folios 1-2; the slip DCXXI.6.624.1.0001 (read at a glance: it is a
  handwritten list of names and phrases signed J. W. Wellington). While sorting, the agent decoded one run in its head
  (5.442.1's signature run FPUWFV); nothing else was decoded.
- Before today: the CEHM catalogue summaries of 6.576.1, 6.624.1, 7.657.2 and 8.731.1 as quoted in our wellington1922
  NOTES (names: Ricardo Suárez Escalante, Luis Corona, José Siliceo, Ricardo Lobato, Pomposo Bonilla, Federico Córdoba,
  Cástulo Pérez; 8.731.1 = Fidencio E. López alias Wellington). The full catalogue records will be opened only after
  decoding.
- The key cannot be tuned (it is fixed); what these exposures could bias is the transcription of a doubtful sign.
  Hence the rule below: a sign settled only with help from the decode makes its word a hole.

## Material (CEHM-Carso, Fondo DCXXI Archivo de Félix Díaz; private study copies in sources/raw/narvaez_push_2026-11-25/cehm/)

Sorted on sight:
(a) typed letters with cipher material - the test material:
- L1 DCXXI.5.442.1.0001-0003: signed M. [cipher] (catalogue: Cortez), 7 Apr 1922, to José González; capital-letter runs.
- L2 DCXXI.6.576.1.0002-0008: 25 Aug 1922, to José González, P.O. Box 1549, N.O.; many capital-letter runs (image 0009
  does not exist: 404 on 25 Nov 2026 19:44 EST).
- L3 DCXXI.6.624.1.0002-0003: J. W. Wellington, 5 Oct 1922; hyphenated groups of numbers and letters ("05-FLN-5-K-...").
- L4 DCXXI.7.647.1.0002: Wellington, 30 Oct 1922 (red typing); hyphenated groups of numbers and letters.
- L5 DCXXI.7.657.2.0004-0006: Wellington, 7 Nov 1922; hyphenated number-letter groups and runs typed in red capitals.
- L6 DCXXI.8.731.1.0001-0002: n.d. (day lost) 1922, to José González; capital-letter runs.
(b) handwritten leaves (later check only; not read closely before decoding is done): DCXXI.6.576.1.0001 (slip with
names and an address), DCXXI.6.624.1.0001, DCXXI.7.647.1.0001, DCXXI.7.657.2.0001-0003; and the interlinear pencil/ink
words on the typed pages of L1 and L2.

## Key (fixed, unchanged)

Narváez's rule as in targets/wellington1922/key.txt: alphabet A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z (27);
cipher = plain shifted forward 3, 1, 3, 3, 1, 3, ...; decipher = shift back 3, 1, 3, ...; the cycle starts with 3 at the
first letter of each run. A "?" (unreadable sign) holds its place in the cycle. No other key, phase or alphabet is tried
in this round.

Two cycle variants, both pre-registered, both reported:
- **A (continuous):** the cycle runs on through the whole run, across spaces and line breaks (as in wellington1922).
- **B (restart at visible word breaks):** the cycle restarts at each visible space inside a run (as sanchez1922 does at
  every word). Where a run has no visible break, B = A.
- For hyphenated number-letter groups (L3, L4, L5): numbers are left as they are and do not advance the cycle; A runs
  the cycle on through all letters of one hyphen-joined chain; B restarts it at each letter group between hyphens.

**Choice per letter:** variant with the higher C2 trigram score on the first third of the letter's runs (runs in page
order, rounded up), then frozen for the whole letter; tie or no difference -> A. The other variant's scores are reported too.
Restarts at word starts that are not visible (the Wellington post hoc kind) are not part of either variant; a word that
reads only with such a restart is a hole (may be noted post hoc, labelled, not counted).

## Runs (what is transcribed)

- A run = a stretch of capital letters typed as one unit that is not clear Spanish as written (capitals that read as
  Spanish as typed, e.g. "SEIS CIENTOS MILLONES", "CALLES", "N.O.", are clear text and are not decoded).
- A single hyphen at a line end followed by capitals on the next line continues the run; any other punctuation (. , ; :
  dash strings, a hyphen not at a line end) ends it, except inside hyphenated number-letter chains (L3-L5), where the
  chain is the unit.
- Overtyped sign: the top layer if clear, else "?" and a doubt. Typewriter ñ/Ñ written Ñ.

## Transcription method

- T1: this agent, from full-resolution crops (scratch only; no crop leaves the scratch folder).
- T2: one helper agent (Claude Opus), blind: it gets the images and these run rules, not T1, not the key, not any decode,
  and is told not to open the handwritten leaves or the catalogue.
- Both files hashed (SHA-256, with `date`) before any decoding. Differences are settled by this agent on the image,
  without the decode; unsettled signs stay "?" or [x|y] doubts. A sign settled only after the decode was seen makes its
  word a hole.

## Controls

- **C1 (decoder check, must pass first):** the four runs of Narváez's printed paragraph 2 of folio 2 of the Wellington
  letter DCXXI.6.588.1 (Narváez 2015 pp. 123-126; cipher strings as printed: FPPWJPJFPWFVGFSDSWLEDDUJRVULHNH,
  UFSXCÑLDD, PPVHÑYLFVXTXÑULOBVSBUDFXWSDUEHÑMHPPBFPPHMHOFPWPVDVPDMFIDWBPWSDVDHPEHPUDÑ, VPEUFWRERIBÑWBVGFHÑFOHÑWRT)
  must decode under variant A to his printed decipherment letter for letter (his "(sic)" letters included).
- **C2 (chance):** Spanish letter-trigram model from sources/raw/ill_photo_leads_2026-11-23/archivosantander14bogo/
  archivosantander14bogo_djvu.txt (Archivo Santander vol. XIV, Bogotá 1918; text folded to the 27 letters, accents
  dropped, Ñ kept, non-letters removed, one continuous stream). Score = mean log P(c3 | c1 c2), add-one smoothing
  (N(abc)+1)/(N(ab)+27), over all trigrams inside the letter's runs (runs under 3 letters skipped; trigrams never cross
  runs). For each letter: 313 against 1,000 random shift triples (each shift 0-26; random.seed(20261125)), and the rank
  of 3-1-3 among all 27^3 = 19,683 triples (same variant).
- **P2 (words):** best segmentation (dynamic programming) of each run's decode into words from a list of the Santander
  text (folded words seen at least twice, length >= 2, plus a, e, o, u, y), maximising letters covered by words of
  length >= 3; coverage = those letters / all letters of the letter's runs. Controls: the same on 100 random triples
  (random.seed(20261126)).

## Pass marks (per letter, on the variant chosen as above)

- Pass = C2 (3-1-3 above every one of the 1,000 random triples; a draw equal to 3-1-3 itself is not counted against it)
  AND P2 (coverage >= 0.50 and above the maximum of the 100 controls). Rank among the 19,683 triples is reported.
- A letter with fewer than 60 decodable letters is "too short to decide", whatever the scores.
- Otherwise a **miss** for that letter. A miss is reported as a miss; no other key is searched in this round; index of
  coincidence or visible structure may be given as a labelled diagnostic only. A miss does not rule out 313 under some
  other phase rule, nor show what the system is.

## Counting (letters that pass)

Strict rule as in wellington1922 scripts/count_words.py: a word is clean only if every letter is as the key gives it;
a word with any supplied, dropped, changed or swapped letter is a hole ({got/intended}); a word holding a doubtful sign
(T1/T2 not settled on the image, or settled with the decode) is a hole; a proper name is clean only if it is spelled the
same in the clear text of these letters, in another run, or is a common Spanish name or place; otherwise [?NAME], a
hole. Unread stretches are estimated as their letters / the mean letters per clean word (at least 1). Report per
letter: cipher word places, clean, holes, share; both minimum (stretch = 1) and estimated.

## Order of work

PLAN + hash -> T1 and T2 (hashed) -> settle -> final transcription hashed -> C1 -> decode both variants, C2, P2 ->
verdicts -> reading and counts for passes -> only then: handwritten leaves, interlinear words, CEHM catalogue records
91350, 91616, 91712, 91758, 91779, 91927 (agreement reported as "fits"; every divergence listed).
