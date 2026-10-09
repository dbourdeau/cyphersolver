# Catalogue 92: BL Add MS 4136 ff. 142-143 and 148v-149 (DECODE R9238, R9241) — NOTES

Status: in progress

Session 2026-09-21. DECODE lists these as "... to unknown recipient, 2 Jan 1562 – 15 Jan 1563". They are two
different letters in Patrick Forbes's deciphering file (Add MS 4136, see `targets/smith1562/NOTES.md`). Forbes copied only
the ciphered passages, numbered, with the letter named in the margin.

## R9238 (ff. 142-143): Coligny to Elizabeth, Villefranche, 12 Jan 1563: read at the time, in print

- Margin: "L'Amiral de France à la Reine d'Angleterre, [1]2 Jan. 1562/3". DECODE read the day as "2". Passages (1)-(35)
  in graphic signs (about 60 types), ending with the signature in cipher.
- The copyist's margin glosses fix the letter. "sins" and "desracine" at passage (9) are *il rallie les siens …
  de desraciner du tout l'evangile de ce royaume*, which is in the Villefranche letter of 12 Jan (Forbes, *Full View*
  ii 272-274, "Du camp a Villefranche, 12 Jan. 1563"), not in the 2 Jan letter from Meur (Forbes ii 247-249).
- *CSP Foreign* vi no. 76: "Admiral Coligni to the Queen … Camp at Villefranche, 12 Jan. Signed. Orig. almost entirely
  in cipher, deciphered." So the English decipherment is on the original (TNA SP 70), and Forbes printed the clear text.
- Closed as already solved. Key: DECODE R335 (TNA SP 106/1 f.69, 'A Cipher of the P. of Condé', endorsed 2 Dec 1562) has the same graphic signs; on it '&' and '14' are nulls and 'ω' = 'La Royne d'Angleterre', which is the heading line of f.142 ('… & 14 ω …'). Not applied beyond that check.
- f.143 lower half starts another "L'Amiral de France à la Reine d'Angleterre" letter ("Si …", passages (1)-(7)).
  That letter, and the passages (15)-(24) at the top of f.148, belong to catalogue 93 (R9237/R9239/R9240, "Amiral to
  D. Angle" = Coligny to the Queen of England). The glosses there ("delivr", "surprendre", "escrire") match Forbes's
  printed Coligny letters of late January (for example "surprendre le dict Lyon par escalade", Forbes ii c. 319).
  Catalogue 93 is very likely in print too. That was not checked passage by passage here.

## R9241 (ff. 148v-149): Catherine de' Medici to Paul de Foix, 15 Jan 1563: attempted, open

- Margin: "La Reine-mere de France a Mr de Foix Ambass: en Angleterre. 15 Jan 1563". Passages (1)-(4), about 1.3 pp.
  Paul de Foix was the French ambassador in London. The English evidently intercepted the letter.
- Not in Forbes ii, and not in *CSP Foreign* vi (all 60 pages of the volume searched for Queen Mother or Catherine with de Foix; every de Foix
  mention), and not in La Ferrière, *Lettres de Catherine de Médicis* i (1880), whose 15 Jan 1563 letters are both
  to Gonnor (from Chartres); vol. ii's letters to de Foix start in May 1563. No decipherment or clear copy is known.
- Sign set: Latin letters, digits, ligatures (ch, so, t6, qs, sz, ff …), a few two-digit numbers (30, 84, 83, 93 …) and
  clear words, probably nulls: *pour*, *assez*, *car*, and one uncertain *quog*. First-pass transcription:
  `qm_tokens.txt`, 952 tokens and 71 types by `_check_profile.py --measure`, IoC 0.035; b 90, 3 71, m 55, d 44.
- Keys ruled out by sight and by spot test: Throckmorton's first cipher (R9260 p.2, which also uses Latin letters and
  digits as values), his second (R9260 p.3), his third (R9262 p.1, which has French null words) and Croft's (R9261 p.2).
- Statistics: 'b' is never adjacent to itself, and 'm' never recurs within three tokens.
- Solver: homophonic annealing (`anneal3.py`, add-0.01 joint quadgrams from `lang/corpora`) recovers a 940-token
  synthetic control with 64 homophones almost fully. On the letter it finds no language (about −9.8 per char, collapsing
  to "ereseue…") in French or English, with or without nulls. So either the transcription merges or splits too many
  signs, or the system is not a one-token-per-letter homophonic (polyphonic values, syllables). Italian, Spanish and
  Latin corpora give the same null result (r4_*.txt). A letter-pair unit is unlikely: token parity within each passage
  is flat. A syllabic variant (SYL=1: a token may stand for one letter or one of 30 common French bigrams) is
  also negative (r5_syl.txt).
- Tooling note: the shared `lang` dense model (`fr-1530-despatches`, `en-modern`, order 5, no spaces) scores "eeee…"
  at −0.26/char, so an annealer on it collapses to runs of one letter. `anneal.py` shows that failure; use a
  joint-count table as in `anneal3.py`.

## R9241: the key identified (4 Oct 2026, contributed by Feyseel Nur, PR #21)

Lawrence Beck's PR #18 (with ChatGPT, 3 Oct 2026, `beck-preliminary/`) proposed a partial decipherment from the images
first; the work below was done independently and complements it.

The sign set is Paul de Foix's own cipher, as reconstructed by S. Tomokiyo (cryptiana `henryiii.htm#Foix0`) from de
Foix's letters of 11 Oct 1565, BnF fr. 15971 ff. 21-22 (contemporary decipherment on f. 25r, marginal one on f. 26r;
Gallica ark btv1b105094409, view 2N+9 for f. Nr). Not on DECODE, hence missed by the known-key search above. Values
confirmed on the 1565 decipherments: 50 = que (the transcription's "so" = 50; "so f so" = quelque), 82 ceulx, 51 qui,
37 me/car, ny n/z, g s, f s/l/u (several signs two-valued); word signs also serve as syllables (83 30 = Le-c-est-re).

Evidence: the unfitted published key scores −1.517 against −1.759 ± 0.031 for 200 token-order shuffles (7.8 SD); an
independent Montaigne LM (OpenAI Codex, `r9241_foix1565key/codex_review/`) gives 10.7 SD (token shuffle) and 4.3 SD
(sign-identity shuffle). Coverage with a pre-specified measure (share of the 1,026 tokens in dictionary words of 4-14
letters; 200 shuffles): frozen key (independent of R9241) grade A 14.0% (shuffled 7.0%, max 10.2%), A+B 25.6% (12.7%,
max 17.1%); with values fitted on R9241 that recur in ≥2 passages 58.5% (20.7%); all fitted 69.6% (24.3%). No full
sentence is forced by the frozen key alone; phrases needing only recurring fitted values: "pour le moins estre de la
partie", "la negotiation prend quelque traict", "dexterité de son esperit", "quelque deboursement de deniers".
The two readings converge: Beck *Et en ceste uisitation passerent entre eulx quelques …* / here *Et en ceste
visitation p[..]erent d'entre eulx quelque[s] …*; Beck *que son but seroit de nous faire entrer en quelque debourssement
de deniers, dont nous n'avons nule intention* / here *… son but … faire, car entrer en quelque deboursement de deniers
… nulle intention*. Files: `r9241_foix1565key/` (graded reading.md, key_k0.json frozen, key_k1.json fitted layer,
v5_coverage.txt, v5_phrases.json, v5_rendering.txt, codex_review/).

## Proposed reading, Beck (PR #18)

Lawrence Beck, with ChatGPT, submitted a proposed partial decipherment of R9241 (`beck-preliminary/`, start with
`REPORT.md`). He made a new transcription (1,038 tokens, 96 sign types; 1,013 tokens carry a key value) and a 78-entry
key: letters, homophones, word signs (30 est, 31 pour, 50 que, 51 qui, 84 la ...) and 9 nulls. The decrypt
(`beck-preliminary/results/literal.txt`) is continuous period French over long stretches, e.g. passage (1) "... sortir
promptement la reconciliation necessaire entre ces deux royaumes" and passage (4) "... faire entrer en quelque
deboursement de deniers dont nous n'avons nulle intention".

Review, 7 Oct 2026 (`beck_control.py`, `lang` model fr-1600-letters, no spaces):

| measure | Beck key, real order | controls |
|---|---|---|
| LM per char | -2.02 | 500 value-shuffled keys -4.28 ± 0.39 (max -3.28), z = 5.8 |
| LM per char | -2.02 | key fitted (swap annealing over Beck's own 78 values) on token-shuffled ciphertext: -1.93 to -2.00 |
| letters in corpus words of 5+ letters | 50.6% | same fitted keys on shuffled ciphertext: 26.1%, 33.4%, 34.2%; Beck key on shuffled order: 4-7% |

- The per-char LM score alone does not separate the reading from overfitting: 78 free values (some whole words) can
  make shuffled ciphertext score as well, as word salad ("fairepourfaire..."). The long-word measure separates them
  (50.6% against at most 34%), and it underestimates the real text, whose 1563 spelling is not in the 1600 corpus.
- Independent confirmation: Feyseel's frozen key from de Foix's own 1565 cipher (PR #21, `r9241_foix1565key/key_k0.json`,
  from Tomokiyo's chart and BnF fr. 15971 ff. 21-26, not fitted on R9241) gives the same value as Beck for 19 of the 25
  sign names both use (a, b = e; 4, 7 = c; m = n; n, d = o; p = r; 30, 31, 32, 50, 51, 83, 84 ...), and 6 = ie/je agrees
  in effect. Differences: D, 3, 2, r, z (sign naming or homophony still to settle).
- Assessment: a real partial break, in de Foix's cipher, not overfitting. It is not at the read bar: 14 of the 78 key
  entries rest on a single occurrence, a dozen signs (RX, monograms, numbers 10, 20, 26, 34, 37, 40, 70, 82) are open,
  and no fraction of tokens read as sense has been measured against the images. Outcome left unchanged here.
- Five-sign audit (Beck, PR #27, 8 Oct 2026; `beck-preliminary/FIVE_SIGN_AUDIT.md`): the D, 3, 2, r, z "conflicts" were partly a
  naming collision. Beck's private labels are not qm2's: his `D` is qm2 `th` and his `r` is qm2 `c`, and the 1565 key agrees on both
  (th = t, c = u). Real conflicts remain on plain `3` (Beck s, 1565 e/t; his descended form = qm2 `Z3` = s in both), `2` (l against i)
  and `z` (i against p; Beck cites the 6 June 1562 marginal decipherment, BnF fr. 6612 f. 54, for z = i, before the early-1564 key change).
  Checked here 9 Oct: pairing 31 equal-length rows of the two transcriptions gives D->th 10, r->c 13, z->z, 2->2, 3->3, THREE_CURL->3/Z3;
  `verify.py` passes with the regenerated manifest. No reading changes.
- Package: `scripts/verify.py` fails on a Windows checkout (core.autocrlf rewrites the hashed files; a
  `.gitattributes` with `-text` is added to the folder) and on `README.md`, which was edited after `manifest.json` was
  written. With LF files and README excluded it passes (17 files, 1,038 tokens replayed).

## Remaining gaps

- R9241 Catherine de' Medici to Paul de Foix, 15 Jan 1563, passages (1)-(4): key identified (de Foix 1565, see above) but the reading is partial; conflicts between the 1565 chart and values fitted on R9241 (r m/d, z p/i, Yb l/u, 3/Z3) and the unvalued 80 and 93 need a glyph audit on the images and a de Foix letter of 1563-64 - blocker: open-codes

## Escalation

- [x] siblings: R9237/R9239/R9240 (catalogue 93) viewed in part; they are Coligny letters in a different sign set, no Queen Mother material
- [x] clear-pages: no clear or deciphered page for the Queen Mother letter among the R9238/R9241 images
- [x] known-keys (4 Oct 2026): Tomokiyo's de Foix key (BnF fr. 15971, 1565) fits R9241, see above. Earlier: Throckmorton first/second/third ciphers and Croft's (R9260-R9262) compared; then every DECODE key record dated 1550-1580 with French plaintext: R335 (Condé 1562, fits R9238 not R9241), R355, R331, R3818, R3820 (Fontenay 1583); none fits R9241
- [x] print: Forbes ii, CSP Foreign vi (whole volume), La Ferrière i-ii searched; not found
- [x] key-rebuild: no crib or sibling key exists; ciphertext-only swap annealing (one letter per sign, with nulls, pairs, syllables; 5 languages) on both transcriptions, all negative
- [x] retry: sign-by-sign re-transcription of both pages (qm2_f148.txt, qm2_f149.txt, merged qm2_tokens.txt: 1007 tokens, 92 types, IoC 0.031); anneal3.py French, English and French-with-nulls on it: no language (r6_*.txt)

## Next steps

1. TNA SP 70/49-50 (Jan 1563): look for the intercepted original, or an English decipherment of the Queen Mother's
   letter to de Foix.
2. French side: de Foix's embassy correspondence (BnF fr. 15875-15970 range, Bibl. nat. 500 Colbert) for the clear
   letter of 15 Jan 1563 (a minute in the secretaries' registers, e.g. L'Aubespine's), or the Catherine-de Foix cipher.
3. Re-transcribe f.148v-149 with a sign table and image crops per sign, then retry with polyphony allowed.

## DECODE corrections

R9238: author Gaspard de Coligny (Admiral of France), recipient Elizabeth I, camp at Villefranche, 12 Jan 1563
(not 2 Jan), French; deciphered at the time (CSP Foreign vi no. 76; Forbes, Full View ii); f.143 lower half begins
another Coligny letter. R9241: f.148 top is the end of a Coligny letter (passages 15-24); the rest is Catherine de'
Medici to Paul de Foix, 15 Jan 1563, French, not deciphered.
