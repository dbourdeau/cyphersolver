# Muslim Heritage deck "Arabic Origins of Cryptology" (27 Nov 2026)

Source: `muslimheritage.com/wp-content/uploads/2018/05/cryptology01.pdf`, Mohammed I. Al-Suwaiyel (KACST), Oxford,
26 April 2018, 27 slides, read in full (plain curl works; the PDF is kept in the git-ignored `src/`). Asked: does it
give any source of leads?

**State: 0 candidate rows, nothing to merge or promote.** The deck holds no ciphertext. It is a survey of the
treatise literature. Its KACST links are down; the Arabic edition of the Mrayati series was found on archive.org and
every page of both volumes was reviewed (sections below): no unsolved cryptogram. The deck's own claims are not checked here.

## What the deck points to

| Pointer in the deck | What it is | Prior coverage in this repo | Opened now |
|---|---|---|---|
| KACST/KFCRIS *Arabic Origins of Cryptology*, vols 1-6 (Mrayati, Meer Alam, at-Tayyan; al-Kindi, Ibn 'Adlan, Ibn al-Durayhim, Ibn Dunaynir, al-Gurhumi, Ibn Tabataba, Ibn Wahb; vols 7-9, Ibn Wahshiyya, al-'Iraqi, Thawban al-Misri, al-Jildaki, not yet published per the deck) | 15 treatises edited with English translation; the deck says they contain worked cryptograms | `sweep_2026-11-15_arabic/part_D.md` lists "the Mrayati series itself (are all worked cryptograms solved?)" as *literature not opened*; `sweep_2026-11-24_arabic_treatises` found the Istanbul and Bursa witnesses but not the edition | **No.** `publications.kacst.edu.sa/SystemFiles/Books_Pdf/300.pdf` (Arabic vols) and `302.pdf` (English vols 1-6): no connection from curl, and Chrome shows an error page (`http` and `https`). Wayback 404 and 429. Only unofficial uploads (Scribd, Pdfcoffee, the latter 403 to curl) turned up; not used |
| Ibn Dunaynir's "example enciphered by numbers for me by some Maghrebi in Dar as-Salaam" | A ciphertext quoted inside a treatise | not listed | Not read (needs vol. 4). The treatise gives its solution, so this is a key lookup unless the editors left it open |
| al-Kadi, *Cryptologia* 16/2 (1992) 97-126 | Survey | listed in `sweep_2026-11-25_geniza_literature` | The deck's URL (`membres-ljk.imag.fr/.../AlKadi_cryptology.pdf`) now redirects to the host's home page; not read |
| Azizi and Azizi, *Cryptologia* 35 (2011) 41-51 and 37 (2013) 328-337 (Morocco; "numerical signature") | Moroccan/Andalusian cryptography | Moroccan Makhzen cipher letters (Tazi; Azizi) already on the "still unswept" list in `COVERAGE.md` | Not read |
| Alukah article on the manuscripts' discovery (Arabic) | Journalistic account | none | 403 to curl |

Works the deck says exist but are lost (al-Farahidi, Jabir b. Hayyan, Abu al-Qasim al-'Iraqi, *Hall al-rumuz wa fath
aqfal al-kunuz*) are not leads: no manuscript is known.

## Next step

The one concrete lead source is the Mrayati series. Open vols 2-4 (Ibn 'Adlan, Ibn al-Durayhim, Ibn Dunaynir) from a
network that reaches KACST, or by an interlibrary copy, and list each cryptogram the editors left unsolved or give
only as a ciphertext. Until then no row can meet the vetting bar (ciphertext seen).

## Arabic edition read (27 Nov 2026, second pass)

Copies: archive.org `BBib-Alex-03259` (vol. 1, 452 pp) and `BBib-Alex-03260` (vol. 2, 484 pp), uploaded by a user, scans of
Mrayati, Meer Alam, at-Tayyan, *'Ilm al-ta'miya wa-istikhraj al-mu'amma 'ind al-'arab* (Damascus Academy, 1987; 1997 on
the title page of the record). Vol. 1: al-Kindi, Ibn 'Adlan, Ibn al-Durayhim. Vol. 2: Ibn Dunaynir, Ibn Tabataba, Ibn
Wahb, al-Gurhumi, the two anonymous essays, with an English summary at the end. Files are in the git-ignored `src/`.

**Traps:** the archive.org `_text.pdf` stores every Arabic line reversed (reverse each line to search it); the OCR is too
rough for phrase search ("not solved" wordings gave 0 hits), so triage was by OCR noise (Latin-letter lines flag symbol
cryptograms) and by looking at the page images.

**The symbol cryptograms seen, with their solutions:**

| Where (vol. 1) | Item | Solution |
|---|---|---|
| pdf p. 361 (book p. 353) | Ibn al-Durayhim, first worked example, 7 lines of invented signs, repeated shapes counted and numbered | worked through pdf pp. 361-367 |
| pdf p. 368 (book p. 360) | second example, 8 lines of signs. The treatise's own facsimile page is pdf p. 323 (book p. 315, "a page of Ibn al-Durayhim's treatise containing the second text's encipherment") and the *Subh al-a'sha* version of the same text is pdf p. 324 (book p. 316) | solved pdf pp. 369-373: the most frequent sign is alif, then lam, giving *lillah*, and the text resolves into four lines of verse, "al-hamdu li-llahi 'ala ma alhama ..." |

So the vol. 1 symbol cryptograms are two, both Ibn al-Durayhim's, both solved by the author with the editors' translation.

Other pages looked at: al-Kindi's examples (pdf 123-128) are substitution tables and short Latin-letter transcriptions;
Ibn Dunaynir (vol. 2, pdf pp. 137-206, 364) gives theory and examples drawn from verses; pdf p. 49 of vol. 2 (book p. 45) is a
facsimile of al-Muqri''s multi-science book (columns of ordinary Arabic, not a cipher).

## Every page reviewed (27 Nov 2026, third pass)

All 936 pages (vol. 1 pdf 1-452, vol. 2 pdf 1-484) were read as 6-page sheets by six reviewers, two at a time, in
ranges of about 150 pages, with sign-string pages re-rendered at 130 dpi; I then rechecked every item a reviewer
flagged as unclear or unsolved. Per-range notes: `findings/*.md`. The reviewers read the pictures and the structure; they
did not transcribe Arabic handwriting, so "solved" means the plaintext is printed beside or after the ciphertext.

**Result: no cryptogram without a solution in either volume, and no editor's note saying one is unsolved or corrupt.**

| Vol. / pdf pp. | Ciphertexts (all solved) |
|---|---|
| 1 / 361-367 (book 353-359) | Ibn al-Durayhim, example 1, 7 lines of signs; plaintext two verses ("sadda 'anni fa-la tulum ya 'adhuli ...") |
| 1 / 368-373, facsimile 323-324 | Ibn al-Durayhim, example 2, 8 lines of signs; plaintext four verses ("al-hamdu li-llahi 'ala ma alhama ...") |
| 1 / 311-315 (book 303-307) | Ibn 'Adlan, bird-name cipher (hamam, hudhud, saqr ... one name per letter-shape), "for a Maghribi in Baghdad (Dar as-Salam), 626 AH"; plaintext verse "tamannaytu min hubbi Buthayna ..."; analysis to the end of p. 315 |
| 1 / 172-173, 191-193 | transposition, jummal-number and 6x6 grid illustrations; plaintext on the page |
| 1 / 47-51, 74-84, 124-132 (editor's illustrations); 2 / 47-50, 74-81, 107 | short examples ("Muhammad Ali", "hasbuna Allah", "Allah wali al-tawfiq"); plaintext on the page |
| 2 / 77-81 (book 73-77) | Maqalatan, "example of solving an enciphered text", 24 lines of signs; worked solution pdf 79-80, plaintext letter on pdf 81 ("katabtu ya sayyidi atala Allah baqa'ak min madinat as-salam ...") |
| 2 / 160-167, 175, 177, 184-193, 261-263 | Ibn Dunaynir: a 187-symbol message with its encipherment, box-sign compound ciphers, concealment of a short message above a cover story (p. 175, plaintext in the index), jummal and day-hour examples; all with plaintext |
| 2 / 224-226, 286-287 | Ibn Dunaynir, two verse cryptograms in three-letter code words ("zafar", "safar", "sa'd" ...); both plain verses in footnotes |
| 2 / 306, 321 | Ibn Tabataba, bird-name rendering of "qifa nabki ..." (44 letters, 44 names) |
| 2 / 327-328, 351-353 | Adab al-shu'ara': a Hamza al-Isfahani verse as single letters; 16 rows of spaced letters with a man's name under each, spelling al-Mutanabbi's "al-khaylu wa-l-laylu wa-l-bayda'u ta'rifuni ..." and 'Antara's verse, each quoted in a footnote |
| 2 / 375-377, 390-392 | al-Gurhumi, eleven-name and 24-word texts; solution tables on the page, verses "nazalat salma ...", "shaghalat alfi ...", "ra'at sa'di ..." |

Alphabets and keys with no ciphertext: 28-sign alphabet of Ibn 'Adlan (vol. 1, pdf 279); the Nasihin translator's key
(vol. 1, pdf 348); Ibn al-Durayhim's tables and cipher disk (vol. 1, pdf 174-194); a 28-form alphabet in Maqalatan II
(vol. 2, pdf 86); bead-colour, chess-board and hand-reckoning keys (vol. 2, pdf 181-190, 261-263).

**Resolved queries from the first two passes.** (1) The "Maghrebi in Dar as-Salam" example the deck attributes to Ibn
Dunaynir is the bird-name cryptogram above (vol. 1, pdf 311, in Ibn 'Adlan's closing chapter), which is solved. The deck's
attribution to Ibn Dunaynir was not checked and may be wrong. (2) Vol. 2, pdf p. 49 (book 45) looked like a sign cipher
to one reviewer; rotated upright it is poorly scanned ordinary Arabic, a facsimile of al-Muqri''s five-sciences-in-one-page
book that the editors describe. (3) "yumn yumn tumn tumn" (vol. 2, pdf 227) is a caliph's note analysed as a prosodic puzzle.
(4) The English summary at the end of vol. 2 says only that a cryptogram too short or with too few repeated symbols cannot
be solved.

**Not checked:** al-Kindi's final facsimile page (vol. 1, pdf 218, book 210) has boxed letter tables and rows of letters,
taken as the treatise's own closing text since the edition prints it; I did not read it letter by letter. The English
series and vol. 3 (old alphabets, *al-aqlam*; "will follow" per both volumes) are not covered. So the Arabic edition gives
no lead; the surviving worked examples in these treatises are all solved by their authors or the editors.
