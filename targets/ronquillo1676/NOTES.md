# Salinas (London) and Ronquillo (Nijmegen) to Fuenmayor, 1676–78 — DECODE R966–R984, R1001

Status: read in part (22 Oct 2026: all twenty letters read and translated, eighteen from their contemporary margins; 14 Nov 2026: R982 re-read by Brice Dudout, twelve holes closed, 0.919 -> 0.954 by hole marks, 0.914 by words, so R982 stays under the bar; holes left in R983 f. 1, R982, R984 and single words, each with an outside blocker)

Recount by words (14 Nov 2026, owner decision: the read share counts holes by words, not by hole marks; a mark with a
number, `[... n]`, is n unread words). The seven multi-word marks of `read/R982_reading.md` are sized from
`read/R982.dec.txt` and the reading's Notes: opening groups 3, after "corra" 4, before "el dolor" 4, "por el" (dul de
Burgomayne) 3, "critico ... el estado" 2, "persistan en" 4, "sino" 2. The cipher is syllabic, so these are estimates,
taken at the least number of words the decode shows. 27 unread words under the twelve marks, 31 holes with [al]eses and
the three [?word]s, against 330 words read: `read_share` 0.914 (was 0.954 by marks; the "about 0.93" of the integration
check below was the same count before sizing). R982 and the target stay read in part.

14 Nov 2026 (verification, Claude Opus 5.5): R982, which has no margin, re-read on the full-resolution DECODE images
(I5093-I5095) wherever the reading had a hole, with a second blind pass on the doubtful figures. Most holes came from
the hand, not the key: its 7 has a heavy flourished head and was transcribed 2 or 3 (72 ti, 71 te, 70 ta, 73 to, 74 tu,
78 on), its 4 and 9 alike (54 gu), and a struck o was taken for a null. Twelve holes closed (actividad, o nos, atender a
todas, aseguro, tan, ambiguedad, Mequelemburg, constitucion, puestos, abrogado, Bruselas, ofrece); [?habra] and
[?tenemos] stay uncertain where the blind pass disagreed. Three code values glossed in the sibling margins but missing
from keyx.py are keyed: fin = ofrece (R975, R977, R981), al = despues (R980, R981; balbases1677 R986 twice), 91 = asist-
(R981; gives "que asisten" in R984). read_share R982 0.954, R984 0.969. The balbases1677 key.json itself lacks al;
its R986 margin glosses it twice.

Integration check (14 Nov 2026, PR #601, Brice Dudout). The class change to read is **not applied**; the re-read and
the three key values are kept.

- Recount of `read/R982_reading.md` with `research/reading_audit/v10_relabel.share`: 330 words, 16 hole marks, 0.954,
  as the pull request says (before: 0.919). R984: 505 words, 16 marks, 0.969.
- That figure counts each `[...]` as one word. Seven of the twelve `[...]` of R982 cover more than one word by the
  reading's own Notes and `read/R982.dec.txt`: the opening groups (M 182 491), "corra [...]" (do y is 55 ed 28 do:
  con, por, la and a noun), the words before "el dolor", "por el [...]" (dul + de bu-r-go-ma-y-ne), "critico [...] el
  estado", "persistan en [...]" (ten groups) and "sino [...]". Counted at the least number of words those groups hold,
  R982 has at least 26 unread words against 330 read: about 0.93 of its words. The bar is 95% of words, so R982 stays
  read in part and the target with it. The 0.954 is recorded as `read_share` with that reservation.
- "ambiguedad" has an unidentified sign and no figures for its ending in the Notes ("kept for the fixed pair"), and the
  blind pass gave "puestos" low confidence; both are kept as the contributor read them. One more hole mark leaves the
  mark count at 0.951, two at 0.948: the margin is one word.
- Not checked here: the figures on the images. DECODE serves the full-size images of R982 only to an account
  ("Insufficient permissions"; the 200-px thumbnails are public). The twelve closures therefore rest on the
  contributor's record, and on the fact that each gives a Spanish word that fits its clause. `tx/R982.txt`, `read2/`
  and `read/R982.dec.txt` still hold the old figures: the corrected figures are only in the reading's Notes.
- The three key values were checked against the DECODE margin transcriptions and the readings: fin = ofrece (R975
  "ofrecen los mediadores", R977 "los papeles que ofrece", R981 "ofrecer montes y valles"), al = despues (R980, R981
  twice; balbases1677 R986 "[al] que franceses" under the margin's "despues que franceses" and "[r] [al] de [con] [cun]"
  under "y despues de haver hecho"), 91 = asist- (R981 "ha asistido", "el asistirnos"). `al` is now also in
  `targets/balbases1677/key.json`.
- A suggestion, not applied: "informado por el [dul] de bu-r-go-ma-y-ne", in a sentence on England, would be the
  marques de Borgomanero, Spanish ambassador in London, which would make dul = marques. No margin glosses dul.

22 Oct 2026, later (re-read, batch ronq; REREAD_BRIEF.md): **all twenty letters read and translated.** For each
letter the contemporary decipherment in the left margin was transcribed from the DECODE images (full-resolution
crops; DECODE's margin transcription checked against them) and aligned word by word with the key decode, cut into
words page by page (`spaced.py` -> `read/R*.dec.txt`). Readings in `read/R*_reading.md` (normalised Spanish, holes
marked), English in `read/R*_en.md`, logs in `read/R*_reread_log.md`, label corrections in `read/R*_corrections.tsv`
and corrected transcriptions in `txi/` (R966-R970, R973, R976, R977, R982, R984). Grades: A for R966, R968-R975,
R978-R981, R1001; B for R967, R976, R977, R982, R983, R984. 23,463 of 23,463 groups are in letters that read.
The tooling (`tx/`, `txi/R976`, `txi/R982`, `keyx.py`, `dec2.py`, `sense.py`, `em.py`, `mktx.py`) is the 5 Oct 2026
push-to-95% work that sat uncommitted in the main checkout; it was copied here (`sense_vocab.pkl` is git-ignored and
rebuilt by sense.py).

Found on the way:
- **R970 and R973 have a margin decipherment.** DECODE's transcriber put it in a #COMMENT block, so it was missed and
  the two were called new readings. Only R982 and R984 are unmargined; they were read on the images with the key.
- **R971 and R972 are one letter** (the seven images are pixel-identical), London 26 Jan 1677; R971's "1677Jan1" is
  wrong. R980 and R981 differ.
- Dates from the clear text: R968 is 6 Oct 1676 (not 8 Dec), R974 is The Hague 21 Sep 1676 (not 21 Dec), R978 is
  10 Feb 1677 (not 20 Feb; signed by Bernardo Navarro for Ronquillo), R981 is 4 Mar 1677 (not 27 Jan).
- DECODE's R977 transcription merges two f. 2 rows and drops one; R978's margin transcription misses a sentence;
  R983 f. 1 has a margin DECODE never transcribed, faded beyond reading on the scan.
- Code values read from the margins (entered in keyx.py where the group had no value; key coverage 93.6% -> 95.4%,
  sense 83.3% -> 85.4% by dec2.py): ers jo, bes espera, 97 aunque, fos/for ningun-, 121 congreso,
  120 congreso/cuidado (two values or two signs), do Lorena, dos Münster, fis negocio, fan oficio, bel favor, fa novedad,
  143 porque, 100 algún, 122 conviene, 123 convenien-, bil forma, cil holande-, cep junta, 59 lu, 82 ir, K j, I i,
  ▽ a, 67 ri (this volume), 51 ge, 12 c, 34 ex, es ja/je, X ju, 135 (me) parece, 139 plenipotencia, 140 particular,
  154 Rey de Francia, 155 Rey de Inglaterra, 116 carta, in España, or Dinamarca, be estado, er Dios, 112 conde,
  168 Su Majestad, 141 para que, dal mucho, dol medio, bo empeño, bu enemigo, bon fuerza, bin franceses, cu general,
  90 ajuste, 99 armas, 104 batalla, 107 beneficio, 109 Bruselas, 173 suceso, 182 siempre, fes noticia, fol ocasión,
  fel opinión, dun nuev-, cun (h)ech-, con haber, 126 correo, 175 secreto/a, 400/470/760 nulls; single places in the
  logs. Conflicts: bi = ne and afectos/efect-; 163 keyed suecia but glossed razón; 170 S.M. Cesárea and Inglés;
  11 consejo and inside "reflexiones".


22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **all twenty letters are
decoded, not read.** The Balbases key gives 88% of the groups a value, but `read/R*.txt` is unspaced decoder output
from DECODE's uncorrected transcriptions with bracketed groups every few words; even the best letters (R971 93.6%,
R974, R978, R979, R1001) build sentences only with guesswork. `outcome.class` read in part -> not read, method -> not
solved, key stays recovered; the 0.88 is withdrawn as a reading figure. Next: space and build the best letters into
sentences with their margin decipherments (re-read from the images), then translate.

Earlier status: read in part (0.88 of groups measured 21 Sept 2026; R970, R973, R982, R984 read for gist)

The remaining ciphered letters in Baltasar de Fuenmayor's volume, Archives générales du Royaume, Brussels,
Secrétairerie d'État et de Guerre, inv. nr. 2559 (see [hernannunez1674](../hernannunez1674/NOTES.md),
[balbases1677](../balbases1677/NOTES.md), [carpio1677](../carpio1677/NOTES.md)):

- **Bernardo de Salinas, Spanish envoy in London**, eight letters, 21 Aug 1676 – 2 Mar 1677 (R966–R973)
- **Pedro Ronquillo, Spanish plenipotentiary at Nijmegen**, twelve letters, 21 Dec 1676 – 19 Mar 1678 (R974–R984,
  R1001)

DECODE's transcriptions were fetched 21 Sept 2026 (`img/`, git-ignored). R1000 in the same volume is French and
already decrypted on DECODE, so it was not taken.

**Result.** All twenty are in **the Balbases 1677 key** (`../balbases1677/key.json`, plus the four values added in
hernannunez1674). No changes were needed. Across the twenty the key reads 88.4% of 23,463 groups. Sixteen letters
carry a contemporary marginal decipherment, and the key output agrees with it. **Four have none in DECODE's
transcription, and these are new readings:**

| rec | letter | groups | read | DECODE status |
|---|---|---|---|---|
| R970 | Salinas, 15 Sept 1676 | 663 | 77% | partially decrypted |
| R973 | Salinas, 2 Mar 1677 | 199 | 86% | partially decrypted |
| R982 | Ronquillo, 19 Mar 1678 | 813 | 71% | non-decrypted |
| R984 | Ronquillo, 26 Feb 1678 | 1,144 | 86% | non-decrypted |

The images of R970 and R973 were not checked for a margin that DECODE's transcriber left out. If one is there, it
is a check on these readings, not a prior reading of them.

So one cipher served Fuenmayor's correspondence with at least three Spanish envoys: Salinas in London, Hernán
Núñez in Stockholm, and Ronquillo and Balbases at Nijmegen. Carpio in Rome used a different one.

Per-letter coverage (from `read.py`): R966 88%, R967 87%, R968 83%, R969 87%, R970 77%, R971 94%, R972 89%, R973 86%,
R974 93%, R975 89%, R976 70%, R977 88%, R978 93%, R979 92%, R980 89%, R981 89%, R982 71%, R983 89%, R984 86%, R1001 93%.

## Transcription formats (the only real work)

DECODE's transcribers used three conventions:

1. Groups are separated by double spaces and characters by single spaces (most records).
2. Every character is single-spaced, with no group boundaries (R971, R974, R978, R979, R983, R1001). The key first
   read these at 0%. They were rejoined and segmented with a dynamic programme over the key's vocabulary (`seg.py`:
   fewest groups, one-character groups penalised).
3. R970 and R973 write a sign as "Infinity" (∞), which is c before a vowel (∞o co, ∞i ci). R970's transcriber also
   writes 5 where the key has *a* and b for *que*, which accounts for most of its unread groups.

Unread groups are almost all transcription noise ("?", "*", split groups). R982's transcription is the worst (full
of "?"), and its reading is gist only.

## What the four new readings say (gist, 21 Sept 2026; superseded by read/R*_reading.md)

- **R970, Salinas, 15 Sept 1676.** "ya se habrá [sabido] el fatal suceso…". Salinas fears the blow will close
  "esta puerta". The discourses at the English court turn to a peace; the "progresos" on Fuenmayor's side move
  minds there; the minister has tolerated the event; the Danish fleet.
- **R973, Salinas, 2 Mar 1677.** The English princes are "no siendo tan malos" when it comes to withdrawing the
  troops from France, "en que me prometo persistirán". The preparations of the last months show that everything is
  in earnest. The discourses treat the peace as good as made.
- **R982, Ronquillo, 19 Mar 1678** (ten days after the fall of Ghent). The congress; Flanders surprised; "nos
  falta"; two months; the Brunswick princes; "estamos muy mal puestos"; "melancólicas reflexiones".
- **R984, Ronquillo, 26 Feb 1678.** On Fuenmayor's reports of the assembly of the northern allies. Everything hangs
  on the resolutions of the English parliament and on whether the King really breaks with France. The Danes
  complain about subsidy remittances. Brandenburg is in Pomerania. The Duke of Hanover's intrigue ("esta trama")
  runs through his kinship with Madame.

## Files

`try.py` (the key plus additions), `seg.py` (segmenter), `read.py` (all twenty letters → `read/R*.txt`, each with
DECODE's margin transcription where there is one). 22 Oct 2026: `keyx.py` (key + sibling additions + em.py values),
`mktx.py` (DOC -> `tx/`), `txi/` (image-corrected transcriptions), `dec2.py` + `sense.py` (decode and sense measure ->
`read2/`), `spaced.py` (decode cut into words, page by page -> `read/R*.dec.txt`), `read/R*_reading.md`, `_en.md`,
`_reread_log.md`, `_corrections.tsv`. Profile edits: `research/reading_audit/reread_ronq.py`.

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: '## Reading' headings added after the titles of read/R966-R984_reading.md (14 files; the sweep had scored the notes with the readings): bodies plain 0.69-0.91 and explicit 0.90-1.0, except R982 (unmargined, read on the image) plain 0.552, explicit 0.828: its plain failures are gaps of the Spanish word list and the known soft-scan / no-key holes, about one per failing sentence; it keeps read on the reader's judgement. The readings' headers say spelling was modernised; not redone in this pass. Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.

**23 Oct 2026, v6 spelling check (research/reading_audit/v6_spelling_files.txt; REREAD_BRIEF step 3-4: no modern spelling in a reading)**: read/R*_reading.md (20 letters) said 'Spelling modernised'. The 22 Oct margin transcriptions were not saved as files, so the spelling was restored from the key decode (read2/R*.txt), the writer's own letters, with research/reading_audit/v6_charalign.py: tomavan, assi, devia, aora, quando, haver, envarazados, Magestad where the key's letters spell the same word; editorial accents off; ñ kept where the key writes n. Holes and brackets kept, no word changed. Explicit-hole shares unchanged (0.828-1.0); all keep read.

## Remaining gaps

- R983 f. 1 passage, many holes - blocker: illegible; the margin is faded almost to nothing on the DECODE scan and groups l, c, 1q, L2, pA, 11, 300 are not in the key
- R982 opening groups and about ten phrase-level holes (12 marks, 27 unread words by the count of 14 Nov 2026); R984 about 11 code groups (M, 491, 36, dul, lop, 188, the al of "los [al]eses", 113, 138, cus, 600) - blocker: no-key-material; no margin on either letter and no gloss that fits these codes in the eighteen margins; [?habra] and [?tenemos] hang on figures (21/31, bc/oc) that two readings of the image did not settle
- single uncertain words in R966, R967, R968, R971/R972, R976, R977, R979, R981, R1001 - blocker: illegible; margin faded or blotted at that word and the figures do not settle it

## Escalation

- [x] siblings: all twenty letters of SEG 2559 taken; R1000 already decrypted on DECODE
- [x] clear-pages: eighteen margin decipherments transcribed from the images and aligned with the key decode (22 Oct 2026; R970 and R973 margins found in DECODE comments)
- [x] known-keys: Balbases 1677 key (with hernannunez1674 additions) fits unchanged
- [n/a] print: no printed edition of Fuenmayor's incoming letters is known from the sibling targets
- [x] key-rebuild: 22 Oct 2026, about 60 code values from the margins added to keyx.py (conflicting groups left as they were, listed above)
- [x] retry (14 Nov 2026, Brice Dudout, PR #601): R982 re-read on the full-size images where it had holes; twelve closed; fin, al, 91 keyed from the sibling margins
- [x] retry: 22 Oct 2026, every letter built into sentences and translated; R982 and R984 re-transcribed from the images and read with the key (read/R*_reading.md, _en.md)
