# 1567: independent verification

Written 2 Nov 2026. No solver file was changed. All sign reading here was done by AI language-model readers viewing
images. No human palaeographer has checked it.

## Verdict: confirmed with corrections

- The key and the system are confirmed. The Italian is real, and the five letters are what the solver says they are.
- The sign transcriptions of cc. 9, 16 and 20 are overclaimed. They carry whole-word sense repairs and invented signs.
- Entry 1567 as a whole is not read. Seven of its 13 letters were opened.
- "Not printed before" is not established. Doglio could not be opened, and the addressee's own cipher tables appear to
  survive at Reggio Emilia.

## 1. Blind test

Method. I chose 14 cipher lines (c. 9r l. 13-16; c. 16r l. 16-19; c. 20r l. 8, 9, 12, 16, 17, 18), 529 signs, from fresh
crops of the raw scans, and recorded them before opening any transcription. Two reads were made:

- Own read. It is not fully blind: the sign inventory prints the key, and I recognised plaintext while reading.
- Key-free read. A separate AI reader got the same crops and a shuffled sign sheet with ids S01-S20. It had no values and
  was told not to reason about language. This is the true blind test.

Both reads were saved before the solver's files were opened. They are in the appendix.

| Letter | Solver signs in sample | Own read differs | Key-free read differs |
|---|---|---|---|
| c. 9r | 167 | 4 (2.4%) | 12 (7.2%) |
| c. 16r | 143 | 8 (5.6%) | 15 (10.5%) |
| c. 20r | 219 | 4 (1.8%) | 9 (4.1%) |
| All | 529 | 16 (3.0%) | 36 (6.8%) |

Counts are alignment differences (`difflib`). Nine of the 36 key-free differences are the reader merging the two V
signs (n and h); without them the rate is 5.1%.

The main result: the key-free read, passed through `key.tsv` afterwards, gives Italian. That reader had no key and no
language. Examples: `dicorregggiosonopessimamenteincaminate`, `taalcontedicollalto`, `gnorducadellamirandolaequellidelprincipedel`.
This confirms the key on cc. 9, 16 and 20, which the solver's own check supported only as a whole.

After 5x zooms, about 15 of the 529 signs (2.8%) in the solver's text are wrong or are unmarked repairs: c. 9r 3,
c. 16r 9, c. 20r 3. Most sit in places where both blind reads agree against the solver. Applied to the 2904 single-pass
signs, that suggests something like 60-100 sign problems across cc. 9, 11, 16 and 20, unevenly spread. c. 16 is the
worst. This is an extrapolation from 14 lines, not a count.

Errors on my side, found on zoom: c. 9r l. 16 is the short h sign, so the solver's `v` is right ("havete"). My first
pass at low zoom also misread two c. 16r signs, which I corrected before comparing. c. 16r l. 19, last sign, is unresolved
(`V` or `x`-like, at the torn edge); the solver's `V` ("in") is plausible.

Shape-weak pairs: V/v (n/h) in all hands, and tailed 3 against g in the H-type hand. Some of these calls rest on sense,
and a sign-by-sign transcription should say so.

## 2. Decryption rerun

My own script decrypted all seven transcriptions from `key.tsv`: 4143 signs, 112 lines, 0 differences from the decryption
files. Word counts match the NOTES table (106, 248, 60, 207, 51, 54, 67). This shows internal consistency only. For
cc. 9, 11, 16 and 20 the transcription was re-encoded from the reading, so transcription, decryption and reading are one
source, and `verify_reading.py` passing proves nothing about the signs.

I also read c. 22 from the image. It agrees with the c. 23r decryption, including the extra "molto", the struck "sito" and
"e Dio vi contenti". The opening of c. 15 agrees with c. 13r, including "quindicimila" against the cipher's "quindecimila".

## 3. Sense repairs found, none marked in the solver's files

| Place | Signs on the page | Solver has | Effect |
|---|---|---|---|
| c. 9r l. 15 | `+ T g V T V c N V T`, "vegnendone" | `+ T c T V c N V T`, "vedendone" | **Meaning.** "If the occasion comes" (vegnendone il taglio), not "seeing how the cut falls" |
| c. 16r l. 16 | `4 A V g + x 3 2 A c T 4`, "l'angustia del" | `4 N x 3 A 3 N c T 4`, "lo stato del" | **Meaning.** "You know the straits of the country". A whole word replaced by an expected one; two signs short |
| c. 16r l. 6 | line ends `+ T 9`, then blank paper | `+ T 9 # T 9`, adds "[?per]" | **Invented signs.** The solver's doubtful "per" is not on the page. Read "d[i a]ver da noi danari" |
| c. 16r l. 19 | `... 2 N # N x x 2 A o N` | adds `T` | **Invented sign.** The "e" before "possiamo" is not on the page |
| c. 16r l. 18 | `... D 2 D A 4 4` | `... D 2 A 4 4 A` | A `D` dropped: "esimerci c all'alloggio", a slip for "dall'alloggio". Also the first `A` of "alloggio" belongs to l. 19, not l. 18 |
| c. 20r l. 12 | `t + D 4 2 r 2 D`, "qucl-" | `t + A 4 2 r 2 D`, "qual-" | Writer's slip silently corrected |
| c. 20r l. 12 | `D N V 3 A V 7 T`, "circontanze" | `D N x 3 A V 7 T`, "circostanze" | Writer's slip silently corrected |
| c. 20r l. 12 | blot over one sign | `o`, unbracketed | Restoration not marked |
| c. 9r l. 14 | A-shaped sign with a blot at its foot | `D`, "oculato" | Sense needs c; both blind reads see A. Mark as `[c]` |

The solver's slip list leaves all of these out, while "coni" (c. 16v l. 2) is kept as written. The treatment is not
consistent. NOTES says the words-read count excludes every word with a restored letter; that is not true until these
are marked.

Doubtful spots that held on zoom: "compiamo" (c. 7r l. 14), "confidenui" (c. 9r l. 17), "coni" (c. 16v l. 2), "roliet"
(c. 9v l. 8, signs certain, sense open; a blot also sits after "alle" in that line) and "qrincipe" with "del principe
del" (c. 20r l. 17-18, both blind reads agree). "Servirà" (c. 16r l. 8) agrees as far as the line runs. c. 11r was not
sampled.

## 4. Sense and history

- The cipher reads as real chancery Italian of the period. Sentence structure, idiom and spelling are consistent across
  the five letters, and the corrected places read better than the solver's text.
- The letters agree with the clear text around them. c. 20r: "Non è compatibile col nostro servigio..." leads straight
  into the cipher on Mirandola and Correggio.
- Missed by the solver: c. 9r is marked "Duplicato" at top left, and the clear text of c. 20r says the Venice courier was
  robbed at the Gradisca border, that dispatches may have been intercepted, and that duplicates are enclosed. So c. 9 is
  probably one of those duplicates. This is independent support and belongs in the summary.
- Outside the file: the Reggio Emilia State Archive inventory, seen as a search-engine extract, describes papers of
  Ottavio di Stefano Bolognesi (1580-1646) on affairs handled for the princes of Correggio and the dukes of Mirandola,
  Savoy and Modena. That explains "vostro principe naturale" (c. 7r) and the reproach in c. 20. It is strong confirmation
  and is not in NOTES.
- Britannica confirms the Emperor's 1630 condemnation of Siro da Correggio. Later steps differ by source (1634, 1635, 1641).
  The rest of the historical context in NOTES is still unchecked, which falls short of Dan's rule 4.
- "Vienna" rests on c. 22, a later hand. The originals give only "Bolognesi" at the foot (c. 9r, c. 16r).
- English: c. 9r and c. 16r need the two meaning changes above. "Sua Eccellenza" (c. 11r) is unidentified and should be
  listed as open.
- NOTES groups c. 7r with the zigzag-N hand. c. 7r l. 13-14 show the H-type N and alpha s, so it belongs with c. 13r and
  c. 16.

## 5. Status under the 95% rule (cipher passages only)

| Document | Solver | Corrected | Status |
|---|---|---|---|
| c. 7r | 105/106 | unchanged, only l. 13-14 spot-checked | read |
| cc. 9r-v | 244/248 | 243/248 = 98.0% | read |
| c. 11r | 59/60 | unchanged, not sampled | read, least tested |
| cc. 16r-v | 198/207 | 195/204 = 95.6% | read, thin margin, may move on re-transcription |
| cc. 20r-v | 50/51 | 50/51 as sense; 47/51 if restored letters are excluded | read under Dan's wording |
| c. 13r | 52/54, first 8 lines only | rest of c. 13r, c. 13v and c. 14r not transcribed | transcription job, read in part |
| c. 23r | 67/67 | unchanged | transcription job, read |

These figures cover only the places I checked. "Read" applies to the cipher. Each letter's clear text is only partly
transcribed, so no whole letter is read yet. **Entry 1567: read in part, 7 of 13 letters.**

## 6. Prior art: not settled

Could not open: Doglio, *Lettere*, vol. I (no scan found; HathiTrust search and catalogue HTTP 403; Google Books API 429 and
Google Books search blocked); Doglio, "Intorno alle lettere edite e inedite di Fulvio Testi", *Lettere Italiane* 16
(1964), 425-444 (JSTOR); the Reggio Emilia inventory page (DNS failure, known only from search extracts). Two Internet
Archive title searches returned nothing.

So it is unknown whether any Feb-Mar 1630 letter is printed. Note that these are ducal letters countersigned by Testi, and
I could not establish whether Doglio includes such letters.

Found:

- No Campori edition of Testi's letters turned up, and Wikipedia's list of editions names none. Treat it as unconfirmed.
- Other editions listed there, none opened: *Opere scelte* II (Modena 1817), https://books.google.com/books?id=uWwWyA4FkpYC ;
  letters to Sassatelli (Modena 1841); "Lettere inedite", *Memorie di Religione, di Morale e di Letteratura* XV-XVI (Modena
  1843), https://books.google.com/books?id=cMwaAAAAYAAJ&pg=RA1-PA333 ; Lazzari (Faenza 1872). The 1843 volumes should be
  checked first.
- **The key may survive.** The same inventory extract says "I cifrari del cav. Ottavio Bolognesi si trovano uniti alle
  carte" on his affairs, in the Archivio Bolognesi, Reggio Emilia. Source:
  https://archiviodistatoreggioemilia.beniculturali.it/getFile.php?id=810 . His papers may also hold clear copies.
- A book on Bolognesi as a diplomat exists, known only from a garbled extract. Title not found.
- Archivio di Stato di Modena keeps 8 buste of ciphers, and the Este court used separate ciphers per correspondent
  (https://www.filodiritto.com/la-parola-incognita-cifre-e-cifrari-alla-corte-estense). No link to these letters was found.

The later hand. c. 15 and c. 22 look like one hand by eye. It is not contemporary, so the phrase "no contemporary
decipherment" in the reading headers misleads. c. 22 is headed "Copia dall'autografo". On c. 15 the words that stand in
clear in c. 13r are underlined, so the writer had the cipher leaf in front of them and could read it: someone before us
knew this key. I found no evidence that this was Campori; his collection stamp proves ownership only, and no sample of his
hand was compared. The solver found no other decipherment in this file. Whether that person deciphered more, or
published, is open.

## 7. Catalogue ids

The 13 letters in the entry:

- Opened, seven in Lettera T: cc. 7-8, 9-10, 11-12, 13-15, 16-17, 20-21, 22-24, all 1630. Their manifests confirm these
  shelfmarks and title them to Bolognesi. The catalogue marks cc. 13-15 "Destinatario incerto".
- Not opened, six in Lettera F: c. 53 (22 Jul 1634), c. 54 (25 Jul 1634, reply), c. 72 (1 Feb 1636), cc. 73-74 (2 Feb 1636),
  c. 4 (25 Oct 1642), cc. 5-6 (25 Oct 1647).

My searches of the Lodovico site returned result pages from which I could not extract records, so the Lettera F scans remain
unlocated. Nothing shows whether they use this key. The addressees differ and the Este practice was one cipher per
correspondent, so assume a different key until seen. Do not confuse Lettera F cc. 5-6 with Lettera T cc. 5-6, which the
solver checked and found without cipher. The catalogue's vetting note also needs correcting: the versos are not blank, and
c. 9 alone has 1273 signs.

## What must be fixed before this goes to Dan

1. Re-transcribe cc. 9, 11, 16 and 20 sign by sign from the images, then compare with a key-free reader. Rule 1 asks for a
   transcription, and these are re-encoded readings. Then recount.
2. Apply section 3, mark every slip and restoration, and fix the English.
3. Claim 7 of 13 letters and "read in part" for the entry. State that "read" means the cipher only.
4. Say that prior art is open, and name Doglio, the 1843 *Memorie* and the Reggio cipher tables. Do not claim the reading
   is new.
5. Correct "contemporary", the hand grouping and the Vienna sourcing. Add "Duplicato", the Gradisca courier and the
   Bolognesi inventory.

## Appendix: the blind reads as saved

Line ids: a1-a4 = c. 9r l. 13-16; b1-b4 = c. 16r l. 16-19; c1 = c. 20r l. 8; c2 = l. 9; c5 = l. 18; c6 = l. 17; c7 = l. 16; c8 = l. 12.

Own read, sign codes as in `key.tsv` (`?` illegible), unaltered. Later zoom showed that the `V` at "havete" in a4 should be `v`:

```
a1 r T x x A T D v T # T 9 A 4 3 9 N o T 9 2 3 A 4 A V N x 3 9 A 2 x t + 2 x 2 3 A
a2 c 2 + N 7 2 N V T x A 9 A / T V T D v T + N 2 x 3 2 A 3 T N A + 4 A 3 N T D v T
a3 + T g V T V c N V T 2 4 3 A g 4 2 N V T r A D D 2 A 3 T D N o T c 2 + N x 3 9 N x T V
a4 x N t + A 4 D v T 3 N D D N A t + T 2 o 2 V 2 x 3 9 2 D v T + N 2 V A + T 3 T # T 9 # 2 +
b1 3 T D 2 9 D A 2 4 c T V A 9 N + N 2 x A # T 3 T 4 A V g + x 3 2 A c T 4
b2 # A T x T N 4 3 9 T 4 A g 9 N x x A x N o o A D v T x 2 T x / N 9 x A
b3 3 A A 4 D N V 3 T c 2 D N 4 4 A 4 3 N # T 9 T x 2 o T 9 D 2 D A 4 4
b4 A 4 4 N g g 2 N # N x x 2 A o N D N V + T 9 2 3 A A x x T + T 9 A 9 T D v T 2 x
c1 g 2 A + N 2 x 3 T x x N + T c T 3 T D V T 4 T D N x T c T 4 # 9 2 V D 2 # T
c2 c 2 D N 9 9 T g g 2 N x N V N # T x x 2 o A o T V 3 T 2 V D A o 2 V A 3 T
c5 t 9 2 V D 2 # T c 2 D N 9 9 T g g 2 N x 2 A V N # 9 T x T V 3 T o T V 3 T c 2 x
c6 g V N 9 c + D A c T 4 4 A o 2 9 A V c N 4 A T t + T 4 4 2 c T 4 # 9 2 V D 2 # T c T 4
c7 t + A V 3 N g 4 2 A r r A 9 2 c T 4 x 2
c8 x 2 A V N t + D 4 2 r 2 D A 3 2 c A g 9 A V c 2 x x 2 ? T D 2 9 D N V 3 A V 7 T #
```

Own read through the key:

```
a1 c. 9r l. 13 fessaecheperaltromeritalanostraisquisita
a2 c. 9r l. 14 diuozionesarabenecheuoistiateoaulatoeche
a3 c. 9r l. 15 uegnendoneiltaglionefacciatecomediuostrosen
a4 c. 9r l. 16 soqualchetoccoaqueiministricheuoinaueteperpiu
b1 c. 16r l. 16 tecircaildenarouoisapetelangustiadel
b2 c. 16r l. 17 paeseoltrelagrossasommachesiesborsa
b3 c. 16r l. 18 taalcontedicollaltoperesimercicall
b4 c. 16r l. 19 alloggiopossiamoconueritaasseuerarecheis
c1 c. 20r l. 8 giauoistessouedetecnelecosedelprincipe
c2 c. 20r l. 9 dicorreggiosonopessimamenteincaminate
c5 c. 20r l. 18 qrincipedicorreggiosianopresentementedis
c6 c. 20r l. 17 gnorducadellamirandolaequellidelprincipedel
c7 c. 20r l. 16 quantogliaffaridelsi
c8 c. 20r l. 12 sianoquclificatidagrandissi?ecircontanzep
```

Key-free read through the key, applied after the read was finished (the doubled g and the `oo` for `ff` are that reader's errors):

```
a1 fessaecneperaltromeritalanostraisquisita
a2 giuozionesarabenecneuoistiateoaulatoecne
a3 uegnenaoneiltaglionefacciatecomedgiuostrosen
a4 soqualcnetoccoaqueiministricneuoinaueteperpiu
b1 tecaircaildenarouoisapetelantustiadel
b2 paeseoltrelagrossasommacnesiesborsa
b3 taalcontedicollaltoperesimercicall
b4 aulsggiopcssiamoconuerigaagsseuerarecnei
c1 giauoistessouedetecnelecosedelprincipe
c2 dicorregggiosonopessimamenteincaminate
c5 qrincipedicorregggiosianopresentementedis
c6 gnorducadellamirandolaequellidelprincipedel
c7 quantogliaooaridelsi
c8 sianoquclioicatidagrandissi?ecircontanzep
```
