# Luis López Méndez to Simón Bolívar, London, 29 Jan 1819 (catalogue 1523)

Status: **read in part, cipher words only.** 14 of the 15 cipher words (93%) read as sense; the 15th, "[?Maracaibo]", is a context guess. These are words read from context, with a partial table consistent with them. This is a plaintext-guided partial table, not a recovered key.

Fifteen underlined words in the letter read as "he estado preso cinco veces y he salido con fianza", "Mac Gregor", "para [?Maracaibo]" and "Santafé". The table fits them without conflict. It has not been checked against a biography or against another López Méndez cipher letter, because none was found or reached.

**Why this status word.** The read bar counts words and sets no minimum length: under 95%, a document that builds coherent sentences is "read in part" (CONTRIBUTING.md; README Conventions), and short passages are already recorded by that bar (`targets/murray1801`, six code groups, is "read"). "Pointer" is for a reading sent without its texts, and all texts are here. The word applies only to the 15 cipher words. Our independent check found that "read in part" overstates the work if it is taken to imply a key, so `outcome.key` is "partial" and `outcome.contribution` claims no recovered key. If the reviewer prefers a pointer, that is a fair record too.

**Correction to the catalogue.** The entry and its vetting read "cinco meses". The signs give "cinco veces" (see Reading).

## Document

Spanish letter, ff. 226-228 of AGN Colombia, Sección Archivo Anexo, Grupo I, Historia, HISTORIA.SAA-I.17,25,D.24 (unit ff. 222-233). Signed by López Méndez and addressed to Bolívar as "Supremo Gefe de la República de Venezuela". Images: DataViva record [66b0cd4f151c9d47762a2382](https://dataviva.archivogeneral.gov.co/explore/agn/detail/66b0cd4f151c9d47762a2382), gallery [index 11](https://dataviva.archivogeneral.gov.co/gallery/66b0cd4f151c9d47762a2382?index=11) (f. 227v) and index 12 (f. 228r), fetched through the public API at 1684 x 1999 px. No images are in this folder.

The cipher is in four places, all underlined:

| Place | Signs | Words |
|---|---|---|
| f. 227v l. 17-18 | 41 | he estado preso cinco veces y he salido con fianza |
| f. 227v l. 23 | 9 | Mac Gregor |
| f. 227v l. 27 (last line) and f. 228r l. 1 | 13 | para [?Maracaibo] |
| f. 228r l. 5-6 | 7 | Santafé |

Total: 15 words, 70 signs. Line numbers are counted on the images, where f. 227v has 27 lines. The catalogue's folio note has "lines 20-22" and "line 27" for the first two places; those numbers do not match the page.

There is no decipherment over or beside the cipher words, and the unit holds no key and no clear copy.

## System

Ordinary lowercase letters, many with a digit 1-7 written above. In this sample each letter + digit, and each bare letter, has one plain value, so it behaves as a single fixed substitution on those symbols. The base letter alone does not fix the value: e1 = b, e2 = f, e3 = l, e4 = r, e5 = t, e6 = v, e7 = y. Commas separate the cipher words and the writer's stops are kept.

21 distinct symbols occur: 20 with a value and one without (the t with an extra stroke, below). 42 of the 70 signs carry a digit.

## Table and what tests it

No pairs exist. The table comes from the clear context around the words, first in the catalogue's vetting of 28 Oct 2026 (`research/latam_vetting/1523_sample.txt`) and then here. It is built from the assumed plaintext (`solve.py`), so "no conflict" tests consistency only.

- **Fit.** 0 conflicts in both directions, one symbol to one letter and one letter to one symbol. 20 symbols cover 69 signs.
- **Real constraints.** About 50 repeats of a symbol, the repeat patterns inside words and the one-to-one mapping. Gregor (A B C A D B: d1 e4 r d1 o2 e4), fianza (letters 3 and 6 equal), veces (A B C B D), cinco (A B C A D), para, Santafé and "he ... he" fit without choice. a = n at four places and m1 = c at six are re-uses.
- **What rests on least.** d1, e1, e3, e6, e7, m3 and o1 are found in one word only. e1 = b, t1 = m and d1 = g rest on context alone.
- **No held-out test.** An earlier draft froze the table on the first ten words and then read "para" and "Santafé". We do not count that as held out: both words use only symbols already seen, and context had supplied them first.
- **Control.** Plain words swapped at random among cipher words of equal length (the 14 words other than [?Maracaibo]). The independent check reported 76 of 20,000 trials without conflict (0.4%). Our rerun (`python solve.py --controls`) gave 62 of 20,000, and all 62 were the true assignment again; none was a different one. The fit is far better than chance, but this is a mild test.
- **Digit order (not checked by the second reader).** Within each base letter the plain values rise through the alphabet with the digit: e gives b f l r t v y, i gives d p, m gives c z, o gives h o, t gives m s. Nothing in the building of the table assumed this. For the seven e values alone, the chance of a rising order is 1 in 5,040 if digits and letters were unrelated. It suggests a partly alphabetical table, and it covers values that occur only once (e1, e3, e6, e7). It is an observation on a small sample, not a proof.

## Independent blind check

A second agent read the cipher lines from enlarged crops before opening this transcription, and reran the fit with its own script.

- Letters: agreement on all 70. Digits: two or three undecided, all unclear marks, none changing a letter value. Disagreement about 3 of 70 symbols (4%). It was one reader, by eye, on 3x crops. (Its report says roughly 55 digit marks; the transcription has 42.)
- The undecided marks, looked at again at 4-7x for this contribution:
  - the 3 on the first i of "i3 l e4 l" is clear;
  - the first m on f. 228r has a stroke above it, at the top of the page with no line above, so it is m1. An earlier draft had a bare m ("digit 1 not seen"). The check's rerun also took it as m1;
  - the stroke over the last t of "t1 l e4 t" stays open (see Reading).

## Reading

Texts: `transcription.txt`, `decryption.txt` (line by line), `reading.md` (with the editorial notes) and `translation.md`. Key file: `key.tsv`.

The first passage stands in a request for money. In the clear text López Méndez presses Bolívar to send funds at once, by bills on Saint Thomas, Grenada, Trinidad or another island, for a debt of 4,100 pounds, 14 shillings and 6 pence that he had bound himself to pay. The cipher sentence is offered as proof of the urgency: "para que no le quede á V.E. la menor duda de quanto urge esta medida". The second passage says Mac Gregor has done untold harm; López Méndez joined an expedition of his and left it. The third says Mac Gregor is trying to go to Santafé.

**"veces", not "meses".** The signs settle it. The word is e6 r m1 r t3. The first symbol is an e with a clear 6. The third is m1, which is c in cinco. The fifth is t3, which is s in four other words. "meses" needs the third and fifth letters to be one plain letter, s, but they are two different symbols, so it would need an unexplained homophone. The clear text then says "en todas estas ocasiones" (on all these occasions), which fits "veces" and not "meses". The digit order points the same way: e6 falls between e5 = t and e7 = y.

**"Maracaibo" is a guess.** M-a-r-?-c-a-i-b-o is nine letters and the caibo part fits. But the fourth sign would have to be a, and it is written t, while a = l in all eleven other places. It needs a homophone, a slip of the pen, or a different word. On a 7x crop the stem has the height of a t, not of an l, with an extra stroke above it that may be a digit. If that digit is 1, the sign is t1 = m, which does not help. No hyphen is written after this sign at the foot of f. 227v, though the writer uses one in "santa-fe"; no comma closes it either, so we take the word as running on, but that join is ours. No outside account of MacGregor's plans was used to decide this.

**The jailings rest on the cipher alone.** One search found no source for an imprisonment of López Méndez in London in 1818-19. It did find the rift between López Méndez and MacGregor over recruiting, and an arrest in Peru in 1826, which is a different event. So the jailings are neither confirmed nor contradicted. The cipher words do not give the cause; only the clear context points to debt. Mondolfi's biography of López Méndez was not checked.

## Prior work

Prior art is open. Checked:

- Catalogue vetting, 28 Oct 2026: not on DECODE or cryptiana, and no hit in 15 O'Leary volumes on archive.org. That grep had "cinco meses" among its strings, but also "perjuicio indecible" and "salido con fianza".
- 2 Nov 2026: one web search in Spanish found no edition or decipherment; one further search on the imprisonment, as above.

Not reached: Bákula 1949, the Archivo del Libertador, the O'Leary correspondence volumes not on archive.org, Mondolfi. The vetting found that no key in the repository fits. We do not call this reading new.

## Scripts

`solve.py` writes `key.tsv` and `decryption.txt` from the transcription and prints the checks above. `python solve.py --controls` adds the control. Standard library only.

## Remaining gaps

- The word "[?Maracaibo]": the fourth sign (written t, extra stroke above) has no value and the identification is a guess.
- The rest of the table: q, u, j, x, k, ñ and most cells of every column but e cannot be filled from 70 signs. A real key needs another letter in this table; none was found.
- e1 = b, t1 = m and d1 = g rest on context alone.
- Whether López Méndez was jailed five times is not confirmed by any other source.
