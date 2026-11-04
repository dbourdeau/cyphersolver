# The Electors of Mainz and Cologne to Gottfried Huyn von Geleen, [Cologne] 22 October 1633 (BSB Clm 10406, no. 206)

Status: read in part (Brice Dudout, 4 Nov 2026; 221 cipher words: 151 certain, 35 probable, 8 restored, 27 unresolved; 84.2% read, below the 95% rule; 19 words lost in the binding cap it at 91.4%).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Lead no. 2183 found by WAINUT
(https://github.com/WAINUTAI), who spotted the document in the Camerariana volumes. To be published as an explained partial reading:
https://bdudout.github.io/europe-chiffree/en/documents.html#ligue-1633
Not in the catalogue; no DECODE record.

## Document

Munich, Bayerische Staatsbibliothek, Clm 10406, no. 206 (Collectio Camerariana 56), fols. 184r–185v; digitised microfilm, MDZ bsb00116454, views 653–656 (Public Domain Mark 1.0).
Date: [Cologne], 22 October 1633 (“Datum den 22. Octobris Anno 1633”); an answer to a letter of Geleen dated Rheinberg, the 11th of the same month.
Senders: Anselm Casimir, Archbishop-Elector of Mainz (“Anselmus Casimirus Archiep. Moguntinus”), and Ferdinand, Elector of Cologne, autograph signatures. Recipient: Gottfried Huyn von Geleen, “General Wachtmeister” of the League army (address on the back, with the seals).
Original letter, signed; German clear text with about 1,180 cipher numbers inserted; no contemporary decipherment on the
piece or in the neighbouring items (nos. 205-207). Images: MDZ (Bayerische Staatsbibliothek), Public Domain Mark 1.0.

In the autumn of 1633 the Catholic League had almost no army left in the north. Hildesheim was besieged by the troops of Brunswick-Lüneburg, allies of the Swedes; Kniphausen and Melander’s Hessians held the County of Mark. The Archbishop-Elector of Mainz, Anselm Casimir Wambolt von Umstadt, in exile at Cologne, and the Elector of Cologne, Ferdinand of Bavaria, answered Gottfried Huyn von Geleen, the League’s major-general (Generalwachtmeister), on 22 October. The letter, signed in their own hands, is in clear, but everything about troops, money and people is in cipher: about 1,180 two-digit numbers slipped into the sentences. There is no contemporary decipherment on the document. We publish the reading as far as we could take it, gaps included: 84.2% of the cipher words. Most of the rest is lost in the binding of the volume, invisible on the digitised microfilm.

## System and key

simple substitution: each letter is a two-digit number (12 to 36), written run together, without word division, in the middle of the clear text; 22 working values (e = 17, n = 31…), two rare numbers without a sure value (33, 38). Key reconstructed here (table below).
Three known keys of the period were tested by a frozen criterion and do not apply (Camerarius 1621: no letter table 12-36;
Rákóczi 1632 and Kurz 1638-39: below the controls). Key K (`key.tsv`) was built by simulated annealing on the letter minus
the held-out lines, then corrected from three clear contexts ("vom Feind" 34 = f, 23 = m; "Kniphausen" 14 = p; "Geltmittel" 28 = l),
then frozen. Validation (`validation.txt`): M5 0.656 against 200 shuffled-key controls max 0.113; M_lm -2.512 against
max -4.182. The held-out lines read: "zum besten nichts erwinden lassen und euch hingegen vor gewiss versichern, das solche
eure merita und getrewe dinsten von uns und den sambtlichen unirten catholischen bundsständen mit würcklichem Danck
remunerirt werden sollen".

## Reading

Partial reading, explained; unpublished to our knowledge (see Prior work: a doubt remains about a summary in the Munich edition of 1982). Rule applied: Daniel Bourdeau’s, 95% of words read for sense to publish a decipherment. Here, of the 221 cipher words: 151 certain (68.3%), 35 probable {x}, 8 restored [x], 27 unresolved ‹…›; words read (certain and probable): 186 / 221 = 84.2%; 87.8% with the restored ones. The threshold is not reached: this is not a complete decipherment. On this microfilm it cannot be: 19 words are cut off in the binding, which caps the reading at 91.4%.
Files: `transcription.txt`, `decryption.txt` (K, mechanical), `reading.md` (German, tagged, with the count),
`translation.md` (English summary), `key.tsv`, `validation.txt`.

## Unresolved words and limits

- The binding. The volume was microfilmed bound: on view 654 (fol. 184v) the ends of the cipher lines vanish into the gutter. 19 words are cut or lost; even read perfectly, the rest would give only 91.4%. Only the original (or a new photograph) could bring the reading to 95%.
- Reading of the numbers. A single reader, on the enlarged microfilm. 2, 3 and 5 are sometimes alike, as are 15 and 18, 23 and 31: such words are counted “probable”. A blind re-reading plate (20 questions on 14 words, rules filed and hashed in advance) was answered by Brice Dudout on 4 November 2026: 9 words were confirmed and are now certain; for 4 words (‹shah›, ‹w??›, ‹waahhmeisher›, ‹ricmten›, expected “Statt”, “Weg”, “Wachtmeister”, “richten”) the numbers are written as transcribed, so the correction is dropped and they become unresolved; one word stays probable.
- Unresolved words. 27 words: 19 lost in the binding, 4 whose written numbers contradict the expected word (see above), 2 word ends at the cut (‹le›, ‹non›) and 2 runs that the key gives without a recognisable word (‹derdselfemlh›, ‹anewerder›). Eight restorations from the sense, two of them where the key gives almost the word: [bem(el)ten] (“bemeldten”, aforesaid; the key gives “bemten”) and ein [u(n)gewisses] (the key gives “einugewisses”); letters in brackets are added. Unverified clue: the re-reading confirms 25 where the sense wants t (Statt, Wachtmeister) and 23 where it wants h (richten); 25 and 23 may have a second value, or these are the encipherer’s slips. The key is not changed.
- No contemporary clear. No deciphered copy is known: the key is validated on the letter itself (five held-out lines), not on an independent control text. The letter’s clear text is read approximately.
- Prior work. No folder or reading in Daniel Bourdeau’s repository or on DECODE; nothing from Tomokiyo. The Munich edition, Briefe und Akten zur Geschichte des Dreißigjährigen Krieges, Neue Folge II/8 (Kathrin Bierther, 1982, January 1633 – May 1634), covers the same episode from the Bavarian archives (relief of Hildesheim, horse for Geleen, the Bönninghausen–Geleen quarrel); it is not online, and a search of its digitised snippets does not find this letter (nor Menselius). A summary of the letter, from a clear copy, cannot be ruled out. The cipher and its reading are, to our knowledge, published nowhere.

## Method

Method: (1) protocol written and hashed (SHA-256) before transcription, with five lines of fol. 185r (186 cipher letters, up to the clear word “Bedanken”) held out; (2) numbers transcribed without any key value, then frozen; three known keys of the period (Camerarius 1621, Rákóczi 1632, Kurz 1639) tested by a frozen criterion: none applies; (3) key built on the rest of the letter (simulated annealing with a model of 17th-century German, then three corrections from the clear context: “vom Feind”, “Kniphausen”, “Geltmittel”), then frozen; (4) a single measurement on the held-out lines: 0.656 of the cipher letters covered by German words of five letters or more, against at best 0.113 for 200 shuffled keys (threshold fixed in advance: 0.60), and a language-model score clearly above all controls (−2.51 against −4.18): key validated; (5) reading of the whole letter by Daniel’s rule. The held-out passage reads: “zum besten nichts erwinden lassen und euch hingegen vor gewiss versichern…”.
