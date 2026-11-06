# "Ex Conde" cipher letters to Diego José Dormer, Catalonia 1693-1696 (catalogue 1272)

Status: read in part (Brice Dudout, 5 Nov 2026; key partial by our protocol: held-out measurements 0.577 and 0.594, under our 0.60 threshold; slip recto and passages of views 169-187 read, slip verso and view 193 read in part; 290 counted cipher words, 91.7% without restorations).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents, for your catalogue entry 1272 (BNE/Hispana sweep).
Not yet published on our site. Text only: the BNE Digital images were used for research and are not reproduced here.

## Documents

Madrid, Biblioteca Nacional de España, MSS/8387, *Cartas políticas y particulares dirigidas a Diego José Dormer*, vol. VI
(BDH bdh0000064262). The volume is served as two PDF halves; "view" below is the rank of the image in the digitisation
(1-134, 135-269), not the folio. Of 269 views, 26 carry cipher: view 10 (one line of geometric signs, another system, 1680s,
not treated) and views 132-197, all in one number cipher. Those letters are signed "Ex Conde" or "El Conde", or with
pseudonyms ("Rojo", "Zabulón", "El Chismoso"), with pseudonymous addressees on the back ("Zacarías", "Astulio"), from
Barcelona, Mataró, Hostalric and Zaragoza, 1693-1696. **The writers are not identified.** Three web searches found no source
naming a correspondent of Dormer in Catalonia in these years; we do not guess.

Two documents in `profile.json`:

- **slip190**: an inserted slip wholly in cipher, fol. 190r-v (views 196 recto, 197 verso), 974 signs, undated. Its content
  (Palamós still in Spanish hands) puts it before the French siege of June 1694. On the verso the end of every line is hidden
  in the binding.
- **passages**: the ciphered words and phrases inside letters in clear, views 132-193, 1,735 signs. Views 132-168 (1,474 signs)
  are the training set A on which the key was built; views 169-193 (261 signs) are the second held-out set H2.

Content. The slip: the muster at Gerona, held under a proclamation (death and twelve doubloons to informers), but leaving out
the sick and the newly arrived cavalry and not merging the officerless troops into the old companies, "all to reduce the
numbers so as not to march out of Gerona"; 2,562 foot inside Gerona, 1,500 to be drawn from Castellfollit and Palamós; the
blame laid on the generals; the verso, in fragments, on the crown, Catalonia and Castile. The passages: a night with no
generals and no rounds and the cavalry caught unsaddled ("El Chismoso", 3 May 1694, before the battle of the Ter); "Amigo
Dormer"; a deposit of money at the Treasury (Angulo, Juan de Torres); the viceroy Villena (duke of Escalona), San Martín,
Monforte, the Diputación; later (1695-1696) "I am an enemy of Bavaria", a man "coward, mad, proud, shameless", Montalto put
at the head, the blame laid on the maestre de campo general.

## System and key

Simple substitution: one number per letter, 1-25, written with dots between them (`key.tsv`): 1 f, 2 g, 3 e, 5 d, 6 c, 7 b,
8 a, 9 h, 11 i, 13 l, 14 m, 15 n, 16 o, 17 p, 18 q, 19 r, 20 s, 21 t, 22 u, 23 x, 24 y, 25 z. The alphabet is in two runs
(a-h running down from 8 with e at 3 and f, g at 1, 2; i-z running up from 11). 4, 10 and 12 were never seen; no value is
guessed for them. In the short passages word gaps are kept; the slip runs on. Two sign shapes are labelled by us: "7" for
the sign like ")" and "17" for "1)".

The key was built on the training set A only, from frequencies and a fixed list of cribs suggested by the clear text
around the passages (kept: "amigo" before "Dormer" in view 157, "Cataluña" after "Amigo" in view 168, guardias, caballo, que,
noche, Villena), then annealing on Spanish quadgrams constrained by those cribs. It was frozen (SHA-256 e40e8fd7...) before
either held-out set was decoded.

## Validation

`validation.txt`. There is no contemporary decipherment, so the measure is M5: the share of the decoded letters of a held-out
set that a maximum-coverage segmentation covers with Spanish words of at least 5 letters (your `lang/lexicons/es.json.gz`,
plus 45 names fixed in advance), against 200 keys made by shuffling the key's values (seed 1693). Criterion fixed in advance:
M5 >= 0.60 and M5 >= best control + 0.30.

| Held-out set | signs | M5 | best of 200 controls | margin | result |
|---|---|---|---|---|---|
| H: slip fol. 190r-v | 974 | 0.577 | 0.033 | 0.544 | partial |
| H2: every passage of views 169-193 | 261 | 0.594 | 0.042 | 0.552 | partial |

Both independent measurements clear the margin by far and both miss the 0.60 threshold, so **the key is partial by our
protocol**. We see two causes, after the fact, and we changed nothing for them. First, the slip's verso: its 24 line ends
lie in the binding, which leaves short fragments that 5-letter words cannot cover (with a few spellings of the writer, such as
"guntos" for juntos, and the abbreviation MRA). Second, H2 is small: 261 signs in 25 segments, many of them a single word
(CULPA, CARGO, MADRID), so a few short words weigh heavily. H2 was meant to be a fully ciphered block of at least 400 signs,
but none exists in views 169-194. The change was declared in a hashed amendment before transcription, and the real count
(261) was declared before decoding. The transcriptions that were measured were not changed afterwards.

## Reading

`transcription_slip.txt`, `transcription_passages.txt` (signs, one manuscript line per line; for A, the clear text around each
passage is given abridged in «...»), `decryption_slip.txt`, `decryption_passages.txt` (mechanical, line for line),
`reading_slip.md`, `reading_passages.md` (Spanish, marked: {x} probable, [x] restored, ‹x› unresolved, with the count of each
piece), `translation_slip.md`, `translation_passages.md` (English). The readings were made after the measurements. Counted
by script on the reading files, by your rule (certain + probable; a word with a restored letter counts as restored; only
cipher words, numbers not counted):

| Piece | words | certain | probable | restored | unresolved | read without restorations | state |
|---|---|---|---|---|---|---|---|
| Slip, recto (view 196) | 133 | 125 | 6 | 1 | 1 | 98.5% | read |
| Slip, verso (view 197), visible words | 103 | 82 | 0 | 14 | 7 | 79.6% | read in part |
| View 169 (Hostalric 1695) | 9 | 8 | 1 | 0 | 0 | 100% | read |
| View 180 | 8 | 5 | 3 | 0 | 0 | 100% | read |
| View 182 | 2 | 2 | 0 | 0 | 0 | 100% | read |
| View 184 (Mataró 1696) | 17 | 17 | 0 | 0 | 0 | 100% | read |
| View 186 | 2 | 1 | 1 | 0 | 0 | 100% | read |
| View 187 (Mataró 1696) | 1 | 1 | 0 | 0 | 0 | 100% | read |
| View 193 (inserted leaf, fol. 187) | 15 | 14 | 0 | 1 | 0 | 93.3% | read in part |
| **All counted** | **290** | **255** | **11** | **16** | **8** | **91.7%** | read in part |

The training set A (views 132-168) is decoded in `decryption_passages.txt` and reads as Spanish, but we did not grade it word
by word: it is the set the key was built on, so it is not in the count and not translated. Doubtful signs at 120 ppi
(15/19, 17/19, 5/13) were settled by the sense in the readings only, for example v150 "patrullas", v196 "soldados", v165
"veedor".

## Remaining gaps

- Slip verso (view 197): the end of all 24 lines is hidden in the binding; 14 words restored, 7 unresolved, 79.6% - blocker: needs-physical-access; an image of the volume opened flat, or the original.
- View 193: one word restored ("[s]e" before Villena), 93.3% of 15 words - blocker: illegible.
- Doubtful signs 15/19, 17/19 and 5/13 at 120 ppi - blocker: illegible; a high-resolution image would settle them sign by sign.
- Signs 4, 10 and 12 never occur - blocker: too-short.

Also open, not blocking: the identity of "Ex Conde" and of the pseudonyms (Rojo, Zabulón, El Chismoso, Zacarías, Astulio).

## Escalation

- [n/a] siblings: the other Dormer volumes at the BNE (MSS/8382-8386, vols. I-V) were not opened; their catalogue records do not mention cipher, and BNE Digital is not reachable from the write-up session (5 Nov 2026), so they stay a lead for a session with access.
- [x] clear-pages: the clear text around every passage was read for context and cribs; no contemporary decipherment, gloss or key in the volume.
- [x] known-keys: no key for this correspondence is known in print, on DECODE or in this repository.
- [x] print: no edition or study of these ciphered passages found (web searches, Tomokiyo, DECODE, 5 Nov 2026).
- [n/a] key-rebuild: the key was rebuilt here; 4, 10 and 12 never occur.
- [x] retry: every doubtful sign re-read by the sense with the frozen key and regraded; the measured transcriptions were left as they were.

## Not gaps of this entry

Noted 5 Nov 2026, at the write-up:

- Training set A (views 132-168, 1,474 signs) is decoded in `decryption_passages.txt` and builds Spanish sentences (v150: "aquella noche ni generales ni ordenes se vieron, nadie reconocio los puestos ..."); by the protocol it is the set the key was learnt on, so it is not graded or counted. It is not an unread piece.
- View 10 (one line of geometric signs, 1680s) is another system and so another entry (one key, one entry): it stays open in catalogue 1272, narrowed to it.


## Prior work

Catalogue: open (vetted 4 Nov 2026: the cipher seen on ff. 129-130, no decipherment). Our check before the attempt found no
target folder, PR or issue for Dormer or 1272 here, nothing at Tomokiyo's, and no edition or reading of the ciphered
passages on the web. If an edition holds a reading, we will credit it.

## Method

One agent transcribed the slip first and set it aside, then transcribed the training set, built and froze the key, and
measured once. A second agent wrote and hashed an amendment for H2 before transcribing it, measured once with the same key and
script, and read the pieces. Images at 120 ppi, no human check against the images yet.
