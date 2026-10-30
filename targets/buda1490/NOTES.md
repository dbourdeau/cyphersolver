# Maffeo da Treviglio to Tamás Bakócz, Milan 30 Nov 1490 (MNL OL DL 46150), catalogue 1235

Status: read in part, 30 Oct 2026; the site page, manifest, README row, reveal and keys.json are left to the
maintainers (review of PR #199). Key recovered from external plaintext (the clear
minute in Milan), extended by the retry pass of 30 Oct 2026; the letter is read in part: 561 of 624 words (89.9%) read
as sense by `measure.py`, under the 95% read bar (before the retry 544, 87.2%). The 39 transcription suspects were
checked on the image (29 Oct 2026: 11 fixed, 19 confirmed as writer departures, 9 ambiguous; transcription/suspects.md).
Every open word has a blocker in "Remaining gaps"; how far the minute can count as a check is set out in "The minute
as evidence: circularity" below. Statistical validation (`docs/_validate.py`, 30 Oct 2026): pass.

## The document

Hungarian National Archives (MNL OL), Diplomatikai Levéltár, DL 46150 (Q 10, Véghely collection; Hungaricana charter
228061, <https://archives.hungaricana.hu/en/charters/228061/>, viewer `/en/charters/view/228061/`). Four paper pages
in cipher, with the closing, date, signature ("Filius Mapheus Triuliensis") and the address in clear on p. 4
(`transcription/p4_clear.txt`): to Tamás Bakócz, bishop of Győr (Jaurinensis), chancellor of the King of Hungary.
The salutation "In christo pater et domine pater honorande" opens p. 1 in clear.

The writer is Maffeo da Treviglio, the Milanese agent who had negotiated the Sforza-Corvinus match since 1489 (the
Milan copies of his cipher letters are `../buda1489`). He writes from Milan on 30 November 1490 (feast of St Andrew;
the minute is dated "Ultimo Novembris 1490") after reaching Duke Gian Galeazzo Sforza ("my Most Illustrious Prince")
on the 20th (the minute says the 24th). After King Matthias's death (April 1490) the planned marriage of Bianca Maria
Sforza, the Duke's sister, to John Corvinus had lapsed; the new king, Vladislas II, took up the "affinity" himself.
The letter:

- reports Maffeo's audience in Buda with the king, Bianca Maria's part ("medio Illustrissime Domine Blance") and the
  Chancellor of Bohemia, and the Duke's warm reception of the offer; the Duke now counts Bakócz among his foremost
  friends;
- presents the alliance as the continuation of the bond with King Matthias;
- on the dowry: the King's demand seemed to exceed all measure and made the Duke hesitate (no king had ever received
  such a sum); still, having come down to 150,000 ducats, he now goes to 200,000, in jewels or money as the King
  chooses; if money, 10,000 of it goes to the bride's trousseau ("in uestitu sponse"); the King is to provide the
  jewels honourably;
- asks Bakócz to send the courier back at once: either envoys with a proper mandate come to Milan, or Milanese envoys
  go to conclude; otherwise Bakócz is to report the new king's will and decision.

Full texts: `reading/latin.md` (Latin), `reading/english.md` (translation), `reading/p1.md`-`p4.md` (line by line).

## The system

A homophonic Latin cipher of letter-like signs, figures and marks: 76 labels in 3,199 tokens (14 lost to damage),
about 60 signs that carry the text (`transcription/signs.md`, `key.md`). It is not Maffeo's 1489 key R5411 of
`../buda1489` (there a = r, 1, f and e = ꝛ, 4, //; here a = to, F (φ), L (⊥) and e = o, w, E, B), nor Somogyi's
reconstruction of it. `../buda1489/key_R5411.md` notes a second key "Cum Mafeo Triviliensi", ASMi cart. 1597 no. 107
(DECODE R5407), "a different alphabet (A = ⊥ ...)": ⊥ (L) is a homophone of a here, so R5407 may be this cipher's key.
Checked as far as this session could, 30 Oct 2026: see "Key R5407" below.

- Homophones: e has five signs (o, w, E, B, q), i four (2, 4, m, ni), a four, s five, t four, u three.
- Polyphonic signs: qA = s (107) / i (4) / t (3) (the i and t cases found by the retry pass, all seven confirmed as qA
  on the image); qB = u (157) / s (14) / f (7); ooA = u (61) / s (7); s = h / f; 3 = n (g six times, probably 3G
  misread); tp = b (a twice); gA = o (t twice).
- Pair units: Ho = p, oH = q, n + u-sign = q (else i), 6/6A + gA = ll.
- Doubled-letter signs: X = ss, LL = ll, Ob = mm, sl = cc, wL = tt, Od = dd; & = et.
- Code signs: ff = Serenissimus Dominus Rex (Hungarie), ve = Illustrissimus Princeps / Dominus meus (the Duke), Tx =
  Maiestas sua, Ga = affinitas, Gp = non, dt / dx = quod, K = quoniam, fo = centum quinquaginta milia; y = ducenta milia (200,000) at both places the
  minute has the sum (adopted in the retry pass; its third case, at the tt of admittendas, stays open).
- Nulls: A, al, aN, Rx, e.
- No word division. Spelling of the cipher writer: double consonants often single (afinitatem, suma, comunem), h
  dropped (retraere).

## How the key was obtained

1. **Images.** The 28 Oct stub could not get past the Hungaricana viewer (CORS in the built-in browser; a 403 to direct
   requests). The user supplied the three image files (p. 1, the pp. 2-3 spread, p. 4) from their own browser; they stay
   out of git (link above).
2. **Transcription** by Claude agents from crops, then shape-only split passes (q into qA/qB/4; g, oo, h, 8, 6) and two
   rounds of key-guided image repairs where every change had to be visible on the image (`transcription/signs.md`,
   per-page fix logs in the working folder).
3. **Ciphertext-only break.** Simulated annealing (`scripts/hsolve.py`, Latin 4-gram model, letter-frequency penalty;
   a synthetic control text by `scripts/control.py`) gave a first key; cribs (reuerendissimam dominationem uestram)
   fixed D = m; then six reading rounds, each decrypting, word-dividing, finding where the Latin broke, checking those
   signs on the images and adjusting the key (`scripts/dec14.py`, `scripts/measure14.py`). Strict words read rose
   from 23% to 79.2% (key14).
4. **External plaintext.** The clear minute of the same letter was then found in Vestigia (<https://www.vestigia.hu>, search by date with `scripts/vsearch.py`): document 194 = ASMi
   Sforzesco 642, "novembre no. 8" (`reading/clear_minute.txt`, read from the Vestigia images). An EM dynamic-
   programming alignment of the cipher with the minute (`scripts/ext/em_align.py`, `report.py`) gave the key sign by
   sign (`key.json`, `key.md`), the alignment (`reading/align.md`) and the list of isolated disagreements
   (`transcription/suspects.md`).
5. **Check of the ciphertext-only work.** Of the 424 words the blind key14 reading had read (not marked doubtful),
   396 = 93.4% match the minute exactly; key14 was right on 60 of 81 signs, 96.2% of tokens. It had missed the code
   signs (taken as nulls) and had ooB as u instead of s.

## The reading

`measure.py` counts the words of the cipher letter (the minute's words the cipher enciphers, plus the words it adds)
and calls a word read when its signs give a Latin word that fits the sentence, including where the wording differs
from the minute. It does not count a word that rests on an unchecked suspect sign, an unvalued sign or damage.

| page | words | read | % | of undamaged | suspect | unvalued | no sense | damage |
|---|---|---|---|---|---|---|---|---|
| 1 | 202 | 178 | 88.1 | 88.6 | 3 | 13 | 7 | 1 |
| 2 | 198 | 179 | 90.4 | 90.9 | 1 | 1 | 16 | 1 |
| 3 | 185 | 163 | 88.1 | 93.1 | 4 | 6 | 2 | 10 |
| 4 | 39 | 38 | 97.4 | 97.4 | 0 | 0 | 1 | 0 |
| all | 624 | 561 | **89.9** | 91.7 | 8 | 20 | 24 | 12 |

Read = 519 exact, 21 spelling variants, 14 different wording, 7 added words (`measure.txt`; before the retry 510, 18, 9,
7). Strict agreement with the minute (`reading/measure_external.txt`): tokens 3047/3199 = 95.2%, minute words 503/616 =
81.7%. Under the 95% bar the letter is read in part.

## Retry pass (30 Oct 2026)

`scripts/retry.py` (output `reading/retry.md`) takes the 80 words the 29 Oct measure left unread and runs each again
under an extended key: key.json, plus any value the alignment gives a sign in two or more other places, plus the
look-alike labels split from one shape family (q -> qA/qB/4, g -> gA/gB, oo, h, 8, 6, 3/3G ...), plus y as a code.
Grades: C+ reads under the extended key; M reads only if a look-alike label was mis-split; M-slip the image confirmed
the sister sign, so the slip is the writer's; - nothing explains it.

- C+ 17 words, adopted in `measure.py` (544 -> 561 words, 87.2% -> 89.9%):
  - qA is polyphonic: s, and i in circa, ipsam, animo, additione, and t in affinitatem, inter, debeat. All seven were
    checked on the image on 29 Oct and confirmed as qA, so they are not transcription errors; one sign giving the same
    letter in four (i) and three (t) unrelated words is a homophone the writer used, as qB is u/s/f (6 words).
  - y = ducenta milia (200,000) at P3L02 and P3L12, the two places the minute has the sum (4 words).
  - cotraxerat, prefatu: a nasal left out, the omitted-macron spelling (2 words).
  - wording the cipher has and that fits: debeat for the minute's doubtful "[?deberet]" (P2L20); necessarie, the
    adverb, for necessaria (P3L08); and P2L22, where the signs give "neque [u]ieat a quibus haberi possit" (nor does he
    see from whom it could be had) in place of the minute's "imo videat quod ambobus haberi possit": neque, a, quibus
    read (3 words); [u]ieat is uideat with the d left out and stays unread.
- M 2 words (reuerendissime P3L17, qB for 4; responso P3L29, gB for gA): both signs were already ambiguous on the
  image; not counted.
- M-slip 2 words (ostendit P1L21, 4 for qA; promiserat P2L27, 4 for q): the image shows the sister sign; not counted.
- Unexplained 47 words, and 12 damaged: no value, sister label or code explains them (Remaining gaps).

## Regrade of the read words (30 Oct 2026)

The second half of the retry step: the doubtful readings among the read words. `scripts/regrade.py` (output
`reading/regrade.md`) decodes every word `measure.py` counts as read again, sign by sign, with every value a key allows
(nulls may give nothing), and grades it by what the reading rests on: B, key.json and the blind key14 (ciphertext only,
before the minute was found) both give the word as read; K, key.json gives it and key14 does not; X, only the extended
key (qA = i/t) gives it; C, a code sign; D, no key gives the form as read. Where the alignment crossed the minute's word
order the stretch is tested as one group in the cipher's order.

- Of the 561 read words: B 466, K 16, X 7, C 72, D 0.
- The doubtful readings: the 21 spelling variants are 19 B, 1 K (sangine: 3 = g, key14 had 3 = n), 1 X (afinitatem,
  qA = t); the 9 wording readings 8 B, 1 X (debeat); the two crossed stretches are B: P3L04-05 "habere uelit tantum"
  is spelt by s F tp o a w qB o hA 2 Q Q to 3 gB qB x under key values, so "uelit" is not supplied from outside, and
  P2L22 spells "neque" in full (P o oH qB w), then [u]ieat (unread) and "a quibus"; of the 7 added words, the three "et"
  are B and non, quoniam, quod are C.
- No read word needs an emendation or abbreviation to be counted: the D grade is empty, so nothing was moved.
- The 16 K words rest on values key14 did not have (3 = g in regnum, regno, dignitatem twice, agi, sangine; gA = t in sit,
  cepta; tp = a in quam, exponenda; 6 = c in cui; H = p in ceptum; and the double-letter signs Ob = mm, sl = cc,
  wL = tt, Bd = x, which key14 left unvalued). Each value recurs in other words, but its source is the alignment.

## The minute as evidence: circularity

The key in `key.json` was rebuilt by aligning the cipher with the clear minute; `measure.py` calls a word exact when it
gives the minute's word; the 41 transcription suspects were chosen because they disagreed with the minute; the damaged
words are filled from the minute; and the retry's minority values come from the same alignment. So agreement with the
minute (tokens 95.2%, words 81.7%) is in large part built in and does not confirm the key or the reading. Said plainly:
the minute is the source of the key, not an independent check of it. What does not depend on the minute:

1. **The blind key.** key14 was recovered from the ciphertext alone (annealing, one crib, six reading rounds with image
   checks) before the minute was found (WORKLOG, 29 Oct 2026: the Vestigia search came after round 6). Compared
   afterwards: 60 of 81 signs right, covering 96.2% of tokens; of the 424 words its reading had read, 396 (93.4%) are
   the minute's word. That is the independent test, and it covers the letter signs. It does not cover the code signs
   (ff, Tx, Ga, Gp, dt, dx, K, fo, ve, y): key14 had them as nulls or unvalued, so their values rest on the minute alone.
2. **Statistical validation** (`docs/_validate.py`, 30 Oct 2026, model la-letters, order 4, no spaces): the decryption
   scores -2.140 per letter; random keys of the same structure -5.566 (sd 0.351, z 9.8); keys annealed onto the
   shuffled ciphertext at best -3.214 (z 41.0); verdict pass. The annealer started from random keys on the real
   ciphertext reaches -2.185, close to the reading: the ciphertext alone supports a key of this quality. The negative
   control (`--control --quick`: the reading replaced by a key fitted to shuffled text) does not pass (underdetermined,
   -3.316). The language model owes nothing to the minute; the test checks the key, not the agreement.
3. **Text the minute does not have.** Under the key the cipher gives Latin that is not in the minute and fits: "non" in
   "amabat non mediocriter" where the minute has a doubtful word, "quoniam" where it is illegible, "debeat" where it has
   "[?deberet]", "neque [u]ieat a quibus" for "imo videat quod ambobus", "habere uelit tantum" for "tantum habere",
   extendet, euenit, debebit, three added "et". A key fitted to the minute would not give sense where the minute is
   silent or different.
4. **The image check went against the minute as often as with it.** Of the 39 suspects, 19 were confirmed as written
   (the writer departed from the minute) and 9 left ambiguous; 11 were changed, each to a shape the crop shows
   (`transcription/checks/`).
5. **The regrade** (`reading/regrade.md`): 466 of the 624 words (74.7%) read with values the blind key14 also has,
   so they do not rest on the minute; the other 95 read words rest on it (72 on code signs, 16 on key.json values key14
   lacked, 7 on the extended qA = i/t). The table in `reading/regrade.md` lists every read word that is not graded B.
6. **The clear closing and address** on p. 4 (date, signature "Filius Mapheus Triuliensis", Bakócz as bishop of Győr and
   chancellor) are read directly and agree with the minute's date and parties.

What the minute alone supplies: the meanings of the code signs (72 read words), the values key14 did not have (16
words), the polyphonic minority values (qA = i/t, 7 words), the 12 damaged words, and the choice of the minute's word
where several readings would fit. These are graded
C (from a known-plaintext letter), not H.

## Key R5407

ASMi Carteggio Sforzesco cart. 1597 no. 107, DECODE R5407, headed "Cum Mafeo Triviliensi" (read on the 23 Oct 2026
contact sheet of the 134 cart. 1597 key headings, `../buda1489/key_R5411.md`). Tried 30 Oct 2026:

- The record could not be opened from this session: de-crypt.org is refused by the session's network policy (HTTP 403
  at the proxy), and the DECODE login cookie the fetch scripts use lives on the maintainer's machine. No image or
  transcription of R5407 is in the repository; the heading band seen on 23 Oct is the only sight of it.
- The one value known, A = ⊥, agrees with this cipher: ⊥ (label L) is a homophone of a here, 38 of 38 aligned cases
  (key.json; with to and F, the three a-signs). In the 1489 key R5411 the same shape is h, which is one reason R5411 was
  ruled out. Weight of the agreement: this cipher has about 60 letter signs, three of them for a, so an unrelated key
  that wrote ⊥ for A would match by chance about 1 time in 20. That supports R5407 as the key of DL 46150 but does not
  prove it: it is one value, and ⊥ = a may be a habit of the Sforza chancery.
- The dates fit: R5411 is Maffeo's key of 1489-90 (Buda, to Ludovico Sforza); a second key with Maffeo is expected
  after Matthias's death (April 1490), and DL 46150 was enciphered in Milan in November 1490 for Bakócz.
- Not done, and the next step: open R5407 on DECODE, transcribe its alphabet, doubles and nomenclator, and compare it
  sign by sign with `key.md`. If it is this key, its nomenclator should name the one-off title signs (P1L06 Bianca,
  P1L10 the Chancellor of Bohemia, P1L17) and settle 8C, y and the "A qB s tp" group, and the minute would no longer be
  the only source of the code values. `decode_updates/queue.json` carries the pointer for R5407.

## The cipher and the minute

The cipher was made from the corrected minute: every interlinear insertion is enciphered (precipue inclinare, bonis
operibus, summa / expeti, conditiones, ut spero, the caret "centum"), and so is the long marginal addition (et eo minus
quoniam ... communem habere solet), in its reading position; none of the deleted passages is ("ne tam immodica petitio
...", "bona habere"). The cipher writer added "et" three times and "non" in "amabat non mediocriter", where the minute
has a doubtful word, and "quoniam" where the minute is illegible. `reading/clear_vs_cipher.md` lists the differences.

## Remaining gaps

- 8 words on signs left ambiguous by the image check - blocker: illegible; P1L04 dominationem, P1L05 cepit, P1L20
  semper, P2L17 adduxit, P3L10 secundum, P3L17 reuerendissime, P3L19 descendit, P3L29 responso: each sign was checked on
  the Hungaricana scan, the only image there is, and lies on a crease or under a blot or falls between two look-alike
  shapes (qB/gA, gA/gB, 5/gB, Q/Y/g); the retry reads reuerendissime and responso if the sign is the sister shape
  (grade M), which only the original in MNL OL could settle.
- 15 words on letter signs standing once for a title or phrase - blocker: open-codes; P1L06 "Illustrissime Domine
  Blance" (x), P1L10 "Magnifico Domino Cancellario Boemie" (a), P1L17 "Serenissimi Domini Regis sui necnon" (w, Q),
  P3L08 "summa ducentorum milium" (A qB s tp): each stands once, so this letter cannot fix a value, and the meaning comes
  from the minute alone; the nomenclator of R5407, if it is this key, would name them (see "Key R5407").
- 4 words on signs with no value at that place - blocker: too-short; P1L12 excellentia (8, a, 6, d in one word, two of
  them confirmed on the image), P3L21 reiici (8C: 4 tokens, i twice, ii once), P3L27 admittendas (y where tt stands),
  P3L09 esse (only the null A stands there: the word is not enciphered): single cases, no second occurrence to fix a
  value; R5407 would settle 8C and y.
- 9 words where the image confirmed the writer's own sign - blocker: too-short; cicius P1L01, amictssimo P1L19, minisse
  P2L14, petite P2L15, ragi P2L27, ostendare P2L28 (no homophone link), oitendit P1L21 and promisirat P2L27 (only a
  sister label), and P3L17 "et" for "ut" (o for u): the writer's departures, each once; the intended word is clear from
  the sentence (grade I) but is not counted.
- 15 words with letters left out or multi-sign departures - blocker: too-short; presenis P1L02, proter P2L07 and P2L08,
  ali P2L24, [u]ieat P2L22 (letters left out); mel and et for "mea ex" P1L11, reeatur P1L19, ubeiimum and frsotum P2L02,
  ad for "et" P2L11, quemamthum P2L15, ssga P3L03, ainc P4L01; and the extra ff on P2L03: each departure occurs once and
  no value, sister label or code in the extended key explains it (retry pass). Still open: a shape check on the image of
  the ten multi-sign ones, as was done for the 39 one-sign suspects. It needs the page images, which are not in the
  repository (they were supplied from the contributor's own browser on 29 Oct 2026), and Hungaricana refuses this
  session; it is the one step that could still change these words.
- 12 words with a lost sign - blocker: illegible; P1L18, P2L16, P3L15-21, P3L28: holes and blots in the paper; filled
  from the minute in ⟨⟩.

## Escalation

- [x] siblings: `../buda1489` (Milan copies of Maffeo's letters) and key R5411: a different alphabet; Vestigia lists a
  later Maffeo letter to Bakócz (13 Nov 1492, sc. 645, Vestigia 2251, a copy) to try with this key
- [x] clear-pages: the closing and address on p. 4 are in clear; the clear minute is ASMi Sforzesco 642 (Vestigia 194)
- [x] known-keys: R5411 and Somogyi's key ruled out; R5407 (second Maffeo key) tried 30 Oct 2026 as far as possible:
  its one known value A = ⊥ agrees (L = a, 38 of 38); the record itself was unreachable from this session (DECODE
  refused by the network policy), so the full comparison is still to do
- [x] print: no edition of DL 46150 found; Vestigia 194 prints the minute
- [x] key-rebuild: ciphertext-only (key14, 79.2% strict), from the minute (key.json), extended in the retry (qA = s/i/t,
  y = 200,000)
- [x] retry: `scripts/retry.py` (30 Oct 2026) re-ran all 80 unread words under the extended key and regraded them: 17
  regained (C+), 2 M, 2 M-slip, 47 unexplained, 12 damaged; `reading/retry.md`. The doubtful read words regraded by
  `scripts/regrade.py` (30 Oct 2026): 466 B, 16 K, 7 X, 72 C, 0 D, nothing withdrawn; `reading/regrade.md`

## History

### 28 Oct 2026: not attempted, blocked (claude-sonnet-5-5)
1. Read buda1489 NOTES, key_R5411.md and the 1235 verification record.
2. Hungaricana viewer: five images (colour target, orig_1 p. 1 3668x3739 px, orig_2 spread of pp. 2-3, orig_3 p. 4,
   seal). The viewer's tile requests are blocked by CORS in the built-in browser and the tile URLs are encrypted
   client-side; only 829 px thumbnails were reachable, too small to transcribe. Nothing was bypassed.

### 29 Oct 2026: transcription, ciphertext-only break, key from the minute (claude-opus-5-5)
See `WORKLOG.md`.

### 30 Oct 2026: review fixes for PR #199 (claude-opus-5-5)
Retry pass (`scripts/retry.py`, 544 -> 561 words), key R5407 tried (one value agrees; record unreachable), circularity
note, statistical validation (`validation.tsv`, `scripts/make_validation.py`; pass), Latin letters model `la-letters`
added to `lang/` (Gutenberg unreachable); regrade of the read words against the blind key
(`scripts/regrade.py`: 466 of 624 words independent of the minute, no reading withdrawn). See `WORKLOG.md`.
A site page and its generated files were pushed at 23:01 and taken out again the same evening: the review asks
the maintainers to add the page, manifest, README row, portrait, snip, reveal and keys.json.

## Files

- `transcription/p1.txt`-`p4.txt` (final), `signs.md`, `suspects.md`, `p4_clear.txt`
- `key.json`, `key.md`; `scripts/build_key.py` writes them from `scripts/data/key_external.json`
- `reading/p1.md`-`p4.md`, `latin.md`, `english.md`; `clear_minute.txt`, `clear_minute_running.txt`,
  `clear_vs_cipher.md`, `align.md`, `measure_external.txt`
- `measure.py` -> `measure.txt` and the reading files; `scripts/retry.py` -> `reading/retry.md`;
  `scripts/regrade.py` -> `reading/regrade.md`
- `validation.tsv` (from `scripts/make_validation.py`) for `docs/_validate.py`
- `scripts/`: `hsolve.py` (annealer), `refine.py`, `control.py`, `dec14.py`, `build14.py`, `measure14.py` (the
  ciphertext-only rounds; they ran from the working folder and expect its files), `ext/` (alignment with the minute),
  `data/` (alignment.json, key_external.json, key14.json)
