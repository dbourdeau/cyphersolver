# Charles VI → Count Leopold Viktorin Windischgrätz, 3 Feb 1720, in the Chancellery key R5017 — **read**

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). This entry keeps No. 1 (3 Feb 1720,
R5019/R5020), in the Court Chancellery nomenclator R5017. The three later letters (Nos. 2, 3, 6; R5021–R5024), in the
Emperor's private key R5018, are now [`targets/windischgraetz1720b/`](../windischgraetz1720b/NOTES.md) (a different
cipher, with its own page); `key5018.md` and `dec_R5018_letters.md` moved there. The sections below keep their
history; figures for this entry: 221 of 223 cipher tokens of No. 1 (446 and 638 uncertain).

Five autograph letters from the Emperor Charles VI to his envoy at The Hague (from 1722 his plenipotentiary at
the Congress of Cambrai), partly in cipher. DECODE lists them as Non-decrypted: R5019 and R5020 (3 Feb 1720, autograph and
copy), R5021 and R5022 (13 Apr 1720), R5023 (24 Jul 1720, copy only) and R5024 (11 Apr 1722, copy only). The DECODE
record also points to both keys, R5017 and R5018. Holder: Státní oblastní archiv v Plzni, pracoviště Klášter u
Nepomuka, Rodinný archiv Windischgrätzů. Autographs are inv. 694, karton 5. The fair copies are in inv. 5, book 5
(a register of the Emperor's letters, one "No." per letter, pp. 401–417). The keys are in the key collection,
karton 164, inv. 1403, sign. 103.

**Result: every cipher passage in the four letters on DECODE reads directly from the two keys.** Nothing had to be
reconstructed. Readings: `dec_R5017_letter.md` (No. 1) and, since 14 Oct 2026 in `../windischgraetz1720b/`, `dec_R5018_letters.md` (Nos. 2, 3, 6).

## Prior work

Jakub Mírka, "Raně novověká šifrovaná korespondence ve fondech šlechtických rodinných archivů SOA v Plzni",
*Západočeské archivy* 2012, pp. 44–72, reprinted in *Crypto-World* 3–4/2013. He describes the 3 Feb 1720 letter:
the Emperor tells Windischgrätz that a new key reserved for their private correspondence will follow, while the
old key stays in use with the Court Chancellery. He adds that the later letters are indeed in the new key and that both keys survive
(n. 40–41). His figures 12–13 show the two-part Reichshofrat nomenclator of about 1720. He does not print any
decryption, and none was found elsewhere (web search, 19 Sept 2026).

## Keys

- **R5017** is the *Ziffer Schlüssel mit der geheimen Hof-Canzley*, a two-part nomenclator (the decipher half). The first leaf gives single
  letters with homophones, then nulls and punctuation. Numbers 1–400 are a syllabary: letters, bigrams and trigrams
  such as schli, stre, spra, plus nulls (*errans*), comma, punctum, duo puncta, punctum cum comate and
  *annulla praecedentia/sequentia*. Numbers 401–977 are words and names in alphabetical order, from *Aachen* to *zu*
  (978–999 are blank). Transcribed in `key5017_syllabary.tsv` (1–400, read here) and `key5017_nomenclator.tsv`
  (401–999, 41 low-confidence cells flagged). This is the old Chancellery key, used in No. 1 before the new key arrived.
- **R5018** is the new private key, on one sheet. Each of 24 letters has a number from 10 to 38 and a graphic sign;
  the vowels have a second number. There are about 300 codes (39–210 and two-letter groups such as ab, fb, zi) and
  the nulls 3 4 5 6 7 9. Transcribed in `key5018.md` (now in `../windischgraetz1720b/`), with glyph crops in `key5018_glyphs/` (git-ignored, here). The
  docket on the back reads "Ziffern mit J[hr]: K[ayserlichen] M[ajestät] …".

Corrections found by using the keys:
- **R5017.** "31" (key: el) stands for *zu* (syllabary 3) all three times it occurs. Cell 268 "em" must be "ein/ei".
- **R5018.** The copyist's signs drift. The q-with-crossbars sign serves D and once N, and p with one crossbar serves both Z and
  G. Each is settled by the surrounding numbered letters.

## Letters and contents

| No. | date | DECODE | key | cipher passages | substance of the cipher |
|---|---|---|---|---|---|
| 1 | Vienna, 3 Feb 1720 | R5019 (autograph), R5020 (copy pp. 401–404) | R5017 | 26 | Report everything to Pentenriedter. Confide in Cadogan and show France and the Regent no suspicion. Now that **Alberoni has been expelled from Spain**, France may seek a **separate peace with "the Duc d'Anjou" (Philip V) through Morville**. Cultivate the Portuguese envoy Tarouca and bring **his king into the Alliance**. The treaty must not be altered. Giving **Sardinia to the Duke of Lorraine** is "sehr ideal". The Emperor insists on **the equivalent for Montferrat** |
| 2 | Vienna, 13 Apr 1720 | R5021 (autograph), R5022 (copy pp. 404–407) | R5018 | 2 | Whether [Spain] **and Orleans** will come to terms with one another again. How one could **free oneself entirely from the burden of the Barrier** |
| 3 | Vienna, 24 Jul 1720 | R5023 (copy pp. 407–409) | R5018 | 3 | **Beretti Landi** (the Spanish envoy at The Hague) proposed, in the name of his court, **a marriage between one or other of the Emperor's children and Anjou's sons**. Charles will stay on good terms with that court, but **"both are so small"** that nothing is to be made known yet |
| 6 | Vienna, 11 Apr 1722 | R5024 (copy pp. 414–416) | R5018 | 4 | Windischgrätz's talks **with Beretti about a marriage between Spain and the Emperor's house**. Beretti is **"embittered against me and Austria"**, but it is not bad to make use of him and to show him every consideration *in utili et honorifico* |

No. 3 is an early trace of the Austro-Spanish marriage scheme that came back in the 1725 Treaty of Vienna. The
Emperor's eldest child, Maria Theresa, was then three. No. 6 opens in clear text with the Emperor's grief at the death of his
Oberststallmeister and favourite, presumably Count Michael Johann Althann (d. March 1722).

Not on DECODE: Nos. 4 and 5 (book pp. 409–414) and No. 7 (p. 417 on). R5023's first image repeats pp. 406–407.
The brothers' own key of 1721 (R5029, L. V. to E. F. Windischgrätz, 8 pp.) is a separate cipher and is not
covered here.

## Files

- `ct_1720-02-03.txt`: No. 1 cipher numbers by passage, with the clear text before each. `dec.py` decodes them with the two TSVs.
- `clear_1720-02-03.txt`: draft transcription of No. 1's clear text (Charles's spelling; uncertain words marked).
- `tile.py`: crop helper. `decode/`: DECODE images and record pages (git-ignored; fetched with the cookie in
  `targets/bordeaux/decode/cookie.txt`).

Open: the clear text of Nos. 2, 3 and 6 is only summarised around the cipher passages. The 41 low-confidence
nomenclator cells do not touch any passage except 446 (N) and 638 (X), which stay uncertain.
