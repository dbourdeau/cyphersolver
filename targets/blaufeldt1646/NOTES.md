# blaufeldt1646: the writer who signs in cipher, to Ottavio Piccolomini, [February?] 1646 (catalogue 2355)

Contributed by WAINUT (lccompany), 12 Nov 2026. Work done by AI language-model agents; no human palaeographer
checked the text. A separate AI language-model agent that took no part in the solution reviewed it blind on 12 Nov
2026 (see "Independent review" below).

Status: read in part.

## Documents

- **inv. 24854** (SOA Zámrsk, Rodinný archiv Piccolominiů (Náchod), inv. č. 24854, microfilm frame "31/2"): one
  page to "Ecc.mo Sig.re" (Ottavio Piccolomini by the archive and the catalogue entry; the letter names no one).
  About five lines of two-figure cipher groups mixed with plain Italian, the close "Di V.E. Devotissimo Servidore"
  in plain script, the signature in cipher, and a cipher line at the foot. No gloss. This is the target.
- **inv. 24852** (frames 24852.jpg, 24852_1.jpg) and **inv. 24853** (24853.jpg, 24853_1.jpg, 24853_2.jpg): letters
  of the same writer, same cipher signature, dated "alli cinque del febraro 1646" (24852_1) and "a 9 di febraro"
  (24853_2, plain script at the foot); their cipher runs carry a contemporary interlinear decipherment. They give the
  key (24852) and the held-out test (24853). They are glossed, so they are not targets; their glosses are not
  transcribed in full here.

Images: Vlnas 2017 (theses.cz/id/p3p2kb), appendix zip P_lohy_A_a_B.zip, fetched once in Chrome on 12 Nov 2026 for
catalogue 2356; frames extracted to `../../2356/scans/` and rotated copies in `../scans/` (not for git). The frames are
photographs of a microfilm-reader screen, about 9 px per figure height: many figures are at the edge of legibility.

## System

Simple substitution in two-figure groups, one letter each, written in continuous runs inside plain Italian.
Main alphabet (from the glosses of 24852): a30 b31 c32 d33 e15 f16 g17 h18 i25 l27 m28 n29 o20 p21 r23 s24 t19
u/v10 z14; q22 from 24853. A bar over a group doubles the letter (24^ = ss in "assedio", "Gissen"; 44^ = nn in
"hanno"). Homophones in the 40-80 range, attested on 24853: 40 a, 44 n, 46 f, 52 c, 63 l, 64 m, 74 s. Code groups
written apart: 77 gente, 88 S.A. (Sua Altezza). The writer often writes one letter for a double without a bar
("tratando").

## Key and held-out test

`pairs.tsv`: 20 glossed words of 24852 (131 groups); `key_frozen.tsv` was built from them and frozen before the
held-out test and before 24854 was decrypted. Ten more rows (q, the seven homophones, two codes) were added from
24853 after the held-out test and before the mechanical decryption of 24854; `check_pairs.py` leaves them out of the
test. `key_frozen.tsv` holds 29 entries on 36 lines (19 letter groups from 24852; 10 rows from 24853: 1 letter, 7
homophones, 2 code groups); `key.tsv` holds the same 29 entries on 35 lines (no value changed after freezing).

Held-out (`heldout_24853.tsv`, 11 glossed words of 24853, read from separate crops): **72 of 72 groups that have a
value in the 24852 key give the gloss letter (100%), 0 wrong**; 7 groups (homophones 40 44 46 52 63 74) have no
value in that key; 6 of 11 words are letter for letter. Small test; the glosses were visible on the crops when the
signs were copied.

## Transcription of 24854

`SIGN_CONVENTIONS.md` written first. Pass 1 (deskewed frame, whole-line crops at 1.5x) and pass 2 (frame not
deskewed, half-line crops at 2.2x) were done by shape before the key was applied to this frame, and reconciled on
3x-4x crops (`transcription_24854.txt` header lists each settled disagreement). Unsettled groups are '?'.

Caveat on independence: the key values were being worked out from 24852 while 24854 was being copied, so pass 2 and
the reconciliation were not blind to the alphabet. The reading marks every place where the signs as copied differ
from what the sense needs.

## Reading

`decryption_24854.txt` is the mechanical output of `scripts/decrypt.py`; `reading_24854.md` marks every departure;
`scripts/check_marks.py` rebuilds the decryption and passes.

Running text: "Questa notte son [?partito] di Giessen et vengo con buona risolutione. Ho tardato tanto, parte per le
gran acque, parte per le gran difficoltà che ho havuto in resolver il negotio, non havendo mancato usare [?ogni]
[?fatica], quando spero vedere presto V.E. ... Devotissimo Servidore Blaufeldt. A [...] di [?febraro] in Giessen."

Word count of the cipher words (`scripts/reading.py check`): **24 cipher words: 15 verbatim from the signs with
glossed values (62.5%), 6 with a marked repair, 0 from a gloss only, 3 holes.** All six repairs give an unglossed
group (50, 70, 86, 73, 60, 80) the value the sense needs, one of them together with a 23 read where c is needed.
These groups may be more homophones of the 40-80 range, or misreadings of a soft photograph (for example 86 for
31 = b, 80 for 10 = u); the image does not settle which.

Dan's reading checker (`docs/_check_reading.py --file`, origin/main 65cdcd9d5, 13 Nov 2026) on the running text
only: Italian clean share **0.571** (4 of 7 sentences, 68 words, hole rate 0.118); English translation 0.571 (4 of 7,
77 words, hole rate 0.104). Before the plain words "ogni fatica" were marked doubtful after the review, it gave 0.714
(5 of 7) for both. Run on the whole files listed in profile.json (English notes included) it scores lower,
because of the notes, not the text (figures in the pull request text).

Proposed state: **read in part**. Most of the text is plain script; the cipher words build coherent sentences with
the plain text, with three holes and six repaired words.

**The signature.** The nine groups 31 27 30 10 16 15 27 33 19 (identical on 24852_1, 24853_2 and 24854) give
**"Blaufeldt"** with glossed values only (b from "buona", f from "fiand(ra)", the rest from many words). No gloss
spells the name, and on 24853_2 the signature is preceded by a 17 under a cross, not explained. Searches for a
Blaufeld(t) at Giessen, in Hessen-Darmstadt service or near Piccolomini in 1646 found nothing (12 Nov 2026), so the
person is not identified; the name could be a cover name.

Context (from the glossed siblings, as glossed): the loss of Marburg and the siege of a place glossed
"...nietstein" (probably Blankenstein), negotiations with S.A. and S.C., Melander, Saxony and Lüneburg, Cassel.
That is the Hessian war of early 1646, and the writer was at Giessen (Hessen-Darmstadt).

## Statistical validation

`validation.tsv` (built by `scripts/make_validation.py`): the 123 cipher tokens of 24854 in text order with the
value the reading gives each; 14 are left unread (the '?' groups, the guessed stretch of "[?partito]" and the date-line
hole); the six unglossed groups carry their values from sense and the 23 of "difficoltà" is read c, as in the reading.
`docs/_validate.py` (13 Nov 2026, model it-cinquecento, order 4): 109 read tokens, 30 types, 3.63 tokens per type;
reading -2.082 per letter; random keys -4.386 (sd 0.474, z 4.9, n 200); key annealed onto shuffled ciphertext best
-2.361 (mean -2.463, z 5.9, n 6); annealer on the real text -2.264. **Verdict: weak** (the random-key margin is 4.9
sd, under the 5 needed for a pass). The text is short. The key does not rest on this test: it comes from the
contemporary glosses of 24852 and was tested on held-out glossed words of 24853.

## Collision check

Dan's repo (local clone, origin/main 65445e3f8, 12 Nov 2026): no target or research file covers inv. 24852-24854 as
a solve (`frankenthal1646` only records that the frames were extracted). `gh pr list --state open`: no PR on
Piccolomini, 1646 or Zámrsk (open: #491 ercole1544, #490 klingenberg1675, #391 draft). `gh pr list --state all
--search "24854 OR 2355 OR Servidore"`: nothing. Rechecked before finishing (12 Nov 2026): no open PR on Piccolomini, 1646, Zámrsk or 2485x; PR and issue search on 24854, Blaufeldt, 2355, Piccolomini empty; targets/ on GitHub has only claudiamedici1646, frankenthal1646, piccolomini1646, ridolfi1646 for 1646 or Piccolomini.

Rechecked 13 Nov 2026 (origin/main 65cdcd9d5, the same commit as main on GitHub): targets/ has no blaufeldt or 2355 folder; open PRs
#500, #498, #497, #496, #495, #494, #391, none on this letter; PR search (all states) on Blaufeldt, 24854 and 2355
empty; the hits on Piccolomini and Giessen are the merged #302, #303, #310 and #462, which treat other letters.

## Prior art (checked 12 Nov 2026)

- Catalogue entry 2355 checks of 6 Nov 2026: Vlnas 2017 lists 24854 as B20 in appendix B (not deciphered); no
  DECODE, Cryptiana, Lasry or edition hit; HistoCrypt 2018 shows only inv. 25039.
- Web searches 12 Nov 2026: "Blaufeldt 1646 Piccolomini Giessen"; "Blaufeld OR Blauvelt 1646 Hessen Marburg Gießen";
  "Blaufeld Hessen-Darmstadt 1646 Landgraf Georg II Piccolomini": no edition, no decipherment, no person found.
- No printed decipherment of 24854 is known; the only crib is the writer's own glossed letters.

## Independent review (12 Nov 2026)

A separate AI language-model agent that took no part in the solution reviewed the folder blind (a model reading, not
a person). It cut its own crops from the frame and copied 68 groups on 7 cipher runs (L1 run 1, L2 start, L3 last
run, L4 runs 1 and 2, L5, the signature) before it opened the transcription: 63 agree, 1 differs and 4 it could not
settle. The one that differs is the last group of L4 run 1 (`30?` in the transcription, 80 to the reviewer), already
marked doubtful. Not settled by the reviewer: L1 50, L2 44 (a crossed pair) and 86, L3 73. It ran
`scripts/check_marks.py` (pass), wrote its own decryptor from `key_frozen.tsv` (same text line by line), reproduced
the held-out result (72 of 72 groups), and read the Italian against the translation. It agreed the state **read in
part** and gave grade **B**: three holes, six repairs from sense, one sign/sense clash (23 = r where "difficoltà"
needs c) and one doubtful plain phrase.

Change made after the review: in L5 the plain words "ogni fatica" are not certain on the photograph (at 6x the last
word looked to the reviewer more like "[d]ifficolta", and the word before it was unclear); they are now
`[?ogni] [?fatica]` in transcription, decryption, reading and translation. They are plain script, so the cipher-word
count is unchanged (24 words, 15 verbatim); the reading checker's clean share fell from 0.714 to 0.571.

## Remaining gaps

- L1 group after "nott-" (50, read e) - blocker: illegible; unglossed, the same on both passes, not settled by the
  reviewer; an e homophone or a misread figure. Marked repair.
- L1 "[?partito]" - blocker: illegible; of seven groups only the 2nd, 3rd and last (a r ... o) are settled on the
  photograph; "partito" is a guess, counted as a hole.
- Unglossed groups 60, 70, 73, 80, 86 (with 50 above) - blocker: too-short; no gloss on 24852 or 24853 attests them;
  the reading gives them the value the sense needs (marked repairs). They may be further homophones of the 40-80
  range or misreadings of a soft photograph (86 for 31 = b, 80 for 10 = u); only a clean image or more glossed text
  would settle it. The reviewer could not settle 86 either.
- L4 "difficoltà" - blocker: illegible; the 5th group reads 23 (r) on both passes and to the reviewer where the word
  needs c (32 or 52): a slip of the writer or a misread figure. Marked repair. The last group of the word is 30? (a)
  in the transcription and 80 to the reviewer; marked doubtful.
- L5 plain words "[?ogni] [?fatica]" - blocker: illegible; perhaps "[d]ifficolta" (reviewer); the sense is close
  either way.
- L8 (date line) - blocker: illegible; the first group is under an ink blot and the groups after "feb" are not
  settled; "febraro" is a guess from the sibling letters, counted as a hole.
- Key rows from 24853 - blocker: too-short; the 10 rows (q, seven homophones, two codes; three of them, 22, 44 and
  74, occur on 24854) were added after the held-out test, so the test does not cover them.
- The writer - blocker: no-key-material; the signature reads "Blaufeldt" with glossed values, but no gloss spells the
  name and quick searches (12 Nov 2026) found no Blaufeld(t) at Giessen or near Piccolomini in 1646; it may be a cover
  name.
- Human check - blocker: needs-physical-access; one blind AI reviewer compared 68 of the 123 groups; no human
  palaeographer has checked any sign. A clean scan of inv. 24852-24854 from SOA Zámrsk (not ordered) would settle
  most of the holes above.

## Escalation

- [x] siblings: the glossed letters 24852 and 24853 of the same writer, cipher signature and month gave the key and
  the held-out test
- [x] clear-pages: the contemporary interlinear decipherments on 24852 and 24853 used (pairs.tsv, heldout_24853.tsv);
  24854 itself has none
- [x] known-keys: Vlnas 2017 lists 24854 as B20, not deciphered, and gives no key for this cipher; the keys of
  claudiamedici1646, piccolomini1646 and frankenthal1646 are other tables
- [x] print: catalogue checks (6 Nov 2026), Vlnas 2017, three web searches (12 Nov 2026); no edition found
- [x] key-rebuild: every settled group of 24854 has a value; the six unglossed groups take values from sense, marked
  as repairs
- [x] retry: every doubtful group retried on 3x-4x crops by the solver and again blind by the reviewer (6x on L5);
  the groups listed above stay open and need a clean scan from SOA Zámrsk (not ordered)
