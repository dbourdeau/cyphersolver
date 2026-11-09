# Lord Cobham to Walsingham, May–June 1588 (BL Harley MS 287, DECODE R8490/R8492/R8495/R8496): key partly rebuilt, not read

Catalogue item: "Cobham (Belgia) to Walsingham, 4 ciphertexts" (DECODE R8490, R8492, R8495, R8496; rule-scored).
**22 Oct 2026, reading audit** (George Lasry's test: can a reader build coherent sentences and translate them?):
all four letters (R8490, R8492, R8495, R8496) are **decoded, not read**. READING.md gives isolated cipher words with
grades between ellipses; the clear English around them reads, the cipher passages do not, and no sentence of cipher
text can be built. Class read in part -> not read, method -> not solved; the 'about a third of the cipher words'
figure (0.35, never measured) is withdrawn as a reading figure. The partial key (signs.tsv) stands.

**22 Oct 2026, re-read** (REREAD_BRIEF, batch b13; `texts/R8490-R8496_reread_log.md`): the clear of ff. 80r-80v, 92r
and 96v transcribed as running text and every run re-checked on the 7,200 px images; partial readings with modern English
in `texts/<doc>_reading.md`, `_en.md`. f. 80r's "armada(s)" is **"treaties" / "treaty of [?Breda]"** (the third sign is
the 7-form e, not ∽ m; `texts/R8490_corrections.tsv`), so the hostages passage reads (*Touching hostages, yt ys honorable
for [7] to […] their surety to these termes, as usuall yn all treaties …*), as does the f. 80v run (*22 hath a desire to
retourne from theym*). The rest of the cipher still gives scattered words; the 21 Sept I-grade guesses are withdrawn. All
four letters stay **decoded, not read**. f. 97r is blank (no runs there).

Outcome: **read in part** (see READING.md; was "attempted, open" until the solver loops of 21 Sept). The cipher system has been identified and most of its alphabet has been rebuilt from
the decrypted sibling letters in the same volume. Only fragments of the four letters read with confidence.

## The documents

William Brooke, 10th Lord Cobham, was one of Elizabeth's commissioners at the Bourbourg peace talks with Parma's
deputies (spring–summer 1588). His letters to Walsingham are in clear English. Short passages and single words are
in cipher, set into the running text.

| DECODE | Harley 287 | date, place | pages with cipher | notes |
|---|---|---|---|---|
| R8490 | ff. 80–81 | Ostend, 5 May 1588 | f. 80r (about 12 cipher groups), f. 81 (2 lines) | "Julio Romeo, Cristophero Mondragon" and "Doctor Dale" in clear |
| R8492 | f. 88 | undated, 1588 | f. 88r: the densest cipher (about 14 lines) | "captain Montgomery ... of late gone into Scotland ... with 40 men of ..." |
| R8495 | ff. 92–93 | 27 May 1588 ("Belgia") | f. 92r, about 8 lines | news: the Armada still at Lisbon, Gonzaga, 200 mariners at Sluys |
| R8496 | ff. 96–97 | Bourbourg ("Binborow"), 9 June 1588 | ff. 96r–97r, scattered | |

Images: DECODE, fetched with the session cookie (see memory decode-access). They are BL images, not in the public
domain: kept in `tmp/cobham/` (git-ignored). Nothing from them is committed except derived text.

DECODE R8497 (Harley 287 f. 187, "The Cowler Cipher for Mr Bodley ... in the Low Countries", December 1590) is the
key record the catalogue pointed at. It is **Bodley's** cipher of 1590, a different alphabet, and does not
apply to these letters.

## Prior art

- CSP Foreign vol. 21 pt 4 (Jan–June 1588) calendars the Cobham letters in SP 77 (Flanders), for example 1 May,
  3 June, 6 June and 10 June. It does not calendar these Harley 287 letters. No printed decipherment was found.
- DECODE marks the sibling Cobham letters in the same volume as **Decrypted**: R8481 (f. 63, Mar 1587/8),
  R8488 (ff. 75–76, Ostend 9 Apr 1588), R8489 (ff. 78–79, Apr 1588), R8493 (f. 89). Their cipher passages carry
  a contemporary **interlinear decipherment**. They are the source of the key below.
- A second session (cypher-7e, folder `harley287`) is working the same system on R8477–R8487 (Ostend, March
  1587/8). Key notes were exchanged on 21 Sept 2026.

## The system

A **monoalphabetic substitution with homophones** in Greek-like letters, arbitrary signs and a few Latin letter
shapes. Nulls are dots, dashes and ".." marks, though ".." also stands for u/v. A few signs are **code signs**; a
square (◻) is one. Word division is mostly kept. It is the same system as the glossed March–April letters.

Key rebuilt from the glosses of f. 75 (R8488: "upon our arrival", "willing to harken", "by the clergy they made
means", "discours", "sent from", "their great desir of", "cardinal is coming", "the pope's legate", "the Duke of
Parma his bastard son") and f. 89 (R8493: "what may be", "further hoped for at their hands", "our abode in this
towne is so advantagious"). The sign names are descriptive:

| plain | signs |
|---|---|
| a | U / ∪ |
| b | + |
| c | 8 |
| d | ∞ |
| e | 7 |
| f | H |
| g | crossed X (Ж) |
| h | ϸ (loop on a long stem) |
| i | ⊥, X (undotted) |
| k | ω |
| l | ϕ (small loop), L, and ".." after a letter (cypher-7e) |
| m | ∝ (loop with tail) |
| n | ǂǂ (double-barred cross) |
| o | Z (z-shape), c, d |
| p | ϑ |
| r | V, γ |
| s, t | Λ (two near-identical forms; not separated) |
| u / v | "..", ":" |
| w | ẋ (dotted x) |
| y | γ |

Doubtful or missing: j, q, x, z. There are unidentified signs on f. 88 (K, υ, ρ, W) and unnamed code signs. Because
the s/t and r/y signs are shared, a letter-by-letter reading needs a clean sign-level transcription. This session
did not make one.

## What reads

Fragments only, grade M (probable) unless marked:

- f. 80r: "hoping them in the ◻ [code] …ances for what chaunces so ever" (the cipher word ends -ances); "it will
  not be … the ho-v-en [haven?] is …" (uncertain); "in all ΛVZΛTΛ in numbers, that at the ΛVZΛT …, which was
  the 20" — the word could not be resolved: ARMADA does not fit the key (V = r, Z = o).
- f. 92r: "imprisoned in …", "it is reported that they have … of letters" (ϕ7ΛΛ..⊥VΛ, l-e-t-t-[e]-r-s, H).
- f. 88r: the clear frame reads "There is captain Montgomery of late gone into Scotland" [cipher] "with 40 men of"
  [cipher] "which have promised the" [cipher] "15 of late there is" …. The cipher words contain signs not in the
  table.

## What would finish it

1. A sign-level transcription of the cipher passages on ff. 80r, 81, 88r, 92r and 96r–97r, from full-resolution
   crops (the images are 7200×10200 px, so each passage can be cut at about 4× reading size).
2. Separate the two Λ forms (s/t) and the r/y signs from the glossed siblings, if they differ at all.
3. Merge with cypher-7e's `harley287` key for R8477–R8487.
4. Read the passages. The letters are in plain English and the context is known (Bourbourg talks, Armada news).

Status (21 Sept; superseded 22 Oct 2026, now decoded, not read): read in part.
- Cross-link: cypher-7e read R8482-R8487 (docs/harley287.html, targets/harley287/key.tsv); its key has narrow ∧ = s, wide ∧ = t.

## Second pass, 21 Sept 2026 (with the harley287 key)

Close crops (about 1.2× the full-resolution scan) of ff. 80r, 88r and 92r. Sign copies below are as seen; "?" is an
unidentified sign. The narrow and wide ∧ forms and the ϕ-family (l / p / h) cannot be told apart reliably at this
resolution, so the readings are from context and graded M or I.

f. 80r
- "and to our drag our forces ffrō c VIII8 f hoping them X ǂǂ ∧ϸ7 ◻ ϸ∪ǂǂ87∧ for what chaunces so ever you bestow
  (and that must be great) it will ǂǂc∧ -7 WLϕ∧· ∧ϸ7 ϸo··7ǂǂ ⊥∧ Xd+o:·87 ) and me[mo] c: other wind hath blown …"
  - "them in the ◻-pances": probably "expences" with ◻ standing for ex- (M). "it will not be … the haven(?) is …" (I).
- "yf honorable for 7/∧c∂ oo7ϸ… ∪ǂǂ∧ϕ… (a long run, unread)", "as usuall in all ∧VZ∧T∧ in numbers, that at the
  ∧VZ∧T c ǂǂ-V7oo which was the 20 and the ∧··- ⊥Ӿ8∧" (unread; ARMADA does not fit).

f. 88r
- "There is captain Montgomery of late gone into Scotland. 8⊥ϸ? ω c ǂǂ K ∪ ϕϕ ∧ ρ c V X ϸ with 40 men of ⊃8cǂǂ∪ have
  promised ∧ϸ7 [the] ϸo··Lǂǂ of V∪+ǂǂ ∩ϕd∧ yn X c·⊥V∪ ∧ϸ7V to 15: of late there is …" (unread beyond "the").
- next line: "… ∧7HLV∤∧ which have ⊃ẋV∧ ϕ7ǂǂ∧∤cǂǂ ϕcǂǂ∧ϸϕT …" (unread).

f. 92r (27 May), after "200 mariners of Hambourgh that were at Sluys are returned to Dunkerk"
- "⊥7ẋ⊥∧ ϕ⊥ẋϸϕ7ǂǂ and 8-ϕ⊥∪V ⊥cǂǂ ∩cǂǂ sent by …", "imprisoned in -V+o∓7∧. It is reported that they have 8ϸcVX
  …", "of ϕ7∧∧··⊥V∧ which …" = "of letters" (M).

Verdict of the second pass: not readable from the scans at sign level by this method. What would move it is a
human transcription at the BL (or the DECODE images at full zoom, glyph by glyph, with a sign inventory drawn
from the glossed ff. 75 and 89 first).

## Third pass, 21 Sept 2026: sign inventory by eye from the glossed leaves

At full scan resolution (7200 px wide) the signs are clear. About 60 glossed words on f. 75 (R8488), f. 79 (R8489,
16 April 1588, the richest) and f. 89 (R8493) were aligned sign by sign; the result is `signs.tsv`. What it settles:

- The families that looked alike separate cleanly: **p** = loop with its tail swept down-left (upon, popes, perswade,
  prelates, persons); **l** = circle crossed by a straight stem (arrival, legat, holding, stil); **h** = stem with a
  bowl to the right (the, harken, thought, hands); **m** = horizontal S with a loop (made, means, perform, coming,
  commission, him); **w** = dot and stroke (willing, newe, sworne, warres, wel).
- The system is **more homophonic, and more polyphonic, than any key so far allowed**: ∧ is s *and* t (and, on
  f. 80, probably a); γ is r *and* y; c is o and once a; ϕ is l and once t. That, not the image, is why the four
  May–June letters do not fall to substitution.
- **Code numbers** are glossed: 7 = her Majesty, 10 = the Lord Admiral, 15 = the Duke of Parma, 16 = the King of
  Spain.

New readings in the target letters (grade M unless stated):

- f. 80r: "as usuall in all **armadas** in numbers, that at the **armada** …, which was the 20" — ∧V∽∧ŧ∧ with
  ∽ = m (glossed) forces ARMADA if the wide ∧ is a and ŧ is d. "hoping them in the ◻**pances**" (ϑ = p, glossed):
  "expences" with ◻ an unglossed sign (M). A run with vertical word-dividers ends "… **to these termes**"
  (∧z | ∧ϸ7∧ | ∧cV∽7∧, with c = e) (M). Last lines: "… **22** is … in the **action** … that he promised
  **Q[ueen]**: … 27 to begin …" (codes 22, 27 unglossed).
- f. 88r: "15:" is **the Duke of Parma**. The opening cipher probably begins "**captain** …" (8⊥ϑ∧…ǂǂ) before a
  name, then "with 40 men of …, [who] have promised the …". The rest turns on signs no gloss shows (L, K).
- f. 92r: "**4** sent by ϑoc··Ӿϕc∧" — perhaps "Portugals" (I); "of **letters**" (M).

Verdict: the sign inventory is now fixed and published; the letters remain unread because several signs are
polyphonic and a few are unglossed. The next step is not more image work but a solver: treat each sign as a set of
possible letters (from `signs.tsv`), enumerate the readings of each cipher word against an English 1580s word list,
and let the clear context choose. That is mechanical and can be scripted from a sign-level transcription of the
runs, which the crops in this pass make possible.

## Fourth pass, 21 Sept 2026: candidate-set solver

`runs.txt` holds a sign-level transcription of 22 cipher runs (ff. 80, 88, 92) in an ASCII sign code. `solve.py` gives
each sign its set of letters from `signs.tsv`, enumerates each cipher word's readings, and scores them against
`wordfreq.tsv` (25,488 words from CSP Foreign vol. 21 pt 4, Jan–June 1588, 266,800 words, plus Gutenberg English
and the glossed plaintext). Elizabethan spelling is normalised (u/v, i/j/y, doubled letters, final e). A fuzzy pass
allows one wrong, extra or missing sign (two for words of 7+ signs). Output: `solve_out.txt`.

Words the solver confirms in context (exact match unless marked "near"):
- f. 80: "in **the** [◻] …", "it will **not be** … **the** …", "to **these** **terms**" (near), "all **armada(s)**",
  "at the **armada** (near: arms) **on** …", "in the **action** (near) that he promised Q[ueen]".
- f. 88: "**captain** (near, 2) …", "have promised **the** …", "in **years**(?) **there** to 15".
- f. 92: "of **letters** (near, 2)", "they have **charge** …", "**clear**" (near), "**legat**" (near).

The long runs (f. 80g, f. 88a second word, f. 88b–d, f. 92a–b, d) find no sensible word, even with two edits. That
points at the transcription of those runs, not the key: the next step is to re-read just those runs at full
resolution with the solver's near-candidates in view, correct `runs.txt`, and rerun. The solver makes that loop
quick.

## Solver loop 1 (f. 88 first), 21 Sept 2026

Re-read at 2x full resolution with the solver's candidates in view; corrections put into `runs.txt`, solver rerun.

- **haven** (H): f. 88 "have promised the ϸc··Lǂǂ" and f. 80 "the ϸc··7ǂǂ is" are the same word, h-a-u-e-n. It
  fixes two things: c stands for a here, and the L-shape (unglossed) is e.
- **forwarde** (H): f. 80, "Dunkergh: 22 is so **forwarde** in the **action** that he promised Q[ueen] to …". The
  first sign is the barred H (f), not n, and ·\ is w: H c V ·\ ∪ V d 7.
- f. 88 now reads: "There is captain Montgomery of late gone into Scotland. [captain(?) + name] with 40 men of …,
  [who] have promised **the haven** of V∪⊥ǂǂ (Rain/Rayne?) … yn … there to **15** [Parma]." CSP Foreign 1588 has
  the King of Spain sending **Semple** (the betrayer of Lier) to Scotland in May 1588; the cipher name after "captain"
  does not spell Semple, so it stays open.
- "an app(e)ring" (∪ǂǂ ∪ϑ7V⊥ǂǂӾ, 1 edit) on the next f. 88 line.
- `solve.py`: added the L sign (e), widened d to {o, d}, and a gazetteer of 1588 places and people.

Open after loop 1: the name after "captain", the word after "haven of", f. 88 lines 3–6, f. 92a–d.

## Clear-duplicate check, 21 Sept 2026
CSP Foreign vol. 21 pt 4 calendars Cobham letters of 1, 4, 9, 13, 24, 29 May and 3, 6, 10 June 1588 (SP 77), none dated 5 May, 27 May or 9 June: no clear duplicate of these Harley letters exists in print. 3 June: "Sent the cipher by Spritwold." Lead closed.

## Remaining gaps

- R8490 (ff. 80r-80v), decoded, not read: runs c∪ǂǂ8ϕ, WLϕΛ, Xd+c:·87, ∞7γǂǂcL and the 22/27 passage of ll. 31-34; codes 22, 27 and the square - blocker: no-key-material; W, the square, 22 and 27 are glossed in no sibling (R8481, R8488, R8489, R8493); the hostages passage and the f. 80v run now read (b13)
- R8492 (f. 88r), decoded, not read: name after 'captain', words after 'haven of', ll. 3-11 and the cipher words of ll. 12-20 - blocker: no-key-material; signs K, ɔ/Q, upsilon, rho glossed nowhere; polyphonic signs leave several readings with nothing to choose between them
- R8495 (f. 92r), decoded, not read: runs 92a-c and the ten cipher lines below "Dunkergh: 4 sent by" - blocker: no-key-material; same signs; solver finds no word with two edits
- R8496 (f. 96v), decoded, not read: all runs but a few probable words - blocker: no-key-material; same signs; f. 97r is blank
- Clear text of f. 96r (R8496) and the bracketed secretary-hand words of ff. 80, 88, 92, 96v - blocker: not-attempted; outside the cipher, not transcribed on 22 Oct 2026

## Escalation

- [x] siblings: glossed R8481, R8488, R8489, R8493 aligned sign by sign (signs.tsv); cypher-7e's harley287 key for R8477-R8487 merged; R8497 checked (Bodley 1590, different alphabet)
- [x] clear-pages: CSP Foreign 21 pt 4 searched for clear duplicates of the 5 May, 27 May and 9 June letters: none (commit 95d37d2f)
- [x] known-keys: harley287 key and Bodley's R8497 key tried
- [x] print: CSP Foreign vol. 21 pt 4 (Jan-June 1588): Harley 287 letters not calendared, no printed decipherment
- [x] key-rebuild: candidate-set solver (solve.py, CSP 1588 word list) with solver loop 1: L = e, c = a, phi = p added
- [x] retry (22 Oct 2026, b13): every run of ff. 80, 88, 92, 96v re-read on the 7,200 px images at 0.5-1.0x with the clear text transcribed round it; f. 80 relabelled (treaties, hostages, surety); f. 97r is blank, so nothing to add to runs.txt; partial readings in texts/

## Contribution, 9 Nov 2026 (Brice Dudout, with Claude): held-out test of the key, codes 22, 26, 27 and the square

See `dudout/README.md` (text only, no image). An alphabet learnt only on the glossed cipher words of f. 78r (DECODE
R8489) was tested once on every glossed cipher word of f. 78v (349 letters): character agreement 0.917 against at best
0.284 for 200 shuffled keys (criterion fixed in advance: 0.85 and best + 0.30), with the errors all on the shared signs
(caret s/t, gamma r/y) and d = o. Declared deviation: the f. 78v crops showed the glosses while the held-out cipher was
transcribed (key already frozen). The f. 78r gloss names three codes: **22 = Sir James Croft** ("Sr J: Croftes"),
**27 = Dr Valentine Dale** and **26 = Dr John Rogers** ("D: Dale and D: Rogers revoked"), and the square = "ye States".
In R8490: "[22: Sir James Croft] is so forwarde yn the action that he promised Q[ueen] to send to [...] [27: Dr Dale] to
begyn the openning of the [...]" (f. 80r) and "[22: Sir James Croft] hath a desire to retourne from theym" (f. 80v). The
class is unchanged: R8490 is still decoded, not read.
