# Fra Giovanni di Lucca to the Emperor, 30 May 1644 (DECODE R2159, ÖStA HHStA Staatskanzlei Interiora, Chiffrenschlüssel Kt. 20 Fasc. 27 ff. 18-19) — NOTES

**Verdict: read.** The cipher paragraph is a 24-figure alphabet with no polyphonic figure (19 = s; three places where t is wanted are the writer's slips, per G. Lasry 21 Sept 2026: apparent polyphony is encipherment or transcription error), groups
delimited by dots, plaintext Italian. All 231 groups read; one spelling is odd (`ogn modo`). *Corrected 22 Sept 2026
against the DECODE images (§7): the "17 = n" of the first session was ten transcription errors for 14, so 17 is only
i, `Bogodania` and `non l'habi` are confirmed, and the clear frame names the speaker as Koniecpolski.* Tomokiyo's unsolved page lists the item under "Variable-length
Figure Code in Austrian Archives (1644, 1627)" with the note that it "can be deciphered to read *Al principe di
trenti…*" and that "someone versed in Italian would be able to complete the decryption"; nobody had. DECODE still
carries the record as *Non-decrypted*, cipher type *Unknown*, with a placeholder date range of 1686–1877.

Session 2026-09-16. Ciphertext is Tomokiyo's transcription (variable2.htm); the DECODE images need a login and
were not seen, so the transcription was taken on trust. Session 2026-09-22: images seen, transcription corrected
(§7); [ct.txt](ct.txt) is now the corrected text, the first-session text is in git history (commit before 22 Sept).
§§1–4 below describe the first session's work on the uncorrected text and are kept as the record of it.

## 1. The ciphertext

231 groups, 24 distinct figures (1–15, 17–19, 21–23, 25, 26, 32), IC 0.050, one doubled pair in the whole text
(`17 17`, twice, in the same word). Tomokiyo: "The number groups may consist of one or two digits, but there is no
difficulty in identifying individual groups because the groups are delimited by dots." His article gives the
provenance: "from Fra Giovannni di Lucca to the Emperor (Ferdinand III), 30 May 1644. In Italian." [ct.txt](ct.txt).

The single doubled pair in 231 letters of Italian (where `ll tt ss nn rr cc` run at 3–4 % of positions) already says
this is not a plain letter-for-letter substitution; homophones for the doubled consonants, or polyphony, would both
produce it. It turned out to be the second.

## 2. Solving

1. **Unconstrained homophonic annealing fails.** A 5-gram Italian model (Villari's *Machiavelli e i suoi tempi*,
   *I promessi sposi*, *La Mandragola*; 4.1 M letters, v→u, Roman-numeral page references stripped) with 16 restarts
   converged on the same non-Italian optimum (−2.52 nats per 5-gram, `estreesitenetrentiuenieseist…`). The solver
   reads a matched 231-letter Italian control in 1 of 3 seeds, so the failure is not conclusive, but it is real: the
   landscape is flat at this length.
2. **Tomokiyo's crib, taken literally, is inconsistent with a substitution.** *Al principe di* = `3 11 | 26 21 17 17
   6 15 26 1 | 8 17` needs 17 = i (from *di*, and *il* = `17 11` later) and 17 = n in the same word. That is the
   whole difficulty of the item, and the reason "someone versed in Italian" had not simply finished it.
3. **Crib-fixed annealing.** Fixing only the eight letters that the crib gives without contradiction
   (3 a, 11 l, 8 d, 17 i, 26 p, 21 r, 1 e, 19 t) and annealing the other 16 figures, all six seeds converge on one
   reading (−2.50 per 5-gram): `alpriicipeditrantiuanialoimpediroconoinmodocheilturcononlidiaaiutoefaroriuoltase…`
   — *lo impedirò … che il Turco non li dia aiuto e farò rivolta(re)…*. The reading is Italian at the word level
   from the first group to the last ([solve.py](solve.py), [crib_anneal](crib_anneal.py)).
4. **Polyphony read off the contexts.** With the letters otherwise fixed, 17 is *n* in *principe* (twice), *manderò*,
   *con una*, *non*, *vinto*, and *i* in *di*, *il*, *impedirò*, *li*, *lui*, *dumilia*, *finché*; 19 is *t* in
   *Transilvania*, *rivoltare*, *tua/sua*, *humiliato*, *vinto* and *s* in *Transilvania*, *se sarà bisogno*,
   *Cosachi*. No third value is needed for either. A Viterbi pass over the two alternatives with the same 5-gram
   ([decode.py](decode.py)) makes the per-occurrence choices mechanically and agrees with the hand reading except at
   *Bogodan(i/n)a* and *(io/no) il habi*, both discussed below.
5. **Control.** The crib-fixed procedure run on five shufflings of the same ciphertext (same figures, same counts,
   same eight letters fixed) reaches −3.40 to −3.68 per 5-gram; the letter reaches −2.50. The gap is about 200 nats
   over 227 5-grams. Note that the unconstrained false optimum in step 1 scored the same as the true reading, so the
   model alone does not pick the solution; the eight crib letters do, and the shuffled controls show that eight fixed
   letters on this text do not manufacture Italian by themselves ([control.py](control.py)).

## 3. The key

| figure | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 17 | 18 | 19 | 21 | 22 | 23 | 25 | 26 | 32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| letter | e | g | a | b | f | c | e | d | a | h | l | m | o | n | i | **i / n** | o | **s** | r | t | u | u | p | r |
| count | 7 | 3 | 16 | 3 | 3 | 13 | 10 | 10 | 12 | 6 | 13 | 6 | 13 | 10 | 18 | 24 | 14 | 9 | 14 | 8 | 4 | 7 | 7 | 1 |

Vowels a, e, o, u have two figures each; i has 15 and shares 17 with n; s exists only through 19. Figures 16, 20, 24
and 27–31 do not occur (231 letters; q, z, v-as-consonant are absent from the text anyway). The arrangement is not
alphabetical and shows no regularity that I can see.

*Alternative to polyphony.* Everything attributed to "17 = n" could also be a transcription of **14** misread as 17
(a 4 and a 7 are close in seventeenth-century hands), and "19 = s" could be a misread figure for an *s* number that is
otherwise unused (16, 20, 24, 27–31). Both would turn this into an ordinary homophonic alphabet. Only the DECODE
images can settle it; the reading is the same either way. **Settled for 17 (22 Sept 2026, §7): every "17 = n" is a
14 on the page. 17 = i only (14 occurrences), 14 = n (20). 19 = s; its three t-contexts (Transiuania twice, rivoltare, humiliato) are encipherment slips.**

## 4. Reading

Figure groups as transcribed, letters beneath, the two polyphonic figures marked:

```
3 11 | 26 21 17 17 6 15 26 1 | 8 17 | 19 21 9 14 19 15 25 3 14 15 3 | 11 13 | 15 12 26 1 8 17 21 18
a l  | p  r  i  N  c c i p e | d i  | T r  a n  S  i  u  a n  i  a | l o  | i  m  p  e d i  r  o
6 13 14 | 18 2 14 12 13 8 18 | 6 10 1 | 15 11 | 22 25 21 6 18 | 14 13 14 | 11 17 | 8 15 9 | 3 15 23 22 13 | 1
c o  n  | o  g n  m  o  d o  | c h  e | i  l  | t  u  r  c o  | n  o  n  | l i  | d i  a | a i  u  t  o  | e
5 9 21 18 | 21 15 25 13 11 19 3 32 7 | 6 13 14 22 21 9 | 8 17 | 11 25 15 | 19 7 | 19 3 21 9 4 15 19 13 2 14 18
f a r  o  | r  i  u  o  l  T a r  e | c o  n  t  r  a | d i  | l  u  i  | S e  | S a r  a b i  S o  g n  o
17 11 | 26 21 17 17 6 15 26 1 | 8 15 | 4 18 2 13 8 3 14 17 9 | 7 22 | 11 17 | 8 3 21 13 | 8 23 12 17 11 15 3
i  l  | p  r  i  N  c i  p  e | d i  | b o  g o  d a n  i  a | e t  | l i  | d a r  o  | d u  m  i  l  i  a
6 18 19 9 6 10 15 | 7 22 | 12 3 17 8 1 21 13 | 9 | 25 18 17 | 6 13 17 | 23 17 3 | 19 25 9 | 11 7 22 1 21 3 | 9 11
c o  S  a c h  i  | e t  | m  a N  d e r  o  | a | u  o  i  | c o  N  | u  N  a | S  u  a | l  e t  e r  a | a l
15 12 26 7 21 9 22 13 21 7 | 6 10 7 | 17 18 | 17 | 5 3 6 15 9 | 26 9 6 7 | 5 17 14 6 10 7 | 17 18 | 17 11
i  m  p  e r  a t  o  r  e | c h  e | N  o  | N  | f a c i  a | p  a c e | f i  n  c h  e | i/N o | i  l
10 9 4 17 | 10 25 12 17 11 15 9 19 13 | 18 | 23 15 17 19 18
h  a b i  | h  u  m  i  l  i  a T o  | o  | u  i  N  T o
```

Normalised:

> **Al principe di Transil[u]ania lo impedirò con ogn[i] modo che il Turco non li dia aiuto, e farò rivoltare contra
> di lui, se sarà bisogno, il principe di Bog[o]dania, et li darò dumilia Cosachi, et manderò a voi con una sua
> lettera all'Imperatore che non faccia pace fin che non l'habbi humiliato o vinto.**

> *As to the Prince of Transylvania: I shall by every means prevent the Turk from giving him help, and if need be I
> shall make the Prince of Moldavia rise against him and give him two thousand Cossacks, and I shall send [him] to you
> with a letter of his to the Emperor, that he make no peace until I have humbled or defeated him.*

Notes on the text:
- *Transiuania* (`19 21 9 14 19 15 25 3 14 15 3`) has no *l*; either the writer's spelling or a dropped group.
- *ogn modo* (`18 2 14 12 13 8 18`) lacks the *i* of *ogni*; same two possibilities.
- *Bogodania* (`4 18 2 13 8 3 14 17 9`): *Bogdania* is the usual Italian and Turkish name of Moldavia (Boğdan).
  The extra `13` (= o) is either the writer's or the transcriber's. Viterbi prefers *Bogodanna* on 5-gram statistics;
  the place-name fixes `17` = i here.
- `19 25 9` before *lettera* is *sua* (Viterbi) or *tua*; *sua* is the grammatical reading (a letter of his, the
  Prince of Moldavia's, or of the speaker's).
- `17 18 17 11 10 9 4 17` is *io il habi* or *no il habi* (*non l'habbi*); Viterbi takes *no*. Either way the sense
  is "until [I] have humbled or defeated him". *Settled 22 Sept 2026 (§7): the page has `14 18 14 11 10 3 4 17`,
  *non l'habi*.*
- `4` = b occurs only in *bisogno*, *Bogodania*, *habi*; `2` = g only in *ogn*, *bisogno*, *Bogodania*; `32` = r once,
  in *rivoltare*. These three values rest on one to three occurrences each, all in words that no other letter fits.

## 5. Context

The date is 30 May 1644 (Tomokiyo, from the cleartext). In February 1644 György Rákóczi I, Prince of Transylvania, had
invaded Habsburg Hungary in alliance with Sweden and France and with the Porte's leave; through the spring Ferdinand
III's diplomacy worked to have Ottoman support withdrawn and to find allies on Rákóczi's flank. The paragraph is a
first-person offer, relayed by the friar, from someone who can influence the Porte, can set the Prince of Moldavia
(Vasile Lupu) against Rákóczi, and can dispose of two thousand Cossacks. *Who is speaking is not in the cipher.* The
combination points to Poland — the King, Władysław IV (Ferdinand III's brother-in-law), or the Grand Hetman
Stanisław Koniecpolski, who kept his own relations with Moldavia and the Tatars and had just beaten the Tatars at
Ochmatów (January 1644) — but that is an inference, not a reading.\*

Fra Giovanni di Lucca (Giovanni Giuliani da Lucca), Dominican, is known from his *Relatione* and *Itinerario* of the
1630s as a missionary to the Tatars, Circassians, Abkhazians, Mingrelians and Georgians, and later from his work in
Moldavia (Cristian Luca, "Note sull'attività missionaria del domenicano Giovanni Giuliani da Lucca", 2004, not
consulted here). A Dominican who moved between Moldavia, the Cossack lands and Vienna is exactly the sort of courier
such an offer would use.\* Whether the cleartext of ff. 18–19 names the principal, the DECODE record would show;
Tomokiyo's article quotes only the cipher.

## 6. What remains

- ~~The images (DECODE, login) to check the 4/7 question~~ done 22 Sept 2026 (§7). Still open: the *s* question
  (does 19 = s hide a different figure?), *Transiuania* without *l*, *ogn* without *i*: the images show `19` in both
  places of *Transiuania* and no extra group, so the spellings look like the writer's; a closer look at the two
  shapes of 19 is the remaining check.
- A full transcription of the clear frame (ff. 18–19), read only in outline in §7.
- The other two items in the same article, R1408 (Warsaw, 24 December 1627, Italian, two-digit groups with letter
  pairs) and R2179 (undelimited digits), are different ciphers and were not attempted.

## 7. Checked against the manuscript (22 Sept 2026)

DECODE R2159 images P1 and P2 (ÖStA HHStA, Staatskanzlei Interiora, Chiffrenschlüssel Kt. 20 Fasc. 27 ff. 18–19;
fetched with the DECODE cookie, kept outside the repository; the record's notice restricts publishing). The cipher is
12 lines on f. 18r between clear Italian. The writer's 4 is a crossed stroke that looks like a barred 7; his 7 is
plain. Tomokiyo's transcription reads the crossed 4 correctly as 14 in most places, but as 17 in ten: *principe*
(twice, `26 21 17 14 6 15 26 1`), *manderò* (`12 3 14 8`), *con una* (`6 13 14 23 14 3`), *non faccia*
(`14 18 14`), *non l'habi* (`14 18 14 11 10 3 4 17`) and *vinto* (`23 15 14 22 18`). Every plain 17 on the page is
*i*. With the ten groups corrected ([ct.txt](ct.txt)), 17 is a single letter and the cipher has one polyphonic figure
(19); the Viterbi choices change in two places, both to what §4 argued for: *Bogodania* (not *Bogodanna*) and *non
l'habi* (not *no il habi*). Tomokiyo's crib *Al principe di* was right; its apparent inconsistency (§2 item 2) came from
the transcription.

The clear frame, read in outline (not transcribed letter by letter): the friar, sent from Vilnius by the King, was
passed on to *il suo Generalissimo il Sig.re Stanislao Conespolschi* (Grand Hetman Stanisław Koniecpolski), told him it
was the moment to help the Emperor, and Koniecpolski "answered angelically" that he would, from affection for the
House of Austria and zeal for religion and reason of state — then the cipher. After it: this has not yet taken effect
because Rákóczi has sent a great sum of money to Constantinople to have the Prince [of Moldavia] made *mazul* (deposed).
The letter is dated *dalla Città di Brodi, Residentia dell'Ill.mo … Generalissimo Conespolschi, li 30 di Maggio 1644*.
So the speaker of the cipher paragraph is **Koniecpolski**, the §5 inference confirmed, and the place is Brody.

## Files

- [ct.txt](ct.txt) — Tomokiyo's transcription, 231 groups, with ten 17→14 corrections from the DECODE images (§7).
- [lm.py](lm.py) — Italian 5-gram model builder (corpus not committed; Gutenberg 45334, 56498, 61704–61706).
- [solve.py](solve.py) — homophonic annealer (unconstrained runs).
- [crib_anneal.py](crib_anneal.py) — the eight-letter crib-fixed annealing that produced the reading.
- [decode.py](decode.py) — Viterbi over the polyphonic alternatives; writes `plaintext_raw.txt`.
- [control.py](control.py) — the shuffled-ciphertext control.

Checked: transcription counts, crib consistency, convergence over seeds, shuffled controls, word-level Italian.
Checked 22 Sept 2026: the cipher against the manuscript images (§7). Read in outline only: the cleartext frame. User must verify: the
historical attribution in §5 before it is repeated anywhere.
