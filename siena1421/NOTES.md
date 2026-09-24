# Siena, Concistoro 2308: "Lettere in cifra" (catalogue 336)

Status: in progress

Session of 24 September 2026. Goal set by Daniel: decipher the 29 cipher letters of ASSi Concistoro 2308, fasc. 2
("Lettere in cifra"), oldest dated 1421 per Meister 1902 pp. 50-51, "solo parzialmente decifrate" per the 1952
inventory; first try the filed keys (fasc. 1) on every letter.

## Access: the whole filza is on DECODE (found this session)

The 23 Sept scan (`oldest/scan_2026-09-23/italy.md`) had only the Yale Ilardi reel 1503 (13 key frames). DECODE
holds the whole busta, photographed in the ASSi reading room (owner 32, created 2020-11-24 and 2023):

- **R4746-R4789 = fasc. 1 "Cifrari"** (cover "Concistoro 2308, Fasc. 1, Pezzi 46", divider sheets "Secolo XV" /
  "Secolo XVI"), DECODE names `Concistoro_2308_01` ... `_43`, record type key (R4787 = type 3, 10 pp.). R4761 is
  not Siena (a Kurtz 1639 record in the id gap); R4783 has no image.
- **R4790-R4814 = fasc. 2 "Lettere in cifra"** (cover "Concistoro 2308, Fasc. 2, Pezzi 25" on R4790 p. 3),
  DECODE names `Concistoro_2308_44` ... `_68`, all dated "1500-1599" (a placeholder), status N/A, no transcription
  or decryption attached.
- **R1858 "Siena keys and ciphers"** (8 pp., status "Decrypted" but no document attached): photos of key sheets
  (the 1454 Milan key, "Cifra cum frate Bernardino", the 1475 key, R4747's slips) and a second photo of no. 12.

Images downloaded with the DECODE cookie to `decode/img/` (git-ignored; ASSi images, not public domain).
Metadata in `decode/views.jsonl`. 1600-px previews in `img_small/` (git-ignored).

## Inventory of fasc. 2 (pencil numbers = Meister's numbering)

Meister's dated anchors hold: no. 4 = 1456, no. 11 = 1478, no. 17 = 1528. So the pencil numbers on the pieces are
the numbering Meister saw in 1902.

| no. | DECODE | what it is |
|---|---|---|
| 1 | - | **not in the fascicle as photographed** (Meister: dated 1421) |
| 2 | - | not photographed |
| 3 | R4792 | clear private letter, "Charissimo compare mio ... Simone nostro", Siena 1 April (no year); no cipher seen |
| 4 | R4793 | Galgano Borghesi, J.U. doctor and orator, Naples 12 May 1456 (Senatore 2009: "Concistoro 2308, c. 4, da Napoli, 12 maggio"), to Leonardo Benvoglienti; cipher runs in capital letters, a few interlinear glosses |
| 5 | R4791 | clear private letter to "Maffeo da Siena", pencil "1460?"; no cipher seen |
| 6 | R4795 | letter to the Magnifici domini, clear salutation then ~20 lines all cipher (Latin-letter-like signs, no word division) |
| 7 | R4796 | long despatch (2 pp.), cipher block of ~10 lines near the end |
| 8 | R4797 | cipher slip (5 lines, a few glosses) + a clear decipherment on the same sheet (Papa Felice, Duca di Milano, Leonello d'Este: c. 1440-47) |
| 9 | R4798 | slip, two short cipher runs in clear text |
| 10 | R4799 | slip, one cipher run glossed "presura di Montepulciano" |
| 11 | R4800 | Donato Acciaiuoli to Lorenzo de' Medici, Rome 13 June 1478 (a Florentine letter held in Siena); two cipher blocks |
| 12 | R4790 (+R1858 p. 7) | whole letter in graphic signs with word separators, ~22 lines + 2-line subscription |
| 13 | R4801 | slip in digits and signs with clear phrases; **its decipherment is no. 16** |
| 14 | R4802 | whole page in cipher, word-separated, to the Priors and Capitano del Popolo of Siena; dorsal list of names |
| 15 | R4803 | 8 pp., Sienese orator at the imperial court, 29 Dec 1546 / Jan 1547 (Schmalkaldic war); short capital-letter cipher runs |
| 16 | R4804 | clear decipherment of no. 13 |
| 17 | R4805 | 20 Aug 1528, to Bartolomeo Tantucci?, docketed "questa cifra è quella di Balìa"; cipher runs of digits/signs |
| 18 | R4806 | Latin treaty articles (petitions of Siena, a king's secretary Niccolò), cipher words throughout (4 pp.) |
| 19 | R4807 | letter to the Magnifici domini, cipher runs |
| 20 | R4808 | "Sacra Regia Maiestas, Serenissime princeps", whole letter in cipher |
| 21 | R4809 | short letter with cipher runs |
| 22-23 | R4810 | clear drafts with numbers as code words (mentions Calixtus III: 1455-58) |
| 23 | R4811 | whole page in cipher |
| 24 | R4812 | whole letter in cipher (2 pp.) |
| 25 | R4813 | slip, all cipher |
| 29 | R4814 | fragment, a few words |
| ? | R4794 | slip, 6 lines all cipher, no number found (erased pencil "4"/"5") |

Nos. 1, 2, 26, 27, 28 are not among the 25 pieces photographed. The fascicle cover says 25 pieces; Meister counted 29.

## Key index (fasc. 1), as read from the images this session

| DECODE | heading / identification | date |
|---|---|---|
| R4746 | alphabet + Duca di Milano, Serenissimus, Niccolò Fortebraccio; "Dns Antonius ... 1433" (Meister's "Siena Beispiele 1") | 1433 |
| R4747 | three small slips (pencil 2, 3, 4/5): a 20-cell number table of words; **slip 3 = signs for whole phrases about "Tartaglia"** (the condottiere Angelo Tartaglia, executed Feb 1421), so c. 1419-21, contemporary with the lost no. 1; slip 4 "Cu Leonardo" (Senesi, Fiorentini, S. Rinaldo, Paola, Gente d'arme, Genovesi, Re d'Aragona, Papa, Denari) | c. 1420 |
| R4748 | "Cifra cum fratre Bernardino": Papa, Duca di Milano, Niccolò Piccinino, Fiorentini, Conte Francesco, Re d'Aragona, Veneziani, Bolognesi, Sanesi, Conte d'Urbino, Antipapa Felice | 1439-44 |
| R4749 | "Cifra con ... Antonio et con Francesco ...": Aluise dal Verme, Sacramoro, Niccolò and Francesco Piccinino, Obizo, Papa Felice | c. 1440-44 |
| R4750 | "a messer Leonardo e messer Antonio, ambasciatori a Milano, 1454"; Latin-word nomenclator (Rex Aragonum gallus, ambasciatore fiorentino storpsi ...) | 1454 |
| R4751 | "Cifra mandata a Lodovico di Salimbene potestà di Casole" (Senenses Stella, Casole Felix ...) | 1450s |
| R4752 | "Cifra de m. Antonio Bichi 1478 Rom." | 1478 |
| R4753 | Latin nomenclator, vowels in capital-letter groups (Imperator 62, Papa 84 ... Imperatrix 20, Rex Portugalie 66) | c. 1452 |
| R4754 | "Cifra data a ... Antonio Petrucci" (Latin code words: florenus, Culmen, Ventus ...) | 1450s |
| R4755 | "Cifra cum Christofano ..." (Papa, Fiorentini, Veneziani, Duca di Milano, Niccolò Piccinino, Conte Francesco, Lucca, Pisa, Pistoia, Siena ...) | c. 1440 |
| R4756 | "Lucensibus": Papa, Cardinales, Rex Aragonum, Dux Calabrie, Dux Mediolani, Florentini, Marchio Ferrarie, Senenses, Lucenses, Comes Jacobus Piccininus, Dominus Sigismundus | 1450s |
| R4757 | "Data domino ... Venetiis" | 15th c. |
| R4758 | "Cu d(omi)no Antonio de Petrucciis" (Senesi = papa, Fiorentini = dux, S. di Piombino = Rex, Balduccio = mons) | 15th c. |
| R4759 | "cu ipso magistro ..." Papa, Duca Valentino, Re de' Romani, Re di Francia, Pandolfo | c. 1500-03 |
| R4760 | "Cifra con m. ..." 1536 | 1536 |
| R4762 | "Data a Luca di Niccolò mandato a Napoli ambasciadore" (Conte Everso, Conte Jacomo, Pitigliano, Patriarcha, Orsino ...) | c. 1455-58 |
| R4763 | long nomenclator (Lombardia 12 ... ; Alessandro Sforza, Corrado da Fogliano ...) | 1450s-60s |
| R4764 | "Cifra con m. Bernardino Buoninsegni oratore a S. M.tà" | 16th c. |
| R4765 | Spagna, Imperador, Re di Francia, Re d'Inghilterra ... | 16th c. |
| R4767 | "Cifra con m. Aglo Venturi" (nulls = the numbers 1-40) | 16th c. |
| R4768 | "Cifra di m. Mercanto ... oratore" | 16th c. |
| R4770 | Papa, Re di Francia, Re di Napoli, Maximiliano, Roano, Ligni, Valentinois, Ascanio, Montepulciano, Ponte a Valiano | c. 1499-1500 |
| R4771, R4781 | "Fano": Papa A ... Duca di Ferrara I, Giovanni Bentivoglio, Franciosi, Mons. di Trans, Roccabertino | c. 1500 |
| R4772 | "D. Mattheus Marinus doctor ... Io. de Gonzaga" | c. 1500 |
| R4773 | "Cifra con Girolamo Tosta" (all-numeric; Duca di Castro, Balìa) | 1540s |
| R4775 | Letter-key "die 4 augusti 1502" | 1502 |
| R4776 | syllabic table, "cifra con ... Donna ..." | 16th c. |
| R4778 | numeric nomenclator (Papa 33 ... Senesi 53, Re Federico 58) | c. 1500 |
| R4779 | "Cifra Giusti" (Papa 2 ... Siena 29) | c. 1500 |
| R4780 | "Capitano ... Pandolfo" (Bolognesi Sinagoga, Fiorentini Hebreus) | c. 1500 |
| R4782 | Papa, Re di Francia ... Bologna, Pisa, Giovanni Bentivoglio, Mons. di Legni, Leonardo Bellanti, Card. di Siena, Trocces, Card. di Capua | c. 1500-03 |
| R4785, R4786 | 16th-c. code books (Latin cover words), "Cifra con la Cesarea M.tà, Rep. Senese" | 16th c. |
| R4787 | titles book 1496 (not a key) | 1496 |
| R4788 | genealogy + numeric columns | ? |
| R4789 | alphabet + nulls + duplicates | ? |

## Letters: what was established

- **No. 8 (R4797), c. 1440.** Ciphered slip pasted at the foot of a sheet whose upper part is the contemporary
  decipherment ("Anchora disse el duca di Milano aveva dato la donna Biancha a misser Leonello figlolo del
  Marchese ... antiveduto questo ..."; antipope Felix, Niccolò Piccinino, the Marquis of Ferrara). Read at the
  time. The nomenclator persons match the c. 1440 keys (R4748, R4749, R4755).
- **No. 10 (R4799).** One cipher run glossed letter by letter "presura di Montepulciano". Read at the time.
- **No. 13 (R4801) + no. 16 (R4804).** No. 16 is the clear decipherment of no. 13 (1527-29: Lautrec, the pope's
  coming to Bologna, "si pigliò Modena e Reggio"). Partial alignment: homophonic substitution with numbers as
  extra homophones (bologna = ∇ E 3 E 17 φ ₀⁰; accordi con = ₀ ⁿθ(cc) E ‡ + 15 ƥ E φ; a sign with superscript n
  = doubled letter). Read at the time.
- **No. 12 (R4790).** Photographed again in R1858, which DECODE marks "Decrypted": taken as read (Daniel's
  instruction, 24 Sept: trust DECODE's Decrypted status).
- **No. 4 (R4793).** Galgano Borghesi, J.U.D., orator, Naples 17 May 1456, to Leonardo Benvoglienti. Cipher runs
  in capitals, digits and signs, with the recipient's glosses ("duca" over the code word *Calor*, "papa",
  "re", "pare", "presto", "chercavano"). Code word *storpsi* is R4750's "Ambasciatore fiorentino", so the key is of
  the R4750 family, but R4750's alphabet does not produce no. 4's letters (L, N, T, Z, 1); R4753, R4756, R4762
  also tried by eye and do not fit.
- **No. 11 (R4800).** Donato Acciaiuoli to Lorenzo de' Medici, "ex Urbe die 13 junii 1478": a Florentine letter
  intercepted by Siena during the Pazzi war. Two cipher blocks (~11 lines). Not a Sienese key; R4752 (Bichi 1478)
  does not fit.
- **No. 20 (R4808).** "Sacra Regia Maiestas, Serenissime princeps ac metuendissime domine, post terre pedum
  oscula": ~18 lines of continuous cipher (lowercase letters, digits, ÷), "Scriptum ... die penultimo mensis
  Martii". The largest ciphertext in the fascicle.

## No. 14 (R4802): key recovered ciphertext-only (24 Sept)

- Whole-page letter to the "Magnificis et potentibus dominis Prioribus [et] Capitaneo Civitatis Senarum", 23 full
  lines + subscription, ~1,300 cipher tokens in 248 point-divided words (transcription agent B, `transcripts/no14.txt`,
  then `no14b.txt` after splitting the old OBAR into OL / OR / O).
- System: Italian, simple substitution with a few homophones (e = TR, 2; o = 6, P; i = Q4, PD, L; a = EQ, Q, TL;
  à = O+")"; q/g = Z), word points kept, two or three code signs for persons (7H, Z7).
- Attack history: plain homophonic anneal (wordsolve.py, 10 x 300k) stuck at nonsense; a hand crib ('8 6 RR IB VB Q'
  = nostra/vostra, 'RR IB EQ IB 6' = stato, 'Y 6 RR IB VB' = vostr-) pinned the key and Italian appeared; then the
  staged solver `homsolve2.py` (order 3 -> 4, frequency-seeded restarts, swap moves) reached the same key with no
  crib at all ("... comandamenti ma perche noi siamo tenuti e disposti sempre ... del vostro stato e dela vostra
  cità ... questa matina trovandosi Domenico ... per ragionare ... la impresa ... perche considerano ... Carlo ...
  guera ... per conservatione ... servidori vostri"). So: key recovered from ciphertext only.
- Reading in progress (agent pinning each line against the image with the key: `transcripts/no14_reading.txt`).
- **First reading (agent B, `transcripts/no14_reading.txt`).** Envoys of Siena on a journey write to the Signoria:
  "per la gracia di dio noi arivamo qui hieri da sera salvi e ... la nostra compagnia, e siamo pronti a seguire lo
  nostro camino ... a seguire li vostri comandamenti ... del vostro stato e dela vostra cità e di tuta Toscana:
  significhiamo a la Signoria vostra come questa matina, trovandosi Domenico con uno servidore di <7H> ... a
  ragionare per spacio d'ore due ... a <7H> è dispiaciuto ... la inpresa ... per <Z7> di (420) ... ancora afferma
  l'amico vostro che Carlo Malatesti e ogni altro sono [in] questa medesima gielosia ... Toscana unita con le ...
  tre potentie ... discopertamente ... guera con <Z7> per conservacione da (420) e per conservacione loro ...
  <7H> è a Napoli ... partiremo per seguire vostro viagio ... a la quale humilmente ci racomandiamo. [Roma?] ...
  li servidori vostri ... Marco". Glyph findings: '8' is two glyphs (compact 8 = v/u; tall theta = n, = D);
  D also covers a delta-c; 'o–o' joined = f; PLUS^dot = i; N? = u/v; arcs = nasal abbreviation; gn written ngn.
- **Date.** Not in the text read so far. Carlo Malatesta of Rimini (1368-1429) is alive; Siena and "tuta
  Toscana" are to join "tre potentie" in open war with <Z7> "per conservacione" of (420) and of themselves.
  Candidates: the Ladislaus war 1409-14 (then <7H> "a Napoli" could be Ladislaus's side) or the Visconti war
  1423-24 (Carlo Malatesta commanded for Florence; Z7 = Duke of Milan). Either way the letter is c. 1409-29,
  i.e. at or before Meister's 1421 for no. 1: a candidate for the project's oldest-cipher record, but only if
  the date can be fixed (second reading pass under way).
