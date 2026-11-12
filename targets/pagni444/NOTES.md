# pagni444: anonymous cipher letter to Cristiano Pagni, undated (ASF, Mediceo del Principato 444, c. 315r-v)

Catalogue row 2348. Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic); issue #426. **Read in part.** Key recovered from the ciphertext alone.

## The document

- Archivio di Stato di Firenze, Mediceo del Principato 444, c. 315r-v. Inventory VII p. 396 and n. 38: sender not named, s.d., to Cristiano Pagni, "In cifra".
- Recto: one line and a half in clear, then 26 lines of cipher (R01-R26; R01 shares its line with the end of the clear text). Verso: 10 lines of cipher (V01-V10) and a dateline in clear. No decipherment on the leaf, no signature, no place.
- Images: the archive's IIIF server, 2000 x 2829 px, which is the largest size it gives. `.../iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mdp_carteggio_universale/444/0636_C_315_R.ptif/full/full/0/default.jpg` and `0637_C_315_V.ptif` on `archiviodistatofirenze.cultura.gov.it`. No image is in this folder.
- c. 318v carries an outside address, "Al my mag.co s.r il segr.o my / cristiano pagni my s.r / in florentia", with a seal remnant; c. 318r is blank. The neighbouring leaves pair off as bifolia (314 with 319, 316 with 317), which leaves 315 with 318. That c. 318 is the address leaf of this letter is **probable, not proved**: no image shows the two leaves joined (`timestamps/stamped/ADDRESS_LEAF.md`).

## Summary

The writer tells Pagni that he has stayed where he is, at the request of the Marquis of Sarria, to see how a negotiation with a person hidden by the code A is going. A friend who knows French secrets tells him that "ours" will be deceived. A league is being negotiated, together with the pledging of Cervia and Ravenna to a person L "of Ferrara" to raise money; "Monsignor di Lansa", who came the evening before, presses it. G "of Lorraine" will come. The French ministers say his coming is no longer needed; the writer suspects that they have settled with A and are playing for time, to see whether L "Ottavio" and the troops they mean to raise can put S in straits and bring about an accord with A as depositary. A has spoken and prepared so openly that the French are uneasy. A is the bitter enemy of B and of L. Money is being spent; horse are coming from Mirandola and Parma; A says he will disarm, and the French will take on the soldiers. The writer does not know when he will be allowed to leave for a place n, and asks to be kept in the good grace of L.

With the proposed values (A the Pope, L "Duke", S Siena, G Cardinal, B the Emperor) this is a report from Rome on Franco-papal dealings against the Imperial side and Cosimo I in the pontificate of Paul IV. None of those values is fixed; see "Codes".

## The system

1. **Paired alphabet.** Figures 1 to 9 and x. A bare figure and the same figure with one dot stand for neighbouring letters: 1 a, 1' b; 2 c, 2. d (dot beside); 3 e, 3' f; 4 g, 4' h; 5 i, 5' l; 6 m, 6' n; 7 o, 7' p; 8 q, 8' r; 9 s, 9' t; x u/v, x' z. A hooked form of the 3 (J) is also e.
2. **Repeat sign.** `b` doubles the letter before it (tut~o, quel~a, gros~a); 49 units, once across a line break (R20-R21, quel|la).
3. **Word signs.** `u` che (23), `a` in (13), `l` per (7 read; three more stand at clause breaks and are not read).
4. **Nulls.** Figures with two dots (1" 2" 3" 5" 7" and others), a dot above the 2, the barred sign `#` and the pi-like sign `N`: 58 units read as nulls by the key, all between words or at a line end.
5. **Capital codes.** A, L, S, G, B, D, Q and small m, n, d, with an ampersand: 23 units. None has a fixed value.

`key.tsv` has every label with its value, kind and how many units are read and not read under it. `timestamps/stamped/KEY_pass3.tsv` is the key as stamped on 11 Nov 2026.

### Where the pairing is weak

The reviewer is right on both counts.

- **g/h.** The dotted 4 that the pairing predicts for h occurs once and is dropped as a null. Where the text wants h (ric-h-iesta, marc-h-ese, c-h-iaramente, tresc-h-a, h-avessino twice, h-iersera) the sign is the bare 4, by context: 7 units, all counted not read. So h is not shown by the key. Either the writer writes g for h, or dots on the 4 are missing or were not seen. At R09 a dot sits between the 4 and the 5 and cannot be given to either.
- **a/b.** 1' is read b by the key in 8 units (ben three times, biu, potrebbe, stabilito, bisogno, brevemente) and is dropped as a null 9 times after adjudication (13 in pass 3). The value b rests on those eight words.
- **z.** x' and x" are read z by the key in four units (frnzesi, sforzo, franzesi twice); the other eight units under those two labels are not read.
- f (3') and p (7') are better supported: 8 and 23 units by the key.

### The dropped signs

In pass 3, 69 units were dropped as nulls by context although the sign has a letter value in the key (9' 16, 5' 13, 1' 13, 3' 5, 7' 4, 9" 3, and 15 others; `dropped_signs.tsv`, `counts.txt` F). These are the reviewer's 69, and the same per-sign tallies. After the adjudication against the blind transcription:

- 9 turned out to be two-dot signs on the image, that is, nulls by the key (the blind reader's stacked pairs of dots). They are now read.
- 4 are left open by the image between a two-dot sign and a one-dot sign.
- 56 are letter signs on the image as far as two readers can tell, most of them with one dot (9' 16, 5' 12, 1' 9, 7' 4). Those 60 (4 + 56), with 2 units that pass 3 had as key nulls and the image now leaves open, are the 62 nulls by context of the final count.

Of those 62, 61 stand between words or at a line start or end; one is inside a word (mar[a]chese). The 58 key nulls stand in the same positions. So the dropped signs behave as a **separator class**: single-dotted consonants, mostly t, l and b, written between words. Whether the writer used them so, or whether more of them are two-dot signs with one dot not visible at 2000 px, we cannot tell from these images. It is not the same as reading them, and all 62 are counted not read. A better image would settle it.

## Codes

| Sign | Units | Proposed | Status |
|---|---|---|---|
| L | 5 | Duca | from context; five uses agree (di Ferrara, Ottavio, al L piaccia, del B e del L, gratia del L). Written `[?Duca]` |
| A | 6 | Papa | from context only. `[?Papa]` |
| S | 2 | Siena | from context only. `[?Siena]` |
| G | 1 | Cardinale | from context only. `[?Cardinale]` |
| B | 1 | Imperatore | from context only. `[?Imperatore]` |
| & | 1 | et | an ampersand, R24. `[?et]` |
| D | 2 | none | "pero" was a candidate; not adopted |
| Q, m, n | 1 each | none | |
| d | 2 | none | follows the clear word "como" at R01 |

Rule of the project: a code is read only if its value is fixed by a clear duplicate. None is, so all 23 are counted not read, L included.

## The count

One final figure: **1,369 of 1,514 units read (90.42%)**; 137 not read (52 letters, 62 nulls, 23 codes); 8 unread. `counts.txt` has the arithmetic and reconciles every figure issue #426 gave:

| Figure | What it was | Now |
|---|---|---|
| 89.7% | 1,364/1,521, first reading: units inside read words, context letters counted as read, nulls not counted | withdrawn as a measure |
| 91.5% | 1,391/1,521, pass 3 with the 23 code signs counted as read | withdrawn |
| 89.94% | 1,368/1,521, the same with the codes not read | superseded by the adjudication |
| 91.72% | 1,395/1,521: **sign agreement** of the blind third transcription with pass 3. Not a share read | stands as an agreement figure |
| 88.56% | 1,347/1,521: the blind third transcription under the same key and rule | stands; it is the independent figure |
| 90.42% | 1,369/1,514 after 138 disputed units were checked on the image | **the figure** |
| 95.7% | 1,224/1,279, letters only, before adjudication | not a headline figure |

By words, the folder gave "279 words and 95 holes, 0.746" on `reading.md`. That does not add up (95 of 279 is a hole share of 0.34, a read share of 0.66), and the verifier's rough count of the same file (about 359 words with the clear lines, 86 holding a bracket) gives 0.76: the word figure is dropped, and 90.42% by units is the only share used.

## How it was done

1. Pass 1 (`passes/`): first transcription, 1,560 sign tokens. An annealer on it gave the vowels and no reading.
2. Pass 2 (`timestamps/stamped/p2_r.txt`, `p2_v.txt`): the same reader again from new crops, without opening pass 1; 1,521 signs. The two passes agree on 82.0% of aligned positions. The key was read off the repeats of pass 2 (questo, quel, con, -stri), with no crib and no gloss, and the verso then read on sight.
3. Pass 3 (`timestamps/stamped/units3.tsv`, `LEDGER_444.tsv`): not blind. Every flagged unit re-viewed on tiles; the rule for m and n (plain 6, dotted 6) and the null 2' came from it.
4. Blind third transcription (`transcription_blind.txt`): another session that opened only the two images; 1,516 units by its own count.
5. Adjudication (`adjudication.tsv`): the 138 units where pass 3 and the blind reader differ, each cropped with its label hidden and read before either transcription was looked at. Pass 3 was right at 60, the blind reader at 41, both readings possible at 34, neither at 3. Seven units of pass 3 have no sign on the image.
6. `transcription.txt` is pass 3 after that adjudication. `scripts/build.py` rebuilds it, the decryption, the ledger and the counts from the stamped files.

Controls of 11 Nov 2026, from our own scripts (in `timestamps/stamped/`: `verify3.out`, `nullcontrol.out`): the key against 5,000 shuffled keys, 0 of 5,000; an unaided solver run on the pass-3 signs recovers 87.1% of the key and beats five frequency-preserving controls. These are language-fit checks, not probabilities. The solver scripts are not in this folder, so please do not cite the figures as verified.

## Errors of ours, found for this folder

- **The clear opening.** Our pass-3 file gave the second clear line as "accio ch'ella intendesse come". The image has "por / acca. co(n) esta intendra como": pass 1 and the blind reader had it. The issue quoted only the first words, with "ragguagliandola" where the leaf has "raguagliandolo".
- **fr[an]zesi (R11-R12).** No a is written; the issue printed "franzesi" and did not list it with Lansa(c), dis(a)rmara and dispiaquer(o).
- **"a a [n]" (V09).** Two a signs; the issue printed one.
- **Lorena.** Before adjudication the 6 of "lore-6-a" was read without a dot (lorema, n by sense). On the adjudication crop the dot is there; n is now by the key.
- **The date in the issue** ("late Oct 1555 and Mar 1556 both possible") was too narrow; see below.
- The three corrections made before the issue was filed were checked again on the image for this folder: R02 has one minim between 6' 7 and 2. ("fino adesso"); R13 u16 is a 7 with its bar and a dot ("sapere"); V04 u18 is a 9 with a dot ("poter"). All three hold. One reader, with the words known.

## The date: not established

- The leaf says only "el dj xx. m" with a bar: day 20 of a month in m (marzo or maggio by the letter). No year.
- The filza is "Lettere del mese di Marzo 1555" and the catalogue has "s.d. [late March 1555]". In March 1555 Julius III was dying; if A is the Pope, the hostility to the Emperor and the Duke does not fit him. The catalogue date looks wrong for the content, as the reviewer says, but that rests on unfixed code values.
- The persons fit late 1555: Lansac reached Rome about 20 Oct 1555 and left on 18 Dec; the Cardinal of Lorraine arrived on 21 Nov 1555 and left on 9 Jan 1556; a plan of 29 Sep 1555 had Ottavio Farnese raise troops against Sienese places (Romier, Les origines politiques des guerres de religion II; Sauze, Correspondance politique de Lanssac; read in archive.org OCR, two pages as images). But no month of late 1555 begins with m.
- March 1556 fits the m, Sarria in Rome and the talk of disarming (Navagero, 19 Mar 1556), but Lansac and Lorraine were then in France.
- Pledging Cervia and Ravenna for money recurs: a rumour of June 1554 (Ribier II) and Carafa's offer of January 1557, with Ravenna otherwise to go to the Duke of Ferrara (Duruy, Le cardinal Carlo Carafa, p. 212; OCR only). Lansac was in Rome again from 7 Sep 1556 to 5 Feb 1557. The Lansac and Lorraine clauses have not been tested against 1557.
- Serristori's letter of 24 Oct 1555 (Mediceo 3274, c. 460), which Romier cites for Lansac's arrival, is not online and was not read.

So: **late 1555 to early 1557, unresolved.** `timestamps/stamped/DATE_MATRIX.tsv` is the scoring of 11 Nov, which favoured late October 1555; it predates the Cervia and Ravenna parallels and should not be read as a result.

## Prior publication

None found; priority not established. Checked on 11-12 Nov 2026: this repository; inventory VII pp. 385-398; archive.org full text of Sauze, Romier II, Serristori's Legazioni, Desjardins III (OCR, not page by page); Calendar of State Papers Venice VI nos. 418-431; web searches. Not checked: the Medici Archive Project database (login), Cantagalli, Ancel, the Cifrari series of the archive (not digitised). Babbi's cipher in the same filza is a different system (`timestamps/stamped/KEY_COMPARATOR.md`).

## Remaining gaps

- 8 unread signs (`holes.md` 1), among them a looped sign that stands three times at the start of a clause - blocker: illegible; no larger image than the archive's 2000 px.
- All eleven code values (A, L, S, G, B, D, Q, m, n, d, &) - blocker: no-key-material; a dated letter in the same cipher or the key register would fix them, and neither is online.
- h, and the 62 signs dropped as nulls by context (mostly single-dotted t, l and b between words) - blocker: illegible; whether a dot is missing or the signs are a separator class cannot be told at 2000 px.
- The date and the writer - blocker: no-key-material; the dateline "el dj xx. m" has no year and the leaf names no sender (Serristori's letter of 24 Oct 1555, Mediceo 3274 c. 460, is not online).
- Whether c. 318 is the address leaf of this letter - blocker: needs-physical-access; no image shows the two leaves joined.

## Escalation

- [x] siblings: the neighbouring leaves cc. 313-317 opened (clear letters of March 1555, none a decipherment); Babbi's cipher in the same filza compared (`timestamps/stamped/KEY_COMPARATOR.md`): a different system
- [x] clear-pages: no decipherment on c. 315, on c. 318 or noted in inventory VII
- [x] known-keys: the figure ciphers of Babbi, Griffoli and Nucci in the same archive do not fit; the Florence chancery keys (Cifrari II serie) are not online
- [x] print: inventory VII, Sauze, Romier, Serristori, Desjardins, Calendar of State Papers Venice read for the context; no edition or decipherment of this leaf found
- [x] key-rebuild: the key was read off the repeats of the ciphertext; an unaided annealer is reported to recover 87.1% of it (our own scripts, not in this folder)
- [n/a] retry: the extended key was applied to every unit in pass 3 and again after the adjudication; nothing further to retry without new images or key material

## Integration check (12 Nov 2026)

The folder was verified before it was written up. What reproduced and what did not:

- `scripts/build.py` run in a copy rebuilds `units.tsv`, `transcription.txt`, `decryption.txt`, `overrides.tsv`, `dropped_signs.tsv`, `key.tsv` and `counts.txt` byte for byte. An independent decoder written from `key.tsv` and `transcription.txt` agrees with the key on all 1,369 units counted as read (15 differ only in the letter case that marks a two-sign image reading). Counts: 1,514 units; 1,369 read (90.42%), 137 not read, 8 unread.
- The Sectigo token carries the manifest hash and the time of 11 Nov 2026 21:08:11 GMT; the 28 stamped files in `timestamps/stamped/` match their manifest lines. The order of events (pass 2 frozen before decoding, the key read off the repeats of pass 2) is **by the contributor's record**: the stamp shows only that the files existed at that time. The certificate chain and the OpenTimestamps proof were not verified.
- The ASF image server answered curl on 12 Nov (2000 x 2829 px, recto and verso). Lines R03 and R04 (about 100 signs) were compared with the image by the verifier: the digits and letters agree throughout and the dots that can be seen at this size agree; the number of dots over a 5, 6 or 9 cannot be settled by eye at 2000 px. The rest of the leaf has not been compared by a person. This replaces the earlier statement that nobody had looked at the images.
- The shuffled-key control (0 of 5,000; real -2.262, best control -3.516) was run by the first verifier on its own decoder with an Italian character model. At integration `docs/_validate.py` was run on the units read by the key (`validation.tsv`, written at integration from `units.tsv`): verdict pass. This is a language-fit test of a key partly built from the same text, not a measure of how much of the text is right.
- The solver run (87.1% of the key recovered) and the five optimised null controls were not re-run (no scripts in the folder); they are the contributor's.
- Figures corrected at integration: the headline stays 1,369 of 1,514 units (90.42%) everywhere, counted by tokens; the per-text `read_share` in `profile.json` was a word count stated as 279 words, 95 holes, 0.746, which does not add up; it is now the unit figure, so that one rule is used in the whole folder.
- The catalogue date "s.d. [late March 1555]" does not fit the content (Julius III was dying in March 1555, and A is hostile to the Emperor and the Duke); this folder leaves the date open (above) and catalogue row 2348 leaves the catalogue with this write-up.

## Tools

Claude (Anthropic) models for the transcriptions, the solving, the scripts, the image checks and these files; own Python (standard library and PIL). The repository's scripts were not run by us.
