# BayHStA Kurbayern Äußeres Archiv 4591 — fourteen ciphertexts in the Bavarian key volume

Status: in progress

Catalogue entry 161 ("Unknown sender to unknown recipient, 14 ciphertexts"). DECODE R9291, R9319, R9322, R9323,
R9325, R9367, R9408, R9409, R9410, R9413, R9416, R9417, R9424, R9427. Images: DECODE, login (cookie in
`bordeaux/decode/cookie.txt`); not public domain, kept in `img/` (git-ignored).

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
| R9408 | 236–239 | Anno 1534, German report to "Sp…nio" (Sperantio?) with Latin clear passages: Hungary, the Turk, Constantinople, Syria, "dreissig tausent man aus dem teutschen land" | System A′ | R9427 gloss key | **broken**, read in part (`r9408/decrypt_working.txt`) |
| R9409 | 240–243 | German intelligence report with clear phrases, numbered articles and answers (pp.5–7), postscript "Auf den Reichstag…"; 11,311 signs transcribed | System A′ (same as R9410/R9427) | anchors from R9427 gloss | **broken**, read in part |
| R9410 | 244–247 | German, Anno 35, to the duke: the Turks, "bruederlich halten" | System A′ | R9427 gloss key | **broken**, read in part (`sysA/r9410_decrypt_working.txt`) |
| R9413 | 252–256 | two German letters to the duke, [July] and 7 June 1534: Niclas Jurisitz, Cornelius (Sperantio?), Antonius Rincon the French king's orator, Constantinople, Emericus (Czibak), the Turk | System A′ | R9427 gloss key | **broken**, read in part (all 8 pp. transcribed, ~7,380 signs; letters of 11 July and 7 June 1534, a 3rd dated "8 Julij"; sign Z unassigned, probably a null) |
| R9416 | 262–263 | pp.1–2 a Bavarian servant to his duke, "eritags nach Jacobi" (Tuesday after 25 July): troops in Austria/Styria, asks for 7 years' pension and the Oberrichter post at Straubing; pp.3–4 another sign set | homophonic signs | interlinear | pp.1–2 **read at the time**; pp.3–4 **broken ciphertext-only** (de-1500s model), report on the Pressburg talks between the two kings and the Turk |
| R9417 | 264 | Łaski at Kraków, 16 June [1530], to the Bavarian secretary "Waisenfelder": Buda siege, Nicolaus Min… sent to France, meeting at Coburg | System B | rebuilt from glosses | **read** |
| R9424 | 274–277 | German letter, cipher in Latin-letter substitution | letters | margin notes | |
| R9427 | 287 | German newsletter to a duke, dated 24 April [15]34, postscript 25 April; gloss over lines 1–10 | System A′ | partial key from gloss: 5 a, 4/ω e, □ n, p i, 8 h, 9 o, ↓ r, ÿ t, 7 m, π b, X = F.G. | **broken**, key rebuilt from its own gloss; P1 11–35 and P2 decoded (`r9427/decrypt.txt`), read in part |

System A (signs ↓ ω π 4 8 ÿ …) is also the system of R9368, R9407 (Augurelio), R9411–R9412 (Cornelio Sperantio):
(R9411–R9412 are written up separately in `sperantio1534/`: King John to the dukes, 6 Feb 1534, and a Buda
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

## System A′ (R9409, R9410, R9427; R9408 and R9413 being transcribed) — key from the R9427 gloss, read in part

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

## Remaining gaps

- R9408 clean reading - blocker: open-codes; paused 21 Sept 2026 (workable): decrypt working, E/X/a+ signs to settle.
- R9413 clean reading - blocker: open-codes; paused 21 Sept 2026 (workable): all pages transcribed and decoded (`r9413/decrypt.txt`); sign Z and A unassigned.
- R9409/R9410/R9427 clean readings - blocker: open-codes; paused 21 Sept 2026 (workable): R9410 look-alikes split on the image (`sysA/r9410_split.md`: d = l vs K word sign; # = g vs U = u/v; n = b/w one sign) and re-decoded (`sysA/r9410_v2_decrypt.txt`: "…vertragen … behandlung … kunig von Frankreich also gehandelt nit so vil als vor…"); same split still to apply to R9408/R9409/R9413/R9427; K's meaning (Kaiser/Kunig?) open.
- R9416 f.263 clean reading - blocker: open-codes; paused 21 Sept 2026 (workable): v2 re-keyed (Pressburg talks read throughout); one sign serves ch but the annealer gives it s ("auss"=auch) — needs a digraph value set by hand.
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

## Steps

- 2026-09-21: record list from the DECODE dump (141 records in KAA 4591: 102 keys, 39 ciphertexts); images of the
  14 targets and 30 neighbouring keys fetched with the cookie.
- Matched R9325 to key R9324 by the null signs (identical set); applied key, all words Latin; read.
