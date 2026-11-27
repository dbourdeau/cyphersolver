# Ḥaram al-sharīf documents, Jerusalem (27 Nov 2026)

Run by a Claude Code session for Daniel Bourdeau. Question: have the Mamluk documents of the Ḥaram al-sharīf
(Islamic Museum, Jerusalem; about 900 legal and administrative papers, mostly 1370s-1390s) been swept for ciphers, and
do they hold any? They had not been swept: no research folder, `COVERAGE.md` row, lead or shelfmark mentioned them.

**State: swept, closed negative. `candidates.json` holds 0 rows, nothing to merge, vet or promote.**

## Result

The corpus holds no enciphered text, no cryptic script and no secret writing. Both printed catalogues were read in full
text and searched; the one study that discusses the corpus's "obscure" numerals rejects the code reading.

| Source | Covers | How read | Cipher-type content |
|---|---|---|---|
| Little, *A Catalogue of the Islamic Documents from al-Ḥaram aš-Šarīf in Jerusalem* (Beiruter Texte und Studien 29, 1984), 528 PDF pages with OCR layer | the "old" corpus, nos. 1-~900 | Halle MENAdoc `opendata.uni-halle.de/handle/1981185920/114326` (DOI 10.25673/112368), searched in text | none. Three uses of "cipher" (book pp. 27 and 31, PDF pp. 43 and 47, and no. 875 on PDF p. 414): all mean a signature-monogram, "ʿalāma in cipher" / "signature in cipher" / "a cipher at top" |
| Aljoumani, Bhalloo, Hirschler, *Catalogue of the New Corpus of Documents from the Ḥaram al-sharīf* (De Gruyter, 2024, open access, DOI 10.1515/9783111330242) | about 100 newly found documents: ch. II Arabic (about 55), III Ottoman, IV Persian, appendices 2, 3a, 3b, index | chapter PDFs 002, 003, 004, 005, 008, 009, 010, 012 searched in text | none. Every "cipher" hit is "deciphering"; "undeciphered" marks only on Persian witness clauses and one accounts item |
| Aljoumani and Hirschler, *Owning Books and Preserving Documents in Medieval Jerusalem* (EUP, 2023, open access), 466 pp | Burhān al-Dīn al-Nāṣirī's library (d. 1387) and the estate documents | PDF by curl from `edinburghuniversitypress.com/pub/media/ebooks/9781474492089.pdf`, searched in text | none. Argues in a footnote and a section on siyāqa numerals (PDF pp. 217-225) that these numerals were not a secret code |

What the searches did show, and why none of it is a lead:

- **ʿAlāma "in cipher" / "undeciphered ʿalāma"** (Little, PDF pp. 43-60 and others): the chancery official's authorising motto or monogram written in a stylised hand, sometimes unread by Little. A signature flourish, not text in a cipher.
- **Siyāqa and Greek/Coptic/Rūmī/ḥurūf al-zimām numerals**: Haarmann called them "camouflage" and earlier scholars "obscure numerals needing deciphering"; Aljoumani and Hirschler (PDF pp. 217-225) show they are an ordinary documentary numeral system that stayed stable for centuries. Their 2024 catalogue entry (15) records accounts in these numerals. Numeral reading, not cryptanalysis.
- **Little no. 875** (Persian, 9 Jumādā II 754/12 July 1353, 16 x 54.4 cm): "a cipher at top, nine lines of Persian with two lines of Uigur between lines 7 and 8", "content undetermined". Mongolian in Uighur script plus a monogram. There are 7 Uigur mentions and 5 "content undetermined" entries in Little; the corpus has no images online, so no ciphertext could be seen (vetting bar item 1).
- **New-corpus Persian marks** (ch. IV): "two undeciphered marks above the witness clause" and one "undeciphered witness clause or scribal signature". Scribal marks.
- **Intro, "undeciphered inventory of expenditure relating to a Mongol (?) woman" ((89)/#963)**: an accounts document in a hand the editors could not read. No key, no cipher sign; not a lead.

## Checked and found unsupported: the link to LJS 51

`targets/qaysarani1350` (Penn LJS 51) cites a **Burhān al-Dīn al-Qudsī** among its authorities on alphabets. The Ḥaram
corpus is built around **Burhān al-Dīn Ibrāhīm al-Nāṣirī** (reciter and faqīh at Turbat Ṭāz, d. 1387), a different
nisba. A text search of Aljoumani and Hirschler finds "Qudsī" on 5 PDF pages; the three read in context (pp. 177, 182, 288) are
the grammarian Aḥmad al-Qudsī Ibn al-Raṣṣāṣ (d. 790/1388-9); pp. 416 and 433 were not read. The book has no hit for Ibn
al-Durayhim, Ibn Dunaynir, Ibn ʿAdlān, al-Jindī, *taʿmiya* or *tarjama*, so Burhān al-Dīn's library list shows no
cryptology title among the names searched. Verdict: the same-name guess does not hold.

## Not read, with reasons

- De Gruyter ch. 001 (preface, 43 MB with images), 006 and 007 (editions of ten documents, 72 MB of facsimiles), 011 (bibliography), 013-015 (indexes): not downloaded or not searched. They are an editorial memoir, edited legal documents, and indexes of names, places and terms; a cipher text would have been catalogued in ch. II-IV.
- The Hamburg project RFE17 database (material traces of archiving) is a research tool; no public image database of the Ḥaram documents was found. Images are in the two printed volumes (Little: 17 plates) and the Islamic Museum.
- The Islamic Museum itself, the Aqsa Library, and the Khalidi Library manuscripts (HMML holds 1,680 Khalidi surrogates; the 24 Nov vHMML pass found no cipher hit there) were not searched item by item.

## Routes (for the next sweep)

| Source | Route | Result |
|---|---|---|
| De Gruyter open-access PDFs | `degruyterbrill.com/document/doi/10.1515/9783111330242-<nnn>/pdf`: `fetch()` inside a Chrome tab works, but a loop of 12 fetches triggered a "confirm you are human" page (Daniel cleared it). Navigating a tab straight to the `/pdf` URL saves the file to Downloads; scripted `<a download>` clicks are blocked after the first | works, one navigation per chapter |
| OAPEN (`library.oapen.org`) | Anubis proof-of-work; curl gets 403, and in Chrome Anubis returned "administrator has misconfigured Anubis" | not reached; De Gruyter has the same text |
| Halle MENAdoc (Little 1984) | Anubis in curl; passes in Chrome; "View/Open" click saves the 287 MB PDF, which has an OCR layer | works |
| Edinburgh University Press | `edinburghuniversitypress.com/pub/media/ebooks/9781474492089.pdf` by plain curl (31 MB) | works |
| A localhost POST from the page to a local receiver | hangs (Chrome's local-network request block) | does not work |

Working files (`src/`: PDFs and text extracts) are git-ignored; nothing from them is quoted beyond the short phrases above.
