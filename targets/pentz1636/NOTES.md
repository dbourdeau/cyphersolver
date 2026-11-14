# Christian Pentz to Christian IV: Vienna 1636 (catalogue 2543), Glückstadt c.1629-30 and Glückstadt 1644-45, in the Zobel-family number cipher

Status: in progress (integration check 13 Nov 2026: folder only, no page; the gaps are workable: second transcription, Glückstadt verso, codes, Vienna clear text; and the codes and corrected decodes of the 1644-45 letters; 14 Nov 2026: five more 1645 letters (PR #545, second part) are in as documents 5-9, all read in part, and the 28 = o suspicion is withdrawn by its contributor (PR #558)).

Documents 3-9 (Glückstadt 1644 and 1645, Brice Dudout, PR #545) use the same key and are filed here under `dudout/` (one key, one entry); see the sections "Documents 3-4" and "Documents 5-9" below. Nothing in Malcolm McBratney's files was changed by that merge.

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

The Glückstadt letter was decoded with table 1 of v1, unchanged. It has no figure under 14 and no 62 or 13, so the index layer does not arise. Figure 28 (z) stands three times where o is wanted (andwzrt, bekzme, anherkzmen): probably a homophone of o outside the Vienna table. **Suspected; not applied** to any decode or count. **Withdrawn by the contributor on 14 Nov 2026** (PR #558): the three figures are 18 written with a hooked 1; see "Correction of 14 Nov 2026" below.

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
- **Order of events.** The RFC 3161 reply of 12 Nov 2026 04:14:03 GMT (Sectigo) carries the SHA-256 of `MANIFEST.sha256` as its message imprint (checked with `openssl ts -reply -text`; the signature chain was not verified), and that manifest lists the stamped b106 key, Vienna transcription (md5 953fd409, the frozen file) and run output, whose SHA-256 match. So the Vienna key, transcription and decode existed by then. That the key was found while transcribing is declared. The Glückstadt files are in no stamp before the PR folder stamp of 13 Nov.

## Documents 3-4: Glückstadt 1644 and 1645 (Brice Dudout, PR #545; files in `dudout/`)

Contributed by Brice Dudout (13 Nov 2026), working with an AI model, as a new target `pentz1644`. The contributor said it is the same key as this target and offered to fold it in; it is folded here under the repository's one-key-one-entry rule (key v3 below agrees with every value of key v1 and v2 and completes table 3). The contributor's own notes and profile are kept unchanged as `dudout/NOTES_PR545.md` and `dudout/profile_PR545.json`; all paths in this section are relative to `dudout/`.

| | 3. Pentz to Christian IV, Glückstadt, 29 Apr 1644 | 4. Pentz to "Herr Cantzler", 1645 |
|---|---|---|
| archive | Rigsarkivet, Tyske Kancelli, SHLK A IV 89, unit 274999 (the unit of the c.1629-30 letter), images 321 (recto, ref 52789089) and 322 = 323 (verso, refs 52789090/91) | same unit, image 425 (ref 52789193; pencil "1645 5/6") |
| cipher | 11 lines on the recto, every figure with a contemporary letter-by-letter decipherment above it; 11 lines on the verso, only line 1 glossed | 12 lines; a contemporary marginal decipherment of lines 1-9 (another hand); later word glosses on lines 6 and 10-12 |
| transcription | recto with its glosses: `key_history/GLOSES-1644.tsv`; verso lines 2-11: `transcriptions/HELDOUT-322-A.txt` | `transcriptions/HELDOUT-425-A.txt` |
| contributor's figure | 27/28 = 96.4 % ("read") | 38/41 = 92.7 % (37/41 without code 301) |
| **strict figure (integration check)** | **26/28 = 92.9 %, read in part** | **37/41 = 90.2 %, read in part** |

**Key v3** (`key.tsv`, `key_history/KEY-v3.json`). Index 62, 63, 64 select table 1; 13, 12, 11 table 2; 10, 9, 8 table 3 (62, 64, 13, 11, 10, 8 attested by the 1644 gloss; 63, 12, 9 from key v2). Tables 1 and 2 are key v1/v2 of this target, unchanged; every glossed value agrees. Table 3 is the mirror of table 1 (a-i = 29 up to 37, k-z = 28 down to 14) with three glossed exceptions, g = 33, e = 35, r = 39; its glossed values include v2's t 19, e 35, n 25, a 29. 251 is a null (never glossed; it stands inside nich-251-t). Code 301 = the Archbishop (of Bremen), from the marginal decipherment on image 425; 560 and 756 open.

**Pre-registered test, by the contributor's record.** The contributor froze, by SHA-256 only and in this order, the pre-registration and its script (`scripts/PREREG-2.md`, `scripts/measure2.py`), then key v3, then the held-out transcription (image 322 lines 2-11, which carry no gloss, and the whole cipher of image 425: 301 groups, 286 figures; two passes said to be identical). No external timestamp exists; the folder arrived in one commit. Bar: N >= 0.75, N >= best control + 0.30, coverage >= 90 %. Result (`controls/MESURE-2.txt`): coverage 254/255 = 99.6 %, N = 0.7595, best of 200 within-table permutations 0.1452: passed, narrowly on the first condition. The reading, not the score, carries the text.

**What the letters say.** 1644: Pentz can no longer harass the enemy from Glückstadt as his raiding parties did, because the garrison was cut and the troops taken to Dithmarschen; at times only four men hold the ravelin before the Krempe gate. 1645: with the consent of the Archbishop of Bremen (code 301) he has ordered a strong party to fall on Wrangel's quarters; the men can move hidden in the wood by a separate road as far as Rendsburg (the Torstensson war). `readings/`, `translations/`.

### Integration check (13 Nov 2026, PR #545)

- **Hashes.** Recomputed: `KEY-v3.json` f5d41697, `GLOSES-1644.tsv` 65a924fa, `PREREG-2.md` 67d733e3, `HELDOUT.json` ca92cbd3 and the three pass files match the hash files. **`scripts/measure2.py` does not match**: its SHA-256 is a3f24f4b..., the frozen value in `controls/HASHES-PREREG-2.sha256` is 198495aa.... The committed script is therefore not the file that was frozen (it was changed after the freeze, by a path or a byte; what changed is not known). Its statistic is the one PREREG-2.md describes, and it reproduces the filed output exactly (next point), but the freeze of the script is not shown by the files.
- **Reproduction.** `measure2.py`, read first (standard library, reads the repository corpus `lang/corpora/de-gutenberg.txt`, SHA-256 4828ed84 as asserted, no network, no writes), run with `python3 -I` on the frozen key and held-out: output byte-identical to `controls/MESURE-2.txt` (N 0.7595, best control 0.1452, PASS). After the move into `dudout/` its corpus path (`parents[3]`) no longer reaches `lang/`; it was run from a scratch copy, and the frozen file is left unchanged.
- **Own decoder** (written from `key.tsv`, not importing the contributor's code or `KEY-v3.json`): the held-out decode equals both files in `decryptions/` letter for letter. On the recto and verso line 1, the 89 figures that carry a gloss letter all agree with the key (0 disagreements).
- **Images.** `api.rigsarkivet.dk/ao/v1/images/52789089`, `52789090`, `52789193` load with plain curl. Image 425, all 12 cipher lines (about 200 figures), and image 322 lines 1-11 (about 100 figures) agree with the transcriptions, with one doubt: in "Revellin" (322 line 3) the third figure, transcribed 39 in both passes, may be 35 (as written it is not clearly either); read as 35 the group gives r e u [struck] e l l i n directly. The recto figures and their glosses (image 321) were looked at line by line and agree with `GLOSES-1644.tsv`; the margin of image 425 reads as quoted in the reading (mit belieben des Ertzbischoffs zu Bremen ...).
- **Strict share (README read bar).** 1644: 26/28 = 92.9 %. Holes: {REVELLIN} (doubtful figures; the contributor also counts it probable) and CREMPER, whose last figure 21 stands inside a table-2 run where the frozen key has no 21 (the reading assumes the writer forgot the index for table 1; a corrected decode, a hole as `berhuren` above). VERRINGER is counted read: every cipher letter is read and glossed; the [T] is an editorial completion of a word the cipher and the gloss both end at r. 1645: 37/41 = 90.2 %. Holes: codes 560 and 756, the group 29 33 28 20 (T1 i e z q, unresolved), and C{O}MMANDIRT (the cipher gives c m m; the o comes from a small 18 written over the first 16 by another hand; a corrected decode). Code 301 is counted read: its value comes from the contemporary marginal decipherment, an external record on the leaf, not from the sense; it was read only after the measure, which matters for the test (301 is a code, ignored by the measure) but not for the reading. Without 301: 36/41 = 87.8 %. The contributor's figures, 27/28 = 96.4 % and 38/41 = 92.7 %, are theirs. Both letters are read in part.
- **Method per document.** The 1644 recto: read from the existing contemporary decipherment (and the key agrees). The 1644 verso and the 1645 letter: deciphered with key v3, which was recovered from the adjacent gloss (key recovered based on adjacent plaintext); code 301 from the marginal decipherment.
- **Key v3 and the Vienna letter.** Key v3 reads 64, 63, 12, 11, 9 and 8 as index numbers. In the Vienna transcription (document 1) these stand where the integration check of PR #522 lists them as open codes; with key v3 the runs after them decode to words (64 34 33 17 "den", 13 12 41 46 42 "die", 8 9 32 29 25 "dan", 13 11 41 42 57 54 60 61 "deruon"). This is a test on the Vienna letter's figures only, not a re-count: McBratney's files and figures are unchanged, and the code list in Remaining gaps now carries the note.
- **Not done.** The other 1644-45 cipher letters of the unit (images 402-405, 408, 411, 412, 420, several pages each, found by the contributor's thumbnail sweep) are not transcribed; the key should read them, and they may give 560 and 756. Catalogue entry 2565 (unit 274999) says images 137-503 were not viewed; it is left as it is until the write-up.

## Documents 5-9: five more letters of 1645 (Brice Dudout, PR #545, second part; files in `dudout/`)

Added to PR #545 by the contributor after the first integration (13-14 Nov 2026) and relocated here at integration from
`targets/pentz1644/` to `dudout/` (files unchanged; their own description is the addendum at the end of
`dudout/NOTES_PR545.md`). All five are letters of Christian Pentz from Glückstadt in Rigsarkivet, Tyske Kancelli, SHLK A IV
89, unit 274999, written during the Torstensson war in spring 1645. They were decoded with key v3 **as frozen** (SHA-256
f5d41697, recomputed): no value was changed and no new test was run, so this is key v3 applied to further letters, not a
validation. Files: `transcriptions/suite/` (pass A per page, `DIFF-AB.tsv`, `C-420.txt`, `DIFF-AC-420.tsv`, the arbitrated
`TRANSCRIPTION-SUITE.json`), `scripts/decode_suite.py`, `decryptions/`, `readings/`, `translations/` (paths relative to
`dudout/`).

| | letter | images | cipher words | contributor's figure (sure + probable) | **strict figure (integration check)** |
|---|---|---|---|---|---|
| 5 | to the Chancellor, 31 Mar 1645 | 402-403 | 72 | 66/72 = 91.7 % | **49/72 = 68.1 %, read in part** |
| 6 | to the Chancellor, 8 Apr 1645 | 404-405 | 52 | 45/52 = 86.5 % | **36/52 = 69.2 %, read in part** |
| 7 | to the Chancellor, 20 Apr 1645 | 408-409 | 16 | 16/16 = 100 % ("read") | **14/16 = 87.5 %, read in part** |
| 8 | to Christian IV, 20 Apr 1645 | 411-412 | 108 | 101/108 = 93.5 % | **87/108 = 80.6 %, read in part** |
| 9 | to the Chancellor, 1645 (pencil "1645 4/5"; answers a letter of 24 April) | 420 | 36 | 31/36 = 86.1 % (27/35 = 77.1 % before the second reader) | **25/36 = 69.4 %, read in part** |

Figures per letter, never pooled. **What the letters say** (`readings/`, `translations/`): damage to Glückstadt from the
March 1645 assault (the Reithofel work, the breastworks and main rampart, the new castle and its bridge, the old town
gate), a retrenchment being built, repair costs (a contract of 2,000 thaler, 330 rixdollars for the bridge), requests for
orders and money, the Spanish loan and a paymaster, the shortage of troops, and in late April Rendsburg "in höchster
Gefahr".

**Transcription.** Each page in two passes by the same reader (an AI model; B on re-made crops without reopening A);
14 differences settled on the image (`DIFF-AB.tsv`). Not frozen before decoding (the key was already fixed). Image 420 was
read a third time by a second reader (pass C, 14 Nov). Pass C is said to have been frozen by SHA-256 4a8f4ab7... before it saw A/B
or any decode, by the contributor's record: the frozen file (a French-annotated original "kept locally") is not in the PR,
and the committed `C-420.txt` hashes to c4fa8ebe..., so the freeze cannot be checked. The arbitration of A/B against C was
not blind: in several places the key's output decided (`DIFF-AC-420.tsv`: L06 pos 1 taken as 31 "key gives g -> Gefahr",
where C read 21; L14 pos 4 taken as 45 for "Nothurfft", where C read 55). C found two interlinear insertions that A and B
had missed (53 in "wer", 27 in "Volck"); both are on the image.

**Word glosses on the leaves.** Images 402-420 carry word glosses in another hand above most cipher words (they skip the
codes): e.g. "dieses festung Zustand" (402), "grosser schaden", "an beiden", "Sturm", "an der Vestung, sonderlich am
Reithoffel" (411), "Fall der Ort", "gar leichtlich", "mit geringer Mannschafft" (411), "nun Rensburg in größter Gefahr" (420).
They were seen while transcribing; the contributor used one ("Mayen", image 404) and none for the key. They are an existing
word-level decipherment of these letters, of unknown date, and they agree with the key's output wherever they were looked
at. Not transcribed or compared systematically.

### Integration check (14 Nov 2026, PR #545 second part)

- **Reproduction.** `scripts/decode_suite.py` (read first; standard library, no network, writes only `dudout/`), run with
  `python3 -I` on a scratch copy: `TRANSCRIPTION-SUITE.json` and the five decryptions are reproduced byte for byte.
- **Own decoder** (written from `key.tsv`, not importing the contributor's code or `KEY-v3.json`), on the arbitrated
  transcription: all five decryptions identical, line for line (127 lines).
- **Images.** `api.rigsarkivet.dk/ao/v1/images/<ref>` with ref = 52788768 + image number (52789170 for 402 ... 52789188 for
  420), plain curl, 200. Compared: image 402, all 11 cipher lines (about 165 figures); image 420, all 15 lines (about 200
  figures, including both interlinear insertions); image 411, lines 1-2 and 17-21 (about 100 figures). All agree except two
  places, both inside words already counted as holes: 420 L12 figure 4 looks like 42 (as pass C), not 62; 420 L14 figure 4
  looks like 55 (as pass C), not the arbitrated 45. Line-final figures on 402-403 are cut by the page edge in the image
  (402 L01, L07; 403 L07, L19, L21), so their letters are partly supplied.
- **Strict recount (README read bar).** Holes are the contributor's probable and unresolved words, and in addition every
  word the contributor counted sure that needs a letter not given by a legible figure under key v3: a figure with no value
  in the running table, a figure read as another (a corrected decode), a figure cut at the edge or illegible, or a figure
  chosen by the expected word where the readers disagreed. Letters the writer simply left out (desiderir(e), erlit(t)ene,
  runirt) are not holes, as VERRINGER in document 3.
  - 5 (31 Mar): 61 sure - 12 = 49/72. Holes added: Vestung (402 L01, last figure cut), [i]st (38, no table-3 value),
    Vestung (402 L05, 49 = m for g), [s]onderlich (33 = e for s), Brustwehren (last figure cut), gescheh[e]n (55, no value),
    begri[f]fen (figure cut), eingezogen (struck figure where e stands), ho[f]fentlich (40 = c for f), W[e]rcke (38 = a),
    Ordre (last figure cut), Commissarius (last figure cut).
  - 6 (8 Apr): 42 sure - 6 = 36/52. Holes added: [M]eyen (28 = k for m; the later gloss "Mayen" supplies it, as
    C{O}MMANDIRT in document 4), kayserlichen (one figure illegible), erkleckliche (figure cut), mehr (the run decodes only
    if the index before it is assumed to be table 3, as for {nicht}), Abdanckung (A 27, B 37, settled by the word),
    Völcker (405 L11, decodes "uoicker").
  - 7 (20 Apr, Chancellor): 16 - 2 = 14/16. Holes: Reparir[u]ng (14, no table-2 value), hi[e]siger (23 = t for e).
  - 8 (20 Apr, King): 95 - 8 = 87/108. Holes added: u[n]d (decodes "unu"), sonderlich (A 50, B 56?, settled by the word),
    Brück[e] (decodes "bruche"), daran (first figure illegible), Sch[a]den (29 = i), Gel[d]er (decodes "delter"),
    herzune[h]men (decodes "herzunehken"), werden (55, no value).
  - 9 (image 420): 28 - 3 = 25/36. Holes added: Rensburg (two overwritten figures: A unreadable, C 18? 22?, settled by the
    word with image 425's "Rensbyrg"), Gefahr (first figure blotted: C 21, taken as 31 because the key gives g), nicht
    (decodes "nicmt", 26 for 36). The figure 38 in {daran} is 38 on the image (it decodes daran exactly), but the contributor
    counts the word probable, and it is left a hole.
  The contributor's figures (sure + probable, restored letters read) are given once in the table above as theirs.
- **Values after the measure.** 252 = {im} and 434 = {dass} come from the sense of the clause only and were never tested;
  both are holes. No other value was added.
- **Method per letter.** Deciphered with key v3 (recovered from the adjacent 1644 gloss; for these letters: read with known
  key). The leaves also carry the later word glosses above, an existing decipherment not used for the reading.
- **Classes.** All five read in part. Letter 7 is not "read" under the strict rule (two corrected decodes in 16 words), and
  it is short. The gaps are workable (corrected decodes can be checked on the original, the glosses can be compared, codes
  remain), so this target stays in progress and gets no page.

## Correction of 14 Nov 2026 (PR #558): 28 = o withdrawn

Malcolm McBratney's file `CORRECTION_2026-11-14_figure28.md`: the suspected homophone 28 = o in the c.1629-30 Glückstadt
letter (andwzrt, bekzme, anherkzmen) is withdrawn. The writer's 1 has a hooked form, like a 2 without its base stroke; the
three "28"s where o is wanted are 18 by form, the same glyph as the 1 of the adjacent 16 (m); 18 = o is the table value.
The one 28 with a based, z-form 2 (line 17) gives z ("zur"). The re-read (b193) was not blind: the reader knew the table and
the suspicion. A second checker (an AI model) gives the hooked-1 reading for four tokens independently, by the contributor's
record.

- **Checked at integration** on image 2 (ref 52788770): in "14 28 16 33" (line 9) and "25 18 21" (line 6) the doubtful first
  digit has no base stroke and matches the hooked 1 of the following 16, while the 2 of 29 and 21 on the same lines has its
  base. The correction is consistent with the image. This is one more non-blind look, not the blind test.
- **Figures.** No figure of record changes: the frozen transcription keeps 28, and 28 = o was never applied. With 18 read in
  the three places the three words decode exactly (andwort, bekome, anherkomen): 26/68 = 38.24 % strict (contributor's rule
  28/68 = 41.18 %), not of record because the re-read is not blind and came after the freeze.
- **Date note (unverified, the contributor's).** The leaf may date to Feb 1644 rather than c.1629-30 (Bricka & Fridericia
  vol. V, letter 381; another citation gives vol. 2, no. 214, p. 234). Not checked here; the date stays "c.1629-30, uncertain".

## Remaining gaps

- Codes: Vienna 168 (3x), 226 (2x), 85, 64, 63, 12 (2x), 11, 8, 9, and 165 (key v3 of documents 3-4 reads 64, 63, 12, 11, 9, 8 as index numbers: see Documents 3-4); Glückstadt 182, 220 (2x), 232, 260 (2x), 280 (2x), 730, 767 - blocker: open-codes; no code list found; some Vienna low numbers may be index numbers (key v2).
- Glückstadt letter, the three figures once suspected as 28 = o (andwzrt, bekzme, anherkzmen): withdrawn as 18 with a hooked 1 (PR #558); a blind, shuffled digit-crop test is still to do - blocker: not-attempted; the frozen transcription and its counts are unchanged.
- Glückstadt letter date (c.1629-30, or Feb 1644 by the contributor's unverified note) - blocker: not-attempted; Bricka & Fridericia vol. V letter 381 and vol. 2 no. 214 not checked.
- Glückstadt verso (image 3) - blocker: not-attempted; the letter runs on there and is not transcribed.
- Second, blind transcription of both letters (including Vienna line 4 figure 8, 25 or 15, wowen / wolen, seen on the image at integration, and code 165) - blocker: not-attempted; one reader each, neither blind.
- Vienna clear text - blocker: not-attempted; transcribed only next to the cipher runs.
- Ny kgl. Saml. Fol. 616c, Fridericia's Bremen Nr. 29, 30 a, TKUA Kejseren 14 - blocker: needs-physical-access; may hold copies or decipherments.
- Short texts (Vienna 20 letter words) - blocker: too-short; the shuffle test is weak on its own.
- The Glückstadt letter was lead 2565 and is now catalogue entry 2565 (promoted 13 Nov 2026, PR #527); it is worked in this folder - blocker: not-attempted; narrow or remove entry 2565 at write-up.
- Documents 3-4, codes 560 and 756 (image 425) - blocker: open-codes; no gloss on either; the untranscribed 1644-45 letters may give them.
- Documents 3-4, image 425 group 29 33 28 20 (T1 i e z q) - blocker: not-attempted; perhaps a misread 23 (ietzt); the margin has "sich", which does not fit.
- Documents 3-4, image 322 "Revellin" third figure (39 or 35) and the struck figure - blocker: not-attempted; a second look at the original or a better image.
- Documents 5-9, corrected decodes and supplied letters (31 Mar 12 words, 8 Apr 6, 20 Apr Chancellor 2, 20 Apr King 8, image 420 3; listed in "Documents 5-9") - blocker: not-attempted; a look at the originals or better images of the page edges (402-403) may settle some; the cut line ends need-physical-access.
- Documents 5-9, codes 1009, 306 (2x), 470, 311, 1000 (2x), 269, 305, 81, 393, 1011, 753, 1400, 101, 560 (2x, with image 425), and 252 {im}, 434 {dass} (sense only) - blocker: open-codes; no gloss on the codes.
- Documents 5-9, unresolved groups ‹Plo?k› (402), ‹km› and ‹re anpariw› (404), ‹?ar› (412), ‹lezere› ‹ineuperqte›, ‹t›, ‹ua› (420) - blocker: not-attempted; the later word glosses above them are not yet compared.
- Documents 5-9, the later word glosses over images 402-420 - blocker: not-attempted; not transcribed or compared with the key's output; date and hand unknown.
- Documents 5-9, second blind transcription of 402-412 (one reader, two passes) and a checkable freeze of pass C of 420 (the frozen file is not in the PR) - blocker: not-attempted.
- Documents 5-9, Kong Christian IV's egenhændige Breve VI (1644-48) and Danish war histories for these dates - blocker: not-attempted.
- Documents 3-4, `dudout/scripts/measure2.py` is not the frozen file (SHA-256 a3f24f4b, frozen value 198495aa) - blocker: not-attempted; the contributor can send the frozen version.
- Documents 3-4, printed editions of the 1644-45 letters - blocker: not-attempted; not searched beyond the checks above.

## Escalation

- [x] siblings: the Glückstadt letter by the same writer found and decoded with table 1; the Günther letter of 1636 (same unit, image 48) gave the v2 gloss, not applied.
- [ ] clear-pages: the Vienna clear text is transcribed only next to the runs; transcribe it whole (codes 168, 226 may be named in it).
- [x] known-keys: Zobel 1629 and the Haxthausen cipher (Cryptiana) compared: same family, different keys.
- [ ] print: Ny kgl. Saml. Fol. 616c, Fridericia's Bremen Nr. 29, 30 a and Kejseren 14 not seen; Fridericia II p. 17 checked.
- [x] key-rebuild: tables 1 and 2 rebuilt from the Vienna runs; table 2 k l m w x y z and the codes have no material yet.
- [ ] retry: a second, blind transcription of both letters (Vienna line 4 figure 8, code 165), the Glückstadt verso (image 3), and the suspected homophone 28 = o.
- [x] siblings (documents 5-9): the 1645 letters at images 402-405, 408-409, 411-412, 420 transcribed and decoded with key v3 (PR #545, second part); strict 68-88 %, read in part.
- [ ] retry (documents 5-9): settle the corrected decodes on the original; compare the later word glosses; a blind second transcription.
- [ ] retry (documents 3-4): re-decode the Vienna letter with key v3 (64, 63, 12, 11, 9, 8 as index numbers) in a new, separately counted pass.
