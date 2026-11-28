# Penn LJS 51, f. 48r l.8 - 48v l.13 and 21r l.1–5: the fourth cipher riddle

Status: read
Outcome: key recovered from ciphertext-only, 27 Nov 2026. Blind annealing on ff. 48r–48v yielded recognizable words. Alignment with the clear riddle refined the key. A later comparison identified five more cipher lines on f. 21r. Together the two portions give the complete riddle. The compiler wrote his own solution on f. 21r l.7 – 21v l.2.

The original break, its transcription history and controls are preserved in ../ljs51corpus/solve_48r/, REPORT.md, recheck_2x.md and ruleout.txt. The continuation is transcribed in ../ljs51corpus/keys_eye/20r.8+47r.1.json under block_21r_1_5. The f. 47r verse riddle and the f. 106v cipher use different keys.

## The document

- University of Pennsylvania, Kislak Center, LJS 51, f. 48r l.8 - 48v l.13 (OPenn master images 0084_0100 and 0084_0101,
  `https://openn.library.upenn.edu/Data/0001/ljs51/data/master/0084_0100.tif`). The initial 19 lines of invented signs, groups of
  2-8 signs between dotted-stem dividers.
- Heading on 48r l.7: one word, first read وابعها [?] (chain record 48r.8: ورابعها "and the fourth of them" or واتبعها
  "and he followed it with" possible); the corpus recheck of 27 Nov 2026 gives ورابعها ("and the fourth of them"). The continuation is on f. 21r (master 0084_0046); the sender is unnamed.
- The remark on 49r that a cipher "was not solved except after much toil" belongs to the short block 49r l.1-4 (chain
  49r.1, answered by the verses on 49r l.6-7), per the corpus recheck of 27 Nov 2026; not to this block.
- Dating: the corpus notes put the correspondence of the volume c. 1325-1360 (al-Mutarjim active in Damascus before
  725/1325 and still there in 745/1344-45; Ibn al-Durayhim, d. 762/1361, praised in it). Penn's record: "Possibly written in Syria, in the 15th century", date "14--"
  (`ljs51corpus/prior_art_2.md`). So the ciphertext read here is probably in a 15th-century copy; the swapped, dropped and
  doubled signs fit a copyist (Dudout). As a document it is not clearly older than Siena 1413. The compiler is very probably Tāj al-Dīn Ibn al-Durayhim. The attribution rests on the compiler’s first-person references to his works; Penn’s record names no author (corpus NOTES.md and identity_ibn_durayhim.md).

## The plaintext

The compiler says at f. 21r l.6 that he worked the cipher out quickly because it was easy. He copies the clear riddle immediately afterwards and gives its answer on f. 21v, the raised couches of Sūrat al-Wāqiʿa. The clear copy has 293 letters (chain record 20r.8).

## The system

Simple substitution of invented signs for Arabic letters, right to left, a dotted stem between words (words may run
over a line end). Same sign family as the f. 47r block, different key. On ff. 48r–48v: 228 signs, 27 sign labels (measured,
`_check_profile.py --measure --drop-first`), 47 dividers. 25 letters have a sign; ي has two labels (AY, O8) and ل two
(X, XN, one occurrence); whether these are true homophones or variant shapes of one sign was not checked. The
three-pronged OM sign is ق in both its places (recheck_2x.md); `solve_48r/key_48r_v2.json` still carries ع for it,
because the alignment scored the clear copy's العسي, so `key.json` here sets OM = ق. Commonest sign W = ا (45).

## How the key was recovered

1. 47r key (`keys_eye/47r.1.json`) applied: does not fit (same sign shapes, different key).
2. Plaintext candidates tested by length and group pattern (chain record 48r.8): the verses on 49r l.6-7 (72 letters),
   the first five verses of the 47r riddle (about 208 letters), the compiler's eight answer-verses (about 320 letters).
   None fits.
3. Simulated annealing over one-to-one keys, word dividers kept as spaces, scored with `lang` model `ar-mamluk`
   (`anneal_sp.py`, 6 restarts x 40,000 steps, no plaintext given). Restart 1 reached -2.51 per character and read
   "... اهل اصلاح تثور اذا ب ن الليل وترحل عند الصفاح ترميها ... وهي معدوده من نعيم اهل الجنه ..."; other restarts scored
   -2.64 to -3.24 with partial words.
4. That text was recognised as the f. 21r riddle (originally recorded under 20r.8). DP alignment with the key re-learned from it
   (`verify.py`, then `verify_v2.py`): v1 218 of 229 signs (95.2%); after the 2x re-read 220 of 228 (96.5%), 3 surplus
   signs, 7 dropped letters; the block covers 232 of the riddle's 293 letters and stops at جملته.
5. 2x-3x re-read of every flagged position on the masters (`recheck_2x.md`): five transcription errors, six misplaced
   dividers corrected (229 -> 228 signs).
6. Found a second time in the corpus recheck by a group-length search over the book's passages (43 of 49 groups;
   corpus NOTES, 27 Nov 2026).
7. Rule-out (`ruleout.txt`): the decoded block against all 206 plaintexts of the book: 20r.8 95.2%, next best 22.3%
   (22r.1), median 9.2%.

The annealer reached the text without it, so the reading is not an artefact of the alignment; the alignment figure
itself is self-consistency.

## What the cipher settles in the clear copy

- ترميها where the 20r.8 record reads توهمها; يحمد منها where it reads وخمد منها; القسي "the bows" where it reads
  العسى[?] (with وتطعنها الاسنه "the spears" after it). اوطا ظهر confirmed.
- Re-read on the f. 21r master (0084_0046, crops at 2-4x, 27 Nov 2026, model's reading; asked for by Dudout): the clear
  copy has ترميها (two dots over the first letter, ر, two dots under the tooth) as the cipher; تحمد (two dots above, no و),
  same skeleton as the cipher's يحمد; العسي/القسي with an undotted head after al-, which the cipher's ق settles; جمّلها with
  a shadda (not جمالها), as the cipher. So the record misread the clear copy; the cipher does not correct the clear copy
  except by settling the undotted ق. Qaws al-naddāf (cotton-carder's bow) + quilting needles would fit القسي (Dudout);
  an Arabist should confirm.
- Scribal slips in the cipher: الاكانف (ن and ا swapped), وطيها (ب dropped), تتجافاها (TH written twice), اصلاح (ل
  dropped, or a correction: see doubts), وجهها for وجمعها, منه ما for منها ما. جملها is not a slip (clear copy جمّلها).

## Transcription doubts
- TT (48r l.12, the ص of اصلاح) - read: ص; checked: image (2x), decode; it carries a hooked ascender the TT of 48v l.1
  lacks and does not look like X (ل); the ل of الصلاح is missing either way. Unresolved: a slip or a correction.
- OM (48v l.2 and l.8) - read: ق; checked: image (2x, side by side `x2_cmp_OM.jpg`), decode; same three-pronged shape in
  both places, ق gives بعقد and القسي.
- W (48v l.2) - read: one W, a small one written below the line; checked: image (2x), decode; v1 had two.
- SW (48v l.10, line start and over the divider) - read: SW SW; checked: image (2x), decode (ما يذم).
- HK/SW (48v l.12, last sign) - read: SW; checked: image (2x), decode (جم-لها).
- W (48v l.13) - read: none; checked: image (2x), decode; v1 had a phantom W.
- XN (48v l.5, الجن) - read: ل; checked: image (2x crop of the master 0084_0101, write-up session), decode; the same
  X-on-legs shape as the X two signs before it in the line, without the small stroke above its head; gives الجن. Looks
  like a variant of X rather than a second sign (one occurrence, not settled).

## The reading

`reading.md` (as enciphered and in normal spelling, emendations in [ ]); English in `translation_en.md` (the corpus
translation of 20r.8, cut to the enciphered part, with the three places the cipher corrects).

## Checks

- Blind annealing found the text (step 3); group-length search found it again (step 6); rule-out against 206 plaintexts (step 7; run on the v1 decode of 229 signs).
- Statistical validation (`docs/_validate.py`): see profile.json `outcome.validation`.

## Prior work

The compiler's own break: he solved this cipher "quickly because of its ease" (21r l.6) and
wrote the plaintext on f. 21r; Penn's record says the letters are "accompanied by transcriptions". So the plaintext of this
block was never lost, and `first_break` is "unpublished prior". Medieval worked solutions of the same type: Ibn
al-Durayhim's Miftāḥ al-kunūz, two ciphers of devised symbols solved from frequencies (Mrayati, Meer Alam, al-Tayyan,
Arabic Origins of Cryptology vol. 3, p. 33, pp. 101-124; cited by Dudout, not seen). Penn cites Transformation of
Knowledge (2006), p. 43, for the manuscript (not reachable, `ljs51corpus/prior_art_2.md`).

No study of the ciphers of LJS 51 found (corpus prior-art notes; the sibling's vetting of 15 Nov 2026: Penn TEI, Digital Scriptorium,
DECODE, Tomokiyo, Lasry's list, web). DECODE has no record of the manuscript.

## Review by Brice Dudout (email, 27 Nov 2026)

- Independent re-run with his own 4-gram model (same five OpenITI texts as ar-mamluk) and annealer: 7 of 11 restarts
  reach the riddle (about -2.10 per sign); shuffled ciphertext, best of 12 restarts -3.18, no sense.
- No leak: none of 14 distinctive phrases of the riddle in the five source texts; 0.7% of its 12-grams occur there.
- Length: 228 signs = 4-7x the unicity distance of a simple substitution in Arabic.
- Narrowing asked for and made on the page: 15th-c. copy; compiler's prior break; Miftāḥ worked examples; plaintext in
  the codex said in the summary; attribution softened; Transformation of Knowledge cited; dates fixed (28 -> 27 Nov).
- Statistics: the _validate shuffled-refit null had n = 6 and started one restart from the final key. Rerun blind vs
  blind (`null_blind.json`, same annealer as _validate.py, all restarts from random keys): real best of 20 -2.658;
  shuffled n = 60 (best of 2 each) mean -2.992, sd 0.075, max -2.856; descriptive z 4.5; 0 of 60 shuffle maxima reached the real maximum. The unequal restart budgets preclude a permutation p-value.
- Still owed: an Arabist's reading (Alan Elbaum asked for f. 106v); Brice offered to rerun nulls or check f. 21r.

## Remaining gaps
- reader: no Arabist has checked the transcription, the reading or the f. 21r re-read; the A grade is a model's.
- للراكبان (dual -ān after li-) in both copies; جملته (21v l.1 جمّلها ربها جملته وازادها نعمته) left untranslated.
- none for the block: every sign has a value; the 8 signs that do not take the letter of the clear copy as recorded are
  scribal slips or places where the record misread the clear copy (ترميها, تحمد/يحمد, القسي undotted).
- the ل of اصلاح (48r l.12): slip or correction, not settled (see Transcription doubts); does not affect the reading.

## Escalation
- [x] siblings: the f. 47r key tried (does not fit); 49r verses and the 47r riddle and answer verses tested
- [x] clear-pages: the clear riddle on f. 21r l.7 - 21v l.2 is the plaintext
- [x] known-keys: 47r.1 key tried
- [n/a] print: no edition or study of the ciphers of LJS 51 found (Transformation of Knowledge 2006 p. 43 not reachable)
- [n/a] key-rebuild: the original key covers ff. 48r–48v; the two additional f. 21r labels are recorded in key.json
- [x] retry: every flagged position re-read at 2-3x (recheck_2x.md)

## Correction from the corpus work (27 Nov 2026; `targets/ljs51corpus/`, keys_eye/REPORT.md)

The volume's write-up (`docs/ljs51corpus.html`) found that quire 3 (ff. 13-20) is bound out of place. Consequences here:
the cipher on ff. 20r-20v (chain 20r.8) is not another copy of this riddle but the first five verses of al-Jawlani's
eight-verse riddle, continued on f. 47r (one cipher, keys_eye/20r.8+47r.1.json); and the five cipher lines at the top of
f. 21r continue the prose after جملته. The full transcription has 24 lines, 290 signs, 29 labels and 63 dividers. The original key gives 59 of the 62 letters in the continuation. Two added labels account for the rest: W2 gives ا and EK gives ح in حين and ش in واشكر. A positional comparison against the clear prose found 44 matches at its ending and at most 11 elsewhere. The physical order of the quires still needs inspection. The alignment, blind trials, statistical tests and Dudout's independent check refer to ff. 48r–48v alone.
