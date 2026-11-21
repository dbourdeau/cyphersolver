# acciaiuoli1513: Roberto Acciaiuoli's dispatch from Amiens, 23 October 1513 (catalogue 2351)

Status: **read in part.** Both faces of ASF Mediceo avanti il Principato LXXII, doc. 192 are transcribed (1,887 signs) and build a continuous Italian text. About 90% of the words (692 of about 770) are read from the signs with nothing supplied; 21 more carry a supplied letter, 30 are proposed words marked `[?word]`, 25 are unread and two are the unidentified number 15. That is under the 95% read bar. [Recto](https://archiviodistatofirenze.cultura.gov.it/map/riproduzione/?id=79574) · [Verso](https://archiviodistatofirenze.cultura.gov.it/map/riproduzione/?id=79575) · [Fuller edition, blind passes, calibration and review](https://github.com/aaymeloglu/unsolved-ciphers/tree/main/amiens-1513)

Contributed by Andrew Aymeloglu. The transcription, key table and reading were made by Claude (Anthropic) on 20 November 2026, after a first partial pass by OpenAI Codex that identified the system from Brice Dudout's pandolfini1514 key. Codex then reviewed Claude's reading against the images, and its confirmed findings are applied. No person has checked the reading against the manuscript. No ASF or DECODE image is included.

## What the letter says

Acciaiuoli writes to the Signoria. Louis XII has ordered Monsieur de Bourbon into Burgundy with 8 hundred lances and 10 thousand Landsknechte. A plan involving a passage of the mountains has been overturned by a copy of a Martelli letter, sent from Florence on the 11th, reporting the rout of the party written 15. In a long conversation the king is torn between fear of the Swiss and anger at people who excuse themselves by fear of the English army: he being their sovereign lord, they had no regard for putting his kingdom in danger. The English king has loaded his baggage and embarked at Calais, the crossing split in three parts. The French have 2,500 lances and 14,000 Landsknechte to meet a Swiss attack, to be placed in Champagne and Burgundy. The king tells Acciaiuoli to write that he is secure and will fight if the Swiss move. The prelates leave for Rome after All Saints, and the king is disposed to please the pope in everything. Texts: [Italian](reading-it.md) · [English](translation-en.md).

Historical context. Sanudo's *Diarii*, vol. XVII, cols. 321-324, has a separate report of Bourbon assigned to Burgundy with 900 men-at-arms and 10,000 infantry, and prints a Florentine letter of 28 August 1513 citing reports from "nostro Piero Martelli" at Vicenza, where the Venetians were routed on 7 October. That is the ground for taking 15 as the Venetians; it is a proposal, and 15 is printed as `[15]`. Desjardins and Canestrini, *Négociations*, vol. II, print Acciaiuoli's letter of 26 September 1513 and then one of 27 January 1514; this letter is not there.

## The system and the key

The cipher is the Florentine syllabary of pandolfini1514: a consonant sign with the vowel as a superscript figure (1-5 = u, o, i, e, a), bare vowel and consonant signs, doubled consonants, word signs, and numbers as code words. Three sources give the values, and `key.tsv` marks each row by source:

- **G120**: Pietro Domenico Gabbrielli's reconstruction of this cipher, no. 120 "Acciaioli (de) Roberto, 1512-13-14" in his nineteenth-century *Alfabeti ... del carteggio dei Dieci di Balìa*, vol. I (ASF; DECODE record R5807, catalogued one leaf off). Transcribed in `gabbrielli-120.md`. It gives the alphabet, the syllabary, the doubles, 35 word signs, the nulls and thirteen numbers (2 Papa, 4 Re di Francia, 5 Re di Spagna, 6 Inghilterra, 8 Re di Portogallo, 20 Svizzeri, 22 Lanzichinecchi, 34, 64, 65, 66, 68, 78). The letter of 23 October 1513 lies outside the filze Gabbrielli worked from, so the key is independent of it. It is an archivist's reconstruction from letters deciphered at the time, not a chancery key sheet.
- **v6**: Dudout's pandolfini1514 key, which first opened the letter. Almost all of its values used here are also in G120.
- **190/191**: docs. 190 and 191 of the same filza are Acciaiuoli's cipher letter of the same day to Giuliano de' Medici and its contemporary copy in clear. Aligned sign by sign, they fix the beta-like e, the closed-loop o, the pi-like p, the barred long s, the barred circle x and several word signs. On held-out signs whose clear word was read before decoding, the corrected key gives the clear's letters at 84% to 94% (93 signs). The alignment is in the linked edition.
- **192**: values that rest on sense within this letter: a plain cross for n, an E-like sign for e, and *ora* for a G with a raised tick (plain G is *ora* in G120).

Gabbrielli's two other keys for Acciaioli, no. 89 (1505-12) and no. 111 (1511-12), are different ciphers and give nothing for the open numbers.

`192-literal.txt` is the unedited output of the key on the transcription (`python3 decode.py --raw`). The reading departs from it at 23 declared places (`192-repairs.tsv`): the 2-like sign read b where the sense wants it (G120 has two different 2-like signs for b and c, which the transcription does not separate), figures read as numerals before *cento* and *mila*, and a few superscripts. `192-reading-rows.txt` gives the reading row by row against the manuscript lines, with every unread group shown sign by sign.

## How it was checked

- Two blind transcriptions of all 41 lines by fresh model instances given shape names and no key: decoded with the same key, their signs give the printed letters at 85% of the signs counted as read. A second pair re-read the thirteen hardest lines from tighter crops; where both agreed against the key-aware pass their sign was usually adopted, which opened V8-10.
- Internal recurrence: *distribuire le gvernigione* (R2) and *distribuito el passaggio* (V4); *gvernigione* again at R22; *passaggi-* with the double-g sign at R4 and V4.
- Codex's review against the manuscript and key images confirmed Bourbon and Burgundy, the troop figures, Martelli and the rout, the king's complaint, Calais and the three-part crossing, the core of the king's message, All Saints and the closing prayer, and corrected *nientedimeno* (R19), *perché* (R11), *facto* and *passaggio* (R4, V4).
- The first key-aware transcription was not hashed before decoding.

## Remaining gaps

- 25 unread words, the largest stretches at R5, V1, V5, V13 and V14-15 - blocker: illegible (superscript 1 against 5 cannot be told apart at 1272 px, the archive's maximum online)
- 30 proposed words marked `[?word]`, among them costà, successo, posta, sono, mesi, Signore - blocker: illegible (the signs as transcribed do not spell them, mostly one superscript or one similar shape off)
- number 15, twice (the party routed) - blocker: open-codes; not in G120; Venetians proposed from Sanudo; in doc. 190 a 15 stands where the clear has Rubertet
- numbers 26 and 47 at R12, the people the king is angry at - blocker: open-codes; not in G120
- word signs B with a raised 1 (V15, V16) and F with a mark above (R13, V5) - blocker: open-codes

## Escalation

- [x] siblings: docs. 190/191 of the same day aligned (cipher against contemporary clear); pandolfini1514 key applied
- [x] clear-pages: docs. 189-197 of the filza checked; no clear copy of 192
- [x] known-keys: Gabbrielli no. 120 found and transcribed (DECODE R5807); nos. 89 and 111 checked, different ciphers
- [x] print: Desjardins-Canestrini vol. II and Sanudo vol. XVII checked; letter not printed
- [x] key-rebuild: key table rebuilt from G120, v6 and the 190/191 pair, each value marked by source
- [x] retry: every unread group and doubtful reading was decoded again after key 120 was applied and again after the Codex review, and regraded; what is left waits for images above 1272 px from the Archivio di Stato di Firenze

## Transcription doubts

- superscript 5 against 1 throughout (e.g. R6 y^1 in forza, V14 7^1 in deliberati) - read: by the word; checked: image, decode, transcription (blind passes); the blind readers split on the same signs, so these stay repairs or `[?word]`
- 2-like sign, b against c (R2 Borgogna, Borbona; V3 imbarcato) - read: b by sense; checked: image, decode; G120 has two shapes, not separable here; listed in 192-repairs.tsv
- R12 signs 12-16 "2 6 F 4 7" - read: [?26] et [?47]; checked: image, decode (o-s-et-g-r as letters makes no word; two numbers joined by et fit de' quali), transcription (both second-round blind readers and Codex give the same five signs); meaning open
- R19 signs after M^n - read: struck through; checked: image (a diagonal stroke crosses both), decode (nientedimeno el respecto reads; di-ma after it does not), transcription (first blind pass offered a deletion)
- R4 and V4 double g in passaggio - read: g#; checked: image, decode (the same compound at both places)
- V3, V4, V6 slashed circle - read: t (altra, distribuito, riscontro); checked: image, decode, G120
- R11 uncrossed Q - read: perché; checked: image (against the crossed Q of V14), decode (perché da un canto), G120
- V1 last three signs "ne u po" - read: unread; checked: image, decode (no place name results); damaged edge
- V9 two signs after scrivete - read: unread; checked: image, decode (no word results); Codex suggests "a .2."
- V19 last sign after desidera - read: not a letter (end mark?); checked: image, decode (desidera is complete without it)

## Tools

Claude (Anthropic, Fable 5.2) for transcription, key table, reading and translation; five further Claude instances for the blind passes and the 190/191 alignment; OpenAI Codex for the first pass and the review; Python 3 (`decode.py`); Pillow for crops. Images: ASF's public viewer (ids 79570-79575) and DECODE records R5777, R5799, R5807 (accessed with the DECODE project's permission).
