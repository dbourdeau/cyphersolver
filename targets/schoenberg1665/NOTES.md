# schoenberg1665: Schönberg's journal of the Dresden negotiations, early December 1665, one cipher passage (LATh - StA Altenburg, Schönbergische Sammlung Nr. 107, fol. 114r)

Status: read in part (Brice Dudout, 9 Nov 2026; 32 words: 25 certain, 4 probable, 2 restored at the binding edge, 1 unresolved; 29/32 = 90.6% read by sense without the restored words, under the 95% rule; key recovered from the cipher, partial on its held-out test, 0.625 vs best of 200 shuffled keys 0.3125). New text.

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. Source: **Landesarchiv Thüringen - Staatsarchiv
Altenburg, Schönbergische Sammlung (1-99-0023), Nr. 107 ("Acta Reiffenbergica")**; digitisation **ThULB Jena**
(urn:nbn:de:urmel-stat-262972), licence **CC BY 3.0** (https://staatsarchive.thulb.uni-jena.de/receive/stat_file_00004364,
checked 9 Nov 2026). Not in the catalogue. Same archive as `thumbshirn1647` (Nr. 85).

## Document

Nr. 107 is Schönberg's journal of the negotiations at Dresden between the Wettin houses and Electoral Mainz over Erfurt
(the Reiffenberg affair), 26 Oct - 23 Dec 1665. One passage of nine lines on fol. 114r (image 0233, early December) is in
cipher, between "… ihn aber auch in einer sache also gangen -" and "Frankreich habe …". No other cipher and no decipherment
in the volume (396 images checked).

## The system and the key (`key.tsv`)

Simple substitution in Latin letters with a regular key over a 24-letter alphabet: odd plaintext letters -> z y x w u t s r
q p o n (reversed), even -> a b c d e f g h i k l m. Word division is kept. Known keys were tried first (Thumbshirn's numeric
key of Nr. 85; Dresden HStA nomenclators): none applies (`frozen/CLES-CONNUES.md`).

## Validation (`validation.txt`)

Transcription frozen before any key was tried; protocol `frozen/PREREG.md` hashed before any key or decoding (it declares that
repeated short words had been noticed). Key learnt on lines L1-L5 only; one measurement on held-out lines L6-L9 (16 words):
German lexicon share **0.625** against at best 0.3125 for 200 shuffled keys (margin 0.31): **partial** (validated needs 0.70).

**Declared after the measurement**: the key was completed from its regular pattern, and five transcription errors were
corrected on re-reading the image: L1 capital A, not L ("Boyneburg"); L5 capital W, not L ("Gott"); L4 q, not g; L7 t, not b;
L9 w. The frozen `frozen/H-CHIFFRE.txt` was not modified; the corrected text is `transcription_0233.txt`.

## Reading (`reading_0233.md`)

"Boyneburg - rede viel ‹diengs›, der Churfürst habe dreysigtausend Thaler pro iuribus {Erfordensibus} ge[w]onnen: Gott möchte
ih[n] behü{ten}, er habe den {seinen} bey [T]eufel holen geschwohren, und Leute darüber zu Zeu{gen} angerufen." 25 certain,
4 probable, 2 restored, 1 unresolved: 29/32 = 90.6% (31/32 = 97% with the restored letters): read in part.

## Prior work (re-checked 9 Nov 2026)

Nothing in this repository (catalogue, leads, key_leads, candidates, issues: no Reiffenberg, Schönbergische, Acta Reiffenbergica).
No edition of the journal or the passage found (LATh and ThULB records cite none; web searches); the printed histories of the
Erfurt affair were not checked volume by volume. No decipherment of the time.

## Remaining gaps

- ‹diengs› (cipher buxswi): letters certain, sense uncertain (Dings? dienst?) - blocker: open-codes; and two letters lost in the binding (ge[w]onnen, [T]eufel), which need the original volume

## Escalation

- [x] siblings: the whole of Nr. 107 checked (396 images): no other cipher, no decipherment
- [x] clear-pages: the clear text around the passage read; it gives the context, not the cipher
- [x] known-keys: Thumbshirn's key (Nr. 85) and the Dresden nomenclators tried: not applicable
- [x] print: LATh and ThULB records, web searches; no edition found
- [x] key-rebuild: key completed from its regular pattern after the measurement
- [n/a] retry: the letters are all read; what is left is sense and the binding edge
