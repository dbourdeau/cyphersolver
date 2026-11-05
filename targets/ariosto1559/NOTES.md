# ariosto1559: Ercole II d'Este to Claudio Ariosto, 23 April 1559 (catalogue 2159)

Status: read in part (Brice Dudout, 5 Nov 2026; 357 of 402 cipher words = 88.8% without restorations; key validated by our protocol, M5 0.605 against 0.155 on a held-out set, one measurement).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Catalogue entry 2159, from WAINUT's Estense
leads (PR #242). No DECODE record, nothing at Cryptiana (Tomokiyo), no edition found.

## Document

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera E, Este (d'), Ercole II d'Este, duca di Ferrara,
cc. 39-41 (IIIF manifest 8d50f9af-95d8-405e-a3a4-f66933e69af1). Ercole II to his secretary Claudio Ariosto, Ferrara,
23 April 1559, with a postscript ("Post.", cc. 40-41). Runs of cipher are set in clear Italian on 39r, 39v, 40r, 40v and
41r: about 1,840 cipher tokens (signs and raised marks), 77 cipher lines.

The Estense images are CC BY-NC-SA. **No image, crop or thumbnail is included here**: the scans were used for research only.

## System and key (`key.tsv`)

- Consonant signs of Greek and Latin shape (alpha = n, omega = c, lambda = s, theta = d, kappa = b, upsilon = t, sigma = r,
  pi = m, tau = h, chi = p, phi = g, the double loop = f...), and a few figures used as signs (8 = l, 1 = l, 3 = a).
- A small raised digit gives the vowel that follows the sign: 2 o, 3 i, 4 e, 5 a, 6 a, 7 e, 8 i, 9 o, 1 u.
- A raised ring doubles the consonant; a dot is a null; "&" = *qu*.
- Code numbers under a bar: {23} fits *Sua Maestà Catolica* (Philip II) at both places and is restored; {22}, {24} and
  {25}{27} occur once each and are not resolved.
- It is not key_1559 (Bentivoglio, `targets/ercole1559`) and not francescoeste1546, bresegno1548 or alfonso1576: each was
  applied once to the training lines before any learning, and none reads the letter.

`key.tsv` gives the frozen, measured value of each token and the value used for the reading. They differ in one place:
the double loop D was *n* in the measured key and is *f* in the reading (see below).

## Validation (`validation.txt`)

Protocol, measuring script and blind transcription were frozen by SHA-256 before any key work. The held-out set H
(40v:08-14, 40vB and 41r: 405 tokens, 22.1%) was excluded in code from learning. The key was learned by annealing on the
other lines, frozen, and measured **once**: M5 (share of decoded letters covered by Italian words of 5+ letters) = **0.605**
on H, against **0.155** for the best of 200 permuted keys (gap 0.451). Our thresholds, fixed in advance: >= 0.60 and
>= 0.30 above the best control. **Validated by our protocol.** There is no contemporary decipherment, so there is no
character score.

After the measurement the reading showed D = *f*, not *n* (15+ places: *satisfare, far, prefata, fosse, favore, figliolo,
Farnesi*...). That change is outside the test; the test held with the wrong value.

## Transcription

Two blind passes by AI agents (the second blind to the first and to the key): 87.7% of tokens identical, 89.3% of signs
and 95.5% of raised marks on aligned places. A blind shape sheet (pre-registered and hashed before it was built; shape
thumbnails only, no values or words shown) was answered by Brice Dudout on the 9 places where the passes differ and the
word depends on it: all 6 d/D places are the double loop D (*f*), all 3 Q/y places are Q. As fixed in advance, those
9 words moved from probable to certain. `transcription.txt` is the first pass with those 9 signs settled; the measured
copy differs only there (listed in its header).

No human palaeographer has checked the transcription. The lines most garbled in both passes are 39r:07-08, 39r:19-21,
40r:12-16 and 40v:02-04, 12-13.

## Reading (`reading.md`, `translation.md`)

Daniel's rule, words written in cipher only, counted by script:

| words | certain | probable | restored | unresolved | certain + probable | with restored |
|---|---|---|---|---|---|---|
| 402 | 262 | 95 | 6 | 39 | 357 = 88.8% | 363 = 90.3% |

Under 95%: **read in part** (`reading_review` grade B: one AI reader, Brice Dudout answered the shape sheet only).
One of the 262, *satisfare* (39r:05), begins with a *t* sign in both passes; it is kept certain as pre-registered and
flagged. A second shape sheet cannot reach 95%: most of the 39 unresolved words read the same in both passes.

**Content.** A countess claims arrears of *censi* (rents) owed by the duke. He refuses those that fell due "at the time of
the rebellion of her consort" ("a causa della sua ribellione non s'ha da haver nulla") and offers to pay the future ones to
her rather than to her husband, who had "false complaints" made against the duke at the court of Philip II. She thinks of
suing her husband for his ill-treatment of her and of their son; a count, her son-in-law, intercedes; a favourite of the
husband, Iacomo, is to have 4,000 ducats; "this peace" (Cateau-Cambrésis, April 1559) lessens the husband's credit. The
duke asks for news of the rivalry between [..] and "don Cesare" and "il marchese", and of their *academie*.

**Not identified**: the countess, her husband and the count. "Don Cesare" may be Cesare Gonzaga, count of Guastalla, and
the unresolved "dastalla" of 41r:01 may be *Guastalla*; "il marchese" may be the marquis of Pescara. These are hypotheses,
not counted and not checked. Four web searches found nothing decisive.

## Not read, declared

- **Ariosto c. 1** (15 Jul 1559, `targets/ercole1559`, WAINUT's target, still not solved): our frozen key was applied once,
  unchanged, to WAINUT's public transcription (M5 0.189, controls 0.294) and once to our own copy from the image
  (0.271 vs 0.204). It does not read c. 1. c. 1 is in Ariosto's own hand and has a sign not in 2159: probably another
  table of the same family. Nothing is claimed for c. 1, and `targets/ercole1559` is not touched.
- **Catalogue 2160** (Ercole II to "secretario domino Claudio", 8 Jan 1547, cc. 16-17): 8 cipher lines transcribed blind
  (455 tokens); another table (Latin-shaped bases, varied accents, bars and crosses as raised marks). The neighbouring
  public keys and our 2159 key were applied once each to its training lines (M5 <= 0.025, all under their controls);
  annealing did not converge. No key was frozen, so no measurement was made on its held-out lines. **Not solved**, and no
  file for it is included.

## Remaining gaps

- 39 unresolved cipher words (39r:07-08, 39r:19-21, 40r:12-16, 40v:02-04, 40v:12-13) - blocker: illegible; read the same in both blind passes, a third human reading at full resolution or a clear minute is needed.
- Code numbers {22}, {24}, {25}{27} - blocker: open-codes; one place each, no defensible value ({23} restored by sense).
- Identity of the countess, her husband and the count - blocker: needs-physical-access; Archivio di Stato di Modena not searched.
- Ariosto c. 1 (targets/ercole1559) - blocker: no-key-material; our key does not fit it (two failed measurements).
- Catalogue 2160 - blocker: too-short; about 180 training signs in another table, no key frozen.

## Escalation

- [x] siblings: Campori E cc. 50-51 (ercole1559), Ariosto c. 1 and Ercole II cc. 16-17 (2160) opened and compared; each is another table.
- [x] clear-pages: the clear parts of cc. 39-41 are the letter itself, not a decipherment; no decipherment leaf in the file.
- [x] known-keys: ercole1559, francescoeste1546, bresegno1548, alfonso1576 applied once each before learning; none fits.
- [x] print: four web searches, DECODE and Cryptiana (Tomokiyo), and a fifth search on 5 Nov 2026 (edition of Ercole II's letters to Claudio Ariosto, 1559): no edition, calendar or study of this letter found; the likely printed source would be the Modena Cancelleria series (Carteggio ambasciatori, Venezia), not searched in print.
- [x] key-rebuild: D = f found by reading after the measurement and confirmed by the blind shape sheet; codes studied (`{23}`).
- [x] retry: every word retried with the reading key on both blind passes and regraded after the shape sheet.

## Prior work

Catalogue 2159 and 2160 were open when checked through the GitHub API (origin/main e2315f8a, 5 Nov 2026): no target, PR or
issue for cc. 39-41 or cc. 16-17. No edition or study of this letter found. We have not searched the Archivio di Stato di
Modena (Cancelleria, Ambasciatori; Ariosto's 1559 correspondence), where a clear minute could exist. If one prints this
letter, we will credit it.

## Credits

- `dudout`: transcription, key, validation, reading.
- `lccompany` (WAINUT): pointer (lead 2159 from the Estense sweep, PR #242); their public transcription of c. 1 was used for
  the external test above, which failed.
- `bourdeau`: pointer (catalogue entry 2159, vetting).

## Files

`transcription.txt` (blind transcription, reading copy), `decryption.txt` (mechanical decryption, no correction),
`key.tsv` (CC BY 4.0), `validation.txt`, `reading.md`, `translation.md`, `profile.json`.
