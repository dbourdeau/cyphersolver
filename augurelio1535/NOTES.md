# Jörg Weinmeister to the Dukes of Bavaria, spring 1533 (DECODE R9407, "Augurellio")

Status: read (96.6% of plaintext words, measured; second pass 22 Sept 2026 read image P6 = f.235r and corrected the date to spring 1533)

The folder name keeps the first pass's '1535'; the letter is of late April-May 1533 (see "Second pass" below).

Catalogue entry 164, "Augurellio to ...". BayHStA Kurbayern Äußeres Archiv 4591 ff. 232-235, DECODE R9407,
7 images (P1 f.232 dorse, P2 address, P3 f.233, P4 f.234 = a column and a slip, P5 f.235, P7 address leaf;
there is no P6). Images: DECODE, login; not public domain, kept in `kaa4591/img/` (git-ignored). Work in
`work/`: transcriptions `p3_v5.txt`, `p5_v5.txt`, `p4a_v3.txt`, `p4b_v2.txt`, `p7_v2.txt`; readings
`*_reading*.txt` (including `p4bp7_reading.txt`); tools `em.py`, `hardem.py`, `beam.py`, `wbeam.py`, `supkey.py`, `measure.py`.

## Who wrote it

DECODE's "Augurellio" is the cover address on the outer face of the address leaf ("Mag.co domino ... Augurello").
The letter itself is signed **in cipher**, twice — at the foot of the slip (f.234) and of the address leaf:
`ɥ m ↓ I π ω ɥ □ 7 ϙ ɥ ʌx ÿ σ γ` = **Iorg Weinmaister** (Jörg/Georg Weinmeister), a Bavarian agent in Hungary.
The address on f.232v is to "dem durchleuchtigen hochgebornen fursten und herrn ... Hertzogen in Bayern"
(Wilhelm IV and Ludwig X), docketed "X Decembris 35".

## The cipher

System A′ of the volume: a homophonic cipher of graphic signs and numerals, no word division, e.g.
ω e, □ n, 4 e / ɥ i, x̸ u, ʌx s, ÿ t, 3 u, ↓ r, 8 n, π b/w/o, ⊏ c, Ӿ k/ch, I g/z, A p, δ l/h, 5 a, ∃ d/ch.
Ligatures: `ɔo` = h, `ꝏo` = sp. Word signs: **X = "F.G."** (fürstliche Gnaden — the same sign as in the sibling
key R9427), ♆ = ll; ʒ, K and Ω are unidentified. Several signs are genuinely two-valued in this hand
(# g/u/k, E d/ch, n b/w, m i/o, σ a/e, T g/z), and three shapes that the first transcription had merged are
separate signs: ‡‡ (g/u), the curved ℋ (sch/h) and Ӿ (k/ch), besides the upright Ħ (u).

The key R9369 (f.172), which is addressed "Dno Aurelio Augurelio", is **not** this letter's key (ω = l there).

## How it was read

R9410's gloss key, applied by shape, gave running German at once; the rest was a loop of
(a) machine decoding — EM over a letter-trigram HMM (`em.py`), hard-EM (`hardem.py`), a Viterbi decoder over
per-sign candidate sets (`beam.py`) and a word-aware beam using DTA word unigrams (`wbeam.py`);
(b) reading rounds over the signs; and (c) a supervised key rebuilt by aligning each reading back to its signs
(`supkey.py`). Every line of f.233 and f.235 was then checked against the image by hand — about 40 transcription
fixes (o- read as ō, Ӿ read as #, the curved ℋ merged into #, the ɔo/ꝏo ligatures, dropped signs).

Measured with `work/measure.py` (a word counts as read only when it carries no "?" and no more than one of its
signs takes a value used nowhere else in the letter): **f. 233 96.4%, f. 235 96.1%, the f.234 column 65%,
the whole letter about 89%.** The slip and the address leaf read 92%; the slip ends "Datum ut in litteris", which matches the faint later gloss over that line.

## What it says

- f.233: herr Caspar was sent into the camp. A powerful Hungarian lord, "More Lesli" (**László Móré**), with
  4000 foot and horse — Hungarians, Turks and Bohemians — holds the strong castle of **Palota** (Várpalota) and
  has long carried on great "morderei" there. At the diet of **Pressburg** both kings left Palota out of the
  settlement, so that whichever king comes first ...; the castle had been pledged by Stuhlweissenburg four years
  since for about 134,000 gulden. Although it was first bombarded in vain, against herr Caspar's advice, he hopes
  to achieve something by digging and battering the wall. Relief (entsetzung) has not been allowed, because of the
  peace made with the Turk; **Török Bálint**, one evening at Vienna well drunk, was sent to talk of the relief,
  and is to be spoken with in the morning when he is sober; the bishop of **Veszprém** was sent with the
  recruitment. What was negotiated at Pressburg, at Constantinople and elsewhere is not yet understood.
- f.235: warnings not to trust the other side's many words; the truce (anstand); the man writes that he has made
  peace with the Turk and will keep to it; the siege of Móré to be raised, or the besieged relieved; a castle
  taken after Easter, "heist **Simantorna**" (Simontornya), very strong; "das eur F.G. Hansen ... haben";
  burghers and merchants to deal by word of mouth; to speak graciously to him, that at Vienna to his factor ...;
  all letters from herr Caspar to be sent on without delay and secretly; the business to be kept quieter and more
  diligently; it will not be necessary to bring the Jews in further; the merchant Holunger.
- f.234 slip: "anheut dato ist ein Retz[?] komen mit briefen komen, sagt wie zu **Kriechischen Weissenburg** [Belgrade]
  funftzig tausent turcken sind auszogen hieher auf **Ofen** zu ...; so waiss er doch nit was fur ein frid ist,
  wie dan eur F.G. aus [dem] schreiben zu uernemen haben. Ist zu besorgen ... der krieg dan frid haben.
  **Datum ut in litteris.** Iorg Weinmaister." (a "Retz" = Ratz, a Rascian/Serb messenger.)
- f.234 column: a covering letter — what he has learnt from the man, good fortifications, eur F.G.'s letters,
  letters passing to the enemy, a separate copy sent "aus schuldiger pflicht", the clear Latin "Quid autem actum
  sit", agreement with the Turk and the peace against it, the messenger, recruiting.
- Clear Latin in the text: "Rarum novarum autem quae hic habemus", "Et propter illum hominem plures",
  "Quid autem actum sit", "Illud tamen summe necessarium esse existimo".

## Second pass (22 Sept 2026): image P6, the date, the full reading

Work in `pass2/`: `transcription.txt` (4,363 signs, one character per sign, all cipher pages), `key.txt`,
`decode.py` (polyphonic beam over the de-1500s model), `solve.py` (numpy annealer), `ctx.py`, `fix.py`,
`decrypt_v7.txt`, and **`reading.txt`**, the reading of the whole letter.

- **P6 is on DECODE.** `bordeaux/decode/fetch_decode.py` lists seven images for R9407 (P1-P7); P6 had simply never
  been downloaded. It is a straight photograph of **f.235r**, 36 lines, the leaf that image P4 shows at an angle
  (the first pass's "f.234 column", P4a: its l.04 `...l5nwt3cvmnQ3` = P6 l.05 `...b5nwt3cvmNf3`). The
  needs-physical-access gap is closed: f.235r reads in full.
- **Page order by sense:** f.233r (P3), P5 (the page with Simontornya), f.235r (P6), the slip on f.234 (P4, "Datum
  ut in literis", signed), the postscript on the address leaf (P7, signed again).
- **The date is spring 1533, not December 1535.** The letter describes King John's siege of Palota against
  Laszlo More (`More Lesl[o]`, P5 l.14): "er [King John] durch den [∇] und herr Casparn mit 4000 zu fuess und ross,
  ungern, turcken und Behamen ... het in ainem festen schloss Palota genent belegern lassen". Hungarian sources
  (hu.wikipedia "Palota ostroma (1533)", rubicon.hu) give exactly this siege: Hieronymus Łaski with Hassan bey's
  Turks and fifty Czech miners, from 14 April 1533, the walls mined at the end of May; Ferdinand stood aside by
  agreement. The letter is written while "si sein noch darvor", after "ostertag" (Easter 1533 = 13 April), and
  Katzianer is told that Ferdinand "mit dem turcken ein frid gemacht" (the 1533 truce/peace). The dorse docket reads
  "10. Decembris 33" (the first pass read 35); it is a filing date or the date of the covering letters ("datum ut
  in literis"). The outer address (P2) is "Doctor Christof [W...], Bayrisch rhat, meinem freundlichen lieben
  bruder": the packet went through the writer's brother, a Bavarian councillor in Munich.
- **The ∇ sign** is a name: it besieges Palota with herr Caspar (P3 l.07, P5 l.17), and recurs with Minckwitz and
  Kraków on f.235r. Probably **Łaski** (grade C). **The dotted ʃ sign** is King Ferdinand ("seins herren [ʃ] ...
  das er [ʃ] mit dem turcken ein frid gemacht"; "von [ʃ] nit bewilligt"; "zu Wien").
- **Key notes:** the hourglass ⧖ (Z) = F.G. is distinct from the slashed ✗ = u; `mγ` is one sign, m; Ψ = ll,
  Ħ-bar B = rr; the tiny superscript ° = p in "Caspar"; clear numerals 4000 (P3 l.08) and 34 (P3 l.16) sit inside the
  cipher. Polyphonic: E d/ch, π w/b/t/o, o b/w, ‡‡ g/u, j s/ch.
- **f.235r (new):** Schetinger is not to use the Jew further, who cannot be trusted: he let the letters be copied at
  Kraków before delivering them; Minckwitz has copies of the dukes' letters and, being at feud with [∇], may turn
  them against them; herr Caspar, who has been told to treat with the Turk on the dukes' behalf, asks them to be
  gracious to him and his children; a copy of a letter of Ferdinand's councillor now in Turkey to the regents at
  Vienna is enclosed; the Chancellor is going to Constantinople; Weinmeister will report what is negotiated there.
- Measured with a word count over `pass2/reading.txt`: 1,002 plaintext words, 34 unread (31 words, 3 uses of ∇):
  **96.7%** (1,003 words, 33 unread, after P3 l.09 "More Lesli genant" was taken from the first pass). The letter meets the read bar.

## Remaining gaps

- about 31 scattered words across the four cipher pages (listed as {?} in pass2/reading.txt) - blocker: open-codes; the signs are legible, each was retried with the extended key and at the image, and none gives a word under a value the letter uses; the sense of each sentence is not in doubt.
- the ∇ name sign (4 uses; probably Łaski) and one name at f.235r l.16 - blocker: open-codes; no key of the volume gives them.
- the first pass's f.234 column (P4a) - closed 22 Sept 2026: it is f.235r, read from image P6.

## Escalation

- [x] siblings: all seven images of R9407 listed and fetched (P6 was on DECODE); the System A′ letters R9408-R9413, R9427 and their keys (kaa4591/sysA, r9413/key_v3) applied;
  R9410's gloss key fits this letter.
- [x] clear-pages: the contemporary gloss over f.233 lines 1-3 read at zoom ("Genedig fursten und herrn ...
  Caspar ... das leger"); the faint single-sign glosses on f.235 used.
- [x] known-keys: R9369 (the key addressed to Augurelio, f.172) tested and rejected; the R9423 register checked.
- [x] print: Hungarian accounts of the 1533 siege of Palota (hu.wikipedia, rubicon.hu) found 22 Sept 2026 and used to date the letter; web searches (Augurelio + Bayern 1535 + Chiffre; Weinmeister + Palota/Móré) found no edition; the
  humanist G. A. Augurello (d. 1524) is a different man.
- [x] key-rebuild: EM, hard-EM, a supervised key from the aligned readings, a word-aware beam.
- [x] retry: second pass re-read every line of all four cipher pages at the image with a polyphonic beam decoder; two look-alike split passes; a full hand check of both main pages against the image; six reading
  rounds; a final targeted pass over every word that failed the measure.

## Steps

- 2026-09-22: images already on disk from the kaa4591 session; R9369 rejected against the gloss; System A′
  identified; P3/P5/P4/P7 transcribed; annealing and greedy climbs failed; R9410 key gave German; look-alike
  splits; EM/hard-EM/supervised key; hand check of both main pages; six reading rounds; f.233 95.7%,
  f.235 96.1% measured; the writer identified as Jörg Weinmeister from the ciphered signature.
- 2026-09-22 (second pass): P6 fetched (f.235r) and read; independent transcription of all pages (4,363 signs);
  annealer + polyphonic beam; every line checked at the image; date fixed to spring 1533 from the Palota siege;
  96.6% of plaintext words read; class raised to read.
