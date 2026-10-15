# The cardinal de Mâcon in Rome to Montmorency, 1536-37, in Mascon's cipher (BnF fr. 3053, DECODE R4233-R4247; BnF fr. 3071 no. 4)

**Split on 14 Oct 2026** under the one-key rule (George Lasry): this entry holds every letter read in
**Mascon's cipher**. Two changes: (1) R4248 (fr. 3053 f. 85), in a second, unrelated fr. 3053 cipher and read from
its contemporary decipherment on f. 86, is now its own entry, `targets/r4248/` (`docs/r4248.html`), a different
cipher with its own page; `R4248.md` moved there. (2) The cardinal's letter of 11 April 1537 (BnF fr. 3071 no. 4),
read on 18 Sept 2026 under `targets/gramont1529/` (catalogue item 6), is in the same key and moved here:
`fr3071_no4/` (reading files and aliases), with the working table `macon_key.md`, the decoder `macon_decode.py` and
the key images `keyimg/` (Lasry's fr. 3071 f. 9 table, Tomokiyo's fr. 3053 tables). The other item-6 letters are
different ciphers with their own pages (`gramont1529`, `langeac1529`, `gramont1530`). The sections below that
speak of "eight records" describe the 21-22 Sept work before the split.

Catalogue item 180 ("Unknown sender (Rome) to Anne de Montmorency, 8 ciphertexts", class A). Session of
21 September 2026. Everything below is unvalidated until Daniel reviews it; the evidence for each claim is named.

## Outcome in one paragraph

The "unknown sender" is **Charles Hémard de Denonville, bishop and (from December 1536) cardinal of Mâcon**,
French ambassador to Paul III: three of the eight records are signed "Charles e. de Mascon" or "E. Card[ina]l de
Mascon" in the clear. The cipher is **"Mascon's cipher"**, reconstructed from this very volume by S. Tomokiyo and
re-tabulated by G. Lasry in 2023; the repository had already applied it (then under `targets/gramont1529/`, now
`fr3071_no4/` here) to Mâcon's letter of 11 April 1537 in fr. 3071. Neither Tomokiyo nor Lasry, and no edition found, gives any plaintext, so the task was
reading, not cryptanalysis. **Seven of the eight records are read in part and one (R4248) is resolved**: its
cipher is not Mâcon's at all but a second fr. 3053 cipher, and the volume itself carries a contemporary clear
decipherment of it on the next leaf (f. 86). Two records are read nearly throughout (R4240 ~85 %, R4247 letter 1
~80 %); four more are read in long stretches (R4233 ~60 %, R4235, R4238 ~65 %, R4239 in passages); the very long
February 1537 letter R4234 (almost wholly in cipher) is now read throughout: 66 lines in the first pass and about
90 more (P8-P20) in a third pass the same day, at about 80 %. The third pass also read R4235 P2-P3 and passage D
(29 + 5 lines), R4247 letter 2 (27 lines, the last six in fragments) and the hundred unread lines of R4239: every
cipher passage in the eight records has now been deciphered at least in part. Six contemporary
marginal or interlinear decipherments found in the volume were used as calibration anchors, and three of them
agree with the independent decoding word for word.

## Prior art (checked 21 Sept 2026)

* **S. Tomokiyo, "French Ciphers during the Reign of Francis I"** (cryptiana.web.fc2.com/code/francis.htm),
  section "BnF fr.3053 (1535-1537)": identifies the volume as letters of the bishop/cardinal of Mâcon, ambassador
  in Rome, to Montmorency, and gives his reconstruction of the cipher (tables copied at
  `keyimg/francisMacon.png`; his second table is `targets/r4248/img/francisMacon2.png`). He notes that f. 67 is from "messrs de Roudez et Lavaur" in Venice to
  Mâcon (= DECODE R4245), and that **one fragment on f. 85 uses a different cipher, "deciphered on f. 86"** —
  confirmed here for R4248. **No plaintext is published.**
* **G. Lasry**, table dated 05/11/2023 for BnF fr. 3071 f. 9 ("Mascon's cipher"), on Tomokiyo's GL.htm; used in
  `macon_key.md` (built 18 Sept 2026 under gramont1529). Keys only, no plaintext. Lasry also decoded the fr. 3071 no. 4
  letter in 2023 (unpublished, his note of 21 Sept 2026); no decipherment of his of the fr. 3053 letters is recorded.
* **DECODE** R4233-R4248, uploaded 2023, are marked "Partially decrypted" / "Decrypted" / "Non-decrypted". No
  transcription or plaintext file is attached to any of the sixteen records; the "Decrypted" marking refers to the
  cipher system being known, not to a text.
* **Editions searched, nothing found**: the letters of this embassy are not in the Dodieu edition table
  (rom.uga.edu, "Lettres et documents de Claude Dodieu 1527-1557", which prints the neighbouring Rome/Naples
  correspondence of 1535-36), and no printed decipherment of fr. 3053 turned up.

## Pass 5 (22 Sept 2026): shape-true re-transcription, about 95 % read

The residue after the third pass was not in the cipher but in the transcription: the readers' one alias `ǂ` covered
four or five distinct key signs (long hooked f = O, £ with looped foot = U/V, two-bar stroke = P, looped p-top = F,
crossbar q = M), and the Q sign before £ had been written as Δ. A clustering pass (`pass5/cluster_REPORT.md`) showed
it; a pilot (`pass5/pilot.md`) cut the character error rate on lines with a contemporary decipherment from 9.2 % to
5.8 %. Every record was then re-transcribed sign by sign from the **Gallica native scans of fr. 3053**
(ark btv1b90601432; view map in `pass5/gallica_views.md`), line baselines straightened, decoded by the key map and a
5-gram beam under `fr-1600-letters` (`pass5/shapedec.py`), and checked against every contemporary clear text.

| record | before | pass 5 | measured against |
|---|---|---|---|
| R4233 | ~60 % | ~95 % (1,904/2,006 letters) | four glosses: CER 8.3 % LM, ~2 % at sign level |
| R4234 | ~75 % | ~94 % (5,369 letters) | P15 clear copy + f18v margin: CER 6.5 %; glossed lines 5.6 % |
| R4235 | ~45 % | ~96.5 % (2,035/2,108) | P6 clear copy, P10/P11 margins, interlinear: CER 6.4 % (~0.5 % sign misreads) |
| R4238 | ~65 % | ~94 % (767/812) | one interlinear gloss (agrees) |
| R4239 | ~75 % | ~94 % (4,925 letters) | **ff. 37r-v are a contemporary clear copy of letter 2 (f36r L07-f38r L14)**: CER 6.1 %; f38v interlinear 3.1 % |
| R4240 | ~85 % | ~98.5 % (829/842) | margin gloss: CER 3.8 % |
| R4247 | ~78 % | ~98 % (letter 1 2,315/2,356; letter 2 783/784) | none; letter 2's "faded" tail is sharp on the Gallica scan |
| R4248 | resolved | resolved | f. 86 decipherment |

Most of the remaining CER against clear copies is spelling variation between the cipher and the copy (pappe/pape,
Loys/Luis, "roy" vs "le Roy"), not misreading. **Nothing in any record is physically unreadable on the Gallica native
scans**; the earlier "faded" lines were an artefact of the DECODE crops.

New readings (details in `pass5/R<rec>_pass5.md`): R4234 names Stefano Colonna for the foot and Giovanni Battista
Savelli for the horse, 20,000 + 10,000 + 10,000 écus, the marriages of Pier Luigi's son to duke Alessandro's widow
and of his daughter to Cosimo de' Medici; the bishop "de Lodes" is **Lodi** (the see Simonetta held from 1536), not
Rodez as first read; R4240 names the auditor sent to the Germans "Vuors[t]" (Peter van der Vorst, identification
ours); R4247 letter 1 gains a whole line missed before ("l'inimitié qu'il avoit avec le dict Dorie") and its end
(the bishop of Lodi, Verulan, Milan to be deposited with the pope, the nephews as kings of Naples and Sicily);
letter 2 ends "il seroit icy fort difficille de recouvrer gens de cheval ne artillerie; bien trouverroit on tant de
gens de pied, et bons, qu'on vouldroit, et beaucoup de gentilz homes forussiz"; R4235 passage D ends "ledict Vitelle
… il n'est pas pour porter le faiz, n'ayant aussi moien de recouvrer argent"; R4233 "Le bonhomme se porte bien,
mais il est septuagenaire et plus"; R4238 the German gentleman's quarrel "avec ung des plus grandz de sa court".
A companion letter to the King of 15 Feb 1537 with its contemporary decipherment (BnF Dupuy 44, ff. 30-38) was
transcribed as a content crib (`pass5/dupuy44_*.md`); it confirmed "Vitelle" and "calomnie du Turc".

## The records and what was read

Images: DECODE serves the fr. 3053 scans as horizontal page-crops; they are **not in the public domain** (BnF) and
are git-ignored here (`targets/rome1536/img/`). Per-record readings, line by line, are in `R4233.md`, `R4234.md`,
`R4235.md`, `R4238.md`, `R4239.md` (P2-P15), `R4239b.md` (P16-P30), `R4240.md`, `R4247.md`, `R4248.md` (now in targets/r4248/); third pass: `R4234_P8-P12.md`,
`R4234_P10.md`, `R4234_P15-P20.md`, `R4235_P2-P3.md`, `R4235_P8D.md`, `R4239_pass3.md`, `R4247_letter2.md`.

| record | leaf | date, place | cipher | read |
|---|---|---|---|---|
| R4233 | f. 6 | Rome, 26 Jan 1536 o.s. (= 1537) | ~70 lines in 9 passages | ~60 %, 4 glosses used |
| R4234 | f. 16 | Rome, Feb 1536 o.s. (= 1537) | ~155 lines, nearly the whole letter | all: P2-P6 ~70 %, P8-P12 ~80 %, P16-P20 ~80 % |
| R4235 | f. 21 | Rome, 15 Feb 1536 o.s. (= 1537) | ~60 lines | P2-P3 (29 lines) ~80 %, passage D ~92 % (clear copy on P6), glossed lines |
| R4238 | f. 32 | Rome, [.] Sept 1536 | ~26 lines in 3 passages | ~65 % |
| R4239 | f. 35 | Rome, 6 Apr 1537 (two letters + postscript) | ~160 lines | all passages; P3-P15 third pass ~72 % |
| R4240 | f. 40 | Orvieto, 2 Sept 1536 | 26 lines | ~85 %, 2 glosses |
| R4247 | f. 77 | Orvieto, 1 Sept 1536 (two letters) | ~57 + ~26 lines | letter 1 ~80 %; letter 2 ~75 % (last 6 lines fragments) |
| R4248 | f. 85 | 1536, no date on the crops | ~20 lines, **a different cipher** | resolved by the f. 86 decipherment |

## What the letters say

* **R4240 (Orvieto, 2 Sept 1536), the general council.** Mâcon has learned "de bon lieu" that Vergerio, nuncio
  under Clement VII and kept on by Paul III, carried word from Ferdinand to the Germans that the pope and the
  College agreed they might come to the council and there "dire et faire ainsi qu'ils seroient inspirez par le
  Sainct Esperit"; on that they resolved to attend, hoping for a decisive peace. The pope, judging this "la totale
  ruine de l'Eglise et sainct siege apostolique", has sent an auditor to summon them on the old law and custom
  instead. The Germans, Mâcon hears, will not consent: they say the morals of pope, cardinals and bishops must be
  reformed, which cannot be done without them. "Je vous laisse a penser sur cela, monseigneur, que ce sera de
  l'assemblee dudict concille" — the last words glossed in the margin by a contemporary, exactly as read here.
* **R4247 letter 1 (Orvieto, early Sept 1536), Andrea Doria and Milan.** Doria had written to the conte
  dell'Anguillara to hold his galleys ready to join his own. Since Antonio Doria had taken one of Anguillara's
  fustas, and Anguillara's galleys are in the pope's service, Mâcon inferred a reconciliation made at the pope's
  command and so a secret treaty with the Emperor, and put it to Paul III. The pope answered that Anguillara had
  indeed shown him the letter, that he marvelled at it, that he did not believe Doria content with him — he had
  made him pay for three months for his three galleys and pay for the dispensation for his wife's son to marry
  Antonio de Leyva's second daughter — and that he knew nothing of the cause. In a second block a man sent by
  cardinal Ennio Filonardi of Veroli sounds Mâcon out on whether the King would consent to Milan passing from the
  Emperor to Pier Luigi Farnese's son, or to the young Sforza; Mâcon answers that neither the King nor his sons
  will ever consent, and that while the crown of France reigns Milan will not go into other hands than its own,
  "estant leur vray heritage" — so it is time lost for the pope.
* **R4238 (Rome, Sept 1536), Siena and a German offer.** The bearer is sent by the Sienese exiles to press the King
  to an enterprise against Siena; Mâcon sees no prospect in it but did not stop the journey, and fears that if the
  exiles are left to themselves they will go over to duke Alessandro de' Medici, who is working to win them and
  "s'impatroniser de l'estat du dict Siennes". A German at Rome, claiming to be of Ferdinand's chamber and to know
  his secrets, gives him letters for a lansquenet captain with count Wilhelm von Fürstenberg and offers to enter
  the King's service; Mâcon suggests having the letters translated in Paris before delivery.
* **R4233 (Rome, 26 Jan 1537), the Farnese marriages and a conclave.** Pourparlers on marriages for Pier Luigi
  Farnese's children, with cardinal Trivulzio's view on stopping them; the imperial ambassador and Venice;
  cardinals Trani, Cesi and Pisani. If the French cardinals were in Rome they could steer a conclave "si quelque
  inconvenient survenoit au pape, que Dieu ne veuille" — he is "septuagenaire et plus" and failing. The King has
  done no favour yet to any of the pope's servants, so little goodwill can be expected. The pope is sending
  cardinal Verulano's secretary, "ung tres mauvais garson", to Switzerland, and means to take the legation of
  Parma and Piacenza from Salviati for Verulano; Mâcon suspects "quelque dessaing sur le duché de Millan". The
  French captains in Piedmont quarrel among themselves, Guido Rangone among them, and grain is nearly gone.
* **R4235 (Rome, 15 Feb 1537), a marriage used as currency.** "J'ay sceu de bon lieu que le dict pape vouloit
  entretenir le Roy de mariage, et ayant de ce dudict seigneur bonnes paroles, pour ce s'en prevaloir vers le dict
  Empereur, pour parvenir a son intendit." He begs Montmorency to speak of it to no one but the King, and to keep
  the secret of the envoys' charge, above all from the bishop of Verona (Giberti), reckoned more devoted to the
  King than to the Emperor. The three contemporary decipherments in the margins of these leaves agree with the
  independent reading word for word.
* **R4239 (Rome, 6 Apr 1537), Ottavio Farnese, Florence, and an estate in France.** The pope speaks of the marriage
  of his grandson Ottavio to the Emperor's daughter Margaret, and insists on neutrality while pressing for peace.
  A glossed line opens the Florentine passage — "quant au faict de florence" — on the intrigues at Rome of the
  exile cardinals Salviati and Ridolfi in the months after Alessandro de' Medici's murder. The heart of the letter
  is a bid for Pier Luigi Farnese: the Imperialists have offered him the investiture of Novara, and Mâcon counters
  with "quelque honneste estat en France", arguing from the pope's age and from Pier Luigi's need of an "occasion
  d'en eschapper" once his father is dead; Pier Luigi will say neither yes nor no without the pope's and the King's
  consent. The clear text around it reports a spy set on Salviati's household, the Bohemian grant to the King of
  the Romans against the Turk, a Lutheran diet in Saxony, and the death of the marquis of Saluzzo and count
  Philippe Torniello by arquebus before Carmagnola in Holy Week.
* **R4234 (Rome, Feb 1537), the bishop of Lodi, the Farnese marriages and Pier Luigi's army.** Read for its first four pages.
  Soundings on a settlement: someone is pressed to come to terms rather than declare himself an enemy; the pope
  means to wrong him through an intermediary and to bring the King to consent; cardinal Cesarini writes in the same
  sense; the bishop "de Lodes" — Lodi, then at Venice, whose see had passed to Cardinal Simonetta (first read as Rodez; corrected in pass 5) holds that the King
  should never consent, and the Venetians are wanted in the business. Cardinal Pisani reports on taking leave of
  the pope and on men "fort prochains et familiers" of Pier Luigi Farnese. A seigneur who got nothing from the
  pope's last distribution of benefices now despairs of the Emperor; Mâcon has cultivated him since arriving to
  draw things out of him, and asks that the King take him and his brother into service. Then the marriages of Pier
  Luigi's sons and the match of his house with Cosimo de' Medici, "sworn several times over"; and the arming: so
  many thousand escuz paid at Pier Luigi's departure from Rome, two thousand more assigned at Parma and Piacenza,
  and a levy of six thousand Italians, five thousand Swiss, five hundred light horse and a hundred men-at-arms,
  the horse under "Jehan Ba[p]tiste".
* **R4248 (f. 85), the second cipher, read at the time.** The glyph set is not Mâcon's (it matches Tomokiyo's
  second fr. 3053 table) and Mâcon's key gives nonsense. f. 86 is a **full contemporary clear decipherment** of the
  passage and agrees with every clear connecting phrase on f. 85. The writer, after a day in the country with
  "monsieur le cardinal Carafe(?)", urged him that everything, above all the conduct of the war, should pass
  through Montmorency's hands and that anything else was "fumee et vent"; the cardinal seemed persuaded, and added
  that the cardinal of Lorraine, in his capitulation with the pope, had conceded things "never thought of before",
  which they meant to undo, leaving the whole matter to Montmorency.

### Third pass (21 Sept 2026): the pages left unread

* **R4234 P8-P12** (~58 lines, ~80 %): Pier Luigi Farnese's horse under Giovanni Battista Savelli ready this month,
  foot by March; a Sienese servant of Pier Luigi says the troops, kept in Parma and Piacenza, are to garrison the
  Milanese fortresses if the Farnese marriages persuade the Emperor to sell Pier Luigi the duchy of Milan; the pope
  "qui est fin" will feign neutrality. Mâcon suspects a plant by the Imperialist cardinals Veroli and "Cesane", yet
  the pope's own admissions give "grant presumption". Contarini, "imperial pour la vie", is now the pope's familiar.
* **R4234 P16-P20** (~30 lines, ~80 %; P15 is a clear copy of P16, glosses and a margin decipherment on P19-P20):
  messire Ambroise is wholly Imperial and "corruptible plus que tous les hommes que je congnoisse"; Mâcon fears the
  King's new demand for three tenths on the clergy, with the three levied last year without papal leave and the
  "calomnie du Turc", will let the pope declare against the King; asks for a ciphered royal letter to show; the
  bishop of Lodi at Venice wants his see back from Cardinal Simonetta; Andrea Doria's letters to the count of
  Anguillara, and Doria's talk of Spain a feint.
* **R4235 P2-P3** (29 lines, ~80 %): the pope seeks the Milanese fortresses, claiming the King's side proposed it;
  do not drive the pope to despair; Pier Luigi's journey to Parma was at the Emperor's request brought by messire
  Ambrogio from Provence; the Emperor shows willing to give his natural daughter to Pier Luigi's son but not Milan
  as dowry. **Passage D** (P8, ~92 %, contemporary clear copy on P6): "si le Roy est fort en Italie du costé de
  Lombardie, facillement ledict estat de Florence se pourra reduire en l'ancienne liberté et devotion dudict
  seigneur Roy…".
* **R4247 letter 2** (Orvieto, 1 Sept 1536; 27 lines, ~75 %): the count of Pitigliano, now in the King's service,
  advises that if the Emperor winters in Milan the King should strike at Naples, discontented and with no strong
  places but the coast; Sicily would revolt with little help; the last six lines (artillery…) are fragments.
* **R4239 P3-P15** (100 lines, ~72 %): the pope would use the Milan question and the Turk to leave neutrality;
  Ridolfi's envoy Albizzi hears from the duke of Urbino of close dealings between pope and Emperor (tenths and
  crusade taxes, a league of Italian princes); Mâcon asks for a ciphered article to show the pope "afin que si la
  raison et l'honnesteté ne le desmeuvent … que la peur l'en peust divertir"; the Novara offer to Pier Luigi, made
  "par [le] commandement" of the pope, whom Pier Luigi told Mâcon in the antechamber, "sans accepter ne refuser",
  not to write to the King.

## The cipher

Homophonic substitution, one glyph per letter, with doubled-letter signs, nulls and three code numbers
(`20` = l'Empereur, `30` = pape, `40` = roy — no other number occurs anywhere in the eight records). The working
table is `macon_key.md`, decoded with `macon_decode.py` (both moved here from targets/gramont1529/ on 14 Oct 2026). Corrections established here from
glossed lines, and not in the published tables:

* The big curly X (ꭓ) is **Q and U**, not N (proved by the glossed `ꭓ£+7G 8ꭓ ǂ3Δ4G 5o ǂ10D27o74g` = "quant au
  faict de florence"); `Δ` serves I **and** Q, and the QUE group is written `ꭓǂg` / `Δ£g` / `Δǂg` indifferently.
* The plain saltire `×` is **N as well as L**; `4` is C, R and (where the compact "27" R-sign is written) T.
* `Ξ` (triple bar on a stem) is RR, proved by PIE-RR-E (Pier Luigi, three times); `∩` is P nearly everywhere but
  F/FF in *affaire*, *frere*, *faire*.
* `7` is N, R **and B**; `5` carries G as well as D; `ω` = PP and the hooked `ʃ` = H (both in *eschapper*);
  `Ξ` is a doubler (SS in *dessuz*, RR in *pourroit*); `ᴖ` = S; `Ω` = X; `ꝏ/∞` = S; `☐` = LL.
* The barred-cross family (`ǂ`, `£`, long `ƒ`) is the main obstacle: within one line it reads F, P, O, U, V and D,
  and is separable only by context. This, not the cryptanalysis, is what limits the readings to 55-85 %.
* The dotted small r alternates between R and a null; in one place it stands for X (*Alexandre*).
* An unexplained `·52` before MANDE at the head of R4239 P30 was left untranslated by the contemporary glossator
  too, and is probably a null pair.

## Open

* All cipher passages are now deciphered at least in part. What remains is residue: doubtful groups inside read
  lines (R4239 P3 ll. 3, 10, 12; P11 ll. 1-2, 10; P14 ll. 7, 10-11, 14), R4247 letter 2 ll. 22-27 (fragments:
  *artillerie*, {20}), R4234 P16 L6 and L15-16, P19 C3-C4, and several names (Cesane, Palmier, the Sienese
  gentleman, Ambroise's surname).
* R4248 (the f. 85 cipher) is now `targets/r4248/`.
* DECODE's full-page .jpeg views (R4234 P1, P4, P7, P10, P13, P14, P18) are lower-resolution duplicates of the
  crops; P14 is the inserted clear slip cropped as P15. No page of R4234 is missing.

## Method and files

`AGENT_BRIEF.md` is the brief given to the reading agents (one or two per record, ≤ 2 at a time). Each `R<rec>.md`
holds, per cipher line, the glyph aliases, the machine decoding and a word-divided reading, then a running reading
and per-letter confidence. Crops are made from the DECODE page-crops with PIL at 1:1 or 1.5x; `work_<rec>/` folders
and `img/` are git-ignored (BnF rights).

## The letter of 11 April 1537 (fr. 3071 no. 4), moved here 14 Oct 2026

BnF fr. 3071 no. 4, ff. 9-10 (Gallica btv1b9060315f, canvases 16-19; slip f. 9bis = canvas 18). Charles Hémard de
Denonville, cardinal de Mâcon, Rome, to Montmorency. Files: `fr3071_no4/fr3071_no4_macon.md` (first pass and the
f. 9r ll. 3-25 reading), `fr3071_no4/macon_9r_26-34.md` (~175 of ~190 signs), `fr3071_no4/macon_9v.md` (ll. 1-16,
~463 signs, all decoded), aliases in `fr3071_no4/aliases/`. Read apart from short spots on f. 9r; the clear text,
in a fast secretary hand, is transcribed only loosely. Codes 20 = Empereur, 30 = pape, 40 = roy (first identified
here). The Farnese marriage offer (Vittoria Farnese to Cosimo de' Medici) and Paul III's threat, relayed through
Latino Giovenale, to declare for the Emperor if it is refused; Pier Luigi Farnese and Novara; the King's Turkish
alliance "se verifie clerement"; Venice expected to follow the Pope; the King "s'amuse en Picardie"; the Venice
ambassadors working on Alessandro Vitelli. **The slip f. 9bis is a contemporary decipherment of the f. 9v passage**,
and the reading, made first, matches it almost word for word.

## Remaining gaps
- fr. 3071 no. 4: seven signs on f. 9r ll. 27-28, the word before *puissance*, the name group on f. 9r l. 8; the clear text read loosely - blocker: illegible; blot and odd signs on the Gallica scan, and the slip f. 9bis covers f. 9v only
- residue inside read lines, about 5 % of letters (R4233 passages 3, 4, 5, 7, 8, 9 ~100 letters; R4234 f16r L1/L3/L16/L24, f16v L2-3/L7/L9/L21/L27, f17r L4-5/L21/L23/L27/L30-31, f17v L14/L20, f18r L15-17; R4235 P7 L5 and two signs in passage B; R4238 ~45 letters; R4239 f35r L06/L24/L32, f35v L08; R4240 13 letters; R4247 ~40 letters) - blocker: illegible; ink legible on the Gallica native scans, but the sign runs are ambiguous (7 = N/B, 4 = C/R, Of/Up) and no clear copy or gloss covers them
- R4239 short cipher runs in f36r L01-L06 and f35v L27-L31, and f38v L4 end, L8 end and the margin block (whose interlinear does not fit the signs) - blocker: illegible; not transcribed or not resolved in pass 5, no clear copy for them
- proper names (the Sienese gentleman "For[?]", the count "Mer[?]le", Christofle's surname and two German captains in R4238, "Cesane", "Palmier") - blocker: open-codes; spelled in cipher but the letters do not settle to a known name
- R4239 f38r L06-L07 - blocker: illegible; doubtful in the contemporary clear copy itself

## Escalation
- [x] siblings: R4236, R4237, R4241-R4246 opened via the DECODE API: all status Decrypted, no transcription or plaintext file attached (six Rome letters to Montmorency 1535-37, one to Mâcon from Venice); outside catalogue 180 and left for a later session; every full-page view of R4234 opened (P10/P13/P14/P18 duplicate the crops; P14 = P15 clear slip used as crib)
- [x] clear-pages: f. 86 decipherment of f. 85; R4234 P15 (f. 18bis) and R4235 P6 clear copies; R4239 ff. 37r-v clear copy of letter 2 (found in pass 5); margins and interlinears; Dupuy 44 companion letter to the King with its decipherment
- [x] known-keys: Mascon's cipher (Tomokiyo; Lasry 2023, macon_key.md); Tomokiyo's Cipher-3 table (keyimg/francisMacon3.png) not this key
- [x] print: Tomokiyo francis.htm, Lasry GL.htm, Dodieu edition (rom.uga.edu): no plaintext
- [x] key-rebuild: key corrections from glossed lines (ꭓ = Q/U, × = N/L, Ξ = RR, 7 = N/R/B, etc.)
- [x] retry: pass 5 (22 Sept) re-transcribed every record by sign shape from the Gallica native scans and re-decoded with the key map + fr-1600-letters beam; every doubtful group retried and regraded against all contemporary clear texts

## Assumptions for George's review

- His Mascon's-cipher credit (table of 05/11/2023 for fr. 3071 f. 9) is applied to the seven fr. 3053 records on the
  identification, made by Tomokiyo and repeated here, that his fr. 3071 f. 9 table and Tomokiyo's fr. 3053
  reconstruction are the same key; the readings agree with the contemporary glosses in both volumes.
- His prior-solution credit covers the fr. 3071 no. 4 letter only (his 21 Sept 2026 note on the four item-6 letters);
  no decipherment of his of the fr. 3053 records is known.
- No Lasry credit on R4248 (now `r4248`).
