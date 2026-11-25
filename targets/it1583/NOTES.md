# BnF italien 1583 ff. 68 and 70 — two Sforza cipher letters of 4 May 1446 (DECODE R7898, R7899 P1)

Status: in progress. f. 68 read; f. 70 decoded, not read (reading audit, 22 Oct 2026).

**20 Nov 2026: CTTS sign-level re-transcription, to test whether the ciphertext-only key holds** (section below;
project `research/ctts/projects/it1583/`, git-ignored; README row in `research/ctts/README.md`; report
`research/ctts/it1583_ctts_report.pdf`). A blind Fable 5.2 first pass, corrected by Claude (Opus 5.5) on enlarged
crops, then compared with Lasry's CTTS project box by box. **The key does not change**: no class value moves; every
place where the new transcription would give another letter was settled for Lasry's reading by the image and the
sense, or stays open with neither reading making words. **One reading gain**: f. 68 line 10 has a sign written above
the line with a caret, between *octo* and *dece*, that Lasry's project has no box for; it is the o-sign (#13), so
the line reads *octo o dece* ("eight or ten"; the edition had supplied "or" in translation only). Two transcription
proposals for the open classes (not adopted into `lasry2026/`, whose checksums `verify.py` guards): #40 + (11) on
f. 68 line 9 are one continuous flourish, not two signs, and without them the line reads *li confidenti respondemo
che*; the #35 at the end of f. 68 line 1 is a line-end stroke, not the R of the two line openings.

**6 Nov 2026: catalogue 1309 (ff. 148, 151, 152, Venice 7 Dec 1446) is `../contucio1446/`.** Only f. 148 (R7911,
Contucio) has cipher; it reads with the Vincentius key, ASMi cart. 1597 no. 14 (R5314), 225 of 226 signs. ff. 151-152
(R7912, R7913) are clear. The R7900/R7901 pair was checked there for the key's code word *stat*.

**29 Oct 2026: the Duke's own cipher slips of Nov-Dec 1446 in this volume (ff. 110-158) are `../visconti1446/`**, read
with his key (DECODE R5323, second copy R1857 image 17), not the f. 68/70 alphabet. Correction to the ark noted in
`bnf.htm`: btv1b10033686w is ital. 1587; ital. 1583 is not on Gallica (BnF Archives et manuscrits gives microfilm
MF 16151 only). 19th-c. copies of several of its letters are in ital. 1597 (Gallica btv1b10037396j).

**23 Oct 2026, re-read (REREAD_BRIEF, batch b29)**: f. 70 still *decoded, not read*. DECODE R7899 fetched (P1 the slip;
P2 an address leaf to Francesco Sforza, not f. 70's); every sign re-checked against Lasry's overlay, no label changed;
**#30 adopted as a null** (8 boundary occurrences in both letters; not written into `lasry2026/ctts/key.txt`, whose
checksums `verify.py` guards). Partial reading `texts/f70_partial_reading.md` (0.50 clean sentences; explicit holes 0.70),
English `texts/f70_en.md`, log `texts/f70_reread_log.md`: sentences 1 and 3 hold, the news clause of lines 4-5 and the
signature do not. Sibling sweep: R7900-R7915 (16 records, ff. 89-158) fetched and viewed; none uses this alphabet.
**Found: R7900 (f. 89, Angelus, 30 Sept 1446, headed "Cum cifra Vincentii") and R7901 (f. 90, "Explication du
chiffre") are one despatch in cipher and in clear** -- a contemporary decipherment of the Vincentius cipher (the
cart. 1597 no. 14 key), a different alphabet from ff. 68/70; a lead for a separate ital. 1583 target and a DECODE
note (R7900 Non-decrypted, its clear text is R7901).

**22 Oct 2026, reading audit** (George Lasry's test): f. 68 (R7898) builds sentences from line 2 to line 11; its ? runs sit at line openings (per-document C overturned to B). f. 70 has holes in every clause of lines 1-5 and an unread signature: *decoded, not read*. Class read in part kept; fraction_read 0.9432 (assigned) -> 0.514 (tokens in f. 68).

Earlier status (before the 22 Oct 2026 reading audit): read in part (George Lasry's CTTS key, PR #60, 20 Oct 2026; written up as `docs/it1583.html`). Earlier:
attempted, closed unread (21 Sept 2026).

## Result (20 Oct 2026): George Lasry's CTTS key, contributed in PR #60

Credit, in George Lasry's words: "Transcribed by George Lasry with CTTS (CrypTool Transcriber and Solver), who also
generated the initial key; the key and reading were improved by Astra and Fable 5.1." Contributed in
https://github.com/dbourdeau/cyphersolver/pull/60; files in `lasry2026/` (`full_letter.md` edition and English
translation, `edition.json` box-aligned edition, `ctts/` native CTTS exports, `ctts/key.txt` the shared key,
`verify.py` checks every box, export and checksum: passes).

- **Method: key recovered from ciphertext-only.** The initial key came from CTTS on the ciphertext; no outside key or
  plaintext of the cipher passages was used (the 208 Sforza keys of September do not fit, and no decipherment exists).
  Note: the first cipher line reads as Mazzatinti's 1883 heading ("resposta facta ad qvelo ha referito zorzo del
  maino" vs "Risposta a quanto ha riferito Zorzo Maino"); the PR does not say it was used as a crib, so it is taken
  as confirmation, not as the source of the key.
- **One key, two letters.** f. 68 (R7898): reply to Zorzo del Maino about Count Francesco's obligations, "our
  security", and a request for a written list of eight or ten trusted persons. f. 70 (photographed on R7899 image P1,
  Mazzatinti: Vincenzo Amidani to Francesco Sforza, Milan): action against Cremona, Venice's stance, help and defence,
  troops in the field; deciphered date line "mediolani die qvarto mai". Signature block unread.
- System: homophonic letters (up to six signs for I and O) plus word/syllable signs CHE, CON, ET, PER, QVA, SE;
  provisional (8)=l, (24)=n, (16)=in. No word division.

### Measured (this session, `measure_sense.py`, `validation.tsv`)

| | cipher tokens | types | assigned | read as sense |
| --- | ---: | ---: | ---: | ---: |
| f. 68 (R7898) | 425 | 52 | 399 (93.9%) | 380 (89.4%) |
| f. 70 (R7899 P1) | 402 | 48 | 381 (94.8%) | 341 (84.8%) |
| both | 827 | 65 | 780 (94.3%) | 721 (87.2%) |

Token counts measured with `docs/_check_profile.py --measure lasry2026/cipher_tokens.txt --drop-first` (and
`companion/`). "Assigned" = the CTTS key gives the token a value (4 of them provisional). "Read as sense" leaves out
segments with a `?` and assigned letters that do not form words (isolated n/o/l at boundaries, f. 70's signature
block of 24 tokens, the untranslated "se mono", "do", "da" and the extra "o o"). 87.2% < 95%: **read in part**.
Statistical validation (`docs/_validate.py`, it-cinquecento order 4): reading -2.070 per letter; random keys -3.761
(z 5.7); shuffled-refit best -2.544; annealer power -2.415; verdict **pass**.

## CTTS re-transcription (20 Nov 2026)

Done by Claude Opus 5.5 at the request of the session coordinating the CTTS gold-standard work (George Lasry's advice
of 20 Nov 2026); the user watched and made no readings. Pipeline: `research/ctts/README.md`.

- **Images**: DECODE R7898 (f. 68) and R7899 image P1 (f. 70), both binarized scans, 3702 px wide, fetched with the
  project's DECODE cookie (git-ignored). The lines are about 37 px apart and touch, so a new script,
  `research/ctts/segment_dense.py`, upscales 2x, finds the lines as peaks of the ink profile, assigns each blob to
  the nearest line and cuts touching strokes at the column with least ink: 4 bands and 650 candidate boxes on f. 68,
  3 bands and 479 on f. 70.
- **Blind first pass**: two Fable 5.2 agents, one per letter, saw only the bands, the box overlays and a shape
  notation (`NOTATION.md`); not `f68_signs.txt`, `f70_signs.txt`, the key, the decryption or Lasry's files.
  f. 68: about 418 signs in 57 codes, 48 doubts, 10 split and 82 part boxes; f. 70: about 398 signs in 49 codes, 66
  doubts, 3 split and 111 part boxes, 6 missed signs. About 12 minutes each, in parallel.
- **Correction** (about 17 min): the first pass's own part and clear-text runs merged by script (102 merges, 817
  boxes, 128 types); the two agents' codes for the same shape unified (f. 70 `+r`=T, `Fr`=F, `J`=f, `t`=c', `r`=y,
  `Z`=J; 97 signs); every doubtful, split, part and missed sign (125) checked on an enlarged crop with no overlay and
  decided (97 label decisions, `decisions.tsv`); splits, merged parts and missed signs fixed (74 box operations,
  `geomfix.log`). Computer use of the CTTS window was requested and came back denied; at the user's choice the box
  fixes were written to CTTS's own files and the project was opened in CTTS, which restored it cleanly (834 boxes,
  83 types, all assigned).
- **Outside comparison** (about 14 min), only after that: Lasry's CTTS boxes fitted onto the same DECODE images
  (scale 1.00, median offset 2 px) and matched box by box; then fixes where the image and the decoded text side with
  Lasry (`fix5c.log`, 68 changes): the dot groups `::` and `.:.` are cipher signs (Lasry #10 = z, #15 = a; "zorzo",
  "facta"), 31 of them, which the first pass and the CTTS pass had dropped as separators because the notation sheet
  said so; b joined to a cross is one sign (per, 7); C with ÷ on its bar (#25) and 9 with a barred m (#36) are one
  sign each (the parts never occur apart, and f. 70 writes #25 as a barred E without dots); the tall h joined to a
  loop (se) is not the barred loop (et); 18 single signs retyped (s for 8, h for b, B2 for B, T for +, p for Q2 ...).
  Final project: f. 68 425 signs, f. 70 400 signs, 89 types.
- **Sign error rates** (alignment, (S+D+I)/N, notations mapped by alignment; `score.py`, `scores.json`):

  | | f. 68 | f. 70 |
  | --- | ---: | ---: |
  | first pass, raw box labels, vs final | 24.2% | 24.8% |
  | first pass with its own notes vs final | 12.7% (7.5% without the dot groups) | 9.2% (7.7%) |
  | CTTS pass before the outside comparison vs final | 10.8% (5.5%) | 6.8% (5.1%) |
  | final vs Lasry's CTTS tokens | 1.9% | 5.2% |
  | final vs the September draft (`f68_signs.txt`, `f70_signs.txt`) | 14.1% | 14.6% |
  | Lasry vs the September draft | 14.4% | 15.1% |

- **Does the key change? No.** 27 boxes where the new transcription's class would give another letter than Lasry's:
  21 settled for Lasry by the image and the sense ("hai resposto per parte", "per rispecti de li oblighi", "in campo",
  "advisata", "tamen per fare", "mediolani die qvarto mai" ...), 3 were naming differences only, 3 stay open
  (f. 68 line 10 B or B2 in "?intita"; f. 70 line 1 last sign, a yogh with a stem rather than the #30 shape; f. 70
  line 6 "altra v[a]ia", where the #15 is a dot group crossed by a descender, and a separator would give "via").
  Lasry's merges of shapes are mostly one sign in two hands (z/2 #6, >/>2 (2), C÷/E #25, V2/Bo #38, a/j #27); his
  splits that the CTTS pass had merged (se/et, the crosses #14/#18/#37, h/b, s/5/8, (6)/8') are all borne out.
  (20) holds two shapes in f. 70 (Y 11, 8' 3), both read N: a possible split, no change of value.
- **The open classes**: #25 and #36 are compound signs, as Lasry boxed them; #40 + (11) are one flourish (proposal
  above); the line-end #35 of f. 68 line 1 is not the R shape; (16) "in" (written above f. 68 line 6) has two loops
  side by side and is not the (6) shape; (24) "n" is the same gamma-like sign both times. f. 70 lines 1-5: the open
  signs (25), (19), (26), (4), #25 are confirmed as distinct shapes, nothing new. f. 70 signature: the new
  transcription differs in four or five signs under and beside the stamp (one sign Lasry reads #12 has no box; a9 for
  e + #30; p for c), and neither gives a name.
- **Decryption re-run** with Lasry's key on his tokens plus the inserted sign: only f. 68 line 10 changes,
  "? n o octo dece per che" -> "? n o octo o dece per che".

## Transcription doubts
Checked 20 Nov 2026 on enlarged crops without overlay (`research/ctts/projects/it1583/check/`), against the decoded text, and against Lasry's CTTS transcription (an independent transcriber).
- inserted sign above the line (f. 68 line 10, between octo and dece, caret below) - read: o-sign (#13), "octo o dece"; checked: image, decode, transcription; Lasry's project has no box for it; the shape is the tick-curve-bar sign
- B or B2 (f. 68 line 10, "?intita le parte") - read: open, B (one bar) on the image, Lasry B2 (t); checked: image, decode, transcription; neither "insitale" nor "intitale" is a known word
- flourish (f. 68 line 9, after "li confidenti") - read: one stroke, probably not a cipher sign; checked: image, decode, transcription; Lasry boxes two signs #40 and (11), both unresolved; without them "li confidenti respondemo che"
- line-end sign (f. 68 line 1, after "maino o") - read: stroke with a hook drawn out into a line, unresolved; checked: image, decode, transcription; Lasry #35, but the two line-opening #35 are an R
- inserted sign above the line (f. 68 line 6, "savere [in] qvesto") - read: two loops side by side with a tail, Lasry (16) provisional in; checked: image, decode, transcription; not the (6) shape, so (16) is not merged with (6)
- last sign of f. 70 line 1 ("contra cremona [?]") - read: open, a barred yogh with a stem (the v-sign) on the image, Lasry #30 null; checked: image, decode, transcription; v makes no word before "credendo"
- dot group crossed by a descender (f. 70 line 6, "altra v[a]ia") - read: .:. (a), open; checked: image, decode, transcription; a separator here would give "via"
- 8 or s (f. 70 line 3, under the clear word) - read: s (top loop open), "che e fato"; checked: image, decode, transcription; the first pass had read 8 with this doubt
- B or B2 (f. 70 line 7, "tamen") - read: B2 (two bars); checked: image, decode, transcription; "tamen" needs t
- small open phi or p (f. 70 line 8, "mediolani die") - read: p; checked: image, decode, transcription; "die"
- cross with a blob on the left (f. 70 line 8, "qvarto mai") - read: T (turnstile); checked: image, decode, transcription; "mai"
- b-like signs (f. 70 lines 4, 5, 7) - read: h twice (crossed by tails), b2 twice (round bowl); checked: image, decode, transcription; "piv", "in campo"
- stain and stamp area (f. 70 lines 6 and 8) - read: the signs after clear "pontt" (F, c', c) and the strokes beside the stamp stay doubtful; checked: image, decode, transcription; a colour BnF scan would decide them

## Remaining gaps
- 47 unresolved cipher occurrences in 14 sign classes (#30 x8 adopted as a null 23 Oct 2026, leaving 39 in 13; #25 x10, (4) x6, (6) x5, #36 x4, #35 x3, (22) x3, (25) x2, six classes once): mostly at line and paragraph openings (#35 (6) (4) opens f. 68 lines 1 and 9) - blocker: no-key-material; probably nulls, titles or abbreviations, but a language-model pass over both letters could not fix any of them, and only the sibling 1446 letters could add occurrences; 20 Nov 2026 CTTS re-transcription: #25 and #36 confirmed as compound signs, #40 + (11) (f. 68 line 9) look like one flourish rather than two signs (proposal, not adopted), the line-end #35 of f. 68 line 1 is not the R shape
- f. 70 signature block after "mediolani die qvarto mai" (24 tokens: p ? v a r qva c e et e ? s m n ? s t a ? ? m r) - blocker: no-key-material; assigned letters do not form the name; Mazzatinti's attribution to Vincenzo Amidani is not confirmed by the cipher
- provisional values (8)=l, (24)=n, (16)=in (4 occurrences) and doubtful words (f. 68 "?intita"; f. 70 "se mono", "do", "vaia" (the #15 there is a dot group crossed by a descender; as a separator it would give "via"), "raconmando", extra "o o") - blocker: no-key-material; each rests on one or two occurrences
- clear-text supplies: f. 68 line 5 end "[aya? ...]"; f. 70 "[fornendo?]", "[ques?]te" (written in clear over damaged or crowded strokes) - blocker: illegible; only a binarized scan of f. 68 and a DECODE photograph of f. 70; a colour BnF scan would decide them
- f. 70 lines 1-5: decoded, not read - blocker: no-key-material; re-read 23 Oct 2026 (b29): labels confirmed on the image, #30 = null adopted, the clause of lines 4-5 rests on (25), (19), (26), #25, (4) with no key value; none of the sibling 1446 records R7900-R7915 uses this alphabet; sense hypotheses (25)=Duca, (19)=ordine, (26)=gente flagged for review

## Escalation
- [x] siblings: 23 Oct 2026 (b29): R7900-R7915 fetched and viewed, none in this alphabet (R7900/R7901 = the Vincentius cipher with its clear text). Earlier: f. 70 (the next leaf, on R7899 P1) is already deciphered with the same key; the seventeen other 1446 cipher records from ital. 1583 (R7899-R7915, ff. 75-158) were not opened that session: they need the DECODE login and a CTTS sign-level transcription of several thousand signs, a separate target. They are the one route to more occurrences of the open classes.
- [x] clear-pages: f. 68's clear phrases are the letter's own clear text, not a decipherment; no decipherment on R7898 or R7899
- [x] known-keys: September 2026, all 208 Sforza key records on DECODE (ASMi cart. 1591, 1597, 1598); 1597 no. 14 is the same family but a different alphabet, no. 17 (1447) different; none is this key
- [x] print: Mazzatinti 1883 gives the headings only; no edition or decipherment found (September search)
- [x] key-rebuild: `extend_open.py` tried every letter, the word values and null for each of the 14 open classes and the 3 provisional ones, scoring both letters with it-cinquecento: no letter value wins by a margin that would justify it (e.g. (6): o vs e, margin 0.8 nats); the scorer prefers null for most, which is consistent with nulls but biased toward them, so nothing adopted
- [x] retry: 20 Nov 2026: CTTS sign-level re-transcription from the DECODE images (blind Fable 5.2 first pass, correction on enlarged crops, box-by-box comparison with Lasry's project): the key does not change; one inserted o-sign added (f. 68 line 10, "octo o dece"); see the CTTS section. 23 Oct 2026 (b29): f. 70 re-read sign by sign on R7899 P1, texts/f70_reread_log.md. Earlier: the provisional l / n / in rechecked in the same pass ((24): t vs n, margin 0.7; (16): null vs in, 1.7): left provisional

## History: the 21 Sept 2026 attempt (failed)

### The document

- BnF italien 1583 (Archivio Sforzesco, documents 1433–1500, bought 1867), f. 68; DECODE R7898, 1 image,
  "Non-decrypted", no metadata. A slip pasted on a guard, numbered (21.) and 68/22.
- Dated at the head in clear: "M°cccc°xlvj die iiij° may" = **4 May 1446**.
- Mazzatinti's inventory (Archivio storico lombardo X, 1883, p. 230; OCR in `asl1883.txt`, line ~10470, from
  archive.org `archiviostoricol10cava`): "f. 68. Risposta a quanto ha riferito Zorzo Maino (4 maggio). In cifre."
  So it is a reply (almost certainly from Francesco Sforza's side, then condottiere in the Marche) to what his agent
  Giorgio (Zorzo) del Maino reported. Next entry: "f. 70. Lettera di Vincenzo Amidani a Fr. Sforza (Milano 4 maggio).
  In cifre."
- Mixed text: clear Lombard Italian with ciphered stretches. Clear phrases read:
  "cetera Che nuy no sapiamo [c] questi ne cerchamo ne domandamo [c] tocha ad nuy cerchare questo, ma solamente
  cerchamo con lo nome de dio [c] nostra raxone(?)"; "gli havemo rechiesto siano contenti fargli quello e dicto et
  ad quello se refferemo"; "[c] voglia essere contento mettere per scripto [c] se tra loro no gli sera noma uno
  che no habia [c] debitamente lo debiamo havere".

### Cipher (as seen in September)

Graphic-sign cipher, 404 signs in 26 types after merging diacritic variants (draft transcription
`transcription.txt`, codes in its header; cipher-only `f68_signs.txt`). Two signs at 12 %, two at 7 %, flat tail.
The cross-circle sign (V) stands before clear clauses several times; in the related key below it is "de".
Repeats: FpBHcdSp (×2), 8zBprJFp (×2), xJpg (×4), FEpS (×3), FpBHc (×5).

### Attempts (21 Sept 2026)

1. Unconstrained homophonic annealing (it-cinquecento, clear text as context): collapses to "iiii".
2. Capped homophones, then nulls allowed: degenerate / nonsense.
3. One-to-one swap annealing (solver checked on a synthetic 400-letter Italian cipher: solved in 1 of 3 restarts):
   16 restarts, nonsense.
4. Word patterns: FpBHcdSp fits "uisconti", but the other repeats contradict that key.
5. **f. 70 found**: the slip at the top right of DECODE R7899 image P1 is f. 70 (pencil "1446 4 Mai"), Amidani's
   letter, all cipher, same sign family, a different hand. Draft transcription `transcription_f70.txt` (390 signs,
   31 types). Annealing on it alone: nonsense.
6. **Sforza keys on DECODE**: all 208 key records of ASMi Carteggio Sforzesco cart. 1591, 1597, 1598 downloaded
   (`fetch_keys.py`, `dl_keys.py`; images git-ignored) and scanned at thumbnail size; the 15th-c. copies at the
   head of cart. 1597 (nos. 2–36) read by heading and alphabet.
   - 1597 no. 14 (R-record name `Carteggio_Sforzesco_scat._n.1597_14`), an 18th-c. copy: "Angelus cum cifra
     Vincentij", used with "Johannes de Stavolis, Augustinus, Baptista, Matheus, et Vincentius". Same family as
     our signs: 2–5 homophones per letter, a sign for every vowel+consonant syllable (ab, ac, ad … uz), word signs
     (de = ♀, che, per, quale, con, ma, quello, perché, …), names (la S. V., lo Duca de Milano, Signoria Veneta),
     nulls. But its letter signs (a = o, ϙ …; e = ƅ, 5, ʒ; o = q …) are not the frequent signs of f. 68 or f. 70
     (⊧, ϕ, ƀ, barred ʒ). Not this key; it explains why simple-substitution solving failed.
   - 1597 no. 17: "M°cccc°xlvij … Zifra oratorum Ill. et Ex. Comitis … ad Ser.mum dnum Aragonum Regem"
     (1447, Sforza's envoys to Alfonso): different signs.
   - Nothing headed Maino or Amidani. cart. 1591 and 1598 are 16th–17th c.

### Why it was closed in September

The system has syllable and word signs over homophonic letters, and the only scan is binarized, so the diacritics
that may separate signs are unreliable. About 800 signs across two hands is not enough for a ciphertext-only
attack on a system like that. What would reopen it: the Maino/Amidani key of 1446 (look in ASMi Sforzesco
cart. 1597 at full size, and in Cerioni, *La diplomazia sforzesca*, 1970, vol. 2), or a colour scan of
ital. 1583 ff. 68–70 from the BnF for a sign-exact transcription.

### Related leads (not worked)

DECODE R7899–R7915 are seventeen more 1446 cipher records from BnF ital. 1583 (ff. 75–158): Nicodemo Tranchedini,
"Angelus" (Simonetta?), Stavoli and others. Some may be in the 1597 no. 14 key (Stavoli and Vincentius are
named on it). Worth a separate target.
