# The Catokwacopa advertisements (1875) — which readings the letters force, and which are guesses

Two personal advertisements signed *W.*, *The Standard*, p. 1 col. 2, 8 and 20 May 1875. The second
ends in clear: *"This will be intelligible if read in connection with my communication published in
this column on the 8th inst."* Number 8 on Schmeh's Top 50, republished on klausschmeh.net on
14 August 2026 with an active thread.

## State of play (September 2026)

The mechanism is agreed. Line *i* of the first ad and line *i* of the second are two order-preserving
halves of one plaintext phrase, from which W. also dropped letters. Nothing is substituted. Readings
have accumulated since 2018: Thomas Bosbach's DYING DECLARATION; Lance Estes and "Dave"'s Oxford
vocabulary (SUMMER TERM, 1853, CONINGTON, JOWETT, BALLIOL, SHIRLEY, I ADDED FIRST LINE SATIRS);
Thomas Ernst's diplomatic line numbering and BNA-checked text; Jozef Krajčovič's QUI FIT (Horace,
*Satires* 1.1) and his 2026 exact-cost audits. They disagree, above all over how much emendation is
allowed. Ernst has proposed SIGNED DECLARATION RELIGIONEM CONFIRMARE and MASTER PUPIL; Krajčovič
costs the former at 14 edits.

**The unanswered question is how much the omission rule lets you read into a line.** With three to
twelve letters freely inserted, plausible English can be made to fit almost anything. Readings are
worth something only where the letters force them. This attempt measures that.

Text: Ernst's BNA-verified transcription (`ads.py`), which corrects a dozen errors in the circulating
one (Hrsclam, 138 not 139, Etfdorshpxn, Tsvlysdinlge, Wtubtrfftrstendinhofsvmnr, …).

## 1. The line pairing is structural, not a reader's choice

Both ads have the same token skeleton, with numerals and dashes in the same slots (`Rep.–`/`Etd. –`,
`Ap. 138.–`/`A.P. 138.–`, `mistrl.–Ding`/`Oatvpu.–Y`). The letter totals are 222 and 219. Over the 24
letter lines, the summed length difference between paired halves is 33; **no random re-pairing in
100,000 comes that close** (`python mech.py`). So W. split each phrase roughly in half, and the pairing
is real.

## 2. The two halves are different in kind

For each word of the readings that fit exactly, I checked which ad supplies its first letter:

* **Consonant-initial words begin in the 8 May half, essentially always**: summer, term, cap, took,
  college, party, broke, left, repeated, conington, hertford, scholarship, motto, previously, second,
  first, line, satirs, qui, fit, told, shirley, dying, declaration. The one exception is *corner* in
  line 4.
* **Vowel-initial words mostly begin in the 20 May half**: away, at, attended (twice), us, is, in,
  instead.

The 8 May half carries onsets, and its line-initial letters are almost all consonants
(`scocsrimhcmciqcbhitimdde`). The 20 May half is vowel-heavy and rich in t, n, d, r, the letters of
inflections and endings. That gives a positional prior which discriminates between rival readings.
For example, I ADDED FIRST LINE **SATIRS** keeps the rule (**SAT**irs), while I ADDED FIRST LINE
**IS ARTS** breaks it (*i*s from the second half).

## 3. Exact costs of every published reading

`cost` = letters W. omitted / cipher letters that must be misprints (`python mech.py`):

| line | reading | omitted | misprints |
|---|---|---|---|
| 27 | DYING | 0 | **0** |
| 28 | DECLARATION | 0 | **0** |
| 16 | I ADDED FIRST LINE SATIRS | 1 | **0** |
| 17 | QUI FIT | 1 | **0** |
| 24 | TOLD SHIRLEY | 1 | **0** |
| 3 | CAP TOOK AWAY AT COLLEGE PARTY | 2 | **0** |
| 4 | OLD CAP BROKE AT CORNER LEFT INSTEAD | 2 | **0** |
| 7 | REPEATED | 2 | **0** |
| 1 | SUMMER TERM | 3 | **0** |
| 8 | I ATTENDED CONINGTON LECSURES | 4 | **0** |
| 25 | I ATTENDED JOWETT LECSURS | 4 | **0** |
| 15 | CONINGTON TOLD US TO ADD A SECOND MOTTO | 7 | **0** |
| 10 | HERTFORD SCHOLARSHIP EXAMINATION | 12 | **0** |
| 14 | MOTTO WAS PREVIOUSLY DISCLOSED IN COLLEGE | 14 | **0** |
| 5 | CONINGTON MET ME IN GARDEN | 5 | 1 |
| 27 | DOING | 0 | 1 |
| 17 | QUIT | 0 | 1 |
| 18 | COUNTED CAP / CONINGTON DEPARTED | 1 / 7 | 3 / 2 |
| 21 | HAD EXAMINATION | 6 | 3 |
| 9, 26 | MASTER PUPIL | 2 | 4 |
| 27 | SIGNED | 1 | 3 |
| 29 | RELIGIONEM CONFIRMARE | 4 | 7 |

This confirms Krajčovič's audit: DYING is exact and SIGNED is not, so DYING DECLARATION stands and
SIGNED DECLARATION is an emendation. MASTER PUPIL needs four misprints in a six-letter half, so it is
not a reading of these letters.

## 4. Which lines the letters decide: an open-vocabulary search

`search.py` enumerates **every** word sequence that fits a line exactly, with no misprints. The
vocabulary is about 30,000 words from 24 nineteenth-century novels, ranked by word frequency, omission
count and the positional prior from §2. It is not given the published readings. It is run twice: once
with a list of the Oxford names the readings use, once without (`search_all.txt`,
`search_all_nonames.txt`).

**Forced by the letters and ordinary vocabulary**, where the search's top reading is the published one
or close to it without any name list:

* 27 DYING · 28 DECLARATION · 7 REPEATED
* 4 OLD CAP BROKE AT CORNER LEFT INSTEAD (top of 30,000-word search)
* 3 CAP TOOK AWAY … PARTY (the middle word contested: *at college* against *catalogue*)
* 16 I ADDED FIRST LINE(S) …
* 1 SUM TERM (SUMMER TERM also fits; the search prefers the abbreviation)

**Exact alternatives the published readings missed:**

* **18 `cagap / ndted` → CHANGE ADOPTED / ADAPTED**, exact. The published COUNTED CAP and CONINGTON
  DEPARTED need 3 and 2 misprints.
* **21 `hodsam / yxn` → HOLIDAYS EXAMINE(D)**, exact. HAD EXAMINATION needs 3.
* **14 `mopredisco / tsvlysdinlge` → MONTHS PREVIOUSLY (or PRIVATELY) DISCLOSED …**, sharing its core
  with Krajčovič's MOTTO WAS PREVIOUSLY DISCLOSED IN COLLEGE but with far fewer omissions.

**Not decided by the letters at all:** 9 and 26 (`mistrl / otenpu`, `mistrl / oatvpu`), 12, 23, 29.
Many unrelated readings fit within a nat or two of each other (*omit stern pull*, *moist relative
put*, *retire followed both mare*). Any reading of these lines is a conjecture, including the author's
own here.

## 5. The name cribs are specific — this is the strongest evidence for the Oxford reading

CONINGTON, JOWETT, SHIRLEY and HERTFORD were introduced as guesses, and without them the search cannot
find those lines. So each frame gets the reverse test (`python names.py`): substitute every one of
**1,645** names and proper nouns from the corpus, and count those that fit exactly with no more
omissions than the published name:

| line | frame | names that fit |
|---|---|---|
| 8 | I ATTENDED ___ LECSURS | **CONINGTON only** |
| 25 | I ATTENDED ___ LECSURS | **JOWETT only** |
| 24 | TOLD ___ | **SHIRLEY only** |
| 15 | ___ TOLD US TO ADD A SECOND MOTTO | **CONINGTON only** |
| 10 | ___ SCHOLARSHIP EXAMINATION | **HERTFORD only** |

A frame that lets a thousand names through would prove nothing. These let exactly one through, and
the parallel lines 8 and 25 each admit a different Oxford classics lecturer of the 1850s. So the frame
readings carry real evidential weight. **The Oxford reading is right in outline**: an 1850s Oxford
undergraduate recalling Conington's and Jowett's lectures, the Hertford scholarship, and a motto
disclosed or used before, closing with a DYING DECLARATION. The frames themselves are partly the
readers' choice, though, and lines 9/26, 12, 23 and 29 remain unread.

## What would finish it

* **Line 29** (`ereflodbr / rileohmae`) completes DYING DECLARATION. It is short enough for an
  exhaustive search over a Latin vocabulary (Ernst's RELIGIONEM CONFIRMARE is 11 edits away) and over
  English phrases, with the positional prior.
* **Line 23** (48 letters) needs a phrase-level language model, not unigrams.
* **Identity**: Ernst's candidate (a W-initial Balliol commoner of 1856) against Krajčovič's
  Jex-Blake, who won the Hertford in 1853. The £138 in line 20 and the DYING DECLARATION of line 27
  are the checkable facts.

Reproduce: `python mech.py` (pairing test, exact costs), `python -c "import mech; mech.rule_report()"`
(positional rule), `python search.py all [--no-names]`, `python search.py 23`, `python names.py`.

## 6. Line 29 in Latin (2026-09-15, second session)

`latin.py` runs the same exact-interleaving search with a Latin vocabulary (19,291 words from 43 Latin Library texts:
Caesar, Cicero, Vergil, Livy, Sallust, Ovid, Horace, Vulgate; u = v, i = j) and a flat positional prior. Control:
line 17 `qft / ui` returns **QUI FIT** first (Horace, *Satires* 1.1, the accepted reading), ahead of *qui fuit*; the
English run puts it ninth behind *qu fit* and *quite fit*. Line 28 returns *declarat omni*, a worse fit than English
DECLARATION (exact, no omissions), so the mixed-language reading of 27-28 is not supported.

Line 29 `ereflodbr / rileohmae`: the best Latin readings are three- and four-word junk (*et refer illo debeo
hiemare*, -61; *uereri fallor debeo hiemare*), as the English ones are (*retire followed oh embrace*, -56). Neither
vocabulary produces a two-word reading without omissions. Ernst's RELIGIONEM CONFIRMARE stays at 11 edits and is a
conjecture; **line 29 is undetermined in both languages.** The English corpus for `search.py` was rebuilt from 24
Gutenberg novels (`../beale/lmcorpus/`), so `vocab.tsv` differs slightly from the first session's.

## 7. Push to 95% and a sense measure (2026-10-05, third session)

**Re-transcription: externally blocked.** The only images of the ads outside the British Newspaper Archive are the
two on klausschmeh.net (now in `img/`, `Catokwacopa.png`, `Catokwacopa-2.png`). They are re-typeset illustrations of
the *old* circulating text, not scans: they show Hfsclam, 139, Eftdorshpxn, Tavlysdinlge, Dmlurpinrtrcamur,
iolapstedtioc and Wtubrfftrs, every one of which Ernst corrected against the BNA originals in 2018 (#24-#25). So they
cannot correct Ernst; they are older and worse. The originals (The Standard p. 1 col. 2, 8 and 20 May 1875) are on
the paywalled BNA; nothing here can be re-read at higher resolution without a subscription. Ernst reported no
doubtful letters in the May ads (his doubtful m/nr and o/b are in the March ad, a different text).

**Phrase-level search (`beam.py`, `beam_open.txt`).** The gap list said line 23 needed a phrase-level model. `beam.py`
generates the plaintext letter by letter under the shared `lang` en-modern 5-gram, each word in the vocabulary,
every cipher letter consumed in its stream, 2.3 nats per omitted letter. Controls: line 7 REPEATED, line 18 CHANGE
ADOPTED, line 3/4 come out on top. On the open lines it gives junk: 23 *with you but portion frog fit first me and
in she chairs of seven mr nor*; 29 *terrible flowed to him bare*; 9 *mist often purely*; 26 *moist relative put*;
12 *case land clutch so find size as more to*; 6 tail *... short is trick arm nor*; 19 *bit of all man postponed
to seems to cover*; 21 *how days examine* against *hold say mixing* (HOLIDAYS EXAMINE no longer first); 5
*conviction me me garden*. The phrase model decides nothing the unigram search left open.

**The old measure did not count sense.** 0.747 counted every character of a line as read whenever any proposal
existed: line 6 (SAID SIMPLY YOUR CAP IS HONESTY IN CHARACTER, 7 misprints), 19 (BALLIOL MAN POSTED, 11 misprints),
21 (HAD EXAMINATION, 3), 5 (1 misprint, not the top fit), 13 (`1.6.9 / cotegr`, no reading at all) and 20 (A.P. 138,
meaning unknown) were all counted read. `measure.py` counts a character only when a misprint-free reading the
letters force consumes it (top of `search.py` or `beam.py`, or a name frame that admits one name in 1,645), and the
credited words score as English under en-modern (> -2.5/char, names and W.'s spellings normalised for the test).
Line 6 is credited for USED SIMPLY YOUR CAP only, line 14 for MONTHS PREVIOUSLY/PRIVATELY DISCLOSED only.

| | old (lines with any proposal) | sense measure |
|---|---|---|
| 8 May ad | 178/238 = 0.748 | 134/238 = 0.563 |
| 20 May ad | 173/232 = 0.746 | 123/232 = 0.530 |
| both | 351/470 = 0.747 | **257/470 = 0.547** |

The honest figure goes down, not up. 95% is not reachable from these letters: the unread lines are open because many
readings fit, and no image, sibling or key can choose between them.

## Remaining gaps

- lines 9 and 26 (mistrl / otenpu, oatvpu) - blocker: too-short; unigram and phrase-level searches give many unrelated exact fits
- line 12 - blocker: too-short; phrase-level search gives junk
- line 23 (48 letters) - blocker: too-short; phrase-level 5-gram search run 5 Oct 2026 (beam.py): junk, no forced reading
- line 29 (ereflodbr / rileohmae) - blocker: too-short; English (unigram + 5-gram) and Latin searches give only junk
- line 5 - blocker: too-short; CONINGTON MET ME IN GARDEN needs one misprint and is not the top fit
- line 6 tail, line 14 tail, line 19, line 21 - blocker: too-short; several exact fits, none forced
- line 13 (1.6.9 / cotegr), line 20 (A.P. 138) - blocker: too-short; no reading of the figures
- re-transcription - blocker: needs-physical-access; originals only on the paywalled British Newspaper Archive; the blog images are re-typeset from the old text

## Escalation

- [n/a] siblings: two newspaper advertisements, both used; the March 1875 ad and the 1879 Fact or Fiction ads are a different system
- [x] clear-pages: the clear closing sentence of the 20 May ad used to pair the ads
- [n/a] known-keys: no key: the mechanism is interleaving with omissions, not substitution
- [x] print: Schmeh blog thread, Bosbach, Estes, Ernst BNA text, Krajcovic audits reviewed
- [x] key-rebuild: open-vocabulary exact-fit search (English 30k, Latin 19k) and name-frame tests
- [x] retry: phrase-level 5-gram search on every open line (beam.py, 5 Oct 2026): no line decided; images checked, BNA originals blocked
