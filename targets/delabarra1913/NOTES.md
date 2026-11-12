# delabarra1913: Francisco León de la Barra, New York, to Relaciones Exteriores, 11 August 1913 (catalogue 1463)

WAINUT, 12 Nov 2026. Work done with AI language-model agents viewing the CEHM images; no human palaeographer has
checked the text. An independent AI language-model agent reviewed the reading from the scans (below).

Read in part, 12 Nov 2026: X-1.4.310.1 is read in part (strict count). Written up on the site (delabarra1913.html) at the
integration of PR #467, 12 Nov 2026.

## Document

CEHM-Carso, Fondo X-1 (Manuscritos de Francisco León de la Barra), X-1.4.310.1, 2 images:
- 0001: pencil text, "Telegrama / N-Y- Aug. 11-13 / Secretaría Relaciones = México =", 13 lines, signed "Delabarra";
- 0002: typed copy, "august 11th - 13 / Secretario Relaciones - Mexico City - Mexico", same text, letters regrouped.

Images (direct JPG, no login): http://visor.cehm.org.mx/assets/docx/fondos/jzd/X-1/4/310/1/X-1.4.310.1.0001.jpg and
.0002.jpg. Scans are not in this folder.

Clear Spanish with 27 cipher words (216 letters). The two copies agree on 215 of 216 cipher letters; the typist dropped
one h in "invitación" (transcription_310.txt).

## System

Lower-case monoalphabetic letter substitution, 20 cipher letters seen (key.tsv). W is written as two v (qq) in
Washington and Wilson. r stands for h (Washington) and for t (latino, reconocimiento), while n is t in nine other
places; rr stands for the y of Bryan (marked as a repair). A different key from the 1912 Mundic telegrams and from the
fondo's key sheet X-1.5.466.1 (tested both ways: no Spanish; scripts/keysheet_test.py, output in
work/keysheet_test.txt).

## Key source

Ciphertext only, with the clear words as context. Simulated annealing on the 216 cipher letters with Spanish 4-grams
converged on most of 12 restarts to "long seccion asuntos latinoamericanos departamento estado ..."; the rare letters
q (v), l (f), s (x) and r (h/t) were set by hand from the words they occur in.

## Held-out test

key_frozen.tsv holds the 18 letters used in the cipher words of lines 1-6. Applied mechanically to lines 7-13
(scripts/heldout.py): **110 of 112 letters right (98.2%), 0 wrong, 2 not in the frozen key** (l in conferenciar and s in
próximo, one occurrence each); 14 of 16 groups wholly right.

Statistical check (docs/_validate.py on validation.tsv, 214 read letters, es-modern 4-grams): the reading scores
-2.275 per letter, against -6.85 for random keys of the same structure (z 7.5) and -3.67 at best for a key annealed
onto the shuffled ciphertext (z 12.2). Verdict: pass.

## Reading

reading_310.md, translation_310.md. In short: "Señor Long, jefe sección asuntos latino-americanos departamento estado" (the contributor identifies him as
Boaz W. Long; the telegram does not give the first name), came from Washington to see De la Barra, surely sent by Wilson and Bryan; De la Barra would gladly confer
with them if formally invited; if invited he leaves for Europe next Saturday, if not invited by tomorrow, on Wednesday;
the ministry is to set out the reasons of justice and expediency for immediate recognition (of the Huerta government).

27 cipher words: 24 verbatim, 3 with a marked repair (vv for W twice, rr for y once), 0 guesses, 0 holes.
Strict share 88.9%; 96.3% if vv for W is taken as the encoder's spelling. State: **read in part** (strict); the
independent review kept the strict count and agreed with read in part. Dan's reading checker (docs/_check_reading.py
--file, origin/main 4a71baf89) on reading_310_sentences.txt: clean share 0.5 (3 of 6 sentences, hole rate 0.13); the
flagged words are names (Wilson, Bryan, Delabarra) and modern words absent from the period word list (conferenciar,
invitación, entrevista and the like), not unread cipher.

`python scripts/check_marks.py` rebuilds the decryption and fails on any unmarked departure; it passes.

## Integration check (12 Nov 2026)

Done by the integrating session. Reproduced: check_marks.py passes (24 of 27 cipher words verbatim = 88.9%); heldout.py
gives 110 of 112 on lines 7-13, 0 wrong. Own control (lang es-modern, 4-grams): the held-out lines score -2.238 per
letter against -6.47 for 2000 shuffled-value keys (best -4.00, z 5.6); the full key -2.412 against best -4.87 (z 6.9).
The clear words around the cipher words guided the key (stated above); the held-out lines have their own clear words.
Image X-1.4.310.1.0001 (the pencil copy) was fetched from the CEHM viewer (no host refused) and compared line by line
with transcription_310.txt on the images: all groups agree (number of letters compared not recorded); the typed copy was fetched and not re-compared letter by letter. The
freezing of key_frozen.tsv before the held-out count rests on the contributor's record (one commit, no external
timestamp). The profile's earlier fraction_read of 1.0 was key coverage; the strict word share is 0.889.

## Remaining gaps

- Bryan: the group xgrroz gives b-r-r-r-a-n; rr for y is unexplained and marked. - blocker: too-short; no other y in
  the telegram to test a value. The typed copy has the same letters, so it is the encoder's own spelling.
- s = x and l = f each rest on one word (próximo, conferenciar). - blocker: too-short.

Not reading gaps: the CEHM catalogue summary of X-1.4.310.1 was not compared with this reading. There is no blind
transcription by a second reader beyond the typed copy (an independent witness of the letters) and the review below,
which checked all 7 typed lines and pencil lines L03, L06, L07 and L13 and found no difference.

## Prior art (checked 12 Nov 2026)

No decipherment on either copy. Web search "León de la Barra August 1913 New York Boaz Long telegram recognition
Huerta Bryan Wilson" found FRUS 1913 and press items on De la Barra's journey (Havana 4 Aug, on to Europe via New York)
and a Boaz Long memorandum cited in the literature, but not this telegram or its decipherment. The vetting of 2 Nov 2026
(DECODE, Tomokiyo, Lasry, Narváez titles) found no edition. No collision in dbourdeau/cyphersolver (12 Nov 2026).

## Independent review (12 Nov 2026)

An AI language-model agent that did not take part in the solve read the scans before opening any transcription,
re-ran every script, and read the text as sentences against the translation. Its sign check of all 7 typed lines and
the pencil lines L03, L06, L07 and L13 found no difference between the images and the transcription. It reproduced the held-out count (110/112,
0 wrong; 14 of 16 groups wholly right) and the mark check, found six coherent sentences with no holes, and agreed with
read in part on the strict count, 24/27 = 88.9% (grade A). Its grade is recorded as `reading_review` in profile.json.

## Escalation

- [x] siblings: the other items of catalogue 1463 opened: X-1.3.207.1 and X-1.3.239.1 (1912, another key, target
  mundic1912), X-1.4.380.1 (clear), X-1.1.94.1 (clear letter with person numbers, seen at the 2 Nov vetting; its key
  is not in the file), and the key sheet X-1.5.466.1.
- [x] clear-pages: the typed copy (image 0002) checked; it is a second copy of the cipher, not a decipherment.
- [x] known-keys: the fondo's key sheet X-1.5.466.1 tested in both directions (scripts/keysheet_test.py): not this key;
  the 1912 key of the Mundic telegrams differs as well.
- [x] print: one web search (12 Nov 2026; FRUS 1913 and press items on the journey, not this telegram) and the vetting
  of 2 Nov 2026 (DECODE, Tomokiyo, Lasry, Narváez titles); no edition found.
- [x] key-rebuild: every cipher letter has a value (key.tsv), from annealing and by hand.
- [x] retry: the one disagreement between the copies settled on the image; the gaps left have the blockers above.

## Files

transcription_310.txt (+ _pass1 pencil copy, _pass2 typed copy), decryption_310.txt, reading_310.md,
reading_310_sentences.txt, translation_310.md, key.tsv, key_frozen.tsv, validation.tsv (cipher letter and reading
pairs for docs/_validate.py), scripts/ (decrypt.py, check_marks.py, heldout.py, keysheet_test.py), work/ (sa.py and
saw.py, the annealing solvers, which need two Project Gutenberg Spanish texts, pg2000 and pg15532, not included;
keysheet_test.txt).

AI language-model agents (WAINUT) did the transcription, solve and reading; no human palaeographer checked it.
