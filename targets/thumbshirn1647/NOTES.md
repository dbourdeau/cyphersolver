# thumbshirn1647: the Saxe-Altenburg envoys at the Westphalian congress (LATh - StA Altenburg, Schönbergische Sammlung Nr. 85): 1647 key rebuilt and validated; a postscript of 1648/49 read with Thumbshirn's key

Status: read (Brice Dudout, 9 Nov 2026; postscript 0837 read 23/23 words, 20 certain and 3 probable, with the period key of image 0003 unchanged; the 1647 homophonic key rebuilt from the decipherments of the time and validated on a held-out letter, 0.966 vs best of 200 shuffled keys 0.245). New text: the postscript only; the 1647 cipher passages have their decipherments of the time.

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. Source: **Landesarchiv Thüringen - Staatsarchiv
Altenburg, Schönbergische Sammlung, Nr. 85**; digitisation **ThULB Jena** (urn:nbn:de:urmel-stat-251122), licence **CC BY 3.0**
(checked on the ThULB record, https://staatsarchive.thulb.uni-jena.de/receive/stat_file_00004384, 9 Nov 2026). Not in the catalogue.

## Documents

Nr. 85: "Korrespondenz der Sachsen-Altenburgischen und Sachsen-Coburgischen Gesandten Wolfgang Conrad von Thumbshirn und
Dr. August Carpzov mit Johann Friedrich von Brand und Herzog Friedrich Wilhelm II.", Osnabrück 1645-1651.
- Image **0003**: "Chiffreschlüssel Thumbshirns", a signed key, simple substitution (24 letters, numbers 1-52), with the note
  that the numbers are written "continuirlich serie" so that words cannot be guessed (`key_0003.tsv`).
- Letters of **13 Nov - 25 Dec 1647** with cipher passages in a homophonic system (2-3 numbers per letter, 5 to 90) and, for
  each, a decipherment of the time on a slip (0549, 0559, 0571, 0581, 0599, 0605): existing.
- **Image 0837 (fol. 399)**: an undated postscript (late 1648 / early 1649) with one cipher sentence in the key-0003 system and
  no decipherment: the new text.

## The keys

`key_1647.tsv`: rebuilt from the decipherments of 13 Nov, 17 Nov, 22 Dec and 25 Dec 1647, aligned number by number
(`frozen/BUILD-PAIRES.tsv`), 49 values, majority vote; no serious contradiction. `key_0003.tsv`: the period key sheet,
transcribed and hashed before any decoding; it does not read the 1647 letters (0.13 on the held-out letter, chance level).

## Validation (`validation.txt`)

Protocol `frozen/PREREG.md` hashed before any decoding. Held-out letter of 24 Dec 1647 (0569, 0573, 0574), cipher hashed before
learning, key frozen before its decipherment (0571) was opened. 9 passages, 441 gloss letters: **0.966** against at best 0.245
for 200 shuffled keys (margin 0.721), coverage 99.8%: **validated**. Remaining differences are transcription or encipherer errors.

## Reading (`reading_0837.md`)

"O miseros {nos} servos. Gott weis und hat meine {Zehr[e]n} {geseh[e]n}, die ich bereit viel vergos[s]en üb[e]r der
schandlich[e]n Servitut, darein wier geführet." 23 words: 20 certain, 3 probable (two numbers under stains), 0 restored,
0 unresolved. Declared deviation: read with key 0003 unchanged and by sense; the pre-registered test measured the other system.

## Prior work (re-checked 9 Nov 2026)

Nothing in this repository (Thumbshirn, Altenburg, Schönbergische Sammlung, Carpzov: no target, entry or lead). No edition of
these letters: the ThULB record cites none; Acta Pacis Westphalicae and Meiern (1734-36) print other Saxe-Altenburg material;
M.-E. Brunert's study of Saxe-Altenburg at the congress uses Nr. 86, not Nr. 85; no study of the cipher found. Every 1647
cipher passage has its decipherment of the time, so those texts are existing; 0837 has none. Related but distinct: catalogue
**1639** (Magdeburg envoys at Osnabrück, LASA A 1 Nr. 530), not compared.

## Remaining gaps

None for the target texts: the postscript reads in full and the 1647 passages are read by their decipherments.

## Escalation

- [x] siblings: the 1647 letters with their decipherments gave the homophonic key; the 24 Dec letter was held out
- [x] clear-pages: the decipherment slips of 1647 used for learning and as the held-out reference
- [x] known-keys: Thumbshirn's key sheet (image 0003) transcribed; it reads 0837 and not the 1647 letters
- [x] print: ThULB record, Acta Pacis Westphalicae, Meiern, Brunert checked; no edition of Nr. 85
- [n/a] key-rebuild: the 1647 key is validated and 0837 reads with the period key
- [n/a] retry: nothing unread
