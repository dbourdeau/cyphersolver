# Count of Siruela to Philip IV, Genoa, 19 May 1638 (catalogue 755, item EST,LEG,3594,156)

Status: read (Brice Dudout, 28 Oct 2026; 93 of 94 words read in their sense, 89 certain, 3 probable, 1 restored, 1 unresolved; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct 2026. Published write-up:
https://bdudout.github.io/europe-chiffree/en/documents.html#genes-1638

## Document

Archivo General de Simancas, Estado, legajo 3594, no. 156 (EST,LEG,3594,156; PARES 3586918), image 1.
19 May 1638; signed original. Genoa → Madrid.
Sender: Juan de Velasco y la Cueva, Count of Siruela, Spanish ambassador at Genoa. Recipient: Philip IV.
PARES record and images: https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3586918. Images are not reproduced here.

In the spring of 1638 the Spanish ambassador at Genoa had to lay in munitions on the spot. The King had ordered the Marquis Pablo Jerónimo Pallavicino (“Palavesín”) to advance him the money; the Marquis was stalling. Velasco told the King in cipher: if he failed his suppliers, they would fail him in turn.

## Scope within entry 755

Entry 755 lists 20 cipher letters (1638-1651). For the 1638 letters of Velasco y la Cueva the bundle EST,LEG,3594 keeps
contemporary plain copies next to most of them: 143/142, 146/145, 147/144, 158/157, 160/159, 169/168 (and, per our
inventory, 149/148, 151/150, 165/164). These are existing decipherments and were used only to rebuild and test the key.
**3594,156 has no plain copy** among items 3594,110-242 (PARES records surveyed one by one): it is the reading contributed here.
The letters of 1643-1651 (3598, 3600, 3602, 3637) are in other ciphers and were not attempted.

## System

the “numerical” cipher of the Genoa embassy in 1638: vowels 16–20, syllabic series of five numbers (25 ba, 30 ca, 35 sa, 40 da, 45 la), disguised syllables (consonant changed, vowel kept: ya = ra, ha = na, at = ma), single letters (m = s, ß = n, E = t) and code signs (85/86 = que, 279 = orden, hnf = Vuestra Majestad).

## Key and validation

`key_K3f.tsv`. Rebuilt on the pairs 146/145, 143/142 and 169/168, frozen (SHA-256) before each test. The earlier held-out
tests (169 later pages; 158/157) gave 0.75-0.84 of characters, below the criterion fixed in advance (>= 0.85 of characters
and >= 0.75 of words); the causes were code words still missing from the key and our own confusion of two signs of the
second hand (tall long-s = s, small loop = a). Final main test, pre-registered: 3594,160 (`validation/160_cipher.txt`,
19 lines, frozen before the plain copy was opened) against 3594,159 (`validation/159_plain.txt`): **0.896 of characters,
0.784 of words**, 200 permuted-value control keys: 99th percentile 0.343 / 0.204. Criterion met.
Further check: applied unchanged to 3594,147, the previous key version recovered its contemporary plain copy 3594,144 at
0.923 of characters / 0.850 of words.

## Reading

First published decipherment, to our knowledge (no plain-text copy found among items 3594,110–242). Rule applied: Daniel Bourdeau’s, 95% of the words read from the sense. Cipher part: 94 words (“V. M.” counted as two); certain 89 (94.7%), probable {x} 3 (3.2%: marqués, me, faltando), restored from the sense [x] 1 (1.1%), unresolved ‹…› 1 (1.1%); read from the sense: 93/94 = 98.9%.

Files: `transcription.txt`, `decryption.txt` (each line and its token values), `reading.md` (Spanish), `translation.md` (English).

## Notes

- The Marquis Pallavicino. The bundle keeps, as nos. 154 and 155, the copy of a letter from the “marqués Pablo Jerónimo Pallavicino” to Velasco dated 25 May 1638 (PARES): presumably the sequel. “Palavesín” is the Spanish form of the name, spelled syllable by syllable in the cipher (an 45 x 16 37 ß).
- {marqués}. Code sign 250 stands for “marqués de Leganés” in Medina de las Torres’s letter of 20 April 1638 (3594,146, aligned with its plain copy 145). Here the sense (“se le ofrecían”, “mandarle”, “que cumpla”, all singular) points to one man, Pallavicino: we read “el marqués” and mark it as probable.
- {me} acudiese. The cipher has ot (= mo) before “acudiese”; “me” is required by the sense (the money was to be paid to the ambassador): probably a copying slip for et (= me).
- {faltando}. The group 8̂ carries a circumflex unknown to the key; ax 8 E 17 8̂ ß 43 gives “fal-ta-?-n-do”, which sense and syntax require us to read “faltando”.
- [haciendo]. After “que le estoy”, code sign 205, followed by a stroke like other code signs, occurs nowhere else; “haciendo” is restored from the sense (“las instancias que le estoy haciendo”).
- ‹197›. A code sign not attested elsewhere; it names the person in whose absence Pallavicino was to advance the money (probably the governor of Milan, the Marquis of Leganés, or another minister); we leave it unresolved.
- Spellings. “fuse” (for fuese), “miniciones” (for municiones) and “necezario” are enciphered as such; we normalise them in the established text.

## Remaining gaps

- Code 197 (the person in whose absence Pallavicino was to pay) and code 205 (restored as "haciendo") occur only here.
