# BayHStA Kurbayern Äußeres Archiv 4591 — fourteen ciphertexts in the Bavarian key volume

Status: in progress

Split entry (Lasry, 25 Sept 2026): primary method stays key from adjacent plaintext; R9416 f. 263, broken ciphertext-only, is a second part (outcome.parts) with its own README row under ciphertext-only.

Catalogue entry 161 ("Unknown sender to unknown recipient, 14 ciphertexts"). DECODE R9291, R9319, R9322, R9323,
R9325, R9367, R9408, R9409, R9410, R9413, R9416, R9417, R9424, R9427. Images: DECODE, login (cookie in
`targets/bordeaux/decode/cookie.txt`); not public domain, kept in `img/` (git-ignored).

## What the volume is

KAA 4591 is the ducal chancery's collection of cipher keys, 1530s–1620 (DECODE lists 102 key records R9277–R9423
from it), with ciphertexts bound in among the keys. The fourteen catalogue records are not one correspondence:
they are separate letters in at least six systems, several with their key a few folios away.

| Record | Folio | What it is | System | Key | State |
|---|---|---|---|---|---|
| R9291 | 36 | a strip of cipher signs (alphabet row + second row), not a letter | graphic alphabet | itself a key fragment | reclassify |
| R9319 | 96–114 | "Post Scripta", dockets "…83": squared grille sheets with dots, laid over a clear cover letter (f.116 visible under f.102: "Die 4 od 5000 Cronen…") | dot grille | the cover letters | **blocked**: f.115–118 not imaged on DECODE |
| R9322 | 121–122 | f.121 Hieronymus Łaski, Buda 24 Nov 1529, copy of his letter to Count Palatine Frederick; f.122 King John of Hungary to Duke Ludwig of Bavaria, Buda 1529 | System B | rebuilt from glosses | **read** |
| R9323 | 123 | Latin note to the Bavarian secretary (Łaski circle) | System B | rebuilt from glosses | 3 of 13 lines, rest in hand |
| R9325 | 129 | Latin note, Fulda affair (1576) | letter substitution + nomenclator | **R9324 (f.124–127)** | **read** |
| R9367 | 169 | German letter, son to father, 22 March 1535, names/phrases in cipher | letter signs | **R9423 block 2_4 ("H. Wilh.")** + values from context | **broken**, read in part (`r9367/decode_test.txt`) |
| R9408 | 236–239 | Jörg Weinmeister (signed in cipher) to the dukes, Ofen 8 Feb 1534, with Latin clear passages: his mission and a ratschlag, the Turk's power and money, mining (Schmaltz, Reinhart), Katzianer before Kaschau, the priest-bishop Emericus, bad coin with the dukes' stamp; P1 a separate news page (Emperor Sigmund, Constantinople, Syria) | System A′ | R9407 key carried over, re-learned per letter (2 Oct 2026) | read in part, **88.9%** of words (`r9408/reading.txt`) |
| R9409 | 240–243 | German intelligence report of early 1534 with clear phrases: Ferdinand and the confederation, the Turkish embassy, Pressburg, Katzianer and Majláth in Transylvania, Késmárk, Poland and Muscovy; numbered articles on mining (Antoni Slesinger, Schmaltz, Freiberger, gold-exchangers); postscript "Auf den Reichstag" | System A′ (same as R9410/R9427) | R9407 key carried over, re-learned per letter | read in part, **80.9%** of words (`r9409/reading.txt`) |
| R9410 | 244–247 | f.244r: German, "datum … ersten [a]brilis Anno 35", to the dukes: a treaty, the King of France, "bruederlich halten" against the Turks. ff.246–247 (P3, P4 = P5, P6): a second letter, in **Latin**, royal "we", "Datum Bude ultima Iunii Anno (15)34": thanks for the dukes' letters and for the Landgrave's and the Duke of Württemberg's news; "nos cum adversario nostro pacem non habere sed … inducias", which the other side breaks; an envoy back at Constantinople; the Turks; offers amicitia and fraternitas — evidently King John (Zápolya) to the Dukes of Bavaria | System A′ | R9407 key carried over, re-learned per letter | f.244r read in part, **83.9%** (`r9410/reading.txt`); ff.246–247 transcribed 2 Oct 2026 and read in part, **82.9%** (`r9410/reading_p3p6.txt`) |
| R9413 | 252–256 | letters of a Bavarian agent to the dukes, July and 7 June 1534 and a third of "8 Julij", addressed to secretary Waisenfelder: Cornelius, the French orator Antonius Rincon at Constantinople, Katzianer, the bishop of Wardein before Hunyad, the Württemberg war, an ore sample from near Ofen, the Turk's fleet, the Pressburg diet | System A′ | R9407 key carried over, re-learned per letter | read in part, **86.0%** (`r9413/reading.txt`) |
| R9416 | 262–263 | pp.1–2 a Bavarian servant to his duke, "eritags nach Jacobi" (Tuesday after 25 July): troops in Austria/Styria, asks for 7 years' pension and the Oberrichter post at Straubing; pp.3–4 another sign set | homophonic signs | interlinear | pp.1–2 **read at the time**; pp.3–4 **broken ciphertext-only** (de-1500s model), report on the Pressburg talks between the two kings and the Turk |
| R9417 | 264 | Łaski at Kraków, 16 June [1530], to the Bavarian secretary "Waisenfelder": Buda siege, Nicolaus Min… sent to France, meeting at Coburg | System B | rebuilt from glosses | **read** |
| R9424 | 274–277 | German letter, cipher in Latin-letter substitution | letters | margin notes | |
| R9427 | 287 | German newsletter to a duke, 15/21/24 April [15]34, postscript 25 April: the Württemberg affair (the Bund, the dukes of Württemberg, the Landgrave), Ferdinand, a provost-priest who married and was imprisoned; gloss over lines 1–10 | System A′ | gloss key, then the R9407 key carried over and re-learned | read in part, **77.3%** (`r9427/reading.txt`) |

System A (signs ↓ ω π 4 8 ÿ …) is also the system of R9368, R9407 (Augurelio), R9411–R9412 (Cornelio Sperantio):
(R9411–R9412 are written up separately in `targets/sperantio1534/`: King John to the dukes, 6 Feb 1534, and a Buda
newsletter of 8 Feb 1534, both read with the key of R9415, System L; catalogue 163.)
the Bavarian agents in Rome/Italy, 1530s. Key R9369 (f.172) is "Dno Aurelio Augurelio".

## R9325 (f.129) — read

Key R9324 (f.124–127): alphabet A x, b t, c o, d þ, e 2, f k, g y, h n, i a, k (looped b), l (barred b), m d, n i,
o c, p δ, q (looped δ), r ɓ, s Λ, t Z, u w, x ɣ, y 7, z ⊙; doubles bb v, cc ꝸ, dd XX, ee (crossed x), ff ß, gg,
ll, mm, nn 4, pp, rr, ss (m with tail), tt 3; sch st sp ch signs; nulls g, -o-, stemmed square, ⊟, W-like, 8
underlined. Nomenclator (f.126–127): Pontifex, Card. Comensis, Card. Matutius(?), Nuncius Ap., Electores
ecclesiastici, Cologne, Trier, Mainz, Würzburg (bishop, chapter, dean), Abbas / Capitulum / Decanus Fuldensis,
Imperator, Archdukes Matthias and Ernst, Landsberg league, Ferdinand of Austria, Dux Bavariae, Philip of Bavaria,
Nobilitas Fuldensis, Conradus til (?) dux nobilium, Nobilitas Franconiae, Landgrave Wilhelm, Elector of Saxony,
Augsburg-Confession princes, the Emperor's vice-chancellor and councillors. That is the 1576 deposition of Abbot
Balthasar von Dernbach of Fulda by his chapter and knights with Julius Echter of Würzburg.

Reading in `r9325/reading.txt`. Normalised:

> Protestatus [est] abbas secreto coactum [se] ad litem acceptare Pontificis inhibitionem. Rogatus Pontifex ut
> contradicendo se interponat, declaret sive sponte sive vi contra canones esse. Si id fiat, Abbas agere cessat et
> cum Pontifice litigabit; ad [quod] cum non possit, Consiliarii Caesaris iudicabunt, aut Pontifex tum facit quod
> iam voluit. Rogatus Dux Bavariae auxilio sit; Nuncius suadeat Pontifici ita ad protectionem via[m].

All signs resolve; slips: "secreto" written without its second e, "auxilio" begins with the i-sign, "voluit" ends
in the d-sign.

## System B (R9322, R9323, R9417) — Hieronymus Łaski, 1529–30

Monoalphabetic graphic substitution with a few word signs; key rebuilt from the interlinear glosses (153 aligned
word pairs; `sysB/key_from_glosses.tsv`): 3 i, X e, ⊕ s, U2 u/v, ⊙ a, N n, O m, M o, ⋇ r, HH t, W c/t, D d, ≡ p,
9 l, B b, Z g, Q q, ≐ f, † f, H h, XH x. Word signs from context: DAG = King John (Zápolya) ("non alio loco vult
habere [DAG] quam loco fratris sui", said of the Sultan), BIGX = Ferdinand ("concordia inter [DAG] et [BIGX]";
"ad oppugnandum dominia [BIGX]"), FLW = probably King John's title. Decoded text in `sysB/decoded.txt`.

- R9322 f.121: Łaski to a Bavarian duke, Buda 24 Nov 1529 (with a copy "ad illustrissimum dominum Fredericum imperii
  capitaneum"): King John followed the dukes' counsel; the Sultan, forced home by plague in his army, left John the
  kingdom of Hungary without tribute, fifty guns and a thousand hundredweight of powder, and will return next summer
  against Ferdinand's lands unless there is a concord; Łaski commends himself as the duke's servant.
- R9322 f.122: "Joannes Dei gratia rex Ungarie" to Duke Ludwig of Bavaria, Buda 1529: sends Lazarus the Jew as envoy.
- R9417 f.264: Łaski, Kraków 16 June [1530], to the dukes' secretary: letters of 12 June received; the siege army
  before Buda; concord best made through imperial princes; Nicolaus Min… sent to the King of France; the Sultan
  willing to receive in friendship whom King John names; asks for envoys to meet at Coburg in Saxony by (date) July.

## R9416 pp.3–4 (f.263) — broken from ciphertext only

3,150 signs, 661 words, word-separated, ~23 frequent signs; 'io' always together (treated as one sign). The
constrained annealer (`anneal.py`, homophone caps) with the new `de-1500s` model (Deutsches Textarchiv prints
1472–1609, added to `lang/` for this target) gave running German on the first run: "…uon beden kunigen zu entlicher
handlung gen Pressburg gesetzt… der tag zu Pressburg erfolgt ist… mit grossem pomp… dem turkischen kaiser… tribut…
zu geben…". The faint interlinear gloss on the first lines of f.263 ("nunmen bag uon beden kunigen zu entlicher /
handlung gen bresburg gesetzt") agrees with the solver's text word for word, which confirms the break independently.

Working decrypt (solver key, before the look-alike split; `r9416/decrypt_f263.txt`; corrected transcription
`r9416/p34_v2.txt`): the report of a Bavarian agent on the Pressburg negotiations between "beden kunigen" (Ferdinand
and John Zápolya) and their commissaries; a Turkish embassy; "der Emrich beeche" (Imre Czibak) offering the Sultan
tribute and "tausent tucaten"; "den hern Griti abgefertigt" (Alvise Gritti, killed Sept 1534) — so c.1533–34. The
cipher (sign codes f/z/j, H/K split in v2) is a homophonic simple substitution; codes "der d", "der g", "der h" are
persons (probably Ferdinand, Gritti's party, the Hungarian king). State: read in part — running German with local
errors; a clean reading needs the v2 transcription re-keyed and the 'y' sign split.

**30 Sept 2026 — recto lines 11-16 read clean** (to fill the gaps in the quotation for Lasry's list;
`r9416/reading_p3_11-16.txt`, word by word with grades). The v2 transcription was re-keyed by hand and every word
checked on the image; lines 11-12 agree with the faint contemporary gloss, which runs further down the page than
"its first lines" (g11: "das aus den tag zu bresburg erfolgt ist dahin auch"; g12: "des Ferd tail ... mit grossem
bumbb kummen sint auch"). The split the notes asked for, on these lines: v2 `z` is two shapes, the one-bar zig-zag
(e) and a two-bar dagger (s: "daraus", "Bresburg", "ist", "grossem", "sich", "das", "Fasnacht"); `b` covers d and l.
Normalised: "... daraus der Tag zu Pressburg erfolgt ist, dahin auch des [Ferd.] Tail mit grossem Pomp kummen
sint, auch volmechtigen Gwalt anzaigt, und sich zu beden Tailn entliche Vertrage versehen. Es hat sich aber
zutragen, das am Ertag in der Fasnacht von dem turkischen Kaiser ain treffliche Botschaft ankummen ..." [Ferd.] is
the code sign g read from the gloss (faint; "Fed" possible). Three signs after "Tail" (circle with dot, I, closing
curve) are passed over by the gloss and are not rendered. Lines 17-19 read in outline "... welcher dem [T] ain
Brief vom Kaiser bracht hat, welcher in Latein transferirt ist, desselben Copei ich E. F. G. hiemit schick";
"mit vy fngioDDio" on line 17 (perhaps "mit ir Scheffe[n]") is not settled. The rest of f. 263 is not re-keyed.

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
- R9416 f.263 clean reading - blocker: open-codes; paused 21 Sept 2026 (workable): v2 re-keyed (Pressburg talks read throughout); one sign serves ch but the annealer gives it s ("auss"=auch) — needs a digraph value set by hand. 30 Sept 2026: recto lines 11-16 read clean by hand (`r9416/reading_p3_11-16.txt`; z split into e and a two-bar s, b into d and l); the rest still to do the same way.
- R9323 lines 4, 8-10 - blocker: illegible; faint signs, several '?' in transcription.
- R9424 - blocker: no-key-material; R9422 alphabet cut at a/b and does not read as transcribed; R9420 (1531 keys, shift alphabet) and R9421 (tabula recta) checked; IoC 0.068 flat over periods 1–8 = monoalphabetic, yet annealing fails in German (de-1500s, with/without '/' and nulls), Latin and Italian — likely code groups (gloss names sit over single groups) plus transcription noise; gloss cribs too few.
- R9367 clean reading - blocker: open-codes; paused 21 Sept 2026 (workable): key block 2_4 read at zoom (`keys9423/2_4_zoom.txt`), reading in `r9367/reading.txt`: ⊡ ≈ ♀ are nulls/dividers; # (13×) and O open; L01–02, 07, 09–10, 13 mostly unread.
- R9319 - blocker: needs-physical-access; dot grille needs cover letters f.115-118, not imaged on DECODE.
R9291 is not a ciphertext (a key fragment, f.36): nothing to read, so it is not a gap.

## R9367 (f.169) — read in part

Son to father, Monday after Palm Sunday, 22 March 1535. In cipher: he was questioned about strange matters
("seltsam khinst gefragt") and denied everything ("aber a[ll]es verlaugnet"); he is taken for a poor writer
("schlechter schreiber") and sent to learn; nothing reliable learnt yet ("noch nicht freintlichs erfaren"); fears for
his person ("meines leib"); the Turks are coming up ("Tirckhen herauf ziechen"); a name read as Nothaft(?);
postscript names a Friedrich and "Schmalcz" (Schmalkalden?): "euch nicht guets". Key: R9423 block 2_4, "H. Wilh.
[15]25" (A 9, B v, C Δ, D +, E 6, F ⊥, G o, H 4, I w, K ‡, L 8, M ¥, N 3, O barred D, P two rings, Q 2, R 7, S y,
T ♉, V ‡‡, X o-o, Y ε, Z π; und 9, auch Z, ch t, das T, ll 9, rr m); the letter adds q a, Λ r, C s, H k, K z.

## Escalation

- [x] siblings: R9324 (key of R9325), R9368 (glossed sibling of System A), R9423 register (19 keys), R9422 (1583 key) all checked.
- [x] clear-pages: glosses used on R9322, R9323, R9416, R9417, R9427, R9424; R9319 cover letters not imaged.
- [x] known-keys: R9423 blocks tried on R9367 — 2_4 first failed with wrong pins, then fitted when the frequent signs were re-matched by shape (reads in part); R9422 on R9424 (failed).
- [x] print: web search for KAA 4591 / Augurelio ciphers found no edition.
- [x] key-rebuild: Łaski (System B) from glosses; System A′ from the R9427 gloss, extended by constrained annealing over R9408+R9410 with the gloss values fixed (open signs settled: # t, o a, X e in running text, A u, S h, | e). Scoring E as d vs ch over the combined text: ch scores better (−3.458 vs −3.537 per char) but gives "charzu" for darzu, so E is two look-alike signs (d and ch) merged in transcription — needs a visual re-split on the images. R9424 and R9367: no key material to rebuild from.
- [x] retry: R9424/R9367 re-annealed with de-1500s, homophone caps and nulls (failed). System A′ letters re-decoded with the extended key and each E resolved as d or ch by de-1500s context (`sysA_decode.py`); decrypts in `r9408/decrypt.txt`, `r9409/decrypt.txt`, `sysA/r9410_decrypt.txt`, `r9413/decrypt.txt`. Remaining noise is transcription-level (merged look-alikes, doubtful signs), not key-level.
- [x] key-rebuild/retry (2 Oct 2026, System A′): the improved R9407 key (augurelio1535 pass 2) carried to R9408, R9409, R9410, R9413, R9427 by sign shape, re-learned per letter by EM and word-beam re-estimation (`sysA2/`), R9408 look-alike split finished at the image (`r9408/split_p6p7.md`), hand reading rounds over every line of all five letters (`r94xx/reading.txt`), a supervised re-key from the readings (no gain). Readings 77-89% of words, 84.0% overall.
- [x] retry (2 Oct 2026, second pass): R9410 ff.246-247 transcribed from the images and read (82.9%); the look-alikes R9408 y/4 and R9409 c+ checked at the images, split, re-decoded and regraded (no gain).
- [x] retry (3-5 Oct 2026): every unread line re-transcribed at the image (R9408, R9413 twice, R9409), sign-constrained pooled-key candidates (fill.py) with second-occurrence checks, reading rounds; 83.9% -> 89.0% of words; R9427/R9410a image passes and an R9408 second pass still to do.

## Steps

- 2026-09-21: record list from the DECODE dump (141 records in KAA 4591: 102 keys, 39 ciphertexts); images of the
  14 targets and 30 neighbouring keys fetched with the cookie.
- Matched R9325 to key R9324 by the null signs (identical set); applied key, all words Latin; read.
- 2026-10-03/05: push toward 95%: image re-transcription of unread lines, pooled-key candidates, reading rounds; 89.0% overall (see the 3-5 Oct paragraph); K = Ferdinand.
- 2026-10-02: R9410 ff.246-247 transcribed from images P3, P4, P6 (`r9410/transcription_p3p6.txt`, 2,342 signs, 65 lines; P5 = P4); Latin; decoded with the R9410 key re-learned on the `la` model (`sysA2/r9410b_g_dec.txt`) and read (`r9410/reading_p3p6.txt`, 82.9%).
- 2026-10-02: System A′ revisited (see the 2 Oct section): R9408 P6 l.24-31, P7 and six flagged signs split at the
  image (`r9408/transcription_v3.txt`); the R9407 pass-2 key carried to R9408/R9409/R9410/R9413/R9427 and re-learned
  per letter (`sysA2/`); lexical share 0.55-0.69 -> 0.84-0.88; hand readings of all five, 84.0% of words read; read in part.
