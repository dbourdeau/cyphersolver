# SP 106/7, DECODE R597: instructions for the Stosch–Walton cipher

Status: explained (read in full), 21 Sept 2026. Catalogue item 64 (class B), removed.

**Record.** TNA SP 106 box 7, images 0091–0092 (DECODE R597, "Partially decrypted", nomenclator, numerical,
cleartext English, plaintext French, date = volume span 1702/1837). DECODE: "Part of letter with instructions ...
lines unsolved ... nomenclature could not yet be identified." Images fetched with the stored DECODE cookie
(`decode/`, git-ignored).

**What it is.** Not a ciphered letter: a one-leaf English instruction sheet (folio 33, bifolium with the end on the
facing page) sent with a cipher "which serves only to correspond with Baron Stosch and Mr Walton who reside at
Rome [Florence]". Philipp von Stosch was the British government's spy on the Stuart court in Rome from 1722 and
signed his reports "John Walton"; he moved to Florence in 1731, which the correction Rome → Florence reflects. So
the sheet is c. 1731 or a little later, from the Secretary of State's office to a British correspondent.
Whether "Stosch and Mr Walton" is the writer's naivety or a deliberate two-name cover is not settled.

**The system (all stated on the sheet).**
- Syllabic code of three-digit groups 100–999: syllables and letter pairs (le, ad, her, en, du, pre, te, nd, an...).
  DECODE's "letter pairs rather than words" is right.
- Two keys, A (black ink) and B (red ink), used alternately at will; 371 in Key A = "changement de clef".
- Groups run on without separation; the decipherer cuts them in threes.
- Nulls: 110, 220 &c. and everything above 900.

**The worked example**, "Les Adherens du Pretendant se donnent beaucoup de mouvement à Rome", is given entirely
in Key A, then again switched to Key B after "donnent". Every group has its syllable written above it, so the
whole sheet reads; the "lines unsolved" in DECODE's note are the same Key-B example written run-on
(3714364333422184466...0 4175534530236208477) to show how a letter looks. Full text: `transcription.txt`.

**Doubtful.** Group 702 appears for both "du" and "up" in Key A (one is probably misread or a slip of the writer);
Key B "tà" read 023, below the stated range 100–999; the run-on line has one digit more than the separated groups
(…620 8477 vs 620|477). None affects the reading.

**Prior art.** DECODE described the sheet but did not read the examples. No printed edition checked; the keys
themselves (A and B) are not on the record. Among the 16 SP 106 key records, none checked for Keys A/B yet: that
would give the full nomenclator, but the target (the sheet) is read.

**Open lead.** Stosch's own letters in SP 98 (Tuscany) / SP 85 are in this cipher; the keys A and B may survive in
SP 106. Not part of this target.

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: transcription.txt is a clear instruction sheet; its prose without the digit tables: plain 0.706, explicit 0.882 (failures: the French example sentence, the digit run). Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.

**14 Nov 2026, full-texts pass.** `outcome.texts` listed `transcription.txt` as transcription and as reading. Split:
`cipher_groups.txt` now holds the cipher as written, i.e. only the code groups of the worked example (28 of Key A,
13 of Key B with the 371 change-of-key group, and the run-on line), extracted from `transcription.txt` without
change; `transcription.txt`, the whole clear sheet with the writer's syllables over the groups, stays the decryption
and reading. Nothing was re-read on the image (DECODE full images need the login); doubtful groups keep their [?].
