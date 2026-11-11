# klogesoren1858: "Kloge Søren" (Søren Christensen), his Cyprianus, a book of charms in his own cipher, c. 1858 (catalogue 2525)

Status: read in part (Brice Dudout, 11 Nov 2026; partial reading explained: key validated on a held-out portion of 790 signs; that held-out portion is read 169/179 words = 94.41% after one blind re-reading sheet, under the 95% rule; the whole book reads about 95.1% of 8,055 words after a targeted blind sheet (K3, 9 signs) on the second session, an indicative figure only). Open: 9 pages read at low resolution only (90.6%), weak pages 064 left and 010 right, a declared re-reading of the shapes flagged by K3.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents (transcription, key, protocol and measurement, reading,
write-up). Catalogue entry **2525**, found and vetted by Daniel Bourdeau on 11 Nov 2026 (KB Copenhagen Primo sweep, Nordic sweep of
11 Nov), who pointed to the book, to its "lønskrift" (secret writing) and to the KB images.

## Document

Copenhagen, Det Kgl. Bibliotek, Dansk Folkemindesamling, **DFS 1997/020** (Kloge Sørens samling). One octavo volume, 109 images
on KB Digitale samlinger (object392246; IIIF DFS_1997_020_4_000a to _107 on kb-images.kb.dk). The KB marks the material as out
of copyright ("Materialet er fri af ophavsret"); even so, **no image, crop or derivative is included here**: link to the KB viewer.
Credit: Det Kgl. Bibliotek / Dansk Folkemindesamling, DFS 1997/020.

Søren Christensen, "Kloge Søren" (1843-1925), a cunning man of Funen, wrote this Cyprianus (a book of charms and cures) from 1858,
as a boy, almost wholly in his own cipher, in red ink, under headings in clear Danish. The cipher text runs from image 003 right
to 079 right; images 080 to 093 are blank leaves, pastedowns and binding; image 091 left carries the writer's table of the cipher
alphabet. Two loose leaves carry cipher in the same signs: 098 (a charm, two copies) and 104 (a circular seal, not read). A private
piece of the 20th century, not part of the grimoire, is excluded from this write-up.

## System and key (`key.tsv`)

A simple substitution, one sign per letter, with **word spaces kept** (the catalogue scan at 1,700 px did not show them; at full
size they are clear). About 27 signs made of chevrons, bars under 1-3 dots (u, n, m), strokes with dots placed above, beside or
below (s, k, h, b, p), hooks (d, g, r, i/j), a cross (t, also f), an arch (v), dots (o, ø). Homophonies and confusions declared:
t/f, o/ø, i/j. Ligatures (aa, tt, nn, mm) and variants are listed in `key.tsv`, section D.

How the key was found (training portion only, images 003 right to 007 left, 1,591 signs transcribed at low resolution): probable
words from the clear marginal "3 gange", the closing formula "i Navnet Gud Fader, Gud Søn og Gud den Hellige Aand. Amen" and the
cipher ordinals of the headings ("Andet / Tredie Begreb"); then a **blind** simulated annealing (simple substitution, Danish
quadrigrams with the space from Project Gutenberg texts, only the space fixed) found by itself "saa sandt ... dette blod ei mere
flyde i navnet gud fader gud søn og gud den hellige aand amen" (6 of 10 restarts converge).

`key.tsv` sections: A = the key as measured (frozen/KEY.json); B = separation of the stroke-and-dot signs at full resolution,
after the measurement; C = the writer's table on image 091 left; D = ligatures and variants of the second session. License CC BY 4.0.

## Validation (`frozen/`)

**Key validated.** One measurement, pre-registered and hashed before the held-out portion was ever looked at:
`frozen/PROTOCOLE.md` SHA-256 106f10c69168ee2aa1c5a1390c040351b512f40bb461b426f3984fd2292a7329, `frozen/KEY.json` 40bf4b2d...,
scorer `mesure.py` 530a86e5..., Danish word list 5c295d99... (`frozen/FREEZE.sha256`; the scorer and the word list are not
included: the scorer holds a local path, the list is built from Gutenberg texts). Held-out portion = image 030, then image 031
added by the protocol's rule because 030 has fewer than 300 signs; both transcribed and hashed before any decoding
(`frozen/RESERVE-p030.txt` d56aef4d..., `frozen/RESERVE-p031.txt` d2d93503...). Result (`frozen/MESURE.out`), on 790 signs
(185 words): lexical cover **COV 0.4025** (C1 >= 0.40: met, narrowly); best of 200 permuted keys 0.1089 (C2 threshold 0.359: met);
best of 200 shuffles of the signs 0.1038 (C3 threshold 0.354: met); S (two consecutive lines read as Danish without correction):
met. Declared bias: the held-out portion was transcribed by an agent who already knew the key; C1 passed with a small margin.

**A second, independent confirmation, after the measurement:** image 091 left (found at the end of the volume during the second
session) is a **table of the cipher alphabet in the writer's own hand**, a to ø, one sign per letter in alphabetical order, without
the letters. Every value of the measured key found in the table falls at its place (19 letters: a, b, c, d, e, f, g, h, i, k, l,
m, n, o, p, r, t, u, v), and it adds q, s (a straight dotted stroke, opposed to the curved dotted i), z, æ, ø. A second form of g is written above
the g, probably added by a later user.

## Reading (`reading.md`, `translation.md`, `decryption.txt`)

Daniel Bourdeau's rule: read = certain + probable words; restored and unresolved words are holes. Clear headings, arabic numerals,
apothecary units and seals are not counted; cipher headings ("Ottende Begreb") are counted.

| part | pages | certain / probable / restored / unresolved | words | read |
|---|---|---|---|---|
| held-out portion (030, 031) after the blind sheet K1, result B (**retained**) | 3 | 133 / 36 / 1 / 9 | 179 | **94.41%** |
| same, result A (the hashed integration rule taken literally) | 3 | 133 / 37 / 1 / 8 | 179 | 94.97% |
| first session, low resolution (003 R - 008 L, except 007 R) | 9 | 292 / 93 / 0 / 40 | 425 | 90.6% |
| second session, full resolution (007 R, 008 R - 079 R, 098), after the blind sheet K3, result B (retained) | 136 | 6,441 / 668 / 76 / 266 | 7,451 | 95.4% |
| **whole book, indicative only**, after K3, result B (retained) | 148 | 6,866 / 797 / 77 / 315 | 8,055 | **95.1%** |
| same, result A (rule as written) | 148 | 6,866 / 796 / 77 / 316 | 8,055 | 95.1% |
| whole book before K3 | 148 | 6,863 / 802 / 77 / 313 | 8,055 | 95.2% |

- The figure we declare is the **held-out portion, 94.41%** (result B, retained at Brice Dudout's request; result A 94.97%). Both
  are under 95%, hence "read in part". See `BLIND-REREADING.md`.
- The whole-book figure, **95.1%** (95.13%, result B; A 95.12%; 95.16% before K3), is given **as an indication only**: the second
  session was checked blind on nine targeted signs only (sheet K3: three probable words became certain, two became
  unresolved, three by the rule as written; see `BLIND-REREADING.md`), and on the held-out portion the blind sheet K1 took the share down by 1.7 points (96.1% -> 94.41%). We do
  not claim 95%. The held-out portion was not touched by K3.
- **Nine pages of the first session were read at low resolution (4,115 px) and are still to be re-read at full resolution**: 003 R,
  004 L, 004 R, 005 L, 005 R, 006 L, 006 R, 007 L, 008 L (90.6%; 005 R 69.4% and 005 L 79.2% are the weakest).
- Weakest pages of the second session: **064 L 61.4%** (a list of conjuration words, stained and faded), **010 R 77.2%** (end of a
  fever litany), then 011 R 82.1%, 019 R 82.5%, 064 R 84.4%, 034 L 86.6%, 010 L 87.1%.
- The 136 full-resolution pages were read by 16 sub-agents (one batch each), each writing a fiche per page with a class per line
  and a list of doubtful sign shapes (1,122 in all). A random draw of them (sheet K2) was pre-registered and abandoned before it was shown; the targeted sheet K3 took 9 of them,
  chosen for the words whose class depends on the answer (`BLIND-REREADING.md`).

Content: about a hundred charms and recipes of a Danish cunning man (summary of each in `translation.md`, section 1). Cures
(bleeding, wounds, colic, toothache, fever, chilblains, childbirth, warts, scrofula, rickets, bed-wetting, consumption), protection
of cattle, horses, poultry, geese, butter and milk against witchcraft, pests summoned to the Thing (caterpillars, rats and mice),
dogs and bulls held at bay, guns bound and men made proof against shot and blades, fire conjured (Mary's cloak; the SATOR square),
winning at cards, and a long series against thieves (to make one stand still, bring back what he took, or suffer). The charm types
are the classic ones of Danish tradition (Ohrt's "Danmarks Trylleformler": the Longinus charm, "Gud sætter sin Stav for Flod",
the impossible condition "førend Jomfru Maria føder en Søn"); what is new is their text in this book, and above all the written
directions for use, which only the cipher held.

Numbering: the cipher Begreb numbers run 1 to 23, the 23rd twice (031 R and 036 L, "Treogtyvende"); the 24th is never read; one
Begreb (butter, 020 R) has no number read; no Begreb number appears after 036 L.

## Prior art

Known before this reading: the existence of the book, its author and its "kodeskrift" (lex.dk, article "folkemedicin" by B.
Rørbye; heuschkel.dk, "Cyprianus: De sorte bøger", reproduces an opening without reading it); the KB description "Størstedelen i
lønskrift". Daniel Bourdeau's vetting (11 Nov 2026) found nothing on DECODE ("Cyprianus", "Kloge", "lønskrift": 0 records), in
Tomokiyo or Lasry, and no edition. Our own textual searches (Danish) found no study that publishes the cipher or its key. Ohrt,
"Danmarks Trylleformler" I-II (1917-1921), cannot have used a manuscript that entered the DFS in 1997; his "Lønformler" are secret
formulas, not a cipher. **Not verified on paper:** B. Rørbye, *Kloge folk og skidtfolk. Kvaksalveriets epoke i Danmark*
(1976), which deals with cypriani; no full text or table of contents is online, so whether it cites or reads this book is not
known. The DFS accession record of 1997/020 is not online either. The writer's own table (091 L) shows the key existed on paper,
so an old reading by a relative or the donor cannot be excluded, though none is published to our knowledge.

## Remaining gaps

- nine pages of the first session (003 R, 004 L-R, 005 L-R, 006 L-R, 007 L, 008 L; 425 words, 40 unresolved) - blocker: illegible; read on the 4,115 px images, where the dots of e, b/h and the bars u/n are often lost; a full-resolution re-reading is the next step (the second session reaches 95.4% at full resolution)
- unresolved words of the second session (266 words, 76 restored, after K3), worst on 064 L (26 unresolved: conjuration words, stained and faded ink) and 010 R (13) - blocker: illegible; the doubtful shapes are listed; K3 checked nine of them
- the shapes flagged by the blind sheet K3 (chevron with a foot on 034 R, closed loop on 073 R, 074 L, 075 L, the star-like sign of 064 L, dot confusions; and "fer / før" on 033 L) - blocker: illegible; a declared re-reading on the full-resolution images, its list hashed first; the rule forbids a further sheet on the same 11 signs
- held-out portion: Kirkegaard, Jomfru, Kabbe, karlegravet, søn and four other words of 030-031 - blocker: illegible; the sheet K1 left them unresolved, and its rule forbids a second sheet on the same signs
- circular seals (018 R, 019 R, 104) - blocker: illegible; in the same signs, written round a circle; not read
- a sign-level transcription of the 136 full-resolution pages - blocker: illegible; these pages were read straight into letters with the key (decryption.txt, Part 3, with unresolved words given in sign shapes); no separate token transcription was made
- prior art on paper: Rørbye, *Kloge folk og skidtfolk* (1976), and the DFS accession record of 1997/020 - blocker: needs-physical-access; not online; only a library or the DFS can settle whether an earlier reading exists

## Escalation

- [x] siblings: all 109 images of DFS 1997/020 opened (contact sheet, then 173 half-openings at full resolution); cipher on 003 R - 079 R, 091 L (alphabet table), 098 and 104 (loose leaves); the other leaves are blank or binding
- [x] clear-pages: clear headings used as cribs; no clear copy of the charms in the volume; the table on 091 L is a key, not a decipherment
- [x] known-keys: no key on DECODE or in print (Daniel's vetting); the only key material is the writer's own table (091 L), which confirms ours
- [x] print: lex.dk / Rørbye, heuschkel.dk, KB record, Ohrt (charm types only); Rørbye 1976 not seen (not online)
- [x] key-rebuild: stroke-and-dot signs separated at full resolution; ligatures aa, tt, nn, mm and variants added (key.tsv B, D); table 091 L adds q, s, z, æ, ø
- [x] retry: image 031 right lines 16-26 re-read at full resolution (85.8% -> 96.1% on the held-out portion before the blind sheet, 94.41% after); the whole book re-read at full resolution except the nine first-session pages
