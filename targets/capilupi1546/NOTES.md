# capilupi1546: Ippolito Capilupi to Ferrante Gonzaga, two cipher letters of May [1546], system Y read with a substitution of 1-2 digit codes (Estense, Autografoteca Campori, cc. 80a-80h; catalogue 1555)

Status: in progress (Brice Dudout, 12 Nov 2026; integration check 13 Nov 2026). System Y is read in part (strict share 91.2 %), several steps are untried, and no write-up page has been made.

- **System Y** (the cursive hand: images 02r, 04r, 05r, 05v, 06r, 06v, 07r) is read in part. Strict share (README rule, sure words only): 631 of 692 = **91.2 %**. The contributor's own figure counts the 37 probable words as read: 668/692 = 96.5 %.
- **By document, strict:** 02r 92.2 %, 04r 96.6 %, 05r-05v 87.3 %, 06r-07r 90.6 %. Only 04r (118 words) reaches the 95 % bar.
- **System X** (images 03r and 09r, about 1,400 digits) is a different hand and system and is not attacked.
- **The key** was proposed by Claude Fable 5.2, frozen, and passed one preregistered measure on the held-out folio 05r: M = 0.7962 against 200 controls (max 0.175).
- **No human palaeographer** has checked the transcription or the reading.

## The document

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera C, Capilupi Ippolito, sfasc. I, cc. 80a-80h (catalogue 1555, Daniel Bourdeau). Ippolito Capilupi writes to Ferrante Gonzaga. There are two letters, according to the dockets:

- images 01-02: 'Capilupo da Civitavecchia 17 mayo' (no year on the docket);
- images 03-09: 'M. Hipp.o Capilupo di Roma alli 10 di maggio', received '7 giugno 1546'.

**Image labels.** The labels used here (01 to 09, with r/v: 02r, 03r, 04r, 05r, 05v, 06r, 06v, 07r, 09r) follow the order of the Lodovico images of cc. 80a-80h. Which carta (80a ... 80h) each label corresponds to has not been checked. It is listed as a gap.

**Images.** Estense Digital Library (Lodovico), CC BY-NC-SA, linked and not committed. The capilupi1545 notes give the IIIF manifest of 'Ippolito cc. 80a-80h' as `https://edl-jarvis.cultura.gov.it/meta/iiif/9c9aab5c-5ed0-4533-a6a0-7b2022ec53c7/manifest`. It still has to be confirmed that this is the record our images came from.

**Date.** The second docket gives 1546 as the year of receipt. The content points to 1545:

- the marriage of Vittoria Farnese with the duke of Orléans is still in play (Charles of Orléans died on 9 September 1545);
- the Milan negotiation is under way;
- the priory of Barletta appears here and in the docket of Camillo Capilupi's letter of 8 May 1545 (capilupi1545).

Either our reading of the docket's year or the docket itself needs checking. The target is named after the catalogue date.

## Two systems

**X (images 03r, 09r).** Careful digits, frequent overlined 9 and separator strokes. On 03r, clear Italian runs between the cipher passages ('tengo per fermo', 'fatta innanzi et offertagli loro come scrissi', 'non sarebbe forse male ricordarle', 'accio che facesse').

A second hand added pale superscript letters over some digits:

- 03r line 1: 8^i 1^c 0^r 9^n 7^a 8^r;
- 03r line 3: 8^i/t 0^s 9^u 7^c 8^i 8^i;
- 03r lines 13 and 16: further letters;
- 09r: k, r, n, l, c, e, t, v, and '9^c 5 8^l 7' twice.

This is a partial period gloss, but it cannot be aligned: 8 carries i on 03r and l on 09r, and no word can be read from it. No crib was drawn from it. X has about 1,400 digits, too short to break alone, and was not attacked.

**Y (the other folios).** A cursive hand with no overlines. The decisive transcription point: the hand has two signs shaped like 7, a short 7 with a flat bar (= 7) and a long descending hook like ')' (= 9). A loop on a stem is 4. Without this distinction the text cannot be used.

Y has the same absent digit pairs (09, 99, 53; 73 nearly absent) and the same recurring units (9170, 1951+even, 7939+even) as Camillo Capilupi's letters c. 48 and c. 49r in `../capilupi1545/` (WAINUT). It is the same numeric system. It is not the homophonic alphabet of Camillo's letter of 8 May 1545 there.

## The key (system Y)

This is a simple substitution with codes of one or two digits, with no homophones and no nomenclator (`dudout/key.txt`):

| Group | Codes |
|---|---|
| Vowels (even digits alone) | 0 i, 2 o, 4 e, 6 a |
| Odd digits alone | 1 m, 3 n, 5 s, 7 r |
| Two-digit codes | 13 z, 15 t, 17 l, 19 q, 29 p, 39 h, 49 g, 51 u/v, 59 f, 69 d, 79 c, 89 b |
| Nulls | 8 and 9 alone, and 31 |

- There is no word division. The text is parsed longest code first.
- The frozen file KEY-1555.json (SHA-256 76ab7684...955e) also lists about 2,000 composite entries of 3-7 digits. They fix how the longest-match parse cuts ambiguous strings. Some are irregular as frozen. They were used unchanged, and `dudout/key.txt` lists the irregular ones.

**Open point on code 11.** Code 11 reads 'mm'. In five places 'mm' stands where t or l is needed:

- dargmmi = dargli (04r);
- imperammor = imperator (05r);
- demmo = deto (05r, 06v);
- inmmender = intender (06r).

Related: 'mignor' for 'signor' twice (06r, 06v). This is either a transcription confusion between two signs of the hand or a code the key lacks. It is to be checked on the images.

## How it was done

1. **Transcription.** Two blind passes by 12 Claude Opus 5.5 agents, each using a different cropping method. The first passes merged the two 7-shapes and were redone.
   - Agreement between passes: 98.5-99.8 % per Y folio, 93.5 % on 03r, 85 % on 09r.
   - 150 differences were arbitrated on the image, with no key.
   - The transcription was frozen on 12 Nov 2026 at 20:07 CET.
2. **Protocol.** `dudout/PREREG-1555.md` was frozen at 19:35 CET (SHA-256 b7c34cfe...8c49, with `dudout/measure_1555.py` b65938e6...c49c), before any key-building.
   - The held-out portion is all of 05r. It was excluded by name from the build scripts and from the package sent to Fable (leak check: 0 leaks, positive control).
   - One measure: M is the share of decoded letters covered by Italian words of 3 letters or more. The 200 controls permute the plaintext values among the key's codes.
   - PASS requires M > max(controls) and M >= 0.60.
   - One run only, behind a readability gate on the training folios.
   - Before the freeze, only structural counts and one vowel-skeleton test on 06r+06v had been made.
3. **Claude Opus 5.5 failed.** The build set was Y without 05r, Camillo Capilupi cc. 44r-44v (a working dossier of ours, not submitted) and the capilupi1545 transcriptions of c. 48 and c. 49r: 5,110 digits in all.
   - A homophonic anneal with unit = letter scored -2.46 to -2.69 per letter, and restarts diverged.
   - A syllabic consonant-vowel model either degenerated or gave four different vowel tables in four restarts.
   - Nothing was frozen.
4. **Claude Fable 5.2 (API)** proposed the key above from that package. It was frozen unchanged as KEY-1555.json at 20:56:15 CET (SHA-256 76ab7684...955e).
5. **Gate.** Our script decodes training folio 04r into continuous Italian ('Salviati mi ha detto che sua nipote moglie del conte di Santa Fiore...'). Fable's decodings of 02r and 06r read the same. Result: readable.
6. **Measure.** One run on 05r at 20:58 CET: M = 0.7962; the 200 controls had max 0.175 and mean 0.018. **PASS** (`dudout/MESURE-1555-H.txt`, verbatim).
7. **Count and reading.** Made by Claude Opus 5.5 via the API, by the README rule (sure / probable / restored / unresolved).

The measure validates the key as a system, not each word. It is a lexical coverage, not a reading.

## The reading

The full text with marks is in `dudout/reading.md`. The working translation is in `dudout/translation.md`. The line-by-line decryption is in `dudout/decryption.txt`.

| Folio | Words | Sure | Probable | Restored | Unresolved | Sure + probable |
|---|---|---|---|---|---|---|
| 02r | 128 | 118 | 6 | 2 | 2 | 96.9 % |
| 04r | 118 | 114 | 3 | 1 | 0 | 99.2 % |
| 05r | 148 | 130 | 9 | 8 | 1 | **93.9 %** |
| 05v | 10 | 8 | 2 | 0 | 0 | 100 % |
| 06r | 144 | 129 | 11 | 3 | 1 | 97.2 % |
| 06v | 102 | 92 | 5 | 5 | 0 | 95.1 % |
| 07r | 42 | 40 | 1 | 1 | 0 | 97.6 % |
| **Total** | **692** | **631** | **37** | **20** | **4** | **96.5 %** |

By document:

| Document | Sure + probable | Status |
|---|---|---|
| 02r | 96.9 % | read |
| 04r | 99.2 % | read |
| 05r-05v | 149/158 = 94.3 % | read in part |
| 06r-07r | 278/288 = 96.5 % | read |

That table is the contributor's (sure + probable). Strict (sure only), recounted at integration: 02r 118/128 = 92.2 % (read in part), 04r 114/118 = 96.6 % (read), 05r-05v 138/158 = 87.3 % (read in part), 06r-07r 261/288 = 90.6 % (read in part), total 631/692 = 91.2 %.

- 05v (10 words) is the end of the 05r passage.
- 07r (about 180 letters) is too short to count alone, so it is counted with 06r-06v.
- About half of the sure words are function words. The harder content words fall disproportionately among the probable and restored ones.

**What the letters say.** Identifications are ours and probable; they are left for historians to check.

- **02r.** Salviati holds a letter of the Count of Reggio. He let Capilupi read it but not copy it. Capilupi sends it from memory.
- **04r.** Salviati's niece, wife of the Count of Santa Fiora, offers to arrange a marriage of Donna Ippolita (probably Ferrante's daughter) to the lord of Piombino.
- **05r-05v.** Juan de Vega (imperial ambassador in Rome) advises Ferrante not to come to Rome. The Pope would use the visit with the French, and a rumour could spread that the Emperor means to give Siena.
- **06r-06v.** Girolamo da Correggio reports Cardinal Farnese's grievances against Ferrante: the Sicilian grain dispute, Monreale, the Milan negotiation. Camillo Colonna reports Farnese telling Vittoria that the Pope consents to her marriage with Orléans.
- **07r.** The Emperor keeps the Pope in suspense about the council, and the Pope wants Farnese sent to him.
- 'Il cardinal nostro' is probably Ercole Gonzaga, Ferrante's brother.

## Integration check (13 Nov 2026)

Done on the files as submitted (PR #497); no human palaeographer.

- **Strict share.** Recounted from `dudout/reading.md`, sure words only (probable, restored and unresolved are holes): 631/692 = 91.2 %. By document 02r 92.2 %, 04r 96.6 %, 05r-05v 87.3 %, 06r-07r 90.6 %. The 96.5 % in the contributor's text counts the 37 probable words as read; it is kept above, labelled as theirs. Class: read in part.
- **Own decoder.** Written from `dudout/key.txt` only (23 simple codes, longest first). It gives the same Italian as `decryption.txt` (letter similarity 0.93-0.98 per folio); the difference is the parse of ambiguous strings (e.g. 51 u against 5 + 1), which the roughly 2,000 composite entries of the frozen JSON settle. **KEY-1555.json and the lexicon file are not in the PR**, so the frozen hash, M = 0.7962 and the controls (max 0.175) could not be reproduced exactly. With my own lexicon (16th-century Italian words of frequency >= 30, 3 letters or more) and the simple key, held-out 05r gives M = 0.83 against 200 permuted-value controls with max 0.34, mean 0.16. The key therefore works as a system on 05r; the order of events (protocol before key) is by the contributor's record only.
- **What the test shows.** The held-out folio is a sibling of the training folios (same hand, same letter, same system), and the key came from a package that held the other Y folios and the 1545 c. 48 and c. 49r digits. It validates the key on that system. It does not validate each word.
- **Image check.** The manifest of cc. 80a-80h (18 images, 0080-01r to 0080-09v) loads with curl; images load as regions at native size (full-size requests above 1599 px are refused). The labels used here are the manifest labels: 02r = 0080-02r (canvas 3), 05r = canvas 9 (0080-05r, penciled 80d), 09r = canvas 17. So the carta mapping is answered by the manifest, as far as the labels go. On 05r, lines 1-4 and the end of line 7 (about 150 groups) agree with the transcription by count and shape. The 7 / 9 distinction (short bar against hook) was not judged independently.
- **Code 11.** At 'imperammor' (05r line 7) the image shows two short 1-shaped strokes before the 2. The transcription is as written, so the 'mm' is a key problem (a second value of 11, mostly t, once l), not a transcription slip. Code 11 never gives a valid 'mm' anywhere in the decryption.
- **Same cipher as capilupi1545?** The digit system of c. 48 and c. 49r (Camillo Capilupi, Feb 1546) is the same as system Y: the simple key gives Italian runs on their first-pass digits (they were in the build set, so this is not independent). The 8 May 1545 letter in that folder is a different, homophonic cipher. One key, one entry: the digit key is held here. When both targets are finished they are to be one page about the digit system, with c. 48 and c. 49r read here from a fresh transcription; until then each folder points to the other.
- **Date.** Docket year 1546 against content that fits 1545 (Charles of Orleans died on 9 Sept 1545): left as a gap; no one has looked at the docket on the image.

## Remaining gaps

- **System X (03r, 09r).** Blocker: too-short. About 1,400 digits in another system; the glosses are partial and not alignable. A table or a clear copy would open it.
- **'mm' for t or l (code 11), and 'mignor' for 'signor'.** Blocker: open-codes. Five and two occurrences.
- **05r under the bar (93.9 %).** Blocker: illegible. It has 8 restored words to check on the image.
- **The key on capilupi1545 c. 48 and c. 49r.** Blocker: not-attempted as a reading. A quick test at integration shows the key gives Italian runs on their first-pass digits (see Integration check), but they were part of the build set and the transcription is a first pass. To be read properly, on a re-transcription.
- **Date (1545 or 1546).** Blocker: needs-physical-access. The docket year conflicts with the content.
- **Carta mapping of the image labels.** Blocker: needs-physical-access.
- **A human reader of transcription and reading.** Blocker: not-attempted.

## Escalation

- [x] siblings: both letters of cc. 80a-80h transcribed. Camillo Capilupi's c. 48 and c. 49r (capilupi1545) identified as the same system; not decoded here.
- [x] clear-pages: the second-hand glosses of 03r and 09r recorded (partial, not alignable). No clear text or gloss on the Y folios.
- [ ] known-keys: no table of Ippolito or Camillo for this system is known. The 1556 and 1560 tables mentioned in capilupi1545 were not tried.
- [ ] print: no printed edition checked. Nothing found in the repository, the issues or catalogue 1555.
- [x] key-rebuild: Opus anneals failed (OPUS-ESSAI); Fable key frozen and measured on held-out 05r: PASS.
- [ ] retry: the 'mm' and 'mignor' places and the restored words of 05r, against the images.

## Credits

Brice Dudout's project, with Claude agents directed by Brice Dudout.

- **Claude Opus 5.5:** transcription and arbitration, protocol, failed key attempts, gate, measure, count and reading.
- **Claude Fable 5.2 (API):** the key proposal.
- **WAINUT (LcCompany, capilupi1545):** the transcriptions of Camillo Capilupi's c. 48 and c. 49r, which were part of the build set, and the Estense manifest of cc. 80a-80h.
- **Daniel Bourdeau:** catalogue 1555.
- **The Biblioteca Estense Universitaria** holds the originals.

## Files

| File | Content |
|---|---|
| `dudout/README.md` | status line and file list |
| `dudout/transcription_*.txt` | the digits as transcribed, one file per image (02r, 03r, 04r, 05r, 05v, 06r, 06v, 07r, 09r) |
| `dudout/key.txt` | the key of system Y, human-readable |
| `dudout/decryption.txt` | the mechanical decryption, line by line against the transcription |
| `dudout/reading.md` | the Italian text with marks, the count, summaries |
| `dudout/translation.md` | working English translation |
| `dudout/PREREG-1555.md` | the frozen protocol |
| `dudout/measure_1555.py` | the frozen measure script |
| `dudout/MESURE-1555-H.txt` | verbatim output of the single run on 05r |
| `profile.json` | the target profile |

## Contributor's note (dudout, 12 Nov 2026)

The protocol was frozen before any key was built. Folio 05r was kept out of everything until the single measure. The key was not made by us: Claude Opus 5.5 failed, and Claude Fable 5.2 proposed it. We froze it unchanged and measured it once.

We count system Y as read and the target as read in part, for two reasons:

- 05r-05v stays under 95 %;
- system X is untouched.

The 'mm' readings may hide a transcription error in one sign of the cursive hand; we have not yet gone back to the images for them. No image or crop is included.
