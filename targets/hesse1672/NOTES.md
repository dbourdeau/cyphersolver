# Hamburg letter to the Hessian chancellor, 4/14 May 1672 (HStAM 4 f Dänemark Nr. 125, ff. 2-4; HCPortal 494)

Catalogue item 341. Opened and worked 9 Oct 2026 (one session, claude-opus-5-5). Outcome: read in part (92.2% of
cipher tokens as sense, measured); one five-sign word open.

## The document

- Hessisches Staatsarchiv Marburg, Best. 4 f (Staatenabteilung: Dänemark), Nr. 125, ff. 2-4. HCPortal record 494
  (`api.hcportal.eu/api/cryptograms/494`, created by Eugen Antal, 20 Nov 2025): "Message containing encrypted parts",
  nomenclator, German, 4 May 1672, sender and recipient "Unknown", solution "Partially solved". Three images
  (media 1385-1387, 2600 x 3950), saved as `images/f2.jpg`, `f3.jpg`, `f4.jpg` (git-ignored). `record494.json` is the
  API record.
- A signed despatch in German (Kurrent, with Latin and French words in Latin script), dated at the foot "Hamburg den
  4/14 May 1672", addressed "Hoch Edler Herr, Mein insonders hochgeehrter Herr Canzler" — the Hessian chancellor at
  Kassel. The signature is not made out here. Topics: the writer's reception at the Danish court (the King of
  Denmark, the Danish ministers), Blumenthal's mission (code 630) and Brandenburg-Danish ceremonial quarrels, the
  French-Swedish treaty that passed Denmark by, the plan to draw Brandenburg into the Danish-Brunswick alliance
  ("Foedus Dano-Brunsvicense"), the Holstein Landtag's refusal of contributions, and an alliance concluded at Hamburg
  by the Duke of Plön between Brunswick and Denmark.
- Cipher: 26 nomenclator numbers (303-834) in the clear text, and two short letter-cipher passages on f. 4r
  (38 signs: two-digit numbers, doubled capitals, syllable signs).
- **Glosses on the leaf.** A second hand (black ink, Latin script) wrote the meaning over almost every code number
  ("K. Dennemarck", "Curbrandenburg", "Berlin", "Hollandt", "Gen. Staden", "Franckreich", "Sueco", "alliance",
  "Herzog von Ploen", "Rey Danae", "Blumenthal"), noted "Schweden 768", "625", "Holstein" in the margins, wrote
  "disgustirt und ertarin holstein" in the margin beside passage 1, and put partial letter glosses over passage 2
  ("Sueco", "g ott", "ge b", "d a s", "amm", "wo", "a b l aut"). This is what HCPortal's "Partially solved" refers
  to. The hand is not dated; it could be the recipient's chancery or a later archivist.

## Prior work (contamination question)

- Found before the attempt and used: the glosses on the leaf (codes and parts of both passages).
- HCPortal 494: "Partially solved", no transcription or key attached (`digitalized_transcriptions` empty,
  `cipher_key_id` null).
- Searched 9 Oct 2026: web (letter, Hamburg 1672, Blumenthal, Plön, Dano-Brunswick alliance, Hessian chancellery
  cipher), HCPortal cryptograms list (only 494 from 4 f Dänemark), Antal & Mírka's HistoCrypt paper on the Marburg
  keys (Thirty Years' War, not this letter), Klausis Krypto Kolumne (Rabenhaupt 1646 from 4 d). No published reading
  of this letter found. Lasry, Tomokiyo (cryptiana) and Kopal: nothing on this document.

## The key

- **HCPortal key 255** = HStAM 4 d Nr. 1234, images 13-16 (`api.hcportal.eu/api/cipher-keys/255`, "used around
  1666"). The back sheet reads (roughly) "Clavis ... mit Secretario Lincker 1666. Item 1676 mit dem Herrn ...".
  Its letter table: A 20 30 40 50 60, B 22 32 ..., C 24 ..., D 26 ..., E 28 ..., F 21 31 ..., G 23 ..., H 25 ...,
  I 27 ..., K 29 ...; L 70 80 90 100 110, M 72 ..., N 74 ..., O 76 ..., P 78 ..., Q 71 ..., R 73 ..., S 75 ...,
  T 77 ..., U 79 ...; W 120 130 ..., X 122 ..., Y 124 ..., Z 126 ...; doubled capitals CC=a, DD=b ... (LL=i,
  NN=l, WW=t, XX=u, YY=w); syllable signs for au eu ei ie ii ou ch ck ct ff ll mm nn pp rr sch ss sp st tt tz;
  nulls 1-19 and a list of three-digit numbers. Key 254 (Nr. 1234 f. 12, "Scala über den Clavem mit Secretarium
  Lincker") is its deciphering table and confirms LL=i ... XX=u.
- Key 255's **nomenclature does not fit** this letter (there Alliance = 311, Dennemarck = 184/212, codes 180-407),
  so the 1672 letter used the same letter table with a different word list (codes 300-830). The word list is not
  on HCPortal; the glosses supply the code values.
- Found by fetching all 319 HCPortal key records, filtering the Marburg 4 d / 4 f keys (106) and looking at their
  first pages in contact sheets (`scratchpad`, not kept): the family with homophone numbers 20-166 and doubled
  capitals is 253, 254, 255 and 266; 255's table reads the glossed letters of passage 2 without a change
  (63 g, 38 e, 22 b, FF d, 20 a, 75 s, 96 o, NN l, 50 a, 32 b, 110 l).

## Transcription

- `ct.txt`: the two letter-cipher passages (38 signs + the codes 634 and 768 they contain), from full-resolution
  crops. In this hand 6 looks like b and 2 like r: "b7" = 67, "ro" = 20, "bb" = 66. The sign after XX in passage 1
  ("6∂") is the key's syllable sign for **st**; the sign after 76 in passage 2 ("e∂") is its sign for **tt**.
  `[I]` in passage 2 is an unclear sign read as the **ll** sign (M).
- `codes.txt`: the 26 code numbers with their glosses. 630 was first read 650/680; the middle digit is the
  hand's long-tailed 3. 576 has a stroke over the 7 ("57ˣ6"); read 576 with the gloss "Franckreich".
- `decrypt.py` applies key 255's letter table to `ct.txt`.

## Reading

`reading.txt`. Passage 1 (after clear "Totaliter"):

> Totaliter disgustirt und ?? [e r t a d] in Holstein, nun sowohl als in Dennemarck Adell, Bürger und Bauern nun
> aller orten in plainten combiniret

FF d, 67 i, 85 s, 33 g, XX u, [st], LL i, 113 r, WW t = "disgustirt"; 119 74 26 = "und"; 37 104 = "in"; 634 =
Holstein. The five signs 28 83 117 20 66 decipher as e r t a d and make no German word; the glosser read the same
place as "ertarin".

Passage 2 (after clear "insidiosus hostis"):

> Sueco: Gott geb das all wol ablauff

768 = Sueco; 55 76 [tt] = "Gott" (55 is h in the table, a slip for 53 g; the gloss reads g); 63 38 22 = "geb";
FF 20 75 = "das"; 20 [I] = "all" (M); YY 96 NN = "wol"; 50 32 110 8 XX = "ablauff" if 8 is the key's **au** sign
and XX here its **ff** sign (both look-alikes; by the key a plain 8 is a null and XX is u) (M).

Code 602: the glosser wrote "Haus Braunschweig", struck it and wrote "Kayser" over "447. 602."; the same line has
447 641 = "Herzog von Ploen", and the clear text above names the "Foedus Dano-Brunsvicense", so 447 602 = Herzog
[von] Braunschweig and the alliance is between Brunswick and the King of Denmark (834 "Rey Danae"). Grade I.

Measure: 64 cipher tokens (38 letter signs + 26 codes). All 64 have a value; 59 read as sense = **92.2%**. Below
the 95% read bar, so read in part.

## Remaining gaps
- passage 1, five signs 28 83 117 20 66 (decipher e r t a d) before "in Holstein" - blocker: too-short; the key reads them unambiguously, they make no word, the contemporary glosser failed at the same place ("ertarin"); an LM search allowing up to two copy slips (`search_gap.py`, de-1640s) gives nothing convincing, and no second copy of the letter is online

## Escalation
- [x] siblings: HCPortal has no other leaf of 4 f Dänemark Nr. 125; the rest of the file (other despatches of the same writer) is not digitised
- [x] clear-pages: the glosses on the leaf are the only decipherment; used for codes and passage 2
- [x] known-keys: all 106 Marburg 4 d / 4 f keys on HCPortal screened; key 255 (Lincker 1666/1676) letter table fits; its nomenclature does not
- [x] print: web search for the letter, Blumenthal 1672, the Dano-Brunswick alliance and Plön; nothing printed found
- [x] key-rebuild: code values taken from the glosses; 602 inferred from the struck gloss and the clear "Foedus Dano-Brunsvicense"
- [x] retry: the five open signs re-read at full resolution and run through `search_gap.py` (single and double slips); no word

## Steps (9 Oct 2026)
1. Fetched HCPortal record 494 and the three images.
2. Read the leaf: clear German despatch, code numbers with interlinear glosses, two letter-cipher passages on f. 4r.
3. Web and HCPortal search for prior readings: none beyond the glosses.
4. Read the passage glosses: margin "disgustirt und ertarin holstein"; passage 2 "Sueco / g ott / ge b / d a s ...".
5. Tried reading passage 1 against the margin gloss with doubled letters as nulls and as letters: inconsistent.
6. Screened key 255 (1666): letter table and doubled capitals of the same type; nomenclature different.
7. Fetched all HCPortal key records; screened the 106 Marburg 4 d / 4 f keys in contact sheets; only the 253/254/255/266
   family is of this type; 255's table (with 254's Scala) reads the glossed signs of passage 2 unchanged.
8. Identified the syllable signs st and tt; passage 1 reads "disgustirt und ... in Holstein", passage 2 "Gott geb das
   all wol ablauff".
9. Transcribed all code numbers with glosses (`codes.txt`); 602 from the struck gloss and context.
10. LM search (de-1640s) for the five open signs with up to two slips: no convincing word.
