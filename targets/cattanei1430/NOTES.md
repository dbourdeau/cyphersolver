# Francesco de' Cattanei (Rome) to Gianfrancesco Gonzaga, 13 and 21 February 1430 (DECODE R1854 images 4-5)

Read 22 Sept 2026 (key recovered from the ciphertext alone). Split on 14 Oct 2026 from `targets/r1854/` under the
one-key rule (George Lasry, 14 Oct 2026): DECODE R1854 holds four letters to Gianfrancesco Gonzaga in four ciphers.
This entry is Cattanei's two letters, one key (image 5 is the verso of the 21 Feb letter, photographed upside down).
The other letters of the record, each a different cipher with its own page: image 2 (`targets/r1854/`, Rome 9 Aug
1428), image 3 (`targets/mutiliana1428/`, Forlì 6 Nov 1428), image 1 (`targets/malatesta1428/`, Pandolfo Malatesta,
not solved). The solver and helper scripts are in `targets/r1854/`; images are git-ignored there (`decode/`, `img/`
in the main checkout) and not reproduced (Archivio di Stato di Mantova).

| image | date | language | signs | read |
|---|---|---|---|---|
| P4 (I8414) | Rome, 13 Feb 1430 | Latin | 1,537 (`p4v2.txt`, `ct_p4.txt`) | 1,505 |
| P5 (I8415) | Rome, 21 Feb 1430 (verso) | Latin | 199 (`p5v2.txt`, `ct_p5.txt`) | 199 |

Together 1,704 of 1,736 signs (0.982), re-counted 5 Oct 2026. Reading: `reading_p4.md` (P4 + P5); notes on the
second pass `p4v2_notes.md`.

## Method

Ciphertext-only anneal (`../r1854/solve.py`, Latin model) gave Latin at once ("sollicitabo bullam", "galeotam"); a
subagent second pass then checked every sign against the image: 209 edits, look-alikes split (slanted b = i vs
rounded = o; η vs 9; ⊢-o = q; o†o = x; Λ-type d), `key4_v2.txt` (earlier stages key4_1-key4_4). Signs for et, con,
-rum; x written cx (dicxit, reducxit). Rescoring outputs `occ_9.txt`, `occ_b.txt`; anneal logs `run_p4*.txt`.

## Content in brief

- P4 (Rome, 13 Feb 1430): Cattanei's news: Carlo (Malatesta?) on a marriage alliance with King Louis (of Anjou); a
  galley of Giovanni de Orlandis took a Catalan ship, lost at Gaeta (5,000 ducats); Castile presses Aragon; an envoy
  of the lords of Rimini left empty-handed; the archbishop of Patras offered the temporal lordship (of Patras) to the
  Venetians with the pope's licence, and the cardinals answered it was better lost than given to Venice; Niccolò da
  Tolentino's chancellor; the abbot's excommunication lifted; six Bolognese citizens expected.
- P5 (Rome, 21 Feb 1430): the Rimini envoys Astorgio and Bartolomeo appeared before the commissaries with a mandate
  and authenticated copies of bulls; "credo parum iuvabit"; in clear "denarios non habeo pro expensis".

## 30 Sept 2026: "Patras io(?)" is "Patrasio"

For the quotation list (George Lasry), the "[…]" after "Patras" in P4 L14 was re-examined. The two signs are `I bo`
(slanted b = i, rounded b = o; each attested dozens of times in P4 with those values), so the key gives
"...depatrasiocumlicencia". Read as one word: "archiepiscopus de Patrasio", a Latin form of the Italian name
Patrasso (grade: letters H from the rebuilt key, word division I). The phrase now reads without a gap: "dominus
a[rchi]episcopus de Patrasio cum licencia domini nostri dare volebat temporale dominium dominio Venetorum".
Corrected in `reading_p4.md`, `p4v2_notes.md` and the page. No count changes.

## 5 Oct 2026

- P4 L20 "debert onorio" re-divided with every letter as keyed: "creditur Nicolaus cito de Bertonorio debeat
  recedere" (Bertinoro; 12 signs). P4 L22 "domicus noster" = dominus noster (c for n, 7 signs).
- P4 L04 "leonebi": the image shows `t +` (e b) clearly, so "Leonelli" (Leonello d'Este) is not forced; left open.

## Decrypt audit, 16 Nov 2026

`research/decrypt_audit/` re-applied `key4_v2.txt` to `p4v2.txt` and `p5v2.txt` and compared the letters with
`texts/R1854-P4_reading.md` and `texts/R1854-P5_reading.md`. It reported 103 of 272 words departing (P4 91 of 240,
P5 12 of 32), almost all of them a t present in the reading and absent from the decrypt.

- Cause, audit artefact (nearly all): the sign for t is written `=` in the transcriptions, and its key line is `==t`.
  The audit's key parser splits a line at the first `=` and also strips a leading `=` from a sign name, so the sign
  `=` is lost and every t it stands for (115 occurrences in P4 and P5) drops out of the audit's decrypt. The key file
  is complete: every token of the two transcriptions except the composite `?` of P4 L02 has a line in it (`d=?` is
  the declared unknown). `../r1854/show.py` splits at the last `=` and reads the file correctly. A key file in
  another layout does not help, because the audit strips the leading `=` in every layout; nothing was changed in the
  key file.
- With the key file parsed as `show.py` parses it (the audit's own comparison otherwise unchanged), 9 of 273 words
  depart (P4 7 of 241, P5 2 of 32). A letter-by-letter comparison of the same decrypt with the two readings gives
  these differences that carry no bracket in `texts/R1854-P4_reading.md` or `texts/R1854-P5_reading.md`:
  - abbreviations expanded (3): P4 L01 `nrum` printed "nostrum" and L02 `dni` printed "domini", P5 L01 `dnorum`
    printed "dominorum". `reading_p4.md` writes these n(ost)rum, d(omi)ni, d(omi)norum; the parentheses were dropped
    when the sentence readings were made. `p4v2_notes.md` records a macron over the first.
  - a stated but unbracketed change (2): P4 L11 `aeragono` printed "Aragonum", and P5 L02 `producxerut` printed
    "producxerunt" (macron for n). Both are named in the header comment of the reading file, not marked in the text.
  - letters changed with no mark (4): P4 L06 `solicitabo` printed "Sollicitabo" (the transcription has one `Z`; these
    notes and `p4v2_notes.md` also quote the word with two l); L12-L13 `offerenu` + `um` printed "offerendum" (d
    for u); L22 `domicus` printed "dominus" (the 5 Oct entry above records c for n, and `reading_p4.md` keeps
    [domicus]); L13 `maleotentus` printed "male[c]ontentus", where the bracket covers the c and not the n.
  - a letter dropped (1): P4 L26 `secx ciues` printed "sex ciues", while dicxit, reducxit and ducxerunt keep the cx.
  Inside marks, so not counted above: `a` + `mhi` printed a[rchi]episcopus (mhi replaced), and L21 `demean becaris`
  printed "[?Meana] [?becaris]" with an a the decrypt does not give.
- The header comment of the P4 reading says "Latin spelling as the key gives it", and that of P5 "spelling as the key
  gives it"; the cases above are exceptions to both. The wording of the reading files was not changed here.
- Changed: nothing but this section and one step in `profile.json`. The audit's own figure stays 103 of 272 until its
  parser accepts a sign named `=`.
- Not checked: the images (the audit compares files only), so whether `solicitabo` and `offerenuum` are slips of the
  writer or of the transcription is open. `outcome.texts[1].decryption` points at `reading_p4.md`, which holds lines
  1-2 of image 5 only; line 3 is decoded in `texts/R1854-P5_reading.md`.

Marked on 16 Nov 2026. In `texts/R1854-P4_reading.md` five places were bracketed where the key does not give the
letters, in the file's own convention ([x] = letters supplied), with no letter changed: Sol[l]icitabo, Aragon[um],
offeren[d]um, male[c]o[n]tentus, domi[n]us (L22). One place is left unmarked because a bracket cannot show a dropped
letter without adding one: "sex ciues", where the key gives secx; the header now says so. The expansions are stated
as a convention in the headers and not marked word by word: nostrum and domini (P4), dominorum and producxerunt
(`texts/R1854-P5_reading.md`, where nothing was marked). Header lines changed: in P4 "Latin spelling as the key gives
it" now lists these exceptions and the Aragonum note reads Aragon[um]; in P5 the sentence on spelling names the two
expansions. In every one of these places the key's own word may be what the letter has; only the marks say so, the
wording stands. Page `docs/cattanei1430.html`: the annealer's output quoted as "sollicitabo bullam" corrected to
"solicitabo bullam" (`run_p4la.txt`); the same quotation in the Method section above is the reading's spelling, not
the annealer's. `v2_score.py` (la) on the P4 reading: hole rate 0.095 before, 0.110 after
(the new brackets count as holes; `read_share` 0.906 in the profile and the 90.6% on the page were not changed); P5 0.024
before and after.

## Remaining gaps
- P4 L04 "leonebi … re[∂]bs", L05 "aisignata pure st", L11 "uniei … cille", L14 "a-mhi" (~32 signs) - blocker: illegible; signs re-read at 10-13x, 786-px scan, values not fixable from single occurrences

## Escalation
- [x] siblings: R1853 register and the Mantova key records on DECODE opened (see `targets/r1854/NOTES.md`); no 1430 key; the other R1854 letters are other ciphers
- [x] clear-pages: P5 is the verso of the second letter, not a clear copy; only "denarios non habeo pro expensis" and the date are clear
- [x] known-keys: the register keys tried; none fits
- [x] print: web search; nothing printed for these letters
- [x] key-rebuild: key rebuilt ciphertext-only, then every sign checked against the image (209 edits)
- [x] retry: open spots re-read at 10-13x (22 Sept) and from the re-fetched images (5 Oct 2026): L14, L20, L22 read
