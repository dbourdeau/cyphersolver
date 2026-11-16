# Segreteria di Stato to the Nunciature in Spain, 1736 (ASV Segr. Stato Spagna 423)

Status: in progress (all eleven letters read 23 Oct 2026; pages and ledgers not yet updated with the clear copies)

23 Oct 2026, re-read r2d (texts/423_r2d_reread_log.md): **the contemporary clear copies were on the DECODE records all
along.** The png documents attached to R26, R179-R183, R186-R188 and labelled "cleartext" are not the cipher pages
(those are the IMG_ images) but neighbouring folios of the volume, and among them are the clear "Copia" of seven of the
ciphered letters: 423/1 (ff. 284r-286r), 423/4 (f. 301r), 423/5 (f. 375r), 423/6 (f. 386r), 423/9 (ff. 416r-v),
423/10 (ff. 493r-494r), 423/11 (ff. 509r-v). The copies of 423/1, 5, 9, 11 were transcribed (texts/423-<n>_copy.txt)
and aligned token by token with the decode (research/reading_audit/r2d_align.py); six figures of NiLan's R26
transcription corrected on the images; the three open spots of 423/9 and 423/11 are cipherer's slips seen on the
images. Key: 26 = del (not Lasry's a) and 80 = dal (not nel); twelve earlier nomenclator values were wrong and are
replaced (1219 ora, 1239 quell, 1608 necessari, 1229 perché, 1231 però, 1818 ragguagli, 1699 pregiudizi, 1865
sodisfazion, 1218 avut, 1223 mentre, 1260 Ambasciator, 1368 congiuntur); about 55 groups valued (1513 Governator, so
Molina's title is "Mons. Governatore del Consiglio"; 1544 Inquisitor; 1449 ecclesiastic; 1389 costì; day groups 1952 =
7, 1953 = 8, 1957 = 12, 1964 = 19), each checked at every occurrence (texts/b04_key_additions.txt, r2d block). **423/1,
5, 9, 11 read** (v2 plain/explicit: 0.92/1.0, 1.0/1.0, 0.94/1.0, 0.94/1.0); the corrections carried into the readings
of 423/2, 4, 6, 7, 8, 10 (r2d_fix_read.py), which all stay read. fraction_read 0.52 -> 1.0; class read. 12 group
tokens stay open, each seen once.

22 Oct 2026, re-read (REREAD_BRIEF, batch b04; texts/423_b04_reread_log.md): **423/2 and 423/4-11 read** (grade B,
texts/423-<n>_reading.md with English _en.md); 423/1 attempted, still decoded, not read. No contemporary text exists
(26 DECODE images checked, no gloss; no edition), so the readings rest on the figures: the DECODE transcriptions
re-segmented (research/reading_audit/b04_seg.py; Lasry's segmented file leaves out about a fifth of the tokens), 15
unclear figures resolved on the images (texts/423_b04_corrections.tsv), and the key corrected: 25 = che, 30 = ta,
69 = z, 93 = nel; 1234 = qual, 1205 = com, 1241 = tant, 1210 = esser (key_extra.txt had Ministr/Nunzi, che, molt,
restar); about 65 more groups valued (texts/b04_key_additions.txt). fraction_read 0.016 -> 0.777 (5,725 of 7,366
non-null tokens). Every reading aligned word by word with its decode (b04_align.py); supplied words bracketed.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read**: 423/3 only (one
sentence, one open group). **Decoded, not read**: the other ten letters: open nomenclator groups (about one per eight to
ten words) and ??? runs stand in almost every sentence. 95.3% (text with a value) is withdrawn as a reading figure;
class already solved -> read in part, 1.6% of the tokens in a letter that reads.

## The target

Catalogue entry: "The Secretariat (Spain) to The Nunciature, 10 ciphertexts". These are ciphered despatches from the papal
Secretariat of State in Rome to the nunciature in Madrid, 14 July to 22 December 1736, in the Archivio Segreto Vaticano,
Segretario di Stato, Spagna 423 (index i. 1025: "Lett. originale e ciffre della Segretaria alla nunziatura, dal 7 gennaio
1736 al 29 dicembre 1736", ff. 9-522). They are DECODE records **R179-R188**, one per item: 21 pages, status "partially
decrypted", homophonic nomenclator, numerical, images behind a login. The corpus actually has 11 items (423/1-11). The
catalogue's "7 Jan 1736" is the start of the volume, not the date of a letter. The addressee on the clear dockets is
"Sig. Ab. Guiccioli, Madrid", who ran the nunciature after the rupture of 1736.

**Item 1 is DECODE R26** (`ASV_i1025_SdS_Spain_423-1`, 5 pp., created 2016, status "partially decrypted"), filed
apart from R179-R188 (items 2-11), which is why the catalogue listed it as a separate target (entry 250, "7 Jan 1736" =
the volume's start date again). It carries the same three attachments (DOC_R26_D1635, D3290, D3291) and five images.
Item 423/1 is in Lasry's decipherment and in `reading.txt` from the first session; checked 21 Sept 2026, nothing new to read.

## Prior art: it is already read

Every record carries the same pattern of attachments as Spagna 364D ([[nunzio1718]]):

1. the item's raw transcription (EHum/Matt F/NiLan, 2015-17), a bare digit stream;
2. `#KEY: reconstructed`, "ASV - S423", **George Lasry, 24 October 2020**;
3. a 68 KB file with Lasry's **segmented and deciphered** text of all eleven items.

So the cipher system was solved and the letters read in October 2020. The DECODE status and the catalogue's "what the
cipher hides is not known" were both out of date. Copies are in `decode/keep/`.

## The system (from Lasry's key)

- Fixed-length homophones, written as an undivided digit stream. Regular elements have **two digits**: letters, plus
  syllables such as `quel`, `per`, `non`, `gli`.
- **7 is a null**, except inside a nomenclator group.
- Nomenclator elements have **four digits beginning with 1** (1130-1985).

Lasry's filed key has **no nomenclator values at all**: every 4-digit group in his decipherment is printed as `<1222>`.
The corpus uses **166 distinct groups in 708 tokens**, 7.9% of the text.

## What this session adds

The 1736 nomenclator is **not alphabetical** (1222 = -mente, 1245 = -zione, 1882 = Spagna, 1935 = V.S.), so the bracketing
method used on 364D does not apply. Values were fixed from context alone. A value was accepted only when **every**
occurrence of the group reads with it, and most groups carry three to twenty occurrences. `key_extra.txt` has 48 lines
(47 groups). The measurement below was run before the last two were added, so it counts 46.

| | before | after |
|---|---|---|
| nomenclator tokens given a value | 0 / 708 | 424 / 708 (46 groups) |
| whole text read (9,001 tokens, nulls counted) | 90.6% | 95.3% |

(`python measure.py`. The 136 unread two-digit tokens are transcription gaps, "?" in the source.)

Selected values, each with the contexts that carry it:

| group | value | evidence |
|---|---|---|
| 1222 | -mente | somma-, diffusa-, pari-, facil-, destra-, sicura-, minuta-mente (44x) |
| 1245 | -zione | na-, situa-, esecu-, considera-, disapprova-, precipita-zione |
| 1655 | N.S. | "N.S. è rimasto sommamente amareggiato"; "ha N.S. lodato"; "le giuste istanze di N.S." |
| 1935 | V.S. | "scritte da V.S. in data dei ..."; "si manda a V.S. copia"; "non manchi V.S. di" |
| 1849 | S. Sede | "tumulti contro la S. Sede"; "i diritti alla S. Sede" |
| 1388 | Cort- | "illuminare codesta Corte"; "alle Corti di Spagna e di Napoli" |
| 1882 / 1606 | Spagna / Napoli | "alle Corti di Spagna e di Napoli"; "pensioni alla Corte di Napoli" |
| 1392 / 1240 | codest- / quest- | "codesta Corte" (Madrid) vs "questa S. Sede", "questa sera" (Rome) |
| 1242 | tutt- | "con tutta la sicurezza"; "di tutto ciò"; "impieghi tutta la sua destrezza" |
| 1241 | molt- | "con molta violenza"; "in molte guise"; "di molta conseguenza"; "dopo molti attentati" |
| 1259 | altr- | "degli altri"; "uno per la ... e l'altro per il"; "degli uni e altri" |
| 1320 | Brev- | "Brevi, uno per la [1828] e l'altro per il Sig. [...]"; "il Breve arrivi sicuramente" |
| 1863 / 1329 | Sig. / Card. | "Sig. Card. Acquaviva"; "il Sig. [1429] di Montemar"; "creando un Card." |
| 1234 / 1594 | Nunzi- / Ministr- | "i nostri Ministri, i Nunzi"; "attual Ministero di una Corte" |
| 1803 | princip- | "contro ogni principio di pietà"; "sul bel principio troncato"; "il cuore de' Principi" |
| 1885 / 1802 | stat- / prim- | "la Corte è stata sorpresa"; "il primo tumulto"; "arrivar prima gli originali" |
| 1692 | port- | "rapporti" (5x), "importante", "in Portogallo" |
| 1423 | dovre- | "non dovrebbero mai servire di esempio"; "non si dovrebbe mai temere" |
| 1908 | temp- | "da lungo tempo"; "da tempo immemorabile" |
| 1614 | notizi- | "se ne dà la notizia a V.S."; "una tal notizia può servire" |
| 1865 | grazi- | "alle grazie accordate"; "alle richieste grazie" |
| 1511 | giust- | "per giustificar poscia"; "le giuste istanze"; "più ingiuste cedole" |
| 1820 | Re | "cedola Reale"; "padronato Reale"; "Regalista" |

Less certain, carried by fewer contexts: 1208 cos-, 1210 restar, 1635 obblig-, 1925 Vescov-, 1239 ecclesiastic-,
1219 ancora, 1889 stess-, 1229 affinché, 1690 mi-, 1943 passat-, 1612 nomin-, 1608 maggior, 1238 quant-, 1231 anch-,
1693 poss-, 1818 inform-.

Open: 120 groups, most seen once or twice. Among them 1591 (16x; "la Maestà"? It fails in "gli arrolamenti [1591]i"),
1596 (11x; before "Molina" and the unread 1513-a-1382: probably "Mons." with a title of Gaspar de Molina, Bishop of
Málaga and Governor of the Council of Castile), 1236 (9x, a conjunction), and the date numerals 1953/1957/1960/1964/1985.

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: '## Reading' headings added to texts/423-2, 4, 6, 7, 8 and 10_reading.md, whose English headers the sweep had scored with the body: bodies plain 0.619-1.0, explicit 0.857-1.0. 423/3 had only Lasry's running text (reading_423-3.txt); texts/423-3_reading.md written from the b04 decode, word-divided: plain 0.667 (3 sentences), explicit 1.0, one run of three valueless groups. Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.

Closed items (moved out of Remaining gaps):
- 423/1 (R26) - closed 23 Oct 2026: read from its contemporary clear copy (ff. 284r-286r) and the figures, six transcription figures corrected on the images
- 423/9 "[..] danno", 423/11 "le la mede [..]" and "ben [..]giata" - closed 23 Oct 2026: cipherer's slips seen on the images; the copies read "Si danno", "l'esame de'", "bene maneggiata"

## Remaining gaps

- 11 nomenclator groups seen once in letters that read (1200, 1335, 1960, 1985 in 423/2; 1232, 1469, 1698, 1942 in 423/7; 1636 in 423/8) - blocker: needs-physical-access; no copy of 423/2, 7, 8 is among the DECODE attachments, the copies or minutes would have to be found in Spagna 423 itself
- 423/1 groups 1268, 1765, 1847 - blocker: too-short; one occurrence each, the words carried by the copy
- the minutes of these letters (Archivio della Nunziatura di Madrid) - blocker: needs-physical-access

## Content

The letters are Clement XII's Secretariat to the nunciature during the **1736 rupture with Spain**. Spanish recruiting
officers ("arrolamenti", "ingaggiature") in Rome and the Papal State set off riots in Trastevere and at Velletri. The
letters cover the tumults "contro la S. Sede", Cardinal **Acquaviva** (Spain's protector), the Duke of **Montemar**, the
Bishop **Molina** "scordatosi degli obblighi di Vescovo", the Corti di Spagna e di Napoli, and the Dataria and pensions.
From October on they turn to the *padronato reale*, the "Regalista" doctrines of the Madrid junta, Briefs to the King and
Queen, and the nomination to cardinals' hats ("col maggior numero di cappelli").

## Files

- `decode/rec179-188.htm`: the DECODE record pages. `decode/DOC_*`: all attachments and page images (git-ignored).
- `decode/keep/`: Lasry's key and decipherment and the per-item transcriptions (kept).
- `corpus.py`: parses Lasry's aligned decipherment into `seq.json`. `ctx.py`: context viewer. `measure.py`: coverage.
- `key_extra.txt`: the groups valued here. `reading.txt`: the running text with those values applied.

## Escalation

Added by the reading audit (22 Oct 2026); worked through in the re-read of 22 Oct 2026 (batch b04).

- [x] siblings: R179-R188 and R26 are the whole series; read together, the key corrected across all of them
- [x] clear-pages: the 26 IMG pages carry no decipherment; 23 Oct: the 'cleartext' png attachments hold the contemporary clear copies of 423/1, 4, 5, 6, 9, 10, 11
- [x] known-keys: Lasry's "ASV - S423" is the only key; corrected (25, 30, 69, 93) and its nomenclator extended
- [x] print: web search, no edition of the 1736 ciphers to Guiccioli; minutes in the Madrid nunciature archive, not online
- [x] key-rebuild: four earlier nomenclator values replaced, about 65 groups valued from context (texts/b04_key_additions.txt)
- [x] retry: 423/2 and 423/4-11 re-read 22 Oct; 23 Oct every attachment opened at full resolution, the clear copies found and aligned, 423/1, 5, 9, 11 read, every open group retried with the extended key (12 tokens left, each seen once)

## Read share over cipher words only (16 Nov 2026)

Checked, no change. Each reading (`texts/423-N_reading.md`) holds the deciphered text alone; the clear copies
(`423-N_copy.txt`), the notes and the translations are separate files, so no clear words had to be separated.
`research/reading_audit/v10_relabel.py` over the reading bodies gives the recorded figures (423/1, 5, 9, 11 1.0;
423/2 and 3 0.970; 423/4 and 6 0.993; 423/7 0.926 read in part; 423/8 0.956; 423/10 0.964); class unchanged. No measure
declaration is needed or possible: there is no clear text in the files to mark. Left for the coordinator, not
changed: in 423/1, 5, 9 and 11 some words follow the contemporary clear copy where a single figure is a cipherer's
slip (about 15, 2, 6 and 8 words, listed in each reading's notes); the readings do not mark them as holes, and they
would count as holes only if the one-digit slip rule is read as needing a surviving period key even where a clear
copy gives the word.
