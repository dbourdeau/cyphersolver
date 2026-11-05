# Adrian of Utrecht (Cardinal of Tortosa) to Charles V, Valladolid, 9 September 1520: the cipher paragraph

Status: in progress (read in part, escalation not yet done: the Remaining gaps blockers and the Escalation checklist are still to be written; Brice Dudout; recounted 5 Nov 2026 under the strict 95% rule: 40 of 46 cipher words read = 87.0%, 28 certain + 12 probable; 4 restored from the sense no longer count as read, 95.7% with them; 2 unresolved; key K7 validated on a fresh held-out pair).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct - 2 Nov 2026. Write-up:
https://bdudout.github.io/europe-chiffree/en/documents.html#tortosa-1520
Not in the catalogue; found through the PARES sweep in research/pares_ags. Different letter and code from
`adrian1521/` (the joint letter of 30 Dec 1521, Estado 8,150): the Cardinal's own letters of 1520-21 use the
"dotted trigraph code" noted there (leb. sa. cab. sih. gig. vuh. ...), which this folder reads.

## Document

Archivo General de Simancas, Patronato Real, PTR,LEG,2,1,19, f. 1r (PARES 12987122); formerly “Comunidades de Castilla, leg. 2, fols. 157–158”. Letter printed without the cipher paragraph by A. Danvila, Historia crítica y documentada de las Comunidades de Castilla, in Memorial histórico español XXXVI (1897), pp. 17–19.
9 September 1520 (“En Valladolid a ix de Setiembre de mil quinientos y veynte”). Valladolid → Charles V, then in the Low Countries.
Sender: Adrian of Utrecht, Cardinal of Tortosa, governor of Castile (signed “Vre tres humble serviteur, Car.l dertusen.”). Recipient: Charles V, King of Castile and Emperor-elect.
PARES: https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/12987122 (images not reproduced: no open licence stated).

On 9 September 1520 Adrian of Utrecht – Cardinal of Tortosa, regent of Castile for Charles V, and sixteen months later Pope Adrian VI – wrote from Valladolid while the Junta of the Comunidades was settling at Ávila. In the middle of the letter are six lines in cipher. Danvila, who printed the letter in 1897, noted only: “Sigue un párrafo cifrado que no ha podido traducirse”. The cipher is the Cardinal’s dotted code; we rebuilt it from his other letters of 1520–1521 whose plain text is known, validated it on a letter held out, and applied it to this paragraph. It tells what the Junta meant to do to the grandees: take from them the alcabalas and the towns that had belonged to the Crown.

## System and key

the Cardinal’s “dotted trigraph” code: consonant-vowel-consonant groups followed by a dot for words and syllables (gig. que, leb. no, sa. de, nof. los, mud. -mente…), and a homophonic alphabet of signs (h, ð, M = e; cf, 4, g, B× = a; ⊥, φ = r; y̥, p = s; ε̥ = t…). The same code in the letters of 1520 and 1521 (PTR,LEG,2,1,23, 30, 32, 61, 68, 70, 71, 73, 85, 88, 99)

Key K7 (`key_K7.json`) is built from cipher/plain pairs of the Cardinal's other letters: PTR,LEG,2,1,23 and 32 (Bergenroth,
CSP Spain, Supplement 1868), 2,1,30, 61 and 88 (Danvila, MHE XXXVI-XXXVIII), 2,1,68, 70, 71, 73 and 85 (contemporary
transcriptions 2,1,69, 72, 83); code groups are kept only when attested twice ("1x:" otherwise). Sign shapes were
re-read blind by Brice Dudout on three plates (choose the shape seen; no value shown), which split confused homophones
(9 = a / ꞡ = r, φ = r / ꝗ = m, ...).
Validation (`validation.txt`): one measurement on a fresh pair named before download, PTR,LEG,2,1,99 (5 Dec 1521),
second cipher passage (10 lines, frozen) against Danvila's plain text (MHE XXXVIII): characters 0.882 (n = 170) against
at best 0.176 for 200 shuffled-key controls (median 0.041), rank 1/201; words 0.770 (controls max 0.119).
Earlier keys: K3 (0.851 characters but 0.541 words on 2,1,68; the first version of this folder, never pushed, rested on
it), K4 (0.783 on 2,1,85) and K6 (0.813 on 2,1,88) failed; those pairs then went into training.

## Reading

First published decipherment, to our knowledge. Rule applied: Daniel Bourdeau’s, 95% of words read for sense. Of 46 cipher words (the two plain words “quanto mas” excluded; “dels” counted as one word): 28 certain (60.9%), 12 probable {x} (26.1%), 4 restored from the sense [x] (8.7%), 2 unresolved ‹…› (4.3%); read: 44 / 46 = 95.7%. The reading therefore just meets the threshold; each probable, restored or unresolved word is justified below. Key K7, validated on 2 November 2026 on a held-out letter (see “Method”).
Files: `transcription.txt`, `decryption.txt` (mechanical, K7), `reading.md` (Spanish), `translation.md` (English, with the
justification of every probable, restored or unresolved word), `key_K7.json`, `validation.txt`.

## Notes

- The moment. In August–September 1520 the Junta of the Comunidades, meeting at Ávila, seized Tordesillas (29 August) and Queen Joanna; Adrian, at Valladolid, tried in vain to draw it to the town (the mission of the commander Hinestrosa, told in plain text in the letter). The cipher paragraph gives the rest of the Junta’s programme against the grandees.
- Alcabalas and Crown towns. Abolishing or reducing the alcabalas (the sales tax) and returning to the Crown the towns and places alienated to lords were among the Comuneros’ demands; the contemporary transcription of the Cardinal’s letters of 21 March 1521 still speaks of “cosas enajenadas de la corona”.
- “La cifra que va dentro desta”. The paragraph follows the plain sentence “el fin que sobresto tienen sabrá V. Al. por la cifra que va dentro desta”. An enclosed cipher sheet therefore existed; its contemporary decipherment survives separately (PTR,LEG,2,1,107: the Junta means to take the title of king from Charles during the Queen’s lifetime, according to the Marquis of Villena’s secretary). It is not the text of the paragraph read here.
- The Cardinal’s other letters. Almost all his cipher letters of 1520–1521 are printed deciphered by Danvila, from the contemporary transcriptions. Still without plain text: this paragraph and a struck-out cipher paragraph of 21 October 1520. The sheet wholly in cipher enclosed with the letter of 7 December 1521 (PTR,LEG,2,1,100, fol. 434), whose decipherment Danvila says “puede pertenecer á otra”, is in fact the cipher original of the paragraphs of the letter from Vitoria of 24 October 1521, which Danvila prints deciphered (MHE XXXVIII, p. 547) from the contemporary transcription (PTR,LEG,2,1,92): key K7 reads its first line “… apareiamos … exercito … mas muy …”. The joint letter of 30 December 1521 (Estado 8,150), in another code, was re-read by Daniel Bourdeau on Gredilla’s decipherment.

## Method and prior work

Method: (1) protocol written before any computation, with dated amendments; (2) key rebuilt from the Cardinal’s other cipher letters whose plain text is known: 8 October, 13 and 17 November 1520 (PTR,LEG,2,1,23, 30, 32 ↔ Bergenroth, CSP Spain, supplement of 1868, and Danvila), 23 February, 15 and 28 March, 8 and 30 August 1521 (2,1,61, 68, 70, 71, 73, 85, 88 ↔ Danvila or the contemporary transcriptions 2,1,69, 72, 83); code groups kept only when attested twice; (3) sign shapes re-read blind by Brice Dudout on three plates (pick the shape seen, no value shown), which separated confused homophones (9 / ꞡ, φ / ꝗ, ʒ / Ƶ…); (4) validation: a single measurement per fresh pair named before download, criterion fixed in advance (character agreement ≥ 0.85 and ≥ the best of 200 shuffled-key controls + 0.30; word agreement reported). A first version of this card (28 October, key K3: 0.851 of characters but 0.541 of words on 2,1,68) was withdrawn the same day; keys K4 (0.783 on 2,1,85) and K6 (0.813 on 2,1,88) failed, and those pairs then went into training. Key K7 is validated on the fresh pair 2,1,99 (letter from Vitoria, 5 December 1521, second cipher passage, ten lines transcribed and frozen before any reading of the plain text) against the plain text printed by Danvila (MHE XXXVIII, same letter): 0.882 of characters (n = 170) against at best 0.176 for 200 controls (median 0.041), rank 1/201; words 0.770 (controls ≤ 0.119). Thirteen tokens of 254 were left out of the score: abbreviations, and the plain-text words glimpsed while locating the letter (exclusion declared before transcription). (5) Reading of the 9 September paragraph with K7, on a sign transcription frozen before the measurement, and count under Daniel’s rule. All SHA-256 fingerprints are in the working folder.
Prior work checked on 28 Oct 2026: Danvila prints the letter without the paragraph ("no ha podido traducirse");
Bergenroth's Supplement (1868) does not include the letter; Höfler printed it in 1881 with a wrong date (per
Danvila, who still calls the paragraph untranslated); nothing in this repository nor on Cryptiana.
Re-checked on 2 Nov 2026: no modern edition of the decipherments; Höfler (1880) gives no Spanish plain text of the paragraph.

## Remaining gaps

- The first cipher word (six signs, p ‹?› u i c a; one uninventoried shape) and the group fud.
- Signs still outside the key: the first signs of [tales] and [juntar], the 2nd sign of [villas], ‹ro›, ‹qx›, ‹m.›.
- Still without plain text in the same code: a struck-out cipher paragraph of 21 Oct 1520 (not yet located on PARES).
- The cipher sheet enclosed with the letter of 7 Dec 1521 (PTR,LEG,2,1,100, fol. 434) is not an open problem: it is the cipher
  original of the paragraphs of 24 Oct 1521 printed by Danvila (MHE XXXVIII p. 547; contemporary transcription
  PTR,LEG,2,1,92, PARES 12987667). K7 decodes its first line as "... apareiamos ... exercito ... mas muy ...".
