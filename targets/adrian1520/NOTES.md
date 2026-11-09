# Adrian of Utrecht (Cardinal of Tortosa) to Charles V, Valladolid, 9 September 1520: the cipher paragraph

Status: read in part (Brice Dudout; recounted 9 Nov 2026 under the strict 95% rule after fol. 434: 43 of 46 cipher words read = 93.5%, 28 certain + 15 probable; 2 restored from the sense not counted as read, 97.8% with them; 1 unresolved; key K7 validated on a fresh held-out pair; three words read with the derived key K7b, declared and not re-validated; was 40 of 46 = 87.0% on 5 Nov).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct - 2 Nov 2026; fol. 434 and key K7b 9 Nov 2026, on Daniel Bourdeau's lead of 7 Nov. Write-up:
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

Derived key K7b (`key_K7b.json`, 9 Nov 2026; declared, NOT re-validated; K7 stays the validated key). Following Daniel
Bourdeau's lead of 7 Nov, the cipher sheet PTR,LEG,2,1,100 fol. 434 (three pages, 98 lines) was transcribed by shape
and frozen, then decoded mechanically with K7 frozen, and only then compared with Danvila's printed decipherment of
the paragraphs of the letter from Vitoria of 24 Oct 1521 (MHE XXXVIII pp. 547-549). K7 reads the sheet almost word
for word ("Acá aparejamos otra vez exercito mas muy a passo para que de muchos se diga publicamente ..."); the
differences are signs and groups not in K7. The pair is an existing decipherment, and part of it (a few lines of Danvila's
text had been seen in an earlier step) was known, so it is training, not a new validation, and no score is given. K7b =
K7 + 18 entries from fol. 434 (17 new labels, and K7's b = z split into b = ll and ƀ = z); nothing else is removed. Entries and their
attestations in fol. 434 (page, line, word of Danvila):

| label | value | attestations in fol. 434 |
|---|---|---|
| ttFx (tt + looped long s with small o) | q | quitome p1 l21; quise p2 l17; quitaria p2 l36; quiero p2 l38; quatro p3 l4; aqui p3 l20 (shape checked on the image for quatro and quitome) |
| Qx (barred q with S-shaped tail) | 1x: q | quitaciones p1 l26 |
| b (plain b) | 1x: ll | allego p1 l16 |
| ƀ (barred b) | z | haziendas p2 l27, l31, l35; hazienda p3 l6 |
| u. | en | more than 50 (en Castilla p1 l4, en ella p1 l14, vendan p2 l28 ...) |
| Z4 | n | crimen p2 l8/l19/l27; gouernar p1 l13; mande p2 l25; murmuran p1 l19; pongan p1 l5 |
| Zb | 1x: e | exercito p1 l1 |
| oq | x | exercito p1 l1; eximiendo p1 l28; dixe p3 l8 |
| T | g | pongan p1 l5; gouernacion p1 l24 |
| ful. | secreta | secretamente p1 l5, p2 l22 |
| zub. | entre | entre estos p1 l18; entre los p1 l26; entervino p1 l35 |
| zie. | algun | algunos p1 l18; algunas p1 l10, p2 l38; algunos p2 l17 |
| ceg. | vez | otra vez p1 l1; vezes p1 l10 (twice); p2 l38 |
| luh. | otra | p1 l1, p1 l10, p2 l6 |
| te. | consejo | p1 l15, p2 l6, p2 l17, p2 l25, p3 l19 |
| hal. | procura | procuradores p2 l13, l26; procurarlo p2 l13; procurador p2 l15 |
| sie. | 1x: don | rey don Juan p2 l30 |
| toe. | das | haziendas p2 l27, l31 |

Remarks: Z is also attested as i (diga p1 l2); the label Zp covers at least two shapes (e six times, m twice), and 6 is
both g (plega) and m (acostumbrado): to be split. The transcription and decoding of fol. 434 are in the working folder
(SHA-256 050551b6... and 647456d0...; K7b 1db608b4...); the PARES images are not reproduced.

## Reading

First published decipherment, to our knowledge. Rule applied: Daniel Bourdeau’s, 95% of words read for sense. Of 46 cipher words (the two plain words “quanto mas” excluded; “dels” counted as one word): 28 certain (60.9%), 12 probable {x} (26.1%), 4 restored from the sense [x] (8.7%), 2 unresolved ‹…› (4.3%); read: 44 / 46 = 95.7% (first count, 2 Nov 2026, when restored words were still counted as read; 40 / 46 = 87.0% under the strict rule of 5 Nov). Each probable, restored or unresolved word is justified below. Key K7, validated on 2 November 2026 on a held-out letter (see “Method”).
Recount of 9 Nov 2026 with the derived key K7b (strict rule: restored words are not read): 28 certain, 15 probable, 2 restored ([tales], [vuestra]), 1 unresolved (fud.); read: 43 / 46 = 93.5%, below the 95% threshold (44 / 46 needed), hence "read in part". Gained: the first word {quiça}, {villas}, and {quitar}, which replaces the restoration [juntar] (see `translation.md`).
Files: `transcription.txt`, `decryption.txt` (mechanical, K7), `reading.md` (Spanish), `translation.md` (English, with the
justification of every probable, restored or unresolved word), `key_K7.json`, `key_K7b.json` (derived, not re-validated), `validation.txt`.

## Notes

- The moment. In August–September 1520 the Junta of the Comunidades, meeting at Ávila, seized Tordesillas (29 August) and Queen Joanna; Adrian, at Valladolid, tried in vain to draw it to the town (the mission of the commander Hinestrosa, told in plain text in the letter). The cipher paragraph gives the rest of the Junta’s programme against the grandees.
- Alcabalas and Crown towns. Abolishing or reducing the alcabalas (the sales tax) and returning to the Crown the towns and places alienated to lords were among the Comuneros’ demands; the contemporary transcription of the Cardinal’s letters of 21 March 1521 still speaks of “cosas enajenadas de la corona”.
- “La cifra que va dentro desta”. The paragraph follows the plain sentence “el fin que sobresto tienen sabrá V. Al. por la cifra que va dentro desta”. An enclosed cipher sheet therefore existed; its contemporary decipherment survives separately (PTR,LEG,2,1,107: the Junta means to take the title of king from Charles during the Queen’s lifetime, according to the Marquis of Villena’s secretary). It is not the text of the paragraph read here.
- The Cardinal’s other letters. Almost all his cipher letters of 1520–1521 are printed deciphered by Danvila, from the contemporary transcriptions. Still without plain text: this paragraph and a struck-out cipher paragraph of 21 October 1520. The sheet wholly in cipher enclosed with the letter of 7 December 1521 (PTR,LEG,2,1,100, fol. 434), whose decipherment Danvila says “puede pertenecer á otra”, is in fact the cipher original of the paragraphs of the letter from Vitoria of 24 October 1521, which Danvila prints deciphered (MHE XXXVIII, p. 547) from the contemporary transcription (PTR,LEG,2,1,92): key K7 reads its first line “… apareiamos … exercito … mas muy …”, and on 9 Nov 2026 the whole sheet almost word for word (see “System and key”, key K7b). The joint letter of 30 December 1521 (Estado 8,150), in another code, was re-read by Daniel Bourdeau on Gredilla’s decipherment.

## Method and prior work

Method: (1) protocol written before any computation, with dated amendments; (2) key rebuilt from the Cardinal’s other cipher letters whose plain text is known: 8 October, 13 and 17 November 1520 (PTR,LEG,2,1,23, 30, 32 ↔ Bergenroth, CSP Spain, supplement of 1868, and Danvila), 23 February, 15 and 28 March, 8 and 30 August 1521 (2,1,61, 68, 70, 71, 73, 85, 88 ↔ Danvila or the contemporary transcriptions 2,1,69, 72, 83); code groups kept only when attested twice; (3) sign shapes re-read blind by Brice Dudout on three plates (pick the shape seen, no value shown), which separated confused homophones (9 / ꞡ, φ / ꝗ, ʒ / Ƶ…); (4) validation: a single measurement per fresh pair named before download, criterion fixed in advance (character agreement ≥ 0.85 and ≥ the best of 200 shuffled-key controls + 0.30; word agreement reported). A first version of this card (28 October, key K3: 0.851 of characters but 0.541 of words on 2,1,68) was withdrawn the same day; keys K4 (0.783 on 2,1,85) and K6 (0.813 on 2,1,88) failed, and those pairs then went into training. Key K7 is validated on the fresh pair 2,1,99 (letter from Vitoria, 5 December 1521, second cipher passage, ten lines transcribed and frozen before any reading of the plain text) against the plain text printed by Danvila (MHE XXXVIII, same letter): 0.882 of characters (n = 170) against at best 0.176 for 200 controls (median 0.041), rank 1/201; words 0.770 (controls ≤ 0.119). Thirteen tokens of 254 were left out of the score: abbreviations, and the plain-text words glimpsed while locating the letter (exclusion declared before transcription). (5) Reading of the 9 September paragraph with K7, on a sign transcription frozen before the measurement, and count under Daniel’s rule. All SHA-256 fingerprints are in the working folder.
Prior work checked on 28 Oct 2026: Danvila prints the letter without the paragraph ("no ha podido traducirse");
Bergenroth's Supplement (1868) does not include the letter; Höfler printed it in 1881 with a wrong date (per
Danvila, who still calls the paragraph untranslated); nothing in this repository nor on Cryptiana.
Re-checked on 2 Nov 2026: no modern edition of the decipherments; Höfler (1880) gives no Spanish plain text of the paragraph.

## Remaining gaps

- The group fud. - blocker: open-codes; no value in K7 or K7b, and absent from fol. 434 (ful. = secreta is attested there; fud. is not). The lead of 7 Nov 2026 (fol. 434) was followed on 9 Nov: it gave the first word {quiça}, {quitar} and {villas} (key K7b)
- Signs still outside the key: the first sign of [tales] (Zx), ‹ro›, and the two signs before mu. in [vuestra] (‹qx› ‹m.›) - blocker: open-codes; no value in K7 or K7b; fol. 434 has no identical shape and always writes cim. mu.

Not gaps of this reading: the struck-out cipher paragraph of 21 October 1520 (a different piece in the same code, not yet located on PARES), and the cipher sheet enclosed with the letter of 7 December 1521 (PTR,LEG,2,1,100, fol. 434), which is the cipher original of paragraphs Danvila prints deciphered (see Notes).

## Escalation

- [x] siblings: the Cardinal's other letters of 1520-21 in PTR,LEG,2,1 (23, 30, 32, 61, 68, 70, 71, 73, 85, 88, 92, 99, 100, 107) were opened as training and validation; the contemporary decipherment PTR,LEG,2,1,107 is not the text of this paragraph
- [x] clear-pages: the sentence "por la cifra que va dentro desta" points to an enclosed sheet; 2,1,107 was checked and is not it
- [x] known-keys: K3, K4 and K6 tried and failed (0.851/0.541 words, 0.783, 0.813); K7 validated on 2,1,99 (0.882 of characters); the code of adrian1521 (Estado 8,150) is a different one
- [x] print: Danvila 1897 (the paragraph "no ha podido traducirse"), Bergenroth's Supplement 1868 (does not include the letter), Höfler 1880-81 (wrong date, no Spanish plain text); nothing on Cryptiana; re-checked 2 Nov 2026
- [x] key-rebuild: K7 rebuilt from cipher/plain pairs of the Cardinal's other letters, with sign shapes re-read blind
- [x] retry: 9 Nov 2026, the unread words retried with the derived key K7b (K7 + fol. 434 against Danvila MHE XXXVIII pp. 547-549, Daniel Bourdeau's lead of 7 Nov); three words gained, three left (fud., [tales], [vuestra])

