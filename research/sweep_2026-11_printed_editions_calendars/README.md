# Printed editions, calendars and Arcinsys "Chiff*" pass, 19-27 Nov 2026 (Brice Dudout, via Claude)

`candidates.json`: **20 rows** in the format of `research/archive_sweep_2026-10/BRIEF.md`, validated (fields, region,
period, cls, needs_archive_scan). None of the originals was viewed (`seen: catalogue`). TNA shelfmarks are inferred
from the calendars' old references or from the month, and each row says when this is the case.

## Method

Each source was read in full text: archive.org OCR, British History Online (read in a browser, one page every 6 s, after a
Cloudflare check passed by hand), or the archive's own catalogue. Every hit was checked against cyphersolver `origin/main`
(catalogue.json, research/leads.json, archive_requests.json, research/, targets/), against open and merged pull requests
(`gh pr list --state all --search`), and against our own folders.

| Source | What was searched | Rows |
|---|---|---|
| Tamizey de Larroque, *Lettres de Peiresc* t. I, VI | "chiffre", "chiffré", "déchiffr", "clef", "interlinéaire" | 0 (crib lead below) |
| Berger de Xivrey, *Lettres missives de Henri IV* t. V-IX, suppl. | the 15 BnF items of fr. 3485/3486 | 0 (update below) |
| Avenel, *Lettres … du cardinal de Richelieu* t. I, III-VIII | cipher terms and runs of ≥ 4 numbers | 0 (read in PR #813) |
| *Lettres de Catherine de Médicis* t. I-X | "chiffr*" and number runs | 0 (crib leads below) |
| Kervyn de Lettenhove, *Relations politiques* vol. 1-11 | cipher terms in five languages; number runs | 1 (AGS Estado 812) |
| Arcinsys Hessen, "Chiff*", 1000-1700 | 116 results, 39 not in `arcinsys_detail.json` | 0 (key and crib leads below) |
| Birkner, "Eine Plön-Wolfenbütteler Geheimschrift", *ZGSHG* 136 (2011) | the whole article | 1 (LASH Abt. 20 Nr. 40) |
| *CSP Foreign, Elizabeth* 1575-77 (Crosby, archive.org) | "undeciphered", "in cipher", index | 5 |
| *CSP Foreign, Elizabeth* vols 1-10, 1558-74 (archive.org; vols 2, 4, 6, 8 not there) | same | 3 |
| *CSP Foreign, Elizabeth* on British History Online, vols 12-23 | BHO search "undeciphered" (pages 1-19), vol. indexes, monthly pages | 10 |
| Narváez 2015 and 2025 (Mexico), and the 2021 review of Narváez 2019 | printed figures and tables | 0 (update and key leads below) |

The Arcinsys wildcard search was suggested by an archivist in Darmstadt, and the Plön lead came from a volunteer
historian; both are thanked (names to be added with their agreement).

## Rows

- **LASH Abt. 20 Nr. 40 a-d** (Rudolf August of Wolfenbüttel → Johann Adolf of Plön, 1676-1703, cls B): Birkner prints the
  sign key and reads about ten extracts of a correspondence of 500-800 letters; the rest is unread. Catalogue 2020
  (NLA Wolfenbüttel 2 Alt Nr. 3565, Rudolf August to Heimburg) may use the same cipher; catalogue 604 names a key in the
  same fonds (Abt. 20 Nr. 37).
- **Edward Stafford, Paris, 1585-88** (SP 78/13, 16, 17, 18; four rows, cls C). The best is Stafford → Burghley, 6 Nov 1586,
  12 pp., "cipher words mostly undeciphered". CSP vol. 18 no. 417 (France XI. 25a, 13 Feb 1584) calendars a contemporary
  decipher sheet of Stafford's ordinary cipher, without printing the table.
- **Horatio Palavicino, Frankfort, Apr 1586-Apr 1587** (SP 81, Germany, States IV-V; two rows, cls C): Italian letters with
  the italic words in cipher, sent in duplicate by two routes, so the ciphertext repeats.
- **Antonio de Guaras → Don John of Austria, 15 Feb 1577** (SP 70/143, cal. no. 1264, cls B): intercepted; Marnix's 1577
  decipherment is printed with gaps by Kervyn (IX no. 3359; X no. 3640); no key in print. Not catalogue 303/1001 (Guaras 1574,
  PRs #743 and #892).
- **Francisco Giraldi (Portuguese ambassador) → the King of Portugal, London, 4 Jun 1574** (SP 70, cal. no. 1441, cls C):
  "very long letter in cipher", 29 pp.
- **Amias Paulet, Blois, 28 Apr 1577** (SP 70/144, nos 1408-1410, cls A): "partly in cipher, undeciphered", a copy in a second
  cipher, and a partial decipherment.
- **Thomas Morgan → Walsingham, Brussels, Feb 1589** (SP 77, cls C): four passages "in cipher, undeciphered".
- **Henry Cobham → Walsingham, Paris, 27 Jul and 12/22 Oct 1583** (SP 78/10, two rows, cls C): "in Cobham's cipher,
  undeciphered". Our key `cobham1588` (PR #343) may be tested on them.
- Smaller rows: Valentine Dale, Paris, Mar 1575 (SP 70/133, "partly deciphered"); John Smith, 16 Dec 1576 (SP 70/141);
  "Affairs in France", 5 Jan 1577 (SP 70/142); Middelburg, 14 May 1585 (SP 83); letters taken at the siege of Edinburgh
  Castle, Jan-Feb 1573 (SP 52, originals to locate; related to, but not the same as, the lead on Killegrew to Burghley,
  17 Mar 1572); "Virtus pro divitiis" → the Lord Admiral, 18 Nov 1558 (SP 70, a short postscript); AGS Estado leg. 812,
  Granvelle → Quadra, 17 Nov 1559 (Kervyn replaces the cipher with dots; not in CSP Spanish vol. 1).

## Left out under the brief: crib and key leads

The brief leaves out an item that carries an attached decipherment or whose clear is printed. These items fall under
that rule; their value is a key rebuilt from cipher plus clear:

- **BnF NAF 5170** (Peiresc → Valavez, 1625-26): interlinear decipherment, clear printed by Tamizey (t. VI), no key in print.
- **BnF fr. 6626 f. 128** (Catherine de Médicis, 20 Nov 1562) and **fr. 6605 ff. 96 ff.** (13 Jun 1562): clear printed by
  La Ferrière (t. X and t. I).
- **AGS Estado 821-824** (Espès ↔ Alba, 1568-71) and **825-829** (Guaras → Alba, Requesens, 1573-75): Kervyn prints them
  deciphered; for 1573-75 they are a check on ajbeling's Guaras key (PRs #743, #892), not a missing key.
- **Guaras 1577**: CSP Foreign 1577-78 no. 768 (Wilson, Antwerp, 5 Apr 1578, SP 83/6 f. 5) sends "the cipher of Guaras's
  letters" (letters or key, not clear); the interrogatory of Guaras (Cal. Cecil Papers II p. 228, Dec 1578) quotes the code
  numbers 82, 29 and 38.
- **CSP Foreign 1558-74**: Killegrew → Cecil, Heidelberg 16 Apr and Cologne 23 Apr 1569 (sense printed in quotes; already in
  the leads); CSP 1558-59 nos 362/363 (one instruction, one copy deciphered and one not).
- **HStAM 4 h 1732** (1644, "Chiffreschreiben mit Übersetzung") and **4 h 537** (The Hague 1623, "aufgelöste Chiffreschrift").
- **LASH Abt. 20 Nr. 472, 473, 535**: the number nomenclator of the imperial embassy to Constantinople, 1699-1700, printed in
  full by Birkner with a short unsolved example.

## Key leads (bare keys)

- Arcinsys: HStAM 3 Nr. 1796 (Philip of Hesse ↔ Zwingli, 1529-31: a key of about 30 signs, and a letter in clear with the
  names replaced by signs); HStAD D 4 240/3 (Louis VI in Sweden, 1655); HStAD D 4 309/5 (Riedesel, Sweden 1672-73);
  HStAM 3 Nr. 926 (1546-47), 3 Nr. 294 (1532); HStAM 4 d 1235, 1218, 1219.
- Mexico (Narváez 2025): AHGE-SRE legajo 14-2-64, "Claves usadas durante el periodo revolucionario de México" (1915, about
  120 keys); magonista keys, 1908 (AHDSREM L-E-954 II ff. 267-270 and 316; exp. 11-4-198 f. 11); "The Nameless" to Carranza,
  CEHM XXI.139.16091.1-2 (two keys, ciphertext not located).

## Updates to existing leads (not new rows)

- **BnF fr. 3485/3486** (Henri IV → Philippe de Béthune, 1602-05; issue #206): none of the 15 letters is in Berger de Xivrey.
  For 10 of them the same volume holds a contemporary "Déchiffrement de la lettre chiffrée …": fr. 3485 nos 5, 7, 19, 21,
  32, 36, 39; fr. 3486 nos 6, 27, 46.
- **Catalogue 1445**, CEHM-Carso DCXXI.3.244.1 and 3.250.2 (Argumedo → Félix Díaz, Oct 1921): Narváez 2015 (*Documenta &
  Instrumenta* 13, p. 122) prints the full number-pair table but reads only part of the runs; folio 2 of 3.250.2 is
  cipher-only in print.
- **Harborne → Walsingham, Pera 1583-85** (Turkey I): already lead 2254, so no row.

## Dead ends

- Fourquevaux: papers at the château, already published (Brunon and Barruol 1953; Douais).
- *Lettres de Catherine de Médicis* and Kervyn never print the cipher itself.
- BnF fr. 6618: a clear draft whose words to be ciphered are underlined. BnF fr. 16113 f. 61: wrong OCR shelfmark.
- Basel UB AN V 9 (catalogue 957): the alphabet is proper to the volume; no other manuscript with the same signs found.

## Not reached

- *CSP Foreign, Elizabeth* vols 2, 4, 6, 8 (1559-68), the vol. 12 index entries under "Ciphers", and four BHO pages of
  vols 18-19 that could not be read.
- Narváez, *Criptografía diplomática, política y militar en México 1813-1926* (SRE 2019): sold, no free copy.
- Avenel t. II; Halphen 1889; Gallica (Cloudflare), HathiTrust (403), Google Books (429).
