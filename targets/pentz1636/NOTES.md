# Christian Pentz to Christian IV: Vienna 1636 (catalogue 2543) and Glückstadt c.1629-30, in the Zobel-family number cipher

Status: in progress (integration check 13 Nov 2026: folder only, no page; the gaps are workable: second transcription, Glückstadt verso, codes, Vienna clear text).

Contributor's status line: **key family recovered; read in part; both documents below our own 65% line.** Contributed. No claim of a first reading (see Prior art).

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic). Not filed before as an issue. The same-family key of Johan Zobel (Paris, 1629) is `targets/zobel1629`; nothing of it is repeated here.

## The two documents

| | Vienna, 26 Mar / 5 Apr 1636 | Glückstadt, c.1629-30 |
|---|---|---|
| archive | Rigsarkivet, TKUA Kejseren, Gesandtskabsrelationer 1630-58, unit 260651, images 37 right (lines 01-16) and 38 left (lines 17-18) | Rigsarkivet, Tyske Kancelli, SHLK A IV 89, "Relationer fra guvernør i Glückstadt Christian Pentz" 1629-45, unit 274999, image 2 (recto, ref 52788770); archive note at foot "Ny kgl. Saml. Fol. 616c" |
| catalogue | 2543 (sweep of 11 Nov 2026) | not in the catalogue |
| text | German clear text with short cipher runs | a whole page of figures, no clear text; continues on the verso (image 3, not transcribed) |
| transcription | b106, one reader, not blind (the key was found while transcribing), frozen 12 Nov 2026 04:11:09 UTC, md5 953fd409 | b157, one reader, **not blind** (he had applied table 1 to line 1 in his head before the freeze; disclosed in his log), frozen 12 Nov 2026 13:30:55 UTC, md5 1e70795f |
| second transcription | none: one reader, not blind | none: one reader, not blind |
| decode | once, b106 (`scripts/original/b106_dec_pentz.py`) | once, b157, key v1 table 1 unchanged (`scripts/original/b157_dec_once.py`) |
| **first pass (of record)** | **17/33 = 51.52%** | **25/68 = 36.76%** |
| with code 165 (b110) | 17/34 = 50.00% | - |
| '?' rule (doubtful figure = hole) | 17/33 = 51.52% | 23/68 = 33.82% |
| S+E | 32/33 | 56/68 = 82.35% |
| shuffled keys (5,000), seed 20261112 / seed 7 | 0 / 0 (true -2.4750; best -3.4441 / -3.4529) | 0 / 0 (true -5.4767; best -6.7301 / -6.5759) |

Figures per document; never pooled. Working in `counts.txt`.

## The system and the key

Same family as `targets/zobel1629`: an index number before a word run selects the number alphabet. Pentz's key is different from Zobel's (Zobel: letters 4-27, index 28-39, four tables).

- Index 62: table 1 follows. Table 1: a-i = 37 down to 29, k-z = 14 up to 28 (24-letter alphabet, i = j, u = v).
- Index 13: table 2 follows. Table 2: a-i = 38 up to 46; n 61, o 60, r 57, s 56, u 54.
- Code numbers (not solved): 168, 226, 85 and others; see `holes.md`.

`key.tsv` is key v1 (b106), the tables exactly as the decoder used them (`key_history/KEY_pentz1636_T1T2.py`, md5 8306f733, a verbatim copy of lines 4-6 of the b106 decoder; `scripts/build.py` checks that `key.tsv` equals it). Provenance per value: every value was built from the ciphertext of the Vienna letter while transcribing it, before the freeze (words seen: einige reale dienste, sache, Fridericus). The `basis` column says whether a value is seen in a Vienna word (and in which) or follows from the run of the table only. No value comes from a gloss.

Key history (`key_history/`):

| key | md5 | made | used here |
|---|---|---|---|
| v1 (b106) `KEY_pentz_v1_b106.txt` + `KEY_pentz1636_T1T2.py` | 1a28f084, 8306f733 | 12 Nov 2026 before 04:11 UTC, from the Vienna ciphertext | yes, for both documents |
| v2 (b110) `KEY_pentz_v2_b110.txt` | 20ad2a86 | 12 Nov 2026 04:36 UTC, from the gloss on Frederik Günther's letter of 30 Jan / 9 Feb 1636 (same unit, image 48): 64, 12, 10 as index numbers, a third table, table 2 m w y; 63, 11, 9, 8 by analogy | **no**: made after the Vienna run; not applied to Glückstadt; post-hoc re-scores in `counts.txt`, not claimed |

The Glückstadt letter was decoded with table 1 of v1, unchanged. It has no figure under 14 and no 62 or 13, so the index layer does not arise. Figure 28 (z) stands three times where o is wanted (andwzrt, bekzme, anherkzmen): probably a homophone of o outside the Vienna table. **Suspected; not applied** to any decode or count.

Method class: key recovered from the ciphertext (Vienna), then applied unchanged to a second letter by the same writer (Glückstadt).

## What the letters say

**Vienna 1636.** Pentz was at the Emperor's court with Gottlieb von Hagen in March 1636 to offer Christian IV's mediation and to press the King's son's claim to Bremen. In cipher: "[the 168] MATTER" he has not yet wished to touch; "SOME REAL SERVICES WILL BE HARD TO OBTAIN"; "IN PERPETUUM"; he wishes "FRIDERICUS were again with Your Majesty"; "our SERVICES are not meant ... THEREOF [168]". `readings/vienna_1636-03-26.md`, `translations/vienna_1636-03-26.md`. The clear German is transcribed only next to the runs.

**Glückstadt c.1629-30.** Addressed "Allergnädigster Herr" (the address panel, image 4: "Kön. Mayt. zu Dennemarck"). Readable pieces: a letter written to Your Majesty; Hamburg; "only three thousand have come here"; "I ask for an admiral", timber(?) from Norway, provisions, constables (gunners) and fireworkers, most needed ... of the fortress. Holes in most sentences. `readings/glueckstadt_c1630_img2.md`, `translations/glueckstadt_c1630_img2.md`. Date proposed from the content: Pentz became governor of Glückstadt about January 1630, and in May 1630 Gabriel Kruse was made admiral and sent with the fleet to the Elbe against Hamburg (Bricka and Fridericia II, pp. 242 n. 1 and 273 n.). Proposed, not proved.

## Controls

`scripts/shuffle_control.py` re-implements the two original controls exactly; `controls/shuffle.txt` is its output; corpora in `controls/CORPUS.txt` (not in git). Vienna: German 4-gram over the decoded word units, letter values permuted within each table. Glückstadt: German 4-gram (Simplicissimus) over the six table-1 runs, letters permuted over the 23 figure types. Seeds 20261112 (as filed by the sessions) and 7 (new here for Vienna; Glückstadt had both). All four: 0 of 5,000.

Short texts (Vienna 137 cipher figures, 20 letter words; Glückstadt 300 figures): the shuffle test is weak on its own. The stronger evidence is that the tables are rule-built alphabets and the words fit their clear sentences (Vienna).

No word-layer control: no reading here rests on a code word; every code is counted not read.

## Prior art

Checked 13 Nov 2026 (b190) in local OCR text, plain search only:

- **Fridericia, Danmarks ydre politiske Historie II (1881), p. 17 n. 1: RISK on content (Vienna).** He cites Pentz and V. Hagen "til Christ. IV, 26. og 30. Marts (Bremen Nr. 29, 30 a)" and paraphrases the Vienna talks (the Emperor accepts the King's mediation at the end of March; Bremen for Duke Frederik). Our letter is of 26 March, filed in TKUA Kejseren; his citation is to a Bremen series. He may have used this letter or a twin. No decipherment is printed and none is mentioned. Priority not established.
- Bricka and Fridericia, Kong Christian IV's egenhændige Breve II (1626-31): the 'Pentz' hits were read in context (10 lines; index: letters 242, 267 f., 273, 282, 324, 358). It prints the King's letters, not Pentz's. p. 242 n. 1: Pentz became governor of Glückstadt about then (January 1630); p. 273 n.: Kruse admiral, the fleet to the Elbe, May 1630. No print or decipherment of the Glückstadt letter found. Vol. IV (1636-40) p. 9 n. 3: Pentz and Günther sent to the Emperor, Dec 1635 / Jan 1636. No print of the 1636 letter. The volumes were searched, not read in full.
- Fridericia I: the 30 'Pentz' hit lines read; none cites a Pentz letter of early 1630 on Hamburg, an admiral or provisions. Not read in full.
- Earlier passes (b94, b106, b110): Danske Magazin, Cryptiana, DECODE, a word count over 60 local texts (`b110 pa_pentz_counts`): nothing printed for these letters. Cryptiana's Danish table-switching cipher (Haxthausen, Lindenfels 1819) is the same family, a different key.
- Cyphersolver main (b157): Pentz only in catalogue 2543; unit 274999 and image ref 52788770 not present.

**Not checked:** Ny kgl. Saml. Fol. 616c (the Royal Library collection named on the Glückstadt leaf: it may hold a copy or a decipherment); the Bremen series Fridericia cites (Nr. 29, 30 a); Kejseren 14 (Pentz/Günther/Lippe 1636-37, unscanned); Hurter, Friedensbestrebungen; Londorp. Bricka and Fridericia were searched by OCR, not read through.

## Checks

Repository scripts not run. With `python3 -I` (standard library):

- `scripts/build.py` reproduces both first-pass figures; the Vienna decryption equals the first 46 lines of the stamped b106 run output byte for byte; the Glückstadt decryption is byte-identical to the b157 run output; the Glückstadt units spell out the decode exactly.
- `scripts/shuffle_control.py` reproduces the filed control lines exactly (Vienna seed 20261112; Glückstadt both seeds) and adds Vienna seed 7.
- `profile.json` passes our static re-implementation of the profile check (b168): 0 errors.
- Timestamps: `timestamps/README.md`. The Glückstadt files are in no stamp.

## Integration check (13 Nov 2026, PR #522)

Done on the files as submitted; no human reader. Folder only, no page: both letters are below the contributor's own 65% line and the gaps can be worked.

- **Scripts.** `scripts/build.py`, `scripts/make_key.py` and `scripts/shuffle_control.py` read first (standard library, no network, writes inside the folder only). `python3 -I scripts/build.py` reproduces every figure in `counts.txt` and leaves the files unchanged. The shuffle control could not be re-run: its Gutenberg corpora are not in git.
- **Own decoder.** Written from the table rules stated above (not from the contributor's key file): the Vienna letters equal `decryptions/vienna_1636-03-26.txt`, and the Glückstadt letters (288) equal the unit list.
- **Own control.** Repository German model (`lang`, de-modern), letter values permuted as in the contributor's controls (within each table for Vienna, over the 23 figure types for Glückstadt): 0 of 1,000 each (Vienna true -3.14 per character, best shuffle -6.46; Glückstadt -6.07 against -7.47).
- **Images.** Rigsarkivet `api.rigsarkivet.dk/ao/v1/images/48703328`, `48703329` (Vienna) and `52788770` (Glückstadt) load with curl. Vienna lines 1-13 and 15-18 (about 130 figures) and Glückstadt lines L01-L09 (131 figures) agree with the frozen transcriptions, with one doubt: Vienna line 4, eighth figure, transcribed 25 (giving `wowen`), is written like the 15 of `reale` on line 6; read as 15 the word is `wolen` (wollen). Not settled; left for the second transcription, and the frozen file is not changed. Code 165 stands on image 38 left, line 1, as the contributor says.
- **Strict share (README read bar).** Vienna **16/33 = 48.48 %**: `berhuren` is a decode with u and h transposed, which the reading corrects to BERUHREN, so it is a hole. Glückstadt **23/68 = 33.82 %**: the two units with a doubtful figure (`nUr`, `Prouiant`) are holes. The contributor's first-pass figures, 17/33 = 51.52 % and 25/68 = 36.76 %, are theirs. Classes: Vienna read in part, Glückstadt decoded, not read.
- **One key, one entry.** Pentz's key (letters 14-37 and 38-61, index 62 and 13) is not Zobel's (letters 4-27, index 28-39, four tables): same family, separate targets, as filed.
- **Prior art.** Fridericia II (1881), archive.org `danmarksydrepoli02frid` (OCR): p. 17 n. 1 reads as quoted ("Pentz og V. Hagen til Kejseren, 13. Marts, og til Christ. IV, 26. og 30. Marts (Bremen Nr. 29, 30 a)"). These are joint letters with Hagen in the Bremen series; the private Vienna letter here is filed in TKUA Kejseren. No cipher or decipherment is mentioned in the volume. Risk on content only, as the contributor says. The right page of image 38 is the joint relation of 30 March 1636 (pencil date '1636 30/3'), not looked at further.
- **Catalogue.** Entry 2543 (the Vienna letter) matches the leaves: autograph, 26 Mar / 5 Apr 1636, cipher on image 37 right and image 38 left, codes 85, 165, 168, 226. It stays in the catalogue while the target is in progress. The Glückstadt letter is not in the catalogue but is `research/leads.json` lead **2565** (sweep b169 backfill, unit 274999): close it into this target at write-up.
- **Order of events.** The RFC 3161 stamps of 12 Nov 04:14 GMT cover the b106 key and the Vienna transcription and run; that the key was found while transcribing is declared. The Glückstadt files are in no stamp before the PR folder stamp of 13 Nov.

## Remaining gaps

- Codes: Vienna 168 (3x), 226 (2x), 85, 64, 63, 12 (2x), 11, 8, 9, and 165; Glückstadt 182, 220 (2x), 232, 260 (2x), 280 (2x), 730, 767 - blocker: open-codes; no code list found; some Vienna low numbers may be index numbers (key v2).
- Suspected homophone 28 = o in the Glückstadt letter (andwzrt, bekzme, anherkzmen) - blocker: no-key-material; not applied to any decode or count.
- Glückstadt verso (image 3) - blocker: not-attempted; the letter runs on there and is not transcribed.
- Second, blind transcription of both letters (including Vienna line 4 figure 8, 25 or 15, wowen / wolen, seen on the image at integration, and code 165) - blocker: not-attempted; one reader each, neither blind.
- Vienna clear text - blocker: not-attempted; transcribed only next to the cipher runs.
- Ny kgl. Saml. Fol. 616c, Fridericia's Bremen Nr. 29, 30 a, TKUA Kejseren 14 - blocker: needs-physical-access; may hold copies or decipherments.
- Short texts (Vienna 20 letter words) - blocker: too-short; the shuffle test is weak on its own.
- The Glückstadt letter is `research/leads.json` lead 2565 - blocker: not-attempted; close it into this target at write-up.

## Escalation

- [x] siblings: the Glückstadt letter by the same writer found and decoded with table 1; the Günther letter of 1636 (same unit, image 48) gave the v2 gloss, not applied.
- [ ] clear-pages: the Vienna clear text is transcribed only next to the runs; transcribe it whole (codes 168, 226 may be named in it).
- [x] known-keys: Zobel 1629 and the Haxthausen cipher (Cryptiana) compared: same family, different keys.
- [ ] print: Ny kgl. Saml. Fol. 616c, Fridericia's Bremen Nr. 29, 30 a and Kejseren 14 not seen; Fridericia II p. 17 checked.
- [x] key-rebuild: tables 1 and 2 rebuilt from the Vienna runs; table 2 k l m w x y z and the codes have no material yet.
- [ ] retry: a second, blind transcription of both letters (Vienna line 4 figure 8, code 165), the Glückstadt verso (image 3), and the suspected homophone 28 = o.
