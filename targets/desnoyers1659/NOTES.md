# Des Noyers 1659: Pierre Des Noyers to Ismaël Boulliau, note in cipher, [Danzig, December 1659] (BnF Français 13020 f. 297)

Status: read (existing contemporary decipherment: the interlinear gloss of the time, transcribed and checked; Brice Dudout, 29 Oct 2026, revised 4 Nov 2026; 12 of 12 words read in their sense: 6 certain, 2 probable, 4 restored from the contemporary gloss, 0 unresolved; Daniel Bourdeau's 95% rule). Not a solution: the note was deciphered at the time.

Contributed by Brice Dudout, 29 Oct 2026 (revised 4 Nov 2026).

**What this is, and what it is not.** The cipher of this note is already deciphered: a contemporary hand (probably Boulliau's) wrote the clear text above every group. The content is therefore *existing* (read at the time), not a new decipherment, and nothing here is claimed as a solution. What this target adds is (1) a transcription of the cipher and of its gloss, checked group by group, of a note that is not in the printed edition of the letters (Berlin, 1859), and (2) the key: the numerical nomenclator 00-99 with superscript marks used by Des Noyers and Boulliau in 1658-1659, rebuilt from the cipher / gloss pairs of the twelve glossed passages of the volume and given as a stand-alone key file (`key.tsv`). That table is not the 1656 sign key of f. 315.
Not in the catalogue. Found while looking for uses of the Des Noyers - Boulliau key of 1656 (BnF Fr. 13020 ff. 314-315).

## Document

Bibliothèque nationale de France, Français 13020 (letters from Des Noyers to Boulliau, 1657–1659), f. 297; Gallica, view 608.
undated; separate note bound among the letters of December 1659 (previous letter: Danzig, 20 December 1659). [Danzig] → Paris.
Sender: Pierre Des Noyers, secretary to Queen Louise-Marie of Poland. Recipient: Ismaël Boulliau (1605–1694), astronomer, in Paris.
Image: https://gallica.bnf.fr/ark:/12148/btv1b9061314b/f608.item (Source gallica.bnf.fr / BnF; not copied here).

Late 1659. The Peace of the Pyrenees (7 November) provides for the marriage of Louis XIV and the Infanta Maria Theresa; at the French court there is still talk of the king’s attachment to Marie Mancini, Mazarin’s niece. From Poland, Pierre Des Noyers, secretary to Queen Louise-Marie de Gonzague, answers a “little note” from his friend the astronomer Ismaël Boulliau in Paris. The key words are in cipher: without the Queen (Anne of Austria), no one would wait for the death of the Prince of Spain to break off the marriage, and la Mancini must be very bold.

## System and key

a numerical nomenclator of about a hundred two-digit groups (00–99): letters and syllables (29 la, 42 de, 46 s, 52 le, 69 n, 23 r…); a mark above the group (ring, circumflex, cross, bar, accent) turns it into a code word (30+ Reine, 29+ Roy, 86^ Prince, 45° Ambassadeur, 00¯ France, 50° Austria). It is not the sign key that Des Noyers had sent in 1656 (BnF Fr. 13020 f. 315)..

`key.tsv` = the table rebuilt from the cipher / gloss pairs of the twelve glossed passages of the volume (Sept 1658 - Dec 1659):
88 distinct groups; consistency group -> syllable 88.8% (450/507), code words 97.2% (105/108; 200 shuffled controls <= 34%).
The same table serves French (1658) and Italian (1659) plaintext. Compared with the 1656 key of f. 315 (sign alphabet + nomenclator
3-39): no sign of that alphabet, 0 agreements in 41 groups 3-39 (200 permuted controls: mean 0.001) -> a different table.

## Prior work

The eleven other glossed passages (views 187-188, 204-205, 362, 461, 469, 558, and 544 in part) are printed in clear in
"Lettres de Pierre Des Noyers" (Berlin, 1859; https://archive.org/details/lettresdepierre00noyegoog). This enclosed note
(f. 297) is not in that edition (search of the Internet Archive OCR text). A second unpublished note (f. 266, Italian,
"Principi di Toscana") reaches only 84% under the same rule and is not contributed.

## Reading

First edition of the note, to our knowledge: the note is not in the edition of the Lettres de Pierre Des Noyers (Berlin, 1859), which prints the other cipher passages of 1658–1659 in clear (search of the digitized text, Internet Archive OCR); web search negative. The reading is the contemporary interlinear gloss (probably by Boulliau), checked group by group against a table rebuilt from the eleven other glossed passages of the volume (Sept. 1658 – Dec. 1659), without this note. Rule applied: Daniel Bourdeau’s, 95% of the words read by sense. Cipher part: 12 words; certain 6, probable {x} 2, restored [x] 4, unresolved 0; read: 12/12 = 100% (certain + probable: 8/12). By groups: 24 groups, 18 certain, 2 probable, 4 restored.

Files: `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`, `key.tsv`.

## Notes

- Cipher and gloss. 24 groups: 29 30+ la Reine · 30^ 21° 86^ 42 46 02 40 54 mort du Prince despagne · 52 20^° le mariage · 29 41 69 57 77 la Mancini · 47 10° 69 33 23 65 10° bien ardie. Above each group, another hand wrote the word or syllable in clear.
- What is certain. The values 29 la, 30+ Reine, 86^ Prince, 42 de, 46 s, 02 pa, 54 ne, 52 le, 41 ma, 69 n, 57 ci, 33 a, 23 r, 65 di, 10° e/ie recur with the same value in the glossed passages of 1658–1659 (“la Reine” six times, “le Prince de Condé”, “injustice”, “chambre”, “congédié”…). 40 g (Longueville) and 77 ni (“ni de gain”) occur there only once: probable. 30^ mort, 21° du, 20^° mariage and 47 b occur nowhere else: their value comes from the gloss alone (restored).
- The Queen. In this cipher 30+ means “the Queen” without saying which: in 1658 the Queen of Poland; here, from the context (the Spanish marriage), Anne of Austria, mother of Louis XIV. “The Prince of Spain” is the Infante Philip Prosper (1657–1661), Philip IV’s only son: his death would have made the Infanta Maria Theresa heiress of Spain.
- What the note adds. Des Noyers answers news from Paris about Marie Mancini (“what you tell me of her”); he thinks that only the Queen Mother holds the Spanish marriage together. The 1859 edition prints the letters, but not this enclosed note.
