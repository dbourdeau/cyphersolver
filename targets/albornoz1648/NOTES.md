# Philip IV to Cardinal Albornoz, Madrid, 24 July 1648 (catalogue 747)

Status: read (Brice Dudout, 28 Oct 2026; 353 of 359 cipher groups read, about 97% certain, about 1% probable, 6 unresolved (4 of them code signs); restored groups not counted separately; counted in groups, not words; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct 2026. Published write-up:
https://bdudout.github.io/europe-chiffree/en/documents.html#albornoz-1648

## Document

Archivo Histórico de la Nobleza (Toledo), OSUNA,CT.2,D.32(1-2) (PARES 3939398): copy A ff. 1r–2r (images 2–3), copy B (image 5). Key: OSUNA,CT.11,D.1(1-6) (PARES 3939336), images 1 and 3.
24 July 1648; two copies (original and duplicate) in the same chancery hand. Madrid → Rome.
Sender: Philip IV (“Yo el Rey”), countersigned by Pedro Coloma, secretary. Recipient: Gil de Albornoz (1581–1649), cardinal, Councillor of State, Spanish ambassador to the Pope.
PARES record and images: https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3939398 (key document: https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3939336). Images are not reproduced here.

In 1648 Innocent X was renewing his nuncios. Philip IV wanted to keep his own: Giulio Rospigliosi, Archbishop of Tarsus, nuncio at Madrid since 1644 – the future Pope Clement IX. He wrote so to his ambassador to the Pope, Cardinal Gil de Albornoz, in a cipher nobody had read: “there can be no instrument more suitable” for the service of both courts, so the ambassador must not desist “in any case”. The letter survives in two ciphered copies with no decipherment; the key came from another paper in the same family archive, a chapter of a letter by Luis de Haro enciphered for Albornoz in 1649, whose plain-text copy was kept.

## Historical summary

In 1648 Innocent X was renewing his nuncios. Philip IV asked his ambassador in Rome,
Cardinal Gil de Albornoz, to obtain that Giulio Rospigliosi (1600-1669), titular Archbishop of Tarsus and nuncio at
Madrid since 1644, stay at his post. A first letter of 10 January 1648 (OSUNA,C.1983,D.7, not digitised) had made the
request; Albornoz reported on 24 March what the Pope had answered. In this reply the King insists: Rospigliosi is
"muy digno de favor", no one could serve better the interests of both courts, and the ambassador must press "por
ningún caso" without giving up. Rospigliosi did stay in Madrid until 1653; he later became Cardinal Secretary of State
and, in 1667, Pope Clement IX. Albornoz left Rome in 1649 and died in December of that year; the embassy papers
passed to the Dukes of the Infantado and then to the Osuna archive, now in the Archivo Histórico de la Nobleza.

## System

syllabic cipher: syllables “disguised” as other syllables (consonant changed, vowel kept: mo = co, ne = de, ra = sa, la = pa, ti = mi), numbers in series of five (35–39 = la le li lo lu; 45–49 = ra…ru; 50–54 = ta…tu), single letters (2 = n, n = s, m = r, g = y/p) and a few code signs (✗ = que, sal = Su Santidad).

## Keys and how they were obtained

Two ciphers occur in the digitised pieces of no. 747 (only four of its 69 shelfmarks have images).

- **K1** (`key_K1.tsv`), the royal cipher of 1644-1645: rebuilt from OSUNA,CT.2,D.16 (12 Dec 1644), whose cipher
  original (images 2-4) was aligned on the contemporary plain copy in the same file (images 6-8;
  `keydocs/D16_alignment.txt`). Frozen (SHA-256 08fd8533...) and validated on OSUNA,CT.2,D.20 (26 Jan 1645), whose
  cipher (`keydocs/D20_cipher.txt`) was transcribed before its plain copy (`keydocs/D20_plain.txt`) was opened:
  0.638 of characters recovered, against a median of 0.467 and a 99th percentile of 0.550 for 200 control keys with
  permuted values. D.20 shifts the number series, so K1 is a family key. **K1 does not read the 1648 letter**, which
  is in another cipher.
- **K2** (`key_K2.tsv`), the cipher of the Albornoz embassy, 1648-1649: rebuilt from OSUNA,CT.11,D.1 image 3, a chapter
  of a letter of Luis de Haro to the Count of Peñaranda (Madrid, 25 Sept 1649) enciphered "to send to Cardinal
  Albornoz", whose plain copy is image 1. The phrase "dentro de Cataluña y", enciphered twice the same way
  (`2 ℓ48 ne ma so 39 40 g`), opened the alignment. Learnt on lines 1-12 only (`keydocs/CT11_cipher.txt`), frozen
  (SHA-256 f4a84e1c...), then validated on held-out lines 13-23 against the period plain text
  (`keydocs/CT11_plain_13-23.txt`): 0.859 of characters recovered, against a median of 0.419 and a 99th percentile
  of 0.476 for 200 permuted-value control keys.
- **K2b** (`key_K2b_additions.tsv`): the values added on the 1648 letter after the freeze, each with its evidence.

Departure from the protocol written before computing: it specified a word-level score; the validation used a
character-level score (longest common subsequence over normalised letters), because the word division of a
mechanical syllabic decoding is not reliable. Both validations clear the 99th percentile of the controls by a wide margin.

**Existing decipherments.** CT.2,D.16 and CT.2,D.20 each have a contemporary decipherment (plain copy in the same
file), so they are not new readings; they were used only to rebuild and test K1. CT.11,D.1 likewise has its
plain copy. The 1648 letter, CT.2,D.32, has none: two cipher copies and no decipherment.

## Reading

First published decipherment, to our knowledge. 359 cipher groups (copy B, checked group by group against A). Read: ≈ 98% of the groups (≈ 97% certain, ≈ 1% probable {x}); six groups remain unresolved ‹…›, four of them code signs (‹74›, ‹A›, ‹124› twice, ‹✗11›). The two copies agree, apart from copying variants (notes).

Files: `transcription.txt` (copies B and A), `decryption.txt` (each line, its token values and, for B, the
established text of the line), `reading.md` (Spanish), `translation.md` (English).

## Notes

- The Archbishop of Tarsus. Giulio Rospigliosi (1600–1669), titular Archbishop of Tarsus, apostolic nuncio in Spain from 1644 to 1653, later Cardinal Secretary of State and Pope Clement IX (1667). The letter of 10 January 1648 to which this one follows up is catalogued in the same fonds: Philip IV already asked Albornoz to obtain from Innocent X that “the Archbishop of Tarsus, nuncio of Spain, continue his residence” (OSUNA,C.1983,D.7, not digitised).
- “His prince and mine”. The nuncio serves two masters: the Pope, whom he represents, and the King at whose court he resides. The King argues that keeping Rospigliosi serves the “interests of the service” of both courts. Rospigliosi did in fact remain at Madrid until 1653.
- The recipient. Cardinal Gil de Albornoz, former governor of Milan, ambassador in Rome and Councillor of State, left Rome soon afterwards (licence to return to Spain, 1649) and died in December 1649. The embassy papers passed into the archives of the Dukes of the Infantado – the seventh Duke succeeded him in Rome in 1649 – and then of Osuna.
- The key. The same fonds keeps (OSUNA,CT.11,D.1) a chapter of a letter from Luis Méndez de Haro to the Count of Peñaranda (Madrid, 25 September 1649) on the army of Catalonia, “to send to Cardinal Albornoz”, in plain text (image 1) and in cipher (image 3): it is the cipher of this letter. The phrase “dentro de Cataluña y”, enciphered twice in the same way (2 ℓ48 ne ma so 39 40 g), opened the alignment.
- The two copies. Copy A (images 2–3) repeats half a line, cancelled by “4”s written above it; B likewise cancels one group in “sujeto”. Copying variants: “el respondió” (A ni = di; B mi), “Su Santidad” (A ra = sa; B ne), a g (y) doubled at a line break in both. We follow A where B departs from the key.
- Still unresolved. Four code signs occur only here: ‹74› (“Veo ‹74› pasastis”, probably “que”), underlined ‹A› (“mostrando los ‹A›s”, perhaps “inconvenientes”), ‹124› (twice: “que en ‹124› considera”, “se fuere ofreciendo en ‹124›”) and ‹✗11› (“su detención ‹✗11› en conformidad”); and the word ‹el› before “respondió”. The b of “sobre” is written with the sign for a; the “Be” of “Beatitud” with the syllable bo/vo.

## Method and prior work

Method (protocol written before computing): (1) inventory of the 69 shelfmarks of no. 747: only four are digitised; two letters of 1644–1645 (CT.2,D.16 and D.20) have their plain-text copies and served to rebuild the royal cipher of those years (key K1, validated on D.20), but the 1648 letter is in a different cipher; (2) that second cipher is the one of CT.11,D.1 (1649), whose plain-text copy survives: key K2 built on lines 1–12 of that piece only, frozen (SHA-256); (3) held-out validation: lines 13–23, decoded mechanically with the frozen K2, recover 0.859 of the letters of the period plain text, against 0.476 at the 99th percentile of 200 control keys with permuted values; (4) transcription of both copies of the 1648 letter, reading with K2, additions (single letters, series numbers) each established on several occurrences and listed separately. Rate: see Reading above.

Prior work, checked on 28 October 2026. Daniel Bourdeau’s catalogue lists these letters as unsolved; his repository holds nothing on this fonds. The PARES record gives only the subject (“para que continúe en sus funciones el Nuncio”). X. Arriazu García’s thesis on Albornoz’s mission (Barcelona, 2024) cites other cipher letters from the Osuna fonds, not this one. Web searches: nothing. To our knowledge this is the first published reading.

## Remaining gaps

- Four code signs found only here: 74 (probably "que"), underlined A ("los [A]s", perhaps "inconvenientes"),
  124 (twice) and ✗11; and the group read "el" before "respondió". Another letter in the same cipher would settle them.
