# Juan Manuel to the Catholic Monarchs, Genoa, 14 April 1497 (AHPZ, Colección Zurita, C_CRAR/000001/0039; catalogue 2857)

Status: in progress. Deciphered in part with George Lasry's key for BnF Espagnol 318 no. 95 (8 January 1497),
applied unchanged: 45 of 56 cipher words read on the working transcription (80%), 38 of 56 (68%) on the strict
blind transcription. Read in part, under the read bar. The reading awaits a reviewer's `reading_review`; no
write-up page yet. All of this was done by AI agents on 16-17 Nov 2026; no person has checked any of it.

**The first planned test passed on the first transcription and missed on an independent blind one.** Lasry's key
scored 73.85% (mark 70%) on the transcription made by the agent that matched the key, and 46.55% on a transcription
by two fresh readers who knew no sign values. The miss is explained below, not excused. A second test that needs no
word division passed on the blind text: the real key beats all 1,000 permuted tables by a wide margin.

**The key is verified on unseen text in the sibling target `../juanmanuel1496/`.** Juan Manuel's letters from Genoa of
10 November and 18 December 1496 (BNE MSS/20212/61/1-2) are in the same cipher. Lasry's key, unchanged, passed both
planned tests on the letter of 18 December before anyone had decoded it, and an independent check with its own blind
readers passed every mark on both 1496 letters. That is the main evidence that this letter, too, is in his key; the
two tests of this folder stand as they were run.

## The document

Archivo Histórico Provincial de Zaragoza (Archivo del Reino de Aragón), Colección Zurita, C_CRAR/000001/0039: one
letter on one leaf, recto and verso. The archive's record, with the images: <https://dara.aragon.es/opac/app/item?i=1056536>
(DARA; the images are for personal use only, and publishing them needs the archive's authorisation, so none is in
this folder).

- **Recto.** The heading "Muy poderosos señores" and seven lines of clear Spanish in a very cursive hand (not
  transcribed here). Then the cipher: seven full lines and two signs, 224 sign positions in the working
  transcription. The right-hand cipher on line 8, after some clear words, continues line 7 ("...no se hazer a-");
  "si." at the left of line 8 ends the passage. Then the clear dating "de Genoua a ... de abril" (read in part) and
  the signature "Juan Manuel". Nothing is written between the lines or in the margins: no decipherment of the time.
- **Verso.** An address in a cursive hand, a seal under a paper slip, an endorsement at lower right naming Juan
  Manuel (read in part), and show-through of the recto cipher.
- The catalogue's "about 15 lines" of cipher is an over-count: there are eight (seven and a fragment).
- Juan Manuel was the Spanish envoy at Genoa. The DARA summary says half of the letter is in cipher.

## The key: Lasry's no. 95 key, by reference

The key is George Lasry's CTTS key for BnF Espagnol 318 no. 95, in his target:
`../esp318no95/lasry2021/ctts/key.txt` (sha256 5ee40781ca8a562dcfd1a760b88806a24f458140007c3ea376cb638c4f08fb06), with
his key image `../esp318no95/lasry2021/cryptiana/images/esp318_1497_key.png` (sha256
b3a4e5a4b3122a946931e054522d3acc47a6eb248c9470eed11cbad770924372, "key updated October 2026"). Nothing of his is copied
here; `decode.py` reads his file by relative path and checks the hash.

- 21 letters with 44 invented signs (one to four each: A2 B1 C2 D3 E2 F1 G1 H1 I2 L3 M3 N2 O3 P2 Q2 R4 S2 T2 U2 Y2
  Z2), three special signs, and 11 code groups written in letters (bac ciudad, bcd cardenal, bnh rey, bon gente, dae
  papa, dif "rey de romanos?", and five unidentified names boo, dah, dal, dcl, dnl).
- Applied unchanged: no value was changed, added or refitted. Signs that are not in his table get no value.
- The signs are named here by his CTTS names (`7`, `7-`, `7o`, `a_`, `ee`, `pi:` ...). Several of his names are
  letters that are not the sign's value: his `S` is a D sign, his `D` a null, his `C` a Y sign, his `L` an N sign.

## Transcription: four readings, eight readers (all AI agents)

The readers worked from enlarged line windows of the recto and a sign sheet: the 58 signs of Lasry's key image (44
alphabet signs, 3 special signs, 11 code groups) cut out, given neutral ids K01-K58 in shuffled order, with no values.
The id-to-sign map (`records/solver/signsheet_K_private_map.json`) was kept from the blind readers. In the check,
each cell of the sheet was located again in Lasry's key image by template matching: all 58 assignments agree, and the
number of signs per letter equals his `key.txt` (`records/verifier/locate_cells.log`). `make_transcriptions.py`
turns the ids into his sign names and checks that each name carries, in his key, the letter of the column it came
from.

**Round 1 (16 Nov 2026), the first transcription.** Reader A was the agent working the item, who knew the key; reader
B was a helper given only the line windows and the sheet. Three shape rules were settled before any decoding by
comparing shapes with Lasry's own leaf (f. 122r): B's T with two dots = Lasry's `T:`; B's closed o joined to a 7 =
Lasry's `7o` (S); B's dotted h = his H `I-o` plus a stray colon. Agreement: 214 of 224 positions (95.5%) after the
rules, about 195 of 224 (87%) before them. Of the ten disagreements, eight were settled by a third look at a zoom,
before decoding (`records/solver/adjudications.tsv`), and two stayed holes (the damaged ends of lines 4 and 5).

**Round 2 (16-17 Nov 2026), the independent check.** Its plan was written and hashed before any reader started and
before the check read the first round's notes, transcriptions or decode. Two fresh readers worked separately, each
with only the sheet and 51 line windows: A wrote 226 signs (13 "?", 1 "#"), B 231 (3 "?", 1 "#"); neither marked a
word space. Both outputs were hashed before any decoding (`records/verifier/HASHES.txt`). A script reconciled them
mechanically: **187 of 234 aligned positions agree (79.9%)**; the other 47 stay holes. About 12 of the 47 are only a
choice between two signs that Lasry gives the same letter (`77` and `pi`, both O): counting those, 200 of 234
(85.5%). Most of the rest come from one sign, the closed o joined to a 7: reader A wrote it as Lasry's P sign `np`,
reader B as two signs (`o` and `7`).

Against the first transcription (224 positions; the blind text has 234): 178 positions equal, 46 different, 10 only
in the blind text (`records/verifier/compare_with_solver.log`).

**Two further blind readings closed some of the holes (17 Nov 2026).** Each under a rule fixed before decoding; neither
changes a value.
- *Third reading* (`records/third_reading/`; plan `PLAN_round2.md`, sha256
  d6b5d932723c64d6c4e09f980d37cd54b2259dff3d9ac781ff05a823b23dd9e0, hashed before its readers started): two fresh blind
  readers re-transcribed all 51 windows with the same sheet; a hole closed only where both agreed with each other and
  with one of the two earlier blind readers (three of four). 17 of the 47 holes closed, one extra sign was dropped
  (three readers see none), 29 stayed open. 13 of the 17 are the choice between Lasry's two O signs. One closure goes
  against the sense: L2 "so entrase" (Lasry's S `7o` where *no* wants n); it stands as the rule gives it, and the word
  is unread.
- *Fourth reading* (`records/fourth_reading/`): two more fresh blind readers transcribed all windows with the sign sheet
  later cut from the 1496 letters; each of the 29 open positions was put to all six blind readers, and closed where four
  of six agree (`tests/recount1497_stretches.tsv`). 5 positions closed: three "o joined to a 7" places go to Lasry's S
  `7o`, as the first transcription's shape rule had it; L5 33 is `p++` (r), giving *hazer*; the dotted h (L5 25) was read as Lasry's H
  `I-o` by both new readers, who had a row for it, but by only two of six, so it stays open.
- The strict text is now 230 positions with 21 holes (`transcription_blind.txt`, rebuilt by `make_transcriptions.py`
  from these records). One position differs from the frozen record `records/fourth_reading/tests/strict_round5_names.txt`:
  L4 22, the l of *les*, where both earlier blind readings and the sheet map give Lasry's `i...` (his l) and that
  record has a hole only because its conversion of the readers' sheet id K50 failed (`transcription_differences.md`).

**The "o joined to a 7" sign is Lasry's S `7o`.** His own leaf shows it: f. 122r, line 2 ends with this sign followed
by `np`, and he decodes the pair "s p". His key image misleads here: its P tile `np` is drawn as a small o joined by a
bar to a long diagonal, which looks like this sign, and blind readers working from the key image alone take it for P
(one reader in each round did).

### The two transcriptions in this folder

- `transcription_blind.txt`: **the strict blind transcription**, round 2 as reconciled with the closures of the third
  and fourth blind readings, in reading order; every position still without agreement is `#`. 230 positions, 21 of
  them holes.
- `transcription_working.txt`: **the working transcription**, round 1 with the five corrections the image supports
  (below), and the dotted h written as its own sign `[N02]` with no value. 224 positions.
- `transcription_differences.md`: the edits, and every place where the two differ.

### Corrections on the image

Where the two blind readers of round 2 agreed with each other but not with the first transcription, the check looked
at the image (zooms at 5-6x):

| line, place | first transcription | round 2 readers | image | result |
|---|---|---|---|---|
| L1 "escandalos" | `7-` (S) | `Z` (A) | first transcription: a bar crosses the long tail of the 7; line 2's sign lies lower | escandalos, unchanged |
| L3 "guela" | `ee` (L) | `a_` (R) | round 2: a top stroke runs over the bowl, as in Lasry's R `a_` | **guera** (guerra) |
| L4 "modtrar" | `7` (D) | `7-` (S) | round 2: a bar crosses the 7's diagonal, clear of line 5 | **mostrar** |
| L4 "led dio" | `7` | `7-` | round 2: crossbar | **les dio** |
| L5 "led hizo" | `7` | `7-` | round 2: crossbar | **les (h)izo** |
| L6 after [dal] | `a_` (R) | `ee` (L) | round 2: an upright bowl with no top stroke, as Lasry's L `ee` | "ala uera": still unclear |
| L4, L5 | `p` (R) | `p++` (R) | not judged | both R: no effect |
| L8 start | `7-` | `7` and a sign cut off | first transcription: a crossbar at the foot of the 7, then `pi0`; the check's crop had cut the line | si, unchanged |

So three of the four places where the first round reported "a plain 7 standing for s" carry the crossbar of Lasry's S
`7-` (mostrar, les dio, les hizo), often low, near the next line. That reported difference from no. 95 was a
misreading. The fourth place (*daoruauan*) reads a plain 7 in both rounds and stays unread. In Lasry's own letter the
plain 7 is d 35 times and s once in his edited reading, and his S signs are never read d
(`records/verifier/t4_lasry_letter.log`).

**The eight adjudications of round 1 against the round 2 readers:**

| place | round 2 readers | round 1 choice | image |
|---|---|---|---|
| L5, sign 17 | agreed with each other | agrees with them | |
| L4, sign 14 | agreed with each other | another sign of the same letter (R) | |
| L1, sign 19 | agreed with each other | against them | supports round 1 |
| L3, sign 20 | agreed with each other | against them | supports round 2, and round 1's own blind reader |
| L6, sign 7 | agreed with each other | against them | supports round 2, and round 1's own blind reader |
| L1, sign 8 | split | matches neither | unclear: closed or open bowl |
| L2, sign 9 | split | matches one of them | not judged |
| L4, sign 25 | split | matches one of them | not judged |

Three of the eight are contradicted by the blind readers (L1, L3 and L6), two of them also by the image (L3 and L6);
at L1 the image favours round 1. At L3 and L6 round 1 overruled its own blind reader in favour of the reading made
knowing the key; three blind readers out of three are against it there.

## Tests, in order

All counts below are from the logs in `records/`.

1. **Calibration of the first measure (16 Nov, before its plan), on Lasry's own letter only.** The measure: share of
   letters lying in dictionary words of 3+ letters (or short words between two such words) after a Viterbi
   segmentation over a fixed word list (Claver 2025 forms plus forms of Pulgar's *Crónica*, 1780 print, of 4+ letters
   seen 5+ times). Three variants were rejected because their permuted-table controls scored too high. The chosen
   one gives Lasry's key on the first 225 signs of his own transcription 72.7% (control 95th percentile 19.3%), on 450
   signs 80.9%, on the whole letter 86.0%. The plan said then that a correct key on a text this short scores only a
   little above the 70% mark (`records/solver/calibration_no95*.log`).
2. **Test 1, the first plan** (`records/solver/TEST_PLAN_2857.md`, sha256
   6eb293fb15e5c488dfdfffec351fbf5e27406abb1c08beaac926e8027865e52d, written before any decoding of this letter). On
   the round 1 transcription: **73.85%**, mark 70%; control 1,000 tables with Lasry's letter values permuted among his
   44 signs: mean 9.2%, 95th percentile 17.7%, maximum 29.6%, none as high. **Pass by that plan**
   (`records/solver/test2857_output.txt`).
3. **The check's plan** (`records/verifier/PLAN.md`, sha256
   dd3d394fc1a250de45bebc64b2e9722f1b53f62a662f33edbe30a8d1c303dbc4, written before the round 2 readers started).
   Each test run once (`records/verifier/tests_output.txt`):
   - **T1, the first measure unchanged on the strict blind text: 46.55% against the 70% mark. A MISS.** 232 letters
     and holes, 47 holes. Control (1,000 permuted tables, seed 2857): mean 5.2%, 95th percentile 11.0%, maximum
     19.2%, none as high. The check's script gives exactly 73.85% on the round 1 text
     (`records/verifier/check_on_solver_text.log`), so the difference comes from the transcription, not the code.
     (By the first plan's own bands, 46.55% would fall in its 30-70% band, "same family, different key?"; the check's
     plan counted anything under 70% as a miss.)
   - **Why it misses.** The 70% mark was calibrated on a clean transcription with no holes. On Lasry's own letter,
     with random signs replaced by holes, the correct key scores a median of 58% (maximum 71%) with 10% holes, and a
     median of 37% (maximum 48%) with 20% holes (`records/verifier/t3_holes_secondary.log`). The blind text has 20%
     holes; 46.55% is at the top of what the correct key gives at that rate. So the first measure, as planned, does
     not survive doubtful places; its pass on the round 1 text depends on that text having almost no holes, and that
     text holds the errors above.
   - **Secondary runs, not in the plan:** with same-letter disagreements kept, 52.6%; adding round 1's `7o` rule to
     the round 2 readers before reconciling (22 holes), 64.4%; the round 1 text corrected only where the two round 2
     readers agree against it, 77.6%; the blind text in the right line order, 46.1%.
   - **T2, a letter-trigram test that needs no word division, on the strict blind text: PASS.** Model trained on
     Pulgar's *Crónica*. The decode scores -1.003 log10 per letter (186 letters in 32 runs); the 1,000 permuted tables
     average -1.619, best -1.352: the real key beats all of them. Against 1,000 passages of Zurita's *Historia del
     rey don Hernando* (1580) with the same run lengths (5th percentile -1.165, median -1.095), the decode sits at the
     99.4th percentile. The Zurita reference is lenient (its OCR is noisy); the margin over the permuted tables is the
     stronger evidence. T2 passes in every secondary run as well.
   - **T3, calibration: reproduced.** The first round's calibration script, unchanged, on Lasry's transcription and
     key gives 72.7% on the first 225 signs (`records/verifier/t3_calibration_rerun.log`). The other five 225-sign
     windows of his letter score 84-91%: the window chosen was the hardest.
   - **T4, the reported differences from no. 95** (descriptive): the barred u/v sign is probably a cursive form of
     Lasry's O, not proven; "plain 7 = s" is a misreading at three of four places; the dotted h has no secure value
     (below).

Both outcomes of this folder's own tests stand as run: the first measure passed on the first transcription and missed
on the blind one; the trigram test passed on the blind one.

## The key on unseen text: see `../juanmanuel1496/`

This letter is too short for a strong test of its own. The test of Lasry's key on text nobody had decoded was made on
Juan Manuel's letter of 18 December 1496, in the same cipher (`../juanmanuel1496/NOTES.md`, "Tests, in order"): with a
plan and sign mapping hashed before any reader started, letter trigrams -1.043 per letter against a best of -1.336
among 1,000 permuted tables and a mark of -1.122 from period Spanish: pass; word share 0.338 against a mark of 0.255
set by rule on Lasry's own letter at the same share of holes (permuted 99th percentile 0.104): pass. An independent
check with its own sheet and readers passed every mark on both 1496 letters. The additions proposed there for this
letter's open signs and groups (barred u/v sign = o; `dal`; `bnm`) missed or gave no result.

## The reading

Built on the working transcription; texts in `decode_working.txt`, `reading.md` (diplomatic and normalised text) and
`translation_en.md` (English, made by an AI agent, unchecked); per-word table `words.tsv`. The cipher has no word
spaces; the word division is ours. Marks: `[?]` a sign with no value or a lost letter; `|...|` letters as the key
gives them that make no sure word (in the normalised text *ala uera* is the hole `[... 2]`, two words); `[?word]` a word supplied or completed by sense; `[r]` a letter supplied by sense
at a damaged line end; `[code bnm, unread]` and `[code dal, unread]` code groups without a value. Every such word
counts as unread.

> Los que [?aquí] [?procuran] escándalos e [?estorvavan] que [code bnm, unread] no entrase en la tregua, diziendo que
> no tenían guerra ni se han de mostrar parte; pero no se les dio luga[r] a lo que querían, antes se les [?hizo]
> haze[r] lo que [code dal, unread] [... 2] cerca deste caso, porque fuera gran [?inconviniente] no se hazer así.

Those here who are stirring up trouble had tried to keep someone (the unread group) out of the truce, saying they had
no war and need not show themselves a party; they were not given room for it, and were made to do what [dal] ...
about this matter, because it would have been a great drawback not to.

**Read share** by the repository's rule (cipher words only; a word counts only when every sign has a value from the
key and no letter is supplied or changed by sense; each code group is one word; the word division is ours, as the
cipher has none):

- **45 of 56 cipher words (80%) on the working transcription.** Not read (11): *aqyi*; *pr?curan* and
  *ync?nuiniente* (the barred u/v sign has no value); *daoruauan*; the code groups *[bnm]* and *[dal]*; *luga#* and
  *haze#* (damaged line ends); *hizo* (the dotted h); *ala* and *uera*. *guera* is read and flagged as a period
  spelling of *guerra*.
- **38 of 56 (68%) on the strict blind transcription** (was 26 before the third and fourth blind readings). Not counted
  there although the strict decode gives the word: *procuran* (L1), because three of four blind readers drew its barred
  u/v sign as Lasry's O `77`, and that sign has no tested value; *so* for *no* (L2). Counted: *les* (L4), whose l is
  Lasry's `i...` in both blind readings; an independent recount gave 37 because its conversion of the readers' sheet ids
  turned that sign into a hole (`transcription_differences.md`).
- Seven read words of the working text (*los*, *escandalos*, *entrase*, *se* three times, *caso*) rest on `7o` = S,
  which Lasry's leaf supports and his key image obscures; on the strict text the fourth reading's six readers closed
  three such places as `7o`.

### Notes on single words

- *guera* (L3) is read and normalised *guerra*: a period spelling with one r. The first transcription read *guela*;
  the image shows Lasry's R sign `a_` there.
- *mostrar*, *les* (L4) and *les* (L5): the first transcription had a plain 7 (Lasry's D) at the s; the image shows
  the crossbar of his S sign `7-` at all three places.
- *[?aquí]*: the key gives *aqyi* (the third sign read as his Y sign `of`; the image does not settle whether its bowl
  is closed or open).
- *[?procuran]*, *[?inconviniente]*: one sign in each, a u/v shape with a bar (`[N03]`), is not in Lasry's table. Three
  of four blind readers took both for his O `77`, and o fits; but the value o missed its planned test on the letter of
  18 December 1496 (it makes words at 22 of 33 places and breaks 11), and the barred signs there are of three shapes, so
  both words count as unread.
- *[?estorvavan]*: the key gives *daoruauan* (after *e*); the sense wants *estorvavan*, which needs two letters
  changed, so the word stays unread.
- *[?hizo]*: the h is Lasry's H sign with two dots before the o (`[N02]`), a sign his table does not have; his O signs
  show that dotted variants can be separate signs, so the sign has no secure value. The two readers of the fourth
  reading, who had a sheet row for Lasry's H, read it as H; four earlier readers, who had none, did not: two of six.
- *luga[r]*, *haze[r]*: the ends of L4 and L5 are damaged; the last letter of each is supplied by sense.
- *|ala| |uera|* (L6): every sign has a value. The first transcription read the second sign after [dal] as R (*ara*,
  "hará"); three blind readers and the image give Lasry's L sign `ee`. Neither *ala uera* nor *ara uera* gives a
  sure sense here, so both words count as unread.
- *[code bnm, unread]*: a group in Latin letters that is not in Lasry's list; his nearest group is `bnh` = *rey*. It
  does not occur in the 1496 letters. *[code dal, unread]*: one of his five unidentified names; it occurs 14 times in
  the 1496 letters, where it stands where the addressee fits ("sea [dal] cierta", feminine), a suggestion only; its
  proposed value "el Rey" gave no result there (`../juanmanuel1496/code_groups_contexts.tsv`).

## Context

- The 2025 book on Claver (C. Villanueva Morte and Á. Fernández de Córdova Miralles, *El embajador Claver. Diplomacia
  y conflicto en las «Guerras de Italia» (1495-1504)*, CSIC 2025), p. 67: after the Spanish-French truce of 25
  February 1497, the republic of Genoa too voiced its unease (note 166 cites this letter); the Italian allies joined
  the truce on 11 May 1497. It says nothing of anyone being kept out.
- Zurita, *Historia del rey don Hernando* (1580), end of book II: in the French attack on Savona in spring 1497 Genoa
  was defended by "Juan Adorno … y Juan Luys de Fiesco"; the Venetians would act only for Milan's and Final's lost
  places, "porque no se querían mostrar parte contra el Rey de Francia". Book III, ch. III: the truce was published in
  Italy on 25 April 1497; the French fleet then seized a Genoese ship, and "la ciudad de Genoua se començo a alterar".
- The decode's "no tenían guerra ni se han de mostrar parte" uses the same language of who was or was not a party to
  the war and the truce; *guerra* fits far better than the first round's *gue la*. Nothing seen names who was being
  kept out: [bnm] stays open.
- **Side lead, not proven:** Lasry suggested that no. 95 (8 January 1497, city not named) was written from Genoa, with
  "micer Juan Luys" perhaps Gian Luigi Fieschi (`../esp318no95/lasry2021/CONTRIBUTION.md`). This letter, from the
  Spanish envoy at Genoa in the same cipher three months later, supports that, and Zurita puts "Juan Luys de Fiesco"
  in Genoa in early 1497. Juan Manuel's own letters from Genoa of November and December 1496 are in the same cipher
  (../juanmanuel1496). No. 95 may be Juan Manuel's own letter.

## Prior work

- No decipherment of this passage is known in print or online. The 2025 Claver book cites the letter once (note 166,
  p. 67) for its clear part and does not print it.
- Lasry has no paper on Espagnol 318; his work on no. 95 is the 2022 alphabet, the partial overlay on Tomokiyo's
  cryptiana page, and pull requests 75 and 85 here. None of it mentions Zaragoza or Juan Manuel.
- Galende Díaz, "La escritura cifrada durante el reinado de los Reyes Católicos y Carlos V" (*Cuadernos de Estudios
  Medievales* 18-19, 1994) prints Juan Manuel's two private ciphers (BRAH 9/15), not this system, and names no Genoa
  letter of 1496-97. Zurita (1580) and Sanuto's *Diarii* vol. I were searched for this letter's content: nothing on who
  was kept out of the truce. Internet Archive full-text searches found nothing.
- The catalogue entry's vetting found no DECODE record and no edition.
- **Not seen:** Suárez Fernández, *Política internacional de Isabel la Católica*, vols. IV-V (not online); Galende Díaz,
  *Criptografía* (1995). So: no decipherment found, not "none exists".

## Remaining gaps

- code group [bnm] (L2) - blocker: open-codes; a group in Latin letters that is not in Lasry's list (his nearest is bnh = rey); one occurrence, absent from the 1496 letters and no. 95, and nothing seen names who was being kept out of the truce
- code group dal (L6) - blocker: open-codes; one of Lasry's five unidentified names in no. 95; the value "el Rey" gave no result on the unseen 1496 letter, whose contexts suggest the addressee
- barred u/v sign [N03] in pr?curan and ync?nuiniente - blocker: no-key-material; not in Lasry's table; the value o missed its planned test on the unseen 1496 letter, and no further unseen text in this cipher is known
- dotted h sign [N02] in ?izo - blocker: no-key-material; Lasry's table has no dotted H, and his O signs show dotted variants can be separate signs; two of six blind readers read it as his H
- aqyi (L1) - blocker: illegible; the third sign is a closed or an open bowl (Y or U) and the archive's image does not settle it
- daoruauan (L1-L2) - blocker: needs-physical-access; both rounds read a plain 7 and an A sign where estorvavan wants s and t; only the original or a sharper image could show missing strokes
- ala uera (L6) - blocker: needs-physical-access; every sign has a value but no sure sense; the reading turns on fine strokes of two signs (L or R; a doubtful u) that the archive's image does not settle
- damaged end of L4 (luga#) - blocker: illegible; the last sign is lost at the edge
- damaged end of L5 (haze#) - blocker: illegible; the last sign is lost at the edge

## Escalation

- [x] siblings: Lasry's no. 95, the key's own letter, compared sign by sign; Juan Manuel's letters of 10 Nov and 18 Dec 1496 (catalogue 1270, BNE MSS/20212/61/1-2) are in the same cipher, transcribed blind and deciphered in part (../juanmanuel1496), where the key passed its tests on unseen text and [bnm] does not occur; letters 3-7 of that volume are clear or in other systems; catalogue 1049 (RAH Salazar N-23 f. 36, Rome 23 June 1497) is not digitised and was not seen
- [x] clear-pages: the clear head, dating and verso hold no decipherment; the clear head was not transcribed
- [x] known-keys: Lasry's no. 95 key applied unchanged; no other key tried, since this one gives Spanish that fits the date
- [x] print: 2025 Claver book (note 166 cites only the clear part), Galende Díaz 1994, Zurita 1580 and Sanuto vol. I searched for context, Internet Archive full text, Lasry's no. 95 files and pull requests 75 and 85; Suárez Fernández IV-V and Galende Díaz 1995 not seen
- [n/a] key-rebuild: by design the key is applied unchanged and not refitted; the two signs not in the table are recorded as gaps, not given values; the proposed additions were tested on the unseen 1496 letter and missed or gave no result
- [x] retry: every doubtful place of the first round was checked on the image where both blind readers agreed against it (five corrections); the holes of the strict text were put to four more fresh blind readers in two readings (22 positions closed); the remaining unread words were regraded on both texts

## What was not checked

- No person has checked any part of this: transcriptions, tests, corrections, reading or translation.
- The clear text of the letter (heading, seven lines, dating) and the verso were not transcribed; the day "14" comes
  from the archive's record.
- Two of the eight round 1 adjudications (L2 sign 9, L4 sign 25) and the R signs at L4 and L5 (`p` or `p++`) were not
  judged on the image; L1 sign 8 is unclear.
- Catalogue 1049 (RAH, Rome 23 June 1497) was not seen (not digitised).
- Suárez Fernández, *Política internacional*, vols. IV-V, and Galende Díaz, *Criptografía* (1995), were not seen.

## Files

- `decode.py`: reads Lasry's `key.txt` from `../esp318no95/` (hash checked), decodes both transcriptions; writes
  `decode_blind.txt` and `decode_working.txt`. Standard library, deterministic.
- `make_transcriptions.py`: rebuilds `transcription_blind.txt`, `transcription_working.txt` and
  `transcription_differences.md` from the records.
- `reading.md`, `translation_en.md`, `words.tsv`: the reading, the English, the 56 words.
- `records/solver/`: round 1 and test 1 as they were frozen: the plan and its hash, `test2857.py`, `wl2857.py`,
  `reconcile2857.py`, `calib_no95_d.py`, the readers' transcriptions in sheet ids, the reconciled text, the
  adjudications, the logs and the output.
- `records/verifier/`: round 2 and the check: the plan and its hash, `HASHES.txt`, `tests.py` (T1 and T2) with its
  unchanged copy of `wl2857.py`, the readers' transcriptions, the reconciliation, the comparison, the word table, the
  T3 and T4 scripts and logs, the secondary runs.
- `records/third_reading/`: the third blind reading as frozen: its plan and hash, `HASHES_helpers.txt`, the two readers'
  transcriptions in sheet ids, the reconciliation script, its output, the holes table and the strict text in sheet ids.
- `records/fourth_reading/`: the fourth: its plan and hash (the plan covers the 1496 letters too and is not a test),
  `HASHES_helpers.txt`, the sheet mapping it used, the reader instructions, the two readers' transcriptions, the
  six-reader recount script and its outputs (the stretches table, its strict text in Lasry's names, its word table).
- The records are kept unchanged, so their hashes can be checked against the plans. They name files by the paths of
  the working folders they were made in, and two plans name the model that ran the readers. The test scripts need
  inputs that are not in this folder: the page image (archive's terms), the value-free sign sheet (cut from Lasry's
  key image), the Claver 2025 word list (built from the CSIC book), and the Internet Archive OCR of Pulgar's
  *Crónica* (1780, item bub_gb_RB9nAr9N5AkC) and Zurita (1580, item bub_gb_XgWt5lHz3_MC); their sha256 are in the
  plans.
- No image of the manuscript, crop or sign cut-out is included, and nothing from Lasry's key image is copied: signs are
  named in words and by his sign names.

## Credits

- George Lasry: the key (his CTTS key and key image for BnF Espagnol 318 no. 95, his target `esp318no95`).
- Andrew Beling, with AI agents: the match of this letter to Lasry's key, both transcriptions, the tests and the
  reading.
