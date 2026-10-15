# De Swart 1782: Dutch legation cipher from St Petersburg (DECODE R1036)

Status: read (R1036, 96.7% of groups); R1040 (1787) read in part

One document, two keys (one-key review, 14 Oct 2026): R1040 changes codebook at group 180 of image 5459, so the
profile gives the outcome per key in `outcome.parts` and README has one row per part, as soria1523 does. Part 1, the
Croiset 1765 key (R1038): R1036 whole and the second part of R1040. Part 2, the missing Rechteren-family code: the
first 1,928 groups of R1040, not solved; the same code family as Rechteren's letter of 1785
(`targets/rechteren1785/`, a different cipher, with its own page). The entry is read in part because R1040 is not
read in full.

## Target

Johan Isaac de Swart, Dutch resident at St Petersburg, to Pieter van Bleiswijk (Grand Pensionary), despatch of
8 March 1782. DECODE R1036, `NA_3.01.25_P._van_Bleiswijk_inr610_by_J.I._de_Swart_1782-03-08`, nine scans, with
DECODE's authenticated manual transcription of the ciphertext. Sister record R1040 (Nationaal Archief 1.01.02
Staten-Generaal inv. 7408, de Swart, 29 November 1787, 23 scans) was worked alongside.

## System

A Dutch code-nomenclator of three-digit groups in which a mark on one digit (two short strokes, underline, caret,
small circle, circle with a bar) makes a different group: `340` and `340^_` are unrelated values. Entries are
words, syllables and letters, so words are often built from pieces (*Spa + nje*, *Dene + mar + ken*). This is the
Croiset codebook of 1765 for the Russia legation, which survives with its key as DECODE R1038.

## Result

The key comes from the archive: DECODE R1038's authenticated partial transcription of the 1765 codebook, parsed
to 5,961 code-to-plaintext entries (`decode_1765.py`, `R1038_key_parsed.tsv`). It reads 1,448 of the 1,719
groups (84.2%). Thirty-four more values were recovered from repeated contexts, each checked against every
occurrence, which brings the reading to 1,613 groups (93.8%). They are labelled "contextual inference" in
`R1038_key_parsed.tsv`. Examples: `881` = *nje* (Spanje), `340^_` = *mar* (Denemarken), `176^^` = *mpli* (*pure et
simpliciter*, twice), `741` = *haar* (the Empress, 12 times), `681^_` = *mogendheden*.

A third pass read the key entries DECODE had left illegible straight from the R1038 scans (the word stands to the left of its code, and parallel columns of homophones confirm faint words). Of 50 entries read, 41 fit their R1036 contexts and were kept, for example `781` = *geheel* (*het Griekse project geheel stil*), `748^"` = *commercie* (*de vrijheid van de commercie der neutralen*), `488^_` = *Zijne Keizerlijke Majesteit*, `515^o` = *twaalf* (twelve Greek boys), `640` with a barred circle = *Russisch*. They are labelled "read from R1038 scan" in `R1038_key_parsed.tsv`, and every reading, kept or not, is in `R1038_scan_readings.tsv`. R1036 now reads 1,663 of 1,719 groups (96.7%). The 56 open groups (51 codes) are entries lost in the scan's binding shadow, blank in the book, or read with too little confidence to use.

The despatch covers three matters:

1. the French and Spanish answers to the Austro-Russian mediation proposal, and Britain's position on the American
   colonies and Gibraltar;
2. Catherine II's Greek project: Grand Duke Constantine is being taught Greek and given Greek attendants;
3. Prussia's accession to the Armed Neutrality, and the Vice-Chancellor's talks with the Swedish and Danish
   ministers about the accession act and its secret articles.

The token-level reading is `R1036_machine_decipherment.txt`, with the audit trail in `R1036_tokens.tsv`. The 56
unread groups are all rare codes, and 51 distinct codes remain (`R1036_unknowns.txt`). A normalised opening and
the method are in `METHOD_AND_STATUS.md`.

## The Emperor and the Greek project: normalised reading (30 Sept 2026)

Asked to normalise the Greek-project passage (machine lines 9-15 and 24-26, tokens 239-466 and 686-775) group
by group; the page had only a paraphrase. Checked against `R1036_tokens.tsv`, the parsed key, the key scans
(`R1038_codebook_p*.png` in the main checkout) and the letter scans (`R1036_p2.png` = image 5416, `R1036_p3.png` =
5417). Findings, each of which changes the machine text (not yet applied to `decode_1765.py`, so the machine file,
the parsed key and the 1,663/1,719 count are unchanged):

- **Key layout.** On every codebook page checked (p4, p7, p8, p9, p11, p13 = images 5433, 5436-5438, 5440,
  5442) the word stands to the left of its code, as the third pass said and as DECODE's own transcription has it
  (51^" agter, 330^_ maaken, 405^_ ma, 642^_ mal, 647^_ mediator, 867^_ obtein, 940^_ oblig, 943^_ occasion). Three
  third-pass readings took the word to the right, which belongs to the next column: **54^" = alhoewel** (the "alle"
  is 130^"), **314^" = behalven** (row bed 312, beg 313, behalven 314, beide 315; the "Behe" to its right is the next
  column's), **941^_ = observeeren** (row oblig 940, observeeren 941, obtineeren 942, occasien 943).
- **47^_ = k, not l.** First underlined column of p8: a 44, der 45, es 46, k 47, om 48, tt 49; the l of DECODE's
  "47^_|53^_|123^_ - l" is right only for 53^_ and 123^_. This gives Griekse here and Denemarken for all eight "den e
  mar l en" of the machine text (47^_ occurs nine times).
- **Other DECODE key misreadings, fixed by the entry's alphabetical place and its contexts:** 327 = el (between 326
  eid and 328 elf; tael, elders), 92^_ = houden (between 88^_ hoor and 94^_ hun; also "aan de hand te houden", token
  1632), 121 = die (diep), 862^^ = het, 448^" = con (Constantijn; between 446^" comp and 449^" conclu), 223^o = veele,
  743 = dat, 853^_ = niet, 559 = gehad, 80 = eeren, 135 barred circle = zoek.
- **Ciphertext transcription.** The "^_" that DECODE puts before a group after a comma (",^_ 3 8 0") is a dash
  written after the previous group (checked on the images at tokens 389 and 776), not a mark on the group. So the
  four "krÿgen?" (380^_) are plain 380 = van (tokens 389, 549, 1397, 1547: in hand[en] van, de ministers van
  Zweden, de hoven van Denemarken, de depeche van) and token 776 is plain 303 = die, not 303^_ = koop. After 362^_
  (jong) on image 5416 an interlinear group inserted with a caret reads **191 = ens** (jongens); DECODE read it as
  19 (daar zal). The decoder attaches that dash to the next group whenever the group has no mark of its own: 53
  tokens in `R1036_tokens.tsv` start with it and 21 take their only mark from it (8, 29, 46, 123, 389, 486, 549,
  599, 671, 776, 858, 904, 1067, 1122, 1160, 1397, 1446, 1468, 1547, 1584, 1683). The plain values read better
  elsewhere too (token 8: 451 = van de, "de antwoorden van de hoven"; tokens 29, 123, 858: 375 = aan, "aan dezelve", "aan haare mediatie",
  "aan te wenden", not konde; tokens 671, 904: 550 = ge, "geaccepteerd", "genomen", not liv?). Next step: drop
  the leading dash in `decode_1765.py` and regenerate.
- **Token 251** is 601 with the bar through the 6 that marks ^_ in this hand (as in 362^_), i.e. komen; the sense
  needs dan, which the writer spells 601 368^" (d + an) at token 686. Read [dan], graded M, as an encoding slip.
- **Names.** 644^_: the word left of 644 on p9 reads "Veld Ma…", the rest under the binding shadow (row: 568
  Marechal, 644 Veld Mar…). 339^_ is faint ("Man"?). With 358^_ r, 533 u, 505^_ z, 585^_ o, 359^_ w: aan den
  Veld[maarschalk] Ru[man]zow, probably Field Marshal P. A. Rumyantsev (not verified; man and the title graded M).
- **Lost line.** The first line of image 5417 is cut off in the photograph (DECODE did not transcribe it). It falls
  between "en het" (end of 5416) and "te maken. Met dit antwoord…", so the end of the Greek sentence is lost; the
  lower halves of its figures are visible but not their marks. Blocker: needs a better image of 5417.

Reading, normalised to modern spelling like the opening; [ ] supplied or open, grades in brackets after the word
(M uncertain, I from context or the entry's place in the book); participles are given where the book has only the
infinitive (stellen, zenden, observeeren):

> Of nu de Keizer in dezen met haar oprecht handelt, [dan] (M) of hij daardoor maar zoekt om haar te amuseren en
> aan zijn lijn te houden, gelijk velen (I) met [grond] (M) veronderstel[len], is niet wel zeker te ontdekken; maar het is
> zeker dat zij tot nog toe van de Keizer zeer [gunst]ig (I) ingenomen is, en dat zij omtrent de bevordering van
> dit haar [favoriet] (I) project op Zijne Majesteit veel rekent en staat maakt. En tot bewijs dat zij het project geheel
> niet geabandonneerd heeft, zo dient dat, behalve dat zij de jonge grootvorst Constantijn, gelijk [ik] reeds de
> eer heb gehad in een mijner voorgaande aan U HoogEdelGestrenge te melden, in hand[en] van [een] Griekse vrouw al
> sedert een geruime tijd gesteld heeft, en hem de Griekse taal laat leren (I), en [verder] (I) een Griekse educatie (I)
> [hooggedachte] (M), zij heeft ook onlangs aan de veld[maarschalk] (M) Ru[man]zow (M) ordre gezonden om twaalf
> Griekse jongens te bezorgen, en het [line lost] te maken.
>
> Alhoewel het sedert enige [tijd] van het bewuste Griekse project geheel stil is, en de Keizerin daaromtrent voor
> haar confidenten (I) [77^o] diep (I) stilzwijgen heeft geobserveerd, zo kan men doch daaruit niet besluiten (I)
> dat het bij haar geheel vervallen zou zijn; veelmeer schijnt haar retenue op dit subject veroorzaakt te zijn door
> de ontijdige [geruchten] (M), die daarover hier gelijk elders [...]

("Whether the Emperor is dealing honestly with her in this, [or] whether he only seeks to amuse her and keep her on
his line, as many suppose [with reason], cannot well be discovered for certain; but it is certain that she is so far very
favourably disposed towards the Emperor, and that for the furtherance of this [favourite] project of hers she counts and
relies much on His Majesty. And as proof that she has by no means abandoned the project: besides having for a
considerable time placed the young Grand Duke Constantine in the hands of a Greek woman, as I have already had the
honour to report to Your Honour in one of my previous letters, and having him taught the Greek language, and [further] a
Greek education [...], she has also lately sent orders to Field [Marshal] Ru[man]zow to procure twelve Greek boys, and
[...] Although it has been entirely quiet about the known Greek project for some time, and the Empress has kept [a]
deep silence about it towards her confidants, one cannot conclude from this that she has wholly dropped it; rather,
her reserve on this subject seems to have been caused by the untimely [rumours] about it, here as elsewhere [...]")

Other details: geabandonneerd has one superfluous group (389 eere) inside it; confidenten is 528^" (faint "confi…")
+ 601 d + 264 ent + 86 en; 553 is "hoog gedachte" in the book (left of 553; "hoogst gedachte" is 626), but its place
in the clause does not resolve. Still open in the passage (738, 299 and 231^o read on 30 Sept 2026, below): 77^o (DECODE and the scan
"Stana"), 792 (faint "gerucht?"), 592 (faint; [gunst] from the entry above it, 591 Gun…, and the sense). Not applied, to
check: on p9 the words left of 412 and 488 are both "Zyn Majesteit" and "Zyn Keiz. Maj." stands right of 488, so
488^_ may be Zijne Majesteit rather than Zijne Keizerlijke Majesteit; its three uses (tokens 1050, 1305, 1678)
concern the King of Prussia.

### Open groups of the Greek passage re-read (30 Sept 2026, for the Lasry quotation)

Read from the codebook scans (`R1038_codebook_p7.png` = 5436, `p6` = 5435, `p13` = 5442, `p14` = 5443, main checkout):

- **738 = grond (M).** p7, fourth column: 734 goed, 736 graaf, 737 gr…, 738 "gro…" (the o and a descender visible),
  739 Gu…, 740 ha, 741 haar; the parallel column's 810 reads "gro[n]d/t". "gelijk velen met grond veronderstellen"
  ("as many suppose with reason") is the idiom.
- **299 = favoriet (I).** p6, third column: 296 fait, 297 familie, 298 fau…, 299 capital F + faint "…ri…", 300 femm…,
  301 fem…. "dit haar favoriet project": Catherine's "projet favori". "Februari" also fits the letters and the place
  but gives no sense.
- **231^o = verder (I).** p14: the word is in the gutter, "verd…" legible, between 230 verdedig… and 232 vereenigen
  (`R1038_scan_readings.tsv`); "en verder een Griekse educatie" continues the list of things done for Constantine.
  "verdient" (the parallel 306) gives no sense here.
- **77^o still open.** p13: the codes 72°-84° stand right of the words Speculatie, Spreek, Men Spreekt, Staat, [long
  entry], "Stans/Stanz" (77°), Ster…, …, de Staaten van het Rijk (80°), Stil (81°). The word before "diep stilzwijgen"
  is not a known Dutch word as read; "steeds" would fit the sense and the place but not the letters. Left open.
- **The line lost at the top of image 5417** stays open (needs a better photograph).

Quotation for the Lasry list (30 Sept 2026): "Of nu de Keizer in dezen met haar oprecht handelt, [dan] of hij daardoor
maar zoekt om haar te amuseren en aan zijn lijn te houden, gelijk velen met [grond] veronderstel[len], is niet wel zeker
te ontdekken; maar het is zeker dat zij tot nog toe van de Keizer zeer [gunst]ig ingenomen is, en dat zij omtrent de
bevordering van dit haar [favoriet] project op Zijne Majesteit veel rekent en staat maakt."

## R1040 (1787)

Leeuw (2000) says this letter was coded "presumably by accident" with two codebooks. The switch point is at
group 180 of image 5459. After it the 1765 key reads the text at 84–90% a page (`R1040_second_key_*`). The first
1,928 groups use a missing Rechteren-family nomenclator. Crib alignments with R2032, R2051 and R2052 (known
plain/cipher pairs from 1784–86) cover only 2–3% and do not yield prose. The key is probably Nationaal Archief
inv. 158, which is not online. That segment is open.

## Prior work

No published decipherment of R1036 or R1040 was found. The search covered record numbers, correspondent, dates
and subject. The Oterleek-codes paper (HistoCrypt 2026) documents the codebook family but not these letters.

## Remaining gaps
- R1040 first part, 1,928 groups (images 5453-5458, 5459 groups 1-179) - blocker: no-key-material; a different, missing Rechteren-family code (probably NA inv. 158, not online); crib transfers from R2032/R2051/R2052 cover 2-3% and give no prose
- R1040 second part, about 700 of 5,956 groups without a value - blocker: open-codes; the 1765 key with the R1036 context values and R1038 scan readings (5,256 given a value, R1040_second_key_tokens.tsv); no context pass yet on this part's own unread groups
- R1036, 56 groups (51 distinct rare codes) - blocker: illegible; entries lost in the binding shadow of the R1038 scans, blank or too faint

## Escalation
- [x] siblings: R1038 (the key), R1039/R2032/R2051/R2052 plain-cipher pairs of the legation opened and aligned
- [x] clear-pages: none on R1036 or R1040; the clear copies are on the 1784-86 sibling records only
- [x] known-keys: 1765 Croiset key fits R1036 and R1040 part 2; the 1803 Croiset relative tried on R1040 part 1, nonsense
- [x] print: no decipherment of R1036 or R1040 in print (Leeuw 2000, Oterleek codes HistoCrypt 2026)
- [x] key-rebuild: 34 context values and 41 scan readings for R1036; crib transfers for R1040 part 1 (2-3%)
- [x] retry: R1040 part 2 decoded again with the extended key (decode_1765.py includes the 34 context values and 41 scan readings); a context pass on its own ~700 unread groups is still to do
