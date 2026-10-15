# System A′ of the Bavarian key volume (BayHStA Kurbayern Äußeres Archiv 4591): reports of the dukes' agents in Hungary and a letter of King John, 1534–1535

Status: in progress — System A′ read in part (89.8% of words); the remaining unread words are workable (open-codes), see Remaining gaps.

**Split on 15 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026).** This folder held catalogue entry 161
("Unknown sender to unknown recipient, 14 ciphertexts": DECODE R9291, R9319, R9322, R9323, R9325, R9367, R9408, R9409,
R9410, R9413, R9416, R9417, R9424, R9427), which are letters in at least six systems bound in the ducal key volume. It now
holds the one system most of them share, **System A′**: R9408, R9409, R9410 (two letters), R9413 and R9427. The others
are different ciphers, each with its own entry and page:

- R9322, R9323, R9417 (Łaski's System B) → [`targets/kaa4591b/`](../kaa4591b/NOTES.md), with R9403 of catalogue 162, in the same key;
- R9325 (Fulda 1576, key R9324) → [`targets/fulda1576/`](../fulda1576/NOTES.md);
- R9367 (22 March 1535, key register R9423) → [`targets/r9367/`](../r9367/NOTES.md);
- R9416 (f.262 read at the time; f.263 broken ciphertext-only) → [`targets/r9416/`](../r9416/NOTES.md);
- R9424 (1583, not solved) → [`targets/r9424/`](../r9424/NOTES.md);
- R9319 (1583 dot grille, blocked) → [`targets/r9319/`](../r9319/NOTES.md);
- R9291 (f.36) is not a ciphertext but a strip of cipher signs (a key fragment): no entry.

The sibling letters in the same system are R9407 (Jörg Weinmeister, spring 1533, [`targets/augurelio1535/`](../augurelio1535/NOTES.md),
whose improved key was carried back here) and R9368 (glossed). They stay in their own entries (see Assumptions).
Files moved out: `sysB/` → kaa4591b, `r9325/` → fulda1576, `r9367/` → r9367, `r9416/` → r9416, `r9424/` → r9424.
`keys9423/` (the R9423 key register) and `anneal.py` stay here as volume material used by several entries.

Images: DECODE, login (cookie in `targets/bordeaux/decode/cookie.txt`); not public domain, kept in `img/` (git-ignored).

## What the volume is

KAA 4591 is the ducal chancery's collection of cipher keys, 1530s–1620 (DECODE lists 102 key records R9277–R9423
from it), with ciphertexts bound in among the keys.

| Record | Folio | What it is | Key | State |
|---|---|---|---|---|
| R9408 | 236–239 | Jörg Weinmeister (signed in cipher) to the dukes, Ofen 8 Feb 1534, with Latin clear passages: his mission and a ratschlag, the Turk's power and money, mining (Schmaltz, Reinhart), Katzianer before Kaschau, the priest-bishop Emericus, bad coin with the dukes' stamp; P1 a separate news page (Emperor Sigmund, Constantinople, Syria) | R9407 key carried over, re-learned per letter (2 Oct 2026) | read in part, **88.9%** of words (`r9408/reading.txt`) |
| R9409 | 240–243 | German intelligence report of early 1534 with clear phrases: Ferdinand and the confederation, the Turkish embassy, Pressburg, Katzianer and Majláth in Transylvania, Késmárk, Poland and Muscovy; numbered articles on mining (Antoni Slesinger, Schmaltz, Freiberger, gold-exchangers); postscript "Auf den Reichstag" | R9407 key carried over, re-learned per letter | read in part, **80.9%** of words (`r9409/reading.txt`) |
| R9410 | 244–247 | f.244r: German, "datum … ersten [a]brilis Anno 35", to the dukes: a treaty, the King of France, "bruederlich halten" against the Turks. ff.246–247 (P3, P4 = P5, P6): a second letter, in **Latin**, royal "we", "Datum Bude ultima Iunii Anno (15)34": thanks for the dukes' letters and for the Landgrave's and the Duke of Württemberg's news; "nos cum adversario nostro pacem non habere sed … inducias", which the other side breaks; an envoy back at Constantinople; the Turks; offers amicitia and fraternitas — evidently King John (Zápolya) to the Dukes of Bavaria | R9407 key carried over, re-learned per letter | f.244r read in part, **83.9%** (`r9410/reading.txt`); ff.246–247 transcribed 2 Oct 2026 and read in part, **82.9%** (`r9410/reading_p3p6.txt`) |
| R9413 | 252–256 | letters of a Bavarian agent to the dukes, July and 7 June 1534 and a third of "8 Julij", addressed to secretary Waisenfelder: Cornelius, the French orator Antonius Rincon at Constantinople, Katzianer, the bishop of Wardein before Hunyad, the Württemberg war, an ore sample from near Ofen, the Turk's fleet, the Pressburg diet | R9407 key carried over, re-learned per letter | read in part, **86.0%** (`r9413/reading.txt`) |
| R9427 | 287 | German newsletter to a duke, 15/21/24 April [15]34, postscript 25 April: the Württemberg affair (the Bund, the dukes of Württemberg, the Landgrave), Ferdinand, a provost-priest who married and was imprisoned; gloss over lines 1–10 | gloss key, then the R9407 key carried over and re-learned | read in part, **77.3%** (`r9427/reading.txt`) |

## System A′ (R9408, R9409, R9410, R9413, R9427), 21 Sept 2026 — key from the R9427 gloss (superseded by the 2 Oct section below)

A full-zoom alignment of R9427's gloss (lines 1–5, 7–10; `r9427/aligned_full.tsv`, `r9427/key_full.tsv`) gives a
homophonic letter substitution with a code sign X = "F.G." (w3vX = "ewr F.G."). In R9410 codes: 4 e, w e, q(□) n,
8 n ("48" = -en), y(ÿ) t, x s, 5 a, m i, p i, #(‡) g, Q g, 9 o, 3 u, v(↓) r, n(π) w, 7 m, t z, b l, d l, D f, 6 d,
g r, L s, J k, j h, c c, E d and ch (two look-alikes or a homophone), Ro = "und", a+ a word sign (open).
With the key pinned, R9410 f.244 reads as running German with local errors (`sysA/r9410_decrypt_working.txt`):
"…seiner zeit darumb … ausserhalb eur F.G. … des handlung … handelt nit so vil … bedanckt sich … zum hochsten …
gegen eur F.G. … in dergleichen fal … dienen … freundt … turcken … bruederlich halten … zu besorgen … eur F.G.
angezaigt … gehorsamen underthenigen … meinen genedigsten herren … datum", Anno 35. R9409 (11,311 signs) reads in
part the same way (`r9409/decrypt_working.txt`): "genedig… februari… angezaigt… der turckische kaiser… Ferdinand…
bruederlich halten…". State: broken; clean readings need the E/a+ signs settled and word division restored.

## System A′, 2 Oct 2026: the improved R9407 key carried back, the look-alike splits applied, hand readings

Work in `sysA2/` (usage in each script's docstring): `prep.py` brings the five v2/v3 transcriptions to one code set
(R9409's own codes mapped to the R9410 codes by shape; merges jo = ʒo (h), a+ = β, mg = ɱ, Ro = "und", R9408 c# = ck,
w3v/wUv before the F.G. sign = "eur", the formula glossed on R9427) and writes `REC.tok`; `run.py` learns a key per
letter (Baum-Welch on a letter-trigram HMM, de-1500s, seeded with the improved R9407 key `augurelio1535/pass2/key.txt`
by sign shape, Dirichlet prior towards the seed) and decodes with a word-aware beam (de-1500s 5-gram + DTA word
unigrams + `vocab.txt`), then re-estimates the key from the beam's own output for 4 rounds; `lexmeasure.py` is the
machine measure; `measure2.py` (the R9407 measure, adapted) and `count.py` measure a hand reading; `show.py` and
`supkey.py` serve the reading rounds.

**Look-alike split.** The R9410 split (d = l vs the big looped K word sign; # = g vs upright U = u/v) had in fact already
been carried to R9409 (all pages), R9413 (all pages) and R9427 (`*/split.md`, `transcription_v2.txt`), but not
recorded here; R9408 had P6 l.24-31 and P7 unchecked. Those lines and the six flagged tall looped signs on P5-P6 were
checked at the image on 2 Oct 2026 (`r9408/split_p6p7.md`): all six are K, a seventh K at P6 l.10, two # -> U, three
ringless δ coded b -> d, one dropped 8; 17 edits -> `r9408/transcription_v3.txt`. Also from the split notes: the X
after c on R9408 is the slanted c#-type sign, so R9408 `c#` = ck (44x), and the F.G.-like signs on R9408 P1 read k.
New look-alike merges found by the per-letter keys (not split; they need the images): R9408 `y` covers ÿ (t) and an
undotted γ (r, 19%); R9408 and R9427 `4` take e and i (probably 4 and the open ч, as on R9407); R9409 `ç+` covers f/v,
sch and da (several signs).

**Measures.** `lexmeasure.py` segments a decrypt into DTA/chancery words (calibrated on R9407: its hand reading scores
0.912, the pass-2 machine decrypt 0.786, the same decrypt under a random letter key 0.194). Hand readings are counted
with `count.py` (words read / all words, {?} unread; on the R9407 reading it gives 95.6%) and checked with
`measure2.py` (strict: a word counts only if every sign under it takes a value the sign takes at least 5% of the
time; it also fails the words next to a {?}).

| letter | signs | lexmeasure: old decrypt | R9407 key as is | re-learned (`*_g`) | hand reading (count.py) | measure2 (strict) |
|---|---|---|---|---|---|---|
| R9408 | 7,068 | 0.585 (`decrypt_v2`) | 0.661 | 0.875 | **1358/1528 = 88.9%** | 0.814 |
| R9409 | 10,930 | 0.582 (`decrypt_v2`) | 0.746 | 0.840 | **1911/2361 = 80.9%** | 0.721 |
| R9410 f.244r | 1,329 | 0.690 (`r9410_v2_decrypt`) | 0.785 | 0.864 | **255/304 = 83.9%** (old reading ~69% firm) | 0.729 |
| R9413 | 7,295 | 0.647 (`decrypt_v3`) | 0.721 | 0.848 | **1431/1663 = 86.0%** | 0.799 |
| R9427 | 2,640 | 0.546 (`decrypt_v2`) | 0.633 | 0.847 | **419/542 = 77.3%** | 0.638 |
| all five | 29,262 | | | | **5374/6398 = 84.0%** | |

No hand readings existed before except R9410's (`sysA/r9410_reading.txt`, 278 tokens, 63 "…" gaps, 22 more doubtful).
Decrypts: `r9408/decrypt_v3.txt`, `r9409/decrypt_v3.txt`, `r9410/decrypt_v3.txt`, `r9413/decrypt_v4.txt`,
`r9427/decrypt_v3.txt`; readings: `r94xx/reading.txt` (R9410 now has its own folder `r9410/`). The readings were drafted
by text-only reading agents from the decrypts with `show.py` and checked with measure2; R9409 P7 was read in the main
session, conservatively. A supervised re-key from the readings (`supkey.py`, then re-decode) did not beat the `_g`
decrypts (lexmeasure 0.838/0.847/0.838/0.817 for R9408/R9410/R9413/R9427), so the `_g` keys stand.

**Key values forced by context** (from the readings; the A′ hands differ, so they are per letter):
- all: E = d and ch; n = b/w (and o in R9410 "entschlossen", "darumb wol"); # = g, after c = k; 5 = a, often e; m = i/o;
  Q = g and l/ll ("aller", "wollen", "allein"; R9410 also z in "angezaigt"); β = b, -er after "ir" (R9410), sch
  (R9408 "schreiben", "schicken"; R9427 "teutschland"); a lone β, and a#, are nulls/dividers (R9408, R9410).
- R9408: my = m (Weinmaister, Sigmund), R = "und", d = r in "her(en)", b also l/n.
- R9409: Ŧ = l (solen, alain), ç = s, ç+ = f/v (Ferdinandischen, abgefertigt), 7o/ço = h, ð = "ich" after "hab",
  Θ = n, ʝ = "und" as a word, o = w for b (Sibenwurgen); the pair ç# brackets clear passages (divider).
- R9413: k = "ich" (word sign), Z = i (EM 85%) and e (komen, schreiben) as well as u; d = r in "heren"; Mj = m;
  ro = h; J+ = sch; [K] probably King Ferdinand ("mit dem [K] ein frid machen").
- R9427: R alone = "und", nn = w, β = sch/f, A = b/p, o = b, 9 = e (briefen, neue, with the gloss).

**What the letters say** (detail in each `reading.txt`):
- R9408 (Ofen, 8 Feb 1534, signed "… Weinmaister" in cipher): back from his mission, he handed over a ratschlag for
  Jörg Weinmeister, put into Latin; the instruction was written without knowledge of the Turk, who pays foreign
  soldiers in cash and thinks himself "herr der welt"; sums of 100,000 and 12 x 100,000 gulden; mining: Friedrich
  Schmaltz and his brother-in-law Reinhart, miners to be sent from Schwaz, a silver purchase via Nuremberg; Ferdinand's
  peace with the Turk, Hieronymus [Zara] and his son Vespasian sent back to the Turk; Katzianer two months before
  Kaschau; Emericus, provost of Stuhlweissenburg and bishop-elect of Neutra, married and was imprisoned; bad half-batzen
  bearing the dukes' stamp. P1 is a separate news page (Emperor Sigmund's 6,000 men, Constantinople and Syria).
- R9409 (early 1534): the dukes and the Roman king to agree on the confederation; a Turkish embassy; the Sultan to
  come to Constantinople; royal commissioners at Pressburg and Vienna achieved nothing; Katzianer's troops and Rascians
  on the Transylvanian border, Majláth forcing Hermannstadt, dearth in Transylvania; the voivode's practices, a truce in
  the Zips, Poland against Muscovy, seven Késmárk burghers held for ransom; the French and English kings advise war;
  numbered articles on a mining concession (Antoni Slesinger, Schmaltz as mining captain, Freiberger, gold-exchangers
  and silver-buyers, export of gold and silver refused); postscript "Auf den Reichstag", "Datum ut in literis".
- R9410 f.244r ("ersten [a]brilis Anno 35"): a treaty; the King of France has not acted as before; someone will accept
  no treaty unless the dukes are included ("in vertrag eingeschlossen"); hold together "bruederlich" against the
  Turks; commends himself "als seinen lieben herren und bruedern".
- R9413 (July / 7 June / 8 July 1534, addressed to secretary Waisenfelder): the dukes' letters received with joy; no
  reliable news of the Turk; Cornelius delayed because the French orator Antonius Rincon came to Constantinople;
  Katzianer's riders, Transylvania; the bishop of Wardein before Margrave Georg's castle Hunyad; the Württemberg war
  and the Landgrave; an ore sample from near Ofen (2½ mark silver); the Turk at sea with 200 galleys; the Hungarian
  lords' diet at Pressburg; herr Caspar to be dispatched; Antoni kept at the dukes' cost.
- R9427 (15/21/24 April [15]34, postscript 25 April): the Württemberg affair (the Bund, the dukes of Württemberg, the
  Landgrave, "kain vertrag"), Ferdinand, Christendom, Hungary; a provost-priest "alhie" took a wife and was imprisoned;
  the dukes' letter came "durch Stehan" on 23 April.

**R9410 ff.246-247, the Latin letter (2 Oct 2026, second session).** Transcribed by hand from images P3, P4 and P6
(P5 is P4 again) in `r9410/transcription_p3p6.txt` (65 lines, 2,342 signs; new codes for this page in its header);
crops in `r9410/crops/` (git-ignored). The contemporary gloss over P3 l.1 ("accepimus literas vestras") and the clear
phrases show it is Latin. Decoded with the R9410 German key re-learned on the `la` model (`sysA2/run.py --lang la`,
`sysA2/r9410b.tok`, `r9410b_g_dec.txt`): Latin at once ("…principem dominum Landtgravium … domini ducis
Wirtenbergensis … nos cum adversario nostro pacem non habere sed … inducias, quas … sancte et inviolabiliter
servaremus … Constantinopolim reversum … in Hungaria … Datum Bude ultima Iunii", Anno (15)34). Read in
`r9410/reading_p3p6.txt`: **350/422 = 82.9%** of words. The 4o sign (R9410 "und") is "et" here, and "in" before q;
the hourglass X follows "Vestre/Vestrarum" as the F.G. sign does in German, so it is the "Dominationes" code. The royal
"we", the "adversarius noster" with whom there is only a truce, the envoy back at Constantinople and Buda as the place
make it a letter of King John (Zápolya) to the Dukes of Bavaria, 30 June 1534.

**Look-alike check at the images (`sysA2/lookalike_check.md`, one image agent, 2 Oct 2026).** R9408 `y` is two signs:
dotted ÿ = t (about 40 checked) and undotted γ = r (15), plus an m+γ ligature (the reading's "my" = m). R9408 `4` is
two signs: closed 4 = e (23 of 25) and open ч = i (32 of 35), as on R9407. R9409 `c+` is one shape for da/ch/f (a key
polyphony, not a merge), but every "sch" is a different sign (open ɔ-hook + cross; also coded bare `+` and `E+`).
The splits were applied from the reading (`sysA2/applysplit.py` -> `r9408s.tok`, 380 signs recoded; `r9409s.tok`,
9) and regraded: the strict measure moved R9408 0.814 -> 0.812 and R9409 0.721 -> 0.724, the re-learned machine
decrypts 0.875 -> 0.870 and 0.840 -> 0.842. No change: the readers had already used the values the shapes carry,
so the splits confirm the readings but do not open the unread words.

**Push toward the bar, 3-5 Oct 2026.** Tools: `sysA2/fill.py` (each {?} located on the signs by a wildcard alignment,
then a beam that allows only lexicon words and only sign values attested in the six hand readings plus R9407,
pooled with per-hand weighting; other occurrences of the same sign string listed for verification);
`measure_pooled.py`; image re-transcription of every line holding an unread word (R9408 98 lines ->
`r9408/transcription_v4.txt`, 143 sign edits, merged as `sysA2/r9408m.tok`; R9413 99 lines -> v3, then a close-zoom
second pass on 67 -> `r9413/transcription_v4.txt`; R9409 181 lines -> `r9409/transcription_v3.txt`, ~356 edits),
each followed by a reading round under fixed rules (real word, fits sense, every sign value attested, other
occurrences agree). R9410 ff.246-247 retried by hand on my own crops. New readings of note: the 4#o ligature =
"auch" (R9410, R9413); Ferenc and Imre Bebek, Zangiacen, Z[i]back (R9413); "die ienitschern", Sigmund, Sibenburgen
(R9408); Schongau, holtz (R9409); Debreczen, Kesmarckt (R9427); in Latin "id eciam iam constare", "[r]esponsio",
"re[sp]onderimus" (z read as sp, doubtful). **K word sign = King Ferdinand** (grade B): it sends Hieronymus of Zara and
his son Vespasian to the Turk (R9408; Ferdinand's 1533 envoys), the Hungarian lords "so mit dem [K] halten" hold the
Pressburg diet (R9413), the Württemberg war is "wider [K]" (R9413, R9427). Not counted as words.

| letter | words read 2 Oct | words read 5 Oct | strict measure2 |
|---|---|---|---|
| R9413 | 86.0% | **94.3%** (1553/1647) | 0.81 |
| R9408 | 88.9% | **91.8%** (1405/1530) | 0.84 (on r9408m.tok) |
| R9410 ff.246-247 (Latin) | 82.9% | **88.9%** (375/422) | |
| R9409 | 80.9% | **87.2%** (2077/2381) | 0.80 |
| R9410 f.244r | 83.9% | **85.8%** (260/303) | |
| R9427 | 77.3% | **82.6%** (450/545) | 0.70 |
| all six | 83.9% | **89.0%** (6120/6828) | |

None reaches 95%: the target stays read in part. A third reading round on R9413 (v4 signs) and the second image pass on
R9408 (20 of 72 lines done, `r9408/retranscribe_v5.txt`, not yet applied) were cut off by the API usage limit on
3 Oct; R9427 and R9410 f.244r have had no image re-transcription yet. Next: finish those three, then reading rounds.

**5 Oct 2026, last pass.** R9413 third reading round: nothing further passes the rules (94.3%). R9408 second image
pass finished (72 lines; 6 corrected -> `r9408/transcription_v5.txt`; the pass was coarse on P2.02-13 and P2.26,
flagged in `retranscribe_v5.txt`). R9427 (44 lines, ~95 sign edits: m?j = M, many 4 = open ч, a+ = c+) and R9410
f.244r (23 lines, 16 edits) re-transcribed at the image (`transcription_v3.txt` in each folder), then a reading round:
R9427 84.3% (458/543; "Franczen Bebeck" again, "furstenthumb zu erobern"), R9410 f.244r 86.1% (261/303), R9408 92.0%
(1408/1531; "all welt" in P1.04 is doubtful). Final per letter: R9413 94.3, R9408 92.0, R9410 ff.246-247 88.9,
R9409 87.2, R9410 f.244r 86.1, R9427 84.3; all six 89.3% (6132/6827). Nothing further moves under the rules: the
remaining unread words are legible signs whose values no reading settles (rare signs, name groups, the arch-with-dot
and a# marks). No letter reaches the 95% bar; the target stays read in part.

**State: read in part** (5 Oct: 89.0%, see the table above; the figures that follow are of 2 Oct). 83.9% of the six letters' words read as sense by count.py (R9408 88.9%, R9413 86.0%,
R9410 f.244r 83.9%, R9410 ff.246-247 82.9%, R9409 80.9%, R9427 77.3%; 5,724 of 6,820), below the 95% bar; no letter meets it. The unread words are legible signs whose
values the letters do not settle (merged look-alikes, rare signs, names), not missing key material.

## Remaining gaps

- R9408 (5 Oct: 125 of 1,530 unread; second image pass 20/72 lines done): 170 of 1,528 words unread ({?} in `r9408/reading.txt`: P1.01-06 and P1.20-26, the P2.01 greeting, the ratschlag clauses P2.06/25-30, P3.10-16, P4.16-28, P5.01-08, P6.04-07/28-30, the signature forename) - blocker: open-codes (workable); the signs are legible but take no value the letter settles; the y (ÿ/γ) and 4 (4/ч) look-alikes were split at the image 2 Oct 2026 without opening further words; next: a second reading round.
- R9413 (5 Oct: 94 of 1,647 unread): 232 of 1,663 words unread (P1 opening and P1.19-26, P2.05-12, P3.04-12 the ore description, the 4o group on P5, P6-P7 short lines, P8 address) - blocker: open-codes (workable); next: image check of the noisy P1 opening lines and of the 4o group, second reading round.
- R9409 (5 Oct: 304 of 2,381 unread, after image re-transcription of 181 lines): 450 of 2,361 words unread (P1.01-03 salutation and date, P7 about half, names at P3.05-30 and P6.18/31, runs at P2.11, P3.04/07/34, P4.03/05/22, P5.18-19, P6.05/09; the F.G.-like sign read as a letter at P1.18, P5.23/26, P6.24) - blocker: open-codes (workable); c+ checked at the image (one shape for da/ch/f; sch a separate sign); next: second reading round of P7.
- R9410 f.244r (5 Oct: 43 of 303 unread): 49 of 304 words unread (P1.03-05, the a# group, P1.29-32, the place in the date line) - blocker: open-codes (workable).
- R9410 ff.246-247 (the Latin letter, Buda 30 June 1534; 5 Oct: 47 unread): 72 of 422 words unread (the P3.01-02 opening, P3.13 and P4.09-11 clauses, the name groups e9vn8/e9v9q4 at P4.12 and P4.20, the a# group, P6.04-05) - blocker: open-codes (workable); transcribed from the images and read 2 Oct 2026.
- R9427 (5 Oct: 95 of 545 unread; image re-transcription not yet done): 123 of 542 words unread (ends of P1.01-03, P1.09-14, names P2.03-23, the signature) - blocker: open-codes (workable).

## Escalation

- [x] siblings: R9368 (glossed sibling of System A), R9407 (augurelio1535), R9411/R9412 (sperantio1534, system L, a different key on look-alike shapes) and the R9423 register checked.
- [x] clear-pages: glosses used on R9427 and R9410 (and the R9368 gloss key tried on R9410: failed).
- [x] known-keys: the R9368 gloss key, the R9427 gloss key and the improved R9407 key (augurelio1535 pass 2) tried; the last fits by sign shape.
- [x] print: web search for KAA 4591 / Augurelio ciphers found no edition.
- [x] key-rebuild: System A′ from the R9427 gloss, extended by constrained annealing over R9408+R9410 with the gloss values fixed (open signs settled: # t, o a, X e in running text, A u, S h, | e). Scoring E as d vs ch over the combined text: ch scores better (−3.458 vs −3.537 per char) but gives "charzu" for darzu, so E is two look-alike signs (d and ch) merged in transcription — needs a visual re-split on the images.
- [x] retry: System A′ letters re-decoded with the extended key and each E resolved as d or ch by de-1500s context (`sysA_decode.py`); decrypts in `r9408/decrypt.txt`, `r9409/decrypt.txt`, `sysA/r9410_decrypt.txt`, `r9413/decrypt.txt`. Remaining noise is transcription-level (merged look-alikes, doubtful signs), not key-level.
- [x] key-rebuild/retry (2 Oct 2026, System A′): the improved R9407 key (augurelio1535 pass 2) carried to R9408, R9409, R9410, R9413, R9427 by sign shape, re-learned per letter by EM and word-beam re-estimation (`sysA2/`), R9408 look-alike split finished at the image (`r9408/split_p6p7.md`), hand reading rounds over every line of all five letters (`r94xx/reading.txt`), a supervised re-key from the readings (no gain). Readings 77-89% of words, 84.0% overall.
- [x] retry (2 Oct 2026, second pass): R9410 ff.246-247 transcribed from the images and read (82.9%); the look-alikes R9408 y/4 and R9409 c+ checked at the images, split, re-decoded and regraded (no gain).
- [x] retry (3-5 Oct 2026): every unread line re-transcribed at the image (R9408, R9413 twice, R9409), sign-constrained pooled-key candidates (fill.py) with second-occurrence checks, reading rounds; 83.9% -> 89.0% of words; R9427/R9410a image passes and an R9408 second pass still to do.

## Assumptions for George's review

- R9407 (augurelio1535) and R9368 are in the same system, System A′, but are kept in their own entries: the keys are
  re-learned per letter (the hands differ), and R9407 is a separate catalogue item (164) with its own write-up. If one
  system should be one entry, augurelio1535 would join this one.
- The overall figure is 6,132 of 6,827 words = 89.8% (5 Oct 2026 counts); the 89.3% printed before 15 Oct 2026 was an
  arithmetic slip.

## Steps

- 2026-09-21: record list from the DECODE dump (141 records in KAA 4591: 102 keys, 39 ciphertexts); images of the
  14 catalogue-161 targets and 30 neighbouring keys fetched with the cookie.
- 2026-10-15: split by key (see the top of this file); this entry keeps System A′.
- 2026-10-03/05: push toward 95%: image re-transcription of unread lines, pooled-key candidates, reading rounds; 89.0% overall (see the 3-5 Oct paragraph); K = Ferdinand.
- 2026-10-02: R9410 ff.246-247 transcribed from images P3, P4, P6 (`r9410/transcription_p3p6.txt`, 2,342 signs, 65 lines; P5 = P4); Latin; decoded with the R9410 key re-learned on the `la` model (`sysA2/r9410b_g_dec.txt`) and read (`r9410/reading_p3p6.txt`, 82.9%).
- 2026-10-02: System A′ revisited (see the 2 Oct section): R9408 P6 l.24-31, P7 and six flagged signs split at the
  image (`r9408/transcription_v3.txt`); the R9407 pass-2 key carried to R9408/R9409/R9410/R9413/R9427 and re-learned
  per letter (`sysA2/`); lexical share 0.55-0.69 -> 0.84-0.88; hand readings of all five, 84.0% of words read; read in part.
