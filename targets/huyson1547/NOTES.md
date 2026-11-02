# Henry II to Suleiman the Magnificent, 1547: Malvezzi's enciphered Latin copy (catalogue 500, HHStA Türkei I 7-2-18)

Status: read (Brice Dudout, 27 Oct 2026; about 97.5% of about 1,550 cipher groups read (counted group by group in part, estimated line by line elsewhere), 18 unresolved; certain, probable and restored groups not counted separately for the whole item; words not counted; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 27 Oct 2026. Write-up:
https://bdudout.github.io/europe-chiffree/en/documents.html#huyson-1547

## Document

Österreichisches Staatsarchiv, Haus-, Hof- und Staatsarchiv (Vienna), Staatenabteilungen, Türkei I, box 7, file 2, fols. 143r–146r (“7-2-18”); 207 ciphered lines. Henry II’s letters: summer–autumn 1547 (undated: Malvezzi notes that the French hand in their letters without a date); ciphered copy: enclosure “A” of Malvezzi’s dispatch of 8 March 1548 (the AIS inventory dates it September 1547). Henry II, King of France (letters); Giovanni Maria Malvezzi, Ferdinand I’s resident at the Porte (copy, notes and cipher) to Suleiman the Magnificent (letters); Ferdinand I, King of the Romans (copy).
AIS: https://www.archivinformationssystem.at/detail.aspx?ID=6567149 (marked "Inhalt nicht dechiffriert"; images not reproduced).

In the autumn of 1547 Henry II, king for six months, sent his pantler, the sieur d’Huyson, to Constantinople with a letter of credence for Suleiman and instructions: join the truce that Charles V and Ferdinand had just made with the Porte, but have the king’s allies — the Swiss first — included in it, and expose imperial bad faith. Ferdinand’s resident in Constantinople, Giovanni Maria Malvezzi, got hold of the text, translated it back “from Turkish into Latin, word for word” and sent it to Vienna in cipher, together with a second, longer letter and a third, carried by a captain, about the Diet of Augsburg and asking for the Ottoman fleet. These four ciphered pages had never been read.

## System and key

Malvezzi’s cipher alphabet: homophonic graphic signs (two to four per letter, numbers for double letters), nulls (syllables Dac, Der, Dam… and whole Latin words cum, etiam, porro), a few code words (Bi = King of France, Ras = the Sultan, Ab = the French)

The key is Malvezzi's alphabet (DECODE R367/R386, as in this repository's `malvezzi1548`), calibrated on 7-3-20
f. 44 against its contemporary decipherment (f. 45) and frozen as K-C01 (`key_KC01.json`, French labels; SHA-256 in
`key_KC01.json.sha256`). Values added later are justified in the reading notes; K-C01 itself was not changed.

## Reading

First published decipherment of this item, as far as we know. All 207 lines are read; about 97.5% of the groups (≈ 1,550). By section: 143r ll. 1–17, 94%; 143r l. 18 – 143v l. 16, ≈ 94%; 143v ll. 17–32, 97.5%; 144r, 98.8%; 144v, 98.6%; 145r, 99.6%; 145v ll. 1–27, 97.4%; 145v ll. 28–30 and 146r, ≈ 95–97% (the last four figures estimated line by line, the others counted group by group). Eighteen groups remain unresolved and are marked ‹…›; probable readings are in braces. The content of the letter of credence and of d’Huyson’s instructions has been known in French since 1666 (Ribier); the Latin text actually delivered to the Porte, Malvezzi’s notes and the third letter were not.

Files: `transcription.txt` (last sign-by-sign reading of every line), `decryption.txt` (mechanical, word by word),
`reading.md` (established Latin/Italian text), `translation.md` (English).

## Prior work

Ribier (1666) prints d'Huyson's credence and instruction in French, not this Latin text sent to the Porte;
Charrière II gives summaries. Austro-Turcica 1995 not consulted.

## Notes

- The bearer. “Duson”, “Dusson”, “Dussun” is the sieur d’Huyson, Henry II’s ordinary pantler. According to the letters printed by Charrière he passed through Venice in September 1547, sailed in October, fell gravely ill in Constantinople and left again at the end of January 1548; the ambassador at Venice, Morvilliers, reported his arrival in March 1548 “with Captain Bartholomeo, who is going ahead to bring you M. d’Aramon’s dispatch”. Ribier prints the letter of credence in French, naming “our beloved and loyal ordinary Pantler the Sieur d’Huyson, bearer of this”.
- The Latin is a back-translation. Malvezzi says so himself: the French have the king’s letters translated into Turkish, undated, “per posser negare”, and he renders them “dal turchesche in latino de uerbo ad uerbum”. Hence the wavering syntax (from “we” to “I”, from “Your Majesty” to the third person) and the formula “et {loco suo}”, read twice before the subscription “Francie rex Enricus”: probably the place of the seal or monogram in the Turkish version, rendered literally. Comparing Ribier’s French (“Très-Haut, Très-Excellent… Soltan Soliman Sach”) with the ciphered Latin (“Serenissime Ottomanorum Imperator… mi frater carissime”) shows that this is not a translation of the French text.
- The truce. The second letter recalls the one-year truce obtained through Francis I, then the five-year truce signed at Adrianople in June 1547 by the envoys of Charles V and Ferdinand (Gerard Veltwyck), “without the knowledge” of the late king, and its imperial ratification, of which the king says he obtained a copy “from the very chanceries of the King of Spain”. Charles V’s Latin letter to the Sultan “de confirmatione induciarum” (Augsburg, 4 February 1548) is also printed by Ribier. The arguments peculiar to the Latin — no imperial oath “as is the custom of emperors and kings”, the Crépy articles slipped in “at the end” of the ratification for want of interpreters, the comparison with the English peace, thirty thousand florins for places in Hungary — are not in the printed French instructions.
- The promises of Crépy (1544). The marriage of Charles of Orléans, Henry II’s brother, to a daughter or niece of the Emperor with Milan as dowry, and the restitution of places by France, lapsed with the death of Charles of Orléans (September 1545) and then of Francis I (31 March 1547). The king asks the Sultan not to allow these articles into the ratification.
- The allies. The French instructions printed by Ribier ask that “the thirteen cantons of the Swiss leagues and the two of the Grey League” be included in the peace. The Latin develops the Swiss argument (“michi iam multis annis confederati”); the Grey League is not named. The group ‹…› between “populi” and “Suiceri” is unresolved.
- The third letter is not in Ribier as a letter to the Sultan: the Diet of Augsburg (“in ciuitate Augusta”, September 1547 – June 1548), a request to keep the Ottoman fleet ready, a promise to send the French fleet if the Spaniards raid Barbary, and the confirmation of Gabriel d’Aramon, “dominus de Ramon”, as ambassador. Captain {Bartolomeo}: the signs of the name read b‑a‑r‑e‑o l‑a‑m‑i‑o; reading the fourth sign, of very similar shape, as t (its value elsewhere on the same page) gives “Bartolamio”, a Venetian form of Bartolomeo — the Captain Bartholomeo who reached Venice with d’Huyson in March 1548 according to Morvilliers, and the “capitaine Barthélemy” whom d’Aramon was expecting at the Sultan’s camp.
- Code words. Bi (King of France), Ras (the Sultan), Ab (the French) and Mes ({His Majesty}, Malvezzi’s addressee) belong to Malvezzi’s small repertory; the nulls are syllables (Dac, Dar, Der, Dam, Dem, Dim, Dom, Dum; Dem added on review, 27 Oct 2026: 7 times in the transcription), single letters (b, d, n, z) and whole Latin words (cum, etiam, idcirco, atque, porro), which makes reading treacherous: cum and etiam are sometimes null, sometimes meaningful. “Itcirco” (146r) opens a sentence and has been kept.
- Unresolved groups (18). Italian heading, 143r l. 2 (two and a half groups: “portata per ‹d s› ‹…› de la ‹…› Ras”); 143r ll. 10 and 12 (one each); 143v l. 30 (three groups after “ne deceptione”); 144r ll. 4 and 6 (three); 144v l. 1 (two) and ll. 25–26 (one); 145r l. 4 (one); 145v l. 3 (two), l. 15 (a final abbreviation) and l. 17 (one). No value was added to the key to force them.

## Method

Method: (1) starting key = Malvezzi’s alphabet preserved with Ferdinand I’s letter to Malvezzi of 23 January 1548 (DECODE R367, read by Daniel Bourdeau), calibrated on another ciphered copy in the same series whose contemporary decipherment survives (7-3-20), then frozen (SHA-256 fingerprint) before any reading of 7-2-18; (2) held-out validation: on an unglossed copy of a ciphered letter of 1550 (8-3-8), decoding frozen before its contemporary decipherment was opened: 92.5% of letters agree with the gloss (84.3% mechanically from the key alone), against 20% on average and 31% at most for permuted keys; (3) atlas of the copyist’s letter forms (the “8” family is told apart by its foot); (4) line-by-line reading of 7-2-18 on the native AIS images, with no known text, counting sure, probable and unresolved groups; the show-through on 145v was digitally subtracted for reading; (5) blind visual review by Brice Dudout of 20 doubtful signs presented as shapes (two sheets, 19 confirmed, one re-examined); (6) Ribier and Charrière were used to identify people and check the sense, never to fix a value.

## Remaining gaps

- 18 groups left unresolved (4 in Malvezzi's Italian heading, 143r l. 2); {Bareo} and one group in 145v l. 17 not identified.
