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

**All six key sets tested** (each frozen by SHA-256 before its test; one measurement each; 200 permuted-value control keys).
K3f, the key in this folder, is the sixth. Four failed, one passed only under the older bar, and the bar was raised (not
lowered) after the second test.

| key | built on | held-out test (transcription frozen before the plain copy was opened) | characters / words | controls p99 | bar | result |
|---|---|---|---|---|---|---|
| K3 (6441306f...) | 146 segment A | 146 segment B against 145 | 0.733 / 0.633 | 0.312 / 0.172 | characters >= 0.80 | failed |
| K3b (ae8abae7...) | K3 + values taken from segment B | 169 against 168 | 0.838 / 0.681 | 0.325 / 0.143 | characters >= 0.80 | passed under that bar (words 0.681, under the later 0.75) |
| K3c (51168c12...) | K3b + 143/142 | 169, later lines, against 168 | 0.750 / 0.713 | 0.292 / 0.138 | 0.85 / 0.75 (protocol addendum 6-8, written before the test) | failed |
| K3d (ab782712...) | K3c + 23 codes from 169/168 | 169 image 3 against 168 | 0.825 / 0.694 | 0.327 / 0.153 | 0.85 / 0.75 | failed (a supplementary test on 147 against 144 gave 0.923 / 0.850; by the protocol it does not replace the main test) |
| K3e (1831a941...) | K3d + 5 values from 144 | 158 against 157 | 0.843 / 0.626 | 0.349 / 0.180 | 0.85 / 0.75 | failed (0.876 / 0.744 after one sign of our transcription was corrected: indicative only) |
| K3f (b0b4d5c9...) | K3e corrected: hi = ni, "hi 245" as one group, tall long-s and small loop told apart in the second hand | 160 against 159 | **0.896 / 0.784** | 0.343 / 0.204 | 0.85 / 0.75 | **passed** |

Each failed test spent its passage: no later key was measured again on it. What the failures taught (missing nomenclator
codes; our confusion of two signs of the second hand; the hi = señor error of K3e) went into the next key, and the next test
was on lines whose plain copy had not been opened (later pages of 169 for K3c and K3d, new pairs for K3e and K3f).

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

## Sign check G, 18 Nov 2026

Level sought: "AI decipherment, human-checked on a sample of signs" (`outcome.sign_check`; files in `sign_check/`). It checks
how signs are written, not the key or the reading, and it changes neither the class nor the read share.

**Who did what.** The checker is Brice Dudout, the contributor of this reading (a project member, not an independent reader).
He answered blind: one boxed sign per question, shapes cut from sure words of the same letter, plus "none / other shape",
"illegible" and "not a sign"; no value, gloss or word shown. An AI model (Claude Opus 5.5) wrote the rule, chose the signs by
it, cut the thumbnails, built the sheet, scored the answers and interpreted the two free-text remarks. The answer key stays
private; its content for each question is in `sign_check/sheet-G-results.tsv`. No image or thumbnail is committed.

**Rule** (fixed on 18 Nov 2026 before the answers; written in French in our files and **not hashed**; given here in English):
1. one sign per unmarked word whose departure from the key may come from the transcription (municiones, fuese), and per
   marked word whose mark may fall on the image ({me});
2. the two hooked-looking 86s (aquí, quien), each shown with plain 86s;
3. a sign the reading leaves out (the 8 of L01); a digit on which a value missing from the key depends (2nd digit of "17/12",
   L08; 3rd digit of 205);
4. the only rare sign on which a sure word depends (ß' = f, once: "ofrecían");
5. two controls with a known answer, in sure words, on the same shape families as the targets of item 1 (the i of "it" in
   cumplimiento; the o of "on" in respondido);
6. no question on normalised spellings, on code 197, or on the accent of 8̂ (clearly visible: a question of value, not shape).

**Answers.** `sign_check/sheet-G-answers.json`, exported 2026-11-18T11:51:38Z (SHA-256
5d64a54a4625579f63339179256cb1c69eb024b6c2e17a6f7c1052222aff005d). Controls 2 of 2. Nine target signs: 4 corrected ("ut" for
"it", municiones; the sign missing at the end of L04, fuese; "et" for "ot", me; 12 for 17, instancias); 4 as transcribed (both
86s are plain 86s, so the hooked-86 hypothesis is rejected and "aquí", "quien" are readings by the sense; 205 confirmed;
ß' is a sign of its own, f); 1 unresolved (the first sign of L01 is a barred 8, a sign with no value, probably a null). No
value of `key_K3f.tsv` is contradicted, and nothing was added to the key.

**Not yet done.** What the answers contradict is to be recoded or marked in the reading first. The four corrections and the
new marks ({aquí}, {quien}, {instancias}, the barred 8) are applied in our local copy only; `transcription.txt`,
`decryption.txt` and `reading.md` here are unchanged. The published reading "con que tenía" should read "con {quien} tenía".
On the corrected local copy: 87 sure, 5 probable, 1 restored, 1 unresolved of 94 words (87/94 = 92.6 % sure; 92/94 read by
the sense).

**Limits.** One checker, inside the project. Two controls show little on their own. The signs were chosen because they were
doubtful: a diagnostic, not a sample of the text. No person has audited the model's part.
