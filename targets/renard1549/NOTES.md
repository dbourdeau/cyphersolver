# renard1549: copy of the imperial ambassador's dispatch from Paris, 12 July 1549, on a French plot against the castle of Nice (catalogue 1560)

Status: read in part (10 Nov 2026). Contributed by Ivan Sourvillo (GitHub sourvillo, issue #373 and its two follow-up comments of 10 Nov 2026), working with Claude as his agent. The project checked his files against his stated key (`VERIFICATION.md`); it did not see the images, because the Estense IIIF host was not reachable from this session.

## The document

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera K, Karl V, sfasc. IV, cc. 131-132; Lodovico record e7e65c38-4c54-48b1-8003-6da1c5c2ba1b, IIIF manifest https://edl-jarvis.cultura.gov.it/meta/iiif/e7e65c38-4c54-48b1-8003-6da1c5c2ba1b/manifest. Catalogue entry 1560 listed it as the undated cipher letter of the Charles V → Ferrante Gonzaga file, unread (`gonzaga1549/NOTES.md`: "undated cc.131-132 … blocker: no-key-material"). c.131r (heading and 35 lines) and c.131v (15 lines) are in cipher; c.132 is blank or bears no address (catalogue entry, 9 Nov 2026). Images CC BY-NC-SA; none are reproduced here.

In the contributor's reading the leaf is a **copy**: the heading reads *Copia de la [?carta] del embaxador en Francia*, and the subscription *De París, a doze de Julio de mil quinientos y quarenta y nueve*. It is the copy that Charles V sent with his letter of 15 July 1549 (sfasc. IV cc. 40-42): the archival decipherment c.41 (`targets/gonzaga1549/c41r_plain.txt`) says "por la copia de la carta que va con esta entendereys lo que nuestro embaxador en francia nos ha scripto … cerca de la empresa que los franceses quieren hazer del castillo de niza". The contributor names the ambassador as Simon Renard, from the *Calendar of State Papers, Spain* IX, which prints extracts of Renard's letters from Paris of 14, 18 and 28 July 1549; that identification was not checked here.

The leaf is a different key from the gonzaga1549 letters (the Imperial sign cipher of 1544-1554): it is the 1548 numeric syllabary of the 15 Jul 1549 letter, so it has its own folder ("one key, one entry").

## What it says (contributor's reading)

The ambassador reports that at about eight in the evening a man who says he is from Navarre, of the following of the lord of Tende (Claude de Savoie, governor of Provence), told him of an enterprise against the castle of Nice resolved by the [?King] and his [?Council]: two men, Care (a *contrareleur*, controller, of the Duke) and Chaulve[?x] (an [office] of the Duke, formerly in the service of the Marquis del Vasto), have won over 63 [?Savoy]ard soldiers of the garrison, under the prior; for [?crowns] and four pays in perpetuity they will sell the castle to the Count of Tende, who is to come with twelve galleys and 300 soldiers under cover of the fort the King is building at Antibes; the enterprise is to be done in Tende's name, on his claim that the Duke withholds villages in the valley of [?Augusta] (Aosta). The informant asks that the service be remembered, promises to show letters of the two plotters, and will go to the ambassador in Genoa to warn him of the exact time. The ambassador asks how to deal with him.

## The cipher and key

The 1548 numeric syllabary (Doria-Figueroa family, Tomokiyo's description; `gonzaga1549/NOTES.md` "Systems identified"), corrected by the contributor on c.40r against c.41: consonant number + vowel mark (dot above a, two dots i, dot below e, dot after o, ring u); bare numerals single letters (a1 … z22, with 19 = u and 20 = v new) or consonant + a (15 = ra); specials (3^2 m, 3^3 n, 3^7 r, 3^8 s, H° ll, x° ss, & rr, XP ñ, e^9 a, 2oo yu); nulls with superscript 13 or 12; code words (dan tra, don tro, fen pro, fon pre, vana embaxador, gis Francia, filo Niça, infle Génoua, lab galera …) from the c.40/41 alignment, and others from context only (fin pri, den tre, hic Duque, oria/ocia/ning Rey, rac Consejo, apud V. Md., allo escudos, bit Saboya …). Full list in `key.tsv`. Tomokiyo's description as written did not fit; the corrections are the contributor's.

## How the contributor got it

1. Aligned c.40r sign by sign against c.41: vowel-mark rules, nulls and the sure code words.
2. Transcribed c.131r-v from deskewed native-resolution IIIF crops: 51 lines, 1,360 signs (measured, `transcription.txt`, label column dropped).
3. A beam decoder with a 6-gram Spanish letter model (Don Quijote plus the repo's 16th-century Spanish readings) over the signs, marked signs held to their key values.
4. Read the output as Spanish and rechecked the crops where it broke (rounds 2-4: 19/20, e^9, &, XP, 2oo, context values of code words).
5. Second pass (comment 1): plotters identified from Gioffredo's *Storia delle Alpi Marittime* (Historiae Patriae Monumenta, Scriptores II, Torino 1839, cols. ~1401-1402, roll of the Nice garrison in the 1543 siege): Care/Car = probably Nicolò di Beaumont detto Carra, treasurer of Savoy and of the castle; Chaulve-F = probably Antonio de l'Eschaulx, former bailli of Savoy, of Aosta, and captain of the castle before the Grand Prior of Lombardy came; fin = pri, so "debaxo del cargo del prior de [bit]" (the castellan was Paolo Simeoni de' Balbi, Grand Prior of Lombardy); hic = Duque (Charles III of Savoy); r35 `20` may be `2°` = bu, "le auía burlado con palabras".
6. Correction (comment 2): r2 `4_ 12 18^ ∝ T` = *de Navarra* (the sign transcribed Q is ∝) and v9 `12 18 & 13` = *navarro*: the informant is a Navarrese, which ties him to the "Navarrese" of the Calendar extracts of 18 and 28 July 1549. These corrections are applied in `reading.md` and `translation.md`; `transcription.txt` and `decryption.txt` are the issue's first-pass files, unchanged.

## Project check (10 Nov 2026)

- Re-decoded the 1,360 signs of `transcription.txt` with the key as stated in the issue (own script, not committed): 1,300 of 1,360 tokens (95.6%) equal the contributor's `decryption.txt`; the 60 others are u/v spelling (18 = v written u), bare 15 = ra, the code word `amo` and a few nulls. So the decryption follows the stated key; it is not a model's free text. `VERIFICATION.md`.
- Measured on `decryption.txt`: 18 signs read `?`, 58 nulls, 33 code words with a context-only value.
- Measured on `reading.md` after the comment corrections: 531 words, 28 holes or bracketed guesses, read share 0.947.
- Not checked: the transcription against the images (the Estense IIIF host, archive.org and british-history.ac.uk were refused by the session's network); the Calendar of State Papers Spain IX extracts; the Gioffredo passages in Historiae Patriae Monumenta. These rest on the contributor.

## Prior work

The repo listed cc.131-132 as unread; the contributor found no printed text of this dispatch. The plot is known in outline from the Calendar extracts of Renard's letters of 14, 18 and 28 July 1549 (Vienna, F. 28), which have no entry for 12 July (contributor). Renard's original dispatch may survive in Vienna (HHStA, Frankreich) and Besançon holds Charles V's letter to Renard of 12/15 July 1549 with a decipherment (CCFr ark:/16871/004a80174782); neither was seen.

## Remaining gaps

- Code word amo (an office of the Duke and of Tende) and the signs Q/∝ elsewhere, X, F, I, T°, 3^1, e^3 - blocker: open-codes; each occurs once or twice and the context does not fix it
- Context-only values of code words (den, bas, ne, mi, oria/ocia/ning, rac, apud, allo, bit) - blocker: open-codes; not found in the c.40/41 alignment, no other text in this key in the file
- Five short holes in the reading and the plotters' names spelled letter by letter (Chaulve-F) - blocker: illegible; the contributor's crops leave them unread, and the project could not reach the images
- Transcription not compared with the images by the project; Renard's original in Vienna and the Besançon decipherment - blocker: needs-physical-access; Estense host refused by this session's network, the Vienna and Besançon papers are not online

## Escalation

- [x] siblings: c.40-42 (15 Jul 1549, same key, decipherment c.41) used for the key; the gonzaga1549 sign letters are another cipher
- [x] clear-pages: c.132 is blank or address only; c.41 is the decipherment of c.40, not of c.131
- [x] known-keys: Tomokiyo's 1548 syllabary, corrected against c.40/41; the gonzaga1542 key does not apply (catalogue entry, 9 Nov)
- [x] print: CSP Spain IX (extracts of 14, 18, 28 July, no 12 July entry) and Gioffredo in HPM Scriptores II searched by the contributor; web search in four languages found no text
- [x] key-rebuild: context values for the code words fitted by the contributor with a beam decoder and by reading
- [x] retry: the contributor's second pass re-read the holes and fixed de Navarra, navarro, Care, fin = pri

## Files

| File | Content |
|---|---|
| `transcription.txt` | c.131r-v sign by sign (contributor, first pass) |
| `decryption.txt` | line-by-line decryption with the key, no language model (contributor) |
| `reading.md` | Spanish reading, comment corrections applied |
| `translation.md` | English translation, comment corrections applied |
| `key.tsv` | the corrected 1548 syllabary as given in the issue |
| `VERIFICATION.md` | what the project re-checked |
| `profile.json` | the target profile |
