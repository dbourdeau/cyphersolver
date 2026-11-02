# Castelcicala (London, Paris) to Naples, 1816–1823: ASNa Esteri 2337 — catalogue 166 and 167

Status: in progress

**22 Oct 2026, reading audit** (George Lasry's test: can a reader build coherent sentences and translate them?):
* **Read**: R9571 and R9589 (Paris, Sept and Oct 1823), from their contemporary interlinear decipherments
  (`transcripts/R9571.txt`, `R9589.txt`), which read as continuous Italian. 244 of 9,428 groups (2.6%). English
  translations still to be added.
* **Decoded, not read**: the other 23 despatches. `reading_partial.txt` has unread code groups between nearly every
  pair of known words (2 of 24 sentences clean, `docs/_check_reading.py`); R9566 p. 3 and R9569 have only fragmentary
  glosses. The 45-47% figure is key coverage, withdrawn as a reading figure. Method now read from existing
  decipherment (the two glossed letters); the key rebuilt from adjacent plaintext stays the work done on the rest.

**22 Oct 2026, re-read** (REREAD_BRIEF, batch mix1, Claude Opus 5.5; `reread_log.md`): the 23 decoded-not-read
despatches checked for an existing text (no gloss beyond R9566 p. 3, R9569, R9571, R9589; no edition; code book not
online) and measured per document: key.tsv covers 0.19-0.68 of the groups, and outside the glosses no run of known
groups is longer than 14. The open retry step was done on the best unglossed stretch (R9566 p. 3 ll. 10-14, the
continuation of the Floridas passage): 17 of 37 groups stay open and no new value could be fixed, the alphabetical
runs being too short to bracket them. R9569's gloss now reads as one sentence ("... ed io ho motivo di credere di no,
e che [...] la suddetta elezione la Francia gli darebbe l'esclusiva"), one of about ten. All 23 stay decoded, not
read; blocker no-key-material (the 1816-19 code book, ASNa Esteri).

Outcome: read in part (21 Sept 2026). Code structure, correspondents and dates established; key rebuilt from four
contemporary interlinear decipherments; 45% of the groups in the target letters get a value, but no letter reads
through. Attempted, open for the rest.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. R9586 and R9588, two
undated Castelcicala letters in a second code (values 100–1100), are a different cipher, with their own page
([`targets/r9586/`](../r9586/), docs/r9586.html); their `transcripts/` and `cipher/` files moved there. This entry keeps
the 25 documents in the Segreteria di Stato code. Coverage recounted on them: 4,340 of 9,286 groups (46.7 %).

Catalogue 167 (R9553, R9555–R9557, R9582–R9586, seen first, below) and catalogue 166: "Marchese di Ciscello? Principe di Castelcicala? (Paris) to unknown recipient, 15 ciphertexts",
DECODE R9554–R9588 (ASNa, Ministero degli affari esteri, busta 2337, items 5–39).

## Who and when

- Sender: Fabrizio Ruffo, principe di Castelcicala, Neapolitan ambassador in London and then Paris. He signs
  R9562, R9566, R9569, R9571, R9579, R9587 and R9589.
- **"Marchese di Ciscello" is the recipient, misread.** The address reads "Eccmo Sig.r Marchese di **Circello**
  ... Napoli" (Tommaso di Somma, foreign minister) on R9554, R9558–R9566 and others. The 1823 letters (R9569–R9571,
  R9589) go to Cavaliere Luigi de' Medici. So DECODE's "unknown recipient" is known.
- Dates from the headings: London 26 Sep, 4 Oct 1816 (R9579, R9558); Paris 17, 19, 23 Oct, 30 Nov, 1 and 3 Dec 1816
  (R9559, R9560, R9587, R9561, R9566, R9562); several undated (nos. 2589, 2814, 3388/3588, 3721, 4086); Paris
  4, 8, 11? Sept and 9 Oct 1823 (R9569, R9571, R9570, R9589). R9553/R9555–R9557 (London, Paris 1816) and
  R9582–R9585 (1817–19 fragments) are further letters in the same code.
- Page order in the images is not reading order: R9579 runs P2, P3, P1, P4; R9569 P2, P1; R9561 starts at P2.
  R9566 holds despatch 3874 (P3, P2, P4) plus a fragment in another hand (P1, P5, P6).

## The code

- Numeric groups 1–~2450 with dots, one code for 1816 and 1823. Units are syllables, common words and names
  (el-e-zione, pon-ti-fi-ca-to, cas-ti-gli-one, par-lan-do-gli; Francia 2353, Spagna 2054, Duca 1529).
- Homophonic: di = 1112 / 2211, del = 2082, ere = 1836 / 2381, pa = 1201 / 2363.
- Two-part but with **local alphabetical runs**: 2201 che, 2205 ci, 2211 di, 2221 fi, 2230 l, 2231 l', 2232 la;
  2082 del, 2083 dell', 2084 della; 2045 quella, 2049 questo; 2161 is, 2162 Isola; 1111 detta, 1112 di; 1919 no,
  1920 non; 2445 ter, 2448 ti, 2450 to. Across runs the order is scattered.
- **Nulls:** a group written with a fifth figure (21900, 18900, 16480, …, ~100 cases) stands where the
  contemporary gloss has nothing. 1531 is probably a null too (ele-1531-zione = elezione beside ele-va-zione).
- R9586 and R9588 are in a different code (values 100–1100, faint pencil syllabic glosses); split off 14 Oct 2026 to `../r9586/`.
- Some pages (R9554 p1, R9561 P4–P7) have a stroke over nearly every group: a later decoder's ticks, recorded only
  where sparse.

## Cribs used

Contemporary interlinear decipherments, all in busta 2337:
- R9566 p3, first ten lines (despatch 3874, 1 Dec 1816): "questo Ministro dell'Interno Conte Decazes che gode
  sempre del più gran favore presso del Re di Francia ha avuto una conferenza col Ministro di S.M. Cattolica Sig.r
  Onis al suo passaggio per qui, nella quale parlandogli della cessione delle Floride, e di quella di cui si è
  parlato dell'Isola di Cuba all'Inghilterra gli ha insinuato destramente…"
- R9571 (8 Sept 1823): France wants Cardinal Castiglioni as Pope; the Duc de Laval blamed; no accord between
  France and Austria on the election.
- R9569 (4 Sept 1823) and R9589 (9 Oct 1823, the Spanish king's liberty; the Duc d'Angoulême not back for two
  months).

## Key and reading

`key.tsv`: 162 values, graded G (glossed, 90), X (glossed and confirmed in a second context, 18), I (inferred
here, 54). `apply.py` decodes; `reading_partial.txt` is the partial decode of every record (unverified; I values
may be wrong, e.g. "il Sr troppo l d'An ta" in R9579 is surely a name). Coverage 45% of target groups.
`solve.py` (it-modern LM candidate scoring) did not discriminate: contexts too sparse, segmentation unknown.

What would move it: hand-reading the 1816 letters against the Florida/Cuba and Decazes crib themes, one letter at a
time, extending runs by alphabetical bracketing; or the code book itself (ASNa Esteri, or Borbone 1666, whose
consular keys R9532–R9541 are on DECODE but are for 1859–60).

## Prior work

DECODE: Non-decrypted. Web search (21 Sept 2026) found no printed decipherment.

## Files

- `decode/fetch.py`, `decode/views_9532_9591.jsonl` (DECODE metadata); images and record pages git-ignored (not public domain).
- `transcripts/R*.txt` transcriptions (with glosses, headers, notes); `cipher/R*.txt` group-only.
- `corpus.py`, `key.tsv`, `apply.py`, `ctx.py`, `solve.py`, `reading_partial.txt`, `profile.json`.

## First pass (catalogue 167)

**Correction to the first pass.** The "decrypted siblings in box 2337" were not all 1850s: R9569, R9570, R9571
and R9589 are Castelcicala's Paris letters of Sept–Oct 1823 in this same code, three with contemporary
interlinear decipherments, and R9566 p3 (1 Dec 1816) has one too. Those glosses are the crib used above.
R9553 is headed "Cifra della Segreteria di Stato": the ministry's general code.


(First pass, 21 Sept 2026, catalogue 167 only; superseded by the section above.)

## What the records are

DECODE R9553, R9555–R9557, R9582–R9586 (ASNa, Ministero degli affari esteri 2337_4…2337_37), 13 images, fetched
with the shared DECODE cookie (images git-ignored in `img/`, metadata in `decode/`).

- Sender: Fabrizio Ruffo, principe di Castelcicala, Neapolitan ambassador (London in 1816, Paris 1815–1832);
  signed "Il Principe di Castelcicala".
- Recipient: **not unknown**. R9553 is addressed "Ecc.mo Sig. Marchese di Circello, S. S. S., Napoli"
  (Tommaso di Somma, Secretary of State for foreign affairs). DECODE leaves the receiver blank.
- R9553 is headed "Cifra della Segreteria di Stato" and numbered 2314: the ministry's general code, not a
  personal one.
- Dates on DECODE: 1 Apr, 3 Jun, 6 Sep, 30 Oct 1816 (London/Paris), 14 Nov 1817, 3 Apr, 13 Jul, 28 Oct 1819; R9586
  undated. The 1819 letters end in clear with "Parigi li …".

## The cipher

A numerical code, groups 14–2460, dots between groups, no word division visible. Almost all groups lie in
1350–2460; low groups (14, 40, 86, 97, 154, 222…) are rare. Some groups in R9585 carry a trailing 0 (15680,
18300, 22321?, 23530, 5810), probably a mark on the base group. Repeated phrases inside one letter (R9553:
"1901 2445 1652 1633" twice, "2358 1726 1454" twice, "1999 1531" four times) show a codebook of words or
syllables, not a letter cipher. 331 groups transcribed from three pages (`transcription.txt`), 208 distinct:
far too few for a ~2,500-entry code to be broken ciphertext-only.

## Where a key could come from, and what was checked

- **Box 2317 plaintexts** (DECODE's note). The only box-2317 record on DECODE is R9549 (2317_1). Its cipher pages
  (a 1798 "Cifra di Vienna" despatch with a clear version, and a letter signed "de Baptiste") use a different
  code: their frequent groups are 441, 486, 563, 1144, 1951, none of which is frequent here, and they stop at
  ~1999. So the box-2317 plaintexts on DECODE do not belong to these ciphertexts.
- **Decrypted siblings in box 2337** (R9550–R9552, R9568–R9581, R9589–R9590) are 1850s–60s telegrams and letters
  (e.g. R9550 Massone, Washington 28 Oct 1859, syllabic code with interlinear reading). Different period, different
  code; not tested further.
- **Print.** Web search (Castelcicala + Circello + cifra/dispacci 1816–1819) found biographies (Treccani DBI) but
  no edition of the ciphered despatches. Not in Tomokiyo's Cryptiana index as far as searched.

## What would move it

The 1816–19 "Cifra della Segreteria di Stato" codebook, or Circello's deciphered copies, in ASNa (Esteri, the
Paris legation series or the Segreteria's cipher office papers). Failing that, a full transcription of catalogue
166 (15 more records, 51 pp., same box, same sender, probably the same code) would roughly quadruple the text,
still short of what a ciphertext-only attack on this code size needs.

## 23 Oct 2026: verification 3 (explicit-hole score)

The v3 sweep scored R9571 on `transcripts/R9571.txt`, where the code-group lines are interleaved with the gloss
(0.577): a false alarm. The contemporary interlinear decipherment (the "P:" lines) is now joined into running text in
`transcripts/R9571_reading.md`: 1.0 explicit-hole and plain (5/5 sentences). Keeps read; the entry's `reading` points
at it, and its stale "decoded, not read" note (left from the first audit pass) is removed.

## Verification 5, 23 Oct 2026

Plain-bar check (Italian 1823): R9589 had been scored on `transcripts/R9589.txt`, gloss lines interleaved with code
groups and notes (plain 0.385). Its contemporary interlinear decipherment is now running text in
`transcripts/R9589_reading.md` (English `_en.md`): plain 0.8, explicit 0.8; keeps read.

## Remaining gaps

Decoded, not read (reading audit, 22 Oct 2026; re-read 22 Oct 2026, reread_log.md): unread groups between nearly every pair of words in each; the
blocker is the code itself (about half the groups have no value, no codebook online, no gloss on these records).

- R9553 (1 Apr 1816), decoded, not read - blocker: no-key-material
- R9554 (undated), decoded, not read - blocker: no-key-material
- R9555 (3 Jun 1816), decoded, not read - blocker: no-key-material
- R9556 (30 Aug 1816), decoded, not read - blocker: no-key-material
- R9557 (6 Sep 1816), decoded, not read - blocker: no-key-material
- R9558 (4 Oct 1816), decoded, not read - blocker: no-key-material
- R9559 (17 Oct 1816), decoded, not read - blocker: no-key-material
- R9560 (19 Oct 1816), decoded, not read - blocker: no-key-material
- R9561 (30 Nov 1816), decoded, not read - blocker: no-key-material
- R9562 (3 Dec 1816), decoded, not read - blocker: no-key-material
- R9563 (no. 2814), decoded, not read - blocker: no-key-material
- R9564 (no. 3388/3588), decoded, not read - blocker: no-key-material
- R9565 (no. 3721), decoded, not read - blocker: no-key-material
- R9566 (1 Dec 1816; gloss on ten lines of p. 3 only), decoded, not read - blocker: no-key-material
- R9567 (no. 4086), decoded, not read - blocker: no-key-material
- R9569 (4 Sep 1823; syllable gloss with gaps, p. 2 out of focus), decoded, not read - blocker: no-key-material
- R9570 (11 Sep? 1823), decoded, not read - blocker: no-key-material
- R9579 (26 Sep 1816), decoded, not read - blocker: no-key-material
- R9582 (14 Nov 1817), decoded, not read - blocker: no-key-material
- R9583 (3 Apr, year cut), decoded, not read - blocker: no-key-material
- R9584 (13 Jul 1819), decoded, not read - blocker: no-key-material
- R9585 (28 Oct 1819 or 1817), decoded, not read - blocker: no-key-material
- R9587 (23 Oct 1816), decoded, not read - blocker: no-key-material
- main-code groups without a value (55% of target groups) - blocker: no-key-material; two-part code of ~2,450 groups; 162 values from four interlinear cribs; solve.py LM scoring did not discriminate
- the 1816-19 Cifra della Segreteria di Stato codebook - blocker: needs-physical-access; not on DECODE (R9532-R9541 are 1859-60 keys); ASNa Esteri

Closed (taken out of the open list, 23 Oct 2026): R9571, R9589 English translations: written (transcripts/R9571_en.md, R9589_en.md); the not-attempted line was stale

## Escalation

- [x] siblings: box 2337 R9550-R9591 and box 2317 R9549 opened; 1823 glossed letters found
- [x] clear-pages: interlinear decipherments on R9566 p3, R9569, R9571, R9589 used as cribs
- [x] known-keys: R9549 (box 2317) and Borbone consular keys R9532-R9541 checked: different codes
- [x] print: web search, Treccani DBI, Tomokiyo: no edition found
- [x] key-rebuild: alphabetical-run bracketing and LM candidate scoring (solve.py); 54 inferred values
- [x] retry (22 Oct 2026): hand-read the best unglossed stretch (R9566 p. 3 ll. 10-14) against the Decazes/Floridas crib with the alphabetical runs; 17 of 37 groups stay open, no new value fixed (reread_log.md)

## Dudout corrections, 29 Oct 2026
- DECODE R9549 (box 2317) values stop at about 1254, not 1999: the clerk writes 2 with a looped tail. Still a different code from R9586/R9588 (1100-1399 = 44% of groups against 0.3%). On the images '268 111 294 808' has 294, not 398; 863 'tan' and 867 'tal' are correctly transcribed.
(Brice Dudout, research/dudout_2026-10-29/; his findings, not re-checked here.)
