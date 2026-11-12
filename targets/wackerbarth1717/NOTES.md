# wackerbarth1717: Wackerbarth's cipher letters, 1715-1717 (Dresden, HStA 10026 Geheimes Kabinett, Loc. 00712/05 and 00713/01): one key rebuilt from the glosses of the time; Relation XXII to Augustus II (Vienna, 14-16 June 1717) and the letter of 20 November 1715 from the camp before Stralsund read in part; the letter to Flemming of 24 April 1717 read from its decipherment of the time

Status: read in part (contributed by Brice Dudout, PR #418, 11 Nov 2026; verified and integrated 12 Nov 2026). Under one strict counting rule for the whole target (a word counts only when every letter of it as read is given by the gloss value of the number under it), Relation XXII reads at 634 of 716 cipher words (88.5%) and the letter of 20 Nov. 1715 at 741 of 922 (80.4%), both under the 95% bar. The key was rebuilt from the interlinear glosses of the time in both volumes. Its declared ground-truth test (A') FAILED; a held-out language test passed, the 1715 letter's own pre-registered measurement passed, and at verification each volume's key was found to read the other volume's letter. Open: numbers that no interlinear gloss gives (79, 96, 1000 and others; 72 rests only on the non-blind alignment of the 24 April cipher on its sheet), a few nomenclator codes, three probable misreadings, and words whose letters the reading takes from the sense where the cipher gives other letters or none. The letter of 24 April 1717 is read from its decipherment sheet of the time, not from the key.

> **Simultaneous work: Anne-Simone Rous.** Anne-Simone Rous (SBG Sachsen, Dresden) is working on this cipher correspondence
> of Wackerbarth and Flemming ("The Keys of Diplomacy. The encrypted correspondence of Saxon-Polish Ministers Wackerbarth
> and Flemming 1700-1720", HistoCrypt 2024, University of Tartu repository,
> https://dspace.ut.ee/items/3b294689-0a66-4b84-80f3-f3d2ab78f45d, DOI 10.58009/aere-perennius0111). The contributor found
> both volumes through her paper. By his statement the reading was made without contact with her and without her
> transcriptions, and nothing else of hers was used. It should be cited **as simultaneous, independent work alongside
> hers**; she may well have gone further.
>
> **Not checked here.** The paper could not be opened at verification (11 Nov) or at integration (12 Nov 2026): the DOI, the
> repository item, its PDF and the Wayback copy were all refused from this network. Only its title and abstract were read
> (OpenAlex record): the paper presents tentative results of the first phase of a project on the whole correspondence of
> 1698-1728, "based on examples from the years 1700, 1706, 1715, 1717, and 1720s". Everything more specific is **the
> contributor's report of the paper**: that the correspondence runs to about 6,500 folios; that she describes the 1717
> system of this volume as numbers of one to three digits, mostly two, with 355 and 1000 in the nomenclator; that she lists
> the 1717 letter as not deciphered, including one of "24th July 1717" (ff. 29-33) which the contributor takes for the
> letter of 24 April (ff. 29-32; he adds that he may have misread her account); and that she reports a glossed simple
> substitution in 1715.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents (transcription, key, protocols, measurements,
reading and write-up), by his statement. No human has read the readings against the scans; at verification two sample
pages were compared with the archive images (see the integration check).

## Document

Dresden, Sächsisches Hauptstaatsarchiv, 10026 Geheimes Kabinett. Two volumes of the series the archive titles "Des
Generalfeldmarschalls Herrn Graf von Flemming mit dem Kabinettsminister und General Herrn Graf von Wackerbarth gehabte
Korrespondenz" (record pages on archiv.sachsen.de, read 12 Nov 2026): **Loc. 00713/01** (Bd. 291, 1717, 298 views) and
**Loc. 00712/05** (Bd. 288, 1715). French, with passages in cipher; many cipher passages carry the decipherment of the time
between the lines, some do not.
- **Relation XXII** (copy, "Sire"), Wackerbarth to King Augustus II, Vienna 14-16 June 1717, Loc. 00713/01 ff. 71-80v (views
  0089-0099). Clear French and cipher mixed. No decipherment of the time.
- **Letter no. 15** to Jacob Heinrich von Flemming ("Monsieur"), Vienna 24 April 1717, Loc. 00713/01 ff. 29-32 (views
  0037-0040), with its decipherment of the time on a separate sheet at ff. 33-33v (views 0042-0043). Read from that sheet.
- **Letter of 20 November 1715**, Wackerbarth (camp before Stralsund) to his wife in Vienna, copy, Loc. 00712/05 ff. 307-314
  (views 0380-0387). No decipherment of the time beyond a few marginal words. See its own section below.

The scans are online at archiv.sachsen.de (`/digitalisate/<guid>/fullsize/NNNN.jpg`; guid b9278593-5104-4d05-8076-ee15ab111332
for Loc. 00713/01, 38624558-02ca-4adc-aa08-1cf2eafc87d8 for Loc. 00712/05; served to a plain request). The contributor reports
them marked "In Copyright", and the archive's imprint reserves copyright on its pages, texts and images unless stated
otherwise; the record pages state no licence. **No image, crop or derivative is included**, here or on the site. Credit:
Sächsisches Staatsarchiv, Hauptstaatsarchiv Dresden.

## System and key (`key.tsv`, `s15_key.tsv`, CC BY 4.0)

**One key, "S1"**, in the letters of 1715 and of March-June 1717: a homophonic substitution of French letters in one- and
two-digit numbers (e = 2/10, i = 9, o = 16/22/33, t = 28/52 ...). Three-digit numbers are polygrams and a nomenclator (154
Votre Excellence, 177 le Czar, 187 le roi de Suède, 217 le roi d'Angleterre, 252 le roi de Prusse, 292 la Pologne, 306 Vienne,
355 premier). Most numbers of four digits, 50xx and others, are taken for nulls (1000 is proposed as "et"; 4527, 4008 and
10009 are unresolved codes). Clear words are mixed in.

The key was rebuilt twice, each time from interlinear glosses of the time only:
- **key c** (`key.tsv` section A, frozen, SHA-256 3322ae87...c49c): from the glossed S1 views of Loc. 00713/01 (0017,
  0057-0062, 0071-0072, 0080-0081, 0086-0088), cipher groups aligned on the glosses (`frozen/scripts/align.py`,
  `build_key_bc.py`). **The decipherment sheet of 24 April was not a source of the key**; it served only the failed test A
  (view 0040) and a non-blind check.
- **K1715** (`s15_key.tsv`, frozen): from the glosses on views 0388-0390 of Loc. 00712/05 (57 numbers, 934 pairs, majority
  vote).

They are the same key: by the verifier's comparison they have 47 numbers in common and agree on 43 (the contributor counted
47 of 50); they share 150, 168 and 700; and each reads the other volume's letter. The four that differ: 20 (ee / b; b is
right), 71 (y / i: the training glosses have y in all 8 cases, so the "i" of `s15_key.tsv` is a slip), 77 (ss / s), 97 (m /
la). Key c's 103 = "les" (view 0088, "V.E. les desire") also reads "le": a gloss of the time gives it, view 0080 L03,
"deloger les russes" over 53 2 12 16 7 10 27 103 29 60 6 77 2 51 (103 29 = les, so 103 = le). 103 = le / les.

`key.tsv` section B holds proposals from the reading, made after the measurement: corrections 20 = b and 78 = le; homophones
seen at least three times (4 x, 38 h, 40 b, 73 z, 76 st, 79 la, 89 z, 92 t, 1000 et); nomenclator values taken from the sheet
of 24 April (187 le roi de Suède, 314 Danzig, 198 Stanislas, 356 second, 364 "10e", 72 ch); five single-case guesses. Of
these, 4 = x, 76 = st, 20 = b and 187 are confirmed by glosses of the 1715 volume, and 78 = le by one gloss in view 0057.

**Another key, not part of this entry.** The Nov.-Dec. 1717 letters of Loc. 00713/01 ("S2") are in the Flemming key K0 of
Loc. 00675/10 (view 0080). The contributor checked five of them (views 0234, 0254, 0275, 0285, 0296), all glossed at the
time: K0 decodes each as glossed; nothing new is read. One key, one entry: if S2 is ever written up it gets its own folder.
S1 is not K0, nor its shifted variant, nor Wackerbarth's 1703 key (contributor's comparison).

## Validation (`validation.txt`; protocols in `frozen/`)

By the contributor's record every protocol was hashed before its run and each run was made once (all commits and timestamps
are of 11 Nov 2026, so the order of events rests on that record).

**The declared ground-truth test failed.**
1. First protocol: both tests FAILED. Test A (view 0040 against the sheet of the time) scored 0.204 against at most 0.086
   for 200 permuted keys, under the threshold. Test B (lexical cover) did not discriminate. The contributor's diagnosis,
   made afterwards: test A was divided by a sheet four times longer than the portion tested.
2. Second protocol. Declared: the letter of 28 May 1717, glossed at the time, is held out of the key; the key must recover
   at least 0.60 of the gloss words exactly, with a margin of at least 0.30 over the best of 200 permuted keys (test A');
   and a held-out language test must pass (test B'); a reading is allowed only if both pass. **A' FAILED: 0.339 against
   0.128, margin 0.21.** B' passed: view 0091, 353 groups never decoded, criterion calibrated on the training views,
   z = 11.5, gap 0.74 (the list of candidate criteria had been widened after a first calibration failed, before the
   measurement; declared). Under the protocol's own rule there was no reading.
3. **A rule changed after the result.** Brice Dudout then accepted B' alone as the condition for reading Relation XXII
   (Avenant 3), with the 95% bar as the final check.

**Other evidence that the key is right**, separate from the failed test:
- the 1715 letter's own pre-registered measurement passed (below);
- at verification (12 Nov 2026), **the cross-volume check**: K1715, learnt only from the 1715 glosses of Loc. 00712/05,
  turns Relation XXII of Loc. 00713/01 into French (90% coverage, z = 8.8 over all 2,939 groups: "juste equilibre ...
  proceder selon ... circonstance ... conformer aux loix ... dans un concert sur ce qu'il y auroit a faire"), and key c
  likewise decodes the 1715 letter (z = 5.6). Neither key saw the other volume;
- every permuted-key control is beaten on every document with either key (verifier's own scorer; view 0091: z = 7.3);
- the readings are coherent diplomatic French that fits the clear text around each cipher passage.

Verdict recorded: "weak" (a failed declared test stays failed).

## Reading: one counting rule (`integration_recount.py`)

The contributor counted the two letters by different rules: in Relation XXII a word containing a number absent from the key
is "restored" and not counted; in the 1715 letter the same kind of word is "probable" and counted. At integration both were
recounted from the files under one rule, which was made strict after the claims review (below). Every word of the reading
is aligned on the cipher numbers under it, and

> a cipher word is counted only when the contributor read it (certain or probable) and **every letter of the word as read
> is given by the gloss value of the number under it**. Gloss values: key c, K1715, or a value that a gloss of the time
> attests: 4 = x, 76 = st, 20 = b and 306 = Vienne (glosses of Loc. 00712/05, views 0388-0390), 78 = le (gloss in view
> 0057), 103 = le (gloss in view 0080). A word is not counted when a number under it has only a value from the sense, when
> a number with a gloss value is read as other letters, when a number with a gloss value inside the word is passed over,
> or when a letter of the word has no number under it. Unresolved words are not counted.

Spelling equivalences allowed, and nothing else: u = v, i = j = y; a consonant written once in the cipher and doubled in
the reading, or the reverse (tranquilité read tranquillité); "est" of the time read "ét" or "êt" (76 = st in estat, estre,
estroite); "à" + 150 "le roy" read "au Roy". Ten counted words use one of them. Letters written in clear inside a cipher
line are given by the manuscript. A number with a gloss value passed over between two words takes no letter from either
word and is reported, not held against a word (18 such numbers in the three texts).

| document | cipher words | counted | share | contributor's own count |
|---|---|---|---|---|
| Relation XXII, 14-16 June 1717 | 716 | 634 | **88.5%** | 641 = 89.5% (575 certain, 66 probable, 66 restored, 9 unresolved) |
| Letter of 20 Nov. 1715 | 922 | 741 | **80.4%** | 892 = 96.75% (774 certain, 118 probable, 12 restored, 18 unresolved) |
| both | 1,638 | 1,375 | 83.9% | |
| 24 April 1717, key check on views 0037-0039 | 207 | 180 | 87.0% | 188 = 90.8% |

Both letters read with the key are under 95%: **read in part**, and so is the target.
- Relation XXII: 82 words are not counted: 43 restored, 8 unresolved, and 31 that the contributor marked certain or
  probable. Of those 31, 2 rest on a number with no gloss value ("le Czar" at 0097 G07, transcribed 174, probably a misread
  177; "de" at 0094 D17, whose e is taken by 79 = la); 17 read a gloss-valued number as other letters (chez on "ches",
  avoit, résolution, convaincre, pour, se on 78, faire, chancellerie, quelque, affaires, qui on "qri", concerter, cercles
  on "eercles", garantir on "xarentir", raport on "rasort", part, vers on "ueri"); 4 pass over a gloss-valued number
  inside the word (donner on "donqer", cour, de, mains); 8 have a letter with no number under it (du from "d" alone,
  comte, concerts, qu'il, des, premiers, donné, ses). 24 words the contributor marked restored or unresolved are counted,
  because their only missing value is 4 = x, 76 = st or 20 = b from the 1715 glosses (aux, paix, exécution, loix,
  Laxenbourg, nouveaux, s'expliquer, expédition; majesté, juste, circonstance, question, instructions) or 306 = Vienne.
- Letter of 20 Nov. 1715: 181 words are not counted: 12 restored, 18 unresolved, and 151 that the contributor counted. Of
  those 151, 53 rest on a number with only a value deduced in the letter or taken from the non-blind reading of 24 April
  (96 = le 19 times, glossed nowhere; 72 = ch 8; 1000 = et 6; 85 = st 4; 64 = c 3; 70 = x 3; 73 3; 284 = comte 2; 40 = b 2;
  609, 11); 28 read a gloss-valued number as other letters (devant on "desant", assaut on "attaut", triste on "tuiste",
  Wismar on 13 = m three times, pour on "four" ...); 9 pass over one (Poel on "poeh", puisque on "suque", prames on
  "prahmes" ...); 61 have letters with no number under them. Of these 61, 36 are words whose cipher stops before the end
  of the word after at least three letters (réellem, infailliblem, allem, Strals, extrém, génér ...): they may be the
  clerk's abbreviations (the 1715 training glosses abbreviate "allem:"), but the transcription does not record an
  abbreviation mark, so they are not counted. Counting them would give 777 of 922 = 84.3%, still under the bar; that is a
  sensitivity figure, not the count.
- 24 April key check: 27 words not counted (10 restored, 4 unresolved, 8 misread numbers, 5 supplied letters).
- Values deduced in both letters independently that agree: 1000 = et, 40 = b, 11 = k (73 is z in Relation XXII and ends
  "alliés" in the 1715 letter, s or z). They are strong candidates but no gloss gives them.
- By the files, the alignment was checked by hand on more than twenty words of each class against the transcription and
  the decryption files (claims review, below).

**Relation XXII** (`reading.md`, `translation.md`). The chancellor Count Sinzendorf, by order of Charles VI, makes
Wackerbarth an overture. The Emperor proposes a concert with the King of Poland and the King of England to restore the
tranquillity of the Empire and an "entire peace" in the North on a "just balance", in keeping with the laws of the Empire.
The same overture was made the day before to Saint-Saphorin, George I's minister. **The "triple alliance" is
Saint-Saphorin's opinion, not Sinzendorf's proposal**: Wackerbarth reports that, according to Saint-Saphorin ("Selon lui"),
the affair might even be carried as far as a triple alliance of the Emperor, the King of England and the King, and that
he, as a third party, could smooth the question of who should explain himself first. The stay of the Russian troops in
the Empire goes to the Diet of Ratisbon and to the directors of the Circles, to get them out and perhaps guarantee against
their return. George I wants the same measures "regarding Poland", and no German province given back to the King of
Sweden. Secrecy is strict: there was no referendary at the conference. Wackerbarth will take the waters at Baden while
Sinzendorf is in Innsbruck.
- **Reservations.** Three numbers are probably misread by the same slip, a 7 with a hooked head read as 4: 0097 G07 174 →
  177 (le Czar), 0097 G15 4 → 7 (g), 0098 G03 184 → 187 (le roi de Suède). They are left as frozen.

**Letter of 24 April 1717** (`a24_reading.md`, `a24_translation.md`): **read from the decipherment of the time.** The sheet
at ff. 33-33v, headed "Le C.te de Wackerbarth du 24. d'avril 1717", was transcribed (`frozen/releves/A-FEUILLE-0042-0043.txt`,
399 words, one doubtful) and translated. By the transcriptions it starts where the cipher of f. 29 starts ("vues du Roy de
Suede sur la Pologne") and ends where the cipher of view 0040 ends ("le traité qui est requis"). The rebuilt key reads the
cipher of views 0037-0039 in agreement with it (180 of 207 cipher words under the one rule). **Not blind**: the sheet had
been transcribed, for test A, before the reading. The letter covers the King of Sweden's designs on Poland (a landing near
Danzig), the fear that Sweden might detach the Czar from the Northern League, and the exchange of the county of Hanau, for
which the Electors' consents must be won directly and not through the Emperor.

## Letter of 20 November 1715: Wackerbarth (camp before Stralsund) to his wife in Vienna, copy (`s15_*`)

Dresden, HStA 10026 Geheimes Kabinett, Loc. 00712/05, ff. 307-314 (views 0380-0387), French, clear and cipher mixed. Same
key as the 1717 letters (above). Read in part: 741 of 922 cipher words (80.4%) under the one rule.

**Title corrected by the contributor.** The volume is catalogued as Flemming-Wackerbarth correspondence, and his first
working inventory (made from thumbnails) had "Flemming (camp before Stralsund) to Wackerbarth". The evidence points to
**Wackerbarth writing, probably to his wife, the Countess of Wackerbarth, in Vienna; the piece is a copy**:
- heading of f. 307: "Reponse à la lettre de 306. au camp devant Stralsund le 20e 9bre 1715"; 306 = Vienna by a gloss of the
  time (view 0389);
- it answers "celle du 5me du courant": f. 315 (view 0388) is the "Extrait d'une lettre de 306.66.857 ... en date du 5 de 9bre
  1715", on the same "raisonnement", and a hand of the time wrote above it "La Comtesse de Wa..." and "au C. de Wa...";
- the cipher reads "Voilà, ma {chère} femme, de quoi répondre ..." ("ma" and "femme" from the key; "chère" rests on 72 = ch);
- f. 306 (view 0379) is a jesting "Pleinpouvoir" signed "Le Comte de Wackerbart" at the camp before Stralsund in 1715 (day 12,
  month hard to read), naming Flemming in the third person;
- the writer directs the siege batteries and writes to General Dücker and to Count Virmond.
Against: a private letter is not expected in a cabinet volume. The contributor takes it for a copy sent on to a third party
(clean secretary's hand, unsigned, marginal notes by a decipherer: "il sera delogé", "prisonnier", "le Roy"). The attribution
is probable, not proved.

**Date: 20 November 1715, not 20 October.** The heading of f. 307 and the title of f. 315 write the month "9bre": a 9 with a
long descender, the same shape as the 9s in the cipher of view 0388. The contributor first read "8bre" and corrected it; the
verifier read the heading of view 0380 on the image and agrees. The frozen transcription files keep "8bre" and file names
with "1715-10-20" (declared). The content agrees with November: the Swedish entrenchment taken before Stralsund (night of
4-5 November 1715) and the capture of Rügen (landing at Stresow, 15-16 November 1715) are behind the writer. The countess's
letter answered is therefore of 5 November 1715. The month of the jesting full power at f. 306 is left open.

**Key and measurement** (`s15_key.tsv`; `s15_validation.txt`; `frozen/s1715/`). K1715 was learnt only from the glosses of the
time on views 0388-0390 and frozen. The target was transcribed blind by two other sub-agents. One pre-registered
measurement on the control portion (view 0384 left, 307 groups): S = 0.945 against at most 0.730 for 400 witness keys, rank
1/401, threshold 0.77 calibrated on training only: **passed**. Verifier's own control on the same page: z = 5.7.

**Reading** (`s15_reading.md`, `s15_translation.md`). Brice Dudout answered a blind plate of nine doubtful digit shapes (W1;
two controls, both passed): three words were corrected (embrasser, mal, beaucoup), six first readings confirmed. The plate
checks how digits are written, not key values.
- **Deviations declared by the contributor:** a thumbnail of view 0380 was seen before anything else (nothing decoded); the
  control portion was displayed before the protocol was written (the key is a deterministic function of the hashed training
  files; the verifier rebuilt it); a transcriber wrote "roit-on" for "voit-on" in clear text; the certain/probable
  classification was made by a single reader; one plate frame was re-set before any answer was exported.
- **Content.** The fall of Stralsund and Wismar is near; Augustus II wants a general peace, not a separate one, and no total
  ruin of the Crown of Sweden, as stipulated with his allies; the "reasoning" heard in Vienna is likened to the Count of
  Croissy's letter at the start of the campaign; the remnants that could carry Charles XII back to Poland and to "our rebels"
  are shut up with him in Stralsund and should be destroyed now; Wackerbarth will write to General Dücker and ask Count Virmond,
  the Emperor's minister, to come, so that peace may be made under the Emperor's mediation.

## Historical context (the contributor's check of 11 Nov 2026 against reference works; not re-checked at integration)

A historical article on both letters, with sources, is published by the contributor at
https://bdudout.github.io/europe-chiffree/fr/stralsund-1715.html (also /en/ and /ja/). Points he checked:
- Wackerbarth commanded the Saxon corps at the siege of Stralsund (July-December 1715) and led the attack of 4-5 November on
  the entrenchment (de.wikipedia, "Belagerung von Stralsund (1715)"; H. Voges 1922 not read).
- Damian Hugo von Virmont was the Emperor's envoy at the court of the King of Sweden in Stralsund in 1715 (de.wikipedia).
- The countess was born Caterina di Balbiano (de.wikipedia, "August Christoph von Wackerbarth"); R. Pons, MIÖG 114 (2006),
  65-95, studies her as an unofficial Saxon envoy in Vienna (cited by Rous, by the contributor's report; not read).
- L. R. Lewitter, "Poland, Russia and the Treaty of Vienna of 5 January 1719", Historical Journal 13/1 (1970), 3-30: Augustus II
  decided for an alliance with the Emperor and George I at the end of August 1717 (full power to Flemming, 6 August), while
  Charles VI was refusing new engagements before the end of the Turkish war.
General knowledge, not checked:
- Wackerbarth (1662-1734) was a Saxon cabinet minister and general.
- Flemming (1667-1728) was the first minister of Augustus II.
- Philipp Ludwig von Sinzendorf (1671-1742) was Hofkanzler of Charles VI.
- François-Louis de Pesme de Saint-Saphorin (1668-1737) was George I's minister in Vienna.
- The Russian troops of Peter I had been in Mecklenburg in 1716-17.
- The Hungarian campaign of 1717 is the Turkish war; Belgrade fell in August 1717.
**Hypothesis, not established:** the overture of June 1717 may be an early step towards the Treaty of Vienna of 5 January
1719 between Charles VI, George I (as Elector of Hanover) and Augustus II (as Elector of Saxony). A direct link is not
established.

## Prior art

- **Anne-Simone Rous**: simultaneous work on this correspondence. See the box at the top; her paper was not opened here.
- **A possible original key, not checked.** DECODE holds the Saxon key series of HStAD 10026 Loc. 03233/02 (e.g. R5139,
  the key of Flemming with Wackerbarth, 1700-1728, Lasry and Rous). The contributor did not try those keys on S1, and they
  were not tried at integration. A web-search snippet of Rous's 2022 book (*Geheimdiplomatie in der Frühen Neuzeit. Spione
  und Chiffren in Sachsen 1500-1763*) says isolated Wackerbarth-Flemming nomenclators exist "for his 1717 Vienna trip"; the
  book was not opened. Lead 1683 in `research/leads.json` (the "Allerhand Chiffren" bundles of Loc. 3233, Wackerbarth among
  them) is the place to look. If an original key is found, the numbers left open here can be settled from it.
- S2 is the Flemming key K0 of Loc. 00675/10, related to issue #357 on lead 1663 (Flemming to George I, Hannover).
- A quick web search (text only) by the contributor found no edition of Wackerbarth's Relations of 1717. Printed
  collections (Sbornik RIO, Urkunden und Actenstücke, Saxon or Austrian state papers) were not searched. An edition may exist.
- `catalogue.json` and `research/leads.json` have no entry for Loc. 00712/05 or Loc. 00713/01 (checked again at
  verification); leads 1683 and 1687 are other Wackerbarth material. No DECODE record of these letters was found in the
  repository's files; the live database was not queried.

## Integration check (12 Nov 2026)

PR #418 was verified independently on 11-12 Nov 2026 (verdict: sound with corrections) and integrated on 12 Nov 2026.

Reproduced:
- frozen hashes all match (`PROTOCOLE.md` excepted, as declared; `frozen/releves/S2-0285.txt` appears in no hash list);
- keys b and c rebuild byte for byte from the glossed views (`build_key_bc.py` in a scratch copy); `key.tsv` section A is
  the frozen key c; K1715 rebuilds from the training glosses (57 numbers, 934 pairs), one value differs (71);
- the raw decryption of Relation XXII is identical with the contributor's script and with a second decoder;
- the contributor's counts (575 / 66 / 66 / 9 of 716; 164 + 24 of 207; 774 / 118 / 12 / 18 of 922);
- test B' with an own scorer and the project's French model: z = 7.3, above all 200 permuted keys (PR: 11.5); the 1715
  control page: z = 5.7; test A' not re-run (lexicon and corpora not in the PR), figures match `MESURE2.json`;
- transcription against the archive images: view 0091 left, lines G02-G20 (about 190 groups), all agree, including the
  struck 289 and the 84>29 overwrite; view 0384 left, L01-L11 (about 150 groups), all agree (at L11 the doubtful 28/25 looks
  like 28; the plate chose 25); heading of view 0380 "le 20.e 9bre 1715";
- `_check_reading`: `reading.md` 0.505 marginal, `a24_reading.md` 0.553 marginal, `s15_reading.md` 0.706 readable (PR:
  0.724), `s15_decryption.txt` 0.716.

Not checked: views 0096 and 0042 (downloaded, not compared); view 0388 (connection reset); the three suspected 4/7
misreadings on views 0097-0098; the coverage of the 24 April sheet on the images; Rous's paper and book.

Corrections made at integration:
1. **One counting rule** for both letters and the key check (`integration_recount.py`, read-only); made strict after the
   claims review: Relation XXII 88.5%, 1715 letter 80.4%. The 1715 letter is "read in part", not "read"; the contributor's figures (89.5%, 96.75%) are given
   once, as his.
2. **The failed test is stated as failed** in this file, `validation.txt`, `profile.json` and on the page; the cross-volume
   check found at verification is recorded as separate evidence.
3. **The key came from the interlinear glosses**, not from the sheet of 24 April (`outcome.method_basis`).
4. **24 April 1717 is "read from existing decipherment"** (`outcome.parts`), with the sheet as the text.
5. The 1715 document id in `profile.json` was `...-1715-10-20`; now `...-1715-11-20`.
6. 71 = y (not i) and 103 = le / les (gloss of view 0080) noted in the key files' headers (frozen rows not edited); the "187 differs" remark
   corrected (187 is not in key c section A).
7. S2 (the Flemming key K0) is another key and is kept out of the entry.
8. Statements about Rous's paper marked as the contributor's report; the possible original key recorded as a gap.
9. `reading_review` recorded by the integration reviewer for the three texts (B, B, A for the sheet).

## Claims review by a second reader (12 Nov 2026)

An independent reader checked the page against these files. Findings and what was done:
- **The counting rule was looser than the page said.** The page said a word counts when every number under it has a value
  from a gloss of the time; `integration_recount.py` dropped a word only when a number under it had no value at all. A
  number with a gloss value read as another letter (garantir on 4 = x, the same 4-for-7 slip as "le Czar"), a number
  passed over, and a letter with no number under it did not drop the word. The script now counts a word only when every
  letter of it as read is given by the gloss value of the number under it (equivalences listed above). New figures:
  Relation XXII 664 → 634 of 716 (92.7% → 88.5%), letter of 1715 841 → 741 of 922 (91.2% → 80.4%), both 1,505 → 1,375 of
  1,638 (91.9% → 83.9%), 24 April key check 193 → 180 of 207 (93.2% → 87.0%). The reviewer estimated about 25 such words
  in Relation XXII (share near 89%); the script finds 29 (31 with the two no-value words) and 88.5%. For the 1715 letter
  the drop is larger, mostly words whose cipher stops short of the word's end (see above).
- Two alignment details fixed on the way: a catchword at the foot of view 0384 left (6 2 12) had been counted as a line,
  and words running over a page break were split; the 1715 letter is now aligned as one stream.
- **103 = le.** The reviewer noted that key c gives 103 = "les" only. A gloss of the time gives "le": view 0080 L03,
  "deloger les russes" over 53 2 12 16 7 10 27 103 29 60 ..., where 103 29 = les. The eleven words that read 103 = le
  (nine in Relation XXII, two in the 24 April check) stay counted; the citation is now in the script and in the key
  files' notes.
- Page wording corrected: 23 restored words rest on 4 = x or 76 = st (16 and 7), none on 20 = b; 72 and 1000 rest on the
  non-blind alignment of the 24 April cipher on its sheet; "no DECODE record" is the repository's copy only; the letter is
  probably to the countess; at view 0384 L11 the doubtful 28/25 looks like 28 while the reading uses 25; most (not all)
  four-digit numbers are nulls; the 1715 test's declared deviations are given beside it; the contributor's own share
  lines in `reading.md` and `s15_reading.md` are now headed by the project's strict count.

## Remaining gaps

- Relation XXII: 82 of 716 cipher words not counted (numbers 79, 1000, 40, 73, 38, 92, 89, 93, 98, 11, 48, 118 with values deduced from the sense only; codes 4527, 289, 172, 169, 184, 1900205 with none; 29 words where the reading gives a gloss-valued number other letters, passes one over or supplies a letter, listed in `integration_recount.py`) - blocker: open-codes; these numbers are glossed nowhere in either volume's training views; key.tsv section B proposes values that fit; 1000, 40 and 11 recur with the same value in the 1715 letter; the misread or skipped numbers need a blind re-reading of the images (not done)
- letter of 20 Nov. 1715: 181 of 922 cipher words not counted (53 rest on numbers with values deduced in the letter: 96 = le 19 times, 72 = ch, 1000 = et, 85 = st, 64 = c, 70 = x, 73, 284 = comte, 40 = b; 98 where the reading gives a gloss-valued number other letters, passes one over or supplies letters, 36 of them possible abbreviations of the clerk; 12 restored; 18 unresolved: 183, 251, 270, 400, 357, 358, 365, 4008, 10009, 680, 68, 94 and five spelled words) - blocker: open-codes; 96 is glossed nowhere (in view 0386 right, L03, it may be a 46); 72 = ch rests on the non-blind alignment of the 24 April letter on its sheet; the misread, skipped and truncated words need the images re-read blind (not done; images In Copyright, not here)
- three probable misreadings in Relation XXII (0097 G07, 0097 G15, 0098 G03) and the doubtful number 0089 M03 - blocker: illegible; a 7 with a hooked head read as 4; to be re-read blind on the images (not done; no plate made)
- a ground-truth test of key c - blocker: no-key-material; test A' failed and no other glossed S1 letter of at least 300 groups is left in the volume (28 May and 24 April are used up); Rous's corpus may hold one
- the original key, if one survives - blocker: no-key-material; the DECODE key records of Loc. 03233/02 (R5139 and others) were not tried on S1 and Rous's 2022 book was not opened (see Prior art); not checked
- what A.-S. Rous's paper says about these volumes - blocker: needs-physical-access; the Tartu repository refused every route from this network on 11 and 12 Nov 2026 (DOI, item page, PDF, Wayback); only the abstract was read

## Further work (outside this target's texts)

- Clear passages of Relation XXII not transcribed in full (views 0098-0099, marked "…"): clear text, not cipher; they would
  complete the translation.
- The S2 letters (another key, K0): the parts without glosses (views 0246-0247, 0284, 0286) and the German enclosure A of
  12 June without glosses (0073-0074) are not transcribed.

## Escalation

- [x] siblings: the volume (298 views) surveyed by the contributor for cipher passages (PROTOCOLE §1 and Avenant 2 §1 list them); glossed S1 views used for the key; the second volume (Loc. 00712/05) brought in with its own glossed views 0388-0390; at verification each volume's key was run on the other volume's letter
- [x] clear-pages: the separate sheet at views 0042-0043 identified as the decipherment of the whole letter of 24 April; no clear copy of Relation XXII or of the 1715 letter in the volumes
- [x] known-keys: Flemming key K0 (Loc. 00675/10, view 0080) and its shifted variant, and Wackerbarth's 1703 key, compared: none is S1; K0 = S2. The DECODE keys of Loc. 03233/02 were not tried on S1 (recorded as a gap)
- [x] print: quick web search, no edition of the 1717 Relations found; Rous's paper read by the contributor, not openable at integration; printed state papers not searched
- [x] key-rebuild: key c rebuilt by alignment on all glossed S1 views, K1715 on the 1715 glosses; the two keys compared and the gloss-backed values of each carried to the other letter (4 = x, 76 = st, 20 = b, 306 = Vienne); extension from the sense kept apart (section B) and not counted
- [x] retry: every word recounted letter by letter on the numbers under it with both gloss-built keys (integration_recount.py lists every number without a value, every misread or skipped number and every supplied letter, with the words they fall in); misreadings noted, not corrected in the frozen transcription
