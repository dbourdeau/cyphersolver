# Biermann copybook 1675 (Unsolved Catalogue no. 465)

Status: in progress (every image-55 letter to Høeg and Meyercron read, eleven here and 26 by Brice Dudout in `dudout/`; Gioë, Schröder and the letters without a key open)

Conrad Biermann's copybook of outgoing letters from the Danish German Chancery (Tyske Kancelli, Udenrigske
Afdeling) to Danish envoys abroad, 1675: Rigsarkivet, TKUA Almindelig del, "Conrad Biermanns kopibog over
udgående skrivelser til danske ministre i udlandet" (Daisy heid 2130515, unit S-1418). 255 images on
Arkivalieronline (epid 15552891, image ids 48573952-48574206). The letters are clear French or German with
long cipher passages copied into the register; there is no interlinear decipherment.

## Survey (26 Oct 2026, `survey_A.tsv` images 1-128, `survey_B.tsv` images 129-255)

About 200 letters, 2 January to 24 June 1675 (pp. 1-249). Cipher on about 356 page sides, roughly 5,500
lines (line counts estimated from the images, not measured). Images 235-236 are Rigsarkivet placeholders
("Ukendt billede"); the foliation runs on, so no page is lost. Image 52 re-shoots the opening of image 51.

Correspondents and their number families (from sample numbers; a family is a hypothesis until a key reads it):

| correspondent | clear language | numbers | key |
|---|---|---|---|
| Just Høeg, The Hague | French | to ~673 | image 55 (read: 2 Jan test, image 5) |
| Meyercron, Paris (from late Jan) | French | to ~673 | image 55 (read: 23 Mar letter) |
| Marcus Gioë, England; Schröder | French | to ~673 | image 55 family (untested) |
| Meyercron, 2 Jan only | French | to ~320 | unknown |
| Lilienkron | German | 14-707, signs Δ θ | unknown |
| Gioë, Moscow | French | to ~764 | unknown |
| George Reetz, Spain | French | to ~740; pattern changes from image 199R | unknown |
| Lindenow, Stockholm | French | 700-986 | unknown |
| Klingenberg | German | 2xx-525 with letter signs | unknown |
| Lincker (Cleves) | French | 600-1105, from April | unknown |
| Høeg, 21 June | French | 400-833, sent with "la chiffre française" | unknown |
| Lente (Brussels), 21 June | French | 2xx-4xx, three lines | unknown |

Leads noted by the survey: Biermann sends Meyercron "le chiffre" augmented with words (3 April, image 121);
the Klingenberg letter of 6 Feb (image 44) asks whether its syllables match the French cipher; the clear
text of the Lindenow letter of 22 Feb (image 71) runs nearly word for word with the clear Meyercron letter of
20 Feb (images 67-70); the Gersdorff/Celle passage recurs in the Lilienkron (245R) and Klingenberg (249R)
letters of 21 June under two ciphers (a crib); several entries end "vide concept an X", copied from
another letter.

## Prior work

Not on DECODE, not in the repo, nothing found in print or on the web (catalogue check of 26 Oct 2026; searched
again 26 Oct 2026: Biermann + 1675 + cipher/chiffre, Danish diplomatic ciphers, Rigsarkivet "Chiffer").
No decipherment in the volume itself.

## Key: TKUA "Chiffer" 1670-1709, image 55

The catalogue's key lead is right. The Tyske Kancelli "Chiffer" volume 1670-1709 (Daisy heid 2132747;
Arkivalieronline epid 15553654, which redirects to 19852193; 309 images, ids 48691476-48691784) holds many
keys. Image 55 (id 48691530) is a one-sheet key headed by the names Pomponne 111 and Terlon 112:

- letters: two sign alphabets and one number 1-24 per letter (`key.tsv` has the sign labels);
- names 25-276 (Kongen 25, Kongen af Frankr. 102, Pomponne 111, Terlon 112, Svenske Ambr. 154, Staten
  General 162, Printz von Oran. 169, countries 210-222, a few adjectives 274-276);
- an alphabetical code from 279 on: open syllables in blocks (ba 312 ... vu 674, wa 688 ... wu 692) with words
  between them in alphabetical place (Alliance 292, Condition 347, defensiv 391, Majesté 526, traité 657 ...).

The sheet is a summary, not the whole key: the gaps between the syllable blocks held words that are not
written on it. Its German/Danish name entries suggest it was the chancery's own copy.

It fits the letter to Meyercron in Paris of 23 March 1675 (images 108-109, pp. [103]-105) exactly:
263 cipher tokens, 262 give sense with the sheet (99.6%), the one open sign an open square in "qui[?]
propose". Reading and translation in `reading_1675-03-23_meyercron.md`. Content: the King wants Meyercron
to keep telling the French court that the Swedish ambassador's (Niels Brahe's) demands do not match what he
had promised, and that his eagerness for a treaty in Copenhagen is hardly sincere.

## Other keys in the volume (not yet matched)

- The letter to Meyercron of 2 January 1675 (image 4, p. 1) uses numbers this sheet does not explain
  ("mesures X, 320, φ, 262, et 262, 136"), so Paris had a different key early in the year, or the gaps hold it.
- The letter to George Reetz in Spain ending on image 108 (left page) uses another numbering
  (598, 680, 376, 379, 352, 629, 702 ...).
- Key-volume image 114 is a 1670s key with Beuningen, Fagel, Amerongen, Tromp, Oxenstierna, Meyercron 57 in
  its name list (probably the Hague key); not yet tested.

## Key volume sweep (26 Oct 2026, `keyhunt.md`)

All 309 images of the "Chiffer" volume were dated by their names and tested, where the range fitted, on
10-20-token runs of each open family. Only image 55 reads anything. Most of the volume is earlier (Christian
IV, 1640s-50s) or later (1680s-1730s). The 1670s keys tested and ruled out for the 1675 letters:

- 294/295, "Chiffren for Jörg. Reetz og Christ. Lindenau i Spanien 1676-77": the successor Spain key; the
  Reetz letters' groups 630/653/680/681 are blank there and ǂ is B.
- 305-308, a Danish key naming Høge, Gioë, Lilienkron as Resident, Lincker in Brandenburg, Reetz in Spain
  (names 42-371, Danish words 382-949): no run reads on Lindenow; Lindenow's and Lincker's 963-1056 lie past it.
- 145-147, German key naming Liliencron in Vienna and Gioë in Moscow (2-814): the frequent Lilienkron and
  Moscow groups fall on blank slots.
- 114-116 (Ahlefeldt as Grand Chancellor, 1676 or later), 265 (Poland 1673-76), 236, 224, 140-142, 075: no fit.

Lead: image 94/95, a German key of 1675 (endorsed "reçu le 18 ... 1675 à Stargard"). Its declared null row
is the sign set of the Klingenberg letters, and 9 of 22 numbers in the 6 Feb Klingenberg letter (image 43R)
fall on filled entries that fit (327 Nach, 117 durch, 220 Herzog, 393 Rath Biermann ...); the other 13 fall
on slots left blank on the sheet. Not proven; the sheet may be an incomplete copy of the Klingenberg key. The Klingenberg key was later rebuilt from the letters themselves in `targets/klingenberg1675/` (12 Nov 2026) and is not this sheet as it stands: 117, 140, 200 and 224 differ.

Not testable: 309 (wrapper "Jens Juel or Petkum to Sweden 1670-71", key too faint), 083/091 rotated,
096/098, 092 (pre-1672), 281-284 and 287-290 (large later keys).

## Brice Dudout's reading of the image-55 letters (27 Oct 2026)

Brice Dudout (Europe chiffrée, `https://bdudout.github.io/europe-chiffree/en/documents.html#hoeg-1675` and
`#meyercrone-1675`) read the letters under the image-55 key (his K55), independently of the work here; his first email
of 27 Oct named the same key sheet the day after this folder's key sweep had found it.

- To Just Høeg, The Hague: eighteen letters, 2 Jan - 5 June 1675 (2, 5, 9, 12, 16, 19, 22, 26, 30 Jan; 6, 9, 13 Feb;
  2, 6, 30 Mar; 10 Apr; 15 May; 5 June), cipher in eleven of them. 2, 5 and 9 Jan: 841 of 849 groups; 12 Jan - 9 Feb:
  2,308 groups, about 2,260 read.
- To Henning Meyercrone, Paris: nineteen letters, 16 Feb - 21 June 1675, 6,103 groups, 6,068 (99.4%) with K55 frozen.
  A cipher "increased by a few words" went to Meyercrone on 3 Apr 1675, so some name codes are not on the sheet:
  ‹35›, ‹37›, ‹53›, ‹29› open, ‹163› and ‹254› unresolved, a few understood from sense. The 2 Jan letter to
  Meyercrone is in another key, as the survey here found.

**Corrected 27 Oct 2026.** This folder had itself read the eleven Høeg letters of 2 Jan - 9 Feb 1675 and the
Meyercron letter of 23 March on 26 Oct (`reading_1675-01-02_hoeg.md` ... `reading_1675-02-09_hoeg.md`,
`reading_1675-03-23_meyercron.md`, with their transcriptions); the section above, written 27 Oct, missed them. Those
twelve were read here and by Dudout independently, with the same key sheet. Dudout's pull request #133 (merged
27 Oct 2026, `dudout/`) adds the 26 letters not read here: Høeg 13 Feb - 5 June (7) and Meyercrone 16 Feb - 21 June
(19, with 23 March read on both sides). So every image-55 letter to Høeg and Meyercrone is now read in this folder.
What is left: the letters to Gioë in England and Schröder (image-55 family, untested), the letters without a key (next
gap), and a comparison of the twelve letters read on both sides. Catalogue 465 narrowed accordingly.

## Remaining gaps

- Letters under the image-55 key to Gioë in England and Schröder - blocker: not-attempted; every Høeg and Meyercron letter of this family is read (eleven here, 26 more in `dudout/`), so these are what is left of it.
- Letters without a surviving key (Lilienkron, Gioë in Moscow, Reetz in Spain, Lindenow in Sweden, Klingenberg (since read in part with a rebuilt key: `targets/klingenberg1675/`), Lincker, Meyercron 2 Jan, Høeg 21 June, Lente 21 June) - blocker: not-attempted; the whole key volume was swept and nothing fits (keyhunt.md), so the next move is a key rebuild from the ciphertext (large volumes per family) plus the cribs listed above.
- 23 March letter to Meyercron, p105.24: one open-square sign, most likely "l" - blocker: open-codes; one occurrence; Dudout's reading of the same letter (`dudout/texts/1675-03-23_meyercrone_reading.md`) and his 19 Paris letters are the retry material.

## Escalation

- [x] siblings: the whole copybook surveyed page by page (survey_A/B.tsv); the leaves around images 108-109 opened; the Høeg letter of 2 Jan reads with the same key.
- [x] clear-pages: no decipherment in the copybook; the clear Meyercron letter of 20 Feb (images 67-70) is a near-parallel of the Lindenow letter of 22 Feb (image 71), noted as a crib, not a decipherment.
- [x] known-keys: all 309 images of TKUA "Chiffer" 1670-1709 dated and the 1670s keys tested on every family (keyhunt.md); only image 55 reads.
- [x] print: web searches 26 Oct 2026 (Biermann 1675 cipher; Meyercron 1675 despatches; Just Høeg 1675 letters; Danish diplomatic ciphers): no edition of these letters or their ciphers found. Not on DECODE, Tomokiyo or Lasry.
- [ ] key-rebuild: not yet (image-55 gaps from use; ciphertext-only rebuild for the keyless families).
- [ ] retry: not yet.

## Files

- `fetch.sh` downloads the scans (`sh fetch.sh book 48573952 255`, `sh fetch.sh keys 48691476 309`);
  images are git-ignored.
- `contact.py`, `crop.py`: contact sheets and crops for reading the scans.
- `key.tsv`: the image-55 key; `decode.py`: applies it to a transcription.
- `transcription_p104-105.txt`, `ct_1675-03-23.txt`: the 23 March cipher; `reading_1675-03-23_meyercron.md`.

## Readings contributed by Brice Dudout (28 Oct 2026)

`dudout/` holds 26 further letters read with the image-55 key (frozen independently on 26 Oct 2026):
Høeg 13 Feb - 5 June 1675 (7) and Meyercrone 16 Feb - 21 June 1675 (19, including 23 March, which can be compared
with `reading_1675-03-23_meyercron.md`). See `dudout/README.md`.
