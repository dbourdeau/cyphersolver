# Penn LJS 51, f. 48r l.8 - 48v l.13: an enciphered copy of al-Jawlānī's rhymed-prose riddle

Status: read
Outcome: key recovered from ciphertext-only (blind annealing; the plaintext match came after), 27 Nov 2026. The block
enciphers the first 232 of the 293 letters of the riddle written in clear on f. 21r l.7 - 21v l.2; aligned, 220 of its
228 signs (96.5%) take the key; the rest are scribal slips or
the three places where the cipher corrects the record of the clear copy. Every sign has a value.

Source folder: the corpus work in the main checkout, `targets/ljs51corpus/` (`solve_48r/`, chain records 48r.8, 47r.1
and 20r.8, `translation_0006_0053.md` section 20r.8, `NOTES.md`). Copied here: `REPORT.md` (the result and method),
`recheck_2x.md` (the 2x re-read), `ruleout.txt` (the rule-out against 206 plaintexts), `transcription.txt`
(= `solve_48r/transcription_v2.txt`), `anneal_sp.py`, `verify_v2.py` (run from `solve_48r/`; paths are relative to it).
New here: `key.json`, `decode.py`, `reading.md`, `translation_en.md`, `validation.tsv`.

One key, one entry: this block has its own key. The same volume's f. 106v cipher (`targets/qaysarani1350/`) and the f. 47r
block (chain 47r.1) use other keys; the riddle's other encipherment, chain 20r.8 (f. 20r l.8 - 21r l.5), is not read here
(the corpus attempt on it scored at chance) and its signs were not compared with these.

## The document

- University of Pennsylvania, Kislak Center, LJS 51, f. 48r l.8 - 48v l.13 (OPenn master images 0084_0100 and 0084_0101,
  `https://openn.library.upenn.edu/Data/0001/ljs51/data/master/0084_0100.tif`). 19 lines of invented signs, groups of
  2-8 signs between dotted-stem dividers.
- Heading on 48r l.7: one word, first read وابعها [?] (chain record 48r.8: ورابعها "and the fourth of them" or واتبعها
  "and he followed it with" possible); the corpus recheck of 28 Nov 2026 gives ورابعها ("and the fourth of them"). No
  plaintext stands after the block, and the sender is not named. The corpus notes think a leaf was probably lost after
  f. 48 (not checked here).
- The remark on 49r that a cipher "was not solved except after much toil" belongs to the short block 49r l.1-4 (chain
  49r.1, answered by the verses on 49r l.6-7), per the corpus recheck of 28 Nov 2026; not to this block.
- Dating: the corpus notes put the correspondence of the volume c. 1325-1360 (al-Mutarjim active in Damascus before
  725/1325 and still there in 745/1344-45; Ibn al-Durayhim, d. 762/1361, praised in it). Penn dates the manuscript
  "14--" (as recorded for the sibling `qaysarani1350`). The compiler is probably Ibn al-Durayhim: supported, not proven
  (`ljs51corpus/identity_ibn_durayhim.md`).

## The plaintext

The compiler gives the riddle in clear on f. 21r l.7 - 21v l.2, after chain 20r.8, which the translation notes call
"the third of al-Jawlānī's test pieces". 20r l.7 introduces that block as "the third of the ciphered pieces"; 21r l.6
"I solved it quickly because of its ease"; 21v l.3-4 "its answer is mentioned in Sūrat al-Wāqiʿa" (the raised couches,
furush marfūʿa). 293 letters, 64 words (chain record 20r.8).

## The system

Simple substitution of invented signs for Arabic letters, right to left, a dotted stem between words (words may run
over a line end). Same sign family as the f. 47r block, different key. 228 signs, 27 sign labels (measured,
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
4. That text was recognised as the f. 21r riddle (plaintext of 20r.8). DP alignment with the key re-learned from it
   (`verify.py`, then `verify_v2.py`): v1 218 of 229 signs (95.2%); after the 2x re-read 220 of 228 (96.5%), 3 surplus
   signs, 7 dropped letters; the block covers 232 of the riddle's 293 letters and stops at جملته.
5. 2x-3x re-read of every flagged position on the masters (`recheck_2x.md`): five transcription errors, six misplaced
   dividers corrected (229 -> 228 signs).
6. Found a second time in the corpus recheck by a group-length search over the book's passages (43 of 49 groups;
   corpus NOTES, 28 Nov 2026).
7. Rule-out (`ruleout.txt`): the decoded block against all 206 plaintexts of the book: 20r.8 95.2%, next best 22.3%
   (22r.1), median 9.2%.

The annealer reached the text without it, so the reading is not an artefact of the alignment; the alignment figure
itself is self-consistency.

## What the cipher settles in the clear copy

- ترميها where the 20r.8 record reads توهمها; يحمد منها where it reads وخمد منها; القسي "the bows" where it reads
  العسى[?] (with وتطعنها الاسنه "the spears" after it). اوطا ظهر confirmed.
- Scribal slips in the cipher: الاكانف (ن and ا swapped), وطيها (ب dropped), تتجافاها (TH written twice), اصلاح (ل
  dropped, or a correction: see doubts), وجهها for وجمعها, منه ما for منها ما, جملها for جمالها.

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

No study of LJS 51 found (corpus prior-art notes; the sibling's vetting of 15 Nov 2026: Penn TEI, Digital Scriptorium,
DECODE, Tomokiyo, Lasry's list, web). DECODE has no record of the manuscript.

## Remaining gaps
- none for the block: every sign has a value; the 8 signs that do not take the letter of the clear copy as recorded are
  scribal slips or the three places where the cipher corrects the record (ترميها, يحمد, القسي).
- the ل of اصلاح (48r l.12): slip or correction, not settled (see Transcription doubts); does not affect the reading.

## Escalation
- [x] siblings: the f. 47r key tried (does not fit); 49r verses and the 47r riddle and answer verses tested
- [x] clear-pages: the clear riddle on f. 21r l.7 - 21v l.2 is the plaintext
- [x] known-keys: 47r.1 key tried
- [n/a] print: no edition or study of LJS 51 found
- [n/a] key-rebuild: the key is complete; all 228 signs have a value
- [x] retry: every flagged position re-read at 2-3x (recheck_2x.md)

## Correction from the corpus work (27 Nov 2026; `targets/ljs51corpus/`, keys_eye/REPORT.md)

The volume's write-up (`docs/ljs51corpus.html`) found that quire 3 (ff. 13-20) is bound out of place. Consequences here:
the cipher on ff. 20r-20v (chain 20r.8) is not another copy of this riddle but the first five verses of al-Jawlani's
eight-verse riddle, continued on f. 47r (one cipher, keys_eye/20r.8+47r.1.json); and the five cipher lines at the top of
f. 21r (62 signs) are the END of this block, read with this key unchanged (62 signs = 62 letters, 58 of 59 repeated-shape
occurrences on one letter; keys_eye/20r.8+47r.1.json, block_21r_1_5). So f. 21r once followed f. 48v, and the clear prose
on 21r l.7 ff. is this block's own solution. The 21r lines are not added to this folder's transcription, key or counts.
The page (sections 02 and 04, glance) says so; "the third of al-Jawlani's test pieces" is dropped from the summary.

