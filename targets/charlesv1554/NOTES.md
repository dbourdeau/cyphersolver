# charlesv1554: Besançon BM Ms 1582, f. 2, the cipher passage of Charles V's letter to his ambassadors in England, 24 January 1554

Status: read in part (210 of 358 words sure = 58.7 %; with probable words 93.6 %). Already solved: deciphered at the time on the page, text in print (Gachard 1882; CSP Spain XII), key published (Pich-Ponce 2024). New here: the identification of the leaf, a check of the published cipher on a new witness, and the cipher-versus-decipherment differences.

## Source

**Bibliothèque municipale de Besançon, Ms 1582, f. 2** (r and v). Library catalogue title: "Lettre chiffrée adressée au
lieutenant d'Amont (avec traduction en marge)", dated "1555" in a later hand. Scans sent free of charge by the library
for research on 18 Nov 2026. **No image is included here or anywhere in this folder**: the library's consent is needed
to publish its images, and its notices ask that any publication of unpublished documents be notified to it. Cite as
"Bibliothèque municipale de Besançon, Ms 1582, f. 2".

## What the leaf is

Two pages of cipher (about 1,075 signs in 48 transcribed lines, plus one cut line at the foot of each page), with the
contemporary decipherment written around it: three or four full-width lines above and below the cipher on each page,
and a column in the margin. No address, signature or date: the text starts and ends in mid-sentence.

**Identification (new).** The text is the central passage of *L'Empereur à ses ambassadeurs en Angleterre*, Brussels,
24 January 1554 (Lalaing, Egmont, Courrières and Simon Renard, the "lieutenant d'Amont"), from "[de no]stre part, que
nous avons toujours eu et avons encores la mesme volunté de desirer la paix" to "il sera bien que de temps à autre
[nous donnez advertissement ... selonc ce]". It answers the French peace overtures (Wotton in France; the French
ambassador to Paget in London), recalls the proposal of September 1553 made at the request of the Cardinal of Imola
(Girolamo Dandino), offers to negotiate through Mary Tudor, and asks Renard to learn from Paget about the French
"partiz de mariage". So the catalogue date "1555" is wrong; the letter is of 24 Jan 1554 (new style).

Printed texts of the same letter:

- **Gachard**, *Collection des voyages des souverains des Pays-Bas*, t. IV (Brussels, 1882), appendix CLV, pp. 311-314,
  the full French text of the minute; this passage pp. 313-314 (Internet Archive `collectiondesvoy04gachuoft`).
- **Tyler (ed.)**, *Calendar of State Papers, Spain* XII (1949), pp. 44-49, "Vienna, E. 23", English calendar of the
  minute; this passage pp. 46-47; the note on p. 49 records "a fragment, from a mutilated copy at Besançon, printed by
  Weiss" (British History Online, cal-state-papers/spain/vol12/pp36-50).
- **Weiss (ed.)**, *Papiers d'État du cardinal de Granvelle* IV (1843), no. LXIII, pp. 188-192, from "Ambassades de
  Renard, III, 119-122" (Besançon, Ms Granvelle 73, ff. 119-122). Weiss prints a first fragment that **stops on p. 190
  at "...que nous avons toujours eu et avons encores"**, with the footnote "Lacune considérable dans le manuscrit", and
  resumes with "Davantaige, pour observer ce qu'est de coustume...". Ms 1582 f. 2 begins with exactly these words in
  cipher and ends where Gachard's next paragraph ("Davantaige...") begins: it holds the passage missing from the
  Besançon copy that Weiss printed.
- **Hypothesis, not checked:** that Ms 1582 f. 2 is the leaf detached from that copy (Ms Granvelle 73, ff. 119-122). It
  would need the two volumes side by side (paper, hand, folding, the text on the preceding leaf: the first cipher line
  of f. 2r continues a word begun elsewhere).

## The cipher and the key

**Prior art, cited first.** Eva Pich-Ponce, "El lenguaje cifrado de Carlos V y el matrimonio de María Tudor",
*Cuadernos de Historia Moderna* 49 (1), 2024, pp. 27-45, describes this cipher from 24 letters of 1549-1554 to Simon
Renard (Charles V, Mary of Hungary, Nicolas and Antoine Perrenot), studies the letter of 31 Jan 1554 (Besançon, Ms
Granvelle 73, ff. 201-206) and checked her table against two original nomenclators in Simancas (AGS Estado leg. 1,1,1,
ff. 136 and 210). Satoshi Tomokiyo's Cryptiana post "Three ciphers used in correspondence" (March 2026) lists it as the
third cipher of the Granvelle-Renard correspondence (1549-1554). Neither mentions Ms 1582 f. 2 or the letter of 24 Jan
1554 in cipher.

Her structure, as stated in her text: single letters a to t by numbers 20 down to 2 (a second series 21-39), u-z by
51-54 and 62-65, *et* by 55 or 66; two-letter syllables by the letter *preceding* the initial consonant in the alphabet
plus a vowel mark: "+" a, bar above e, bar below i, two dots o, dot below u; double letters by a vowel plus the
consonant; nulls marked by two dots; code signs for persons (Pope, Emperor, King of France ...).

**What was done here (not a new key).** The key in `key.tsv` was re-derived *without* her paper (it was found only
afterwards, at the prior-art check of 18 Nov 2026), by aligning the blind transcription of the cipher with the
contemporary decipherment on the page (EM alignment, then a rule fit). It agrees with her structure on every point we
can compare from her text: numbers 8 n, 7 o, 9 m, 6 p, 2 t, 4 r (her a20 ... t2 series); 66 *et*; bar above = e
(`q^` re, `c^` de, `h^` le, `x^` se, `m^` ne), bar below = i (`o_` ti, `c_` di, `x_` si), two dots = o (`t:` vo, `q:`
ro, `6:` co), dot below = u, an attached t = a (her "+": `qt` ra, `kt` la, `tt` va); the base letter is the letter
before the consonant (`c` for d, `k` for l, `q` for r, `m` for n, `t` for v, `b`/`6` for c, `p` for qu). Agreement
with the contemporary decipherment 79 % of letters; split-page hold-out 0.726 (train recto, test verso) and 0.691
(train verso, test recto) against 200 shuffled keys at most 0.25 (`holdout.txt`; the seed alignment used both pages,
so this is not a strict validation). So this folder is a **verification of Pich-Ponce's cipher on a new witness**,
not a key of our own. Her tables are printed as images and were not compared sign by sign.

## The cipher against the contemporary decipherment and the minute

The contemporary decipherer (top, bottom and margin of the page) kept the sense but not always the words. Read with
the key, the cipher differs from his decipherment in about two dozen places (`divergences_cipher_vs_gloss.tsv`). The
minute printed by Gachard settles them (`divergences_vs_minute.tsv`): in **21 places the minute agrees with the cipher
against the decipherment**, e.g. *comporté et dissimulé* (decipherment *supporté et ...*), *sans cause quelconque*
(*sans contraincte*), *rebouté* (*cessé*), *combien que* (*ainsy que*), *condicions convenables* (*raisonnables*), *pour
estre chose qui se négocie par elle et où elle mect la main* (*pour autre chose que se negocie par elle et en elle mist la
main*), *l'on vous respondera* (*luy vous respondra*); in **one** (r13 *mit en avant*) it agrees with the decipherment;
the passage at v17-v18 (*le lieutenant d'Amont, assentiz dudit Paget*), garbled in the decipherment, reads in the
cipher once the minute is known. Pich-Ponce noted the same habit of the marginal decipherments (2024, conclusions),
and that Weiss printed from them.

## Files

| file | content |
|---|---|
| `transcription/pass_A.tsv`, `pass_B.tsv` | two blind transcriptions, margin masked, made independently (Claude Opus 5.5), with their notes and sign lists (French, as written; image file names in the notes refer to local crops that are not published) |
| `transcription/cipher_reconciled_AB.tsv` | the two passes aligned sign by sign (91 % agreement after mapping the two naming schemes), with the key value of each sign |
| `key.tsv` | the re-derived key (value, occurrences, agreement, rule base + mark), French column notes |
| `decryption.tsv` | line-by-line decode of the cipher with the contemporary decipherment aligned beside it |
| `holdout.txt` | split-page hold-out against shuffled keys |
| `period_plaintext_full_width.md`, `period_plaintext_margin.tsv` | diplomatic transcription of the contemporary decipherment (full-width lines and margin), French |
| `divergences_cipher_vs_gloss.tsv` | places where the decoded cipher and the contemporary decipherment differ |
| `divergences_vs_minute.tsv` | the same places against Gachard's minute, with a verdict |
| `reading.md` | reading (sure / {probable} / [restored]), count, English translation, summary |

## Remaining gaps

- The last line of each page (r24, v26) is on the library's scans but fell outside the crops used for the two blind passes; not transcribed here (no outside blocker); about 19 words, known from the minute and counted as not read.
- Key gaps: the *no/po* syllable read as `nus`/`pur`; the two forms behind `nz` (d/i) and `w` (a/l), and `mt`/`nt` (n/p); the cipher's table is in print (Pich-Ponce 2024, as images), so these values are not unknown, only not transferred into `key.tsv`; matching her printed shapes to our sign names was not done here (her article is not in our files).
- Whether Ms 1582 f. 2 was detached from Ms Granvelle 73 ff. 119-122 is not checked.

## Escalation
- [x] siblings: the Besançon copy (Ms Granvelle 73 ff. 119-122, printed by Weiss with a lacuna here) and the minute (Vienna E. 23, printed by Gachard) located in print; the manuscript copy itself not seen
- [x] clear-pages: the contemporary decipherment on the leaf transcribed (period_plaintext_*)
- [x] known-keys: Pich-Ponce 2024 found after the re-derivation; structure matches; her image tables not applied sign by sign
- [x] print: Weiss IV, Gachard IV, CSP Spain XI-XII, Pich-Ponce 2024, Cryptiana: text and key in print
- [x] key-rebuild: EM alignment on the contemporary decipherment, 79 % of letters
- [n/a] retry: the text is in print; the two cut lines need a fresh crop of the library's scans, left for a later pass

## Method

Claude (Opus 5.5) agents for Brice Dudout, 18 Nov 2026: two blind transcriptions with the margin masked; a diplomatic
transcription of the contemporary decipherment by a third pass; key re-derived by alignment; prior-art check
afterwards (Weiss IV and Gachard IV on the Internet Archive; CSP Spain XI-XII on British History Online; Pich-Ponce
2024; Cryptiana; this repository's ledgers), which found the printed text and the published cipher.

Outcome method (`profile.json`): *key recovered based on adjacent plaintext*. The cipher was decoded with a key
re-derived from the leaf's own contemporary decipherment, and the decode was checked against the minute printed by
Gachard; it is not a transcription of the existing decipherment alone.
